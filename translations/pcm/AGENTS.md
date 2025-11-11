<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-11-11T17:17:44+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pcm"
}
-->
# AGENTS.md

> **Developer Guide wey go help you contribute to EdgeAI for Beginners**
> 
> Dis document dey give full gist for developers, AI agents, and people wey wan contribute for dis repository. E cover setup, how to dey work on am, testing, and better ways to do am.
> 
> **Last Update**: October 30, 2025 | **Document Version**: 3.0

## Table of Contents

- [Project Overview](../..)
- [Repository Structure](../..)
- [Prerequisites](../..)
- [Setup Commands](../..)
- [Development Workflow](../..)
- [Testing Instructions](../..)
- [Code Style Guidelines](../..)
- [Pull Request Guidelines](../..)
- [Translation System](../..)
- [Foundry Local Integration](../..)
- [Build and Deployment](../..)
- [Common Issues and Troubleshooting](../..)
- [Additional Resources](../..)
- [Project-Specific Notes](../..)
- [Getting Help](../..)

## Project Overview

EdgeAI for Beginners na one educational repository wey dey teach Edge AI development with Small Language Models (SLMs). Di course dey cover EdgeAI basics, how to deploy model, optimization techniques, and how to use am for production with Microsoft Foundry Local and different AI frameworks.

**Key Technologies:**
- Python 3.8+ (na di main language for AI/ML samples)
- .NET C# (AI/ML Samples)
- JavaScript/Node.js with Electron (for desktop applications)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI Frameworks: LangChain, Semantic Kernel, Chainlit
- Model Optimization: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository Type:** Educational content repository wey get 8 modules and 10 full sample applications

**Architecture:** Multi-module learning path wey dey show practical samples for how to deploy edge AI

## Repository Structure

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Prerequisites

### Tools wey you need

- **Python 3.8+** - For AI/ML samples and notebooks
- **Node.js 16+** - For Electron sample application
- **Git** - For version control
- **Microsoft Foundry Local** - To run AI models for your system

### Tools wey go make your work easy

- **Visual Studio Code** - With Python, Jupyter, and Pylance extensions
- **Windows Terminal** - For better command-line experience (Windows users)
- **Docker** - For containerized development (optional)

### System Requirements

- **RAM**: At least 8GB, but 16GB+ go better for multi-model work
- **Storage**: At least 10GB free space for models and dependencies
- **OS**: Windows 10/11, macOS 11+, or Linux (Ubuntu 20.04+)
- **Hardware**: CPU wey get AVX2 support; GPU (CUDA, Qualcomm NPU) optional but e go help

### Knowledge wey you need

- Small knowledge of Python programming
- Know how to use command-line
- Understand AI/ML concepts (to work on samples)
- Know how Git workflows and pull request dey work

## Setup Commands

### Repository Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python Sample Setup (Module08 and Workshop samples)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Node.js Sample Setup (Sample 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local Setup

Foundry Local na wetin you need to run di samples. Download and install am from di official repository:

