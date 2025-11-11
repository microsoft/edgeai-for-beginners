<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "efb0e70d6e87d0795f4d381c3bc99074",
  "translation_date": "2025-11-11T17:53:05+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "pcm"
}
-->
# AI Toolkit for Visual Studio Code - Edge AI Development Guide

## Introduction

Welcome to dis guide wey go show you how to use AI Toolkit for Visual Studio Code for Edge AI development. As AI dey move from cloud computing go edge devices, developers need better tools wey go fit handle di wahala wey dey edge deployment - like resource constraints and offline operation.

AI Toolkit for Visual Studio Code dey help bridge dis gap by giving developers one complete environment wey dem fit use build, test, and optimize AI apps wey go run well for edge devices. Whether na IoT sensors, mobile devices, embedded systems, or edge servers you dey work on, dis toolkit go make your work easy inside di VS Code environment wey you sabi.

Dis guide go show you di main things, tools, and best practices wey you need to use AI Toolkit for your Edge AI projects, from di time you dey choose model till di time you deploy am.

## Overview

AI Toolkit for Visual Studio Code na one strong extension wey dey make agent development and AI app creation easy. Di toolkit get plenty features wey go help you explore, test, and deploy AI models from different providers like Anthropic, OpenAI, GitHub, Google, and e still support local model execution with ONNX and Ollama.

Wetin make AI Toolkit special na di way e cover di whole AI development process. E no be like di regular AI tools wey dey focus on only one part. AI Toolkit dey give you everything you need for model discovery, testing, agent development, evaluation, and deployment—all inside di VS Code environment wey you sabi.

Di platform dey designed for quick prototyping and production deployment, with features like prompt generation, quick starters, MCP (Model Context Protocol) tool integration, and evaluation tools. For Edge AI development, e mean say you fit develop, test, and optimize AI apps for edge deployment without stress.

## Learning Objectives

By di end of dis guide, you go sabi:

### Core Competencies
- **Install and configure** AI Toolkit for Visual Studio Code for Edge AI workflows
- **Navigate and use** di AI Toolkit interface like Model Catalog, Playground, and Agent Builder
- **Choose and test** AI models wey fit edge deployment based on performance and resource constraints
- **Convert and optimize** models using ONNX format and quantization techniques for edge devices

### Edge AI Development Skills
- **Design and build** Edge AI apps using di integrated development environment
- **Test models** under edge-like conditions using local inference and resource monitoring
- **Create and customize** AI agents wey dey optimized for edge deployment
- **Check model performance** using metrics wey dey important for edge computing (latency, memory usage, accuracy)

### Optimization and Deployment
- **Use quantization and pruning** techniques to reduce model size but still keep performance okay
- **Optimize models** for specific edge hardware like CPU, GPU, and NPU acceleration
- **Follow best practices** for edge AI development like resource management and fallback strategies
- **Prepare models and apps** for production deployment on edge devices

### Advanced Edge AI Concepts
- **Work with edge AI frameworks** like ONNX Runtime, Windows ML, and TensorFlow Lite
- **Use multi-model architectures** and federated learning for edge environments
- **Solve common edge AI problems** like memory constraints, inference speed, and hardware compatibility
- **Plan monitoring and logging** for edge AI apps wey don enter production

### Practical Application
- **Build complete Edge AI solutions** from model selection to deployment
- **Show skill** in edge-specific workflows and optimization techniques
- **Use wetin you learn** for real-world edge AI projects like IoT, mobile, and embedded apps
- **Compare different edge AI deployment methods** and di pros and cons

## Key Features for Edge AI Development

### 1. Model Catalog and Discovery
- **Multi-Provider Support**: Find AI models from Anthropic, OpenAI, GitHub, Google, and others
- **Local Model Integration**: Easy discovery of ONNX and Ollama models for edge deployment
- **GitHub Models**: Direct access to models wey dey GitHub
- **Model Comparison**: Compare models side-by-side to choose di best one for edge devices

