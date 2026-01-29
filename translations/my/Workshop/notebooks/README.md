# Workshop Notebooks

> **Edge AI သင်ယူမှုအတွက် လက်တွေ့ကျကျ Interactive Jupyter Notebooks**
>
> အခြေခံ chat completions မှစ၍ Microsoft Foundry Local နှင့် Small Language Models ကို အသုံးပြုသော အဆင့်မြင့် multi-agent systems အထိ တိုးတက်မှုရှိသော tutorials များ။

---

## 📖 အကျဉ်းချုပ်

**EdgeAI for Beginners Workshop Notebooks** စုစည်းမှုမှ ကြိုဆိုပါတယ်။ ဒီ interactive Jupyter notebooks တွေက real-time မှာ Edge AI code ကို ရေးသား၊ အကောင်အထည်ဖော်၊ စမ်းသပ်နိုင်တဲ့ လက်တွေ့ကျကျ သင်ယူမှုအတွေ့အကြုံကို ပေးစွမ်းပါတယ်။

### Jupyter Notebooks ကို ဘာကြောင့် အသုံးပြုသင့်လဲ?

ရိုးရှင်းတဲ့ tutorials များနှင့် မတူဘဲ၊ ဒီ notebooks တွေက အောက်ပါအကျိုးကျေးဇူးများကို ပေးစွမ်းပါတယ်-

- **Interactive Learning**: Code cells များကို run လုပ်ပြီး ချက်ချင်းရလဒ်ကို ကြည့်ရှုနိုင်ခြင်း  
- **Experimentation**: Parameters များကို ပြောင်းလဲပြီး ချက်ချင်းအပြောင်းအလဲများကို တွေ့မြင်နိုင်ခြင်း  
- **Documentation**: Inline explanations နှင့် markdown cells များက အကြောင်းအရာများကို လမ်းညွှန်ပေးခြင်း  
- **Reproducibility**: ပြန်လည်အသုံးပြုနိုင်သော အလုပ်လုပ်တဲ့ နမူနာများ  
- **Visualization**: Performance metrics, embeddings, နှင့် ရလဒ်များကို inline မှာ ကြည့်ရှုနိုင်ခြင်း  

### ဒီ Notebooks တွေက ဘာကြောင့် ထူးခြားသလဲ?

Notebook တစ်ခုစီကို **ထုတ်လုပ်မှုအဆင့်အထိ အသုံးပြုနိုင်သော အကောင်းဆုံး လုပ်နည်းများ** အတိုင်း ဒီဇိုင်းဆွဲထားပါတယ်-

✅ **Comprehensive Error Handling** - Error များကို သက်သာစွာ ကိုင်တွယ်ပြီး အသိပေး message များ  
✅ **Type Hints & Documentation** - Function အကြောင်းအရာများနှင့် docstrings များကို ရှင်းလင်းစွာ ဖော်ပြထားခြင်း  
✅ **Performance Monitoring** - Token အသုံးပြုမှု tracking နှင့် latency အတိုင်းအတာများ  
✅ **Modular Design** - သင့် project များအတွက် ပြန်လည်အသုံးပြုနိုင်သော patterns  
✅ **Progressive Complexity** - အတန်းများကို အဆင့်ဆင့် တိုးတက်စွာ တည်ဆောက်ထားခြင်း  

---

## 🎯 သင်ယူရမည့် ရည်မှန်းချက်များ

### သင်တိုးတက်စွာ တိုးတက်နိုင်မည့် အရည်အချင်းများ

ဒီ notebooks များကို လုပ်ဆောင်ခြင်းအားဖြင့် သင်သည် အောက်ပါအရည်အချင်းများကို ကျွမ်းကျင်လာမည်ဖြစ်သည်-

1. **Local AI Service Management**
   - Microsoft Foundry Local services ကို configure နှင့် စီမံခြင်း  
   - သင့် hardware အတွက် သင့်လျော်သော models များကို ရွေးချယ်နှင့် load လုပ်ခြင်း  
   - Resource အသုံးပြုမှုကို စောင့်ကြည့်ပြီး performance ကို အကောင်းဆုံးဖြစ်အောင် ပြုလုပ်ခြင်း  
   - Service discovery နှင့် health checking ကို ကိုင်တွယ်ခြင်း  

