# Workshop 笔记本

> **用于动手学习边缘 AI 的交互式 Jupyter 笔记本**
>
> 逐步、自主学习的教程，从基础的聊天补全到使用 Microsoft Foundry Local 和小型语言模型构建高级多代理系统。

---

## 📖 介绍

欢迎来到 **边缘 AI 初学者工作坊笔记本** 集合。这些交互式 Jupyter 笔记本提供了一个动手学习的体验，您可以实时编写、执行和实验边缘 AI 代码。

### 为什么选择 Jupyter 笔记本？

与传统教程不同，这些笔记本提供：

- **交互式学习**：运行代码单元并立即查看结果  
- **实验性**：修改参数并实时观察变化  
- **文档化**：内嵌的解释和 Markdown 单元指导您理解概念  
- **可复现性**：完整的工作示例，可供参考和重复使用  
- **可视化**：直接查看性能指标、嵌入和结果  

### 这些笔记本有什么特别之处？

每个笔记本都遵循 **生产级最佳实践** 设计：

✅ **全面的错误处理** - 优雅降级和信息丰富的错误消息  
✅ **类型提示和文档** - 清晰的函数签名和文档字符串  
✅ **性能监控** - 令牌使用跟踪和延迟测量  
✅ **模块化设计** - 可重用的模式，适应您的项目  
✅ **逐步复杂性** - 系统性地建立在之前的课程基础上  

---

## 🎯 学习目标

### 您将掌握的核心技能

通过学习这些笔记本，您将掌握：

1. **本地 AI 服务管理**
   - 配置和管理 Microsoft Foundry Local 服务  
   - 根据硬件选择和加载适当的模型  
   - 监控资源使用并优化性能  
   - 处理服务发现和健康检查  

2. **AI 应用开发**
   - 本地实现兼容 OpenAI 的聊天补全  
   - 构建流式界面以提升用户体验  
   - 为小型语言模型设计有效的提示  
   - 将本地模型集成到应用程序中  

3. **检索增强生成 (RAG)**
   - 使用向量嵌入创建语义搜索  
   - 在领域特定文档中为 LLM 响应提供依据  
   - 使用 RAGAS 指标评估 RAG 质量  
   - 从原型扩展到生产环境  

4. **性能优化**
   - 系统性地对多个模型进行基准测试  
   - 测量延迟、吞吐量和首令牌时间  
   - 比较小型语言模型与大型语言模型  
   - 根据性能/质量权衡选择最佳模型  

5. **多代理编排**
   - 为不同任务设计专用代理  
   - 实现代理记忆和上下文管理  
   - 在复杂工作流中协调多个代理  
   - 构建代理协作的协调模式  

6. **智能模型路由**
   - 实现意图检测和模式匹配  
   - 自动将查询路由到适当的模型  
   - 构建多步骤管道（计划 → 执行 → 改进）  
   - 设计可扩展的模型工具架构  

---

## 🎓 学习成果

### 您将构建的内容

| 笔记本 | 交付成果 | 展示的技能 | 难度 |
|--------|----------|------------|------|
| **Session 01** | 带流式功能的聊天应用 | 服务设置、基础补全、流式 UX | ⭐ 初学者 |
| **Session 02 (RAG)** | 带评估功能的 RAG 管道 | 嵌入、语义搜索、质量指标 | ⭐⭐ 中级 |
| **Session 02 (Eval)** | RAG 质量评估器 | RAGAS 指标、系统性评估 | ⭐⭐ 中级 |
| **Session 03** | 多模型基准测试 | 性能测量、模型比较 | ⭐⭐ 中级 |
| **Session 04** | SLM 与 LLM 比较器 | 权衡分析、优化策略 | ⭐⭐⭐ 高级 |
| **Session 05** | 多代理编排器 | 代理设计、记忆、协调 | ⭐⭐⭐ 高级 |
| **Session 06 (Router)** | 智能路由系统 | 意图检测、模型选择 | ⭐⭐⭐ 高级 |
| **Session 06 (Pipeline)** | 多步骤管道 | 计划/执行/改进工作流 | ⭐⭐⭐ 高级 |

### 能力进阶

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 工作坊时间表

### 🚀 半日工作坊 (3.5 小时)

**适合：团队培训、黑客松、会议工作坊**

| 时间 | 时长 | 课程 | 主题 | 活动 |
|------|------|------|------|------|
| **0:00** | 30 分钟 | 设置与介绍 | 环境设置、Foundry Local 安装 | 安装依赖项，验证设置 |
| **0:30** | 30 分钟 | Session 01 | 基础聊天补全、流式功能 | 运行笔记本，修改提示 |
| **1:00** | 45 分钟 | Session 02 | RAG 管道、嵌入、评估 | 构建 RAG 系统，测试查询 |
| **1:45** | 15 分钟 | 休息 | ☕ 咖啡与问答 | — |
| **2:00** | 30 分钟 | Session 03 | 多模型基准测试 | 比较 3+ 模型 |
| **2:30** | 30 分钟 | Session 04 | SLM 与 LLM 权衡 | 分析性能/质量 |
| **3:00** | 30 分钟 | Session 05-06 | 多代理系统与路由 | 探索高级模式 |

