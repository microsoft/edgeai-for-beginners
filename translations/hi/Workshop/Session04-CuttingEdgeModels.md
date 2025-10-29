<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T21:00:36+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "hi"
}
-->
# सत्र 4: अत्याधुनिक मॉडल्स का अन्वेषण – LLMs, SLMs और ऑन-डिवाइस इंफेरेंस

## सारांश

स्थानीय बनाम क्लाउड इंफेरेंस परिदृश्यों के लिए बड़े भाषा मॉडल्स (LLMs) और छोटे भाषा मॉडल्स (SLMs) की तुलना करें। ONNX Runtime एक्सेलेरेशन, WebGPU निष्पादन, और हाइब्रिड RAG अनुभवों का उपयोग करके डिप्लॉयमेंट पैटर्न सीखें। इसमें स्थानीय मॉडल के साथ एक Chainlit RAG डेमो और वैकल्पिक OpenWebUI अन्वेषण शामिल है। आप WebGPU इंफेरेंस स्टार्टर को अनुकूलित करेंगे और Phi बनाम GPT-OSS-20B की क्षमता और लागत/प्रदर्शन के संतुलन का मूल्यांकन करेंगे।

## सीखने के उद्देश्य

- **तुलना करें** SLM बनाम LLM को विलंबता, मेमोरी, और गुणवत्ता के आधार पर
- **मॉडल्स को डिप्लॉय करें** ONNXRuntime और (जहां समर्थित हो) WebGPU के साथ
- **ब्राउज़र-आधारित इंफेरेंस चलाएं** (गोपनीयता-संरक्षण इंटरैक्टिव डेमो)
- **एकीकृत करें** एक Chainlit RAG पाइपलाइन को स्थानीय SLM बैकएंड के साथ
- **मूल्यांकन करें** हल्के गुणवत्ता + लागत के मापदंडों का उपयोग करके

## आवश्यकताएँ

- सत्र 1–3 पूरे किए गए हों
- `chainlit` इंस्टॉल हो (Module08 के लिए `requirements.txt` में पहले से मौजूद)
- WebGPU-सक्षम ब्राउज़र (Windows 11 पर Edge / Chrome का नवीनतम संस्करण)
- Foundry Local चालू हो (`foundry status`)

### क्रॉस-प्लेटफॉर्म नोट्स

Windows प्राथमिक लक्ष्य वातावरण बना हुआ है। macOS डेवलपर्स जो नेटिव बाइनरी की प्रतीक्षा कर रहे हैं:
1. Foundry Local को Windows 11 VM (Parallels / UTM) या रिमोट Windows वर्कस्टेशन में चलाएं।
2. सेवा को एक्सपोज़ करें (डिफ़ॉल्ट पोर्ट 5273) और macOS पर सेट करें:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. पिछले सत्रों की तरह ही Python वर्चुअल एनवायरनमेंट स्टेप्स का उपयोग करें।

Chainlit इंस्टॉल (दोनों प्लेटफॉर्म्स पर):
```bash
pip install chainlit
```

## डेमो फ्लो (30 मिनट)

### 1. Phi (SLM) बनाम GPT-OSS-20B (LLM) की तुलना करें (6 मिनट)

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

ट्रैक करें: प्रतिक्रिया की गहराई, तथ्यात्मक सटीकता, शैलीगत समृद्धि, विलंबता।

### 2. ONNX Runtime एक्सेलेरेशन (5 मिनट)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

GPU सक्षम करने के बाद थ्रूपुट में बदलाव देखें, CPU-केवल मोड की तुलना में।

### 3. ब्राउज़र में WebGPU इंफेरेंस (6 मिनट)

स्टार्टर `04-webgpu-inference` को अनुकूलित करें (बनाएं `samples/04-cutting-edge/webgpu_demo.html`):

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

फाइल को ब्राउज़र में खोलें; कम विलंबता वाले स्थानीय राउंडट्रिप को देखें।

### 4. Chainlit RAG चैट ऐप (7 मिनट)

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