2. **AI Application Development**
   - OpenAI-compatible chat completions ကို locally မှာ အကောင်အထည်ဖော်ခြင်း  
   - User experience အတွက် streaming interfaces တည်ဆောက်ခြင်း  
   - Small Language Models အတွက် ထိရောက်သော prompts များ ဒီဇိုင်းဆွဲခြင်း  
   - Local models များကို applications တွင် ပေါင်းစပ်ခြင်း  

3. **Retrieval Augmented Generation (RAG)**
   - Vector embeddings ဖြင့် semantic search တည်ဆောက်ခြင်း  
   - LLM responses ကို domain-specific documents တွင် အခြေခံခြင်း  
   - RAGAS metrics ဖြင့် RAG quality ကို အကဲဖြတ်ခြင်း  
   - Prototype မှ production အထိ scale လုပ်ခြင်း  

4. **Performance Optimization**
   - Models များကို စနစ်တကျ benchmark လုပ်ခြင်း  
   - Latency, throughput, နှင့် first-token time ကို တိုင်းတာခြင်း  
   - Small Language Models နှင့် Large Language Models ကို နှိုင်းယှဉ်ခြင်း  
   - Performance/quality trade-offs အပေါ် အကောင်းဆုံး models ကို ရွေးချယ်ခြင်း  

5. **Multi-Agent Orchestration**
   - အလုပ်အမျိုးမျိုးအတွက် အထူး agent များကို ဒီဇိုင်းဆွဲခြင်း  
   - Agent memory နှင့် context management ကို အကောင်အထည်ဖော်ခြင်း  
   - အလုပ်ရှုပ်သော workflows တွင် multiple agents များကို စီမံခြင်း  
   - Agent collaboration အတွက် coordinator patterns တည်ဆောက်ခြင်း  

6. **Intelligent Model Routing**
   - Intent detection နှင့် pattern matching ကို အကောင်အထည်ဖော်ခြင်း  
   - Queries များကို သင့် model များသို့ အလိုအလျောက် route လုပ်ခြင်း  
   - Multi-step pipelines (plan → execute → refine) တည်ဆောက်ခြင်း  
   - Scalable model-as-tools architectures ကို ဒီဇိုင်းဆွဲခြင်း  

---

## 🎓 သင်ယူပြီးရရှိမည့် အကျိုးကျေးဇူးများ

### သင်တည်ဆောက်မည့် အရာများ

| Notebook | Deliverable | Skills Demonstrated | Difficulty |
|----------|-------------|---------------------|------------|
| **Session 01** | Streaming chat app | Service setup, basic completions, streaming UX | ⭐ Beginner |
| **Session 02 (RAG)** | RAG pipeline with evaluation | Embeddings, semantic search, quality metrics | ⭐⭐ Intermediate |
| **Session 02 (Eval)** | RAG quality evaluator | RAGAS metrics, systematic evaluation | ⭐⭐ Intermediate |
| **Session 03** | Multi-model benchmark | Performance measurement, model comparison | ⭐⭐ Intermediate |
| **Session 04** | SLM vs LLM comparator | Trade-off analysis, optimization strategies | ⭐⭐⭐ Advanced |
| **Session 05** | Multi-agent orchestrator | Agent design, memory, coordination | ⭐⭐⭐ Advanced |
| **Session 06 (Router)** | Intelligent routing system | Intent detection, model selection | ⭐⭐⭐ Advanced |
| **Session 06 (Pipeline)** | Multi-step pipeline | Plan/execute/refine workflows | ⭐⭐⭐ Advanced |

### Competency Progression

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Workshop Schedule

### 🚀 Half-Day Workshop (3.5 hours)

**Team training sessions, hackathons, conference workshops အတွက် အကောင်းဆုံး**

