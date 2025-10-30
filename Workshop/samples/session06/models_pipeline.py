#!/usr/bin/env python3
"""Session 6 Sample: Multi-step plan -> execute -> refine pipeline with routing.

Demonstrates a multi-stage pipeline:
  1. Plan: Break task into steps
  2. Execute: Route each step to specialized model
  3. Refine: Summarize combined outputs

Usage:
    From inside the Workshop/Samples directory, run:
        python -m session06.models_pipeline

Environment Variables:
  FOUNDRY_LOCAL_ENDPOINT=<url>       # Override endpoint
  PIPELINE_TASK="Your task"          # Task to process

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
"""
from __future__ import annotations
import sys
from typing import Dict, List, Tuple, Any
from session06.models_router import detect_intent, pick_model
from utils.workshop_utils import chat_once

def chat(alias: str, content: str) -> str:
    """Execute single chat completion for pipeline step.
    
    Args:
        alias: Model alias to use
        content: Prompt content
    
    Returns:
        Model response text
    
    Raises:
        Exception: If chat completion fails
    """
    try:
        text, _ = chat_once(
            alias,
            messages=[{"role": "user", "content": content}],
            max_tokens=200,
            temperature=0.4
        )
        return text
    except Exception as e:
        print(f"[ERROR] Chat failed for alias '{alias}': {e}")
        raise

def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
    print(f"[INFO] Starting pipeline for task: {task[:50]}..." if len(task) > 50 else f"[INFO] Starting pipeline for task: {task}")
    
    # Step 1: Plan - break into steps
    print("[INFO] Stage 1: Planning (breaking task into steps)...")
    plan_alias = pick_model("general")
    plan = chat(plan_alias, f"Break the task into 3 concise steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    print(f"[INFO] Generated {len(steps)} steps")
    
    # Step 2: Execute - route each step to specialized model
    print("[INFO] Stage 2: Executing steps...")
    outputs: List[Tuple[str, str, str]] = []
    for i, step in enumerate(steps, 1):
        intent = detect_intent(step)
        alias = pick_model(intent)
        print(f"  Step {i}/{len(steps)}: {step[:50]}... -> {alias}")
        result = chat(alias, step)
        outputs.append((step, alias, result))
    
    # Step 3: Refine - summarize combined outputs
    print("[INFO] Stage 3: Refining results...")
    refine_alias = pick_model("summarize")
    combined = "\n".join(o[2] for o in outputs)
    final_answer = chat(refine_alias, f"Summarize cohesively:\n{combined}")
    
    return {"plan": plan, "steps": outputs, "final": final_answer}

if __name__ == "__main__":
    import json
    import os
    
    task = os.getenv(
        "PIPELINE_TASK",
        "Generate a refactored version of a slow Python loop and summarize performance gains."
    )
    
    try:
        result = pipeline(task)
        print("\n[PIPELINE RESULTS]")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"\n[ERROR] Pipeline failed: {e}")
        sys.exit(1)
