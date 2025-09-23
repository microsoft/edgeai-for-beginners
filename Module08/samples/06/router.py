import os
import sys
import json
import requests
from typing import Dict, Any, Literal
from foundry_local import FoundryLocalManager

# Create a FoundryLocalManager instance. This will start the Foundry
# Local service if it is not already running and load the specified model.

# Tool registry mapping task -> model (env-overridable)
DEFAULT_TOOLS: Dict[str, Dict[str, str]] = {
    "general": {
        "model": os.environ.get("GENERAL_MODEL", "phi-4-mini"),
        "notes": "default fast chat",
    },
    "reasoning": {
        "model": os.environ.get("REASONING_MODEL", "deepseek-r1-7b"),
        "notes": "use for step-by-step tasks",
    },
    "code": {
        "model": os.environ.get("CODE_MODEL", "qwen2.5-7b"),
        "notes": "use for code-related requests",
    },
}

TOOLS_ENV = os.environ.get("TOOL_REGISTRY")
if TOOLS_ENV:
    try:
        TOOLS: Dict[str, Dict[str, str]] = json.loads(TOOLS_ENV)
    except Exception:
        TOOLS = DEFAULT_TOOLS
else:
    TOOLS = DEFAULT_TOOLS


def check_foundry(foundry_manager: FoundryLocalManager):
    try:
        if foundry_manager.is_service_running():
            return foundry_manager.list_cached_models()
        else:
            raise RuntimeError("Foundry Local service is not running.")
    except Exception as e:
        raise RuntimeError(f"Error checking Foundry Local: {e}")


def select_tool(user_query: str) -> Literal["general", "reasoning", "code"]:
    q = user_query.lower()
    if any(k in q for k in ["why", "how", "explain", "step-by-step", "reason"]):
        return "reasoning"
    if any(k in q for k in ["code", "python", "function", "class", "bug"]):
        return "code"
    return "general"


def chat(
    foundry_manager: FoundryLocalManager,
    model_id: str,
    content: str,
    max_tokens: int = 256,
) -> str:
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": content}],
        "max_tokens": max_tokens,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {foundry_manager.api_key}",
    }
    r = requests.post(
        f"{foundry_manager.endpoint}/chat/completions",
        json=payload,
        headers=headers,
        timeout=60,
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def route_and_run(prompt: str) -> Dict[str, Any]:
    tool_key = select_tool(prompt)
    model = TOOLS[tool_key]["model"]
    foundry_manager = FoundryLocalManager(
        model, bootstrap=False
    )  # assume already running
    model_info = foundry_manager.get_model_info(model)
    if not model_info:
        raise ValueError(f"Model {model} not found in Foundry Local.")
    try:
        answer = chat(foundry_manager, model_info.id, prompt)
    except Exception as e:
        print(f"Error with model {model}")
        raise RuntimeError(f"Error during chat: {e}")
    return {"tool": tool_key, "model": model_info.alias, "answer": answer}


if __name__ == "__main__":
    # Basic availability check for Foundry Local
    foundry_manager = FoundryLocalManager()
    try:
        models_info = check_foundry(foundry_manager)
        print({"base_url": foundry_manager.endpoint, "available_models": models_info})
    except Exception as e:
        raise RuntimeError(
            f"Warning: Could not reach Foundry Local at {foundry_manager.endpoint} ({e})"
        )

    user_prompt = (
        " ".join(sys.argv[1:])
        or "Write three JSON bullets of benefits of on-device AI."
    )
    try:
        result = route_and_run(user_prompt)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"{e}")