| Time | Duration | Session | Topics | Activities |
|------|----------|---------|--------|------------|
| **0:00** | 30 min | Setup & Intro | Environment setup, Foundry Local installation | Install dependencies, verify setup |
| **0:30** | 30 min | Session 01 | Basic chat completions, streaming | Run notebook, modify prompts |
| **1:00** | 45 min | Session 02 | RAG pipeline, embeddings, evaluation | Build RAG system, test queries |
| **1:45** | 15 min | Break | ☕ Coffee & questions | — |
| **2:00** | 30 min | Session 03 | Multi-model benchmarking | Compare 3+ models |
| **2:30** | 30 min | Session 04 | SLM vs LLM trade-offs | Analyze performance/quality |
| **3:00** | 30 min | Session 05-06 | Multi-agent systems & routing | Explore advanced patterns |

**Output**: Workshop ပြီးဆုံးချိန်တွင် 6 Edge AI applications နှင့် production-ready code patterns ရရှိမည်။

---

### 🎓 Full-Day Workshop (6 hours)

**In-depth training, bootcamps, university courses အတွက် အကောင်းဆုံး**

| Time | Duration | Session | Topics | Activities |
|------|----------|---------|--------|------------|
| **0:00** | 45 min | Setup & Theory | Environment setup, Edge AI fundamentals | Install, verify, discuss use cases |
| **0:45** | 45 min | Session 01 | Chat completions deep dive | Implement basic & streaming chat |
| **1:30** | 30 min | Break | ☕ Coffee & networking | — |
| **2:00** | 60 min | Session 02 (Both) | RAG pipeline + RAGAS evaluation | Build complete RAG system |
| **3:00** | 30 min | Hands-On Lab 1 | Custom RAG for your domain | Apply to own documents |
| **3:30** | 30 min | Lunch | 🍽️ | — |
| **4:00** | 45 min | Session 03 | Benchmarking methodology | Systematic model comparison |
| **4:45** | 45 min | Session 04 | Optimization strategies | SLM vs LLM analysis |
| **5:30** | 60 min | Session 05-06 | Advanced orchestration | Multi-agent systems, routing |
| **6:30** | 30 min | Hands-On Lab 2 | Build custom agent system | Design your own orchestrator |

**Output**: Edge AI patterns အပေါ် အနက်ရှိုင်းသော နားလည်မှုနှင့် 2 custom projects ရရှိမည်။

---

### 📚 Self-Paced Learning (2 weeks)

**Individual learners, online courses, self-study အတွက် အကောင်းဆုံး**

#### Week 1: Foundations (6 hours)

| Day | Focus | Duration | Notebooks | Homework |
|-----|-------|----------|-----------|----------|
| **Mon** | Setup & Basics | 1.5 hrs | Session 01 | Modify prompts, test streaming |
| **Wed** | RAG Fundamentals | 2 hrs | Session 02 (both) | Add your own documents |
| **Fri** | Benchmarking | 1.5 hrs | Session 03 | Compare additional models |
| **Sat** | Review & Practice | 1 hr | All Week 1 | Complete exercises, debug |

#### Week 2: Advanced (5 hours)

| Day | Focus | Duration | Notebooks | Homework |
|-----|-------|----------|-----------|----------|
| **Mon** | Optimization | 1.5 hrs | Session 04 | Document trade-offs |
| **Wed** | Multi-Agent Systems | 2 hrs | Session 05 | Design custom agents |
| **Fri** | Intelligent Routing | 1.5 hrs | Session 06 (both) | Build routing logic |
| **Sat** | Final Project | 2 hrs | Integration | Combine multiple patterns |

**Output**: Edge AI patterns အပေါ် ကျွမ်းကျင်မှုနှင့် portfolio project ရရှိမည်။

---

## 📔 Notebook Descriptions

### 📘 Session 01: Chat Bootstrap
**File**: `session01_chat_bootstrap.ipynb`  
**Duration**: 20-30 minutes  
**Prerequisites**: None  
**Difficulty**: ⭐ Beginner

