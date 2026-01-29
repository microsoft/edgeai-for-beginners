# Bộ công cụ AI cho Visual Studio Code - Hướng dẫn phát triển AI tại biên

## Giới thiệu

Chào mừng bạn đến với hướng dẫn toàn diện về cách sử dụng Bộ công cụ AI cho Visual Studio Code trong phát triển AI tại biên. Khi trí tuệ nhân tạo chuyển từ điện toán đám mây tập trung sang các thiết bị biên phân tán, các nhà phát triển cần những công cụ mạnh mẽ, tích hợp để xử lý các thách thức độc đáo của việc triển khai tại biên - từ hạn chế tài nguyên đến yêu cầu hoạt động ngoại tuyến.

Bộ công cụ AI cho Visual Studio Code lấp đầy khoảng cách này bằng cách cung cấp một môi trường phát triển hoàn chỉnh, được thiết kế đặc biệt để xây dựng, kiểm tra và tối ưu hóa các ứng dụng AI hoạt động hiệu quả trên các thiết bị biên. Dù bạn đang phát triển cho cảm biến IoT, thiết bị di động, hệ thống nhúng hay máy chủ biên, bộ công cụ này sẽ đơn giản hóa toàn bộ quy trình phát triển của bạn trong môi trường VS Code quen thuộc.

Hướng dẫn này sẽ đưa bạn qua các khái niệm cơ bản, công cụ và các thực hành tốt nhất để tận dụng Bộ công cụ AI trong các dự án AI tại biên của bạn, từ việc lựa chọn mô hình ban đầu đến triển khai sản xuất.

## Tổng quan

Bộ công cụ AI cho Visual Studio Code là một tiện ích mở rộng mạnh mẽ giúp đơn giản hóa việc phát triển tác nhân và tạo ứng dụng AI. Bộ công cụ cung cấp các khả năng toàn diện để khám phá, đánh giá và triển khai các mô hình AI từ nhiều nhà cung cấp—bao gồm Anthropic, OpenAI, GitHub, Google—đồng thời hỗ trợ thực thi mô hình cục bộ bằng ONNX và Ollama.

Điều làm cho Bộ công cụ AI nổi bật là cách tiếp cận toàn diện đối với toàn bộ vòng đời phát triển AI. Không giống như các công cụ phát triển AI truyền thống chỉ tập trung vào một khía cạnh, Bộ công cụ AI cung cấp một môi trường tích hợp bao gồm khám phá mô hình, thử nghiệm, phát triển tác nhân, đánh giá và triển khai—tất cả trong môi trường VS Code quen thuộc.

Nền tảng này được thiết kế đặc biệt cho việc tạo mẫu nhanh và triển khai sản xuất, với các tính năng như tạo lời nhắc, khởi động nhanh, tích hợp công cụ MCP (Model Context Protocol) liền mạch và khả năng đánh giá mở rộng. Đối với phát triển AI tại biên, điều này có nghĩa là bạn có thể phát triển, kiểm tra và tối ưu hóa các ứng dụng AI cho các kịch bản triển khai tại biên một cách hiệu quả trong khi vẫn duy trì toàn bộ quy trình phát triển trong VS Code.

## Mục tiêu học tập

Kết thúc hướng dẫn này, bạn sẽ có thể:

### Năng lực cốt lõi
- **Cài đặt và cấu hình** Bộ công cụ AI cho Visual Studio Code cho các quy trình phát triển AI tại biên
- **Điều hướng và sử dụng** giao diện Bộ công cụ AI, bao gồm Model Catalog, Playground và Agent Builder
- **Lựa chọn và đánh giá** các mô hình AI phù hợp để triển khai tại biên dựa trên hiệu suất và hạn chế tài nguyên
- **Chuyển đổi và tối ưu hóa** các mô hình bằng định dạng ONNX và các kỹ thuật lượng hóa cho thiết bị biên

### Kỹ năng phát triển AI tại biên
- **Thiết kế và triển khai** các ứng dụng AI tại biên bằng môi trường phát triển tích hợp
- **Kiểm tra mô hình** trong các điều kiện giống như tại biên bằng cách suy luận cục bộ và giám sát tài nguyên
- **Tạo và tùy chỉnh** các tác nhân AI được tối ưu hóa cho các kịch bản triển khai tại biên
- **Đánh giá hiệu suất mô hình** bằng các chỉ số liên quan đến tính toán tại biên (độ trễ, sử dụng bộ nhớ, độ chính xác)

