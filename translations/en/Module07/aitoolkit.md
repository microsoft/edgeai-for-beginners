# AI Toolkit for Visual Studio Code - Edge AI Development Guide

## Introduction

Welcome to the complete guide for using AI Toolkit for Visual Studio Code in Edge AI development. As artificial intelligence transitions from centralized cloud computing to distributed edge devices, developers require robust, integrated tools to address the unique challenges of edge deployment—such as resource limitations and offline operation needs.

AI Toolkit for Visual Studio Code bridges this gap by offering a comprehensive development environment tailored for building, testing, and optimizing AI applications that run efficiently on edge devices. Whether you're working with IoT sensors, mobile devices, embedded systems, or edge servers, this toolkit simplifies your entire development workflow within the familiar VS Code interface.

This guide will walk you through the key concepts, tools, and best practices for utilizing AI Toolkit in your Edge AI projects, from initial model selection to production deployment.

## Overview

AI Toolkit for Visual Studio Code is a powerful extension that simplifies agent development and AI application creation. The toolkit offers extensive capabilities for exploring, evaluating, and deploying AI models from various providers—including Anthropic, OpenAI, GitHub, and Google—while supporting local model execution using ONNX and Ollama.

What makes AI Toolkit unique is its holistic approach to the entire AI development lifecycle. Unlike traditional AI tools that focus on specific aspects, AI Toolkit provides an integrated environment covering model discovery, experimentation, agent development, evaluation, and deployment—all within the familiar VS Code interface.

The platform is designed for rapid prototyping and production deployment, featuring tools like prompt generation, quick starters, seamless MCP (Model Context Protocol) integrations, and robust evaluation capabilities. For Edge AI development, this means you can efficiently create, test, and optimize AI applications for edge deployment scenarios while maintaining a streamlined workflow in VS Code.

## Learning Objectives

By the end of this guide, you will be able to:

### Core Competencies
- **Install and configure** AI Toolkit for Visual Studio Code to support Edge AI development workflows
- **Navigate and utilize** the AI Toolkit interface, including Model Catalog, Playground, and Agent Builder
- **Select and evaluate** AI models suitable for edge deployment based on performance and resource constraints
- **Convert and optimize** models using ONNX format and quantization techniques for edge devices

### Edge AI Development Skills
- **Design and implement** Edge AI applications using the integrated development environment
- **Perform model testing** under edge-like conditions using local inference and resource monitoring
- **Create and customize** AI agents optimized for edge deployment scenarios
- **Evaluate model performance** using metrics relevant to edge computing (latency, memory usage, accuracy)

### Optimization and Deployment
- **Apply quantization and pruning** techniques to reduce model size while maintaining acceptable performance
- **Optimize models** for specific edge hardware platforms, including CPU, GPU, and NPU acceleration
- **Implement best practices** for edge AI development, including resource management and fallback strategies
- **Prepare models and applications** for production deployment on edge devices

### Advanced Edge AI Concepts
- **Integrate with edge AI frameworks** such as ONNX Runtime, Windows ML, and TensorFlow Lite
- **Implement multi-model architectures** and federated learning scenarios for edge environments
- **Troubleshoot common edge AI issues** like memory constraints, inference speed, and hardware compatibility
- **Design monitoring and logging** strategies for edge AI applications in production

### Practical Application
- **Build end-to-end Edge AI solutions** from model selection to deployment
- **Demonstrate proficiency** in edge-specific development workflows and optimization techniques
- **Apply learned concepts** to real-world edge AI use cases, including IoT, mobile, and embedded applications
- **Evaluate and compare** different edge AI deployment strategies and their trade-offs

## Key Features for Edge AI Development

### 1. Model Catalog and Discovery
- **Multi-Provider Support**: Browse and access AI models from Anthropic, OpenAI, GitHub, Google, and other providers
- **Local Model Integration**: Easily discover ONNX and Ollama models for edge deployment
- **GitHub Models**: Direct integration with GitHub's model hosting for streamlined access
- **Model Comparison**: Compare models side-by-side to find the best fit for edge device constraints

