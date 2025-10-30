<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T13:33:39+00:00",
  "source_file": "AGENTS.md",
  "language_code": "vi"
}
-->
# AGENTS.md

> **Hướng dẫn dành cho nhà phát triển đóng góp vào EdgeAI cho người mới bắt đầu**
> 
> Tài liệu này cung cấp thông tin toàn diện cho các nhà phát triển, tác nhân AI và những người đóng góp làm việc với kho lưu trữ này. Nó bao gồm thiết lập, quy trình phát triển, kiểm thử và các phương pháp tốt nhất.
> 
> **Cập nhật lần cuối**: 30 tháng 10, 2025 | **Phiên bản tài liệu**: 3.0

## Mục lục

- [Tổng quan dự án](../..)
- [Cấu trúc kho lưu trữ](../..)
- [Yêu cầu trước](../..)
- [Lệnh thiết lập](../..)
- [Quy trình phát triển](../..)
- [Hướng dẫn kiểm thử](../..)
- [Hướng dẫn về phong cách mã](../..)
- [Hướng dẫn yêu cầu kéo](../..)
- [Hệ thống dịch thuật](../..)
- [Tích hợp Foundry Local](../..)
- [Xây dựng và triển khai](../..)
- [Các vấn đề thường gặp và cách khắc phục](../..)
- [Tài nguyên bổ sung](../..)
- [Ghi chú cụ thể về dự án](../..)
- [Nhận hỗ trợ](../..)

## Tổng quan dự án

EdgeAI cho người mới bắt đầu là một kho lưu trữ giáo dục toàn diện dạy về phát triển Edge AI với các Mô hình Ngôn ngữ Nhỏ (SLMs). Khóa học bao gồm các nguyên tắc cơ bản về EdgeAI, triển khai mô hình, kỹ thuật tối ưu hóa và các triển khai sẵn sàng sản xuất sử dụng Microsoft Foundry Local và các khung AI khác nhau.

**Công nghệ chính:**
- Python 3.8+ (ngôn ngữ chính cho các mẫu AI/ML)
- .NET C# (mẫu AI/ML)
- JavaScript/Node.js với Electron (cho ứng dụng máy tính để bàn)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Các khung AI: LangChain, Semantic Kernel, Chainlit
- Tối ưu hóa mô hình: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Loại kho lưu trữ:** Kho nội dung giáo dục với 8 mô-đun và 10 ứng dụng mẫu toàn diện

**Kiến trúc:** Lộ trình học đa mô-đun với các mẫu thực hành minh họa các mẫu triển khai Edge AI

## Cấu trúc kho lưu trữ

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Yêu cầu trước

### Công cụ cần thiết

- **Python 3.8+** - Cho các mẫu AI/ML và notebook
- **Node.js 16+** - Cho ứng dụng mẫu Electron
- **Git** - Cho kiểm soát phiên bản
- **Microsoft Foundry Local** - Để chạy các mô hình AI cục bộ

### Công cụ khuyến nghị

- **Visual Studio Code** - Với các tiện ích mở rộng Python, Jupyter và Pylance
- **Windows Terminal** - Để trải nghiệm dòng lệnh tốt hơn (người dùng Windows)
- **Docker** - Cho phát triển trong container (tùy chọn)

### Yêu cầu hệ thống

- **RAM**: Tối thiểu 8GB, khuyến nghị 16GB+ cho các kịch bản đa mô hình
- **Dung lượng lưu trữ**: Tối thiểu 10GB không gian trống cho mô hình và phụ thuộc
- **Hệ điều hành**: Windows 10/11, macOS 11+, hoặc Linux (Ubuntu 20.04+)
- **Phần cứng**: CPU hỗ trợ AVX2; GPU (CUDA, Qualcomm NPU) tùy chọn nhưng được khuyến nghị

### Yêu cầu kiến thức

- Hiểu cơ bản về lập trình Python
- Quen thuộc với giao diện dòng lệnh
- Hiểu các khái niệm AI/ML (cho phát triển mẫu)
- Quy trình Git và yêu cầu kéo

## Lệnh thiết lập

