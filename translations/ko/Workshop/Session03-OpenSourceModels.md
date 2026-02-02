# 세션 3: Foundry Local에서 오픈소스 모델 활용

## 개요

Hugging Face 및 기타 오픈소스 모델을 Foundry Local에 도입하는 방법을 알아보세요. 모델 선택 전략, 커뮤니티 기여 워크플로우, 성능 비교 방법론, 그리고 Foundry를 사용자 정의 모델 등록으로 확장하는 방법을 배웁니다. 이 세션은 주간 "Model Mondays" 탐구 주제와 연결되며, 오픈소스 모델을 로컬에서 평가하고 운영화한 후 Azure로 확장할 수 있는 능력을 제공합니다.

## 학습 목표

세션 종료 후, 다음을 수행할 수 있습니다:

- **발견 및 평가**: 품질과 리소스 간의 균형을 고려하여 후보 모델(mistral, gemma, qwen, deepseek)을 식별합니다.
- **로드 및 실행**: Foundry Local CLI를 사용하여 커뮤니티 모델을 다운로드, 캐시 및 실행합니다.
- **벤치마크**: 일관된 지연 시간 + 토큰 처리량 + 품질 기준을 적용합니다.
- **확장**: SDK 호환 패턴을 따라 사용자 정의 모델 래퍼를 등록하거나 수정합니다.
- **비교**: SLM과 중간 크기 LLM 선택 결정을 위한 구조화된 비교를 생성합니다.

## 사전 요구 사항

- 세션 1 및 2 완료
- `foundry-local-sdk`가 설치된 Python 환경
- 여러 모델 캐시를 위한 최소 15GB의 여유 디스크 공간

### 크로스 플랫폼 환경 빠른 시작

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS에서 Windows 호스트 서비스를 벤치마킹할 때 설정:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## 데모 흐름 (30분)

### 1. CLI를 통해 Hugging Face 모델 로드 (8분)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. 실행 및 간단한 탐색 (5분)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. 벤치마크 스크립트 (8분)

`samples/03-oss-models/benchmark_models.py` 생성:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

실행:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. 성능 비교 (5분)

로드 시간, 메모리 사용량(Task Manager / `nvidia-smi` / OS 리소스 모니터 관찰), 출력 품질과 속도 간의 트레이드오프를 논의합니다. Python 벤치마크 스크립트(Session 3)를 사용하여 지연 시간 및 처리량을 측정하고 GPU 가속을 활성화한 후 반복합니다.

### 5. 시작 프로젝트 (4분)

벤치마크 스크립트를 확장하여 마크다운 내보내기를 추가하여 모델 비교 보고서 생성.

## 시작 프로젝트: `03-huggingface-models` 확장

기존 샘플을 다음과 같이 개선합니다:

1. 벤치마크 집계 및 CSV/Markdown 출력 추가.
2. 간단한 정성적 점수화 구현(프롬프트 쌍 세트 + 수동 주석 스텁 파일).
3. JSON 구성(`models.json`)을 추가하여 플러그 가능한 모델 목록 및 프롬프트 세트 제공.

## 검증 체크리스트

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

모든 대상 모델이 나타나고 프로브 채팅 요청에 응답해야 합니다.

## 샘플 시나리오 및 워크숍 매핑

| 워크숍 스크립트 | 시나리오 | 목표 | 프롬프트 / 데이터셋 출처 |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | 엣지 플랫폼 팀이 내장 요약 도구를 위한 기본 SLM 선택 | 후보 모델 간의 지연 시간 + p95 + 토큰/초 비교 생성 | 인라인 `PROMPT` 변수 + 환경 `BENCH_MODELS` 목록 |

### 시나리오 내러티브
제품 엔지니어링 팀은 오프라인 회의 노트 기능을 위한 기본 경량 요약 모델을 선택해야 합니다. 고정된 프롬프트 세트를 사용하여 제어된 결정론적 벤치마크(temperature=0)를 실행하고 GPU 가속 여부에 따라 지연 시간 및 처리량 메트릭을 수집합니다.

### 예제 프롬프트 세트 JSON (확장 가능)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

각 모델별로 프롬프트를 반복 실행하며 프롬프트별 지연 시간을 캡처하여 분포 메트릭을 도출하고 이상값을 감지합니다.

## 모델 선택 프레임워크

| 차원 | 메트릭 | 중요성 |
|------|--------|--------|
| 지연 시간 | 평균 / p95 | 사용자 경험 일관성 |
| 처리량 | 토큰/초 | 배치 및 스트리밍 확장성 |
| 메모리 | 상주 크기 | 장치 적합성 및 동시성 |
| 품질 | 기준 프롬프트 | 작업 적합성 |
| 발자국 | 디스크 캐시 | 배포 및 업데이트 |
| 라이선스 | 사용 허가 | 상업적 준수 |

## 사용자 정의 모델 확장

고수준 패턴(의사 코드):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

진화하는 어댑터 인터페이스에 대한 공식 저장소를 참조하세요:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## 문제 해결

| 문제 | 원인 | 해결책 |
|------|------|--------|
| mistral-7b에서 OOM 발생 | RAM/GPU 부족 | 다른 모델 중지; 더 작은 변형 시도 |
| 첫 응답 느림 | 초기 로드 | 가벼운 프롬프트를 주기적으로 실행하여 예열 유지 |
| 다운로드 중단 | 네트워크 불안정 | 재시도; 비혼잡 시간에 미리 가져오기 |

## 참고 자료

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face 모델 탐색: https://huggingface.co/models

---

**세션 시간**: 30분 (+ 선택적 심화 학습)  
**난이도**: 중급

### 선택적 개선 사항

| 개선 사항 | 이점 | 방법 |
|-----------|------|------|
| 스트리밍 첫 토큰 지연 시간 | 인지된 응답성 측정 | `BENCH_STREAM=1`로 벤치마크 실행 (`Workshop/samples/session03`의 개선된 스크립트 사용) |
| 결정론적 모드 | 안정적인 회귀 비교 | `temperature=0`, 고정 프롬프트 세트, JSON 출력 캡처 및 버전 관리 |
| 품질 기준 점수화 | 정성적 차원 추가 | 예상 측면이 포함된 `prompts.json` 유지; 점수(1–5)를 수동으로 또는 보조 모델을 통해 주석 처리 |
| CSV / Markdown 내보내기 | 공유 가능한 보고서 | 스크립트를 확장하여 테이블 및 하이라이트가 포함된 `benchmark_report.md` 작성 |
| 모델 기능 태그 | 이후 자동 라우팅에 도움 | `{alias: {capabilities:[], size_mb:..}}`가 포함된 `models.json` 유지 |
| 캐시 예열 단계 | 초기 시작 편향 감소 | 타이밍 루프 전에 한 번의 예열 라운드 실행 (이미 구현됨) |
| 백분위 정확도 | 강력한 꼬리 지연 시간 | numpy 백분위 사용 (이미 리팩토링된 스크립트에 포함됨) |
| 토큰 비용 추정 | 경제적 비교 | 대략적인 비용 = (토큰/초 * 요청당 평균 토큰) * 에너지 추정치 |
| 실패한 모델 자동 건너뛰기 | 배치 실행의 복원력 | 각 벤치마크를 try/except로 감싸고 상태 필드 표시 |

#### 최소 Markdown 내보내기 스니펫

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### 결정론적 프롬프트 세트 예제

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

고정된 목록을 반복 실행하여 커밋 간 비교 가능한 메트릭을 생성합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->