**What You'll Learn**:
- Foundry Local Python SDK ကို install နှင့် configure လုပ်ခြင်း  
- `FoundryLocalManager` ကို အသုံးပြု၍ automatic service discovery  
- OpenAI-compatible API ဖြင့် basic chat completions ကို အကောင်အထည်ဖော်ခြင်း  
- Streaming responses တည်ဆောက်ခြင်း  
- Error များနှင့် service unavailability ကို သက်သာစွာ ကိုင်တွယ်ခြင်း  

**Key Concepts**: Service management, chat completions, streaming, error handling

**You'll Build**: Streaming support ပါသော interactive chat application

---

### 📗 Session 02: RAG Pipeline
**File**: `session02_rag_pipeline.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Session 01  
**Difficulty**: ⭐⭐ Intermediate

**What You'll Learn**:
- Retrieval Augmented Generation (RAG) pattern ကို အကောင်အထည်ဖော်ခြင်း  
- Sentence-transformers ဖြင့် vector embeddings တည်ဆောက်ခြင်း  
- Cosine similarity ဖြင့် semantic search တည်ဆောက်ခြင်း  
- LLM responses ကို domain-specific documents တွင် အခြေခံခြင်း  
- Import guards ဖြင့် optional dependencies ကို ကိုင်တွယ်ခြင်း  

**Key Concepts**: RAG architecture, embeddings, semantic search, vector similarity

**You'll Build**: Document-grounded question-answering system

---

### 📗 Session 02: RAG Evaluation with RAGAS
**File**: `session02_rag_eval_ragas.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Session 02 RAG Pipeline  
**Difficulty**: ⭐⭐ Intermediate

**What You'll Learn**:
- RAG quality ကို industry-standard metrics ဖြင့် အကဲဖြတ်ခြင်း  
- Context relevance, answer relevance, faithfulness ကို တိုင်းတာခြင်း  
- RAGAS framework ကို systematic evaluation အတွက် အသုံးပြုခြင်း  
- RAG quality ပြဿနာများကို ရှာဖွေပြီး ပြင်ဆင်ခြင်း  
- သင့် domain အတွက် evaluation datasets တည်ဆောက်ခြင်း  

**Key Concepts**: RAG evaluation, RAGAS metrics, quality measurement, systematic testing

**You'll Build**: RAG quality evaluation framework

---

### 📙 Session 03: Benchmark OSS Models
**File**: `session03_benchmark_oss_models.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Session 01  
**Difficulty**: ⭐⭐ Intermediate

**What You'll Learn**:
- Models များကို စနစ်တကျ benchmark လုပ်ခြင်း  
- Latency, throughput, first-token time ကို တိုင်းတာခြင်း  
- Model များ fail ဖြစ်ပါက graceful degradation ကို အကောင်အထည်ဖော်ခြင်း  
- Model families များအကြား performance ကို နှိုင်းယှဉ်ခြင်း  
- Benchmark results များကို visualization နှင့် analysis ပြုလုပ်ခြင်း  

**Key Concepts**: Performance benchmarking, latency measurement, model comparison, statistical analysis

**You'll Build**: Multi-model benchmarking suite

---

### 📙 Session 04: Model Comparison (SLM vs LLM)
**File**: `session04_model_compare.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Sessions 01, 03  
**Difficulty**: ⭐⭐⭐ Advanced

**What You'll Learn**:
- Small Language Models နှင့် Large Language Models ကို နှိုင်းယှဉ်ခြင်း  
- Performance နှင့် quality trade-offs ကို analysis ပြုလုပ်ခြင်း  
- Edge-suitability metrics ကို တိုင်းတာခြင်း  
- Deployment constraints အပေါ် အကောင်းဆုံး models ကို ရွေးချယ်ခြင်း  
- Model selection အတွက် decision criteria ကို documentation ပြုလုပ်ခြင်း  

**Key Concepts**: Model selection, trade-off analysis, optimization strategies, deployment planning

**You'll Build**: SLM vs LLM comparison framework

---

### 📕 Session 05: Multi-Agent Orchestrator
**File**: `session05_agents_orchestrator.ipynb`  
**Duration**: 45-60 minutes  
**Prerequisites**: Sessions 01-02  
**Difficulty**: ⭐⭐⭐ Advanced

