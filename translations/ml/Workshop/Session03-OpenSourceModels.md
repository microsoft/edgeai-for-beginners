# സെഷൻ 3: ഫൗണ്ട്രി ലോക്കലിൽ ഓപ്പൺ-സോഴ്‌സ് മോഡലുകൾ

## സംക്ഷേപം

ഹഗ്ഗിംഗ് ഫെയ്‌സ് ഉൾപ്പെടെയുള്ള മറ്റ് ഓപ്പൺ-സോഴ്‌സ് മോഡലുകൾ ഫൗണ്ട്രി ലോക്കലിലേക്ക് എങ്ങനെ കൊണ്ടുവരാമെന്ന് കണ്ടെത്തുക. തിരഞ്ഞെടുപ്പ് തന്ത്രങ്ങൾ, കമ്മ്യൂണിറ്റി സംഭാവന പ്രവാഹങ്ങൾ, പ്രകടന താരതമ്യ രീതി, ഫൗണ്ട്രി കസ്റ്റം മോഡൽ രജിസ്ട്രേഷനുകൾ ഉപയോഗിച്ച് എങ്ങനെ വിപുലീകരിക്കാമെന്ന് പഠിക്കുക. ഈ സെഷൻ ആഴ്ചവാര "മോഡൽ മണ്ടേസ്" അന്വേഷണ വിഷയങ്ങളുമായി പൊരുത്തപ്പെടുന്നു, കൂടാതെ ഓപ്പൺ-സോഴ്‌സ് മോഡലുകൾ ലോക്കലായി വിലയിരുത്തി പ്രവർത്തനക്ഷമമാക്കാൻ സഹായിക്കുന്നു, പിന്നീട് അത് ആസ്യൂറിലേക്ക് സ്കെയിൽ ചെയ്യാം.

## പഠന ലക്ഷ്യങ്ങൾ

അവസാനിക്കുമ്പോൾ നിങ്ങൾക്ക് കഴിയും:

- **കണ്ടെത്തുക & വിലയിരുത്തുക**: ഗുണനിലവാരവും വിഭവങ്ങളുടെ വ്യാപാര-offs ഉപയോഗിച്ച് സ്ഥാനാർത്ഥി മോഡലുകൾ (mistral, gemma, qwen, deepseek) തിരിച്ചറിയുക.
- **ലോഡ് & ഓടിക്കുക**: ഫൗണ്ട്രി ലോക്കൽ CLI ഉപയോഗിച്ച് കമ്മ്യൂണിറ്റി മോഡലുകൾ ഡൗൺലോഡ്, കാഷ്, ആരംഭിക്കുക.
- **ബെഞ്ച്മാർക്ക്**: സ്ഥിരമായ ലാറ്റൻസി + ടോക്കൺ ത്രൂപുട്ട് + ഗുണനിലവാര ഹ്യൂറിസ്റ്റിക്സ് പ്രയോഗിക്കുക.
- **വിപുലീകരിക്കുക**: SDK-സമർത്ഥമായ മാതൃകകൾ പിന്തുടർന്ന് കസ്റ്റം മോഡൽ റാപ്പർ രജിസ്റ്റർ ചെയ്യുക അല്ലെങ്കിൽ അനുയോജ്യമായി മാറ്റം വരുത്തുക.
- **താരതമ്യം ചെയ്യുക**: SLM vs മിഡ്-സൈസ് LLM തിരഞ്ഞെടുപ്പ് തീരുമാനങ്ങൾക്ക് ഘടനാപരമായ താരതമ്യങ്ങൾ സൃഷ്ടിക്കുക.

## മുൻകൂട്ടി ആവശ്യങ്ങൾ

- സെഷനുകൾ 1 & 2 പൂർത്തിയായി
- `foundry-local-sdk` ഇൻസ്റ്റാൾ ചെയ്ത പൈത്തൺ പരിസ്ഥിതി
- നിരവധി മോഡൽ കാഷുകൾക്കായി കുറഞ്ഞത് 15GB ഫ്രീ ഡിസ്ക്

### ക്രോസ്-പ്ലാറ്റ്ഫോം പരിസ്ഥിതി ക്വിക്ക് സ്റ്റാർട്ട്

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
  
macOS-ൽ നിന്ന് Windows ഹോസ്റ്റ് സർവീസിനെതിരെ ബെഞ്ച്മാർക്ക് ചെയ്യുമ്പോൾ, സജ്ജമാക്കുക:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ഡെമോ ഫ്ലോ (30 മിനിറ്റ്)

### 1. CLI വഴി Hugging Face മോഡലുകൾ ലോഡ് ചെയ്യുക (8 മിനിറ്റ്)