### Thiết lập kho lưu trữ

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Thiết lập mẫu Python (Mô-đun08 và các mẫu Workshop)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Thiết lập mẫu Node.js (Mẫu 08 - Ứng dụng Chat Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Thiết lập Foundry Local

Foundry Local cần thiết để chạy các mẫu. Tải xuống và cài đặt từ kho lưu trữ chính thức:

**Cài đặt:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Thủ công**: Tải xuống từ [trang phát hành](https://github.com/microsoft/Foundry-Local/releases)

**Bắt đầu nhanh:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Lưu ý**: Foundry Local tự động chọn biến thể mô hình tốt nhất cho phần cứng của bạn (GPU CUDA, NPU Qualcomm, hoặc CPU).

## Quy trình phát triển

### Phát triển nội dung

Kho lưu trữ này chủ yếu chứa **nội dung giáo dục Markdown**. Khi thực hiện thay đổi:

1. Chỉnh sửa các tệp `.md` trong các thư mục mô-đun tương ứng
2. Tuân theo các mẫu định dạng hiện có
3. Đảm bảo các ví dụ mã chính xác và đã được kiểm thử
4. Cập nhật nội dung dịch tương ứng nếu cần (hoặc để tự động hóa xử lý)

### Phát triển ứng dụng mẫu

Đối với các mẫu Python Mô-đun08 (mẫu 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Đối với các mẫu Python Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Đối với mẫu Electron (mẫu 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Kiểm thử ứng dụng mẫu

Các mẫu Python không có kiểm thử tự động nhưng có thể được xác thực bằng cách chạy chúng:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Mẫu Electron có cơ sở hạ tầng kiểm thử:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Hướng dẫn kiểm thử

### Xác thực nội dung

Kho lưu trữ sử dụng quy trình dịch tự động. Không cần kiểm thử thủ công cho các bản dịch.

**Xác thực thủ công cho thay đổi nội dung:**
1. Xem trước hiển thị Markdown bằng cách xem trước các tệp `.md`
2. Xác minh tất cả các liên kết trỏ đến mục tiêu hợp lệ
3. Kiểm thử bất kỳ đoạn mã nào được bao gồm trong tài liệu
4. Kiểm tra rằng hình ảnh tải đúng cách

### Kiểm thử ứng dụng mẫu

**Mô-đun08/mẫu/08 (ứng dụng Electron) có kiểm thử toàn diện:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Các mẫu Python nên được kiểm thử thủ công:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Hướng dẫn về phong cách mã

### Nội dung Markdown

- Sử dụng hệ thống tiêu đề nhất quán (# cho tiêu đề, ## cho các phần chính, ### cho các phần phụ)
- Bao gồm các khối mã với chỉ định ngôn ngữ: ```python, ```bash, ```javascript
- Tuân theo định dạng hiện có cho bảng, danh sách và nhấn mạnh
- Giữ các dòng dễ đọc (nhắm đến ~80-100 ký tự, nhưng không nghiêm ngặt)
- Sử dụng liên kết tương đối cho các tham chiếu nội bộ

### Phong cách mã Python

- Tuân theo quy ước PEP 8
- Sử dụng gợi ý kiểu khi thích hợp
- Bao gồm docstring cho các hàm và lớp
- Sử dụng tên biến có ý nghĩa
- Giữ các hàm tập trung và ngắn gọn

### Phong cách mã JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Quy ước chính:**
- Cấu hình ESLint được cung cấp trong mẫu 08
- Prettier để định dạng mã
- Sử dụng cú pháp ES6+ hiện đại
- Tuân theo các mẫu hiện có trong cơ sở mã

## Hướng dẫn yêu cầu kéo

### Quy trình đóng góp

1. **Fork kho lưu trữ** và tạo một nhánh mới từ `main`
2. **Thực hiện thay đổi của bạn** theo hướng dẫn phong cách mã
3. **Kiểm thử kỹ lưỡng** sử dụng hướng dẫn kiểm thử ở trên
4. **Commit với thông điệp rõ ràng** theo định dạng commit thông thường
5. **Đẩy lên fork của bạn** và tạo yêu cầu kéo
6. **Phản hồi phản hồi** từ người duyệt trong quá trình xem xét

### Quy ước đặt tên nhánh

- `feature/<module>-<description>` - Cho tính năng mới hoặc nội dung
- `fix/<module>-<description>` - Cho sửa lỗi
- `docs/<description>` - Cho cải tiến tài liệu
- `refactor/<description>` - Cho tái cấu trúc mã

### Định dạng thông điệp commit

Tuân theo [Commit thông thường](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Ví dụ:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Định dạng tiêu đề
```
[ModuleXX] Brief description of change
```
hoặc
```
[Module08/samples/XX] Description for sample changes
```

### Quy tắc ứng xử

Tất cả người đóng góp phải tuân theo [Quy tắc ứng xử mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/). Vui lòng xem [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) trước khi đóng góp.

### Trước khi gửi

**Đối với thay đổi nội dung:**
- Xem trước tất cả các tệp Markdown đã sửa đổi
- Xác minh liên kết và hình ảnh hoạt động
- Kiểm tra lỗi chính tả và ngữ pháp

**Đối với thay đổi mã mẫu (Mô-đun08/mẫu/08):**
```bash
npm run lint
npm test
```

**Đối với thay đổi mẫu Python:**
- Kiểm thử mẫu chạy thành công
- Xác minh xử lý lỗi hoạt động
- Kiểm tra khả năng tương thích với Foundry Local

### Quy trình xem xét

- Thay đổi nội dung giáo dục được xem xét về độ chính xác và rõ ràng
- Mẫu mã được kiểm thử về chức năng
- Cập nhật dịch thuật được xử lý tự động bởi GitHub Actions

## Hệ thống dịch thuật

**QUAN TRỌNG:** Kho lưu trữ này sử dụng dịch tự động qua GitHub Actions.

- Các bản dịch nằm trong thư mục `/translations/` (50+ ngôn ngữ)
- Tự động qua quy trình `co-op-translator.yml`
- **KHÔNG chỉnh sửa thủ công các tệp dịch** - chúng sẽ bị ghi đè
- Chỉ chỉnh sửa các tệp nguồn tiếng Anh trong thư mục gốc và mô-đun
- Các bản dịch được tạo tự động khi đẩy lên nhánh `main`

## Tích hợp Foundry Local

Hầu hết các mẫu Mô-đun08 yêu cầu Microsoft Foundry Local đang chạy.

### Cài đặt & Thiết lập

**Cài đặt Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Cài đặt Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Khởi động Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Sử dụng SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Xác minh Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Biến môi trường cho các mẫu

Hầu hết các mẫu sử dụng các biến môi trường này:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Lưu ý**: Khi sử dụng `FoundryLocalManager`, SDK tự động xử lý khám phá dịch vụ và tải mô hình. Các bí danh mô hình (như `phi-3.5-mini`) đảm bảo biến thể tốt nhất được chọn cho phần cứng của bạn.

## Xây dựng và triển khai

### Triển khai nội dung

Kho lưu trữ này chủ yếu là tài liệu - không cần quy trình xây dựng cho nội dung.

### Xây dựng ứng dụng mẫu

**Ứng dụng Electron (Mô-đun08/mẫu/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Mẫu Python:**
Không có quy trình xây dựng - các mẫu được chạy trực tiếp với trình thông dịch Python.

## Các vấn đề thường gặp và cách khắc phục

> **Mẹo**: Kiểm tra [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) để biết các vấn đề và giải pháp đã biết.

### Vấn đề nghiêm trọng (Chặn)

#### Foundry Local không chạy
**Vấn đề:** Các mẫu không hoạt động với lỗi kết nối

**Giải pháp:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Vấn đề thường gặp (Trung bình)

#### Vấn đề môi trường ảo Python
**Vấn đề:** Lỗi nhập mô-đun

**Giải pháp:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Vấn đề xây dựng Electron
**Vấn đề:** npm install hoặc lỗi xây dựng

**Giải pháp:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Vấn đề quy trình làm việc (Nhẹ)

#### Xung đột quy trình dịch thuật
**Vấn đề:** PR dịch thuật xung đột với thay đổi của bạn

**Giải pháp:**
- Chỉ chỉnh sửa các tệp nguồn tiếng Anh
- Để quy trình dịch tự động xử lý các bản dịch
- Nếu xảy ra xung đột, hợp nhất `main` vào nhánh của bạn sau khi các bản dịch được hợp nhất

#### Lỗi tải xuống mô hình
**Vấn đề:** Foundry Local không tải được mô hình

**Giải pháp:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Tài nguyên bổ sung

### Lộ trình học tập
- **Lộ trình cơ bản:** Mô-đun 01-02 (7-9 giờ)
- **Lộ trình trung cấp:** Mô-đun 03-04 (9-11 giờ)
- **Lộ trình nâng cao:** Mô-đun 05-07 (12-15 giờ)
- **Lộ trình chuyên gia:** Mô-đun 08 (8-10 giờ)
- **Workshop thực hành:** Tài liệu workshop (6-8 giờ)

### Nội dung chính của mô-đun
- **Mô-đun01:** Các nguyên tắc cơ bản về EdgeAI và các nghiên cứu trường hợp thực tế
- **Mô-đun02:** Các họ và kiến trúc của Mô hình Ngôn ngữ Nhỏ (SLM)
- **Mô-đun03:** Chiến lược triển khai cục bộ và đám mây
- **Mô-đun04:** Tối ưu hóa mô hình với nhiều khung (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Mô-đun05:** SLMOps - vận hành sản xuất
- **Mô-đun06:** Tác nhân AI và gọi hàm
- **Mô-đun07:** Triển khai cụ thể theo nền tảng
- **Mô-đun08:** Bộ công cụ Foundry Local với 10 mẫu toàn diện

### Phụ thuộc bên ngoài
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime mô hình AI cục bộ với API tương thích OpenAI
  - [Tài liệu](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Khung tối ưu hóa
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Bộ công cụ tối ưu hóa mô hình
- [OpenVINO](https://docs.openvino.ai/) - Bộ công cụ tối ưu hóa của Intel

## Ghi chú cụ thể về dự án

### Ứng dụng mẫu Mô-đun08

Kho lưu trữ bao gồm 10 ứng dụng mẫu toàn diện:

1. **01-REST Chat Quickstart** - Tích hợp cơ bản OpenAI SDK
2. **02-OpenAI SDK Integration** - Các tính năng nâng cao của SDK
3. **03-Model Discovery & Benchmarking** - Công cụ so sánh mô hình
4. **04-Chainlit RAG Application** - Tạo nội dung dựa trên truy xuất
5. **05-Multi-Agent Orchestration** - Điều phối tác nhân cơ bản
6. **06-Models-as-Tools Router** - Định tuyến mô hình thông minh
7. **07-Direct API Client** - Tích hợp API cấp thấp
8. **08-Windows 11 Chat App** - Ứng dụng máy tính để bàn Electron gốc
9. **09-Advanced Multi-Agent System** - Điều phối tác nhân phức tạp
10. **10-Công cụ Framework Foundry** - Tích hợp LangChain/Semantic Kernel

### Ứng dụng mẫu trong Workshop

Workshop bao gồm 6 buổi học tiến bộ với các triển khai thực tế:

1. **Buổi 01** - Khởi động chat với tích hợp Foundry Local
2. **Buổi 02** - Quy trình RAG và đánh giá với RAGAS
3. **Buổi 03** - Đánh giá hiệu năng các mô hình mã nguồn mở
4. **Buổi 04** - So sánh và lựa chọn mô hình
5. **Buổi 05** - Hệ thống điều phối đa tác nhân
6. **Buổi 06** - Định tuyến mô hình và quản lý quy trình

Mỗi mẫu minh họa các khía cạnh khác nhau của phát triển AI biên với Foundry Local.

### Các yếu tố hiệu năng

- SLMs được tối ưu hóa cho triển khai biên (2-16GB RAM)
- Suy luận cục bộ cung cấp thời gian phản hồi từ 50-500ms
- Kỹ thuật lượng hóa giảm kích thước 75% với 85% hiệu năng được giữ lại
- Khả năng hội thoại thời gian thực với các mô hình cục bộ

### Bảo mật và quyền riêng tư

- Tất cả xử lý diễn ra cục bộ - không gửi dữ liệu lên đám mây
- Phù hợp cho các ứng dụng nhạy cảm về quyền riêng tư (y tế, tài chính)
- Đáp ứng yêu cầu về chủ quyền dữ liệu
- Foundry Local hoạt động hoàn toàn trên phần cứng cục bộ

## Hỗ trợ

### Tài liệu

- **README chính**: [README.md](README.md) - Tổng quan kho lưu trữ và lộ trình học tập
- **Hướng dẫn học tập**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Tài nguyên học tập và thời gian biểu
- **Hỗ trợ**: [SUPPORT.md](SUPPORT.md) - Cách nhận hỗ trợ
- **Bảo mật**: [SECURITY.md](SECURITY.md) - Báo cáo vấn đề bảo mật

### Hỗ trợ cộng đồng

- **GitHub Issues**: [Báo lỗi hoặc yêu cầu tính năng](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Đặt câu hỏi và chia sẻ ý tưởng](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Vấn đề Foundry Local**: [Vấn đề kỹ thuật với Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Liên hệ

- **Người duy trì**: Xem [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Vấn đề bảo mật**: Thực hiện báo cáo có trách nhiệm trong [SECURITY.md](SECURITY.md)
- **Hỗ trợ Microsoft**: Đối với hỗ trợ doanh nghiệp, liên hệ dịch vụ khách hàng Microsoft

### Tài nguyên bổ sung

- **Microsoft Learn**: [Lộ trình học AI và Machine Learning](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Tài liệu Foundry Local**: [Tài liệu chính thức](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Mẫu cộng đồng**: Xem [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) để tìm đóng góp từ cộng đồng

---

**Đây là kho lưu trữ giáo dục tập trung vào việc giảng dạy phát triển AI biên. Mô hình đóng góp chính là cải thiện nội dung giáo dục và thêm/nâng cấp các ứng dụng mẫu minh họa các khái niệm AI biên.**

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.