**What You'll Learn**:
- အလုပ်အမျိုးမျိုးအတွက် အထူး agent များကို ဒီဇိုင်းဆွဲခြင်း  
- Agent memory နှင့် context management ကို အကောင်အထည်ဖော်ခြင်း  
- Agent collaboration အတွက် coordinator patterns တည်ဆောက်ခြင်း  
- Agent communication နှင့် handoffs ကို ကိုင်တွယ်ခြင်း  
- Multi-agent system performance ကို စောင့်ကြည့်ခြင်း  

**Key Concepts**: Agent architecture, coordinator patterns, memory management, agent orchestration

**You'll Build**: Multi-agent system with coordinator and specialists

---

### 📕 Session 06: Model Router
**File**: `session06_models_router.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Sessions 01, 03  
**Difficulty**: ⭐⭐⭐ Advanced

**What You'll Learn**:
- Intent detection နှင့် pattern matching ကို အကောင်အထည်ဖော်ခြင်း  
- Keyword-based model routing တည်ဆောက်ခြင်း  
- Queries များကို သင့် model များသို့ အလိုအလျောက် route လုပ်ခြင်း  
- Multi-model registries ကို configure လုပ်ခြင်း  
- Routing decisions နှင့် performance ကို စောင့်ကြည့်ခြင်း  

**Key Concepts**: Intent detection, model routing, pattern matching, intelligent selection

**You'll Build**: Intelligent model routing system

---

### 📕 Session 06: Multi-Step Pipeline
**File**: `session06_models_pipeline.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Sessions 01, 06 Router  
**Difficulty**: ⭐⭐⭐ Advanced

**What You'll Learn**:
- Multi-step AI pipelines (plan → execute → refine) တည်ဆောက်ခြင်း  
- Intelligent model selection အတွက် router ကို ပေါင်းစပ်ခြင်း  
- Pipeline error handling နှင့် recovery ကို အကောင်အထည်ဖော်ခြင်း  
- Pipeline performance နှင့် stages ကို စောင့်ကြည့်ခြင်း  
- အဆင့်မြင့်မော်ဒယ်-အဖြစ်-ကိရိယာများ၏ အဆင့်မြှင့်တင်နိုင်သော ဖွဲ့စည်းပုံများကို ဒီဇိုင်းဆွဲပါ

**အဓိကအကြောင်းအရာများ**: ပိုက်လိုင်းဖွဲ့စည်းပုံ, အဆင့်များဖြင့် အဆက်မပြတ်လုပ်ဆောင်မှု, အမှားပြန်လည်ကောင်းမွန်ရေး, အဆင့်မြှင့်တင်နိုင်မှုပုံစံများ

**သင်တည်ဆောက်မည့်အရာ**: လမ်းကြောင်းသတ်မှတ်ထားသော အဆင့်များစွာပါဝင်သော ဉာဏ်ရည်ပိုက်လိုင်း

---

## 🚀 စတင်လိုက်ပါ

### ကြိုတင်လိုအပ်ချက်များ

**စနစ်လိုအပ်ချက်များ**:
- **OS**: Windows 10/11, macOS 11+, သို့မဟုတ် Linux (Ubuntu 20.04+)
- **RAM**: အနည်းဆုံး 8GB, အကြံပြုချက် 16GB+
- **သိုလှောင်မှု**: မော်ဒယ်များအတွက် အခမဲ့နေရာ 10GB+
- **ဟာ့ဒ်ဝဲ**: AVX2 ပါဝင်သော CPU; GPU (CUDA, Qualcomm NPU) ရွေးချယ်နိုင်သည်

**ဆော့ဖ်ဝဲလိုအပ်ချက်များ**:
- **Python 3.8+** နှင့် pip
- **Jupyter Notebook** သို့မဟုတ် **VS Code** (Jupyter extension ပါဝင်)
- **Microsoft Foundry Local** တပ်ဆင်ပြီး ဖွဲ့စည်းထားသည်
- **Git** (repository ကို clone လုပ်ရန်)

### တပ်ဆင်ခြင်းအဆင့်များ