**成果**：参与者将获得 6 个工作边缘 AI 应用和生产级代码模式。

---

### 🎓 全天工作坊 (6 小时)

**适合：深入培训、训练营、大学课程**

| 时间 | 时长 | 课程 | 主题 | 活动 |
|------|------|------|------|------|
| **0:00** | 45 分钟 | 设置与理论 | 环境设置、边缘 AI 基础 | 安装、验证、讨论用例 |
| **0:45** | 45 分钟 | Session 01 | 聊天补全深度解析 | 实现基础与流式聊天 |
| **1:30** | 30 分钟 | 休息 | ☕ 咖啡与交流 | — |
| **2:00** | 60 分钟 | Session 02 (两部分) | RAG 管道 + RAGAS 评估 | 构建完整 RAG 系统 |
| **3:00** | 30 分钟 | 实践实验室 1 | 定制领域的 RAG | 应用于自己的文档 |
| **3:30** | 30 分钟 | 午餐 | 🍽️ | — |
| **4:00** | 45 分钟 | Session 03 | 基准测试方法 | 系统性模型比较 |
| **4:45** | 45 分钟 | Session 04 | 优化策略 | SLM 与 LLM 分析 |
| **5:30** | 60 分钟 | Session 05-06 | 高级编排 | 多代理系统、路由 |
| **6:30** | 30 分钟 | 实践实验室 2 | 构建定制代理系统 | 设计自己的编排器 |

**成果**：深入理解边缘 AI 模式以及 2 个定制项目。

---

### 📚 自主学习 (2 周)

**适合：个人学习者、在线课程、自学**

#### 第 1 周：基础 (6 小时)

| 日期 | 重点 | 时长 | 笔记本 | 作业 |
|------|------|------|--------|------|
| **周一** | 设置与基础 | 1.5 小时 | Session 01 | 修改提示，测试流式功能 |
| **周三** | RAG 基础 | 2 小时 | Session 02 (两部分) | 添加自己的文档 |
| **周五** | 基准测试 | 1.5 小时 | Session 03 | 比较额外的模型 |
| **周六** | 复习与练习 | 1 小时 | 第 1 周所有内容 | 完成练习，调试问题 |

#### 第 2 周：高级 (5 小时)

| 日期 | 重点 | 时长 | 笔记本 | 作业 |
|------|------|------|--------|------|
| **周一** | 优化 | 1.5 小时 | Session 04 | 记录权衡分析 |
| **周三** | 多代理系统 | 2 小时 | Session 05 | 设计定制代理 |
| **周五** | 智能路由 | 1.5 小时 | Session 06 (两部分) | 构建路由逻辑 |
| **周六** | 最终项目 | 2 小时 | 集成 | 综合多个模式 |

**成果**：掌握边缘 AI 模式并完成作品集项目。

---

## 📔 笔记本描述

### 📘 Session 01: 聊天启动
**文件**: `session01_chat_bootstrap.ipynb`  
**时长**: 20-30 分钟  
**前置条件**: 无  
**难度**: ⭐ 初学者  

**您将学习**：
- 安装和配置 Foundry Local Python SDK  
- 使用 `FoundryLocalManager` 自动发现服务  
- 实现兼容 OpenAI 的基础聊天补全  
- 构建流式响应以提升用户体验  
- 优雅处理错误和服务不可用情况  

**关键概念**：服务管理、聊天补全、流式功能、错误处理  

**您将构建**：带流式支持的交互式聊天应用  

---

### 📗 Session 02: RAG 管道
**文件**: `session02_rag_pipeline.ipynb`  
**时长**: 30-45 分钟  
**前置条件**: Session 01  
**难度**: ⭐⭐ 中级  

**您将学习**：
- 实现检索增强生成 (RAG) 模式  
- 使用 sentence-transformers 创建向量嵌入  
- 使用余弦相似度构建语义搜索  
- 在领域文档中为 LLM 响应提供依据  
- 使用导入保护处理可选依赖项  

**关键概念**：RAG 架构、嵌入、语义搜索、向量相似度  

**您将构建**：基于文档的问答系统  

---

### 📗 Session 02: 使用 RAGAS 评估 RAG
**文件**: `session02_rag_eval_ragas.ipynb`  
**时长**: 30-45 分钟  
**前置条件**: Session 02 RAG 管道  
**难度**: ⭐⭐ 中级  