चलाएं:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. स्टार्टर प्रोजेक्ट: `04-webgpu-inference` को अनुकूलित करें (6 मिनट)

डिलीवरबल्स:
- प्लेसहोल्डर फेच लॉजिक को स्ट्रीमिंग टोकन्स से बदलें (एक बार `stream=True` एंडपॉइंट वेरिएंट सक्षम होने पर उपयोग करें)
- विलंबता चार्ट जोड़ें (क्लाइंट-साइड) phi बनाम gpt-oss-20b टॉगल्स के लिए
- RAG संदर्भ को इनलाइन एम्बेड करें (रेफरेंस डॉक्यूमेंट्स के लिए टेक्स्टएरिया)

## मूल्यांकन मापदंड

| श्रेणी | Phi-4-mini | GPT-OSS-20B | अवलोकन |
|--------|------------|-------------|---------|
| विलंबता (कोल्ड) | तेज | धीमा | SLM जल्दी गर्म होता है |
| मेमोरी | कम | अधिक | डिवाइस की व्यवहार्यता |
| संदर्भ पालन | अच्छा | मजबूत | बड़ा मॉडल अधिक विस्तृत हो सकता है |
| लागत (स्थानीय) | न्यूनतम | अधिक (संसाधन) | ऊर्जा/समय संतुलन |
| सर्वोत्तम उपयोग का मामला | एज ऐप्स | गहन तर्क | हाइब्रिड पाइपलाइन संभव |

## पर्यावरण मान्यकरण

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

| लक्षण | कारण | कार्रवाई |
|-------|-------|----------|
| वेब पेज फेच विफल | CORS या सेवा डाउन | एंडपॉइंट को सत्यापित करने के लिए `curl` का उपयोग करें; यदि आवश्यक हो तो CORS प्रॉक्सी सक्षम करें |
| Chainlit खाली | एनव सक्रिय नहीं | venv को सक्रिय करें और डिप्स को पुनः इंस्टॉल करें |
| उच्च विलंबता | मॉडल अभी लोड हुआ है | छोटे प्रॉम्प्ट अनुक्रम के साथ गर्म करें |

## संदर्भ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG मूल्यांकन (Ragas): https://docs.ragas.io

---

**सत्र अवधि**: 30 मिनट  
**कठिनाई स्तर**: उन्नत

## नमूना परिदृश्य और कार्यशाला मैपिंग

| कार्यशाला आर्टिफैक्ट्स | परिदृश्य | उद्देश्य | डेटा / प्रॉम्प्ट स्रोत |
|------------------------|----------|----------|------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | आर्किटेक्चर टीम जो कार्यकारी सारांश जनरेटर के लिए SLM बनाम LLM का मूल्यांकन कर रही है | विलंबता + टोकन उपयोग डेल्टा को मापें | एकल `COMPARE_PROMPT` एनव वेरिएबल |
| `chainlit_app.py` (RAG डेमो) | आंतरिक ज्ञान सहायक प्रोटोटाइप | न्यूनतम शब्दावली पुनर्प्राप्ति के साथ छोटे उत्तरों को आधार बनाना | फाइल में इनलाइन `DOCS` सूची |
| `webgpu_demo.html` | भविष्यवादी ऑन-डिवाइस ब्राउज़र इंफेरेंस पूर्वावलोकन | कम विलंबता वाले स्थानीय राउंडट्रिप + UX नैरेटिव दिखाएं | केवल लाइव उपयोगकर्ता प्रॉम्प्ट |

