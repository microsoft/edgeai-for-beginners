"""Workshop Utilities for Foundry Local Samples.

Centralizes:
  * Cached manager + client creation (avoid repeated init work)
  * Simple chat helper returning (text, usage)
  * Optional usage printing (guarded by SHOW_USAGE=1)
  * Basic retry logic for transient errors

Environment Variables:
  SHOW_USAGE=1               -> Print token usage when available
  FOUNDRY_LOCAL_ALIAS=<name> -> Default single-model alias (used by some samples)
  FOUNDRY_LOCAL_ENDPOINT=<url> -> Override service endpoint (optional)

SDK Reference:
  https://github.com/microsoft/Foundry-Local
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

NOTE: We keep dependencies minimal; all scripts already depend on openai + foundry-local-sdk.
"""
from __future__ import annotations
from typing import Dict, Tuple, List, Any, Optional
import os, time, logging
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )

_LOGGER = logging.getLogger("workshop_utils")
if not _LOGGER.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[workshop] %(levelname)s: %(message)s"))
    _LOGGER.addHandler(_h)
_LOGGER.setLevel(logging.INFO)

# Simple in-memory cache: alias -> (manager, client, model_id)
_CACHE: Dict[str, Tuple[FoundryLocalManager, OpenAI, str]] = {}

def get_client(alias: str, endpoint: Optional[str] = None) -> Tuple[FoundryLocalManager, OpenAI, str]:
    """Return (manager, OpenAI client, model_id) with caching.
    
    This follows the official Foundry Local SDK pattern:
    1. Create FoundryLocalManager instance (starts service if needed)
    2. Create OpenAI client with manager's endpoint and API key
    3. Get model info to resolve the model ID
    
    Args:
        alias: Model alias to initialize (e.g., 'phi-4-mini', 'phi-3.5-mini')
        endpoint: Optional endpoint override (from FOUNDRY_LOCAL_ENDPOINT)
    
    Returns:
        Tuple of (FoundryLocalManager, OpenAI client, resolved model_id)
    
    Raises:
        RuntimeError: If manager initialization or model info retrieval fails
    
    Note:
        By using an alias, the most suitable model variant will be selected
        for the user's hardware (CUDA, NPU, or CPU optimized).
    """
    cache_key = f"{alias}:{endpoint or 'default'}"
    if cache_key in _CACHE:
        return _CACHE[cache_key]
    
    try:
        # Initialize FoundryLocalManager - this starts the Foundry Local service
        # if it is not already running and loads the specified model
        if endpoint:
            manager = FoundryLocalManager(alias, endpoint=endpoint)
        else:
            manager = FoundryLocalManager(alias)
        
        # Configure the OpenAI client to use the local Foundry service
        # This provides OpenAI-compatible API access to local models
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key  # API key is not required for local usage
        )
        
        # Get the resolved model ID from the manager
        # The manager handles model alias resolution to actual model IDs
        model_info = manager.get_model_info(alias)
        model_id = model_info.id
        
        _CACHE[cache_key] = (manager, client, model_id)
        _LOGGER.info(f"✓ Initialized Foundry Local client: '{alias}' -> '{model_id}'")
        _LOGGER.info(f"  Endpoint: {manager.endpoint}")
        return manager, client, model_id
        
    except Exception as e:
        _LOGGER.error(f"✗ Failed to initialize client for alias '{alias}': {e}")
        _LOGGER.error("✗ Ensure Foundry Local service is running: foundry service start")
        raise RuntimeError(f"Client initialization failed for '{alias}': {e}") from e

def chat_once(alias: str, messages: List[dict], **kwargs) -> Tuple[str, Any]:
    """Execute a single chat completion using Foundry Local, returning (text, usage).

    This follows the official OpenAI SDK pattern with Foundry Local:
    - Uses the OpenAI client configured for local Foundry service
    - Supports streaming and non-streaming completions
    - Retries on transient exceptions (network / load) if RETRY_ON_FAIL=1
    - Uses exponential backoff for retries
    
    Args:
        alias: Model alias to use (e.g., 'phi-4-mini', 'qwen2.5-0.5b')
        messages: Chat messages in OpenAI format [{'role': 'user', 'content': '...'}]
        **kwargs: Additional parameters for chat.completions.create
                 (max_tokens, temperature, stream, etc.)
    
    Returns:
        Tuple of (response_text, usage_object)
    
    Environment Variables:
        RETRY_ON_FAIL: Enable retry logic (default: "1")
        RETRY_BACKOFF: Initial retry delay in seconds (default: "1.0")
        SHOW_USAGE: Print token usage statistics (default: "0")
        FOUNDRY_LOCAL_ENDPOINT: Override default endpoint (optional)
    
    Example:
        >>> text, usage = chat_once(
        ...     'phi-4-mini',
        ...     messages=[{'role': 'user', 'content': 'What is AI?'}],
        ...     max_tokens=100,
        ...     temperature=0.7
        ... )
    """
    retries = 1 if os.getenv("RETRY_ON_FAIL", "1") == "1" else 0
    delay = float(os.getenv("RETRY_BACKOFF", "1.0"))
    endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
    attempt = 0
    last_exception = None
    
    while True:
        attempt += 1
        try:
            # Get cached client and model ID
            _, client, model_id = get_client(alias, endpoint=endpoint)
            
            # Call OpenAI-compatible chat completion API
            # The client is configured to use the local Foundry service endpoint
            resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
            
            if not resp.choices:
                raise RuntimeError("No completion choices returned from model")
            
            text = resp.choices[0].message.content
            usage = getattr(resp, "usage", None)
            
            if os.getenv("SHOW_USAGE") == "1" and usage:
                print_usage(usage)
            
            return text, usage
            
        except Exception as e:  # noqa: BLE001 broad for demo simplicity
            last_exception = e
            if attempt > retries:
                _LOGGER.error(f"✗ chat_once failed after {attempt} attempts: {e}")
                _LOGGER.error(f"  Check if model '{alias}' is available: foundry model ls")
                raise
            _LOGGER.warning("⚠ chat_once attempt %d failed (%s); retrying in %.1fs", attempt, e, delay)
            time.sleep(delay)
            delay *= 2  # Exponential backoff

def print_usage(usage: Any) -> None:
    """Pretty print token usage object if present."""
    try:
        total = getattr(usage, "total_tokens", None)
        comp = getattr(usage, "completion_tokens", None)
        prompt = getattr(usage, "prompt_tokens", None)
        print(f"[USAGE] prompt={prompt} completion={comp} total={total}")
    except Exception:  # pragma: no cover - defensive
        print(f"[USAGE] raw={usage}")

__all__ = ["get_client", "chat_once", "print_usage"]
