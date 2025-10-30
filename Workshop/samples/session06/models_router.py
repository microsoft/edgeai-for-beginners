#!/usr/bin/env python3
"""Session 6 Sample: Intent-based model routing using Foundry Local Manager.

Demonstrates intelligent routing of prompts to specialized models based on
detected intent patterns.

Environment Variables:
  FOUNDRY_LOCAL_ENDPOINT=<url>       # Override endpoint

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
"""
from __future__ import annotations
import os
import sys
import re
from typing import Dict, Any
from utils.workshop_utils import chat_once

ENDPOINT = os.getenv("FOUNDRY_LOCAL_ENDPOINT")

print("[INFO] Initializing intent-based model router")

CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3},
}

RULES = [
    (re.compile(r"code|refactor|function", re.I), "code"),
    (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
    (re.compile(r"classif|category|label", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    """Detect intent from user prompt using pattern matching.
    
    Args:
        prompt: User prompt text
    
    Returns:
        Detected intent string (e.g., 'code', 'summarize', 'classification', 'general')
    """
    for pat, intent in RULES:
        if pat.search(prompt):
            return intent
    return "general"

def pick_model(intent: str) -> str:
    """Select best model for given intent.
    
    Args:
        intent: Detected intent string
    
    Returns:
        Model alias best suited for the intent
    
    Note:
        Models are ranked by:
        1. Whether they support the intent (capability match)
        2. Priority (lower number = higher priority)
    """
    ranked = []
    for name, meta in CATALOG.items():
        ranked.append((name, intent in meta["capabilities"], meta["priority"]))
    ranked.sort(key=lambda t: (not t[1], t[2]))
    return ranked[0][0]

def route(prompt: str) -> Dict[str, Any]:
    """Route prompt to appropriate model based on detected intent.
    
    Args:
        prompt: User prompt to route
    
    Returns:
        Dictionary with intent, selected model, output, and token usage
    
    Raises:
        Exception: If model execution fails
    """
    intent = detect_intent(prompt)
    alias = pick_model(intent)
    print(f"[INFO] Routing: '{prompt[:50]}...' -> intent='{intent}', model='{alias}'")
    
    try:
        text, usage = chat_once(
            alias,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.5
        )
        return {
            "intent": intent,
            "alias": alias,
            "output": text,
            "tokens": getattr(usage, 'total_tokens', None) if usage else None
        }
    except Exception as e:
        print(f"[ERROR] Routing failed for prompt: {e}")
        raise

if __name__ == "__main__":
    tests = [
        "Refactor this Python snippet for readability",
        "Summarize the importance of small language models",
        "Classify this feedback: 'The UI is slow but pretty'"
    ]
    print(f"\n[INFO] Testing router with {len(tests)} prompts\n")
    
    results = []
    for i, t in enumerate(tests, 1):
        try:
            result = route(t)
            results.append(result)
            print(f"\n[TEST {i}/{len(tests)}]")
            print(f"Prompt: {t}")
            print(f"Intent: {result['intent']}")
            print(f"Model: {result['alias']}")
            print(f"Output: {result['output'][:100]}..." if len(result['output']) > 100 else f"Output: {result['output']}")
            print(f"Tokens: {result['tokens']}\n")
        except Exception as e:
            print(f"\n[ERROR] Test {i} failed: {e}\n")
    
    if not results:
        print("[ERROR] All routing tests failed")
        sys.exit(1)
