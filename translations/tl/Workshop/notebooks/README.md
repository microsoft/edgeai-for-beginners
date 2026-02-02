# Mga Notebook ng Workshop

> **Interactive Jupyter Notebooks para sa Praktikal na Pag-aaral ng Edge AI**
>
> Progresibo, self-paced na mga tutorial na nagsisimula sa mga pangunahing chat completions hanggang sa mga advanced na multi-agent systems gamit ang Microsoft Foundry Local at Small Language Models.

---

## 📖 Panimula

Maligayang pagdating sa koleksyon ng **EdgeAI for Beginners Workshop Notebooks**. Ang mga interactive na Jupyter notebook na ito ay nagbibigay ng praktikal na karanasan sa pag-aaral kung saan ikaw ay magsusulat, magpapatakbo, at mag-eeksperimento sa Edge AI code nang real-time.

### Bakit Jupyter Notebooks?

Hindi tulad ng mga tradisyunal na tutorial, ang mga notebook na ito ay nag-aalok ng:

- **Interactive na Pag-aaral**: Patakbuhin ang mga code cell at makita agad ang resulta  
- **Eksperimentasyon**: Baguhin ang mga parameter at obserbahan ang mga pagbabago nang real-time  
- **Dokumentasyon**: May mga paliwanag at markdown cells na gumagabay sa iyo sa mga konsepto  
- **Reproducibility**: Kumpletong mga gumaganang halimbawa na maaari mong balikan at gamitin muli  
- **Visualization**: Tingnan ang mga performance metrics, embeddings, at resulta nang direkta sa notebook  

### Ano ang Espesyal sa mga Notebook na Ito?

Ang bawat notebook ay dinisenyo batay sa **mga best practices na handa para sa produksyon**:

✅ **Komprehensibong Error Handling** - Maayos na paghawak sa mga error at nagbibigay ng malinaw na mensahe ng error  
✅ **Type Hints at Dokumentasyon** - Malinaw na mga pirma ng function at docstrings  
✅ **Performance Monitoring** - Pagsubaybay sa paggamit ng token at pagsukat ng latency  
✅ **Modular na Disenyo** - Mga reusable na pattern na maaari mong iakma sa iyong mga proyekto  
✅ **Progresibong Komplikasyon** - Sistematikong bumubuo mula sa mga naunang sesyon  

---

## 🎯 Mga Layunin sa Pag-aaral

### Mga Pangunahing Kasanayan na Iyong Mabubuo

Sa pamamagitan ng pagdaan sa mga notebook na ito, matututuhan mo ang:

1. **Pamamahala ng Local AI Service**
   - I-configure at pamahalaan ang mga serbisyo ng Microsoft Foundry Local  
   - Pumili at mag-load ng angkop na mga modelo para sa iyong hardware  
   - Subaybayan ang paggamit ng mga resources at i-optimize ang performance  
   - Pangasiwaan ang service discovery at health checking  

2. **Pagbuo ng AI Application**
   - Magpatupad ng OpenAI-compatible na chat completions nang lokal  
   - Gumawa ng mga streaming interface para sa mas magandang karanasan ng user  
   - Magdisenyo ng epektibong mga prompt para sa Small Language Models  
   - Isama ang mga lokal na modelo sa mga aplikasyon  

3. **Retrieval Augmented Generation (RAG)**
   - Gumawa ng semantic search gamit ang vector embeddings  
   - I-ground ang mga sagot ng LLM sa mga dokumentong may kaugnayan sa domain  
   - Suriin ang kalidad ng RAG gamit ang mga RAGAS metrics  
   - Mag-scale mula prototype hanggang produksyon  

4. **Pag-optimize ng Performance**
   - Sistematikong i-benchmark ang maraming modelo  
   - Sukatin ang latency, throughput, at first-token time  
   - Ihambing ang Small Language Models sa Large Language Models  
   - Pumili ng pinakamainam na mga modelo batay sa trade-offs ng performance/quality  

5. **Multi-Agent Orchestration**
   - Magdisenyo ng mga espesyal na agent para sa iba't ibang gawain  
   - Magpatupad ng agent memory at context management  
   - I-coordinate ang maraming agent sa mga kumplikadong workflow  
   - Gumawa ng mga coordinator pattern para sa kolaborasyon ng mga agent  

