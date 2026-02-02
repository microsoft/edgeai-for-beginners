# Sổ Tay Workshop

> **Sổ tay Jupyter tương tác để học Edge AI thực hành**
>
> Các hướng dẫn tiến bộ, tự học từ cơ bản về hoàn thành hội thoại đến hệ thống đa tác nhân nâng cao sử dụng Microsoft Foundry Local và các Mô hình Ngôn ngữ Nhỏ.

---

## 📖 Giới thiệu

Chào mừng bạn đến với bộ sưu tập **Sổ tay Workshop EdgeAI cho Người Mới Bắt Đầu**. Những sổ tay Jupyter tương tác này mang đến trải nghiệm học tập thực hành, nơi bạn sẽ viết, thực thi và thử nghiệm mã Edge AI trong thời gian thực.

### Tại sao lại là Sổ tay Jupyter?

Khác với các hướng dẫn truyền thống, những sổ tay này cung cấp:

- **Học tập tương tác**: Chạy các ô mã và xem kết quả ngay lập tức
- **Thử nghiệm**: Thay đổi tham số và quan sát sự thay đổi trong thời gian thực
- **Tài liệu**: Các giải thích trực tiếp và ô markdown hướng dẫn bạn qua các khái niệm
- **Khả năng tái sử dụng**: Các ví dụ hoàn chỉnh có thể tham khảo và sử dụng lại
- **Hình ảnh hóa**: Xem các chỉ số hiệu suất, embeddings và kết quả trực tiếp

### Điều gì làm cho những sổ tay này đặc biệt?

Mỗi sổ tay được thiết kế theo **các thực hành tốt nhất sẵn sàng cho sản xuất**:

✅ **Xử lý lỗi toàn diện** - Giảm thiểu lỗi một cách duyên dáng và cung cấp thông báo lỗi thông tin  
✅ **Gợi ý kiểu và tài liệu** - Chữ ký hàm rõ ràng và docstrings  
✅ **Theo dõi hiệu suất** - Theo dõi sử dụng token và đo lường độ trễ  
✅ **Thiết kế mô-đun** - Các mẫu có thể tái sử dụng để bạn điều chỉnh cho dự án của mình  
✅ **Phức tạp tiến bộ** - Xây dựng dựa trên các buổi học trước một cách hệ thống

---

## 🎯 Mục tiêu học tập

### Kỹ năng cốt lõi bạn sẽ phát triển

Khi làm việc qua các sổ tay này, bạn sẽ thành thạo:

1. **Quản lý Dịch vụ AI Cục bộ**
   - Cấu hình và quản lý các dịch vụ Microsoft Foundry Local
   - Chọn và tải các mô hình phù hợp với phần cứng của bạn
   - Theo dõi sử dụng tài nguyên và tối ưu hóa hiệu suất
   - Xử lý khám phá dịch vụ và kiểm tra sức khỏe

2. **Phát triển Ứng dụng AI**
   - Triển khai hoàn thành hội thoại tương thích với OpenAI tại chỗ
   - Xây dựng giao diện streaming để cải thiện trải nghiệm người dùng
   - Thiết kế các lời nhắc hiệu quả cho các Mô hình Ngôn ngữ Nhỏ
   - Tích hợp các mô hình cục bộ vào ứng dụng

3. **Tạo Dữ liệu Tăng cường Truy xuất (RAG)**
   - Tạo tìm kiếm ngữ nghĩa với embeddings vector
   - Căn cứ phản hồi LLM vào các tài liệu cụ thể theo lĩnh vực
   - Đánh giá chất lượng RAG với các chỉ số RAGAS
   - Mở rộng từ nguyên mẫu đến sản xuất

4. **Tối ưu hóa Hiệu suất**
   - Đánh giá nhiều mô hình một cách hệ thống
   - Đo lường độ trễ, thông lượng và thời gian token đầu tiên
   - So sánh Mô hình Ngôn ngữ Nhỏ với Mô hình Ngôn ngữ Lớn
   - Chọn mô hình tối ưu dựa trên sự đánh đổi giữa hiệu suất/chất lượng