**Installation:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: Download from [releases page](https://github.com/microsoft/Foundry-Local/releases)

**Quick Start:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Note**: Foundry Local dey automatically choose di best model variant for your hardware (CUDA GPU, Qualcomm NPU, or CPU).

## Development Workflow

### Content Development

Dis repository na mainly **Markdown educational content**. If you wan make changes:

1. Edit `.md` files for di correct module directories
2. Follow di formatting wey dey already dey
3. Make sure say di code examples dey correct and dem don test am
4. Update di translated content if e dey necessary (or make automation handle am)

### Sample Application Development

For Module08 Python samples (samples 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

For Workshop Python samples:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

For Electron sample (sample 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testing Sample Applications

Python samples no get automated tests but you fit validate am by running dem:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron sample get test infrastructure:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testing Instructions

### Content Validation

Di repository dey use automated translation workflows. No need manual testing for translations.

**Manual validation for content changes:**
1. Check how Markdown dey render by previewing `.md` files
2. Make sure say all links dey go correct place
3. Test any code snippets wey dey inside di documentation
4. Confirm say images dey load well

### Sample Application Testing

**Module08/samples/08 (Electron app) get full testing:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python samples suppose dey test manually:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Code Style Guidelines

### Markdown Content

- Use di same heading hierarchy (# for title, ## for main sections, ### for subsections)
- Add code blocks with language specifiers: ```python, ```bash, ```javascript
- Follow di formatting wey dey already dey for tables, lists, and emphasis
- Make lines dey readable (aim for ~80-100 characters, but no strict)
- Use relative links for internal references

### Python Code Style

- Follow PEP 8 rules
- Use type hints if e dey necessary
- Add docstrings for functions and classes
- Use better variable names
- Make functions dey focused and short

### JavaScript/Node.js Code Style

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Key rules:**
- ESLint configuration dey for sample 08
- Prettier for code formatting
- Use modern ES6+ syntax
- Follow di patterns wey dey di codebase

## Pull Request Guidelines

### Contribution Workflow

1. **Fork di repository** and create new branch from `main`
2. **Make your changes** follow di code style guidelines
3. **Test well well** using di testing instructions wey dey above
4. **Commit with clear messages** follow conventional commits format
5. **Push to your fork** and create pull request
6. **Answer feedback** from maintainers during review

### Branch Naming Convention

- `feature/<module>-<description>` - For new features or content
- `fix/<module>-<description>` - For bug fixes
- `docs/<description>` - For documentation improvements
- `refactor/<description>` - For code refactoring

### Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Examples:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Title Format
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### Code of Conduct

All contributors must follow di [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Abeg check [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before you contribute.

### Before Submitting

**For content changes:**
- Preview all di Markdown files wey you change
- Confirm say links and images dey work
- Check for typos and grammar errors

**For sample code changes (Module08/samples/08):**
```bash
npm run lint
npm test
```

**For Python sample changes:**
- Test say di sample dey run well
- Confirm say error handling dey work
- Check say e dey compatible with Foundry Local

### Review Process

- Educational content changes go dey check for accuracy and clarity
- Code samples go dey test for functionality
- Translation updates go dey handle automatically by GitHub Actions

## Translation System

**IMPORTANT:** Dis repository dey use automated translation via GitHub Actions.

- Translations dey for `/translations/` directory (50+ languages)
- Automation dey via `co-op-translator.yml` workflow
- **NO TOUCH translation files manually** - dem go dey overwrite
- Edit only English source files for root and module directories
- Translations go dey automatically generate when you push to `main` branch

## Foundry Local Integration

Most Module08 samples need Microsoft Foundry Local to dey run.

### Installation & Setup

**Install Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Install Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Starting Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK Usage (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Verifying Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Environment Variables for Samples

Most samples dey use dis environment variables:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Note**: If you dey use `FoundryLocalManager`, di SDK go automatically handle service discovery and model loading. Model aliases (like `phi-3.5-mini`) go make sure say di best variant dey select for your hardware.

## Build and Deployment

### Content Deployment

Dis repository na mainly documentation - no need build process for content.

### Sample Application Building

**Electron Application (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python Samples:**
No build process - samples dey run directly with Python interpreter.

## Common Issues and Troubleshooting

> **Tip**: Check [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) for known problems and solutions.

### Critical Issues (Blocking)

#### Foundry Local No Dey Run
**Issue:** Samples dey fail with connection errors

**Solution:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Common Issues (Moderate)

#### Python Virtual Environment Wahala
**Issue:** Module import errors

**Solution:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron Build Wahala
**Issue:** npm install or build dey fail

**Solution:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Workflow Wahala (Minor)

#### Translation Workflow Conflicts
**Issue:** Translation PR dey conflict with your changes

**Solution:**
- Edit only English source files
- Make di automated translation workflow handle translations
- If conflicts dey, merge `main` into your branch after translations don merge

#### Model Download Wahala
**Issue:** Foundry Local dey fail to download models

**Solution:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Additional Resources

### Learning Paths
- **Beginner Path:** Modules 01-02 (7-9 hours)
- **Intermediate Path:** Modules 03-04 (9-11 hours)
- **Advanced Path:** Modules 05-07 (12-15 hours)
- **Expert Path:** Module 08 (8-10 hours)
- **Hands-On Workshop:** Workshop materials (6-8 hours)

### Key Module Content
- **Module01:** EdgeAI basics and real-world case studies
- **Module02:** Small Language Model (SLM) families and architectures
- **Module03:** Local and cloud deployment strategies
- **Module04:** Model optimization with different frameworks (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - production operations
- **Module06:** AI agents and function calling
- **Module07:** Platform-specific implementations
- **Module08:** Foundry Local toolkit with 10 full samples

### External Dependencies
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Local AI model runtime with OpenAI-compatible API
  - [Documentation](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimization framework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Model optimization toolkit
- [OpenVINO](https://docs.openvino.ai/) - Intel's optimization toolkit

## Project-Specific Notes

### Module08 Sample Applications

Di repository get 10 full sample applications:

1. **01-REST Chat Quickstart** - Basic OpenAI SDK integration
2. **02-OpenAI SDK Integration** - Advanced SDK features
3. **03-Model Discovery & Benchmarking** - Model comparison tools
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - Basic agent coordination
6. **06-Models-as-Tools Router** - Intelligent model routing
7. **07-Direct API Client** - Low-level API integration
8. **08-Windows 11 Chat App** - Native Electron desktop application
9. **09-Advanced Multi-Agent System** - Complex agent orchestration
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel integration

### Workshop Sample Applications

Di Workshop get 6 sessions wey dey progress step by step wit practical examples:

1. **Session 01** - Chat setup wit Foundry Local integration
2. **Session 02** - RAG pipeline and evaluation wit RAGAS
3. **Session 03** - Test open-source models performance
4. **Session 04** - Compare and choose model
5. **Session 05** - Multi-agent orchestration systems
6. **Session 06** - Model routing and pipeline management

Each example dey show different parts of edge AI development wit Foundry Local.

### Performance Considerations

- SLMs don dey optimized for edge deployment (2-16GB RAM)
- Local inference dey give 50-500ms response time
- Quantization techniques fit reduce size by 75% and still keep 85% performance
- E fit do real-time conversation wit local models

### Security and Privacy

- All processing dey happen for local - no data dey go cloud
- E good for applications wey need privacy (healthcare, finance)
- E dey meet data sovereignty requirements
- Foundry Local dey run completely for local hardware

## Getting Help

### Documentation

- **Main README**: [README.md](README.md) - Repository overview and learning paths
- **Study Guide**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Learning resources and timeline
- **Support**: [SUPPORT.md](SUPPORT.md) - How to get help
- **Security**: [SECURITY.md](SECURITY.md) - How to report security issues

### Community Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Ask questions and share ideas](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Technical issues wit Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Contact

- **Maintainers**: Check [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Security Issues**: Follow responsible disclosure for [SECURITY.md](SECURITY.md)
- **Microsoft Support**: For enterprise support, contact Microsoft customer service

### Additional Resources

- **Microsoft Learn**: [AI and Machine Learning Learning Paths](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Documentation**: [Official Docs](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Community Samples**: Check [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) for community contributions

---

**Dis na educational repository wey dey focus on teaching Edge AI development. Di main way to contribute na to improve di educational content and add or make better sample applications wey dey show Edge AI concepts.**

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->