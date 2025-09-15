<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "56dfdb5231720282ba90359277270086",
  "translation_date": "2025-09-15T15:12:19+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# EdgeAI 初学者指南

![课程封面图片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.zh.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

按照以下步骤开始使用这些资源：

1. **Fork 仓库**：点击 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **克隆仓库**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，与专家和开发者交流**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 多语言支持

#### 通过 GitHub Action 支持（自动化且始终保持最新）

[法语](../fr/README.md) | [西班牙语](../es/README.md) | [中文（简体）](./README.md) | [中文（繁体，澳门）](../mo/README.md) | [中文（繁体，香港）](../hk/README.md) | [中文（繁体，台湾）](../tw/README.md) | [日语](../ja/README.md) | [韩语](../ko/README.md) |  
**如果您希望支持其他语言，支持的语言列表请参见 [这里](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 简介

欢迎来到 EdgeAI 初学者课程，这里将语言模型的强大功能与本地设备的高效性相结合。本课程介绍了如何在边缘硬件（如智能手机、物联网板和紧凑型服务器）上直接运行小型优化语言模型（SLM），无需依赖云访问。您将探索实时、注重隐私的 AI 推理如何通过轻量化部署改变智能家居、工业监控和离线应用的面貌，同时兼顾速度、安全性和模块化。

### 边缘 AI

边缘 AI 是指在本地硬件上运行 AI 算法和语言模型——靠近数据生成的地方——而无需依赖云资源进行推理。它减少了延迟，增强了隐私，并支持实时决策。

### 核心原则：
- **设备端推理**：AI 模型在边缘设备（手机、路由器、微控制器、工业 PC）上运行。
- **离线能力**：无需持续互联网连接即可运行。
- **低延迟**：适合实时系统的即时响应。
- **数据主权**：将敏感数据保留在本地，提高安全性和合规性。

**小型语言模型（SLM）**  
SLM 如 Phi-4、Mistral-7B 或 Gemma 是大型语言模型的优化版本——通过训练或蒸馏实现：
- 减少内存占用
- 降低计算需求
- 加快启动时间

它们在以下场景中解锁强大的自然语言处理能力，同时满足约束条件：
- 嵌入式系统
- 移动设备
- 物联网设备
- GPU有限的边缘服务器
- 个人电脑

## 课程架构

### [模块 01：边缘 AI 基础与转型](./Module01/README.md)  
**主题**：边缘 AI 部署的变革性转变  

#### 章节结构：
- [**第 1 节：边缘 AI 基础**](./Module01/01.EdgeAIFundamentals.md)  
  - 传统云 AI 与边缘 AI 的比较  
  - 边缘计算的挑战与限制  
  - 核心技术：模型量化、压缩优化、小型语言模型（SLM）  
  - 硬件加速：NPU、GPU优化、CPU优化  
  - 优势：隐私安全、低延迟、离线能力、成本效率  

- [**第 2 节：真实案例研究**](./Module01/02.RealWorldCaseStudies.md)  
  - Microsoft Phi 和 Mu 模型生态系统  
  - 日本航空 AI 报告系统案例研究  
  - 市场影响与未来方向  
  - 部署注意事项与最佳实践  

- [**第 3 节：实践实施指南**](./Module01/03.PracticalImplementationGuide.md)  
  - 开发环境设置（Python 3.10+，.NET 8+）  
  - 硬件要求与推荐配置  
  - 核心模型家族资源  
  - 量化与优化工具（Llama.cpp、Microsoft Olive、Apple MLX）  
  - 评估与验证清单  

- [**第 4 节：边缘 AI 部署硬件平台**](./Module01/04.EdgeDeployment.md)  
  - 边缘 AI 部署的注意事项与要求  
  - Intel 边缘 AI 硬件与优化技术  
  - Qualcomm 移动与嵌入式系统 AI 解决方案  
  - NVIDIA Jetson 与边缘计算平台  
  - Windows AI PC 平台与 NPU 加速  
  - 硬件特定优化策略  

---

### [模块 02：小型语言模型基础](./Module02/README.md)  
**主题**：SLM 理论基础、实施策略与生产部署  

#### 章节结构：
- [**第 1 节：Microsoft Phi 模型家族基础**](./Module02/01.PhiFamily.md)  
  - 设计理念演变（Phi-1 到 Phi-4）  
  - 以效率为先的架构设计  
  - 专业能力（推理、多模态、边缘部署）  

- [**第 2 节：Qwen 模型家族基础**](./Module02/02.QwenFamily.md)  
  - 开源卓越（Qwen 1.0 到 Qwen3）——可通过 Hugging Face 获取  
  - 具有思维模式能力的高级推理架构  
  - 可扩展部署选项（0.5B-235B 参数）  

- [**第 3 节：Gemma 模型家族基础**](./Module02/03.GemmaFamily.md)  
  - 以研究为驱动的创新（Gemma 3 & 3n）  
  - 多模态卓越  
  - 移动优先架构  

- [**第 4 节：BitNET 模型家族基础**](./Module02/04.BitNETFamily.md)  
  - 革命性量化技术（1.58-bit）  
  - 专用推理框架：https://github.com/microsoft/BitNet  
  - 通过极高效率实现可持续 AI 领导力  

- [**第 5 节：Microsoft Mu 模型基础**](./Module02/05.mumodel.md)  
  - 为设备优先架构设计，内置于 Windows 11  
  - 与 Windows 11 设置集成  
  - 注重隐私的离线操作  

- [**第 6 节：Phi-Silica 基础**](./Module02/06.phisilica.md)  
  - 为 Windows 11 Copilot+ PC 优化的 NPU 架构  
  - 卓越效率（650 tokens/second，功耗仅 1.5W）  
  - 开发者可通过 Windows App SDK 集成  

---

### [模块 03：小型语言模型部署](./Module03/README.md)  
**主题**：从理论到生产环境的完整 SLM 生命周期部署  

#### 章节结构：
- [**第 1 节：SLM 高级学习**](./Module03/01.SLMAdvancedLearning.md)  
  - 参数分类框架（微型 SLM 100M-1.4B，中型 SLM 14B-30B）  
  - 高级优化技术（量化方法、BitNET 1-bit 量化）  
  - 模型获取策略（Azure AI Foundry 提供 Phi 模型，Hugging Face 提供选定模型）  

- [**第 2 节：本地环境部署**](./Module03/02.DeployingSLMinLocalEnv.md)  
  - Ollama 通用平台部署  
  - Microsoft Foundry 本地企业级解决方案  
  - 框架对比分析  

- [**第 3 节：容器化云部署**](./Module03/03.DeployingSLMinCloud.md)  
  - vLLM 高性能推理部署  
  - Ollama 容器编排  
  - ONNX Runtime 边缘优化实现  

---

### [模块 04：模型格式转换与量化](./Module04/README.md)  
**主题**：跨平台边缘部署的完整模型优化工具包  

#### 章节结构：
- [**第 1 节：模型格式转换与量化基础**](./Module04/01.Introduce.md)  
  - 精度分类框架（超低、低、中精度）  
  - GGUF 和 ONNX 格式的优势与使用场景  
  - 量化对操作效率的益处  
  - 性能基准与内存占用比较  

- [**第 2 节：Llama.cpp 实施指南**](./Module04/02.Llamacpp.md)  
  - 跨平台安装（Windows、macOS、Linux）  
  - GGUF 格式转换与量化级别（Q2_K 到 Q8_0）  
  - 硬件加速（CUDA、Metal、OpenCL、Vulkan）  
  - Python 集成与 REST API 部署  

- [**第 3 节：Microsoft Olive 优化套件**](./Module04/03.MicrosoftOlive.md)  
  - 硬件感知模型优化，内置 40+ 组件  
  - 动态与静态量化的自动优化  
  - 与 Azure ML 工作流的企业集成  
  - 支持的热门模型（Llama、Phi、选定 Qwen 模型、Gemma）  

- [**第 4 节：Apple MLX 框架深度解析**](./Module04/04.AppleMLX.md)  
  - Apple Silicon 的统一内存架构  
  - 支持 LLaMA、Mistral、Phi-3、选定 Qwen 模型  
  - LoRA 微调与模型定制  
  - 与 Hugging Face 集成，支持 4-bit/8-bit 量化  

---

### [模块 05：SLMOps - 小型语言模型操作](./Module05/README.md)  
**主题**：从蒸馏到生产部署的完整 SLM 生命周期操作  

#### 章节结构：
- [**第 1 节：SLMOps 简介**](./Module05/01.IntroduceSLMOps.md)  
  - SLMOps 在 AI 操作中的范式转变  
  - 成本效率与隐私优先架构  
  - 战略业务影响与竞争优势  
  - 真实实施中的挑战与解决方案  

- [**第 2 节：模型蒸馏——从理论到实践**](./Module05/02.SLMOps-Distillation.md)  
  - 从教师模型到学生模型的知识转移  
  - 两阶段蒸馏过程实施  
  - Azure ML 蒸馏工作流与实际示例  
  - 推理时间减少 85%，准确率保留 92%  

- [**第 3 节：微调——为特定任务定制模型**](./Module05/03.SLMOps-Finetuing.md)  
  - 参数高效微调（PEFT）技术  
  - LoRA 和 QLoRA 高级方法  
  - Microsoft Olive 微调实施  
  - 多适配器训练与超参数优化  

- [**第 4 节：部署——生产就绪实施**](./Module05/04.SLMOps.Deployment.md)  
  - 模型转换与量化以适应生产  
  - Foundry 本地部署配置  
  - 性能基准测试与质量验证  
  - 尺寸减少 75%，生产监控  

---

### [模块 06：SLM Agentic 系统——AI 代理与函数调用](./Module06/README.md)  
**主题**：从基础到高级函数调用与模型上下文协议集成的 SLM Agentic 系统实施  

#### 章节结构：
- [**第 1 节：AI 代理与小型语言模型基础**](./Module06/01.IntroduceAgent.md)  
  - 代理分类框架（反射型、基于模型、目标导向型、学习型代理）  
  - SLM 基础与优化策略（GGUF、量化、边缘框架）  
  - SLM 与 LLM 的权衡分析（成本减少 10-30 倍，任务有效性 70-80%）  
- 使用 Ollama、VLLM 和 Microsoft Edge 解决方案进行实际部署

- [**第2节：小型语言模型中的函数调用**](./Module06/02.FunctionCalling.md)
  - 系统化工作流程实施（意图检测、JSON输出、外部执行）
  - 平台特定实现（Phi-4-mini、选定的Qwen模型、Microsoft Foundry Local）
  - 高级示例（多代理协作、动态工具选择）
  - 生产环境考虑（速率限制、审计日志、安全措施）

- [**第3节：模型上下文协议（MCP）集成**](./Module06/03.IntroduceMCP.md)
  - 协议架构和分层系统设计
  - 多后端支持（开发使用Ollama，生产使用vLLM）
  - 连接协议（STDIO和SSE模式）
  - 实际应用（网页自动化、数据处理、API集成）

---

### [模块07：EdgeAI实施示例](./Module07/README.md)
**主题**：跨多种平台和框架的全面EdgeAI实施

#### 章节结构：
- [**NVIDIA Jetson Orin Nano中的EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 信用卡大小的设备提供67 TOPS AI性能
  - 支持生成式AI模型（视觉变换器、LLM、视觉语言模型）
  - 应用于机器人、无人机、智能摄像头、自动化设备
  - 价格实惠的$249平台，推动AI开发普及化

- [**使用.NET MAUI和ONNX Runtime GenAI的移动应用中的EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 单一C#代码库实现跨平台移动AI
  - 硬件加速支持（CPU、GPU、移动AI处理器）
  - 平台特定优化（iOS的CoreML，Android的NNAPI）
  - 完整的生成式AI循环实施

- [**在Azure中使用小型语言模型引擎的EdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 云-边缘混合部署架构
  - Azure AI服务与ONNX Runtime集成
  - 企业级部署和持续模型管理
  - 智能文档处理的混合AI工作流

- [**使用Windows ML的EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry为高效的设备端推理提供基础
  - 通用硬件支持（AMD、Intel、NVIDIA、Qualcomm芯片）
  - 自动硬件抽象和优化
  - 适用于多样化Windows硬件生态系统的统一框架

- [**使用Foundry Local应用的EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 注重隐私的RAG实施，使用本地资源
  - Phi-3语言模型与语义搜索集成（仅限Phi模型）
  - 支持本地向量数据库（SQLite、Qdrant）
  - 数据主权和离线操作能力

## 学习成果概览

### 模块01学习成果：
- 理解云AI架构与边缘AI架构的基本差异
- 掌握边缘部署的核心优化技术
- 识别实际应用和成功案例
- 获得实施EdgeAI解决方案的实用技能

### 模块02学习成果：
- 深刻理解不同SLM设计理念及其部署影响
- 掌握基于计算约束和性能需求的战略决策能力
- 理解部署灵活性的权衡
- 拥有面向未来的高效AI架构洞察力

### 模块03学习成果：
- 战略模型选择能力
- 优化技术掌握
- 部署灵活性掌握
- 生产就绪配置能力

### 模块04学习成果：
- 深刻理解量化边界及实际应用
- 掌握多种优化框架的实践经验（Llama.cpp、Olive、MLX）
- 硬件感知的优化选择能力
- 跨平台边缘计算环境的生产部署技能

### 模块05学习成果：
- 掌握SLMOps范式及操作原则
- 实施模型蒸馏以实现知识转移和效率优化
- 应用微调技术进行领域特定模型定制
- 部署生产就绪的SLM解决方案并实施监控和维护策略

### 模块06学习成果：
- 理解AI代理和小型语言模型架构的基础概念
- 掌握跨多个平台和框架的函数调用实施
- 集成模型上下文协议（MCP），实现标准化的外部工具交互
- 构建复杂的代理系统，减少人工干预需求

### 模块07学习成果：
- 获得在多种EdgeAI平台和实施策略上的实践经验
- 掌握针对NVIDIA、移动、Azure和Windows平台的硬件特定优化技术
- 理解性能、成本和隐私需求之间的部署权衡
- 开发跨不同生态系统的实际EdgeAI应用的实用技能

## 文件结构树图

```
edgeai-for-beginners/
├── imgs/
│   └── cover.png
├── Module01/ (EdgeAI Fundamentals and Transformation)
│   ├── 01.EdgeAIFundamentals.md
│   ├── 02.RealWorldCaseStudies.md
│   ├── 03.PracticalImplementationGuide.md
│   ├── 04.EdgeDeployment.md
│   └── README.md
├── Module02/ (Small Language Model Foundations)
│   ├── 01.PhiFamily.md
│   ├── 02.QwenFamily.md
│   ├── 03.GemmaFamily.md
│   ├── 04.BitNETFamily.md
│   ├── 05.mumodel.md
│   ├── 06.phisilica.md
│   └── README.md
├── Module03/ (SLM Deployment Practice)
│   ├── 01.SLMAdvancedLearning.md
│   ├── 02.DeployingSLMinLocalEnv.md
│   ├── 03.DeployingSLMinCloud.md
│   └── README.md
├── Module04/ (Model Format Conversion and Quantization)
│   ├── 01.Introduce.md
│   ├── 02.Llamacpp.md
│   ├── 03.MicrosoftOlive.md
│   ├── 04.AppleMLX.md
│   └── README.md
├── Module05/ (SLMOps - Small Language Model Operations)
│   ├── 01.IntroduceSLMOps.md
│   ├── 02.SLMOps-Distillation.md
│   ├── 03.SLMOps-Finetuing.md
│   ├── 04.SLMOps.Deployment.md
│   └── README.md
├── Module06/ (SLM Agentic Systems)
│   ├── 01.IntroduceAgent.md
│   ├── 02.FunctionCalling.md
│   ├── 03.IntroduceMCP.md
│   └── README.md
├── Module07/ (EdgeAI Implementation Samples)
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## 课程特点

- **渐进式学习**：从基础概念逐步深入到高级部署
- **理论与实践结合**：每个模块包含理论基础和实际操作
- **真实案例研究**：基于Microsoft、阿里巴巴、Google等的实际案例
- **实践操作**：完整的配置文件、API测试流程和部署脚本
- **性能基准**：详细比较推理速度、内存使用和资源需求
- **企业级考虑**：安全实践、合规框架和数据保护策略

## 入门指南

推荐学习路径：
1. 从**模块01**开始，建立EdgeAI的基础理解
2. 进入**模块02**，深入了解各种SLM模型家族
3. 学习**模块03**，掌握实际部署技能
4. 继续学习**模块04**，进行高级模型优化和格式转换
5. 完成**模块05**，掌握生产就绪的SLMOps实施
6. 探索**模块06**，理解SLM代理系统和函数调用能力
7. 最后学习**模块07**，获得多样化EdgeAI实施示例的实践经验

每个模块都设计为独立完整，但按顺序学习将获得最佳效果。

## 学习指南

提供了全面的[学习指南](STUDY_GUIDE.md)，帮助您最大化学习体验。学习指南包括：

- **结构化学习路径**：优化的时间表，20小时内完成课程
- **时间分配建议**：具体建议，平衡阅读、练习和项目
- **关键概念重点**：每个模块的优先学习目标
- **自我评估工具**：测试理解的题目和练习
- **迷你项目创意**：实践应用以巩固学习

学习指南适合密集学习（1周）和兼职学习（3周），即使您只能投入10小时，也有明确的时间分配指导。

---

**EdgeAI的未来在于持续改进模型架构、量化技术和部署策略，优先考虑效率和专业化而非通用能力。拥抱这一范式转变的组织将能够充分利用AI的变革潜力，同时保持对数据和运营的控制。**

## 其他课程

我们的团队还制作了其他课程！查看以下内容：

- [MCP入门](https://github.com/microsoft/mcp-for-beginners)
- [AI代理入门](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [使用.NET的生成式AI入门](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [使用JavaScript的生成式AI入门](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [生成式AI入门](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [机器学习入门](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [数据科学入门](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI入门](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [网络安全入门](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web开发入门](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [物联网入门](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR开发入门](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [掌握GitHub Copilot进行AI配对编程](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [掌握GitHub Copilot为C#/.NET开发者服务](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [选择你的Copilot冒险](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。