5. **Điều phối Đa Tác Nhân**
   - Thiết kế các tác nhân chuyên biệt cho các nhiệm vụ khác nhau
   - Triển khai bộ nhớ tác nhân và quản lý ngữ cảnh
   - Phối hợp nhiều tác nhân trong các quy trình phức tạp
   - Xây dựng các mẫu điều phối cho sự hợp tác giữa các tác nhân

6. **Định tuyến Mô hình Thông minh**
   - Triển khai phát hiện ý định và khớp mẫu
   - Tự động định tuyến truy vấn đến các mô hình phù hợp
   - Xây dựng các pipeline nhiều bước (lập kế hoạch → thực thi → tinh chỉnh)
   - Thiết kế kiến trúc mô hình như công cụ có khả năng mở rộng

---

## 🎓 Kết quả học tập

### Những gì bạn sẽ xây dựng

| Sổ tay | Thành phẩm | Kỹ năng thể hiện | Độ khó |
|--------|------------|------------------|--------|
| **Buổi 01** | Ứng dụng chat với streaming | Cài đặt dịch vụ, hoàn thành cơ bản, UX streaming | ⭐ Người mới bắt đầu |
| **Buổi 02 (RAG)** | Pipeline RAG với đánh giá | Embeddings, tìm kiếm ngữ nghĩa, chỉ số chất lượng | ⭐⭐ Trung cấp |
| **Buổi 02 (Đánh giá)** | Bộ đánh giá chất lượng RAG | Chỉ số RAGAS, đánh giá hệ thống | ⭐⭐ Trung cấp |
| **Buổi 03** | Đánh giá nhiều mô hình | Đo lường hiệu suất, so sánh mô hình | ⭐⭐ Trung cấp |
| **Buổi 04** | So sánh SLM và LLM | Phân tích sự đánh đổi, chiến lược tối ưu hóa | ⭐⭐⭐ Nâng cao |
| **Buổi 05** | Điều phối đa tác nhân | Thiết kế tác nhân, bộ nhớ, phối hợp | ⭐⭐⭐ Nâng cao |
| **Buổi 06 (Định tuyến)** | Hệ thống định tuyến thông minh | Phát hiện ý định, chọn mô hình | ⭐⭐⭐ Nâng cao |
| **Buổi 06 (Pipeline)** | Pipeline nhiều bước | Quy trình lập kế hoạch/thực thi/tinh chỉnh | ⭐⭐⭐ Nâng cao |

### Tiến trình năng lực

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Lịch trình Workshop

### 🚀 Workshop Nửa Ngày (3.5 giờ)

**Hoàn hảo cho: Các buổi đào tạo nhóm, hackathon, workshop hội nghị**

| Thời gian | Thời lượng | Buổi | Chủ đề | Hoạt động |
|-----------|------------|------|--------|-----------|
| **0:00** | 30 phút | Cài đặt & Giới thiệu | Cài đặt môi trường, cài đặt Foundry Local | Cài đặt phụ thuộc, xác minh thiết lập |
| **0:30** | 30 phút | Buổi 01 | Hoàn thành hội thoại cơ bản, streaming | Chạy sổ tay, chỉnh sửa lời nhắc |
| **1:00** | 45 phút | Buổi 02 | Pipeline RAG, embeddings, đánh giá | Xây dựng hệ thống RAG, kiểm tra truy vấn |
| **1:45** | 15 phút | Nghỉ | ☕ Cà phê & câu hỏi | — |
| **2:00** | 30 phút | Buổi 03 | Đánh giá nhiều mô hình | So sánh 3+ mô hình |
| **2:30** | 30 phút | Buổi 04 | Sự đánh đổi giữa SLM và LLM | Phân tích hiệu suất/chất lượng |
| **3:00** | 30 phút | Buổi 05-06 | Hệ thống đa tác nhân & định tuyến | Khám phá các mẫu nâng cao |

**Thành phẩm**: Người tham dự sẽ rời đi với 6 ứng dụng Edge AI hoạt động và các mẫu mã sẵn sàng cho sản xuất.

