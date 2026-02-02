# ಸೆಷನ್ 3: ಫೌಂಡ್ರಿ ಲೋಕಲ್‌ನಲ್ಲಿ ಓಪನ್-ಸೋರ್ಸ್ ಮಾದರಿಗಳು

## ಸಾರಾಂಶ

ಹಗ್ಗಿಂಗ್ ಫೇಸ್ ಮತ್ತು ಇತರ ಓಪನ್-ಸೋರ್ಸ್ ಮಾದರಿಗಳನ್ನು ಫೌಂಡ್ರಿ ಲೋಕಲ್‌ಗೆ ಹೇಗೆ ತರಬೇಕು ಎಂಬುದನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ. ಆಯ್ಕೆ ತಂತ್ರಗಳು, ಸಮುದಾಯ ಕೊಡುಗೆ ಕಾರ್ಯಪ್ರವಾಹಗಳು, ಕಾರ್ಯಕ್ಷಮತೆ ಹೋಲಿಕೆ ವಿಧಾನಶಾಸ್ತ್ರ ಮತ್ತು ಕಸ್ಟಮ್ ಮಾದರಿ ನೋಂದಣಿಗಳನ್ನು ಬಳಸಿ ಫೌಂಡ್ರಿಯನ್ನು ವಿಸ್ತರಿಸುವ ವಿಧಾನವನ್ನು ತಿಳಿಯಿರಿ. ಈ ಸೆಷನ್ ವಾರದ "ಮಾದರಿ ಸೋಮವಾರಗಳು" ಅನ್ವೇಷಣಾ ಥೀಮ್‌ಗಳಿಗೆ ಹೊಂದಿಕೆಯಾಗಿದ್ದು, ನೀವು ಓಪನ್-ಸೋರ್ಸ್ ಮಾದರಿಗಳನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಮೌಲ್ಯಮಾಪನ ಮಾಡಿ ಕಾರ್ಯಗತಗೊಳಿಸಲು ಮತ್ತು ನಂತರ ಅದನ್ನು ಅಜೂರ್‌ಗೆ ವಿಸ್ತರಿಸಲು ಸಜ್ಜಾಗಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಅಂತ್ಯಕ್ಕೆ ನೀವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- **ಹುಡುಕಿ & ಮೌಲ್ಯಮಾಪನ ಮಾಡಿ**: ಗುಣಮಟ್ಟ ಮತ್ತು ಸಂಪನ್ಮೂಲ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಆಧರಿಸಿ ಅಭ್ಯರ್ಥಿ ಮಾದರಿಗಳನ್ನು (ಮಿಸ್ಟ್ರಲ್, ಜೆಮ್ಮಾ, ಕ್ವೆನ್, ಡೀಪ್ಸೀಕ್) ಗುರುತಿಸಿ.
- **ಲೋಡ್ ಮಾಡಿ & ಚಾಲನೆ ಮಾಡಿ**: ಫೌಂಡ್ರಿ ಲೋಕಲ್ CLI ಬಳಸಿ ಸಮುದಾಯ ಮಾದರಿಗಳನ್ನು ಡೌನ್‌ಲೋಡ್, ಕ್ಯಾಶ್ ಮತ್ತು ಪ್ರಾರಂಭಿಸಿ.
- **ಬೆಂಚ್‌ಮಾರ್ಕ್ ಮಾಡಿ**: ಸತತ ಲೇಟೆನ್ಸಿ + ಟೋಕನ್ ಥ್ರೂಪುಟ್ + ಗುಣಮಟ್ಟದ ನಿಯಮಗಳನ್ನು ಅನ್ವಯಿಸಿ.
- **ವಿಸ್ತರಿಸಿ**: SDK-ಸಮ್ಮತ ಮಾದರಿ ರ್ಯಾಪರ್ ಅನ್ನು ನೋಂದಣಿ ಅಥವಾ ಹೊಂದಿಸಿ.
- **ಹೋಲಿಸಿ**: SLM ಮತ್ತು ಮಧ್ಯಮ ಗಾತ್ರದ LLM ಆಯ್ಕೆ ನಿರ್ಣಯಗಳಿಗೆ ರಚನಾತ್ಮಕ ಹೋಲಿಕೆಗಳನ್ನು ತಯಾರಿಸಿ.

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- ಸೆಷನ್‌ಗಳು 1 ಮತ್ತು 2 ಪೂರ್ಣಗೊಂಡಿವೆ
- `foundry-local-sdk` ಹೊಂದಿರುವ ಪೈಥಾನ್ ಪರಿಸರ
- ಹಲವಾರು ಮಾದರಿ ಕ್ಯಾಶ್‌ಗಳಿಗೆ ಕನಿಷ್ಠ 15GB ಖಾಲಿ ಡಿಸ್ಕ್

