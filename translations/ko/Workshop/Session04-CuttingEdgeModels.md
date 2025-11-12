<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T22:10:15+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "ko"
}
-->
# 세션 4: 최첨단 모델 탐구 – LLM, SLM 및 디바이스 내 추론

## 개요

클라우드와 로컬 추론 시나리오에서 대형 언어 모델(LLM)과 소형 언어 모델(SLM)을 비교합니다. ONNX Runtime 가속화, WebGPU 실행 및 하이브리드 RAG 경험을 활용한 배포 패턴을 배웁니다. 로컬 모델을 사용한 Chainlit RAG 데모와 선택적으로 OpenWebUI 탐색이 포함됩니다. WebGPU 추론 스타터를 조정하고 Phi와 GPT-OSS-20B의 성능 및 비용/효율성 트레이드오프를 평가합니다.

## 학습 목표

- **비교**: SLM과 LLM의 지연 시간, 메모리, 품질 축에서의 차이점
- **배포**: ONNXRuntime 및 (지원되는 경우) WebGPU를 사용하여 모델 배포
- **실행**: 브라우저 기반 추론(개인정보 보호를 위한 인터랙티브 데모)
- **통합**: 로컬 SLM 백엔드와 Chainlit RAG 파이프라인 통합
- **평가**: 경량 품질 및 비용 휴리스틱을 사용한 평가

## 사전 요구 사항

- 세션 1–3 완료
- `chainlit` 설치됨 (Module08의 `requirements.txt`에 이미 포함됨)
- WebGPU 지원 브라우저(Windows 11에서 최신 Edge / Chrome)
- Foundry Local 실행 중 (`foundry service status`)

### 크로스 플랫폼 참고 사항

Windows는 주요 대상 환경입니다. macOS 개발자가 네이티브 바이너리를 기다리는 동안:
1. Windows 11 VM(Parallels / UTM) 또는 원격 Windows 워크스테이션에서 Foundry Local 실행.
2. 서비스를 노출(default port 5273)하고 macOS에서 설정:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. 이전 세션과 동일한 Python 가상 환경 단계를 사용.

Chainlit 설치(두 플랫폼 모두):
```bash
pip install chainlit
```

## 데모 흐름 (30분)

### 1. Phi(SLM) vs GPT-OSS-20B(LLM) 비교 (6분)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

추적: 응답 깊이, 사실 정확성, 스타일 풍부함, 지연 시간.

GPU 활성화 후 처리량 변화를 관찰(CPU 전용과 비교).

### 3. 브라우저에서 WebGPU 추론 (6분)

스타터 `04-webgpu-inference` 조정(`samples/04-cutting-edge/webgpu_demo.html` 생성):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

브라우저에서 파일 열기; 저지연 로컬 라운드트립 관찰.

### 4. Chainlit RAG 채팅 앱 (7분)

최소한의 `samples/04-cutting-edge/chainlit_app.py`:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

실행:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. 스타터 프로젝트: `04-webgpu-inference` 조정 (6분)

산출물:
- 플레이스홀더 fetch 로직을 스트리밍 토큰으로 교체(`stream=True` 엔드포인트 변형 사용 가능 시)
- phi와 gpt-oss-20b 토글을 위한 지연 시간 차트(클라이언트 측) 추가
- RAG 컨텍스트를 인라인으로 포함(참조 문서를 위한 텍스트 영역)

## 평가 휴리스틱

| 카테고리 | Phi-4-mini | GPT-OSS-20B | 관찰 |
|----------|------------|-------------|-------------|
| 지연 시간(콜드) | 빠름 | 느림 | SLM은 빠르게 워밍업 |
| 메모리 | 낮음 | 높음 | 디바이스 적합성 |
| 컨텍스트 준수 | 좋음 | 강력함 | 더 큰 모델은 더 장황할 수 있음 |
| 비용(로컬) | 최소 | 높음(자원) | 에너지/시간 트레이드오프 |
| 최적 사용 사례 | 엣지 앱 | 심층적 추론 | 하이브리드 파이프라인 가능 |

## 환경 검증

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## 문제 해결

| 증상 | 원인 | 조치 |
|---------|-------|--------|
| 웹 페이지 fetch 실패 | CORS 또는 서비스 다운 | 엔드포인트를 확인하려면 `curl` 사용; 필요 시 CORS 프록시 활성화 |
| Chainlit 빈 화면 | 환경 활성화되지 않음 | venv 활성화 및 종속성 재설치 |
| 높은 지연 시간 | 모델이 방금 로드됨 | 작은 프롬프트 시퀀스로 워밍업 |