---

### 🎓 Workshop Cả Ngày (6 giờ)

**Hoàn hảo cho: Đào tạo chuyên sâu, bootcamp, khóa học đại học**

| Thời gian | Thời lượng | Buổi | Chủ đề | Hoạt động |
|-----------|------------|------|--------|-----------|
| **0:00** | 45 phút | Cài đặt & Lý thuyết | Cài đặt môi trường, các nguyên tắc cơ bản về Edge AI | Cài đặt, xác minh, thảo luận trường hợp sử dụng |
| **0:45** | 45 phút | Buổi 01 | Hoàn thành hội thoại chuyên sâu | Triển khai hội thoại cơ bản & streaming |
| **1:30** | 30 phút | Nghỉ | ☕ Cà phê & kết nối | — |
| **2:00** | 60 phút | Buổi 02 (Cả hai) | Pipeline RAG + Đánh giá RAGAS | Xây dựng hệ thống RAG hoàn chỉnh |
| **3:00** | 30 phút | Phòng thực hành 1 | RAG tùy chỉnh cho lĩnh vực của bạn | Áp dụng vào tài liệu của riêng bạn |
| **3:30** | 30 phút | Ăn trưa | 🍽️ | — |
| **4:00** | 45 phút | Buổi 03 | Phương pháp đánh giá | So sánh mô hình một cách hệ thống |
| **4:45** | 45 phút | Buổi 04 | Chiến lược tối ưu hóa | Phân tích SLM và LLM |
| **5:30** | 60 phút | Buổi 05-06 | Điều phối nâng cao | Hệ thống đa tác nhân, định tuyến |
| **6:30** | 30 phút | Phòng thực hành 2 | Xây dựng hệ thống tác nhân tùy chỉnh | Thiết kế bộ điều phối của riêng bạn |

**Thành phẩm**: Hiểu sâu về các mẫu Edge AI cộng với 2 dự án tùy chỉnh.

---

### 📚 Học Tự Chọn (2 tuần)

**Hoàn hảo cho: Người học cá nhân, khóa học trực tuyến, tự học**

#### Tuần 1: Nền tảng (6 giờ)

| Ngày | Trọng tâm | Thời lượng | Sổ tay | Bài tập về nhà |
|------|-----------|------------|--------|----------------|
| **Thứ Hai** | Cài đặt & Cơ bản | 1.5 giờ | Buổi 01 | Chỉnh sửa lời nhắc, kiểm tra streaming |
| **Thứ Tư** | Nguyên tắc RAG | 2 giờ | Buổi 02 (cả hai) | Thêm tài liệu của riêng bạn |
| **Thứ Sáu** | Đánh giá | 1.5 giờ | Buổi 03 | So sánh thêm các mô hình |
| **Thứ Bảy** | Ôn tập & Thực hành | 1 giờ | Tất cả Tuần 1 | Hoàn thành bài tập, gỡ lỗi |

#### Tuần 2: Nâng cao (5 giờ)

| Ngày | Trọng tâm | Thời lượng | Sổ tay | Bài tập về nhà |
|------|-----------|------------|--------|----------------|
| **Thứ Hai** | Tối ưu hóa | 1.5 giờ | Buổi 04 | Tài liệu hóa sự đánh đổi |
| **Thứ Tư** | Hệ thống Đa Tác Nhân | 2 giờ | Buổi 05 | Thiết kế tác nhân tùy chỉnh |
| **Thứ Sáu** | Định tuyến Thông minh | 1.5 giờ | Buổi 06 (cả hai) | Xây dựng logic định tuyến |
| **Thứ Bảy** | Dự án Cuối | 2 giờ | Tích hợp | Kết hợp nhiều mẫu |

**Thành phẩm**: Thành thạo các mẫu Edge AI cộng với dự án danh mục đầu tư.

---

## 📔 Mô tả Sổ tay

### 📘 Buổi 01: Khởi động Chat
**Tệp**: `session01_chat_bootstrap.ipynb`  
**Thời lượng**: 20-30 phút  
**Yêu cầu trước**: Không có  
**Độ khó**: ⭐ Người mới bắt đầu