**您将学习**：
- 使用行业标准指标评估 RAG 质量  
- 测量上下文相关性、答案相关性、真实性  
- 使用 RAGAS 框架进行系统性评估  
- 识别并修复 RAG 质量问题  
- 为您的领域构建评估数据集  

**关键概念**：RAG 评估、RAGAS 指标、质量测量、系统性测试  

**您将构建**：RAG 质量评估框架  

---

### 📙 Session 03: 基准测试开源模型
**文件**: `session03_benchmark_oss_models.ipynb`  
**时长**: 30-45 分钟  
**前置条件**: Session 01  
**难度**: ⭐⭐ 中级  

**您将学习**：
- 系统性地对多个模型进行基准测试  
- 测量延迟、吞吐量、首令牌时间  
- 为模型故障实现优雅降级  
- 比较不同模型家族的性能  
- 可视化并分析基准测试结果  

**关键概念**：性能基准测试、延迟测量、模型比较、统计分析  

**您将构建**：多模型基准测试套件  

---

### 📙 Session 04: 模型比较 (SLM vs LLM)
**文件**: `session04_model_compare.ipynb`  
**时长**: 30-45 分钟  
**前置条件**: Sessions 01, 03  
**难度**: ⭐⭐⭐ 高级  

**您将学习**：
- 比较小型语言模型与大型语言模型  
- 分析性能与质量的权衡  
- 测量边缘适用性指标  
- 根据部署限制选择最佳模型  
- 记录模型选择的决策标准  

**关键概念**：模型选择、权衡分析、优化策略、部署规划  

**您将构建**：SLM 与 LLM 比较框架  

---

### 📕 Session 05: 多代理编排器
**文件**: `session05_agents_orchestrator.ipynb`  
**时长**: 45-60 分钟  
**前置条件**: Sessions 01-02  
**难度**: ⭐⭐⭐ 高级  

**您将学习**：
- 为不同任务设计专用代理  
- 实现代理记忆和上下文管理  
- 构建代理协作的协调模式  
- 处理代理间的通信和交接  
- 监控多代理系统性能  

**关键概念**：代理架构、协调模式、记忆管理、代理编排  

**您将构建**：带协调器和专家代理的多代理系统  

---

### 📕 Session 06: 模型路由器
**文件**: `session06_models_router.ipynb`  
**时长**: 30-45 分钟  
**前置条件**: Sessions 01, 03  
**难度**: ⭐⭐⭐ 高级  

**您将学习**：
- 实现意图检测和模式匹配  
- 构建基于关键词的模型路由  
- 自动将查询路由到适当的模型  
- 配置多模型注册表  
- 监控路由决策和性能  

**关键概念**：意图检测、模型路由、模式匹配、智能选择  

**您将构建**：智能模型路由系统  

---

### 📕 Session 06: 多步骤管道
**文件**: `session06_models_pipeline.ipynb`  
**时长**: 30-45 分钟  
**前置条件**: Sessions 01, 06 Router  
**难度**: ⭐⭐⭐ 高级  

**您将学习**：
- 构建多步骤 AI 管道（计划 → 执行 → 改进）  
- 集成路由器以实现智能模型选择  
- 实现管道错误处理和恢复  
- 监控管道性能和阶段  
- 设计可扩展的模型即工具架构

**关键概念**：流水线架构、多阶段处理、错误恢复、可扩展性模式

**你将构建**：具有路由功能的多步骤智能流水线

---

## 🚀 快速开始

### 先决条件

**系统要求**：
- **操作系统**：Windows 10/11、macOS 11+ 或 Linux (Ubuntu 20.04+)
- **内存**：最低 8GB，推荐 16GB 以上
- **存储**：至少 10GB 可用空间用于模型
- **硬件**：支持 AVX2 的 CPU；可选 GPU（CUDA、Qualcomm NPU）

**软件要求**：
- **Python 3.8+**，并安装 pip
- **Jupyter Notebook** 或 **VS Code**（带 Jupyter 扩展）
- 安装并配置 **Microsoft Foundry Local**
- **Git**（用于克隆代码库）

### 安装步骤

#### 1. 安装 Foundry Local

**Windows**：
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**：
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**验证安装**：
```bash
foundry --version
```

#### 2. 设置 Python 环境

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. 启动 Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. 启动 Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### 快速验证

在 Python 单元格中运行以下代码以验证设置：

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**预期输出**：来自本地模型的问候响应。

---

## 📝 研讨会最佳实践

### 对于讲师

**在研讨会之前**：
- ✅ 提前一周发送安装说明
- ✅ 在目标硬件上测试所有笔记本
- ✅ 准备常见问题的故障排除指南
- ✅ 准备备用模型（如果 phi-4-mini 失败，则使用 phi-3.5-mini）
- ✅ 设置共享的聊天渠道以便提问

