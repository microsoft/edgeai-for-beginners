<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-12-15T21:20:42+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "kn"
}
-->
# ಸೆಷನ್ 4: ಅಗ್ರಗಣ್ಯ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸಿ – LLMಗಳು, SLMಗಳು ಮತ್ತು ಡಿವೈಸ್‌ನಲ್ಲಿ ಇನ್ಫರೆನ್ಸ್

## ಸಾರಾಂಶ

ಸ್ಥಳೀಯ ಮತ್ತು ಕ್ಲೌಡ್ ಇನ್ಫರೆನ್ಸ್ ಸನ್ನಿವೇಶಗಳಿಗೆ ದೊಡ್ಡ ಭಾಷಾ ಮಾದರಿಗಳು (LLMಗಳು) ಮತ್ತು ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿಗಳನ್ನು (SLMಗಳು) ಹೋಲಿಸಿ. ONNX ರನ್‌ಟೈಮ್ ವೇಗವರ್ಧನೆ, WebGPU ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ ಮತ್ತು ಸಂಯುಕ್ತ RAG ಅನುಭವಗಳನ್ನು ಬಳಸಿಕೊಂಡು ನಿಯೋಜನೆ ಮಾದರಿಗಳನ್ನು ಕಲಿಯಿರಿ. ಸ್ಥಳೀಯ ಮಾದರಿಯೊಂದಿಗೆ Chainlit RAG ಡೆಮೊ ಮತ್ತು ಐಚ್ಛಿಕ OpenWebUI ಅನ್ವೇಷಣೆಯನ್ನು ಒಳಗೊಂಡಿದೆ. ನೀವು WebGPU ಇನ್ಫರೆನ್ಸ್ ಸ್ಟಾರ್ಟರ್ ಅನ್ನು ಹೊಂದಿಸಿ Phi ಮತ್ತು GPT-OSS-20B ಸಾಮರ್ಥ್ಯ ಮತ್ತು ವೆಚ್ಚ/ಕಾರ್ಯಕ್ಷಮತೆ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡುತ್ತೀರಿ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

- **SLM ಮತ್ತು LLM** ಅನ್ನು ವಿಳಂಬ, ಮೆಮೊರಿ, ಗುಣಮಟ್ಟ ಅಕ್ಷಗಳ ಮೇಲೆ **ತೂಕಮಾಡಿ**
- ONNXRuntime ಮತ್ತು (ಬೆಂಬಲಿತಿದ್ದಲ್ಲಿ) WebGPU ಬಳಸಿ ಮಾದರಿಗಳನ್ನು **ನಿಯೋಜಿಸಿ**
- ಬ್ರೌಸರ್ ಆಧಾರಿತ ಇನ್ಫರೆನ್ಸ್ ಅನ್ನು **ನಡೆಗೊಳಿಸಿ** (ಗೌಪ್ಯತೆ-ರಕ್ಷಿಸುವ ಇಂಟರಾಕ್ಟಿವ್ ಡೆಮೊ)
- ಸ್ಥಳೀಯ SLM ಬ್ಯಾಕೆಂಡ್ ಜೊತೆಗೆ Chainlit RAG ಪೈಪ್ಲೈನ್ ಅನ್ನು **ಸಂಯೋಜಿಸಿ**
- ಲಘು ತೂಕದ ಗುಣಮಟ್ಟ + ವೆಚ್ಚ ಹ್ಯೂರಿಸ್ಟಿಕ್ಸ್ ಬಳಸಿ **ಮೌಲ್ಯಮಾಪನ ಮಾಡಿ**

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- ಸೆಷನ್‌ಗಳು 1–3 ಪೂರ್ಣಗೊಂಡಿವೆ
- `chainlit` ಸ್ಥಾಪಿಸಲಾಗಿದೆ (Module08 ಗಾಗಿ `requirements.txt` ನಲ್ಲಿ ಈಗಾಗಲೇ ಇದೆ)
- WebGPU-ಸಮರ್ಥ ಬ್ರೌಸರ್ (Edge / Chrome ಇತ್ತೀಚಿನ ಆವೃತ್ತಿ Windows 11 ನಲ್ಲಿ)
- Foundry Local ಚಾಲನೆಯಲ್ಲಿದೆ (`foundry service status`)

### ಕ್ರಾಸ್-ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಟಿಪ್ಪಣಿಗಳು