### परिदृश्य नैरेटिव
प्रोडक्ट ऑर्गनाइजेशन एक कार्यकारी ब्रीफिंग जनरेटर चाहता है। एक हल्का SLM (phi‑4‑mini) सारांश तैयार करता है; एक बड़ा LLM (gpt‑oss‑20b) केवल उच्च प्राथमिकता वाली रिपोर्ट्स को परिष्कृत कर सकता है। सत्र स्क्रिप्ट्स अनुभवजन्य विलंबता और टोकन मेट्रिक्स को कैप्चर करते हैं ताकि हाइब्रिड डिज़ाइन को उचित ठहराया जा सके, जबकि Chainlit डेमो यह दिखाता है कि कैसे ग्राउंडेड पुनर्प्राप्ति छोटे मॉडल के उत्तरों को तथ्यात्मक बनाए रखती है। WebGPU कॉन्सेप्ट पेज पूरी तरह से क्लाइंट-साइड प्रोसेसिंग के लिए एक विज़न पथ प्रदान करता है जब ब्राउज़र एक्सेलेरेशन परिपक्व हो।

### न्यूनतम RAG संदर्भ (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### हाइब्रिड ड्राफ्ट→परिष्कृत प्रवाह (छद्म)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

दोनों विलंबता घटकों को ट्रैक करें ताकि मिश्रित औसत लागत की रिपोर्ट की जा सके।

### वैकल्पिक सुधार

| फोकस | सुधार | क्यों | कार्यान्वयन संकेत |
|------|-------|------|-------------------|
| तुलनात्मक मेट्रिक्स | टोकन उपयोग + प्रथम-टोकन विलंबता को ट्रैक करें | समग्र प्रदर्शन दृश्य | उन्नत बेंचमार्क स्क्रिप्ट (सत्र 3) का उपयोग करें `BENCH_STREAM=1` के साथ |
| हाइब्रिड पाइपलाइन | SLM ड्राफ्ट → LLM परिष्कृत करें | विलंबता और लागत कम करें | phi-4-mini के साथ जनरेट करें, gpt-oss-20b के साथ सारांश को परिष्कृत करें |
| स्ट्रीमिंग UI | Chainlit में बेहतर UX | क्रमिक प्रतिक्रिया | `stream=True` का उपयोग करें एक बार स्थानीय स्ट्रीमिंग एक्सपोज़ हो जाए; चंक्स को इकट्ठा करें |
| WebGPU कैशिंग | तेज़ JS प्रारंभ | पुनः संकलन ओवरहेड कम करें | संकलित शेडर आर्टिफैक्ट्स को कैश करें (भविष्य की रनटाइम क्षमता) |
| निर्धारक QA सेट | निष्पक्ष मॉडल तुलना | भिन्नता हटाएं | फिक्स्ड प्रॉम्प्ट सूची + मूल्यांकन रन के लिए `temperature=0` |
| आउटपुट स्कोरिंग | संरचित गुणवत्ता लेंस | उपाख्यानों से आगे बढ़ें | सरल रूब्रिक: सामंजस्य / तथ्यात्मकता / संक्षिप्तता (1–5) |
| ऊर्जा / संसाधन नोट्स | कक्षा चर्चा | व्यापार-ऑफ दिखाएं | OS मॉनिटर्स (`foundry system info`, Task Manager, `nvidia-smi`) + बेंचमार्क स्क्रिप्ट आउटपुट्स का उपयोग करें |
| लागत अनुकरण | प्री-क्लाउड औचित्य | स्केलिंग की योजना बनाएं | टोकन्स को काल्पनिक क्लाउड प्राइसिंग के साथ TCO नैरेटिव के लिए मैप करें |
| विलंबता विघटन | बाधाओं की पहचान करें | अनुकूलन लक्षित करें | प्रॉम्प्ट तैयारी, अनुरोध भेजें, पहला टोकन, पूर्ण समापन को मापें |
| RAG + LLM फॉलबैक | गुणवत्ता सुरक्षा जाल | कठिन प्रश्नों में सुधार करें | यदि SLM उत्तर लंबाई < थ्रेशोल्ड या कम आत्मविश्वास → एस्केलेट करें |

#### उदाहरण हाइब्रिड ड्राफ्ट/परिष्कृत पैटर्न

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### विलंबता ब्रेकडाउन स्केच

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

निष्पक्ष तुलना के लिए मॉडलों के बीच सुसंगत मापन ढांचे का उपयोग करें।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।