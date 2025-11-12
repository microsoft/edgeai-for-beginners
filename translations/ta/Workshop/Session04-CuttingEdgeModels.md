<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-12T00:55:23+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "ta"
}
-->
# அமர்வு 4: முன்னணி மாடல்களை ஆராயுங்கள் – LLMs, SLMs மற்றும் சாதனத்தில் தீர்மானம்

## சுருக்கம்

பெரிய மொழி மாடல்கள் (LLMs) மற்றும் சிறிய மொழி மாடல்கள் (SLMs) இடையே உள்ள வித்தியாசங்களை உள்ளூர் மற்றும் மேக தீர்மான சூழல்களில் ஒப்பிடுங்கள். ONNX Runtime வேகத்தை, WebGPU செயல்பாட்டை மற்றும் கலப்பு RAG அனுபவங்களை பயன்படுத்தி மாடல்களை செயல்படுத்தும் முறைகளை கற்றுக்கொள்ளுங்கள். உள்ளூர் மாடலுடன் ஒரு Chainlit RAG டெமோ மற்றும் விருப்பமான OpenWebUI ஆராய்ச்சியை உள்ளடக்கியது. WebGPU தீர்மான தொடக்கத்தை மாற்றி Phi மற்றும் GPT-OSS-20B திறன் மற்றும் செலவு/செயல்திறன் சமநிலைகளை மதிப்பீடு செய்யுங்கள்.

## கற்றல் நோக்கங்கள்

- **SLM மற்றும் LLM** இடையே தாமதம், நினைவகம், தரம் ஆகியவற்றில் வித்தியாசங்களை ஒப்பிடுங்கள்
- **ONNXRuntime மற்றும் (ஆதரவு உள்ள இடங்களில்) WebGPU** மூலம் மாடல்களை செயல்படுத்துங்கள்
- **உலாவியில் அடிப்படையிலான தீர்மானம்** (தனியுரிமை பாதுகாக்கும் இடைமுக டெமோ) இயக்குங்கள்
- **Chainlit RAG குழாய்** ஒன்றை உள்ளூர் SLM பின்புலத்துடன் ஒருங்கிணைக்கவும்
- **இலகுவான தரம் + செலவு மதிப்பீடுகளை** பயன்படுத்தி மதிப்பீடு செய்யுங்கள்

## முன் தேவைகள்

- அமர்வுகள் 1–3 முடிக்கப்பட்டது
- `chainlit` நிறுவப்பட்டுள்ளது (`requirements.txt` இல் Module08 க்கானது)
- WebGPU-க்கு திறன் வாய்ந்த உலாவி (Windows 11 இல் Edge / Chrome சமீபத்தியது)
- Foundry Local இயங்குகிறது (`foundry service status`)

### குறுக்குவெளி குறிப்புகள்

Windows முதன்மை இலக்கு சூழலாக உள்ளது. macOS டெவலப்பர்கள் இயல்பான பைனரிகளை காத்திருக்கும்போது:
1. Foundry Local ஐ Windows 11 VM (Parallels / UTM) அல்லது ஒரு தொலை Windows வேலைநிலையத்தில் இயக்கவும்.
2. சேவையை (இயல்புநிலை துறைமுகம் 5273) வெளிப்படுத்தி macOS இல் அமைக்கவும்:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. முந்தைய அமர்வுகளின் Python மெய்நிகர் சூழல் படிகளைப் பயன்படுத்தவும்.

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

பின்தொடரவும்: பதிலளிப்பு ஆழம், உண்மையான துல்லியம், பாணி செறிவு, தாமதம்.

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

குறைந்தபட்ச `samples/04-cutting-edge/chainlit_app.py`:

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

வழங்கல்:
- பிளேஸ்ஹோல்டர் fetch தார்மீகத்தை ஸ்ட்ரீமிங் டோக்கன்களுடன் மாற்றவும் (`stream=True` இறுதிப்புள்ளி மாறுபாட்டைப் பயன்படுத்தவும்)
- தாமத வரைபடத்தை (வாடிக்கையாளர் பக்கம்) phi மற்றும் gpt-oss-20b மாற்றங்களுக்காகச் சேர்க்கவும்
- RAG சூழலை நேரடியாக இணைக்கவும் (குறிப்பு ஆவணங்களுக்கான textarea)

