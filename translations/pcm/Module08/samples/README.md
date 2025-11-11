<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "729f809c84e99609364180c090c43405",
  "translation_date": "2025-11-11T17:59:48+00:00",
  "source_file": "Module08/samples/README.md",
  "language_code": "pcm"
}
-->
# Module 08 Samples: Foundry Local Development Guide

## Overview

Dis kain collection dey show how to use **Foundry Local SDK** and **Shell Command** to build AI apps wey fit work well for production. Each sample dey show different ways to do edge AI development, from simple REST integration to advanced multi-agent systems.

## Development Approach: SDK vs Shell Commands

### Use Foundry Local SDK When:

- **Programmatic Control**: You need full control to manage agent lifecycle, evaluation, or deployment workflows
- **Custom Tooling**: To build automation around Foundry Local (like CI/CD integration, multi-agent orchestration)
- **Fine-Grained Access**: If you need detailed agent metadata, versioning, or evaluation runner control
- **Python Integration**: If you dey work for Python-heavy environments or wan put Foundry logic inside bigger applications
- **Enterprise Workflows**: To create modular workflows and reproducible evaluation pipelines wey match Microsoft reference architectures

### Use Shell Commands When:

- **Quick Testing**: To do fast local testing, launch agents manually, or check setup
- **CLI Simplicity**: If you need simple CLI operations to start/stop agents, check logs, or do basic evaluations
- **Lightweight Automation**: To write small automation scripts wey no need full SDK integration
- **Rapid Iteration**: For debugging and development cycles, especially for environments wey dey tight or resource group-level deployments
- **Setup & Validation**: To configure environment and verify things quickly

## Best Practices & Recommended Workflow

Based on agent lifecycle management, dependency tracking, and least-privilege reproducibility principles:

### Phase 1: Foundation & Setup
1. **Start with Shell Commands** to set up and validate things fast
2. **Verify Environment** with CLI tools and deploy simple model
3. **Test Connectivity** using small REST calls and health checks

### Phase 2: Development & Integration
1. **Transition to SDK** for workflows wey fit scale and trace well
2. **Implement Programmatic Control** for complex agent interactions
3. **Build Custom Tools** for templates wey community fit use and Azure OpenAI integration

### Phase 3: Production & Scale
1. **Hybrid Approach** wey combine CLI for operations and SDK for application logic
2. **Enterprise Integration** with monitoring, logging, and deployment pipelines
3. **Community Contribution** by sharing reusable templates and best practices

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->