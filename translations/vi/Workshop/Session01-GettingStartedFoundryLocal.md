# Buổi 1: Bắt đầu với Foundry Local

## Tóm tắt

Học cách cài đặt, cấu hình và chạy các mô hình AI đầu tiên của bạn bằng Microsoft Foundry Local. Buổi thực hành này cung cấp hướng dẫn từng bước về suy luận cục bộ, từ cài đặt đến xây dựng ứng dụng chat đầu tiên của bạn sử dụng các mô hình như Phi-4, Qwen và DeepSeek.

## Mục tiêu học tập

Sau buổi học này, bạn sẽ:

- **Cài đặt và cấu hình**: Thiết lập Foundry Local với xác minh cài đặt đúng cách
- **Thành thạo thao tác CLI**: Sử dụng Foundry Local CLI để quản lý và triển khai mô hình
- **Chạy mô hình đầu tiên**: Triển khai và tương tác thành công với một mô hình AI cục bộ
- **Xây dựng ứng dụng chat**: Tạo ứng dụng chat cơ bản sử dụng Foundry Local Python SDK
- **Hiểu AI cục bộ**: Nắm vững các nguyên tắc cơ bản về suy luận cục bộ và quản lý mô hình

## Yêu cầu trước

### Yêu cầu hệ thống

- **Windows**: Windows 11 (22H2 hoặc mới hơn) HOẶC **macOS**: macOS 11+ (hỗ trợ hạn chế)
- **RAM**: Tối thiểu 8GB, khuyến nghị 16GB+
- **Dung lượng lưu trữ**: Tối thiểu 10GB trống cho các mô hình
- **Python**: Phiên bản 3.10 hoặc mới hơn
- **Quyền quản trị**: Quyền quản trị để cài đặt

### Môi trường phát triển

- Visual Studio Code với phần mở rộng Python (khuyến nghị)
- Truy cập dòng lệnh (PowerShell trên Windows, Terminal trên macOS)
- Git để clone các kho lưu trữ (tùy chọn)

## Quy trình workshop (30 phút)

### Bước 1: Cài đặt Foundry Local (5 phút)

#### Cài đặt trên Windows

Cài đặt Foundry Local bằng trình quản lý gói Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Lựa chọn khác: Tải xuống trực tiếp từ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Cài đặt trên macOS (Hỗ trợ hạn chế)

> [!NOTE] 
> Hỗ trợ macOS hiện đang trong giai đoạn thử nghiệm. Kiểm tra tài liệu chính thức để biết thông tin mới nhất.

Nếu có sẵn, cài đặt bằng Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Lựa chọn khác cho người dùng macOS:**
- Sử dụng máy ảo Windows 11 (Parallels/UTM) và làm theo các bước trên Windows
- Chạy qua container nếu có và cấu hình `FOUNDRY_LOCAL_ENDPOINT`

### Bước 2: Xác minh cài đặt (3 phút)

Sau khi cài đặt, khởi động lại terminal của bạn và xác minh Foundry Local hoạt động:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Kết quả mong đợi sẽ hiển thị thông tin phiên bản và các lệnh có sẵn.

### Bước 3: Thiết lập môi trường Python (5 phút)

Tạo môi trường Python chuyên dụng cho workshop này:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Bước 4: Chạy mô hình đầu tiên của bạn (7 phút)

Bây giờ hãy chạy mô hình AI đầu tiên của chúng ta cục bộ!

#### Bắt đầu với Phi-4 Mini (Mô hình đầu tiên được khuyến nghị)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Lệnh này tải xuống mô hình (lần đầu tiên) và tự động khởi động dịch vụ Foundry Local.

#### Kiểm tra những gì đang chạy

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Thử các mô hình khác

Khi phi-4-mini hoạt động, hãy thử nghiệm với các mô hình khác:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Bước 5: Xây dựng ứng dụng chat đầu tiên của bạn (10 phút)

Bây giờ hãy tạo một ứng dụng Python sử dụng các mô hình mà chúng ta vừa khởi động.

#### Tạo script chat

Tạo một file mới tên là `my_first_chat.py` (hoặc sử dụng mẫu được cung cấp):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Ví dụ liên quan**: Để sử dụng nâng cao hơn, xem:
>
> - **Mẫu Python**: `Workshop/samples/session01/chat_bootstrap.py` - Bao gồm phản hồi streaming và xử lý lỗi
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Phiên bản tương tác với giải thích chi tiết

#### Kiểm tra ứng dụng chat của bạn

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Lựa chọn khác: Sử dụng trực tiếp các mẫu được cung cấp

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Hoặc khám phá notebook tương tác
Mở Workshop/notebooks/session01_chat_bootstrap.ipynb trong VS Code

Thử các cuộc hội thoại ví dụ sau:

- "Microsoft Foundry Local là gì?"
- "Liệt kê 3 lợi ích của việc chạy mô hình AI cục bộ"
- "Giúp tôi hiểu AI edge"

## Những gì bạn đã đạt được

Chúc mừng! Bạn đã thành công:

1. ✅ **Cài đặt Foundry Local** và xác minh nó hoạt động
2. ✅ **Khởi động mô hình AI đầu tiên** (phi-4-mini) cục bộ
3. ✅ **Thử nghiệm các mô hình khác** qua dòng lệnh
4. ✅ **Xây dựng ứng dụng chat** kết nối với AI cục bộ của bạn
5. ✅ **Trải nghiệm suy luận AI cục bộ** mà không cần phụ thuộc vào đám mây