**Những gì bạn sẽ học**:
- Cài đặt và cấu hình Foundry Local Python SDK
- Sử dụng `FoundryLocalManager` để tự động khám phá dịch vụ
- Triển khai hoàn thành hội thoại cơ bản với API tương thích OpenAI
- Xây dựng phản hồi streaming để cải thiện trải nghiệm người dùng
- Xử lý lỗi và dịch vụ không khả dụng một cách duyên dáng

**Khái niệm chính**: Quản lý dịch vụ, hoàn thành hội thoại, streaming, xử lý lỗi

**Bạn sẽ xây dựng**: Ứng dụng chat tương tác với hỗ trợ streaming

---

### 📗 Buổi 02: Pipeline RAG
**Tệp**: `session02_rag_pipeline.ipynb`  
**Thời lượng**: 30-45 phút  
**Yêu cầu trước**: Buổi 01  
**Độ khó**: ⭐⭐ Trung cấp

**Những gì bạn sẽ học**:
- Triển khai mẫu Tạo Dữ liệu Tăng cường Truy xuất (RAG)
- Tạo embeddings vector với sentence-transformers
- Xây dựng tìm kiếm ngữ nghĩa với độ tương đồng cosine
- Căn cứ phản hồi LLM vào tài liệu theo lĩnh vực
- Xử lý các phụ thuộc tùy chọn với import guards

**Khái niệm chính**: Kiến trúc RAG, embeddings, tìm kiếm ngữ nghĩa, độ tương đồng vector

**Bạn sẽ xây dựng**: Hệ thống hỏi-đáp dựa trên tài liệu

---

### 📗 Buổi 02: Đánh giá RAG với RAGAS
**Tệp**: `session02_rag_eval_ragas.ipynb`  
**Thời lượng**: 30-45 phút  
**Yêu cầu trước**: Buổi 02 Pipeline RAG  
**Độ khó**: ⭐⭐ Trung cấp

**Những gì bạn sẽ học**:
- Đánh giá chất lượng RAG với các chỉ số tiêu chuẩn ngành
- Đo lường sự liên quan của ngữ cảnh, sự liên quan của câu trả lời, tính trung thực
- Sử dụng framework RAGAS để đánh giá hệ thống
- Xác định và sửa các vấn đề chất lượng RAG
- Xây dựng tập dữ liệu đánh giá cho lĩnh vực của bạn

**Khái niệm chính**: Đánh giá RAG, chỉ số RAGAS, đo lường chất lượng, kiểm tra hệ thống

**Bạn sẽ xây dựng**: Framework đánh giá chất lượng RAG

---

### 📙 Buổi 03: Đánh giá Mô hình OSS
**Tệp**: `session03_benchmark_oss_models.ipynb`  
**Thời lượng**: 30-45 phút  
**Yêu cầu trước**: Buổi 01  
**Độ khó**: ⭐⭐ Trung cấp

**Những gì bạn sẽ học**:
- Đánh giá nhiều mô hình một cách hệ thống
- Đo lường độ trễ, thông lượng, thời gian token đầu tiên
- Triển khai giảm thiểu lỗi một cách duyên dáng khi mô hình thất bại
- So sánh hiệu suất giữa các họ mô hình
- Hình ảnh hóa và phân tích kết quả đánh giá

**Khái niệm chính**: Đánh giá hiệu suất, đo lường độ trễ, so sánh mô hình, phân tích thống kê

**Bạn sẽ xây dựng**: Bộ đánh giá nhiều mô hình

---

### 📙 Buổi 04: So sánh Mô hình (SLM vs LLM)
**Tệp**: `session04_model_compare.ipynb`  
**Thời lượng**: 30-45 phút  
**Yêu cầu trước**: Buổi 01, 03  
**Độ khó**: ⭐⭐⭐ Nâng cao

