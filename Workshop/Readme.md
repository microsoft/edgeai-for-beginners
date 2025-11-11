# EdgeAI for Beginners - Workshop

> **Hands-On Learning Path for Building Production-Ready Edge AI Applications**
>
> Master local AI deployment with Microsoft Foundry Local, from first chat completion to multi-agent orchestration in 6 progressive sessions.

---

## 🎯 Introduction

Welcome to the **EdgeAI for Beginners Workshop** - your practical, hands-on guide to building intelligent applications that run entirely on local hardware. This workshop transforms theoretical Edge AI concepts into real-world skills through progressively challenging exercises using Microsoft Foundry Local and Small Language Models (SLMs).

### Why This Workshop?

**The Edge AI Revolution is Here**

Organizations worldwide are shifting from cloud-dependent AI to edge computing for three critical reasons:

1. **Privacy & Compliance** - Process sensitive data locally without cloud transmission (HIPAA, GDPR, financial regulations)
2. **Performance** - Eliminate network latency (50-500ms local vs 500-2000ms cloud round-trip)
3. **Cost Control** - Remove per-token API costs and scale without cloud expenses

**But Edge AI is Different**

Running AI on-premises requires new skills:
- Model selection and optimization for resource constraints
- Local service management and hardware acceleration
- Prompt engineering for smaller models
- Production deployment patterns for edge devices

**This Workshop Delivers Those Skills**

In 6 focused sessions (~3 hours total), you'll progress from "Hello World" to deploying production-ready multi-agent systems - all running locally on your machine.

---

## 📚 Learning Objectives

By completing this workshop, you will be able to:

### Core Competencies
1. **Deploy and Manage Local AI Services**
   - Install and configure Microsoft Foundry Local
   - Select appropriate models for edge deployment
   - Manage model lifecycle (download, load, cache)
   - Monitor resource usage and optimize performance

2. **Build AI-Powered Applications**
   - Implement OpenAI-compatible chat completions locally
   - Design effective prompts for Small Language Models
   - Handle streaming responses for better UX
   - Integrate local models into existing applications

3. **Create RAG (Retrieval Augmented Generation) Systems**
   - Build semantic search with embeddings
   - Ground LLM responses in domain-specific knowledge
   - Evaluate RAG quality with industry-standard metrics
   - Scale from prototype to production

4. **Optimize Model Performance**
   - Benchmark multiple models for your use case
   - Measure latency, throughput, and first-token time
   - Select optimal models based on speed/quality tradeoffs
   - Compare SLM vs LLM trade-offs in real scenarios

5. **Orchestrate Multi-Agent Systems**
   - Design specialized agents for different tasks
   - Implement agent memory and context management
   - Coordinate agents in complex workflows
   - Route requests intelligently across multiple models

6. **Deploy Production-Ready Solutions**
   - Implement error handling and retry logic
   - Monitor token usage and system resources
   - Build scalable architectures with model-as-tools patterns
   - Plan migration paths from edge to hybrid (edge + cloud)

---

## 🎓 Learning Outcomes

### What You'll Build

By the end of this workshop, you will have created:

| Session | Deliverable | Skills Demonstrated |
|---------|-------------|---------------------|
| **1** | Chat application with streaming | Service setup, basic completions, streaming UX |
| **2** | RAG system with evaluation | Embeddings, semantic search, quality metrics |
| **3** | Multi-model benchmark suite | Performance measurement, model comparison |
| **4** | SLM vs LLM comparator | Trade-off analysis, optimization strategies |
| **5** | Multi-agent orchestrator | Agent design, memory management, coordination |
| **6** | Intelligent routing system | Intent detection, model selection, scalability |

### Competency Matrix

| Skill Level | Session 1-2 | Session 3-4 | Session 5-6 |
|-------------|-------------|-------------|-------------|
| **Beginner** | ✅ Setup & basics | ⚠️ Challenging | ❌ Too advanced |
| **Intermediate** | ✅ Quick review | ✅ Core learning | ⚠️ Stretch goals |
| **Advanced** | ✅ Breeze through | ✅ Refinement | ✅ Production patterns |

### Career-Ready Skills

**After this workshop, you'll be prepared to:**

