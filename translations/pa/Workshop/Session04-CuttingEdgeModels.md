<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T21:22:13+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "pa"
}
-->
# ਸੈਸ਼ਨ 4: ਅਧੁਨਿਕ ਮਾਡਲਾਂ ਦੀ ਖੋਜ – LLMs, SLMs ਅਤੇ ਔਨ-ਡਿਵਾਈਸ ਇੰਫਰੈਂਸ

## ਸਾਰ

ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਅਤੇ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲ (SLMs) ਦੀ ਤੁਲਨਾ ਕਰੋ, ਜਦੋਂ ਕਿ ਸਥਾਨਕ ਅਤੇ ਕਲਾਉਡ ਇੰਫਰੈਂਸ ਸਥਿਤੀਆਂ ਲਈ। ONNX Runtime ਤੇਜ਼ੀ, WebGPU ਐਗਜ਼ਿਕਿਊਸ਼ਨ, ਅਤੇ ਹਾਈਬ੍ਰਿਡ RAG ਅਨੁਭਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਿਪਲੌਇਮੈਂਟ ਪੈਟਰਨ ਸਿੱਖੋ। ਇਸ ਵਿੱਚ ਸਥਾਨਕ ਮਾਡਲ ਨਾਲ ਇੱਕ ਚੇਨਲਿਟ RAG ਡੈਮੋ ਅਤੇ ਇੱਕ ਵਿਕਲਪਿਕ OpenWebUI ਖੋਜ ਸ਼ਾਮਲ ਹੈ। ਤੁਸੀਂ WebGPU ਇੰਫਰੈਂਸ ਸਟਾਰਟਰ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰੋਗੇ ਅਤੇ Phi ਅਤੇ GPT-OSS-20B ਦੀ ਸਮਰੱਥਾ ਅਤੇ ਲਾਗਤ/ਪ੍ਰਦਰਸ਼ਨ ਦੇ ਵਪਾਰ-ਅੱਪਾਂ ਦਾ ਮੁਲਾਂਕਨ ਕਰੋਗੇ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

- **ਤੁਲਨਾ ਕਰੋ** SLM ਅਤੇ LLM ਨੂੰ ਲੈਟੈਂਸੀ, ਮੈਮੋਰੀ, ਅਤੇ ਗੁਣਵੱਤਾ ਦੇ ਪੱਖਾਂ 'ਤੇ
- **ਡਿਪਲੌਇ** ਮਾਡਲ ONNXRuntime ਅਤੇ (ਜਿੱਥੇ ਸਹਾਇਕ) WebGPU ਨਾਲ
- **ਚਲਾਓ** ਬ੍ਰਾਊਜ਼ਰ-ਅਧਾਰਿਤ ਇੰਫਰੈਂਸ (ਪ੍ਰਾਈਵੇਸੀ-ਸੁਰੱਖਿਅਤ ਇੰਟਰੈਕਟਿਵ ਡੈਮੋ)
- **ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ** ਇੱਕ ਚੇਨਲਿਟ RAG ਪਾਈਪਲਾਈਨ ਨੂੰ ਸਥਾਨਕ SLM ਬੈਕਐਂਡ ਨਾਲ
- **ਮੁਲਾਂਕਨ ਕਰੋ** ਹਲਕੇ ਗੁਣਵੱਤਾ + ਲਾਗਤ ਹਿਊਰਿਸਟਿਕਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ

## ਪੂਰਵ ਸ਼ਰਤਾਂ

