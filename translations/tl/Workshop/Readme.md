<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T22:46:18+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "tl"
}
-->
# EdgeAI para sa mga Baguhan - Workshop

> **Praktikal na Landas ng Pag-aaral para sa Paggawa ng Production-Ready na Edge AI Applications**
>
> Masterin ang lokal na AI deployment gamit ang Microsoft Foundry Local, mula sa unang chat completion hanggang sa multi-agent orchestration sa 6 na progresibong sesyon.

---

## 🎯 Panimula

Maligayang pagdating sa **EdgeAI para sa mga Baguhan Workshop** - ang iyong praktikal na gabay sa paggawa ng mga intelligent na aplikasyon na tumatakbo nang buo sa lokal na hardware. Ang workshop na ito ay nagbabago ng mga teoretikal na konsepto ng Edge AI sa mga kasanayan sa totoong mundo sa pamamagitan ng mga progresibong hamon gamit ang Microsoft Foundry Local at Small Language Models (SLMs).

### Bakit Itong Workshop?

**Narito na ang Edge AI Revolution**

Ang mga organisasyon sa buong mundo ay lumilipat mula sa cloud-dependent AI patungo sa edge computing para sa tatlong mahahalagang dahilan:

1. **Privacy at Pagsunod** - Iproseso ang sensitibong data nang lokal nang hindi ipinapadala sa cloud (HIPAA, GDPR, mga regulasyon sa pananalapi)
2. **Pagganap** - Tanggalin ang network latency (50-500ms lokal kumpara sa 500-2000ms cloud round-trip)
3. **Kontrol sa Gastos** - Alisin ang per-token API costs at mag-scale nang walang gastos sa cloud

**Ngunit Iba ang Edge AI**

Ang pagpapatakbo ng AI on-premises ay nangangailangan ng mga bagong kasanayan:
- Pagpili at pag-optimize ng modelo para sa mga limitasyon ng resources
- Pamamahala ng lokal na serbisyo at hardware acceleration
- Prompt engineering para sa mas maliliit na modelo
- Mga pattern ng deployment para sa mga edge device

**Ibinibigay ng Workshop na Ito ang Mga Kasanayang Iyon**

Sa 6 na nakatuong sesyon (~3 oras kabuuan), magpapatuloy ka mula sa "Hello World" hanggang sa pag-deploy ng production-ready multi-agent systems - lahat ay tumatakbo nang lokal sa iyong makina.

---

## 📚 Mga Layunin sa Pag-aaral

Sa pagtatapos ng workshop na ito, magagawa mo ang:

### Pangunahing Kasanayan
1. **Mag-deploy at Mag-manage ng Lokal na AI Services**
   - I-install at i-configure ang Microsoft Foundry Local
   - Pumili ng angkop na mga modelo para sa edge deployment
   - Pamahalaan ang lifecycle ng modelo (download, load, cache)
   - Subaybayan ang paggamit ng resources at i-optimize ang performance

2. **Gumawa ng AI-Powered Applications**
   - Mag-implement ng OpenAI-compatible chat completions nang lokal
   - Magdisenyo ng epektibong prompts para sa Small Language Models
   - Mag-handle ng streaming responses para sa mas magandang UX
   - Isama ang mga lokal na modelo sa mga umiiral na aplikasyon

3. **Gumawa ng RAG (Retrieval Augmented Generation) Systems**
   - Gumawa ng semantic search gamit ang embeddings
   - I-ground ang LLM responses sa domain-specific na kaalaman
   - Suriin ang kalidad ng RAG gamit ang industry-standard metrics
   - Mag-scale mula prototype hanggang production

4. **I-optimize ang Performance ng Modelo**
   - Mag-benchmark ng maraming modelo para sa iyong use case
   - Sukatin ang latency, throughput, at first-token time
   - Pumili ng optimal na mga modelo batay sa speed/quality tradeoffs
   - Ikumpara ang SLM vs LLM trade-offs sa totoong mga senaryo

