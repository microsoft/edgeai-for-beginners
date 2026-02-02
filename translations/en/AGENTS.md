# AGENTS.md

> **Developer Guide for Contributing to EdgeAI for Beginners**
> 
> This document provides detailed information for developers, AI agents, and contributors working with this repository. It includes setup instructions, development workflows, testing procedures, and best practices.
> 
> **Last Updated**: October 30, 2025 | **Document Version**: 3.0

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

EdgeAI for Beginners is an educational repository designed to teach Edge AI development using Small Language Models (SLMs). The course covers EdgeAI basics, model deployment, optimization techniques, and production-ready implementations using Microsoft Foundry Local and various AI frameworks.

**Key Technologies:**
- Python 3.8+ (main language for AI/ML examples)
- .NET C# (AI/ML examples)
- JavaScript/Node.js with Electron (for desktop apps)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI Frameworks: LangChain, Semantic Kernel, Chainlit
- Model Optimization: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository Type:** Educational content repository with 8 modules and 10 detailed sample applications

**Architecture:** Multi-module learning path with practical examples demonstrating Edge AI deployment patterns

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

### Required Tools

- **Python 3.8+** - For AI/ML examples and notebooks
- **Node.js 16+** - For the Electron sample application
- **Git** - For version control
- **Microsoft Foundry Local** - For running AI models locally

### Recommended Tools

- **Visual Studio Code** - With Python, Jupyter, and Pylance extensions
- **Windows Terminal** - For an improved command-line experience (Windows users)
- **Docker** - For containerized development (optional)

### System Requirements

- **RAM**: Minimum 8GB, 16GB+ recommended for multi-model scenarios
- **Storage**: At least 10GB free space for models and dependencies
- **OS**: Windows 10/11, macOS 11+, or Linux (Ubuntu 20.04+)
- **Hardware**: CPU with AVX2 support; GPU (CUDA, Qualcomm NPU) optional but recommended

### Knowledge Prerequisites

- Basic Python programming knowledge
- Familiarity with command-line interfaces
- Understanding of AI/ML concepts (for developing examples)
- Git workflows and pull request processes

## Setup Commands

### Repository Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python Sample Setup (Module08 and Workshop examples)

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

Foundry Local is required to run the examples. Download and install it from the official repository:

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

**Note**: Foundry Local automatically selects the best model variant for your hardware (CUDA GPU, Qualcomm NPU, or CPU).

## Development Workflow

### Content Development

This repository primarily contains **Markdown educational content**. When making changes:

1. Edit `.md` files in the appropriate module directories
2. Follow the existing formatting patterns
3. Ensure code examples are accurate and tested
4. Update corresponding translated content if necessary (or let automation handle it)

### Sample Application Development

