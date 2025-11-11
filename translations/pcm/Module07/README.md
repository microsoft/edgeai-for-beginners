<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c86f39ae10a967d9b337934c067b64f9",
  "translation_date": "2025-11-11T17:54:06+00:00",
  "source_file": "Module07/README.md",
  "language_code": "pcm"
}
-->
# Chapter 07 : EdgeAI Samples

Edge AI na di mix wey dey happen between artificial intelligence and edge computing, wey go make am possible to process things wey dey smart directly for device, no need to depend on cloud connection. Dis chapter go show five different EdgeAI setups for different platforms and frameworks, wey go show how flexible and strong AI models fit run for edge.

## 1. EdgeAI for NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano na big step for edge AI computing wey people fit afford, e dey deliver up to 67 TOPS AI performance for small size wey be like credit card. Dis strong edge AI platform dey make generative AI development easy for hobby people, students, and professional developers.

### Key Features
- E dey deliver up to 67 TOPS AI performance—1.7X better pass di one wey dey before am
- 1024 CUDA cores and up to 32 Tensor Cores for AI processing
- 6-core Arm Cortex-A78AE v8.2 64-bit CPU wey fit reach maximum speed of 1.5 GHz
- E dey cost only $249, wey go make am easy for developers, students, and makers to use am

### Applications
Jetson Orin Nano sabi run modern generative AI models like vision transformers, big language models, and vision-language models. E dey specially design for GenAI use cases and now you fit run plenty LLMs for palm device. Popular use cases na AI-powered robots, smart drones, intelligent cameras, and autonomous edge devices.

**Learn More**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI for Mobile Apps with .NET MAUI and ONNX Runtime GenAI

Dis solution dey show how to put Generative AI and Large Language Models (LLMs) inside mobile apps wey fit work for different platforms using .NET MAUI (Multi-platform App UI) and ONNX Runtime GenAI. Dis method go help .NET developers build strong AI-powered mobile apps wey go work well for Android and iOS devices.

### Key Features
- E dey use .NET MAUI framework, wey go make am possible to use one code for both Android and iOS apps
- ONNX Runtime GenAI dey allow generative AI models to run directly for mobile devices
- E dey support different hardware accelerators wey dey fit mobile devices, like CPU, GPU, and special mobile AI processors
- E get platform-specific optimizations like CoreML for iOS and NNAPI for Android through ONNX Runtime
- E dey do full generative AI process like pre and post processing, inference, logits processing, search and sampling, and KV cache management

### Development Benefits
With .NET MAUI, developers fit use di C# and .NET skills wey dem already get to build cross-platform AI apps. ONNX Runtime GenAI dey support plenty model types like Llama, Mistral, Phi, Gemma, and others. Optimized ARM64 kernels dey make INT4 quantized matrix multiplication fast, wey go make di mobile hardware perform well while still dey use di normal .NET development style.

### Use Cases
Dis solution dey perfect for developers wey wan build AI-powered mobile apps using .NET technologies, like smart chatbots, image recognition apps, language translation tools, and personalized recommendation systems wey dey work offline and dey protect privacy.

**Learn More**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI for Azure with Small Language Models Engine

Microsoft Azure EdgeAI solution dey focus on how to deploy Small Language Models (SLMs) well for cloud-edge hybrid environments. Dis method dey connect di gap between big cloud AI services and edge deployment needs.

### Architecture Advantages
- E dey work well with Azure AI services
- Fit run SLMs/LLMs and multi-modal models for device and cloud with ONNX Runtime
- E dey optimized for enterprise-level deployment
- E dey support continuous model updates and management

### Use Cases
Azure EdgeAI dey shine for enterprise-level AI deployment wey need cloud management. E dey good for things like smart document processing, real-time analytics, and hybrid AI workflows wey dey use both cloud and edge computing.

**Learn More**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI with Windows ML](./windowdeveloper.md)

Windows ML na Microsoft runtime wey dey optimized for fast on-device model inference and easy deployment, e dey serve as di base for Windows AI Foundry. Dis platform dey help developers create AI-powered Windows apps wey go use di full power of PC hardware.

### Platform Capabilities
- E dey work for all Windows 11 PCs wey dey run version 24H2 (build 26100) or higher
- E dey work for all x64 and ARM64 PC hardware, even PCs wey no get NPUs or GPUs
- E dey allow developers bring their own models and deploy am well across silicon partner ecosystem like AMD, Intel, NVIDIA, and Qualcomm wey dey include CPU, GPU, NPU
- With infrastructure APIs, developers no need to create different builds of their app to target different silicon

