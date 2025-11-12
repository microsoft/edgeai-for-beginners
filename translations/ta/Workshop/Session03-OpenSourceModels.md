<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-12T00:59:30+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "ta"
}
-->
# அமர்வு 3: Foundry Local இல் திறந்த மூல மாடல்கள்

## சுருக்கம்

Hugging Face மற்றும் பிற திறந்த மூல மாடல்களை Foundry Local இல் கொண்டு வருவது எப்படி என்பதை அறிக. தேர்வு உத்திகள், சமூக பங்களிப்பு பணிமுறைகள், செயல்திறன் ஒப்பீட்டு முறைமைகள் மற்றும் Foundry ஐ தனிப்பயன் மாடல் பதிவுகளுடன் விரிவாக்குவது எப்படி என்பதை கற்றுக்கொள்ளுங்கள். இந்த அமர்வு வாராந்திர "Model Mondays" ஆராய்ச்சி கருப்பொருள்களுடன் இணைக்கப்படுகிறது மற்றும் Azure க்கு பரவுவதற்கு முன் திறந்த மூல மாடல்களை உள்ளூர் அளவில் மதிப்பீடு செய்து செயல்படுத்த உங்களை சீரமைக்கிறது.

## கற்றல் நோக்கங்கள்

இவ்வமர்வு முடிவில், நீங்கள்:

- **கண்டறிந்து மதிப்பீடு செய்ய**: தரம் மற்றும் வளங்களின் சமநிலையைப் பயன்படுத்தி (mistral, gemma, qwen, deepseek போன்ற) மாடல்களை அடையாளம் காணவும்.
- **ஏற்றவும் இயக்கவும்**: Foundry Local CLI ஐப் பயன்படுத்தி சமூக மாடல்களை பதிவிறக்கவும், சேமிக்கவும், இயக்கவும்.
- **மதிப்பீடு செய்ய**: நிலையான தாமதம் + டோக்கன் துரிதம் + தரம் குறியீடுகளைப் பயன்படுத்தவும்.
- **விரிவாக்கம் செய்ய**: SDK-இன் இணக்கமான வடிவமைப்புகளைப் பின்பற்றி தனிப்பயன் மாடல் மடக்குகளை பதிவு செய்யவும் அல்லது மாற்றவும்.
- **ஒப்பிடவும்**: SLM மற்றும் நடுத்தர அளவிலான LLM தேர்வு முடிவுகளுக்கான அமைந்த ஒப்பீடுகளை உருவாக்கவும்.

## முன் தேவைகள்

- அமர்வுகள் 1 மற்றும் 2 முடிக்கப்பட்டிருக்க வேண்டும்
- `foundry-local-sdk` நிறுவப்பட்ட Python சூழல்
- பல மாடல் சேமிப்புகளுக்காக குறைந்தது 15GB இலவச டிஸ்க் இடம்

### குறுக்குவெளி சூழல் விரைவான தொடக்கம்

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

macOS இல் இருந்து Windows ஹோஸ்ட் சேவையை எதிர்த்து மதிப்பீடு செய்யும்போது அமைக்கவும்:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## டெமோ ஓட்டம் (30 நிமிடங்கள்)

### 1. CLI மூலம் Hugging Face மாடல்களை ஏற்றுதல் (8 நிமிடங்கள்)

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

### 2. இயக்கவும் & விரைவான சோதனை (5 நிமிடங்கள்)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. மதிப்பீட்டு ஸ்கிரிப்ட் (8 நிமிடங்கள்)

`samples/03-oss-models/benchmark_models.py` உருவாக்கவும்:

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

இயக்கவும்:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. செயல்திறன் ஒப்பீடு (5 நிமிடங்கள்)

சந்தேகங்கள்: ஏற்றுமதி நேரம், நினைவக அளவு (Task Manager / `nvidia-smi` / OS resource monitor ஐ கவனிக்கவும்), வெளியீட்டு தரம் மற்றும் வேகம். Python மதிப்பீட்டு ஸ்கிரிப்டை (Session 3) தாமதம் மற்றும் துரிதத்திற்காக பயன்படுத்தவும்; GPU வேகத்தை இயக்கிய பிறகு மீண்டும் முயற்சிக்கவும்.

### 5. தொடக்க திட்டம் (4 நிமிடங்கள்)