6. **Intelligent Model Routing**
   - Magpatupad ng intent detection at pattern matching  
   - I-route ang mga query sa angkop na mga modelo nang awtomatiko  
   - Gumawa ng mga multi-step pipeline (plan → execute → refine)  
   - Magdisenyo ng scalable na model-as-tools architectures  

---

## 🎓 Mga Layunin sa Pag-aaral

### Ano ang Iyong Mabubuo

| Notebook | Output | Mga Kasanayang Naipakita | Antas ng Hirap |
|----------|--------|--------------------------|----------------|
| **Session 01** | Chat app na may streaming | Setup ng serbisyo, basic completions, streaming UX | ⭐ Baguhan |
| **Session 02 (RAG)** | RAG pipeline na may pagsusuri | Embeddings, semantic search, quality metrics | ⭐⭐ Intermediate |
| **Session 02 (Eval)** | RAG quality evaluator | RAGAS metrics, systematic evaluation | ⭐⭐ Intermediate |
| **Session 03** | Multi-model benchmark | Pagsukat ng performance, paghahambing ng modelo | ⭐⭐ Intermediate |
| **Session 04** | SLM vs LLM comparator | Pagsusuri ng trade-offs, mga estratehiya sa pag-optimize | ⭐⭐⭐ Advanced |
| **Session 05** | Multi-agent orchestrator | Disenyo ng agent, memorya, koordinasyon | ⭐⭐⭐ Advanced |
| **Session 06 (Router)** | Intelligent routing system | Intent detection, pagpili ng modelo | ⭐⭐⭐ Advanced |
| **Session 06 (Pipeline)** | Multi-step pipeline | Plan/execute/refine workflows | ⭐⭐⭐ Advanced |

### Pag-unlad ng Kakayahan

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Iskedyul ng Workshop

### 🚀 Half-Day Workshop (3.5 oras)

**Perpekto para sa: Team training sessions, hackathons, conference workshops**

| Oras | Tagal | Sesyon | Mga Paksa | Mga Aktibidad |
|------|-------|--------|-----------|--------------|
| **0:00** | 30 min | Setup & Intro | Setup ng environment, pag-install ng Foundry Local | Mag-install ng dependencies, i-verify ang setup |
| **0:30** | 30 min | Session 01 | Basic chat completions, streaming | Patakbuhin ang notebook, baguhin ang mga prompt |
| **1:00** | 45 min | Session 02 | RAG pipeline, embeddings, pagsusuri | Gumawa ng RAG system, subukan ang mga query |
| **1:45** | 15 min | Break | ☕ Kape at mga tanong | — |
| **2:00** | 30 min | Session 03 | Multi-model benchmarking | Ihambing ang 3+ na modelo |
| **2:30** | 30 min | Session 04 | SLM vs LLM trade-offs | Suriin ang performance/quality |
| **3:00** | 30 min | Session 05-06 | Multi-agent systems & routing | Tuklasin ang mga advanced na pattern |

**Output**: Ang mga kalahok ay aalis na may 6 na gumaganang Edge AI applications at mga production-ready code patterns.

---

### 🎓 Full-Day Workshop (6 oras)

**Perpekto para sa: Mas malalim na pagsasanay, bootcamps, mga kurso sa unibersidad**

| Oras | Tagal | Sesyon | Mga Paksa | Mga Aktibidad |
|------|-------|--------|-----------|--------------|
| **0:00** | 45 min | Setup & Theory | Setup ng environment, mga pundasyon ng Edge AI | Mag-install, mag-verify, talakayin ang mga use case |
| **0:45** | 45 min | Session 01 | Malalim na talakayan sa chat completions | Magpatupad ng basic at streaming chat |
| **1:30** | 30 min | Break | ☕ Kape at networking | — |
| **2:00** | 60 min | Session 02 (Pareho) | RAG pipeline + RAGAS evaluation | Gumawa ng kumpletong RAG system |
| **3:00** | 30 min | Hands-On Lab 1 | Custom RAG para sa iyong domain | I-apply sa sariling mga dokumento |
| **3:30** | 30 min | Tanghalian | 🍽️ | — |
| **4:00** | 45 min | Session 03 | Pamamaraan ng benchmarking | Sistematikong paghahambing ng modelo |
| **4:45** | 45 min | Session 04 | Mga estratehiya sa pag-optimize | SLM vs LLM analysis |
| **5:30** | 60 min | Session 05-06 | Advanced na orkestrasyon | Multi-agent systems, routing |
| **6:30** | 30 min | Hands-On Lab 2 | Gumawa ng custom na agent system | Disenyo ng sariling orchestrator |

