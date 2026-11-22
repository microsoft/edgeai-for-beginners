# Hướng Dẫn Phát Triển AI Edge trên Windows

## Giới Thiệu

Chào mừng bạn đến với phát triển AI Edge trên Windows - hướng dẫn toàn diện về xây dựng các ứng dụng thông minh tận dụng sức mạnh AI trên thiết bị bằng nền tảng Windows AI Foundry của Microsoft. Hướng dẫn này được thiết kế dành riêng cho các nhà phát triển Windows muốn tích hợp các khả năng AI Edge hiện đại vào ứng dụng của họ đồng thời khai thác toàn bộ năng lực tăng tốc phần cứng Windows.

### Lợi Thế của Windows AI

Windows AI Foundry đại diện cho một nền tảng hợp nhất, đáng tin cậy và bảo mật hỗ trợ toàn bộ vòng đời phát triển AI - từ lựa chọn và tinh chỉnh mô hình đến tối ưu hóa và triển khai trên CPU, GPU, NPU và kiến trúc đám mây lai. Nền tảng này dân chủ hóa phát triển AI bằng cách cung cấp:

- **Trừu tượng phần cứng**: Triển khai liền mạch trên silicon AMD, Intel, NVIDIA và Qualcomm
- **Trí tuệ trên thiết bị**: AI bảo vệ quyền riêng tư chạy hoàn toàn trên phần cứng địa phương
- **Hiệu năng tối ưu**: Mô hình được tối ưu trước cho cấu hình phần cứng Windows
- **Sẵn sàng doanh nghiệp**: Tính năng bảo mật và tuân thủ đạt chuẩn sản xuất

### Windows ML 
Windows Machine Learning (ML) cho phép các nhà phát triển C#, C++, và Python chạy các mô hình AI ONNX cục bộ trên máy tính Windows thông qua ONNX Runtime, với quản lý tự động nhà cung cấp thực thi cho các phần cứng khác nhau (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) có thể được dùng với các mô hình từ PyTorch, Tensorflow/Keras, TFLite, scikit-learn và các framework khác.


