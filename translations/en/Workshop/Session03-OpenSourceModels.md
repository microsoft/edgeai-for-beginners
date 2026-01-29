# Session 3: Open-Source Models in Foundry Local

## Abstract

Learn how to integrate Hugging Face and other open-source models into Foundry Local. This session covers strategies for model selection, workflows for community contributions, methods for performance comparison, and extending Foundry with custom model registrations. It aligns with the weekly "Model Mondays" exploration themes and prepares you to evaluate and operationalize open-source models locally before scaling to Azure.

## Learning Objectives

By the end of this session, you will be able to:

- **Discover & Evaluate**: Identify potential models (mistral, gemma, qwen, deepseek) by balancing quality and resource requirements.
- **Load & Run**: Use Foundry Local CLI to download, cache, and execute community models.
- **Benchmark**: Apply consistent heuristics for latency, token throughput, and quality.
- **Extend**: Register or modify a custom model wrapper using SDK-compatible patterns.
- **Compare**: Create structured comparisons to guide decisions between SLM and mid-size LLMs.

## Prerequisites

- Completion of Sessions 1 & 2
- Python environment with `foundry-local-sdk` installed
- At least 15GB of free disk space for multiple model caches

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

Discuss trade-offs: load time, memory usage (check Task Manager / `nvidia-smi` / OS resource monitor), output quality versus speed. Use the Python benchmark script (Session 3) to measure latency and throughput; repeat tests with GPU acceleration enabled.

### 5. Starter Project (4 min)

Create a model comparison report generator by extending the benchmarking script with markdown export functionality.

## Starter Project: Extend `03-huggingface-models`

Enhance the existing sample by:

1. Adding benchmark aggregation with CSV/Markdown output.
2. Implementing simple qualitative scoring (prompt pair set + manual annotation stub file).
3. Introducing a JSON config (`models.json`) for a pluggable model list and prompt set.

## Validation Checklist

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Ensure all target models appear and respond to a probe chat request.

## Sample Scenario & Workshop Mapping

| Workshop Script | Scenario | Goal | Prompt / Dataset Source |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge platform team selecting default SLM for embedded summarizer | Generate latency + p95 + tokens/sec comparison across candidate models | Inline `PROMPT` var + environment `BENCH_MODELS` list |

### Scenario Narrative

The product engineering team needs to select a default lightweight summarization model for an offline meeting-notes feature. They conduct controlled deterministic benchmarks (temperature=0) using a fixed prompt set (example below) and collect latency and throughput metrics with and without GPU acceleration.

### Example Prompt Set JSON (expandable)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Iterate through each prompt for every model, capturing per-prompt latency to calculate distribution metrics and identify outliers.

## Model Selection Framework

| Dimension | Metric | Why It Matters |
|----------|--------|----------------|
| Latency | avg / p95 | Ensures consistent user experience |
| Throughput | tokens/sec | Supports batch and streaming scalability |
| Memory | resident size | Determines device compatibility and concurrency |
| Quality | rubric prompts | Evaluates task suitability |
| Footprint | disk cache | Affects distribution and updates |
| License | use allowance | Ensures compliance for commercial use |

## Extending With Custom Model

High-level pattern (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Refer to the official repository for updates on adapter interfaces:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| OOM on mistral-7b | Insufficient RAM/GPU | Stop other models; try a smaller variant |
| Slow first response | Cold load | Use a periodic lightweight prompt to keep the model warm |
| Download stalls | Network instability | Retry; prefetch during off-peak hours |

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
| Deterministic Mode | Ensures stable regression comparisons | Use `temperature=0`, fixed prompt set, and capture JSON outputs under version control |
| Quality Rubric Scoring | Adds a qualitative evaluation dimension | Maintain `prompts.json` with expected facets; annotate scores (1–5) manually or via a secondary model |
| CSV / Markdown Export | Creates shareable reports | Extend the script to generate `benchmark_report.md` with tables and highlights |
| Model Capability Tags | Facilitates automated routing later | Maintain `models.json` with `{alias: {capabilities:[], size_mb:..}}` |
| Cache Warmup Phase | Reduces cold-start bias | Run one warm-up round before the timing loop (already implemented) |
| Percentile Accuracy | Improves tail latency robustness | Use numpy percentile (already in refactored script) |
| Token Cost Approximation | Enables economic comparison | Approximate cost = (tokens/sec * avg tokens per request) * energy heuristic |
| Auto-Skipping Failed Models | Ensures resilience in batch runs | Wrap each benchmark in try/except and mark the status field |

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

Use a static list instead of random prompts to ensure comparable metrics across different commits.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->