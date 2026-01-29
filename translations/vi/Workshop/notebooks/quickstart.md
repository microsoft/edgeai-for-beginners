# Sổ Tay Workshop - Hướng Dẫn Nhanh

## Mục Lục

- [Yêu Cầu Trước](../../../../Workshop/notebooks)
- [Cài Đặt Ban Đầu](../../../../Workshop/notebooks)
- [Phiên 04: So Sánh Mô Hình](../../../../Workshop/notebooks)
- [Phiên 05: Điều Phối Đa Tác Nhân](../../../../Workshop/notebooks)
- [Phiên 06: Định Tuyến Mô Hình Dựa Trên Ý Định](../../../../Workshop/notebooks)
- [Biến Môi Trường](../../../../Workshop/notebooks)
- [Lệnh Thông Dụng](../../../../Workshop/notebooks)

---

## Yêu Cầu Trước

### 1. Cài Đặt Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Xác Minh Cài Đặt:**
```bash
foundry --version
```

### 2. Cài Đặt Các Thư Viện Python

```bash
cd Workshop
pip install -r requirements.txt
```

Hoặc cài đặt từng thư viện riêng lẻ:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Cài Đặt Ban Đầu

### Khởi Động Dịch Vụ Foundry Local

**Bắt buộc trước khi chạy bất kỳ sổ tay nào:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Kết quả mong đợi:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Tải Xuống và Nạp Mô Hình

Các sổ tay sử dụng các mô hình sau theo mặc định:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Xác Minh Cài Đặt

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Phiên 04: So Sánh Mô Hình

### Mục Đích
So sánh hiệu suất giữa Mô Hình Ngôn Ngữ Nhỏ (SLM) và Mô Hình Ngôn Ngữ Lớn (LLM).

### Cài Đặt Nhanh

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Chạy Sổ Tay

1. **Mở** `session04_model_compare.ipynb` trong VS Code hoặc Jupyter
2. **Khởi động lại kernel** (Kernel → Restart Kernel)
3. **Chạy tất cả các ô lệnh** theo thứ tự

### Cấu Hình Chính

**Mô Hình Mặc Định:**
- **SLM:** `phi-4-mini` (~4GB RAM, nhanh hơn)
- **LLM:** `qwen2.5-3b` (~3GB RAM, tối ưu bộ nhớ)

**Biến Môi Trường (tùy chọn):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Kết Quả Mong Đợi

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Tùy Chỉnh

**Sử dụng mô hình khác:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Tùy chỉnh prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Danh Sách Kiểm Tra Xác Minh

- [ ] Ô 12 hiển thị đúng mô hình (phi-4-mini, qwen2.5-3b)
- [ ] Ô 12 hiển thị đúng endpoint (cổng 59959)
- [ ] Ô 16 kiểm tra chẩn đoán thành công (✅ Dịch vụ đang chạy)
- [ ] Ô 20 kiểm tra trước khi chạy thành công (cả hai mô hình đều ổn)
- [ ] Ô 22 so sánh hoàn tất với các giá trị độ trễ
- [ ] Ô 24 xác minh hiển thị 🎉 TẤT CẢ KIỂM TRA ĐÃ THÀNH CÔNG!

### Thời Gian Ước Tính
- **Lần chạy đầu tiên:** 5-10 phút (bao gồm tải xuống mô hình)
- **Các lần chạy sau:** 1-2 phút

---

## Phiên 05: Điều Phối Đa Tác Nhân

### Mục Đích
Trình diễn sự hợp tác giữa các tác nhân đa nhiệm sử dụng Foundry Local SDK - các tác nhân làm việc cùng nhau để tạo ra kết quả tinh chỉnh.

### Cài Đặt Nhanh

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Chạy Sổ Tay

1. **Mở** `session05_agents_orchestrator.ipynb`
2. **Khởi động lại kernel**
3. **Chạy tất cả các ô lệnh** theo thứ tự

### Cấu Hình Chính

**Cài Đặt Mặc Định (Cùng Mô Hình Cho Cả Hai Tác Nhân):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Cài Đặt Nâng Cao (Mô Hình Khác Nhau):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Kiến Trúc

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Kết Quả Mong Đợi

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Mở Rộng

**Thêm nhiều tác nhân hơn:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Kiểm tra theo lô:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Thời Gian Ước Tính
- **Lần chạy đầu tiên:** 3-5 phút
- **Các lần chạy sau:** 1-2 phút mỗi câu hỏi

---

## Phiên 06: Định Tuyến Mô Hình Dựa Trên Ý Định

### Mục Đích
Định tuyến thông minh các prompt đến các mô hình chuyên biệt dựa trên ý định được phát hiện.

### Cài Đặt Nhanh

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Lưu ý:** Phiên 06 mặc định sử dụng các mô hình CPU để đảm bảo tương thích tối đa.

### Chạy Sổ Tay

1. **Mở** `session06_models_router.ipynb`
2. **Khởi động lại kernel**
3. **Chạy tất cả các ô lệnh** theo thứ tự

### Cấu Hình Chính