5. **Mag-orchestrate ng Multi-Agent Systems**
   - Magdisenyo ng specialized agents para sa iba't ibang gawain
   - Mag-implement ng agent memory at context management
   - Mag-coordinate ng mga agents sa complex workflows
   - Mag-route ng mga request nang matalino sa iba't ibang modelo

6. **Mag-deploy ng Production-Ready Solutions**
   - Mag-implement ng error handling at retry logic
   - Subaybayan ang token usage at system resources
   - Gumawa ng scalable architectures gamit ang model-as-tools patterns
   - Magplano ng migration paths mula edge patungo sa hybrid (edge + cloud)

---

## 🎓 Mga Resulta ng Pag-aaral

### Ano ang Iyong Mabubuo

Sa pagtatapos ng workshop na ito, makakabuo ka ng:

| Sisyon | Output | Mga Kasanayang Naipakita |
|--------|--------|--------------------------|
| **1** | Chat application na may streaming | Setup ng serbisyo, basic completions, streaming UX |
| **2** | RAG system na may evaluation | Embeddings, semantic search, quality metrics |
| **3** | Multi-model benchmark suite | Pagsukat ng performance, paghahambing ng modelo |
| **4** | SLM vs LLM comparator | Trade-off analysis, optimization strategies |
| **5** | Multi-agent orchestrator | Disenyo ng agent, memory management, coordination |
| **6** | Intelligent routing system | Intent detection, model selection, scalability |

### Competency Matrix

| Antas ng Kasanayan | Sisyon 1-2 | Sisyon 3-4 | Sisyon 5-6 |
|--------------------|------------|------------|------------|
| **Baguhan**        | ✅ Setup & basics | ⚠️ Hamon | ❌ Masyadong advanced |
| **Intermediate**   | ✅ Mabilis na review | ✅ Pangunahing pag-aaral | ⚠️ Stretch goals |
| **Advanced**       | ✅ Madaling matapos | ✅ Pagpapahusay | ✅ Production patterns |

### Mga Kasanayang Handa sa Karera

**Pagkatapos ng workshop na ito, handa ka nang:**

✅ **Gumawa ng Privacy-First Applications**
- Mga healthcare apps na nagha-handle ng PHI/PII nang lokal
- Mga serbisyo sa pananalapi na may mga kinakailangan sa pagsunod
- Mga sistema ng gobyerno na may pangangailangan sa data sovereignty

✅ **I-optimize para sa Edge Environments**
- Mga IoT device na may limitadong resources
- Offline-first na mga mobile application
- Mga real-time na sistema na may mababang latency

✅ **Magdisenyo ng Intelligent Architectures**
- Multi-agent systems para sa complex workflows
- Hybrid edge-cloud deployments
- Cost-optimized AI infrastructure

✅ **Pangunahan ang Edge AI Initiatives**
- Suriin ang feasibility ng Edge AI para sa mga proyekto
- Pumili ng angkop na mga modelo at frameworks
- Magdisenyo ng scalable local AI solutions

---

## 🗺️ Estruktura ng Workshop

### Overview ng Sisyon (6 Sisyon × 30 Minuto = 3 Oras)

| Sisyon | Paksa | Pokus | Tagal |
|--------|-------|-------|-------|
| **1** | Pagsisimula sa Foundry Local | Install, validate, unang completions | 30 min |
| **2** | Paggawa ng AI Solutions gamit ang RAG | Prompt engineering, embeddings, evaluation | 30 min |
| **3** | Open Source Models | Model discovery, benchmarking, selection | 30 min |
| **4** | Cutting Edge Models | SLM vs LLM, optimization, frameworks | 30 min |
| **5** | AI-Powered Agents | Disenyo ng agent, orchestration, memory | 30 min |
| **6** | Models as Tools | Routing, chaining, scaling strategies | 30 min |

---

## 🚀 Mabilis na Pagsisimula

### Mga Kinakailangan