### 2. Interactive Playground
- **Interactive Testing Environment**: Quickly experiment with model capabilities in a controlled setting
- **Multi-modal Support**: Test with images, text, and other inputs typical in edge scenarios
- **Real-time Experimentation**: Get immediate feedback on model responses and performance
- **Parameter Optimization**: Fine-tune model parameters for edge deployment needs

### 3. Prompt (Agent) Builder
- **Natural Language Generation**: Create starter prompts using natural language descriptions
- **Iterative Refinement**: Enhance prompts based on model responses and performance
- **Task Decomposition**: Break down complex tasks with prompt chaining and structured outputs
- **Variable Support**: Use variables in prompts for dynamic agent behavior
- **Production Code Generation**: Generate production-ready code for rapid application development

### 4. Bulk Run and Evaluation
- **Multi-Model Testing**: Run multiple prompts across selected models simultaneously
- **Efficient Testing at Scale**: Test various inputs and configurations efficiently
- **Custom Test Cases**: Validate agent functionality with test cases
- **Performance Comparison**: Compare results across different models and configurations

### 5. Model Evaluation with Datasets
- **Standard Metrics**: Evaluate AI models using built-in metrics (F1 score, relevance, similarity, coherence)
- **Custom Evaluators**: Create custom evaluation metrics for specific use cases
- **Dataset Integration**: Test models against comprehensive datasets
- **Performance Measurement**: Quantify model performance for edge deployment decisions

### 6. Fine-tuning Capabilities
- **Model Customization**: Tailor models for specific use cases and domains
- **Specialized Adaptation**: Adapt models to specialized requirements
- **Edge Optimization**: Fine-tune models specifically for edge deployment constraints
- **Domain-Specific Training**: Develop models tailored to specific edge use cases

### 7. MCP Tool Integration
- **External Tool Connectivity**: Connect agents to external tools via Model Context Protocol servers
- **Real-world Actions**: Enable agents to query databases, access APIs, or execute custom logic
- **Existing MCP Servers**: Use tools from command (stdio) or HTTP (server-sent event) protocols
- **Custom MCP Development**: Build and test new MCP servers using Agent Builder

### 8. Agent Development and Testing
- **Function Calling Support**: Allow agents to dynamically invoke external functions
- **Real-time Integration Testing**: Test integrations with real-time runs and tool usage
- **Agent Versioning**: Version control for agents with comparison capabilities for evaluation results
- **Debugging and Tracing**: Local debugging and tracing tools for agent development

## Edge AI Development Workflow

### Phase 1: Model Discovery and Selection
1. **Explore Model Catalog**: Use the catalog to find models suitable for edge deployment
2. **Compare Performance**: Evaluate models based on size, accuracy, and inference speed
3. **Test Locally**: Use Ollama or ONNX models for local testing before edge deployment
4. **Assess Resource Requirements**: Determine memory and computational needs for target edge devices

### Phase 2: Model Optimization
1. **Convert to ONNX**: Convert selected models to ONNX format for edge compatibility
2. **Apply Quantization**: Reduce model size using INT8 or INT4 quantization
3. **Hardware Optimization**: Optimize for target edge hardware (ARM, x86, specialized accelerators)
4. **Performance Validation**: Ensure optimized models maintain acceptable accuracy

### Phase 3: Application Development
1. **Agent Design**: Use Agent Builder to create edge-optimized AI agents
2. **Prompt Engineering**: Develop prompts tailored for smaller edge models
3. **Integration Testing**: Test agents in simulated edge conditions
4. **Code Generation**: Generate production-ready code optimized for edge deployment

### Phase 4: Evaluation and Testing
1. **Batch Evaluation**: Test multiple configurations to identify optimal edge settings
2. **Performance Profiling**: Analyze inference speed, memory usage, and accuracy
3. **Edge Simulation**: Test in conditions similar to the target edge deployment environment
4. **Stress Testing**: Evaluate performance under varying load conditions

### Phase 5: Deployment Preparation
1. **Final Optimization**: Apply final tweaks based on testing results
2. **Deployment Packaging**: Package models and code for edge deployment
3. **Documentation**: Document deployment requirements and configurations
4. **Monitoring Setup**: Prepare monitoring and logging for edge deployment

## Target Audience for Edge AI Development

### Edge AI Developers
- Application developers creating AI-powered edge devices and IoT solutions
- Embedded systems developers integrating AI into resource-constrained devices
- Mobile developers building on-device AI applications for smartphones and tablets