**Output**: Malalim na pag-unawa sa mga pattern ng Edge AI kasama ang 2 custom na proyekto.

---

### 📚 Self-Paced Learning (2 linggo)

**Perpekto para sa: Mga indibidwal na nag-aaral, online courses, self-study**

#### Linggo 1: Mga Pundasyon (6 oras)

| Araw | Pokus | Tagal | Mga Notebook | Takdang-Aralin |
|------|-------|-------|--------------|----------------|
| **Lunes** | Setup & Mga Pangunahing Kaalaman | 1.5 oras | Session 01 | Baguhin ang mga prompt, subukan ang streaming |
| **Miyerkules** | Mga Pundasyon ng RAG | 2 oras | Session 02 (pareho) | Magdagdag ng sariling mga dokumento |
| **Biyernes** | Benchmarking | 1.5 oras | Session 03 | Ihambing ang karagdagang mga modelo |
| **Sabado** | Pagsusuri at Pagsasanay | 1 oras | Lahat ng Linggo 1 | Kumpletuhin ang mga ehersisyo, mag-debug |

#### Linggo 2: Advanced (5 oras)

| Araw | Pokus | Tagal | Mga Notebook | Takdang-Aralin |
|------|-------|-------|--------------|----------------|
| **Lunes** | Pag-optimize | 1.5 oras | Session 04 | Idokumento ang mga trade-offs |
| **Miyerkules** | Multi-Agent Systems | 2 oras | Session 05 | Magdisenyo ng custom na mga agent |
| **Biyernes** | Intelligent Routing | 1.5 oras | Session 06 (pareho) | Gumawa ng routing logic |
| **Sabado** | Panghuling Proyekto | 2 oras | Integration | Pagsamahin ang maraming pattern |

**Output**: Mastery ng mga pattern ng Edge AI kasama ang portfolio project.

---

## 📔 Mga Deskripsyon ng Notebook

### 📘 Session 01: Chat Bootstrap
**File**: `session01_chat_bootstrap.ipynb`  
**Tagal**: 20-30 minuto  
**Mga Kinakailangan**: Wala  
**Antas ng Hirap**: ⭐ Baguhan

**Ano ang Iyong Matututuhan**:
- Mag-install at mag-configure ng Foundry Local Python SDK  
- Gamitin ang `FoundryLocalManager` para sa awtomatikong service discovery  
- Magpatupad ng basic chat completions gamit ang OpenAI-compatible API  
- Gumawa ng streaming responses para sa mas magandang karanasan ng user  
- Maayos na pangasiwaan ang mga error at service unavailability  

**Pangunahing Konsepto**: Pamamahala ng serbisyo, chat completions, streaming, error handling  

**Iyong Mabubuo**: Interactive na chat application na may streaming support  

---

### 📗 Session 02: RAG Pipeline
**File**: `session02_rag_pipeline.ipynb`  
**Tagal**: 30-45 minuto  
**Mga Kinakailangan**: Session 01  
**Antas ng Hirap**: ⭐⭐ Intermediate

**Ano ang Iyong Matututuhan**:
- Magpatupad ng Retrieval Augmented Generation (RAG) pattern  
- Gumawa ng vector embeddings gamit ang sentence-transformers  
- Gumawa ng semantic search gamit ang cosine similarity  
- I-ground ang mga sagot ng LLM sa mga dokumento ng domain  
- Pangasiwaan ang mga optional dependencies gamit ang import guards  

**Pangunahing Konsepto**: RAG architecture, embeddings, semantic search, vector similarity  

**Iyong Mabubuo**: Document-grounded question-answering system  

---

### 📗 Session 02: RAG Evaluation with RAGAS
**File**: `session02_rag_eval_ragas.ipynb`  
**Tagal**: 30-45 minuto  
**Mga Kinakailangan**: Session 02 RAG Pipeline  
**Antas ng Hirap**: ⭐⭐ Intermediate