**在研讨会期间**：
- ✅ 开始时快速检查环境（5 分钟）
- ✅ 立即分享故障排除资源
- ✅ 鼓励实验和修改
- ✅ 合理安排休息时间（每两节课后）
- ✅ 提供助教进行一对一帮助

**在研讨会之后**：
- ✅ 分享完整的工作笔记本和解决方案
- ✅ 提供额外资源的链接
- ✅ 创建反馈调查以便改进
- ✅ 提供后续问题的答疑时间

### 对于学习者

**最大化学习效果**：
- ✅ 在研讨会开始前完成设置
- ✅ 自己运行每个代码单元（不要只是阅读）
- ✅ 尝试调整参数和提示
- ✅ 记录见解和注意事项
- ✅ 遇到问题时提问（其他人可能也有同样的问题）

**常见错误需避免**：
- ❌ 跳过单元格的执行顺序（需按顺序运行）
- ❌ 不仔细阅读错误信息
- ❌ 匆忙完成而不理解内容
- ❌ 忽略 markdown 的解释
- ❌ 不保存修改后的笔记本

**调试提示**：
1. **服务未运行**：检查 `foundry service status`
2. **导入错误**：确认虚拟环境已激活
3. **未找到模型**：运行 `foundry model ls` 查看已加载的模型
4. **性能缓慢**：检查内存使用情况，关闭其他应用程序
5. **结果异常**：重启内核并从头运行所有单元格

---

## 🔗 额外资源

### 研讨会材料

- **[研讨会主指南](../Readme.md)** - 概述、学习目标、职业发展
- **[Python 示例](../../../../Workshop/samples)** - 每节课对应的 Python 脚本
- **[课程指南](../../../../Workshop)** - 详细的 markdown 指南（Session01-06）
- **[脚本](../../../../Workshop/scripts)** - 验证和测试工具
- **[故障排除](./TROUBLESHOOTING.md)** - 常见问题及解决方案
- **[快速开始](./quickstart.md)** - 快速入门指南

### 文档

- **[Foundry Local 文档](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Microsoft 官方文档
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK 参考
- **[Sentence Transformers](https://www.sbert.net/)** - 嵌入模型文档
- **[RAGAS 框架](https://docs.ragas.io/)** - RAG 评估指标

### 社区

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - 提问、分享项目
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - 实时社区支持
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - 技术问答

---

## 🎯 学习路径推荐

### 初学者路径（从这里开始）

1. **Session 01** - 聊天启动
2. **Session 02** - RAG 流水线
3. **Session 03** - 模型基准测试

**时间**：约 2 小时 | **重点**：基础模式

---

### 中级路径

1. 完成初学者路径
2. **Session 02** - RAG 评估
3. **Session 04** - 模型比较

**时间**：约 4 小时 | **重点**：质量和优化

---

### 高级路径（完整研讨会）

1. 完成中级路径
2. **Session 05** - 多代理协调器
3. **Session 06** - 模型路由器
4. **Session 06** - 多步骤流水线

**时间**：约 6 小时 | **重点**：生产模式

---

### 自定义项目路径

1. 完成初学者路径（Session 01-03）
2. 根据目标选择一个高级课程：
   - **构建 RAG 应用？** → Session 02 评估
   - **优化性能？** → Session 04 比较
   - **复杂工作流？** → Session 05 协调器
   - **可扩展架构？** → Session 06 路由器 + 流水线

**时间**：约 3 小时 | **重点**：项目特定技能

---

## 📊 成功指标

通过以下里程碑跟踪您的进度：

- [ ] **完成设置** - Foundry Local 运行，所有依赖项已安装
- [ ] **首次聊天** - 完成 Session 01，流式聊天功能正常
- [ ] **构建 RAG** - 完成 Session 02，文档问答系统正常运行
- [ ] **模型基准测试** - 完成 Session 03，收集性能数据
- [ ] **分析权衡** - 完成 Session 04，记录模型选择标准
- [ ] **协调代理** - 完成 Session 05，多代理系统正常运行
- [ ] **实现路由** - 完成 Session 06，智能模型选择功能正常
- [ ] **自定义项目** - 将研讨会模式应用于您的用例

---

## 🤝 贡献

发现问题或有建议？我们欢迎您的贡献！

- **报告问题**：[GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **提出改进建议**：[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **提交 PR**：请遵循 [贡献指南](../../AGENTS.md)

---

## 📄 许可证

本研讨会是 [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) 仓库的一部分，遵循 [MIT 许可证](../../../../LICENSE)。

---

**准备好构建生产级的边缘 AI 应用了吗？**  
**从 [Session 01: 聊天启动](./session01_chat_bootstrap.ipynb) 开始 →**

---

*最后更新：2025 年 10 月 8 日 | 研讨会版本：2.0*

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而引起的任何误解或误读，我们概不负责。