**Danh Mục Mặc Định (Mô Hình CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Thay Thế (Mô Hình GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Phát Hiện Ý Định

Bộ định tuyến sử dụng các mẫu regex để phát hiện ý định:

| Ý Định | Ví Dụ Mẫu | Định Tuyến Đến |
|--------|-----------------|-----------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Tất cả các trường hợp khác | phi-4-mini-cpu |

### Kết Quả Mong Đợi

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Tùy Chỉnh

**Thêm ý định tùy chỉnh:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Bật theo dõi token:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Chuyển Sang Mô Hình GPU

Nếu bạn có VRAM 8GB+:

1. Trong **Ô #6**, bình luận danh mục CPU
2. Bỏ bình luận danh mục GPU
3. Tải mô hình GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Khởi động lại kernel và chạy lại sổ tay

### Thời Gian Ước Tính
- **Lần chạy đầu tiên:** 5-10 phút (tải mô hình)
- **Các lần chạy sau:** 30-60 giây mỗi lần kiểm tra

---

## Biến Môi Trường

### Cấu Hình Toàn Cục

Thiết lập trước khi khởi động Jupyter/VS Code:

**Windows (Command Prompt):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Cấu Hình Trong Sổ Tay

Thiết lập ở đầu bất kỳ sổ tay nào:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Lệnh Thông Dụng

### Quản Lý Dịch Vụ

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Quản Lý Mô Hình

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Kiểm Tra Endpoint

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Lệnh Chẩn Đoán

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Thực Hành Tốt Nhất

### Trước Khi Bắt Đầu Bất Kỳ Sổ Tay Nào

1. **Kiểm tra dịch vụ đang chạy:**
   ```bash
   foundry service status
   ```

2. **Xác minh các mô hình đã được nạp:**
   ```bash
   foundry model ls
   ```

3. **Khởi động lại kernel của sổ tay** nếu chạy lại

4. **Xóa tất cả kết quả đầu ra** để chạy sạch

### Quản Lý Tài Nguyên

1. **Sử dụng mô hình CPU theo mặc định** để đảm bảo tương thích
2. **Chuyển sang mô hình GPU** chỉ khi bạn có VRAM 8GB+
3. **Đóng các ứng dụng GPU khác** trước khi chạy
4. **Giữ dịch vụ chạy** giữa các phiên sổ tay
5. **Theo dõi sử dụng tài nguyên** bằng Task Manager / nvidia-smi

### Xử Lý Sự Cố

1. **Luôn kiểm tra dịch vụ trước** khi gỡ lỗi mã
2. **Khởi động lại kernel** nếu bạn thấy cấu hình cũ
3. **Chạy lại các ô chẩn đoán** sau bất kỳ thay đổi nào
4. **Kiểm tra tên mô hình** khớp với những gì đã nạp
5. **Xác minh cổng endpoint** khớp với trạng thái dịch vụ

---

## Tham Khảo Nhanh: Bí Danh Mô Hình

### Các Mô Hình Thông Dụng

| Bí Danh | Kích Thước | Tốt Nhất Cho | RAM/VRAM | Biến Thể |
|-------|------|----------|----------|----------|
| `phi-4-mini` | ~4B | Chat tổng quát, tóm tắt | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Sinh mã, tái cấu trúc | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Nhiệm vụ tổng quát, hiệu quả | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Nhanh, ít tài nguyên | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Phân loại, ít tài nguyên | 1-2GB | `-cpu`, `-cuda-gpu` |

### Quy Ước Đặt Tên Biến Thể

- **Tên cơ bản** (ví dụ: `phi-4-mini`): Tự động chọn biến thể tốt nhất cho phần cứng của bạn
- **`-cpu`**: Tối ưu hóa cho CPU, hoạt động ở mọi nơi
- **`-cuda-gpu`**: Tối ưu hóa cho GPU NVIDIA, yêu cầu VRAM 8GB+
- **`-npu`**: Tối ưu hóa cho Qualcomm NPU, yêu cầu trình điều khiển NPU

**Khuyến nghị:** Sử dụng tên cơ bản (không có hậu tố) và để Foundry Local tự động chọn biến thể tốt nhất.

---

## Chỉ Số Thành Công

Bạn đã sẵn sàng khi thấy:

✅ `foundry service status` hiển thị "running"  
✅ `foundry model ls` hiển thị các mô hình bạn cần  
✅ Dịch vụ truy cập được tại endpoint chính xác  
✅ Kiểm tra sức khỏe trả về 200 OK  
✅ Các ô chẩn đoán trong sổ tay thành công  
✅ Không có lỗi kết nối trong kết quả đầu ra  

---

## Nhận Trợ Giúp

### Tài Liệu
- **Kho Chính**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Tham Khảo CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **Xử Lý Sự Cố**: Xem `troubleshooting.md` trong thư mục này  

### Vấn Đề GitHub
- https://github.com/microsoft/Foundry-Local/issues  
- https://github.com/microsoft/edgeai-for-beginners/issues  

---

**Cập Nhật Lần Cuối:** 8 Tháng 10, 2025  
**Phiên Bản:** Workshop Notebooks 2.0  

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.