### Edge AI Engineers
- AI engineers optimizing models for edge deployment and managing inference pipelines
- DevOps engineers deploying and managing AI models across distributed edge infrastructure
- Performance engineers optimizing AI workloads for edge hardware constraints

### Researchers and Educators
- AI researchers developing efficient models and algorithms for edge computing
- Educators teaching edge AI concepts and demonstrating optimization techniques
- Students learning about the challenges and solutions in edge AI deployment

## Edge AI Use Cases

### Smart IoT Devices
- **Real-time Image Recognition**: Deploy computer vision models on IoT cameras and sensors
- **Voice Processing**: Implement speech recognition and natural language processing on smart speakers
- **Predictive Maintenance**: Run anomaly detection models on industrial edge devices
- **Environmental Monitoring**: Deploy sensor data analysis models for environmental applications

### Mobile and Embedded Applications
- **On-device Translation**: Implement language translation models that work offline
- **Augmented Reality**: Deploy real-time object recognition and tracking for AR applications
- **Health Monitoring**: Run health analysis models on wearable devices and medical equipment
- **Autonomous Systems**: Implement decision-making models for drones, robots, and vehicles

### Edge Computing Infrastructure
- **Edge Data Centers**: Deploy AI models in edge data centers for low-latency applications
- **CDN Integration**: Integrate AI processing capabilities into content delivery networks
- **5G Edge**: Utilize 5G edge computing for AI-powered applications
- **Fog Computing**: Implement AI processing in fog computing environments

## Installation and Setup

### Extension Installation
Install the AI Toolkit extension directly from the Visual Studio Code Marketplace:

