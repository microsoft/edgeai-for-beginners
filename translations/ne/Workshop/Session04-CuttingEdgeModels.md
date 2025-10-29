<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T21:16:49+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "ne"
}
-->
# सत्र ४: अत्याधुनिक मोडेलहरूको अन्वेषण – LLMs, SLMs र अन-डिभाइस इन्फरेन्स

## सारांश

स्थानीय बनाम क्लाउड इन्फरेन्स परिदृश्यहरूको लागि ठूला भाषा मोडेलहरू (LLMs) र साना भाषा मोडेलहरू (SLMs) तुलना गर्नुहोस्। ONNX Runtime एक्सेलेरेशन, WebGPU कार्यान्वयन, र हाइब्रिड RAG अनुभवहरू प्रयोग गरेर परिनियोजन ढाँचाहरू सिक्नुहोस्। स्थानीय मोडेलसहितको Chainlit RAG डेमो र वैकल्पिक OpenWebUI अन्वेषण समावेश छ। तपाईं WebGPU इन्फरेन्स स्टार्टरलाई अनुकूलन गर्नुहुनेछ र Phi बनाम GPT-OSS-20B क्षमता र लागत/प्रदर्शन व्यापार-अफहरूको मूल्याङ्कन गर्नुहुनेछ।

## सिक्ने उद्देश्यहरू

- **तुलना गर्नुहोस्** SLM बनाम LLM लेटेंसी, मेमोरी, गुणस्तर अक्षहरूमा
- **परिनियोजन गर्नुहोस्** मोडेलहरू ONNXRuntime र (जहाँ समर्थित छ) WebGPU प्रयोग गरेर
- **चलाउनुहोस्** ब्राउजर-आधारित इन्फरेन्स (गोपनीयता-संरक्षण गर्ने अन्तरक्रियात्मक डेमो)
- **एकीकृत गर्नुहोस्** स्थानीय SLM ब्याकएन्डसहितको Chainlit RAG पाइपलाइन
- **मूल्याङ्कन गर्नुहोस्** हल्का गुणस्तर + लागत ह्युरिस्टिक्स प्रयोग गरेर

## पूर्वापेक्षाहरू

- सत्र १–३ पूरा गरिएका
- `chainlit` स्थापना गरिएको (पहिले नै `requirements.txt` मा Module08 का लागि)
- WebGPU-सक्षम ब्राउजर (Windows 11 मा Edge / Chrome को पछिल्लो संस्करण)
- Foundry Local चलिरहेको (`foundry status`)

### क्रस-प्ल्याटफर्म नोट्स

Windows प्राथमिक लक्ष्य वातावरण रहन्छ। macOS विकासकर्ताहरूका लागि जो नेटिभ बाइनरीहरूको प्रतीक्षा गर्दैछन्:
1. Foundry Local लाई Windows 11 VM (Parallels / UTM) वा रिमोट Windows वर्कस्टेशनमा चलाउनुहोस्।
2. सेवा (डिफल्ट पोर्ट 5273) एक्सपोज गर्नुहोस् र macOS मा सेट गर्नुहोस्:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. अघिल्लो सत्रहरूमा जस्तै Python भर्चुअल वातावरण चरणहरू प्रयोग गर्नुहोस्।

Chainlit स्थापना (दुबै प्लेटफर्महरू):
```bash
pip install chainlit
```

## डेमो प्रवाह (३० मिनेट)

### १. Phi (SLM) बनाम GPT-OSS-20B (LLM) तुलना गर्नुहोस् (६ मिनेट)

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

ट्र्याक गर्नुहोस्: प्रतिक्रिया गहिराई, तथ्यात्मक शुद्धता, शैलीगत समृद्धि, लेटेंसी।

### २. ONNX Runtime एक्सेलेरेशन (५ मिनेट)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

GPU सक्रिय गरेपछि throughput परिवर्तनहरू अवलोकन गर्नुहोस् बनाम CPU मात्र।

### ३. ब्राउजरमा WebGPU इन्फरेन्स (६ मिनेट)

स्टार्टर `04-webgpu-inference` अनुकूलन गर्नुहोस् ( `samples/04-cutting-edge/webgpu_demo.html` सिर्जना गर्नुहोस्):

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

फाइल ब्राउजरमा खोल्नुहोस्; कम लेटेंसी स्थानीय राउन्डट्रिप अवलोकन गर्नुहोस्।

