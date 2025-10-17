<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b994c57f1207012e4d7f58b7c0d1ae7",
  "translation_date": "2025-10-17T10:16:43+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "my"
}
-->
# EdgeAI အတွက် မူလတန်း - အလုပ်ရုံဆွေးနွေးပွဲ

> **ထုတ်လုပ်မှုအဆင်သင့် Edge AI အက်ပလီကေးရှင်းများ တည်ဆောက်ရန် လက်တွေ့လေ့လာမှုလမ်းကြောင်း**
>
> Microsoft Foundry Local ကို အသုံးပြု၍ ပထမဆုံး chat completion မှ multi-agent orchestration အထိ ၆ ခုသော အဆင့်ဆင့် session များတွင် ဒေသခံ AI deployment ကို ကျွမ်းကျင်ပါ။

---

## 🎯 အကျဉ်းချုပ်

**EdgeAI အတွက် မူလတန်း အလုပ်ရုံဆွေးနွေးပွဲ** သို့ ကြိုဆိုပါသည်။ ဒေသခံ hardware ပေါ်တွင် အပြည့်အဝ လည်ပတ်နိုင်သော ဉာဏ်ရည်ရှိသော အက်ပလီကေးရှင်းများ တည်ဆောက်ရန် လက်တွေ့လမ်းညွှန်ဖြစ်သည်။ ဒီအလုပ်ရုံဆွေးနွေးပွဲသည် Microsoft Foundry Local နှင့် Small Language Models (SLMs) ကို အသုံးပြု၍ Edge AI အကြောင်းအရာများကို လက်တွေ့ကျကျ အတတ်ပညာများအဖြစ် ပြောင်းလဲပေးသည်။

### ဒီအလုပ်ရုံဆွေးနွေးပွဲကို ဘာကြောင့် လိုအပ်သလဲ?

**Edge AI တိုးတက်မှုကာလ ရောက်ရှိနေပြီ**

ကမ္ဘာတစ်ဝှမ်းရှိ အဖွဲ့အစည်းများသည် cloud မှာ အခြေခံထားသော AI မှ edge computing သို့ ပြောင်းလဲနေကြသည်။ အဓိကအကြောင်းရင်း ၃ ခုမှာ -

1. **Privacy & Compliance** - အရေးကြီးသော ဒေတာများကို cloud သို့ ပို့ဆောင်ခြင်းမရှိဘဲ ဒေသတွင်းတွင် လုပ်ဆောင်ခြင်း (HIPAA, GDPR, ငွေကြေးဆိုင်ရာ စည်းမျဉ်းများ)
2. **Performance** - network latency ကို ဖယ်ရှားခြင်း (ဒေသတွင်း 50-500ms vs cloud round-trip 500-2000ms)
3. **Cost Control** - per-token API ကုန်ကျစရိတ်များကို ဖယ်ရှားပြီး cloud ကုန်ကျစရိတ်မရှိဘဲ scale လုပ်ခြင်း

**Edge AI သည် ကွဲပြားခြားနားသည်**

AI ကို on-premises တွင် လည်ပတ်ရန် အသစ်သော ကျွမ်းကျင်မှုများ လိုအပ်သည် -
- အရင်းအမြစ်ကန့်သတ်မှုများအတွက် မော်ဒယ်ရွေးချယ်ခြင်းနှင့် အဆင့်မြှင့်တင်ခြင်း
- ဒေသတွင်း service စီမံခန့်ခွဲမှုနှင့် hardware acceleration
- မော်ဒယ်အသေးစားများအတွက် prompt engineering
- edge devices များအတွက် ထုတ်လုပ်မှု deployment ပုံစံများ

**ဒီအလုပ်ရုံဆွေးနွေးပွဲသည် အတတ်ပညာများကို ပေးစွမ်းသည်**

6 ခုသော အဓိက session များ (~3 နာရီ စုစုပေါင်း) တွင် "Hello World" မှ multi-agent systems များကို ထုတ်လုပ်မှုအဆင်သင့်အဖြစ် deploy လုပ်ခြင်းအထိ တိုးတက်မှုရှိမည် - အားလုံးကို သင့်စက်ပေါ်တွင် ဒေသတွင်းတွင် လည်ပတ်စေမည်။

