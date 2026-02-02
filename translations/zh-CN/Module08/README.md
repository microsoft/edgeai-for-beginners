# 模块 08：深入体验 Microsoft Foundry Local - 完整开发者工具包

## 概述

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) 代表了边缘 AI 开发的下一代技术，为开发者提供强大的工具，用于本地构建、部署和扩展 AI 应用，同时保持与 Azure AI Foundry 的无缝集成。本模块全面覆盖 Foundry Local 的安装到高级代理开发。

**关键技术：**
- Microsoft Foundry Local CLI 和 SDK
- Azure AI Foundry 集成
- 设备上的模型推理
- 本地模型缓存和优化
- 基于代理的架构

## 学习目标

完成本模块后，您将能够：

- **掌握 Foundry Local**：安装、配置并优化 Windows 11 开发环境
- **部署多样化模型**：使用 CLI 命令本地运行 phi、qwen、deepseek 和 GPT 模型
- **构建生产解决方案**：通过高级提示工程和数据集成创建 AI 应用
- **利用开源生态系统**：集成 Hugging Face 模型和社区贡献
- **开发 AI 代理**：构建具有基础和编排能力的智能代理
- **实施企业模式**：创建模块化、可扩展的 AI 解决方案以进行生产部署

## 课程结构

### [1: 开始使用 Foundry Local](./01.FoundryLocalSetup.md)
**重点**：安装、CLI 设置、模型部署和硬件优化

**关键主题**：完整安装 • CLI 命令 • 模型缓存 • 硬件加速 • 多模型部署

**示例**：[REST 聊天快速入门](./samples/01/README.md) • [OpenAI SDK 集成](./samples/02/README.md) • [模型发现与基准测试](./samples/03/README.md)

**时长**：2-3 小时 | **难度**：初级

---

### [2: 使用 Azure AI Foundry 构建 AI 解决方案](./02.AzureAIFoundryIntegration.md)
**重点**：高级提示工程、数据集成和云连接

**关键主题**：提示工程 • 数据集成 • Azure 工作流 • 性能优化 • 监控

**示例**：[Chainlit RAG 应用](./samples/04/README.md)

**时长**：2-3 小时 | **难度**：中级

---

### [3: Foundry Local 的开源模型](./03.OpenSourceModels.md)
**重点**：Hugging Face 集成、BYOM 策略和社区模型

**关键主题**：Hugging Face 集成 • 自带模型 • Model Mondays 洞察 • 社区贡献 • 模型选择

**示例**：[多代理编排](./samples/05/README.md)

**时长**：2-3 小时 | **难度**：中级

---

### [4: 探索前沿模型](./04.CuttingEdgeModels.md)
**重点**：LLM 与 SLM 的比较、EdgeAI 实现和高级演示

**关键主题**：模型比较 • 边缘与云推理 • Phi + ONNX Runtime • Chainlit RAG 应用 • WebGPU 优化

**示例**：[工具化模型路由器](./samples/06/README.md)

**时长**：3-4 小时 | **难度**：高级

---

### [5: 快速构建 AI 驱动代理](./05.AIPoweredAgents.md)
**重点**：代理架构、系统提示、基础和编排

**关键主题**：代理设计模式 • 系统提示工程 • 基础技术 • 多代理系统 • 生产部署

**示例**：[多代理编排](./samples/05/README.md) • [高级多代理系统](./samples/09/README.md)

**时长**：3-4 小时 | **难度**：高级

---

### [6: Foundry Local - 工具化模型](./06.ModelsAsTools.md)
**重点**：模块化 AI 解决方案、企业扩展和生产模式

**关键主题**：工具化模型 • 设备上的部署 • SDK/API 集成 • 企业架构 • 扩展策略

**示例**：[工具化模型路由器](./samples/06/README.md) • [Foundry 工具框架](./samples/10/README.md)

**时长**：3-4 小时 | **难度**：专家级

---

### [7: 直接 API 集成模式](./samples/07/README.md)
**重点**：无需 SDK 依赖的纯 REST API 集成以实现最大控制

