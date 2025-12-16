<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-12-15T20:36:03+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "te"
}
-->
# సెషన్ 3: ఫౌండ్రీ లోకల్‌లో ఓపెన్-సోర్స్ మోడల్స్

## సారాంశం

హగ్గింగ్ ఫేస్ మరియు ఇతర ఓపెన్-సోర్స్ మోడల్స్‌ను ఫౌండ్రీ లోకల్‌లో ఎలా తీసుకురావాలో తెలుసుకోండి. ఎంపిక వ్యూహాలు, కమ్యూనిటీ కాంట్రిబ్యూషన్ వర్క్‌ఫ్లోలు, పనితీరు సరిపోలింపు విధానం, మరియు కస్టమ్ మోడల్ రిజిస్ట్రేషన్లతో ఫౌండ్రీని ఎలా విస్తరించాలో నేర్చుకోండి. ఈ సెషన్ వారానికి "మోడల్ మండేస్" అన్వేషణ థీమ్స్‌కు అనుగుణంగా ఉంటుంది మరియు మీరు ఓపెన్-సోర్స్ మోడల్స్‌ను లోకల్‌గా అంచనా వేసి ఆపరేషనల్ చేయడానికి Azureకి స్కేల్ చేయడానికి సిద్ధం చేస్తుంది.

## నేర్చుకునే లక్ష్యాలు

ముగింపు వరకు మీరు చేయగలుగుతారు:

- **కనుగొనడం & అంచనా వేయడం**: నాణ్యత మరియు వనరుల వ్యత్యాసాలను ఉపయోగించి అభ్యర్థి మోడల్స్ (mistral, gemma, qwen, deepseek) గుర్తించండి.
- **లోడ్ & నడపడం**: ఫౌండ్రీ లోకల్ CLI ఉపయోగించి కమ్యూనిటీ మోడల్స్‌ను డౌన్లోడ్ చేసి, క్యాష్ చేసి, ప్రారంభించండి.
- **బెంచ్‌మార్క్**: సారూప్య లేటెన్సీ + టోకెన్ థ్రూపుట్ + నాణ్యత హ్యూరిస్టిక్స్ వర్తించండి.
- **విస్తరించండి**: SDK-అనుకూల నమూనాలను అనుసరించి కస్టమ్ మోడల్ రాపర్‌ను నమోదు చేయండి లేదా అనుకూలీకరించండి.
- **తులనాత్మకంగా చూడండి**: SLM మరియు మధ్యస్థ LLM ఎంపిక నిర్ణయాల కోసం నిర్మిత తులనాలు తయారు చేయండి.

## ముందస్తు అవసరాలు

- సెషన్లు 1 & 2 పూర్తి చేయాలి
- `foundry-local-sdk` ఇన్‌స్టాల్ చేసిన పైథాన్ వాతావరణం
- బహుళ మోడల్ క్యాష్‌ల కోసం కనీసం 15GB ఖాళీ డిస్క్

### క్రాస్-ప్లాట్‌ఫారమ్ వాతావరణం త్వరిత ప్రారంభం

విండోస్ పవర్‌షెల్:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
macOS / లినక్స్:  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
macOS నుండి విండోస్ హోస్ట్ సర్వీస్‌పై బెంచ్‌మార్క్ చేస్తున్నప్పుడు, సెట్ చేయండి:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## డెమో ఫ్లో (30 నిమిషాలు)

### 1. CLI ద్వారా హగ్గింగ్ ఫేస్ మోడల్స్ లోడ్ చేయడం (8 నిమిషాలు)

```powershell
# క్యాటలాగ్ ఎంట్రీలను జాబితా చేయండి (అవసరమైతే మాన్యువల్‌గా ఫిల్టర్ చేయండి)
foundry model list

# పోలిక లక్ష్యాల సెట్‌ను డౌన్లోడ్ చేయండి
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# క్యాష్‌ను ధృవీకరించండి
foundry cache list
```
  
### 2. నడపడం & త్వరిత ప్రోబ్ (5 నిమిషాలు)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  
### 3. బెంచ్‌మార్క్ స్క్రిప్ట్ (8 నిమిషాలు)

`samples/03-oss-models/benchmark_models.py` సృష్టించండి:

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
  
నడపండి:

```powershell
python samples/03-oss-models/benchmark_models.py
```
  
### 4. పనితీరు తులన (5 నిమిషాలు)

ట్రేడ్-ఆఫ్స్ చర్చించండి: లోడ్ సమయం, మెమరీ ఫుట్‌ప్రింట్ (టాస్క్ మేనేజర్ / `nvidia-smi` / OS వనరు మానిటర్ గమనించండి), అవుట్‌పుట్ నాణ్యత మరియు వేగం. లేటెన్సీ & థ్రూపుట్ కోసం పైథాన్ బెంచ్‌మార్క్ స్క్రిప్ట్ (సెషన్ 3) ఉపయోగించండి; GPU యాక్సిలరేషన్ ఎనేబుల్ చేసిన తర్వాత మళ్లీ పునరావృతం చేయండి.