## மதிப்பீட்டு ஹியூரிஸ்டிக்ஸ்

| வகை | Phi-4-mini | GPT-OSS-20B | கவனிப்பு |
|------|------------|-------------|-----------|
| தாமதம் (குளிர்) | வேகமாக | மெதுவாக | SLM விரைவாக சூடாகிறது |
| நினைவகம் | குறைந்தது | அதிகம் | சாதன சாத்தியம் |
| சூழல் பின்பற்றல் | நல்லது | வலுவானது | பெரிய மாடல் அதிகமாக விவரிக்கலாம் |
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
|---------|--------|-----------|
| வலைப்பக்கம் fetch தோல்வி | CORS அல்லது சேவை முடங்கியது | இறுதிப்புள்ளியை சரிபார்க்க `curl` ஐப் பயன்படுத்தவும்; CORS proxy ஐ இயக்கவும் |
| Chainlit வெற்று | சூழல் செயல்படவில்லை | venv ஐ செயல்படுத்தி தேவைகளை மீண்டும் நிறுவவும் |
| அதிக தாமதம் | மாடல் புதிதாக ஏற்றப்பட்டது | சிறிய prompt வரிசையுடன் சூடாக்கவும் |

## குறிப்புகள்

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit ஆவணங்கள்: https://docs.chainlit.io
- RAG மதிப்பீடு (Ragas): https://docs.ragas.io

---

**அமர்வு காலம்**: 30 நிமிடம்  
**கடினம்**: மேம்பட்டது

## மாதிரி சூழல் & பணிக்கூட்டம் வரைபடம்

| பணிக்கூட்டக் கலைப்பொருட்கள் | சூழல் | நோக்கம் | தரவு / Prompt மூலங்கள் |
|-----------------------------|--------|---------|-------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | நிர்வாக சுருக்கம் உருவாக்குவதற்கான கட்டமைப்பு குழு SLM மற்றும் LLM ஐ மதிப்பீடு செய்கிறது | தாமதம் + டோக்கன் பயன்பாட்டில் வித்தியாசத்தை அளவிடுங்கள் | ஒற்றை `COMPARE_PROMPT` சூழல் மாறி |
| `chainlit_app.py` (RAG டெமோ) | உள்நாட்டு அறிவு உதவியாளர் மாதிரி | குறைந்த சொற்களைக் கொண்டு குறுகிய பதில்களை தரவுகளுடன் இணைத்தல் | கோப்பில் உள்ள `DOCS` பட்டியல் நேரடியாக |
| `webgpu_demo.html` | சாதனத்தில் உள்ள உலாவி தீர்மான முன்னோட்டம் | குறைந்த தாமத உள்ளூர் சுற்றுப்பயணத்தை + UX கதை விளக்கத்தை காட்டுங்கள் | நேரடி பயனர் prompt மட்டும் |

### சூழல் கதை
தயாரிப்பு அமைப்பு நிர்வாக சுருக்கம் உருவாக்குபவரை விரும்புகிறது. ஒரு இலகு SLM (phi‑4‑mini) சுருக்கங்களை உருவாக்குகிறது; ஒரு பெரிய LLM (gpt‑oss‑20b) முக்கியமான அறிக்கைகளை மட்டுமே மேம்படுத்தலாம். அமர்வு ஸ்கிரிப்ட்கள் கலப்பு வடிவமைப்பை நியாயப்படுத்துவதற்கான உண்மையான தாமதம் மற்றும் டோக்கன் அளவீடுகளைப் பதிவு செய்கின்றன, அதே நேரத்தில் Chainlit டெமோ சிறிய மாடல் பதில்களை உண்மையானதாக வைத்திருக்க எப்படி தரவுகளை மீட்டெடுப்பது என்பதை விளக்குகிறது. WebGPU கருத்து பக்கம் உலாவி வேகத்தை மேம்படுத்தும் போது முழுமையான வாடிக்கையாளர் பக்கம் செயலாக்கத்திற்கான பார்வை பாதையை வழங்குகிறது.