Windows ಮುಖ್ಯ ಗುರಿ ಪರಿಸರವಾಗಿಯೇ ಉಳಿದಿದೆ. macOS ಡೆವಲಪರ್‌ಗಳಿಗೆ ಸ್ಥಳೀಯ ಬೈನರಿಗಳನ್ನು ಕಾಯುತ್ತಿರುವವರಿಗೆ:  
1. Windows 11 VM (Parallels / UTM) ಅಥವಾ ದೂರಸ್ಥ Windows ವರ್ಕ್‌ಸ್ಟೇಷನ್‌ನಲ್ಲಿ Foundry Local ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ.  
2. ಸೇವೆಯನ್ನು (ಡೀಫಾಲ್ಟ್ ಪೋರ್ಟ್ 5273) ಬಹಿರಂಗಗೊಳಿಸಿ ಮತ್ತು macOS ನಲ್ಲಿ ಸೆಟ್ ಮಾಡಿ:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. ಹಿಂದಿನ ಸೆಷನ್‌ಗಳಂತೆ Python ವರ್ಚುವಲ್ ಪರಿಸರದ ಹಂತಗಳನ್ನು ಬಳಸಿ.

Chainlit ಸ್ಥಾಪನೆ (ಎರಡೂ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್‌ಗಳು):  
```bash
pip install chainlit
```

## ಡೆಮೊ ಪ್ರಕ್ರಿಯೆ (30 ನಿಮಿಷ)

### 1. Phi (SLM) ಮತ್ತು GPT-OSS-20B (LLM) ಹೋಲಿಕೆ (6 ನಿಮಿಷ)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# ವೇಗದ ಸಾಮರ್ಥ್ಯ ಪರೀಕ್ಷೆಗಳು (ಒಂದು ಬಾರಿ, ಅಸಂವಾದಾತ್ಮಕ)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# ಮೂಲ ಟೋಕನ್ / ವಿಳಂಬ ಪರೀಕ್ಷೆ (ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಕೆಲವು ಬಾರಿ ಪುನರಾವರ್ತನೆ ಮಾಡಿ)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```
  
ಪ್ರತಿಕ್ರಿಯೆಯ ಆಳ, ವಾಸ್ತವಿಕತೆ, ಶೈಲಿಯ ವೈವಿಧ್ಯತೆ, ವಿಳಂಬವನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ.

GPU ಸಕ್ರಿಯಗೊಳಿಸಿದ ನಂತರ ಮತ್ತು CPU-ಮಾತ್ರದ ನಂತರ throughput ಬದಲಾವಣೆಗಳನ್ನು ಗಮನಿಸಿ.

### 3. ಬ್ರೌಸರ್‌ನಲ್ಲಿ WebGPU ಇನ್ಫರೆನ್ಸ್ (6 ನಿಮಿಷ)

ಸ್ಟಾರ್ಟರ್ `04-webgpu-inference` ಅನ್ನು ಹೊಂದಿಸಿ (`samples/04-cutting-edge/webgpu_demo.html` ರಚಿಸಿ):

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
  
ಫೈಲ್ ಅನ್ನು ಬ್ರೌಸರ್‌ನಲ್ಲಿ ತೆರೆಯಿರಿ; ಕಡಿಮೆ ವಿಳಂಬದ ಸ್ಥಳೀಯ ರೌಂಡ್‌ಟ್ರಿಪ್ ಅನ್ನು ಗಮನಿಸಿ.

### 4. Chainlit RAG ಚಾಟ್ ಅಪ್ಲಿಕೇಶನ್ (7 ನಿಮಿಷ)

ಕನಿಷ್ಠ `samples/04-cutting-edge/chainlit_app.py`:

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
    # ಸರಳ ಲೆಕ್ಸಿಕಲ್ ಅಂಕೆಮಾಪನ
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
  