### ಕ್ರಾಸ್-ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಪರಿಸರ ತ್ವರಿತ ಪ್ರಾರಂಭ

ವಿಂಡೋಸ್ ಪವರ್‌ಶೆಲ್:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
ಮ್ಯಾಕ್‌ಒಎಸ್ / ಲಿನಕ್ಸ:  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
ಮ್ಯಾಕ್‌ಒಎಸ್‌ನಿಂದ ವಿಂಡೋಸ್ ಹೋಸ್ಟ್ ಸೇವೆಗೆ ಬೆಂಚ್‌ಮಾರ್ಕ್ ಮಾಡುವಾಗ, ಸೆಟ್ ಮಾಡಿ:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## ಡೆಮೋ ಫ್ಲೋ (30 ನಿಮಿಷ)

### 1. CLI ಮೂಲಕ ಹಗ್ಗಿಂಗ್ ಫೇಸ್ ಮಾದರಿಗಳನ್ನು ಲೋಡ್ ಮಾಡಿ (8 ನಿಮಿಷ)

```powershell
# ಪಟ್ಟಿಯ ಕ್ಯಾಟಲಾಗ್ ಎಂಟ್ರಿಗಳನ್ನು (ಅಗತ್ಯವಿದ್ದರೆ ಕೈಯಿಂದ ಫಿಲ್ಟರ್ ಮಾಡಿ)
foundry model list

# ಹೋಲಿಕೆ ಗುರಿಗಳ ಒಂದು ಸೆಟ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# ಕ್ಯಾಶೆ ಪರಿಶೀಲಿಸಿ
foundry cache list
```
  
### 2. ಚಾಲನೆ ಮಾಡಿ & ತ್ವರಿತ ಪರೀಕ್ಷೆ (5 ನಿಮಿಷ)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  
### 3. ಬೆಂಚ್‌ಮಾರ್ಕ್ ಸ್ಕ್ರಿಪ್ಟ್ (8 ನಿಮಿಷ)

`samples/03-oss-models/benchmark_models.py` ರಚಿಸಿ:

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
  
ಚಾಲನೆ ಮಾಡಿ:

```powershell
python samples/03-oss-models/benchmark_models.py
```
  
### 4. ಕಾರ್ಯಕ್ಷಮತೆ ಹೋಲಿಕೆ (5 ನಿಮಿಷ)

ಲೋಡ್ ಸಮಯ, ಮೆಮೊರಿ ಫುಟ್‌ಪ್ರಿಂಟ್ (ಟಾಸ್ಕ್ ಮ್ಯಾನೇಜರ್ / `nvidia-smi` / OS ಸಂಪನ್ಮೂಲ ಮಾನಿಟರ್ ನೋಡಿ), ಔಟ್‌ಪುಟ್ ಗುಣಮಟ್ಟ ಮತ್ತು ವೇಗದ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಚರ್ಚಿಸಿ. ಪೈಥಾನ್ ಬೆಂಚ್‌ಮಾರ್ಕ್ ಸ್ಕ್ರಿಪ್ಟ್ (ಸೆಷನ್ 3) ಬಳಸಿ ಲೇಟೆನ್ಸಿ ಮತ್ತು ಥ್ರೂಪುಟ್; GPU ವೇಗವರ್ಧನೆ ಸಕ್ರಿಯಗೊಳಿಸಿದ ನಂತರ ಪುನರಾವರ್ತಿಸಿ.

