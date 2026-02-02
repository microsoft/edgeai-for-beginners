# Windows 11 Chat Sample - Foundry Local

Một ứng dụng chat hiện đại dành cho Windows 11, tích hợp Microsoft Foundry Local với giao diện gốc đẹp mắt. Được xây dựng bằng Electron và tuân theo các mẫu chính thức của Microsoft Foundry Local.

## Tổng quan

Mẫu này minh họa cách tạo một ứng dụng chat sẵn sàng cho sản xuất, tận dụng các mô hình AI cục bộ thông qua Foundry Local, mang đến cho người dùng các cuộc trò chuyện AI tập trung vào quyền riêng tư mà không phụ thuộc vào đám mây.

## Tính năng

### 🎨 **Thiết kế gốc Windows 11**
- Tích hợp Fluent Design System
- Hiệu ứng vật liệu Mica và độ trong suốt
- Hỗ trợ chủ đề gốc Windows 11
- Bố cục đáp ứng cho mọi kích thước màn hình
- Chuyển đổi tự động giữa chế độ sáng/tối

### 🤖 **Tích hợp mô hình AI**
- Tích hợp dịch vụ Foundry Local
- Hỗ trợ nhiều mô hình với khả năng chuyển đổi nhanh
- Phản hồi trực tuyến theo thời gian thực
- Chuyển đổi giữa mô hình cục bộ và đám mây
- Giám sát sức khỏe và trạng thái của mô hình

### 💬 **Trải nghiệm chat**
- Hiển thị trạng thái đang nhập theo thời gian thực
- Lưu trữ lịch sử tin nhắn
- Xuất các cuộc trò chuyện
- Tùy chỉnh lời nhắc hệ thống
- Quản lý và phân nhánh cuộc trò chuyện

### ⚡ **Tính năng hiệu suất**
- Tải chậm và ảo hóa
- Tối ưu hóa hiển thị cho các cuộc trò chuyện dài
- Tải trước mô hình trong nền
- Quản lý bộ nhớ hiệu quả
- Hiệu ứng chuyển động và chuyển đổi mượt mà

## Kiến trúc

```
┌─────────────────────────────────────────────────────────────┐
│                    Windows 11 Chat App                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Electron UI   │   IPC Bridge    │    Foundry Manager      │
│                 │                 │                         │
│ • Fluent Design │ • Secure Comms  │ • Model Loading         │
│ • Chat Interface│ • Event Routing │ • Health Monitoring     │
│ • Settings      │ • State Sync    │ • Performance Tracking │
│ • Themes        │ • Error Handler │ • Resource Management   │
└─────────────────┴─────────────────┴─────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               Microsoft Foundry Local Service               │
│                                                             │
│ • Local Model Hosting    • OpenAI API Compatibility        │
│ • Real-time Inference    • Model Catalog Management        │
│ • Streaming Responses    • Health & Status Monitoring      │
└─────────────────────────────────────────────────────────────┘
```

## Yêu cầu trước

### Yêu cầu hệ thống
- **Hệ điều hành**: Windows 11 (khuyến nghị 22H2 hoặc mới hơn)
- **RAM**: Tối thiểu 8GB, khuyến nghị 16GB+ cho các mô hình lớn hơn
- **Dung lượng lưu trữ**: Tối thiểu 10GB dung lượng trống cho các mô hình
- **GPU**: Không bắt buộc nhưng khuyến nghị để suy luận nhanh hơn

### Phụ thuộc phần mềm
- **Node.js**: v18.0.0 hoặc mới hơn
- **Foundry Local**: Phiên bản mới nhất từ Microsoft
- **Git**: Để nhân bản và phát triển

## Cài đặt

### 1. Cài đặt Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Nhân bản và thiết lập
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Cấu hình môi trường
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Chạy ứng dụng
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Cấu trúc dự án

```
08/
├── README.md                 # This documentation
├── package.json             # Project dependencies and scripts
├── electron.js              # Main Electron process
├── preload.js              # Secure preload script
├── src/
│   ├── index.html          # Main application UI
│   ├── styles/
│   │   ├── fluent.css      # Windows 11 Fluent Design
│   │   ├── chat.css        # Chat interface styles
│   │   └── themes.css      # Light/Dark theme support
│   ├── scripts/
│   │   ├── app.js          # Main application logic
│   │   ├── chat.js         # Chat functionality
│   │   ├── models.js       # Model management
│   │   ├── settings.js     # Settings and preferences
│   │   └── utils.js        # Utility functions
│   └── assets/
│       ├── icons/          # Application icons
│       ├── sounds/         # Notification sounds
│       └── images/         # UI images and illustrations
├── foundry/
│   ├── manager.js          # Foundry Local integration
│   └── health.js           # Health monitoring
└── build/
    ├── icon.ico            # Windows application icon
    └── installer.nsi       # NSIS installer script
```

