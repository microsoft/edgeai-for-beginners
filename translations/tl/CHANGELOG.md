# Changelog

Ang lahat ng mahahalagang pagbabago sa EdgeAI para sa mga Nagsisimula ay dokumentado dito. Ang proyektong ito ay gumagamit ng mga entry na nakabase sa petsa at ang estilo ng Keep a Changelog (Idinagdag, Binago, Naayos, Tinanggal, Dokumentasyon, Inilipat).

## 2025-10-30

### Idinagdag - Module06 AI Agents Comprehensive Enhancement
- **Microsoft Agent Framework Integration** (`Module06/01.IntroduceAgent.md`):
  - Kumpletong seksyon tungkol sa Microsoft Agent Framework para sa produksyon-ready na pag-develop ng mga agent
  - Detalyadong mga pattern ng integrasyon gamit ang Foundry Local para sa edge deployment
  - Mga halimbawa ng multi-agent orchestration gamit ang mga espesyal na SLM model
  - Mga pattern ng enterprise deployment na may resource management at monitoring
  - Mga tampok sa seguridad at pagsunod para sa mga edge agent system
  - Mga halimbawa ng totoong implementasyon (retail, healthcare, customer service)

- **Mga Estratehiya sa Produksyon ng SLM Agent Deployment**:
  - **Foundry Local**: Kumpletong dokumentasyon ng enterprise-grade edge AI runtime na may installation, configuration, at mga pattern ng produksyon
  - **Ollama**: Pinahusay na deployment na nakatuon sa komunidad na may komprehensibong monitoring at model management
  - **VLLM**: High-performance inference engine na may advanced optimization techniques at mga tampok ng enterprise
  - Mga checklist ng deployment sa produksyon at mga comparison table para sa lahat ng tatlong platform

- **Pagpapahusay ng Edge-Optimized SLM Frameworks**:
  - **ONNX Runtime**: Bagong komprehensibong seksyon para sa cross-platform SLM agent deployment
  - Mga universal deployment pattern sa Windows, Linux, macOS, iOS, at Android
  - Mga opsyon sa hardware acceleration (CPU, GPU, NPU) na may automatic detection
  - Mga tampok na handa sa produksyon at mga optimizations na partikular sa agent
  - Kumpletong mga halimbawa ng implementasyon na may integrasyon sa Microsoft Agent Framework

- **Mga Sanggunian at Karagdagang Pagbabasa**:
  - Komprehensibong library ng mga mapagkukunan na may 100+ awtoritatibong sanggunian
  - Mga pangunahing research paper tungkol sa AI agents at Small Language Models
  - Opisyal na dokumentasyon para sa lahat ng pangunahing framework at tools
  - Mga ulat sa industriya, pagsusuri sa merkado, at mga teknikal na benchmark
  - Mga mapagkukunan sa edukasyon, mga kumperensya, at mga forum ng komunidad
  - Mga pamantayan, espesipikasyon, at mga framework ng pagsunod

### Binago - Module06 Content Modernization
- **Pinahusay na Learning Objectives**: Idinagdag ang mastery sa Microsoft Agent Framework at mga kakayahan sa edge deployment
- **Produksyon na Pokus**: Lumipat mula sa konsepto patungo sa mga gabay na handa sa implementasyon na may mga halimbawa ng produksyon
- **Mga Halimbawa ng Code**: In-update ang lahat ng halimbawa upang gumamit ng modernong SDK patterns at best practices
- **Mga Pattern ng Arkitektura**: Idinagdag ang hierarchical agent architectures at edge-to-cloud coordination
- **Pag-optimize ng Performance**: Pinahusay gamit ang mga rekomendasyon sa resource management at auto-scaling

### Dokumentasyon - Module06 Structure Enhancement
- **Komprehensibong Coverage ng Agent Framework**: Mula sa mga pangunahing konsepto hanggang sa enterprise deployment
- **Mga Estratehiya sa Deployment ng Produksyon**: Kumpletong mga gabay para sa Foundry Local, Ollama, at VLLM
- **Cross-Platform Optimization**: Idinagdag ang ONNX Runtime para sa universal deployment
- **Library ng Mapagkukunan**: Malawak na mga sanggunian para sa patuloy na pag-aaral at implementasyon