**Mga Kinakailangan sa Sistema:**
- **OS**: Windows 10/11, macOS 11+, o Linux (Ubuntu 20.04+)
- **RAM**: Minimum na 8GB, inirerekomenda ang 16GB+
- **Storage**: 10GB+ na libreng espasyo para sa mga modelo
- **CPU**: Modernong processor na may AVX2 support
- **GPU** (opsyonal): CUDA-compatible o Qualcomm NPU para sa acceleration

**Mga Kinakailangan sa Software:**
- **Python 3.8+** ([I-download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Gabay sa Pag-install](../../../Workshop))
- **Git** ([I-download](https://git-scm.com/downloads))
- **Visual Studio Code** (inirerekomenda) ([I-download](https://code.visualstudio.com/))

### Setup sa 3 Hakbang

#### 1. I-install ang Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**I-verify ang Installation:**
```bash
foundry --version
foundry service status
```

**Siguraduhing tumatakbo ang Azure AI Foundry Local na may fixed port**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**I-verify na gumagana ito:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Paghanap ng Available na Mga Modelo**
Upang makita kung aling mga modelo ang available sa iyong Foundry Local instance, maaari mong i-query ang models endpoint:

```bash
# cmd/bash/powershell
foundry model list
```

Gamit ang Web Endpoint 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Clone Repository & I-install ang Dependencies

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

#### 3. Patakbuhin ang Iyong Unang Sample

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Tagumpay!** Makikita mo ang isang streaming response tungkol sa edge AI.

---

## 📦 Mga Resources ng Workshop

### Python Samples

Mga progresibong hands-on na halimbawa na nagpapakita ng bawat konsepto:

| Sisyon | Sample | Deskripsyon | Run Time |
|--------|--------|-------------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Basic & streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG na may embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Pagsusuri ng kalidad ng RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Multi-model benchmarking | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM comparison | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Multi-agent system | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Intent-based routing | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Multi-step pipeline | ~60s |

### Jupyter Notebooks

Interactive na pag-explore na may mga paliwanag at visualizations:

| Sisyon | Notebook | Deskripsyon | Hirap |
|--------|----------|-------------|-------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Mga batayan ng chat & streaming | ⭐ Baguhan |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Gumawa ng RAG system | ⭐⭐ Intermediate |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02/rag_eval_ragas.ipynb) | Suriin ang kalidad ng RAG | ⭐⭐ Intermediate |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03/benchmark_oss_models.ipynb) | Benchmarking ng modelo | ⭐⭐ Intermediate |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04/model_compare.ipynb) | Paghahambing ng modelo | ⭐⭐ Intermediate |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05/agents_orchestrator.ipynb) | Orchestration ng agent | ⭐⭐⭐ Advanced |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06/models_router.ipynb) | Intent routing | ⭐⭐⭐ Advanced |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06/models_pipeline.ipynb) | Pipeline orchestration | ⭐⭐⭐ Advanced |

### Dokumentasyon

Komprehensibong mga gabay at reference:

| Dokumento | Deskripsyon | Gamitin Kapag |
|-----------|-------------|---------------|
| [QUICK_START.md](./QUICK_START.md) | Mabilis na gabay sa setup | Simula mula sa umpisa |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Command & API cheat sheet | Kailangan ng mabilis na sagot |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Mga pattern ng SDK & halimbawa | Pagsusulat ng code |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Gabay sa environment variable | Pag-configure ng mga sample |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Pinakabagong mga pagpapabuti sa sample | Pag-unawa sa mga pagbabago |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Gabay sa migration | Pag-upgrade ng code |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Karaniwang mga isyu & solusyon | Pag-debug ng mga problema |

---

## 🎓 Mga Rekomendasyon sa Landas ng Pag-aaral

