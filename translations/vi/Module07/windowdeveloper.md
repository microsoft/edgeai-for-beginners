# Hướng Dẫn Phát Triển AI Edge Trên Windows

## Giới Thiệu

Chào mừng bạn đến với hướng dẫn phát triển AI Edge trên Windows - tài liệu toàn diện giúp bạn xây dựng các ứng dụng thông minh tận dụng sức mạnh của AI trên thiết bị thông qua nền tảng Windows AI Foundry của Microsoft. Hướng dẫn này được thiết kế đặc biệt cho các nhà phát triển Windows muốn tích hợp các khả năng AI tiên tiến vào ứng dụng của mình, đồng thời tận dụng tối đa khả năng tăng tốc phần cứng của Windows.

### Lợi Thế Của Windows AI

Windows AI Foundry là một nền tảng thống nhất, đáng tin cậy và an toàn, hỗ trợ toàn bộ vòng đời phát triển AI - từ việc chọn mô hình, tinh chỉnh, tối ưu hóa đến triển khai trên CPU, GPU, NPU và kiến trúc đám mây lai. Nền tảng này giúp phổ biến hóa việc phát triển AI bằng cách cung cấp:

- **Trừu Tượng Phần Cứng**: Triển khai liền mạch trên các chip của AMD, Intel, NVIDIA và Qualcomm
- **Trí Tuệ Trên Thiết Bị**: AI bảo vệ quyền riêng tư hoạt động hoàn toàn trên phần cứng cục bộ
- **Hiệu Suất Tối Ưu**: Các mô hình được tối ưu hóa trước cho cấu hình phần cứng Windows
- **Sẵn Sàng Cho Doanh Nghiệp**: Các tính năng bảo mật và tuân thủ cấp độ sản xuất

### Windows ML 
Windows Machine Learning (ML) cho phép các nhà phát triển C#, C++, và Python chạy các mô hình AI ONNX cục bộ trên máy tính Windows thông qua ONNX Runtime, với khả năng quản lý tự động các nhà cung cấp thực thi cho phần cứng khác nhau (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) có thể được sử dụng với các mô hình từ PyTorch, Tensorflow/Keras, TFLite, scikit-learn và các framework khác.