**Ano ang Iyong Matututuhan**:
- Suriin ang kalidad ng RAG gamit ang mga industry-standard metrics  
- Sukatin ang context relevance, answer relevance, faithfulness  
- Gamitin ang RAGAS framework para sa sistematikong pagsusuri  
- Tukuyin at ayusin ang mga isyu sa kalidad ng RAG  
- Gumawa ng mga dataset para sa pagsusuri sa iyong domain  

**Pangunahing Konsepto**: RAG evaluation, RAGAS metrics, quality measurement, systematic testing  

**Iyong Mabubuo**: RAG quality evaluation framework  

---

### 📙 Session 03: Benchmark OSS Models
**File**: `session03_benchmark_oss_models.ipynb`  
**Tagal**: 30-45 minuto  
**Mga Kinakailangan**: Session 01  
**Antas ng Hirap**: ⭐⭐ Intermediate

**Ano ang Iyong Matututuhan**:
- Sistematikong i-benchmark ang maraming modelo  
- Sukatin ang latency, throughput, first-token time  
- Magpatupad ng maayos na paghawak sa mga pagkabigo ng modelo  
- Ihambing ang performance sa iba't ibang pamilya ng modelo  
- I-visualize at suriin ang mga resulta ng benchmark  

**Pangunahing Konsepto**: Performance benchmarking, latency measurement, model comparison, statistical analysis  

**Iyong Mabubuo**: Multi-model benchmarking suite  

---

### 📙 Session 04: Model Comparison (SLM vs LLM)
**File**: `session04_model_compare.ipynb`  
**Tagal**: 30-45 minuto  
**Mga Kinakailangan**: Sessions 01, 03  
**Antas ng Hirap**: ⭐⭐⭐ Advanced

**Ano ang Iyong Matututuhan**:
- Ihambing ang Small Language Models sa Large Language Models  
- Suriin ang trade-offs ng performance vs quality  
- Sukatin ang mga edge-suitability metrics  
- Pumili ng pinakamainam na mga modelo para sa mga deployment constraints  
- Idokumento ang mga pamantayan sa desisyon para sa pagpili ng modelo  

**Pangunahing Konsepto**: Model selection, trade-off analysis, optimization strategies, deployment planning  

**Iyong Mabubuo**: SLM vs LLM comparison framework  

---

### 📕 Session 05: Multi-Agent Orchestrator
**File**: `session05_agents_orchestrator.ipynb`  
**Tagal**: 45-60 minuto  
**Mga Kinakailangan**: Sessions 01-02  
**Antas ng Hirap**: ⭐⭐⭐ Advanced

**Ano ang Iyong Matututuhan**:
- Magdisenyo ng mga espesyal na agent para sa iba't ibang gawain  
- Magpatupad ng agent memory at context management  
- Gumawa ng mga coordinator pattern para sa kolaborasyon ng mga agent  
- Pangasiwaan ang komunikasyon at handoffs ng agent  
- Subaybayan ang performance ng multi-agent system  

**Pangunahing Konsepto**: Agent architecture, coordinator patterns, memory management, agent orchestration  

**Iyong Mabubuo**: Multi-agent system na may coordinator at mga espesyalista  

---

### 📕 Session 06: Model Router
**File**: `session06_models_router.ipynb`  
**Tagal**: 30-45 minuto  
**Mga Kinakailangan**: Sessions 01, 03  
**Antas ng Hirap**: ⭐⭐⭐ Advanced

**Ano ang Iyong Matututuhan**:
- Magpatupad ng intent detection at pattern matching  
- Gumawa ng keyword-based model routing  
- I-route ang mga query sa angkop na mga modelo nang awtomatiko  
- I-configure ang mga multi-model registries  
- Subaybayan ang mga desisyon sa routing at performance  

**Pangunahing Konsepto**: Intent detection, model routing, pattern matching, intelligent selection  

**Iyong Mabubuo**: Intelligent model routing system  

---

### 📕 Session 06: Multi-Step Pipeline
**File**: `session06_models_pipeline.ipynb`  
**Tagal**: 30-45 minuto  
**Mga Kinakailangan**: Sessions 01, 06 Router  
**Antas ng Hirap**: ⭐⭐⭐ Advanced

**Ano ang Iyong Matututuhan**:
- Gumawa ng multi-step AI pipelines (plan → execute → refine)  
- Isama ang router para sa intelligent model selection  
- Magpatupad ng error handling at recovery sa pipeline  
- Subaybayan ang performance at mga yugto ng pipeline  
- Disenyo ng scalable na arkitektura para sa model-as-tools