### Para sa mga Baguhan (3-4 oras)
1. ✅ Sisyon 1: Pagsisimula (pokus sa setup at basic chat)
2. ✅ Sisyon 2: Mga Batayan ng RAG (laktawan ang evaluation sa simula)
3. ✅ Sisyon 3: Simpleng Benchmarking (2 modelo lamang)
4. ⏭️ Laktawan ang Sisyon 4-6 sa ngayon
5. 🔄 Bumalik sa Sisyon 4-6 pagkatapos makabuo ng unang aplikasyon

### Para sa Intermediate na mga Developer (3 oras)
1. ⚡ Sisyon 1: Mabilis na validation ng setup
2. ✅ Sisyon 2: Kumpletuhin ang RAG pipeline na may evaluation
3. ✅ Sisyon 3: Buong benchmarking suite
4. ✅ Sisyon 4: Optimization ng modelo
5. ✅ Sisyon 5-6: Pokus sa mga pattern ng arkitektura

### Para sa Advanced na mga Practitioner (2-3 oras)
1. ⚡ Sisyon 1-3: Mabilis na review at validation
2. ✅ Sisyon 4: Malalim na pag-aaral sa optimization
3. ✅ Sisyon 5: Arkitektura ng multi-agent
4. ✅ Sisyon 6: Mga pattern ng production at scaling
5. 🚀 Palawakin: Gumawa ng custom routing logic at hybrid deployments

---

## Workshop Session Pack (Nakatuon na 30‑Minutong Labs)

Kung sinusunod mo ang condensed na 6-session workshop format, gamitin ang mga dedikadong gabay na ito (bawat isa ay tumutugma at kumukumpleto sa mas malawak na module docs sa itaas):

| Workshop Session | Gabay | Pangunahing Pokus |
|------------------|-------|-------------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Install, validate, patakbuhin ang phi & GPT-OSS-20B, acceleration |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt engineering, RAG patterns, CSV & document grounding, migration |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face integration, benchmarking, model selection |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX acceleration |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Mga papel ng ahente, memorya, mga tool, orkestrasyon |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, chaining, scaling path sa Azure |

Ang bawat session file ay naglalaman ng: abstrak, mga layunin sa pag-aaral, 30-minutong demo flow, panimulang proyekto, checklist ng beripikasyon, troubleshooting, at mga sanggunian sa opisyal na Foundry Local Python SDK.

### Mga Sample na Script

I-install ang mga kinakailangan para sa workshop (Windows):

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

