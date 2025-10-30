<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T20:36:17+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "zh"
}
-->
# 工作坊示例 - 快速参考卡

**最后更新**：2025年10月8日

---

## 🚀 快速开始

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 示例概览

| 会话 | 示例 | 目的 | 时间 |
|------|------|------|------|
| 01 | `chat_bootstrap.py` | 基础聊天 + 流式传输 | ~30秒 |
| 02 | `rag_pipeline.py` | RAG与嵌入 | ~45秒 |
| 02 | `rag_eval_ragas.py` | RAG评估 | ~60秒 |
| 03 | `benchmark_oss_models.py` | 模型基准测试 | ~2分钟 |
| 04 | `model_compare.py` | SLM与LLM对比 | ~45秒 |
| 05 | `agents_orchestrator.py` | 多代理系统 | ~60秒 |
| 06 | `models_router.py` | 意图路由 | ~45秒 |
| 06 | `models_pipeline.py` | 多步骤管道 | ~60秒 |

---

## 🛠️ 环境变量

### 必需
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### 会话特定
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ 验证与测试

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 故障排除

### 连接错误
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### 导入错误
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### 模型未找到
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### 性能缓慢
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 常见模式

### 基础聊天
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### 获取客户端
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### 错误处理
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 流式传输
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 模型选择

| 模型 | 大小 | 最适合 | 速度 |
|------|------|--------|------|
| `qwen2.5-0.5b` | 0.5B | 快速分类 | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | 快速代码生成 | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | 创意写作 | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | 代码、重构 | ⚡⚡ |
| `phi-4-mini` | 4B | 通用、摘要 | ⚡⚡ |
| `qwen2.5-7b` | 7B | 复杂推理 | ⚡ |

---

## 🔗 资源

- **SDK文档**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **快速参考**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **更新摘要**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **迁移说明**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 提示

1. **缓存客户端**：`workshop_utils`会为您缓存
2. **使用较小的模型**：测试时从`qwen2.5-0.5b`开始
3. **启用使用统计**：设置`SHOW_USAGE=1`以跟踪token使用情况
4. **批量处理**：按顺序处理多个提示
5. **降低max_tokens**：减少延迟以获得快速响应

---

## 🎯 示例工作流

### 测试所有内容
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### 基准测试模型
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG管道
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### 多代理系统
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**快速帮助**：从`samples`目录运行任何示例并使用`--help`，或查看文档字符串：
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**所有示例已于2025年10月更新，符合Foundry Local SDK最佳实践** ✨

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。