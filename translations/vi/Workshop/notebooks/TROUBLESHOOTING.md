# Sổ Tay Workshop - Hướng Dẫn Khắc Phục Sự Cố

## Mục Lục

- [Các Vấn Đề Chung và Giải Pháp](../../../../Workshop/notebooks)
- [Vấn Đề Cụ Thể của Buổi 04](../../../../Workshop/notebooks)
- [Vấn Đề Cụ Thể của Buổi 05](../../../../Workshop/notebooks)
- [Vấn Đề Cụ Thể của Buổi 06](../../../../Workshop/notebooks)
- [Vấn Đề Liên Quan Đến Phần Cứng](../../../../Workshop/notebooks)
- [Lệnh Chẩn Đoán](../../../../Workshop/notebooks)
- [Nhận Hỗ Trợ](../../../../Workshop/notebooks)

---

## Các Vấn Đề Chung và Giải Pháp

### 🔴 CUDA Out of Memory

**Thông Báo Lỗi:**
```
CUDA failure 2: out of memory
```

**Nguyên Nhân:** GPU không có đủ VRAM để tải mô hình.

**Giải Pháp:**

#### Lựa Chọn 1: Sử Dụng Biến Thể CPU (Khuyến Nghị)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Lựa Chọn 2: Sử Dụng Mô Hình Nhỏ Hơn trên GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Lựa Chọn 3: Xóa Bộ Nhớ GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Lựa Chọn 4: Tăng Bộ Nhớ GPU (nếu có thể)
- Đóng các tab trình duyệt, trình chỉnh sửa video, hoặc ứng dụng sử dụng GPU khác
- Giảm hiệu ứng hình ảnh của Windows
- Sử dụng GPU chuyên dụng nếu bạn có cả GPU tích hợp và chuyên dụng

---

### 🔴 APIConnectionError: Connection Error

**Thông Báo Lỗi:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Nguyên Nhân:** Dịch vụ Foundry Local không chạy hoặc không thể truy cập.

**Giải Pháp:**

#### Bước 1: Kiểm Tra Trạng Thái Dịch Vụ
```bash
foundry service status
```

#### Bước 2: Khởi Động Dịch Vụ Nếu Đã Dừng
```bash
foundry service start
```

#### Bước 3: Xác Minh Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Bước 4: Tải Các Mô Hình Cần Thiết
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Bước 5: Khởi Động Lại Kernel của Notebook
Sau khi khởi động dịch vụ và tải mô hình, khởi động lại kernel của notebook và chạy lại tất cả các ô.

---

### 🔴 Model Not Found in Catalog

**Thông Báo Lỗi:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Nguyên Nhân:** Mô hình chưa được tải xuống hoặc chưa được tải vào Foundry Local.

**Giải Pháp:**