### 5. స్టార్టర్ ప్రాజెక్ట్ (4 నిమిషాలు)

మోడల్ తులన నివేదిక జనరేటర్ సృష్టించండి (బెంచ్‌మార్కింగ్ స్క్రిప్ట్‌ను మార్క్‌డౌన్ ఎగుమతితో విస్తరించండి).

## స్టార్టర్ ప్రాజెక్ట్: `03-huggingface-models` విస్తరణ

ఉన్న నమూనాను మెరుగుపరచండి:

1. బెంచ్‌మార్క్ సమాహరణ + CSV/Markdown అవుట్‌పుట్ జోడించడం.  
2. సులభమైన గుణాత్మక స్కోరింగ్ అమలు (ప్రాంప్ట్ జంట సెట్ + మాన్యువల్ అనోటేషన్ స్టబ్ ఫైల్).  
3. ప్లగ్ చేయదగిన మోడల్ జాబితా & ప్రాంప్ట్ సెట్ కోసం JSON కాన్ఫిగ్ (`models.json`) పరిచయం.

## ధృవీకరణ చెక్లిస్ట్

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
అన్ని లక్ష్య మోడల్స్ కనబడాలి మరియు ప్రోబ్ చాట్ అభ్యర్థనకు స్పందించాలి.

## నమూనా సన్నివేశం & వర్క్‌షాప్ మ్యాపింగ్

| వర్క్‌షాప్ స్క్రిప్ట్ | సన్నివేశం | లక్ష్యం | ప్రాంప్ట్ / డేటాసెట్ మూలం |
|-----------------------|-----------|--------|-----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | ఎడ్జ్ ప్లాట్‌ఫారమ్ టీమ్ ఎంబెడ్డెడ్ సమ్మరైజర్ కోసం డిఫాల్ట్ SLM ఎంపిక | అభ్యర్థి మోడల్స్ మధ్య లేటెన్సీ + p95 + టోకెన్స్/సెకను తులన తయారు చేయండి | Inline `PROMPT` వేరియబుల్ + వాతావరణం `BENCH_MODELS` జాబితా |

### సన్నివేశ కథనం  
ఉత్పత్తి ఇంజనీరింగ్ ఆఫ్‌లైన్ మీటింగ్-నోట్స్ ఫీచర్ కోసం డిఫాల్ట్ లైట్‌వెయిట్ సమ్మరైజేషన్ మోడల్ ఎంచుకోవాలి. వారు నియంత్రిత డిటర్మినిస్టిక్ బెంచ్‌మార్క్‌లు (temperature=0) ఒక స్థిర ప్రాంప్ట్ సెట్‌పై (కింద ఉదాహరణ చూడండి) నడిపించి, GPU యాక్సిలరేషన్ తో మరియు లేకుండా లేటెన్సీ + థ్రూపుట్ మెట్రిక్స్ సేకరిస్తారు.

### ఉదాహరణ ప్రాంప్ట్ సెట్ JSON (విస్తరించదగినది)  
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
ప్రతి మోడల్‌కు ప్రతి ప్రాంప్ట్‌ను లూప్ చేయండి, ప్రాంప్ట్-ప్రతి లేటెన్సీని క్యాప్చర్ చేసి పంపిణీ మెట్రిక్స్ మరియు అవుట్లయర్లను గుర్తించండి.

## మోడల్ ఎంపిక ఫ్రేమ్‌వర్క్

| కొలమానం | మెట్రిక్ | ఎందుకు ముఖ్యం |
|----------|----------|----------------|
| లేటెన్సీ | సగటు / p95 | వినియోగదారు అనుభవం స్థిరత్వం |
| థ్రూపుట్ | టోకెన్స్/సెకను | బ్యాచ్ & స్ట్రీమింగ్ స్కేలబిలిటీ |
| మెమరీ | రెసిడెంట్ సైజ్ | పరికరం సరిపోవడం & సమకాలీనత |
| నాణ్యత | రూబ్రిక్ ప్రాంప్ట్స్ | పనికి అనుకూలత |
| ఫుట్‌ప్రింట్ | డిస్క్ క్యాష్ | పంపిణీ & నవీకరణలు |
| లైసెన్స్ | ఉపయోగ అనుమతి | వాణిజ్య అనుగుణత |

## కస్టమ్ మోడల్‌తో విస్తరించడం

హై-లెవల్ ప్యాటర్న్ (సూచనాత్మకం):

