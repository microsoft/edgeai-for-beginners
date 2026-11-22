# Bộ Công Cụ AI cho Visual Studio Code - Hướng Dẫn Phát Triển AI Biên

## Giới Thiệu

Chào mừng bạn đến với hướng dẫn toàn diện về việc sử dụng Bộ Công Cụ AI cho Visual Studio Code trong phát triển AI Biên. Khi trí tuệ nhân tạo chuyển từ điện toán đám mây tập trung sang các thiết bị biên phân tán, các nhà phát triển cần các công cụ tích hợp mạnh mẽ có thể xử lý các thách thức đặc thù của việc triển khai biên - từ hạn chế về tài nguyên đến yêu cầu hoạt động ngoại tuyến.

Bộ Công Cụ AI cho Visual Studio Code kết nối khoảng cách này bằng cách cung cấp một môi trường phát triển hoàn chỉnh được thiết kế đặc biệt để xây dựng, thử nghiệm và tối ưu hóa các ứng dụng AI chạy hiệu quả trên các thiết bị biên. Dù bạn phát triển cho cảm biến IoT, thiết bị di động, hệ thống nhúng hay máy chủ biên, bộ công cụ này sẽ tinh gọn toàn bộ quy trình phát triển trong môi trường VS Code quen thuộc.

Hướng dẫn này sẽ dẫn bạn qua những khái niệm thiết yếu, công cụ và thực tiễn tốt nhất để tận dụng Bộ Công Cụ AI trong các dự án AI Biên của bạn, từ lựa chọn mô hình ban đầu đến triển khai sản xuất.

## Tổng Quan

Bộ Công Cụ AI cho Visual Studio Code là một tiện ích mở rộng mạnh mẽ, giúp đơn giản hóa việc phát triển tác nhân và tạo ứng dụng AI. Bộ công cụ cung cấp khả năng toàn diện để khám phá, đánh giá và triển khai các mô hình AI từ nhiều nhà cung cấp khác nhau — bao gồm Anthropic, OpenAI, GitHub, Google — đồng thời hỗ trợ thực thi mô hình cục bộ sử dụng ONNX và Ollama.

Điểm nổi bật của Bộ Công Cụ AI là cách tiếp cận toàn diện trong vòng đời phát triển AI. Không giống các công cụ phát triển AI truyền thống tập trung vào từng khía cạnh đơn lẻ, Bộ Công Cụ AI cung cấp một môi trường tích hợp, bao phủ phát hiện mô hình, thử nghiệm, phát triển tác nhân, đánh giá, và triển khai — tất cả đều trong môi trường VS Code quen thuộc.

Nền tảng này được thiết kế riêng cho việc tạo mẫu nhanh và triển khai sản xuất, với các tính năng như tạo prompt, các khởi đầu nhanh, tích hợp liền mạch công cụ MCP (Model Context Protocol), và khả năng đánh giá mở rộng. Đối với phát triển AI Biên, điều này có nghĩa là bạn có thể phát triển, thử nghiệm và tối ưu hóa ứng dụng AI cho các kịch bản triển khai biên một cách hiệu quả trong khi duy trì toàn bộ quy trình phát triển trong VS Code.

## Mục Tiêu Học Tập

Đến cuối hướng dẫn này, bạn sẽ có khả năng:

### Các Năng Lực Cốt Lõi
- **Cài đặt và cấu hình** Bộ Công Cụ AI cho Visual Studio Code cho các quy trình phát triển AI Biên
- **Điều hướng và sử dụng** giao diện Bộ Công Cụ AI, bao gồm Danh Mục Mô Hình, Playground, và Agent Builder
- **Lựa chọn và đánh giá** các mô hình AI phù hợp cho triển khai biên dựa trên hiệu suất và giới hạn tài nguyên
- **Chuyển đổi và tối ưu hóa** mô hình bằng định dạng ONNX và kỹ thuật lượng tử hóa cho thiết bị biên

### Kỹ Năng Phát Triển AI Biên
- **Thiết kế và triển khai** các ứng dụng AI Biên sử dụng môi trường phát triển tích hợp
- **Thực hiện kiểm thử mô hình** trong điều kiện giống biên sử dụng suy luận cục bộ và giám sát tài nguyên
- **Tạo và tùy chỉnh** các tác nhân AI được tối ưu cho các kịch bản triển khai biên
- **Đánh giá hiệu suất mô hình** sử dụng các chỉ số liên quan đến điện toán biên (độ trễ, sử dụng bộ nhớ, độ chính xác)