### 5. ಪ್ರಾರಂಭಿಕ ಪ್ರಾಜೆಕ್ಟ್ (4 ನಿಮಿಷ)

ಮಾದರಿ ಹೋಲಿಕೆ ವರದಿ ಜನರೇಟರ್ ರಚಿಸಿ (ಬೆಂಚ್‌ಮಾರ್ಕ್ ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ಮಾರ್ಕ್‌ಡೌನ್ ರಫ್ತು ಜೊತೆಗೆ ವಿಸ್ತರಿಸಿ).

## ಪ್ರಾರಂಭಿಕ ಪ್ರಾಜೆಕ್ಟ್: `03-huggingface-models` ವಿಸ್ತರಿಸಿ

ಇದೀಗಿನ ಮಾದರಿಯನ್ನು ಸುಧಾರಿಸಿ:

1. ಬೆಂಚ್‌ಮಾರ್ಕ್ ಸಂಗ್ರಹಣೆ + CSV/ಮಾರ್ಕ್‌ಡೌನ್ ಔಟ್‌ಪುಟ್ ಸೇರಿಸಿ.
2. ಸರಳ ಗುಣಮಟ್ಟದ ಅಂಕಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ (ಪ್ರಾಂಪ್ಟ್ ಜೋಡಿ ಸೆಟ್ + ಕೈಯಿಂದ ಟಿಪ್ಪಣಿ ಸ್ಟಬ್ ಫೈಲ್).
3. ಪ್ಲಗ್‌ಅಬಲ್ ಮಾದರಿ ಪಟ್ಟಿ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ ಸೆಟ್‌ಗಾಗಿ JSON ಕಾನ್ಫಿಗ್ (`models.json`) ಪರಿಚಯಿಸಿ.

## ಮಾನ್ಯತೆ ಪರಿಶೀಲನಾ ಪಟ್ಟಿಕೆ

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
ಎಲ್ಲಾ ಗುರಿ ಮಾದರಿಗಳು ಕಾಣಿಸಬೇಕು ಮತ್ತು ಪ್ರೋಬ್ ಚಾಟ್ ವಿನಂತಿಗೆ ಪ್ರತಿಕ್ರಿಯಿಸಬೇಕು.

## ಮಾದರಿ ದೃಶ್ಯ ಮತ್ತು ಕಾರ್ಯಾಗಾರ ನಕ್ಷೆ

| ಕಾರ್ಯಾಗಾರ ಸ್ಕ್ರಿಪ್ಟ್ | ದೃಶ್ಯ | ಗುರಿ | ಪ್ರಾಂಪ್ಟ್ / ಡೇಟಾಸೆಟ್ ಮೂಲ |
|---------------------|--------|-------|---------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | ಎಡ್ಜ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ತಂಡವು ಎम्बೆಡ್ಡೆಡ್ ಸಮಾರೈಸರ್‌ಗೆ ಡೀಫಾಲ್ಟ್ SLM ಆಯ್ಕೆಮಾಡುವುದು | ಅಭ್ಯರ್ಥಿ ಮಾದರಿಗಳ ನಡುವೆ ಲೇಟೆನ್ಸಿ + p95 + ಟೋಕನ್ಸ್/ಸೆಕ್ ಹೋಲಿಕೆ ತಯಾರಿಸಿ | ಇನ್‌ಲೈನ್ `PROMPT` ವ್ಯಾರಿ + ಪರಿಸರ `BENCH_MODELS` ಪಟ್ಟಿ |

