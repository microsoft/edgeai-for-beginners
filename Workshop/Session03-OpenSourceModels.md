# Session 3: Open-Source Models in Foundry Local

## Abstract

Discover how to bring Hugging Face and other open-source models into Foundry Local. Learn selection strategies, community contribution workflows, performance comparison methodology, and how to extend Foundry with custom model registrations. This session maps to the weekly "Model Mondays" exploration themes and equips you to evaluate and operationalize open-source models locally before scaling to Azure.

## Learning Objectives

By the end you will be able to:

- **Discover & Evaluate**: Identify candidate models (mistral, gemma, qwen, deepseek) using quality vs resource trade-offs.
- **Load & Run**: Use Foundry Local CLI to download, cache, and launch community models.
- **Benchmark**: Apply consistent latency + token throughput + quality heuristics.
- **Extend**: Register or adapt a custom model wrapper following SDK-compatible patterns.
- **Compare**: Produce structured comparisons for SLM vs mid-size LLM selection decisions.

## Prerequisites

- Sessions 1 & 2 completed
- Python environment with `foundry-local-sdk` installed
- At least 15GB free disk for multiple model caches

### Cross-Platform Environment Quick Start

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

When benchmarking from macOS against a Windows host service, set:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Demo Flow (30 min)

### 1. Load Hugging Face Models via CLI (8 min)

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

### 2. Run & Quick Probe (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. Benchmark Script (8 min)

Create `samples/03-oss-models/benchmark_models.py`:

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

Run:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. Compare Performance (5 min)

Discuss trade-offs: load time, memory footprint (observe Task Manager / `nvidia-smi` / OS resource monitor), output quality vs speed. Use the Python benchmark script (Session 3) for latency & throughput; repeat after enabling GPU acceleration.

### 5. Starter Project (4 min)

Create a model comparison report generator (extend benchmarking script with markdown export).

## Starter Project: Extend `03-huggingface-models`

Enhance the existing sample by:

1. Adding benchmark aggregation + CSV/Markdown output.
2. Implementing simple qualitative scoring (prompt pair set + manual annotation stub file).
3. Introducing a JSON config (`models.json`) for pluggable model list & prompt set.

## Validation Checklist

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

All target models should appear and respond to a probe chat request.

## Sample Scenario & Workshop Mapping

| Workshop Script | Scenario | Goal | Prompt / Dataset Source |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge platform team selecting default SLM for embedded summarizer | Produce latency + p95 + tokens/sec comparison across candidate models | Inline `PROMPT` var + environment `BENCH_MODELS` list |

### Scenario Narrative
Product engineering must choose a default lightweight summarization model for an offline meeting-notes feature. They run controlled deterministic benchmarks (temperature=0) across a fixed prompt set (see example below) and collect latency + throughput metrics with and without GPU acceleration.

### Example Prompt Set JSON (expandable)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Loop each prompt per model, capture per‑prompt latency to derive distribution metrics and detect outliers.

## Model Selection Framework

| Dimension | Metric | Why It Matters |
|----------|--------|----------------|
| Latency | avg / p95 | User experience consistency |
| Throughput | tokens/sec | Batch & streaming scalability |
| Memory | resident size | Device fit & concurrency |
| Quality | rubric prompts | Task suitability |
| Footprint | disk cache | Distribution & updates |
| License | use allowance | Commercial compliance |

## Extending With Custom Model

High-level pattern (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Consult the official repo for evolving adapter interfaces:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| OOM on mistral-7b | Insufficient RAM/GPU | Stop other models; try smaller variant |
| Slow first response | Cold load | Keep warm with a periodic lightweight prompt |
| Download stalls | Network instability | Retry; prefetch during off-peak |

## References

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Session Duration**: 30 min (+ optional deep dive)  
**Difficulty**: Intermediate

### Optional Enhancements

| Enhancement | Benefit | How |
|-------------|---------|-----|
| Streaming First-Token Latency | Measures perceived responsiveness | Run benchmark with `BENCH_STREAM=1` (enhanced script in `Workshop/samples/session03`) |
| Deterministic Mode | Stable regression comparisons | `temperature=0`, fixed prompt set, capture JSON outputs under version control |
| Quality Rubric Scoring | Adds qualitative dimension | Maintain `prompts.json` with expected facets; annotate scores (1–5) manually or via secondary model |
| CSV / Markdown Export | Shareable report | Extend script to write `benchmark_report.md` with table & highlights |
| Model Capability Tags | Helps automated routing later | Maintain `models.json` with `{alias: {capabilities:[], size_mb:..}}` |
| Cache Warmup Phase | Reduce cold-start bias | Execute one warm round before timing loop (already implemented) |
| Percentile Accuracy | Robust tail latency | Use numpy percentile (already in refactored script) |
| Token Cost Approximation | Economic comparison | Approx cost = (tokens/sec * avg tokens per request) * energy heuristic |
| Auto-Skipping Failed Models | Resilience in batch runs | Wrap each benchmark in try/except and mark status field |

#### Minimal Markdown Export Snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Deterministic Prompt Set Example

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Loop the static list instead of random prompts for comparable metrics across commits.
