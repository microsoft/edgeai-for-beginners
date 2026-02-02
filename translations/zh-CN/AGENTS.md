# AGENTS.md

> **初学者开发者指南：贡献于EdgeAI**
> 
> 本文档为开发者、AI代理和贡献者提供了关于本仓库的全面信息。内容涵盖了设置、开发工作流、测试以及最佳实践。
> 
> **最后更新日期**：2025年10月30日 | **文档版本**：3.0

## 目录

- [项目概述](../..)
- [仓库结构](../..)
- [先决条件](../..)
- [设置命令](../..)
- [开发工作流](../..)
- [测试说明](../..)
- [代码风格指南](../..)
- [拉取请求指南](../..)
- [翻译系统](../..)
- [Foundry Local集成](../..)
- [构建与部署](../..)
- [常见问题与故障排除](../..)
- [附加资源](../..)
- [项目特定说明](../..)
- [获取帮助](../..)

## 项目概述

EdgeAI for Beginners 是一个全面的教育性仓库，旨在教授使用小型语言模型（SLMs）进行边缘AI开发。课程内容包括EdgeAI基础知识、模型部署、优化技术以及使用Microsoft Foundry Local和各种AI框架的生产级实现。

**关键技术：**
- Python 3.8+（AI/ML示例的主要语言）
- .NET C#（AI/ML示例）
- JavaScript/Node.js与Electron（用于桌面应用程序）
- Microsoft Foundry Local SDK
- Microsoft Windows ML
- VSCode AI工具包
- OpenAI SDK
- AI框架：LangChain、Semantic Kernel、Chainlit
- 模型优化：Llama.cpp、Microsoft Olive、OpenVINO、Apple MLX

**仓库类型：** 包含8个模块和10个综合示例应用的教育内容仓库

**架构：** 多模块学习路径，提供展示边缘AI部署模式的实践示例

## 仓库结构

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## 先决条件

### 必需工具

- **Python 3.8+** - 用于AI/ML示例和笔记本
- **Node.js 16+** - 用于Electron示例应用程序
- **Git** - 用于版本控制
- **Microsoft Foundry Local** - 用于本地运行AI模型

### 推荐工具

- **Visual Studio Code** - 配备Python、Jupyter和Pylance扩展
- **Windows Terminal** - 提供更好的命令行体验（Windows用户）
- **Docker** - 用于容器化开发（可选）

### 系统要求

- **内存**：最低8GB，推荐16GB以上以支持多模型场景
- **存储**：至少10GB可用空间用于模型和依赖项
- **操作系统**：Windows 10/11、macOS 11+或Linux（Ubuntu 20.04+）
- **硬件**：支持AVX2的CPU；推荐使用GPU（CUDA、Qualcomm NPU）

### 知识要求

- 具备Python编程的基础知识
- 熟悉命令行界面
- 理解AI/ML概念（用于示例开发）
- 熟悉Git工作流和拉取请求流程

## 设置命令

### 仓库设置

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python示例设置（模块08和Workshop示例）

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Node.js示例设置（示例08 - Windows聊天应用）

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local设置

Foundry Local是运行示例所需的工具。请从官方仓库下载并安装：