### ४. Chainlit RAG च्याट एप (७ मिनेट)

न्यूनतम `samples/04-cutting-edge/chainlit_app.py`:

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

चलाउनुहोस्:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### ५. स्टार्टर प्रोजेक्ट: `04-webgpu-inference` अनुकूलन गर्नुहोस् (६ मिनेट)

डेलिभरेबलहरू:
- प्लेसहोल्डर फेच तर्कलाई स्ट्रिमिङ टोकनहरूसँग प्रतिस्थापन गर्नुहोस् (`stream=True` अन्त बिन्दु भेरियन्ट सक्षम भएपछि प्रयोग गर्नुहोस्)
- लेटेंसी चार्ट थप्नुहोस् (क्लाइन्ट-साइड) phi बनाम gpt-oss-20b टगलहरूको लागि
- RAG सन्दर्भ इनलाइन समावेश गर्नुहोस् (सन्दर्भ कागजातहरूको लागि टेक्स्टएरिया)

## मूल्याङ्कन ह्युरिस्टिक्स

| श्रेणी | Phi-4-mini | GPT-OSS-20B | अवलोकन |
|--------|------------|-------------|---------|
| लेटेंसी (चिसो) | छिटो | ढिलो | SLM छिटो तात्छ |
| मेमोरी | कम | उच्च | उपकरण सम्भाव्यता |
| सन्दर्भ पालन | राम्रो | बलियो | ठूलो मोडेल बढी विस्तृत हुन सक्छ |
| लागत (स्थानीय) | न्यूनतम | उच्च (स्रोत) | ऊर्जा/समय व्यापार-अफ |
| उत्तम प्रयोग केस | एज एप्स | गहिरो तर्क | हाइब्रिड पाइपलाइन सम्भव |

## वातावरण मान्यता

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## समस्या समाधान

| लक्षण | कारण | कार्य |
|-------|-------|-------|
| वेब पृष्ठ फेच असफल | CORS वा सेवा डाउन | अन्त बिन्दु प्रमाणित गर्न `curl` प्रयोग गर्नुहोस्; आवश्यक परे CORS प्रोक्सी सक्षम गर्नुहोस् |
| Chainlit खाली | Env सक्रिय छैन | venv सक्रिय गर्नुहोस् र निर्भरता पुनःस्थापना गर्नुहोस् |
| उच्च लेटेंसी | मोडेल भर्खरै लोड गरिएको | सानो प्रम्प्ट अनुक्रमसँग तातो बनाउनुहोस् |

## सन्दर्भहरू

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG मूल्याङ्कन (Ragas): https://docs.ragas.io

---

**सत्र अवधि**: ३० मिनेट  
**कठिनाई**: उन्नत

## नमूना परिदृश्य र कार्यशाला म्यापिङ

| कार्यशाला सामग्री | परिदृश्य | उद्देश्य | डेटा / प्रम्प्ट स्रोत |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | कार्य वास्तुकला टोलीले कार्यकारी सारांश जेनेरेटरको लागि SLM बनाम LLM मूल्याङ्कन गर्दै | लेटेंसी + टोकन प्रयोग डेल्टा मापन गर्नुहोस् | एकल `COMPARE_PROMPT` env var |
| `chainlit_app.py` (RAG डेमो) | आन्तरिक ज्ञान सहायक प्रोटोटाइप | सानो लेक्सिकल पुनःप्राप्तिसहित छोटो उत्तरहरू आधार बनाउनुहोस् | फाइलमा इनलाइन `DOCS` सूची |
| `webgpu_demo.html` | भविष्यवादी अन-डिभाइस ब्राउजर इन्फरेन्स पूर्वावलोकन | कम-लेटेंसी स्थानीय राउन्डट्रिप + UX कथा देखाउनुहोस् | लाइभ प्रयोगकर्ता प्रम्प्ट मात्र |

