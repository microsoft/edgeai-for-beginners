# Changelog

All notable changes to EdgeAI for Beginners are documented here. This project uses date-based entries and the Keep a Changelog style (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-10-30

### Added - Module06 AI Agents Comprehensive Enhancement
- **Microsoft Agent Framework Integration** (`Module06/01.IntroduceAgent.md`):
  - Complete section on Microsoft Agent Framework for production-ready agent development
  - Detailed integration patterns with Foundry Local for edge deployment
  - Multi-agent orchestration examples with specialized SLM models
  - Enterprise deployment patterns with resource management and monitoring
  - Security and compliance features for edge agent systems
  - Real-world implementation examples (retail, healthcare, customer service)

- **Production SLM Agent Deployment Strategies**:
  - **Foundry Local**: Complete enterprise-grade edge AI runtime documentation with installation, configuration, and production patterns
  - **Ollama**: Enhanced community-focused deployment with comprehensive monitoring and model management
  - **VLLM**: High-performance inference engine with advanced optimization techniques and enterprise features
  - Production deployment checklists and comparison tables for all three platforms

- **Edge-Optimized SLM Frameworks Enhancement**:
  - **ONNX Runtime**: New comprehensive section for cross-platform SLM agent deployment
  - Universal deployment patterns across Windows, Linux, macOS, iOS, and Android
  - Hardware acceleration options (CPU, GPU, NPU) with automatic detection
  - Production-ready features and agent-specific optimizations
  - Complete implementation examples with Microsoft Agent Framework integration

- **References and Further Reading**:
  - Comprehensive resource library with 100+ authoritative sources
  - Core research papers on AI agents and Small Language Models
  - Official documentation for all major frameworks and tools
  - Industry reports, market analysis, and technical benchmarks
  - Educational resources, conferences, and community forums
  - Standards, specifications, and compliance frameworks

### Changed - Module06 Content Modernization
- **Enhanced Learning Objectives**: Added Microsoft Agent Framework mastery and edge deployment capabilities
- **Production Focus**: Shifted from conceptual to implementation-ready guidance with production examples
- **Code Examples**: Updated all examples to use modern SDK patterns and best practices
- **Architecture Patterns**: Added hierarchical agent architectures and edge-to-cloud coordination
- **Performance Optimization**: Enhanced with resource management and auto-scaling recommendations

### Docs - Module06 Structure Enhancement
- **Comprehensive Agent Framework Coverage**: From basic concepts to enterprise deployment
- **Production Deployment Strategies**: Complete guides for Foundry Local, Ollama, and VLLM
- **Cross-Platform Optimization**: Added ONNX Runtime for universal deployment
- **Resource Library**: Extensive references for continued learning and implementation

### Added - Module06 Model Context Protocol (MCP) Documentation Update
- **MCP Introduction Modernization** (`Module06/03.IntroduceMCP.md`):
  - Updated with latest MCP specifications from modelcontextprotocol.io (2025-06-18 version)
  - Added official USB-C analogy for standardized AI application connections
  - Updated architecture section with official two-layer design (Data Layer + Transport Layer)
  - Enhanced core primitives documentation with server primitives (Tools, Resources, Prompts) and client primitives (Sampling, Elicitation, Logging)

- **Comprehensive MCP References and Resources**:
  - Added **MCP for Beginners** link (https://aka.ms/mcp-for-beginners) 
  - Official MCP documentation and specifications (modelcontextprotocol.io)
  - Development resources including MCP Inspector and reference implementations
  - Technical standards (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Added - Module04 Qualcomm QNN Integration
- **New Section 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Comprehensive 400+ line guide covering Qualcomm's unified AI inference framework
  - Detailed coverage of heterogeneous computing (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardware-aware optimization for Snapdragon platforms with intelligent workload distribution
  - Advanced quantization techniques (INT8, INT16, mixed-precision) for mobile deployment
  - Power-efficient inference optimization for battery-powered devices and real-time applications
  - Complete installation guide with QNN SDK setup and environment configuration
  - Practical examples: PyTorch to QNN conversion, multi-backend optimization, context binary generation
  - Advanced usage patterns: custom backend configuration, dynamic quantization, performance profiling
  - Comprehensive troubleshooting section and community resources

- **Enhanced Module04 structure**:
  - Updated README.md to include 7 progressive sections (was 6)
  - Added Qualcomm QNN to performance benchmarks table (5-15x speed improvement, 50-80% memory reduction)
  - Comprehensive learning outcomes for mobile AI deployment and power optimization

### Changed - Module04 Documentation Updates
- **Microsoft Olive documentation enhancement** (`Module04/03.MicrosoftOlive.md`):
  - Added comprehensive "Olive Recipes Repository" section covering 100+ pre-built optimization recipes
  - Detailed coverage of supported model families (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Practical usage examples for recipe customization and community contributions
  - Enhanced with performance benchmarks and integration guidance

- **Section reordering in Module04**:
  - Apple MLX moved to Section 5 (was Section 6)
  - Workflow Synthesis moved to Section 6 (was Section 7)  
  - Qualcomm QNN positioned as Section 7 (specialized mobile/edge focus)
  - Updated all file references and navigation links accordingly

### Fixed - Workshop Sample Validation
- **chat_bootstrap.py validation and repair**:
  - Fixed corrupted import statement (`util.util.workshop_utils` → `util.workshop_utils`)
  - Created missing `__init__.py` in util package for proper Python module resolution
  - Installed required dependencies (openai, foundry-local-sdk) in conda environment
  - Successfully validated sample execution with both default and custom prompts
  - Confirmed integration with Foundry Local service and model loading (phi-4-mini with CUDA optimization)

### Docs - Comprehensive Guide Updates
- **Module04 README.md complete restructure**:
  - Added Qualcomm QNN as major optimization framework alongside OpenVINO, Olive, MLX
  - Updated chapter learning outcomes to include mobile AI deployment and power optimization
  - Enhanced performance comparison table with QNN metrics and mobile/edge use cases
  - Maintained logical progression from enterprise solutions to platform-specific optimizations

- **Cross-references and navigation**:
  - Updated all internal links and file references for new section numbering
  - Enhanced workflow synthesis description to include mobile, desktop, and cloud environments
  - Added comprehensive resource links for Qualcomm developer ecosystem

## 2025-10-08

### Added - Workshop Comprehensive Update
- **Workshop README.md complete rewrite**:
  - Added comprehensive introduction explaining Edge AI value proposition (privacy, performance, cost)
  - Created 6 core learning objectives with detailed competencies
  - Added learning outcomes table with deliverables and competency matrix
  - Included career-ready skills section for industry relevance
  - Added quick start guide with prerequisites and 3-step setup
  - Created resource tables for Python samples (8 files with run times)
  - Added Jupyter notebooks table (8 notebooks with difficulty ratings)
  - Created documentation table (7 key docs with "Use When" guidance)
  - Added learning path recommendations for different skill levels

- **Workshop validation and testing infrastructure**:
  - Created `scripts/validate_samples.py` - Comprehensive validation tool for syntax, imports, and best practices
  - Created `scripts/test_samples.py` - Smoke test runner for all Python samples
  - Added validation documentation to `scripts/README.md`

- **Comprehensive documentation**:
  - Created `SAMPLES_UPDATE_SUMMARY.md` - 400+ line detailed guide covering all improvements
  - Created `UPDATE_COMPLETE.md` - Executive summary of update completion
  - Created `QUICK_REFERENCE.md` - Quick reference card for Workshop

### Changed - Workshop Python Sample Modernization
- **All 8 Python samples updated with best practices**:
  - Enhanced error handling with try-except blocks around all I/O operations
  - Added type hints and comprehensive docstrings
  - Implemented consistent [INFO]/[ERROR]/[RESULT] logging pattern
  - Protected optional imports with installation hints
  - Improved user feedback throughout all samples

- **session01/chat_bootstrap.py**:
  - Enhanced client initialization with comprehensive error messages
  - Improved streaming error handling with chunk validation
  - Added better exception handling for service unavailability

- **session02/rag_pipeline.py**:
  - Added import guards for sentence-transformers with installation hints
  - Enhanced error handling for embedding and generation operations
  - Improved output formatting with structured results

- **session02/rag_eval_ragas.py**:
  - Protected optional imports (ragas, datasets) with user-friendly error messages
  - Added error handling for evaluation metrics
  - Enhanced output formatting for evaluation results

- **session03/benchmark_oss_models.py**:
  - Implemented graceful degradation (continues on model failures)
  - Added detailed progress reporting and per-model error handling
  - Enhanced statistics calculation with comprehensive error recovery

- **session04/model_compare.py**:
  - Added type hints (Tuple return types)
  - Enhanced output formatting with structured JSON results
  - Implemented per-model error handling with recovery

- **session05/agents_orchestrator.py**:
  - Enhanced Agent.act() with comprehensive docstrings
  - Added pipeline error handling with stage-by-stage logging
  - Improved memory management and state tracking

- **session06/models_router.py**:
  - Enhanced function documentation for all routing components
  - Added detailed logging in route() function
  - Improved test output with structured results

- **session06/models_pipeline.py**:
  - Added error handling to chat() helper function
  - Enhanced pipeline() with stage logging and progress reporting
  - Improved main() with comprehensive error recovery

### Docs - Workshop Documentation Enhancement
- Updated main README.md with Workshop section highlighting hands-on learning path
- Enhanced STUDY_GUIDE.md with comprehensive Workshop section including:
  - Learning objectives and study focus areas
  - Self-assessment questions
  - Hands-on exercises with time estimates
  - Time allocation for concentrated and part-time study
  - Added Workshop to progress tracking template
- Updated time allocation guide from 20 hours to 30 hours (including Workshop)
- Added Workshop sample descriptions and learning outcomes to README

### Fixed
- Resolved inconsistent error handling patterns across Workshop samples
- Fixed optional dependency import errors with proper guards
- Corrected missing type hints in critical functions
- Addressed insufficient user feedback in error scenarios
- Fixed validation issues with comprehensive testing infrastructure

---

## 2025-09-23

### Changed - Major Module 08 Modernization
- **Comprehensive alignment with Microsoft Foundry-Local repository patterns**
  - Updated all code examples to use modern `FoundryLocalManager` and OpenAI SDK integration
  - Replaced deprecated manual `requests` calls with proper SDK usage
  - Aligned implementation patterns with official Microsoft documentation and samples

- **05.AIPoweredAgents.md modernization**:
  - Updated multi-agent orchestration to use modern SDK patterns
  - Enhanced coordinator implementation with advanced features (feedback loops, performance monitoring)
  - Added comprehensive error handling and service health checking
  - Integrated proper references to local samples (`samples/05/multi_agent_orchestration.ipynb`)
  - Updated function calling examples to use modern `tools` parameter instead of deprecated `functions`
  - Added production-ready patterns with monitoring and statistics tracking

- **06.ModelsAsTools.md complete rewrite**:
  - Replaced basic tool registry with intelligent model router implementation
  - Added keyword-based model selection for different task types (general, reasoning, code, creative)
  - Integrated environment-based configuration with flexible model assignment
  - Enhanced with comprehensive service health monitoring and error handling
  - Added production deployment patterns with request monitoring and performance tracking
  - Aligned with local implementation in `samples/06/router.py` and `samples/06/model_router.ipynb`

- **Documentation structure improvements**:
  - Added overview sections highlighting modernization and SDK alignment
  - Enhanced with emojis and better formatting for improved readability
  - Added proper references to local sample files throughout documentation
  - Included production-ready implementation guidance and best practices

### Added
- Comprehensive overview sections in Module 08 files highlighting modern SDK integration
- Architecture highlights showcasing advanced features (multi-agent systems, intelligent routing)
- Direct references to local sample implementations for hands-on experience
- Production deployment guidance with monitoring and error handling patterns
- Interactive Jupyter notebook examples with advanced features and benchmarks

### Fixed
- Alignment discrepancies between documentation and actual sample implementations
- Outdated SDK usage patterns throughout Module 08
- Missing references to comprehensive local sample library
- Inconsistent implementation approaches across different sections

---

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Complete Developer Toolkit
  - Six sessions: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, and models-as-tools
  - Runnable samples under `Module08/samples/01`–`06` with Windows cmd instructions
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart with OpenAI/Foundry Local and Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support in Session 2 SDK sample with environment variable configuration
- `.vscode/settings.json` to point to `Module08/.venv` and improve Python analysis resolution
- `.env` with `PYTHONPATH` hint for VS Code/Pylance awareness

### Changed
- Default model updated to `phi-4-mini` across Module 08 docs and samples; removed remaining `phi-3.5` mentions within Module 08
- Router (`Module08/samples/06/router.py`) improvements:
  - Endpoint discovery via `foundry service status` with regex parsing
  - `/v1/models` health check on startup
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requirements updated: `Module08/requirements.txt` now includes `openai` (alongside `requests`, `chainlit`)
- Chainlit sample guidance clarified and troubleshooting added; import resolution via workspace settings

### Fixed
- Resolved import issues:
  - Router no longer depends on a non-existent `utils` module; functions are inlined
  - Coordinator uses relative import (`from .specialists import ...`) and is invoked via module path
  - VS Code/Pylance configuration to resolve `chainlit` and package imports
- Corrected minor typo in `STUDY_GUIDE.md` and added Module 08 coverage

### Removed
- Deleted unused `Module08/infra/obs.py` and removed the empty `infra/` directory; observability patterns retained as optional in docs

### Moved
- Consolidated Module 08 demos under `Module08/samples` with session-numbered folders
  - Moved Chainlit app to `samples/04`
  - Moved agents to `samples/05` and added `__init__.py` files for package resolution

### Docs
- Module 08 session docs and all sample READMEs enriched with Microsoft Learn and trusted vendor references
- `Module08/README.md` updated with Samples Overview, router configuration, and validation tips
- `Module07/README.md` Windows Foundry Local section validated against Learn docs
- `STUDY_GUIDE.md` updated:
  - Added Module 08 to overview, schedules, progress tracker
  - Added comprehensive References section (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Course architecture and modules established (Modules 01–07)
- Iterative content modernization, formatting standardization, and added case studies
- Expanded optimization frameworks coverage (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Optional per-sample smoke tests to validate Foundry Local availability
- Review translations to align model references (e.g., `phi-4-mini`) where appropriate
- Add minimal pyright config if teams prefer workspace-wide strictness