### குறைந்தபட்ச RAG சூழல் (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### கலப்பு வரைவு→மேம்படுத்தும் ஓட்டம் (பசுடோ)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

இரு தாமத கூறுகளையும் கண்காணித்து கலந்த சராசரி செலவைப் பதிவு செய்யுங்கள்.

### விருப்ப மேம்பாடுகள்

| கவனம் | மேம்பாடு | ஏன் | செயல்படுத்தல் குறிப்புகள் |
|-------|---------|-----|--------------------------|
| ஒப்பீட்டு அளவீடுகள் | டோக்கன் பயன்பாடு + முதல்-டோக்கன் தாமதத்தை கண்காணிக்கவும் | முழுமையான செயல்திறன் பார்வை | மேம்பட்ட பெஞ்ச்மார்க் ஸ்கிரிப்டைப் பயன்படுத்தவும் (அமர்வு 3) `BENCH_STREAM=1` உடன் |
| கலப்பு குழாய் | SLM வரைவு → LLM மேம்பாடு | தாமதம் மற்றும் செலவை குறைக்கவும் | phi-4-mini உடன் உருவாக்கவும், gpt-oss-20b உடன் சுருக்கத்தை மேம்படுத்தவும் |
| ஸ்ட்ரீமிங் UI | Chainlit இல் சிறந்த UX | படிப்படியாக கருத்து | உள்ளூர் ஸ்ட்ரீமிங் வெளிப்படுத்தப்பட்டவுடன் `stream=True` ஐப் பயன்படுத்தவும்; துண்டுகளை சேர்க்கவும் |
| WebGPU கேஷிங் | வேகமான JS தொடக்கம் | மீண்டும் தொகுப்பு செலவினத்தை குறைக்கவும் | தொகுக்கப்பட்ட ஷேடர் கலைப்பொருட்களை கேஷ் செய்யவும் (எதிர்கால runtime திறன்) |
| தீர்மான QA தொகுப்பு | நியாயமான மாடல் ஒப்பீடு | மாறுபாட்டை நீக்கவும் | நிலையான prompt பட்டியல் + மதிப்பீடு ஓட்டங்களுக்கு `temperature=0` |
| வெளியீடு மதிப்பீடு | அமைந்த தரக்கண்ணோட்டம் | அனுபவங்களை மீறுங்கள் | எளிய அளவுகோல்: ஒழுங்கு / உண்மைத்தன்மை / சுருக்கம் (1–5) |
| ஆற்றல் / வள குறிப்புகள் | வகுப்பறை விவாதம் | சமநிலைகளை காட்டுங்கள் | OS கண்காணிப்புகள் (Task Manager, `nvidia-smi`) + பெஞ்ச்மார்க் ஸ்கிரிப்ட் வெளியீடுகள் |
| செலவு முறைமைகள் | மேக நியாயப்படுத்தல் | அளவீடு திட்டமிடல் | TCO கதைக்கான டோக்கன்களை கற்பனை மேக விலைக்கு வரைபடம் |
| தாமத சிதைவுகள் | bottlenecks ஐ அடையாளம் காணுங்கள் | மேம்பாடுகளை இலக்கு | prompt தயாரிப்பு, கோரிக்கை அனுப்புதல், முதல் டோக்கன், முழு முடிவு ஆகியவற்றை அளவிடுங்கள் |
| RAG + LLM fallback | தர பாதுகாப்பு வலை | கடினமான கேள்விகளை மேம்படுத்துங்கள் | SLM பதில் நீளம் < வரம்பு அல்லது குறைந்த நம்பிக்கை → escalate |

#### உதாரண கலப்பு வரைவு/மேம்பாடு முறை

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### தாமத சிதைவுகள் வரைபடம்

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

நியாயமான ஒப்பீடுகளுக்காக மாடல்களுக்கிடையே நிலையான அளவீட்டு அமைப்புகளைப் பயன்படுத்தவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->