**Mga Pangunahing Konsepto**: Arkitektura ng pipeline, multi-stage na pagproseso, pag-recover ng error, mga pattern ng scalability

**Gagawin Mo**: Multi-step na intelligent pipeline na may routing

---

## 🚀 Pagsisimula

### Mga Kinakailangan

**Mga Kinakailangan sa Sistema**:
- **OS**: Windows 10/11, macOS 11+, o Linux (Ubuntu 20.04+)
- **RAM**: Minimum na 8GB, inirerekomenda ang 16GB+
- **Storage**: 10GB+ na libreng espasyo para sa mga modelo
- **Hardware**: CPU na may AVX2; GPU (CUDA, Qualcomm NPU) opsyonal

**Mga Kinakailangan sa Software**:
- **Python 3.8+** na may pip
- **Jupyter Notebook** o **VS Code** na may Jupyter extension
- **Microsoft Foundry Local** na naka-install at naka-configure
- **Git** (para sa pag-clone ng repository)

### Mga Hakbang sa Pag-install

#### 1. I-install ang Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**I-verify ang Pag-install**:
```bash
foundry --version
```

#### 2. I-set Up ang Python Environment

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

#### 3. Simulan ang Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. I-launch ang Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Mabilis na Pag-verify

Patakbuhin ito sa isang Python cell upang i-verify ang setup:

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

**Inaasahang Output**: Isang greeting response mula sa lokal na modelo.

---

## 📝 Mga Pinakamahusay na Praktika sa Workshop

### Para sa mga Instruktor

**Bago ang Workshop**:
- ✅ Magpadala ng mga tagubilin sa pag-install 1 linggo bago magsimula
- ✅ Subukan ang lahat ng notebook sa target na hardware
- ✅ Maghanda ng gabay sa pag-troubleshoot para sa mga karaniwang isyu
- ✅ Magkaroon ng backup na mga modelo (phi-3.5-mini kung sakaling mag-fail ang phi-4-mini)
- ✅ Mag-set up ng shared chat channel para sa mga tanong

**Habang Nasa Workshop**:
- ✅ Magsimula sa mabilis na pag-check ng environment (5 minuto)
- ✅ Agad na ibahagi ang mga resource para sa troubleshooting
- ✅ Hikayatin ang eksperimento at mga pagbabago
- ✅ Gumamit ng mga break nang maayos (pagkatapos ng bawat 2 session)
- ✅ Magkaroon ng mga TA para sa 1-on-1 na tulong

**Pagkatapos ng Workshop**:
- ✅ Ibahagi ang kumpletong working notebooks at mga solusyon
- ✅ Magbigay ng mga link sa karagdagang resources
- ✅ Gumawa ng feedback survey para sa pagpapabuti
- ✅ Mag-alok ng office hours para sa mga follow-up na tanong

### Para sa mga Nag-aaral

**Sulitin ang Iyong Pag-aaral**:
- ✅ Kumpletuhin ang setup bago magsimula ang workshop
- ✅ Patakbuhin ang bawat code cell nang sarili (huwag lang basahin)
- ✅ Mag-eksperimento sa mga parameter at prompt
- ✅ Magtala ng mga insight at mga natutunan
- ✅ Magtanong kapag nahihirapan (malamang may parehong tanong ang iba)

**Mga Karaniwang Pagkakamali na Dapat Iwasan**:
- ❌ Pag-skip sa pagkakasunod-sunod ng cell execution (patakbuhin nang sunod-sunod)
- ❌ Hindi maingat na pagbabasa ng mga error message
- ❌ Pagmamadali nang hindi nauunawaan
- ❌ Pagwawalang-bahala sa mga paliwanag sa markdown
- ❌ Hindi pag-save ng mga binagong notebook

**Mga Tip sa Pag-debug**:
1. **Hindi Tumatakbo ang Serbisyo**: I-check ang `foundry service status`
2. **Import Errors**: Siguraduhing naka-activate ang virtual environment
3. **Model Not Found**: Patakbuhin ang `foundry model ls` upang makita ang mga loaded na modelo
4. **Mabagal na Performance**: I-check ang RAM usage, isara ang ibang mga application
5. **Hindi Inaasahang Resulta**: I-restart ang kernel at patakbuhin ang lahat ng cell mula sa simula

