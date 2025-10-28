#!/usr/bin/env python3
"""Session 5 Sample: Multi-agent orchestration with Foundry Local manager.

Demonstrates coordinating multiple specialized agents using different models.

Usage:
    From inside the Workshop/Samples directory, run:
        python -m session05.agents_orchestrator

Environment Variables:
  AGENT_MODEL_PRIMARY=phi-4-mini     # Primary agent model
  AGENT_MODEL_EDITOR=phi-4-mini      # Editor agent model
  AGENT_QUESTION="Your question"     # Test question
  FOUNDRY_LOCAL_ENDPOINT=<url>       # Override endpoint

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import os
import sys
from utils.workshop_utils import get_client, chat_once

PRIMARY_ALIAS = os.getenv("AGENT_MODEL_PRIMARY", os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini"))
EDITOR_ALIAS = os.getenv("AGENT_MODEL_EDITOR", PRIMARY_ALIAS)
ENDPOINT = os.getenv("FOUNDRY_LOCAL_ENDPOINT")

print("[INFO] Initializing multi-agent orchestrator")
print(f"  Primary agent model: {PRIMARY_ALIAS}")
print(f"  Editor agent model: {EDITOR_ALIAS}")

# Initialize clients
try:
    get_client(PRIMARY_ALIAS, endpoint=ENDPOINT)
    if EDITOR_ALIAS != PRIMARY_ALIAS:
        get_client(EDITOR_ALIAS, endpoint=ENDPOINT)
    print("[INFO] All agents initialized successfully\n")
except Exception as e:
    print(f"[ERROR] Failed to initialize agents: {e}")
    sys.exit(1)

@dataclass
class AgentMsg:
    role: str
    content: str

@dataclass
class Agent:
    name: str
    system: str
    memory: List[AgentMsg] = field(default_factory=list)

    def _history(self):
        msgs = [{"role": "system", "content": self.system}]
        msgs += [{"role": m.role, "content": m.content} for m in self.memory[-6:]]
        return msgs

    def act(self, prompt: str, temperature: float = 0.4, alias: Optional[str] = None) -> str:
        """Execute agent action with given prompt.
        
        Args:
            prompt: User prompt for the agent
            temperature: Sampling temperature (0.0-1.0)
            alias: Model alias override (uses PRIMARY_ALIAS if not specified)
        
        Returns:
            Agent's response text
        
        Raises:
            Exception: If chat completion fails
        """
        alias = alias or PRIMARY_ALIAS
        self.memory.append(AgentMsg("user", prompt))
        try:
            text, _ = chat_once(
                alias,
                messages=self._history()+[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=300,
            )
            self.memory.append(AgentMsg("assistant", text))
            return text
        except Exception as e:
            print(f"[ERROR] Agent {self.name} failed: {e}")
            raise

researcher = Agent("Researcher", "You collect concise factual bullet points.")
editor = Agent("Editor", "You rewrite content for clarity and executive tone.")

def pipeline(question: str) -> Dict[str, str]:
    """Execute multi-agent pipeline: research -> edit.
    
    Args:
        question: User question to process
    
    Returns:
        Dictionary with research and final outputs
    
    Raises:
        Exception: If any agent fails
    """
    print(f"[INFO] Processing question: {question}")
    print(f"[INFO] Stage 1: Research agent...")
    research = researcher.act(question, alias=PRIMARY_ALIAS)
    
    print(f"[INFO] Stage 2: Editor agent...")
    rewrite = editor.act(f"Rewrite professionally with a 1-sentence summary first:\n{research}", alias=EDITOR_ALIAS)
    
    return {"research": research, "final": rewrite}

if __name__ == "__main__":
    q = os.getenv("AGENT_QUESTION", "Explain why edge AI matters for compliance.")
    try:
        result = pipeline(q)
        print("\n[PIPELINE RESULTS]")
        for k, v in result.items():
            print(f"\n== {k.upper()} ==")
            print(v)
    except Exception as e:
        print(f"\n[ERROR] Pipeline failed: {e}")
        sys.exit(1)
