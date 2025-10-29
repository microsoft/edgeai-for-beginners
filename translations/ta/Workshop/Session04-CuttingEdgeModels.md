<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T23:51:24+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "ta"
}
-->
# அமர்வு 4: முன்னணி மாதிரிகளை ஆராயுங்கள் – LLMs, SLMs மற்றும் சாதனத்தில் உள்ள தீர்மானம்

## சுருக்கம்

பெரிய மொழி மாதிரிகள் (LLMs) மற்றும் சிறிய மொழி மாதிரிகள் (SLMs) இடையே உள்ள வித்தியாசங்களை உள்ளூர் மற்றும் மேக தீர்மான சூழல்களில் ஒப்பிடுங்கள். ONNX Runtime வேகத்தை அதிகரித்தல், WebGPU செயல்பாடு மற்றும் கலப்பு RAG அனுபவங்களை பயன்படுத்தி முறைமைகளை அறிக. உள்ளூர் மாதிரியுடன் ஒரு Chainlit RAG டெமோ மற்றும் விருப்பமான OpenWebUI ஆராய்ச்சியுடன் சேர்க்கப்பட்டுள்ளது. WebGPU தீர்மான தொடக்கத்தை மாற்றி Phi மற்றும் GPT-OSS-20B திறன் மற்றும் செலவு/செயல்திறன் சமநிலைகளை மதிப்பீடு செய்யுங்கள்.

## கற்றல் நோக்கங்கள்

- **SLM மற்றும் LLM** இடையே தாமதம், நினைவகம், தரம் ஆகியவற்றில் வித்தியாசங்களை ஒப்பிடுங்கள்
- ONNXRuntime மற்றும் (ஆதரவு அளிக்கப்படும் இடங்களில்) WebGPU மூலம் மாதிரிகளை **விநியோகிக்கவும்**
- **உலாவியில் அடிப்படையிலான தீர்மானம்** (தனியுரிமை பாதுகாக்கும் இடைமுக டெமோ) இயக்கவும்
- உள்ளூர் SLM பின்புலத்துடன் Chainlit RAG குழாய் **ஒன்றிணைக்கவும்**
- எளிய தரம் + செலவு ஹியூரிஸ்டிக்ஸ் பயன்படுத்தி **மதிப்பீடு செய்யவும்**

## முன் தேவைகள்

- அமர்வுகள் 1–3 முடிக்கப்பட்டது
- `chainlit` நிறுவப்பட்டுள்ளது (`requirements.txt` இல் Module08 க்கானது)
- WebGPU-க்கு திறன் வாய்ந்த உலாவி (Windows 11 இல் Edge / Chrome சமீபத்தியது)
- Foundry Local இயங்குகிறது (`foundry status`)

### குறுக்குவெளி குறிப்புகள்

Windows முதன்மை இலக்கு சூழலமாக உள்ளது. macOS டெவலப்பர்கள் இயற்கை பைனரிகளை காத்திருக்கும்போது:
1. Foundry Local ஐ Windows 11 VM (Parallels / UTM) அல்லது ஒரு தொலை Windows வேலைநிலையத்தில் இயக்கவும்.
2. சேவையை (இயல்புநிலை துறைமுகம் 5273) வெளிப்படுத்தி macOS இல் அமைக்கவும்:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. முந்தைய அமர்வுகளின் போல Python மெய்நிகர் சூழல் படிகளைப் பயன்படுத்தவும்.

Chainlit நிறுவல் (இரு தளங்களிலும்):
```bash
pip install chainlit
```

## டெமோ ஓட்டம் (30 நிமிடம்)

### 1. Phi (SLM) மற்றும் GPT-OSS-20B (LLM) ஐ ஒப்பிடுங்கள் (6 நிமிடம்)

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

பின்தொடரவும்: பதில் ஆழம், உண்மையான துல்லியம், பாணி செறிவு, தாமதம்.

### 2. ONNX Runtime வேகத்தை அதிகரித்தல் (5 நிமிடம்)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

GPU ஐ இயக்கிய பிறகு throughput மாற்றங்களை கவனிக்கவும், CPU மட்டும்.

### 3. உலாவியில் WebGPU தீர்மானம் (6 நிமிடம்)

தொடக்க `04-webgpu-inference` ஐ மாற்றவும் (`samples/04-cutting-edge/webgpu_demo.html` உருவாக்கவும்):

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

கோப்பை உலாவியில் திறக்கவும்; குறைந்த தாமத உள்ளூர் சுற்றுப்பயணத்தை கவனிக்கவும்.