ನಡೆಗೊಳಿಸಿ:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```
  
### 5. ಸ್ಟಾರ್ಟರ್ ಪ್ರಾಜೆಕ್ಟ್: `04-webgpu-inference` ಅನ್ನು ಹೊಂದಿಸಿ (6 ನಿಮಿಷ)

ವಿತರಣಾ ವಿಷಯಗಳು:  
- ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್ ಫೆಚ್ ಲಾಜಿಕ್ ಅನ್ನು ಸ್ಟ್ರೀಮಿಂಗ್ ಟೋಕನ್‌ಗಳೊಂದಿಗೆ ಬದಲಾಯಿಸಿ (`stream=True` ಎಂಡ್ಪಾಯಿಂಟ್ ವೈರಿಯಂಟ್ ಸಕ್ರಿಯಗೊಳಿಸಿದ ನಂತರ ಬಳಸಿ)  
- phi ಮತ್ತು gpt-oss-20b ಟಾಗಲ್‌ಗಳಿಗಾಗಿ ವಿಳಂಬ ಚಾರ್ಟ್ (ಕ್ಲೈಂಟ್-ಸೈಡ್) ಸೇರಿಸಿ  
- RAG ಸಾಂದರ್ಭಿಕ ಮಾಹಿತಿಯನ್ನು ಇನ್‌ಲೈನ್‌ನಲ್ಲಿ (ಉಲ್ಲೇಖ ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳಿಗಾಗಿ ಟೆಕ್ಸ್ಟ್‌ಎರಿಯಾ) ನೇರವಾಗಿ ಸೇರಿಸಿ

## ಮೌಲ್ಯಮಾಪನ ಹ್ಯೂರಿಸ್ಟಿಕ್ಸ್

| ವರ್ಗ | Phi-4-mini | GPT-OSS-20B | ಗಮನಿಕೆ |
|----------|------------|-------------|-------------|
| ವಿಳಂಬ (ತಣಿದ) | ವೇಗವಾಗಿ | ನಿಧಾನವಾಗಿ | SLM ತ್ವರಿತವಾಗಿ ಬಿಸಿಯಾಗುತ್ತದೆ |
| ಮೆಮೊರಿ | ಕಡಿಮೆ | ಹೆಚ್ಚು | ಸಾಧನ ಸಾಧ್ಯತೆ |
| ಸಾಂದರ್ಭಿಕ ಅನುಸರಣೆ | ಉತ್ತಮ | ಬಲವಾದ | ದೊಡ್ಡ ಮಾದರಿ ಹೆಚ್ಚು ವಿವರಣಾತ್ಮಕವಾಗಿರಬಹುದು |
| ವೆಚ್ಚ (ಸ್ಥಳೀಯ) | ಕನಿಷ್ಠ | ಹೆಚ್ಚು (ಸಂಪನ್ಮೂಲ) | ಶಕ್ತಿ/ಸಮಯ ವ್ಯತ್ಯಾಸ |
| ಉತ್ತಮ ಬಳಕೆ ಪ್ರಕರಣ | ಎಡ್ಜ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು | ಆಳವಾದ ತರ್ಕ | ಸಂಯುಕ್ತ ಪೈಪ್ಲೈನ್ ಸಾಧ್ಯ |

## ಪರಿಸರ ಪರಿಶೀಲನೆ

```powershell
# ಪಟ್ಟಿಯ ಕ್ಯಾಟಲಾಗ್ (ನಡೆಸುತ್ತಿರುವ ಫ್ಲ್ಯಾಗ್ ಇಲ್ಲ; ಲೋಡ್ ಮಾಡಲಾದ ಮಾದರಿಗಳು ನೀವು ಹಿಂದಿನ ಬಾರಿ ಚಾಲನೆ ಮಾಡಿದವು)
foundry model list