```python
# ప్సూడో_అడాప్టర్.py (సంకల్పనాత్మక)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# స్థానిక రూటింగ్‌తో నమోదు చేయండి (భవిష్యత్తు విస్తరణ బిందువు)
```
  
అడాప్టర్ ఇంటర్‌ఫేస్‌ల అభివృద్ధికి అధికారిక రిపోను సంప్రదించండి:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## సమస్య పరిష్కారం

| సమస్య | కారణం | పరిష్కారం |
|--------|---------|-----------|
| mistral-7b పై OOM | తగినంత RAM/GPU లేదు | ఇతర మోడల్స్ ఆపండి; చిన్న వెర్షన్ ప్రయత్నించండి |
| మొదటి స్పందన నెమ్మదిగా | కోల్డ్ లోడ్ | పీరియాడిక్ లైట్‌వెయిట్ ప్రాంప్ట్‌తో వేడి ఉంచండి |
| డౌన్లోడ్ నిలిచిపోవడం | నెట్‌వర్క్ అస్థిరత | మళ్లీ ప్రయత్నించండి; ఆఫ్-పీక్ సమయంలో ప్రీఫెచ్ చేయండి |

## సూచనలు

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Model Mondays: https://aka.ms/model-mondays  
- Hugging Face Model Discovery: https://huggingface.co/models

---

**సెషన్ వ్యవధి**: 30 నిమిషాలు (+ ఐచ్ఛిక లోతైన అధ్యయనం)  
**కష్టత**: మధ్యస్థ

### ఐచ్ఛిక మెరుగుదలలు

| మెరుగుదల | లాభం | ఎలా |
|-----------|--------|-------|
| స్ట్రీమింగ్ ఫస్ట్-టోకెన్ లేటెన్సీ | గ్రహించదగిన స్పందనశీలత కొలుస్తుంది | `BENCH_STREAM=1` తో బెంచ్‌మార్క్ నడపండి (`Workshop/samples/session03`లో మెరుగైన స్క్రిప్ట్) |
| డిటర్మినిస్టిక్ మోడ్ | స్థిరమైన రిగ్రెషన్ తులనాలు | `temperature=0`, స్థిర ప్రాంప్ట్ సెట్, JSON అవుట్‌పుట్‌లను వెర్షన్ కంట్రోల్‌లో క్యాప్చర్ చేయండి |
| నాణ్యత రూబ్రిక్ స్కోరింగ్ | గుణాత్మక కొలమానం జోడిస్తుంది | అంచనా వేయబడిన ఫాసెట్స్‌తో `prompts.json` నిర్వహించండి; స్కోర్లు (1–5) మాన్యువల్ లేదా ద్వితీయ మోడల్ ద్వారా అనోటేట్ చేయండి |
| CSV / Markdown ఎగుమతి | పంచుకునే నివేదిక | టేబుల్ & హైలైట్స్‌తో `benchmark_report.md` రాయడానికి స్క్రిప్ట్‌ను విస్తరించండి |
| మోడల్ సామర్థ్య ట్యాగ్స్ | తర్వాత ఆటోమేటెడ్ రూటింగ్‌కు సహాయం | `{alias: {capabilities:[], size_mb:..}}`తో `models.json` నిర్వహించండి |
| క్యాష్ వార్మప్ దశ | కోల్డ్-స్టార్ట్ పక్షపాతం తగ్గిస్తుంది | టైమింగ్ లూప్ ముందు ఒక వార్మ్ రౌండ్ నడపండి (ఇప్పటికే అమలు) |
| శాతం ఖచ్చితత్వం | బలమైన టెయిల్ లేటెన్సీ | numpy percentile ఉపయోగించండి (ఇప్పటికే రిఫాక్టర్డ్ స్క్రిప్ట్‌లో ఉంది) |
| టోకెన్ ఖర్చు అంచనా | ఆర్థిక తులన | అంచనా ఖర్చు = (టోకెన్స్/సెకను * సగటు టోకెన్స్ ప్రతి అభ్యర్థన) * ఎనర్జీ హ్యూరిస్టిక్ |
| విఫలమైన మోడల్స్ ఆటో-స్కిప్ | బ్యాచ్ నడపడంలో సహనం | ప్రతి బెంచ్‌మార్క్‌ను try/exceptలో చుట్టండి మరియు స్థితి ఫీల్డ్‌ను గుర్తించండి |

#### కనిష్ట మార్క్‌డౌన్ ఎగుమతి స్నిపెట్

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  
#### డిటర్మినిస్టిక్ ప్రాంప్ట్ సెట్ ఉదాహరణ

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
తులనీయమైన మెట్రిక్స్ కోసం రాండమ్ ప్రాంప్ట్‌ల స్థానంలో స్థిర జాబితాను లూప్ చేయండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->