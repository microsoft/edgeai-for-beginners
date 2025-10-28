#!/usr/bin/env python3
"""Session 4 Sample: Compare SLM vs LLM responses and latency.

Usage:
    From inside the Workshop/Samples directory, run:
        python -m session04.model_compare

Environment Variables:
  SLM_ALIAS=phi-4-mini              # Small language model
  LLM_ALIAS=qwen2.5-7b              # Larger language model
  COMPARE_PROMPT="Your prompt"      # Test prompt
  FOUNDRY_LOCAL_ENDPOINT=<url>      # Override endpoint

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
"""
from __future__ import annotations
import os
import sys
import time
import json
from typing import Tuple, Optional
from utils.workshop_utils import get_client, chat_once

SLM = os.getenv("SLM_ALIAS", "phi-4-mini")
LLM = os.getenv("LLM_ALIAS", "qwen2.5-7b")
PROMPT = os.getenv("COMPARE_PROMPT", "List 5 benefits of local AI inference.")
ENDPOINT = os.getenv("FOUNDRY_LOCAL_ENDPOINT")

print("[INFO] Comparing models:")
print(f"  SLM: {SLM}")
print(f"  LLM: {LLM}")
print(f"  Prompt: {PROMPT[:50]}..." if len(PROMPT) > 50 else f"  Prompt: {PROMPT}")
print()

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias.
    
    Args:
        alias: Model alias to test
    
    Returns:
        Tuple of (latency_seconds, response_text, total_tokens)
    
    Raises:
        Exception: If model execution fails
    """
    print(f"[INFO] Running {alias}...")
    start = time.time()
    text, usage = chat_once(
        alias,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=160,
        temperature=0.5,
    )
    latency = time.time() - start
    tokens = getattr(usage, 'total_tokens', None) if usage else None
    print(f"[INFO] {alias} completed in {latency:.3f}s ({tokens or 'N/A'} tokens)")
    return latency, text, tokens

results = []
for alias in (SLM, LLM):
    try:
        # Ensure cache is populated
        get_client(alias, endpoint=ENDPOINT)
        latency, text, tokens = run(alias)
        results.append({
            "alias": alias,
            "latency_sec": round(latency, 3),
            "tokens": tokens,
            "sample": text
        })
    except Exception as e:
        print(f"[ERROR] Failed to run {alias}: {e}")
        results.append({
            "alias": alias,
            "error": str(e)
        })

if not any('sample' in r for r in results):
    print("[ERROR] All model comparisons failed")
    sys.exit(1)

print("\n[COMPARISON RESULTS]")
print(json.dumps(results, indent=2))
