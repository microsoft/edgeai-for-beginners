<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T11:08:16+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "zh"
}
-->
# 更新日志

所有关于 EdgeAI for Beginners 的重要更新都记录在此。本项目采用基于日期的条目和 Keep a Changelog 风格（新增、变更、修复、移除、文档、移动）。

## 2025-10-30

### 新增 - Module06 AI代理全面增强
- **Microsoft Agent Framework集成** (`Module06/01.IntroduceAgent.md`):
  - 完整的 Microsoft Agent Framework 章节，用于生产级代理开发
  - 与 Foundry Local 的详细集成模式，用于边缘部署
  - 使用专业化的SLM模型进行多代理编排示例
  - 企业部署模式，包括资源管理和监控
  - 用于边缘代理系统的安全性和合规性功能
  - 实际应用示例（零售、医疗、客户服务）

- **生产级SLM代理部署策略**：
  - **Foundry Local**：企业级边缘AI运行时的完整文档，包括安装、配置和生产模式
  - **Ollama**：增强的社区化部署，提供全面的监控和模型管理
  - **VLLM**：高性能推理引擎，具有高级优化技术和企业功能
  - 所有三个平台的生产部署清单和比较表

- **边缘优化SLM框架增强**：
  - **ONNX Runtime**：新增跨平台SLM代理部署的全面章节
  - 跨 Windows、Linux、macOS、iOS 和 Android 的通用部署模式
  - 硬件加速选项（CPU、GPU、NPU），具有自动检测功能
  - 生产级功能和代理特定优化
  - 包含 Microsoft Agent Framework 集成的完整实现示例

- **参考资料和进一步阅读**：
  - 包含100+权威资源的综合资源库
  - 关于AI代理和小型语言模型的核心研究论文
  - 所有主要框架和工具的官方文档
  - 行业报告、市场分析和技术基准
  - 教育资源、会议和社区论坛
  - 标准、规范和合规框架

### 变更 - Module06内容现代化
- **增强学习目标**：新增 Microsoft Agent Framework 精通和边缘部署能力
- **生产重点**：从概念转向实施准备指导，提供生产示例
- **代码示例**：更新所有示例以使用现代SDK模式和最佳实践
- **架构模式**：新增分层代理架构和边缘到云的协调
- **性能优化**：增强资源管理和自动扩展建议

### 文档 - Module06结构增强
- **全面的代理框架覆盖**：从基础概念到企业部署
- **生产部署策略**：Foundry Local、Ollama 和 VLLM 的完整指南
- **跨平台优化**：新增 ONNX Runtime 用于通用部署
- **资源库**：广泛的参考资料，用于持续学习和实施

### 新增 - Module06模型上下文协议 (MCP) 文档更新
- **MCP介绍现代化** (`Module06/03.IntroduceMCP.md`):
  - 更新至最新的 MCP 规范（modelcontextprotocol.io，2025-06-18版本）
  - 添加官方 USB-C 类比，用于标准化 AI 应用连接
  - 更新架构部分，包含官方两层设计（数据层 + 传输层）
  - 增强核心原语文档，包含服务器原语（工具、资源、提示）和客户端原语（采样、引导、日志记录）