```powershell
# പട്ടിക കാറ്റലോഗ് എൻട്രികൾ (ആവശ്യമായാൽ കൈയോടെ ഫിൽട്ടർ ചെയ്യുക)
foundry model list

# താരതമ്യ ലക്ഷ്യങ്ങളുടെ ഒരു സെറ്റ് ഡൗൺലോഡ് ചെയ്യുക
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# കാഷെ സ്ഥിരീകരിക്കുക
foundry cache list
```
  
### 2. ഓടിക്കുക & ക്വിക്ക് പ്രോബിംഗ് (5 മിനിറ്റ്)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  
### 3. ബെഞ്ച്മാർക്ക് സ്ക്രിപ്റ്റ് (8 മിനിറ്റ്)

`samples/03-oss-models/benchmark_models.py` സൃഷ്ടിക്കുക:

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
  
ഓടിക്കുക:

```powershell
python samples/03-oss-models/benchmark_models.py
```
  
### 4. പ്രകടനം താരതമ്യം ചെയ്യുക (5 മിനിറ്റ്)

ട്രേഡ്-ഓഫുകൾ ചർച്ച ചെയ്യുക: ലോഡ് സമയം, മെമ്മറി ഫുട്പ്രിന്റ് (ടാസ്‌ക് മാനേജർ / `nvidia-smi` / OS റിസോഴ്‌സ് മോണിറ്റർ കാണുക), ഔട്ട്പുട്ട് ഗുണനിലവാരം vs വേഗം. പൈത്തൺ ബെഞ്ച്മാർക്ക് സ്ക്രിപ്റ്റ് (സെഷൻ 3) ലാറ്റൻസി & ത്രൂപുട്ടിനായി ഉപയോഗിക്കുക; GPU ആക്സിലറേഷൻ സജീവമാക്കിയ ശേഷം ആവർത്തിക്കുക.

### 5. സ്റ്റാർട്ടർ പ്രോജക്ട് (4 മിനിറ്റ്)

മോഡൽ താരതമ്യ റിപ്പോർട്ട് ജനറേറ്റർ സൃഷ്ടിക്കുക (ബെഞ്ച്മാർക്ക് സ്ക്രിപ്റ്റ് മാർക്ക്ഡൗൺ എക്സ്പോർട്ടുമായി വിപുലീകരിക്കുക).

## സ്റ്റാർട്ടർ പ്രോജക്ട്: `03-huggingface-models` വിപുലീകരിക്കുക

നിലവിലുള്ള സാമ്പിൾ മെച്ചപ്പെടുത്തുക:

1. ബെഞ്ച്മാർക്ക് ആഗ്രിഗേഷൻ + CSV/Markdown ഔട്ട്പുട്ട് ചേർക്കുക.
2. ലളിതമായ ഗുണനിലവാര സ്കോറിംഗ് നടപ്പിലാക്കുക (പ്രോംപ്റ്റ് ജോഡി സെറ്റ് + മാനുവൽ അനോട്ടേഷൻ സ്റ്റബ് ഫയൽ).
3. പ്ലഗ്ഗബിൾ മോഡൽ ലിസ്റ്റ് & പ്രോംപ്റ്റ് സെറ്റിനായി JSON കോൺഫിഗ് (`models.json`) പരിചയപ്പെടുത്തുക.

## സാധുത പരിശോധന പട്ടിക

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
എല്ലാ ലക്ഷ്യ മോഡലുകളും പ്രോബ്ചാറ്റ് അഭ്യർത്ഥനയ്ക്ക് പ്രതികരിക്കണം.

## സാമ്പിൾ സീനാരിയോ & വർക്ക്‌ഷോപ്പ് മാപ്പിംഗ്

| വർക്ക്‌ഷോപ്പ് സ്ക്രിപ്റ്റ് | സീനാരിയോ | ലക്ഷ്യം | പ്രോംപ്റ്റ് / ഡാറ്റാസെറ്റ് ഉറവിടം |
|-------------------------|----------|--------|-------------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | എഡ്ജ് പ്ലാറ്റ്ഫോം ടീം എംബെഡഡ് സംഗ്രഹകത്തിനായി ഡിഫോൾട്ട് SLM തിരഞ്ഞെടുക്കുന്നു | സ്ഥാനാർത്ഥി മോഡലുകൾക്കിടയിൽ ലാറ്റൻസി + p95 + ടോക്കൺ/സെക്കൻഡ് താരതമ്യം സൃഷ്ടിക്കുക | ഇൻലൈൻ `PROMPT` വാരി + പരിസ്ഥിതി `BENCH_MODELS` ലിസ്റ്റ് |

