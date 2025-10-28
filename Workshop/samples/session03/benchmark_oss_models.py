#!/usr/bin/env python3
"""Session 3 Sample: Benchmark multiple OSS models via Foundry Local.

Extends simple latency measurement with optional warmup, token/sec stats,
and (optional) streaming first-token latency.

Usage:
    From inside the Workshop/Samples directory, run:
        python -m session03.benchmark_oss_models

Environment Variables:
  BENCH_MODELS=model1,model2         # Comma-separated model aliases
  BENCH_ROUNDS=3                     # Number of benchmark iterations
  BENCH_PROMPT="Your prompt"         # Test prompt
  BENCH_STREAM=1                     # Measure first-token latency
  FOUNDRY_LOCAL_ENDPOINT=<url>       # Override endpoint

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

Outputs JSON with latency_avg, latency_p95, tokens_per_sec_avg per model.
"""
from __future__ import annotations
import os
import sys
import time
import statistics
import json

try:
    import numpy as _np  # optional for precise percentile
except ImportError:  # pragma: no cover
    _np = None

from utils.workshop_utils import get_client, chat_once

MODELS = os.getenv("BENCH_MODELS", "phi-4-mini,qwen2.5-0.5b").split(",")
ROUNDS = int(os.getenv("BENCH_ROUNDS", "3"))
PROMPT = os.getenv("BENCH_PROMPT", "Explain retrieval augmented generation briefly.")
MEASURE_STREAM = os.getenv("BENCH_STREAM", "0") == "1"
ENDPOINT = os.getenv("FOUNDRY_LOCAL_ENDPOINT")

def ensure_loaded(alias: str):
    """Ensure model is loaded and client is cached.
    
    Args:
        alias: Model alias to load
    
    Returns:
        Tuple of (manager, client, model_id)
    
    Raises:
        RuntimeError: If model loading fails
    """
    try:
        manager, client, model_id = get_client(alias, endpoint=ENDPOINT)
        print(f"[INFO] Loaded model: {alias} -> {model_id}")
        return manager, client, model_id
    except Exception as e:
        print(f"[ERROR] Failed to load model '{alias}': {e}")
        raise

def run_round(alias: str):
    """Run single benchmark round with optional streaming measurement."""
    start = time.time()
    text, usage = chat_once(
        alias,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=120,
        temperature=0.2,
    )
    end = time.time()
    total_tokens = getattr(usage, "total_tokens", None) if usage else None
    first_token_latency = None
    
    # Optional streaming measurement (one-off) when MEASURE_STREAM enabled
    if MEASURE_STREAM:
        _, client, model_id = get_client(alias, endpoint=ENDPOINT)
        t0 = time.time()
        stream = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": PROMPT}],
            stream=True,
            max_tokens=60,
            temperature=0.2,
        )
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta and getattr(chunk.choices[0].delta, 'content', None):
                first_token_latency = time.time() - t0
                break
    
    return end - start, total_tokens, first_token_latency

print(f"[INFO] Benchmarking {len([a for a in MODELS if a.strip()])} models with {ROUNDS} rounds each")
print(f"[INFO] Prompt: {PROMPT[:50]}..." if len(PROMPT) > 50 else f"[INFO] Prompt: {PROMPT}")
print(f"[INFO] Stream measurement: {'enabled' if MEASURE_STREAM else 'disabled'}\n")

summary = []
for alias in [a.strip() for a in MODELS if a.strip()]:
    try:
        print(f"[INFO] Benchmarking {alias}...")
        ensure_loaded(alias)  # warm manager cache
        run_round(alias)  # warmup
        latencies, tps, ft_latencies = [], [], []
        for round_num in range(ROUNDS):
            latency, tokens, ft = run_round(alias)
            latencies.append(latency)
            if tokens:
                tps.append(tokens/latency)
            if ft is not None:
                ft_latencies.append(ft)
            print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s" + (f" ({tokens} tokens)" if tokens else ""))
        
        if _np and len(latencies) > 1:
            p95 = float(_np.percentile(latencies, 95))
        else:
            p95 = statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0]
        
        entry = {
            "alias": alias,
            "latency_avg": statistics.mean(latencies),
            "latency_p95": p95,
            "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
            "rounds": ROUNDS,
        }
        if ft_latencies:
            entry["first_token_latency_avg"] = statistics.mean(ft_latencies)
        summary.append(entry)
        print(f"[INFO] Completed {alias}\n")
    except Exception as e:
        print(f"[ERROR] Benchmark failed for {alias}: {e}")
        print(f"[INFO] Skipping {alias} and continuing...\n")

if not summary:
    print("[ERROR] All benchmarks failed")
    sys.exit(1)

print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
