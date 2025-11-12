<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T22:18:15+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "hi"
}
-->
# सत्र 3: फाउंड्री लोकल में ओपन-सोर्स मॉडल्स

## सारांश

जानें कि Hugging Face और अन्य ओपन-सोर्स मॉडल्स को फाउंड्री लोकल में कैसे लाया जाए। चयन रणनीतियों, सामुदायिक योगदान वर्कफ़्लो, प्रदर्शन तुलना पद्धति, और कस्टम मॉडल पंजीकरण के साथ फाउंड्री को कैसे विस्तारित किया जाए, इसके बारे में जानकारी प्राप्त करें। यह सत्र साप्ताहिक "मॉडल मंडे" अन्वेषण थीम्स से जुड़ा है और आपको ओपन-सोर्स मॉडल्स को स्थानीय रूप से मूल्यांकन और संचालन करने के लिए तैयार करता है, इससे पहले कि आप Azure पर स्केल करें।

## सीखने के उद्देश्य

सत्र के अंत तक आप सक्षम होंगे:

- **खोजें और मूल्यांकन करें**: गुणवत्ता बनाम संसाधन संतुलन का उपयोग करके संभावित मॉडल्स (mistral, gemma, qwen, deepseek) की पहचान करें।
- **लोड करें और चलाएं**: फाउंड्री लोकल CLI का उपयोग करके सामुदायिक मॉडल्स को डाउनलोड, कैश और लॉन्च करें।
- **बेंचमार्क करें**: स्थिर लेटेंसी + टोकन थ्रूपुट + गुणवत्ता हीयूरिस्टिक्स लागू करें।
- **विस्तार करें**: SDK-संगत पैटर्न का पालन करते हुए कस्टम मॉडल रैपर को पंजीकृत या अनुकूलित करें।
- **तुलना करें**: SLM बनाम मिड-साइज़ LLM चयन निर्णयों के लिए संरचित तुलना तैयार करें।

## आवश्यकताएँ

- सत्र 1 और 2 पूरे किए गए हों
- Python वातावरण जिसमें `foundry-local-sdk` इंस्टॉल हो
- कई मॉडल कैश के लिए कम से कम 15GB खाली डिस्क स्थान

### क्रॉस-प्लेटफ़ॉर्म वातावरण त्वरित शुरुआत

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

जब macOS से Windows होस्ट सेवा के खिलाफ बेंचमार्किंग करें, सेट करें:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## डेमो फ्लो (30 मिनट)

### 1. CLI के माध्यम से Hugging Face मॉडल्स लोड करें (8 मिनट)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. चलाएं और त्वरित जांच करें (5 मिनट)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. बेंचमार्क स्क्रिप्ट (8 मिनट)

`samples/03-oss-models/benchmark_models.py` बनाएं:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

चलाएं:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. प्रदर्शन की तुलना करें (5 मिनट)

ट्रेड-ऑफ्स पर चर्चा करें: लोड समय, मेमोरी उपयोग (Task Manager / `nvidia-smi` / OS संसाधन मॉनिटर का अवलोकन करें), आउटपुट गुणवत्ता बनाम गति। लेटेंसी और थ्रूपुट के लिए Python बेंचमार्क स्क्रिप्ट (सत्र 3) का उपयोग करें; GPU एक्सेलेरेशन सक्षम करने के बाद दोहराएं।

### 5. स्टार्टर प्रोजेक्ट (4 मिनट)

बेंचमार्किंग स्क्रिप्ट के साथ मार्कडाउन निर्यात को बढ़ाकर मॉडल तुलना रिपोर्ट जनरेटर बनाएं।

## स्टार्टर प्रोजेक्ट: `03-huggingface-models` को विस्तारित करें

मौजूदा नमूने को बेहतर बनाएं:

1. बेंचमार्क एग्रीगेशन + CSV/Markdown आउटपुट जोड़ें।
2. सरल गुणात्मक स्कोरिंग लागू करें (प्रॉम्प्ट पेयर सेट + मैनुअल एनोटेशन स्टब फ़ाइल)।
3. JSON कॉन्फ़िगरेशन (`models.json`) पेश करें प्लग करने योग्य मॉडल सूची और प्रॉम्प्ट सेट के लिए।

## सत्यापन चेकलिस्ट

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

सभी लक्षित मॉडल्स को प्रकट होना चाहिए और जांच चैट अनुरोध का उत्तर देना चाहिए।

## नमूना परिदृश्य और कार्यशाला मैपिंग

| कार्यशाला स्क्रिप्ट | परिदृश्य | लक्ष्य | प्रॉम्प्ट / डेटासेट स्रोत |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | एज़ प्लेटफ़ॉर्म टीम एम्बेडेड समरीज़ेशन के लिए डिफ़ॉल्ट SLM का चयन कर रही है | उम्मीदवार मॉडल्स के बीच लेटेंसी + p95 + टोकन/सेकंड तुलना तैयार करें | इनलाइन `PROMPT` var + वातावरण `BENCH_MODELS` सूची |

### परिदृश्य कथा