மதிப்பீட்டு ஸ்கிரிப்டுடன் மார்க்டவுன் ஏற்றுமதியை விரிவாக்கி மாடல் ஒப்பீட்டு அறிக்கை உருவாக்கவும்.

## தொடக்க திட்டம்: `03-huggingface-models` ஐ விரிவாக்கவும்

இருப்பிலுள்ள மாதிரியை மேம்படுத்த:

1. மதிப்பீட்டு தொகுப்பு + CSV/Markdown வெளியீட்டைச் சேர்க்கவும்.
2. எளிய தரமான மதிப்பீட்டைப் (prompt pair set + கையேடு குறிப்பு கோப்பு) செயல்படுத்தவும்.
3. JSON கட்டமைப்பை (`models.json`) அறிமுகப்படுத்தவும், மாடல் பட்டியல் மற்றும் prompt தொகுப்புக்கான இணைக்கக்கூடிய அமைப்பாக.

## சரிபார்ப்பு சோதனை பட்டியல்

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

எல்லா இலக்கு மாடல்களும் தோன்ற வேண்டும் மற்றும் ஒரு சோதனை உரையாடல் கோரிக்கைக்கு பதிலளிக்க வேண்டும்.

## மாதிரி சூழ்நிலை & பணிமனை வரைபடம்

| பணிமனை ஸ்கிரிப்ட் | சூழ்நிலை | இலக்கு | Prompt / Dataset மூலங்கள் |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge பிளாட்ஃபார்ம் குழு எம்பெடட் சுருக்கி பயன்பாட்டிற்கான இயல்புநிலை SLM ஐத் தேர்ந்தெடுக்கும் | வேகத்தன்மை + p95 + டோக்கன்கள்/வினாடி ஒப்பீடு | Inline `PROMPT` var + சூழல் `BENCH_MODELS` பட்டியல் |

### சூழ்நிலை விளக்கம்
தயாரிப்பு பொறியியல் குழு ஆஃப்லைன் கூட்டம்-குறிப்புகள் அம்சத்திற்கான இயல்புநிலை இலகு சுருக்க மாடலைத் தேர்ந்தெடுக்க வேண்டும். அவர்கள் கட்டுப்படுத்தப்பட்ட தீர்மானமான மதிப்பீடுகளை (temperature=0) ஒரு நிர்ணய prompt தொகுப்பில் (கீழே உள்ள உதாரணத்தைப் பார்க்கவும்) இயக்கி, GPU வேகத்தை இயக்கியதன் பிறகு தாமதம் + துரிதம் அளவுகோல்களை சேகரிக்கின்றனர்.

### உதாரண Prompt தொகுப்பு JSON (விரிவாக்கக்கூடியது)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

ஒவ்வொரு மாடலுக்கும் ஒவ்வொரு prompt ஐ முறைப்படி இயக்கி, ஒவ்வொரு prompt தாமதத்தைப் பதிவு செய்து விநியோக அளவுகோல்களை உருவாக்கவும் மற்றும் வெளிப்படையானவற்றை கண்டறியவும்.

## மாடல் தேர்வு அமைப்பு

| பரிமாணம் | அளவுகோல் | ஏன் இது முக்கியம் |
|----------|--------|----------------|
| தாமதம் | சராசரி / p95 | பயனர் அனுபவத்தின் நிலைத்தன்மை |
| துரிதம் | டோக்கன்கள்/வினாடி | தொகுதி மற்றும் ஸ்ட்ரீமிங் அளவீடு |
| நினைவகம் | நிலையான அளவு | சாதன பொருத்தம் மற்றும் ஒருங்கிணைப்பு |
| தரம் | rubric prompts | பணிக்கான பொருத்தம் |
| தடம் | டிஸ்க் சேமிப்பு | விநியோகம் மற்றும் புதுப்பிப்புகள் |
| உரிமம் | பயன்பாட்டு அனுமதி | வணிக இணக்கம் |

## தனிப்பயன் மாடலுடன் விரிவாக்கம்

உயர் நிலை முறை (பசுடோ):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

மாறும் அடாப்டர் இடைமுகங்களுக்கான அதிகாரப்பூர்வ களஞ்சியத்தைப் பாருங்கள்:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## சிக்கல்களை சரிசெய்தல்

