<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T21:11:12+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "mr"
}
-->
# सत्र ४: अत्याधुनिक मॉडेल्सचा अभ्यास – LLMs, SLMs आणि ऑन-डिव्हाइस इनफरन्स

## सारांश

स्थानिक आणि क्लाउड इनफरन्स परिस्थितीसाठी मोठ्या भाषा मॉडेल्स (LLMs) आणि लहान भाषा मॉडेल्स (SLMs) यांची तुलना करा. ONNX Runtime गती, WebGPU कार्यान्वयन, आणि हायब्रिड RAG अनुभवांचा उपयोग करून डिप्लॉयमेंट पॅटर्न शिकून घ्या. स्थानिक मॉडेलसह Chainlit RAG डेमो समाविष्ट आहे, तसेच OpenWebUI एक्सप्लोरेशनचा पर्याय. तुम्ही WebGPU इनफरन्स स्टार्टर अडॅप्ट कराल आणि Phi वि GPT-OSS-20B क्षमता आणि खर्च/प्रदर्शन व्यापार-बंदांचे मूल्यांकन कराल.

## शिकण्याची उद्दिष्टे

- **तुलना करा** SLM वि LLM विलंबता, मेमरी, गुणवत्ता अक्षांवर
- **डिप्लॉय करा** मॉडेल्स ONNXRuntime आणि (जिथे समर्थित आहे) WebGPU सह
- **चालवा** ब्राउझर-आधारित इनफरन्स (गोपनीयता-संरक्षणात्मक संवादात्मक डेमो)
- **एकत्रित करा** स्थानिक SLM बॅकएंडसह Chainlit RAG पाइपलाइन
- **मूल्यांकन करा** हलकी गुणवत्ता + खर्च ह्युरिस्टिक्स वापरून

## पूर्वतयारी

- सत्र १–३ पूर्ण केलेले असणे आवश्यक आहे
- `chainlit` स्थापित केलेले (Module08 साठी `requirements.txt` मध्ये आधीच आहे)
- WebGPU-सक्षम ब्राउझर (Windows 11 वर Edge / Chrome नवीनतम)
- Foundry Local चालू (`foundry status`)

### क्रॉस-प्लॅटफॉर्म नोट्स

Windows प्राथमिक लक्ष्य वातावरण राहते. macOS डेव्हलपर्ससाठी जे स्थानिक बायनरीजची वाट पाहत आहेत:
1. Windows 11 VM (Parallels / UTM) किंवा रिमोट Windows वर्कस्टेशनमध्ये Foundry Local चालवा.
2. सेवा उघडा (डिफॉल्ट पोर्ट 5273) आणि macOS वर सेट करा:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. पूर्व सत्रांप्रमाणेच Python वर्च्युअल वातावरण चरणांचा वापर करा.

Chainlit इंस्टॉल (दोन्ही प्लॅटफॉर्मसाठी):
```bash
pip install chainlit
```

## डेमो फ्लो (३० मिनिटे)

### १. Phi (SLM) वि GPT-OSS-20B (LLM) ची तुलना करा (६ मिनिटे)

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

ट्रॅक करा: प्रतिसादाची खोली, तथ्यात्मक अचूकता, शैलीगत समृद्धता, विलंबता.

### २. ONNX Runtime गती (५ मिनिटे)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

GPU सक्षम केल्यानंतर थ्रूपुट बदल पहा व CPU-फक्त मोड.

### ३. ब्राउझरमध्ये WebGPU इनफरन्स (६ मिनिटे)

स्टार्टर `04-webgpu-inference` अडॅप्ट करा (निर्माण करा `samples/04-cutting-edge/webgpu_demo.html`):

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

फाइल ब्राउझरमध्ये उघडा; कमी विलंबता स्थानिक राउंडट्रिप पहा.

### ४. Chainlit RAG चॅट अॅप (७ मिनिटे)

मिनिमल `samples/04-cutting-edge/chainlit_app.py`:

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

चालवा:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### ५. स्टार्टर प्रोजेक्ट: `04-webgpu-inference` अडॅप्ट करा (६ मिनिटे)

डिलिव्हरेबल्स:
- प्लेसहोल्डर फेच लॉजिक प्रवाहित टोकन्ससह बदला (`stream=True` एंडपॉइंट व्हेरिएंट सक्षम झाल्यावर वापरा)
- विलंबता चार्ट (क्लायंट-साइड) phi वि gpt-oss-20b टॉगलसाठी जोडा
- RAG संदर्भ एम्बेड करा (रेफरन्स डॉकसाठी टेक्स्टएरिया)

## मूल्यांकन ह्युरिस्टिक्स

| श्रेणी | Phi-4-mini | GPT-OSS-20B | निरीक्षण |
|--------|------------|-------------|----------|
| विलंबता (थंड) | जलद | हळू | SLM लवकर गरम होते |
| मेमरी | कमी | जास्त | डिव्हाइस व्यवहार्यता |
| संदर्भ पालन | चांगले | मजबूत | मोठे मॉडेल अधिक विस्तृत असू शकते |
| खर्च (स्थानिक) | कमी | जास्त (संसाधन) | ऊर्जा/वेळ व्यापार-बंद |
| सर्वोत्तम उपयोग प्रकरण | एज अॅप्स | सखोल विचार | हायब्रिड पाइपलाइन शक्य |

## वातावरण सत्यापित करणे

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## समस्या निवारण

| लक्षण | कारण | कृती |
|-------|-------|------|
| वेब पृष्ठ फेच अयशस्वी | CORS किंवा सेवा बंद | एंडपॉइंट सत्यापित करण्यासाठी `curl` वापरा; आवश्यक असल्यास CORS प्रॉक्सी सक्षम करा |
| Chainlit रिक्त | Env सक्रिय नाही | venv सक्रिय करा आणि डिप्स पुन्हा स्थापित करा |
| उच्च विलंबता | मॉडेल नुकतेच लोड केले | लहान प्रॉम्प्ट सिक्वेन्ससह गरम करा |