**关键主题**：HTTP 客户端实现 • 自定义认证 • 模型健康监控 • 流式响应 • 生产错误处理

**示例**：[直接 API 客户端](./samples/07/README.md)

**时长**：2-3 小时 | **难度**：中级

---

### [8: Windows 11 原生聊天应用](./samples/08/README.md)
**重点**：使用 Foundry Local 集成构建现代原生聊天应用

**关键主题**：Electron 开发 • Fluent Design System • 原生 Windows 集成 • 实时流式传输 • 聊天界面设计

**示例**：[Windows 11 聊天应用](./samples/08/README.md)

**时长**：3-4 小时 | **难度**：高级

---

### [9: 高级多代理编排](./samples/09/README.md)
**重点**：复杂的代理协调、专门任务分配和协作 AI 工作流

**关键主题**：智能代理协调 • 函数调用模式 • 跨代理通信 • 工作流编排 • 质量保证机制

**示例**：[高级多代理系统](./samples/09/README.md)

**时长**：4-5 小时 | **难度**：专家级

---

### [10: Foundry Local 作为工具框架](./samples/10/README.md)
**重点**：以工具为中心的架构，将 Foundry Local 集成到现有应用和框架中

**关键主题**：LangChain 集成 • 语义内核功能 • REST API 框架 • CLI 工具 • Jupyter 集成 • 生产部署模式

**示例**：[Foundry 工具框架](./samples/10/README.md)

**时长**：4-5 小时 | **难度**：专家级

## 前置条件

### 系统要求
- **操作系统**：Windows 11（22H2 或更高版本）
- **内存**：16GB RAM（建议 32GB 以支持更大的模型）
- **存储**：50GB 可用空间用于模型缓存
- **硬件**：建议使用支持 NPU 的设备（Copilot+ PC），GPU 可选
- **网络**：高速互联网以下载初始模型

### 开发环境
- 安装 Visual Studio Code 和 AI Toolkit 扩展
- Python 3.10+ 和 pip
- Git 用于版本控制
- PowerShell 或命令提示符
- Azure CLI（可选，用于云集成）

### 知识要求
- 基本的 AI/ML 概念理解
- 命令行操作熟悉
- Python 编程基础
- REST API 概念
- 提示工程和模型推理的基本知识

## 模块时间表

**总预计时间**：30-38 小时

| 课程 | 重点领域 | 示例 | 时间 | 难度 |
|------|----------|------|------|------|
|  1 | 设置与基础 | 01, 02, 03 | 2-3 小时 | 初级 |
|  2 | AI 解决方案 | 04 | 2-3 小时 | 中级 |
|  3 | 开源模型 | 05 | 2-3 小时 | 中级 |
|  4 | 高级模型 | 06 | 3-4 小时 | 高级 |
|  5 | AI 代理 | 05, 09 | 3-4 小时 | 高级 |
|  6 | 企业工具 | 06, 10 | 3-4 小时 | 专家级 |
|  7 | 直接 API 集成 | 07 | 2-3 小时 | 中级 |
|  8 | Windows 11 聊天应用 | 08 | 3-4 小时 | 高级 |
|  9 | 高级多代理 | 09 | 4-5 小时 | 专家级 |
| 10 | 工具框架 | 10 | 4-5 小时 | 专家级 |

## 关键资源