**Những gì bạn sẽ học**:
- So sánh Mô hình Ngôn ngữ Nhỏ với Mô hình Ngôn ngữ Lớn
- Phân tích sự đánh đổi giữa hiệu suất và chất lượng
- Đo lường các chỉ số phù hợp với edge
- Chọn mô hình tối ưu cho các ràng buộc triển khai
- Tài liệu hóa tiêu chí quyết định cho việc chọn mô hình

**Khái niệm chính**: Chọn mô hình, phân tích sự đánh đổi, chiến lược tối ưu hóa, lập kế hoạch triển khai

**Bạn sẽ xây dựng**: Framework so sánh SLM và LLM

---

### 📕 Buổi 05: Điều phối Đa Tác Nhân
**Tệp**: `session05_agents_orchestrator.ipynb`  
**Thời lượng**: 45-60 phút  
**Yêu cầu trước**: Buổi 01-02  
**Độ khó**: ⭐⭐⭐ Nâng cao

**Những gì bạn sẽ học**:
- Thiết kế các tác nhân chuyên biệt cho các nhiệm vụ khác nhau
- Triển khai bộ nhớ tác nhân và quản lý ngữ cảnh
- Xây dựng các mẫu điều phối cho sự hợp tác giữa các tác nhân
- Xử lý giao tiếp và chuyển giao giữa các tác nhân
- Theo dõi hiệu suất hệ thống đa tác nhân

**Khái niệm chính**: Kiến trúc tác nhân, mẫu điều phối, quản lý bộ nhớ, điều phối tác nhân

**Bạn sẽ xây dựng**: Hệ thống đa tác nhân với bộ điều phối và các chuyên gia

---

### 📕 Buổi 06: Định tuyến Mô hình
**Tệp**: `session06_models_router.ipynb`  
**Thời lượng**: 30-45 phút  
**Yêu cầu trước**: Buổi 01, 03  
**Độ khó**: ⭐⭐⭐ Nâng cao

**Những gì bạn sẽ học**:
- Triển khai phát hiện ý định và khớp mẫu
- Xây dựng định tuyến mô hình dựa trên từ khóa
- Tự động định tuyến truy vấn đến các mô hình phù hợp
- Cấu hình các registry mô hình đa dạng
- Theo dõi quyết định định tuyến và hiệu suất

**Khái niệm chính**: Phát hiện ý định, định tuyến mô hình, khớp mẫu, chọn lựa thông minh

**Bạn sẽ xây dựng**: Hệ thống định tuyến mô hình thông minh

---

### 📕 Buổi 06: Pipeline Nhiều Bước
**Tệp**: `session06_models_pipeline.ipynb`  
**Thời lượng**: 30-45 phút  
**Yêu cầu trước**: Buổi 01, 06 Định tuyến  
**Độ khó**: ⭐⭐⭐ Nâng cao

**Những gì bạn sẽ học**:
- Xây dựng các pipeline AI nhiều bước (lập kế hoạch → thực thi → tinh chỉnh)
- T
- Thiết kế kiến trúc mô hình như công cụ có khả năng mở rộng

**Khái niệm chính**: Kiến trúc pipeline, xử lý nhiều giai đoạn, khôi phục lỗi, mô hình mở rộng

**Bạn sẽ xây dựng**: Pipeline thông minh nhiều bước với định tuyến

---

## 🚀 Bắt đầu

### Yêu cầu trước

**Yêu cầu hệ thống**:
- **Hệ điều hành**: Windows 10/11, macOS 11+, hoặc Linux (Ubuntu 20.04+)
- **RAM**: Tối thiểu 8GB, khuyến nghị 16GB+
- **Dung lượng lưu trữ**: Tối thiểu 10GB trống cho các mô hình
- **Phần cứng**: CPU hỗ trợ AVX2; GPU (CUDA, Qualcomm NPU) tùy chọn

**Yêu cầu phần mềm**:
- **Python 3.8+** với pip
- **Jupyter Notebook** hoặc **VS Code** với extension Jupyter
- **Microsoft Foundry Local** đã cài đặt và cấu hình
- **Git** (để clone repository)

### Các bước cài đặt

#### 1. Cài đặt Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Xác minh cài đặt**:
```bash
foundry --version
```