### Tối Ưu Hóa và Triển Khai
- **Áp dụng kỹ thuật lượng tử hóa và cắt tỉa** để giảm kích thước mô hình trong khi giữ hiệu suất chấp nhận được
- **Tối ưu hóa mô hình** cho các nền tảng phần cứng biên cụ thể bao gồm tăng tốc CPU, GPU và NPU
- **Triển khai các thực hành tốt nhất** cho phát triển AI Biên bao gồm quản lý tài nguyên và chiến lược dự phòng
- **Chuẩn bị mô hình và ứng dụng** cho triển khai sản xuất trên các thiết bị biên

### Khái Niệm Nâng Cao về AI Biên
- **Tích hợp với các framework AI biên** bao gồm ONNX Runtime, Windows ML, và TensorFlow Lite
- **Triển khai kiến trúc đa mô hình** và kịch bản học liên kết cho môi trường biên
- **Khắc phục sự cố phổ biến của AI Biên** bao gồm hạn chế bộ nhớ, tốc độ suy luận và tương thích phần cứng
- **Thiết kế chiến lược giám sát và ghi nhật ký** cho ứng dụng AI biên trong sản xuất

### Ứng Dụng Thực Tiễn
- **Xây dựng giải pháp AI Biên đầu-cuối** từ lựa chọn mô hình đến triển khai
- **Thể hiện sự thành thạo** trong các quy trình phát triển cụ thể cho biên và kỹ thuật tối ưu hóa
- **Áp dụng các khái niệm đã học** vào các trường hợp sử dụng AI biên thực tế bao gồm IoT, di động và ứng dụng nhúng
- **Đánh giá và so sánh** các chiến lược triển khai AI biên khác nhau và những đánh đổi của chúng

## Tính Năng Chính cho Phát Triển AI Biên

### 1. Danh Mục Mô Hình và Khám Phá
- **Hỗ trợ đa nhà cung cấp**: Duyệt và truy cập các mô hình AI từ Anthropic, OpenAI, GitHub, Google và các nhà cung cấp khác
- **Tích hợp mô hình cục bộ**: Khám phá đơn giản các mô hình ONNX và Ollama cho triển khai biên
- **Mô hình GitHub**: Tích hợp trực tiếp với lưu trữ mô hình của GitHub để truy cập thuận tiện
- **So sánh mô hình**: So sánh mô hình cạnh nhau để tìm sự cân bằng tối ưu cho giới hạn thiết bị biên

### 2. Playground Tương Tác
- **Môi trường thử nghiệm tương tác**: Thử nghiệm nhanh với khả năng mô hình trong môi trường kiểm soát
- **Hỗ trợ đa phương thức**: Thử nghiệm với hình ảnh, văn bản và các đầu vào khác thường thấy trong kịch bản biên
- **Thử nghiệm thời gian thực**: Phản hồi ngay lập tức về phản hồi và hiệu suất mô hình
- **Tối ưu tham số**: Tinh chỉnh tham số mô hình cho yêu cầu triển khai biên

### 3. Trình Tạo Prompt (Agent)
- **Tạo ngôn ngữ tự nhiên**: Sinh prompt khởi đầu sử dụng mô tả ngôn ngữ tự nhiên
- **Tinh chỉnh lặp đi lặp lại**: Cải thiện prompt dựa trên phản hồi và hiệu suất mô hình
- **Phân rã tác vụ**: Phân tách các tác vụ phức tạp với xâu chuỗi prompt và đầu ra có cấu trúc
- **Hỗ trợ biến**: Sử dụng biến trong prompt để hành vi tác nhân linh hoạt
- **Sinh mã sản xuất**: Tạo mã sẵn sàng cho sản xuất để phát triển ứng dụng nhanh chóng

### 4. Chạy Hàng Loạt và Đánh Giá
- **Kiểm thử đa mô hình**: Thực hiện nhiều prompt trên các mô hình được chọn cùng lúc
- **Kiểm thử hiệu quả quy mô lớn**: Thử nhiều đầu vào và cấu hình một cách hiệu quả
- **Trường hợp kiểm thử tùy chỉnh**: Chạy tác nhân với các trường hợp kiểm thử để xác thực chức năng
- **So sánh hiệu suất**: So sánh kết quả giữa các mô hình và cấu hình khác nhau

