# Windows Edge AI Development Guide

## Introduction

Welcome to Windows Edge AI Development - your all-in-one guide to creating intelligent applications that utilize on-device AI through Microsoft's Windows AI Foundry platform. This guide is tailored for Windows developers aiming to incorporate advanced Edge AI features into their applications while taking full advantage of Windows hardware acceleration.

### The Windows AI Advantage

Windows AI Foundry offers a unified, dependable, and secure platform that supports the entire AI development lifecycle—from model selection and fine-tuning to optimization and deployment across CPU, GPU, NPU, and hybrid cloud architectures. This platform democratizes AI development by providing:

- **Hardware Abstraction**: Effortless deployment across AMD, Intel, NVIDIA, and Qualcomm hardware
- **On-Device Intelligence**: Privacy-focused AI that operates entirely on local hardware
- **Optimized Performance**: Models pre-configured for Windows hardware setups
- **Enterprise-Ready**: Security and compliance features suitable for production environments

### Windows ML 
Windows Machine Learning (ML) allows developers using C#, C++, and Python to run ONNX AI models locally on Windows PCs via the ONNX Runtime, with automatic management of execution providers for various hardware (CPUs, GPUs, NPUs). [ONNX Runtime](https://onnxruntime.ai/docs/) supports models from PyTorch, Tensorflow/Keras, TFLite, scikit-learn, and other frameworks.