## संदर्भ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG मूल्यांकन (Ragas): https://docs.ragas.io

---

**सत्र कालावधी**: ३० मिनिटे  
**अडचण स्तर**: प्रगत

## नमुना परिस्थिती आणि कार्यशाळा मॅपिंग

| कार्यशाळा वस्तू | परिस्थिती | उद्दिष्ट | डेटा / प्रॉम्प्ट स्रोत |
|------------------|------------|----------|------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | कार्यसंरचना टीम कार्यकारी सारांश जनरेटरसाठी SLM वि LLM चे मूल्यांकन करत आहे | विलंबता + टोकन वापर डेल्टा मोजा | सिंगल `COMPARE_PROMPT` env var |
| `chainlit_app.py` (RAG डेमो) | अंतर्गत ज्ञान सहाय्यक प्रोटोटाइप | लहान उत्तरांना किमान शब्दसंग्रह पुनर्प्राप्तीसह आधार द्या | फाइलमधील इनलाइन `DOCS` यादी |
| `webgpu_demo.html` | भविष्यवादी ऑन-डिव्हाइस ब्राउझर इनफरन्स पूर्वावलोकन | कमी विलंबता स्थानिक राउंडट्रिप + UX कथन दाखवा | लाइव्ह युजर प्रॉम्प्ट फक्त |

### परिस्थिती कथन
उत्पादन संघाला कार्यकारी ब्रीफिंग जनरेटर हवा आहे. हलके SLM (phi‑4‑mini) सारांश तयार करते; मोठे LLM (gpt‑oss‑20b) फक्त उच्च-प्राधान्य अहवाल सुधारू शकते. सत्र स्क्रिप्ट्स अनुभवात्मक विलंबता आणि टोकन मेट्रिक्स कॅप्चर करतात जेणेकरून हायब्रिड डिझाइनचे समर्थन करता येईल, तर Chainlit डेमो दाखवतो की ग्राउंडेड पुनर्प्राप्ती लहान मॉडेल उत्तरांना तथ्यात्मक ठेवते. WebGPU संकल्पना पृष्ठ पूर्णपणे क्लायंट-साइड प्रक्रिया कशी होऊ शकते यासाठी एक दृष्टिकोन प्रदान करते.

### मिनिमल RAG संदर्भ (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### हायब्रिड ड्राफ्ट→सुधारणा प्रवाह (छद्म)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

मिश्रित सरासरी खर्चाचा अहवाल देण्यासाठी दोन्ही विलंबता घटक ट्रॅक करा.

### पर्यायी सुधारणा

| लक्ष केंद्रित | सुधारणा | का | अंमलबजावणी सूचना |
|---------------|----------|----|------------------|
| तुलनात्मक मेट्रिक्स | टोकन वापर + पहिल्या टोकन विलंबता ट्रॅक करा | समग्र प्रदर्शन दृश्य | सुधारित बेंचमार्क स्क्रिप्ट वापरा (सत्र ३) `BENCH_STREAM=1` सह |
| हायब्रिड पाइपलाइन | SLM ड्राफ्ट → LLM सुधारणा | विलंबता आणि खर्च कमी करा | phi-4-mini सह तयार करा, gpt-oss-20b सह सारांश सुधारित करा |
| प्रवाहित UI | Chainlit मध्ये चांगले UX | क्रमिक अभिप्राय | स्थानिक प्रवाह उघड झाल्यावर `stream=True` वापरा; तुकडे जमा करा |
| WebGPU कॅशिंग | जलद JS प्रारंभ | पुन्हा संकलन ओव्हरहेड कमी करा | संकलित शेडर आर्टिफॅक्ट्स कॅश करा (भविष्यातील रनटाइम क्षमता) |
| निर्धारक QA सेट | योग्य मॉडेल तुलना | फरक काढा | निश्चित प्रॉम्प्ट यादी + मूल्यांकन रनसाठी `temperature=0` |
| आउटपुट स्कोरिंग | संरचित गुणवत्ता लेन्स | अनुभवांपलीकडे जा | साधा निकष: सुसंगतता / तथ्यात्मकता / संक्षिप्तता (१–५) |
| ऊर्जा / संसाधन नोट्स | वर्ग चर्चा | व्यापार-बंद दाखवा | OS मॉनिटर्स (`foundry system info`, Task Manager, `nvidia-smi`) + बेंचमार्क स्क्रिप्ट आउटपुट वापरा |
| खर्च अनुकरण | प्री-क्लाउड समर्थन | स्केलिंग योजना | टोकन्सला TCO कथनासाठी काल्पनिक क्लाउड किंमतींशी नकाशा करा |
| विलंबता विघटन | अडथळे ओळखा | ऑप्टिमायझेशन्स लक्ष्य करा | प्रॉम्प्ट तयारी, विनंती पाठवणे, पहिला टोकन, पूर्ण पूर्णता मोजा |
| RAG + LLM फॉलबॅक | गुणवत्ता सुरक्षा जाळे | कठीण प्रश्न सुधारित करा | जर SLM उत्तर लांबी < थ्रेशोल्ड किंवा कमी आत्मविश्वास → वाढवा |

#### उदाहरण हायब्रिड ड्राफ्ट/सुधारणा पॅटर्न

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### विलंबता विघटन स्केच

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

मॉडेल्समध्ये योग्य तुलना करण्यासाठी सातत्यपूर्ण मोजमाप संरचना वापरा.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.