उत्पाद इंजीनियरिंग को ऑफ़लाइन मीटिंग-नोट्स फीचर के लिए डिफ़ॉल्ट हल्के समरीज़ेशन मॉडल का चयन करना होगा। वे नियंत्रित निर्धारक बेंचमार्क (temperature=0) एक निश्चित प्रॉम्प्ट सेट पर चलाते हैं (नीचे उदाहरण देखें) और GPU एक्सेलेरेशन के साथ और बिना लेटेंसी + थ्रूपुट मेट्रिक्स एकत्र करते हैं।

### उदाहरण प्रॉम्प्ट सेट JSON (विस्तार योग्य)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

प्रत्येक प्रॉम्प्ट को प्रत्येक मॉडल पर लूप करें, वितरण मेट्रिक्स प्राप्त करने और आउटलायर्स का पता लगाने के लिए प्रति-प्रॉम्प्ट लेटेंसी कैप्चर करें।

## मॉडल चयन फ्रेमवर्क

| आयाम | मीट्रिक | क्यों महत्वपूर्ण है |
|----------|--------|----------------|
| लेटेंसी | औसत / p95 | उपयोगकर्ता अनुभव की स्थिरता |
| थ्रूपुट | टोकन/सेकंड | बैच और स्ट्रीमिंग स्केलेबिलिटी |
| मेमोरी | रेजिडेंट साइज | डिवाइस फिट और समवर्तीता |
| गुणवत्ता | रूब्रिक प्रॉम्प्ट्स | कार्य उपयुक्तता |
| फुटप्रिंट | डिस्क कैश | वितरण और अपडेट्स |
| लाइसेंस | उपयोग अनुमति | व्यावसायिक अनुपालन |

## कस्टम मॉडल के साथ विस्तार

उच्च-स्तरीय पैटर्न (छद्म):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

विकसित एडेप्टर इंटरफेस के लिए आधिकारिक रिपॉजिटरी पर परामर्श करें:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## समस्या निवारण

| समस्या | कारण | समाधान |
|-------|-------|-----|
| mistral-7b पर OOM | अपर्याप्त RAM/GPU | अन्य मॉडल्स को रोकें; छोटे वेरिएंट का प्रयास करें |
| पहली प्रतिक्रिया धीमी | कोल्ड लोड | एक आवधिक हल्के प्रॉम्प्ट के साथ गर्म रखें |
| डाउनलोड रुक जाता है | नेटवर्क अस्थिरता | पुनः प्रयास करें; ऑफ-पीक के दौरान प्रीफेच करें |

## संदर्भ

- फाउंड्री लोकल SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- मॉडल मंडे: https://aka.ms/model-mondays
- Hugging Face मॉडल डिस्कवरी: https://huggingface.co/models

---

**सत्र अवधि**: 30 मिनट (+ वैकल्पिक गहन अध्ययन)  
**कठिनाई स्तर**: मध्यम

### वैकल्पिक सुधार

| सुधार | लाभ | कैसे |
|-------------|---------|-----|
| स्ट्रीमिंग फर्स्ट-टोकन लेटेंसी | अनुभव की गई प्रतिक्रिया समय को मापता है | `BENCH_STREAM=1` के साथ बेंचमार्क चलाएं (`Workshop/samples/session03` में उन्नत स्क्रिप्ट) |
| निर्धारक मोड | स्थिर प्रतिगमन तुलना | `temperature=0`, निश्चित प्रॉम्प्ट सेट, JSON आउटपुट को संस्करण नियंत्रण के तहत कैप्चर करें |
| गुणवत्ता रूब्रिक स्कोरिंग | गुणात्मक आयाम जोड़ता है | अपेक्षित पहलुओं के साथ `prompts.json` बनाए रखें; स्कोर (1–5) मैन्युअल रूप से या द्वितीयक मॉडल के माध्यम से एनोटेट करें |
| CSV / Markdown निर्यात | साझा करने योग्य रिपोर्ट | स्क्रिप्ट को `benchmark_report.md` लिखने के लिए विस्तारित करें जिसमें तालिका और मुख्य बिंदु हों |
| मॉडल क्षमता टैग्स | बाद में स्वचालित रूटिंग में मदद करता है | `{alias: {capabilities:[], size_mb:..}}` के साथ `models.json` बनाए रखें |
| कैश वार्मअप चरण | कोल्ड-स्टार्ट पूर्वाग्रह को कम करें | समय लूप से पहले एक गर्म राउंड निष्पादित करें (पहले से लागू) |
| पर्सेंटाइल सटीकता | मजबूत टेल लेटेंसी | numpy पर्सेंटाइल का उपयोग करें (पहले से पुनर्गठित स्क्रिप्ट में) |
| टोकन लागत अनुमान | आर्थिक तुलना | अनुमानित लागत = (टोकन/सेकंड * प्रति अनुरोध औसत टोकन) * ऊर्जा हीयूरिस्टिक |
| असफल मॉडल्स को स्वचालित रूप से छोड़ना | बैच रन में लचीलापन | प्रत्येक बेंचमार्क को try/except में लपेटें और स्थिति फ़ील्ड को चिह्नित करें |

#### न्यूनतम मार्कडाउन निर्यात स्निपेट

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### निर्धारक प्रॉम्प्ट सेट उदाहरण

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

समान मेट्रिक्स के लिए कमिट्स के बीच यादृच्छिक प्रॉम्प्ट्स के बजाय स्थिर सूची को लूप करें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->