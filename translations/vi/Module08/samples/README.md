# Module 08 Samples: Hướng dẫn phát triển Foundry Local

## Tổng quan

Bộ sưu tập toàn diện này trình bày cả hai cách tiếp cận **Foundry Local SDK** và **Shell Command** để xây dựng các ứng dụng AI sẵn sàng cho sản xuất. Mỗi mẫu minh họa các khía cạnh khác nhau của phát triển AI tại biên, từ tích hợp REST cơ bản đến hệ thống đa tác nhân nâng cao.

## Cách tiếp cận phát triển: SDK vs Shell Commands

### Sử dụng Foundry Local SDK khi:

- **Kiểm soát chương trình**: Bạn cần kiểm soát toàn diện vòng đời của tác nhân, quy trình đánh giá hoặc triển khai
- **Công cụ tùy chỉnh**: Xây dựng tự động hóa xung quanh Foundry Local (tích hợp CI/CD, điều phối đa tác nhân)
- **Truy cập chi tiết**: Yêu cầu thông tin chi tiết về metadata của tác nhân, phiên bản, hoặc kiểm soát trình đánh giá
- **Tích hợp Python**: Làm việc trong môi trường sử dụng nhiều Python hoặc nhúng logic Foundry vào các ứng dụng rộng hơn
- **Quy trình doanh nghiệp**: Triển khai các quy trình mô-đun và đường dẫn đánh giá có thể tái tạo phù hợp với kiến trúc tham chiếu của Microsoft

### Sử dụng Shell Commands khi:

- **Kiểm tra nhanh**: Thực hiện kiểm tra nhanh tại địa phương, khởi chạy tác nhân thủ công hoặc xác minh thiết lập
- **Đơn giản hóa CLI**: Cần các thao tác CLI đơn giản để khởi động/dừng tác nhân, kiểm tra nhật ký hoặc đánh giá cơ bản
- **Tự động hóa nhẹ**: Viết kịch bản tự động hóa đơn giản mà không cần tích hợp SDK đầy đủ
- **Lặp lại nhanh**: Chu kỳ gỡ lỗi và phát triển, đặc biệt trong môi trường hạn chế hoặc triển khai ở cấp nhóm tài nguyên
- **Thiết lập & xác minh**: Cấu hình môi trường ban đầu và các nhiệm vụ xác minh nhanh

## Thực hành tốt nhất & Quy trình khuyến nghị

Dựa trên quản lý vòng đời tác nhân, theo dõi phụ thuộc và nguyên tắc tái tạo với quyền hạn tối thiểu:

### Giai đoạn 1: Nền tảng & Thiết lập
1. **Bắt đầu với Shell Commands** để thiết lập ban đầu và xác minh nhanh
2. **Xác minh môi trường** bằng công cụ CLI và triển khai mô hình cơ bản
3. **Kiểm tra kết nối** với các cuộc gọi REST đơn giản và kiểm tra trạng thái

### Giai đoạn 2: Phát triển & Tích hợp
1. **Chuyển sang SDK** để có quy trình mở rộng và có thể theo dõi
2. **Triển khai kiểm soát chương trình** cho các tương tác tác nhân phức tạp
3. **Xây dựng công cụ tùy chỉnh** cho các mẫu sẵn sàng cộng đồng và tích hợp Azure OpenAI

### Giai đoạn 3: Sản xuất & Mở rộng
1. **Cách tiếp cận kết hợp** kết hợp CLI cho vận hành và SDK cho logic ứng dụng
2. **Tích hợp doanh nghiệp** với giám sát, ghi nhật ký và đường dẫn triển khai
3. **Đóng góp cộng đồng** thông qua các mẫu có thể tái sử dụng và thực hành tốt nhất

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.