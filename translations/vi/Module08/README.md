# Module 08: Thực hành với Microsoft Foundry Local - Bộ công cụ hoàn chỉnh dành cho nhà phát triển

## Tổng quan

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) đại diện cho thế hệ tiếp theo của phát triển AI tại thiết bị, cung cấp cho các nhà phát triển các công cụ mạnh mẽ để xây dựng, triển khai và mở rộng ứng dụng AI tại chỗ, đồng thời duy trì tích hợp liền mạch với Azure AI Foundry. Module này cung cấp hướng dẫn toàn diện về Foundry Local từ cài đặt đến phát triển tác nhân nâng cao.

**Công nghệ chính:**
- Microsoft Foundry Local CLI và SDK
- Tích hợp Azure AI Foundry
- Suy luận mô hình trên thiết bị
- Bộ nhớ đệm và tối ưu hóa mô hình tại chỗ
- Kiến trúc dựa trên tác nhân

## Mục tiêu học tập

Khi hoàn thành module này, bạn sẽ:

- **Thành thạo Foundry Local**: Cài đặt, cấu hình và tối ưu hóa cho phát triển trên Windows 11
- **Triển khai nhiều mô hình**: Chạy các mô hình phi, qwen, deepseek và GPT tại chỗ bằng lệnh CLI
- **Xây dựng giải pháp sản xuất**: Tạo ứng dụng AI với kỹ thuật nhắc nâng cao và tích hợp dữ liệu
- **Tận dụng hệ sinh thái mã nguồn mở**: Tích hợp các mô hình Hugging Face và đóng góp từ cộng đồng
- **Phát triển tác nhân AI**: Xây dựng các tác nhân thông minh với khả năng định hướng và điều phối
- **Áp dụng các mẫu doanh nghiệp**: Tạo giải pháp AI mô-đun, có khả năng mở rộng để triển khai sản xuất

## Cấu trúc buổi học

### [1: Bắt đầu với Foundry Local](./01.FoundryLocalSetup.md)
**Trọng tâm**: Cài đặt, thiết lập CLI, triển khai mô hình và tối ưu hóa phần cứng

**Chủ đề chính**: Cài đặt hoàn chỉnh • Lệnh CLI • Bộ nhớ đệm mô hình • Tăng tốc phần cứng • Triển khai nhiều mô hình

**Mẫu**: [REST Chat Quickstart](./samples/01/README.md) • [Tích hợp OpenAI SDK](./samples/02/README.md) • [Khám phá & Đánh giá mô hình](./samples/03/README.md)

**Thời lượng**: 2-3 giờ | **Cấp độ**: Người mới bắt đầu

---

### [2: Xây dựng giải pháp AI với Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Trọng tâm**: Kỹ thuật nhắc nâng cao, tích hợp dữ liệu và kết nối đám mây

**Chủ đề chính**: Kỹ thuật nhắc • Tích hợp dữ liệu • Quy trình Azure • Tối ưu hóa hiệu suất • Giám sát

**Mẫu**: [Ứng dụng Chainlit RAG](./samples/04/README.md)

**Thời lượng**: 2-3 giờ | **Cấp độ**: Trung cấp

---

### [3: Mô hình mã nguồn mở với Foundry Local](./03.OpenSourceModels.md)
**Trọng tâm**: Tích hợp Hugging Face, chiến lược BYOM và mô hình cộng đồng

**Chủ đề chính**: Tích hợp HuggingFace • Mang mô hình của riêng bạn • Thông tin từ Model Mondays • Đóng góp cộng đồng • Lựa chọn mô hình

**Mẫu**: [Điều phối đa tác nhân](./samples/05/README.md)

**Thời lượng**: 2-3 giờ | **Cấp độ**: Trung cấp

---

### [4: Khám phá mô hình tiên tiến](./04.CuttingEdgeModels.md)
**Trọng tâm**: LLMs vs SLMs, triển khai EdgeAI và các bản demo nâng cao

**Chủ đề chính**: So sánh mô hình • Suy luận tại thiết bị vs đám mây • Phi + ONNX Runtime • Ứng dụng Chainlit RAG • Tối ưu hóa WebGPU

**Mẫu**: [Router Mô hình như Công cụ](./samples/06/README.md)

**Thời lượng**: 3-4 giờ | **Cấp độ**: Nâng cao

---

