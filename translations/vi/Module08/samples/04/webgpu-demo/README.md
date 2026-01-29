# WebGPU + ONNX Runtime Demo

Demo này cho thấy cách chạy các mô hình AI trực tiếp trên trình duyệt bằng WebGPU để tăng tốc phần cứng và ONNX Runtime Web.

## Những Điều Được Minh Họa

- **AI trên trình duyệt**: Chạy mô hình hoàn toàn trên trình duyệt
- **Tăng tốc WebGPU**: Suy luận được tăng tốc phần cứng khi khả dụng
- **Ưu tiên quyền riêng tư**: Không có dữ liệu nào rời khỏi thiết bị của bạn
- **Không cần cài đặt**: Hoạt động trên bất kỳ trình duyệt tương thích nào
- **Chuyển đổi linh hoạt**: Tự động chuyển sang CPU nếu WebGPU không khả dụng

## Yêu Cầu

**Tương thích trình duyệt:**
- Chrome/Edge 113+ với WebGPU được kích hoạt
- Kiểm tra trạng thái WebGPU: `chrome://gpu`
- Kích hoạt WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Cách Chạy Demo

### Cách 1: Máy chủ cục bộ (Khuyến nghị)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Cách 2: Live Server trong VS Code

1. Cài đặt tiện ích "Live Server" trong VS Code
2. Nhấp chuột phải vào `index.html` → "Open with Live Server"
3. Demo sẽ tự động mở trong trình duyệt

## Những Gì Bạn Sẽ Thấy

1. **Phát hiện WebGPU**: Kiểm tra khả năng tương thích của trình duyệt
2. **Tải mô hình**: Tải xuống và khởi tạo bộ phân loại MNIST
3. **Thực thi suy luận**: Chạy dự đoán trên dữ liệu mẫu
4. **Thống kê hiệu suất**: Hiển thị thời gian tải và tốc độ suy luận
5. **Hiển thị kết quả**: Độ tin cậy của dự đoán và kết quả thô

## Hiệu Suất Dự Kiến

| Nhà cung cấp thực thi | Tải mô hình | Suy luận | Ghi chú |
|-----------------------|-------------|----------|---------|
| **WebGPU**            | ~2-5s       | ~10-50ms | Tăng tốc phần cứng |
| **CPU (WASM)**        | ~2-5s       | ~50-200ms| Dự phòng phần mềm |

## Xử Lý Sự Cố

**WebGPU Không Khả Dụng:**
- Cập nhật lên Chrome/Edge 113+
- Kích hoạt WebGPU trong `chrome://flags`
- Kiểm tra trình điều khiển GPU đã được cập nhật
- Demo sẽ tự động chuyển sang CPU

**Lỗi Tải:**
- Đảm bảo bạn đang phục vụ qua HTTP (không phải file://)
- Kiểm tra kết nối mạng để tải mô hình
- Xác minh CORS không chặn mô hình ONNX

**Vấn Đề Hiệu Suất:**
- WebGPU cung cấp tốc độ đáng kể so với CPU
- Lần chạy đầu tiên có thể chậm hơn do tải mô hình
- Các lần chạy sau sử dụng bộ nhớ cache của trình duyệt

## Tích Hợp với Foundry Local

Demo WebGPU này bổ sung cho Foundry Local bằng cách minh họa:

- **Suy luận phía client** để tối ưu quyền riêng tư
- **Khả năng offline** khi không có internet  
- **Triển khai tại biên** cho môi trường hạn chế tài nguyên
- **Kiến trúc lai** kết hợp suy luận cục bộ và trên máy chủ

Đối với ứng dụng sản xuất, hãy cân nhắc:
- Sử dụng Foundry Local cho suy luận phía máy chủ
- Sử dụng WebGPU cho tiền xử lý/hậu xử lý phía client
- Triển khai định tuyến thông minh giữa suy luận cục bộ và từ xa

## Chi Tiết Kỹ Thuật

**Mô Hình Sử Dụng:**
- Bộ phân loại chữ số MNIST (định dạng ONNX)
- Đầu vào: Hình ảnh xám 28x28
- Đầu ra: Phân phối xác suất 10 lớp
- Kích thước: ~500KB (tải nhanh)

**ONNX Runtime Web:**
- Nhà cung cấp thực thi WebGPU để tăng tốc GPU
- Nhà cung cấp thực thi WASM cho dự phòng CPU
- Tự động tối ưu hóa và tối ưu hóa đồ thị

**API Trình Duyệt:**
- WebGPU để truy cập phần cứng
- Web Workers để xử lý nền (nâng cấp trong tương lai)
- WebAssembly để tính toán hiệu quả

## Bước Tiếp Theo

- Thử với các mô hình ONNX tùy chỉnh
- Triển khai tải lên hình ảnh thực và phân loại
- Thêm suy luận streaming cho các mô hình lớn hơn
- Tích hợp với đầu vào từ camera/microphone

---