#### 2. Thiết lập môi trường Python

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Khởi động Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Mở Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Xác minh nhanh

Chạy đoạn mã này trong một ô Python để kiểm tra thiết lập:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Kết quả mong đợi**: Một phản hồi chào hỏi từ mô hình cục bộ.

---

## 📝 Thực hành tốt nhất trong workshop

### Dành cho giảng viên

**Trước workshop**:
- ✅ Gửi hướng dẫn cài đặt trước 1 tuần
- ✅ Kiểm tra tất cả notebook trên phần cứng mục tiêu
- ✅ Chuẩn bị hướng dẫn xử lý sự cố cho các vấn đề phổ biến
- ✅ Có sẵn các mô hình dự phòng (phi-3.5-mini nếu phi-4-mini không hoạt động)
- ✅ Thiết lập kênh chat chung để giải đáp thắc mắc

**Trong workshop**:
- ✅ Bắt đầu với kiểm tra nhanh môi trường (5 phút)
- ✅ Chia sẻ tài liệu xử lý sự cố ngay lập tức
- ✅ Khuyến khích thử nghiệm và chỉnh sửa
- ✅ Sử dụng thời gian nghỉ hợp lý (sau mỗi 2 phiên)
- ✅ Có trợ giảng hỗ trợ 1-1

**Sau workshop**:
- ✅ Chia sẻ notebook hoàn chỉnh và giải pháp
- ✅ Cung cấp liên kết đến tài liệu bổ sung
- ✅ Tạo khảo sát phản hồi để cải thiện
- ✅ Cung cấp giờ hỗ trợ để giải đáp thắc mắc sau workshop

### Dành cho học viên

**Tối đa hóa việc học của bạn**:
- ✅ Hoàn thành thiết lập trước khi workshop bắt đầu
- ✅ Tự chạy từng ô mã (đừng chỉ đọc)
- ✅ Thử nghiệm với các tham số và gợi ý
- ✅ Ghi chú lại những điều học được và các vấn đề gặp phải
- ✅ Đặt câu hỏi khi gặp khó khăn (người khác có thể cũng có cùng câu hỏi)

**Những lỗi thường gặp cần tránh**:
- ❌ Bỏ qua thứ tự chạy các ô mã (chạy tuần tự)
- ❌ Không đọc kỹ thông báo lỗi
- ❌ Vội vàng mà không hiểu rõ
- ❌ Bỏ qua các giải thích trong markdown
- ❌ Không lưu lại các notebook đã chỉnh sửa

**Mẹo xử lý lỗi**:
1. **Dịch vụ không chạy**: Kiểm tra `foundry service status`
2. **Lỗi nhập khẩu**: Xác minh môi trường ảo đã được kích hoạt
3. **Không tìm thấy mô hình**: Chạy `foundry model ls` để liệt kê các mô hình đã tải
4. **Hiệu suất chậm**: Kiểm tra mức sử dụng RAM, đóng các ứng dụng khác
5. **Kết quả không mong đợi**: Khởi động lại kernel và chạy tất cả các ô từ đầu

---

## 🔗 Tài liệu bổ sung

### Tài liệu workshop

- **[Hướng dẫn chính của workshop](../Readme.md)** - Tổng quan, mục tiêu học tập, kết quả nghề nghiệp
- **[Mẫu Python](../../../../Workshop/samples)** - Các script Python tương ứng cho từng phiên
- **[Hướng dẫn phiên](../../../../Workshop)** - Hướng dẫn chi tiết bằng markdown (Session01-06)
- **[Scripts](../../../../Workshop/scripts)** - Công cụ xác thực và kiểm tra
- **[Xử lý sự cố](./TROUBLESHOOTING.md)** - Các vấn đề phổ biến và giải pháp
- **[Bắt đầu nhanh](./quickstart.md)** - Hướng dẫn bắt đầu nhanh

### Tài liệu

