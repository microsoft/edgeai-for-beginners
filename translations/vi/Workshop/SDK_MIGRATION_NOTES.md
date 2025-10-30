<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:35:25+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "vi"
}
-->
# Ghi chú di chuyển SDK Local Foundry

## Tổng quan

Tất cả các tệp Python trong thư mục Workshop đã được cập nhật để tuân theo các mẫu mới nhất từ [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Tóm tắt thay đổi

### Hạ tầng cốt lõi (`workshop_utils.py`)

#### Tính năng nâng cao:
- **Hỗ trợ ghi đè Endpoint**: Thêm hỗ trợ biến môi trường `FOUNDRY_LOCAL_ENDPOINT`
- **Cải thiện xử lý lỗi**: Xử lý ngoại lệ tốt hơn với thông báo lỗi chi tiết
- **Tăng cường bộ nhớ đệm**: Các khóa bộ nhớ đệm hiện bao gồm endpoint cho các kịch bản đa endpoint
- **Backoff lũy thừa**: Logic thử lại hiện sử dụng backoff lũy thừa để tăng độ tin cậy
- **Chú thích kiểu**: Thêm các gợi ý kiểu toàn diện để hỗ trợ tốt hơn cho IDE

#### Khả năng mới:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Ứng dụng mẫu

#### Phiên 01: Khởi động Chat (`chat_bootstrap.py`)
- Cập nhật mô hình mặc định từ `phi-3.5-mini` sang `phi-4-mini`
- Thêm hỗ trợ ghi đè endpoint
- Tăng cường tài liệu với tham chiếu SDK

#### Phiên 02: Pipeline RAG (`rag_pipeline.py`)
- Cập nhật để sử dụng `phi-4-mini` làm mặc định
- Thêm hỗ trợ ghi đè endpoint
- Cải thiện tài liệu với chi tiết biến môi trường

#### Phiên 02: Đánh giá RAG (`rag_eval_ragas.py`)
- Cập nhật mặc định mô hình
- Thêm cấu hình endpoint
- Tăng cường xử lý lỗi

#### Phiên 03: Đánh giá hiệu năng (`benchmark_oss_models.py`)
- Cập nhật danh sách mô hình mặc định để bao gồm `phi-4-mini`
- Thêm tài liệu biến môi trường toàn diện
- Cải thiện tài liệu chức năng
- Thêm hỗ trợ ghi đè endpoint toàn bộ

#### Phiên 04: So sánh mô hình (`model_compare.py`)
- Cập nhật LLM mặc định từ `gpt-oss-20b` sang `qwen2.5-7b`
- Thêm cấu hình endpoint
- Tăng cường tài liệu

#### Phiên 05: Điều phối đa tác nhân (`agents_orchestrator.py`)
- Thêm gợi ý kiểu (thay đổi `str | None` thành `Optional[str]`)
- Tăng cường tài liệu lớp Agent
- Thêm hỗ trợ ghi đè endpoint
- Cải thiện mẫu khởi tạo

#### Phiên 06: Bộ định tuyến mô hình (`models_router.py`)
- Thêm cấu hình endpoint
- Tăng cường tài liệu phát hiện ý định
- Cải thiện tài liệu logic định tuyến

#### Phiên 06: Pipeline (`models_pipeline.py`)
- Thêm tài liệu chức năng toàn diện
- Cải thiện tài liệu từng bước
- Tăng cường xử lý lỗi

### Scripts

#### Xuất đánh giá hiệu năng (`export_benchmark_markdown.py`)
- Thêm hỗ trợ ghi đè endpoint
- Cập nhật mô hình mặc định
- Tăng cường tài liệu chức năng
- Cải thiện xử lý lỗi

#### CLI Linter (`lint_markdown_cli.py`)
- Thêm liên kết tham chiếu SDK
- Cải thiện tài liệu sử dụng

### Tests

#### Kiểm tra nhanh (`smoke.py`)
- Thêm hỗ trợ ghi đè endpoint
- Tăng cường tài liệu
- Cải thiện tài liệu trường hợp kiểm tra
- Báo cáo lỗi tốt hơn

## Biến môi trường

Tất cả các mẫu hiện hỗ trợ các biến môi trường sau:

### Cấu hình cốt lõi
- `FOUNDRY_LOCAL_ALIAS` - Bí danh mô hình để sử dụng (mặc định thay đổi theo mẫu)
- `FOUNDRY_LOCAL_ENDPOINT` - Ghi đè endpoint dịch vụ (tùy chọn)
- `SHOW_USAGE` - Hiển thị thống kê sử dụng token (mặc định: "0")
- `RETRY_ON_FAIL` - Bật logic thử lại (mặc định: "1")
- `RETRY_BACKOFF` - Độ trễ thử lại ban đầu tính bằng giây (mặc định: "1.0")

### Cụ thể theo mẫu
- `EMBED_MODEL` - Mô hình nhúng cho các mẫu RAG
- `BENCH_MODELS` - Các mô hình phân cách bằng dấu phẩy để đánh giá hiệu năng
- `BENCH_ROUNDS` - Số vòng đánh giá hiệu năng
- `BENCH_PROMPT` - Lời nhắc kiểm tra cho đánh giá hiệu năng
- `BENCH_STREAM` - Đo độ trễ token đầu tiên
- `RAG_QUESTION` - Câu hỏi kiểm tra cho các mẫu RAG
- `AGENT_MODEL_PRIMARY` - Mô hình tác nhân chính
- `AGENT_MODEL_EDITOR` - Mô hình tác nhân chỉnh sửa
- `SLM_ALIAS` - Bí danh mô hình ngôn ngữ nhỏ
- `LLM_ALIAS` - Bí danh mô hình ngôn ngữ lớn

## Các thực hành tốt nhất của SDK đã được triển khai

### 1. Khởi tạo Client đúng cách
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

### 2. Truy xuất thông tin mô hình
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Xử lý lỗi
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logic thử lại với Backoff lũy thừa
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

### 5. Hỗ trợ Streaming
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

## Hướng dẫn di chuyển cho các mẫu tùy chỉnh

Nếu bạn đang tạo các mẫu mới hoặc cập nhật các mẫu hiện có:

1. **Sử dụng các trợ giúp từ `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Hỗ trợ ghi đè endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Thêm tài liệu toàn diện**:
   - Biến môi trường trong docstring
   - Liên kết tham chiếu SDK
   - Ví dụ sử dụng

4. **Sử dụng gợi ý kiểu**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Triển khai xử lý lỗi đúng cách**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Kiểm tra

Tất cả các mẫu có thể được kiểm tra với:

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

## Tham chiếu tài liệu SDK

- **Kho chính**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Tài liệu API**: Kiểm tra kho SDK để biết tài liệu API mới nhất

## Thay đổi lớn

### Không có dự kiến
Tất cả các thay đổi đều tương thích ngược. Các cập nhật chủ yếu:
- Thêm các tính năng tùy chọn mới (ghi đè endpoint)
- Cải thiện xử lý lỗi
- Tăng cường tài liệu
- Cập nhật tên mô hình mặc định theo khuyến nghị hiện tại

### Cải tiến tùy chọn
Bạn có thể muốn cập nhật mã của mình để sử dụng:
- `FOUNDRY_LOCAL_ENDPOINT` để kiểm soát endpoint rõ ràng
- `SHOW_USAGE=1` để hiển thị sử dụng token
- Cập nhật mô hình mặc định (`phi-4-mini` thay vì `phi-3.5-mini`)

## Các vấn đề thường gặp & giải pháp

### Vấn đề: "Khởi tạo Client thất bại"
**Giải pháp**: Đảm bảo dịch vụ Foundry Local đang chạy:
```bash
foundry service start
foundry model run phi-4-mini
```

### Vấn đề: "Không tìm thấy mô hình"
**Giải pháp**: Kiểm tra các mô hình có sẵn:
```bash
foundry model list
```

### Vấn đề: Lỗi kết nối endpoint
**Giải pháp**: Xác minh endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Các bước tiếp theo

1. **Cập nhật các mẫu Module08**: Áp dụng các mẫu tương tự cho Module08/samples
2. **Thêm kiểm tra tích hợp**: Tạo bộ kiểm tra toàn diện
3. **Đánh giá hiệu năng**: So sánh hiệu năng trước/sau
4. **Cập nhật tài liệu**: Cập nhật README chính với các mẫu mới

## Hướng dẫn đóng góp

Khi thêm các mẫu mới:
1. Sử dụng `workshop_utils.py` để đảm bảo tính nhất quán
2. Tuân theo mẫu trong các mẫu hiện có
3. Thêm docstring toàn diện
4. Bao gồm các liên kết tham chiếu SDK
5. Hỗ trợ ghi đè endpoint
6. Thêm gợi ý kiểu đúng cách
7. Bao gồm các ví dụ sử dụng trong docstring

## Tương thích phiên bản

Các cập nhật này tương thích với:
- `foundry-local-sdk` (mới nhất)
- `openai>=1.30.0`
- Python 3.8+

---

**Cập nhật lần cuối**: 08-01-2025  
**Người quản lý**: Đội ngũ EdgeAI Workshop  
**Phiên bản SDK**: Foundry Local SDK (mới nhất 0.7.117+67073234e7)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.