### ದೃಶ್ಯ ಕಥನ  
ಉತ್ಪನ್ನ ಎಂಜಿನಿಯರಿಂಗ್ ತಂಡವು ಆಫ್‌ಲೈನ್ ಮೀಟಿಂಗ್-ನೋಟ್ಸ್ ವೈಶಿಷ್ಟ್ಯಕ್ಕಾಗಿ ಡೀಫಾಲ್ಟ್ ಲಘು ತೂಕದ ಸಮಾರೈಸರ್ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಬೇಕು. ಅವರು ನಿಯಂತ್ರಿತ ನಿರ್ಧಾರಾತ್ಮಕ ಬೆಂಚ್‌ಮಾರ್ಕ್‌ಗಳನ್ನು (ತಾಪಮಾನ=0) ನಿಗದಿತ ಪ್ರಾಂಪ್ಟ್ ಸೆಟ್‌ನಲ್ಲಿ ನಡೆಸುತ್ತಾರೆ ಮತ್ತು ಲೇಟೆನ್ಸಿ + ಥ್ರೂಪುಟ್ ಮೆಟ್ರಿಕ್‌ಗಳನ್ನು GPU ವೇಗವರ್ಧನೆ ಸಕ್ರಿಯಗೊಳಿಸುವ ಮೊದಲು ಮತ್ತು ನಂತರ ಸಂಗ್ರಹಿಸುತ್ತಾರೆ.

### ಉದಾಹರಣಾ ಪ್ರಾಂಪ್ಟ್ ಸೆಟ್ JSON (ವಿಸ್ತರಿಸಬಹುದಾದ)  
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
ಪ್ರತಿ ಮಾದರಿಗಾಗಿ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಲೂಪ್ ಮಾಡಿ, ಪ್ರತಿ ಪ್ರಾಂಪ್ಟ್ ಲೇಟೆನ್ಸಿಯನ್ನು ಹಿಡಿದು ವಿತರಣೆ ಮೆಟ್ರಿಕ್‌ಗಳನ್ನು ಮತ್ತು ಹೊರಗಿನ ಮೌಲ್ಯಗಳನ್ನು ಪತ್ತೆಮಾಡಿ.

## ಮಾದರಿ ಆಯ್ಕೆ ಚಟುವಟಿಕೆ

| ಆಯಾಮ | ಮೆಟ್ರಿಕ್ | ಮಹತ್ವವೇನು |
|--------|----------|-------------|
| ಲೇಟೆನ್ಸಿ | ಸರಾಸರಿ / p95 | ಬಳಕೆದಾರ ಅನುಭವದ ಸ್ಥಿರತೆ |
| ಥ್ರೂಪುಟ್ | ಟೋಕನ್ಸ್/ಸೆಕ್ | ಬ್ಯಾಚ್ ಮತ್ತು ಸ್ಟ್ರೀಮಿಂಗ್ ವಿಸ್ತರಣೆ |
| ಮೆಮೊರಿ | ರೆಸಿಡೆಂಟ್ ಗಾತ್ರ | ಸಾಧನ ಹೊಂದಿಕೆ ಮತ್ತು ಸಮಕಾಲೀನತೆ |
| ಗುಣಮಟ್ಟ | ರೂಬ್ರಿಕ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳು | ಕಾರ್ಯ ಸೂಕ್ತತೆ |
| ಫುಟ್‌ಪ್ರಿಂಟ್ | ಡಿಸ್ಕ್ ಕ್ಯಾಶ್ | ವಿತರಣೆ ಮತ್ತು ನವೀಕರಣಗಳು |
| ಪರವಾನಗಿ | ಬಳಕೆ ಅನುಮತಿ | ವಾಣಿಜ್ಯ ಅನುಕೂಲತೆ |

## ಕಸ್ಟಮ್ ಮಾದರಿಯೊಂದಿಗೆ ವಿಸ್ತರಣೆ

ಹೆಚ್ಚಿನ ಮಟ್ಟದ ಮಾದರಿ (ಪ್ಸ್ಯೂಡೋ):

```python
# ಸುಡೋ_ಅಡಾಪ್ಟರ್.py (ಸಿದ್ಧಾಂತಾತ್ಮಕ)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# ಸ್ಥಳೀಯ ಮಾರ್ಗದರ್ಶನದೊಂದಿಗೆ ನೋಂದಣಿ (ಭವಿಷ್ಯ ವಿಸ್ತರಣಾ ಬಿಂದು)
```
  
