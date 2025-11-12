<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T22:38:59+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "pa"
}
-->
# ਸੈਸ਼ਨ 3: Foundry Local ਵਿੱਚ ਓਪਨ-ਸੋਰਸ ਮਾਡਲ

## ਸਾਰ

Foundry Local ਵਿੱਚ Hugging Face ਅਤੇ ਹੋਰ ਓਪਨ-ਸੋਰਸ ਮਾਡਲ ਲਿਆਉਣ ਦੇ ਤਰੀਕੇ ਸਿੱਖੋ। ਚੋਣ ਦੀਆਂ ਰਣਨੀਤੀਆਂ, ਕਮਿਊਨਿਟੀ ਯੋਗਦਾਨ ਵਰਕਫਲੋ, ਪ੍ਰਦਰਸ਼ਨ ਦੀ ਤੁਲਨਾ ਵਿਧੀ ਅਤੇ Foundry ਨੂੰ ਕਸਟਮ ਮਾਡਲ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਨਾਲ ਵਧਾਉਣ ਦੇ ਤਰੀਕੇ ਸਿੱਖੋ। ਇਹ ਸੈਸ਼ਨ ਹਫਤਾਵਾਰ "Model Mondays" ਖੋਜ ਥੀਮਾਂ ਨਾਲ ਜੁੜਦਾ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਓਪਨ-ਸੋਰਸ ਮਾਡਲਾਂ ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਮੁਲਾਂਕਣ ਅਤੇ ਚਲਾਉਣ ਲਈ ਸਾਜ਼ੋ-ਸਾਮਾਨ ਦਿੰਦਾ ਹੈ, Azure ਵਿੱਚ ਸਕੇਲ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਸੈਸ਼ਨ ਦੇ ਅੰਤ ਤੱਕ ਤੁਸੀਂ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੋਵੋਗੇ:

- **ਖੋਜ ਅਤੇ ਮੁਲਾਂਕਣ**: ਗੁਣਵੱਤਾ ਅਤੇ ਸਰੋਤਾਂ ਦੇ ਵਪਾਰ-ਅਫਸੋਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਉਮੀਦਵਾਰ ਮਾਡਲਾਂ (mistral, gemma, qwen, deepseek) ਦੀ ਪਛਾਣ ਕਰੋ।
- **ਲੋਡ ਅਤੇ ਚਲਾਓ**: Foundry Local CLI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਮਿਊਨਿਟੀ ਮਾਡਲਾਂ ਨੂੰ ਡਾਊਨਲੋਡ, ਕੈਸ਼ ਅਤੇ ਲਾਂਚ ਕਰੋ।
- **ਬੈਂਚਮਾਰਕ**: ਲਗਾਤਾਰ latency + ਟੋਕਨ throughput + ਗੁਣਵੱਤਾ ਹਿਊਰਿਸਟਿਕਸ ਲਾਗੂ ਕਰੋ।
- **ਵਧਾਓ**: SDK-ਅਨੁਕੂਲ ਪੈਟਰਨਾਂ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹੋਏ ਕਸਟਮ ਮਾਡਲ ਵ੍ਰੈਪਰ ਨੂੰ ਰਜਿਸਟਰ ਜਾਂ ਅਨੁਕੂਲਿਤ ਕਰੋ।
- **ਤੁਲਨਾ ਕਰੋ**: SLM ਅਤੇ ਮਿਡ-ਸਾਈਜ਼ LLM ਚੋਣ ਦੇ ਫੈਸਲੇ ਲਈ ਸੰਰਚਿਤ ਤੁਲਨਾਵਾਂ ਤਿਆਰ ਕਰੋ।

## ਪੂਰਵ ਸ਼ਰਤਾਂ

