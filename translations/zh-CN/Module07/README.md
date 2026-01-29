# 第七章：EdgeAI 示例

边缘人工智能（Edge AI）是人工智能与边缘计算的结合，使设备能够直接进行智能处理，而无需依赖云连接。本章将探讨五种不同平台和框架上的 EdgeAI 实现，展示在边缘运行 AI 模型的多样性和强大功能。

## 1. NVIDIA Jetson Orin Nano 的 EdgeAI

NVIDIA Jetson Orin Nano 是边缘 AI 计算领域的一项突破性产品，提供高达 67 TOPS 的 AI 性能，体积仅有信用卡大小。这款强大的边缘 AI 平台使生成式 AI 开发变得触手可及，无论是爱好者、学生还是专业开发者都能轻松使用。

### 主要特点
- 提供高达 67 TOPS 的 AI 性能，比前代产品提升 1.7 倍
- 配备 1024 个 CUDA 核心和最多 32 个 Tensor 核心，用于 AI 处理
- 6 核 Arm Cortex-A78AE v8.2 64 位 CPU，最高频率为 1.5 GHz
- 售价仅为 $249，为开发者、学生和创客提供最实惠且易于使用的平台

### 应用场景
Jetson Orin Nano 擅长运行现代生成式 AI 模型，包括视觉变换器、大型语言模型和视觉语言模型。它专为生成式 AI（GenAI）用例设计，现在可以在掌上设备上运行多个 LLM。常见应用场景包括 AI 驱动的机器人、智能无人机、智能摄像头和自主边缘设备。

