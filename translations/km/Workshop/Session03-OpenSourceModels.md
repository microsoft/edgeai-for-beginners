# សម័យ 3៖ ម៉ូដែលប្រភពបើកនៅក្នុង Foundry Local

## សេចក្តីសង្ខេប

ស្វែងយល់ពីរបៀបយក Hugging Face និងម៉ូដែលប្រភពបើកផ្សេងទៀតចូលទៅក្នុង Foundry Local។ រៀនយុទ្ធសាស្រ្តជ្រើសរើស ផលិតកម្មសហគមន៍ វិធីសាស្រ្តប្រៀបធៀបកម្រិតការអនុវត្ត និងរបៀបបន្ថែម Foundry ជាមួយការចុះបញ្ជីម៉ូដែលផ្ទាល់ខ្លួន។ សម័យនេះត្រូវបានផ្នែកជាមួយប្រធានបទស្វែងយល់ "Model Mondays" ប្រចាំសប្តាហ៍ ហើយផ្ដល់ឱ្យអ្នកនូវឧបករណ៍ដើម្បីវាយតម្លៃ និងដំណើរការម៉ូដែលប្រភពបើកមូលដ្ឋាននៅក្នុងស្រុកមុនពេលពង្រីកទៅ Azure។

## ប្រយោជន៍ការសិក្សា

នៅចុងបញ្ចប់ អ្នកនឹងអាច៖

- **ស្វែងរក និងវាយតម្លៃ**៖ កំណត់ម៉ូដែលជម្រើស (mistral, gemma, qwen, deepseek) ដោយប្រើប្រសិទ្ធភាពគុណភាពទល់នឹងធនធាន។
- **បន្ថែម និងបើកដំណើរការ**៖ ប្រើ Foundry Local CLI ដើម្បីទាញយក បង្កក់ និងចាប់ផ្តើមម៉ូដែលសហគមន៍។
- **វាយតម្លៃប្រសិទ្ធភាព**៖ អនុវត្ត latency + token throughput + គុណភាពដោយមានម៉ាកស្ដង់ដារ។
- **បន្ថែម**៖ ចុះបញ្ជីឬកែសម្រួល Wrapper ម៉ូដែលផ្ទាល់ខ្លួន ដោយអនុវត្តតាមលំនាំ SDK-compatible។
- **ប្រៀបធៀប**៖ បង្កើតការប្រៀបធៀបរចនាសម្ព័ន្ធសម្រាប់ជម្រើស SLM ទល់នឹង mid-size LLM។

## តម្រូវការ​មុន

- បញ្ចប់សម័យ 1 និង 2
- បរិយាកាស Python មាន `foundry-local-sdk` តម្លើងរួច
- មានទំហំដីសេវាកម្មទំនេរ 15GB ឬច្រើនសម្រាប់កាសស៍ម៉ូដែលជាច្រើន

### ចាប់ផ្តើមបរិយាកាសឆ្លងកាត់​វេទិកា

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
  
ពេលវាយតម្លៃពី macOS ទៅសេវាកម្មម៉ាស៊ីនផ្ទះ Windows, កំណត់៖  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ដំណើរការតំណាង (30 នាទី)

### 1. បន្ថែមម៉ូដែល Hugging Face តាម CLI (8 នាទី)

```powershell
# បញ្ជីចំនុះក្នុងកាតាឡុក (ច្រាញ់ដោយដៃប្រសិនបើចាំបាច់)
foundry model list

# ទាញយកកំណត់គោលដៅប្រៀបធៀបមួយសំណុំ
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# ផ្ទៀងផ្ទាត់កេស
foundry cache list
```


### 2. បើកដំណើរការ និងពិនិត្យឆាប់ៗ (5 នាទី)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. វាយតម្លៃពិនិត្យកូដ (8 នាទី)

បង្កើត `samples/03-oss-models/benchmark_models.py`:

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
  
បើកដំណើរការ៖

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. ប្រៀបធៀបប្រសិទ្ធភាព (5 នាទី)

ពិភាក្សាអំពីការជួញដូរ៖ ពេលបញ្ចូល ម៉ាស៊ីនចងចាំ (មើល Task Manager / `nvidia-smi` / មន្ត្រីត្រួតពិនិត្យធនធាន OS) គុណភាពលទ្ធផល ទល់នឹងល្បឿន។ ប្រើ Python benchmark script (សម័យ 3) សម្រាប់ latency និង throughput; ប្រសិនបើបើក GPU acceleration សូមធ្វើម្ដងទៀត។

### 5. គំរោងចាប់ផ្តើម (4 នាទី)