### 4. Chainlit RAG உரையாடல் பயன்பாடு (7 நிமிடம்)

குறைந்த `samples/04-cutting-edge/chainlit_app.py`:

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

இயக்கவும்:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. தொடக்க திட்டம்: `04-webgpu-inference` ஐ மாற்றவும் (6 நிமிடம்)

விநியோகங்கள்:
- placeholder fetch logic ஐ streaming tokens மூலம் மாற்றவும் (`stream=True` இறுதிப்புள்ளி மாறுபாடு இயக்கப்பட்டவுடன் பயன்படுத்தவும்)
- latency வரைபடத்தை (வாடிக்கையாளர் பக்கம்) phi மற்றும் gpt-oss-20b மாற்றங்களுக்கு சேர்க்கவும்
- RAG சூழலை inline சேர்க்கவும் (reference docs க்கான textarea)

## மதிப்பீட்டு ஹியூரிஸ்டிக்ஸ்

| வகை | Phi-4-mini | GPT-OSS-20B | கவனிக்கவும் |
|----------|------------|-------------|-------------|
| தாமதம் (குளிர்) | வேகமாக | மெதுவாக | SLM விரைவாக சூடாகிறது |
| நினைவகம் | குறைவு | அதிகம் | சாதன சாத்தியமுள்ளது |
| சூழல் பின்பற்றுதல் | நல்லது | வலுவானது | பெரிய மாதிரி அதிகமாக விவரிக்கலாம் |
| செலவு (உள்ளூர்) | குறைந்தது | அதிகம் (வளங்கள்) | ஆற்றல்/நேர சமநிலை |
| சிறந்த பயன்பாட்டு வழக்கு | Edge பயன்பாடுகள் | ஆழமான காரணம் | கலப்பு குழாய் சாத்தியம் |

## சூழலை சரிபார்த்தல்

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## சிக்கல்களை சரிசெய்தல்

| அறிகுறி | காரணம் | நடவடிக்கை |
|---------|-------|--------|
| வலைப்பக்கம் fetch தோல்வி | CORS அல்லது சேவை முடங்கியது | இறுதிப்புள்ளியை சரிபார்க்க `curl` ஐ பயன்படுத்தவும்; CORS proxy ஐ இயக்கவும் |
| Chainlit வெற்று | சூழல் செயல்படவில்லை | venv ஐ இயக்கவும் & dependencies ஐ மீண்டும் நிறுவவும் |
| அதிக தாமதம் | மாதிரி புதிதாக ஏற்றப்பட்டது | சிறிய prompt வரிசையுடன் சூடாக்கவும் |

## குறிப்புகள்

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG மதிப்பீடு (Ragas): https://docs.ragas.io

---

**அமர்வு காலம்**: 30 நிமிடம்  
**கடினம்**: மேம்பட்டது

## மாதிரி சூழல் & பணிக்கூடம் வரைபடம்

| பணிக்கூடக் கலைப்பொருட்கள் | சூழல் | நோக்கம் | தரவு / Prompt மூலங்கள் |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | நிர்வாக சுருக்கம் உருவாக்குவதற்கான கட்டமைப்பு குழு SLM மற்றும் LLM ஐ மதிப்பீடு செய்கிறது | தாமதம் + token பயன்பாட்டு வேறுபாட்டை அளவிடுங்கள் | ஒற்றை `COMPARE_PROMPT` சூழல் மாறி |
| `chainlit_app.py` (RAG டெமோ) | உள்துறை அறிவு உதவியாளர் மாதிரி | குறைந்த சொற்களால் பதில்களை தரவுகளுடன் நிலைநிறுத்துங்கள் | கோப்பில் உள்ள inline `DOCS` பட்டியல் |
| `webgpu_demo.html` | சாதனத்தில் உள்ள உலாவி தீர்மான முன்னோட்டம் | குறைந்த தாமத உள்ளூர் சுற்றுப்பயணம் + UX கதை | நேரடி பயனர் prompt மட்டும் |