- ਸੈਸ਼ਨ 1 ਅਤੇ 2 ਪੂਰੇ ਕੀਤੇ
- Python ਵਾਤਾਵਰਣ ਜਿਸ ਵਿੱਚ `foundry-local-sdk` ਇੰਸਟਾਲ ਹੈ
- ਕਈ ਮਾਡਲ ਕੈਸ਼ ਲਈ ਘੱਟੋ-ਘੱਟ 15GB ਖਾਲੀ ਡਿਸਕ

### ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਵਾਤਾਵਰਣ ਕਵਿਕ ਸਟਾਰਟ

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

macOS ਤੋਂ Windows ਹੋਸਟ ਸੇਵਾ ਵਿਰੁੱਧ ਬੈਂਚਮਾਰਕਿੰਗ ਕਰਦੇ ਸਮੇਂ ਸੈਟ ਕਰੋ:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ਡੈਮੋ ਫਲੋ (30 ਮਿੰਟ)

### 1. CLI ਰਾਹੀਂ Hugging Face ਮਾਡਲ ਲੋਡ ਕਰੋ (8 ਮਿੰਟ)

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


### 2. ਚਲਾਓ ਅਤੇ ਤੁਰੰਤ ਜਾਂਚ ਕਰੋ (5 ਮਿੰਟ)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. ਬੈਂਚਮਾਰਕ ਸਕ੍ਰਿਪਟ (8 ਮਿੰਟ)

`samples/03-oss-models/benchmark_models.py` ਬਣਾਓ:

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

ਚਲਾਓ:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. ਪ੍ਰਦਰਸ਼ਨ ਦੀ ਤੁਲਨਾ ਕਰੋ (5 ਮਿੰਟ)

ਵਿਚਾਰ ਕਰੋ: ਲੋਡ ਕਰਨ ਦਾ ਸਮਾਂ, ਮੈਮੋਰੀ ਫੁਟਪ੍ਰਿੰਟ (Task Manager / `nvidia-smi` / OS resource monitor ਦੇਖੋ), ਆਉਟਪੁੱਟ ਗੁਣਵੱਤਾ ਵਿਰੁੱਧ ਗਤੀ। latency ਅਤੇ throughput ਲਈ Python ਬੈਂਚਮਾਰਕ ਸਕ੍ਰਿਪਟ (ਸੈਸ਼ਨ 3) ਦੀ ਵਰਤੋਂ ਕਰੋ; GPU ਤੀਵਰਤਾ ਨੂੰ ਯੋਗ ਕਰਨ ਤੋਂ ਬਾਅਦ ਦੁਹਰਾਓ।

### 5. ਸਟਾਰਟਰ ਪ੍ਰੋਜੈਕਟ (4 ਮਿੰਟ)

ਮਾਡਲ ਤੁਲਨਾ ਰਿਪੋਰਟ ਜਨਰੇਟਰ ਬਣਾਓ (ਬੈਂਚਮਾਰਕਿੰਗ ਸਕ੍ਰਿਪਟ ਨੂੰ ਮਾਰਕਡਾਊਨ ਐਕਸਪੋਰਟ ਨਾਲ ਵਧਾਓ)।

## ਸਟਾਰਟਰ ਪ੍ਰੋਜੈਕਟ: `03-huggingface-models` ਨੂੰ ਵਧਾਓ

ਮੌਜੂਦਾ ਨਮੂਨੇ ਨੂੰ ਵਧਾਓ:

1. ਬੈਂਚਮਾਰਕ ਏਗਰੀਗੇਸ਼ਨ + CSV/Markdown ਆਉਟਪੁੱਟ ਸ਼ਾਮਲ ਕਰੋ।
2. ਸਧਾਰਨ ਗੁਣਵੱਤਾ ਸਕੋਰਿੰਗ (ਪ੍ਰੋਮਪਟ ਪੈਰ ਸੈੱਟ + ਮੈਨੂਅਲ ਐਨੋਟੇਸ਼ਨ ਸਟਬ ਫਾਈਲ) ਲਾਗੂ ਕਰੋ।
3. JSON ਕਨਫਿਗ (`models.json`) ਸ਼ਾਮਲ ਕਰੋ ਜੋ ਕਿ ਮਾਡਲ ਲਿਸਟ ਅਤੇ ਪ੍ਰੋਮਪਟ ਸੈੱਟ ਲਈ ਪਲੱਗਗੇਬਲ ਹੋਵੇ।