### Developer Benefits
Windows ML dey handle di hardware and execution providers, so developers fit focus on di code wey dem dey write. Plus, Windows ML dey update by itself to support di latest NPUs, GPUs, and CPUs as dem dey release. Di platform dey provide one framework for AI development across di different Windows hardware.

**Learn More**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md) - Full guide for Windows Edge AI development

## [5. EdgeAI with Foundry Local Applications](./foundrylocal.md)

Foundry Local dey allow Windows and Mac developers build Retrieval Augmented Generation (RAG) apps using local resources for .NET, wey dey mix local language models with semantic search. Dis method dey provide AI solutions wey dey focus on privacy and dey work only for local infrastructure.

### Technical Architecture
- E dey mix Phi language model, Local Embeddings, and Semantic Kernel to create RAG setup
- E dey use embeddings as vectors (arrays) of floating-point values wey dey represent content and di semantic meaning
- Semantic Kernel dey act as di main controller, e dey mix Phi and Smart Components to create smooth RAG pipeline
- E dey support local vector databases like SQLite and Qdrant

### Implementation Benefits
RAG, or Retrieval Augmented Generation, na just big grammar wey mean "find some info and put am inside di prompt". Dis local setup dey make sure say data dey private while e dey provide smart answers wey dey based on custom knowledge bases. Dis method dey useful for enterprise setups wey need data privacy and offline operation.

**Learn More**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local dey provide OpenAI‑compatible REST server wey ONNX Runtime dey power to run models locally for Windows. Below na quick summary wey don validate; check official docs for full details.

- Get started: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Full Windows guide for dis repo: [foundrylocal.md](./foundrylocal.md)

Install or upgrade for Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Check CLI categories:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Run model and find di dynamic endpoint:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Quick REST check to list models (replace PORT from status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tips:
- SDK integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Bring your own model (compile): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI Development Resources

For developers wey dey target Windows platform, we don create full guide wey cover di complete Windows EdgeAI ecosystem. Dis resource dey provide detailed info about Windows AI Foundry, including APIs, tools, and best practices for EdgeAI development for Windows.

### Windows AI Foundry Platform
Windows AI Foundry platform dey provide full tools and APIs wey dey specially design for Edge AI development for Windows devices. Dis include special support for NPU-accelerated hardware, Windows ML integration, and platform-specific optimization methods.

**Comprehensive Guide**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Dis guide dey cover:
- Windows AI Foundry platform overview and components
- Phi Silica API for fast inference for NPU hardware
- Computer Vision APIs for image processing and OCR
- Windows ML runtime integration and optimization
- Foundry Local CLI for local development and testing
- Hardware optimization methods for Windows devices
- Practical examples and best practices

### [AI Toolkit for Edge AI Development](./aitoolkit.md)
For developers wey dey use Visual Studio Code, di AI Toolkit extension dey provide full development environment wey dey specially design for building, testing, and deploying Edge AI apps. Dis toolkit dey make di whole Edge AI development process easy inside VS Code.

**Development Guide**: [AI Toolkit for Edge AI Development](./aitoolkit.md)

Di AI Toolkit guide dey cover:
- Model discovery and selection for edge deployment
- Local testing and optimization process
- ONNX and Ollama integration for edge models
- Model conversion and quantization methods
- Agent development for edge setups
- Performance check and monitoring
- Deployment preparation and best practices

## Conclusion

Dis five EdgeAI setups dey show how mature and different edge AI solutions don dey today. From hardware-accelerated edge devices like Jetson Orin Nano to software frameworks like ONNX Runtime GenAI and Windows ML, developers get plenty options to deploy smart apps for edge.

Di main thing wey dey connect all dis platforms na di way dem dey make AI easy for developers wey get different levels of skills and needs. Whether na mobile apps, desktop software, or embedded systems, dis EdgeAI solutions dey provide di base for di next generation of smart apps wey go work well and keep things private for edge.

Each platform get im own special benefits: Jetson Orin Nano for hardware-accelerated edge computing, ONNX Runtime GenAI for cross-platform mobile development, Azure EdgeAI for enterprise cloud-edge integration, Windows ML for Windows-native apps, and Foundry Local for privacy-focused RAG setups. Together, dem dey form one complete ecosystem for EdgeAI development.

[Next AI Toolkit](aitoolkit.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->