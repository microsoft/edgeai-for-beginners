# Mẫu 02: Tích hợp OpenAI SDK

Trình bày tích hợp nâng cao với OpenAI Python SDK, hỗ trợ cả Microsoft Foundry Local và Azure OpenAI với phản hồi dạng streaming và xử lý lỗi đúng cách.

## Tổng quan

Mẫu này giới thiệu:
- Chuyển đổi linh hoạt giữa Foundry Local và Azure OpenAI
- Phản hồi dạng streaming để cải thiện trải nghiệm người dùng
- Sử dụng đúng FoundryLocalManager SDK
- Cơ chế xử lý lỗi và dự phòng mạnh mẽ
- Các mẫu mã sẵn sàng cho sản xuất

## Yêu cầu

- **Foundry Local**: Đã cài đặt và chạy (cho suy luận cục bộ)
- **Python**: Phiên bản 3.8 hoặc mới hơn với OpenAI SDK
- **Azure OpenAI**: Endpoint hợp lệ và API key (cho suy luận trên đám mây)

## Cài đặt

1. **Thiết lập môi trường Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Cài đặt các phụ thuộc:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Khởi động Foundry Local (cho chế độ cục bộ):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Các kịch bản sử dụng

### Foundry Local (Mặc định)

**Tùy chọn 1: Sử dụng FoundryLocalManager (Khuyến nghị)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Tùy chọn 2: Cấu hình thủ công**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## Kiến trúc mã

### Mẫu Factory Client

Mẫu này sử dụng mẫu factory để tạo các client phù hợp:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### Phản hồi dạng streaming

Mẫu này trình bày cách sử dụng streaming để tạo phản hồi theo thời gian thực:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## Biến môi trường

### Cấu hình Foundry Local

| Biến       | Mô tả                        | Mặc định         | Bắt buộc |
|------------|------------------------------|------------------|----------|
| `MODEL`    | Bí danh mô hình sử dụng      | `phi-4-mini`     | Không    |
| `BASE_URL` | Endpoint Foundry Local       | `http://localhost:8000` | Không |
| `API_KEY`  | API key (tùy chọn cho cục bộ)| `""`             | Không    |

### Cấu hình Azure OpenAI

| Biến                     | Mô tả                          | Mặc định               | Bắt buộc |
|--------------------------|--------------------------------|------------------------|----------|
| `AZURE_OPENAI_ENDPOINT`  | Endpoint tài nguyên Azure OpenAI | -                    | Có       |
| `AZURE_OPENAI_API_KEY`   | API key Azure OpenAI          | -                      | Có       |
| `AZURE_OPENAI_API_VERSION` | Phiên bản API               | `2024-08-01-preview`   | Không    |
| `MODEL`                  | Tên triển khai Azure          | `your-deployment-name` | Có       |

## Tính năng nâng cao

### Tự động phát hiện dịch vụ

Mẫu này tự động phát hiện dịch vụ phù hợp dựa trên các biến môi trường:

1. **Chế độ Azure**: Nếu `AZURE_OPENAI_ENDPOINT` và `AZURE_OPENAI_API_KEY` được thiết lập
2. **Chế độ Foundry SDK**: Nếu Foundry Local SDK khả dụng
3. **Chế độ thủ công**: Dự phòng cho cấu hình thủ công

### Xử lý lỗi

- Dự phòng linh hoạt từ SDK sang cấu hình thủ công
- Thông báo lỗi rõ ràng để khắc phục sự cố
- Xử lý ngoại lệ đúng cách cho các vấn đề mạng
- Xác thực các biến môi trường bắt buộc

## Cân nhắc về hiệu suất

### So sánh giữa cục bộ và đám mây

**Ưu điểm của Foundry Local:**
- ✅ Không tốn chi phí API
- ✅ Bảo mật dữ liệu (dữ liệu không rời khỏi thiết bị)
- ✅ Độ trễ thấp cho các mô hình được hỗ trợ
- ✅ Hoạt động ngoại tuyến

**Ưu điểm của Azure OpenAI:**
- ✅ Truy cập các mô hình lớn mới nhất
- ✅ Hiệu suất cao hơn
- ✅ Không yêu cầu tài nguyên tính toán cục bộ
- ✅ SLA cấp doanh nghiệp

## Khắc phục sự cố

### Các vấn đề thường gặp

1. **Cảnh báo "Không thể sử dụng Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Lỗi xác thực Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Mô hình không khả dụng:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Kiểm tra sức khỏe

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Bước tiếp theo

- **Mẫu 03**: Khám phá và đánh giá mô hình
- **Mẫu 04**: Xây dựng ứng dụng Chainlit RAG
- **Mẫu 05**: Điều phối đa tác nhân
- **Mẫu 06**: Định tuyến mô hình như công cụ

## Tài liệu tham khảo

- [Tài liệu Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Tài liệu tham khảo Foundry Local SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Tài liệu OpenAI Python SDK](https://github.com/openai/openai-python)
- [Hướng dẫn phản hồi dạng streaming](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

