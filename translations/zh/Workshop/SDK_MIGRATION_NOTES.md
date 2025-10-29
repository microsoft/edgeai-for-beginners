<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:36:41+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "zh"
}
-->
# Foundry本地SDK迁移说明

## 概述

Workshop文件夹中的所有Python文件已更新，以遵循官方[Foundry本地Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local)的最新模式。

## 变更摘要

### 核心基础设施 (`workshop_utils.py`)

#### 增强功能：
- **端点覆盖支持**：新增支持环境变量`FOUNDRY_LOCAL_ENDPOINT`
- **改进的错误处理**：更好的异常处理，提供详细的错误信息
- **增强的缓存**：缓存键现在包含端点，以支持多端点场景
- **指数退避**：重试逻辑现在使用指数退避以提高可靠性
- **类型注解**：添加了全面的类型提示以支持IDE

#### 新功能：
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### 示例应用

#### Session 01: 聊天引导 (`chat_bootstrap.py`)
- 默认模型从`phi-3.5-mini`更新为`phi-4-mini`
- 添加端点覆盖支持
- 使用SDK参考增强文档

#### Session 02: RAG管道 (`rag_pipeline.py`)
- 默认模型更新为`phi-4-mini`
- 添加端点覆盖支持
- 增强文档，包含环境变量详细信息

#### Session 02: RAG评估 (`rag_eval_ragas.py`)
- 更新默认模型
- 添加端点配置
- 改进错误处理

#### Session 03: 基准测试 (`benchmark_oss_models.py`)
- 默认模型列表更新，包含`phi-4-mini`
- 添加全面的环境变量文档
- 改进函数文档
- 全面支持端点覆盖

#### Session 04: 模型比较 (`model_compare.py`)
- 默认LLM从`gpt-oss-20b`更新为`qwen2.5-7b`
- 添加端点配置
- 增强文档

#### Session 05: 多代理编排 (`agents_orchestrator.py`)
- 添加类型提示（将`str | None`更改为`Optional[str]`）
- 增强Agent类文档
- 添加端点覆盖支持
- 改进初始化模式

#### Session 06: 模型路由器 (`models_router.py`)
- 添加端点配置
- 增强意图检测文档
- 改进路由逻辑文档

#### Session 06: 管道 (`models_pipeline.py`)
- 添加全面的函数文档
- 改进逐步文档
- 增强错误处理

### 脚本

#### 基准导出 (`export_benchmark_markdown.py`)
- 添加端点覆盖支持
- 更新默认模型
- 增强函数文档
- 改进错误处理

#### CLI代码检查器 (`lint_markdown_cli.py`)
- 添加SDK参考链接
- 改进使用文档

### 测试

#### 冒烟测试 (`smoke.py`)
- 添加端点覆盖支持
- 增强文档
- 改进测试用例文档
- 更好的错误报告

## 环境变量

所有示例现在支持以下环境变量：

### 核心配置
- `FOUNDRY_LOCAL_ALIAS` - 使用的模型别名（默认值因示例而异）
- `FOUNDRY_LOCAL_ENDPOINT` - 覆盖服务端点（可选）
- `SHOW_USAGE` - 显示令牌使用统计（默认值："0"）
- `RETRY_ON_FAIL` - 启用重试逻辑（默认值："1"）
- `RETRY_BACKOFF` - 初始重试延迟时间（秒）（默认值："1.0"）

### 示例特定
- `EMBED_MODEL` - RAG示例的嵌入模型
- `BENCH_MODELS` - 基准测试的逗号分隔模型
- `BENCH_ROUNDS` - 基准测试轮数
- `BENCH_PROMPT` - 基准测试的测试提示
- `BENCH_STREAM` - 测量首个令牌延迟
- `RAG_QUESTION` - RAG示例的测试问题
- `AGENT_MODEL_PRIMARY` - 主代理模型
- `AGENT_MODEL_EDITOR` - 编辑代理模型
- `SLM_ALIAS` - 小型语言模型别名
- `LLM_ALIAS` - 大型语言模型别名

## 实施的SDK最佳实践

### 1. 正确的客户端初始化
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. 模型信息检索
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. 错误处理
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. 带指数退避的重试逻辑
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. 流式支持
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## 自定义示例的迁移指南

如果您正在创建新示例或更新现有示例：

1. **使用`workshop_utils.py`助手**：
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **支持端点覆盖**：
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **添加全面的文档**：
   - 在文档字符串中包含环境变量
   - SDK参考链接
   - 使用示例

4. **使用类型提示**：
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **实施正确的错误处理**：
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## 测试

所有示例可以通过以下方式测试：

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK文档参考

- **主仓库**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API文档**: 请查看SDK仓库以获取最新API文档

## 重大变更

### 无预期
所有更改均向后兼容。更新主要包括：
- 添加新的可选功能（端点覆盖）
- 改进错误处理
- 增强文档
- 更新默认模型名称以符合当前推荐

### 可选增强
您可能希望更新代码以使用：
- `FOUNDRY_LOCAL_ENDPOINT`进行显式端点控制
- `SHOW_USAGE=1`以显示令牌使用情况
- 更新的默认模型（`phi-4-mini`替代`phi-3.5-mini`）

## 常见问题及解决方案

### 问题: "客户端初始化失败"
**解决方案**: 确保Foundry本地服务正在运行：
```bash
foundry service start
foundry model run phi-4-mini
```

### 问题: "模型未找到"
**解决方案**: 检查可用模型：
```bash
foundry model list
```

### 问题: 端点连接错误
**解决方案**: 验证端点：
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## 下一步

1. **更新Module08示例**: 将类似模式应用于Module08/samples
2. **添加集成测试**: 创建全面的测试套件
3. **性能基准测试**: 比较更新前后的性能
4. **文档更新**: 使用新模式更新主README

## 贡献指南

添加新示例时：
1. 使用`workshop_utils.py`以保持一致性
2. 遵循现有示例中的模式
3. 添加全面的文档字符串
4. 包含SDK参考链接
5. 支持端点覆盖
6. 添加正确的类型提示
7. 在文档字符串中包含使用示例

## 版本兼容性

这些更新与以下版本兼容：
- `foundry-local-sdk`（最新版本）
- `openai>=1.30.0`
- Python 3.8+

---

**最后更新日期**: 2025-01-08  
**维护者**: EdgeAI Workshop团队  
**SDK版本**: Foundry Local SDK (最新0.7.117+67073234e7)

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。