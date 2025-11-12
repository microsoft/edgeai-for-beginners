<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T21:14:44+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "en"
}
-->
# Session 4: Explore Cutting-Edge Models – LLMs, SLMs & On-Device Inference

## Abstract

Compare Large Language Models (LLMs) and Small Language Models (SLMs) for local versus cloud inference scenarios. Learn deployment strategies using ONNX Runtime acceleration, WebGPU execution, and hybrid RAG experiences. Includes a Chainlit RAG demo with a local model and an optional OpenWebUI exploration. You will adapt a WebGPU inference starter and evaluate Phi versus GPT-OSS-20B in terms of capability and cost/performance trade-offs.

## Learning Objectives

- **Contrast** SLM and LLM based on latency, memory usage, and quality
- **Deploy** models using ONNXRuntime and (where supported) WebGPU
- **Run** browser-based inference (privacy-preserving interactive demo)
- **Integrate** a Chainlit RAG pipeline with a local SLM backend
- **Evaluate** using lightweight quality and cost heuristics

## Prerequisites

- Completion of Sessions 1–3
- `chainlit` installed (already included in `requirements.txt` for Module08)
- WebGPU-capable browser (latest Edge/Chrome on Windows 11)
- Foundry Local running (`foundry service status`)

### Cross-Platform Notes

Windows remains the primary target environment. For macOS developers awaiting native binaries:
1. Run Foundry Local in a Windows 11 VM (Parallels / UTM) OR a remote Windows workstation.
2. Expose the service (default port 5273) and configure on macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Follow the same Python virtual environment steps as in previous sessions.

Chainlit installation (both platforms):
```bash
pip install chainlit
```

## Demo Flow (30 min)

### 1. Compare Phi (SLM) vs GPT-OSS-20B (LLM) (6 min)

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

Track: response depth, factual accuracy, stylistic richness, latency.

Observe throughput changes after enabling GPU versus CPU-only.

### 3. WebGPU Inference in Browser (6 min)

Adapt starter `04-webgpu-inference` (create `samples/04-cutting-edge/webgpu_demo.html`):

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

Open the file in a browser; observe low-latency local roundtrip.

### 4. Chainlit RAG Chat App (7 min)

Minimal `samples/04-cutting-edge/chainlit_app.py`:

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

Run:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Starter Project: Adapt `04-webgpu-inference` (6 min)

Deliverables:
- Replace placeholder fetch logic with streaming tokens (use `stream=True` endpoint variant once enabled)
- Add latency chart (client-side) for Phi versus GPT-OSS-20B toggles
- Embed RAG context inline (textarea for reference docs)

## Evaluation Heuristics

| Category | Phi-4-mini | GPT-OSS-20B | Observation |
|----------|------------|-------------|-------------|
| Latency (cold) | Fast | Slower | SLM warms quickly |
| Memory | Low | High | Device feasibility |
| Context adherence | Good | Strong | Larger model may be more verbose |
| Cost (local) | Minimal | Higher (resource) | Energy/time trade-off |
| Best use case | Edge apps | Deep reasoning | Hybrid pipeline possible |

## Validating Environment

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Troubleshooting

| Symptom | Cause | Action |
|---------|-------|--------|
| Web page fetch fails | CORS or service down | Use `curl` to verify endpoint; enable CORS proxy if needed |
| Chainlit blank | Env not active | Activate venv & reinstall dependencies |
| High latency | Model just loaded | Warm with small prompt sequence |

## References

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG Evaluation (Ragas): https://docs.ragas.io

---

**Session Duration**: 30 min  
**Difficulty**: Advanced

## Sample Scenario & Workshop Mapping

| Workshop Artifacts | Scenario | Objective | Data / Prompt Source |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Architecture team evaluating SLM vs LLM for executive summary generator | Quantify latency + token usage delta | Single `COMPARE_PROMPT` env var |
| `chainlit_app.py` (RAG demo) | Internal knowledge assistant prototype | Ground short answers with minimal lexical retrieval | Inline `DOCS` list in file |
| `webgpu_demo.html` | Futuristic on‑device browser inference preview | Show low‑latency local roundtrip + UX narrative | Live user prompt only |

### Scenario Narrative
The product team wants an executive briefing generator. A lightweight SLM (Phi‑4‑mini) drafts summaries; a larger LLM (GPT‑OSS‑20B) may refine only high‑priority reports. Session scripts capture empirical latency and token metrics to justify a hybrid design, while the Chainlit demo illustrates how grounded retrieval keeps small model answers factual. The WebGPU concept page provides a vision path for fully client‑side processing when browser acceleration matures.

### Minimal RAG Context (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hybrid Draft→Refine Flow (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Track both latency components to report blended average cost.

### Optional Enhancements

| Focus | Enhancement | Why | Implementation Hint |
|-------|------------|-----|---------------------|
| Comparative Metrics | Track token usage + first-token latency | Holistic performance view | Use enhanced benchmark script (Session 3) with `BENCH_STREAM=1` |
| Hybrid Pipeline | SLM draft → LLM refine | Reduce latency & cost | Generate with Phi-4-mini, refine summary with GPT-OSS-20B |
| Streaming UI | Better UX in Chainlit | Incremental feedback | Use `stream=True` once local streaming is exposed; accumulate chunks |
| WebGPU Caching | Faster JS initialization | Reduce recompile overhead | Cache compiled shader artifacts (future runtime capability) |
| Deterministic QA Set | Fair model comparison | Remove variance | Fixed prompt list + `temperature=0` for evaluation runs |
| Output Scoring | Structured quality lens | Move beyond anecdotes | Simple rubric: coherence / factuality / brevity (1–5) |
| Energy / Resource Notes | Classroom discussion | Show trade-offs | Use OS monitors (Task Manager, `nvidia-smi`) + benchmark script outputs |
| Cost Emulation | Pre-cloud justification | Plan scaling | Map tokens to hypothetical cloud pricing for TCO narrative |
| Latency Decomposition | Identify bottlenecks | Target optimizations | Measure prompt prep, request send, first token, full completion |
| RAG + LLM Fallback | Quality safety net | Improve difficult queries | If SLM answer length < threshold or low confidence → escalate |

#### Example Hybrid Draft/Refine Pattern

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Latency Breakdown Sketch

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Use consistent measurement scaffolding across models for fair comparisons.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->