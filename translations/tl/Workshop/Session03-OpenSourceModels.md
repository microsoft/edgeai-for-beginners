<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:56:01+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "tl"
}
-->
# Session 3: Mga Open-Source Model sa Foundry Local

## Abstrak

Alamin kung paano dalhin ang Hugging Face at iba pang open-source na mga modelo sa Foundry Local. Matutunan ang mga estratehiya sa pagpili, mga workflow para sa kontribusyon ng komunidad, metodolohiya ng paghahambing ng performance, at kung paano palawakin ang Foundry gamit ang custom na pagrehistro ng modelo. Ang sesyon na ito ay tumutugma sa lingguhang tema ng "Model Mondays" at magbibigay sa iyo ng kakayahan upang suriin at gamitin ang mga open-source na modelo nang lokal bago ito i-scale sa Azure.

## Mga Layunin sa Pag-aaral

Sa pagtatapos ng sesyon, magagawa mo ang:

- **Pagdiskubre at Pagsusuri**: Tukuyin ang mga kandidato na modelo (mistral, gemma, qwen, deepseek) gamit ang trade-offs sa kalidad at resources.
- **Pag-load at Pagpatakbo**: Gamitin ang Foundry Local CLI upang mag-download, mag-cache, at magpatakbo ng mga modelo mula sa komunidad.
- **Benchmarking**: Mag-apply ng pare-parehong latency + token throughput + quality heuristics.
- **Pagpapalawak**: Magrehistro o mag-adapt ng custom na model wrapper na sumusunod sa mga pattern na compatible sa SDK.
- **Paghahambing**: Gumawa ng structured na paghahambing para sa SLM vs mid-size LLM na mga desisyon sa pagpili.

## Mga Kinakailangan

- Natapos ang Sessions 1 & 2
- Python environment na may naka-install na `foundry-local-sdk`
- Hindi bababa sa 15GB na libreng disk space para sa maraming model cache

### Mabilis na Pagsisimula sa Cross-Platform Environment

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

Kapag nagbe-benchmark mula sa macOS laban sa Windows host service, itakda:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 minuto)

### 1. Pag-load ng Hugging Face Models gamit ang CLI (8 minuto)

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


### 2. Pagpatakbo at Mabilis na Pagsusuri (5 minuto)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Benchmark Script (8 minuto)

Gumawa ng `samples/03-oss-models/benchmark_models.py`:

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

Patakbuhin:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Paghahambing ng Performance (5 minuto)

Talakayin ang trade-offs: oras ng pag-load, memory footprint (obserbahan ang Task Manager / `nvidia-smi` / OS resource monitor), kalidad ng output laban sa bilis. Gamitin ang Python benchmark script (Session 3) para sa latency at throughput; ulitin pagkatapos i-enable ang GPU acceleration.

### 5. Starter Project (4 minuto)

Gumawa ng generator para sa ulat ng paghahambing ng modelo (palawakin ang benchmarking script gamit ang markdown export).

## Starter Project: Palawakin ang `03-huggingface-models`

Pagandahin ang umiiral na sample sa pamamagitan ng:

1. Pagdaragdag ng benchmark aggregation + CSV/Markdown output.
2. Pagpapatupad ng simpleng qualitative scoring (prompt pair set + manual annotation stub file).
3. Pagpapakilala ng JSON config (`models.json`) para sa pluggable na listahan ng modelo at prompt set.

## Validation Checklist

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Lahat ng target na modelo ay dapat lumitaw at tumugon sa isang probe chat request.

## Sample Scenario at Workshop Mapping

| Workshop Script | Scenario | Layunin | Pinagmulan ng Prompt / Dataset |
|-----------------|----------|---------|--------------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge platform team na pumipili ng default na SLM para sa embedded summarizer | Gumawa ng latency + p95 + tokens/sec na paghahambing sa mga kandidato na modelo | Inline `PROMPT` var + environment `BENCH_MODELS` list |

### Narrative ng Scenario