**了解更多**：[NVIDIA 的 Jetson Orin Nano 超级计算机：边缘 AI 的下一大突破](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. 使用 .NET MAUI 和 ONNX Runtime GenAI 的移动应用 EdgeAI

此解决方案展示了如何将生成式 AI 和大型语言模型（LLMs）集成到跨平台移动应用中，使用 .NET MAUI（多平台应用 UI）和 ONNX Runtime GenAI。这种方法使 .NET 开发者能够构建在 Android 和 iOS 设备上原生运行的复杂 AI 驱动移动应用。

### 主要特点
- 基于 .NET MAUI 框架，提供单一代码库支持 Android 和 iOS 应用
- 集成 ONNX Runtime GenAI，可直接在移动设备上运行生成式 AI 模型
- 支持针对移动设备的各种硬件加速器，包括 CPU、GPU 和专用移动 AI 处理器
- 平台特定优化，例如 iOS 的 CoreML 和 Android 的 NNAPI，通过 ONNX Runtime 实现
- 实现完整的生成式 AI 流程，包括预处理和后处理、推理、logits 处理、搜索和采样以及 KV 缓存管理

### 开发优势
使用 .NET MAUI 方法，开发者可以利用现有的 C# 和 .NET 技能，同时构建跨平台 AI 应用。ONNX Runtime GenAI 框架支持多种模型架构，包括 Llama、Mistral、Phi、Gemma 等。优化的 ARM64 内核加速 INT4 量化矩阵乘法，确保在移动硬件上高效运行，同时保持熟悉的 .NET 开发体验。

### 应用场景
此解决方案非常适合希望使用 .NET 技术构建 AI 驱动移动应用的开发者，包括智能聊天机器人、图像识别应用、语言翻译工具和个性化推荐系统，这些应用完全在设备上运行，增强隐私性和离线能力。

**了解更多**：[.NET MAUI ONNX Runtime GenAI 示例](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. 使用小型语言模型引擎的 Azure EdgeAI

微软基于 Azure 的 EdgeAI 解决方案专注于在云边混合环境中高效部署小型语言模型（SLMs）。这种方法弥合了云规模 AI 服务与边缘部署需求之间的差距。

### 架构优势
- 与 Azure AI 服务无缝集成
- 使用 ONNX Runtime 在设备和云端运行 SLMs/LLMs 和多模态模型
- 针对企业级部署进行优化
- 支持持续的模型更新和管理

### 应用场景
Azure EdgeAI 实现擅长需要企业级 AI 部署和云管理能力的场景，包括智能文档处理、实时分析和利用云与边缘计算资源的混合 AI 工作流。

**了解更多**：[Azure EdgeAI SLM 引擎](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. 使用 Windows ML 的 EdgeAI](./windowdeveloper.md)

Windows ML 是微软优化的运行时，专为高效的设备端模型推理和简化部署而设计，是 Windows AI Foundry 的基础。该平台使开发者能够创建利用 PC 硬件全能力的 AI 驱动 Windows 应用。

### 平台能力
- 适用于所有运行版本 24H2（构建 26100）或更高版本的 Windows 11 PC
- 适用于所有 x64 和 ARM64 PC 硬件，即使是没有 NPU 或 GPU 的 PC
- 允许开发者使用自己的模型，并高效部署到包括 AMD、Intel、NVIDIA 和 Qualcomm 在内的硅合作伙伴生态系统，涵盖 CPU、GPU、NPU
- 利用基础设施 API，开发者无需为不同的硅目标创建多个应用构建版本

### 开发者优势
Windows ML 抽象了硬件和执行提供者，因此开发者可以专注于编写代码。此外，Windows ML 会自动更新以支持最新的 NPU、GPU 和 CPU。该平台为 Windows 硬件生态系统提供了统一的 AI 开发框架。

**了解更多**：
- [Windows ML 概述](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI 开发指南](./windowdeveloper.md) - Windows Edge AI 开发的全面指南

## [5. 使用 Foundry Local 应用的 EdgeAI](./foundrylocal.md)

Foundry Local 使 Windows 和 Mac 开发者能够使用本地资源在 .NET 中构建检索增强生成（RAG）应用，将本地语言模型与语义搜索功能相结合。这种方法提供了完全在本地基础设施上运行的隐私保护 AI 解决方案。

### 技术架构
- 结合 Phi 语言模型、本地嵌入和语义内核创建 RAG 场景
- 使用嵌入作为浮点值数组，表示内容及其语义意义
- 语义内核作为主要协调器，集成 Phi 和智能组件，创建无缝的 RAG 管道
- 支持本地向量数据库，包括 SQLite 和 Qdrant

### 实现优势
RAG，即检索增强生成，是一种“查找信息并将其放入提示”的方式。这种本地实现确保数据隐私，同时提供基于自定义知识库的智能响应。该方法在需要数据主权和离线操作能力的企业场景中尤为有价值。

**了解更多**：
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG 示例](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

微软 Foundry Local 提供了一个由 ONNX Runtime 驱动的 OpenAI 兼容 REST 服务器，用于在 Windows 上本地运行模型。以下是快速验证的摘要；完整详情请参阅官方文档。

- 入门指南：https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- 架构概述：https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI 参考：https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- 本仓库中的完整 Windows 指南：[foundrylocal.md](./foundrylocal.md)

在 Windows 上安装或升级（cmd.exe）：
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

探索 CLI 类别：
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

运行模型并发现动态端点：
```cmd
foundry model run gpt-oss-20b
foundry service status
```

快速 REST 检查列出模型（替换状态中的端口）：
```cmd
curl -s http://localhost:PORT/v1/models
```

提示：
- SDK 集成：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- 使用自己的模型（编译）：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI 开发资源

针对专门面向 Windows 平台的开发者，我们创建了一份全面指南，涵盖完整的 Windows EdgeAI 生态系统。该资源提供了有关 Windows AI Foundry 的详细信息，包括 API、工具和 Windows 上 EdgeAI 开发的最佳实践。

### Windows AI Foundry 平台
Windows AI Foundry 平台提供了一套专门为 Windows 设备上的 Edge AI 开发设计的工具和 API，包括对 NPU 加速硬件的专门支持、Windows ML 集成以及平台特定的优化技术。

**全面指南**：[Windows EdgeAI 开发指南](../windowdeveloper.md)

本指南涵盖：
- Windows AI Foundry 平台概述及组件
- Phi Silica API，用于 NPU 硬件上的高效推理
- 计算机视觉 API，用于图像处理和 OCR
- Windows ML 运行时集成与优化
- Foundry Local CLI，用于本地开发和测试
- Windows 设备的硬件优化策略
- 实际实施示例和最佳实践

### [Edge AI 开发的 AI 工具包](./aitoolkit.md)
对于使用 Visual Studio Code 的开发者，AI 工具包扩展提供了一个专门为构建、测试和部署 Edge AI 应用设计的全面开发环境。此工具包简化了整个 Edge AI 开发工作流程。

**开发指南**：[Edge AI 开发的 AI 工具包](./aitoolkit.md)

AI 工具包指南涵盖：
- 边缘部署的模型发现与选择
- 本地测试与优化工作流程
- ONNX 和 Ollama 集成，用于边缘模型
- 模型转换与量化技术
- 边缘场景的代理开发
- 性能评估与监控
- 部署准备与最佳实践

## 结论

这五种 EdgeAI 实现展示了当前边缘 AI 解决方案的成熟度和多样性。从像 Jetson Orin Nano 这样的硬件加速边缘设备到像 ONNX Runtime GenAI 和 Windows ML 这样的软件框架，开发者拥有前所未有的选择，可以在边缘部署智能应用。

这些平台的共同点是 AI 能力的普及，使复杂的机器学习对不同技能水平和用例的开发者都变得可访问。无论是构建移动应用、桌面软件还是嵌入式系统，这些 EdgeAI 解决方案都为下一代智能应用提供了基础，使其能够高效且私密地在边缘运行。

每个平台都有独特优势：Jetson Orin Nano 适用于硬件加速边缘计算，ONNX Runtime GenAI 适用于跨平台移动开发，Azure EdgeAI 适用于企业云边集成，Windows ML 适用于 Windows 原生应用，Foundry Local 适用于隐私保护的 RAG 实现。它们共同构成了一个全面的 EdgeAI 开发生态系统。

[下一步 AI 工具包](aitoolkit.md)

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或错误解释承担责任。