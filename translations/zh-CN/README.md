# EdgeAI 入门指南


![课程封面图片](../../translated_images/zh-CN/cover.eb18d1b9605d754b.webp)

[![GitHub 贡献者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub 问题](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub 拉取请求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![欢迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub 关注者](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub 分叉](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub 星标](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

按照以下步骤开始使用这些资源：

1. **Fork 仓库**：点击 [![GitHub 分叉](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **克隆仓库**： `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，结识专家和其他开发者**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多语言支持

#### 通过 GitHub Action 支持（自动且始终保持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯语](../ar/README.md) | [孟加拉语](../bn/README.md) | [保加利亚语](../bg/README.md) | [缅甸语](../my/README.md) | [中文（简体）](./README.md) | [中文（繁体，香港）](../zh-HK/README.md) | [中文（繁体，澳门）](../zh-MO/README.md) | [中文（繁体，台湾）](../zh-TW/README.md) | [克罗地亚语](../hr/README.md) | [捷克语](../cs/README.md) | [丹麦语](../da/README.md) | [荷兰语](../nl/README.md) | [爱沙尼亚语](../et/README.md) | [芬兰语](../fi/README.md) | [法语](../fr/README.md) | [德语](../de/README.md) | [希腊语](../el/README.md) | [希伯来语](../he/README.md) | [印地语](../hi/README.md) | [匈牙利语](../hu/README.md) | [印度尼西亚语](../id/README.md) | [意大利语](../it/README.md) | [日语](../ja/README.md) | [卡纳达语](../kn/README.md) | [韩语](../ko/README.md) | [立陶宛语](../lt/README.md) | [马来语](../ms/README.md) | [马拉雅拉姆语](../ml/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [尼日利亚皮钦语](../pcm/README.md) | [挪威语](../no/README.md) | [波斯语（法尔西语）](../fa/README.md) | [波兰语](../pl/README.md) | [葡萄牙语（巴西）](../pt-BR/README.md) | [葡萄牙语（葡萄牙）](../pt-PT/README.md) | [旁遮普语（古鲁姆克希文）](../pa/README.md) | [罗马尼亚语](../ro/README.md) | [俄语](../ru/README.md) | [塞尔维亚语（西里尔文）](../sr/README.md) | [斯洛伐克语](../sk/README.md) | [斯洛文尼亚语](../sl/README.md) | [西班牙语](../es/README.md) | [斯瓦希里语](../sw/README.md) | [瑞典语](../sv/README.md) | [他加禄语（菲律宾语）](../tl/README.md) | [泰米尔语](../ta/README.md) | [泰卢固语](../te/README.md) | [泰语](../th/README.md) | [土耳其语](../tr/README.md) | [乌克兰语](../uk/README.md) | [乌尔都语](../ur/README.md) | [越南语](../vi/README.md)

> **更喜欢本地克隆？**

> 本仓库包括50多种语言的翻译，大幅增加下载大小。若想克隆时不含翻译，可以使用稀疏检出：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 这样你将获得完成课程所需的一切，同时显著加快下载速度。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**如果您希望支持更多的翻译语言，列表请见[这里](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 介绍

欢迎来到 **EdgeAI 入门指南** —— 您通往边缘人工智能变革世界的全面旅程。本课程填补了强大 AI 能力与边缘设备实际部署之间的鸿沟，使您能够直接在数据生成和决策发生的地方利用 AI 的潜能。

### 您将掌握的内容

本课程将带您从基础概念到生产级实现，包括：
- **适合边缘部署的小型语言模型（SLMs）**
- **涵盖多平台的硬件感知优化**
- **具备隐私保护的实时推断**
- **企业级生产部署策略**

### 为什么 EdgeAI 重要

边缘 AI 代表了一场范式转变，应对了现代关键挑战：
- **隐私与安全**：本地处理敏感数据，无需云端暴露
- **实时性能**：消除网络延迟，适用于时间关键应用
- **成本效益**：降低带宽及云计算费用
- **弹性操作**：网络中断时依然维持功能
- **合规性要求**：满足数据主权法规

### 边缘 AI

边缘 AI 指的是在靠近数据生成地的硬件本地运行 AI 算法和语言模型，无需云端资源进行推断。它减少延迟，增强隐私，并实现实时决策。

### 核心原则：
- **设备端推断**：AI 模型在边缘设备（手机、路由器、微控制器、工业电脑）上运行
- **离线能力**：无需持续网络连接即可工作
- **低延迟**：适合实时系统的即时响应
- **数据主权**：敏感数据保留在本地，提升安全性和合规性

### 小型语言模型（SLMs）

SLMs 如 Phi-4、Mistral-7B 和 Gemma 是针对大型 LLM 优化的版本——经过训练或蒸馏，实现：
- **减少内存占用**：高效利用有限边缘设备内存
- **降低计算需求**：优化 CPU 和边缘 GPU 性能
- **更快启动时间**：快速初始化，实现响应式应用

它们在满足以下设备限制的同时，释放强大 NLP 能力：
- **嵌入式系统**：物联网设备和工业控制器
- **移动设备**：具备离线能力的智能手机和平板
- **物联网设备**：资源有限的传感器和智能终端
- **边缘服务器**：具有限制 GPU 资源的本地处理单元
- **个人电脑**：桌面和笔记本部署场景

## 课程模块及导航

| 模块 | 主题 | 关注领域 | 关键内容 | 级别 | 时长 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI 介绍](./introduction.md) | 基础与背景 | EdgeAI 概览 • 行业应用 • SLM 介绍 • 学习目标 | 入门 | 1-2 小时 |
| [📚 01](../../Module01) | [EdgeAI 基础](./Module01/README.md) | 云端与边缘 AI 比较 | EdgeAI 基础 • 真实案例 • 实施指南 • 边缘部署 | 入门 | 3-4 小时 |
| [🧠 02](../../Module02) | [SLM 模型基础](./Module02/README.md) | 模型系列与架构 | Phi 系列 • Qwen 系列 • Gemma 系列 • BitNET • μModel • Phi-Silica | 入门 | 4-5 小时 |
| [🚀 03](../../Module03) | [SLM 部署实践](./Module03/README.md) | 本地与云端部署 | 高阶学习 • 本地环境 • 云端部署 | 中级 | 4-5 小时 |
| [⚙️ 04](../../Module04) | [模型优化工具包](./Module04/README.md) | 跨平台优化 | 介绍 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流综合 | 中级 | 5-6 小时 |
| [🔧 05](../../Module05) | [SLMOps 生产实践](./Module05/README.md) | 生产运维 | SLMOps 介绍 • 模型蒸馏 • 微调 • 生产部署 | 高级 | 5-6 小时 |
| [🤖 06](../../Module06) | [AI 代理与函数调用](./Module06/README.md) | 代理框架与 MCP | 代理介绍 • 函数调用 • 模型上下文协议 | 高级 | 4-5 小时 |
| [💻 07](../../Module07) | [平台实现](./Module07/README.md) | 跨平台示例 | AI 工具包 • Foundry Local • Windows 开发 | 高级 | 3-4 小时 |
| [🏭 08](../../Module08) | [Foundry Local 工具包](./Module08/README.md) | 生产级示例 | 示例应用（见下文详细内容） | 专家 | 8-10 小时 |

### 🏭 **模块 08：示例应用**

- [01：REST 聊天快速上手](./Module08/samples/01/README.md)
- [02：OpenAI SDK 集成](./Module08/samples/02/README.md)
- [03：模型发现与基准测试](./Module08/samples/03/README.md)
- [04：Chainlit RAG 应用](./Module08/samples/04/README.md)
- [05：多代理编排](./Module08/samples/05/README.md)
- [06：作为工具的模型路由器](./Module08/samples/06/README.md)
- [07：直接 API 客户端](./Module08/samples/07/README.md)
- [08：Windows 11 聊天应用](./Module08/samples/08/README.md)
- [09：高级多代理系统](./Module08/samples/09/README.md)
- [10：Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **研讨会：实操学习路径**

全面的实操研讨会材料，配备生产就绪的实现：

- **[研讨会指南](./Workshop/Readme.md)** - 完整学习目标、成果和资源导航
- **Python 示例**（6 个单元）- 更新最佳实践、错误处理和完整文档
- **Jupyter 笔记本**（8 个交互式笔记本）- 逐步教程，含基准测试和性能监控
- **单元指南** - 每个研讨会单元的详细 Markdown 指南
- **验证工具** - 验证代码质量和运行冒烟测试的脚本

**您将构建的内容：**
- 支持流媒体的本地 AI 聊天应用
- 具备质量评估的 RAG 流水线（RAGAS）
- 多模型基准测试和比较工具
- 多代理编排系统
- 基于任务选择的智能模型路由

### 🎙️ **Agentic 研讨会：实操 - AI 播客工作室**

从零开始构建一个 AI 驱动的播客制作流水线！本沉浸式研讨会教您创建完整的多代理系统，将想法转化为专业播客节目。
**[🎬 启动 AI 播客工作室研讨会](./WorkshopForAgentic/README.md)**

**你的使命**：启动“未来字节”——一个完全由你自己构建的 AI 代理驱动的科技播客。无需云依赖，无需 API 费用——一切都在你的本地机器上运行。

**独特之处：**
- **🤖 真正的多代理协调** - 构建专门的 AI 代理进行研究、写作和音频制作
- **🎯 完整生产流水线** - 从话题选择到最终播客音频输出
- **💻 100% 本地部署** - 使用 Ollama 和本地模型（Qwen-3-8B）保障隐私和控制权
- **🎤 文本转语音集成** - 将剧本转化为自然多说话人对话
- **✋ 人工参与工作流** - 审批关卡确保质量，同时保持自动化

**三幕式学习旅程：**

| 幕 | 重点 | 关键技能 | 时长 |
|-----|-------|------------|----------|
| **[第一幕：认识你的 AI 助手](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | 构建你的第一个 AI 代理 | 工具集成 • 网络搜索 • 解决问题 • 代理推理 | 2-3 小时 |
| **[第二幕：组建你的制作团队](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | 协调多代理 | 团队协调 • 审批工作流 • DevUI 界面 • 人工监督 | 3-4 小时 |
| **[第三幕：让你的播客活起来](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | 生成播客音频 | 文本转语音 • 多说话人合成 • 长格式音频 • 全自动化 | 2-3 小时 |

**使用技术：**
- **Microsoft Agent Framework** - 多代理协调和管理
- **Ollama** - 本地 AI 模型运行时（无需云）
- **Qwen-3-8B** - 针对代理任务优化的开源语言模型
- **文本转语音 API** - 用于播客生成的自然语音合成

**硬件支持：**
- ✅ **CPU 模式** - 适用于任何现代电脑（推荐 8GB+ 内存）
- 🚀 **GPU 加速** - NVIDIA/AMD GPU 显著提升推理速度
- ⚡ **NPU 支持** - 下一代神经处理单元加速

**适合人群：**
- 学习多代理 AI 系统的开发者
- 对 AI 自动化和工作流感兴趣的任何人
- 探索 AI 辅助制作的内容创作者
- 学习实用 AI 协同模式的学生

**开始构建**：[🎙️ AI 播客工作室研讨会 →](./WorkshopForAgentic/README.md)

### 📊 **学习路径摘要**
- **总时长**：36-45 小时
- **初级路径**：模块 01-02（7-9 小时）  
- **中级路径**：模块 03-04（9-11 小时）
- **高级路径**：模块 05-07（12-15 小时）
- **专家路径**：模块 08（8-10 小时）

## 你将构建的内容

### 🎯 核心能力
- **边缘 AI 架构**：设计本地优先且带云集成的 AI 系统
- **模型优化**：量化和压缩模型以适应边缘部署（提升速度85%，缩减大小75%）
- **多平台部署**：Windows、移动、嵌入式及云边混合系统
- **生产运维**：边缘 AI 的监控、扩展和维护

### 🏗️ 实践项目
- **Foundry 本地聊天应用**：Windows 11 原生应用，支持模型切换
- **多代理系统**：协调员与专家代理，实现复杂工作流  
- **RAG 应用**：本地文档处理和向量搜索
- **模型路由器**：基于任务分析智能选择模型
- **API 框架**：支持流式和健康监控的生产就绪客户端
- **跨平台工具**：LangChain/Semantic Kernel 集成模式

### 🏢 行业应用
**制造业** • **医疗健康** • **自动驾驶** • **智慧城市** • **移动应用**

## 快速入门

**推荐学习路径**（总计 20-30 小时）：

0. **📖 介绍** ([Introduction.md](./introduction.md))：EdgeAI 基础 + 行业背景 + 学习框架
1. **📚 基础**（模块 01-02）：EdgeAI 概念 + SLM 模型家族
2. **⚙️ 优化**（模块 03-04）：部署 + 量化框架  
3. **🚀 生产**（模块 05-06）：SLMOps + AI 代理 + 函数调用
4. **💻 实现**（模块 07-08）：平台示例 + Foundry 本地工具包

每个模块包含理论、动手练习和生产就绪代码示例。

## 职业影响

**技术岗位**：EdgeAI 解决方案架构师 • 边缘 ML 工程师 • 物联网 AI 开发者 • 移动 AI 开发者

**行业领域**：制造业 4.0 • 医疗技术 • 自动化系统 • 金融科技 • 消费电子

**作品集项目**：多代理系统 • 生产级 RAG 应用 • 跨平台部署 • 性能优化

## 代码库结构

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## 课程亮点

✅ **渐进学习**：理论 → 实践 → 生产部署  
✅ **真实案例研究**：微软、日本航空、企业实践  
✅ **动手示例**：50+ 示例，10 个全面 Foundry 本地演示  
✅ **性能聚焦**：85% 提速，75% 缩减  
✅ **多平台支持**：Windows、移动、嵌入式、云边混合  
✅ **生产就绪**：监控、扩展、安全、合规框架

📖 **[学习指南](STUDY_GUIDE.md)**：结构化 20 小时学习路径，含时间分配和自我评估工具。

---

**EdgeAI 代表 AI 部署的未来**：本地优先，隐私保护，高效。掌握这些技能，构建下一代智能应用。

## 其他课程

我们团队还制作了其他课程！请查阅：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![面向初学者的 LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![面向初学者的 LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / 代理
[![初学者的 AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![初学者的 Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![初学者的 MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![初学者的 AI 代理](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成式 AI 系列
[![初学者的生成式 AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心学习
[![初学者机器学习](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![初学者数据科学](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![初学者 AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![初学者网络安全](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![初学者网页开发](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![初学者物联网](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![初学者 XR 开发](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![用于 AI 配对编程的 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 获取帮助

如果您遇到困难或对构建 AI 应用有任何疑问，请加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果您在构建过程中有产品反馈或遇到错误，请访问：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译而成。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原文档的原始语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而引起的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->