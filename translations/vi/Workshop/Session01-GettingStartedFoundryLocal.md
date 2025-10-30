<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T22:32:38+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "vi"
}
-->
# Buổi 1: Bắt đầu với Foundry Local

## Tóm tắt

Khởi đầu hành trình của bạn với Foundry Local bằng cách cài đặt và cấu hình trên Windows 11. Tìm hiểu cách thiết lập CLI, kích hoạt tăng tốc phần cứng và lưu trữ mô hình để suy luận nhanh tại chỗ. Buổi thực hành này hướng dẫn cách chạy các mô hình như Phi, Qwen, DeepSeek và GPT-OSS-20B bằng các lệnh CLI có thể tái sử dụng.

## Mục tiêu học tập

Sau buổi học này, bạn sẽ:

- **Cài đặt và cấu hình**: Thiết lập Foundry Local trên Windows 11 với các cài đặt hiệu suất tối ưu
- **Thành thạo thao tác CLI**: Sử dụng Foundry Local CLI để quản lý và triển khai mô hình
- **Kích hoạt tăng tốc phần cứng**: Cấu hình tăng tốc GPU với ONNXRuntime hoặc WebGPU
- **Triển khai nhiều mô hình**: Chạy các mô hình phi-4, GPT-OSS-20B, Qwen và DeepSeek tại chỗ
- **Xây dựng ứng dụng đầu tiên**: Điều chỉnh các mẫu hiện có để sử dụng Foundry Local Python SDK

# Kiểm tra mô hình (một lần nhắc không tương tác)
foundry model run phi-4-mini --prompt "Xin chào, hãy giới thiệu về bản thân"

- Windows 11 (22H2 hoặc mới hơn)
# Liệt kê các mô hình trong danh mục (các mô hình đã tải xuất hiện sau khi chạy)
foundry model list
## NOTE: Hiện tại không có cờ `--running` chuyên dụng; để xem mô hình nào đã tải, hãy bắt đầu một cuộc trò chuyện hoặc kiểm tra nhật ký dịch vụ.
- Python 3.10+ đã cài đặt
- Visual Studio Code với tiện ích mở rộng Python
- Quyền quản trị để cài đặt

### (Tùy chọn) Biến môi trường

Tạo `.env` (hoặc thiết lập trong shell) để làm cho các script có thể di chuyển:
# So sánh phản hồi (không tương tác)
foundry model run gpt-oss-20b --prompt "Giải thích AI biên một cách đơn giản"
| Biến | Mục đích | Ví dụ |
|------|----------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Bí danh mô hình ưu tiên (danh mục tự động chọn biến thể tốt nhất) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Ghi đè điểm cuối (nếu không sẽ tự động từ trình quản lý) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Kích hoạt demo streaming | `true` |

> Nếu `FOUNDRY_LOCAL_ENDPOINT=auto` (hoặc không được thiết lập), chúng tôi sẽ lấy từ trình quản lý SDK.

## Quy trình demo (30 phút)

### 1. Cài đặt Foundry Local và xác minh thiết lập CLI (10 phút)

# Liệt kê các mô hình đã lưu trữ
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Xem trước / Nếu được hỗ trợ)**

Nếu có gói macOS gốc (kiểm tra tài liệu chính thức để biết thông tin mới nhất):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Nếu các tệp nhị phân gốc macOS chưa có sẵn, bạn vẫn có thể: 
1. Sử dụng VM Windows 11 ARM/Intel (Parallels / UTM) và làm theo các bước trên Windows. 
2. Chạy các mô hình qua container (nếu hình ảnh container được xuất bản) và thiết lập `FOUNDRY_LOCAL_ENDPOINT` tới cổng được mở.

**Tạo môi trường ảo Python (Đa nền tảng)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Nâng cấp pip và cài đặt các phụ thuộc cốt lõi:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Bước 1.2: Xác minh cài đặt

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Bước 1.3: Cấu hình môi trường

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Khởi động SDK (Khuyến nghị)

Thay vì khởi động dịch vụ và chạy mô hình thủ công, **Foundry Local Python SDK** có thể khởi động mọi thứ:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Nếu bạn thích kiểm soát rõ ràng, bạn vẫn có thể sử dụng CLI + client OpenAI như được hiển thị sau.

### 2. Chạy mô hình tại chỗ qua CLI (10 phút)

#### Bước 3.1: Triển khai mô hình Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Bước 3.2: Triển khai GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Bước 3.3: Tải thêm mô hình

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Dự án khởi đầu: Điều chỉnh 01-run-phi cho Foundry Local (5 phút)

#### Bước 4.1: Tạo ứng dụng trò chuyện cơ bản

Tạo `samples/01-foundry-quickstart/chat_quickstart.py` (cập nhật để sử dụng trình quản lý nếu có):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Bước 4.2: Kiểm tra ứng dụng

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Các khái niệm chính được đề cập

### 1. Kiến trúc Foundry Local

- **Công cụ suy luận tại chỗ**: Chạy mô hình hoàn toàn trên thiết bị của bạn
- **Tương thích SDK OpenAI**: Tích hợp liền mạch với mã OpenAI hiện có
- **Quản lý mô hình**: Tải xuống, lưu trữ và chạy nhiều mô hình một cách hiệu quả
- **Tối ưu hóa phần cứng**: Tận dụng tăng tốc GPU, NPU và CPU

### 2. Tham chiếu lệnh CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Tích hợp Python SDK

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Khắc phục sự cố thường gặp

### Vấn đề 1: "Không tìm thấy lệnh Foundry"