### Tối ưu hóa và triển khai
- **Áp dụng các kỹ thuật lượng hóa và cắt tỉa** để giảm kích thước mô hình trong khi vẫn duy trì hiệu suất chấp nhận được
- **Tối ưu hóa mô hình** cho các nền tảng phần cứng biên cụ thể bao gồm tăng tốc CPU, GPU và NPU
- **Thực hiện các thực hành tốt nhất** cho phát triển AI tại biên bao gồm quản lý tài nguyên và chiến lược dự phòng
- **Chuẩn bị mô hình và ứng dụng** cho triển khai sản xuất trên các thiết bị biên

### Các khái niệm nâng cao về AI tại biên
- **Tích hợp với các khung AI tại biên** bao gồm ONNX Runtime, Windows ML và TensorFlow Lite
- **Triển khai kiến trúc đa mô hình** và các kịch bản học liên kết cho môi trường biên
- **Khắc phục các vấn đề phổ biến về AI tại biên** bao gồm hạn chế bộ nhớ, tốc độ suy luận và khả năng tương thích phần cứng
- **Thiết kế chiến lược giám sát và ghi nhật ký** cho các ứng dụng AI tại biên trong sản xuất

### Ứng dụng thực tế
- **Xây dựng các giải pháp AI tại biên từ đầu đến cuối** từ việc lựa chọn mô hình đến triển khai
- **Thể hiện sự thành thạo** trong các quy trình phát triển và kỹ thuật tối ưu hóa cụ thể cho biên
- **Áp dụng các khái niệm đã học** vào các trường hợp sử dụng AI tại biên thực tế bao gồm IoT, di động và ứng dụng nhúng
- **Đánh giá và so sánh** các chiến lược triển khai AI tại biên khác nhau và các đánh đổi của chúng

## Các tính năng chính cho phát triển AI tại biên

### 1. Danh mục và khám phá mô hình
- **Hỗ trợ đa nhà cung cấp**: Duyệt và truy cập các mô hình AI từ Anthropic, OpenAI, GitHub, Google và các nhà cung cấp khác
- **Tích hợp mô hình cục bộ**: Khám phá đơn giản các mô hình ONNX và Ollama cho triển khai tại biên
- **Mô hình GitHub**: Tích hợp trực tiếp với lưu trữ mô hình của GitHub để truy cập dễ dàng
- **So sánh mô hình**: So sánh các mô hình cạnh nhau để tìm sự cân bằng tối ưu cho các hạn chế của thiết bị biên

### 2. Playground tương tác
- **Môi trường thử nghiệm tương tác**: Thử nghiệm nhanh các khả năng của mô hình trong môi trường được kiểm soát
- **Hỗ trợ đa phương thức**: Thử nghiệm với hình ảnh, văn bản và các đầu vào khác thường gặp trong các kịch bản biên
- **Thử nghiệm thời gian thực**: Phản hồi ngay lập tức về các phản hồi và hiệu suất của mô hình
- **Tối ưu hóa tham số**: Tinh chỉnh các tham số mô hình cho các yêu cầu triển khai tại biên

### 3. Trình tạo lời nhắc (Agent Builder)
- **Tạo ngôn ngữ tự nhiên**: Tạo các lời nhắc khởi đầu bằng mô tả ngôn ngữ tự nhiên
- **Cải thiện lặp lại**: Cải thiện lời nhắc dựa trên phản hồi và hiệu suất của mô hình
- **Phân chia nhiệm vụ**: Phân chia các nhiệm vụ phức tạp bằng cách xâu chuỗi lời nhắc và tạo đầu ra có cấu trúc
- **Hỗ trợ biến**: Sử dụng các biến trong lời nhắc để tạo hành vi động cho tác nhân
- **Tạo mã sản xuất**: Tạo mã sẵn sàng sản xuất để phát triển ứng dụng nhanh chóng

