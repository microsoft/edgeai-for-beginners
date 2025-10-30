<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T22:34:56+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "vi"
}
-->
# Thẻ Tham Khảo Nhanh - Mẫu Workshop

**Cập nhật lần cuối**: 8 tháng 10, 2025

---

## 🚀 Bắt Đầu Nhanh

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

## 📂 Tổng Quan Mẫu

| Phiên | Mẫu | Mục Đích | Thời Gian |
|-------|-----|----------|-----------|
| 01 | `chat_bootstrap.py` | Chat cơ bản + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG với embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | Đánh giá RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Đánh giá hiệu năng mô hình | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Hệ thống đa tác nhân | ~60s |
| 06 | `models_router.py` | Định tuyến ý định | ~45s |
| 06 | `models_pipeline.py` | Quy trình nhiều bước | ~60s |

---

## 🛠️ Biến Môi Trường

### Cần Thiết
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Theo Phiên
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

## ✅ Xác Thực & Kiểm Tra

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

## 🐛 Xử Lý Lỗi

### Lỗi Kết Nối
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Lỗi Import
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Không Tìm Thấy Mô Hình
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Hiệu Năng Chậm
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Mẫu Thường Dùng

### Chat Cơ Bản
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Lấy Client
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Xử Lý Lỗi
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Streaming
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

## 📊 Lựa Chọn Mô Hình

| Mô Hình | Kích Thước | Tốt Nhất Cho | Tốc Độ |
|---------|------------|--------------|--------|
| `qwen2.5-0.5b` | 0.5B | Phân loại nhanh | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Sinh mã nhanh | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Viết sáng tạo | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Mã, tái cấu trúc | ⚡⚡ |
| `phi-4-mini` | 4B | Tổng quát, tóm tắt | ⚡⚡ |
| `qwen2.5-7b` | 7B | Lý luận phức tạp | ⚡ |

---

## 🔗 Tài Nguyên

- **Tài liệu SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Tham Khảo Nhanh**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Tóm Tắt Cập Nhật**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Ghi Chú Di Chuyển**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Mẹo

1. **Bộ nhớ cache client**: `workshop_utils` tự động lưu trữ cho bạn
2. **Dùng mô hình nhỏ hơn**: Bắt đầu với `qwen2.5-0.5b` để thử nghiệm
3. **Bật thống kê sử dụng**: Đặt `SHOW_USAGE=1` để theo dõi token
4. **Xử lý hàng loạt**: Xử lý nhiều prompt liên tiếp
5. **Giảm max_tokens**: Giảm độ trễ cho phản hồi nhanh

---

## 🎯 Quy Trình Mẫu

### Kiểm Tra Tất Cả
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Đánh Giá Mô Hình
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### Quy Trình RAG
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Hệ Thống Đa Tác Nhân
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Trợ Giúp Nhanh**: Chạy bất kỳ mẫu nào với `--help` từ thư mục `samples` hoặc kiểm tra docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Tất cả các mẫu đã được cập nhật vào tháng 10 năm 2025 với các thực hành tốt nhất của Foundry Local SDK** ✨

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.