**Giải pháp:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Vấn đề 2: "Mô hình không tải được"

**Giải pháp:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Vấn đề 3: "Kết nối bị từ chối trên localhost:5273"

**Giải pháp:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Mẹo tối ưu hóa hiệu suất

### 1. Chiến lược chọn mô hình

- **Phi-4-mini**: Tốt nhất cho các nhiệm vụ chung, sử dụng ít bộ nhớ
- **Qwen2.5-0.5b**: Suy luận nhanh nhất, tài nguyên tối thiểu
- **GPT-OSS-20B**: Chất lượng cao nhất, yêu cầu nhiều tài nguyên hơn
- **DeepSeek-Coder**: Tối ưu hóa cho các nhiệm vụ lập trình

### 2. Tối ưu hóa phần cứng

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Giám sát hiệu suất

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### Nâng cấp tùy chọn

| Nâng cấp | Nội dung | Cách thực hiện |
|----------|----------|----------------|
| Tiện ích chia sẻ | Loại bỏ logic client/bootstrap trùng lặp | Sử dụng `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Hiển thị sử dụng token | Dạy tư duy về chi phí/hiệu quả sớm | Thiết lập `SHOW_USAGE=1` để in token nhắc/hoàn thành/tổng cộng |
| So sánh xác định | Kiểm tra hiệu suất & hồi quy ổn định | Sử dụng `temperature=0`, `top_p=1`, văn bản nhắc nhất quán |
| Độ trễ token đầu tiên | Chỉ số phản hồi cảm nhận | Điều chỉnh script benchmark với streaming (`BENCH_STREAM=1`) |
| Thử lại khi lỗi thoáng qua | Demo bền bỉ khi khởi động lạnh | `RETRY_ON_FAIL=1` (mặc định) & điều chỉnh `RETRY_BACKOFF` |
| Kiểm tra nhanh | Kiểm tra nhanh các luồng chính | Chạy `python Workshop/tests/smoke.py` trước workshop |
| Hồ sơ bí danh mô hình | Chuyển đổi nhanh giữa các bộ mô hình trên máy | Duy trì `.env` với `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Hiệu quả lưu trữ | Tránh khởi động lại nhiều lần trong chạy mẫu | Tiện ích quản lý lưu trữ; tái sử dụng giữa các script/notebook |
| Khởi động lần đầu | Giảm đột biến độ trễ p95 | Gửi một nhắc nhỏ sau khi tạo `FoundryLocalManager` |

Ví dụ khởi động cơ bản xác định (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Bạn sẽ thấy đầu ra tương tự & số lượng token giống hệt nhau trong lần chạy thứ hai, xác nhận tính xác định.

## Bước tiếp theo

Sau khi hoàn thành buổi học này:

1. **Khám phá Buổi 2**: Xây dựng giải pháp AI với Azure AI Foundry RAG
2. **Thử các mô hình khác nhau**: Thử nghiệm với Qwen, DeepSeek và các dòng mô hình khác
3. **Tối ưu hóa hiệu suất**: Tinh chỉnh cài đặt cho phần cứng cụ thể của bạn
4. **Xây dựng ứng dụng tùy chỉnh**: Sử dụng Foundry Local SDK trong các dự án của riêng bạn

## Tài nguyên bổ sung

### Tài liệu
- [Tham chiếu Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Hướng dẫn cài đặt Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Danh mục mô hình](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Mã mẫu
- [Mẫu Module08 01](./samples/01/README.md) - Khởi đầu trò chuyện REST
- [Mẫu Module08 02](./samples/02/README.md) - Tích hợp SDK OpenAI
- [Mẫu Module08 03](./samples/03/README.md) - Khám phá & đánh giá mô hình

### Cộng đồng
- [Thảo luận GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Cộng đồng Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Thời lượng buổi học**: 30 phút thực hành + 15 phút hỏi đáp  
**Mức độ khó**: Người mới bắt đầu  
**Yêu cầu trước**: Windows 11, Python 3.10+, quyền quản trị

## Kịch bản mẫu & ánh xạ workshop

| Script / Notebook Workshop | Kịch bản | Mục tiêu | Ví dụ đầu vào | Dataset cần thiết |
|----------------------------|----------|----------|---------------|-------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Đội IT nội bộ đánh giá suy luận tại chỗ cho cổng đánh giá quyền riêng tư | Chứng minh SLM tại chỗ phản hồi trong độ trễ dưới một giây với các nhắc chuẩn | "Liệt kê hai lợi ích của suy luận tại chỗ." | Không (một lần nhắc) |
| Mã khởi đầu điều chỉnh nhanh | Nhà phát triển chuyển đổi script OpenAI hiện có sang Foundry Local | Hiển thị khả năng tương thích thay thế | "Đưa ra hai lợi ích của suy luận tại chỗ." | Chỉ nhắc nội tuyến |

### Tường thuật kịch bản
Đội bảo mật & tuân thủ phải xác nhận liệu dữ liệu nguyên mẫu nhạy cảm có thể được xử lý tại chỗ hay không. Họ chạy script khởi động với nhiều nhắc (quyền riêng tư, độ trễ, chi phí) sử dụng chế độ xác định temperature=0 để ghi lại đầu ra cơ bản cho so sánh sau (đánh giá hiệu suất Buổi 3 và đối chiếu SLM vs LLM Buổi 4).

### JSON bộ nhắc tối thiểu (tùy chọn)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Sử dụng danh sách này để tạo vòng lặp đánh giá có thể tái tạo hoặc để khởi tạo một bộ kiểm tra hồi quy trong tương lai.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.