## Phân tích chi tiết các tính năng chính

### Tích hợp Windows 11

**Fluent Design System**
- Vật liệu nền Mica
- Hiệu ứng trong suốt Acrylic
- Góc bo tròn và khoảng cách hiện đại
- Bảng màu gốc Windows 11
- Token màu ngữ nghĩa để hỗ trợ truy cập

**Tính năng gốc Windows**
- Tích hợp danh sách nhảy cho các cuộc trò chuyện gần đây
- Thông báo Windows cho tin nhắn mới
- Tiến trình trên thanh tác vụ cho các hoạt động mô hình
- Tích hợp khay hệ thống với các hành động nhanh
- Hỗ trợ xác thực Windows Hello

### Quản lý mô hình AI

**Mô hình cục bộ**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hỗ trợ kết hợp đám mây/cục bộ**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Tính năng giao diện chat

**Phát trực tuyến theo thời gian thực**
- Hiển thị phản hồi từng token một
- Hiệu ứng nhập mượt mà
- Yêu cầu có thể hủy bỏ
- Hiển thị trạng thái đang nhập và trạng thái

**Quản lý cuộc trò chuyện**
- Lưu trữ lịch sử chat
- Xuất/nhập cuộc trò chuyện
- Tìm kiếm và lọc tin nhắn
- Phân nhánh cuộc trò chuyện
- Lời nhắc hệ thống tùy chỉnh cho từng cuộc trò chuyện

**Khả năng truy cập**
- Điều hướng hoàn toàn bằng bàn phím
- Tương thích với trình đọc màn hình
- Hỗ trợ chế độ tương phản cao
- Kích thước phông chữ có thể tùy chỉnh
- Tích hợp nhập liệu bằng giọng nói

## Ví dụ sử dụng

### Tích hợp chat cơ bản
```javascript
// Initialize the chat system
const chat = new ChatManager({
    foundryEndpoint: 'http://localhost:5273',
    defaultModel: 'phi-4-mini',
    streaming: true
});

// Send a message
const response = await chat.sendMessage({
    content: 'Explain quantum computing',
    model: 'phi-4-mini',
    systemPrompt: 'You are a helpful physics teacher.'
});

// Handle streaming responses
chat.on('chunk', (chunk) => {
    appendMessageChunk(chunk.content);
});
```

### Quản lý mô hình
```javascript
// Load a new model
await modelManager.loadModel('qwen2.5-coder-0.5b', {
    showProgress: true,
    autoStart: true
});

// Monitor model performance
modelManager.on('performance', (metrics) => {
    updatePerformanceUI(metrics);
});

// Switch models mid-conversation
await chat.switchModel('phi-4-mini', {
    preserveContext: true
});
```

### Cài đặt và tùy chỉnh
```javascript
// Configure chat behavior
const settings = {
    theme: 'system', // auto, light, dark
    model: 'phi-4-mini',
    streaming: true,
    maxTokens: 1000,
    temperature: 0.7,
    systemPrompt: 'You are a helpful assistant.'
};

await settingsManager.updateSettings(settings);
```

## Tùy chọn cấu hình

### Cài đặt ứng dụng
- **Chủ đề**: Tự động, chế độ sáng, chế độ tối
- **Mô hình**: Lựa chọn mô hình mặc định
- **Hiệu suất**: Cài đặt suy luận
- **Quyền riêng tư**: Chính sách lưu giữ dữ liệu
- **Thông báo**: Cảnh báo tin nhắn
- **Phím tắt**: Phím tắt trên bàn phím

### Cài đặt chat
- **Phát trực tuyến**: Bật/tắt phản hồi theo thời gian thực
- **Độ dài ngữ cảnh**: Bộ nhớ cuộc trò chuyện
- **Nhiệt độ**: Độ sáng tạo của phản hồi
- **Số token tối đa**: Giới hạn độ dài phản hồi
- **Lời nhắc hệ thống**: Hành vi trợ lý mặc định