**安装：**
- **Windows**：`winget install Microsoft.FoundryLocal`
- **macOS**：`brew tap microsoft/foundrylocal && brew install foundrylocal`
- **手动安装**：从[发布页面](https://github.com/microsoft/Foundry-Local/releases)下载

**快速开始：**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**注意**：Foundry Local会自动为您的硬件选择最佳模型版本（CUDA GPU、Qualcomm NPU或CPU）。

## 开发工作流

### 内容开发

本仓库主要包含**Markdown教育内容**。进行更改时：

1. 编辑适当模块目录下的`.md`文件
2. 遵循现有的格式模式
3. 确保代码示例准确且经过测试
4. 必要时更新对应的翻译内容（或由自动化处理）

### 示例应用开发

对于模块08的Python示例（示例01-07、09-10）：
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

对于Workshop Python示例：
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

对于Electron示例（示例08）：
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### 测试示例应用

Python示例没有自动化测试，但可以通过运行进行验证：
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron示例具有测试基础设施：
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## 测试说明

### 内容验证

仓库使用自动化翻译工作流。翻译无需手动测试。

**内容更改的手动验证：**
1. 通过预览`.md`文件检查Markdown渲染
2. 验证所有链接指向有效目标
3. 测试文档中包含的代码片段
4. 确保图片正确加载

### 示例应用测试

**模块08/示例/08（Electron应用）具有全面测试：**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python示例需手动测试：**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## 代码风格指南

### Markdown内容

- 使用一致的标题层级（#用于标题，##用于主要部分，###用于子部分）
- 包含带语言说明的代码块：```python, ```bash, ```javascript
- 遵循现有的表格、列表和强调格式
- 保持行可读性（目标约80-100字符，但不严格限制）
- 对内部引用使用相对链接

### Python代码风格

- 遵循PEP 8规范
- 适当使用类型提示
- 为函数和类添加文档字符串
- 使用有意义的变量名
- 保持函数专注且简洁

### JavaScript/Node.js代码风格

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**关键约定：**
- 示例08提供了ESLint配置
- 使用Prettier进行代码格式化
- 使用现代ES6+语法
- 遵循代码库中的现有模式

## 拉取请求指南

### 贡献工作流

1. **Fork仓库**并从`main`创建新分支
2. **根据代码风格指南进行更改**
3. **按照上述测试说明进行彻底测试**
4. **使用清晰的消息提交**，遵循规范化提交格式
5. **推送到您的Fork**并创建拉取请求
6. **在审查期间响应维护者的反馈**

### 分支命名约定

- `feature/<module>-<description>` - 用于新功能或内容
- `fix/<module>-<description>` - 用于错误修复
- `docs/<description>` - 用于文档改进
- `refactor/<description>` - 用于代码重构

### 提交消息格式

遵循[规范化提交](https://www.conventionalcommits.org/)：

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**示例：**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### 标题格式
```
[ModuleXX] Brief description of change
```
或
```
[Module08/samples/XX] Description for sample changes
```

### 行为准则

所有贡献者必须遵守[Microsoft开源行为准则](https://opensource.microsoft.com/codeofconduct/)。请在贡献之前查看[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

### 提交前检查

**对于内容更改：**
- 预览所有修改的Markdown文件
- 验证链接和图片是否正常工作
- 检查拼写和语法错误

**对于示例代码更改（模块08/示例/08）：**
```bash
npm run lint
npm test
```

**对于Python示例更改：**
- 测试示例是否成功运行
- 验证错误处理是否正常
- 检查与Foundry Local的兼容性

### 审查流程

- 教育内容更改需审查准确性和清晰度
- 代码示例需测试功能性
- 翻译更新由GitHub Actions自动处理

## 翻译系统

**重要：** 本仓库使用GitHub Actions进行自动翻译。

- 翻译文件位于`/translations/`目录（支持50多种语言）
- 通过`co-op-translator.yml`工作流自动化处理
- **请勿手动编辑翻译文件** - 它们会被覆盖
- 仅编辑根目录和模块目录中的英文源文件
- 推送到`main`分支时会自动生成翻译

## Foundry Local集成

大多数模块08示例需要运行Microsoft Foundry Local。

### 安装与设置

**安装Foundry Local：**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**安装Python SDK：**
```bash
pip install foundry-local-sdk openai
```

### 启动Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK使用（Python）
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### 验证Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### 示例所需环境变量

大多数示例使用以下环境变量：
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**注意**：使用`FoundryLocalManager`时，SDK会自动处理服务发现和模型加载。模型别名（如`phi-3.5-mini`）确保为您的硬件选择最佳版本。

## 构建与部署

### 内容部署

本仓库主要是文档内容 - 无需构建过程。

### 示例应用构建

**Electron应用（模块08/示例/08）：**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python示例：**
无需构建过程 - 示例直接使用Python解释器运行。

## 常见问题与故障排除

> **提示**：查看[GitHub问题](https://github.com/microsoft/edgeai-for-beginners/issues)以获取已知问题和解决方案。

### 严重问题（阻塞）

#### Foundry Local未运行
**问题：** 示例因连接错误而失败

**解决方案：**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### 常见问题（中等）

#### Python虚拟环境问题
**问题：** 模块导入错误

**解决方案：**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron构建问题
**问题：** npm安装或构建失败

**解决方案：**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### 工作流问题（轻微）

#### 翻译工作流冲突
**问题：** 翻译PR与您的更改冲突

**解决方案：**
- 仅编辑英文源文件
- 让自动化翻译工作流处理翻译
- 如果发生冲突，在翻译合并后将`main`合并到您的分支

#### 模型下载失败
**问题：** Foundry Local无法下载模型

**解决方案：**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## 附加资源

### 学习路径
- **初学者路径：** 模块01-02（7-9小时）
- **中级路径：** 模块03-04（9-11小时）
- **高级路径：** 模块05-07（12-15小时）
- **专家路径：** 模块08（8-10小时）
- **实践Workshop：** Workshop材料（6-8小时）

### 关键模块内容
- **模块01：** EdgeAI基础知识和真实案例研究
- **模块02：** 小型语言模型（SLM）家族和架构
- **模块03：** 本地和云部署策略
- **模块04：** 使用多个框架进行模型优化（Llama.cpp、Microsoft Olive、OpenVINO、Qualcomm QNN、Apple MLX）
- **模块05：** SLMOps - 生产操作
- **模块06：** AI代理和函数调用
- **模块07：** 平台特定实现
- **模块08：** Foundry Local工具包，包含10个综合示例

### 外部依赖
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - 本地AI模型运行时，兼容OpenAI API
  - [文档](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - 优化框架
- [Microsoft Olive](https://microsoft.github.io/Olive/) - 模型优化工具包
- [OpenVINO](https://docs.openvino.ai/) - Intel的优化工具包

## 项目特定说明

### 模块08示例应用

仓库包含10个综合示例应用：

1. **01-REST聊天快速入门** - 基本OpenAI SDK集成
2. **02-OpenAI SDK集成** - 高级SDK功能
3. **03-模型发现与基准测试** - 模型比较工具
4. **04-Chainlit RAG应用** - 检索增强生成
5. **05-多代理编排** - 基本代理协调
6. **06-模型作为工具路由器** - 智能模型路由
7. **07-直接API客户端** - 低级API集成
8. **08-Windows 11聊天应用** - 原生Electron桌面应用
9. **09-高级多代理系统** - 复杂代理编排
10. **10-Foundry 工具框架** - LangChain/Semantic Kernel 集成

### 工作坊示例应用

工作坊包括6个循序渐进的实践课程：

1. **课程 01** - 使用 Foundry Local 集成进行聊天启动
2. **课程 02** - 使用 RAGAS 进行 RAG 管道和评估
3. **课程 03** - 开源模型的基准测试
4. **课程 04** - 模型比较与选择
5. **课程 05** - 多代理编排系统
6. **课程 06** - 模型路由与管道管理

每个示例展示了使用 Foundry Local 进行边缘 AI 开发的不同方面。

### 性能考量

- SLMs 针对边缘部署进行了优化（2-16GB RAM）
- 本地推理提供 50-500ms 的响应时间
- 量化技术实现了 75% 的大小缩减，同时保留 85% 的性能
- 使用本地模型实现实时对话功能

### 安全与隐私

- 所有处理均在本地完成 - 无数据发送至云端
- 适用于隐私敏感型应用（医疗、金融）
- 符合数据主权要求
- Foundry Local 完全运行于本地硬件

## 获取帮助

### 文档

- **主 README**: [README.md](README.md) - 仓库概览和学习路径
- **学习指南**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - 学习资源和时间表
- **支持**: [SUPPORT.md](SUPPORT.md) - 如何获取帮助
- **安全性**: [SECURITY.md](SECURITY.md) - 报告安全问题

### 社区支持

- **GitHub 问题**: [报告错误或请求功能](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub 讨论**: [提问和分享想法](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local 问题**: [Foundry Local 的技术问题](https://github.com/microsoft/Foundry-Local/issues)

### 联系方式

- **维护者**: 查看 [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **安全问题**: 按照 [SECURITY.md](SECURITY.md) 中的负责任披露流程
- **微软支持**: 对于企业支持，请联系微软客户服务

### 其他资源

- **Microsoft Learn**: [AI 和机器学习学习路径](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local 文档**: [官方文档](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **社区示例**: 查看 [GitHub 讨论](https://github.com/microsoft/edgeai-for-beginners/discussions) 了解社区贡献

---

**这是一个专注于教授边缘 AI 开发的教育性仓库。主要的贡献模式是改进教育内容以及添加/增强示例应用，以展示边缘 AI 概念。**

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。