## ਵੈਰੀਫਿਕੇਸ਼ਨ ਚੈੱਕਲਿਸਟ

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

ਸਾਰੇ ਟਾਰਗੇਟ ਮਾਡਲ ਦਿਖਾਈ ਦੇਣੇ ਚਾਹੀਦੇ ਹਨ ਅਤੇ ਇੱਕ ਪ੍ਰੋਬ ਚੈਟ ਬੇਨਤੀ ਦਾ ਜਵਾਬ ਦੇਣ ਦੇ ਯੋਗ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ।

## ਨਮੂਨਾ ਸਥਿਤੀ ਅਤੇ ਵਰਕਸ਼ਾਪ ਮੈਪਿੰਗ

| ਵਰਕਸ਼ਾਪ ਸਕ੍ਰਿਪਟ | ਸਥਿਤੀ | ਉਦੇਸ਼ | ਪ੍ਰੋਮਪਟ / ਡਾਟਾਸੈੱਟ ਸਰੋਤ |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | ਐਜ ਪਲੇਟਫਾਰਮ ਟੀਮ ਜੋ ਐਂਬੈਡਿਡ ਸਮਰੀਜ਼ਰ ਲਈ ਡਿਫਾਲਟ SLM ਦੀ ਚੋਣ ਕਰ ਰਹੀ ਹੈ | ਉਮੀਦਵਾਰ ਮਾਡਲਾਂ ਵਿੱਚ latency + p95 + tokens/sec ਦੀ ਤੁਲਨਾ ਤਿਆਰ ਕਰੋ | Inline `PROMPT` var + environment `BENCH_MODELS` list |

### ਸਥਿਤੀ ਕਹਾਣੀ

ਉਤਪਾਦ ਇੰਜੀਨੀਅਰਿੰਗ ਨੂੰ ਇੱਕ ਆਫਲਾਈਨ ਮੀਟਿੰਗ-ਨੋਟਸ ਫੀਚਰ ਲਈ ਡਿਫਾਲਟ ਹਲਕਾ ਸਮਰੀਕਰਨ ਮਾਡਲ ਦੀ ਚੋਣ ਕਰਨੀ ਪੈਂਦੀ ਹੈ। ਉਹ ਨਿਰਧਾਰਤ ਡਿਟਰਮਿਨਿਸਟਿਕ ਬੈਂਚਮਾਰਕ (temperature=0) ਨੂੰ ਇੱਕ ਫਿਕਸਡ ਪ੍ਰੋਮਪਟ ਸੈੱਟ 'ਤੇ ਚਲਾਉਂਦੇ ਹਨ (ਹੇਠਾਂ ਦਿੱਤੇ ਉਦਾਹਰਣ ਵੇਖੋ) ਅਤੇ GPU ਤੀਵਰਤਾ ਦੇ ਨਾਲ ਅਤੇ ਬਿਨਾ latency + throughput ਮੈਟ੍ਰਿਕਸ ਇਕੱਠੇ ਕਰਦੇ ਹਨ।

### ਉਦਾਹਰਣ ਪ੍ਰੋਮਪਟ ਸੈੱਟ JSON (ਵਧਾਉਣਯੋਗ)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

