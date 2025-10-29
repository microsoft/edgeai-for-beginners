<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T20:57:02+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "ko"
}
-->
# 세션 5: Foundry Local로 AI 기반 에이전트를 빠르게 구축하기

## 개요

Foundry Local의 저지연, 개인정보 보호 실행 환경을 활용하여 다중 역할 AI 에이전트를 설계하고 조율합니다. 에이전트 역할, 메모리 전략, 도구 호출 패턴, 실행 그래프를 정의합니다. 이 세션에서는 Chainlit 또는 LangGraph로 확장할 수 있는 스캐폴딩 패턴을 소개합니다. 시작 프로젝트는 기존 에이전트 아키텍처 샘플을 확장하여 메모리 지속성과 평가 훅을 추가합니다.

## 학습 목표

- **역할 정의**: 시스템 프롬프트 및 기능 경계 설정
- **메모리 구현**: 단기(대화), 장기(벡터/파일), 임시 스크래치패드
- **워크플로우 스캐폴딩**: 순차적, 분기형, 병렬 에이전트 단계
- **도구 통합**: 경량 함수 도구 호출 패턴
- **평가**: 기본 추적 + 루브릭 기반 결과 점수화

## 사전 요구 사항

- 세션 1–4 완료
- `foundry-local-sdk`, `openai`, 선택적 `chainlit`을 포함한 Python
- 로컬 모델 실행 중 (최소 `phi-4-mini`)

### 크로스 플랫폼 환경 코드 스니펫

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS에서 원격 Windows 호스트 서비스를 대상으로 에이전트를 실행하는 경우:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## 데모 흐름 (30분)

### 1. 에이전트 역할 및 메모리 정의 (7분)

`samples/05-agents/agents_core.py` 생성:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. CLI 스캐폴딩 패턴 (3분)

```powershell
python samples/05-agents/agents_core.py
```


### 3. 도구 호출 추가 (7분)

`samples/05-agents/tools.py`로 확장:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```


`agents_core.py`를 수정하여 간단한 도구 구문을 허용: 사용자가 `#tool:get_time`을 작성하면 에이전트가 생성 전에 컨텍스트에 도구 출력을 확장합니다.

### 4. 워크플로우 조율 (6분)

`samples/05-agents/orchestrator.py` 생성:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. 시작 프로젝트: `05-agent-architecture` 확장 (7분)

추가:
1. 지속적인 메모리 계층 (예: 대화 내용을 JSON 라인으로 추가)
2. 간단한 평가 루브릭: 사실성 / 명확성 / 스타일 플레이스홀더
3. 선택적 Chainlit 프론트엔드 (두 개의 탭: 대화 및 추적)
4. 선택적 LangGraph 스타일 상태 기계 (종속성 추가 시)로 분기 결정

## 검증 체크리스트

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```


도구 삽입 노트가 포함된 구조화된 파이프라인 출력을 기대하세요.

## 메모리 전략 개요

| 계층 | 목적 | 예시 |
|------|------|------|
| 단기 | 대화 연속성 | 마지막 N개의 메시지 |
| 에피소드 | 세션 회상 | 세션당 JSON |
| 의미적 | 장기 검색 | 요약의 벡터 저장소 |
| 스크래치패드 | 추론 단계 | 인라인 체인-오브-생각 (비공개) |

## 평가 훅 (개념적)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## 문제 해결

| 문제 | 원인 | 해결책 |
|------|------|--------|
| 반복적인 답변 | 컨텍스트 창이 너무 크거나 작음 | 메모리 창 매개변수 조정 |
| 도구가 호출되지 않음 | 잘못된 구문 | `#tool:tool_name` 형식 사용 |
| 느린 조율 | 여러 냉 모델 | 사전 실행 웜업 프롬프트 사용 |

## 참고 자료

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (선택적 개념): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**세션 시간**: 30분  
**난이도**: 고급

## 샘플 시나리오 및 워크숍 매핑

| 워크숍 스크립트 | 시나리오 | 목표 | 예시 프롬프트 |
|-----------------|----------|------|--------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | 경영진 친화적 요약을 생성하는 지식 연구 봇 | 두 에이전트 파이프라인 (연구 → 편집적 다듬기) 및 선택적 개별 모델 | 엣지 추론이 컴플라이언스에 왜 중요한지 설명하세요. |
| (확장된) `tools.py` 개념 | 시간 및 토큰 추정 도구 추가 | 경량 도구 호출 패턴 시연 | #tool:get_time |

### 시나리오 내러티브

컴플라이언스 문서화 팀은 클라우드 서비스로 초안을 보내지 않고 로컬 지식에서 빠르게 내부 브리핑을 생성해야 합니다. 연구 에이전트는 간결한 사실적 요점을 수집하고, 편집 에이전트는 경영진의 명확성을 위해 다시 작성합니다. 지연 시간을 최적화하기 위해 (빠른 SLM)와 스타일 다듬기 (필요할 때만 더 큰 모델) 간에 별도의 모델 별칭을 할당할 수 있습니다.

### 예시 다중 모델 환경

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### 추적 구조 (선택적)

```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```


각 단계를 JSONL 파일에 저장하여 나중에 루브릭 점수를 매깁니다.

### 선택적 개선 사항

| 테마 | 개선 사항 | 이점 | 구현 스케치 |
|------|----------|------|------------|
| 다중 모델 역할 | 에이전트별로 다른 모델 (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | 전문화 및 속도 | 별칭 환경 변수 선택, 역할별 별칭으로 `chat_once` 호출 |
| 구조화된 추적 | 각 행위(tool, input, latency, tokens)의 JSON 추적 | 디버그 및 평가 | 딕트를 리스트에 추가; 끝에 `.jsonl` 작성 |
| 메모리 지속성 | 다시 로드 가능한 대화 컨텍스트 | 세션 연속성 | `Agent.memory`를 `sessions/<ts>.json`에 덤프 |
| 도구 레지스트리 | 동적 도구 검색 | 확장성 | `TOOLS` 딕트를 유지하고 이름/설명을 탐색 |
| 재시도 및 백오프 | 견고한 긴 체인 | 일시적 오류 감소 | `act`를 try/except + 지수 백오프와 함께 래핑 |
| 루브릭 점수화 | 자동화된 정성적 레이블 | 개선 사항 추적 | 모델을 프롬프트하여 "명확성을 1-5로 평가" |
| 벡터 메모리 | 의미적 회상 | 풍부한 장기 컨텍스트 | 요약을 임베딩하고 시스템 메시지에 상위-k 검색 |
| 스트리밍 응답 | 더 빠른 응답 인식 | UX 개선 | 스트리밍 사용 가능 시 사용하고 부분 토큰 플러시 |
| 결정론적 테스트 | 회귀 제어 | 안정적인 CI | `temperature=0`, 고정된 프롬프트 시드로 실행 |
| 병렬 분기 | 더 빠른 탐색 | 처리량 | 독립적인 에이전트 단계를 위해 `concurrent.futures` 사용 |

#### 추적 기록 예시

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### 간단한 평가 프롬프트

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```


(`answer`, `rating`) 쌍을 저장하여 역사적 품질 그래프를 구축합니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.