![WindowsML A diagram illustrating an ONNX model going through Windows ML to then reach NPUs, GPUs, and CPUs.l](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML cung cấp một bản sao ONNX Runtime dùng chung trên toàn Windows, cộng với khả năng tải xuống động các nhà cung cấp thực thi (EP).

### Tại Sao Chọn Windows cho AI Edge?

**Hỗ Trợ Phần Cứng Toàn Diện**
Windows ML cung cấp tối ưu hóa phần cứng tự động trên toàn bộ hệ sinh thái Windows, đảm bảo các ứng dụng AI của bạn hoạt động tối ưu bất kể kiến trúc silicon nền tảng.

**Runtime AI Tích Hợp**
Bộ máy suy luận Windows ML tích hợp sẵn loại bỏ các yêu cầu cài đặt phức tạp, cho phép nhà phát triển tập trung vào logic ứng dụng thay vì lo lắng về hạ tầng.

**Tối ưu hoá PC Copilot+**
API được thiết kế đặc thù cho các thiết bị Windows thế hệ tiếp theo với Bộ Xử lý Thần Kinh (NPU) chuyên dụng mang lại hiệu suất xuất sắc trên mỗi watt điện năng.

**Hệ Sinh Thái Phát Triển**
Bộ công cụ đa dạng, bao gồm tích hợp Visual Studio, tài liệu toàn diện, và các ứng dụng mẫu giúp tăng tốc chu trình phát triển.

## Mục Tiêu Học Tập

Bằng việc hoàn thành hướng dẫn phát triển AI Edge trên Windows này, bạn sẽ làm chủ các kỹ năng thiết yếu để xây dựng các ứng dụng AI sẵn sàng sản xuất trên nền tảng Windows.

### Những Năng Lực Kỹ Thuật Cốt Lõi

**Thành Thạo Windows AI Foundry**
- Hiểu kiến trúc và các thành phần của nền tảng Windows AI Foundry
- Điều hướng toàn bộ vòng đời phát triển AI trong hệ sinh thái Windows
- Áp dụng các thực tiễn bảo mật tốt nhất cho ứng dụng AI trên thiết bị
- Tối ưu ứng dụng cho các cấu hình phần cứng Windows khác nhau

**Chuyên Môn Tích Hợp API**
- Thành thạo các API Windows AI cho văn bản, thị giác và ứng dụng đa phương thức
- Triển khai tích hợp mô hình ngôn ngữ Phi Silica cho tạo văn bản và suy luận
- Triển khai khả năng thị giác máy tính sử dụng API xử lý hình ảnh tích hợp sẵn
- Tùy chỉnh các mô hình đã huấn luyện trước bằng kỹ thuật LoRA (Low-Rank Adaptation)

**Triển Khai Foundry Local**
- Truy cập, đánh giá và triển khai các mô hình ngôn ngữ mã nguồn mở bằng CLI Foundry Local
- Hiểu về tối ưu hóa mô hình và lượng tử hóa để triển khai cục bộ
- Triển khai các khả năng AI ngoại tuyến hoạt động mà không cần kết nối internet
- Quản lý vòng đời và cập nhật mô hình trong môi trường sản xuất

**Triển Khai Windows ML**
- Mang mô hình ONNX tùy chỉnh tới các ứng dụng Windows bằng Windows ML
- Tận dụng khả năng tăng tốc phần cứng tự động trên CPU, GPU, và NPU
- Triển khai suy luận thời gian thực với tối ưu hóa sử dụng tài nguyên
- Thiết kế các ứng dụng AI có thể mở rộng cho nhiều loại thiết bị Windows

### Kỹ Năng Phát Triển Ứng Dụng

**Phát Triển Windows Đa Nền Tảng**
- Xây dựng ứng dụng chạy AI sử dụng .NET MAUI cho triển khai Windows toàn diện
- Tích hợp khả năng AI vào Win32, UWP, và Ứng dụng Web Tiến Bộ (Progressive Web Apps)
- Thiết kế UI đáp ứng tương thích với trạng thái xử lý AI
- Xử lý các thao tác AI bất đồng bộ với các mẫu trải nghiệm người dùng phù hợp

**Tối Ưu Hiệu Năng**
- Phân tích và tối ưu hiệu năng suy luận AI trên các cấu hình phần cứng khác nhau
- Thực hiện quản lý bộ nhớ hiệu quả cho các mô hình ngôn ngữ lớn
- Thiết kế ứng dụng có khả năng giảm dần hiệu năng một cách mượt mà dựa trên khả năng phần cứng sẵn có
- Áp dụng chiến lược lưu bộ đệm cho các thao tác AI thường dùng

**Sẵn Sàng Sản Xuất**
- Triển khai xử lý lỗi toàn diện và các cơ chế dự phòng
- Thiết kế hệ thống thu thập số liệu và giám sát hiệu năng ứng dụng AI
- Áp dụng các thực tiễn bảo mật tốt nhất cho lưu trữ mô hình AI và thực thi cục bộ
- Lập kế hoạch chiến lược triển khai cho ứng dụng doanh nghiệp và người tiêu dùng

### Hiểu Biết Kinh Doanh và Chiến Lược

**Kiến Trúc Ứng Dụng AI**
- Thiết kế kiến trúc lai tối ưu hóa giữa xử lý AI cục bộ và đám mây
- Đánh giá sự đánh đổi giữa kích thước mô hình, độ chính xác và tốc độ suy luận
- Lập kế hoạch kiến trúc luồng dữ liệu giữ gìn quyền riêng tư đồng thời kích hoạt trí tuệ
- Triển khai các giải pháp AI chi phí-hiệu quả có thể mở rộng theo nhu cầu người dùng

**Định Vị Thị Trường**
- Hiểu các lợi thế cạnh tranh của ứng dụng AI bản địa Windows
- Xác định các trường hợp sử dụng mà AI trên thiết bị mang lại trải nghiệm người dùng vượt trội
- Phát triển chiến lược ra thị trường cho ứng dụng Windows được tăng cường AI
- Định vị ứng dụng để tận dụng các lợi ích của hệ sinh thái Windows

## Các Mẫu AI Windows App SDK

Windows App SDK cung cấp các mẫu toàn diện minh họa tích hợp AI trên nhiều framework và kịch bản triển khai khác nhau. Các mẫu này là tài liệu tham khảo thiết yếu để hiểu các mô hình phát triển Windows AI.

### Mẫu Windows AI Foundry

| Mẫu | Framework | Lĩnh Vực Tập Trung | Tính Năng Chính |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Tích Hợp API Windows AI | Ứng dụng WinUI hoàn chỉnh minh họa API Windows AI, tối ưu ARM64, triển khai đóng gói |

**Công Nghệ Chính:**
- API Windows AI
- Framework WinUI 3
- Tối ưu nền tảng ARM64
- Tương thích PC Copilot+
- Triển khai ứng dụng đóng gói

**Yêu Cầu Trước:**
- Windows 11 với PC Copilot+ được khuyến nghị
- Visual Studio 2022
- Cấu hình xây dựng ARM64
- Windows App SDK 1.8.1+

### Mẫu Windows ML

#### Mẫu C++

| Mẫu | Loại | Lĩnh Vực Tập Trung | Tính Năng Chính |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Ứng dụng Console | Windows ML Cơ Bản | Phát hiện EP, tùy chọn dòng lệnh, biên dịch mô hình |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Ứng dụng Console | Triển khai phụ thuộc Framework | Runtime dùng chung, kích thước triển khai nhỏ hơn |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Ứng dụng Console | Triển khai độc lập | Triển khai độc lập, không phụ thuộc runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Sử Dụng Thư Viện | WindowsML trong thư viện dùng chung, quản lý bộ nhớ |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Hướng dẫn ResNet | Chuyển đổi mô hình, biên dịch EP, hướng dẫn Build 2025 |

#### Mẫu C#

**Ứng Dụng Console**

| Mẫu | Loại | Lĩnh Vực Tập Trung | Tính Năng Chính |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Ứng dụng Console | Tích hợp C# Cơ Bản | Sử dụng trợ giúp dùng chung, giao diện dòng lệnh |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Hướng dẫn ResNet | Chuyển đổi mô hình, biên dịch EP, hướng dẫn Build 2025 |

**Ứng Dụng GUI**

| Mẫu | Framework | Lĩnh Vực Tập Trung | Tính Năng Chính |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI Máy tính để bàn | Phân loại hình ảnh với giao diện WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI truyền thống | Phân loại hình ảnh với Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI Hiện đại | Phân loại hình ảnh với giao diện WinUI 3 |

#### Mẫu Python

| Mẫu | Ngôn Ngữ | Lĩnh Vực Tập Trung | Tính Năng Chính |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Phân loại hình ảnh | Ràng buộc WinML Python, xử lý ảnh theo lô |

### Yêu Cầu Trước Mẫu

**Yêu cầu hệ thống:**
- Máy tính Windows 11 chạy phiên bản 24H2 (build 26100) trở lên
- Visual Studio 2022 với workloads C++ và .NET
- Windows App SDK 1.8.1 trở lên
- Python 3.10-3.13 cho mẫu Python trên thiết bị x64 và ARM64

**Đối với Windows AI Foundry:**
- PC Copilot+ được khuyến nghị để có hiệu năng tối ưu
- Cấu hình xây dựng ARM64 cho mẫu Windows AI
- Yêu cầu định danh gói (ứng dụng không đóng gói không còn được hỗ trợ)

### Quy Trình Mẫu Thông Dụng

Hầu hết các mẫu Windows ML tuân theo mô hình tiêu chuẩn này:

1. **Khởi tạo môi trường** - Tạo môi trường ONNX Runtime
2. **Đăng ký nhà cung cấp thực thi** - Phát hiện và đăng ký các bộ tăng tốc phần cứng sẵn có (CPU, GPU, NPU)
3. **Tải Mô Hình** - Tải mô hình ONNX, tùy chọn biên dịch cho phần cứng mục tiêu
4. **Tiền xử lý đầu vào** - Chuyển đổi ảnh/dữ liệu về định dạng đầu vào mô hình
5. **Chạy suy luận** - Thực thi mô hình và lấy dự đoán
6. **Xử lý kết quả** - Áp dụng softmax và hiển thị các dự đoán hàng đầu

### Các Tệp Mô Hình Được Dùng

| Mô Hình | Mục Đích | Bao Gồm | Ghi Chú |
|-------|---------|----------|-------|
| SqueezeNet | Phân loại hình ảnh nhẹ | ✅ Bao gồm | Đã huấn luyện sẵn, sẵn dùng |
| ResNet-50 | Phân loại hình ảnh độ chính xác cao | ❌ Yêu cầu chuyển đổi | Dùng [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) để chuyển đổi |

### Hỗ Trợ Phần Cứng

Tất cả các mẫu tự động phát hiện và sử dụng phần cứng khả dụng:
- **CPU** - Hỗ trợ phổ quát trên mọi thiết bị Windows
- **GPU** - Phát hiện tự động và tối ưu hóa cho phần cứng đồ họa khả dụng
- **NPU** - Tận dụng Bộ Xử lý Thần Kinh trên các thiết bị hỗ trợ (PC Copilot+)

## Các Thành Phần Nền Tảng Windows AI Foundry

### 1. API Windows AI

API Windows AI cung cấp các khả năng AI sẵn dùng được vận hành bởi các mô hình trên thiết bị, tối ưu cho hiệu quả và hiệu năng trên các thiết bị PC Copilot+ với yêu cầu thiết lập tối thiểu.

#### Các Danh Mục API Chính

**Mô Hình Ngôn Ngữ Phi Silica**
- Mô hình ngôn ngữ nhỏ nhưng mạnh mẽ cho tạo văn bản và suy luận
- Tối ưu cho suy luận thời gian thực với mức tiêu thụ năng lượng tối thiểu
- Hỗ trợ tinh chỉnh tùy chỉnh bằng kỹ thuật LoRA
- Tích hợp với tìm kiếm ngữ nghĩa và truy xuất kiến thức trong Windows

**API Thị Giác Máy Tính**
- **Nhận dạng văn bản (OCR)**: Trích xuất văn bản từ hình ảnh với độ chính xác cao
- **Siêu phân giải hình ảnh**: Phóng to hình ảnh bằng mô hình AI cục bộ
- **Phân vùng hình ảnh**: Xác định và tách riêng các đối tượng cụ thể trong hình ảnh
- **Mô tả hình ảnh**: Tạo mô tả văn bản chi tiết cho nội dung hình ảnh
- **Xóa đối tượng**: Loại bỏ các đối tượng không mong muốn khỏi hình ảnh bằng kỹ thuật tô lại AI

**Khả Năng Đa Phương Thức**
- **Tích hợp Thị giác và Ngôn ngữ**: Kết hợp hiểu biết văn bản và hình ảnh
- **Tìm kiếm Ngữ nghĩa**: Hỗ trợ truy vấn ngôn ngữ tự nhiên trên nội dung đa phương tiện
- **Truy xuất Kiến thức**: Xây dựng trải nghiệm tìm kiếm thông minh với dữ liệu cục bộ

### 2. Foundry Local

Foundry Local cung cấp cho nhà phát triển quyền truy cập nhanh đến các mô hình ngôn ngữ mã nguồn mở sẵn dùng trên Silicon Windows, với khả năng duyệt, thử nghiệm, tương tác và triển khai mô hình trong ứng dụng cục bộ.

#### Ứng Dụng Mẫu Foundry Local

Kho [Foundry Local repository](https://github.com/microsoft/Foundry-Local/tree/main/samples) cung cấp các mẫu toàn diện trên nhiều ngôn ngữ lập trình và framework, minh họa các mẫu tích hợp và các trường hợp sử dụng đa dạng.

| Mẫu | Ngôn Ngữ/Framework | Lĩnh Vực Tập Trung | Tính Năng Chính |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Triển khai RAG | Tích hợp Semantic Kernel, lưu trữ vector Qdrant, nhúng JINA, xử lý tài liệu, trò chuyện streaming |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Ứng dụng Chat trên máy tính để bàn | Chat đa nền tảng, chuyển đổi mô hình cục bộ/đám mây, tích hợp SDK OpenAI, streaming real-time |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Tích hợp Cơ Bản | Sử dụng SDK đơn giản, khởi tạo mô hình, chức năng trò chuyện cơ bản |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Tích hợp Cơ Bản | Sử dụng SDK Python, phản hồi streaming, API tương thích OpenAI |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Tích hợp hệ thống | Sử dụng SDK cấp thấp, thao tác bất đồng bộ, client HTTP reqwest |

#### Các danh mục mẫu theo trường hợp sử dụng

**RAG (Tạo sinh được tăng cường truy xuất)**
- **dotNET/rag**: Triển khai RAG hoàn chỉnh sử dụng Semantic Kernel, cơ sở dữ liệu vector Qdrant và embeddings JINA
- **Kiến trúc**: Nhập tài liệu → Chia nhỏ văn bản → Embeddings vector → Tìm kiếm tương tự → Phản hồi theo ngữ cảnh
- **Công nghệ**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, hoàn thành trò chuyện theo luồng

**Ứng dụng trên máy tính để bàn**
- **electron/foundry-chat**: Ứng dụng chat sẵn sàng sản xuất với chuyển đổi mô hình cục bộ/đám mây
- **Tính năng**: Bộ chọn mô hình, phản hồi luồng, xử lý lỗi, triển khai đa nền tảng
- **Kiến trúc**: Quá trình chính Electron, giao tiếp IPC, script preload an toàn

**Ví dụ tích hợp SDK**
- **JavaScript (Node.js)**: Tương tác mô hình cơ bản và phản hồi theo luồng
- **Python**: Sử dụng API tương thích OpenAI với luồng bất đồng bộ
- **Rust**: Tích hợp cấp thấp với reqwest và tokio cho thao tác bất đồng bộ

#### Yêu cầu tiên quyết cho các mẫu Foundry Local

**Yêu cầu hệ thống:**
- Windows 11 đã cài đặt Foundry Local
- Node.js v16+ cho mẫu JavaScript/Electron
- .NET 8.0+ cho mẫu C#
- Python 3.10+ cho mẫu Python
- Rust 1.70+ cho mẫu Rust

**Cài đặt:**
```powershell
# Cài đặt Foundry Local
winget install Microsoft.FoundryLocal

# Xác minh cài đặt
foundry --version
foundry model list
```

#### Thiết lập đặc thù cho từng mẫu

**Mẫu RAG dotNET:**
```powershell
# Cài đặt các gói cần thiết qua NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Khởi động cơ sở dữ liệu vector Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Chạy sổ tay Jupyter
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Mẫu chat Electron:**
```powershell
# Đặt biến môi trường cho dự phòng đám mây
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Cài đặt các phụ thuộc và chạy
npm install
npm start
```

**Mẫu JavaScript/Python/Rust:**
```powershell
# Tải xuống mô hình (ví dụ với phi-3.5-mini)
foundry model run phi-3.5-mini

# Chạy mẫu tương ứng
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Tính năng chính

**Danh mục mô hình**
- Bộ sưu tập toàn diện các mô hình mã nguồn mở đã tối ưu sẵn
- Mô hình tối ưu trên CPU, GPU và NPU để triển khai ngay lập tức
- Hỗ trợ các họ mô hình phổ biến bao gồm Llama, Mistral, Phi, và các mô hình chuyên ngành

**Tích hợp CLI**
- Giao diện dòng lệnh để quản lý và triển khai mô hình
- Quy trình tự động tối ưu hóa và lượng tử hóa
- Tích hợp với môi trường phát triển phổ biến và pipeline CI/CD

**Triển khai cục bộ**
- Hoạt động hoàn toàn ngoại tuyến không phụ thuộc đám mây
- Hỗ trợ định dạng và cấu hình mô hình tùy chỉnh
- Phục vụ mô hình hiệu quả với tối ưu phần cứng tự động

### 3. Windows ML

Windows ML là nền tảng AI cốt lõi và runtime suy diễn tích hợp trên Windows, cho phép nhà phát triển triển khai mô hình tùy chỉnh hiệu quả trên toàn bộ hệ sinh thái phần cứng Windows rộng lớn.

#### Lợi ích kiến trúc

**Hỗ trợ phần cứng toàn cầu**
- Tối ưu hóa tự động cho silicon AMD, Intel, NVIDIA và Qualcomm
- Hỗ trợ thực thi trên CPU, GPU và NPU với chuyển đổi minh bạch
- Trừu tượng phần cứng loại bỏ công việc tối ưu hóa riêng theo nền tảng

**Tính linh hoạt mô hình**
- Hỗ trợ định dạng mô hình ONNX với chuyển đổi tự động từ các framework phổ biến
- Triển khai mô hình tùy chỉnh với hiệu suất cấp sản xuất
- Tích hợp với kiến trúc ứng dụng Windows hiện có

**Tích hợp doanh nghiệp**
- Tương thích với các framework bảo mật và tuân thủ của Windows
- Hỗ trợ công cụ triển khai và quản lý doanh nghiệp
- Tích hợp hệ thống quản lý và giám sát thiết bị Windows

## Quy trình phát triển

### Giai đoạn 1: Thiết lập môi trường và cấu hình công cụ

**Chuẩn bị môi trường phát triển**
1. Cài đặt Visual Studio 2022 với workload C++ và .NET
2. Cài đặt Windows App SDK 1.8.1 hoặc mới hơn
3. Cấu hình công cụ CLI Windows AI Foundry
4. Thiết lập tiện ích mở rộng AI Toolkit cho Visual Studio Code
5. Thiết lập công cụ profiling và giám sát hiệu năng
6. Đảm bảo cấu hình build ARM64 để tối ưu hóa PC Copilot+

**Thiết lập kho mẫu**
1. Clone kho [Windows App SDK Samples repository](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Điều hướng tới `Samples/WindowsAIFoundry/cs-winui` để ví dụ API Windows AI
3. Điều hướng tới `Samples/WindowsML` cho ví dụ Windows ML toàn diện
4. Xem [yêu cầu build](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) cho nền tảng mục tiêu của bạn

**Khám phá AI Dev Gallery**
- Khám phá các ứng dụng mẫu và cài đặt tham khảo
- Thử nghiệm API Windows AI với các minh họa tương tác
- Xem xét mã nguồn cho thực hành và mẫu tốt nhất
- Xác định mẫu phù hợp với trường hợp sử dụng của bạn

### Giai đoạn 2: Lựa chọn và tích hợp mô hình

**Phân tích yêu cầu**
- Xác định yêu cầu chức năng cho khả năng AI
- Thiết lập giới hạn hiệu suất và mục tiêu tối ưu
- Đánh giá yêu cầu bảo mật và riêng tư
- Lập kế hoạch kiến trúc triển khai và chiến lược mở rộng

**Đánh giá mô hình**
- Dùng Foundry Local để thử nghiệm mô hình mã nguồn mở cho trường hợp của bạn
- Đo hiệu năng API Windows AI với yêu cầu mô hình tùy chỉnh
- Đánh giá sự đánh đổi giữa kích thước mô hình, độ chính xác và tốc độ suy diễn
- Prototype các cách tiếp cận tích hợp với mô hình đã chọn

### Giai đoạn 3: Phát triển ứng dụng

**Tích hợp lõi**
- Thực hiện tích hợp API Windows AI với xử lý lỗi phù hợp
- Thiết kế giao diện người dùng phù hợp với quy trình xử lý AI
- Triển khai các chiến lược cache và tối ưu cho suy diễn mô hình
- Thêm theo dõi và giám sát hiệu năng vận hành AI

**Kiểm thử và xác nhận**
- Kiểm thử ứng dụng trên nhiều cấu hình phần cứng Windows khác nhau
- Xác nhận các chỉ số hiệu năng dưới các điều kiện tải khác nhau
- Triển khai kiểm thử tự động cho độ tin cậy chức năng AI
- Tiến hành kiểm thử trải nghiệm người dùng với tính năng AI nâng cao

### Giai đoạn 4: Tối ưu và triển khai

**Tối ưu hiệu suất**
- Phân tích hiệu suất ứng dụng trên cấu hình phần cứng mục tiêu
- Tối ưu hóa sử dụng bộ nhớ và chiến lược tải mô hình
- Triển khai hành vi thích ứng dựa trên khả năng phần cứng sẵn có
- Tinh chỉnh trải nghiệm người dùng cho các kịch bản hiệu suất khác nhau

**Triển khai sản xuất**
- Đóng gói ứng dụng với các phụ thuộc mô hình AI phù hợp
- Triển khai cơ chế cập nhật cho mô hình và logic ứng dụng
- Cấu hình giám sát và phân tích cho môi trường sản xuất
- Lập kế hoạch chiến lược rollout cho triển khai doanh nghiệp và người tiêu dùng

## Ví dụ thực tiễn triển khai

### Ví dụ 1: Ứng dụng xử lý tài liệu thông minh

Xây dựng ứng dụng Windows xử lý tài liệu với nhiều khả năng AI:

**Công nghệ sử dụng:**
- Phi Silica cho tóm tắt tài liệu và trả lời câu hỏi
- API OCR cho trích xuất văn bản từ tài liệu quét
- API mô tả hình ảnh cho phân tích biểu đồ và sơ đồ
- Mô hình ONNX tùy chỉnh cho phân loại tài liệu

**Cách tiếp cận triển khai:**
- Thiết kế kiến trúc mô-đun với thành phần AI có thể cắm được
- Triển khai xử lý bất đồng bộ cho lô tài liệu lớn
- Thêm chỉ báo tiến trình và hỗ trợ hủy cho thao tác dài
- Bao gồm khả năng offline cho xử lý tài liệu nhạy cảm

### Ví dụ 2: Hệ thống quản lý tồn kho bán lẻ

Tạo hệ thống tồn kho AI cho ứng dụng bán lẻ:

**Công nghệ sử dụng:**
- Phân đoạn hình ảnh để nhận dạng sản phẩm
- Mô hình thị giác tùy chỉnh cho phân loại thương hiệu và danh mục
- Triển khai Foundry Local các mô hình ngôn ngữ bán lẻ chuyên ngành
- Tích hợp với hệ thống POS và tồn kho hiện có

**Cách tiếp cận triển khai:**
- Xây dựng tích hợp camera cho quét sản phẩm thời gian thực
- Triển khai nhận dạng mã vạch và sản phẩm bằng hình ảnh
- Thêm truy vấn tồn kho bằng ngôn ngữ tự nhiên sử dụng mô hình ngôn ngữ cục bộ
- Thiết kế kiến trúc mở rộng cho nhiều cửa hàng

### Ví dụ 3: Trợ lý tài liệu y tế

Phát triển công cụ tài liệu y tế bảo vệ quyền riêng tư:

**Công nghệ sử dụng:**
- Phi Silica cho tạo ghi chú y tế và hỗ trợ quyết định lâm sàng
- OCR để số hóa hồ sơ y tế viết tay
- Mô hình ngôn ngữ y tế tùy chỉnh triển khai qua Windows ML
- Lưu trữ vector cục bộ cho truy xuất kiến thức y tế

**Cách tiếp cận triển khai:**
- Đảm bảo hoạt động hoàn toàn offline để bảo vệ quyền riêng tư bệnh nhân
- Thực hiện kiểm tra và gợi ý thuật ngữ y tế
- Thêm ghi lại kiểm toán cho tuân thủ quy định
- Thiết kế tích hợp với hệ thống Hồ sơ Sức khỏe Điện tử hiện có

## Chiến lược tối ưu hiệu suất

### Phát triển nhận biết phần cứng

**Tối ưu NPU**
- Thiết kế ứng dụng tận dụng khả năng NPU trên PC Copilot+
- Triển khai fallback mềm mại sang GPU/CPU trên thiết bị không có NPU
- Tối ưu định dạng mô hình cho tăng tốc đặc thù NPU
- Giám sát sử dụng NPU và đặc tính nhiệt độ

**Quản lý bộ nhớ**
- Triển khai chiến lược tải và cache mô hình hiệu quả
- Sử dụng memory mapping cho mô hình lớn giảm thời gian khởi động
- Thiết kế ứng dụng tiết kiệm bộ nhớ cho thiết bị hạn chế tài nguyên
- Triển khai lượng tử hóa mô hình để tối ưu bộ nhớ

**Hiệu quả pin**
- Tối ưu hoạt động AI để tiêu thụ năng lượng tối thiểu
- Triển khai xử lý thích ứng dựa trên trạng thái pin
- Thiết kế xử lý nền hiệu quả cho hoạt động AI liên tục
- Sử dụng công cụ profiling năng lượng để tối ưu hóa sử dụng điện

### Xem xét khả năng mở rộng

**Đa luồng**
- Thiết kế hoạt động AI an toàn luồng cho xử lý đồng thời
- Triển khai phân phối công việc hiệu quả trên các lõi có sẵn
- Sử dụng mẫu async/await cho hoạt động AI không khóa
- Lập kế hoạch tối ưu pool luồng cho các cấu hình phần cứng khác nhau

**Chiến lược cache**
- Triển khai cache thông minh cho hoạt động AI thường dùng
- Thiết kế chiến lược xóa cache cho cập nhật mô hình
- Sử dụng cache bền vững cho các bước tiền xử lý tốn kém
- Triển khai cache phân phối cho kịch bản đa người dùng

## Thực hành bảo mật và riêng tư tốt nhất

### Bảo vệ dữ liệu

**Xử lý cục bộ**
- Đảm bảo dữ liệu nhạy cảm không bao giờ rời thiết bị cục bộ
- Triển khai lưu trữ an toàn cho mô hình AI và dữ liệu tạm thời
- Sử dụng tính năng bảo mật Windows cho sandboxing ứng dụng
- Áp dụng mã hóa cho mô hình lưu trữ và kết quả xử lý trung gian

**Bảo mật mô hình**
- Xác thực tính toàn vẹn mô hình trước tải và thực thi
- Triển khai cơ chế cập nhật mô hình an toàn
- Sử dụng mô hình ký để ngăn chặn thay đổi trái phép
- Áp dụng kiểm soát truy cập cho tập tin và cấu hình mô hình

### Các cân nhắc tuân thủ

**Phù hợp quy định**
- Thiết kế ứng dụng đáp ứng GDPR, HIPAA và các yêu cầu quy định khác
- Triển khai ghi log kiểm toán cho quy trình ra quyết định AI
- Cung cấp tính năng minh bạch cho kết quả tạo bởi AI
- Cho phép người dùng kiểm soát xử lý dữ liệu AI

**Bảo mật doanh nghiệp**
- Tích hợp với chính sách bảo mật doanh nghiệp Windows
- Hỗ trợ triển khai quản lý qua công cụ doanh nghiệp
- Triển khai kiểm soát truy cập dựa trên vai trò cho tính năng AI
- Cung cấp điều khiển quản trị cho chức năng AI

## Khắc phục sự cố và gỡ lỗi

### Thách thức phát triển phổ biến

**Vấn đề cấu hình build**
- Đảm bảo cấu hình nền tảng ARM64 cho mẫu API Windows AI
- Kiểm tra tương thích phiên bản Windows App SDK (yêu cầu 1.8.1+)
- Kiểm tra cấu hình danh tính package đúng (bắt buộc cho API Windows AI)
- Xác thực công cụ build hỗ trợ phiên bản framework mục tiêu

**Vấn đề tải mô hình**
- Xác thực tương thích mô hình ONNX với Windows ML
- Kiểm tra tính toàn vẹn tập tin mô hình và tiêu chuẩn định dạng
- Kiểm tra yêu cầu khả năng phần cứng cho mô hình cụ thể
- Gỡ lỗi các vấn đề phân bổ bộ nhớ trong quá trình tải mô hình
- Đảm bảo đăng ký nhà cung cấp thực thi cho tăng tốc phần cứng

**Cân nhắc chế độ triển khai**
- **Chế độ tự chứa**: Hỗ trợ đầy đủ với kích thước triển khai lớn hơn
- **Chế độ phụ thuộc framework**: Kích thước nhỏ hơn nhưng yêu cầu runtime chia sẻ
- **Ứng dụng chưa đóng gói**: Không còn hỗ trợ cho API Windows AI
- Sử dụng `dotnet run -p:Platform=ARM64 -p:SelfContained=true` để triển khai ARM64 tự chứa

**Vấn đề hiệu suất**
- Phân tích hiệu suất ứng dụng trên các cấu hình phần cứng khác nhau
- Xác định điểm nghẽn trong pipeline xử lý AI
- Tối ưu hóa tiền xử lý và hậu xử lý dữ liệu
- Triển khai giám sát hiệu suất và cảnh báo

**Khó khăn tích hợp**
- Gỡ lỗi vấn đề tích hợp API với xử lý lỗi phù hợp
- Xác thực định dạng dữ liệu đầu vào và yêu cầu tiền xử lý
- Kiểm thử kỹ các trường hợp đặc biệt và điều kiện lỗi
- Triển khai ghi log toàn diện để gỡ lỗi sự cố sản xuất

### Công cụ và kỹ thuật gỡ lỗi

**Tích hợp Visual Studio**
- Sử dụng trình gỡ lỗi AI Toolkit để phân tích thực thi mô hình
- Thực hiện profiling hiệu năng cho hoạt động AI
- Gỡ lỗi hoạt động AI bất đồng bộ với xử lý ngoại lệ phù hợp
- Sử dụng công cụ profiling bộ nhớ để tối ưu hóa

**Công cụ Windows AI Foundry**
- Tận dụng CLI Foundry Local để test và xác thực mô hình
- Sử dụng công cụ kiểm tra API Windows AI để xác minh tích hợp
- Triển khai ghi log tùy chỉnh cho giám sát hoạt động AI
- Tạo kiểm thử tự động cho độ tin cậy chức năng AI

## Bảo đảm tương lai cho ứng dụng của bạn

### Công nghệ mới nổi

**Phần cứng thế hệ tiếp theo**
- Thiết kế ứng dụng để tận dụng khả năng NPU trong tương lai
- Lập kế hoạch cho kích thước và độ phức tạp mô hình tăng
- Triển khai kiến trúc thích ứng cho phần cứng phát triển
- Xem xét thuật toán sẵn sàng lượng tử cho tương thích tương lai

**Khả năng AI nâng cao**
- Chuẩn bị tích hợp AI đa phương thức trên nhiều loại dữ liệu hơn
- Lập kế hoạch AI hợp tác thời gian thực giữa nhiều thiết bị
- Thiết kế cho khả năng học liên kết phân tán (federated learning)
- Xem xét kiến trúc trí tuệ lai edge-cloud

### Học tập và thích ứng liên tục

**Cập nhật mô hình**
- Triển khai cơ chế cập nhật mô hình liền mạch
- Thiết kế ứng dụng thích nghi với khả năng mô hình cải tiến
- Lập kế hoạch tương thích ngược với mô hình hiện có
- Triển khai thử nghiệm A/B cho đánh giá hiệu suất mô hình

**Tiến hóa tính năng**
- Thiết kế kiến trúc mô-đun để tích hợp khả năng AI mới
- Lập kế hoạch cho tích hợp API Windows AI mới nổi
- Triển khai cờ tính năng cho rollout năng lực từng bước
- Thiết kế giao diện người dùng thích ứng với tính năng AI nâng cao

## Kết luận

Phát triển Windows Edge AI đại diện cho sự hội tụ của khả năng AI mạnh mẽ với nền tảng Windows chắc chắn, an toàn và có khả năng mở rộng. Bằng cách thành thạo hệ sinh thái Windows AI Foundry, nhà phát triển có thể tạo ứng dụng thông minh cung cấp trải nghiệm người dùng xuất sắc đồng thời duy trì tiêu chuẩn cao nhất về riêng tư, bảo mật và hiệu suất.

Sự kết hợp của API Windows AI, Foundry Local và Windows ML cung cấp nền tảng vô song để xây dựng thế hệ ứng dụng Windows thông minh tiếp theo. Khi AI tiếp tục phát triển, nền tảng Windows đảm bảo rằng ứng dụng của bạn sẽ mở rộng cùng công nghệ mới nổi đồng thời duy trì tương thích và hiệu suất trên đa dạng phần cứng Windows.

Dù bạn xây dựng ứng dụng tiêu dùng, giải pháp doanh nghiệp hay công cụ chuyên ngành, phát triển Windows Edge AI giúp bạn tạo ra trải nghiệm thông minh, phản hồi linh hoạt và tích hợp sâu sắc tận dụng tối đa tiềm năng của thiết bị Windows hiện đại.

## Tài nguyên bổ sung

### Tài liệu và học tập
- [Tài liệu Windows AI Foundry](https://learn.microsoft.com/windows/ai/)
- [Tham khảo API Windows AI](https://learn.microsoft.com/windows/ai/apis/)
- [Bắt đầu xây dựng ứng dụng với API Windows AI](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Bắt đầu với Foundry Local](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Tổng quan về Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Yêu cầu hệ thống Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Cài đặt Môi trường Phát triển Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Kho Lưu trữ Mẫu và Mẫu Mã
- [Mẫu Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Mẫu Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Ví dụ Chạy Inference ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Kho Lưu trữ Mẫu Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Công cụ Phát triển
- [Bộ Công cụ AI cho Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Thư viện AI Dev](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Mẫu Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Công cụ Chuyển đổi Mẫu](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Hỗ trợ Kỹ thuật
- [Tài liệu Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Tài liệu ONNX Runtime](https://onnxruntime.ai/docs/)
- [Tài liệu Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Báo cáo Sự cố - Mẫu Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Cộng đồng và Hỗ trợ
- [Cộng đồng Nhà phát triển Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Đào tạo AI Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Hướng dẫn này được thiết kế để phát triển cùng với hệ sinh thái Windows AI đang tiến bộ nhanh chóng. Các bản cập nhật thường xuyên giúp đảm bảo sự phù hợp với các khả năng nền tảng mới nhất và các thực hành phát triển tốt nhất.*

[08. Thực hành với Microsoft Foundry Local - Bộ Công cụ Phát triển Đầy đủ](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->