### [5: Xây dựng tác nhân AI nhanh chóng](./05.AIPoweredAgents.md)
**Trọng tâm**: Kiến trúc tác nhân, nhắc hệ thống, định hướng và điều phối

**Chủ đề chính**: Mẫu thiết kế tác nhân • Kỹ thuật nhắc hệ thống • Kỹ thuật định hướng • Hệ thống đa tác nhân • Triển khai sản xuất

**Mẫu**: [Điều phối đa tác nhân](./samples/05/README.md) • [Hệ thống đa tác nhân nâng cao](./samples/09/README.md)

**Thời lượng**: 3-4 giờ | **Cấp độ**: Nâng cao

---

### [6: Foundry Local - Mô hình như Công cụ](./06.ModelsAsTools.md)
**Trọng tâm**: Giải pháp AI mô-đun, mở rộng doanh nghiệp và mẫu sản xuất

**Chủ đề chính**: Mô hình như công cụ • Triển khai tại thiết bị • Tích hợp SDK/API • Kiến trúc doanh nghiệp • Chiến lược mở rộng

**Mẫu**: [Router Mô hình như Công cụ](./samples/06/README.md) • [Khung công cụ Foundry](./samples/10/README.md)

**Thời lượng**: 3-4 giờ | **Cấp độ**: Chuyên gia

---

### [7: Mẫu tích hợp API trực tiếp](./samples/07/README.md)
**Trọng tâm**: Tích hợp API REST thuần túy không phụ thuộc SDK để kiểm soát tối đa

**Chủ đề chính**: Triển khai HTTP client • Xác thực tùy chỉnh • Giám sát sức khỏe mô hình • Phản hồi streaming • Xử lý lỗi sản xuất

**Mẫu**: [API Client trực tiếp](./samples/07/README.md)

**Thời lượng**: 2-3 giờ | **Cấp độ**: Trung cấp

---

### [8: Ứng dụng chat gốc Windows 11](./samples/08/README.md)
**Trọng tâm**: Xây dựng ứng dụng chat gốc hiện đại với tích hợp Foundry Local

**Chủ đề chính**: Phát triển Electron • Hệ thống thiết kế Fluent • Tích hợp gốc Windows • Streaming thời gian thực • Thiết kế giao diện chat

**Mẫu**: [Ứng dụng chat Windows 11](./samples/08/README.md)

**Thời lượng**: 3-4 giờ | **Cấp độ**: Nâng cao

---

### [9: Điều phối đa tác nhân nâng cao](./samples/09/README.md)
**Trọng tâm**: Phối hợp tác nhân phức tạp, phân công nhiệm vụ chuyên biệt và quy trình làm việc AI hợp tác

**Chủ đề chính**: Phối hợp tác nhân thông minh • Mẫu gọi hàm • Giao tiếp giữa các tác nhân • Điều phối quy trình làm việc • Cơ chế đảm bảo chất lượng

**Mẫu**: [Hệ thống đa tác nhân nâng cao](./samples/09/README.md)

**Thời lượng**: 4-5 giờ | **Cấp độ**: Chuyên gia

---

### [10: Foundry Local như Khung công cụ](./samples/10/README.md)
**Trọng tâm**: Kiến trúc ưu tiên công cụ để tích hợp Foundry Local vào các ứng dụng và khung hiện có

**Chủ đề chính**: Tích hợp LangChain • Chức năng Semantic Kernel • Khung API REST • Công cụ CLI • Tích hợp Jupyter • Mẫu triển khai sản xuất

**Mẫu**: [Khung công cụ Foundry](./samples/10/README.md)

**Thời lượng**: 4-5 giờ | **Cấp độ**: Chuyên gia

## Yêu cầu trước

### Yêu cầu hệ thống
- **Hệ điều hành**: Windows 11 (22H2 hoặc mới hơn)
- **Bộ nhớ**: RAM 16GB (khuyến nghị 32GB cho các mô hình lớn hơn)
- **Dung lượng lưu trữ**: 50GB trống để lưu trữ mô hình
- **Phần cứng**: Thiết bị hỗ trợ NPU được khuyến nghị (Copilot+ PC), GPU tùy chọn
- **Mạng**: Internet tốc độ cao để tải mô hình ban đầu

### Môi trường phát triển
- Visual Studio Code với tiện ích mở rộng AI Toolkit
- Python 3.10+ và pip
- Git để kiểm soát phiên bản
- PowerShell hoặc Command Prompt
- Azure CLI (tùy chọn cho tích hợp đám mây)

