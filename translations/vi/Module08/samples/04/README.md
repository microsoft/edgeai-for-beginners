# Mẫu 04: Ứng dụng Chat Sản xuất với Chainlit

Một mẫu toàn diện trình bày nhiều cách tiếp cận để xây dựng các ứng dụng chat sẵn sàng cho sản xuất sử dụng Microsoft Foundry Local, với giao diện web hiện đại, phản hồi theo luồng và các công nghệ trình duyệt tiên tiến.

## Những gì được bao gồm

- **🚀 Ứng dụng Chat Chainlit** (`app.py`): Ứng dụng chat sẵn sàng sản xuất với phản hồi theo luồng
- **🌐 Demo WebGPU** (`webgpu-demo/`): Suy luận AI trên trình duyệt với tăng tốc phần cứng
- **🎨 Tích hợp Open WebUI** (`open-webui-guide.md`): Giao diện chuyên nghiệp giống ChatGPT
- **📚 Notebook giáo dục** (`chainlit_app.ipynb`): Tài liệu học tập tương tác

## Bắt đầu nhanh

### 1. Ứng dụng Chat Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Mở tại: `http://localhost:8080`

### 2. Demo WebGPU trên trình duyệt

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Mở tại: `http://localhost:5173`

### 3. Cài đặt Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Mở tại: `http://localhost:3000`

## Mẫu kiến trúc

### Ma trận quyết định Local vs Cloud

| Tình huống | Khuyến nghị | Lý do |
|------------|-------------|-------|
| **Dữ liệu nhạy cảm về quyền riêng tư** | 🏠 Local (Foundry) | Dữ liệu không rời khỏi thiết bị |
| **Lý luận phức tạp** | ☁️ Cloud (Azure OpenAI) | Truy cập vào các mô hình lớn hơn |
| **Chat thời gian thực** | 🏠 Local (Foundry) | Độ trễ thấp, phản hồi nhanh hơn |
| **Phân tích tài liệu** | 🔄 Kết hợp | Local để trích xuất, cloud để phân tích |
| **Tạo mã** | 🏠 Local (Foundry) | Quyền riêng tư + mô hình chuyên biệt |
| **Nhiệm vụ nghiên cứu** | ☁️ Cloud (Azure OpenAI) | Cần cơ sở kiến thức rộng |

### So sánh công nghệ

| Công nghệ | Trường hợp sử dụng | Ưu điểm | Nhược điểm |
|-----------|--------------------|---------|------------|
| **Chainlit** | Nhà phát triển Python, tạo mẫu nhanh | Dễ thiết lập, hỗ trợ theo luồng | Chỉ hỗ trợ Python |
| **WebGPU** | Quyền riêng tư tối đa, kịch bản offline | Tích hợp trình duyệt, không cần máy chủ | Kích thước mô hình hạn chế |
| **Open WebUI** | Triển khai sản xuất, nhóm làm việc | Giao diện chuyên nghiệp, quản lý người dùng | Yêu cầu Docker |

## Yêu cầu