Ang product engineering ay kailangang pumili ng default na lightweight summarization model para sa offline na feature ng meeting-notes. Gumagawa sila ng kontroladong deterministic benchmarks (temperature=0) sa isang fixed prompt set (tingnan ang halimbawa sa ibaba) at nangongolekta ng latency + throughput metrics na may at walang GPU acceleration.

### Halimbawa ng Prompt Set JSON (maaaring palawakin)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

I-loop ang bawat prompt sa bawat modelo, kunin ang latency sa bawat prompt upang makuha ang mga distribution metrics at matukoy ang mga outliers.

## Framework sa Pagpili ng Modelo

| Dimensyon | Sukatan | Bakit Mahalaga |
|-----------|---------|----------------|
| Latency | avg / p95 | Konsistensya ng karanasan ng user |
| Throughput | tokens/sec | Scalability ng batch at streaming |
| Memory | resident size | Pagkakasya sa device at concurrency |
| Kalidad | rubric prompts | Angkop para sa task |
| Footprint | disk cache | Pamamahagi at mga update |
| Lisensya | pahintulot sa paggamit | Pagsunod sa komersyal na regulasyon |

## Pagpapalawak Gamit ang Custom na Modelo

High-level na pattern (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konsultahin ang opisyal na repo para sa mga umuusbong na adapter interfaces:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Pag-aayos ng Problema

| Isyu | Sanhi | Solusyon |
|------|-------|----------|
| OOM sa mistral-7b | Hindi sapat na RAM/GPU | Itigil ang ibang mga modelo; subukan ang mas maliit na variant |
| Mabagal na unang tugon | Cold load | Panatilihing mainit gamit ang periodic na magaan na prompt |
| Pagkaantala sa pag-download | Kawalan ng katatagan sa network | Subukang muli; mag-prefetch sa oras na hindi abala |

## Mga Sanggunian

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Model Mondays: https://aka.ms/model-mondays  
- Hugging Face Model Discovery: https://huggingface.co/models  

---

**Tagal ng Sesyon**: 30 minuto (+ opsyonal na mas malalim na talakayan)  
**Kahirapan**: Intermediate

### Opsyonal na Mga Pagpapahusay

| Pagpapahusay | Benepisyo | Paano |
|--------------|-----------|-------|
| Streaming First-Token Latency | Sinusukat ang perceived responsiveness | Patakbuhin ang benchmark gamit ang `BENCH_STREAM=1` (pinahusay na script sa `Workshop/samples/session03`) |
| Deterministic Mode | Matatag na paghahambing ng regression | `temperature=0`, fixed prompt set, kunin ang JSON outputs sa ilalim ng version control |
| Quality Rubric Scoring | Nagdaragdag ng qualitative na dimensyon | Panatilihin ang `prompts.json` na may inaasahang aspeto; mag-annotate ng scores (1–5) nang manu-mano o gamit ang pangalawang modelo |
| CSV / Markdown Export | Maibabahaging ulat | Palawakin ang script upang magsulat ng `benchmark_report.md` na may table at highlights |
| Model Capability Tags | Tinutulungan ang automated routing sa hinaharap | Panatilihin ang `models.json` na may `{alias: {capabilities:[], size_mb:..}}` |
| Cache Warmup Phase | Binabawasan ang cold-start bias | Magpatakbo ng isang warm round bago ang timing loop (naipatupad na) |
| Percentile Accuracy | Mas matibay na tail latency | Gamitin ang numpy percentile (na nasa refactored script na) |
| Token Cost Approximation | Paghahambing sa ekonomiya | Approx cost = (tokens/sec * avg tokens per request) * energy heuristic |
| Auto-Skipping Failed Models | Resilience sa batch runs | I-wrap ang bawat benchmark sa try/except at markahan ang status field |

#### Minimal Markdown Export Snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Halimbawa ng Deterministic Prompt Set

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

I-loop ang static na listahan sa halip na random na mga prompt para sa maihahambing na mga sukatan sa bawat commit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->