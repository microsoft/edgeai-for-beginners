<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T22:44:20+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "tl"
}
-->
# Session 4: Tuklasin ang Pinakabagong Modelo – LLMs, SLMs & On-Device Inference

## Abstrak

Ihambing ang Large Language Models (LLMs) at Small Language Models (SLMs) para sa mga senaryo ng lokal at cloud inference. Matutunan ang mga pattern ng deployment gamit ang ONNX Runtime acceleration, WebGPU execution, at hybrid RAG experiences. Kasama ang Chainlit RAG demo gamit ang lokal na modelo at opsyonal na OpenWebUI exploration. Aangkopin mo ang WebGPU inference starter at susuriin ang kakayahan ng Phi kumpara sa GPT-OSS-20B pati na rin ang trade-offs sa gastos/performance.

## Mga Layunin sa Pag-aaral

- **Ihambing** ang SLM at LLM sa latency, memory, at kalidad
- **I-deploy** ang mga modelo gamit ang ONNXRuntime at (kung suportado) WebGPU
- **Patakbuhin** ang inference sa browser (privacy-preserving interactive demo)
- **Isama** ang Chainlit RAG pipeline gamit ang lokal na SLM backend
- **Suriin** gamit ang magaan na heuristics para sa kalidad at gastos

## Mga Kinakailangan

- Natapos ang Sessions 1–3
- Naka-install ang `chainlit` (nasa `requirements.txt` para sa Module08)
- Browser na may kakayahang WebGPU (Edge / Chrome pinakabagong bersyon sa Windows 11)
- Naka-on ang Foundry Local (`foundry status`)

### Mga Tala para sa Iba't Ibang Platform

Ang Windows ang pangunahing target na environment. Para sa mga developer ng macOS na naghihintay ng native binaries:
1. Patakbuhin ang Foundry Local sa Windows 11 VM (Parallels / UTM) O sa remote Windows workstation.
2. I-expose ang serbisyo (default port 5273) at i-set sa macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Gamitin ang parehong hakbang sa Python virtual environment tulad ng sa mga naunang session.

Pag-install ng Chainlit (parehong platform):
```bash
pip install chainlit
```

## Daloy ng Demo (30 minuto)

### 1. Ihambing ang Phi (SLM) vs GPT-OSS-20B (LLM) (6 minuto)

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

Subaybayan: lalim ng sagot, katumpakan ng impormasyon, yaman ng estilo, latency.

### 2. ONNX Runtime Acceleration (5 minuto)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Obserbahan ang mga pagbabago sa throughput pagkatapos i-enable ang GPU kumpara sa CPU-only.

### 3. WebGPU Inference sa Browser (6 minuto)

Iangkop ang starter `04-webgpu-inference` (gumawa ng `samples/04-cutting-edge/webgpu_demo.html`):

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

Buksan ang file sa browser; obserbahan ang mababang latency sa lokal na roundtrip.

### 4. Chainlit RAG Chat App (7 minuto)

Minimal na `samples/04-cutting-edge/chainlit_app.py`:

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

Patakbuhin:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Starter Project: Iangkop ang `04-webgpu-inference` (6 minuto)

Mga Deliverables:
- Palitan ang placeholder fetch logic ng streaming tokens (gamitin ang `stream=True` endpoint variant kapag na-enable)
- Magdagdag ng latency chart (client-side) para sa phi vs gpt-oss-20b toggles
- I-embed ang RAG context inline (textarea para sa reference docs)

## Heuristics sa Pagsusuri

| Kategorya | Phi-4-mini | GPT-OSS-20B | Obserbasyon |
|-----------|------------|-------------|-------------|
| Latency (cold) | Mabilis | Mas mabagal | Mabilis mag-init ang SLM |
| Memory | Mababa | Mataas | Kakayahan ng device |
| Pagsunod sa konteksto | Maganda | Malakas | Mas detalyado ang mas malaking modelo |
| Gastos (lokal) | Minimal | Mas mataas (resource) | Trade-off sa enerhiya/oras |
| Pinakamainam na paggamit | Edge apps | Malalim na pag-iisip | Posibleng hybrid pipeline |

## Pagpapatunay ng Environment

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Pag-aayos ng Problema