#### 1. Foundry Local ကို တပ်ဆင်ပါ

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**တပ်ဆင်မှုအတည်ပြုခြင်း**:
```bash
foundry --version
```

#### 2. Python ပတ်ဝန်းကျင်ကို စတင်ပါ

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Foundry Local ကို စတင်ပါ

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Jupyter ကို ဖွင့်ပါ

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### အမြန်အတည်ပြုခြင်း

Python cell တွင် အောက်ပါကို run လုပ်ပါ:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**မျှော်မှန်းရလဒ်**: ဒေသခံမော်ဒယ်မှ အပြန်အလှန်ကြိုဆိုချက်တစ်ခု။

---

## 📝 အလုပ်ရုံဆွေးနွေးပွဲအကောင်းဆုံးအလေ့အကျင့်များ

### ဆရာများအတွက်

**အလုပ်ရုံဆွေးနွေးပွဲမတိုင်မီ**:
- ✅ တပ်ဆင်မှုညွှန်ကြားချက်များကို 1 ပတ်ကြိုပို့ပါ
- ✅ ရည်ရွယ်ထားသော ဟာ့ဒ်ဝဲပေါ်တွင် notebook အားလုံးကို စမ်းသပ်ပါ
- ✅ အမှားများအတွက် ဖြေရှင်းချက်လမ်းညွှန်ကို ပြင်ဆင်ထားပါ
- ✅ မော်ဒယ်အရန်များကို ပြင်ဆင်ထားပါ (phi-4-mini မအောင်မြင်ပါက phi-3.5-mini)
- ✅ မေးခွန်းများအတွက် မျှဝေထားသော chat channel ကို စီစဉ်ပါ

**အလုပ်ရုံဆွေးနွေးပွဲအတွင်း**:
- ✅ ပတ်ဝန်းကျင်အတည်ပြုမှုကို အမြန်စတင်ပါ (5 မိနစ်)
- ✅ အမှားပြင်ဆင်မှုအရင်းအမြစ်များကို ချက်ချင်းမျှဝေပါ
- ✅ စမ်းသပ်မှုနှင့် ပြင်ဆင်မှုကို လှုံ့ဆော်ပါ
- ✅ အစည်းအဝေး 2 ခုပြီးတိုင်း အနားယူရန် စီစဉ်ပါ
- ✅ 1-on-1 အကူအညီအတွက် TA များကို ရှိစေပါ

**အလုပ်ရုံဆွေးနွေးပွဲပြီးနောက်**:
- ✅ အလုပ်လုပ်နေသော notebook များနှင့် ဖြေရှင်းချက်များကို မျှဝေပါ
- ✅ ထပ်ဆောင်းအရင်းအမြစ်များကို link ပေးပါ
- ✅ တိုးတက်မှုအတွက် အကြံပြုချက် survey ဖန်တီးပါ
- ✅ ဆက်လက်မေးခွန်းများအတွက် office hours ပေးပါ

### သင်ယူသူများအတွက်

**သင်ယူမှုကို အများဆုံးအကျိုးရှိစေပါ**:
- ✅ အလုပ်ရုံဆွေးနွေးပွဲမစတင်မီ setup ကို ပြီးစီးပါ
- ✅ code cell တစ်ခုချင်းစီကို run လုပ်ပါ (ဖတ်ရုံမလုပ်ပါနှင့်)
- ✅ parameters နှင့် prompts များကို စမ်းသပ်ပါ
- ✅ အထောက်အထားများနှင့် အရေးကြီးသောအချက်များကို မှတ်စုယူပါ
- ✅ အခက်အခဲရှိပါက မေးပါ (အခြားသူများလည်း တူညီသောမေးခွန်းရှိနိုင်သည်)

**ရှောင်ရှားရန် အများဆုံးဖြစ်နိုင်သောအမှားများ**:
- ❌ cell အစီအစဉ်ကို ကျော်သွားခြင်း (အဆင့်လိုက် run လုပ်ပါ)
- ❌ အမှားစာတန်းများကို သေချာမဖတ်ခြင်း
- ❌ နားမလည်ဘဲ အလျင်အမြန်လုပ်ဆောင်ခြင်း
- ❌ markdown ရှင်းလင်းချက်များကို မဖတ်ခြင်း
- ❌ ပြင်ဆင်ထားသော notebook များကို မသိမ်းဆည်းခြင်း