### परिदृश्य कथा
उत्पादन संगठनले कार्यकारी ब्रीफिङ जेनेरेटर चाहन्छ। हल्का SLM (phi‑4‑mini) ले सारांशहरू तयार गर्छ; ठूलो LLM (gpt‑oss‑20b) ले मात्र उच्च प्राथमिकता रिपोर्टहरू परिष्कृत गर्न सक्छ। सत्र स्क्रिप्टहरूले हाइब्रिड डिजाइनलाई न्याय दिनको लागि अनुभवजन्य लेटेंसी र टोकन मेट्रिक्स समेट्छ, जबकि Chainlit डेमोले देखाउँछ कि आधारभूत पुनःप्राप्तिले सानो मोडेल उत्तरहरू तथ्यात्मक राख्छ। WebGPU अवधारणा पृष्ठले ब्राउजर एक्सेलेरेशन परिपक्व हुँदा पूर्णत: क्लाइन्ट-साइड प्रशोधनको लागि दृष्टि मार्ग प्रदान गर्दछ।

### न्यूनतम RAG सन्दर्भ (Chainlit)
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

दुवै लेटेंसी घटकहरू ट्र्याक गर्नुहोस् र मिश्रित औसत लागत रिपोर्ट गर्नुहोस्।

### वैकल्पिक सुधारहरू

| ध्यान केन्द्रित | सुधार | किन | कार्यान्वयन संकेत |
|------------------|-------|-----|-------------------|
| तुलनात्मक मेट्रिक्स | टोकन प्रयोग + पहिलो-टोकन लेटेंसी ट्र्याक गर्नुहोस् | समग्र प्रदर्शन दृश्य | सुधारिएको बेंचमार्क स्क्रिप्ट प्रयोग गर्नुहोस् (सत्र ३) `BENCH_STREAM=1` सहित |
| हाइब्रिड पाइपलाइन | SLM ड्राफ्ट → LLM परिष्कृत | लेटेंसी र लागत घटाउनुहोस् | phi-4-mini प्रयोग गरेर सिर्जना गर्नुहोस्, gpt-oss-20b सँग सारांश परिष्कृत गर्नुहोस् |
| स्ट्रिमिङ UI | Chainlit मा राम्रो UX | क्रमिक प्रतिक्रिया | स्थानीय स्ट्रिमिङ एक्सपोज भएपछि `stream=True` प्रयोग गर्नुहोस्; चंक्स जम्मा गर्नुहोस् |
| WebGPU क्यासिङ | छिटो JS इनिट | पुनः कम्पाइल ओभरहेड घटाउनुहोस् | क्यास गरिएको शेडर कलाकृति (भविष्यको रनटाइम क्षमता) |
| निर्धारणात्मक QA सेट | निष्पक्ष मोडेल तुलना | भिन्नता हटाउनुहोस् | फिक्स्ड प्रम्प्ट सूची + मूल्याङ्कन रनहरूको लागि `temperature=0` |
| आउटपुट स्कोरिङ | संरचित गुणस्तर लेंस | कथाहरूभन्दा पर जानुहोस् | सरल मापदण्ड: सुसंगतता / तथ्यात्मकता / संक्षिप्तता (१–५) |
| ऊर्जा / स्रोत नोट्स | कक्षा छलफल | व्यापार-अफ देखाउनुहोस् | OS मोनिटरहरू प्रयोग गर्नुहोस् (`foundry system info`, Task Manager, `nvidia-smi`) + बेंचमार्क स्क्रिप्ट आउटपुटहरू |
| लागत अनुकरण | प्रि-क्लाउड औचित्य | स्केलिङ योजना | टोकनहरूलाई TCO कथाको लागि काल्पनिक क्लाउड मूल्य निर्धारणमा म्याप गर्नुहोस् |
| लेटेंसी विघटन | बाधाहरू पहिचान गर्नुहोस् | अनुकूलनहरू लक्ष्य गर्नुहोस् | प्रम्प्ट तयारी, अनुरोध पठाउनुहोस्, पहिलो टोकन, पूर्ण समाप्ति मापन गर्नुहोस् |
| RAG + LLM फलब्याक | गुणस्तर सुरक्षा जाल | कठिन प्रश्नहरू सुधार गर्नुहोस् | यदि SLM उत्तर लम्बाइ < थ्रेसहोल्ड वा कम आत्मविश्वास → वृद्धि गर्नुहोस् |

#### उदाहरण हाइब्रिड ड्राफ्ट/परिष्कृत ढाँचा

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### लेटेंसी ब्रेकडाउन स्केच

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

निष्पक्ष तुलनाको लागि मोडेलहरूमा लगातार मापन संरचना प्रयोग गर्नुहोस्।

---

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।