### Kiến thức yêu cầu
- Hiểu cơ bản về các khái niệm AI/ML
- Quen thuộc với dòng lệnh
- Kiến thức cơ bản về lập trình Python
- Khái niệm REST API
- Kiến thức cơ bản về nhắc và suy luận mô hình

## Lộ trình module

**Thời gian ước tính tổng cộng**: 30-38 giờ

| Buổi học | Khu vực trọng tâm | Mẫu | Thời gian | Độ phức tạp |
|----------|-------------------|------|-----------|-------------|
|  1 | Cài đặt & Cơ bản | 01, 02, 03 | 2-3 giờ | Người mới bắt đầu |
|  2 | Giải pháp AI | 04 | 2-3 giờ | Trung cấp |
|  3 | Mã nguồn mở | 05 | 2-3 giờ | Trung cấp |
|  4 | Mô hình nâng cao | 06 | 3-4 giờ | Nâng cao |
|  5 | Tác nhân AI | 05, 09 | 3-4 giờ | Nâng cao |
|  6 | Công cụ doanh nghiệp | 06, 10 | 3-4 giờ | Chuyên gia |
|  7 | Tích hợp API trực tiếp | 07 | 2-3 giờ | Trung cấp |
|  8 | Ứng dụng chat Windows 11 | 08 | 3-4 giờ | Nâng cao |
|  9 | Điều phối đa tác nhân nâng cao | 09 | 4-5 giờ | Chuyên gia |
| 10 | Khung công cụ | 10 | 4-5 giờ | Chuyên gia |

## Tài nguyên chính