### 4. Chạy hàng loạt và đánh giá
- **Kiểm tra đa mô hình**: Thực hiện nhiều lời nhắc trên các mô hình đã chọn đồng thời
- **Kiểm tra hiệu quả ở quy mô lớn**: Kiểm tra các đầu vào và cấu hình khác nhau một cách hiệu quả
- **Trường hợp kiểm tra tùy chỉnh**: Chạy các tác nhân với các trường hợp kiểm tra để xác thực chức năng
- **So sánh hiệu suất**: So sánh kết quả trên các mô hình và cấu hình khác nhau

### 5. Đánh giá mô hình với tập dữ liệu
- **Chỉ số tiêu chuẩn**: Kiểm tra các mô hình AI bằng các bộ đánh giá tích hợp (điểm F1, mức độ liên quan, độ tương đồng, sự mạch lạc)
- **Bộ đánh giá tùy chỉnh**: Tạo các chỉ số đánh giá riêng cho các trường hợp sử dụng cụ thể
- **Tích hợp tập dữ liệu**: Kiểm tra các mô hình với các tập dữ liệu toàn diện
- **Đo lường hiệu suất**: Định lượng hiệu suất mô hình để đưa ra quyết định triển khai tại biên

### 6. Khả năng tinh chỉnh
- **Tùy chỉnh mô hình**: Tùy chỉnh mô hình cho các trường hợp sử dụng và lĩnh vực cụ thể
- **Thích nghi chuyên biệt**: Điều chỉnh mô hình cho các lĩnh vực và yêu cầu chuyên biệt
- **Tối ưu hóa cho biên**: Tinh chỉnh mô hình đặc biệt cho các hạn chế triển khai tại biên
- **Đào tạo theo lĩnh vực**: Tạo các mô hình phù hợp với các trường hợp sử dụng tại biên cụ thể

### 7. Tích hợp công cụ MCP
- **Kết nối công cụ bên ngoài**: Kết nối các tác nhân với các công cụ bên ngoài thông qua các máy chủ Model Context Protocol
- **Hành động thực tế**: Cho phép các tác nhân truy vấn cơ sở dữ liệu, truy cập API hoặc thực thi logic tùy chỉnh
- **Máy chủ MCP hiện có**: Sử dụng các công cụ từ giao thức lệnh (stdio) hoặc HTTP (sự kiện gửi từ máy chủ)
- **Phát triển MCP tùy chỉnh**: Xây dựng và tạo khung các máy chủ MCP mới với thử nghiệm trong Agent Builder

### 8. Phát triển và kiểm tra tác nhân
- **Hỗ trợ gọi hàm**: Cho phép các tác nhân gọi các hàm bên ngoài một cách động
- **Kiểm tra tích hợp thời gian thực**: Kiểm tra tích hợp với các lần chạy thời gian thực và sử dụng công cụ
- **Phiên bản hóa tác nhân**: Kiểm soát phiên bản cho các tác nhân với khả năng so sánh kết quả đánh giá
- **Gỡ lỗi và theo dõi**: Khả năng theo dõi và gỡ lỗi cục bộ cho phát triển tác nhân

## Quy trình phát triển AI tại biên

### Giai đoạn 1: Khám phá và lựa chọn mô hình
1. **Khám phá Danh mục Mô hình**: Sử dụng danh mục mô hình để tìm các mô hình phù hợp cho triển khai tại biên
2. **So sánh hiệu suất**: Đánh giá các mô hình dựa trên kích thước, độ chính xác và tốc độ suy luận
3. **Kiểm tra cục bộ**: Sử dụng các mô hình Ollama hoặc ONNX để kiểm tra cục bộ trước khi triển khai tại biên
4. **Đánh giá yêu cầu tài nguyên**: Xác định nhu cầu bộ nhớ và tính toán cho các thiết bị biên mục tiêu

### Giai đoạn 2: Tối ưu hóa mô hình
1. **Chuyển đổi sang ONNX**: Chuyển đổi các mô hình đã chọn sang định dạng ONNX để tương thích với biên
2. **Áp dụng lượng hóa**: Giảm kích thước mô hình thông qua lượng hóa INT8 hoặc INT4
3. **Tối ưu hóa phần cứng**: Tối ưu hóa cho phần cứng biên mục tiêu (ARM, x86, bộ tăng tốc chuyên dụng)
4. **Xác thực hiệu suất**: Xác thực các mô hình được tối ưu hóa duy trì độ chính xác chấp nhận được