### 2. Interactive Playground
- **Interactive Testing Environment**: Test model features in one controlled space
- **Multi-modal Support**: Test with images, text, and other inputs wey dey common for edge scenarios
- **Real-time Experimentation**: Get quick feedback on model performance
- **Parameter Optimization**: Adjust model settings for edge deployment needs

### 3. Prompt (Agent) Builder
- **Natural Language Generation**: Create prompts using natural language
- **Refine Prompts**: Make prompts better based on model feedback
- **Task Decomposition**: Break down complex tasks into smaller ones
- **Variable Support**: Add variables to prompts for dynamic agent actions
- **Production Code Generation**: Create code wey fit go straight to production

### 4. Bulk Run and Evaluation
- **Multi-Model Testing**: Test many prompts across different models at once
- **Efficient Testing**: Test different inputs and settings fast
- **Custom Test Cases**: Use test cases to check agent functionality
- **Performance Comparison**: Compare results from different models and settings

### 5. Model Evaluation with Datasets
- **Standard Metrics**: Test AI models with built-in evaluators like F1 score, relevance, similarity, coherence
- **Custom Evaluators**: Create your own metrics for specific needs
- **Dataset Integration**: Test models with big datasets
- **Performance Measurement**: Measure model performance for edge deployment

### 6. Fine-tuning Capabilities
- **Model Customization**: Adjust models for specific needs
- **Specialized Adaptation**: Make models fit special requirements
- **Edge Optimization**: Fine-tune models for edge constraints
- **Domain-Specific Training**: Train models for specific edge use cases

### 7. MCP Tool Integration
- **External Tool Connectivity**: Connect agents to external tools with Model Context Protocol servers
- **Real-world Actions**: Make agents query databases, use APIs, or run custom logic
- **Existing MCP Servers**: Use tools from command (stdio) or HTTP (server-sent event) protocols
- **Custom MCP Development**: Create new MCP servers and test dem with Agent Builder

### 8. Agent Development and Testing
- **Function Calling Support**: Make agents call external functions
- **Real-time Integration Testing**: Test integrations with live runs and tools
- **Agent Versioning**: Keep track of agent versions and compare results
- **Debugging and Tracing**: Debug and trace agents locally

## Edge AI Development Workflow

### Phase 1: Model Discovery and Selection
1. **Explore Model Catalog**: Find models wey fit edge deployment
2. **Compare Performance**: Check models based on size, accuracy, and speed
3. **Test Locally**: Use Ollama or ONNX models to test before deployment
4. **Check Resource Needs**: Know di memory and computational needs for di edge devices

### Phase 2: Model Optimization
1. **Convert to ONNX**: Change models to ONNX format for edge compatibility
2. **Use Quantization**: Make models smaller with INT8 or INT4 quantization
3. **Hardware Optimization**: Adjust models for di edge hardware (ARM, x86, accelerators)
4. **Performance Validation**: Make sure optimized models still dey perform well

### Phase 3: Application Development
1. **Agent Design**: Use Agent Builder to create AI agents for edge
2. **Prompt Engineering**: Write prompts wey go work well with small edge models
3. **Integration Testing**: Test agents in edge-like conditions
4. **Code Generation**: Create production-ready code for edge deployment

### Phase 4: Evaluation and Testing
1. **Batch Evaluation**: Test different settings to find di best one for edge
2. **Performance Profiling**: Check speed, memory usage, and accuracy
3. **Edge Simulation**: Test in conditions wey be like di real edge environment
4. **Stress Testing**: Check performance under heavy load

### Phase 5: Deployment Preparation
1. **Final Optimization**: Make di final adjustments based on testing
2. **Deployment Packaging**: Package models and code for edge deployment
3. **Documentation**: Write down di deployment requirements and setup
4. **Monitoring Setup**: Prepare monitoring and logging for edge deployment

## Target Audience for Edge AI Development