---

## 📚 လေ့လာမှုရည်မှန်းချက်များ

ဒီအလုပ်ရုံဆွေးနွေးပွဲကို ပြီးမြောက်ပြီးနောက် သင်သည် အောက်ပါအတတ်ပညာများကို ရရှိမည် -

### အဓိကကျွမ်းကျင်မှုများ
1. **ဒေသတွင်း AI Services များကို Deploy နှင့် စီမံခန့်ခွဲခြင်း**
   - Microsoft Foundry Local ကို ထည့်သွင်းပြီး configure လုပ်ခြင်း
   - edge deployment အတွက် သင့်လျော်သော မော်ဒယ်များကို ရွေးချယ်ခြင်း
   - မော်ဒယ်၏ lifecycle ကို စီမံခန့်ခွဲခြင်း (download, load, cache)
   - အရင်းအမြစ်အသုံးပြုမှုကို စောင့်ကြည့်ပြီး performance ကို အဆင့်မြှင့်တင်ခြင်း

2. **AI-Powered Applications များ တည်ဆောက်ခြင်း**
   - OpenAI-compatible chat completions ကို ဒေသတွင်းတွင် အကောင်အထည်ဖော်ခြင်း
   - Small Language Models အတွက် ထိရောက်သော prompts ကို ဒီဇိုင်းဆွဲခြင်း
   - UX အတွက် streaming responses ကို ကိုင်တွယ်ခြင်း
   - ဒေသတွင်းမော်ဒယ်များကို ရှိပြီးသား အက်ပလီကေးရှင်းများနှင့် ပေါင်းစပ်ခြင်း

3. **RAG (Retrieval Augmented Generation) Systems များ ဖန်တီးခြင်း**
   - embeddings ဖြင့် semantic search တည်ဆောက်ခြင်း
   - domain-specific knowledge တွင် LLM responses ကို အခြေခံခြင်း
   - RAG quality ကို စက်မှုစံချိန်များဖြင့် အကဲဖြတ်ခြင်း
   - prototype မှ production သို့ scale လုပ်ခြင်း

4. **မော်ဒယ် performance ကို အဆင့်မြှင့်တင်ခြင်း**
   - သင့်အသုံးအတွက် မော်ဒယ်များကို benchmark လုပ်ခြင်း
   - latency, throughput, first-token time ကို တိုင်းတာခြင်း
   - speed/quality tradeoffs အပေါ် အကောင်းဆုံး မော်ဒယ်များကို ရွေးချယ်ခြင်း
   - SLM နှင့် LLM trade-offs ကို လက်တွေ့အခြေအနေများတွင် နှိုင်းယှဉ်ခြင်း

5. **Multi-Agent Systems များကို Orchestrate လုပ်ခြင်း**
   - အလုပ်အမျိုးမျိုးအတွက် agent များကို ဒီဇိုင်းဆွဲခြင်း
   - agent memory နှင့် context management ကို အကောင်အထည်ဖော်ခြင်း
   - အလုပ်အဆင့်များတွင် agent များကို စီမံခန့်ခွဲခြင်း
   - မော်ဒယ်များအကြား requests များကို အဆင်ပြေစွာ route လုပ်ခြင်း

6. **ထုတ်လုပ်မှုအဆင်သင့်ဖြေရှင်းချက်များကို Deploy လုပ်ခြင်း**
   - error handling နှင့် retry logic ကို အကောင်အထည်ဖော်ခြင်း
   - token usage နှင့် system resources ကို စောင့်ကြည့်ခြင်း
   - model-as-tools patterns ဖြင့် scalable architectures တည်ဆောက်ခြင်း
   - edge မှ hybrid (edge + cloud) သို့ ပြောင်းလဲမှုလမ်းကြောင်းများကို စီစဉ်ခြင်း

---

## 🎓 လေ့လာမှုရလဒ်များ

### သင်တည်ဆောက်မည့်အရာများ

ဒီအလုပ်ရုံဆွေးနွေးပွဲအဆုံးတွင် သင်သည် အောက်ပါအရာများကို ဖန်တီးထားမည် -