### 5. Đánh Giá Mô Hình với Bộ Dữ Liệu
- **Chỉ số chuẩn**: Kiểm thử mô hình AI sử dụng trình đánh giá tích hợp (điểm F1, mức độ liên quan, sự tương đồng, tính mạch lạc)
- **Trình đánh giá tùy chỉnh**: Tạo chỉ số đánh giá riêng cho các trường hợp sử dụng cụ thể
- **Tích hợp bộ dữ liệu**: Kiểm thử mô hình với các bộ dữ liệu toàn diện
- **Đo lường hiệu suất**: Định lượng hiệu năng mô hình cho quyết định triển khai biên

### 6. Khả Năng Tinh Chỉnh
- **Tùy chỉnh mô hình**: Tùy biến mô hình cho các trường hợp sử dụng và lĩnh vực cụ thể
- **Thích nghi chuyên sâu**: Điều chỉnh mô hình với các lĩnh vực chuyên biệt và yêu cầu riêng
- **Tối ưu biên**: Tinh chỉnh mô hình đặc biệt cho các giới hạn triển khai biên
- **Đào tạo theo miền**: Tạo mô hình phù hợp với các trường hợp sử dụng biên cụ thể

### 7. Tích Hợp Công Cụ MCP
- **Kết nối công cụ bên ngoài**: Kết nối tác nhân với các công cụ bên ngoài qua máy chủ Model Context Protocol
- **Hành động thực tế**: Cho phép tác nhân truy vấn cơ sở dữ liệu, truy cập API hoặc thi hành logic tùy chỉnh
- **Máy chủ MCP hiện có**: Sử dụng công cụ từ lệnh (stdio) hoặc HTTP (sự kiện do máy chủ gửi) giao thức
- **Phát triển MCP tùy chỉnh**: Xây dựng và tạo khung máy chủ MCP mới với kiểm thử trong Agent Builder

### 8. Phát Triển và Kiểm Thử Tác Nhân
- **Hỗ trợ gọi hàm**: Cho phép tác nhân gọi các hàm bên ngoài một cách động
- **Kiểm thử tích hợp thời gian thực**: Kiểm tra các tích hợp với các lần chạy thực và sử dụng công cụ
- **Kiểm soát phiên bản tác nhân**: Quản lý phiên bản cho tác nhân với khả năng so sánh kết quả đánh giá
- **Gỡ lỗi và theo dõi**: Khả năng theo dõi và gỡ lỗi cục bộ cho phát triển tác nhân

## Quy Trình Phát Triển AI Biên

### Giai Đoạn 1: Khám Phá và Lựa Chọn Mô Hình
1. **Khám phá Danh Mục Mô Hình**: Sử dụng danh mục mô hình để tìm mô hình phù hợp cho triển khai biên
2. **So sánh hiệu suất**: Đánh giá mô hình dựa trên kích thước, độ chính xác và tốc độ suy luận
3. **Thử nghiệm cục bộ**: Sử dụng mô hình Ollama hoặc ONNX để thử nghiệm cục bộ trước khi triển khai biên
4. **Đánh giá yêu cầu tài nguyên**: Xác định nhu cầu bộ nhớ và tính toán cho thiết bị biên mục tiêu

### Giai Đoạn 2: Tối Ưu Hóa Mô Hình
1. **Chuyển đổi sang ONNX**: Chuyển đổi mô hình đã chọn sang định dạng ONNX cho khả năng tương thích biên
2. **Áp dụng lượng tử hóa**: Giảm kích thước mô hình thông qua lượng tử hóa INT8 hoặc INT4
3. **Tối ưu hóa phần cứng**: Tối ưu cho phần cứng biên mục tiêu (ARM, x86, bộ tăng tốc chuyên biệt)
4. **Xác thực hiệu suất**: Đảm bảo mô hình tối ưu hóa vẫn duy trì độ chính xác chấp nhận được

### Giai Đoạn 3: Phát Triển Ứng Dụng
1. **Thiết kế tác nhân**: Sử dụng Agent Builder để tạo các tác nhân AI tối ưu cho biên
2. **Kỹ thuật prompt**: Phát triển các prompt hoạt động hiệu quả với các mô hình biên nhỏ hơn
3. **Kiểm thử tích hợp**: Thử tác nhân trong các điều kiện mô phỏng biên
4. **Sinh mã**: Tạo mã sản xuất tối ưu cho triển khai biên