## Hiểu những gì đã xảy ra

### Suy luận AI cục bộ

- Các mô hình AI của bạn chạy hoàn toàn trên máy tính của bạn
- Không có dữ liệu nào được gửi lên đám mây
- Phản hồi được tạo cục bộ sử dụng CPU/GPU của bạn
- Quyền riêng tư và bảo mật được duy trì

### Quản lý mô hình

- `foundry model run` tải xuống và khởi động các mô hình
- **FoundryLocalManager SDK** tự động xử lý khởi động dịch vụ và tải mô hình
- Các mô hình được lưu trữ cục bộ để sử dụng trong tương lai
- Nhiều mô hình có thể được tải xuống nhưng thường chỉ chạy một mô hình tại một thời điểm
- Dịch vụ tự động quản lý vòng đời mô hình

### SDK vs CLI

- **Cách tiếp cận CLI**: Quản lý mô hình thủ công với `foundry model run <model>`
- **Cách tiếp cận SDK**: Quản lý dịch vụ + mô hình tự động với `FoundryLocalManager(alias)`
- **Khuyến nghị**: Sử dụng SDK cho ứng dụng, CLI để thử nghiệm và khám phá

## Tham khảo các lệnh thông dụng

### Các lệnh CLI cần thiết

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Gợi ý mô hình

- **phi-4-mini**: Mô hình khởi đầu tốt nhất - nhanh, nhẹ, chất lượng tốt
- **qwen2.5-0.5b**: Suy luận nhanh nhất, sử dụng ít bộ nhớ
- **gpt-oss-20b**: Phản hồi chất lượng cao hơn, cần nhiều tài nguyên hơn
- **deepseek-coder-1.3b**: Tối ưu hóa cho lập trình và các tác vụ mã hóa

## Xử lý sự cố

### "Không tìm thấy lệnh Foundry"

**Giải pháp:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Mô hình không tải được"

**Giải pháp:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Kết nối bị từ chối trên localhost"

**Giải pháp:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Các bước tiếp theo

### Hành động ngay lập tức

1. **Thử nghiệm** với các mô hình và lời nhắc khác nhau
2. **Chỉnh sửa** ứng dụng chat của bạn để thử các mô hình khác
3. **Tạo** lời nhắc của riêng bạn và kiểm tra phản hồi
4. **Khám phá** Buổi 2: Xây dựng ứng dụng RAG

### Lộ trình học nâng cao

1. **Buổi 2**: Xây dựng giải pháp AI với RAG (Retrieval-Augmented Generation)
2. **Buổi 3**: So sánh các mô hình mã nguồn mở khác nhau
3. **Buổi 4**: Làm việc với các mô hình tiên tiến
4. **Buổi 5**: Xây dựng hệ thống AI đa tác nhân

## Biến môi trường (Tùy chọn)

Để sử dụng nâng cao hơn, bạn có thể thiết lập các biến môi trường sau:

| Biến | Mục đích | Ví dụ |
|------|----------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Mô hình mặc định để sử dụng | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Ghi đè URL endpoint | `http://localhost:5273/v1` |

Tạo file `.env` trong thư mục dự án của bạn:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Tài nguyên bổ sung

### Tài liệu

- [Tham khảo Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Hướng dẫn cài đặt Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Danh mục mô hình](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Mã mẫu

- **Mẫu Python Buổi 01**: `Workshop/samples/session01/chat_bootstrap.py` - Ứng dụng chat hoàn chỉnh với streaming
- **Notebook Buổi 01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Hướng dẫn tương tác  
- [Mẫu 01 Module08](../Module08/samples/01/README.md) - Khởi động nhanh REST Chat
- [Mẫu 02 Module08](../Module08/samples/02/README.md) - Tích hợp OpenAI SDK
- [Mẫu 03 Module08](../Module08/samples/03/README.md) - Khám phá & đánh giá mô hình

### Cộng đồng

- [Thảo luận GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Cộng đồng Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Thời lượng buổi học**: 30 phút thực hành + 15 phút hỏi đáp  
**Mức độ khó**: Người mới bắt đầu  
**Yêu cầu trước**: Windows 11/macOS 11+, Python 3.10+, Quyền quản trị

## Kịch bản ví dụ trong workshop

### Bối cảnh thực tế

**Kịch bản**: Một nhóm IT doanh nghiệp cần đánh giá suy luận AI trên thiết bị để xử lý phản hồi nhạy cảm của nhân viên mà không gửi dữ liệu đến các dịch vụ bên ngoài.

**Mục tiêu của bạn**: Chứng minh rằng các mô hình AI cục bộ có thể cung cấp phản hồi chất lượng với độ trễ dưới một giây trong khi duy trì hoàn toàn quyền riêng tư dữ liệu.

### Lời nhắc kiểm tra

Sử dụng các lời nhắc này để xác thực thiết lập của bạn:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Tiêu chí thành công

- ✅ Tất cả các lời nhắc nhận được phản hồi trong vòng dưới 2 giây
- ✅ Không có dữ liệu nào rời khỏi máy cục bộ của bạn
- ✅ Phản hồi phù hợp và hữu ích
- ✅ Ứng dụng chat của bạn hoạt động mượt mà

Việc xác thực này đảm bảo thiết lập Foundry Local của bạn đã sẵn sàng cho các workshop nâng cao trong Buổi 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->