# ರನ್‌ಟೈಮ್ ಮೆಟ್ರಿಕ್ಸ್‌ಗಾಗಿ Python ಬೆಂಚ್‌ಮಾರ್ಕ್ ಸ್ಕ್ರಿಪ್ಟ್ (ಸೆಷನ್ 3) ಮತ್ತು OS ಉಪಕರಣಗಳನ್ನು (ಟಾಸ್ಕ್ ಮ್ಯಾನೇಜರ್ / nvidia-smi) 'ಮಾದರಿ ಅಂಕಿಅಂಶಗಳು' ಬದಲು ಬಳಸಿ
# ಉದಾಹರಣೆ:
#   cd ವರ್ಕ್‌ಶಾಪ್/ಸ್ಯಾಂಪಲ್ಸ್
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```
  
## ಸಮಸ್ಯೆ ಪರಿಹಾರ

| ಲಕ್ಷಣ | ಕಾರಣ | ಕ್ರಮ |
|---------|-------|--------|
| ವೆಬ್ ಪುಟ ಫೆಚ್ ವಿಫಲ | CORS ಅಥವಾ ಸೇವೆ ಡೌನ್ | ಎಂಡ್ಪಾಯಿಂಟ್ ಪರಿಶೀಲಿಸಲು `curl` ಬಳಸಿ; ಅಗತ್ಯವಿದ್ದರೆ CORS ಪ್ರಾಕ್ಸಿ ಸಕ್ರಿಯಗೊಳಿಸಿ |
| Chainlit ಖಾಲಿ | ಪರಿಸರ ಸಕ್ರಿಯವಿಲ್ಲ | ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ಸಕ್ರಿಯಗೊಳಿಸಿ ಮತ್ತು ಅವಲಂಬನೆಗಳನ್ನು ಮರುಸ್ಥಾಪಿಸಿ |
| ಹೆಚ್ಚಿನ ವಿಳಂಬ | ಮಾದರಿ ಇತ್ತೀಚೆಗೆ ಲೋಡ್ ಆಗಿದೆ | ಸಣ್ಣ ಪ್ರಾಂಪ್ಟ್ ಸರಣಿಯಿಂದ ಬಿಸಿಯಾಗಿಸಿ |

## ಉಲ್ಲೇಖಗಳು

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Chainlit ಡಾಕ್ಯುಮೆಂಟೇಶನ್: https://docs.chainlit.io  
- RAG ಮೌಲ್ಯಮಾಪನ (Ragas): https://docs.ragas.io

---

**ಸೆಷನ್ ಅವಧಿ**: 30 ನಿಮಿಷ  
**ಕಷ್ಟದ ಮಟ್ಟ**: ಉನ್ನತ

## ಮಾದರಿ ಸನ್ನಿವೇಶ ಮತ್ತು ಕಾರ್ಯಾಗಾರ ನಕ್ಷೆ

| ಕಾರ್ಯಾಗಾರ ವಸ್ತುಗಳು | ಸನ್ನಿವೇಶ | ಉದ್ದೇಶ | ಡೇಟಾ / ಪ್ರಾಂಪ್ಟ್ ಮೂಲ |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | ಕಾರ್ಯನಿರ್ವಹಣಾ ತಂಡ SLM ಮತ್ತು LLM ಅನ್ನು ಕಾರ್ಯನಿರ್ವಾಹಕ ಸಾರಾಂಶ ಜನರೇಟರ್ ಗಾಗಿ ಮೌಲ್ಯಮಾಪನ ಮಾಡುತ್ತಿದೆ | ವಿಳಂಬ ಮತ್ತು ಟೋಕನ್ ಬಳಕೆಯ ವ್ಯತ್ಯಾಸವನ್ನು ಪ್ರಮಾಣೀಕರಿಸಿ | ಏಕೈಕ `COMPARE_PROMPT` ಪರಿಸರ ಚರ |
| `chainlit_app.py` (RAG ಡೆಮೊ) | ಆಂತರಿಕ ಜ್ಞಾನ ಸಹಾಯಕ ಪ್ರೋಟೋಟೈಪ್ | ಕನಿಷ್ಠ ಶಬ್ದ ಸಂಗ್ರಹಣೆಯೊಂದಿಗೆ ಸಣ್ಣ ಉತ್ತರಗಳನ್ನು ನೆಲಸಿರಿ | ಫೈಲ್‌ನಲ್ಲಿ ಇನ್‌ಲೈನ್ `DOCS` ಪಟ್ಟಿ |
| `webgpu_demo.html` | ಭವಿಷ್ಯತ್ಮಕ ಡಿವೈಸ್-ಆಧಾರಿತ ಬ್ರೌಸರ್ ಇನ್ಫರೆನ್ಸ್ ಪೂರ್ವದೃಶ್ಯ | ಕಡಿಮೆ ವಿಳಂಬದ ಸ್ಥಳೀಯ ರೌಂಡ್‌ಟ್ರಿಪ್ ಮತ್ತು ಬಳಕೆದಾರ ಅನುಭವವನ್ನು ತೋರಿಸಿ | ಲೈವ್ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಮಾತ್ರ |

### ಸನ್ನಿವೇಶ ಕಥನ  
ಉತ್ಪನ್ನ ಸಂಘಟನೆ ಕಾರ್ಯನಿರ್ವಹಣಾ ಸಂಕ್ಷಿಪ್ತ ವರದಿ ಜನರೇಟರ್ ಅನ್ನು ಬಯಸುತ್ತದೆ. ಲಘು ತೂಕದ SLM (phi-4-mini) ಸಾರಾಂಶಗಳನ್ನು ರಚಿಸುತ್ತದೆ; ದೊಡ್ಡ LLM (gpt-oss-20b) ಕೇವಲ ಉನ್ನತ ಪ್ರಾಥಮಿಕತೆಯ ವರದಿಗಳನ್ನು ಸುಧಾರಿಸುತ್ತದೆ. ಸೆಷನ್ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು ಸಂಯುಕ್ತ ವಿನ್ಯಾಸವನ್ನು ನ್ಯಾಯಸಮ್ಮತಗೊಳಿಸಲು ಅನುಭವಾತ್ಮಕ ವಿಳಂಬ ಮತ್ತು ಟೋಕನ್ ಅಳತೆಗಳನ್ನು ಸೆರೆಹಿಡಿಯುತ್ತವೆ, Chainlit ಡೆಮೊ ಸಣ್ಣ ಮಾದರಿ ಉತ್ತರಗಳನ್ನು ವಾಸ್ತವಿಕವಾಗಿರಿಸಲು ನೆಲಸುವ retrieval ಅನ್ನು ತೋರಿಸುತ್ತದೆ. WebGPU ಕಲ್ಪನೆ ಪುಟವು ಬ್ರೌಸರ್ ವೇಗವರ್ಧನೆ ಬೆಳೆಯುವಾಗ ಸಂಪೂರ್ಣ ಕ್ಲೈಂಟ್-ಸೈಡ್ ಪ್ರಕ್ರಿಯೆಗೆ ದೃಷ್ಟಿ ಮಾರ್ಗವನ್ನು ಒದಗಿಸುತ್ತದೆ.

### ಕನಿಷ್ಠ RAG ಸಾಂದರ್ಭಿಕ (Chainlit)  
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```
  