**Extension ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installation Methods**:
1. **VS Code Marketplace**: Search for "AI Toolkit" in the Extensions view
2. **Command Line**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direct Install**: Download from [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Prerequisites for Edge AI Development
- **Visual Studio Code**: Latest version recommended
- **Python Environment**: Python 3.8+ with required AI libraries
- **ONNX Runtime** (Optional): For ONNX model inference
- **Ollama** (Optional): For local model serving
- **Hardware Acceleration Tools**: CUDA, OpenVINO, or platform-specific accelerators

### Initial Configuration
1. **Extension Activation**: Open VS Code and verify AI Toolkit appears in the Activity Bar
2. **Model Provider Setup**: Configure access to GitHub, OpenAI, Anthropic, or other model providers
3. **Local Environment**: Set up Python environment and install required packages
4. **Hardware Acceleration**: Configure GPU/NPU acceleration if available
5. **MCP Integration**: Set up Model Context Protocol servers if needed

### First-Time Setup Checklist
- [ ] AI Toolkit extension installed and activated
- [ ] Model catalog accessible and models discoverable
- [ ] Playground functional for model testing
- [ ] Agent Builder accessible for prompt development
- [ ] Local development environment configured
- [ ] Hardware acceleration (if available) properly configured

## Getting Started with AI Toolkit

### Quick Start Guide

We recommend starting with models hosted by GitHub for the most streamlined experience:

1. **Installation**: Follow the [installation guide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) to set up AI Toolkit for your device
2. **Model Discovery**: From the extension tree view, select **CATALOG > Models** to explore available models
3. **GitHub Models**: Start with models hosted by GitHub for optimal integration
4. **Playground Testing**: From any model card, select **Try in Playground** to start experimenting with model capabilities

### Step-by-Step Edge AI Development

#### Step 1: Model Exploration and Selection
1. Open the AI Toolkit view in VS Code Activity Bar
2. Browse the Model Catalog for models suitable for edge deployment
3. Filter by provider (GitHub, ONNX, Ollama) based on your edge requirements
4. Use **Try in Playground** to test model capabilities immediately

#### Step 2: Agent Development
1. Use the **Prompt (Agent) Builder** to create edge-optimized AI agents
2. Generate initial prompts using natural language descriptions  
3. Refine and iterate prompts based on model feedback  
4. Utilize MCP tools to enhance agent functionalities  

#### Step 3: Testing and Evaluation  
1. Use **Bulk Run** to test multiple prompts across selected models  
2. Execute agents with test cases to verify functionality  
3. Assess accuracy and performance using built-in or custom metrics  
4. Compare various models and configurations  

#### Step 4: Fine-tuning and Optimization  
1. Adapt models for specific edge use cases  
2. Implement domain-specific fine-tuning  
3. Optimize for constraints in edge deployment  
4. Version and evaluate different agent configurations  

#### Step 5: Deployment Preparation  
1. Generate production-ready code using the Agent Builder  
2. Configure MCP server connections for production environments  
3. Prepare deployment packages for edge devices  
4. Set up monitoring and evaluation metrics  

## Samples for AI Toolkit  

Explore Our Samples  
The [AI Toolkit samples](https://github.com/Azure-Samples/AI_Toolkit_Samples) are designed to assist developers and researchers in effectively exploring and implementing AI solutions.  

Our samples include:  

Sample Code: Pre-built examples showcasing AI functionalities, such as training, deployment, or model integration into applications.  
Documentation: Tutorials and guides to help users understand AI Toolkit features and their usage.  

Prerequisites  

- Visual Studio Code  
- AI Toolkit for Visual Studio Code  
- GitHub Fine-grained personal access token (PAT)  
- Foundry Local  

## Best Practices for Edge AI Development  

### Model Selection  
- **Size Constraints**: Select models that fit within the memory limits of target devices  
- **Inference Speed**: Prioritize models with fast inference times for real-time applications  
- **Accuracy Trade-offs**: Balance model accuracy with resource limitations  
- **Format Compatibility**: Opt for ONNX or hardware-optimized formats for edge deployment  

### Optimization Techniques  
- **Quantization**: Apply INT8 or INT4 quantization to reduce model size and enhance speed  
- **Pruning**: Eliminate unnecessary model parameters to lower computational demands  
- **Knowledge Distillation**: Develop smaller models that retain the performance of larger ones  
- **Hardware Acceleration**: Utilize NPUs, GPUs, or specialized accelerators when available  

### Development Workflow  
- **Iterative Testing**: Conduct frequent tests in edge-like conditions during development  
- **Performance Monitoring**: Continuously track resource usage and inference speed  
- **Version Control**: Maintain records of model versions and optimization settings  
- **Documentation**: Document all optimization decisions and performance trade-offs  

### Deployment Considerations  
- **Resource Monitoring**: Track memory, CPU, and power usage in production environments  
- **Fallback Strategies**: Implement mechanisms to handle model failures  
- **Update Mechanisms**: Plan for model updates and version management  
- **Security**: Ensure appropriate security measures for edge AI applications  

## Integration with Edge AI Frameworks  

### ONNX Runtime  
- **Cross-platform Deployment**: Deploy ONNX models across various edge platforms  
- **Hardware Optimization**: Utilize ONNX Runtime's hardware-specific optimizations  
- **Mobile Support**: Deploy ONNX Runtime Mobile for smartphones and tablets  
- **IoT Integration**: Use ONNX Runtime's lightweight distributions for IoT devices  

### Windows ML  
- **Windows Devices**: Optimize for Windows-based edge devices and PCs  
- **NPU Acceleration**: Utilize Neural Processing Units on Windows devices  
- **DirectML**: Employ DirectML for GPU acceleration on Windows platforms  
- **UWP Integration**: Integrate with Universal Windows Platform applications  

### TensorFlow Lite  
- **Mobile Optimization**: Deploy TensorFlow Lite models on mobile and embedded devices  
- **Hardware Delegates**: Use specialized hardware delegates for acceleration  
- **Micro Controllers**: Deploy TensorFlow Lite Micro on microcontrollers  
- **Cross-platform Support**: Deploy across Android, iOS, and embedded Linux systems  

### Azure IoT Edge  
- **Cloud-Edge Hybrid**: Combine cloud-based training with edge inference  
- **Module Deployment**: Deploy AI models as IoT Edge modules  
- **Device Management**: Manage edge devices and model updates remotely  
- **Telemetry**: Gather performance data and model metrics from edge deployments  

## Advanced Edge AI Scenarios  

### Multi-Model Deployment  
- **Model Ensembles**: Deploy multiple models for enhanced accuracy or redundancy  
- **A/B Testing**: Simultaneously test different models on edge devices  
- **Dynamic Selection**: Select models based on current device conditions  
- **Resource Sharing**: Optimize resource usage across multiple deployed models  

### Federated Learning  
- **Distributed Training**: Train models across multiple edge devices  
- **Privacy Preservation**: Keep training data local while sharing model updates  
- **Collaborative Learning**: Enable devices to learn from shared experiences  
- **Edge-Cloud Coordination**: Coordinate learning between edge devices and cloud infrastructure  

### Real-time Processing  
- **Stream Processing**: Handle continuous data streams on edge devices  
- **Low-latency Inference**: Optimize for minimal inference delays  
- **Batch Processing**: Efficiently process data batches on edge devices  
- **Adaptive Processing**: Adjust processing based on current device capabilities  

## Troubleshooting Edge AI Development  

### Common Issues  
- **Memory Constraints**: Model exceeds memory capacity of target device  
- **Inference Speed**: Model inference is too slow for real-time applications  
- **Accuracy Degradation**: Optimization compromises model accuracy  
- **Hardware Compatibility**: Model is incompatible with target hardware  

### Debugging Strategies  
- **Performance Profiling**: Use AI Toolkit's tracing features to identify bottlenecks  
- **Resource Monitoring**: Track memory and CPU usage during development  
- **Incremental Testing**: Test optimizations step-by-step to isolate issues  
- **Hardware Simulation**: Use development tools to simulate target hardware  

### Optimization Solutions  
- **Further Quantization**: Apply more aggressive quantization techniques  
- **Model Architecture**: Explore alternative model architectures optimized for edge  
- **Preprocessing Optimization**: Enhance data preprocessing for edge constraints  
- **Inference Optimization**: Utilize hardware-specific inference optimizations  

## Resources and Next Steps  

### Official Documentation  
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)  
- [Installation and Setup Guide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps Documentation](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io/)  

### Community and Support  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues and Feature Requests](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Technical Resources  
- [ONNX Runtime Documentation](https://onnxruntime.ai/)  
- [Ollama Documentation](https://ollama.ai/)  
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Learning Pathways  
- [Edge AI Fundamentals Course](../Module01/README.md)  
- [Small Language Models Guide](../Module02/README.md)  
- [Edge Deployment Strategies](../Module03/README.md)  
- [Windows Edge AI Development](./windowdeveloper.md)  

### Additional Resources  
- **Repository Stats**: 1.8k+ stars, 150+ forks, 18+ contributors  
- **License**: MIT License  
- **Security**: Microsoft security policies apply  
- **Telemetry**: Respects VS Code telemetry settings  

## Conclusion  

AI Toolkit for Visual Studio Code offers a comprehensive platform for modern AI development, particularly suited for Edge AI applications. With its extensive model catalog supporting providers like Anthropic, OpenAI, GitHub, and Google, along with local execution options via ONNX and Ollama, the toolkit provides the flexibility required for diverse edge deployment scenarios.  

The toolkit excels in its integrated approach—from model discovery and experimentation in the Playground to advanced agent development with the Prompt Builder, robust evaluation capabilities, and seamless MCP tool integration. For Edge AI developers, this enables rapid prototyping and testing of AI agents before deployment, with the ability to iterate and optimize for resource-constrained environments.  

Key benefits for Edge AI development include:  
- **Rapid Experimentation**: Quickly test models and agents before edge deployment  
- **Multi-Provider Flexibility**: Access models from various sources to find optimal solutions  
- **Local Development**: Test with ONNX and Ollama for offline and privacy-focused development  
- **Production Readiness**: Generate production-ready code and integrate external tools via MCP  
- **Comprehensive Evaluation**: Validate edge AI performance using built-in and custom metrics  

As AI increasingly moves toward edge deployment scenarios, AI Toolkit for VS Code provides the tools and workflow necessary to build, test, and optimize intelligent applications for resource-constrained environments. Whether developing IoT solutions, mobile AI applications, or embedded intelligence systems, the toolkit supports the entire edge AI development lifecycle.  

With ongoing updates and an active community (1.8k+ GitHub stars), AI Toolkit remains a leading choice for AI development tools, continuously evolving to meet the needs of developers working on edge deployment scenarios.  

[Next Foundry Local](./foundrylocal.md)  

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.