### சூழல் கதை
தயாரிப்பு அமைப்பு நிர்வாக சுருக்கம் உருவாக்குபவரை விரும்புகிறது. ஒரு எளிய SLM (phi‑4‑mini) சுருக்கங்களை உருவாக்குகிறது; ஒரு பெரிய LLM (gpt‑oss‑20b) முக்கியமான அறிக்கைகளை மட்டுமே மேம்படுத்தலாம். அமர்வு ஸ்கிரிப்ட்கள் கலப்பு வடிவமைப்பை நியாயப்படுத்துவதற்கான உண்மையான தாமதம் மற்றும் token அளவீடுகளைப் பிடிக்கின்றன, அதே நேரத்தில் Chainlit டெமோ சிறிய மாதிரி பதில்களை உண்மையாக வைத்திருக்க நிலைநிறுத்தப்பட்ட மீட்பை எப்படி விளக்குகிறது என்பதை காட்டுகிறது. WebGPU கருத்து பக்கம் உலாவி வேகத்தை மேம்படுத்தும் போது முழுமையான வாடிக்கையாளர் பக்கம் செயலாக்கத்திற்கான பார்வை பாதையை வழங்குகிறது.

### குறைந்த RAG சூழல் (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### கலப்பு வரைவு→மேம்படுத்தல் ஓட்டம் (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

இரண்டு தாமத கூறுகளையும் கண்காணித்து கலந்த சராசரி செலவைப் பதிவு செய்யுங்கள்.

### விருப்ப மேம்பாடுகள்

| கவனம் | மேம்பாடு | ஏன் | செயல்படுத்தல் குறிப்புகள் |
|-------|------------|-----|---------------------|
| ஒப்பீட்டு அளவீடுகள் | token பயன்பாடு + முதல்-token தாமதத்தை கண்காணிக்கவும் | முழுமையான செயல்திறன் பார்வை | மேம்படுத்தப்பட்ட அளவீட்டு ஸ்கிரிப்டை (அமர்வு 3) `BENCH_STREAM=1` உடன் பயன்படுத்தவும் |
| கலப்பு குழாய் | SLM வரைவு → LLM மேம்பாடு | தாமதம் மற்றும் செலவை குறைக்கவும் | phi-4-mini மூலம் உருவாக்கவும், gpt-oss-20b மூலம் சுருக்கத்தை மேம்படுத்தவும் |
| Streaming UI | Chainlit இல் சிறந்த UX | படிப்படியாக கருத்து | உள்ளூர் streaming வெளிப்படுத்தப்பட்டவுடன் `stream=True` ஐ பயன்படுத்தவும்; துண்டுகளை சேர்க்கவும் |
| WebGPU காட்சிப்படுத்தல் | JS தொடக்கத்தை வேகமாக்கவும் | மீண்டும் தொகுப்பு மேலதிகத்தை குறைக்கவும் | தொகுக்கப்பட்ட shader கலைப்பொருட்களை cache செய்யவும் (எதிர்கால runtime திறன்) |
| தீர்மான QA தொகுப்பு | நியாயமான மாதிரி ஒப்பீடு | மாறுபாட்டை நீக்கவும் | நிலையான prompt பட்டியல் + `temperature=0` மதிப்பீட்டு ஓட்டங்களுக்கு |
| வெளியீட்டு மதிப்பீடு | அமைப்பான தரக்கண்ணோட்டம் | அனுபவங்களை மீறவும் | எளிய அளவுகோல்: coherence / factuality / brevity (1–5) |
| ஆற்றல் / வள குறிப்புகள் | வகுப்பறை விவாதம் | சமநிலைகளை காட்டவும் | OS கண்காணிப்புகளை (`foundry system info`, Task Manager, `nvidia-smi`) + அளவீட்டு ஸ்கிரிப்ட் வெளியீடுகளைப் பயன்படுத்தவும் |
| செலவு கற்பனை | மேக நியாயப்படுத்தல் | அளவீட்டு திட்டமிடல் | TCO கதைப்பாட்டிற்கான hypothetical மேக விலை நிர்ணயத்திற்கு tokens ஐ வரைபடம் |
| தாமத சிதைவம் | bottlenecks ஐ அடையாளம் காணவும் | மேம்பாடுகளை இலக்கு | prompt தயாரிப்பு, கோரிக்கை அனுப்புதல், முதல் token, முழு முடிவு ஆகியவற்றை அளவிடுங்கள் |
| RAG + LLM fallback | தரக் பாதுகாப்பு வலை | கடினமான கேள்விகளை மேம்படுத்தவும் | SLM பதில் நீளம் < வரம்பு அல்லது குறைந்த நம்பிக்கை → escalate |

#### உதாரண கலப்பு வரைவு/மேம்படுத்தல் முறை

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### தாமத சிதைவின் வரைபடம்

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

நியாயமான ஒப்பீடுகளுக்காக மாதிரிகள் முழுவதும் ஒரே அளவீட்டு அமைப்புகளைப் பயன்படுத்தவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள அசல் ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.