ಅಡಾಪ್ಟರ್ ಇಂಟರ್ಫೇಸ್‌ಗಳ ಅಭಿವೃದ್ಧಿಗಾಗಿ ಅಧಿಕೃತ ರೆಪೊವನ್ನು ನೋಡಿ:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

| ಸಮಸ್ಯೆ | ಕಾರಣ | ಪರಿಹಾರ |
|---------|--------|---------|
| ಮಿಸ್ಟ್ರಲ್-7b ನಲ್ಲಿ OOM | RAM/GPU ಕೊರತೆ | ಇತರ ಮಾದರಿಗಳನ್ನು ನಿಲ್ಲಿಸಿ; ಸಣ್ಣ ರೂಪಾಂತರ ಪ್ರಯತ್ನಿಸಿ |
| ಮೊದಲ ಪ್ರತಿಕ್ರಿಯೆ ನಿಧಾನ | ಶೀತಲ ಲೋಡ್ | ನಿಯಮಿತ ಲಘು ತೂಕದ ಪ್ರಾಂಪ್ಟ್ ಮೂಲಕ ತಾಪಮಾನ ಇಡಿ |
| ಡೌನ್‌ಲೋಡ್ ನಿಲ್ಲುತ್ತದೆ | ನೆಟ್‌ವರ್ಕ್ ಅಸ್ಥಿರತೆ | ಮರುಪ್ರಯತ್ನಿಸಿ; ಆಫ್-ಪೀಕ್ ಸಮಯದಲ್ಲಿ ಪೂರ್ವಹೊಂದಿಕೆ ಮಾಡಿ |

## ಉಲ್ಲೇಖಗಳು

- ಫೌಂಡ್ರಿ ಲೋಕಲ್ SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- ಮಾದರಿ ಸೋಮವಾರಗಳು: https://aka.ms/model-mondays  
- ಹಗ್ಗಿಂಗ್ ಫೇಸ್ ಮಾದರಿ ಅನ್ವೇಷಣೆ: https://huggingface.co/models

---

**ಸೆಷನ್ ಅವಧಿ**: 30 ನಿಮಿಷ (+ ಐಚ್ಛಿಕ ಆಳವಾದ ಅಧ್ಯಯನ)  
**ಕಷ್ಟದ ಮಟ್ಟ**: ಮಧ್ಯಮ

### ಐಚ್ಛಿಕ ಸುಧಾರಣೆಗಳು