**အမှားပြင်ဆင်မှုအကြံပြုချက်များ**:
1. **ဝန်ဆောင်မှုမလုပ်ဆောင်ခြင်း**: `foundry service status` ကို စစ်ဆေးပါ
2. **Import အမှားများ**: virtual environment ကို ဖွင့်ထားသည်ကို အတည်ပြုပါ
3. **မော်ဒယ်မတွေ့ရှိခြင်း**: `foundry model ls` ကို run လုပ်ပြီး loaded မော်ဒယ်များကို စစ်ဆေးပါ
4. **အလုပ်ဆောင်မှုနှေးကွေးခြင်း**: RAM အသုံးပြုမှုကို စစ်ဆေးပြီး အခြား app များကို ပိတ်ပါ
5. **မျှော်မှန်းမရလဒ်များ**: kernel ကို ပြန်စပြီး အပေါ်မှ cell အားလုံးကို run လုပ်ပါ

---

## 🔗 ထပ်ဆောင်းအရင်းအမြစ်များ

### အလုပ်ရုံဆွေးနွေးပွဲပစ္စည်းများ

- **[အလုပ်ရုံဆွေးနွေးပွဲအဓိကလမ်းညွှန်](../Readme.md)** - အကျဉ်းချုပ်, သင်ယူရည်ရွယ်ချက်များ, အလုပ်အကိုင်ရလဒ်များ
- **[Python နမူနာများ](../../../../Workshop/samples)** - အစည်းအဝေးတစ်ခုချင်းစီအတွက် Python script များ
- **[အစည်းအဝေးလမ်းညွှန်များ](../../../../Workshop)** - အသေးစိတ် markdown လမ်းညွှန်များ (Session01-06)
- **[Scripts](../../../../Workshop/scripts)** - အတည်ပြုခြင်းနှင့် စမ်းသပ်မှု utility များ
- **[Troubleshooting](./TROUBLESHOOTING.md)** - အများဆုံးဖြစ်နိုင်သောအခက်အခဲများနှင့် ဖြေရှင်းချက်များ
- **[Quick Start](./quickstart.md)** - အမြန်စတင်ရန်လမ်းညွှန်