Kung pinapatakbo ang Foundry Local service sa ibang (Windows) makina o VM mula sa macOS, i-export ang endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Session | Script(s) | Deskripsyon |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap service & streaming chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimal RAG (in-memory embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | Pagsusuri ng RAG gamit ang ragas metrics |
| 3 | `samples/session03/benchmark_oss_models.py` | Multi-model latency & throughput benchmarking |
| 4 | `samples/session04/model_compare.py` | Paghahambing ng SLM vs LLM (latency & sample output) |
| 5 | `samples/session05/agents_orchestrator.py` | Dalawang ahente: pananaliksik → editorial pipeline |
| 6 | `samples/session06/models_router.py` | Demo ng routing batay sa intensyon |
|   | `samples/session06/models_pipeline.py` | Multi-step plan/execute/refine chain |

### Mga Variable ng Kapaligiran (Karaniwan sa Lahat ng Sample)

| Variable | Layunin | Halimbawa |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Default na alias ng isang modelo para sa mga simpleng sample | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Tiyak na SLM vs mas malaking modelo para sa paghahambing | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Listahan ng mga alias para sa benchmarking | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Pag-uulit ng benchmark kada modelo | `3` |
| `BENCH_PROMPT` | Prompt na ginamit sa benchmarking | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Override test query para sa RAG pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Override agents pipeline query | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias ng modelo para sa research agent | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias ng modelo para sa editor agent (maaaring magkaiba) | `gpt-oss-20b` |
| `SHOW_USAGE` | Kapag `1`, ipinapakita ang paggamit ng token kada completion | `1` |
| `RETRY_ON_FAIL` | Kapag `1`, subukang muli kapag may transient chat errors | `1` |
| `RETRY_BACKOFF` | Segundong paghihintay bago subukang muli | `1.0` |

Kung ang isang variable ay hindi nakatakda, ang mga script ay babalik sa mga makatuwirang default. Para sa mga demo ng isang modelo, karaniwang kailangan mo lamang ang `FOUNDRY_LOCAL_ALIAS`.

### Utility Module

Ang lahat ng sample ay gumagamit na ngayon ng helper na `samples/workshop_utils.py` na nagbibigay ng:

* Cached na `FoundryLocalManager` + OpenAI client creation
* `chat_once()` helper na may opsyonal na retry + usage printing
* Simpleng ulat ng paggamit ng token (i-enable gamit ang `SHOW_USAGE=1`)

Binabawasan nito ang pag-uulit at itinatampok ang pinakamahusay na mga kasanayan para sa mahusay na lokal na orkestrasyon ng modelo.

## Opsyonal na Mga Pagpapahusay (Cross-Session)

| Tema | Pagpapahusay | Mga Session | Env / Toggle |
|-------|-------------|----------|--------------|
| Determinism | Fixed temperature + stable prompt sets | 1–6 | Itakda ang `temperature=0`, `top_p=1` |
| Visibility ng Paggamit ng Token | Konsistent na pagtuturo ng gastos/episyensya | 1–6 | `SHOW_USAGE=1` |
| Streaming First Token | Sukatan ng latency na nararamdaman | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Retry Resilience | Hinahawakan ang transient cold-start | Lahat | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-Model Agents | Heterogeneous na espesyalisasyon ng papel | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptive Routing | Intensyon + cost heuristics | 6 | Palawakin ang router gamit ang escalation logic |
| Vector Memory | Pangmatagalang semantic recall | 2,5,6 | Isama ang FAISS/Chroma embedding index |
| Trace Export | Auditing & evaluation | 2,5,6 | Magdagdag ng JSON lines kada hakbang |
| Quality Rubrics | Pagsubaybay sa kalidad | 3–6 | Sekundaryong scoring prompts |
| Smoke Tests | Mabilis na beripikasyon bago ang workshop | Lahat | `python Workshop/tests/smoke.py` |

### Deterministic Quick Start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Asahan ang stable na bilang ng token sa mga paulit-ulit na magkaparehong input.

### Pagsusuri ng RAG (Session 2)

Gamitin ang `rag_eval_ragas.py` upang kalkulahin ang answer relevancy, faithfulness, at context precision sa isang maliit na synthetic dataset:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Palawakin sa pamamagitan ng pagbibigay ng mas malaking JSONL ng mga tanong, konteksto, at ground truths, pagkatapos ay i-convert sa Hugging Face `Dataset`.

## CLI Command Accuracy Appendix

Ang workshop ay sadyang gumagamit lamang ng kasalukuyang dokumentado / stable na Foundry Local CLI commands.

### Stable Commands na Binanggit

| Kategorya | Command | Layunin |
|----------|---------|---------|
| Core | `foundry --version` | Ipakita ang naka-install na bersyon |
| Core | `foundry init` | I-initialize ang configuration |
| Service | `foundry service start` | Simulan ang lokal na serbisyo (kung hindi auto) |
| Service | `foundry status` | Ipakita ang status ng serbisyo |
| Models | `foundry model list` | Ilista ang catalog / mga available na modelo |
| Models | `foundry model download <alias>` | I-download ang model weights sa cache |
| Models | `foundry model run <alias>` | Ipatakbo (i-load) ang isang modelo nang lokal; pagsamahin sa `--prompt` para sa one-shot |
| Models | `foundry model unload <alias>` / `foundry model stop <alias>` | I-unload ang isang modelo mula sa memorya (kung suportado) |
| Cache | `foundry cache list` | Ilista ang mga naka-cache (na-download) na modelo |
| System | `foundry system info` | Snapshot ng hardware & acceleration capabilities |
| System | `foundry system gpu-info` | Impormasyon sa GPU diagnostic |
| Config | `foundry config list` | Ipakita ang kasalukuyang config values |
| Config | `foundry config set <key> <value>` | I-update ang configuration |

### One‑Shot Prompt Pattern

Sa halip na ang deprecated na `model chat` subcommand, gamitin:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Ito ay nagsasagawa ng isang single prompt/response cycle pagkatapos ay mag-eexit.

### Mga Tinanggal / Iniiwasang Pattern

| Deprecated / Undocumented | Kapalit / Gabay |
|---------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Gumamit ng simpleng `foundry model list` + kamakailang aktibidad / logs |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Gumamit ng benchmark Python script + OS tools (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetry

- Latency, p95, tokens/sec: `samples/session03/benchmark_oss_models.py`
- First‑token latency (streaming): itakda ang `BENCH_STREAM=1`
- Resource usage: OS monitors (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Kapag ang mga bagong CLI telemetry commands ay naging stable upstream, maaari itong isama nang may kaunting edits sa session markdowns.

### Automated Lint Guard

Isang automated na linter ang pumipigil sa muling pagpapakilala ng mga deprecated na CLI patterns sa loob ng fenced code blocks ng mga markdown file:

Script: `Workshop/scripts/lint_markdown_cli.py`

Ang mga deprecated na pattern ay naka-block sa loob ng code fences.

Mga inirerekomendang kapalit:
| Deprecated | Kapalit |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark script + system tools |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Patakbuhin nang lokal:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` tumatakbo sa bawat push & PR.

Opsyonal na pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Quick CLI → SDK Migration Table

| Gawain | CLI One-Liner | SDK (Python) Equivalent | Tala |
|------|---------------|-------------------------|-------|
| Patakbuhin ang isang modelo (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | Ang SDK ay awtomatikong nagbo-bootstrap ng serbisyo & caching |
| I-download (cache) ang modelo | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Pinipili ng Manager ang pinakamahusay na variant kung ang alias ay tumutugma sa maraming builds |
| Ilista ang catalog | `foundry model list` | `# gamitin ang manager para sa bawat alias o panatilihin ang kilalang listahan` | Ang CLI ay nag-aaggregate; ang SDK ay kasalukuyang per-alias instantiation |
| Ilista ang mga naka-cache na modelo | `foundry cache list` | `manager.list_cached_models()` | Pagkatapos ng manager init (anumang alias) |
| I-enable ang GPU acceleration | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | Ang configuration ay external side effect |
| Kunin ang endpoint URL | (implicit) | `manager.endpoint` | Ginagamit upang lumikha ng OpenAI-compatible client |
| I-warm ang isang modelo | `foundry model run <alias>` pagkatapos ng unang prompt | `chat_once(alias, messages=[...])` (utility) | Ang mga utility ay humahawak sa initial cold latency warmup |
| Sukatin ang latency | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (o bagong exporter script) | Mas mainam ang script para sa consistent metrics |
| Ihinto / i-unload ang modelo | `foundry model unload <alias>` | (Hindi exposed – i-restart ang serbisyo / proseso) | Karaniwang hindi kinakailangan para sa workshop flow |
| Kunin ang paggamit ng token | (tingnan ang output) | `resp.usage.total_tokens` | Ibinibigay kung ang backend ay nagbabalik ng usage object |

## Benchmark Markdown Export

Gamitin ang script na `Workshop/scripts/export_benchmark_markdown.py` upang magpatakbo ng bagong benchmark (parehong lohika tulad ng `samples/session03/benchmark_oss_models.py`) at maglabas ng GitHub-friendly na Markdown table plus raw JSON.

### Halimbawa

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Mga na-generate na file:
| File | Nilalaman |
|------|----------|
| `benchmark_report.md` | Markdown table + mga interpretasyon na hint |
| `benchmark_report.json` | Raw metrics array (para sa diffing / trend tracking) |

Itakda ang `BENCH_STREAM=1` sa environment upang isama ang first-token latency kung suportado.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.