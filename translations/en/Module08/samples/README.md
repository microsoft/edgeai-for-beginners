# Module 08 Samples: Foundry Local Development Guide

## Overview

This detailed collection demonstrates both the **Foundry Local SDK** and **Shell Command** methods for creating production-ready AI applications. Each example highlights various aspects of edge AI development, ranging from basic REST integration to advanced multi-agent systems.

## Development Approach: SDK vs Shell Commands

### Use Foundry Local SDK When:

- **Programmatic Control**: You require complete control over agent lifecycle, evaluation, or deployment workflows.
- **Custom Tooling**: Developing automation around Foundry Local (e.g., CI/CD integration, multi-agent orchestration).
- **Fine-Grained Access**: Need detailed agent metadata, versioning, or control over evaluation runners.
- **Python Integration**: Working in Python-centric environments or embedding Foundry logic into larger applications.
- **Enterprise Workflows**: Implementing modular workflows and reproducible evaluation pipelines aligned with Microsoft's reference architectures.

### Use Shell Commands When:

- **Quick Testing**: Conducting rapid local tests, manually launching agents, or verifying setups.
- **CLI Simplicity**: Requiring straightforward CLI operations for starting/stopping agents, checking logs, or performing basic evaluations.
- **Lightweight Automation**: Writing simple scripts for automation without needing full SDK integration.
- **Rapid Iteration**: Debugging and development cycles, especially in constrained environments or deployments at the resource group level.
- **Setup & Validation**: Configuring the environment and performing quick verification tasks.

## Best Practices & Recommended Workflow

Following principles of agent lifecycle management, dependency tracking, and reproducibility with minimal privileges:

### Phase 1: Foundation & Setup
1. **Begin with Shell Commands** for initial setup and quick validation.
2. **Verify Environment** using CLI tools and basic model deployment.
3. **Test Connectivity** with simple REST calls and health checks.

### Phase 2: Development & Integration
1. **Switch to SDK** for scalable and traceable workflows.
2. **Enable Programmatic Control** for handling complex agent interactions.
3. **Develop Custom Tools** for community-ready templates and Azure OpenAI integration.

### Phase 3: Production & Scale
1. **Adopt a Hybrid Approach** using CLI for operations and SDK for application logic.
2. **Enterprise Integration** with monitoring, logging, and deployment pipelines.
3. **Contribute to the Community** by sharing reusable templates and best practices.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.