### Giai Đoạn 4: Đánh Giá và Thử Nghiệm
1. **Đánh giá hàng loạt**: Thử nhiều cấu hình để tìm cài đặt biên tối ưu
2. **Phân tích hiệu năng**: Phân tích tốc độ suy luận, sử dụng bộ nhớ và độ chính xác
3. **Mô phỏng biên**: Thử nghiệm trong môi trường giống môi trường triển khai biên mục tiêu
4. **Kiểm thử chịu tải**: Đánh giá hiệu suất dưới các điều kiện tải khác nhau

### Giai Đoạn 5: Chuẩn Bị Triển Khai
1. **Tối ưu hóa cuối cùng**: Áp dụng các tối ưu cuối cùng dựa trên kết quả thử nghiệm
2. **Đóng gói triển khai**: Đóng gói mô hình và mã cho triển khai biên
3. **Tài liệu**: Ghi chép yêu cầu và cấu hình triển khai
4. **Thiết lập giám sát**: Chuẩn bị giám sát và ghi nhật ký cho triển khai biên

## Đối Tượng Mục Tiêu cho Phát Triển AI Biên

### Nhà Phát Triển AI Biên
- Nhà phát triển ứng dụng xây dựng thiết bị biên và giải pháp IoT tích hợp AI
- Nhà phát triển hệ thống nhúng tích hợp khả năng AI vào thiết bị hạn chế tài nguyên
- Nhà phát triển di động tạo ứng dụng AI trên thiết bị cho điện thoại và máy tính bảng

### Kỹ Sư AI Biên
- Kỹ sư AI tối ưu mô hình cho triển khai biên và quản lý pipeline suy luận
- Kỹ sư DevOps triển khai và quản lý mô hình AI trên hạ tầng biên phân tán
- Kỹ sư hiệu năng tối ưu tải AI theo giới hạn phần cứng biên

### Nhà Nghiên Cứu và Giảng Viên
- Nhà nghiên cứu AI phát triển mô hình và thuật toán hiệu quả cho điện toán biên
- Giảng viên giảng dạy khái niệm AI biên và minh họa kỹ thuật tối ưu hóa
- Sinh viên học về thách thức và giải pháp trong triển khai AI biên

## Các Trường Hợp Sử Dụng AI Biên

### Thiết Bị IoT Thông Minh
- **Nhận diện hình ảnh thời gian thực**: Triển khai mô hình thị giác máy trên camera và cảm biến IoT
- **Xử lý giọng nói**: Triển khai nhận dạng giọng nói và xử lý ngôn ngữ tự nhiên trên loa thông minh
- **Bảo trì dự đoán**: Chạy mô hình phát hiện bất thường trên thiết bị biên công nghiệp
- **Giám sát môi trường**: Triển khai mô hình phân tích dữ liệu cảm biến cho các ứng dụng môi trường

### Ứng Dụng Di Động và Nhúng
- **Phiên dịch trên thiết bị**: Triển khai mô hình dịch ngôn ngữ hoạt động ngoại tuyến
- **Thực tế tăng cường**: Triển khai nhận diện và theo dõi đối tượng thời gian thực cho ứng dụng AR
- **Giám sát sức khỏe**: Chạy mô hình phân tích sức khỏe trên thiết bị đeo và thiết bị y tế
- **Hệ thống tự chủ**: Triển khai mô hình ra quyết định cho drone, robot và xe cộ

### Hạ Tầng Điện Toán Biên
- **Trung tâm dữ liệu biên**: Triển khai mô hình AI trong trung tâm dữ liệu biên cho các ứng dụng độ trễ thấp
- **Tích hợp CDN**: Tích hợp khả năng xử lý AI vào mạng phân phối nội dung
- **Biên 5G**: Tận dụng điện toán biên 5G cho các ứng dụng tích hợp AI
- **Điện toán sương mù**: Triển khai xử lý AI trong môi trường điện toán sương mù

## Cài Đặt và Thiết Lập

### Cài Đặt Tiện Ích Mở Rộng
Cài đặt tiện ích mở rộng AI Toolkit trực tiếp từ Visual Studio Code Marketplace:

**ID Tiện Ích**: `ms-windows-ai-studio.windows-ai-studio`

