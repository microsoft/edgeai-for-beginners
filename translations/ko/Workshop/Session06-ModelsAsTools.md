<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T20:59:16+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "ko"
}
-->
# 세션 6: Foundry Local – 도구로서의 모델

## 개요

모델을 로컬 AI 운영 계층 내에서 조합 가능한 도구로 취급합니다. 이 세션에서는 여러 특화된 SLM/LLM 호출을 연결하고, 작업을 선택적으로 라우팅하며, 애플리케이션에 통합된 SDK 표면을 노출하는 방법을 보여줍니다. 경량 모델 라우터와 작업 계획자를 구축하고 이를 앱 스크립트에 통합하며, 프로덕션 워크로드를 위한 Azure AI Foundry로의 확장 경로를 개요화합니다.

## 학습 목표

- **개념화**: 모델을 선언된 기능을 가진 원자적 도구로 이해하기
- **라우팅**: 의도/휴리스틱 점수에 기반하여 요청 라우팅
- **연결**: 다단계 작업에서 출력 연결 (분해 → 해결 → 개선)
- **통합**: 다운스트림 애플리케이션을 위한 통합 클라이언트 API
- **확장**: 클라우드로 설계 확장 (OpenAI 호환 계약 유지)

## 사전 요구사항

- 세션 1–5 완료
- 여러 로컬 모델 캐시됨 (예: `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### 크로스 플랫폼 환경 코드 스니펫

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS에서 원격/VM 서비스 액세스:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## 데모 흐름 (30분)

### 1. 도구 기능 선언 (5분)

`samples/06-tools/models_catalog.py` 생성:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. 의도 감지 및 라우팅 (8분)

`samples/06-tools/router.py` 생성:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. 다단계 작업 연결 (7분)

`samples/06-tools/pipeline.py` 생성:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. 시작 프로젝트: `06-models-as-tools` 조정 (5분)

개선 사항:
- 스트리밍 토큰 지원 추가 (점진적 UI 업데이트)
- 신뢰도 점수 추가: 어휘적 중복 또는 프롬프트 기준
- 추적 JSON 내보내기 (의도 → 모델 → 지연 시간 → 토큰 사용량)
- 반복된 하위 단계에 대한 캐시 재사용 구현

### 5. Azure로의 확장 경로 (5분)

| 계층 | 로컬 (Foundry) | 클라우드 (Azure AI Foundry) | 전환 전략 |
|------|----------------|-----------------------------|-----------|
| 라우팅 | 휴리스틱 Python | 내구성 있는 마이크로서비스 | API 컨테이너화 및 배포 |
| 모델 | SLMs 캐시됨 | 관리형 배포 | 로컬 이름을 배포 ID로 매핑 |
| 관측성 | CLI 통계/수동 | 중앙 로깅 및 메트릭 | 구조화된 추적 이벤트 추가 |
| 보안 | 로컬 호스트 전용 | Azure 인증/네트워킹 | 비밀을 위한 키 보관소 도입 |
| 비용 | 디바이스 리소스 | 소비 기반 청구 | 예산 가드레일 추가 |

## 검증 체크리스트

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

의도 기반 모델 선택 및 최종 개선된 출력 기대.

## 문제 해결

| 문제 | 원인 | 해결책 |
|------|------|--------|
| 모든 작업이 동일한 모델로 라우팅됨 | 약한 규칙 | INTENT_RULES 정규 표현식 세트 강화 |
| 파이프라인이 중간 단계에서 실패 | 로드된 모델 누락 | `foundry model run <model>` 실행 |
| 출력 일관성이 낮음 | 개선 단계 없음 | 요약/검증 패스 추가 |

## 참고 자료

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry 문서: https://learn.microsoft.com/azure/ai-foundry
- 프롬프트 품질 패턴: 세션 2 참조

---

**세션 소요 시간**: 30분  
**난이도**: 전문가

## 샘플 시나리오 및 워크숍 매핑

| 워크숍 스크립트 / 노트북 | 시나리오 | 목표 | 데이터셋 / 카탈로그 소스 |
|--------------------------|----------|------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | 혼합된 의도 프롬프트를 처리하는 개발자 도우미 (리팩터링, 요약, 분류) | 휴리스틱 의도 → 모델 별칭 라우팅 및 토큰 사용 | 인라인 `CATALOG` + 정규 표현식 `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | 복잡한 코딩 지원 작업을 위한 다단계 계획 및 개선 | 분해 → 특화된 실행 → 요약 개선 단계 | 동일한 `CATALOG`; 계획 출력에서 파생된 단계 |

### 시나리오 내러티브
엔지니어링 생산성 도구는 다양한 작업을 처리합니다: 코드 리팩터링, 아키텍처 노트 요약, 피드백 분류. 지연 시간 및 리소스 사용을 최소화하기 위해, 작은 일반 모델이 계획 및 요약을 처리하고, 코드 특화 모델이 리팩터링을 수행하며, 경량 분류 가능 모델이 피드백을 라벨링합니다. 파이프라인 스크립트는 연결 및 개선을 시연하며, 라우터 스크립트는 적응형 단일 프롬프트 라우팅을 분리합니다.

### 카탈로그 스냅샷
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### 테스트 프롬프트 예시
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### 추적 확장 (선택 사항)
`models_pipeline.py`에 대한 단계별 추적 JSON 라인 추가:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### 에스컬레이션 휴리스틱 (아이디어)
계획에 "최적화", "보안"과 같은 키워드가 포함되거나 단계 길이가 280자를 초과할 경우 → 해당 단계에만 더 큰 모델 (예: `gpt-oss-20b`)로 에스컬레이션.

### 선택적 개선 사항

| 영역 | 개선 사항 | 가치 | 힌트 |
|------|----------|------|------|
| 캐싱 | 관리자 + 클라이언트 객체 재사용 | 지연 시간 감소, 오버헤드 감소 | `workshop_utils.get_client` 사용 |
| 사용량 메트릭 | 토큰 및 단계별 지연 시간 캡처 | 프로파일링 및 최적화 | 각 라우팅 호출 시간 측정; 추적 리스트에 저장 |
| 적응형 라우팅 | 신뢰도/비용 인식 | 품질-비용 균형 개선 | 점수 추가: 프롬프트 > N자 또는 정규 표현식이 도메인 일치 → 더 큰 모델로 에스컬레이션 |
| 동적 기능 레지스트리 | 카탈로그 핫 리로드 | 재시작 재배포 불필요 | 런타임에 `catalog.json` 로드; 파일 타임스탬프 감시 |
| 폴백 전략 | 실패 시 견고성 | 가용성 향상 | 기본 시도 → 예외 발생 시 폴백 별칭 |
| 스트리밍 파이프라인 | 초기 피드백 | UX 개선 | 각 단계를 스트리밍하고 최종 개선 입력 버퍼링 |
| 벡터 의도 임베딩 | 더 정교한 라우팅 | 의도 정확도 향상 | 프롬프트 임베딩, 클러스터링 및 중심 → 기능 매핑 |
| 추적 내보내기 | 감사 가능한 체인 | 규정 준수/보고 | JSON 라인 내보내기: 단계, 의도, 모델, 지연 시간_ms, 토큰 |
| 비용 시뮬레이션 | 클라우드 이전 추정 | 예산 계획 | 모델당 토큰당 가상 비용 할당 및 작업당 집계 |
| 결정론적 모드 | 재현 가능성 | 안정적인 벤치마킹 | 환경: `temperature=0`, 고정된 단계 수 |

#### 추적 구조 예시

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### 적응형 에스컬레이션 스케치

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### 모델 카탈로그 핫 리로드

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.