---

## 🔗 Karagdagang Resources

### Mga Materyales sa Workshop

- **[Workshop Main Guide](../Readme.md)** - Overview, mga layunin sa pag-aaral, mga resulta sa karera
- **[Python Samples](../../../../Workshop/samples)** - Mga kaukulang Python script para sa bawat session
- **[Session Guides](../../../../Workshop)** - Detalyadong markdown guides (Session01-06)
- **[Scripts](../../../../Workshop/scripts)** - Mga utility para sa validation at testing
- **[Troubleshooting](./TROUBLESHOOTING.md)** - Mga karaniwang isyu at solusyon
- **[Quick Start](./quickstart.md)** - Gabay para sa mabilis na pagsisimula

### Dokumentasyon

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Opisyal na dokumentasyon ng Microsoft
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Reference para sa OpenAI SDK
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentasyon ng embedding models
- **[RAGAS Framework](https://docs.ragas.io/)** - Mga sukatan para sa RAG evaluation

### Komunidad

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Magtanong, magbahagi ng mga proyekto
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Real-time na suporta mula sa komunidad
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Mga teknikal na Q&A

---

## 🎯 Mga Rekomendasyon sa Learning Path

### Beginner Track (Simulan Dito)

1. **Session 01** - Chat Bootstrap
2. **Session 02** - RAG Pipeline
3. **Session 03** - Benchmark Models

**Oras**: ~2 oras | **Pokos**: Mga pundasyong pattern

---

### Intermediate Track

1. Kumpletuhin ang Beginner Track
2. **Session 02** - RAG Evaluation
3. **Session 04** - Model Comparison

**Oras**: ~4 oras | **Pokos**: Kalidad at optimisasyon

---

### Advanced Track (Buong Workshop)

1. Kumpletuhin ang Intermediate Track
2. **Session 05** - Multi-Agent Orchestrator
3. **Session 06** - Model Router
4. **Session 06** - Multi-Step Pipeline

**Oras**: ~6 oras | **Pokos**: Mga pattern para sa produksyon

---

### Custom Project Track

1. Kumpletuhin ang Beginner Track (Sessions 01-03)
2. Pumili ng ISA pang advanced session batay sa iyong layunin:
   - **Gumagawa ng RAG app?** → Session 02 Evaluation
   - **Nag-o-optimize ng performance?** → Session 04 Comparison
   - **Mga complex na workflow?** → Session 05 Orchestrator
   - **Scalable na arkitektura?** → Session 06 Router + Pipeline

**Oras**: ~3 oras | **Pokos**: Mga kasanayan para sa proyekto

---

## 📊 Mga Sukatan ng Tagumpay

Subaybayan ang iyong progreso gamit ang mga milestone na ito:

- [ ] **Setup Kumpleto** - Foundry Local tumatakbo, lahat ng dependencies naka-install
- [ ] **Unang Chat** - Session 01 kumpleto, streaming chat gumagana
- [ ] **RAG Naitayo** - Session 02 kumpleto, document QA system functional
- [ ] **Mga Modelo Na-benchmark** - Session 03 kumpleto, performance data nakolekta
- [ ] **Mga Trade-off Nasuri** - Session 04 kumpleto, pamantayan sa pagpili ng modelo na-dokumentado
- [ ] **Mga Agent Na-orchestrate** - Session 05 kumpleto, multi-agent system gumagana
- [ ] **Routing Naipatupad** - Session 06 kumpleto, intelligent model selection functional
- [ ] **Custom Project** - Na-apply ang mga pattern ng workshop sa iyong sariling use case

---

## 🤝 Pag-aambag

May nakita kang isyu o may mungkahi? Malugod naming tinatanggap ang mga kontribusyon!

- **Mag-report ng mga Isyu**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Magmungkahi ng Pagpapabuti**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Mag-submit ng PRs**: Sundin ang [Contributing Guidelines](../../AGENTS.md)

---

## 📄 Lisensya

Ang workshop na ito ay bahagi ng [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) repository at lisensyado sa ilalim ng [MIT License](../../../../LICENSE).

---

**Handa ka na bang gumawa ng production-ready na Edge AI applications?**  
**Simulan sa [Session 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Huling Na-update: Oktubre 8, 2025 | Bersyon ng Workshop: 2.0*

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.