| Sintomas | Sanhi | Aksyon |
|----------|-------|--------|
| Nabigo ang pag-fetch ng web page | CORS o serbisyo ay down | Gamitin ang `curl` para i-verify ang endpoint; i-enable ang CORS proxy kung kinakailangan |
| Blangko ang Chainlit | Hindi aktibo ang env | I-activate ang venv at i-reinstall ang mga dependency |
| Mataas na latency | Kakabukas lang ng modelo | I-init gamit ang maliit na prompt sequence |

## Mga Sanggunian

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG Evaluation (Ragas): https://docs.ragas.io

---

**Tagal ng Session**: 30 minuto  
**Kahirapan**: Advanced

## Halimbawang Scenario at Pagmamapa ng Workshop

| Mga Artifact ng Workshop | Scenario | Layunin | Pinagmulan ng Data / Prompt |
|--------------------------|----------|---------|-----------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Koponan ng arkitektura na nagsusuri ng SLM vs LLM para sa executive summary generator | Sukatin ang pagkakaiba sa latency + token usage | Single `COMPARE_PROMPT` env var |
| `chainlit_app.py` (RAG demo) | Prototype ng internal knowledge assistant | Magbigay ng maikling sagot na may minimal lexical retrieval | Inline na listahan ng `DOCS` sa file |
| `webgpu_demo.html` | Preview ng futuristic on-device browser inference | Ipakita ang mababang latency sa lokal na roundtrip + UX narrative | Live user prompt lamang |

### Narrative ng Scenario
Nais ng product org na magkaroon ng executive briefing generator. Ang magaan na SLM (phi-4-mini) ang gumagawa ng mga draft ng summary; ang mas malaking LLM (gpt-oss-20b) ay maaaring mag-refine ng mga high-priority na ulat lamang. Ang mga script ng session ay nagtatala ng empirical latency at token metrics upang bigyang-katwiran ang hybrid na disenyo, habang ang Chainlit demo ay nagpapakita kung paano pinapanatili ng grounded retrieval ang factual na sagot ng maliit na modelo. Ang WebGPU concept page ay nagbibigay ng vision path para sa ganap na client-side processing kapag umunlad ang browser acceleration.

### Minimal na RAG Context (Chainlit)
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

Subaybayan ang parehong latency components upang iulat ang blended average cost.

### Opsyonal na Mga Pagpapahusay

| Pokus | Pagpapahusay | Bakit | Pahiwatig sa Implementasyon |
|-------|-------------|-------|-----------------------------|
| Mga Comparative Metrics | Subaybayan ang token usage + first-token latency | Holistic na view ng performance | Gamitin ang enhanced benchmark script (Session 3) na may `BENCH_STREAM=1` |
| Hybrid Pipeline | SLM draft → LLM refine | Bawasan ang latency at gastos | Gumawa gamit ang phi-4-mini, i-refine ang summary gamit ang gpt-oss-20b |
| Streaming UI | Mas magandang UX sa Chainlit | Incremental na feedback | Gamitin ang `stream=True` kapag na-expose na ang local streaming; i-accumulate ang chunks |
| WebGPU Caching | Mas mabilis na JS init | Bawasan ang recompile overhead | I-cache ang compiled shader artifacts (future runtime capability) |
| Deterministic QA Set | Makatarungang paghahambing ng modelo | Alisin ang variance | Fixed prompt list + `temperature=0` para sa evaluation runs |
| Output Scoring | Structured na lens ng kalidad | Lumampas sa anecdotal | Simpleng rubric: coherence / factuality / brevity (1–5) |
| Mga Tala sa Enerhiya / Resource | Talakayan sa klase | Ipakita ang trade-offs | Gamitin ang OS monitors (`foundry system info`, Task Manager, `nvidia-smi`) + benchmark script outputs |
| Cost Emulation | Pre-cloud na pagbibigay-katwiran | Planuhin ang scaling | I-map ang tokens sa hypothetical cloud pricing para sa TCO narrative |
| Latency Decomposition | Tukuyin ang bottlenecks | Target ang optimizations | Sukatin ang prompt prep, request send, first token, full completion |
| RAG + LLM Fallback | Quality safety net | Pagbutihin ang mahihirap na query | Kung ang haba ng sagot ng SLM ay mas mababa sa threshold o mababa ang confidence → escalate |

#### Halimbawa ng Hybrid Draft/Refine Pattern

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Sketch ng Latency Breakdown

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Gumamit ng pare-parehong measurement scaffolding sa mga modelo para sa makatarungang paghahambing.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.