✅ **Build Privacy-First Applications**
- Healthcare apps handling PHI/PII locally
- Financial services with compliance requirements
- Government systems with data sovereignty needs

✅ **Optimize for Edge Environments**
- IoT devices with limited resources
- Offline-first mobile applications
- Low-latency real-time systems

✅ **Design Intelligent Architectures**
- Multi-agent systems for complex workflows
- Hybrid edge-cloud deployments
- Cost-optimized AI infrastructure

✅ **Lead Edge AI Initiatives**
- Evaluate Edge AI feasibility for projects
- Select appropriate models and frameworks
- Architect scalable local AI solutions

---

## 🗺️ Workshop Structure

### Session Overview (6 Sessions × 30 Minutes = 3 Hours)

| Session | Topic | Focus | Duration |
|---------|-------|-------|----------|
| **1** | Getting Started with Foundry Local | Install, validate, first completions | 30 min |
| **2** | Building AI Solutions with RAG | Prompt engineering, embeddings, evaluation | 30 min |
| **3** | Open Source Models | Model discovery, benchmarking, selection | 30 min |
| **4** | Cutting Edge Models | SLM vs LLM, optimization, frameworks | 30 min |
| **5** | AI-Powered Agents | Agent design, orchestration, memory | 30 min |
| **6** | Models as Tools | Routing, chaining, scaling strategies | 30 min |

---

## 🚀 Quick Start

### Prerequisites

**System Requirements:**
- **OS**: Windows 10/11, macOS 11+, or Linux (Ubuntu 20.04+)
- **RAM**: 8GB minimum, 16GB+ recommended
- **Storage**: 10GB+ free space for models
- **CPU**: Modern processor with AVX2 support
- **GPU** (optional): CUDA-compatible or Qualcomm NPU for acceleration