**Phương thức cài đặt**:
1. **VS Code Marketplace**: Tìm kiếm "AI Toolkit" trong cửa sổ Extensions
2. **Dòng lệnh**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Cài đặt trực tiếp**: Tải từ [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Yêu Cầu Tiền Tạo cho Phát Triển AI Biên
- **Visual Studio Code**: Phiên bản mới nhất được khuyến nghị
- **Môi trường Python**: Python 3.8+ với các thư viện AI cần thiết
- **ONNX Runtime** (Tùy chọn): Cho suy luận mô hình ONNX
- **Ollama** (Tùy chọn): Cho phục vụ mô hình cục bộ
- **Công cụ tăng tốc phần cứng**: CUDA, OpenVINO, hoặc bộ tăng tốc chuyên biệt nền tảng

### Cấu Hình Ban Đầu
1. **Kích hoạt tiện ích mở rộng**: Mở VS Code và xác nhận AI Toolkit xuất hiện trên Thanh Hoạt Động
2. **Thiết lập nhà cung cấp mô hình**: Cấu hình truy cập GitHub, OpenAI, Anthropic hoặc các nhà cung cấp mô hình khác
3. **Môi trường cục bộ**: Thiết lập môi trường Python và cài đặt các gói cần thiết
4. **Tăng tốc phần cứng**: Cấu hình tăng tốc GPU/NPU nếu có
5. **Tích hợp MCP**: Thiết lập máy chủ Model Context Protocol nếu cần

### Danh Sách Kiểm Tra Cấu Hình Lần Đầu
- [ ] Tiện ích AI Toolkit đã được cài đặt và kích hoạt
- [ ] Danh mục mô hình có thể truy cập và mô hình có thể khám phá
- [ ] Playground hoạt động để thử nghiệm mô hình
- [ ] Agent Builder có thể truy cập để phát triển prompt
- [ ] Môi trường phát triển cục bộ đã được cấu hình
- [ ] Tăng tốc phần cứng (nếu có) được cấu hình đúng

## Bắt Đầu Với Bộ Công Cụ AI

### Hướng Dẫn Khởi Đầu Nhanh

Chúng tôi khuyên bạn nên bắt đầu với các mô hình lưu trữ bởi GitHub để có trải nghiệm mượt mà nhất:

1. **Cài đặt**: Thực hiện theo [hướng dẫn cài đặt](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) để thiết lập Bộ Công Cụ AI cho thiết bị của bạn
2. **Khám phá mô hình**: Từ cây tiện ích mở rộng, chọn **CATALOG > Models** để khám phá các mô hình có sẵn
3. **Mô hình GitHub**: Bắt đầu với mô hình do GitHub lưu trữ để tích hợp tối ưu
4. **Thử nghiệm Playground**: Từ bất kỳ thẻ mô hình nào, chọn **Try in Playground** để bắt đầu thử nghiệm khả năng mô hình

### Phát Triển AI Biên Từng Bước

#### Bước 1: Khám phá và Lựa chọn Mô hình
1. Mở giao diện AI Toolkit trong Thanh Hoạt Động VS Code
2. Duyệt Danh Mục Mô Hình để tìm mô hình phù hợp cho triển khai biên
3. Lọc theo nhà cung cấp (GitHub, ONNX, Ollama) dựa trên yêu cầu biên của bạn
4. Sử dụng **Try in Playground** để thử ngay khả năng mô hình

#### Bước 2: Phát Triển Tác Nhân
1. Sử dụng **Prompt (Agent) Builder** để tạo các tác nhân AI tối ưu cho biên
2. Sinh prompt khởi đầu dựa trên mô tả ngôn ngữ tự nhiên
3. Lặp lại và tinh chỉnh prompt dựa trên phản hồi mô hình
4. Tích hợp các công cụ MCP để nâng cao khả năng của tác nhân


#### Bước 3: Kiểm thử và Đánh giá
1. Sử dụng **Bulk Run** để kiểm thử nhiều prompt trên các mô hình được chọn
2. Chạy các agent với các trường hợp kiểm thử để xác nhận chức năng
3. Đánh giá độ chính xác và hiệu năng bằng các chỉ số tích hợp sẵn hoặc tùy chỉnh
4. So sánh các mô hình và cấu hình khác nhau

#### Bước 4: Tinh chỉnh và Tối ưu hóa
1. Tùy chỉnh mô hình cho các trường hợp dùng đặc thù
2. Áp dụng tinh chỉnh chuyên ngành
3. Tối ưu cho các ràng buộc triển khai tại edge
4. Phiên bản hóa và so sánh các cấu hình agent khác nhau

#### Bước 5: Chuẩn bị Triển khai
1. Tạo mã nguồn sẵn sàng sản xuất sử dụng Agent Builder
2. Thiết lập các kết nối server MCP cho sử dụng trong sản xuất
3. Chuẩn bị các gói triển khai cho thiết bị edge
4. Cấu hình các chỉ số giám sát và đánh giá

## Mẫu cho AI Toolkit 

Thử các mẫu của chúng tôi
Các [mẫu AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) được thiết kế để giúp các nhà phát triển và nhà nghiên cứu khám phá và triển khai các giải pháp AI hiệu quả.

Các mẫu của chúng tôi bao gồm:

Mã mẫu: Các ví dụ có sẵn để minh họa chức năng AI, như đào tạo, triển khai, hoặc tích hợp mô hình vào ứng dụng.
Tài liệu: Hướng dẫn và bài học giúp người dùng hiểu các tính năng AI Toolkit và cách sử dụng chúng.
Điều kiện tiên quyết

- Visual Studio Code
- AI Toolkit cho Visual Studio Code
- Token truy cập cá nhân (PAT) có quyền truy cập chi tiết trên GitHub
- Foundry Local

## Các Thực hành Tốt nhất cho Phát triển Edge AI

### Lựa chọn Mô hình
- **Giới hạn Kích thước**: Chọn mô hình phù hợp với giới hạn bộ nhớ của thiết bị mục tiêu
- **Tốc độ suy luận**: Ưu tiên mô hình có thời gian suy luận nhanh cho ứng dụng thời gian thực
- **Đánh đổi Độ chính xác**: Cân bằng độ chính xác của mô hình với giới hạn tài nguyên
- **Tương thích Định dạng**: Ưu tiên định dạng ONNX hoặc định dạng tối ưu phần cứng cho triển khai edge

### Kỹ thuật Tối ưu hóa
- **Lượng tử hóa (Quantization)**: Sử dụng lượng tử hóa INT8 hoặc INT4 để giảm kích thước mô hình và tăng tốc độ
- **Cắt tỉa (Pruning)**: Loại bỏ các tham số mô hình không cần thiết để giảm yêu cầu tính toán
- **Chưng cất Tri thức (Knowledge Distillation)**: Tạo các mô hình nhỏ hơn nhưng duy trì hiệu năng của mô hình lớn hơn
- **Gia tốc phần cứng**: Tận dụng NPU, GPU hoặc bộ gia tốc chuyên biệt khi có sẵn

### Quy trình Phát triển
- **Kiểm thử lặp lại**: Kiểm thử thường xuyên trong điều kiện gần giống với edge trong quá trình phát triển
- **Giám sát Hiệu năng**: Liên tục theo dõi mức sử dụng tài nguyên và tốc độ suy luận
- **Kiểm soát Phiên bản**: Theo dõi các phiên bản mô hình và cài đặt tối ưu hóa
- **Tài liệu**: Ghi lại tất cả các quyết định tối ưu và đánh đổi hiệu năng

### Cân nhắc Triển khai
- **Giám sát tài nguyên**: Theo dõi bộ nhớ, CPU và mức tiêu thụ điện trong môi trường sản xuất
- **Chiến lược Dự phòng**: Triển khai cơ chế dự phòng khi mô hình gặp lỗi
- **Cơ chế Cập nhật**: Lên kế hoạch cho các cập nhật mô hình và quản lý phiên bản
- **Bảo mật**: Thực hiện các biện pháp bảo mật phù hợp cho các ứng dụng AI tại edge

## Tích hợp với các Framework Edge AI

### ONNX Runtime
- **Triển khai đa nền tảng**: Triển khai các mô hình ONNX trên các nền tảng edge khác nhau
- **Tối ưu phần cứng**: Tận dụng các tối ưu phần cứng đặc thù của ONNX Runtime
- **Hỗ trợ di động**: Sử dụng ONNX Runtime Mobile cho các ứng dụng trên smartphone và máy tính bảng
- **Tích hợp IoT**: Triển khai trên các thiết bị IoT bằng các bản phân phối nhẹ của ONNX Runtime

### Windows ML
- **Thiết bị Windows**: Tối ưu cho các thiết bị edge và PC chạy Windows
- **Gia tốc NPU**: Tận dụng Neural Processing Units trên thiết bị Windows
- **DirectML**: Sử dụng DirectML để gia tốc GPU trên nền tảng Windows
- **Tích hợp UWP**: Tích hợp với ứng dụng Universal Windows Platform

### TensorFlow Lite
- **Tối ưu di động**: Triển khai mô hình TensorFlow Lite trên thiết bị di động và nhúng
- **Delegate phần cứng**: Sử dụng các delegate phần cứng chuyên biệt để gia tốc
- **Vi điều khiển**: Triển khai trên bộ vi điều khiển sử dụng TensorFlow Lite Micro
- **Hỗ trợ đa nền tảng**: Triển khai trên Android, iOS và hệ thống Linux nhúng

### Azure IoT Edge
- **Hybrid Đám mây-Edge**: Kết hợp đào tạo trên đám mây với suy luận tại edge
- **Triển khai Module**: Triển khai các mô hình AI dưới dạng module IoT Edge
- **Quản lý Thiết bị**: Quản lý thiết bị edge và cập nhật mô hình từ xa
- **Telemetri**: Thu thập dữ liệu hiệu năng và chỉ số mô hình từ triển khai edge

## Kịch bản Edge AI Nâng cao

### Triển khai đa mô hình
- **Mô hình Tổng hợp (Ensembles)**: Triển khai nhiều mô hình để cải thiện độ chính xác hoặc dự phòng
- **Kiểm thử A/B**: Kiểm thử đồng thời các mô hình khác nhau trên thiết bị edge
- **Lựa chọn Động**: Chọn mô hình dựa trên điều kiện hiện tại của thiết bị
- **Chia sẻ Tài nguyên**: Tối ưu việc sử dụng tài nguyên trên nhiều mô hình triển khai

### Học Liên kết Phân tán (Federated Learning)
- **Đào tạo Phân phối**: Đào tạo mô hình trên nhiều thiết bị edge
- **Bảo mật Quyền Riêng tư**: Giữ dữ liệu đào tạo tại chỗ trong khi chia sẻ cải tiến mô hình
- **Học Cộng tác**: Cho phép các thiết bị học hỏi từ kinh nghiệm tập thể
- **Phối hợp Edge-Cloud**: Phối hợp học giữa thiết bị edge và hạ tầng đám mây

### Xử lý thời gian thực
- **Xử lý luồng dữ liệu**: Xử lý liên tục các luồng dữ liệu trên thiết bị edge
- **Suy luận độ trễ thấp**: Tối ưu để giảm độ trễ suy luận tối thiểu
- **Xử lý theo lô**: Xử lý hiệu quả các lô dữ liệu trên thiết bị edge
- **Xử lý thích ứng**: Điều chỉnh xử lý dựa trên khả năng hiện tại của thiết bị

## Khắc phục sự cố phát triển Edge AI

### Vấn đề Thường gặp
- **Giới hạn bộ nhớ**: Mô hình quá lớn so với bộ nhớ thiết bị mục tiêu
- **Tốc độ suy luận chậm**: Suy luận mô hình quá chậm cho yêu cầu thời gian thực
- **Suy giảm độ chính xác**: Tối ưu hóa làm giảm không chấp nhận được độ chính xác mô hình
- **Tương thích phần cứng**: Mô hình không tương thích với phần cứng mục tiêu

### Chiến lược Gỡ lỗi
- **Phân tích hiệu năng**: Sử dụng tính năng theo dõi của AI Toolkit để xác định nút thắt cổ chai
- **Giám sát tài nguyên**: Theo dõi bộ nhớ và CPU trong quá trình phát triển
- **Kiểm thử Từng bước**: Kiểm thử tối ưu hóa theo từng bước để cô lập lỗi
- **Mô phỏng phần cứng**: Sử dụng công cụ phát triển để mô phỏng phần cứng mục tiêu

### Giải pháp Tối ưu hóa
- **Lượng tử hóa thêm**: Áp dụng kỹ thuật lượng tử hóa mạnh hơn
- **Kiến trúc Mô hình**: Xem xét kiến trúc mô hình khác được tối ưu cho edge
- **Tối ưu hóa tiền xử lý**: Tối ưu tiền xử lý dữ liệu cho giới hạn của edge
- **Tối ưu hóa suy luận**: Sử dụng tối ưu hóa suy luận đặc thù phần cứng

## Tài nguyên và Bước tiếp theo

### Tài liệu chính thức
- [Tài liệu phát triển AI Toolkit](https://aka.ms/AIToolkit/doc)
- [Hướng dẫn cài đặt và thiết lập](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [Tài liệu VS Code Intelligent Apps](https://code.visualstudio.com/docs/intelligentapps)
- [Tài liệu Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

### Cộng đồng và Hỗ trợ
- [Kho lưu trữ AI Toolkit trên GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [Vấn đề và yêu cầu tính năng trên GitHub](https://aka.ms/AIToolkit/feedback)
- [Cộng đồng Azure AI Foundry trên Discord](https://aka.ms/azureaifoundry/discord)
- [Marketplace mở rộng VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Tài nguyên kỹ thuật
- [Tài liệu ONNX Runtime](https://onnxruntime.ai/)
- [Tài liệu Ollama](https://ollama.ai/)
- [Tài liệu Windows ML](https://docs.microsoft.com/en-us/windows/ai/)
- [Tài liệu Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Lộ trình học tập
- [Khóa học cơ bản Edge AI](../Module01/README.md)
- [Hướng dẫn Mô hình Ngôn ngữ Nhỏ](../Module02/README.md)
- [Chiến lược Triển khai Edge](../Module03/README.md)
- [Phát triển Windows Edge AI](./windowdeveloper.md)

### Tài nguyên bổ sung
- **Thống kê kho lưu trữ**: hơn 1.8k sao, hơn 150 nhánh (forks), hơn 18 cộng tác viên
- **Giấy phép**: Giấy phép MIT
- **Bảo mật**: Chính sách bảo mật của Microsoft áp dụng
- **Telemetri**: Tuân thủ cài đặt telemetri của VS Code

## Kết luận

AI Toolkit cho Visual Studio Code đại diện cho một nền tảng toàn diện cho phát triển AI hiện đại, cung cấp khả năng phát triển agent đơn giản hóa đặc biệt hữu ích cho các ứng dụng Edge AI. Với danh mục mô hình rộng lớn hỗ trợ các nhà cung cấp như Anthropic, OpenAI, GitHub và Google, cùng với việc thực thi cục bộ qua ONNX và Ollama, bộ công cụ cung cấp sự linh hoạt cần thiết cho các kịch bản triển khai tại edge đa dạng.

Sức mạnh của toolkit nằm ở cách tiếp cận tích hợp — từ khám phá mô hình và thử nghiệm trên Playground đến phát triển agent chuyên sâu với Prompt Builder, khả năng đánh giá toàn diện và tích hợp mượt mà với công cụ MCP. Đối với các nhà phát triển Edge AI, điều này có nghĩa là có thể tạo mẫu nhanh và kiểm thử các agent AI trước khi triển khai edge, với khả năng lặp nhanh và tối ưu cho môi trường giới hạn tài nguyên.

Các lợi thế chính cho phát triển Edge AI bao gồm:
- **Thử nghiệm nhanh**: Kiểm thử mô hình và agent nhanh trước khi cam kết triển khai edge
- **Linh hoạt đa nhà cung cấp**: Truy cập mô hình từ nhiều nguồn để tìm giải pháp edge tối ưu
- **Phát triển cục bộ**: Kiểm thử với ONNX và Ollama cho phát triển offline và bảo vệ quyền riêng tư
- **Sẵn sàng sản xuất**: Tạo mã nguồn sẵn sàng sản xuất và tích hợp với công cụ bên ngoài qua MCP
- **Đánh giá toàn diện**: Sử dụng chỉ số tích hợp sẵn và tùy chỉnh để xác nhận hiệu năng Edge AI

Khi AI tiếp tục hướng tới các kịch bản triển khai tại edge, AI Toolkit cho VS Code cung cấp môi trường phát triển và quy trình làm việc cần thiết để xây dựng, kiểm thử và tối ưu ứng dụng thông minh trong môi trường giới hạn tài nguyên. Dù bạn đang phát triển giải pháp IoT, ứng dụng AI di động hay hệ thống thông minh nhúng, bộ công cụ với đầy đủ tính năng và quy trình tích hợp hỗ trợ toàn bộ vòng đời phát triển Edge AI.

Với sự phát triển không ngừng và cộng đồng năng động (hơn 1.8k sao trên GitHub), AI Toolkit vẫn là công cụ dẫn đầu trong phát triển AI, liên tục tiến hoá để đáp ứng nhu cầu của các nhà phát triển AI hiện đại xây dựng cho các kịch bản triển khai edge.

[Next Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->