- ਸੈਸ਼ਨ 1–3 ਪੂਰੇ ਕੀਤੇ
- `chainlit` ਇੰਸਟਾਲ ਕੀਤਾ ਹੋਇਆ (Module08 ਲਈ `requirements.txt` ਵਿੱਚ ਪਹਿਲਾਂ ਹੀ ਹੈ)
- WebGPU-ਸਮਰੱਥ ਬ੍ਰਾਊਜ਼ਰ (Windows 11 'ਤੇ Edge / Chrome ਦਾ ਨਵਾਂ ਵਰਜਨ)
- Foundry Local ਚੱਲ ਰਿਹਾ (`foundry status`)

### ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਨੋਟਸ

Windows ਮੁੱਖ ਟਾਰਗਟ ਵਾਤਾਵਰਣ ਹੈ। macOS ਡਿਵੈਲਪਰਾਂ ਲਈ ਜੋ ਮੂਲ ਬਾਈਨਰੀ ਦੀ ਉਡੀਕ ਕਰ ਰਹੇ ਹਨ:
1. Foundry Local ਨੂੰ Windows 11 VM (Parallels / UTM) ਜਾਂ ਦੂਰ-ਦੂਰ Windows ਵਰਕਸਟੇਸ਼ਨ 'ਤੇ ਚਲਾਓ।
2. ਸੇਵਾ ਨੂੰ ਉਜਾਗਰ ਕਰੋ (ਡਿਫਾਲਟ ਪੋਰਟ 5273) ਅਤੇ macOS 'ਤੇ ਸੈਟ ਕਰੋ:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. ਪਿਛਲੇ ਸੈਸ਼ਨਾਂ ਦੇ ਜਿਵੇਂ ਹੀ Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਕਦਮ ਵਰਤੋ।

ਚੇਨਲਿਟ ਇੰਸਟਾਲ (ਦੋਵੇਂ ਪਲੇਟਫਾਰਮਾਂ):
```bash
pip install chainlit
```

## ਡੈਮੋ ਫਲੋ (30 ਮਿੰਟ)

### 1. Phi (SLM) ਅਤੇ GPT-OSS-20B (LLM) ਦੀ ਤੁਲਨਾ ਕਰੋ (6 ਮਿੰਟ)

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

ਟ੍ਰੈਕ ਕਰੋ: ਜਵਾਬ ਦੀ ਗਹਿਰਾਈ, ਤਥਯਿਕ ਸਹੀਤਾ, ਸ਼ੈਲੀਕ ਰਿਚਨੈਸ, ਲੈਟੈਂਸੀ।

### 2. ONNX Runtime ਤੇਜ਼ੀ (5 ਮਿੰਟ)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

GPU ਨੂੰ ਚਾਲੂ ਕਰਨ ਤੋਂ ਬਾਅਦ throughput ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਨੂੰ ਦੇਖੋ।

### 3. ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ WebGPU ਇੰਫਰੈਂਸ (6 ਮਿੰਟ)

ਸਟਾਰਟਰ `04-webgpu-inference` ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰੋ (ਬਣਾਓ `samples/04-cutting-edge/webgpu_demo.html`):

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

ਫਾਈਲ ਨੂੰ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਖੋਲ੍ਹੋ; ਘੱਟ-ਲੈਟੈਂਸੀ ਸਥਾਨਕ ਰਾਊਂਡਟ੍ਰਿਪ ਨੂੰ ਦੇਖੋ।

### 4. ਚੇਨਲਿਟ RAG ਚੈਟ ਐਪ (7 ਮਿੰਟ)

ਘੱਟੋ-ਘੱਟ `samples/04-cutting-edge/chainlit_app.py`:

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

ਚਲਾਓ:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. ਸਟਾਰਟਰ ਪ੍ਰੋਜੈਕਟ: `04-webgpu-inference` ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰੋ (6 ਮਿੰਟ)

ਡਿਲੀਵਰੇਬਲ:
- ਪਲੇਸਹੋਲਡਰ ਫੈਚ ਲੌਜਿਕ ਨੂੰ ਸਟ੍ਰੀਮਿੰਗ ਟੋਕਨ ਨਾਲ ਬਦਲੋ (ਜਦੋਂ `stream=True` ਐਂਡਪੌਇੰਟ ਵਰਜਨ ਸਮਰੱਥ ਹੋਵੇ)
- ਲੈਟੈਂਸੀ ਚਾਰਟ (ਕਲਾਇੰਟ-ਸਾਈਡ) ਸ਼ਾਮਲ ਕਰੋ ਜੋ phi ਅਤੇ gpt-oss-20b ਟੌਗਲ ਲਈ ਹੈ
- RAG ਸੰਦਰਭ ਨੂੰ inline ਸ਼ਾਮਲ ਕਰੋ (ਸੰਬੰਧਿਤ ਦਸਤਾਵੇਜ਼ਾਂ ਲਈ ਟੈਕਸਟੇਰੀਆ)

## ਮੁਲਾਂਕਨ ਹਿਊਰਿਸਟਿਕਸ

| ਸ਼੍ਰੇਣੀ | Phi-4-mini | GPT-OSS-20B | ਅਵਲੋਕਨ |
|----------|------------|-------------|-------------|
| ਲੈਟੈਂਸੀ (ਠੰਡਾ) | ਤੇਜ਼ | ਹੌਲੀ | SLM ਜਲਦੀ ਗਰਮ ਹੁੰਦਾ ਹੈ |
| ਮੈਮੋਰੀ | ਘੱਟ | ਉੱਚਾ | ਡਿਵਾਈਸ ਯੋਗਤਾ |
| ਸੰਦਰਭ ਪਾਲਣਾ | ਚੰਗਾ | ਮਜ਼ਬੂਤ | ਵੱਡਾ ਮਾਡਲ ਹੋ ਸਕਦਾ ਹੈ ਜ਼ਿਆਦਾ verbose |
| ਲਾਗਤ (ਸਥਾਨਕ) | ਘੱਟ | ਉੱਚਾ (ਸੰਸਾਧਨ) | ਊਰਜਾ/ਸਮਾਂ ਵਪਾਰ-ਅੱਪ |
| ਸਭ ਤੋਂ ਵਧੀਆ ਵਰਤੋਂ ਦਾ ਕੇਸ | ਐਜ ਐਪਸ | ਡੀਪ ਰੀਜ਼ਨਿੰਗ | ਹਾਈਬ੍ਰਿਡ ਪਾਈਪਲਾਈਨ ਸੰਭਵ |

## ਵਾਤਾਵਰਣ ਦੀ ਪੁਸ਼ਟੀ

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## ਸਮੱਸਿਆ ਹੱਲ

| ਲੱਛਣ | ਕਾਰਨ | ਕਾਰਵਾਈ |
|---------|-------|--------|
| ਵੈੱਬ ਪੇਜ ਫੈਚ ਫੇਲ | CORS ਜਾਂ ਸੇਵਾ ਡਾਊਨ | ਐਂਡਪੌਇੰਟ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ `curl` ਵਰਤੋਂ ਕਰੋ; ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ CORS ਪ੍ਰੌਕਸੀ ਚਾਲੂ ਕਰੋ |
| ਚੇਨਲਿਟ ਖਾਲੀ | Env ਚਾਲੂ ਨਹੀਂ | venv ਨੂੰ ਚਾਲੂ ਕਰੋ ਅਤੇ deps ਨੂੰ ਦੁਬਾਰਾ ਇੰਸਟਾਲ ਕਰੋ |
| ਉੱਚੀ ਲੈਟੈਂਸੀ | ਮਾਡਲ ਹੁਣੇ ਹੀ ਲੋਡ ਕੀਤਾ | ਛੋਟੇ ਪ੍ਰੌਮਪਟ ਸੀਕਵੈਂਸ ਨਾਲ ਗਰਮ ਕਰੋ |

## ਰੈਫਰੈਂਸ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG ਮੁਲਾਂਕਨ (Ragas): https://docs.ragas.io

---

**ਸੈਸ਼ਨ ਦੀ ਮਿਆਦ**: 30 ਮਿੰਟ  
**ਮੁਸ਼ਕਲਾਈ**: ਅਡਵਾਂਸਡ

## ਨਮੂਨਾ ਸਥਿਤੀ ਅਤੇ ਵਰਕਸ਼ਾਪ ਮੈਪਿੰਗ

| ਵਰਕਸ਼ਾਪ ਆਰਟੀਫੈਕਟ | ਸਥਿਤੀ | ਉਦੇਸ਼ | ਡਾਟਾ / ਪ੍ਰੌਮਪਟ ਸਰੋਤ |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | ਆਰਕੀਟੈਕਚਰ ਟੀਮ SLM ਅਤੇ LLM ਦੀ ਤੁਲਨਾ ਕਰ ਰਹੀ ਹੈ ਐਗਜ਼ਿਕਟਿਵ ਸਮਰੀ ਜਨਰੇਟਰ ਲਈ | ਲੈਟੈਂਸੀ + ਟੋਕਨ ਵਰਤੋਂ ਦੇ ਫਰਕ ਨੂੰ ਮਾਪੋ | ਸਿੰਗਲ `COMPARE_PROMPT` env var |
| `chainlit_app.py` (RAG ਡੈਮੋ) | ਅੰਦਰੂਨੀ ਗਿਆਨ ਸਹਾਇਕ ਪ੍ਰੋਟੋਟਾਈਪ | ਘੱਟ ਲੈਕਸਿਕਲ ਰੀਟਰੀਵਲ ਨਾਲ ਛੋਟੇ ਜਵਾਬਾਂ ਨੂੰ ਗ੍ਰਾਊਂਡ ਕਰੋ | ਫਾਈਲ ਵਿੱਚ inline `DOCS` ਸੂਚੀ |
| `webgpu_demo.html` | ਭਵਿੱਖ ਦੇ ਔਨ-ਡਿਵਾਈਸ ਬ੍ਰਾਊਜ਼ਰ ਇੰਫਰੈਂਸ ਪੂਰਵ ਦਰਸ਼ਨ | ਘੱਟ-ਲੈਟੈਂਸੀ ਸਥਾਨਕ ਰਾਊਂਡਟ੍ਰਿਪ + UX ਕਹਾਣੀ ਦਿਖਾਓ | ਸਿਰਫ਼ ਲਾਈਵ ਯੂਜ਼ਰ ਪ੍ਰੌਮਪਟ |

### ਸਥਿਤੀ ਕਹਾਣੀ
ਉਤਪਾਦ ਸੰਗਠਨ ਇੱਕ ਐਗਜ਼ਿਕਟਿਵ ਬ੍ਰੀਫਿੰਗ ਜਨਰੇਟਰ ਚਾਹੁੰਦਾ ਹੈ। ਇੱਕ ਹਲਕਾ SLM (phi‑4‑mini) ਸਮਰੀਆਂ ਤਿਆਰ ਕਰਦਾ ਹੈ; ਇੱਕ ਵੱਡਾ LLM (gpt‑oss‑20b) ਸਿਰਫ਼ ਉੱਚ-ਪ੍ਰਾਥਮਿਕਤਾ ਰਿਪੋਰਟਾਂ ਨੂੰ ਸੁਧਾਰ ਸਕਦਾ ਹੈ। ਸੈਸ਼ਨ ਸਕ੍ਰਿਪਟਾਂ ਅਨੁਭਵ ਲੈਟੈਂਸੀ ਅਤੇ ਟੋਕਨ ਮੈਟ੍ਰਿਕਸ ਨੂੰ ਕੈਪਚਰ ਕਰਦੀਆਂ ਹਨ ਹਾਈਬ੍ਰਿਡ ਡਿਜ਼ਾਈਨ ਨੂੰ ਜਾਇਜ਼ ਠਹਿਰਾਉਣ ਲਈ, ਜਦੋਂ ਕਿ ਚੇਨਲਿਟ ਡੈਮੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਗ੍ਰਾਊਂਡ ਰੀਟਰੀਵਲ ਛੋਟੇ ਮਾਡਲ ਦੇ ਜਵਾਬਾਂ ਨੂੰ ਕਿਵੇਂ ਤਥਯਿਕ ਰੱਖਦਾ ਹੈ। WebGPU ਕਾਨਸੈਪਟ ਪੇਜ ਪੂਰੀ ਤਰ੍ਹਾਂ ਕਲਾਇੰਟ-ਸਾਈਡ ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ ਇੱਕ ਵਿਜ਼ਨ ਪਾਥ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜਦੋਂ ਬ੍ਰਾਊਜ਼ਰ ਤੇਜ਼ੀ ਪੱਕੀ ਹੋ ਜਾਂਦੀ ਹੈ।

### ਘੱਟੋ-ਘੱਟ RAG ਸੰਦਰਭ (ਚੇਨਲਿਟ)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### ਹਾਈਬ੍ਰਿਡ ਡ੍ਰਾਫਟ→ਸੁਧਾਰ ਫਲੋ (ਪਸੂਡੋ)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

ਦੋਵੇਂ ਲੈਟੈਂਸੀ ਕੰਪੋਨੈਂਟਾਂ ਨੂੰ ਟ੍ਰੈਕ ਕਰੋ ਮਿਲੀ ਜੁਲੀ ਔਸਤ ਲਾਗਤ ਦੀ ਰਿਪੋਰਟ ਕਰਨ ਲਈ।

### ਵਿਕਲਪਿਕ ਸੁਧਾਰ

| ਫੋਕਸ | ਸੁਧਾਰ | ਕਿਉਂ | ਅਮਲ ਕਰਨ ਦਾ ਸੰਕੇਤ |
|-------|------------|-----|---------------------|
| ਤੁਲਨਾਤਮਕ ਮੈਟ੍ਰਿਕਸ | ਟੋਕਨ ਵਰਤੋਂ + ਪਹਿਲੇ ਟੋਕਨ ਲੈਟੈਂਸੀ ਨੂੰ ਟ੍ਰੈਕ ਕਰੋ | ਸਮੁੱਚੇ ਪ੍ਰਦਰਸ਼ਨ ਦਾ ਦ੍ਰਿਸ਼ | ਵਧੇਰੇ ਬੈਂਚਮਾਰਕ ਸਕ੍ਰਿਪਟ (ਸੈਸ਼ਨ 3) ਨੂੰ `BENCH_STREAM=1` ਨਾਲ ਵਰਤੋਂ |
| ਹਾਈਬ੍ਰਿਡ ਪਾਈਪਲਾਈਨ | SLM ਡ੍ਰਾਫਟ → LLM ਸੁਧਾਰ | ਲੈਟੈਂਸੀ ਅਤੇ ਲਾਗਤ ਘਟਾਓ | phi-4-mini ਨਾਲ ਜਨਰੇਟ ਕਰੋ, gpt-oss-20b ਨਾਲ ਸਮਰੀ ਸੁਧਾਰ |
| ਸਟ੍ਰੀਮਿੰਗ UI | ਚੇਨਲਿਟ ਵਿੱਚ ਬਿਹਤਰ UX | ਤਰਤੀਬਵਾਰ ਫੀਡਬੈਕ | ਜਦੋਂ ਸਥਾਨਕ ਸਟ੍ਰੀਮਿੰਗ ਉਜਾਗਰ ਹੋਵੇ `stream=True` ਵਰਤੋਂ; ਚੰਕਸ ਨੂੰ ਇਕੱਠਾ ਕਰੋ |
| WebGPU ਕੈਸ਼ਿੰਗ | ਤੇਜ਼ JS ਸ਼ੁਰੂਆਤ | ਰੀਕੰਪਾਇਲ ਓਵਰਹੈੱਡ ਘਟਾਓ | ਕੈਸ਼ ਕੀਤੇ ਸ਼ੇਡਰ ਆਰਟੀਫੈਕਟ (ਭਵਿੱਖ Runtime ਸਮਰੱਥਾ) |
| ਨਿਰਧਾਰਤ QA ਸੈੱਟ | ਨਿਰਪੱਖ ਮਾਡਲ ਤੁਲਨਾ | ਵੈਰੀਅੰਸ ਹਟਾਓ | ਫਿਕਸਡ ਪ੍ਰੌਮਪਟ ਸੂਚੀ + ਮੁਲਾਂਕਨ ਰਨ ਲਈ `temperature=0` |
| ਆਉਟਪੁੱਟ ਸਕੋਰਿੰਗ | ਸਟ੍ਰਕਚਰਡ ਗੁਣਵੱਤਾ ਲੈਂਸ | ਕਹਾਣੀਆਂ ਤੋਂ ਅੱਗੇ ਜਾਓ | ਸਧਾਰਨ ਰੂਬ੍ਰਿਕ: ਸੰਗਠਨ / ਤਥਯਿਕਤਾ / ਸੰਖੇਪਤਾ (1–5) |
| ਊਰਜਾ / ਸੰਸਾਧਨ ਨੋਟਸ | ਕਲਾਸਰੂਮ ਚਰਚਾ | ਵਪਾਰ-ਅੱਪ ਦਿਖਾਓ | OS ਮਾਨੀਟਰ ਵਰਤੋਂ (`foundry system info`, ਟਾਸਕ ਮੈਨੇਜਰ, `nvidia-smi`) + ਬੈਂਚਮਾਰਕ ਸਕ੍ਰਿਪਟ ਆਉਟਪੁੱਟ |
| ਲਾਗਤ ਅਨੁਕਰਣ | ਪ੍ਰੀ-ਕਲਾਉਡ ਜਾਇਜ਼ਾ | ਸਕੇਲਿੰਗ ਦੀ ਯੋਜਨਾ | ਟੋਕਨ ਨੂੰ ਕਲਾਉਡ ਕੀਮਤਾਂ ਨਾਲ ਨਕਸ਼ਾ ਬਣਾਓ TCO ਕਹਾਣੀ ਲਈ |
| ਲੈਟੈਂਸੀ ਡੀਕੰਪੋਜ਼ੀਸ਼ਨ | ਬੋਤਲਨੈਕਸ ਦੀ ਪਛਾਣ ਕਰੋ | ਟੀਕਾ ਲਗਾਓ | ਪ੍ਰੌਮਪਟ ਤਿਆਰੀ, ਬੇਨਤੀ ਭੇਜੋ, ਪਹਿਲਾ ਟੋਕਨ, ਪੂਰੀ ਪੂਰੀਕਰਨ ਨੂੰ ਮਾਪੋ |
| RAG + LLM ਫਾਲਬੈਕ | ਗੁਣਵੱਤਾ ਸੁਰੱਖਿਆ ਜਾਲ | ਮੁਸ਼ਕਲ ਪ੍ਰਸ਼ਨਾਂ ਨੂੰ ਸੁਧਾਰੋ | ਜੇ SLM ਜਵਾਬ ਦੀ ਲੰਬਾਈ < ਥ੍ਰੈਸ਼ਹੋਲਡ ਜਾਂ ਘੱਟ ਭਰੋਸੇਯੋਗ → ਵਧਾਓ |

#### ਉਦਾਹਰਣ ਹਾਈਬ੍ਰਿਡ ਡ੍ਰਾਫਟ/ਸੁਧਾਰ ਪੈਟਰਨ

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### ਲੈਟੈਂਸੀ ਬ੍ਰੇਕਡਾਊਨ ਸਕੈਚ

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

ਨਿਰਪੱਖ ਤੁਲਨਾਵਾਂ ਲਈ ਮਾਡਲਾਂ ਵਿੱਚ ਸਥਿਰ ਮਾਪਣ ਸਹਾਇਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜੋ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।