**Software Requirements:**
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Installation Guide](#install-foundry-local))
- **Git** ([Download](https://git-scm.com/downloads))
- **Visual Studio Code** (recommended) ([Download](https://code.visualstudio.com/))

### Setup in 3 Steps

#### 1. Install Foundry Local

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

**Ensure Azure AI Foundry Local is running with a fixed port**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verify it's working:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Finding Available Models**
To see which models are available in your Foundry Local instance, you can query the models endpoint:

```bash
# cmd/bash/powershell
foundry model list
```

Using Web Endpoint 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Clone Repository & Install Dependencies

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

#### 3. Run Your First Sample

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Success!** You should see a streaming response about edge AI.

---

## 📦 Workshop Resources

### Python Samples

Progressive hands-on examples demonstrating each concept:

| Session | Sample | Description | Run Time |
|---------|--------|-------------|----------|
| 1 | [`chat_bootstrap.py`](./samples/session01/chat_bootstrap.py) | Basic & streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](./samples/session02/rag_pipeline.py) | RAG with embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](./samples/session02/rag_eval_ragas.py) | RAG quality evaluation | ~60s |
| 3 | [`benchmark_oss_models.py`](./samples/session03/benchmark_oss_models.py) | Multi-model benchmarking | ~2-3m |
| 4 | [`model_compare.py`](./samples/session04/model_compare.py) | SLM vs LLM comparison | ~45s |
| 5 | [`agents_orchestrator.py`](./samples/session05/agents_orchestrator.py) | Multi-agent system | ~60s |
| 6 | [`models_router.py`](./samples/session06/models_router.py) | Intent-based routing | ~45s |
| 6 | [`models_pipeline.py`](./samples/session06/models_pipeline.py) | Multi-step pipeline | ~60s |

### Jupyter Notebooks

Interactive exploration with explanations and visualizations:

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

Comprehensive guides and references:

| Document | Description | Use When |
|----------|-------------|----------|
| [QUICK_START.md](./QUICK_START.md) | Fast-track setup guide | Starting from scratch |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Command & API cheat sheet | Need quick answers |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK patterns & examples | Writing code |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Environment variable guide | Configuring samples |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Common issues & fixes | Debugging problems |

---

## 🎓 Learning Path Recommendations

### For Beginners (3-4 hours)
1. ✅ Session 1: Getting Started (focus on setup and basic chat)
2. ✅ Session 2: RAG Basics (skip evaluation initially)
3. ✅ Session 3: Simple Benchmarking (2 models only)
4. ⏭️ Skip Sessions 4-6 for now
5. 🔄 Return to Sessions 4-6 after building first application

### For Intermediate Developers (3 hours)
1. ⚡ Session 1: Quick setup validation
2. ✅ Session 2: Complete RAG pipeline with evaluation
3. ✅ Session 3: Full benchmarking suite
4. ✅ Session 4: Model optimization
5. ✅ Sessions 5-6: Focus on architecture patterns

### For Advanced Practitioners (2-3 hours)
1. ⚡ Sessions 1-3: Quick review and validation
2. ✅ Session 4: Optimization deep-dive
3. ✅ Session 5: Multi-agent architecture
4. ✅ Session 6: Production patterns and scaling
5. 🚀 Extend: Build custom routing logic and hybrid deployments

---

## Workshop Session Pack (Focused 30‑Minute Labs)

If you're following the condensed 6-session workshop format, use these dedicated guides (each maps to and complements the broader module docs above):

| Workshop Session | Guide | Core Focus |
|------------------|-------|------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Install, validate, run phi & GPT-OSS-20B, acceleration |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt engineering, RAG patterns, CSV & document grounding, migration |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face integration, benchmarking, model selection |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX acceleration |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Agent roles, memory, tools, orchestration |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, chaining, scaling path to Azure |

Each session file includes: abstract, learning objectives, 30‑minute demo flow, starter project, validation checklist, troubleshooting, and references to the official Foundry Local Python SDK.

### Sample Scripts

Install workshop dependencies (Windows):

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

If running the Foundry Local service on a different (Windows) machine or VM from macOS, export the endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Session | Script(s) | Description |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap service & streaming chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimal RAG (in-memory embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | RAG evaluation with ragas metrics |
| 3 | `samples/session03/benchmark_oss_models.py` | Multi-model latency & throughput benchmarking |
| 4 | `samples/session04/model_compare.py` | SLM vs LLM comparison (latency & sample output) |
| 5 | `samples/session05/agents_orchestrator.py` | Two‑agent research → editorial pipeline |
| 6 | `samples/session06/models_router.py` | Intent-based routing demo |
|   | `samples/session06/models_pipeline.py` | Multi-step plan/execute/refine chain |

### Environment Variables (Common Across Samples)

| Variable | Purpose | Example |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Default single model alias for basic samples | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Explicit SLM vs larger model for comparison | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Comma list of aliases to benchmark | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Benchmark repetitions per model | `3` |
| `BENCH_PROMPT` | Prompt used in benchmarking | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Override test query for RAG pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Override agents pipeline query | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Model alias for research agent | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Model alias for editor agent (can differ) | `gpt-oss-20b` |
| `SHOW_USAGE` | When `1`, prints token usage per completion | `1` |
| `RETRY_ON_FAIL` | When `1`, retry once on transient chat errors | `1` |
| `RETRY_BACKOFF` | Seconds to wait before retry | `1.0` |

If a variable isn’t set, scripts fall back to sensible defaults. For single‑model demos you typically only need `FOUNDRY_LOCAL_ALIAS`.

### Utility Module

All samples now share a helper `samples/workshop_utils.py` providing:

* Cached `FoundryLocalManager` + OpenAI client creation
* `chat_once()` helper with optional retry + usage printing
* Simple token usage reporting (enable via `SHOW_USAGE=1`)

This reduces duplication and highlights best practices for efficient local model orchestration.

## Optional Enhancements (Cross-Session)

| Theme | Enhancement | Sessions | Env / Toggle |
|-------|-------------|----------|--------------|
| Determinism | Fixed temperature + stable prompt sets | 1–6 | Set `temperature=0`, `top_p=1` |
| Token Usage Visibility | Consistent cost/efficiency teaching | 1–6 | `SHOW_USAGE=1` |
| Streaming First Token | Perceived latency metric | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Retry Resilience | Handles transient cold-start | All | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-Model Agents | Heterogeneous role specialization | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptive Routing | Intent + cost heuristics | 6 | Extend router with escalation logic |
| Vector Memory | Long-term semantic recall | 2,5,6 | Integrate FAISS/Chroma embedding index |
| Trace Export | Auditing & evaluation | 2,5,6 | Append JSON lines per step |
| Quality Rubrics | Qualitative tracking | 3–6 | Secondary scoring prompts |
| Smoke Tests | Quick pre-workshop validation | All | `python Workshop/tests/smoke.py` |

### Deterministic Quick Start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Expect stable token counts across repeated identical inputs.

### RAG Evaluation (Session 2)

Use `rag_eval_ragas.py` to compute answer relevancy, faithfulness, and context precision on a tiny synthetic dataset:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Extend by supplying a larger JSONL of questions, contexts, and ground truths, then converting to a Hugging Face `Dataset`.

## CLI Command Accuracy Appendix

The workshop deliberately uses only currently documented / stable Foundry Local CLI commands.

### Stable Commands Referenced

| Category | Command | Purpose |
|----------|---------|---------|
| Core | `foundry --version` | Show installed version |
| Service | `foundry service start` | Start local service (if not auto) |
| Service | `foundry service status` | Show service status |
| Models | `foundry model list` | List catalog / available models |
| Models | `foundry model download <alias>` | Download model weights into cache |
| Models | `foundry model run <alias>` | Launch (load) a model locally; combine with `--prompt` for one‑shot |
| Models | `foundry model unload <alias>` / `foundry model stop <alias>` | Unload a model from memory (if supported) |
| Cache | `foundry cache list` | List cached (downloaded) models |

### One‑Shot Prompt Pattern

Instead of a deprecated `model chat` subcommand, use:

```powershell
foundry model run <alias> --prompt "Your question here"
```

This executes a single prompt/response cycle then exits.

### Removed / Avoided Patterns

| Deprecated / Undocumented | Replacement / Guidance |
|---------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Use plain `foundry model list` + recent activity / logs |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Use benchmark Python script + OS tools (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetry

- Latency, p95, tokens/sec: `samples/session03/benchmark_oss_models.py`
- First‑token latency (streaming): set `BENCH_STREAM=1`
- Resource usage: OS monitors (Task Manager, Activity Monitor, `nvidia-smi`).

As new CLI telemetry commands stabilize upstream, they can be incorporated with minimal edits to session markdowns.

### Automated Lint Guard

An automated linter prevents reintroduction of deprecated CLI patterns inside fenced code blocks of markdown files:

Script: `Workshop/scripts/lint_markdown_cli.py`

Deprecated patterns are blocked inside code fences.

Recommended replacements:
| Deprecated | Replacement |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark script + system tools |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Run locally:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` runs on every push & PR.

Optional pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Quick CLI → SDK Migration Table

| Task | CLI One-Liner | SDK (Python) Equivalent | Notes |
|------|---------------|-------------------------|-------|
| Run a model once (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK bootstraps service & caching automatically |
| Download (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager picks best variant if alias maps to multiple builds |
| List catalog | `foundry model list` | `# use manager for each alias or maintain known list` | CLI aggregates; SDK currently per-alias instantiation |
| List cached models | `foundry cache list` | `manager.list_cached_models()` | After manager init (any alias) |
| Get endpoint URL | (implicit) | `manager.endpoint` | Used to create OpenAI-compatible client |
| Warm a model | `foundry model run <alias>` then first prompt | `chat_once(alias, messages=[...])` (utility) | Utilities handle initial cold latency warmup |
| Measure latency | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (or new exporter script) | Prefer script for consistent metrics |
| Stop / unload model | `foundry model unload <alias>` | (Not exposed – restart service / process) | Typically not required for workshop flow |
| Retrieve token usage | (view output) | `resp.usage.total_tokens` | Provided if backend returns usage object |

## Benchmark Markdown Export

Use the script `Workshop/scripts/export_benchmark_markdown.py` to run a fresh benchmark (same logic as `samples/session03/benchmark_oss_models.py`) and emit a GitHub-friendly Markdown table plus raw JSON.

### Example

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generated files:
| File | Contents |
|------|----------|
| `benchmark_report.md` | Markdown table + interpretation hints |
| `benchmark_report.json` | Raw metrics array (for diffing / trend tracking) |

Set `BENCH_STREAM=1` in the environment to include first-token latency if supported.