### Cài đặt mô hình
- **Tự động tải xuống**: Cập nhật mô hình tự động
- **Kích thước bộ nhớ cache**: Giới hạn lưu trữ mô hình cục bộ
- **Chế độ hiệu suất**: Ưu tiên CPU hoặc GPU
- **Kiểm tra sức khỏe**: Khoảng thời gian giám sát

## Phát triển

### Xây dựng từ mã nguồn
```bash
# Install development dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Gỡ lỗi
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Kiểm tra
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Tối ưu hóa hiệu suất

### Quản lý bộ nhớ
- Ảo hóa tin nhắn hiệu quả
- Thu gom rác tự động
- Giám sát bộ nhớ mô hình
- Dọn dẹp tài nguyên khi thoát

### Tối ưu hóa hiển thị
- Cuộn ảo cho các cuộc trò chuyện dài
- Tải chậm lịch sử tin nhắn
- Tối ưu hóa cập nhật React/DOM
- Hiệu ứng chuyển động tăng tốc GPU

### Tối ưu hóa mạng
- Gom kết nối
- Gom yêu cầu
- Logic thử lại tự động
- Hỗ trợ chế độ ngoại tuyến

## Cân nhắc về bảo mật

### Quyền riêng tư dữ liệu
- Kiến trúc ưu tiên cục bộ
- Không truyền dữ liệu lên đám mây (chế độ cục bộ)
- Lưu trữ cuộc trò chuyện được mã hóa
- Quản lý thông tin đăng nhập an toàn

### Bảo mật ứng dụng
- Quy trình renderer được sandbox
- Chính sách bảo mật nội dung (CSP)
- Không thực thi mã từ xa
- Giao tiếp IPC an toàn

## Khắc phục sự cố

### Các vấn đề thường gặp

**Foundry Local không khởi động**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Lỗi tải mô hình**
- Kiểm tra dung lượng ổ đĩa đủ
- Kiểm tra kết nối internet để tải xuống
- Đảm bảo trình điều khiển GPU đã được cập nhật
- Thử các biến thể mô hình khác nhau

**Vấn đề hiệu suất**
- Giám sát tài nguyên hệ thống
- Điều chỉnh cài đặt mô hình
- Bật tăng tốc phần cứng
- Đóng các ứng dụng tiêu tốn tài nguyên khác

### Chế độ gỡ lỗi
Bật ghi nhật ký gỡ lỗi bằng cách thiết lập các biến môi trường:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Đóng góp

### Thiết lập phát triển
1. Fork kho lưu trữ
2. Tạo nhánh tính năng
3. Cài đặt phụ thuộc: `npm install`
4. Thực hiện thay đổi và kiểm tra
5. Gửi yêu cầu kéo

### Phong cách mã hóa
- Cấu hình ESLint được cung cấp
- Prettier để định dạng mã
- TypeScript để đảm bảo kiểu dữ liệu
- Bình luận JSDoc để tài liệu hóa

## Kết quả học tập

Sau khi hoàn thành mẫu này, bạn sẽ hiểu:

1. **Phát triển gốc Windows 11**
   - Triển khai Fluent Design System
   - Tích hợp gốc Windows
   - Các thực hành bảo mật Electron

2. **Tích hợp mô hình AI**
   - Kiến trúc dịch vụ Foundry Local
   - Quản lý vòng đời mô hình
   - Giám sát và tối ưu hóa hiệu suất

3. **Hệ thống chat theo thời gian thực**
   - Xử lý phản hồi phát trực tuyến
   - Quản lý trạng thái cuộc trò chuyện
   - Các mẫu trải nghiệm người dùng

4. **Phát triển ứng dụng sản xuất**
   - Xử lý lỗi và khôi phục
   - Tối ưu hóa hiệu suất
   - Cân nhắc về bảo mật
   - Chiến lược kiểm tra

## Bước tiếp theo

- **Mẫu 09**: Hệ thống điều phối đa tác nhân
- **Mẫu 10**: Foundry Local như tích hợp công cụ
- **Chủ đề nâng cao**: Tinh chỉnh mô hình tùy chỉnh
- **Triển khai**: Các mẫu triển khai doanh nghiệp

## Giấy phép

Mẫu này tuân theo cùng giấy phép với dự án Microsoft Foundry Local.

---