ਹਰੇਕ ਮਾਡਲ ਪ੍ਰਤੀ ਹਰੇਕ ਪ੍ਰੋਮਪਟ ਨੂੰ ਲੂਪ ਕਰੋ, ਪ੍ਰਤੀ-ਪ੍ਰੋਮਪਟ latency ਨੂੰ ਕੈਪਚਰ ਕਰੋ ਤਾਂ ਜੋ ਵੰਡ ਮੈਟ੍ਰਿਕਸ ਅਤੇ ਆਊਟਲਾਇਰਜ਼ ਦੀ ਪਛਾਣ ਕੀਤੀ ਜਾ ਸਕੇ।

## ਮਾਡਲ ਚੋਣ ਫਰੇਮਵਰਕ

| ਪਹਲੂ | ਮੈਟ੍ਰਿਕ | ਇਹ ਕਿਉਂ ਮਹੱਤਵਪੂਰਨ ਹੈ |
|----------|--------|----------------|
| Latency | avg / p95 | ਯੂਜ਼ਰ ਅਨੁਭਵ ਦੀ ਲਗਾਤਾਰਤਾ |
| Throughput | tokens/sec | ਬੈਚ ਅਤੇ ਸਟ੍ਰੀਮਿੰਗ ਸਕੇਲਬਿਲਟੀ |
| Memory | resident size | ਡਿਵਾਈਸ ਫਿਟ ਅਤੇ ਕਨਕਰੰਸੀ |
| Quality | rubric prompts | ਟਾਸਕ ਯੋਗਤਾ |
| Footprint | disk cache | ਵੰਡ ਅਤੇ ਅਪਡੇਟ |
| License | use allowance | ਵਪਾਰਕ ਅਨੁਕੂਲਤਾ |

## ਕਸਟਮ ਮਾਡਲ ਨਾਲ ਵਧਾਉਣਾ