### സീനാരിയോ വിവരണം  
പ്രോഡക്റ്റ് എഞ്ചിനീയറിംഗ് ഓഫ്ലൈൻ മീറ്റിംഗ്-നോട്ട്സ് ഫീച്ചറിനായി ഡിഫോൾട്ട് ലൈറ്റ്‌വെയിറ്റ് സംഗ്രഹ മോഡൽ തിരഞ്ഞെടുക്കണം. അവർ നിയന്ത്രിത ഡിറ്റർമിനിസ്റ്റിക് ബെഞ്ച്മാർക്കുകൾ (temperature=0) സ്ഥിരമായ പ്രോംപ്റ്റ് സെറ്റിൽ നടത്തുകയും GPU ആക്സിലറേഷൻ ഉള്ളതും ഇല്ലാത്തതും ലാറ്റൻസി + ത്രൂപുട്ട് മെട്രിക്‌സ് ശേഖരിക്കുകയും ചെയ്യുന്നു.

### ഉദാഹരണ പ്രോംപ്റ്റ് സെറ്റ് JSON (വിപുലീകരിക്കാവുന്നതാണ്)  
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
ഓരോ മോഡലിനും ഓരോ പ്രോംപ്റ്റും ലൂപ്പ് ചെയ്ത്, പ്രോംപ്റ്റ്-പ്രതി ലാറ്റൻസി പിടിച്ച് വിതരണ മെട്രിക്‌സ് കണ്ടെത്തുകയും ഔട്ട്‌ലൈയർമാർ കണ്ടെത്തുകയും ചെയ്യുക.

## മോഡൽ തിരഞ്ഞെടുപ്പ് ഫ്രെയിംവർക്ക്

| അളവുകോണം | മെട്രിക് | പ്രാധാന്യം |
|------------|---------|------------|
| ലാറ്റൻസി | ശരാശരി / p95 | ഉപയോക്തൃ അനുഭവ സ്ഥിരത |
| ത്രൂപുട്ട് | ടോക്കൺ/സെക്കൻഡ് | ബാച്ച് & സ്ട്രീമിംഗ് സ്കെയിലബിലിറ്റി |
| മെമ്മറി | റെസിഡന്റ് സൈസ് | ഉപകരണം അനുയോജ്യത & സമകാലിക പ്രവർത്തനം |
| ഗുണനിലവാരം | റൂബ്രിക് പ്രോംപ്റ്റുകൾ | ടാസ്‌ക് അനുയോജ്യത |
| ഫുട്പ്രിന്റ് | ഡിസ്ക് കാഷ് | വിതരണം & അപ്‌ഡേറ്റുകൾ |
| ലൈസൻസ് | ഉപയോഗാനുമതി | വാണിജ്യ അനുസരണം |

## കസ്റ്റം മോഡലുമായി വിപുലീകരിക്കൽ

ഉയർന്ന തലത്തിലുള്ള മാതൃക (സ്യൂഡോ):

```python
# പ്സ്യൂഡോ_അഡാപ്റ്റർ.py (സങ്കൽപ്പാത്മകമായി)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# പ്രാദേശിക റൂട്ടിംഗുമായി രജിസ്റ്റർ ചെയ്യുക (ഭാവി വിപുലീകരണ ബിന്ദു)
```
  
അഡാപ്റ്റർ ഇന്റർഫേസുകൾ വികസിപ്പിക്കുന്നതിനായി ഔദ്യോഗിക റിപോ പരിശോധിക്കുക:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## പ്രശ്നപരിഹാരം

| പ്രശ്നം | കാരണം | പരിഹാരം |
|--------|---------|----------|
| mistral-7b-ൽ OOM | RAM/GPU അപര്യാപ്തം | മറ്റ് മോഡലുകൾ നിർത്തുക; ചെറിയ വകഭേദം പരീക്ഷിക്കുക |
| ആദ്യ പ്രതികരണം മന്ദം | കൊൾഡ് ലോഡ് | കാലാനുസൃതമായി ലളിതമായ പ്രോംപ്റ്റ് ഉപയോഗിച്ച് വാര്മ് നിലനിർത്തുക |
| ഡൗൺലോഡ് തടസം | നെറ്റ്‌വർക്ക് അസ്ഥിരത | വീണ്ടും ശ്രമിക്കുക; ഓഫ്പീക്ക് സമയത്ത് പ്രിഫെച്ച് ചെയ്യുക |

## റഫറൻസുകൾ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Model Mondays: https://aka.ms/model-mondays  
- Hugging Face Model Discovery: https://huggingface.co/models

---

**സെഷൻ ദൈർഘ്യം**: 30 മിനിറ്റ് (+ ഐച്ഛിക ഡീപ്പ് ഡൈവ്)  
**പ്രയാസം**: മധ്യസ്ഥ