| சிக்கல் | காரணம் | தீர்வு |
|-------|-------|-----|
| OOM on mistral-7b | போதுமான RAM/GPU இல்லை | பிற மாடல்களை நிறுத்தவும்; சிறிய மாறுபாட்டை முயற்சிக்கவும் |
| முதல் பதில் மெதுவாக | குளிர் ஏற்றுதல் | ஒரு காலாண்டு லேசான prompt ஐப் பயன்படுத்தி சூடாக வைத்திருங்கள் |
| பதிவிறக்கம் தடைபடுகிறது | நெட்வொர்க் நிலைத்தன்மை | மீண்டும் முயற்சிக்கவும்; பிக்அவர்களுக்கு முன் பதிவிறக்கவும் |

## குறிப்புகள்

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**அமர்வு காலம்**: 30 நிமிடங்கள் (+ விருப்பமான ஆழமான ஆராய்ச்சி)  
**சிரமம்**: நடுத்தர

### விருப்பமான மேம்பாடுகள்

| மேம்பாடு | நன்மை | எப்படி |
|-------------|---------|-----|
| ஸ்ட்ரீமிங் முதல்-டோக்கன் தாமதம் | உணரப்பட்ட பதிலளிப்பு அளவீடு | `BENCH_STREAM=1` (விரிவாக்கப்பட்ட ஸ்கிரிப்ட் `Workshop/samples/session03` இல்) மூலம் மதிப்பீடு இயக்கவும் |
| தீர்மானமான முறை | நிலையான பின்வாங்கல் ஒப்பீடுகள் | `temperature=0`, நிர்ணய prompt தொகுப்பு, JSON வெளியீடுகளை பதிப்பு கட்டுப்பாட்டின் கீழ் பதிவு செய்யவும் |
| தரம் மதிப்பீட்டு மதிப்பீடு | தரமான பரிமாணத்தைச் சேர்க்கிறது | `prompts.json` ஐ எதிர்பார்க்கப்படும் அம்சங்களுடன் பராமரிக்கவும்; மதிப்பீடுகளை (1–5) கையேடு அல்லது இரண்டாம் நிலை மாடல் மூலம் குறிக்கவும் |
| CSV / Markdown ஏற்றுமதி | பகிரக்கூடிய அறிக்கை | `benchmark_report.md` ஐ அட்டவணை மற்றும் முக்கிய அம்சங்களுடன் எழுத ஸ்கிரிப்டை விரிவாக்கவும் |
| மாடல் திறன் குறிச்சொற்கள் | பின்னர் தானியங்கிய வழிமுறைக்கு உதவுகிறது | `{alias: {capabilities:[], size_mb:..}}` உடன் `models.json` ஐ பராமரிக்கவும் |
| Cache Warmup கட்டம் | குளிர்-தொடக்க பாகுபாட்டை குறைக்கிறது | நேரத்தை அளவிடும் சுற்றுக்கு முன் ஒரு சூடான சுற்றைச் செயல்படுத்தவும் (ஏற்கனவே செயல்படுத்தப்பட்டுள்ளது) |
| சதவீத துல்லியம் | வலுவான வால் தாமதம் | numpy சதவீதத்தைப் பயன்படுத்தவும் (ஏற்கனவே மறுசீரமைக்கப்பட்ட ஸ்கிரிப்டில் உள்ளது) |
| டோக்கன் செலவு மதிப்பீடு | பொருளாதார ஒப்பீடு | சராசரி கோரிக்கைக்கு (tokens/sec * avg tokens) * ஆற்றல் அளவுகோல் மூலம் சுமார் செலவு |
| தோல்வியடைந்த மாடல்களை தானாகத் தவிர்க்கிறது | தொகுதி இயக்கங்களில் நிலைத்தன்மை | ஒவ்வொரு மதிப்பீட்டையும் try/except இல் மடக்கி நிலை புலத்தை குறிக்கவும் |

#### குறைந்தபட்ச மார்க்டவுன் ஏற்றுமதி துணுக்குகள்

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### தீர்மானமான Prompt தொகுப்பு உதாரணம்

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

நிரந்தரமான பட்டியலை commit களுக்கிடையே ஒப்பிடக்கூடிய அளவுகோல்களுக்கு பயன்படுத்தவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->