### Giai đoạn 3: Phát triển ứng dụng
1. **Thiết kế tác nhân**: Sử dụng Agent Builder để tạo các tác nhân AI được tối ưu hóa cho biên
2. **Kỹ thuật lời nhắc**: Phát triển các lời nhắc hoạt động hiệu quả với các mô hình biên nhỏ hơn
3. **Kiểm tra tích hợp**: Kiểm tra các tác nhân trong các điều kiện mô phỏng tại biên
4. **Tạo mã**: Tạo mã sản xuất được tối ưu hóa cho triển khai tại biên

### Giai đoạn 4: Đánh giá và kiểm tra
1. **Đánh giá hàng loạt**: Kiểm tra nhiều cấu hình để tìm cài đặt biên tối ưu
2. **Hồ sơ hiệu suất**: Phân tích tốc độ suy luận, sử dụng bộ nhớ và độ chính xác
3. **Mô phỏng biên**: Kiểm tra trong các điều kiện tương tự như môi trường triển khai tại biên mục tiêu
4. **Kiểm tra áp lực**: Đánh giá hiệu suất dưới các điều kiện tải khác nhau

### Giai đoạn 5: Chuẩn bị triển khai
1. **Tối ưu hóa cuối cùng**: Áp dụng các tối ưu hóa cuối cùng dựa trên kết quả kiểm tra
2. **Đóng gói triển khai**: Đóng gói mô hình và mã cho triển khai tại biên
3. **Tài liệu hóa**: Tài liệu hóa các yêu cầu và cấu hình triển khai
4. **Thiết lập giám sát**: Chuẩn bị giám sát và ghi nhật ký cho triển khai tại biên

## Đối tượng mục tiêu cho phát triển AI tại biên

### Nhà phát triển AI tại biên
- Các nhà phát triển ứng dụng xây dựng các thiết bị biên và giải pháp IoT tích hợp AI
- Các nhà phát triển hệ thống nhúng tích hợp khả năng AI vào các thiết bị hạn chế tài nguyên
- Các nhà phát triển di động tạo ứng dụng AI trên thiết bị cho điện thoại thông minh và máy tính bảng

### Kỹ sư AI tại biên
- Các kỹ sư AI tối ưu hóa mô hình cho triển khai tại biên và quản lý các đường dẫn suy luận
- Các kỹ sư DevOps triển khai và quản lý các mô hình AI trên cơ sở hạ tầng biên phân tán
- Các kỹ sư hiệu suất tối ưu hóa khối lượng công việc AI cho các hạn chế phần cứng biên

### Nhà nghiên cứu và giáo dục
- Các nhà nghiên cứu AI phát triển các mô hình và thuật toán hiệu quả cho tính toán tại biên
- Các nhà giáo dục giảng dạy các khái niệm AI tại biên và trình diễn các kỹ thuật tối ưu hóa
- Sinh viên học về các thách thức và giải pháp trong triển khai AI tại biên

## Các trường hợp sử dụng AI tại biên

### Thiết bị IoT thông minh
- **Nhận diện hình ảnh thời gian thực**: Triển khai các mô hình thị giác máy tính trên camera và cảm biến IoT
- **Xử lý giọng nói**: Thực hiện nhận diện giọng nói và xử lý ngôn ngữ tự nhiên trên loa thông minh
- **Bảo trì dự đoán**: Chạy các mô hình phát hiện bất thường trên các thiết bị biên công nghiệp
- **Giám sát môi trường**: Triển khai các mô hình phân tích dữ liệu cảm biến cho các ứng dụng môi trường

### Ứng dụng di động và nhúng
- **Dịch thuật trên thiết bị**: Thực hiện các mô hình dịch ngôn ngữ hoạt động ngoại tuyến
- **Thực tế tăng cường**: Triển khai nhận diện và theo dõi đối tượng thời gian thực cho các ứng dụng AR
- **Giám sát sức khỏe**: Chạy các mô hình phân tích sức khỏe trên thiết bị đeo và thiết bị y tế
- **Hệ thống tự động**: Thực hiện các mô hình ra quyết định cho máy bay không người lái, robot và phương tiện