- **[Tài liệu Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Tài liệu chính thức của Microsoft
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Tham khảo SDK của OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Tài liệu về mô hình embedding
- **[Khung RAGAS](https://docs.ragas.io/)** - Các chỉ số đánh giá RAG

### Cộng đồng

- **[Thảo luận trên GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Đặt câu hỏi, chia sẻ dự án
- **[Discord Azure AI Foundry](https://discord.com/invite/ByRwuEEgH4)** - Hỗ trợ cộng đồng theo thời gian thực
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Hỏi đáp kỹ thuật

---

## 🎯 Lộ trình học tập được khuyến nghị

### Lộ trình dành cho người mới bắt đầu (Bắt đầu từ đây)

1. **Phiên 01** - Khởi động Chat
2. **Phiên 02** - Pipeline RAG
3. **Phiên 03** - Đánh giá mô hình

**Thời gian**: ~2 giờ | **Trọng tâm**: Các mẫu cơ bản

---

### Lộ trình trung cấp

1. Hoàn thành lộ trình dành cho người mới bắt đầu
2. **Phiên 02** - Đánh giá RAG
3. **Phiên 04** - So sánh mô hình

**Thời gian**: ~4 giờ | **Trọng tâm**: Chất lượng và tối ưu hóa

---

### Lộ trình nâng cao (Workshop đầy đủ)

1. Hoàn thành lộ trình trung cấp
2. **Phiên 05** - Điều phối đa tác nhân
3. **Phiên 06** - Định tuyến mô hình
4. **Phiên 06** - Pipeline nhiều bước

**Thời gian**: ~6 giờ | **Trọng tâm**: Các mẫu sản xuất

---

### Lộ trình dự án tùy chỉnh

1. Hoàn thành lộ trình dành cho người mới bắt đầu (Phiên 01-03)
2. Chọn MỘT phiên nâng cao dựa trên mục tiêu của bạn:
   - **Xây dựng ứng dụng RAG?** → Phiên 02 Đánh giá
   - **Tối ưu hóa hiệu suất?** → Phiên 04 So sánh
   - **Quy trình phức tạp?** → Phiên 05 Điều phối
   - **Kiến trúc mở rộng?** → Phiên 06 Định tuyến + Pipeline

**Thời gian**: ~3 giờ | **Trọng tâm**: Kỹ năng theo dự án

---

## 📊 Các tiêu chí thành công

Theo dõi tiến độ của bạn với các cột mốc sau:

- [ ] **Hoàn thành thiết lập** - Foundry Local chạy, tất cả phụ thuộc đã cài đặt
- [ ] **Chat đầu tiên** - Hoàn thành Phiên 01, chat streaming hoạt động
- [ ] **Xây dựng RAG** - Hoàn thành Phiên 02, hệ thống QA tài liệu hoạt động
- [ ] **Đánh giá mô hình** - Hoàn thành Phiên 03, thu thập dữ liệu hiệu suất
- [ ] **Phân tích đánh đổi** - Hoàn thành Phiên 04, tiêu chí chọn mô hình được ghi lại
- [ ] **Điều phối tác nhân** - Hoàn thành Phiên 05, hệ thống đa tác nhân hoạt động
- [ ] **Định tuyến được triển khai** - Hoàn thành Phiên 06, lựa chọn mô hình thông minh hoạt động
- [ ] **Dự án tùy chỉnh** - Áp dụng các mẫu workshop vào trường hợp sử dụng của bạn

---

## 🤝 Đóng góp

Phát hiện vấn đề hoặc có đề xuất? Chúng tôi hoan nghênh đóng góp!

- **Báo cáo vấn đề**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Đề xuất cải tiến**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Gửi PRs**: Làm theo [Hướng dẫn đóng góp](../../AGENTS.md)

---

## 📄 Giấy phép

Workshop này là một phần của repository [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) và được cấp phép theo [Giấy phép MIT](../../../../LICENSE).

---

**Sẵn sàng xây dựng các ứng dụng Edge AI sẵn sàng sản xuất?**  
**Bắt đầu với [Phiên 01: Khởi động Chat](./session01_chat_bootstrap.ipynb) →**

---

*Cập nhật lần cuối: 8 tháng 10, 2025 | Phiên bản Workshop: 2.0*

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.