![WindowsML Một sơ đồ minh họa mô hình ONNX đi qua Windows ML để đến các NPU, GPU và CPU.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML cung cấp một bản sao ONNX Runtime dùng chung trên toàn bộ Windows, cùng với khả năng tải xuống các nhà cung cấp thực thi (EPs) một cách động.

### Tại Sao Chọn Windows Cho AI Edge?

**Hỗ Trợ Phần Cứng Toàn Diện**  
Windows ML cung cấp tối ưu hóa phần cứng tự động trên toàn bộ hệ sinh thái Windows, đảm bảo các ứng dụng AI của bạn hoạt động tối ưu bất kể kiến trúc silicon bên dưới.

**Tích Hợp AI Runtime**  
Công cụ suy luận Windows ML tích hợp sẵn loại bỏ các yêu cầu thiết lập phức tạp, cho phép các nhà phát triển tập trung vào logic ứng dụng thay vì các vấn đề hạ tầng.

**Tối Ưu Hóa PC Copilot+**  
Các API được thiết kế đặc biệt cho các thiết bị Windows thế hệ mới với các Đơn Vị Xử Lý Thần Kinh (NPU) chuyên dụng, mang lại hiệu suất vượt trội trên mỗi watt.

**Hệ Sinh Thái Nhà Phát Triển**  
Công cụ phong phú bao gồm tích hợp Visual Studio, tài liệu toàn diện và các ứng dụng mẫu giúp tăng tốc chu kỳ phát triển.

## Mục Tiêu Học Tập

Hoàn thành hướng dẫn phát triển AI Edge trên Windows này, bạn sẽ nắm vững các kỹ năng cần thiết để xây dựng các ứng dụng AI sẵn sàng cho sản xuất trên nền tảng Windows.

### Năng Lực Kỹ Thuật Cốt Lõi

**Thành Thạo Windows AI Foundry**  
- Hiểu kiến trúc và các thành phần của nền tảng Windows AI Foundry  
- Điều hướng toàn bộ vòng đời phát triển AI trong hệ sinh thái Windows  
- Áp dụng các thực tiễn bảo mật tốt nhất cho các ứng dụng AI trên thiết bị  
- Tối ưu hóa ứng dụng cho các cấu hình phần cứng Windows khác nhau  

**Chuyên Môn Tích Hợp API**  
- Thành thạo các API AI của Windows cho ứng dụng văn bản, hình ảnh và đa phương tiện  
- Tích hợp mô hình ngôn ngữ Phi Silica để tạo văn bản và suy luận  
- Triển khai khả năng thị giác máy tính bằng các API xử lý hình ảnh tích hợp  
- Tùy chỉnh các mô hình được huấn luyện trước bằng kỹ thuật LoRA (Low-Rank Adaptation)  

**Triển Khai Foundry Local**  
- Duyệt, đánh giá và triển khai các mô hình ngôn ngữ mã nguồn mở bằng Foundry Local CLI  
- Hiểu tối ưu hóa mô hình và lượng hóa cho triển khai cục bộ  
- Triển khai khả năng AI ngoại tuyến hoạt động mà không cần kết nối internet  
- Quản lý vòng đời mô hình và cập nhật trong môi trường sản xuất  

**Triển Khai Windows ML**  
- Đưa các mô hình ONNX tùy chỉnh vào ứng dụng Windows bằng Windows ML  
- Tận dụng tăng tốc phần cứng tự động trên các kiến trúc CPU, GPU và NPU  
- Triển khai suy luận thời gian thực với tối ưu hóa tài nguyên  
- Thiết kế các ứng dụng AI có khả năng mở rộng cho các danh mục thiết bị Windows đa dạng  

### Kỹ Năng Phát Triển Ứng Dụng

**Phát Triển Windows Đa Nền Tảng**  
- Xây dựng các ứng dụng tích hợp AI bằng .NET MAUI để triển khai toàn diện trên Windows  
- Tích hợp khả năng AI vào Win32, UWP và Ứng Dụng Web Tiến Bộ (PWA)  
- Triển khai thiết kế giao diện người dùng đáp ứng, thích nghi với trạng thái xử lý AI  
- Xử lý các hoạt động AI không đồng bộ với các mẫu trải nghiệm người dùng phù hợp  

**Tối Ưu Hóa Hiệu Suất**  
- Phân tích và tối ưu hóa hiệu suất suy luận AI trên các cấu hình phần cứng khác nhau  
- Quản lý bộ nhớ hiệu quả cho các mô hình ngôn ngữ lớn  
- Thiết kế ứng dụng giảm thiểu gracefully dựa trên khả năng phần cứng hiện có  
- Áp dụng chiến lược lưu trữ tạm thời cho các hoạt động AI được sử dụng thường xuyên  

**Sẵn Sàng Cho Sản Xuất**  
- Triển khai xử lý lỗi toàn diện và cơ chế dự phòng  
- Thiết kế hệ thống giám sát và đo lường hiệu suất ứng dụng AI  
- Áp dụng các thực tiễn bảo mật tốt nhất cho lưu trữ và thực thi mô hình AI cục bộ  
- Lập kế hoạch chiến lược triển khai cho các ứng dụng doanh nghiệp và người tiêu dùng  

### Hiểu Biết Kinh Doanh Và Chiến Lược

**Kiến Trúc Ứng Dụng AI**  
- Thiết kế kiến trúc lai tối ưu giữa xử lý AI cục bộ và đám mây  
- Đánh giá các đánh đổi giữa kích thước mô hình, độ chính xác và tốc độ suy luận  
- Lập kế hoạch kiến trúc luồng dữ liệu duy trì quyền riêng tư trong khi vẫn cung cấp trí tuệ  
- Triển khai các giải pháp AI hiệu quả về chi phí, có khả năng mở rộng theo nhu cầu người dùng  

**Định Vị Thị Trường**  
- Hiểu lợi thế cạnh tranh của các ứng dụng AI gốc Windows  
- Xác định các trường hợp sử dụng nơi AI trên thiết bị mang lại trải nghiệm người dùng vượt trội  
- Phát triển chiến lược tiếp cận thị trường cho các ứng dụng Windows tích hợp AI  
- Định vị ứng dụng để tận dụng lợi ích của hệ sinh thái Windows  

## Các Mẫu AI Trong Windows App SDK

Windows App SDK cung cấp các mẫu toàn diện minh họa việc tích hợp AI trên nhiều framework và kịch bản triển khai. Các mẫu này là tài liệu tham khảo thiết yếu để hiểu các mẫu phát triển AI trên Windows.

### Các Mẫu Windows AI Foundry

| Mẫu | Framework | Khu Vực Tập Trung | Tính Năng Chính |
|-----|-----------|-------------------|-----------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Tích Hợp API AI Windows | Ứng dụng WinUI hoàn chỉnh minh họa các API AI Windows, tối ưu hóa ARM64, triển khai gói |

**Công Nghệ Chính:**  
- API AI Windows  
- Framework WinUI 3  
- Tối ưu hóa nền tảng ARM64  
- Tương thích PC Copilot+  
- Triển khai ứng dụng dạng gói  

**Yêu Cầu:**  
- Windows 11 với PC Copilot+ được khuyến nghị  
- Visual Studio 2022  
- Cấu hình build ARM64  
- Windows App SDK 1.8.1+  

### Các Mẫu Windows ML

#### Mẫu C++

| Mẫu | Loại | Khu Vực Tập Trung | Tính Năng Chính |
|-----|------|-------------------|-----------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Ứng dụng Console | Windows ML Cơ Bản | Khám phá EP, tùy chọn dòng lệnh, biên dịch mô hình |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Ứng dụng Console | Triển Khai Framework | Runtime dùng chung, footprint triển khai nhỏ hơn |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Ứng dụng Console | Triển Khai Độc Lập | Triển khai độc lập, không phụ thuộc runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Sử Dụng Thư Viện | WindowsML trong thư viện dùng chung, quản lý bộ nhớ |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Hướng Dẫn ResNet | Chuyển đổi mô hình, biên dịch EP, hướng dẫn Build 2025 |

#### Mẫu C#

**Ứng Dụng Console**

| Mẫu | Loại | Khu Vực Tập Trung | Tính Năng Chính |
|-----|------|-------------------|-----------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Ứng dụng Console | Tích Hợp C# Cơ Bản | Sử dụng helper dùng chung, giao diện dòng lệnh |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Hướng Dẫn ResNet | Chuyển đổi mô hình, biên dịch EP, hướng dẫn Build 2025 |

**Ứng Dụng GUI**

| Mẫu | Framework | Khu Vực Tập Trung | Tính Năng Chính |
|-----|-----------|-------------------|-----------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI Desktop | Phân loại hình ảnh với giao diện WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI Truyền Thống | Phân loại hình ảnh với Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI Hiện Đại | Phân loại hình ảnh với giao diện WinUI 3 |

#### Mẫu Python

| Mẫu | Ngôn Ngữ | Khu Vực Tập Trung | Tính Năng Chính |
|-----|----------|-------------------|-----------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Phân Loại Hình Ảnh | Ràng buộc WinML Python, xử lý hình ảnh theo lô |

### Yêu Cầu Mẫu

**Yêu Cầu Hệ Thống:**  
- PC Windows 11 chạy phiên bản 24H2 (build 26100) hoặc cao hơn  
- Visual Studio 2022 với các workload C++ và .NET  
- Windows App SDK 1.8.1 hoặc mới hơn  
- Python 3.10-3.13 cho các mẫu Python trên thiết bị x64 và ARM64  

**Cụ Thể Cho Windows AI Foundry:**  
- PC Copilot+ được khuyến nghị để có hiệu suất tối ưu  
- Cấu hình build ARM64 cho các mẫu AI Windows  
- Yêu cầu danh tính gói (ứng dụng không đóng gói không còn được hỗ trợ)  

### Quy Trình Mẫu Chung

Hầu hết các mẫu Windows ML tuân theo quy trình chuẩn sau:

1. **Khởi Tạo Môi Trường** - Tạo môi trường ONNX Runtime  
2. **Đăng Ký Nhà Cung Cấp Thực Thi** - Khám phá và đăng ký các bộ tăng tốc phần cứng có sẵn (CPU, GPU, NPU)  
3. **Tải Mô Hình** - Tải mô hình ONNX, tùy chọn biên dịch cho phần cứng mục tiêu  
4. **Tiền Xử Lý Đầu Vào** - Chuyển đổi hình ảnh/dữ liệu sang định dạng đầu vào mô hình  
5. **Chạy Suy Luận** - Thực thi mô hình và nhận dự đoán  
6. **Xử Lý Kết Quả** - Áp dụng softmax và hiển thị các dự đoán hàng đầu  

### Các Tệp Mô Hình Được Sử Dụng

| Mô Hình | Mục Đích | Đã Bao Gồm | Ghi Chú |
|---------|----------|------------|--------|
| SqueezeNet | Phân loại hình ảnh nhẹ | ✅ Đã Bao Gồm | Được huấn luyện trước, sẵn sàng sử dụng |
| ResNet-50 | Phân loại hình ảnh độ chính xác cao | ❌ Yêu cầu chuyển đổi | Sử dụng [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) để chuyển đổi |

### Hỗ Trợ Phần Cứng

Tất cả các mẫu tự động phát hiện và sử dụng phần cứng có sẵn:  
- **CPU** - Hỗ trợ toàn diện trên tất cả các thiết bị Windows  
- **GPU** - Phát hiện và tối ưu hóa tự động cho phần cứng đồ họa có sẵn  
- **NPU** - Tận dụng các Đơn Vị Xử Lý Thần Kinh trên các thiết bị được hỗ trợ (PC Copilot+)  

## Các Thành Phần Nền Tảng Windows AI Foundry

### 1. API AI Windows

API AI Windows cung cấp các khả năng AI sẵn sàng sử dụng được hỗ trợ bởi các mô hình trên thiết bị, được tối ưu hóa cho hiệu quả và hiệu suất trên các thiết bị PC Copilot+ với yêu cầu thiết lập tối thiểu.

#### Các Danh Mục API Cốt Lõi

**Mô Hình Ngôn Ngữ Phi Silica**  
- Mô hình ngôn ngữ nhỏ nhưng mạnh mẽ để tạo văn bản và suy luận  
- Tối ưu hóa cho suy luận thời gian thực với mức tiêu thụ năng lượng tối thiểu  
- Hỗ trợ tinh chỉnh tùy chỉnh bằng kỹ thuật LoRA  
- Tích hợp với tìm kiếm ngữ nghĩa và truy xuất kiến thức của Windows  

**API Thị Giác Máy Tính**  
- **Nhận Diện Văn Bản (OCR)**: Trích xuất văn bản từ hình ảnh với độ chính xác cao  
- **Siêu Phân Giải Hình Ảnh**: Nâng cấp hình ảnh bằng các mô hình AI cục bộ  
- **Phân Đoạn Hình Ảnh**: Xác định và cô lập các đối tượng cụ thể trong hình ảnh  
- **Mô Tả Hình Ảnh**: Tạo mô tả văn bản chi tiết cho nội dung hình ảnh  
- **Xóa Đối Tượng**: Loại bỏ các đối tượng không mong muốn khỏi hình ảnh bằng công nghệ inpainting AI  

**Khả Năng Đa Phương Tiện**  
- **Tích Hợp Thị Giác-Ngôn Ngữ**: Kết hợp hiểu biết văn bản và hình ảnh  
- **Tìm Kiếm Ngữ Nghĩa**: Cho phép truy vấn ngôn ngữ tự nhiên trên nội dung đa phương tiện  
- **Truy Xuất Kiến Thức**: Xây dựng trải nghiệm tìm kiếm thông minh với dữ liệu cục bộ  

### 2. Foundry Local

Foundry Local cung cấp cho các nhà phát triển quyền truy cập nhanh vào các mô hình ngôn ngữ mã nguồn mở sẵn sàng sử dụng trên Windows Silicon, cho phép duyệt, thử nghiệm, tương tác và triển khai mô hình trong các ứng dụng cục bộ.

#### Các Ứng Dụng Mẫu Foundry Local

Kho [Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) cung cấp các mẫu toàn diện trên nhiều ngôn ngữ lập trình và framework, minh họa các mẫu tích hợp và trường hợp sử dụng khác nhau.

| Mẫu | Ngôn Ngữ/Framework | Khu Vực Tập Trung | Tính Năng Chính |
|-----|---------------------|-------------------|-----------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Triển Khai RAG | Tích hợp Semantic Kernel, lưu trữ vector Qdrant, nhúng JINA, nhập tài liệu, chat streaming |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Ứng Dụng Chat Desktop | Chat đa nền tảng, chuyển đổi mô hình cục bộ/đám mây, tích hợp SDK OpenAI, streaming thời
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Tích hợp hệ thống | Sử dụng SDK cấp thấp, hoạt động bất đồng bộ, reqwest HTTP client |

#### Danh mục mẫu theo trường hợp sử dụng

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Triển khai RAG hoàn chỉnh sử dụng Semantic Kernel, cơ sở dữ liệu vector Qdrant, và JINA embeddings
- **Kiến trúc**: Nhập liệu tài liệu → Chia nhỏ văn bản → Vector embeddings → Tìm kiếm tương đồng → Phản hồi theo ngữ cảnh
- **Công nghệ**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, hoàn thành chat theo luồng

**Ứng dụng Desktop**
- **electron/foundry-chat**: Ứng dụng chat sẵn sàng sản xuất với khả năng chuyển đổi mô hình cục bộ/đám mây
- **Tính năng**: Bộ chọn mô hình, phản hồi theo luồng, xử lý lỗi, triển khai đa nền tảng
- **Kiến trúc**: Quy trình chính của Electron, giao tiếp IPC, script preload an toàn

**Ví dụ tích hợp SDK**
- **JavaScript (Node.js)**: Tương tác mô hình cơ bản và phản hồi theo luồng
- **Python**: Sử dụng API tương thích OpenAI với luồng bất đồng bộ
- **Rust**: Tích hợp cấp thấp với reqwest và tokio cho các hoạt động bất đồng bộ

#### Yêu cầu trước khi sử dụng mẫu Foundry Local

**Yêu cầu hệ thống:**
- Windows 11 với Foundry Local đã cài đặt
- Node.js v16+ cho các mẫu JavaScript/Electron
- .NET 8.0+ cho các mẫu C#
- Python 3.10+ cho các mẫu Python
- Rust 1.70+ cho các mẫu Rust

**Cài đặt:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Cài đặt cụ thể cho từng mẫu

**Mẫu dotNET RAG:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Mẫu Electron Chat:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**Mẫu JavaScript/Python/Rust:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Các tính năng chính

**Danh mục mô hình**
- Bộ sưu tập toàn diện các mô hình mã nguồn mở đã được tối ưu hóa
- Mô hình được tối ưu hóa trên CPU, GPU, và NPU để triển khai ngay lập tức
- Hỗ trợ các dòng mô hình phổ biến như Llama, Mistral, Phi, và các mô hình chuyên biệt theo lĩnh vực

**Tích hợp CLI**
- Giao diện dòng lệnh để quản lý và triển khai mô hình
- Quy trình tối ưu hóa và lượng hóa tự động
- Tích hợp với các môi trường phát triển phổ biến và pipeline CI/CD

**Triển khai cục bộ**
- Hoạt động hoàn toàn ngoại tuyến mà không cần phụ thuộc vào đám mây
- Hỗ trợ các định dạng và cấu hình mô hình tùy chỉnh
- Phục vụ mô hình hiệu quả với tối ưu hóa phần cứng tự động

### 3. Windows ML

Windows ML là nền tảng AI cốt lõi và runtime suy luận tích hợp trên Windows, cho phép các nhà phát triển triển khai mô hình tùy chỉnh một cách hiệu quả trên hệ sinh thái phần cứng rộng lớn của Windows.

#### Lợi ích kiến trúc

**Hỗ trợ phần cứng toàn diện**
- Tối ưu hóa tự động cho silicon của AMD, Intel, NVIDIA, và Qualcomm
- Hỗ trợ thực thi trên CPU, GPU, và NPU với chuyển đổi minh bạch
- Trừu tượng hóa phần cứng giúp loại bỏ công việc tối ưu hóa theo nền tảng

**Linh hoạt mô hình**
- Hỗ trợ định dạng mô hình ONNX với chuyển đổi tự động từ các framework phổ biến
- Triển khai mô hình tùy chỉnh với hiệu suất cấp sản xuất
- Tích hợp với các kiến trúc ứng dụng Windows hiện có

**Tích hợp doanh nghiệp**
- Tương thích với các framework bảo mật và tuân thủ của Windows
- Hỗ trợ các công cụ triển khai và quản lý doanh nghiệp
- Tích hợp với hệ thống quản lý và giám sát thiết bị Windows

## Quy trình phát triển

### Giai đoạn 1: Thiết lập môi trường và cấu hình công cụ

**Chuẩn bị môi trường phát triển**
1. Cài đặt Visual Studio 2022 với các workload C++ và .NET
2. Cài đặt Windows App SDK 1.8.1 hoặc mới hơn
3. Cấu hình các công cụ CLI của Windows AI Foundry
4. Thiết lập tiện ích mở rộng AI Toolkit cho Visual Studio Code
5. Thiết lập các công cụ giám sát và phân tích hiệu suất
6. Đảm bảo cấu hình build ARM64 để tối ưu hóa cho PC Copilot+

**Thiết lập kho mẫu**
1. Clone [kho mẫu Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Điều hướng đến `Samples/WindowsAIFoundry/cs-winui` để xem các ví dụ API AI của Windows
3. Điều hướng đến `Samples/WindowsML` để xem các ví dụ toàn diện về Windows ML
4. Xem lại [yêu cầu build](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) cho các nền tảng mục tiêu của bạn

**Khám phá AI Dev Gallery**
- Khám phá các ứng dụng mẫu và triển khai tham khảo
- Kiểm tra các API AI của Windows với các bản demo tương tác
- Xem lại mã nguồn để tìm hiểu các thực tiễn và mẫu tốt nhất
- Xác định các mẫu phù hợp với trường hợp sử dụng cụ thể của bạn

### Giai đoạn 2: Lựa chọn và tích hợp mô hình

**Phân tích yêu cầu**
- Xác định yêu cầu chức năng cho các khả năng AI
- Thiết lập các ràng buộc hiệu suất và mục tiêu tối ưu hóa
- Đánh giá các yêu cầu về quyền riêng tư và bảo mật
- Lập kế hoạch kiến trúc triển khai và chiến lược mở rộng

**Đánh giá mô hình**
- Sử dụng Foundry Local để kiểm tra các mô hình mã nguồn mở cho trường hợp sử dụng của bạn
- Đo hiệu suất các API AI của Windows với các yêu cầu mô hình tùy chỉnh
- Đánh giá các đánh đổi giữa kích thước mô hình, độ chính xác, và tốc độ suy luận
- Tạo nguyên mẫu các phương pháp tích hợp với các mô hình đã chọn

### Giai đoạn 3: Phát triển ứng dụng

**Tích hợp cốt lõi**
- Triển khai tích hợp API AI của Windows với xử lý lỗi phù hợp
- Thiết kế giao diện người dùng phù hợp với quy trình xử lý AI
- Triển khai các chiến lược caching và tối ưu hóa cho suy luận mô hình
- Thêm telemetry và giám sát để theo dõi hiệu suất hoạt động AI

**Kiểm tra và xác thực**
- Kiểm tra ứng dụng trên các cấu hình phần cứng Windows khác nhau
- Xác thực các chỉ số hiệu suất dưới các điều kiện tải khác nhau
- Triển khai kiểm tra tự động để đảm bảo độ tin cậy của chức năng AI
- Thực hiện kiểm tra trải nghiệm người dùng với các tính năng được cải tiến bởi AI

### Giai đoạn 4: Tối ưu hóa và triển khai

**Tối ưu hóa hiệu suất**
- Phân tích hiệu suất ứng dụng trên các cấu hình phần cứng mục tiêu
- Tối ưu hóa việc sử dụng bộ nhớ và chiến lược tải mô hình
- Triển khai hành vi thích ứng dựa trên khả năng phần cứng có sẵn
- Tinh chỉnh trải nghiệm người dùng cho các kịch bản hiệu suất khác nhau

**Triển khai sản xuất**
- Đóng gói ứng dụng với các phụ thuộc mô hình AI phù hợp
- Triển khai cơ chế cập nhật cho mô hình và logic ứng dụng
- Cấu hình giám sát và phân tích cho môi trường sản xuất
- Lập kế hoạch chiến lược triển khai cho doanh nghiệp và người tiêu dùng

## Ví dụ triển khai thực tế

### Ví dụ 1: Ứng dụng xử lý tài liệu thông minh

Xây dựng một ứng dụng Windows xử lý tài liệu sử dụng nhiều khả năng AI:

**Công nghệ sử dụng:**
- Phi Silica để tóm tắt tài liệu và trả lời câu hỏi
- API OCR để trích xuất văn bản từ tài liệu quét
- API mô tả hình ảnh để phân tích biểu đồ và sơ đồ
- Mô hình ONNX tùy chỉnh để phân loại tài liệu

**Phương pháp triển khai:**
- Thiết kế kiến trúc module với các thành phần AI có thể cắm vào
- Triển khai xử lý bất đồng bộ cho các lô tài liệu lớn
- Thêm chỉ báo tiến độ và hỗ trợ hủy bỏ cho các hoạt động dài
- Bao gồm khả năng ngoại tuyến để xử lý tài liệu nhạy cảm

### Ví dụ 2: Hệ thống quản lý hàng tồn kho bán lẻ

Tạo hệ thống quản lý hàng tồn kho được hỗ trợ bởi AI cho các ứng dụng bán lẻ:

**Công nghệ sử dụng:**
- Phân đoạn hình ảnh để nhận diện sản phẩm
- Mô hình thị giác tùy chỉnh để phân loại thương hiệu và danh mục
- Triển khai Foundry Local của các mô hình ngôn ngữ chuyên biệt cho bán lẻ
- Tích hợp với hệ thống POS và quản lý hàng tồn kho hiện có

**Phương pháp triển khai:**
- Xây dựng tích hợp camera để quét sản phẩm theo thời gian thực
- Triển khai nhận diện mã vạch và sản phẩm bằng hình ảnh
- Thêm truy vấn hàng tồn kho bằng ngôn ngữ tự nhiên sử dụng mô hình ngôn ngữ cục bộ
- Thiết kế kiến trúc có thể mở rộng cho triển khai đa cửa hàng

### Ví dụ 3: Trợ lý tài liệu y tế

Phát triển công cụ tài liệu y tế bảo vệ quyền riêng tư:

**Công nghệ sử dụng:**
- Phi Silica để tạo ghi chú y tế và hỗ trợ quyết định lâm sàng
- OCR để số hóa hồ sơ y tế viết tay
- Mô hình ngôn ngữ y tế tùy chỉnh triển khai qua Windows ML
- Lưu trữ vector cục bộ để truy xuất kiến thức y tế

**Phương pháp triển khai:**
- Đảm bảo hoạt động hoàn toàn ngoại tuyến để bảo vệ quyền riêng tư bệnh nhân
- Triển khai xác thực và gợi ý thuật ngữ y tế
- Thêm ghi nhật ký kiểm toán để tuân thủ quy định
- Thiết kế tích hợp với các hệ thống hồ sơ y tế điện tử hiện có

## Chiến lược tối ưu hóa hiệu suất

### Phát triển nhận thức phần cứng

**Tối ưu hóa NPU**
- Thiết kế ứng dụng để tận dụng khả năng NPU trên PC Copilot+
- Triển khai fallback linh hoạt sang GPU/CPU trên các thiết bị không có NPU
- Tối ưu hóa định dạng mô hình cho tăng tốc cụ thể của NPU
- Giám sát việc sử dụng NPU và đặc điểm nhiệt

**Quản lý bộ nhớ**
- Triển khai các chiến lược tải và caching mô hình hiệu quả
- Sử dụng ánh xạ bộ nhớ cho các mô hình lớn để giảm thời gian khởi động
- Thiết kế ứng dụng tiết kiệm bộ nhớ cho các thiết bị hạn chế tài nguyên
- Triển khai lượng hóa mô hình để tối ưu hóa bộ nhớ

**Hiệu quả pin**
- Tối ưu hóa các hoạt động AI để tiêu thụ năng lượng tối thiểu
- Triển khai xử lý thích ứng dựa trên trạng thái pin
- Thiết kế xử lý nền hiệu quả cho các hoạt động AI liên tục
- Sử dụng các công cụ phân tích năng lượng để tối ưu hóa việc sử dụng năng lượng

### Cân nhắc khả năng mở rộng

**Đa luồng**
- Thiết kế các hoạt động AI an toàn luồng cho xử lý đồng thời
- Triển khai phân phối công việc hiệu quả trên các lõi có sẵn
- Sử dụng các mẫu async/await cho các hoạt động AI không chặn
- Lập kế hoạch tối ưu hóa pool luồng cho các cấu hình phần cứng khác nhau

**Chiến lược caching**
- Triển khai caching thông minh cho các hoạt động AI được sử dụng thường xuyên
- Thiết kế các chiến lược vô hiệu hóa cache cho các cập nhật mô hình
- Sử dụng caching liên tục cho các hoạt động tiền xử lý tốn kém
- Triển khai caching phân tán cho các kịch bản nhiều người dùng

## Thực tiễn tốt nhất về bảo mật và quyền riêng tư

### Bảo vệ dữ liệu

**Xử lý cục bộ**
- Đảm bảo dữ liệu nhạy cảm không bao giờ rời khỏi thiết bị cục bộ
- Triển khai lưu trữ an toàn cho các mô hình AI và dữ liệu tạm thời
- Sử dụng các tính năng bảo mật của Windows để sandbox ứng dụng
- Áp dụng mã hóa cho các mô hình được lưu trữ và kết quả xử lý trung gian

**Bảo mật mô hình**
- Xác thực tính toàn vẹn của mô hình trước khi tải và thực thi
- Triển khai cơ chế cập nhật mô hình an toàn
- Sử dụng các mô hình đã ký để ngăn chặn giả mạo
- Áp dụng kiểm soát truy cập cho các tệp mô hình và cấu hình

### Cân nhắc tuân thủ

**Tuân thủ quy định**
- Thiết kế ứng dụng để đáp ứng GDPR, HIPAA, và các yêu cầu quy định khác
- Triển khai ghi nhật ký kiểm toán cho các quy trình ra quyết định AI
- Cung cấp các tính năng minh bạch cho kết quả do AI tạo ra
- Cho phép người dùng kiểm soát việc xử lý dữ liệu AI

**Bảo mật doanh nghiệp**
- Tích hợp với các chính sách bảo mật doanh nghiệp của Windows
- Hỗ trợ triển khai được quản lý thông qua các công cụ quản lý doanh nghiệp
- Triển khai kiểm soát truy cập dựa trên vai trò cho các tính năng AI
- Cung cấp các kiểm soát quản trị cho chức năng AI

## Khắc phục sự cố và gỡ lỗi

### Các thách thức phát triển phổ biến

**Vấn đề cấu hình build**
- Đảm bảo cấu hình nền tảng ARM64 cho các mẫu API AI của Windows
- Xác minh khả năng tương thích phiên bản Windows App SDK (yêu cầu 1.8.1+)
- Kiểm tra rằng danh tính gói được cấu hình đúng (yêu cầu cho các API AI của Windows)
- Xác thực rằng các công cụ build hỗ trợ phiên bản framework mục tiêu

**Vấn đề tải mô hình**
- Xác thực khả năng tương thích mô hình ONNX với Windows ML
- Kiểm tra tính toàn vẹn tệp mô hình và yêu cầu định dạng
- Xác minh các yêu cầu khả năng phần cứng cho các mô hình cụ thể
- Gỡ lỗi các vấn đề phân bổ bộ nhớ trong quá trình tải mô hình
- Đảm bảo đăng ký nhà cung cấp thực thi để tăng tốc phần cứng

**Cân nhắc chế độ triển khai**
- **Chế độ tự chứa**: Được hỗ trợ đầy đủ với kích thước triển khai lớn hơn
- **Chế độ phụ thuộc framework**: Dấu chân nhỏ hơn nhưng yêu cầu runtime chia sẻ
- **Ứng dụng không đóng gói**: Không còn được hỗ trợ cho các API AI của Windows
- Sử dụng `dotnet run -p:Platform=ARM64 -p:SelfContained=true` cho triển khai tự chứa ARM64

**Vấn đề hiệu suất**
- Phân tích hiệu suất ứng dụng trên các cấu hình phần cứng khác nhau
- Xác định các nút thắt trong các pipeline xử lý AI
- Tối ưu hóa các hoạt động tiền xử lý và hậu xử lý dữ liệu
- Triển khai giám sát hiệu suất và cảnh báo

**Khó khăn tích hợp**
- Gỡ lỗi các vấn đề tích hợp API với xử lý lỗi phù hợp
- Xác thực các định dạng dữ liệu đầu vào và yêu cầu tiền xử lý
- Kiểm tra kỹ các trường hợp biên và điều kiện lỗi
- Triển khai ghi nhật ký toàn diện để gỡ lỗi các vấn đề sản xuất

### Công cụ và kỹ thuật gỡ lỗi

**Tích hợp Visual Studio**
- Sử dụng trình gỡ lỗi AI Toolkit để phân tích thực thi mô hình
- Triển khai phân tích hiệu suất cho các hoạt động AI
- Gỡ lỗi các hoạt động AI bất đồng bộ với xử lý ngoại lệ phù hợp
- Sử dụng các công cụ phân tích bộ nhớ để tối ưu hóa

**Công cụ Windows AI Foundry**
- Tận dụng CLI của Foundry Local để kiểm tra và xác thực mô hình
- Sử dụng các công cụ kiểm tra API AI của Windows để xác minh tích hợp
- Triển khai ghi nhật ký tùy chỉnh để giám sát hoạt động AI
- Tạo kiểm tra tự động để đảm bảo độ tin cậy của chức năng AI

## Tương lai hóa ứng dụng của bạn

### Công nghệ mới nổi

**Phần cứng thế hệ tiếp theo**
- Thiết kế ứng dụng để tận dụng khả năng NPU trong tương lai
- Lập kế hoạch cho kích thước và độ phức tạp mô hình tăng lên
- Triển khai các kiến trúc thích ứng cho phần cứng đang phát triển
- Cân nhắc các thuật toán sẵn sàng cho lượng tử để đảm bảo khả năng tương thích trong tương lai

**Khả năng AI tiên tiến**
- Chuẩn bị cho tích hợp AI đa phương thức trên nhiều loại dữ liệu hơn
- Lập kế hoạch cho AI hợp tác theo thời gian thực giữa nhiều thiết bị
- Thiết kế cho các khả năng học liên kết
- Cân nhắc các kiến trúc trí tuệ lai edge-cloud

### Học tập và thích ứng liên tục

**Cập nhật mô hình**
- Triển khai các cơ chế cập nhật mô hình liền mạch
- Thiết kế ứng dụng để thích ứng với các khả năng mô hình được cải thiện
- Lập kế hoạch cho khả năng tương thích ngược với các mô hình hiện có
- Triển khai kiểm tra A/B để đánh giá hiệu suất mô hình

**Tiến hóa tính năng**
- Thiết kế các kiến trúc module có thể chứa các khả năng AI mới
- Lập kế hoạch cho tích hợp các
- [Tổng quan về Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Yêu cầu hệ thống của Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Thiết lập môi trường phát triển Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Kho mẫu và mã nguồn
- [Mẫu Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Mẫu Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Ví dụ về suy luận ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Kho mẫu Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Công cụ phát triển
- [Bộ công cụ AI cho Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Thư viện phát triển AI](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Mẫu Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Công cụ chuyển đổi mô hình](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Hỗ trợ kỹ thuật
- [Tài liệu Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Tài liệu ONNX Runtime](https://onnxruntime.ai/docs/)
- [Tài liệu Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Báo cáo vấn đề - Mẫu Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Cộng đồng và hỗ trợ
- [Cộng đồng nhà phát triển Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Đào tạo AI trên Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Hướng dẫn này được thiết kế để phát triển cùng với hệ sinh thái Windows AI đang tiến bộ nhanh chóng. Các cập nhật thường xuyên đảm bảo sự phù hợp với các khả năng nền tảng mới nhất và các thực tiễn phát triển tốt nhất.*

[08. Thực hành với Microsoft Foundry Local - Bộ công cụ hoàn chỉnh cho nhà phát triển](../Module08/README.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.