### Edge AI Developers
- Developers wey dey build AI-powered edge devices and IoT solutions
- Embedded systems developers wey dey add AI to devices wey no get plenty resources
- Mobile developers wey dey create AI apps for phones and tablets

### Edge AI Engineers
- AI engineers wey dey optimize models for edge deployment
- DevOps engineers wey dey manage AI models across edge infrastructure
- Performance engineers wey dey make AI workloads better for edge hardware

### Researchers and Educators
- AI researchers wey dey create efficient models for edge computing
- Educators wey dey teach edge AI concepts and optimization techniques
- Students wey dey learn about edge AI deployment challenges and solutions

## Edge AI Use Cases

### Smart IoT Devices
- **Real-time Image Recognition**: Use computer vision models for IoT cameras and sensors
- **Voice Processing**: Add speech recognition and natural language processing to smart speakers
- **Predictive Maintenance**: Use anomaly detection models for industrial devices
- **Environmental Monitoring**: Analyze sensor data for environmental applications

### Mobile and Embedded Applications
- **On-device Translation**: Use language translation models offline
- **Augmented Reality**: Add real-time object recognition for AR apps
- **Health Monitoring**: Use health analysis models for wearables and medical devices
- **Autonomous Systems**: Add decision-making models for drones, robots, and vehicles

### Edge Computing Infrastructure
- **Edge Data Centers**: Deploy AI models for low-latency apps
- **CDN Integration**: Add AI processing to content delivery networks
- **5G Edge**: Use 5G edge computing for AI-powered apps
- **Fog Computing**: Process AI in fog computing environments

## Installation and Setup

### Extension Installation
Install di AI Toolkit extension from di Visual Studio Code Marketplace:

**Extension ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installation Methods**:
1. **VS Code Marketplace**: Search "AI Toolkit" for Extensions view
2. **Command Line**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direct Install**: Download from [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Prerequisites for Edge AI Development
- **Visual Studio Code**: Latest version recommended
- **Python Environment**: Python 3.8+ with AI libraries
- **ONNX Runtime** (Optional): For ONNX model inference
- **Ollama** (Optional): For local model serving
- **Hardware Acceleration Tools**: CUDA, OpenVINO, or platform-specific accelerators

### Initial Configuration
1. **Extension Activation**: Open VS Code and confirm AI Toolkit dey for Activity Bar
2. **Model Provider Setup**: Configure access to GitHub, OpenAI, Anthropic, or other providers
3. **Local Environment**: Set up Python environment and install packages
4. **Hardware Acceleration**: Configure GPU/NPU acceleration if available
5. **MCP Integration**: Set up Model Context Protocol servers if needed

### First-Time Setup Checklist
- [ ] AI Toolkit extension installed and activated
- [ ] Model catalog dey accessible
- [ ] Playground dey work for model testing
- [ ] Agent Builder dey available for prompt development
- [ ] Local development environment dey ready
- [ ] Hardware acceleration (if available) dey configured

## Getting Started with AI Toolkit

### Quick Start Guide

We recommend say you start with models wey GitHub dey host for easy experience:

1. **Installation**: Follow di [installation guide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) to set up AI Toolkit
2. **Model Discovery**: From di extension tree view, select **CATALOG > Models** to explore models
3. **GitHub Models**: Start with GitHub-hosted models for better integration
4. **Playground Testing**: From any model card, select **Try in Playground** to test model features

### Step-by-Step Edge AI Development

#### Step 1: Model Exploration and Selection
1. Open AI Toolkit view for VS Code Activity Bar
2. Browse Model Catalog for edge deployment models
3. Filter by provider (GitHub, ONNX, Ollama) based on edge needs
4. Use **Try in Playground** to test model features

#### Step 2: Agent Development
1. Use **Prompt (Agent) Builder** to create edge-optimized AI agents
2. Generate starter prompts wit natural language description
3. Change an fix prompts based on wetin model dey respond
4. Use MCP tools to make agent sabi work well well

#### Step 3: Testing an Evaluation
1. Use **Bulk Run** test plenty prompts for different models wey you choose
2. Run agents wit test cases to make sure say e dey work well
3. Check how correct an fast e dey work wit built-in or custom metrics
4. Compare different models an configurations

#### Step 4: Fine-tuning an Optimization
1. Change models to fit special edge use cases
2. Use domain-specific fine-tuning
3. Make am better for edge deployment constraints
4. Version an compare different agent configurations

#### Step 5: Deployment Preparation
1. Create production-ready code wit Agent Builder
2. Connect MCP server for production use
3. Prepare deployment packages for edge devices
4. Set up monitoring an evaluation metrics

## Samples for AI Toolkit 

Try Our Samples
The [AI Toolkit samples](https://github.com/Azure-Samples/AI_Toolkit_Samples) dey help developers an researchers to sabi an use AI solutions well.

Our samples get:

Sample Code: Pre-built examples wey dey show AI functionalities, like training, deploying, or putting models inside applications.
Documentation: Guides an tutorials wey go help users understand AI Toolkit features an how dem go use am.
Prequisites

- Visual Studio Code
- AI Toolkit for Visual Studio Code
- GitHub Fine-grained personal access token (PAT)
- Foundry Local

## Best Practices for Edge AI Development

### Model Selection
- **Size Constraints**: Pick models wey go fit inside memory wey dey target devices
- **Inference Speed**: Choose models wey dey fast for real-time applications
- **Accuracy Trade-offs**: Balance model accuracy wit resource constraints
- **Format Compatibility**: Use ONNX or hardware-optimized formats for edge deployment

### Optimization Techniques
- **Quantization**: Use INT8 or INT4 quantization to make model small an fast
- **Pruning**: Remove model parameters wey no dey necessary to reduce computational requirements
- **Knowledge Distillation**: Create smaller models wey still dey perform like big ones
- **Hardware Acceleration**: Use NPUs, GPUs, or special accelerators if dem dey

### Development Workflow
- **Iterative Testing**: Test am plenty times for edge-like conditions during development
- **Performance Monitoring**: Always dey check resource usage an inference speed
- **Version Control**: Keep track of model versions an optimization settings
- **Documentation**: Write down all optimization decisions an performance trade-offs

### Deployment Considerations
- **Resource Monitoring**: Check memory, CPU, an power usage for production
- **Fallback Strategies**: Put fallback plans for when model no work
- **Update Mechanisms**: Plan how you go dey update model an manage versions
- **Security**: Make sure say edge AI applications dey secure

## Integration wit Edge AI Frameworks

### ONNX Runtime
- **Cross-platform Deployment**: Deploy ONNX models for different edge platforms
- **Hardware Optimization**: Use ONNX Runtime hardware-specific optimizations
- **Mobile Support**: Use ONNX Runtime Mobile for phone an tablet applications
- **IoT Integration**: Deploy for IoT devices wit ONNX Runtime lightweight distributions

### Windows ML
- **Windows Devices**: Make am better for Windows-based edge devices an PCs
- **NPU Acceleration**: Use Neural Processing Units for Windows devices
- **DirectML**: Use DirectML for GPU acceleration for Windows platforms
- **UWP Integration**: Put am inside Universal Windows Platform applications

### TensorFlow Lite
- **Mobile Optimization**: Deploy TensorFlow Lite models for phone an embedded devices
- **Hardware Delegates**: Use special hardware delegates for acceleration
- **Micro Controllers**: Deploy for microcontrollers wit TensorFlow Lite Micro
- **Cross-platform Support**: Deploy for Android, iOS, an embedded Linux systems

### Azure IoT Edge
- **Cloud-Edge Hybrid**: Mix cloud training wit edge inference
- **Module Deployment**: Deploy AI models as IoT Edge modules
- **Device Management**: Manage edge devices an model updates from far
- **Telemetry**: Collect performance data an model metrics from edge deployments

## Advanced Edge AI Scenarios

### Multi-Model Deployment
- **Model Ensembles**: Deploy plenty models for better accuracy or backup
- **A/B Testing**: Test different models at the same time for edge devices
- **Dynamic Selection**: Pick models based on how device dey perform
- **Resource Sharing**: Make sure say resources dey share well for plenty deployed models

### Federated Learning
- **Distributed Training**: Train models for plenty edge devices
- **Privacy Preservation**: Keep training data local but share model improvements
- **Collaborative Learning**: Make devices learn from each other experience
- **Edge-Cloud Coordination**: Make edge devices an cloud dey work together for learning

### Real-time Processing
- **Stream Processing**: Process continuous data streams for edge devices
- **Low-latency Inference**: Make inference dey fast well well
- **Batch Processing**: Process batches of data well for edge devices
- **Adaptive Processing**: Change processing based on how device dey perform

## Troubleshooting Edge AI Development

### Common Issues
- **Memory Constraints**: Model too big for device memory
- **Inference Speed**: Model inference too slow for real-time use
- **Accuracy Degradation**: Optimization make model accuracy no good
- **Hardware Compatibility**: Model no fit work for target hardware

### Debugging Strategies
- **Performance Profiling**: Use AI Toolkit tracing features to find bottlenecks
- **Resource Monitoring**: Check memory an CPU usage during development
- **Incremental Testing**: Test optimizations small small to find issues
- **Hardware Simulation**: Use development tools to simulate target hardware

### Optimization Solutions
- **Further Quantization**: Use more aggressive quantization techniques
- **Model Architecture**: Try different model architectures wey fit edge
- **Preprocessing Optimization**: Make data preprocessing better for edge constraints
- **Inference Optimization**: Use hardware-specific inference optimizations

## Resources an Next Steps

### Official Documentation
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)
- [Installation an Setup Guide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [VS Code Intelligent Apps Documentation](https://code.visualstudio.com/docs/intelligentapps)
- [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io/)

### Community an Support
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub Issues an Feature Requests](https://aka.ms/AIToolkit/feedback)
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
- **Security**: Microsoft security policies dey apply
- **Telemetry**: E dey respect VS Code telemetry settings

## Conclusion

AI Toolkit for Visual Studio Code na better platform for modern AI development, e dey make agent development easy an e good well well for Edge AI applications. Wit plenty model catalog wey support providers like Anthropic, OpenAI, GitHub, an Google, plus local execution wit ONNX an Ollama, the toolkit dey flexible for different edge deployment scenarios.

The toolkit strong because e dey combine everything—from model discovery an testing for Playground to agent development wit Prompt Builder, evaluation features, an MCP tool integration. For Edge AI developers, e mean say dem fit quickly test an prototype AI agents before dem deploy am for edge, an dem fit optimize am for resource-constrained environments.

Key advantages for Edge AI development na:
- **Rapid Experimentation**: Test models an agents fast before edge deployment
- **Multi-Provider Flexibility**: Use models from different sources to find better edge solutions
- **Local Development**: Test wit ONNX an Ollama for offline an privacy-preserving development
- **Production Readiness**: Create production-ready code an connect wit external tools via MCP
- **Comprehensive Evaluation**: Use built-in an custom metrics to check edge AI performance

As AI dey move go edge deployment scenarios, AI Toolkit for VS Code dey give developers wetin dem need to build, test, an optimize intelligent applications for resource-constrained environments. Whether na IoT solutions, mobile AI applications, or embedded intelligence systems, the toolkit features an workflow dey support the whole edge AI development process.

Wit ongoing development an active community (1.8k+ GitHub stars), AI Toolkit dey lead for AI development tools, an e dey grow to meet wetin modern AI developers need for edge deployment scenarios.

[Next Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg make you sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important mata, e good make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->