### ഐച്ഛിക മെച്ചപ്പെടുത്തലുകൾ

| മെച്ചപ്പെടുത്തൽ | ഗുണം | എങ്ങനെ |
|---------------|--------|---------|
| സ്ട്രീമിംഗ് ഫസ്റ്റ്-ടോക്കൺ ലാറ്റൻസി | അനുഭവപ്രദമായ പ്രതികരണക്ഷമത അളക്കുന്നു | `BENCH_STREAM=1` ഉപയോഗിച്ച് ബെഞ്ച്മാർക്ക് ഓടിക്കുക (`Workshop/samples/session03`-ൽ മെച്ചപ്പെടുത്തിയ സ്ക്രിപ്റ്റ്) |
| ഡിറ്റർമിനിസ്റ്റിക് മോഡ് | സ്ഥിരമായ റിഗ്രഷൻ താരതമ്യങ്ങൾ | `temperature=0`, സ്ഥിരമായ പ്രോംപ്റ്റ് സെറ്റ്, JSON ഔട്ട്പുട്ടുകൾ വേർഷൻ നിയന്ത്രണത്തിൽ പിടിക്കുക |
| ഗുണനിലവാര റൂബ്രിക് സ്കോറിംഗ് | ഗുണനിലവാരപരമായ അളവുകോണം ചേർക്കുന്നു | പ്രതീക്ഷിച്ച ഫാസറ്റുകൾ ഉൾക്കൊള്ളുന്ന `prompts.json` നിലനിർത്തുക; സ്കോറുകൾ (1–5) മാനുവലായി അല്ലെങ്കിൽ സെക്കൻഡറി മോഡൽ വഴി അനോട്ടേറ്റ് ചെയ്യുക |
| CSV / Markdown എക്സ്പോർട്ട് | പങ്കുവെക്കാവുന്ന റിപ്പോർട്ട് | `benchmark_report.md` എഴുതാൻ സ്ക്രിപ്റ്റ് വിപുലീകരിക്കുക, പട്ടികയും ഹൈലൈറ്റുകളും ഉൾപ്പെടെ |
| മോഡൽ കഴിവ് ടാഗുകൾ | പിന്നീട് ഓട്ടോമേറ്റഡ് റൂട്ടിംഗ് സഹായിക്കുന്നു | `{alias: {capabilities:[], size_mb:..}}` ഉള്ള `models.json` നിലനിർത്തുക |
| കാഷ് വാര്മപ്പ് ഘട്ടം | കൊൾഡ്-സ്റ്റാർട്ട് ബയാസ് കുറയ്ക്കുന്നു | ടൈമിംഗ് ലൂപ്പിന് മുമ്പ് ഒരു വാര്മ് റൗണ്ട് നടത്തുക (ഇപ്പോൾ നടപ്പിലാക്കിയിട്ടുണ്ട്) |
| പേഴ്സന്റൈൽ കൃത്യത | ശക്തമായ ടെയിൽ ലാറ്റൻസി | numpy പേഴ്സന്റൈൽ ഉപയോഗിക്കുക (പുനഃസംഘടിപ്പിച്ച സ്ക്രിപ്റ്റിൽ ഇതിനകം ഉണ്ട്) |
| ടോക്കൺ ചെലവ് ഏകദേശം | സാമ്പത്തിക താരതമ്യം | ഏകദേശം ചെലവ് = (ടോക്കൺ/സെക്കൻഡ് * ശരാശരി ടോക്കൺസ് പ്രതി അഭ്യർത്ഥന) * ഊർജ്ജ ഹ്യൂറിസ്റ്റിക് |
| പരാജയപ്പെട്ട മോഡലുകൾ സ്വയം ഒഴിവാക്കൽ | ബാച്ച് ഓടലിൽ പ്രതിരോധം | ഓരോ ബെഞ്ച്മാർക്കും try/except ഉപയോഗിച്ച് ചുറ്റി സ്റ്റാറ്റസ് ഫീൽഡ് അടയാളപ്പെടുത്തുക |

#### ലഘു മാർക്ക്ഡൗൺ എക്സ്പോർട്ട് സ്നിപ്പറ്റ്

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  
#### ഡിറ്റർമിനിസ്റ്റിക് പ്രോംപ്റ്റ് സെറ്റ് ഉദാഹരണം

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
തുല്യമായ മെട്രിക്‌സിനായി റാൻഡം പ്രോംപ്റ്റുകൾക്ക് പകരം സ്റ്റാറ്റിക് ലിസ്റ്റ് ലൂപ്പ് ചെയ്യുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്രം ചെയ്ത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ വ്യാഖ്യാനക്കേടുകൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->