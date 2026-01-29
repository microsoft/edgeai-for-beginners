# Workshop Notebooks

> **Interactive Jupyter Notebooks for Hands-On Edge AI Learning**
>
> Progressive, self-paced tutorials that range from basic chat completions to advanced multi-agent systems using Microsoft Foundry Local and Small Language Models.

---

## 📖 Introduction

Welcome to the **EdgeAI for Beginners Workshop Notebooks** collection. These interactive Jupyter notebooks offer a hands-on learning experience where you can write, execute, and experiment with Edge AI code in real-time.

### Why Jupyter Notebooks?

Unlike traditional tutorials, these notebooks provide:

- **Interactive Learning**: Run code cells and see immediate results
- **Experimentation**: Modify parameters and observe changes in real-time
- **Documentation**: Inline explanations and markdown cells to guide you through concepts
- **Reproducibility**: Complete working examples you can reference and reuse
- **Visualization**: View performance metrics, embeddings, and results inline

### What Makes These Notebooks Special?

Each notebook is designed with **production-ready best practices** in mind:

✅ **Comprehensive Error Handling** - Graceful degradation and informative error messages  
✅ **Type Hints & Documentation** - Clear function signatures and docstrings  
✅ **Performance Monitoring** - Token usage tracking and latency measurements  
✅ **Modular Design** - Reusable patterns you can adapt to your projects  
✅ **Progressive Complexity** - Builds on previous sessions systematically  

---

## 🎯 Learning Objectives

### Core Skills You'll Develop

By working through these notebooks, you will master:

1. **Local AI Service Management**
   - Configure and manage Microsoft Foundry Local services
   - Select and load appropriate models for your hardware
   - Monitor resource usage and optimize performance
   - Handle service discovery and health checking

2. **AI Application Development**
   - Implement OpenAI-compatible chat completions locally
   - Build streaming interfaces for better user experience
   - Design effective prompts for Small Language Models
   - Integrate local models into applications

3. **Retrieval Augmented Generation (RAG)**
   - Create semantic search with vector embeddings
   - Ground LLM responses in domain-specific documents
   - Evaluate RAG quality with RAGAS metrics
   - Scale from prototype to production

4. **Performance Optimization**
   - Benchmark multiple models systematically
   - Measure latency, throughput, and first-token time
   - Compare Small Language Models vs Large Language Models
   - Select optimal models based on performance/quality trade-offs

5. **Multi-Agent Orchestration**
   - Design specialized agents for different tasks
   - Implement agent memory and context management
   - Coordinate multiple agents in complex workflows
   - Build coordinator patterns for agent collaboration

6. **Intelligent Model Routing**
   - Implement intent detection and pattern matching
   - Route queries to appropriate models automatically
   - Build multi-step pipelines (plan → execute → refine)
   - Design scalable model-as-tools architectures

---

## 🎓 Learning Outcomes

### What You'll Build

| Notebook | Deliverable | Skills Demonstrated | Difficulty |
|----------|-------------|---------------------|------------|
| **Session 01** | Chat app with streaming | Service setup, basic completions, streaming UX | ⭐ Beginner |
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

**Perfect for: Team training sessions, hackathons, conference workshops**

| Time | Duration | Session | Topics | Activities |
|------|----------|---------|--------|------------|
| **0:00** | 30 min | Setup & Intro | Environment setup, Foundry Local installation | Install dependencies, verify setup |
| **0:30** | 30 min | Session 01 | Basic chat completions, streaming | Run notebook, modify prompts |
| **1:00** | 45 min | Session 02 | RAG pipeline, embeddings, evaluation | Build RAG system, test queries |
| **1:45** | 15 min | Break | ☕ Coffee & questions | — |
| **2:00** | 30 min | Session 03 | Multi-model benchmarking | Compare 3+ models |
| **2:30** | 30 min | Session 04 | SLM vs LLM trade-offs | Analyze performance/quality |
| **3:00** | 30 min | Session 05-06 | Multi-agent systems & routing | Explore advanced patterns |

**Output**: Attendees leave with 6 working Edge AI applications and production-ready code patterns.

---

### 🎓 Full-Day Workshop (6 hours)

**Perfect for: In-depth training, bootcamps, university courses**

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

**Output**: Deep understanding of Edge AI patterns plus 2 custom projects.

---

### 📚 Self-Paced Learning (2 weeks)

**Perfect for: Individual learners, online courses, self-study**

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

**Output**: Mastery of Edge AI patterns plus portfolio project.

---

## 📔 Notebook Descriptions

### 📘 Session 01: Chat Bootstrap
**File**: `session01_chat_bootstrap.ipynb`  
**Duration**: 20-30 minutes  
**Prerequisites**: None  
**Difficulty**: ⭐ Beginner

**What You'll Learn**:
- Install and configure Foundry Local Python SDK
- Use `FoundryLocalManager` for automatic service discovery
- Implement basic chat completions with OpenAI-compatible API
- Build streaming responses for better user experience
- Handle errors and service unavailability gracefully