## 참고 자료

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG 평가(Ragas): https://docs.ragas.io

---

**세션 소요 시간**: 30분  
**난이도**: 고급

## 샘플 시나리오 및 워크숍 매핑

| 워크숍 아티팩트 | 시나리오 | 목표 | 데이터 / 프롬프트 소스 |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | 경영진 요약 생성기를 평가하는 아키텍처 팀 | 지연 시간 및 토큰 사용량 차이를 정량화 | 단일 `COMPARE_PROMPT` 환경 변수 |
| `chainlit_app.py` (RAG 데모) | 내부 지식 보조 프로토타입 | 최소한의 어휘 검색으로 짧은 답변을 기반화 | 파일 내 인라인 `DOCS` 목록 |
| `webgpu_demo.html` | 미래 지향적 디바이스 내 브라우저 추론 미리보기 | 저지연 로컬 라운드트립 및 UX 내러티브 표시 | 라이브 사용자 프롬프트만 사용 |

### 시나리오 내러티브
제품 조직은 경영진 브리핑 생성기를 원합니다. 경량 SLM(phi‑4‑mini)이 요약을 작성하고, 더 큰 LLM(gpt‑oss‑20b)은 고우선 보고서만 정제할 수 있습니다. 세션 스크립트는 하이브리드 설계를 정당화하기 위해 경험적 지연 시간 및 토큰 메트릭을 캡처하며, Chainlit 데모는 소형 모델 답변을 사실적으로 유지하는 방법을 보여줍니다. WebGPU 개념 페이지는 브라우저 가속이 성숙할 때 완전히 클라이언트 측 처리를 위한 비전 경로를 제공합니다.

### 최소 RAG 컨텍스트(Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### 하이브리드 초안→정제 흐름(의사 코드)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

두 지연 시간 구성 요소를 추적하여 혼합 평균 비용을 보고합니다.

### 선택적 개선 사항

| 초점 | 개선 사항 | 이유 | 구현 힌트 |
|-------|------------|-----|---------------------|
| 비교 메트릭 | 토큰 사용량 및 첫 번째 토큰 지연 시간 추적 | 전체적인 성능 보기 | `BENCH_STREAM=1`을 사용한 향상된 벤치마크 스크립트(Session 3) 사용 |
| 하이브리드 파이프라인 | SLM 초안 → LLM 정제 | 지연 시간 및 비용 감소 | phi-4-mini로 생성하고 gpt-oss-20b로 요약 정제 |
| 스트리밍 UI | Chainlit에서 더 나은 UX | 점진적 피드백 | 로컬 스트리밍이 노출되면 `stream=True` 사용; 청크 누적 |
| WebGPU 캐싱 | 더 빠른 JS 초기화 | 재컴파일 오버헤드 감소 | 컴파일된 셰이더 아티팩트 캐싱(미래 런타임 기능) |
| 결정론적 QA 세트 | 공정한 모델 비교 | 변동성 제거 | 고정된 프롬프트 목록 및 평가 실행을 위한 `temperature=0` |
| 출력 점수화 | 구조화된 품질 렌즈 | 일화적 평가를 넘어 이동 | 간단한 루브릭: 일관성 / 사실성 / 간결성(1–5) |
| 에너지 / 자원 노트 | 교실 토론 | 트레이드오프 표시 | OS 모니터(Task Manager, `nvidia-smi`) 및 벤치마크 스크립트 출력 사용 |
| 비용 에뮬레이션 | 클라우드 사전 정당화 | 확장 계획 | 토큰을 가상 클라우드 가격에 매핑하여 TCO 내러티브 작성 |
| 지연 시간 분해 | 병목 현상 식별 | 최적화 대상 | 프롬프트 준비, 요청 전송, 첫 번째 토큰, 전체 완료 측정 |
| RAG + LLM 폴백 | 품질 안전망 | 어려운 쿼리 개선 | SLM 답변 길이가 임계값 미만이거나 신뢰도가 낮을 경우 → 상위 모델로 에스컬레이션 |

#### 하이브리드 초안/정제 패턴 예시

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### 지연 시간 분해 스케치

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

모델 간 공정한 비교를 위해 일관된 측정 구조를 사용하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->