### Documentation

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Microsoft မှတရားဝင် documentation
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK ကိုးကားချက်
- **[Sentence Transformers](https://www.sbert.net/)** - Embedding မော်ဒယ်များ documentation
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG အကဲဖြတ်မှု metrics

### Community

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - မေးခွန်းမေးရန်၊ project များမျှဝေရန်
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - အချိန်နှင့်တပြေးညီ community အထောက်အပံ့
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - နည်းပညာဆိုင်ရာ Q&A

---

## 🎯 သင်ယူလမ်းကြောင်းအကြံပြုချက်များ

### Beginner Track (ဒီနေရာမှ စတင်ပါ)

1. **Session 01** - Chat Bootstrap
2. **Session 02** - RAG Pipeline
3. **Session 03** - Benchmark Models

**အချိန်**: ~2 နာရီ | **အာရုံစိုက်မှု**: အခြေခံပုံစံများ

---

### Intermediate Track

1. Beginner Track ကို ပြီးစီးပါ
2. **Session 02** - RAG Evaluation
3. **Session 04** - Model Comparison

**အချိန်**: ~4 နာရီ | **အာရုံစိုက်မှု**: အရည်အသွေးနှင့် အဆင့်မြှင့်တင်မှု

---

### Advanced Track (အလုပ်ရုံဆွေးနွေးပွဲအပြည့်အစုံ)

1. Intermediate Track ကို ပြီးစီးပါ
2. **Session 05** - Multi-Agent Orchestrator
3. **Session 06** - Model Router
4. **Session 06** - Multi-Step Pipeline

**အချိန်**: ~6 နာရီ | **အာရုံစိုက်မှု**: ထုတ်လုပ်မှုပုံစံများ

---

### Custom Project Track

1. Beginner Track (Session 01-03) ကို ပြီးစီးပါ
2. သင့်ရည်ရွယ်ချက်အပေါ်မူတည်၍ အဆင့်မြင့် session တစ်ခုကို ရွေးချယ်ပါ:
   - **RAG app တည်ဆောက်ခြင်း?** → Session 02 Evaluation
   - **အလုပ်ဆောင်မှုကို အဆင့်မြှင့်တင်ခြင်း?** → Session 04 Comparison
   - **ရှုပ်ထွေးသော workflow များ?** → Session 05 Orchestrator
   - **အဆင့်မြှင့်တင်နိုင်သော ဖွဲ့စည်းပုံ?** → Session 06 Router + Pipeline

**အချိန်**: ~3 နာရီ | **အာရုံစိုက်မှု**: Project-specific ကျွမ်းကျင်မှုများ

---

## 📊 အောင်မြင်မှုအတိုင်းအတာများ

သင့်တိုးတက်မှုကို milestone များဖြင့် စစ်ဆေးပါ:

- [ ] **Setup ပြီးစီး** - Foundry Local ကို run လုပ်ပြီး၊ အားလုံး dependency များကို တပ်ဆင်ပြီး
- [ ] **ပထမဆုံး Chat** - Session 01 ကို ပြီးစီးပြီး၊ streaming chat အလုပ်လုပ်နေ
- [ ] **RAG တည်ဆောက်ပြီး** - Session 02 ကို ပြီးစီးပြီး၊ document QA စနစ်အလုပ်လုပ်နေ
- [ ] **မော်ဒယ်များကို Benchmark ပြုလုပ်ပြီး** - Session 03 ကို ပြီးစီးပြီး၊ performance data ရရှိ
- [ ] **Trade-offs ကို ခွဲခြားပြီး** - Session 04 ကို ပြီးစီးပြီး၊ မော်ဒယ်ရွေးချယ်မှု criteria ရရှိ
- [ ] **Agents ကို Orchestrate ပြုလုပ်ပြီး** - Session 05 ကို ပြီးစီးပြီး၊ multi-agent စနစ်အလုပ်လုပ်နေ
- [ ] **Routing ကို Implement ပြုလုပ်ပြီး** - Session 06 ကို ပြီးစီးပြီး၊ ဉာဏ်ရည်မော်ဒယ်ရွေးချယ်မှုအလုပ်လုပ်နေ
- [ ] **Custom Project** - Workshop ပုံစံများကို သင့်ရည်ရွယ်ချက်အပေါ် အကျိုးသက်ရောက်စွာ အသုံးပြု

---

## 🤝 အထောက်အကူပြုခြင်း

အခက်အခဲတစ်ခုကို တွေ့ရှိပါသို့မဟုတ် အကြံပြုချက်ရှိပါသလား? ကျွန်ုပ်တို့သည် အထောက်အကူပြုမှုများကို ကြိုဆိုပါသည်!

- **အခက်အခဲများကို Report ပြုလုပ်ပါ**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **တိုးတက်မှုများကို အကြံပြုပါ**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **PR များကို တင်ပါ**: [Contributing Guidelines](../../AGENTS.md) ကို လိုက်နာပါ

---

## 📄 လိုင်စင်

ဤအလုပ်ရုံဆွေးနွေးပွဲသည် [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) repository ၏ အစိတ်အပိုင်းတစ်ခုဖြစ်ပြီး [MIT License](../../../../LICENSE) အောက်တွင် လိုင်စင်ရရှိထားသည်။

---

**ထုတ်လုပ်မှုအဆင့် Edge AI အက်ပလီကေးရှင်းများကို တည်ဆောက်ရန် အသင့်ဖြစ်ပါသလား?**  
**[Session 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) → မှ စတင်ပါ**

---

*နောက်ဆုံးအပ်ဒိတ်: 2025 ခုနှစ် အောက်တိုဘာ 8 | Workshop Version: 2.0*

---

**ဝန်ခံချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူလဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။