#!/usr/bin/env python3
"""Session 1 Sample: Foundry Local bootstrap + basic & streaming chat.

Usage:
  From inside the Workshop/Samples directory, run:
    python -m session01.chat_bootstrap "Your question here"

Environment Variables (optional):
  FOUNDRY_LOCAL_ALIAS=phi-4-mini      # Model alias to use
  FOUNDRY_LOCAL_ENDPOINT=<url>        # Override service endpoint
  SHOW_USAGE=1                        # Show token usage statistics

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

This script demonstrates:
  * FoundryLocalManager for automatic service management
  * Model auto-download and loading of optimal variant
  * Standard (blocking) chat completion
  * Streaming chat completion
  * Proper error handling and logging
"""
from __future__ import annotations
import os
import sys
from utils.workshop_utils import get_client, chat_once

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")

try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)

prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "List two benefits of local inference."

print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")

standard, usage = chat_once(
    alias,
    messages=[{"role": "user", "content": prompt}],
    max_tokens=120,
    temperature=0.5
)
print("\n[STANDARD RESPONSE]\n" + standard + "\n")

print("[STREAMING RESPONSE]")
try:
    stream = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
        max_tokens=120,
        temperature=0.5
    )
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta:
            delta = chunk.choices[0].delta
            if getattr(delta, "content", None):
                print(delta.content, end="", flush=True)
    print("\n")
except Exception as e:
    print(f"\n[ERROR] Streaming failed: {e}")
    sys.exit(1)