**Tài liệu chính thức:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Mã nguồn và mẫu chính thức
- [Tài liệu Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Hướng dẫn cài đặt và sử dụng đầy đủ
- [Series Model Mondays](https://aka.ms/model-mondays) - Điểm nổi bật và hướng dẫn mô hình hàng tuần

**Cộng đồng & Hỗ trợ:**
- [Thảo luận Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Hỏi đáp cộng đồng và yêu cầu tính năng
- [Cộng đồng nhà phát triển AI Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence) - Tin tức mới nhất và thực tiễn tốt nhất

## Kết quả học tập

Khi hoàn thành module này, bạn sẽ có khả năng:

### Thành thạo kỹ thuật
- **Triển khai và quản lý**: Cài đặt Foundry Local trên các môi trường phát triển và sản xuất
- **Tích hợp mô hình**: Làm việc liền mạch với các dòng mô hình đa dạng từ Microsoft, Hugging Face và nguồn cộng đồng
- **Xây dựng ứng dụng**: Tạo ứng dụng AI sẵn sàng sản xuất với các tính năng và tối ưu hóa nâng cao
- **Phát triển tác nhân**: Triển khai các tác nhân AI phức tạp với định hướng, lý luận và tích hợp công cụ

### Hiểu biết chiến lược
- **Quyết định kiến trúc**: Đưa ra lựa chọn thông minh giữa triển khai tại thiết bị và đám mây
- **Tối ưu hóa hiệu suất**: Tối ưu hóa hiệu suất suy luận trên các cấu hình phần cứng khác nhau
- **Mở rộng doanh nghiệp**: Thiết kế ứng dụng có khả năng mở rộng từ nguyên mẫu tại thiết bị đến triển khai doanh nghiệp
- **Bảo mật và quyền riêng tư**: Triển khai giải pháp AI bảo vệ quyền riêng tư với suy luận tại thiết bị

### Khả năng đổi mới
- **Tạo nguyên mẫu nhanh**: Nhanh chóng xây dựng và kiểm tra ý tưởng ứng dụng AI trên tất cả 10 mẫu
- **Tích hợp cộng đồng**: Tận dụng các mô hình mã nguồn mở và đóng góp vào hệ sinh thái
- **Mẫu nâng cao**: Triển khai các mẫu AI tiên tiến bao gồm RAG, tác nhân và tích hợp công cụ
- **Thành thạo khung công cụ**: Tích hợp chuyên sâu với LangChain, Semantic Kernel, Chainlit và Electron
- **Triển khai sản xuất**: Triển khai giải pháp AI có khả năng mở rộng từ nguyên mẫu tại thiết bị đến hệ thống doanh nghiệp
- **Phát triển sẵn sàng cho tương lai**: Xây dựng ứng dụng sẵn sàng cho các công nghệ và mẫu AI mới nổi

## Bắt đầu

1. **Thiết lập môi trường**: Đảm bảo Windows 11 với phần cứng được khuyến nghị (xem Yêu cầu trước)
2. **Cài đặt Foundry Local**: Làm theo Buổi học 1 để cài đặt và cấu hình hoàn chỉnh
3. **Chạy Mẫu 01**: Bắt đầu với tích hợp API REST cơ bản để xác minh thiết lập
4. **Tiến bộ qua các mẫu**: Hoàn thành các mẫu 01-10 để thành thạo toàn diện

## Chỉ số thành công

Theo dõi tiến trình của bạn qua tất cả 10 mẫu toàn diện:

### Cấp độ cơ bản (Mẫu 01-03)
- [ ] Cài đặt và cấu hình Foundry Local thành công
- [ ] Hoàn thành tích hợp API REST (Mẫu 01)
- [ ] Triển khai tương thích OpenAI SDK (Mẫu 02)
- [ ] Thực hiện khám phá và đánh giá mô hình (Mẫu 03)

### Cấp độ ứng dụng (Mẫu 04-06)
- [ ] Triển khai và chạy ít nhất 4 dòng mô hình khác nhau
- [ ] Xây dựng ứng dụng chat RAG hoạt động (Mẫu 04)
- [ ] Tạo hệ thống điều phối đa tác nhân (Mẫu 05)
- [ ] Triển khai định tuyến mô hình thông minh (Mẫu 06)

### Cấp độ tích hợp nâng cao (Mẫu 07-10)
- [ ] Xây dựng API client sẵn sàng sản xuất (Mẫu 07)
- [ ] Phát triển ứng dụng chat gốc Windows 11 (Mẫu 08)
- [ ] Triển khai hệ thống đa tác nhân nâng cao (Mẫu 09)
- [ ] Tạo khung công cụ toàn diện (Mẫu 10)

### Chỉ số thành thạo
- [ ] Chạy thành công tất cả 10 mẫu mà không gặp lỗi
- [ ] Tùy chỉnh ít nhất 3 mẫu cho các trường hợp sử dụng cụ thể
- [ ] Triển khai 2+ mẫu trong môi trường giống sản xuất
- [ ] Đóng góp cải tiến hoặc mở rộng mã mẫu
- [ ] Tích hợp các mẫu Foundry Local vào dự án cá nhân/chuyên nghiệp

## Hướng dẫn bắt đầu nhanh - Tất cả 10 mẫu

### Thiết lập môi trường (Yêu cầu cho tất cả mẫu)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Mẫu cơ bản (01-06)

**Mẫu 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Mẫu 02: Tích hợp OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Mẫu 03: Khám phá & Đánh giá mô hình**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Mẫu 04: Ứng dụng Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Mẫu 05: Điều phối đa tác nhân**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Mẫu 06: Router Mô hình như Công cụ**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Mẫu tích hợp nâng cao (07-10)

**Mẫu 07: API Client trực tiếp**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Mẫu 08: Ứng dụng chat Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Mẫu 09: Hệ thống đa tác nhân nâng cao**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Mẫu 10: Khung công cụ Foundry**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Xử lý sự cố thường gặp

**Lỗi kết nối Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Vấn đề tải mô hình**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Vấn đề phụ thuộc**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Tóm tắt
Module này đại diện cho bước tiến mới nhất trong phát triển AI biên, kết hợp các công cụ cấp doanh nghiệp của Microsoft với sự linh hoạt và sáng tạo của hệ sinh thái mã nguồn mở. Bằng cách nắm vững Foundry Local thông qua toàn bộ 10 mẫu chi tiết, bạn sẽ đứng ở vị trí tiên phong trong phát triển ứng dụng AI.

**Lộ trình học tập hoàn chỉnh:**
- **Nền tảng** (Mẫu 01-03): Tích hợp API và quản lý mô hình
- **Ứng dụng** (Mẫu 04-06): RAG, tác nhân, và định tuyến thông minh
- **Nâng cao** (Mẫu 07-10): Khung sản xuất và tích hợp doanh nghiệp

Đối với tích hợp Azure OpenAI (Phiên 2), hãy xem các tệp README của từng mẫu để biết các biến môi trường cần thiết và cài đặt phiên bản API.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.