| Session | Deliverable | Skills Demonstrated |
|---------|-------------|---------------------|
| **1** | streaming ဖြင့် chat application | Service setup, basic completions, streaming UX |
| **2** | RAG system with evaluation | Embeddings, semantic search, quality metrics |
| **3** | Multi-model benchmark suite | Performance measurement, model comparison |
| **4** | SLM vs LLM comparator | Trade-off analysis, optimization strategies |
| **5** | Multi-agent orchestrator | Agent design, memory management, coordination |
| **6** | Intelligent routing system | Intent detection, model selection, scalability |

### ကျွမ်းကျင်မှု Matrix

| Skill Level | Session 1-2 | Session 3-4 | Session 5-6 |
|-------------|-------------|-------------|-------------|
| **Beginner** | ✅ Setup & basics | ⚠️ Challenging | ❌ Too advanced |
| **Intermediate** | ✅ Quick review | ✅ Core learning | ⚠️ Stretch goals |
| **Advanced** | ✅ Breeze through | ✅ Refinement | ✅ Production patterns |

### အလုပ်အကိုင်အတွက် အသင့်ဖြစ်သော အတတ်ပညာများ

**ဒီအလုပ်ရုံဆွေးနွေးပွဲပြီးနောက် သင်သည် အောက်ပါအတတ်ပညာများကို ရရှိမည် -**

✅ **Privacy-First Applications တည်ဆောက်ခြင်း**
- PHI/PII ကို ဒေသတွင်းတွင် ကိုင်တွယ်သော ကျန်းမာရေးအက်ပလီကေးရှင်းများ
- စည်းမျဉ်းများနှင့် ကိုက်ညီသော ငွေကြေးဆိုင်ရာ ဝန်ဆောင်မှုများ
- ဒေတာအာဏာပိုင်မှုလိုအပ်သော အစိုးရစနစ်များ

✅ **Edge ပတ်ဝန်းကျင်များအတွက် အဆင့်မြှင့်တင်ခြင်း**
- အရင်းအမြစ်ကန့်သတ်ထားသော IoT devices
- Offline-first mobile applications
- Low-latency real-time systems

✅ **ဉာဏ်ရည်ရှိသော Architectures ကို ဒီဇိုင်းဆွဲခြင်း**
- အလုပ်အဆင့်များအတွက် Multi-agent systems
- Hybrid edge-cloud deployments
- ကုန်ကျစရိတ်အဆင့်မြှင့်တင်ထားသော AI infrastructure

✅ **Edge AI Initiatives များကို ဦးဆောင်ခြင်း**
- Project များအတွက် Edge AI feasibility ကို အကဲဖြတ်ခြင်း
- သင့်လျော်သော မော်ဒယ်များနှင့် frameworks ကို ရွေးချယ်ခြင်း
- Scalable local AI solutions ကို Architect လုပ်ခြင်း

---

## 🗺️ အလုပ်ရုံဆွေးနွေးပွဲဖွဲ့စည်းမှု

### Session အကျဉ်းချုပ် (6 Sessions × 30 မိနစ် = 3 နာရီ)

| Session | Topic | Focus | Duration |
|---------|-------|-------|----------|
| **1** | Foundry Local ဖြင့် စတင်ခြင်း | Install, validate, first completions | 30 min |
| **2** | RAG ဖြင့် AI Solutions တည်ဆောက်ခြင်း | Prompt engineering, embeddings, evaluation | 30 min |
| **3** | Open Source Models | Model discovery, benchmarking, selection | 30 min |
| **4** | Cutting Edge Models | SLM vs LLM, optimization, frameworks | 30 min |
| **5** | AI-Powered Agents | Agent design, orchestration, memory | 30 min |
| **6** | Models as Tools | Routing, chaining, scaling strategies | 30 min |

---

## 🚀 အမြန်စတင်ခြင်း

### လိုအပ်ချက်များ

**System Requirements:**
- **OS**: Windows 10/11, macOS 11+, or Linux (Ubuntu 20.04+)
- **RAM**: အနည်းဆုံး 8GB, အကြံပြုချက် 16GB+
- **Storage**: မော်ဒယ်များအတွက် အခမဲ့နေရာ 10GB+
- **CPU**: AVX2 support ပါသော နောက်ဆုံးပေါ် processor
- **GPU** (optional): CUDA-compatible သို့မဟုတ် Qualcomm NPU acceleration အတွက်