#### Lựa Chọn 1: Tải Xuống và Tải Mô Hình
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Lựa Chọn 2: Sử Dụng Chế Độ Tự Động Chọn
Cập nhật CATALOG để sử dụng tên mô hình cơ bản (không có hậu tố `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK sẽ tự động chọn biến thể tốt nhất (CPU, GPU, hoặc NPU) cho phần cứng của bạn.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Thông Báo Lỗi:**
```
HttpResponseError: 500 - Failed loading model
```

**Nguyên Nhân:** Tệp mô hình bị hỏng hoặc không tương thích với phần cứng.

**Giải Pháp:**

#### Tải Lại Mô Hình
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Sử Dụng Biến Thể Khác
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Thông Báo Lỗi:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Nguyên Nhân:** Gói foundry-local-sdk chưa được cài đặt.

**Giải Pháp:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Yêu Cầu Đầu Tiên Chậm

**Triệu Chứng:** Lần hoàn thành đầu tiên mất hơn 30 giây, các yêu cầu sau đó nhanh hơn.

**Nguyên Nhân:** Đây là hành vi bình thường - dịch vụ đang tải mô hình vào bộ nhớ trong lần yêu cầu đầu tiên.

**Giải Pháp:**

#### Tải Trước Mô Hình
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Giữ Dịch Vụ Chạy
```bash
# Start service manually and leave it running
foundry service start
```

---

## Vấn Đề Cụ Thể của Buổi 04

### Cấu Hình Cổng Sai

**Vấn Đề:** Notebook kết nối với cổng sai (55769 vs 59959 vs 57127)

**Giải Pháp:**

1. Kiểm tra cổng mà Foundry Local đang sử dụng:
```bash
foundry service status
# Note the port number displayed
```

2. Cập nhật Ô 10 trong notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Khởi động lại kernel và chạy lại các ô 6, 8, 10, 12, 16, 20, 22

---

### Chọn Sai Mô Hình

**Vấn Đề:** Notebook hiển thị gpt-oss-20b hoặc qwen2.5-7b thay vì qwen2.5-3b

**Giải Pháp:**

1. Khởi động lại kernel của notebook (xóa trạng thái biến cũ)
2. Chạy lại Ô 10 (Đặt Bí Danh Mô Hình)
3. Chạy lại Ô 12 (Hiển Thị Cấu Hình)
4. **Xác Minh:** Ô 12 phải hiển thị `LLM Model: qwen2.5-3b`

---

### Ô Chẩn Đoán Không Hoạt Động

**Vấn Đề:** Ô 16 hiển thị "❌ Foundry Local service not found!"

**Giải Pháp:**

1. Xác minh dịch vụ đang chạy:
```bash
foundry service status
```

2. Kiểm tra endpoint thủ công:
```bash
curl http://localhost:59959/v1/models
```

3. Nếu curl hoạt động nhưng notebook không:
   - Khởi động lại kernel của notebook
   - Chạy lại các ô theo thứ tự: 6, 8, 10, 12, 14, 16

4. Nếu curl không hoạt động:
   - Khởi động dịch vụ: `foundry service start`
   - Tải mô hình: `foundry model run phi-4-mini` và `foundry model run qwen2.5-3b`

---

### Kiểm Tra Trước Khi Chạy Không Thành Công

**Vấn Đề:** Ô 20 hiển thị lỗi kết nối mặc dù chẩn đoán đã thành công

**Giải Pháp:**

1. Kiểm tra các mô hình đã được tải:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Nếu thiếu mô hình:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Chạy lại Ô 20 sau khi các mô hình đã được tải

---

### So Sánh Thất Bại với Giá Trị None

**Vấn Đề:** Ô 22 hoàn thành nhưng hiển thị độ trễ là None

**Giải Pháp:**

1. Kiểm tra rằng kiểm tra trước đã thành công (Ô 20)
2. Chạy lại Ô 22 - các mô hình có thể cần khởi động trong lần yêu cầu đầu tiên
3. Xác minh cả hai mô hình đã được tải: `foundry model ls`

---

## Vấn Đề Cụ Thể của Buổi 05

### Agent Sử Dụng Sai Mô Hình

**Vấn Đề:** Agent không sử dụng mô hình mong đợi

**Giải Pháp:**

Xác minh cấu hình:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Khởi động lại kernel nếu mô hình không chính xác.

---

### Tràn Bộ Nhớ Ngữ Cảnh

**Vấn Đề:** Phản hồi của agent giảm chất lượng theo thời gian

**Giải Pháp:** Đã được xử lý tự động - các agent chỉ giữ lại 6 tin nhắn cuối trong bộ nhớ.

---

## Vấn Đề Cụ Thể của Buổi 06

### Nhầm Lẫn Giữa Mô Hình CPU và GPU

**Vấn Đề:** Gặp lỗi CUDA khi sử dụng cấu hình mặc định

**Giải Pháp:** Cấu hình mặc định hiện sử dụng mô hình CPU. Nếu bạn gặp lỗi CUDA:

1. Xác minh bạn đang sử dụng catalog CPU mặc định:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Khởi động lại kernel và chạy lại tất cả các ô

---

### Phát Hiện Ý Định Không Hoạt Động

**Vấn Đề:** Các prompt được chuyển hướng đến mô hình sai

**Giải Pháp:**

Kiểm tra phát hiện ý định:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Cập nhật RULES nếu cần điều chỉnh mẫu.

---

## Vấn Đề Liên Quan Đến Phần Cứng

### GPU NVIDIA

**Kiểm Tra Trạng Thái GPU:**
```bash
nvidia-smi
```

**Các Vấn Đề Thường Gặp:**
- **Driver lỗi thời**: Cập nhật driver NVIDIA
- **Không khớp phiên bản CUDA**: Cài đặt lại Foundry Local
- **Bộ nhớ GPU bị phân mảnh**: Khởi động lại hệ thống

### Qualcomm NPU

**Kiểm Tra Trạng Thái NPU:**
```bash
foundry device info
```

**Các Vấn Đề Thường Gặp:**
- **Driver NPU chưa được cài đặt**: Cài đặt driver Qualcomm NPU
- **Không có biến thể NPU**: Sử dụng biến thể CPU
- **Phiên bản Windows quá cũ**: Cập nhật lên Windows 11 mới nhất

### Hệ Thống Chỉ Dùng CPU

**Mô Hình Khuyến Nghị:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Mẹo Tăng Hiệu Suất:**
- Sử dụng mô hình nhỏ nhất
- Giảm max_tokens
- Kiên nhẫn với yêu cầu đầu tiên

---

## Lệnh Chẩn Đoán

### Kiểm Tra Tất Cả
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### Trong Python
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## Nhận Hỗ Trợ

### 1. Kiểm Tra Nhật Ký
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. Vấn Đề trên GitHub
- Tìm kiếm các vấn đề hiện có: https://github.com/microsoft/Foundry-Local/issues
- Tạo vấn đề mới với:
  - Thông báo lỗi (toàn bộ nội dung)
  - Kết quả của `foundry service status`
  - Kết quả của `foundry --version`
  - Thông tin GPU/NPU (nvidia-smi, v.v.)
  - Các bước để tái hiện vấn đề

### 3. Tài Liệu
- **Kho Chính:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Tham Khảo CLI:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Khắc Phục Sự Cố:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Danh Sách Kiểm Tra Sửa Lỗi Nhanh

Khi gặp sự cố, hãy thử các bước sau theo thứ tự:

- [ ] Kiểm tra dịch vụ đang chạy: `foundry service status`
- [ ] Khởi động lại dịch vụ: `foundry service stop && foundry service start`
- [ ] Xác minh mô hình tồn tại: `foundry model ls | grep phi-4-mini`
- [ ] Tải các mô hình cần thiết: `foundry model run phi-4-mini`
- [ ] Kiểm tra bộ nhớ GPU: `nvidia-smi` (nếu dùng NVIDIA)
- [ ] Thử biến thể CPU: Sử dụng `phi-4-mini-cpu` thay vì `phi-4-mini`
- [ ] Khởi động lại kernel của notebook
- [ ] Xóa đầu ra của notebook và chạy lại tất cả các ô
- [ ] Cài đặt lại SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Khởi động lại hệ thống (biện pháp cuối cùng)

---

## Mẹo Phòng Ngừa

### Thực Hành Tốt Nhất

1. **Luôn kiểm tra dịch vụ trước:**
   ```bash
   foundry service status
   ```

2. **Sử dụng biến thể CPU theo mặc định:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Tải trước mô hình trước khi chạy notebook:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Giữ dịch vụ chạy:**
   - Không dừng/khởi động lại dịch vụ không cần thiết
   - Để dịch vụ chạy nền giữa các buổi làm việc

5. **Giám sát tài nguyên:**
   - Kiểm tra bộ nhớ GPU trước khi chạy
   - Đóng các ứng dụng GPU không cần thiết
   - Sử dụng Task Manager / nvidia-smi

6. **Cập nhật thường xuyên:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Cập Nhật Lần Cuối:** Ngày 8 tháng 10 năm 2025

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.