For Module08 Python examples (samples 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

For Workshop Python examples:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

For the Electron sample (sample 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testing Sample Applications

Python examples do not have automated tests but can be validated by running them:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

The Electron sample includes a test infrastructure:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testing Instructions

### Content Validation

The repository uses automated translation workflows. No manual testing is required for translations.

**Manual validation for content changes:**
1. Preview `.md` files to check Markdown rendering
2. Verify all links point to valid targets
3. Test any code snippets included in the documentation
4. Ensure images load correctly

### Sample Application Testing

**Module08/samples/08 (Electron app) includes comprehensive testing:**
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

**Python examples should be tested manually:**
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

- Use consistent heading hierarchy (# for title, ## for main sections, ### for subsections)
- Include code blocks with language specifiers: ```python, ```bash, ```javascript
- Follow existing formatting for tables, lists, and emphasis
- Keep lines readable (aim for ~80-100 characters, but not strict)
- Use relative links for internal references

### Python Code Style

- Follow PEP 8 conventions
- Use type hints where appropriate
- Include docstrings for functions and classes
- Use meaningful variable names
- Keep functions focused and concise

### JavaScript/Node.js Code Style

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Key conventions:**
- ESLint configuration provided in sample 08
- Prettier for code formatting
- Use modern ES6+ syntax
- Follow existing patterns in the codebase

## Pull Request Guidelines

### Contribution Workflow

1. **Fork the repository** and create a new branch from `main`
2. **Make your changes** following the code style guidelines
3. **Test thoroughly** using the testing instructions above
4. **Commit with clear messages** following the conventional commits format
5. **Push to your fork** and create a pull request
6. **Respond to feedback** from maintainers during review

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

All contributors must follow the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Please review [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

### Before Submitting

**For content changes:**
- Preview all modified Markdown files
- Verify links and images work
- Check for typos and grammatical errors

**For sample code changes (Module08/samples/08):**
```bash
npm run lint
npm test
```

**For Python sample changes:**
- Test the sample runs successfully
- Verify error handling works
- Check compatibility with Foundry Local

### Review Process

- Educational content changes are reviewed for accuracy and clarity
- Code samples are tested for functionality
- Translation updates are handled automatically by GitHub Actions

## Translation System

**IMPORTANT:** This repository uses automated translation via GitHub Actions.

- Translations are in the `/translations/` directory (50+ languages)
- Automated via the `co-op-translator.yml` workflow
- **DO NOT manually edit translation files** - they will be overwritten
- Edit only English source files in the root and module directories
- Translations are automatically generated on push to the `main` branch

## Foundry Local Integration

Most Module08 examples require Microsoft Foundry Local to be running.

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

Most examples use these environment variables:
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

**Note**: When using `FoundryLocalManager`, the SDK automatically handles service discovery and model loading. Model aliases (like `phi-3.5-mini`) ensure the best variant is selected for your hardware.

## Build and Deployment

### Content Deployment

This repository is primarily documentation - no build process is required for content.

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

**Python Examples:**
No build process - examples are run directly with the Python interpreter.

## Common Issues and Troubleshooting

> **Tip**: Check [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) for known problems and solutions.

### Critical Issues (Blocking)

#### Foundry Local Not Running
**Issue:** Examples fail with connection errors

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

#### Python Virtual Environment Issues
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

#### Electron Build Issues
**Issue:** npm install or build failures

**Solution:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Workflow Issues (Minor)

#### Translation Workflow Conflicts
**Issue:** Translation PR conflicts with your changes

**Solution:**
- Only edit English source files
- Let the automated translation workflow handle translations
- If conflicts occur, merge `main` into your branch after translations are merged

#### Model Download Failures
**Issue:** Foundry Local fails to download models

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
- **Module01:** EdgeAI fundamentals and real-world case studies
- **Module02:** Small Language Model (SLM) families and architectures
- **Module03:** Local and cloud deployment strategies
- **Module04:** Model optimization with multiple frameworks (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - production operations
- **Module06:** AI agents and function calling
- **Module07:** Platform-specific implementations
- **Module08:** Foundry Local toolkit with 10 detailed examples

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

The repository includes 10 detailed sample applications:

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

The Workshop includes 6 progressive sessions with practical implementations:

1. **Session 01** - Chat setup with Foundry Local integration
2. **Session 02** - RAG pipeline and evaluation using RAGAS
3. **Session 03** - Benchmarking open-source models
4. **Session 04** - Model comparison and selection
5. **Session 05** - Multi-agent orchestration systems
6. **Session 06** - Model routing and pipeline management

Each sample showcases different aspects of edge AI development with Foundry Local.

### Performance Considerations

- SLMs are optimized for edge deployment (2-16GB RAM)
- Local inference delivers response times of 50-500ms
- Quantization techniques reduce size by 75% while retaining 85% performance
- Enables real-time conversation capabilities with local models

### Security and Privacy

- All processing is done locally - no data is sent to the cloud
- Suitable for privacy-sensitive applications (e.g., healthcare, finance)
- Complies with data sovereignty requirements
- Foundry Local operates entirely on local hardware

## Getting Help

### Documentation

- **Main README**: [README.md](README.md) - Repository overview and learning paths
- **Study Guide**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Learning resources and timeline
- **Support**: [SUPPORT.md](SUPPORT.md) - How to get help
- **Security**: [SECURITY.md](SECURITY.md) - Reporting security issues

### Community Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Ask questions and share ideas](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Technical issues with Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Contact

- **Maintainers**: See [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Security Issues**: Follow responsible disclosure in [SECURITY.md](SECURITY.md)
- **Microsoft Support**: For enterprise support, contact Microsoft customer service

### Additional Resources

- **Microsoft Learn**: [AI and Machine Learning Learning Paths](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Documentation**: [Official Docs](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Community Samples**: Check [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) for community contributions

---

**This is an educational repository aimed at teaching Edge AI development. The primary contribution focus is on improving educational content and adding/enhancing sample applications that demonstrate Edge AI concepts.**

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.