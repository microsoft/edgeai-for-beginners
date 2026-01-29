# Workshop အမြန်စတင်လမ်းညွှန်

## ကြိုတင်လိုအပ်ချက်များ

### 1. Foundry Local ကိုထည့်သွင်းပါ

တရားဝင်ထည့်သွင်းလမ်းညွှန်ကိုလိုက်နာပါ:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python Dependencies ကိုထည့်သွင်းပါ

Workshop directory မှာ:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Workshop နမူနာများကိုအလုပ်လုပ်စေခြင်း

### Session 01: အခြေခံ Chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Environment Variables:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Session 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Environment Variables:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Session 02: RAG အကဲဖြတ်ခြင်း (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**မှတ်ချက်**: `requirements.txt` မှတစ်ဆင့်ထည့်သွင်းရမည့်အပို dependencies လိုအပ်သည်

### Session 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Environment Variables:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Output**: latency, throughput, နှင့် first-token metrics ပါသော JSON

### Session 04: Model နှိုင်းယှဉ်ခြင်း

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Environment Variables:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Session 05: Multi-Agent Orchestration

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Environment Variables:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Session 06: Model Router

```bash
cd Workshop/samples
python -m session06.models_router
```

**Tests routing logic** ကို intents များစွာ (code, summarize, classification) ဖြင့်စမ်းသပ်သည်

### Session 06: Pipeline

```bash
python -m session06.models_pipeline
```

**စီစဉ်ခြင်း၊ အကောင်အထည်ဖော်ခြင်းနှင့် ပြန်လည်တိုးတက်အောင်လုပ်ခြင်းပါသော အဆင့်များစွာရှိသော pipeline**

## Scripts

### Benchmark Report ကို Export လုပ်ပါ

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Output**: Markdown table + JSON metrics

### Markdown CLI Patterns ကို Lint လုပ်ပါ

```bash
python lint_markdown_cli.py --verbose
```

**ရည်ရွယ်ချက်**: documentation မှာ CLI patterns များမသုံးတော့ဘူးဆိုတာကိုရှာဖွေပါ

## စမ်းသပ်ခြင်း

### Smoke Tests

```bash
cd Workshop
python -m tests.smoke
```

**Tests**: အဓိကနမူနာများ၏ အခြေခံလုပ်ဆောင်မှုကိုစမ်းသပ်သည်

## ပြဿနာများကိုဖြေရှင်းခြင်း

### Service မအလုပ်လုပ်ခြင်း

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Module Import Errors

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Connection Errors

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model မတွေ့ခြင်း

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Environment Variable ကိုရည်ညွှန်းခြင်း

### Core Configuration
| Variable | Default | Description |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Varies | အသုံးပြုရန် Model alias |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | service endpoint ကို override လုပ်ပါ |
| `SHOW_USAGE` | `0` | token usage stats ကိုပြပါ |
| `RETRY_ON_FAIL` | `1` | retry logic ကို enable လုပ်ပါ |
| `RETRY_BACKOFF` | `1.0` | အစပိုင်း retry နောက်ကျမှု (စက္ကန့်) |

### Session-Specific
| Variable | Default | Description |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding model |
| `RAG_QUESTION` | See sample | RAG စမ်းသပ်မေးခွန်း |
| `BENCH_MODELS` | Varies | Comma-separated models |
| `BENCH_ROUNDS` | `3` | Benchmark iterations |
| `BENCH_PROMPT` | See sample | Benchmark prompt |
| `BENCH_STREAM` | `0` | first-token latency ကိုတိုင်းတာပါ |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primary agent model |
| `AGENT_MODEL_EDITOR` | Primary | Editor agent model |
| `SLM_ALIAS` | `phi-4-mini` | Small language model |
| `LLM_ALIAS` | `qwen2.5-7b` | Large language model |
| `COMPARE_PROMPT` | See sample | Comparison prompt |

## အကြံပြုထားသော Models

### Development & Testing
- **phi-4-mini** - အရည်အသွေးနှင့်အမြန်နှုန်းကိုထိန်းညှိထားသည်
- **qwen2.5-0.5b** - Classification အတွက်အလွန်မြန်ဆန်သည်
- **gemma-2-2b** - အရည်အသွေးကောင်းပြီး အလယ်အလတ်မြန်နှုန်းရှိသည်

### Production Scenarios
- **phi-4-mini** - အထွေထွေအသုံးပြုမှု
- **deepseek-coder-1.3b** - Code generation
- **qwen2.5-7b** - အရည်အသွေးမြင့်မားသောအဖြေများ

## SDK Documentation

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## အကူအညီရယူခြင်း

1. Service status ကိုစစ်ဆေးပါ: `foundry service status`
2. Logs ကိုကြည့်ပါ: Foundry Local service logs ကိုစစ်ဆေးပါ
3. SDK docs ကိုကြည့်ပါ: https://github.com/microsoft/Foundry-Local
4. နမူနာ code ကိုကြည့်ပါ: နမူနာအားလုံးမှာအသေးစိတ် docstrings ပါရှိသည်

## နောက်တစ်ဆင့်များ

1. Workshop session အားလုံးကိုအစဉ်လိုက်ပြီးမြောက်ပါ
2. Model များကိုစမ်းသပ်ပါ
3. သင့်အသုံးအဆောင်များအတွက်နမူနာများကိုပြင်ဆင်ပါ

---

**နောက်ဆုံးအပ်ဒိတ်**: 2025-01-08  
**Workshop Version**: နောက်ဆုံး  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->