**Key Concepts**: Service management, chat completions, streaming, error handling

**You'll Build**: Interactive chat application with streaming support

---

### 📗 Session 02: RAG Pipeline
**File**: `session02_rag_pipeline.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Session 01  
**Difficulty**: ⭐⭐ Intermediate

**What You'll Learn**:
- Implement Retrieval Augmented Generation (RAG) pattern
- Create vector embeddings with sentence-transformers
- Build semantic search with cosine similarity
- Ground LLM responses in domain documents
- Handle optional dependencies with import guards

**Key Concepts**: RAG architecture, embeddings, semantic search, vector similarity

**You'll Build**: Document-grounded question-answering system

---

### 📗 Session 02: RAG Evaluation with RAGAS
**File**: `session02_rag_eval_ragas.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Session 02 RAG Pipeline  
**Difficulty**: ⭐⭐ Intermediate

**What You'll Learn**:
- Evaluate RAG quality with industry-standard metrics
- Measure context relevance, answer relevance, faithfulness
- Use RAGAS framework for systematic evaluation
- Identify and fix RAG quality issues
- Build evaluation datasets for your domain

**Key Concepts**: RAG evaluation, RAGAS metrics, quality measurement, systematic testing

**You'll Build**: RAG quality evaluation framework

---

### 📙 Session 03: Benchmark OSS Models
**File**: `session03_benchmark_oss_models.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Session 01  
**Difficulty**: ⭐⭐ Intermediate

**What You'll Learn**:
- Systematically benchmark multiple models
- Measure latency, throughput, first-token time
- Implement graceful degradation for model failures
- Compare performance across model families
- Visualize and analyze benchmark results

**Key Concepts**: Performance benchmarking, latency measurement, model comparison, statistical analysis

**You'll Build**: Multi-model benchmarking suite

---

### 📙 Session 04: Model Comparison (SLM vs LLM)
**File**: `session04_model_compare.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Sessions 01, 03  
**Difficulty**: ⭐⭐⭐ Advanced

**What You'll Learn**:
- Compare Small Language Models vs Large Language Models
- Analyze performance vs quality trade-offs
- Measure edge-suitability metrics
- Select optimal models for deployment constraints
- Document decision criteria for model selection

**Key Concepts**: Model selection, trade-off analysis, optimization strategies, deployment planning

**You'll Build**: SLM vs LLM comparison framework

---

### 📕 Session 05: Multi-Agent Orchestrator
**File**: `session05_agents_orchestrator.ipynb`  
**Duration**: 45-60 minutes  
**Prerequisites**: Sessions 01-02  
**Difficulty**: ⭐⭐⭐ Advanced

**What You'll Learn**:
- Design specialized agents for different tasks
- Implement agent memory and context management
- Build coordinator patterns for agent collaboration
- Handle agent communication and handoffs
- Monitor multi-agent system performance

**Key Concepts**: Agent architecture, coordinator patterns, memory management, agent orchestration

**You'll Build**: Multi-agent system with coordinator and specialists

---