![WindowsML A diagram illustrating an ONNX model going through Windows ML to then reach NPUs, GPUs, and CPUs.l](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML includes a shared Windows-wide copy of the ONNX Runtime and the ability to dynamically download execution providers (EPs).

### Why Windows for Edge AI?

**Universal Hardware Support**
Windows ML automatically optimizes hardware across the Windows ecosystem, ensuring your AI applications perform efficiently regardless of the underlying silicon architecture.

**Integrated AI Runtime**
The built-in Windows ML inference engine simplifies setup, enabling developers to focus on application logic rather than infrastructure.

**Copilot+ PC Optimization**
Specialized APIs designed for next-generation Windows devices with dedicated Neural Processing Units (NPUs) deliver outstanding performance per watt.

**Developer Ecosystem**
Comprehensive tools, including Visual Studio integration, detailed documentation, and sample applications, accelerate development cycles.

## Learning Objectives

By completing this Windows Edge AI development guide, you will acquire the essential skills to create production-ready AI applications on the Windows platform.

### Core Technical Competencies

**Windows AI Foundry Mastery**
- Understand the architecture and components of the Windows AI Foundry platform
- Navigate the full AI development lifecycle within the Windows ecosystem
- Apply security best practices for on-device AI applications
- Optimize applications for various Windows hardware configurations

**API Integration Expertise**
- Master Windows AI APIs for text, vision, and multimodal applications
- Integrate the Phi Silica language model for text generation and reasoning
- Deploy computer vision features using built-in image processing APIs
- Customize pre-trained models using LoRA (Low-Rank Adaptation) techniques

**Foundry Local Implementation**
- Explore, evaluate, and deploy open-source language models using Foundry Local CLI
- Understand model optimization and quantization for local deployment
- Implement offline AI capabilities that work without internet connectivity
- Manage model lifecycles and updates in production environments

**Windows ML Deployment**
- Integrate custom ONNX models into Windows applications using Windows ML
- Utilize automatic hardware acceleration across CPU, GPU, and NPU architectures
- Implement real-time inference with optimal resource utilization
- Design scalable AI applications for diverse Windows device categories

### Application Development Skills

**Cross-Platform Windows Development**
- Create AI-powered applications using .NET MAUI for universal Windows deployment
- Add AI features to Win32, UWP, and Progressive Web Applications
- Design responsive UIs that adapt to AI processing states
- Handle asynchronous AI operations with user-friendly patterns

**Performance Optimization**
- Profile and enhance AI inference performance across different hardware setups
- Manage memory efficiently for large language models
- Design applications that adapt gracefully to available hardware capabilities
- Implement caching strategies for frequently used AI operations

**Production Readiness**
- Develop robust error handling and fallback mechanisms
- Design telemetry and monitoring for AI application performance
- Apply security best practices for local AI model storage and execution
- Plan deployment strategies for enterprise and consumer applications

### Business and Strategic Understanding

**AI Application Architecture**
- Design hybrid architectures that balance local and cloud AI processing
- Assess trade-offs between model size, accuracy, and inference speed
- Plan data flow architectures that ensure privacy while enabling intelligence
- Develop cost-effective AI solutions that scale with user needs

**Market Positioning**
- Understand the competitive advantages of Windows-native AI applications
- Identify scenarios where on-device AI delivers superior user experiences
- Create go-to-market strategies for AI-enhanced Windows applications
- Position applications to leverage the benefits of the Windows ecosystem

## Windows App SDK AI Samples

The Windows App SDK offers detailed samples showcasing AI integration across various frameworks and deployment scenarios. These samples are invaluable for understanding Windows AI development patterns.

### Windows AI Foundry Samples

| Sample | Framework | Focus Area | Key Features |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI APIs Integration | Complete WinUI app demonstrating Windows AI APIs, ARM64 optimization, packaged deployment |

**Key Technologies:**
- Windows AI APIs
- WinUI 3 framework
- ARM64 platform optimization
- Copilot+ PC compatibility
- Packaged app deployment

**Prerequisites:**
- Windows 11 with Copilot+ PC recommended
- Visual Studio 2022
- ARM64 build configuration
- Windows App SDK 1.8.1+

### Windows ML Samples

#### C++ Samples

| Sample | Type | Focus Area | Key Features |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | Basic Windows ML | EP discovery, command-line options, model compilation |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | Framework Deployment | Shared runtime, smaller deployment footprint |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | Self-Contained Deployment | Standalone deployment, no runtime dependencies |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Library Usage | WindowsML in shared library, memory management |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet Tutorial | Model conversion, EP compilation, Build 2025 tutorial |

#### C# Samples

**Console Applications**

| Sample | Type | Focus Area | Key Features |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Console App | Basic C# Integration | Shared helper usage, command-line interface |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet Tutorial | Model conversion, EP compilation, Build 2025 tutorial |

**GUI Applications**

| Sample | Framework | Focus Area | Key Features |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Image classification with WPF interface |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Traditional GUI | Image classification with Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Modern GUI | Image classification with WinUI 3 interface |

#### Python Samples

| Sample | Language | Focus Area | Key Features |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Image Classification | WinML Python bindings, batch image processing |

### Sample Prerequisites

**System Requirements:**
- Windows 11 PC running version 24H2 (build 26100) or greater
- Visual Studio 2022 with C++ and .NET workloads
- Windows App SDK 1.8.1 or later
- Python 3.10-3.13 for Python samples on x64 and ARM64 devices

**Windows AI Foundry Specific:**
- Copilot+ PC recommended for optimal performance
- ARM64 build configuration for Windows AI samples
- Package identity required (unpackaged apps no longer supported)

### Common Sample Workflow

Most Windows ML samples follow this standard pattern:

1. **Initialize Environment** - Create ONNX Runtime environment
2. **Register Execution Providers** - Discover and register available hardware accelerators (CPU, GPU, NPU)
3. **Load Model** - Load ONNX model, optionally compile for target hardware
4. **Preprocess Input** - Convert images/data to model input format
5. **Run Inference** - Execute model and get predictions
6. **Process Results** - Apply softmax and display top predictions

### Model Files Used

| Model | Purpose | Included | Notes |
|-------|---------|----------|-------|
| SqueezeNet | Lightweight image classification | ✅ Included | Pre-trained, ready to use |
| ResNet-50 | High-accuracy image classification | ❌ Requires conversion | Use [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) for conversion |

### Hardware Support

All samples automatically detect and utilize available hardware:
- **CPU** - Universal support across all Windows devices
- **GPU** - Automatic detection and optimization for available graphics hardware
- **NPU** - Leverages Neural Processing Units on supported devices (Copilot+ PCs)

## Windows AI Foundry Platform Components

### 1. Windows AI APIs

Windows AI APIs offer ready-to-use AI features powered by on-device models, optimized for efficiency and performance on Copilot+ PC devices with minimal setup required.

#### Core API Categories

**Phi Silica Language Model**
- Compact yet powerful language model for text generation and reasoning
- Optimized for real-time inference with low power consumption
- Supports custom fine-tuning using LoRA techniques
- Integrates with Windows semantic search and knowledge retrieval

**Computer Vision APIs**
- **Text Recognition (OCR)**: Extract text from images with high accuracy
- **Image Super Resolution**: Enhance image quality using local AI models
- **Image Segmentation**: Identify and isolate objects in images
- **Image Description**: Generate detailed text descriptions for visual content
- **Object Erase**: Remove unwanted objects from images using AI-powered inpainting

**Multimodal Capabilities**
- **Vision-Language Integration**: Combine text and image understanding
- **Semantic Search**: Enable natural language queries across multimedia content
- **Knowledge Retrieval**: Build intelligent search experiences with local data

### 2. Foundry Local

Foundry Local provides developers with quick access to ready-to-use open-source language models on Windows Silicon, enabling browsing, testing, interaction, and deployment of models in local applications.

#### Foundry Local Sample Applications

The [Foundry Local repository](https://github.com/microsoft/Foundry-Local/tree/main/samples) offers detailed samples across multiple programming languages and frameworks, showcasing various integration patterns and use cases.

| Sample | Language/Framework | Focus Area | Key Features |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG Implementation | Semantic Kernel integration, Qdrant vector store, JINA embeddings, document ingestion, streaming chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktop Chat App | Cross-platform chat, local/cloud model switching, OpenAI SDK integration, real-time streaming |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Basic Integration | Simple SDK usage, model initialization, basic chat functionality |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Basic Integration | Python SDK usage, streaming responses, OpenAI-compatible API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Systems Integration | Low-level SDK usage, async operations, reqwest HTTP client |

#### Sample Categories by Use Case

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Complete RAG implementation using Semantic Kernel, Qdrant vector database, and JINA embeddings
- **Architecture**: Document ingestion → Text chunking → Vector embeddings → Similarity search → Context-aware responses
- **Technologies**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, streaming chat completion

**Desktop Applications**
- **electron/foundry-chat**: Production-ready chat application with local/cloud model switching
- **Features**: Model selector, streaming responses, error handling, cross-platform deployment
- **Architecture**: Electron main process, IPC communication, secure preload scripts

**SDK Integration Examples**
- **JavaScript (Node.js)**: Basic model interaction and streaming responses
- **Python**: OpenAI-compatible API usage with async streaming
- **Rust**: Low-level integration with reqwest and tokio for async operations

#### Prerequisites for Foundry Local Samples

**System Requirements:**
- Windows 11 with Foundry Local installed
- Node.js v16+ for JavaScript/Electron samples
- .NET 8.0+ for C# samples
- Python 3.10+ for Python samples
- Rust 1.70+ for Rust samples

**Installation:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Sample-Specific Setup

**dotNET RAG Sample:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Chat Sample:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust Samples:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Key Features

**Model Catalog**
- Comprehensive collection of pre-optimized open-source models
- Models optimized across CPUs, GPUs, and NPUs for immediate deployment
- Support for popular model families including Llama, Mistral, Phi, and specialized domain models

**CLI Integration**
- Command-line interface for model management and deployment
- Automated optimization and quantization workflows
- Integration with popular development environments and CI/CD pipelines

**Local Deployment**
- Complete offline operation without cloud dependencies
- Support for custom model formats and configurations
- Efficient model serving with automatic hardware optimization

### 3. Windows ML

Windows ML serves as the core AI platform and integrated inferencing runtime on Windows, allowing developers to deploy custom models efficiently across the broad Windows hardware ecosystem.

#### Architecture Benefits

**Universal Hardware Support**
- Automatic optimization for AMD, Intel, NVIDIA, and Qualcomm silicon
- Support for CPU, GPU, and NPU execution with transparent switching
- Hardware abstraction that eliminates platform-specific optimization work

**Model Flexibility**
- Support for ONNX model format with automatic conversion from popular frameworks
- Custom model deployment with production-grade performance
- Integration with existing Windows application architectures

**Enterprise Integration**
- Compatible with Windows security and compliance frameworks
- Support for enterprise deployment and management tools
- Integration with Windows device management and monitoring systems

## Development Workflow

### Phase 1: Environment Setup and Tool Configuration

**Development Environment Preparation**
1. Install Visual Studio 2022 with C++ and .NET workloads
2. Install Windows App SDK 1.8.1 or later
3. Configure Windows AI Foundry CLI tools
4. Set up AI Toolkit extension for Visual Studio Code
5. Establish performance profiling and monitoring tools
6. Ensure ARM64 build configuration for Copilot+ PC optimization

**Sample Repository Setup**
1. Clone the [Windows App SDK Samples repository](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Navigate to `Samples/WindowsAIFoundry/cs-winui` for Windows AI API examples
3. Navigate to `Samples/WindowsML` for comprehensive Windows ML examples
4. Review the [build requirements](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) for your target platforms

**AI Dev Gallery Exploration**
- Explore sample applications and reference implementations
- Test Windows AI APIs with interactive demonstrations
- Review source code for best practices and patterns
- Identify relevant samples for your specific use case

### Phase 2: Model Selection and Integration

**Requirements Analysis**
- Define functional requirements for AI capabilities
- Establish performance constraints and optimization targets
- Evaluate privacy and security requirements
- Plan deployment architecture and scaling strategies

**Model Evaluation**
- Use Foundry Local to test open-source models for your use case
- Benchmark Windows AI APIs against custom model requirements
- Evaluate trade-offs between model size, accuracy, and inference speed
- Prototype integration approaches with selected models

### Phase 3: Application Development

**Core Integration**
- Implement Windows AI API integration with proper error handling
- Design user interfaces that accommodate AI processing workflows
- Implement caching and optimization strategies for model inference
- Add telemetry and monitoring for AI operation performance

**Testing and Validation**
- Test applications across different Windows hardware configurations
- Validate performance metrics under various load conditions
- Implement automated testing for AI functionality reliability
- Conduct user experience testing with AI-enhanced features

### Phase 4: Optimization and Deployment

**Performance Optimization**
- Profile application performance across target hardware configurations
- Optimize memory usage and model loading strategies
- Implement adaptive behavior based on available hardware capabilities
- Fine-tune user experience for different performance scenarios

**Production Deployment**
- Package applications with proper AI model dependencies
- Implement update mechanisms for models and application logic
- Configure monitoring and analytics for production environments
- Plan rollout strategies for enterprise and consumer deployments

## Practical Implementation Examples

### Example 1: Intelligent Document Processing Application

Build a Windows application that processes documents using multiple AI capabilities:

**Technologies Used:**
- Phi Silica for document summarization and question answering
- OCR APIs for text extraction from scanned documents
- Image Description APIs for chart and diagram analysis
- Custom ONNX models for document classification

**Implementation Approach:**
- Design modular architecture with pluggable AI components
- Implement async processing for large document batches
- Add progress indicators and cancellation support for long-running operations
- Include offline capability for sensitive document processing

### Example 2: Retail Inventory Management System

Create an AI-powered inventory system for retail applications:

**Technologies Used:**
- Image Segmentation for product identification
- Custom vision models for brand and category classification
- Foundry Local deployment of specialized retail language models
- Integration with existing POS and inventory systems

**Implementation Approach:**
- Build camera integration for real-time product scanning
- Implement barcode and visual product recognition
- Add natural language inventory queries using local language models
- Design scalable architecture for multi-store deployment

### Example 3: Healthcare Documentation Assistant

Develop a privacy-preserving healthcare documentation tool:

**Technologies Used:**
- Phi Silica for medical note generation and clinical decision support
- OCR for digitizing handwritten medical records
- Custom medical language models deployed via Windows ML
- Local vector storage for medical knowledge retrieval

**Implementation Approach:**
- Ensure complete offline operation for patient privacy
- Implement medical terminology validation and suggestion
- Add audit logging for regulatory compliance
- Design integration with existing Electronic Health Record systems

## Performance Optimization Strategies

### Hardware-Aware Development

**NPU Optimization**
- Design applications to leverage NPU capabilities on Copilot+ PCs
- Implement graceful fallback to GPU/CPU on devices without NPU
- Optimize model formats for NPU-specific acceleration
- Monitor NPU utilization and thermal characteristics

**Memory Management**
- Implement efficient model loading and caching strategies
- Use memory mapping for large models to reduce startup time
- Design memory-conscious applications for resource-constrained devices
- Implement model quantization for memory optimization

**Battery Efficiency**
- Optimize AI operations for minimal power consumption
- Implement adaptive processing based on battery status
- Design efficient background processing for continuous AI operations
- Use power profiling tools to optimize energy usage

### Scalability Considerations

**Multi-Threading**
- Design thread-safe AI operations for concurrent processing
- Implement efficient work distribution across available cores
- Use async/await patterns for non-blocking AI operations
- Plan thread pool optimization for different hardware configurations

**Caching Strategies**
- Implement intelligent caching for frequently used AI operations
- Design cache invalidation strategies for model updates
- Use persistent caching for expensive preprocessing operations
- Implement distributed caching for multi-user scenarios

## Security and Privacy Best Practices

### Data Protection

**Local Processing**
- Ensure sensitive data never leaves the local device
- Implement secure storage for AI models and temporary data
- Use Windows security features for application sandboxing
- Apply encryption for stored models and intermediate processing results

**Model Security**
- Validate model integrity before loading and execution
- Implement secure model update mechanisms
- Use signed models to prevent tampering
- Apply access controls for model files and configuration

### Compliance Considerations

**Regulatory Alignment**
- Design applications to meet GDPR, HIPAA, and other regulatory requirements
- Implement audit logging for AI decision-making processes
- Provide transparency features for AI-generated results
- Enable user control over AI data processing

**Enterprise Security**
- Integrate with Windows enterprise security policies
- Support managed deployment through enterprise management tools
- Implement role-based access controls for AI features
- Provide administrative controls for AI functionality

## Troubleshooting and Debugging

### Common Development Challenges

**Build Configuration Issues**
- Ensure ARM64 platform configuration for Windows AI API samples
- Verify Windows App SDK version compatibility (1.8.1+ required)
- Check that package identity is properly configured (required for Windows AI APIs)
- Validate that build tools support the target framework version

**Model Loading Issues**
- Validate ONNX model compatibility with Windows ML
- Check model file integrity and format requirements
- Verify hardware capability requirements for specific models
- Debug memory allocation issues during model loading
- Ensure execution provider registration for hardware acceleration

**Deployment Mode Considerations**
- **Self-Contained Mode**: Fully supported with larger deployment size
- **Framework-Dependent Mode**: Smaller footprint but requires shared runtime
- **Unpackaged Applications**: No longer supported for Windows AI APIs
- Use `dotnet run -p:Platform=ARM64 -p:SelfContained=true` for self-contained ARM64 deployment

**Performance Problems**
- Profile application performance across different hardware configurations
- Identify bottlenecks in AI processing pipelines
- Optimize data preprocessing and postprocessing operations
- Implement performance monitoring and alerting

**Integration Difficulties**
- Debug API integration issues with proper error handling
- Validate input data formats and preprocessing requirements
- Test edge cases and error conditions thoroughly
- Implement comprehensive logging for debugging production issues

### Debugging Tools and Techniques

**Visual Studio Integration**
- Use AI Toolkit debugger for model execution analysis
- Implement performance profiling for AI operations
- Debug async AI operations with proper exception handling
- Use memory profiling tools for optimization

**Windows AI Foundry Tools**
- Leverage Foundry Local CLI for model testing and validation
- Use Windows AI API testing tools for integration verification
- Implement custom logging for AI operation monitoring
- Create automated testing for AI functionality reliability

## Future-Proofing Your Applications

### Emerging Technologies

**Next-Generation Hardware**
- Design applications to leverage future NPU capabilities
- Plan for increased model sizes and complexity
- Implement adaptive architectures for evolving hardware
- Consider quantum-ready algorithms for future compatibility

**Advanced AI Capabilities**
- Prepare for multimodal AI integration across more data types
- Plan for real-time collaborative AI between multiple devices
- Design for federated learning capabilities
- Consider edge-cloud hybrid intelligence architectures

### Continuous Learning and Adaptation

**Model Updates**
- Implement seamless model update mechanisms
- Design applications to adapt to improved model capabilities
- Plan for backward compatibility with existing models
- Implement A/B testing for model performance evaluation

**Feature Evolution**
- Design modular architectures that accommodate new AI capabilities
- Plan for integration of emerging Windows AI APIs
- Implement feature flags for gradual capability rollout
- Design user interfaces that adapt to enhanced AI features

## Conclusion

Windows Edge AI development represents the convergence of powerful AI capabilities with the robust, secure, and scalable Windows platform. By mastering the Windows AI Foundry ecosystem, developers can create intelligent applications that provide exceptional user experiences while maintaining the highest standards of privacy, security, and performance.

The combination of Windows AI APIs, Foundry Local, and Windows ML provides an unparalleled foundation for building the next generation of intelligent Windows applications. As AI continues to evolve, the Windows platform ensures that your applications will scale with emerging technologies while maintaining compatibility and performance across the diverse Windows hardware ecosystem.

Whether you're building consumer applications, enterprise solutions, or specialized industry tools, Windows Edge AI development empowers you to create intelligent, responsive, and deeply integrated experiences that leverage the full potential of modern Windows devices.

## Additional Resources

### Documentation and Learning
- [Windows AI Foundry Documentation](https://learn.microsoft.com/windows/ai/)
- [Windows AI APIs Reference](https://learn.microsoft.com/windows/ai/apis/)
- [Get started building an app with Windows AI APIs](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local Getting Started](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML Overview](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK System Requirements](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Windows App SDK Development Environment Setup](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Sample Repositories and Code
- [Windows App SDK Samples - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK Samples - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Inference Examples](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK Samples Repository](https://github.com/microsoft/WindowsAppSDK-Samples)

### Development Tools
- [AI Toolkit for Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Samples](https://learn.microsoft.com/windows/ai/samples/)
- [Model Conversion Tools](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Technical Support
- [Windows ML Documentation](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Documentation](https://onnxruntime.ai/docs/)
- [Windows App SDK Documentation](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Report Issues - Windows App SDK Samples](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Community and Support
- [Windows Developer Community](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Training](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*This guide is designed to evolve with the rapidly advancing Windows AI ecosystem. Regular updates ensure alignment with the latest platform capabilities and development best practices.*

[08. Hands on With Microsoft Foundry Local - Complete Developer Toolkit](../Module08/README.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.