| ಸುಧಾರಣೆ | ಲಾಭ | ಹೇಗೆ |
|-----------|--------|-------|
| ಸ್ಟ್ರೀಮಿಂಗ್ ಮೊದಲ ಟೋಕನ್ ಲೇಟೆನ್ಸಿ | ಗ್ರಾಹಕ ಅನುಭವದ ಪ್ರತಿಕ್ರಿಯಾಶೀಲತೆ ಅಳೆಯುತ್ತದೆ | `BENCH_STREAM=1` ಜೊತೆ ಬೆಂಚ್‌ಮಾರ್ಕ್ ನಡೆಸಿ (`Workshop/samples/session03` ನಲ್ಲಿ ಸುಧಾರಿತ ಸ್ಕ್ರಿಪ್ಟ್) |
| ನಿರ್ಧಾರಾತ್ಮಕ ಮೋಡ್ | ಸ್ಥಿರ ರಿಗ್ರೆಷನ್ ಹೋಲಿಕೆಗಳು | `temperature=0`, ನಿಗದಿತ ಪ್ರಾಂಪ್ಟ್ ಸೆಟ್, JSON ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ಆವೃತ್ತಿ ನಿಯಂತ್ರಣದಲ್ಲಿ ಹಿಡಿಯಿರಿ |
| ಗುಣಮಟ್ಟ ರೂಬ್ರಿಕ್ ಅಂಕಗಳು | ಗುಣಮಟ್ಟದ ಆಯಾಮ ಸೇರಿಸುತ್ತದೆ | ನಿರೀಕ್ಷಿತ ಅಂಶಗಳೊಂದಿಗೆ `prompts.json` ಅನ್ನು ನಿರ್ವಹಿಸಿ; ಅಂಕಗಳನ್ನು ಕೈಯಿಂದ ಅಥವಾ ದ್ವಿತೀಯ ಮಾದರಿಯಿಂದ ಟಿಪ್ಪಣಿ ಮಾಡಿ |
| CSV / ಮಾರ್ಕ್‌ಡೌನ್ ರಫ್ತು | ಹಂಚಿಕೊಳ್ಳಬಹುದಾದ ವರದಿ | `benchmark_report.md` ಅನ್ನು ಟೇಬಲ್ ಮತ್ತು ಮುಖ್ಯಾಂಶಗಳೊಂದಿಗೆ ಬರೆಯಲು ಸ್ಕ್ರಿಪ್ಟ್ ವಿಸ್ತರಿಸಿ |
| ಮಾದರಿ ಸಾಮರ್ಥ್ಯ ಟ್ಯಾಗ್‌ಗಳು | ನಂತರ ಸ್ವಯಂಚಾಲಿತ ಮಾರ್ಗದರ್ಶನಕ್ಕೆ ಸಹಾಯ | `{alias: {capabilities:[], size_mb:..}}` ಹೊಂದಿರುವ `models.json` ನಿರ್ವಹಿಸಿ |
| ಕ್ಯಾಶ್ ವಾರ್ಮ್‌ಅಪ್ ಹಂತ | ಶೀತಲ ಪ್ರಾರಂಭ ಬಯಾಸ್ ಕಡಿಮೆ ಮಾಡಿ | ಸಮಯ ಲೂಪ್ ಮೊದಲು ಒಂದು ವಾರ್ಮ್ ರೌಂಡ್ ನಡೆಸಿ (ಇದೀಗ ಅನುಷ್ಠಾನಗೊಂಡಿದೆ) |
| ಶತಮಾನಿಕ ಶುದ್ಧತೆ | ಬಲವಾದ ಟೇಲ್ ಲೇಟೆನ್ಸಿ | numpy ಶತಮಾನಿಕ ಬಳಸಿ (ಇದೀಗ ಪುನರ್‌ರಚಿಸಲಾದ ಸ್ಕ್ರಿಪ್ಟ್‌ನಲ್ಲಿ ಇದೆ) |
| ಟೋಕನ್ ವೆಚ್ಚ ಅಂದಾಜು | ಆರ್ಥಿಕ ಹೋಲಿಕೆ | ಅಂದಾಜು ವೆಚ್ಚ = (ಟೋಕನ್ಸ್/ಸೆಕ್ * ಪ್ರತಿ ವಿನಂತಿಯ ಸರಾಸರಿ ಟೋಕನ್ಸ್) * ಶಕ್ತಿ ನಿಯಮ |
| ವಿಫಲವಾದ ಮಾದರಿಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಬಿಟ್ಟುಹಾಕುವುದು | ಬ್ಯಾಚ್ ಚಾಲನೆಗಳಲ್ಲಿ ಸ್ಥಿರತೆ | ಪ್ರತಿ ಬೆಂಚ್‌ಮಾರ್ಕ್ ಅನ್ನು try/except ನಲ್ಲಿ ಮುಚ್ಚಿ ಮತ್ತು ಸ್ಥಿತಿ ಕ್ಷೇತ್ರವನ್ನು ಗುರುತಿಸಿ |

#### ಕನಿಷ್ಠ ಮಾರ್ಕ್‌ಡೌನ್ ರಫ್ತು ತುಣುಕು

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  
#### ನಿರ್ಧಾರಾತ್ಮಕ ಪ್ರಾಂಪ್ಟ್ ಸೆಟ್ ಉದಾಹರಣೆ

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
ಹೋಲಿಕೆಗಾಗಿ ರ್ಯಾಂಡಮ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳ ಬದಲು ಸ್ಥಿರ ಪಟ್ಟಿಯನ್ನು ಲೂಪ್ ಮಾಡಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->