<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-11-11T17:37:26+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "pcm"
}
-->
# Session 4: Explore Cutting-Edge Models – LLMs, SLMs & On-Device Inference

## Abstract

Compare Large Language Models (LLMs) and Small Language Models (SLMs) for local vs cloud inference scenarios. Learn how to deploy models using ONNX Runtime acceleration, WebGPU execution, and hybrid RAG experiences. E go include Chainlit RAG demo wey dey use local model plus optional OpenWebUI exploration. You go adapt WebGPU inference starter and check Phi vs GPT-OSS-20B capability & cost/performance trade-offs.

## Learning Objectives

- **Compare** SLM vs LLM for latency, memory, and quality
- **Deploy** models with ONNXRuntime and (if e dey supported) WebGPU
- **Run** inference for browser (privacy-preserving interactive demo)
- **Integrate** Chainlit RAG pipeline with local SLM backend
- **Check** lightweight quality + cost heuristics

## Prerequisites

- You don complete Sessions 1–3
- `chainlit` don dey installed (e dey already for `requirements.txt` for Module08)
- WebGPU-capable browser (Edge / Chrome latest for Windows 11)
- Foundry Local dey run (`foundry status`)

### Cross-Platform Notes

Windows na di main environment wey we dey target. For macOS developers wey dey wait for native binaries:
1. Run Foundry Local for Windows 11 VM (Parallels / UTM) OR remote Windows workstation.
2. Make di service dey available (default port 5273) and set am for macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Use di same Python virtual environment steps wey you don use for di previous sessions.

Chainlit install (both platforms):
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

### 2. ONNX Runtime Acceleration (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Observe throughput changes after you enable GPU vs CPU-only.

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

Open di file for browser; observe low-latency local roundtrip.

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
- Add latency chart (client-side) for phi vs gpt-oss-20b toggles
- Embed RAG context inline (textarea for reference docs)

## Evaluation Heuristics

| Category | Phi-4-mini | GPT-OSS-20B | Observation |
|----------|------------|-------------|-------------|
| Latency (cold) | Fast | Slower | SLM dey warm quick |
| Memory | Low | High | Device feasibility |
| Context adherence | Good | Strong | Bigger model fit dey verbose |
| Cost (local) | Minimal | Higher (resource) | Energy/time trade-off |
| Best use case | Edge apps | Deep reasoning | Hybrid pipeline fit dey possible |

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
| Web page fetch fails | CORS or service down | Use `curl` to check endpoint; enable CORS proxy if e dey needed |
| Chainlit blank | Env no dey active | Activate venv & reinstall dependencies |
| High latency | Model just load | Warm am with small prompt sequence |

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
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Architecture team dey evaluate SLM vs LLM for executive summary generator | Quantify latency + token usage delta | Single `COMPARE_PROMPT` env var |
| `chainlit_app.py` (RAG demo) | Internal knowledge assistant prototype | Ground short answers with minimal lexical retrieval | Inline `DOCS` list for file |
| `webgpu_demo.html` | Futuristic on‑device browser inference preview | Show low‑latency local roundtrip + UX narrative | Live user prompt only |

### Scenario Narrative
Di product org wan executive briefing generator. Lightweight SLM (phi‑4‑mini) dey draft summaries; bigger LLM (gpt‑oss‑20b) fit refine only high‑priority reports. Session scripts dey capture empirical latency & token metrics to justify hybrid design, while di Chainlit demo dey show how grounded retrieval dey keep small model answers factual. Di WebGPU concept page dey provide vision path for fully client‑side processing when browser acceleration don mature.

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
| Comparative Metrics | Track token usage + first-token latency | Holistic perf view | Use enhanced benchmark script (Session 3) with `BENCH_STREAM=1` |
| Hybrid Pipeline | SLM draft → LLM refine | Reduce latency & cost | Generate with phi-4-mini, refine summary w/ gpt-oss-20b |
| Streaming UI | Better UX in Chainlit | Incremental feedback | Use `stream=True` once local streaming don dey exposed; accumulate chunks |
| WebGPU Caching | Faster JS init | Reduce recompile overhead | Cache compiled shader artifacts (future runtime capability) |
| Deterministic QA Set | Fair model comparison | Remove variance | Fixed prompt list + `temperature=0` for evaluation runs |
| Output Scoring | Structured quality lens | Move beyond anecdotes | Simple rubric: coherence / factuality / brevity (1–5) |
| Energy / Resource Notes | Classroom discussion | Show trade-offs | Use OS monitors (`foundry system info`, Task Manager, `nvidia-smi`) + benchmark script outputs |
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
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->