### Cơ sở hạ tầng tính toán tại biên
- **Trung tâm dữ liệu biên**: Triển khai các mô hình AI trong các trung tâm dữ liệu biên cho các ứng dụng độ trễ thấp
- **Tích hợp CDN**: Tích hợp khả năng xử lý AI vào các mạng phân phối nội dung
- **Biên 5G**: Tận dụng tính toán biên 5G cho các ứng dụng hỗ trợ AI
- **Tính toán sương mù**: Thực hiện xử lý AI trong các môi trường tính toán sương mù

## Cài đặt và thiết lập

### Cài đặt tiện ích mở rộng
Cài đặt tiện ích mở rộng Bộ công cụ AI trực tiếp từ Visual Studio Code Marketplace:

**ID tiện ích mở rộng**: `ms-windows-ai-studio.windows-ai-studio`

**Phương pháp cài đặt**:
1. **VS Code Marketplace**: Tìm kiếm "AI Toolkit" trong chế độ xem Extensions
2. **Dòng lệnh**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Cài đặt trực tiếp**: Tải xuống từ [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Yêu cầu trước khi phát triển AI tại biên
- **Visual Studio Code**: Khuyến nghị phiên bản mới nhất
- **Môi trường Python**: Python 3.8+ với các thư viện AI cần thiết
- **ONNX Runtime** (Tùy chọn): Để suy luận mô hình ONNX
- **Ollama** (Tùy chọn): Để phục vụ mô hình cục bộ
- **Công cụ tăng tốc phần cứng**: CUDA, OpenVINO hoặc các bộ tăng tốc cụ thể của nền tảng

### Cấu hình ban đầu
1. **Kích hoạt tiện ích mở rộng**: Mở VS Code và xác minh Bộ công cụ AI xuất hiện trong Activity Bar
2. **Cài đặt nhà cung cấp mô hình**: Cấu hình truy cập vào GitHub, OpenAI, Anthropic hoặc các nhà cung cấp mô hình khác
3. **Môi trường cục bộ**: Thiết lập môi trường Python và cài đặt các gói cần thiết
4. **Tăng tốc phần cứng**: Cấu hình tăng tốc GPU/NPU nếu có
5. **Tích hợp MCP**: Thiết lập các máy chủ Model Context Protocol nếu cần

###
2. Tạo các gợi ý ban đầu bằng mô tả ngôn ngữ tự nhiên  
3. Lặp lại và tinh chỉnh gợi ý dựa trên phản hồi của mô hình  
4. Tích hợp công cụ MCP để nâng cao khả năng của tác nhân  

#### Bước 3: Kiểm tra và Đánh giá  
1. Sử dụng **Bulk Run** để kiểm tra nhiều gợi ý trên các mô hình đã chọn  
2. Chạy các tác nhân với các trường hợp kiểm tra để xác thực chức năng  
3. Đánh giá độ chính xác và hiệu suất bằng các chỉ số tích hợp hoặc tùy chỉnh  
4. So sánh các mô hình và cấu hình khác nhau  

#### Bước 4: Tinh chỉnh và Tối ưu hóa  
1. Tùy chỉnh mô hình cho các trường hợp sử dụng đặc biệt  
2. Áp dụng tinh chỉnh theo lĩnh vực cụ thể  
3. Tối ưu hóa cho các hạn chế triển khai tại biên  
4. Phiên bản hóa và so sánh các cấu hình tác nhân khác nhau  

#### Bước 5: Chuẩn bị Triển khai  
1. Tạo mã sẵn sàng sản xuất bằng Agent Builder  
2. Thiết lập kết nối máy chủ MCP cho mục đích sản xuất  
3. Chuẩn bị các gói triển khai cho thiết bị biên  
4. Cấu hình các chỉ số giám sát và đánh giá  

## Mẫu cho Bộ công cụ AI  

Thử các mẫu của chúng tôi  
[Mẫu Bộ công cụ AI](https://github.com/Azure-Samples/AI_Toolkit_Samples) được thiết kế để giúp các nhà phát triển và nhà nghiên cứu khám phá và triển khai các giải pháp AI một cách hiệu quả.  

Các mẫu của chúng tôi bao gồm:  

Mã mẫu: Các ví dụ được xây dựng sẵn để minh họa các chức năng AI, như huấn luyện, triển khai hoặc tích hợp mô hình vào ứng dụng.  
Tài liệu: Hướng dẫn và tài liệu giúp người dùng hiểu các tính năng của Bộ công cụ AI và cách sử dụng chúng.  
Yêu cầu  

- Visual Studio Code  
- Bộ công cụ AI cho Visual Studio Code  
- GitHub Fine-grained personal access token (PAT)  
- Foundry Local  

## Thực hành tốt nhất cho Phát triển AI tại Biên  

### Lựa chọn Mô hình  
- **Hạn chế kích thước**: Chọn các mô hình phù hợp với giới hạn bộ nhớ của thiết bị mục tiêu  
- **Tốc độ suy luận**: Ưu tiên các mô hình có tốc độ suy luận nhanh cho ứng dụng thời gian thực  
- **Cân nhắc độ chính xác**: Cân bằng độ chính xác của mô hình với các hạn chế về tài nguyên  
- **Tương thích định dạng**: Ưu tiên định dạng ONNX hoặc tối ưu hóa phần cứng cho triển khai tại biên  

### Kỹ thuật Tối ưu hóa  
- **Quantization**: Sử dụng quantization INT8 hoặc INT4 để giảm kích thước mô hình và cải thiện tốc độ  
- **Pruning**: Loại bỏ các tham số mô hình không cần thiết để giảm yêu cầu tính toán  
- **Knowledge Distillation**: Tạo các mô hình nhỏ hơn nhưng vẫn duy trì hiệu suất của mô hình lớn  
- **Tăng tốc phần cứng**: Tận dụng NPUs, GPUs hoặc các bộ tăng tốc chuyên dụng khi có  

### Quy trình Phát triển  
- **Kiểm tra lặp lại**: Kiểm tra thường xuyên trong điều kiện giống biên trong quá trình phát triển  
- **Giám sát hiệu suất**: Liên tục giám sát việc sử dụng tài nguyên và tốc độ suy luận  
- **Quản lý phiên bản**: Theo dõi các phiên bản mô hình và cài đặt tối ưu hóa  
- **Tài liệu hóa**: Ghi lại tất cả các quyết định tối ưu hóa và cân nhắc hiệu suất  

### Cân nhắc Triển khai  
- **Giám sát tài nguyên**: Giám sát bộ nhớ, CPU và mức tiêu thụ năng lượng trong sản xuất  
- **Chiến lược dự phòng**: Triển khai cơ chế dự phòng cho các lỗi mô hình  
- **Cơ chế cập nhật**: Lên kế hoạch cho các cập nhật mô hình và quản lý phiên bản  
- **Bảo mật**: Triển khai các biện pháp bảo mật phù hợp cho ứng dụng AI tại biên  

## Tích hợp với Các Khung AI tại Biên  

### ONNX Runtime  
- **Triển khai đa nền tảng**: Triển khai các mô hình ONNX trên các nền tảng biên khác nhau  
- **Tối ưu hóa phần cứng**: Tận dụng các tối ưu hóa phần cứng cụ thể của ONNX Runtime  
- **Hỗ trợ di động**: Sử dụng ONNX Runtime Mobile cho các ứng dụng trên điện thoại thông minh và máy tính bảng  
- **Tích hợp IoT**: Triển khai trên các thiết bị IoT bằng các phân phối nhẹ của ONNX Runtime  

### Windows ML  
- **Thiết bị Windows**: Tối ưu hóa cho các thiết bị biên và PC chạy Windows  
- **Tăng tốc NPU**: Tận dụng Neural Processing Units trên các thiết bị Windows  
- **DirectML**: Sử dụng DirectML để tăng tốc GPU trên nền tảng Windows  
- **Tích hợp UWP**: Tích hợp với các ứng dụng Universal Windows Platform  

### TensorFlow Lite  
- **Tối ưu hóa di động**: Triển khai các mô hình TensorFlow Lite trên thiết bị di động và nhúng  
- **Đại diện phần cứng**: Sử dụng các đại diện phần cứng chuyên dụng để tăng tốc  
- **Vi điều khiển**: Triển khai trên vi điều khiển bằng TensorFlow Lite Micro  
- **Hỗ trợ đa nền tảng**: Triển khai trên Android, iOS và hệ thống Linux nhúng  

### Azure IoT Edge  
- **Kết hợp đám mây-biên**: Kết hợp huấn luyện trên đám mây với suy luận tại biên  
- **Triển khai module**: Triển khai các mô hình AI dưới dạng module IoT Edge  
- **Quản lý thiết bị**: Quản lý thiết bị biên và cập nhật mô hình từ xa  
- **Telemetry**: Thu thập dữ liệu hiệu suất và chỉ số mô hình từ các triển khai tại biên  

## Các Kịch bản AI tại Biên Nâng cao  

### Triển khai Nhiều Mô hình  
- **Tập hợp mô hình**: Triển khai nhiều mô hình để cải thiện độ chính xác hoặc dự phòng  
- **Kiểm tra A/B**: Kiểm tra đồng thời các mô hình khác nhau trên thiết bị biên  
- **Lựa chọn động**: Chọn mô hình dựa trên điều kiện hiện tại của thiết bị  
- **Chia sẻ tài nguyên**: Tối ưu hóa việc sử dụng tài nguyên giữa các mô hình được triển khai  

### Học Liên kết  
- **Huấn luyện phân tán**: Huấn luyện mô hình trên nhiều thiết bị biên  
- **Bảo vệ quyền riêng tư**: Giữ dữ liệu huấn luyện tại chỗ trong khi chia sẻ cải tiến mô hình  
- **Học tập hợp tác**: Cho phép các thiết bị học hỏi từ kinh nghiệm chung  
- **Phối hợp biên-đám mây**: Phối hợp học tập giữa các thiết bị biên và hạ tầng đám mây  

### Xử lý Thời gian Thực  
- **Xử lý luồng**: Xử lý các luồng dữ liệu liên tục trên thiết bị biên  
- **Suy luận độ trễ thấp**: Tối ưu hóa để giảm thiểu độ trễ suy luận  
- **Xử lý theo lô**: Xử lý hiệu quả các lô dữ liệu trên thiết bị biên  
- **Xử lý thích ứng**: Điều chỉnh xử lý dựa trên khả năng hiện tại của thiết bị  

## Khắc phục sự cố Phát triển AI tại Biên  

### Các Vấn đề Thường Gặp  
- **Hạn chế bộ nhớ**: Mô hình quá lớn so với bộ nhớ của thiết bị mục tiêu  
- **Tốc độ suy luận**: Suy luận mô hình quá chậm so với yêu cầu thời gian thực  
- **Suy giảm độ chính xác**: Tối ưu hóa làm giảm độ chính xác của mô hình một cách không chấp nhận được  
- **Tương thích phần cứng**: Mô hình không tương thích với phần cứng mục tiêu  

### Chiến lược Gỡ lỗi  
- **Phân tích hiệu suất**: Sử dụng các tính năng theo dõi của Bộ công cụ AI để xác định các điểm nghẽn  
- **Giám sát tài nguyên**: Giám sát việc sử dụng bộ nhớ và CPU trong quá trình phát triển  
- **Kiểm tra từng bước**: Kiểm tra các tối ưu hóa từng bước để xác định vấn đề  
- **Mô phỏng phần cứng**: Sử dụng các công cụ phát triển để mô phỏng phần cứng mục tiêu  

### Giải pháp Tối ưu hóa  
- **Quantization thêm**: Áp dụng các kỹ thuật quantization mạnh mẽ hơn  
- **Kiến trúc mô hình**: Xem xét các kiến trúc mô hình khác được tối ưu hóa cho biên  
- **Tối ưu hóa tiền xử lý**: Tối ưu hóa tiền xử lý dữ liệu cho các hạn chế tại biên  
- **Tối ưu hóa suy luận**: Sử dụng các tối ưu hóa suy luận cụ thể cho phần cứng  

## Tài nguyên và Bước Tiếp theo  

### Tài liệu Chính thức  
- [Tài liệu Nhà phát triển Bộ công cụ AI](https://aka.ms/AIToolkit/doc)  
- [Hướng dẫn Cài đặt và Thiết lập](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Tài liệu Ứng dụng Thông minh VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Tài liệu Giao thức Ngữ cảnh Mô hình (MCP)](https://modelcontextprotocol.io/)  

### Cộng đồng và Hỗ trợ  
- [Kho GitHub Bộ công cụ AI](https://github.com/microsoft/vscode-ai-toolkit)  
- [Vấn đề và Yêu cầu Tính năng trên GitHub](https://aka.ms/AIToolkit/feedback)  
- [Cộng đồng Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace Tiện ích Mở rộng VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tài nguyên Kỹ thuật  
- [Tài liệu ONNX Runtime](https://onnxruntime.ai/)  
- [Tài liệu Ollama](https://ollama.ai/)  
- [Tài liệu Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Tài liệu Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Lộ trình Học tập  
- [Khóa học Cơ bản về AI tại Biên](../Module01/README.md)  
- [Hướng dẫn Mô hình Ngôn ngữ Nhỏ](../Module02/README.md)  
- [Chiến lược Triển khai tại Biên](../Module03/README.md)  
- [Phát triển AI tại Biên trên Windows](./windowdeveloper.md)  

### Tài nguyên Bổ sung  
- **Thống kê Kho**: Hơn 1.8k sao, hơn 150 fork, hơn 18 cộng tác viên  
- **Giấy phép**: Giấy phép MIT  
- **Bảo mật**: Áp dụng chính sách bảo mật của Microsoft  
- **Telemetry**: Tôn trọng cài đặt telemetry của VS Code  

## Kết luận  

Bộ công cụ AI cho Visual Studio Code đại diện cho một nền tảng toàn diện cho phát triển AI hiện đại, cung cấp khả năng phát triển tác nhân được tối ưu hóa đặc biệt cho các ứng dụng AI tại biên. Với danh mục mô hình phong phú hỗ trợ các nhà cung cấp như Anthropic, OpenAI, GitHub, và Google, kết hợp với khả năng thực thi cục bộ thông qua ONNX và Ollama, bộ công cụ này mang lại sự linh hoạt cần thiết cho các kịch bản triển khai tại biên đa dạng.  

Điểm mạnh của bộ công cụ nằm ở cách tiếp cận tích hợp—từ khám phá và thử nghiệm mô hình trong Playground đến phát triển tác nhân tinh vi với Prompt Builder, khả năng đánh giá toàn diện, và tích hợp liền mạch công cụ MCP. Đối với các nhà phát triển AI tại biên, điều này có nghĩa là tạo mẫu nhanh và kiểm tra các tác nhân AI trước khi triển khai tại biên, với khả năng lặp lại nhanh chóng và tối ưu hóa cho các môi trường hạn chế tài nguyên.  

Những lợi thế chính cho phát triển AI tại biên bao gồm:  
- **Thử nghiệm nhanh**: Kiểm tra mô hình và tác nhân nhanh chóng trước khi triển khai tại biên  
- **Linh hoạt đa nhà cung cấp**: Truy cập các mô hình từ nhiều nguồn để tìm giải pháp tối ưu tại biên  
- **Phát triển cục bộ**: Kiểm tra với ONNX và Ollama để phát triển ngoại tuyến và bảo vệ quyền riêng tư  
- **Sẵn sàng sản xuất**: Tạo mã sẵn sàng sản xuất và tích hợp với các công cụ bên ngoài qua MCP  
- **Đánh giá toàn diện**: Sử dụng các chỉ số tích hợp và tùy chỉnh để xác thực hiệu suất AI tại biên  

Khi AI tiếp tục hướng tới các kịch bản triển khai tại biên, Bộ công cụ AI cho VS Code cung cấp môi trường phát triển và quy trình làm việc cần thiết để xây dựng, kiểm tra, và tối ưu hóa các ứng dụng thông minh cho các môi trường hạn chế tài nguyên. Dù bạn đang phát triển các giải pháp IoT, ứng dụng AI di động, hay hệ thống trí tuệ nhúng, bộ công cụ này với bộ tính năng toàn diện và quy trình làm việc tích hợp hỗ trợ toàn bộ vòng đời phát triển AI tại biên.  

Với sự phát triển liên tục và cộng đồng hoạt động tích cực (hơn 1.8k sao trên GitHub), Bộ công cụ AI vẫn dẫn đầu trong các công cụ phát triển AI, không ngừng phát triển để đáp ứng nhu cầu của các nhà phát triển AI hiện đại xây dựng cho các kịch bản triển khai tại biên.  

[Next Foundry Local](./foundrylocal.md)  

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.