**Software Requirements:**
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Installation Guide](../../../Workshop))
- **Git** ([Download](https://git-scm.com/downloads))
- **Visual Studio Code** (recommended) ([Download](https://code.visualstudio.com/))

### 3 ခြေလှမ်းဖြင့် Setup

#### 1. Foundry Local ကို Install လုပ်ပါ

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verify Installation:**
```bash
foundry --version
foundry service status
```

**Azure AI Foundry Local ကို fixed port ဖြင့် လည်ပတ်နေသည်ကို သေချာပါ**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verify လုပ်ပါ:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**ရရှိနိုင်သော မော်ဒယ်များကို ရှာဖွေခြင်း**
Foundry Local instance တွင် ရရှိနိုင်သော မော်ဒယ်များကို models endpoint မှ query လုပ်နိုင်သည်:

```bash
# cmd/bash/powershell
foundry model list
```

Web Endpoint ကို အသုံးပြုခြင်း 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Repository ကို Clone လုပ်ပြီး Dependencies ကို Install လုပ်ပါ

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. သင့်ပထမဆုံး Sample ကို Run လုပ်ပါ

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ အောင်မြင်မှု!** သင်သည် edge AI အကြောင်း streaming response ကို မြင်ရမည်။

---

## 📦 အလုပ်ရုံဆွေးနွေးပွဲ Resources

### Python Samples

အဓိကအကြောင်းအရာများကို ဖော်ပြသည့် လက်တွေ့လေ့လာမှုများ -

| Session | Sample | Description | Run Time |
|---------|--------|-------------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Basic & streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG with embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG quality evaluation | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Multi-model benchmarking | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM comparison | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Multi-agent system | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Intent-based routing | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Multi-step pipeline | ~60s |

### Jupyter Notebooks

ရှင်းလင်းချက်များနှင့် visualization များပါသော interactive exploration -

| Session | Notebook | Description | Difficulty |
|---------|----------|-------------|------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Chat basics & streaming | ⭐ Beginner |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Build RAG system | ⭐⭐ Intermediate |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluate RAG quality | ⭐⭐ Intermediate |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Model benchmarking | ⭐⭐ Intermediate |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Model comparison | ⭐⭐ Intermediate |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Agent orchestration | ⭐⭐⭐ Advanced |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Intent routing | ⭐⭐⭐ Advanced |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Pipeline orchestration | ⭐⭐⭐ Advanced |

### Documentation

လမ်းညွှန်များနှင့် ရည်ညွှန်းချက်များ -

| Document | Description | Use When |
|----------|-------------|----------|
| [QUICK_START.md](./QUICK_START.md) | Fast-track setup guide | Starting from scratch |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Command & API cheat sheet | Need quick answers |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK patterns & examples | Writing code |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Environment variable guide | Configuring samples |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Latest sample improvements | Understanding changes |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Migration guide | Upgrading code |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Common issues & fixes | Debugging problems |

---

## 🎓 လေ့လာမှုလမ်းကြောင်း အကြံပြုချက်များ

### မူလတန်း (3-4 နာရီ)
1. ✅ Session 1: စတင်ခြင်း (setup နှင့် basic chat ကို အဓိကထား)
2. ✅ Session 2: RAG Basics (evaluation ကို စတင်မှာ ကျော်သွားပါ)
3. ✅ Session 3: ရိုးရှင်းသော Benchmarking (မော်ဒယ် 2 ခုသာ)
4. ⏭️ Session 4-6 ကို ယာယီ ကျော်သွားပါ
5. 🔄 ပထမဆုံး application တည်ဆောက်ပြီးနောက် Session 4-6 သို့ ပြန်လာပါ

### အလယ်အလတ် Developer များအတွက် (3 နာရီ)
1. ⚡ Session 1: Setup validation ကို အမြန်လုပ်ပါ
2. ✅ Session 2: RAG pipeline ကို evaluation ဖြင့် ပြည့်စုံစွာ ပြီးမြောက်ပါ
3. ✅ Session 3: Benchmarking suite အပြည့်
4. ✅ Session 4: မော်ဒယ် optimization
5. ✅ Session 5-6: Architecture patterns ကို အဓိကထား

### ကျွမ်းကျင် Practitioner များအတွက် (2-3 နာရီ)
1. ⚡ Session 1-3: အမြန် review နှင့် validation
2. ✅ Session 4: Optimization deep-dive
3. ✅ Session 5: Multi-agent architecture
4. ✅ Session 6: Production patterns နှင့် scaling
5. 🚀 Extend:
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM နှင့် LLM, WebGPU, Chainlit RAG, ONNX acceleration |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Agent အခန်းကဏ္ဍများ, မှတ်ဉာဏ်, ကိရိယာများ, စီမံခန့်ခွဲမှု |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, chaining, Azure သို့သွားသော scale လမ်းကြောင်း |

Session ဖိုင်တစ်ခုစီတွင် ပါဝင်သည် - အကျဉ်းချုပ်, သင်ယူရမည့်ရည်ရွယ်ချက်များ, ၃၀ မိနစ်အတွင်း demo flow, starter project, validation checklist, troubleshooting, နှင့် Foundry Local Python SDK အတွက်ရင်းနှီးသောအရင်းအမြစ်များ။

### နမူနာ Scripts

Workshop အတွက်လိုအပ်သော dependencies ကို install လုပ်ရန် (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Foundry Local service ကို macOS မှ Windows မျက်နှာပြင်သို့ (သို့) VM မှ run လုပ်နေပါက endpoint ကို export လုပ်ပါ:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Session | Script(s) | ဖော်ပြချက် |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap service & streaming chat |
| 2 | `samples/session02/rag_pipeline.py` | အနည်းဆုံး RAG (in-memory embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | RAG ကို ragas metrics ဖြင့်အကဲဖြတ်ခြင်း |
| 3 | `samples/session03/benchmark_oss_models.py` | Multi-model latency & throughput benchmarking |
| 4 | `samples/session04/model_compare.py` | SLM နှင့် LLM ကို (latency & sample output) နှိုင်းယှဉ်ခြင်း |
| 5 | `samples/session05/agents_orchestrator.py` | Two-agent research → editorial pipeline |
| 6 | `samples/session06/models_router.py` | Intent-based routing demo |
|   | `samples/session06/models_pipeline.py` | Multi-step plan/execute/refine chain |

### Environment Variables (Samples အားလုံးတွင်တူညီ)

| Variable | ရည်ရွယ်ချက် | နမူနာ |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | အခြေခံနမူနာများအတွက် default single model alias | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM နှင့် LLM model ကိုရှင်းလင်းစွာနှိုင်းယှဉ်ရန် | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Benchmark လုပ်ရန် aliases များစာရင်း | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Model တစ်ခုစီအတွက် benchmark repetitions | `3` |
| `BENCH_PROMPT` | Benchmarking အတွက်အသုံးပြုသော prompt | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | RAG pipeline အတွက် test query ကို override | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Agents pipeline query ကို override | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Research agent အတွက် model alias | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Editor agent အတွက် model alias (ကွဲပြားနိုင်သည်) | `gpt-oss-20b` |
| `SHOW_USAGE` | `1` ဖြစ်ပါက completion တစ်ခုစီအတွက် token usage ကို print လုပ်သည် | `1` |
| `RETRY_ON_FAIL` | `1` ဖြစ်ပါက transient chat errors တွင်တစ်ကြိမ် retry လုပ်သည် | `1` |
| `RETRY_BACKOFF` | Retry မလုပ်မီ seconds | `1.0` |

Variable မရှိပါက script များသည် default ကို fallback လုပ်သည်။ Single-model demos အတွက် `FOUNDRY_LOCAL_ALIAS` သာလိုအပ်သည်။

### Utility Module

နမူနာအားလုံးသည် `samples/workshop_utils.py` helper ကိုမျှဝေထားပြီး:

* Cached `FoundryLocalManager` နှင့် OpenAI client ဖန်တီးခြင်း
* `chat_once()` helper (optional retry နှင့် usage printing ပါဝင်သည်)
* Simple token usage reporting (`SHOW_USAGE=1` ဖြင့် enable လုပ်ပါ)

ဤသည်သည် duplication ကိုလျှော့ချပြီး efficient local model orchestration အတွက်အကောင်းဆုံးအလေ့အကျင့်များကိုဖော်ပြသည်။

## Optional Enhancements (Session များအနှံ့)

| Theme | Enhancement | Sessions | Env / Toggle |
|-------|-------------|----------|--------------|
| Determinism | Fixed temperature + stable prompt sets | 1–6 | `temperature=0`, `top_p=1` ကို set လုပ်ပါ |
| Token Usage Visibility | Cost/efficiency သင်ကြားမှုကိုတိုးတက်စေသည် | 1–6 | `SHOW_USAGE=1` |
| Streaming First Token | Perceived latency metric | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Retry Resilience | Transient cold-start ကို handle လုပ်သည် | All | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-Model Agents | Heterogeneous role specialization | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptive Routing | Intent + cost heuristics | 6 | Router ကို escalation logic ဖြင့်တိုးချဲ့ပါ |
| Vector Memory | Long-term semantic recall | 2,5,6 | FAISS/Chroma embedding index ကိုထည့်သွင်းပါ |
| Trace Export | Auditing & evaluation | 2,5,6 | JSON lines ကိုတစ်ဆင့်ချင်း append လုပ်ပါ |
| Quality Rubrics | Qualitative tracking | 3–6 | Secondary scoring prompts |
| Smoke Tests | Workshop မတိုင်မီ validation လုပ်ရန် | All | `python Workshop/tests/smoke.py` |

### Deterministic Quick Start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

တူညီသော input များကိုထပ်ခါတလဲလဲ run လုပ်ပါက stable token count များကိုမျှော်လင့်ပါ။

### RAG Evaluation (Session 2)

`rag_eval_ragas.py` ကိုအသုံးပြု၍ tiny synthetic dataset အပေါ် relevancy, faithfulness, နှင့် context precision ကိုအကဲဖြတ်ပါ:

```powershell
python samples/session02/rag_eval_ragas.py
```

မေးခွန်းများ, contexts, နှင့် ground truths များပါဝင်သော JSONL ကိုထည့်သွင်းပြီး Hugging Face `Dataset` သို့ convert လုပ်ပါ။

## CLI Command Accuracy Appendix

Workshop သည် Foundry Local CLI commands တွင်လက်ရှိ document လုပ်ထားသော / stable commands များကိုသာအသုံးပြုသည်။

### Stable Commands Referenced

| Category | Command | ရည်ရွယ်ချက် |
|----------|---------|---------|
| Core | `foundry --version` | Installed version ကိုပြပါ |
| Core | `foundry init` | Configuration ကို initialize လုပ်ပါ |
| Service | `foundry service start` | Local service ကိုစတင်ပါ (auto မဟုတ်ပါက) |
| Service | `foundry status` | Service status ကိုပြပါ |
| Models | `foundry model list` | Catalog / available models ကိုစာရင်းပြပါ |
| Models | `foundry model download <alias>` | Model weights ကို cache ထဲသို့ download လုပ်ပါ |
| Models | `foundry model run <alias>` | Model ကို locally launch (load) လုပ်ပါ; `--prompt` နှင့်ပေါင်းစပ်၍ one-shot |
| Models | `foundry model unload <alias>` / `foundry model stop <alias>` | Model ကို memory မှ unload လုပ်ပါ (supported ဖြစ်ပါက) |
| Cache | `foundry cache list` | Cached (downloaded) models ကိုစာရင်းပြပါ |
| System | `foundry system info` | Hardware & acceleration capabilities snapshot |
| System | `foundry system gpu-info` | GPU diagnostic info |
| Config | `foundry config list` | လက်ရှိ config values ကိုပြပါ |
| Config | `foundry config set <key> <value>` | Configuration ကို update လုပ်ပါ |

### One-Shot Prompt Pattern

`model chat` subcommand ကိုမသုံးတော့ဘဲ:

```powershell
foundry model run <alias> --prompt "Your question here"
```

ဤသည်သည် prompt/response cycle တစ်ခုကို run လုပ်ပြီးထွက်သွားသည်။

### Removed / Avoided Patterns

| Deprecated / Undocumented | Replacement / Guidance |
|---------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | `foundry model list` + recent activity / logs ကိုအသုံးပြုပါ |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Benchmark Python script + OS tools (Task Manager / `nvidia-smi`) ကိုအသုံးပြုပါ |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetry

- Latency, p95, tokens/sec: `samples/session03/benchmark_oss_models.py`
- First-token latency (streaming): `BENCH_STREAM=1` ကို set လုပ်ပါ
- Resource usage: OS monitors (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info` ကိုအသုံးပြုပါ။

CLI telemetry commands များ upstream တွင် stable ဖြစ်လာသည်နှင့်အမျှ session markdowns တွင်အလွယ်တကူထည့်သွင်းနိုင်သည်။

### Automated Lint Guard

Automated linter သည် markdown ဖိုင်များ၏ fenced code blocks အတွင်း deprecated CLI patterns များပြန်လည်ထည့်သွင်းခြင်းကိုကာကွယ်သည်:

Script: `Workshop/scripts/lint_markdown_cli.py`

Deprecated patterns များကို code fences အတွင်း blocked လုပ်သည်။

အကြံပြုထားသောအစားထိုးများ:
| Deprecated | Replacement |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark script + system tools |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Local မှ run လုပ်ပါ:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` သည် push & PR တစ်ခုစီတွင် run လုပ်သည်။

Optional pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Quick CLI → SDK Migration Table

| Task | CLI One-Liner | SDK (Python) Equivalent | Notes |
|------|---------------|-------------------------|-------|
| Run a model once (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK သည် service & caching ကို auto bootstrap လုပ်သည် |
| Download (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager သည် alias များအတွက်အကောင်းဆုံး variant ကိုရွေးချယ်သည် |
| List catalog | `foundry model list` | `# manager ကို alias တစ်ခုစီအတွက်အသုံးပြုပါ သို့မဟုတ် known list ကို maintain လုပ်ပါ` | CLI သည် aggregate လုပ်သည်; SDK သည်လက်ရှိအခြေအနေတွင် per-alias instantiation |
| List cached models | `foundry cache list` | `manager.list_cached_models()` | Manager init (alias တစ်ခု) ပြီးနောက် |
| Enable GPU acceleration | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK သည် config ကိုအသုံးပြုထားသည်ဟုယူဆသည်` | Configuration သည် external side effect ဖြစ်သည် |
| Get endpoint URL | (implicit) | `manager.endpoint` | OpenAI-compatible client ဖန်တီးရန်အသုံးပြုသည် |
| Warm a model | `foundry model run <alias>` then first prompt | `chat_once(alias, messages=[...])` (utility) | Utilities သည် initial cold latency warmup ကို handle လုပ်သည် |
| Measure latency | `python benchmark_oss_models.py` | `import benchmark_oss_models` (သို့မဟုတ် new exporter script) | Consistent metrics အတွက် script ကို prefer လုပ်ပါ |
| Stop / unload model | `foundry model unload <alias>` | (Not exposed – service / process ကို restart လုပ်ပါ) | Workshop flow အတွက်မလိုအပ်ပါ |
| Retrieve token usage | (view output) | `resp.usage.total_tokens` | Backend သည် usage object ကို return လုပ်ပါကပေးသည် |

## Benchmark Markdown Export

`Workshop/scripts/export_benchmark_markdown.py` script ကိုအသုံးပြု၍ (logic သည် `samples/session03/benchmark_oss_models.py` နှင့်တူသည်) GitHub-friendly Markdown table နှင့် raw JSON ကို emit လုပ်ပါ။

### နမူနာ

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

ဖန်တီးထားသောဖိုင်များ:
| File | Contents |
|------|----------|
| `benchmark_report.md` | Markdown table + interpretation hints |
| `benchmark_report.json` | Raw metrics array (diffing / trend tracking အတွက်) |

Environment တွင် `BENCH_STREAM=1` ကို set လုပ်၍ first-token latency ကိုထည့်သွင်းပါ (supported ဖြစ်ပါက)။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာပိုင်အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။