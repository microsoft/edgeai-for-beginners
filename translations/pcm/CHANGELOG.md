<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-11-11T17:16:14+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "pcm"
}
-->
# Changelog

All di beta wey don change for EdgeAI for Beginners dey here. Dis project dey use date-based entries and di Keep a Changelog style (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-10-30

### Added - Module06 AI Agents Comprehensive Enhancement
- **Microsoft Agent Framework Integration** (`Module06/01.IntroduceAgent.md`):
  - Full section wey explain Microsoft Agent Framework for agents wey fit work for production
  - Detailed integration patterns wit Foundry Local for edge deployment
  - Multi-agent orchestration examples wit special SLM models
  - Enterprise deployment patterns wit resource management and monitoring
  - Security and compliance features for edge agent systems
  - Real-life examples (retail, healthcare, customer service)

- **Production SLM Agent Deployment Strategies**:
  - **Foundry Local**: Full enterprise-grade edge AI runtime documentation wit installation, configuration, and production patterns
  - **Ollama**: Better community-focused deployment wit full monitoring and model management
  - **VLLM**: High-performance inference engine wit advanced optimization techniques and enterprise features
  - Production deployment checklists and comparison tables for di three platforms

- **Edge-Optimized SLM Frameworks Enhancement**:
  - **ONNX Runtime**: New full section for cross-platform SLM agent deployment
  - Universal deployment patterns for Windows, Linux, macOS, iOS, and Android
  - Hardware acceleration options (CPU, GPU, NPU) wit automatic detection
  - Production-ready features and agent-specific optimizations
  - Full implementation examples wit Microsoft Agent Framework integration

- **References and Further Reading**:
  - Full resource library wit 100+ correct sources
  - Core research papers on AI agents and Small Language Models
  - Official documentation for all di major frameworks and tools
  - Industry reports, market analysis, and technical benchmarks
  - Educational resources, conferences, and community forums
  - Standards, specifications, and compliance frameworks

### Changed - Module06 Content Modernization
- **Better Learning Objectives**: Add Microsoft Agent Framework mastery and edge deployment capabilities
- **Production Focus**: Change from concept to implementation-ready guidance wit production examples
- **Code Examples**: Update all examples to use modern SDK patterns and best practices
- **Architecture Patterns**: Add hierarchical agent architectures and edge-to-cloud coordination
- **Performance Optimization**: Add resource management and auto-scaling recommendations

### Docs - Module06 Structure Enhancement
- **Full Agent Framework Coverage**: From basic concepts to enterprise deployment
- **Production Deployment Strategies**: Full guides for Foundry Local, Ollama, and VLLM
- **Cross-Platform Optimization**: Add ONNX Runtime for universal deployment
- **Resource Library**: Big references for continued learning and implementation

### Added - Module06 Model Context Protocol (MCP) Documentation Update
- **MCP Introduction Modernization** (`Module06/03.IntroduceMCP.md`):
  - Update wit latest MCP specifications from modelcontextprotocol.io (2025-06-18 version)
  - Add official USB-C analogy for standardized AI application connections
  - Update architecture section wit official two-layer design (Data Layer + Transport Layer)
  - Better core primitives documentation wit server primitives (Tools, Resources, Prompts) and client primitives (Sampling, Elicitation, Logging)

- **Full MCP References and Resources**:
  - Add **MCP for Beginners** link (https://aka.ms/mcp-for-beginners) 
  - Official MCP documentation and specifications (modelcontextprotocol.io)
  - Development resources including MCP Inspector and reference implementations
  - Technical standards (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Added - Module04 Qualcomm QNN Integration
- **New Section 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Full 400+ line guide wey cover Qualcomm unified AI inference framework
  - Detailed coverage of heterogeneous computing (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardware-aware optimization for Snapdragon platforms wit smart workload distribution
  - Advanced quantization techniques (INT8, INT16, mixed-precision) for mobile deployment
  - Power-efficient inference optimization for battery-powered devices and real-time applications
  - Full installation guide wit QNN SDK setup and environment configuration
  - Practical examples: PyTorch to QNN conversion, multi-backend optimization, context binary generation
  - Advanced usage patterns: custom backend configuration, dynamic quantization, performance profiling
  - Full troubleshooting section and community resources

- **Better Module04 structure**:
  - Update README.md to include 7 progressive sections (before na 6)
  - Add Qualcomm QNN to performance benchmarks table (5-15x speed improvement, 50-80% memory reduction)
  - Full learning outcomes for mobile AI deployment and power optimization

### Changed - Module04 Documentation Updates
- **Microsoft Olive documentation enhancement** (`Module04/03.MicrosoftOlive.md`):
  - Add full "Olive Recipes Repository" section wey cover 100+ pre-built optimization recipes
  - Detailed coverage of supported model families (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Practical usage examples for recipe customization and community contributions
  - Better wit performance benchmarks and integration guidance

- **Section reordering in Module04**:
  - Apple MLX move to Section 5 (before na Section 6)
  - Workflow Synthesis move to Section 6 (before na Section 7)  
  - Qualcomm QNN dey Section 7 (specialized mobile/edge focus)
  - Update all file references and navigation links as e suppose be

### Fixed - Workshop Sample Validation
- **chat_bootstrap.py validation and repair**:
  - Fix corrupted import statement (`util.util.workshop_utils` → `util.workshop_utils`)
  - Create missing `__init__.py` for util package to make Python module resolution correct
  - Install required dependencies (openai, foundry-local-sdk) for conda environment
  - Validate sample execution wit both default and custom prompts
  - Confirm integration wit Foundry Local service and model loading (phi-4-mini wit CUDA optimization)

### Docs - Full Guide Updates
- **Module04 README.md full restructure**:
  - Add Qualcomm QNN as major optimization framework alongside OpenVINO, Olive, MLX
  - Update chapter learning outcomes to include mobile AI deployment and power optimization
  - Better performance comparison table wit QNN metrics and mobile/edge use cases
  - Maintain logical progression from enterprise solutions to platform-specific optimizations

- **Cross-references and navigation**:
  - Update all internal links and file references for new section numbering
  - Better workflow synthesis description to include mobile, desktop, and cloud environments
  - Add full resource links for Qualcomm developer ecosystem

## 2025-10-08

### Added - Workshop Full Update
- **Workshop README.md full rewrite**:
  - Add full introduction wey explain Edge AI value proposition (privacy, performance, cost)
  - Create 6 core learning objectives wit detailed competencies
  - Add learning outcomes table wit deliverables and competency matrix
  - Include career-ready skills section for industry relevance
  - Add quick start guide wit prerequisites and 3-step setup
  - Create resource tables for Python samples (8 files wit run times)
  - Add Jupyter notebooks table (8 notebooks wit difficulty ratings)
  - Create documentation table (7 key docs wit "Use When" guidance)
  - Add learning path recommendations for different skill levels

- **Workshop validation and testing infrastructure**:
  - Create `scripts/validate_samples.py` - Full validation tool for syntax, imports, and best practices
  - Create `scripts/test_samples.py` - Smoke test runner for all Python samples
  - Add validation documentation to `scripts/README.md`

- **Full documentation**:
  - Create `SAMPLES_UPDATE_SUMMARY.md` - 400+ line detailed guide wey cover all improvements
  - Create `UPDATE_COMPLETE.md` - Executive summary of update completion
  - Create `QUICK_REFERENCE.md` - Quick reference card for Workshop

### Changed - Workshop Python Sample Modernization
- **All 8 Python samples update wit best practices**:
  - Better error handling wit try-except blocks around all I/O operations
  - Add type hints and full docstrings
  - Implement consistent [INFO]/[ERROR]/[RESULT] logging pattern
  - Protect optional imports wit installation hints
  - Better user feedback for all samples

- **session01/chat_bootstrap.py**:
  - Better client initialization wit full error messages
  - Better streaming error handling wit chunk validation
  - Add better exception handling for service unavailability

- **session02/rag_pipeline.py**:
  - Add import guards for sentence-transformers wit installation hints
  - Better error handling for embedding and generation operations
  - Better output formatting wit structured results

- **session02/rag_eval_ragas.py**:
  - Protect optional imports (ragas, datasets) wit user-friendly error messages
  - Add error handling for evaluation metrics
  - Better output formatting for evaluation results

- **session03/benchmark_oss_models.py**:
  - Implement graceful degradation (e go continue if model fail)
  - Add detailed progress reporting and per-model error handling
  - Better statistics calculation wit full error recovery

- **session04/model_compare.py**:
  - Add type hints (Tuple return types)
  - Better output formatting wit structured JSON results
  - Implement per-model error handling wit recovery

- **session05/agents_orchestrator.py**:
  - Better Agent.act() wit full docstrings
  - Add pipeline error handling wit stage-by-stage logging
  - Better memory management and state tracking

- **session06/models_router.py**:
  - Better function documentation for all routing components
  - Add detailed logging for route() function
  - Better test output wit structured results

- **session06/models_pipeline.py**:
  - Add error handling to chat() helper function
  - Better pipeline() wit stage logging and progress reporting
  - Better main() wit full error recovery

### Docs - Workshop Documentation Enhancement
- Update main README.md wit Workshop section wey highlight hands-on learning path
- Better STUDY_GUIDE.md wit full Workshop section including:
  - Learning objectives and study focus areas
  - Self-assessment questions
  - Hands-on exercises wit time estimates
  - Time allocation for concentrated and part-time study
  - Add Workshop to progress tracking template
- Update time allocation guide from 20 hours to 30 hours (including Workshop)
- Add Workshop sample descriptions and learning outcomes to README

### Fixed
- Solve inconsistent error handling patterns across Workshop samples
- Fix optional dependency import errors wit proper guards
- Correct missing type hints for important functions
- Address insufficient user feedback for error scenarios
- Fix validation issues wit full testing infrastructure

---

## 2025-09-23

### Changed - Major Module 08 Modernization
- **Full alignment wit Microsoft Foundry-Local repository patterns**
  - Update all code examples to use modern `FoundryLocalManager` and OpenAI SDK integration
  - Replace old manual `requests` calls wit correct SDK usage
  - Align implementation patterns wit official Microsoft documentation and samples

- **05.AIPoweredAgents.md modernization**:
  - Update multi-agent orchestration to use modern SDK patterns
  - Better coordinator implementation wit advanced features (feedback loops, performance monitoring)
  - Add full error handling and service health checking
  - Integrate correct references to local samples (`samples/05/multi_agent_orchestration.ipynb`)
  - Update function calling examples to use modern `tools` parameter instead of old `functions`
  - Add production-ready patterns wit monitoring and statistics tracking

- **06.ModelsAsTools.md full rewrite**:
  - Replace basic tool registry wit smart model router implementation
  - Add keyword-based model selection for different task types (general, reasoning, code, creative)
  - Integrate environment-based configuration wit flexible model assignment
  - Better wit full service health monitoring and error handling
  - Add production deployment patterns wit request monitoring and performance tracking
  - Align wit local implementation in `samples/06/router.py` and `samples/06/model_router.ipynb`

- **Documentation structure improvements**:
  - Add overview sections wey highlight modernization and SDK alignment
  - Better wit emojis and better formatting for easy reading
  - Add correct references to local sample files for di documentation
  - Include production-ready implementation guidance and best practices

### Added
- Full overview sections for Module 08 files wey highlight modern SDK integration
- Architecture highlights wey show advanced features (multi-agent systems, smart routing)
- Direct references to local sample implementations for hands-on experience
- Production deployment guidance wit monitoring and error handling patterns
- Interactive Jupyter notebook examples wit advanced features and benchmarks

### Fixed
- Alignment problems between documentation and di actual sample implementations
- Old SDK usage patterns for Module 08
- Missing references to full local sample library
- Inconsistent implementation approaches across different sections

---

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Full Developer Toolkit
  - Six sessions: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, and models-as-tools
  - Samples wey you fit run dey under `Module08/samples/01`–`06` wit Windows cmd instructions
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart wey support OpenAI/Foundry Local and Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support dey for Session 2 SDK sample wit environment variable configuration
- `.vscode/settings.json` dey point to `Module08/.venv` to make Python analysis better
- `.env` get `PYTHONPATH` hint for VS Code/Pylance awareness

### Changed
- Default model don change to `phi-4-mini` for all Module 08 docs and samples; dem don remove all `phi-3.5` mentions wey still dey Module 08
- Router (`Module08/samples/06/router.py`) don get better:
  - E dey find endpoint wit `foundry service status` wey dey use regex parsing
  - `/v1/models` health check dey run when e start
  - Model registry wey fit configure wit environment (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requirements don update: `Module08/requirements.txt` now dey include `openai` (join `requests`, `chainlit`)
- Chainlit sample guide don clear well and dem add troubleshooting; import resolution dey use workspace settings

### Fixed
- Import issues don resolve:
  - Router no dey depend on `utils` module wey no dey exist again; dem don put functions inside
  - Coordinator dey use relative import (`from .specialists import ...`) and e dey run wit module path
  - VS Code/Pylance configuration don dey resolve `chainlit` and package imports
- Dem correct small typo for `STUDY_GUIDE.md` and dem add Module 08 coverage

### Removed
- Dem don delete `Module08/infra/obs.py` wey no dey use and dem remove empty `infra/` folder; observability patterns still dey optional for docs

### Moved
- Module 08 demos don dey one place under `Module08/samples` wit session-numbered folders
  - Dem move Chainlit app go `samples/04`
  - Dem move agents go `samples/05` and dem add `__init__.py` files for package resolution

### Docs
- Module 08 session docs and all sample READMEs don get better wit Microsoft Learn and trusted vendor references
- `Module08/README.md` don update wit Samples Overview, router configuration, and validation tips
- `Module07/README.md` Windows Foundry Local section don validate wit Learn docs
- `STUDY_GUIDE.md` don update:
  - Dem add Module 08 to overview, schedules, progress tracker
  - Dem add full References section (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Course architecture and modules don dey set (Modules 01–07)
- Dem dey modernize content small small, dey standardize formatting, and dey add case studies
- Dem don expand optimization frameworks coverage (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Optional smoke tests for each sample to check Foundry Local availability
- Review translations to make sure model references (e.g., `phi-4-mini`) dey correct
- Add small pyright config if teams wan workspace-wide strictness

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important mata, e good make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->