- **Foundry Local**: Đã cài đặt và chạy ([Tải xuống](https://aka.ms/foundry-local-installer))
- **Python**: Phiên bản 3.10+ với môi trường ảo
- **Mô hình**: Ít nhất một mô hình đã tải (`foundry model run phi-4-mini`)
- **Trình duyệt**: Chrome/Edge hỗ trợ WebGPU cho các demo
- **Docker**: Dành cho Open WebUI (tùy chọn)

## Cài đặt & Thiết lập

### 1. Thiết lập môi trường Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Thiết lập Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Ứng dụng mẫu

### Ứng dụng Chat Chainlit

**Tính năng:**
- 🚀 **Phản hồi theo luồng thời gian thực**: Các token xuất hiện khi được tạo
- 🛡️ **Xử lý lỗi mạnh mẽ**: Giảm thiểu và phục hồi một cách linh hoạt
- 🎨 **Giao diện hiện đại**: Giao diện chat chuyên nghiệp có sẵn
- 🔧 **Cấu hình linh hoạt**: Biến môi trường và tự động phát hiện
- 📱 **Thiết kế đáp ứng**: Hoạt động trên cả máy tính và thiết bị di động

**Bắt đầu nhanh:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### Demo WebGPU trên trình duyệt

**Tính năng:**
- 🌐 **AI tích hợp trình duyệt**: Không cần máy chủ, chạy hoàn toàn trên trình duyệt
- ⚡ **Tăng tốc WebGPU**: Tăng tốc phần cứng khi khả dụng
- 🔒 **Quyền riêng tư tối đa**: Dữ liệu không bao giờ rời khỏi thiết bị của bạn
- 🎯 **Không cần cài đặt**: Hoạt động trên bất kỳ trình duyệt tương thích nào
- 🔄 **Giảm thiểu linh hoạt**: Tự động chuyển sang CPU nếu WebGPU không khả dụng

**Chạy:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Tích hợp Open WebUI

**Tính năng:**
- 🎨 **Giao diện giống ChatGPT**: Chuyên nghiệp, giao diện quen thuộc
- 👥 **Hỗ trợ nhiều người dùng**: Tài khoản người dùng và lịch sử hội thoại
- 📁 **Xử lý tệp**: Tải lên và phân tích tài liệu
- 🔄 **Chuyển đổi mô hình**: Dễ dàng chuyển đổi giữa các mô hình khác nhau
- 🐳 **Triển khai Docker**: Thiết lập container sẵn sàng sản xuất

**Thiết lập nhanh:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Tham chiếu cấu hình

### Biến môi trường

| Biến | Mô tả | Mặc định | Ví dụ |
|------|-------|----------|-------|
| `MODEL` | Bí danh mô hình sử dụng | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Điểm cuối Foundry Local | Tự động phát hiện | `http://localhost:51211` |
| `API_KEY` | Khóa API (tùy chọn cho local) | `""` | `your-api-key` |

## Xử lý sự cố

### Các vấn đề thường gặp

**Ứng dụng Chainlit:**

1. **Dịch vụ không khả dụng:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Xung đột cổng:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Vấn đề môi trường Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Demo WebGPU:**

1. **WebGPU không được hỗ trợ:**
   - Cập nhật Chrome/Edge lên phiên bản 113+
   - Bật WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Kiểm tra trạng thái GPU: `chrome://gpu`
   - Demo sẽ tự động chuyển sang CPU

2. **Lỗi tải mô hình:**
   - Đảm bảo kết nối internet để tải mô hình
   - Kiểm tra console trình duyệt để tìm lỗi CORS
   - Xác minh bạn đang phục vụ qua HTTP (không phải file://)

**Open WebUI:**

1. **Kết nối bị từ chối:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Mô hình không xuất hiện:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Danh sách kiểm tra xác thực

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Sử dụng nâng cao

### Tối ưu hóa hiệu suất

**Chainlit:**
- Sử dụng phản hồi theo luồng để cải thiện hiệu suất cảm nhận
- Triển khai kết nối pooling để xử lý đồng thời cao
- Bộ nhớ đệm phản hồi mô hình cho các truy vấn lặp lại
- Giám sát sử dụng bộ nhớ với lịch sử hội thoại lớn

**WebGPU:**
- Sử dụng WebGPU để đạt quyền riêng tư và tốc độ tối đa
- Triển khai lượng hóa mô hình để giảm kích thước mô hình
- Sử dụng Web Workers để xử lý nền
- Bộ nhớ đệm mô hình đã biên dịch trong lưu trữ trình duyệt

**Open WebUI:**
- Sử dụng các volume persistent để lưu lịch sử hội thoại
- Cấu hình giới hạn tài nguyên cho container Docker
- Triển khai chiến lược sao lưu cho dữ liệu người dùng
- Thiết lập proxy ngược để kết thúc SSL

### Mẫu tích hợp

**Kết hợp Local/Cloud:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Pipeline đa phương thức:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Triển khai sản xuất

### Cân nhắc về bảo mật

- **Khóa API**: Sử dụng biến môi trường, không bao giờ mã hóa cứng
- **Mạng**: Sử dụng HTTPS trong sản xuất, cân nhắc VPN cho truy cập nhóm
- **Kiểm soát truy cập**: Triển khai xác thực cho Open WebUI
- **Quyền riêng tư dữ liệu**: Kiểm tra dữ liệu nào ở lại local và dữ liệu nào lên cloud
- **Cập nhật**: Giữ Foundry Local và các container được cập nhật

### Giám sát và bảo trì

- **Kiểm tra sức khỏe**: Triển khai giám sát điểm cuối
- **Ghi nhật ký**: Tập trung nhật ký từ tất cả các thành phần
- **Số liệu**: Theo dõi thời gian phản hồi, tỷ lệ lỗi, sử dụng tài nguyên
- **Sao lưu**: Sao lưu thường xuyên dữ liệu hội thoại và cấu hình

## Tài liệu tham khảo và tài nguyên

### Tài liệu

- [Tài liệu Chainlit](https://docs.chainlit.io/) - Hướng dẫn đầy đủ về framework
- [Tài liệu Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Tài liệu chính thức của Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Tích hợp WebGPU
- [Tài liệu Open WebUI](https://docs.openwebui.com/) - Cấu hình nâng cao

### Tệp mẫu

- [`app.py`](../../../../../Module08/samples/04/app.py) - Ứng dụng Chainlit sản xuất
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Notebook giáo dục
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Suy luận AI trên trình duyệt
- [`open-webui-guide.md`](./open-webui-guide.md) - Hướng dẫn thiết lập Open WebUI hoàn chỉnh

### Mẫu liên quan

- [Tài liệu Phiên 4](../../04.CuttingEdgeModels.md) - Hướng dẫn phiên đầy đủ
- [Mẫu Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Mẫu chính thức

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.