បង្កើតអ្នកបង្កើតរបាយការណ៍ប្រៀបធៀបម៉ូដែល (បន្ថែម script វាយតម្លៃជាមួយនឹងការនាំចេញ markdown)។

## គំរោងចាប់ផ្តើម៖ បន្ថែមទៅលើ `03-huggingface-models`

បង្កើនគំរូដែលមានដោយ៖

1. បន្ថែមការរួមបញ្ចូលតម្លៃវាយតម្លៃ + បញ្ចូលចេញ CSV/Markdown។
2. អនុវត្តការវាយតម្លៃគុណភាពសាមញ្ញ (បញ្ជីកំណត់ prompt ជូង + ឯកសារចំណាំដៃលើសំណុំបែបបទ)។
3. សម្រួលភាព JSON (`models.json`) សម្រាប់បញ្ជីម៉ូដែលដែលអាចភ្ជាប់ និងបញ្ជី prompt។

## បញ្ជីពិនិត្យការផ្ទៀងផ្ទាត់

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
ម៉ូដែលគោលដៅទាំងអស់គួរតែបង្ហាញ ហើយឆ្លើយតបចំពោះសំណើ probe chat នៅក្នុងសំណុំ។

## ទីតាំងគំរូ និងផែនការបម្រើវគ្គបណ្តុះបណ្តាល

| ឯកសារវគ្គបណ្តុះបណ្តាល | ទីតាំងគំរូ | គោលដៅ | ប្រភព Prompt / Dataset |
|-------------------------|--------------|----------|--------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | ក្រុមផ្នែកផ្លាស់ប្ដូរបឋមភាគនៅទីតាំង Edge ជ្រើសរើស SLM ដើមថាសម្រាប់អ្នកសរុបបញ្ហារង​ខ្នាតតូច | ផលិតប្រៀបធៀប latency + p95 + tokens/sec ទូទាំងម៉ូដែលជម្រើស | ខ្ទង់ PROMPT inline + បញ្ជីបរិយាកាស BENCH_MODELS |

### ពិពណ៌នាទីតាំងគំរូ

វិស្វករផលិតផលត្រូវជ្រើសរើសម៉ូដែលសង្ខេបតូចស្រាលត្រូវបានប្រើសម្រាប់មុខងារសម្គាល់កំណត់ហេតុកិច្ចប្រជុំក្រៅបណ្ដាញ។ ពួកគេបើកដំណើរការវាយតម្លៃគ្រប់គ្រង (temperature=0) លើបញ្ជី prompt ដដែល ហើយប្រមូលសំគាល់ latency និង throughput ជាមួយនឹងគ្មាន និងមាន GPU acceleration ។

### ឧទាហរណ៍សំណុំ Prompt JSON (អាចពង្រីកបាន)  
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
ធ្វើវិនិយោគហ្វើង prompt មួយចំនួននីមួយៗនៃម៉ូដែល ហើយថតទុក latency លើមួយ prompt ដើម្បីទទួលបានស្ថិតិប្រែកាត់ និងរកឃើញតម្លើងក្រៅបង្អួត។

## ស៊ុមជ្រើសរើសម៉ូដែល

| មាតិកា | អង្គវិធី | ហេតុអ្វីវាសំខាន់ |
|----------|----------|--------------------|
| Latency | avg / p95 | មុខងារប្រើប្រាស់ផ្ទាល់ខ្លួនមិនប្រែប្រួល |
| Throughput | tokens/sec | កំណត់ល្បឿនកញ្ចប់ និងចេញចុងចរបាន |
| Memory | ទំហំអង្គចងចាំ | តម្រូវឧបករណ៍ និងហាមឃាត់ការប្រើប្រាស់ជារួម |
| Quality | prompt តារាងវាយតម្លៃ | សមត្ថភាព អនុវត្តភារកិច្ច |
| Footprint | កាសស៍នៅលើ đĩa | ការចែកចាយ និងធ្វើបច្ចុប្បន្នភាព |
| License | ការអនុញ្ញាតប្រើប្រាស់ | ស្របច្បាប់ពាណិជ្ជកម្ម |

## បន្ថែមជាមួយម៉ូដែលផ្ទាល់ខ្លួន

រូបមន្តកម្រិតខ្ពស់ (pseudo):

```python
# pseudo_adapter.py (គំនិតទូទៅ)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# ធ្វើការចុះបញ្ជីជាមួយផ្លូវការបញ្ជូនក្នុងស្រុក (ចំណុចអាចពង្រីកបាននៅអនាគត)
```
  
