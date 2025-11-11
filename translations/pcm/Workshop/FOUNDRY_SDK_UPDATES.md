<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-11-11T17:36:33+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "pcm"
}
-->
# Foundry Local SDK Updates

## Overview

We don update di Workshop notebooks and utilities make dem fit use di **official Foundry Local Python SDK** well well, follow di pattern wey dey:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Files We Change

### 1. `Workshop/samples/workshop_utils.py`

**Wetin we change:**
- ✅ Add import error handling for `foundry-local-sdk` package
- ✅ Improve di documentation wit official SDK patterns
- ✅ Make logging better wit Unicode symbols (✓, ✗, ⚠)
- ✅ Add better docstrings wit examples
- ✅ Better error messages wey dey show CLI commands
- ✅ Update comments make dem match official SDK documentation

**Key Improvements:**

#### Import Error Handling
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Better `get_client()` Function
- Add detailed documentation about how SDK dey initialize
- Explain say `FoundryLocalManager` go start di service automatically
- Talk about how model alias dey resolve to hardware-optimized variants
- Improve logging wit endpoint info
- Better error messages wey dey suggest troubleshooting steps

#### Better `chat_once()` Function
- Add better docstring wit usage examples
- Explain OpenAI SDK compatibility
- Document streaming support (via kwargs)
- Improve error messages wit CLI command suggestions
- Add notes about model availability checking

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Wetin we change:**
- ✅ Update all markdown cells wit SDK references
- ✅ Improve code comments wit SDK pattern explanations
- ✅ Make cell documentation and explanations better
- ✅ Add troubleshooting guidance
- ✅ Update model catalog (change 'gpt-oss-20b' to 'phi-3.5-mini')
- ✅ Better output formatting wit visual indicators
- ✅ Add SDK links and references everywhere

**Cell-by-Cell Updates:**

#### Cell 1 (Title)
- Add SDK documentation links
- Reference official GitHub repositories

#### Cell 2 (Scenario)
- Reformat wit numbered steps
- Explain intent-based routing pattern well
- Talk about di benefits of local execution

#### Cell 3 (Dependency Installation)
- Add explanation of wetin each package dey do
- Document SDK capabilities (alias resolution, hardware optimization)

#### Cell 4 (Environment Setup)
- Make function docstrings better
- Add inline comments wey dey explain SDK patterns
- Document model catalog structure
- Explain priority/capability matching

#### Cell 5 (Catalog Check)
- Add visual checkmarks (✓)
- Format output better

#### Cell 6 (Intent Detection Test)
- Reformat output as table-style
- Show both intent and di model wey dem select

#### Cell 7 (Routing Function)
- Comprehensive SDK pattern explanation
- Document di initialization flow
- List all di features (retry, tracking, errors)
- Add SDK reference link

#### Cell 8 (Batch Demo)
- Explain wetin to expect better
- Add troubleshooting section
- Include CLI commands for debugging
- Format output display better

### 3. `Workshop/notebooks/session06_README.md` (New File)

**We create better documentation wey cover:**

1. **Overview**: Architecture diagram and component explanation
2. **SDK Integration**: Code examples wey follow official patterns
3. **Prerequisites**: Step-by-step setup instructions
4. **Usage**: How to run and customize di notebook
5. **Model Aliases**: Explanation of hardware-optimized variants
6. **Troubleshooting**: Common issues and solutions
7. **Extending**: How to add intents, models, and custom logic
8. **Performance Tips**: Best practices for production use
9. **Resources**: Links to official docs and community

## SDK Pattern Implementation

### Official Pattern (from Foundry Local docs)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Our Implementation (in workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Benefits of Our Approach:**
- ✅ Follow official SDK pattern well well
- ✅ Add caching make initialization no repeat
- ✅ Include retry logic for production robustness
- ✅ Support token usage tracking
- ✅ Provide better error messages
- ✅ Still dey compatible wit official examples

## Model Catalog Changes

### Before
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### After
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Reason:** We change 'gpt-oss-20b' (non-standard alias) to 'phi-3.5-mini' (official Foundry Local alias).

## Dependencies

### Updated requirements.txt

Di Workshop requirements.txt don already include:
```
foundry-local-sdk
openai>=1.30.0
```

Na only dis packages you need for Foundry Local integration.

## Testing di Updates

### 1. Confirm say Foundry Local dey Run

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Check Available Models

```bash
foundry model ls
```

Make sure say dis models dey or dem go auto-download:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Run di Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Or open am for VS Code and run all di cells.

### 4. Wetin we expect

**Cell 1 (Install):** Successfully install packages
**Cell 2 (Setup):** No errors, imports go work
**Cell 3 (Verify):** Show ✓ wit model list
**Cell 4 (Test Intent):** Show intent detection results
**Cell 5 (Router):** Show ✓ Route function ready
**Cell 6 (Execute):** Route prompts to models, show results

### 5. Troubleshooting Connection Errors

If you see `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Environment Variables

Di environment variables wey dey supported na:

| Variable | Default | Description |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Set am to `1` make e print token usage |
| `RETRY_ON_FAIL` | `1` | Enable retry logic |
| `RETRY_BACKOFF` | `1.0` | Initial retry delay (seconds) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Override service endpoint |

### Usage Examples

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migration from Old Pattern

If you get old code wey dey use direct API calls, dis na how to migrate:

### Before (Direct API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### After (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Benefits of Migration
- ✅ Automatic service management
- ✅ Model alias resolution
- ✅ Hardware optimization selection
- ✅ Better error handling
- ✅ OpenAI SDK compatibility
- ✅ Streaming support

## References

### Official Documentation
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK Source**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop Resources
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Sample Notebook**: `Workshop/notebooks/session06_models_router.ipynb`

### Community
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Next Steps

1. **Review Changes**: Read di updated files
2. **Test Notebook**: Run session06_models_router.ipynb
3. **Verify SDK**: Confirm say foundry-local-sdk dey installed
4. **Check Service**: Make sure say Foundry Local dey run
5. **Explore Docs**: Read di new session06_README.md

## Summary

Dis updates don make sure say di Workshop materials dey follow di **official Foundry Local SDK patterns** well well as dem document am for di GitHub repository. All code examples, documentation, and utilities now dey align wit Microsoft's recommended best practices for local AI model deployment.

Di changes don improve:
- ✅ **Correctness**: E dey use official SDK patterns
- ✅ **Documentation**: Better explanations and examples
- ✅ **Error Handling**: Better messages and troubleshooting guidance
- ✅ **Maintainability**: E dey follow official conventions
- ✅ **User Experience**: Clearer instructions and debugging help

---

**Updated:** October 8, 2025  
**SDK Version:** foundry-local-sdk (latest)  
**Workshop Branch:** Reactor

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even though we dey try make am accurate, abeg make you sabi say automated translations fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey used. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->