### 📕 Session 06: Model Router
**File**: `session06_models_router.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Sessions 01, 03  
**Difficulty**: ⭐⭐⭐ Advanced

**What You'll Learn**:
- Implement intent detection and pattern matching
- Build keyword-based model routing
- Route queries to appropriate models automatically
- Configure multi-model registries
- Monitor routing decisions and performance

**Key Concepts**: Intent detection, model routing, pattern matching, intelligent selection

**You'll Build**: Intelligent model routing system

---

### 📕 Session 06: Multi-Step Pipeline
**File**: `session06_models_pipeline.ipynb`  
**Duration**: 30-45 minutes  
**Prerequisites**: Sessions 01, 06 Router  
**Difficulty**: ⭐⭐⭐ Advanced

**What You'll Learn**:
- Build multi-step AI pipelines (plan → execute → refine)
- Integrate router for intelligent model selection
- Implement pipeline error handling and recovery
- Monitor pipeline performance and stages
- Design scalable model-as-tools architectures

**Key Concepts**: Pipeline architecture, multi-stage processing, error recovery, scalability patterns

**You'll Build**: Multi-step intelligent pipeline with routing

---

## 🚀 Getting Started

### Prerequisites

**System Requirements**:
- **OS**: Windows 10/11, macOS 11+, or Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, recommended 16GB+
- **Storage**: At least 10GB free space for models
- **Hardware**: CPU with AVX2; GPU (CUDA, Qualcomm NPU) optional

**Software Requirements**:
- **Python 3.8+** with pip
- **Jupyter Notebook** or **VS Code** with Jupyter extension
- **Microsoft Foundry Local** installed and configured
- **Git** (for cloning the repository)

### Installation Steps

#### 1. Install Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verify Installation**:
```bash
foundry --version
```

#### 2. Set Up Python Environment

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

#### 3. Start Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Launch Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Quick Verification

Run this in a Python cell to verify setup:

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

**Expected Output**: A greeting response from the local model.

---

## 📝 Workshop Best Practices

### For Instructors

**Before the Workshop**:
- ✅ Send installation instructions one week in advance
- ✅ Test all notebooks on the target hardware
- ✅ Prepare a troubleshooting guide for common issues
- ✅ Have backup models ready (phi-3.5-mini if phi-4-mini fails)
- ✅ Set up a shared chat channel for questions

**During the Workshop**:
- ✅ Start with a quick environment check (5 minutes)
- ✅ Share troubleshooting resources immediately
- ✅ Encourage experimentation and modifications
- ✅ Use breaks strategically (after every two sessions)
- ✅ Have TAs available for one-on-one help

**After the Workshop**:
- ✅ Share complete working notebooks and solutions
- ✅ Provide links to additional resources
- ✅ Create a feedback survey for improvement
- ✅ Offer office hours for follow-up questions

### For Learners

**Maximize Your Learning**:
- ✅ Complete setup before the workshop starts
- ✅ Run every code cell yourself (don’t just read)
- ✅ Experiment with parameters and prompts
- ✅ Take notes on insights and challenges
- ✅ Ask questions when stuck (others likely have the same question)

**Common Pitfalls to Avoid**:
- ❌ Skipping cell execution order (run sequentially)
- ❌ Not reading error messages carefully
- ❌ Rushing through without understanding
- ❌ Ignoring markdown explanations
- ❌ Not saving your modified notebooks

**Debugging Tips**:
1. **Service Not Running**: Check `foundry service status`
2. **Import Errors**: Verify the virtual environment is activated
3. **Model Not Found**: Run `foundry model ls` to list loaded models
4. **Slow Performance**: Check RAM usage, close other applications
5. **Unexpected Results**: Restart the kernel and run all cells from the top

---

## 🔗 Additional Resources

### Workshop Materials

- **[Workshop Main Guide](../Readme.md)** - Overview, learning objectives, career outcomes
- **[Python Samples](../../../../Workshop/samples)** - Corresponding Python scripts for each session
- **[Session Guides](../../../../Workshop)** - Detailed markdown guides (Session01-06)
- **[Scripts](../../../../Workshop/scripts)** - Validation and testing utilities
- **[Troubleshooting](./TROUBLESHOOTING.md)** - Common issues and solutions
- **[Quick Start](./quickstart.md)** - Fast-track getting started guide

### Documentation

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Official Microsoft documentation
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK reference
- **[Sentence Transformers](https://www.sbert.net/)** - Embedding models documentation
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG evaluation metrics

### Community

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Ask questions, share projects
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Real-time community support
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Technical Q&A

---

## 🎯 Learning Path Recommendations

### Beginner Track (Start Here)

1. **Session 01** - Chat Bootstrap
2. **Session 02** - RAG Pipeline
3. **Session 03** - Benchmark Models

**Time**: ~2 hours | **Focus**: Foundational patterns

---

### Intermediate Track

1. Complete Beginner Track
2. **Session 02** - RAG Evaluation
3. **Session 04** - Model Comparison

**Time**: ~4 hours | **Focus**: Quality and optimization

---

### Advanced Track (Full Workshop)

1. Complete Intermediate Track
2. **Session 05** - Multi-Agent Orchestrator
3. **Session 06** - Model Router
4. **Session 06** - Multi-Step Pipeline

**Time**: ~6 hours | **Focus**: Production patterns

---

### Custom Project Track

1. Complete Beginner Track (Sessions 01-03)
2. Choose ONE advanced session based on your goal:
   - **Building RAG app?** → Session 02 Evaluation
   - **Optimizing performance?** → Session 04 Comparison
   - **Complex workflows?** → Session 05 Orchestrator
   - **Scalable architecture?** → Session 06 Router + Pipeline

**Time**: ~3 hours | **Focus**: Project-specific skills

---

## 📊 Success Metrics

Track your progress with these milestones:

- [ ] **Setup Complete** - Foundry Local running, all dependencies installed
- [ ] **First Chat** - Session 01 completed, streaming chat working
- [ ] **RAG Built** - Session 02 completed, document QA system functional
- [ ] **Models Benchmarked** - Session 03 completed, performance data collected
- [ ] **Trade-offs Analyzed** - Session 04 completed, model selection criteria documented
- [ ] **Agents Orchestrated** - Session 05 completed, multi-agent system working
- [ ] **Routing Implemented** - Session 06 completed, intelligent model selection functional
- [ ] **Custom Project** - Applied workshop patterns to your own use case

---

## 🤝 Contributing

Found an issue or have a suggestion? We welcome contributions!

- **Report Issues**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Suggest Improvements**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Submit PRs**: Follow [Contributing Guidelines](../../AGENTS.md)

---

## 📄 License

This workshop is part of the [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) repository and is licensed under the [MIT License](../../../../LICENSE).

---

**Ready to build production-ready Edge AI applications?**  
**Start with [Session 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Last Updated: October 8, 2025 | Workshop Version: 2.0*

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.