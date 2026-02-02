# Mẫu 01: Trò chuyện nhanh qua OpenAI SDK

Một ví dụ đơn giản về trò chuyện, minh họa cách sử dụng OpenAI SDK với Microsoft Foundry Local để suy luận AI cục bộ.

## Tổng quan

Mẫu này hướng dẫn cách:
- Sử dụng OpenAI Python SDK với Foundry Local
- Xử lý cả cấu hình Azure OpenAI và Foundry cục bộ
- Triển khai xử lý lỗi đúng cách và chiến lược dự phòng
- Sử dụng FoundryLocalManager để quản lý dịch vụ

## Yêu cầu

- **Foundry Local**: Đã cài đặt và có sẵn trong PATH
- **Python**: Phiên bản 3.8 hoặc mới hơn
- **Mô hình**: Một mô hình đã được tải trong Foundry Local (ví dụ: `phi-4-mini`)

## Cài đặt

1. **Thiết lập môi trường Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Cài đặt các thư viện phụ thuộc:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Khởi động dịch vụ Foundry Local và tải mô hình:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Sử dụng

### Foundry Local (Mặc định)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```

## Tính năng của mã

### Tích hợp FoundryLocalManager

Mẫu sử dụng SDK chính thức của Foundry Local để quản lý dịch vụ đúng cách:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```

### Xử lý lỗi

Xử lý lỗi mạnh mẽ với dự phòng cấu hình thủ công:
- Tự động phát hiện dịch vụ
- Giảm thiểu lỗi một cách linh hoạt nếu SDK không khả dụng
- Thông báo lỗi rõ ràng để hỗ trợ khắc phục sự cố

## Biến môi trường

| Biến | Mô tả | Mặc định | Bắt buộc |
|------|-------|----------|----------|
| `MODEL` | Bí danh hoặc tên mô hình | `phi-4-mini` | Không |
| `BASE_URL` | URL cơ sở của Foundry Local | `http://localhost:8000` | Không |
| `API_KEY` | API key (thường không cần cho cục bộ) | `""` | Không |
| `AZURE_OPENAI_ENDPOINT` | Endpoint của Azure OpenAI | - | Đối với Azure |
| `AZURE_OPENAI_API_KEY` | API key của Azure OpenAI | - | Đối với Azure |
| `AZURE_OPENAI_API_VERSION` | Phiên bản API của Azure | `2024-08-01-preview` | Không |

## Khắc phục sự cố

### Các vấn đề thường gặp

1. **Cảnh báo "Không thể sử dụng Foundry SDK":**
   - Cài đặt foundry-local-sdk: `pip install foundry-local-sdk`
   - Hoặc thiết lập các biến môi trường để cấu hình thủ công

2. **Kết nối bị từ chối:**
   - Đảm bảo Foundry Local đang chạy: `foundry service status`
   - Kiểm tra xem mô hình đã được tải chưa: `foundry service ps`

3. **Không tìm thấy mô hình:**
   - Liệt kê các mô hình có sẵn: `foundry model list`
   - Tải một mô hình: `foundry model run phi-4-mini`

### Xác minh

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Tài liệu tham khảo

- [Tài liệu Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Tài liệu API tương thích OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