ពិនិត្យសំណុំផ្លូវការ សម្រាប់ចំនុចផ្លាស់ប្តូររបស់ adapter៖  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## ជំនួយបញ្ហា

| បញ្ហា | មូលហេតុ | វិធីជួសជុល |
|-------|---------|---------------|
| OOM នៅ mistral-7b | RAM/GPU មិនគ្រប់គ្រាន់ | ឈប់ម៉ូដែលផ្សេងទៀត; ព្យាយាមប្រភេទតូចជាង |
| ពេលចាប់ផ្តើមប្រតិកម្មយឺត | បង្ហោះត្រជាក់ទាប | រក្សាគន្លងកម្ដៅជាមួយ prompt ស្រាលបន្តបន្ទាប់ |
| ចុចបញ្ឈប់ទាញយក | បណ្តាញមិនស្ថిర | សាកល្បងម្តងទៀត; ទាញយកជាមុនពេលពេលបិទ |

## ឯកសារយោង

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Model Mondays: https://aka.ms/model-mondays  
- ស្វែងរកម៉ូដែល Hugging Face: https://huggingface.co/models

---

**រយៈពេលសម័យ**: 30 នាទី (+ ជ្រាបជ្រាបជម្រើស)  
**កម្រិត**: មធ្យម

### ការកែលម្អជម្រើស

| ការកែលម្អ | អត្ថប្រយោជន៍ | របៀបធ្វើ |
|-----------|----------------|------------|
| Streaming First-Token Latency | វាស់ប្រតិកម្មដែលបានយល់ពី | ប្រតិបត្តិវាយតម្លៃជាមួយ `BENCH_STREAM=1` (script ត្រូវបានបង្កើតបន្ថែមនៅ `Workshop/samples/session03`) |
| របៀប Deterministic | វាយតម្លៃប្រៀបធៀបអនុលោម | `temperature=0`, បញ្ជី prompt ដដែល, ថត JSON ក្រោមការគ្រប់គ្រងកំណែ |
| វាយតម្លៃគុណភាព Rubric | បន្ថែមវិមាត្របែបគុណភាព | រក្សាទុក `prompts.json` មានមុខងារ ពិនិត្យ ពិន្ទុ (1–5) ដោយដៃ ឬម៉ូដែលទី២ |
| នាំចេញ CSV / Markdown | រាយការណ៍ចែករំលែកបាន | បន្ថែម script ដើម្បីសរសេរ `benchmark_report.md` ជាមួយតារាង និងលម្អិត |
| ស្លាកសមត្ថភាពម៉ូដែល | ជួយក្នុងការបែងចែកបន្ទាប់ | រក្សាទុក `models.json` ជា `{alias: {capabilities:[], size_mb:..}}` |
| ជំហានកម្ដៅកាសស៍ | កាត់បន្ថយបញ្ហាចាប់ផ្តើមត្រជាក់ | ប្រតិបត្តិមួយវដ្តកម្ដៅមុនលំនឹងពេលវេលា (បានអនុវត្តរួច) |
| ភាពត្រឹមត្រូវភាគរយ | ប្រសិទ្ធភាព tail latency | ប្រើ numpy percentile (មាននៅក្នុង script ចាស់) |
| ប៉ាន់ស្មានថ្លៃ Token | ប្រៀបធៀបសេដ្ឋកិច្ច | ប៉ាន់ស្មានថ្លៃ = (tokens/sec * avg tokens per request) * heuristic energy |
| ជៀសវាងម៉ូដែលបរាជ័យស្វ័យប្រវត្តិ | ភាពរឹងមាំក្នុងករណីបញ្ហា | បង់កញ្ចប់វិញក្នុងសំណុំពិនិត្យ try/except ហើយកំណត់ស្ថានភាព |

#### កំណត់ត្រានាំចេញ Markdown តិចបំផុត

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  
#### ឧទាហរណ៍សំណុំ Prompt Deterministic

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
វាយ prompt តាមបញ្ជីថេរមិនបំរែបំរួលជំនួសការជ្រើសរើសចៃដន្យ សម្រាប់វិមាត្រការប្រៀបធៀបលើកំណែផែនការបន្តៗ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬភាពមិនត្រឹមត្រូវបាន។ ឯកសារដើមជាភាសាទូទៅគួរត្រូវបានយកជាដើមទុនដ៏ទៃសម្រាប់ព័ត៌មានណាមួយ។ សម្រាប់ព័ត៌មានសំខាន់ សូមណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសដែលកើតឡើងពីការប្រើប្រាស់បកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->