- **全面的 MCP 参考和资源**：
  - 添加 **MCP for Beginners** 链接 (https://aka.ms/mcp-for-beginners)
  - 官方 MCP 文档和规范 (modelcontextprotocol.io)
  - 开发资源，包括 MCP Inspector 和参考实现
  - 技术标准 (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### 新增 - Module04 Qualcomm QNN集成
- **新增第7节：Qualcomm QNN优化套件** (`Module04/05.QualcommQNN.md`):
  - 涵盖Qualcomm统一AI推理框架的全面400+行指南
  - 详细介绍异构计算（Hexagon NPU、Adreno GPU、Kryo CPU）
  - 针对Snapdragon平台的硬件感知优化，智能工作负载分配
  - 高级量化技术（INT8、INT16、混合精度）用于移动部署
  - 针对电池供电设备和实时应用的节能推理优化
  - 完整安装指南，包括QNN SDK设置和环境配置
  - 实用示例：PyTorch到QNN转换、多后端优化、上下文二进制生成
  - 高级使用模式：自定义后端配置、动态量化、性能分析
  - 全面的故障排除部分和社区资源

- **增强的Module04结构**：
  - 更新README.md，包含7个渐进式章节（之前为6个）
  - 将Qualcomm QNN添加到性能基准表（5-15倍速度提升，50-80%内存减少）
  - 增强学习成果，涵盖移动AI部署和功耗优化

### 变更 - Module04文档更新
- **Microsoft Olive文档增强** (`Module04/03.MicrosoftOlive.md`):
  - 添加全面的“Olive Recipes Repository”章节，涵盖100+预构建优化配方
  - 详细介绍支持的模型系列（Phi、Llama、Qwen、Gemma、Mistral、DeepSeek）
  - 提供配方定制和社区贡献的实用示例
  - 增强性能基准和集成指导

- **Module04章节重新排序**：
  - Apple MLX移至第5节（之前为第6节）
  - 工作流合成移至第6节（之前为第7节）
  - Qualcomm QNN定位为第7节（专注于移动/边缘）
  - 更新所有文件参考和导航链接

### 修复 - 研讨会样本验证
- **chat_bootstrap.py验证和修复**：
  - 修复损坏的导入语句 (`util.util.workshop_utils` → `util.workshop_utils`)
  - 在util包中创建缺失的`__init__.py`，以正确解析Python模块
  - 在conda环境中安装所需依赖项（openai, foundry-local-sdk）
  - 成功验证样本执行，包括默认和自定义提示
  - 确认与Foundry Local服务和模型加载（phi-4-mini，带CUDA优化）的集成

### 文档 - 全面指南更新
- **Module04 README.md完整重构**：
  - 添加Qualcomm QNN作为主要优化框架，与OpenVINO、Olive、MLX并列
  - 更新章节学习成果，包含移动AI部署和功耗优化
  - 增强性能比较表，包含QNN指标和移动/边缘用例
  - 保持从企业解决方案到平台特定优化的逻辑进展

- **交叉引用和导航**：
  - 更新所有内部链接和文件参考，适应新章节编号
  - 增强工作流合成描述，涵盖移动、桌面和云环境
  - 添加Qualcomm开发者生态系统的全面资源链接

## 2025-10-08

### 新增 - 研讨会全面更新
- **研讨会README.md完整重写**：
  - 添加全面介绍，解释边缘AI的价值主张（隐私、性能、成本）
  - 创建6个核心学习目标，包含详细能力
  - 添加学习成果表，包含交付物和能力矩阵
  - 包含行业相关的职业技能部分
  - 添加快速入门指南，包含先决条件和3步设置
  - 创建资源表，用于Python样本（8个文件及运行时间）
  - 添加Jupyter笔记本表（8个笔记本及难度评级）
  - 创建文档表（7个关键文档及“使用场景”指导）
  - 添加不同技能水平的学习路径推荐

- **研讨会验证和测试基础设施**：
  - 创建`scripts/validate_samples.py` - 综合验证工具，用于语法、导入和最佳实践
  - 创建`scripts/test_samples.py` - 用于所有Python样本的烟雾测试运行器
  - 添加验证文档至`scripts/README.md`

- **全面文档**：
  - 创建`SAMPLES_UPDATE_SUMMARY.md` - 400+行详细指南，涵盖所有改进
  - 创建`UPDATE_COMPLETE.md` - 更新完成的执行摘要
  - 创建`QUICK_REFERENCE.md` - 研讨会的快速参考卡

### 变更 - 研讨会Python样本现代化
- **所有8个Python样本更新为最佳实践**：
  - 增强错误处理，在所有I/O操作周围添加try-except块
  - 添加类型提示和全面的文档字符串
  - 实现一致的[INFO]/[ERROR]/[RESULT]日志记录模式
  - 使用安装提示保护可选导入
  - 改善用户反馈，贯穿所有样本

- **session01/chat_bootstrap.py**：
  - 增强客户端初始化，提供全面的错误信息
  - 改善流式错误处理，添加块验证
  - 添加服务不可用的更好异常处理

- **session02/rag_pipeline.py**：
  - 添加句子转换器的导入保护，附安装提示
  - 增强嵌入和生成操作的错误处理
  - 改善输出格式，提供结构化结果

- **session02/rag_eval_ragas.py**：
  - 保护可选导入（ragas, datasets），提供用户友好的错误信息
  - 添加评估指标的错误处理
  - 改善评估结果的输出格式

- **session03/benchmark_oss_models.py**：
  - 实现优雅降级（在模型失败时继续运行）
  - 添加详细的进度报告和每个模型的错误处理
  - 增强统计计算，提供全面的错误恢复

- **session04/model_compare.py**：
  - 添加类型提示（元组返回类型）
  - 改善输出格式，提供结构化JSON结果
  - 实现每个模型的错误处理和恢复

- **session05/agents_orchestrator.py**：
  - 增强Agent.act()，提供全面的文档字符串
  - 添加管道错误处理，提供阶段性日志记录
  - 改善内存管理和状态跟踪

- **session06/models_router.py**：
  - 增强所有路由组件的函数文档
  - 在route()函数中添加详细日志记录
  - 改善测试输出，提供结构化结果

- **session06/models_pipeline.py**：
  - 在chat()辅助函数中添加错误处理
  - 在pipeline()中增强阶段日志记录和进度报告
  - 在main()中改善错误恢复

### 文档 - 研讨会文档增强
- 更新主README.md，突出研讨会部分，强调动手学习路径
- 增强STUDY_GUIDE.md，包含全面的研讨会部分，包括：
  - 学习目标和学习重点领域
  - 自我评估问题
  - 动手练习及时间估算
  - 集中和兼职学习的时间分配
  - 添加研讨会至进度跟踪模板
- 将时间分配指南从20小时更新为30小时（包括研讨会）
- 添加研讨会样本描述和学习成果至README

### 修复
- 解决研讨会样本中不一致的错误处理模式
- 修复可选依赖导入错误，添加适当保护
- 修正关键函数中缺失的类型提示
- 解决错误场景中用户反馈不足的问题
- 修复验证问题，提供全面的测试基础设施

---

## 2025-09-23

### 变更 - Module 08重大现代化
- **全面与Microsoft Foundry-Local存储库模式对齐**
  - 更新所有代码示例，使用现代`FoundryLocalManager`和OpenAI SDK集成
  - 用正确的SDK使用替换过时的手动`requests`调用
  - 与官方Microsoft文档和示例对齐实施模式

- **05.AIPoweredAgents.md现代化**：
  - 更新多代理编排，使用现代SDK模式
  - 增强协调器实现，添加高级功能（反馈循环、性能监控）
  - 添加全面的错误处理和服务健康检查
  - 正确引用本地样本（`samples/05/multi_agent_orchestration.ipynb`）
  - 更新函数调用示例，使用现代`tools`参数替代过时的`functions`
  - 添加生产级模式，包含监控和统计跟踪

- **06.ModelsAsTools.md完整重写**：
  - 用智能模型路由器实现替代基本工具注册表
  - 添加基于关键词的模型选择，用于不同任务类型（通用、推理、代码、创意）
  - 集成基于环境的配置，提供灵活的模型分配
  - 增强服务健康监控和错误处理
  - 添加生产部署模式，包含请求监控和性能跟踪
  - 与本地实现对齐（`samples/06/router.py`和`samples/06/model_router.ipynb`）

- **文档结构改进**：
  - 添加概述部分，突出现代化和SDK对齐
  - 增强格式，使用表情符号和更好的排版，提升可读性
  - 正确引用本地样本文件，贯穿文档
  - 包含生产级实施指导和最佳实践

### 新增
- Module 08文件中的全面概述部分，突出现代SDK集成
- 架构亮点，展示高级功能（多代理系统、智能路由）
- 直接引用本地样本实现，用于动手体验
- 生产部署指导，包含监控和错误处理模式
- 交互式Jupyter笔记本示例，包含高级功能和基准测试

### 修复
- 文档与实际样本实现之间的对齐差异
- Module 08中过时的SDK使用模式
- 缺失全面的本地样本库引用
- 不同章节间不一致的实施方法

---

## 2025-09-18

### 新增
- Module 08: Microsoft Foundry Local – 完整开发者工具包
  - 六个课程：设置、Azure AI Foundry集成、开源模型、尖端演示、代理和模型作为工具
- 可运行示例位于 `Module08/samples/01`–`06`，包含 Windows cmd 指令
  - `01` REST 快速聊天 (`chat_quickstart.py`)
  - `02` SDK 快速入门，支持 OpenAI/Foundry Local 和 Azure OpenAI (`sdk_quickstart.py`)
  - `03` CLI 列表与基准测试 (`list_and_bench.cmd`)
  - `04` Chainlit 演示 (`app.py`)
  - `05` 多代理编排 (`python -m samples.05.agents.coordinator`)
  - `06` 模型工具路由器 (`router.py`)
- Session 2 SDK 示例中支持 Azure OpenAI，使用环境变量配置
- `.vscode/settings.json` 指向 `Module08/.venv`，提升 Python 分析解析能力
- `.env` 文件中添加 `PYTHONPATH` 提示，以便 VS Code/Pylance 识别

### 更改
- 默认模型更新为 `phi-4-mini`，覆盖 Module 08 文档和示例；移除 Module 08 中剩余的 `phi-3.5` 提及
- 路由器 (`Module08/samples/06/router.py`) 改进：
  - 通过 `foundry service status` 使用正则表达式解析进行端点发现
  - 启动时进行 `/v1/models` 健康检查
  - 环境变量可配置的模型注册表 (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- 更新依赖项：`Module08/requirements.txt` 现在包括 `openai`（以及 `requests`, `chainlit`）
- 明确 Chainlit 示例指导并添加故障排除；通过工作区设置解决导入问题

### 修复
- 解决导入问题：
  - 路由器不再依赖不存在的 `utils` 模块；相关函数已内联
  - 协调器使用相对导入 (`from .specialists import ...`)，通过模块路径调用
  - 配置 VS Code/Pylance 以解决 `chainlit` 和包导入问题
- 修正 `STUDY_GUIDE.md` 中的小错误，并添加 Module 08 的覆盖内容

### 移除
- 删除未使用的 `Module08/infra/obs.py`，并移除空的 `infra/` 目录；文档中保留可选的可观测性模式

### 移动
- 将 Module 08 演示整合到 `Module08/samples` 中，按会话编号分类
  - 将 Chainlit 应用移至 `samples/04`
  - 将代理移至 `samples/05`，并添加 `__init__.py` 文件以解决包解析问题

### 文档
- 丰富了 Module 08 会话文档和所有示例的 README，添加了 Microsoft Learn 和可信供应商参考
- 更新了 `Module08/README.md`，包括示例概览、路由器配置和验证提示
- 验证了 `Module07/README.md` 中的 Windows Foundry Local 部分与 Learn 文档的一致性
- 更新了 `STUDY_GUIDE.md`：
  - 在概览、时间表、进度追踪中添加了 Module 08
  - 增加了全面的参考部分（Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML）

---

## 历史记录（摘要）
- 建立课程架构和模块（Modules 01–07）
- 迭代内容现代化、格式标准化，并添加案例研究
- 扩展优化框架覆盖范围（Llama.cpp, Olive, OpenVINO, Apple MLX）

## 未发布 / 待办事项（建议）
- 为每个示例添加可选的冒烟测试，以验证 Foundry Local 的可用性
- 审核翻译以确保模型引用的一致性（例如 `phi-4-mini`）
- 如果团队偏好工作区范围的严格性，建议添加最小的 pyright 配置

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。