### ಸಂಯುಕ್ತ ಡ್ರಾಫ್ಟ್→ಸುಧಾರಣೆ ಪ್ರಕ್ರಿಯೆ (ಅರ್ಧಸತ್ಯ)  
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: ದೀರ್ಘ ಬ್ರೀಫ್ಗಳು ಅಥವಾ ಧ್ವಜಸೂಚಿತ ವಿಷಯಗಳಿಗೆ ಮಾತ್ರ ಹೆಚ್ಚಿಸುವುದು
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```
  
ಮಿಶ್ರ ಸರಾಸರಿ ವೆಚ್ಚವನ್ನು ವರದಿ ಮಾಡಲು ಎರಡೂ ವಿಳಂಬ ಘಟಕಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ.

### ಐಚ್ಛಿಕ ಸುಧಾರಣೆಗಳು

| ಗಮನ | ಸುಧಾರಣೆ | ಕಾರಣ | ಅನುಷ್ಠಾನ ಸೂಚನೆ |
|-------|------------|-----|---------------------|
| ಹೋಲಿಕೆ ಮೌಲ್ಯಗಳು | ಟೋಕನ್ ಬಳಕೆ + ಮೊದಲ ಟೋಕನ್ ವಿಳಂಬವನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ | ಸಮಗ್ರ ಕಾರ್ಯಕ್ಷಮತೆ ದೃಷ್ಟಿಕೋನ | ಸುಧಾರಿತ ಬೆಂಚ್‌ಮಾರ್ಕ್ ಸ್ಕ್ರಿಪ್ಟ್ (ಸೆಷನ್ 3) ನಲ್ಲಿ `BENCH_STREAM=1` ಬಳಸಿ |
| ಸಂಯುಕ್ತ ಪೈಪ್ಲೈನ್ | SLM ಡ್ರಾಫ್ಟ್ → LLM ಸುಧಾರಣೆ | ವಿಳಂಬ ಮತ್ತು ವೆಚ್ಚ ಕಡಿಮೆಮಾಡಿ | phi-4-mini ಬಳಸಿ ರಚಿಸಿ, gpt-oss-20b ಮೂಲಕ ಸಾರಾಂಶ ಸುಧಾರಿಸಿ |
| ಸ್ಟ್ರೀಮಿಂಗ್ UI | Chainlit ನಲ್ಲಿ ಉತ್ತಮ UX | ಕ್ರಮೇಣ ಪ್ರತಿಕ್ರಿಯೆ | ಸ್ಥಳೀಯ ಸ್ಟ್ರೀಮಿಂಗ್ ಸಕ್ರಿಯಗೊಳಿಸಿದ ನಂತರ `stream=True` ಬಳಸಿ; ತುಂಡುಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ |
| WebGPU ಕ್ಯಾಶಿಂಗ್ | ವೇಗವಾದ JS ಪ್ರಾರಂಭ | ಮರುಸಂಯೋಜನೆ ವೆಚ್ಚ ಕಡಿಮೆಮಾಡಿ | ಸಂಯೋಜಿತ ಶೇಡರ್ ಕಲೆಗಳನ್ನು ಕ್ಯಾಶ್ ಮಾಡಿ (ಭವಿಷ್ಯದ ರನ್‌ಟೈಮ್ ಸಾಮರ್ಥ್ಯ) |
| ನಿರ್ಧಾರಾತ್ಮಕ QA ಸೆಟ್ | ನ್ಯಾಯಸಮ್ಮತ ಮಾದರಿ ಹೋಲಿಕೆ | ವ್ಯತ್ಯಾಸವನ್ನು ತೆಗೆದುಹಾಕಿ | ಸ್ಥಿರ ಪ್ರಾಂಪ್ಟ್ ಪಟ್ಟಿ + ಮೌಲ್ಯಮಾಪನ ಓಟಗಳಿಗೆ `temperature=0` |
| ಔಟ್‌ಪುಟ್ ಸ್ಕೋರಿಂಗ್ | ರಚನಾತ್ಮಕ ಗುಣಮಟ್ಟ ಲೆನ್ಸ್ | ಕಥನಾತ್ಮಕತೆ ಮೀರಿ ಹೋಗಿ | ಸರಳ ರೂಬ್ರಿಕ್: ಸಮ್ಮಿಲನ / ವಾಸ್ತವಿಕತೆ / ಸಂಕ್ಷಿಪ್ತತೆ (1–5) |
| ಶಕ್ತಿ / ಸಂಪನ್ಮೂಲ ಟಿಪ್ಪಣಿಗಳು | ತರಗತಿ ಚರ್ಚೆ | ವ್ಯತ್ಯಾಸಗಳನ್ನು ತೋರಿಸಿ | OS ಮಾನಿಟರ್‌ಗಳು (ಟಾಸ್ಕ್ ಮ್ಯಾನೇಜರ್, `nvidia-smi`) + ಬೆಂಚ್‌ಮಾರ್ಕ್ ಸ್ಕ್ರಿಪ್ಟ್ ಔಟ್‌ಪುಟ್‌ಗಳು |
| ವೆಚ್ಚ ಅನುಕರಣೆ | ಪೂರ್ವ-ಕ್ಲೌಡ್ ನ್ಯಾಯಸಮ್ಮತತೆ | ವಿಸ್ತರಣಾ ಯೋಜನೆ | ಟೋಕನ್‌ಗಳನ್ನು ಕಲ್ಪಿತ ಕ್ಲೌಡ್ ಬೆಲೆಗೆ ನಕ್ಷೆ ಮಾಡಿ TCO ಕಥನಕ್ಕಾಗಿ |
| ವಿಳಂಬ ವಿಭಜನೆ | ಬಾಟಲ್‌ನೆಕ್ ಗುರುತಿಸಿ | ಗುರಿ ಸುಧಾರಣೆಗಳು | ಪ್ರಾಂಪ್ಟ್ ತಯಾರಿ, ವಿನಂತಿ ಕಳುಹಿಸುವಿಕೆ, ಮೊದಲ ಟೋಕನ್, ಪೂರ್ಣ ಮುಗింపు ಅಳತೆ ಮಾಡಿ |
| RAG + LLM ಬ್ಯಾಕಪ್ | ಗುಣಮಟ್ಟ ಸುರಕ್ಷತಾ ಜಾಲಿ | ಕಠಿಣ ಪ್ರಶ್ನೆಗಳನ್ನು ಸುಧಾರಿಸಿ | SLM ಉತ್ತರದ ಉದ್ದ < ಮಿತಿ ಅಥವಾ ಕಡಿಮೆ ವಿಶ್ವಾಸ → ಏರಿಕೆ ಮಾಡಿ |

#### ಉದಾಹರಣೆಯ ಸಂಯುಕ್ತ ಡ್ರಾಫ್ಟ್/ಸುಧಾರಣೆ ಮಾದರಿ

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```
  
#### ವಿಳಂಬ ವಿಭಜನೆ ರೇಖಾಚಿತ್ರ

```python
import time
t0 = time.time(); # ಸಂದೇಶಗಳನ್ನು ನಿರ್ಮಿಸಿ
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```
  
ನ್ಯಾಯಸಮ್ಮತ ಹೋಲಿಕೆಗಾಗಿ ಮಾದರಿಗಳಾದ್ಯಂತ ಸತತ ಅಳತೆ ಸೌಲಭ್ಯವನ್ನು ಬಳಸಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->