ਉੱਚ-ਪੱਧਰ ਪੈਟਰਨ (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

ਵਧ ਰਹੇ ਐਡਾਪਟਰ ਇੰਟਰਫੇਸ ਲਈ ਅਧਿਕਾਰਤ ਰਿਪੋ ਦੀ ਸਲਾਹ ਲਵੋ:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## ਸਮੱਸਿਆ ਹੱਲ

| ਸਮੱਸਿਆ | ਕਾਰਨ | ਹੱਲ |
|-------|-------|-----|
| mistral-7b 'ਤੇ OOM | ਅਪਰਯਾਪਤ RAM/GPU | ਹੋਰ ਮਾਡਲਾਂ ਨੂੰ ਰੋਕੋ; ਛੋਟੇ ਵੈਰੀਐਂਟ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ |
| ਪਹਿਲਾ ਜਵਾਬ ਧੀਮਾ | ਠੰਡਾ ਲੋਡ | ਇੱਕ ਪੀਰੀਓਡਿਕ ਹਲਕਾ ਪ੍ਰੋਮਪਟ ਨਾਲ ਗਰਮ ਰੱਖੋ |
| ਡਾਊਨਲੋਡ ਰੁਕ ਜਾਂਦਾ ਹੈ | ਨੈਟਵਰਕ ਅਸਥਿਰਤਾ | ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ; ਆਫ-ਪੀਕ ਦੌਰਾਨ ਪ੍ਰੀਫੈਚ ਕਰੋ |

## ਸੰਦਰਭ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**ਸੈਸ਼ਨ ਦੀ ਮਿਆਦ**: 30 ਮਿੰਟ (+ ਵਿਕਲਪਿਕ ਡੀਪ ਡਾਈਵ)  
**ਕਠਿਨਾਈ**: ਮੱਧਮ

### ਵਿਕਲਪਿਕ ਸੁਧਾਰ

| ਸੁਧਾਰ | ਲਾਭ | ਕਿਵੇਂ |
|-------------|---------|-----|
| Streaming First-Token Latency | ਮਹਿਸੂਸ ਕੀਤੀ ਗਈ ਜਵਾਬਦੇਹੀ ਨੂੰ ਮਾਪਦਾ ਹੈ | `BENCH_STREAM=1` ਨਾਲ ਬੈਂਚਮਾਰਕ ਚਲਾਓ (ਵਧਾਏ ਗਏ ਸਕ੍ਰਿਪਟ ਵਿੱਚ `Workshop/samples/session03`) |
| Deterministic Mode | ਸਥਿਰ ਰਿਗਰੈਸ਼ਨ ਤੁਲਨਾਵਾਂ | `temperature=0`, ਫਿਕਸਡ ਪ੍ਰੋਮਪਟ ਸੈੱਟ, JSON ਆਉਟਪੁੱਟ ਨੂੰ ਵਰਜਨ ਕੰਟਰੋਲ ਹੇਠ ਕੈਪਚਰ ਕਰੋ |
| Quality Rubric Scoring | ਗੁਣਵੱਤਾ ਦਾ ਪਹਲੂ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ | `prompts.json` ਨੂੰ ਉਮੀਦਵਾਰ ਪਹਲੂਆਂ ਨਾਲ ਰੱਖੋ; ਸਕੋਰ (1–5) ਨੂੰ ਮੈਨੂਅਲ ਜਾਂ ਦੂਜੇ ਮਾਡਲ ਰਾਹੀਂ ਐਨੋਟੇਟ ਕਰੋ |
| CSV / Markdown Export | ਸਾਂਝੇ ਕਰਨ ਯੋਗ ਰਿਪੋਰਟ | ਸਕ੍ਰਿਪਟ ਨੂੰ `benchmark_report.md` ਲਿਖਣ ਲਈ ਵਧਾਓ ਜਿਸ ਵਿੱਚ ਟੇਬਲ ਅਤੇ ਹਾਈਲਾਈਟਸ ਹੋਣ |
| Model Capability Tags | ਬਾਅਦ ਵਿੱਚ ਆਟੋਮੈਟਿਕ ਰੂਟਿੰਗ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ | `{alias: {capabilities:[], size_mb:..}}` ਨਾਲ `models.json` ਨੂੰ ਰੱਖੋ |
| Cache Warmup Phase | ਠੰਡੇ-ਸ਼ੁਰੂ ਬਾਇਸ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ | ਟਾਈਮਿੰਗ ਲੂਪ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਗਰਮ ਰਾਊਂਡ ਚਲਾਓ (ਪਹਿਲਾਂ ਹੀ ਲਾਗੂ ਕੀਤਾ ਗਿਆ) |
| Percentile Accuracy | ਮਜ਼ਬੂਤ ਟੇਲ latency | numpy percentile ਦੀ ਵਰਤੋਂ ਕਰੋ (ਪਹਿਲਾਂ ਹੀ refactored ਸਕ੍ਰਿਪਟ ਵਿੱਚ) |
| Token Cost Approximation | ਆਰਥਿਕ ਤੁਲਨਾ | ਲਗਭਗ ਖਰਚ = (tokens/sec * avg tokens per request) * energy heuristic |
| Auto-Skipping Failed Models | ਬੈਚ ਰਨ ਵਿੱਚ ਲਚਕਦਾਰਤਾ | ਹਰ ਬੈਂਚਮਾਰਕ ਨੂੰ try/except ਵਿੱਚ ਲਪੇਟੋ ਅਤੇ ਸਥਿਤੀ ਫੀਲਡ ਨੂੰ ਚਿੰਨ੍ਹਿਤ ਕਰੋ |

#### ਨਿਊਨਤਮ ਮਾਰਕਡਾਊਨ ਐਕਸਪੋਰਟ ਸਨਿੱਪਟ

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### ਨਿਰਧਾਰਤ ਪ੍ਰੋਮਪਟ ਸੈੱਟ ਉਦਾਹਰਣ

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

ਸਥਿਰ ਮੈਟ੍ਰਿਕਸ ਲਈ ਕਮਿਟਸ ਵਿੱਚ ਸਥਿਰ ਸੂਚੀ ਨੂੰ ਲੂਪ ਕਰੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->