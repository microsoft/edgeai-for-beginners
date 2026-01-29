# Hướng Dẫn Tích Hợp Open WebUI + Foundry Local

Hướng dẫn này chỉ cách kết nối Open WebUI với Microsoft Foundry Local để tạo giao diện chuyên nghiệp giống ChatGPT, sử dụng các mô hình AI cục bộ của bạn.

## Tổng Quan

Open WebUI cung cấp giao diện chat hiện đại, thân thiện với người dùng, có thể kết nối với bất kỳ API tương thích OpenAI nào. Khi kết nối với Foundry Local, bạn sẽ có:

- **Giao diện chuyên nghiệp**: Giao diện giống ChatGPT với thiết kế hiện đại
- **Bảo mật cục bộ**: Tất cả xử lý diễn ra trên thiết bị của bạn
- **Chuyển đổi mô hình**: Dễ dàng chuyển đổi giữa các mô hình cục bộ khác nhau
- **Lịch sử hội thoại**: Lưu trữ lịch sử chat và ngữ cảnh
- **Tải lên tệp**: Phân tích tài liệu và xử lý tệp
- **Nhân vật tùy chỉnh**: Tùy chỉnh lời nhắc hệ thống và vai trò

## Yêu Cầu

### Phần Mềm Cần Thiết

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Tải Mô Hình

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Cài Đặt Nhanh (Khuyến Nghị)

### Bước 1: Chạy Open WebUI với Docker

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### Bước 2: Cài Đặt Ban Đầu

1. **Mở Trình Duyệt**: Truy cập `http://localhost:3000`
2. **Tạo Tài Khoản**: Thiết lập người dùng admin (người dùng đầu tiên sẽ trở thành admin)
3. **Xác Minh Kết Nối**: Các mô hình sẽ tự động xuất hiện trong danh sách thả xuống

### Bước 3: Kiểm Tra Kết Nối

1. Chọn mô hình từ danh sách thả xuống (ví dụ: "phi-4-mini")
2. Nhập tin nhắn thử nghiệm: "Xin chào! Bạn có thể giới thiệu về mình không?"
3. Bạn sẽ thấy phản hồi trực tuyến từ mô hình cục bộ của mình

## Cấu Hình Nâng Cao

### Biến Môi Trường

| Biến | Mục Đích | Mặc Định | Ví Dụ |
|------|----------|----------|-------|
| `OPENAI_API_BASE_URL` | Endpoint Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API key (yêu cầu nhưng không sử dụng cục bộ) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Khóa mã hóa phiên | tự động tạo | `your-secret-key` |
| `ENABLE_SIGNUP` | Cho phép đăng ký người dùng mới | `True` | `False` |

### Cấu Hình Thủ Công (Thay Thế)

Nếu biến môi trường không hoạt động, cấu hình thủ công:

1. **Mở Cài Đặt**: Nhấp vào biểu tượng bánh răng
2. **Đi Đến Kết Nối**: Cài đặt → Kết nối → OpenAI
3. **Thiết Lập Chi Tiết API**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (bất kỳ giá trị nào cũng được)
4. **Lưu và Kiểm Tra**: Nhấp "Lưu" rồi kiểm tra với một mô hình

### Lưu Trữ Dữ Liệu Bền Vững

Để lưu trữ hội thoại và cài đặt:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Xử Lý Sự Cố

### Vấn Đề Kết Nối

**Vấn Đề**: "Connection refused" hoặc không tải được mô hình

**Giải Pháp**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### Mô Hình Không Xuất Hiện

**Vấn Đề**: Open WebUI không hiển thị mô hình trong danh sách thả xuống

**Các Bước Gỡ Lỗi**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Khắc Phục**: Đảm bảo mô hình được tải đúng cách:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Vấn Đề Mạng Docker

**Vấn Đề**: `host.docker.internal` không hoạt động

**Giải Pháp Windows**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**Thay Thế**: Tìm IP của máy:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Vấn Đề Hiệu Suất

**Phản Hồi Chậm**:
1. Kiểm tra mô hình có sử dụng tăng tốc GPU: `foundry service ps`
2. Xác minh tài nguyên hệ thống đủ (RAM/bộ nhớ GPU)
3. Cân nhắc sử dụng mô hình nhỏ hơn để thử nghiệm

**Vấn Đề Bộ Nhớ**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Hướng Dẫn Sử Dụng

### Chat Cơ Bản

1. **Chọn Mô Hình**: Chọn từ danh sách thả xuống (hiển thị các mô hình Foundry Local)
2. **Nhập Tin Nhắn**: Sử dụng ô nhập văn bản ở dưới cùng
3. **Gửi**: Nhấn Enter hoặc nhấp nút Gửi
4. **Xem Phản Hồi**: Xem phản hồi trực tuyến theo thời gian thực

### Tính Năng Nâng Cao

**Tải Lên Tệp**:
1. Nhấp vào biểu tượng kẹp giấy
2. Tải lên tài liệu (PDF, TXT, v.v.)
3. Đặt câu hỏi về nội dung
4. Mô hình sẽ phân tích và phản hồi dựa trên tài liệu

**Lời Nhắc Hệ Thống Tùy Chỉnh**:
1. Cài đặt → Cá nhân hóa
2. Thiết lập lời nhắc hệ thống tùy chỉnh
3. Tạo tính cách/hành vi AI nhất quán

**Quản Lý Hội Thoại**:
- **Chat Mới**: Nhấp vào "+" để bắt đầu hội thoại mới
- **Lịch Sử Chat**: Truy cập các hội thoại trước từ thanh bên
- **Xuất**: Tải xuống lịch sử chat dưới dạng văn bản/JSON

**So Sánh Mô Hình**:
1. Mở nhiều tab trình duyệt đến cùng Open WebUI
2. Chọn các mô hình khác nhau trong mỗi tab
3. So sánh phản hồi với cùng lời nhắc

### Mẫu Tích Hợp

**Quy Trình Phát Triển**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Triển Khai Sản Xuất

### Cài Đặt Bảo Mật

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Cài Đặt Nhiều Người Dùng

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Giám Sát và Ghi Log

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Dọn Dẹp

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## Các Bước Tiếp Theo

### Ý Tưởng Nâng Cấp

1. **Mô Hình Tùy Chỉnh**: Thêm các mô hình được tinh chỉnh của bạn vào Foundry Local
2. **Tích Hợp API**: Kết nối với các API bên ngoài qua chức năng Open WebUI
3. **Xử Lý Tài Liệu**: Thiết lập các pipeline RAG nâng cao
4. **Đa Phương Thức**: Cấu hình mô hình thị giác để phân tích hình ảnh

### Cân Nhắc Về Quy Mô

- **Cân Bằng Tải**: Nhiều instance Foundry Local sau proxy ngược
- **Định Tuyến Mô Hình**: Các mô hình khác nhau cho các trường hợp sử dụng khác nhau
- **Quản Lý Tài Nguyên**: Tối ưu hóa bộ nhớ GPU cho người dùng đồng thời
- **Chiến Lược Sao Lưu**: Sao lưu thường xuyên dữ liệu hội thoại và cấu hình

## Tài Liệu Tham Khảo

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

