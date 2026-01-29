# Hướng Dẫn Cấu Hình Môi Trường

## Tổng Quan

Các mẫu trong Workshop sử dụng biến môi trường để cấu hình, được tập trung trong tệp `.env` tại thư mục gốc của kho lưu trữ. Điều này cho phép tùy chỉnh dễ dàng mà không cần sửa đổi mã nguồn.

## Bắt Đầu Nhanh

### 1. Kiểm Tra Yêu Cầu

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Cấu Hình Môi Trường

Tệp `.env` đã được cấu hình với các giá trị mặc định hợp lý. Hầu hết người dùng sẽ không cần thay đổi gì.

**Tùy chọn**: Xem xét và tùy chỉnh cài đặt:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Áp Dụng Cấu Hình

**Đối với Script Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Đối với Notebook:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Tham Khảo Biến Môi Trường

### Cấu Hình Cốt Lõi

| Biến | Mặc định | Mô tả |
|------|----------|-------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Mô hình mặc định cho các mẫu |
| `FOUNDRY_LOCAL_ENDPOINT` | (trống) | Ghi đè điểm cuối dịch vụ |
| `PYTHONPATH` | Đường dẫn Workshop | Đường dẫn tìm kiếm module Python |

**Khi nào cần thiết lập FOUNDRY_LOCAL_ENDPOINT:**
- Phiên bản Foundry Local từ xa
- Cấu hình cổng tùy chỉnh
- Phân tách phát triển/sản xuất

**Ví dụ:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Biến Cụ Thể Theo Phiên

#### Phiên 02: RAG Pipeline
| Biến | Mặc định | Mục đích |
|------|----------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Mô hình nhúng |
| `RAG_QUESTION` | Được cấu hình trước | Câu hỏi kiểm tra |

#### Phiên 03: Benchmarking
| Biến | Mặc định | Mục đích |
|------|----------|----------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Các mô hình để đánh giá |
| `BENCH_ROUNDS` | `3` | Số lần lặp mỗi mô hình |
| `BENCH_PROMPT` | Được cấu hình trước | Lời nhắc kiểm tra |
| `BENCH_STREAM` | `0` | Đo độ trễ token đầu tiên |

#### Phiên 04: So Sánh Mô Hình
| Biến | Mặc định | Mục đích |
|------|----------|----------|
| `SLM_ALIAS` | `phi-4-mini` | Mô hình ngôn ngữ nhỏ |
| `LLM_ALIAS` | `qwen2.5-7b` | Mô hình ngôn ngữ lớn |
| `COMPARE_PROMPT` | Được cấu hình trước | Lời nhắc so sánh |
| `COMPARE_RETRIES` | `2` | Số lần thử lại |

#### Phiên 05: Điều Phối Đa Tác Nhân
| Biến | Mặc định | Mục đích |
|------|----------|----------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Mô hình tác nhân nghiên cứu |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Mô hình tác nhân biên tập |
| `AGENT_QUESTION` | Được cấu hình trước | Câu hỏi kiểm tra |

### Cấu Hình Độ Tin Cậy

| Biến | Mặc định | Mục đích |
|------|----------|----------|
| `SHOW_USAGE` | `1` | In ra lượng token đã sử dụng |
| `RETRY_ON_FAIL` | `1` | Bật logic thử lại |
| `RETRY_BACKOFF` | `1.0` | Thời gian chờ thử lại (giây) |

## Cấu Hình Thông Dụng

### Cài Đặt Phát Triển (Lặp Nhanh)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Cài Đặt Sản Xuất (Tập Trung Vào Chất Lượng)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Cài Đặt Đánh Giá
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Chuyên Môn Hóa Đa Tác Nhân
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Phát Triển Từ Xa
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Các Mô Hình Được Khuyến Nghị

### Theo Trường Hợp Sử Dụng

**Mục Đích Chung:**
- `phi-4-mini` - Cân bằng giữa chất lượng và tốc độ

**Phản Hồi Nhanh:**
- `qwen2.5-0.5b` - Rất nhanh, tốt cho phân loại
- `phi-4-mini` - Nhanh với chất lượng tốt

**Chất Lượng Cao:**
- `qwen2.5-7b` - Chất lượng tốt nhất, sử dụng tài nguyên cao hơn
- `phi-4-mini` - Chất lượng tốt, ít tài nguyên hơn

**Tạo Mã:**
- `deepseek-coder-1.3b` - Chuyên biệt cho mã hóa
- `phi-4-mini` - Mục đích chung cho mã hóa

### Theo Khả Năng Tài Nguyên

**Tài Nguyên Thấp (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Tài Nguyên Trung Bình (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Tài Nguyên Cao (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Cấu Hình Nâng Cao

### Điểm Cuối Tùy Chỉnh

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Nhiệt Độ & Lấy Mẫu (Ghi Đè Trong Mã)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Cài Đặt Kết Hợp Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Xử Lý Sự Cố

### Biến Môi Trường Không Được Tải

**Triệu chứng:**
- Script sử dụng sai mô hình
- Lỗi kết nối
- Biến không được nhận diện

**Giải pháp:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Vấn Đề Kết Nối Dịch Vụ

**Triệu chứng:**
- Lỗi "Connection refused"
- "Dịch vụ không khả dụng"
- Lỗi hết thời gian kết nối

**Giải pháp:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Mô Hình Không Tìm Thấy

**Triệu chứng:**
- Lỗi "Model not found"
- "Alias không được nhận diện"

**Giải pháp:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Lỗi Nhập Khẩu

**Triệu chứng:**
- Lỗi "Module not found"

**Giải pháp:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Kiểm Tra Cấu Hình

### Xác Minh Tải Môi Trường

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Kiểm Tra Kết Nối Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## Thực Hành Bảo Mật Tốt Nhất

### 1. Không Bao Giờ Cam Kết Bí Mật

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Sử Dụng Các Tệp .env Riêng Biệt

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Xoay Vòng API Keys

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Sử Dụng Cấu Hình Theo Môi Trường

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Tài Liệu SDK

- **Kho Chính**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Tài Liệu API**: Xem kho SDK để biết thông tin mới nhất

## Tài Nguyên Bổ Sung

- `QUICK_START.md` - Hướng dẫn bắt đầu
- `Workshop/samples/*/README.md` - Hướng dẫn cụ thể cho từng mẫu

---

**Cập Nhật Lần Cuối**: 2025-01-08  
**Phiên Bản**: 2.0  
**SDK**: Foundry Local Python SDK (mới nhất)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->