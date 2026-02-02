# Foundry Local như API Mẫu

Mẫu này minh họa cách sử dụng Microsoft Foundry Local như một dịch vụ REST API mà không cần dựa vào OpenAI SDK. Nó trình bày các mẫu tích hợp HTTP trực tiếp để tối ưu hóa kiểm soát và tùy chỉnh.

## Tổng quan

Dựa trên các mẫu chính thức của Microsoft Foundry Local, mẫu này cung cấp:
- Tích hợp REST API trực tiếp với FoundryLocalManager
- Triển khai khách HTTP tùy chỉnh
- Quản lý mô hình và giám sát sức khỏe
- Xử lý phản hồi dạng streaming và không streaming
- Xử lý lỗi và logic thử lại sẵn sàng cho sản xuất

## Yêu cầu trước

1. **Cài đặt Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Phụ thuộc Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Kiến trúc

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Các tính năng chính

### 1. **Tích hợp HTTP trực tiếp**
- Gọi REST API thuần túy mà không phụ thuộc vào SDK
- Xác thực và tiêu đề tùy chỉnh
- Kiểm soát hoàn toàn việc xử lý yêu cầu/phản hồi

### 2. **Quản lý mô hình**
- Tải và gỡ tải mô hình động
- Giám sát sức khỏe và kiểm tra trạng thái
- Thu thập số liệu hiệu suất

### 3. **Mẫu sản xuất**
- Cơ chế thử lại với backoff lũy thừa
- Circuit breaker để chịu lỗi
- Ghi nhật ký và giám sát toàn diện

### 4. **Xử lý phản hồi linh hoạt**
- Phản hồi dạng streaming cho các ứng dụng thời gian thực
- Xử lý theo lô cho các kịch bản thông lượng cao
- Phân tích và xác thực phản hồi tùy chỉnh

## Ví dụ sử dụng

### Tích hợp API cơ bản
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Tích hợp dạng streaming
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Giám sát sức khỏe
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Cấu trúc tệp

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Tích hợp Microsoft Foundry Local

Mẫu này tuân theo các mẫu chính thức của Microsoft:

1. **Tích hợp SDK**: Sử dụng `FoundryLocalManager` để quản lý dịch vụ
2. **Điểm cuối REST**: Gọi trực tiếp đến `/v1/chat/completions` và các điểm cuối khác
3. **Xác thực**: Xử lý khóa API đúng cách cho các dịch vụ cục bộ
4. **Quản lý mô hình**: Liệt kê danh mục, tải xuống và tải mô hình
5. **Xử lý lỗi**: Mã lỗi và phản hồi được Microsoft khuyến nghị

## Bắt đầu

1. **Cài đặt phụ thuộc**
   ```bash
   pip install -r requirements.txt
   ```

2. **Chạy ví dụ cơ bản**
   ```bash
   python examples/basic_usage.py
   ```

3. **Thử dạng streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Thiết lập sản xuất**
   ```bash
   python examples/production.py
   ```

## Cấu hình

Các biến môi trường để tùy chỉnh:
- `FOUNDRY_MODEL`: Mô hình mặc định sử dụng (mặc định: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Thời gian chờ yêu cầu tính bằng giây (mặc định: 30)
- `FOUNDRY_RETRIES`: Số lần thử lại (mặc định: 3)
- `FOUNDRY_LOG_LEVEL`: Mức độ ghi nhật ký (mặc định: "INFO")

## Thực hành tốt nhất

1. **Quản lý kết nối**: Tái sử dụng kết nối HTTP để cải thiện hiệu suất
2. **Xử lý lỗi**: Triển khai logic thử lại đúng cách với backoff lũy thừa
3. **Giám sát tài nguyên**: Theo dõi việc sử dụng bộ nhớ mô hình và hiệu suất
4. **Bảo mật**: Sử dụng xác thực đúng cách ngay cả với các dịch vụ cục bộ
5. **Kiểm thử**: Bao gồm cả kiểm thử đơn vị và kiểm thử tích hợp

## Khắc phục sự cố

### Các vấn đề thường gặp

**Dịch vụ không chạy**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Vấn đề tải mô hình**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Lỗi kết nối**
- Xác minh Foundry Local đang chạy trên cổng đúng
- Kiểm tra cài đặt tường lửa
- Đảm bảo tiêu đề xác thực đúng cách

## Tối ưu hóa hiệu suất

1. **Kết nối nhóm**: Sử dụng đối tượng session cho nhiều yêu cầu
2. **Hoạt động bất đồng bộ**: Tận dụng asyncio cho các yêu cầu đồng thời
3. **Bộ nhớ đệm**: Bộ nhớ đệm phản hồi mô hình khi thích hợp
4. **Giám sát**: Theo dõi thời gian phản hồi và điều chỉnh thời gian chờ

## Kết quả học tập

Sau khi hoàn thành mẫu này, bạn sẽ hiểu:
- Tích hợp REST API trực tiếp với Foundry Local
- Các mẫu triển khai khách HTTP tùy chỉnh
- Xử lý lỗi và giám sát sẵn sàng cho sản xuất
- Kiến trúc dịch vụ Microsoft Foundry Local
- Kỹ thuật tối ưu hóa hiệu suất cho các dịch vụ AI cục bộ

## Bước tiếp theo

- Khám phá Mẫu 08: Ứng dụng Chat Windows 11
- Thử Mẫu 09: Điều phối Đa-Agent
- Tìm hiểu Mẫu 10: Tích hợp Foundry Local như Công cụ

---