### Idinagdag - Module06 Model Context Protocol (MCP) Documentation Update
- **Modernisasyon ng MCP Introduction** (`Module06/03.IntroduceMCP.md`):
  - In-update gamit ang pinakabagong MCP specifications mula sa modelcontextprotocol.io (bersyon 2025-06-18)
  - Idinagdag ang opisyal na USB-C analogy para sa standardized AI application connections
  - In-update ang seksyon ng arkitektura gamit ang opisyal na two-layer design (Data Layer + Transport Layer)
  - Pinahusay ang dokumentasyon ng core primitives gamit ang server primitives (Tools, Resources, Prompts) at client primitives (Sampling, Elicitation, Logging)

- **Komprehensibong MCP References at Resources**:
  - Idinagdag ang **MCP for Beginners** link (https://aka.ms/mcp-for-beginners) 
  - Opisyal na dokumentasyon at mga espesipikasyon ng MCP (modelcontextprotocol.io)
  - Mga mapagkukunan sa pag-develop kabilang ang MCP Inspector at mga reference implementations
  - Mga teknikal na pamantayan (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Idinagdag - Module04 Qualcomm QNN Integration
- **Bagong Seksyon 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Komprehensibong 400+ linya ng gabay na sumasaklaw sa unified AI inference framework ng Qualcomm
  - Detalyadong coverage ng heterogeneous computing (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardware-aware optimization para sa Snapdragon platforms na may intelligent workload distribution
  - Advanced quantization techniques (INT8, INT16, mixed-precision) para sa mobile deployment
  - Power-efficient inference optimization para sa mga device na pinapagana ng baterya at mga real-time na aplikasyon
  - Kumpletong gabay sa pag-install gamit ang QNN SDK setup at environment configuration
  - Praktikal na mga halimbawa: PyTorch to QNN conversion, multi-backend optimization, context binary generation
  - Mga advanced na pattern ng paggamit: custom backend configuration, dynamic quantization, performance profiling
  - Komprehensibong seksyon ng troubleshooting at mga mapagkukunan ng komunidad

- **Pinahusay na istruktura ng Module04**:
  - In-update ang README.md upang isama ang 7 progresibong seksyon (dating 6)
  - Idinagdag ang Qualcomm QNN sa performance benchmarks table (5-15x speed improvement, 50-80% memory reduction)
  - Komprehensibong learning outcomes para sa mobile AI deployment at power optimization

### Binago - Module04 Documentation Updates
- **Pinahusay na dokumentasyon ng Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Idinagdag ang komprehensibong seksyon ng "Olive Recipes Repository" na sumasaklaw sa 100+ pre-built optimization recipes
  - Detalyadong coverage ng mga suportadong model families (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Mga praktikal na halimbawa ng paggamit para sa recipe customization at kontribusyon ng komunidad
  - Pinahusay gamit ang mga performance benchmark at gabay sa integrasyon

- **Pagkakaayos ng mga seksyon sa Module04**:
  - Ang Apple MLX ay inilipat sa Seksyon 5 (dating Seksyon 6)
  - Ang Workflow Synthesis ay inilipat sa Seksyon 6 (dating Seksyon 7)  
  - Ang Qualcomm QNN ay inilagay bilang Seksyon 7 (nakatuon sa mobile/edge)
  - In-update ang lahat ng file references at navigation links nang naaayon

### Naayos - Workshop Sample Validation
- **chat_bootstrap.py validation at repair**:
  - Naayos ang corrupted import statement (`util.util.workshop_utils` → `util.workshop_utils`)
  - Ginawa ang nawawalang `__init__.py` sa util package para sa tamang Python module resolution
  - Na-install ang mga kinakailangang dependencies (openai, foundry-local-sdk) sa conda environment
  - Matagumpay na na-validate ang sample execution gamit ang parehong default at custom prompts
  - Nakumpirma ang integrasyon sa Foundry Local service at model loading (phi-4-mini na may CUDA optimization)

### Dokumentasyon - Comprehensive Guide Updates
- **Module04 README.md kumpletong restructure**:
  - Idinagdag ang Qualcomm QNN bilang pangunahing optimization framework kasama ang OpenVINO, Olive, MLX
  - In-update ang mga learning outcomes ng chapter upang isama ang mobile AI deployment at power optimization
  - Pinahusay ang performance comparison table gamit ang QNN metrics at mga mobile/edge use cases
  - Pinanatili ang lohikal na progression mula sa enterprise solutions patungo sa platform-specific optimizations

- **Mga cross-references at navigation**:
  - In-update ang lahat ng internal links at file references para sa bagong numbering ng seksyon
  - Pinahusay ang deskripsyon ng workflow synthesis upang isama ang mobile, desktop, at cloud environments
  - Idinagdag ang komprehensibong mga resource links para sa Qualcomm developer ecosystem

## 2025-10-08

### Idinagdag - Workshop Comprehensive Update
- **Workshop README.md kumpletong rewrite**:
  - Idinagdag ang komprehensibong introduksyon na nagpapaliwanag ng halaga ng Edge AI (privacy, performance, cost)
  - Gumawa ng 6 pangunahing learning objectives na may detalyadong competencies
  - Idinagdag ang learning outcomes table na may deliverables at competency matrix
  - Isinama ang seksyon ng career-ready skills para sa industry relevance
  - Idinagdag ang quick start guide na may prerequisites at 3-step setup
  - Gumawa ng mga resource tables para sa Python samples (8 files na may run times)
  - Idinagdag ang Jupyter notebooks table (8 notebooks na may difficulty ratings)
  - Gumawa ng documentation table (7 key docs na may "Use When" guidance)
  - Idinagdag ang mga rekomendasyon sa learning path para sa iba't ibang skill levels

- **Workshop validation at testing infrastructure**:
  - Gumawa ng `scripts/validate_samples.py` - Komprehensibong validation tool para sa syntax, imports, at best practices
  - Gumawa ng `scripts/test_samples.py` - Smoke test runner para sa lahat ng Python samples
  - Idinagdag ang validation documentation sa `scripts/README.md`

- **Komprehensibong dokumentasyon**:
  - Gumawa ng `SAMPLES_UPDATE_SUMMARY.md` - 400+ linya ng detalyadong gabay na sumasaklaw sa lahat ng pagpapabuti
  - Gumawa ng `UPDATE_COMPLETE.md` - Executive summary ng update completion
  - Gumawa ng `QUICK_REFERENCE.md` - Quick reference card para sa Workshop

### Binago - Workshop Python Sample Modernization
- **Lahat ng 8 Python samples ay in-update gamit ang best practices**:
  - Pinahusay ang error handling gamit ang try-except blocks sa lahat ng I/O operations
  - Idinagdag ang type hints at komprehensibong docstrings
  - Nagpatupad ng consistent [INFO]/[ERROR]/[RESULT] logging pattern
  - Protektado ang optional imports na may installation hints
  - Pinahusay ang user feedback sa lahat ng samples

- **session01/chat_bootstrap.py**:
  - Pinahusay ang client initialization na may komprehensibong error messages
  - Pinahusay ang streaming error handling gamit ang chunk validation
  - Idinagdag ang mas mahusay na exception handling para sa service unavailability

- **session02/rag_pipeline.py**:
  - Idinagdag ang import guards para sa sentence-transformers na may installation hints
  - Pinahusay ang error handling para sa embedding at generation operations
  - Pinahusay ang output formatting gamit ang structured results

- **session02/rag_eval_ragas.py**:
  - Protektado ang optional imports (ragas, datasets) na may user-friendly error messages
  - Idinagdag ang error handling para sa evaluation metrics
  - Pinahusay ang output formatting para sa evaluation results

- **session03/benchmark_oss_models.py**:
  - Nagpatupad ng graceful degradation (nagpapatuloy sa model failures)
  - Idinagdag ang detalyadong progress reporting at per-model error handling
  - Pinahusay ang statistics calculation gamit ang komprehensibong error recovery

- **session04/model_compare.py**:
  - Idinagdag ang type hints (Tuple return types)
  - Pinahusay ang output formatting gamit ang structured JSON results
  - Nagpatupad ng per-model error handling na may recovery

- **session05/agents_orchestrator.py**:
  - Pinahusay ang Agent.act() gamit ang komprehensibong docstrings
  - Idinagdag ang pipeline error handling na may stage-by-stage logging
  - Pinahusay ang memory management at state tracking

- **session06/models_router.py**:
  - Pinahusay ang dokumentasyon ng function para sa lahat ng routing components
  - Idinagdag ang detalyadong logging sa route() function
  - Pinahusay ang test output gamit ang structured results

- **session06/models_pipeline.py**:
  - Idinagdag ang error handling sa chat() helper function
  - Pinahusay ang pipeline() gamit ang stage logging at progress reporting
  - Pinahusay ang main() gamit ang komprehensibong error recovery

### Dokumentasyon - Workshop Documentation Enhancement
- In-update ang pangunahing README.md na may seksyon ng Workshop na nagha-highlight ng hands-on learning path
- Pinahusay ang STUDY_GUIDE.md na may komprehensibong seksyon ng Workshop kabilang ang:
  - Mga learning objectives at mga pokus na lugar ng pag-aaral
  - Mga tanong sa self-assessment
  - Mga hands-on exercises na may time estimates
  - Time allocation para sa concentrated at part-time study
  - Idinagdag ang Workshop sa progress tracking template
- In-update ang time allocation guide mula 20 oras patungo sa 30 oras (kasama ang Workshop)
- Idinagdag ang mga deskripsyon ng Workshop sample at mga learning outcomes sa README

### Naayos
- Naresolba ang hindi pare-parehong mga pattern ng error handling sa mga Workshop samples
- Naayos ang mga error sa optional dependency import gamit ang tamang guards
- Na-correct ang mga nawawalang type hints sa mga critical functions
- Tinugunan ang hindi sapat na user feedback sa mga error scenarios
- Naayos ang mga validation issues gamit ang komprehensibong testing infrastructure

---

## 2025-09-23

### Binago - Major Module 08 Modernization
- **Komprehensibong alignment sa mga pattern ng Microsoft Foundry-Local repository**
  - In-update ang lahat ng halimbawa ng code upang gumamit ng modernong `FoundryLocalManager` at OpenAI SDK integration
  - Pinalitan ang deprecated manual `requests` calls gamit ang tamang SDK usage
  - In-align ang mga pattern ng implementasyon sa opisyal na dokumentasyon at mga halimbawa ng Microsoft

- **05.AIPoweredAgents.md modernization**:
  - In-update ang multi-agent orchestration upang gumamit ng modernong SDK patterns
  - Pinahusay ang coordinator implementation gamit ang advanced features (feedback loops, performance monitoring)
  - Idinagdag ang komprehensibong error handling at service health checking
  - In-integrate ang tamang mga reference sa local samples (`samples/05/multi_agent_orchestration.ipynb`)
  - In-update ang mga halimbawa ng function calling upang gumamit ng modernong `tools` parameter sa halip na deprecated `functions`
  - Idinagdag ang mga pattern na handa sa produksyon na may monitoring at statistics tracking

- **06.ModelsAsTools.md kumpletong rewrite**:
  - Pinalitan ang basic tool registry gamit ang intelligent model router implementation
  - Idinagdag ang keyword-based model selection para sa iba't ibang uri ng task (general, reasoning, code, creative)
  - In-integrate ang environment-based configuration na may flexible model assignment
  - Pinahusay gamit ang komprehensibong service health monitoring at error handling
  - Idinagdag ang mga pattern ng deployment sa produksyon na may request monitoring at performance tracking
  - In-align sa local implementation sa `samples/06/router.py` at `samples/06/model_router.ipynb`

- **Mga pagpapabuti sa istruktura ng dokumentasyon**:
  - Idinagdag ang mga overview sections na nagha-highlight ng modernization at SDK alignment
  - Pinahusay gamit ang emojis at mas magandang formatting para sa mas mahusay na readability
  - Idinagdag ang tamang mga reference sa local sample files sa buong dokumentasyon
  - Isinama ang mga gabay sa implementasyon na handa sa produksyon at best practices

### Idinagdag
- Komprehensibong overview sections sa mga file ng Module 08 na nagha-highlight ng modern SDK integration
- Mga highlight ng arkitektura na nagpapakita ng advanced features (multi-agent systems, intelligent routing)
- Direktang mga reference sa local sample implementations para sa hands-on experience
- Mga gabay sa deployment sa produksyon na may monitoring at error handling patterns
- Mga interactive na halimbawa ng Jupyter notebook na may advanced features at benchmarks

### Naayos
- Mga discrepancies sa alignment sa pagitan ng dokumentasyon at aktwal na mga sample implementations
- Mga outdated SDK usage patterns sa buong Module 08
- Mga nawawalang reference sa komprehensibong local sample library
- Hindi pare-parehong mga approach sa implementasyon sa iba't ibang seksyon

---

## 2025-09-18

### Idinagdag
- Module 08: Microsoft Foundry Local – Kumpletong Developer Toolkit
  - Anim na session: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, at models-as-tools
- Mga sample na maaaring patakbuhin sa ilalim ng `Module08/samples/01`–`06` gamit ang mga Windows cmd na utos
  - `01` REST mabilisang chat (`chat_quickstart.py`)
  - `02` SDK mabilisang simula gamit ang OpenAI/Foundry Local at Azure OpenAI support (`sdk_quickstart.py`)
  - `03` CLI listahan-at-benchmark (`list_and_bench.cmd`)
  - `04` Chainlit demo (`app.py`)
  - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
  - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support sa Session 2 SDK sample gamit ang environment variable configuration
- `.vscode/settings.json` upang ituro sa `Module08/.venv` at mapabuti ang Python analysis resolution
- `.env` na may `PYTHONPATH` na hint para sa VS Code/Pylance awareness

### Binago
- Ang default na modelo ay na-update sa `phi-4-mini` sa lahat ng Module 08 na dokumento at mga sample; tinanggal ang natitirang mga banggit sa `phi-3.5` sa loob ng Module 08
- Mga pagpapabuti sa Router (`Module08/samples/06/router.py`):
  - Pagtuklas ng endpoint gamit ang `foundry service status` na may regex parsing
  - `/v1/models` health check sa pagsisimula
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Na-update ang mga requirements: `Module08/requirements.txt` ngayon ay kasama ang `openai` (kasama ang `requests`, `chainlit`)
- Nilinaw ang gabay sa Chainlit sample at nagdagdag ng troubleshooting; import resolution gamit ang workspace settings

### Naayos
- Naresolba ang mga isyu sa import:
  - Ang Router ay hindi na umaasa sa isang hindi umiiral na `utils` module; ang mga function ay in-line na
  - Ang Coordinator ay gumagamit ng relative import (`from .specialists import ...`) at tinatawag gamit ang module path
  - VS Code/Pylance configuration upang ma-resolve ang `chainlit` at mga package imports
- Naayos ang maliit na typo sa `STUDY_GUIDE.md` at nagdagdag ng Module 08 coverage

### Tinanggal
- Tinanggal ang hindi nagagamit na `Module08/infra/obs.py` at tinanggal ang walang laman na `infra/` directory; ang mga observability pattern ay nananatiling opsyonal sa mga dokumento

### Inilipat
- Pinagsama-sama ang mga demo ng Module 08 sa ilalim ng `Module08/samples` na may mga folder na naka-base sa session number
  - Inilipat ang Chainlit app sa `samples/04`
  - Inilipat ang mga agents sa `samples/05` at nagdagdag ng mga `__init__.py` file para sa package resolution

### Dokumento
- Ang mga dokumento ng session ng Module 08 at lahat ng sample READMEs ay pinayaman ng mga Microsoft Learn at mga pinagkakatiwalaang vendor na reference
- Na-update ang `Module08/README.md` na may Samples Overview, router configuration, at validation tips
- Na-validate ang seksyon ng Windows Foundry Local sa `Module07/README.md` laban sa Learn docs
- Na-update ang `STUDY_GUIDE.md`:
  - Idinagdag ang Module 08 sa overview, schedules, progress tracker
  - Idinagdag ang komprehensibong seksyon ng References (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Kasaysayan (buod)
- Itinatag ang arkitektura ng kurso at mga module (Modules 01–07)
- Iterative na modernisasyon ng nilalaman, standardisasyon ng formatting, at pagdaragdag ng mga case study
- Pinalawak ang saklaw ng optimization frameworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Hindi Pa Nailalabas / Backlog (mga panukala)
- Opsyonal na smoke tests kada sample upang i-validate ang Foundry Local availability
- Suriin ang mga pagsasalin upang i-align ang mga reference ng modelo (hal., `phi-4-mini`) kung naaangkop
- Magdagdag ng minimal na pyright config kung mas gusto ng mga team ang workspace-wide strictness

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.