**官方文档：**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - 源代码和官方示例
- [Azure AI Foundry 文档](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - 完整的设置和使用指南
- [Model Mondays 系列](https://aka.ms/model-mondays) - 每周模型亮点和教程

**社区与支持：**
- [Foundry Local 讨论区](https://github.com/microsoft/Foundry-Local/discussions) - 社区问答和功能请求
- [Microsoft AI 开发者社区](https://techcommunity.microsoft.com/category/artificialintelligence) - 最新新闻和最佳实践

## 学习成果

完成本模块后，您将具备以下能力：

### 技术掌握
- **部署与管理**：在开发和生产环境中安装和管理 Foundry Local
- **集成模型**：无缝使用来自 Microsoft、Hugging Face 和社区的多样化模型
- **构建应用**：创建具有高级功能和优化的生产级 AI 应用
- **开发代理**：实现具有基础、推理和工具集成的复杂 AI 代理

### 战略理解
- **架构决策**：在本地与云部署之间做出明智选择
- **性能优化**：优化不同硬件配置上的推理性能
- **企业扩展**：设计从本地原型到企业部署的可扩展应用
- **隐私与安全**：实施隐私保护的 AI 解决方案，支持本地推理

### 创新能力
- **快速原型开发**：快速构建和测试 AI 应用概念，涵盖所有 10 个示例模式
- **社区集成**：利用开源模型并为生态系统做出贡献
- **高级模式**：实现包括 RAG、代理和工具集成在内的前沿 AI 模式
- **框架掌握**：专家级集成 LangChain、语义内核、Chainlit 和 Electron
- **生产部署**：从本地原型到企业系统部署可扩展的 AI 解决方案
- **面向未来的开发**：构建适应新兴 AI 技术和模式的应用

## 开始使用

1. **环境设置**：确保使用推荐硬件的 Windows 11（参见前置条件）
2. **安装 Foundry Local**：按照课程 1 完成安装和配置
3. **运行示例 01**：从基本的 REST API 集成开始验证设置
4. **完成所有示例**：完成示例 01-10 以全面掌握

## 成功指标

通过所有 10 个全面示例跟踪您的进度：

### 基础级别（示例 01-03）
- [ ] 成功安装和配置 Foundry Local
- [ ] 完成 REST API 集成（示例 01）
- [ ] 实现 OpenAI SDK 兼容性（示例 02）
- [ ] 执行模型发现和基准测试（示例 03）

### 应用级别（示例 04-06）
- [ ] 部署并运行至少 4 个不同的模型系列
- [ ] 构建功能性 RAG 聊天应用（示例 04）
- [ ] 创建多代理编排系统（示例 05）
- [ ] 实现智能模型路由（示例 06）

### 高级集成级别（示例 07-10）
- [ ] 构建生产级 API 客户端（示例 07）
- [ ] 开发 Windows 11 原生聊天应用（示例 08）
- [ ] 实现高级多代理系统（示例 09）
- [ ] 创建全面的工具框架（示例 10）

### 掌握指标
- [ ] 成功运行所有 10 个示例且无错误
- [ ] 针对特定用例自定义至少 3 个示例
- [ ] 在类似生产环境中部署 2+ 示例
- [ ] 为示例代码贡献改进或扩展
- [ ] 将 Foundry Local 模式集成到个人/专业项目中

## 快速入门指南 - 所有 10 个示例

### 环境设置（所有示例必需）

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### 核心基础示例（01-06）

**示例 01：REST 聊天快速入门**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**示例 02：OpenAI SDK 集成**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**示例 03：模型发现与基准测试**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**示例 04：Chainlit RAG 应用**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**示例 05：多代理编排**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**示例 06：工具化模型路由器**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### 高级集成示例（07-10）

**示例 07：直接 API 客户端**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**示例 08：Windows 11 聊天应用**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**示例 09：高级多代理系统**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**示例 10：Foundry 工具框架**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### 常见问题排查

**Foundry Local 连接错误**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**模型加载问题**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**依赖问题**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## 总结
本模块代表了边缘人工智能开发的前沿技术，将微软的企业级工具与开源生态系统的灵活性和创新性相结合。通过掌握 Foundry Local 的全部 10 个综合示例，您将站在人工智能应用开发的最前沿。

**完整学习路径：**
- **基础**（示例 01-03）：API 集成和模型管理
- **应用**（示例 04-06）：RAG、代理和智能路由
- **高级**（示例 07-10）：生产框架和企业集成

有关 Azure OpenAI 集成（第 2 节），请参阅各示例的 README 文件以获取所需的环境变量和 API 版本设置。

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。