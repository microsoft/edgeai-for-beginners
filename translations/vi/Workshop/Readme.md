<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "04951692a100dcd716df01efca2d3f0d",
  "translation_date": "2025-11-11T23:41:49+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "vi"
}
-->
# EdgeAI cho Người Mới Bắt Đầu - Hội Thảo

> **Lộ trình học thực hành để xây dựng các ứng dụng Edge AI sẵn sàng cho sản xuất**
>
> Làm chủ triển khai AI cục bộ với Microsoft Foundry Local, từ hoàn thành hội thoại đầu tiên đến điều phối đa tác nhân trong 6 buổi học tiến bộ.

---

## 🎯 Giới thiệu

Chào mừng bạn đến với **Hội Thảo EdgeAI cho Người Mới Bắt Đầu** - hướng dẫn thực hành giúp bạn xây dựng các ứng dụng thông minh hoạt động hoàn toàn trên phần cứng cục bộ. Hội thảo này sẽ biến các khái niệm lý thuyết về Edge AI thành các kỹ năng thực tế thông qua các bài tập ngày càng thách thức, sử dụng Microsoft Foundry Local và Small Language Models (SLMs).

### Tại sao nên tham gia hội thảo này?

**Cuộc cách mạng Edge AI đã đến**

Các tổ chức trên toàn thế giới đang chuyển từ AI phụ thuộc vào đám mây sang điện toán biên vì ba lý do quan trọng:

1. **Bảo mật & Tuân thủ** - Xử lý dữ liệu nhạy cảm tại chỗ mà không cần truyền qua đám mây (tuân thủ HIPAA, GDPR, các quy định tài chính)
2. **Hiệu suất** - Loại bỏ độ trễ mạng (50-500ms cục bộ so với 500-2000ms vòng lặp đám mây)
3. **Kiểm soát chi phí** - Loại bỏ chi phí API theo token và mở rộng quy mô mà không cần chi phí đám mây

**Nhưng Edge AI thì khác**

Chạy AI tại chỗ đòi hỏi các kỹ năng mới:
- Lựa chọn và tối ưu hóa mô hình cho các hạn chế tài nguyên
- Quản lý dịch vụ cục bộ và tăng tốc phần cứng
- Kỹ thuật gợi ý cho các mô hình nhỏ hơn
- Mô hình triển khai sản xuất cho các thiết bị biên

**Hội thảo này sẽ cung cấp những kỹ năng đó**

Trong 6 buổi học tập trung (~3 giờ tổng cộng), bạn sẽ tiến từ "Hello World" đến triển khai các hệ thống đa tác nhân sẵn sàng cho sản xuất - tất cả đều chạy cục bộ trên máy của bạn.

---

## 📚 Mục tiêu học tập

Khi hoàn thành hội thảo này, bạn sẽ có thể:

### Năng lực cốt lõi
1. **Triển khai và Quản lý Dịch vụ AI Cục bộ**
   - Cài đặt và cấu hình Microsoft Foundry Local
   - Lựa chọn mô hình phù hợp cho triển khai biên
   - Quản lý vòng đời mô hình (tải xuống, tải lên, lưu trữ)
   - Giám sát sử dụng tài nguyên và tối ưu hóa hiệu suất

2. **Xây dựng Ứng dụng AI**
   - Thực hiện hoàn thành hội thoại tương thích OpenAI cục bộ
   - Thiết kế gợi ý hiệu quả cho Small Language Models
   - Xử lý phản hồi theo luồng để cải thiện trải nghiệm người dùng
   - Tích hợp các mô hình cục bộ vào các ứng dụng hiện có

3. **Tạo Hệ thống RAG (Retrieval Augmented Generation)**
   - Xây dựng tìm kiếm ngữ nghĩa với embeddings
   - Cung cấp phản hồi LLM dựa trên kiến thức cụ thể của lĩnh vực
   - Đánh giá chất lượng RAG với các chỉ số tiêu chuẩn ngành
   - Mở rộng từ nguyên mẫu đến sản xuất

4. **Tối ưu hóa Hiệu suất Mô hình**
   - Đo lường nhiều mô hình cho trường hợp sử dụng của bạn
   - Đo độ trễ, thông lượng và thời gian token đầu tiên
   - Lựa chọn mô hình tối ưu dựa trên sự cân bằng giữa tốc độ/chất lượng
   - So sánh các lựa chọn giữa SLM và LLM trong các tình huống thực tế

5. **Điều phối Hệ thống Đa Tác Nhân**
   - Thiết kế các tác nhân chuyên biệt cho các nhiệm vụ khác nhau
   - Thực hiện quản lý bộ nhớ và ngữ cảnh của tác nhân
   - Điều phối các tác nhân trong các quy trình làm việc phức tạp
   - Định tuyến yêu cầu một cách thông minh qua nhiều mô hình

6. **Triển khai Giải pháp Sẵn sàng Sản xuất**
   - Thực hiện xử lý lỗi và logic thử lại
   - Giám sát sử dụng token và tài nguyên hệ thống
   - Xây dựng kiến trúc có thể mở rộng với mô hình như công cụ
   - Lập kế hoạch lộ trình di chuyển từ biên sang kết hợp (biên + đám mây)

---

## 🎓 Kết quả học tập

### Những gì bạn sẽ xây dựng

Khi kết thúc hội thảo, bạn sẽ tạo ra:

| Buổi học | Thành phẩm | Kỹ năng thể hiện |
|----------|------------|------------------|
| **1** | Ứng dụng chat với phản hồi theo luồng | Cài đặt dịch vụ, hoàn thành cơ bản, UX theo luồng |
| **2** | Hệ thống RAG với đánh giá | Embeddings, tìm kiếm ngữ nghĩa, chỉ số chất lượng |
| **3** | Bộ công cụ đánh giá đa mô hình | Đo lường hiệu suất, so sánh mô hình |
| **4** | Công cụ so sánh SLM và LLM | Phân tích đánh đổi, chiến lược tối ưu hóa |
| **5** | Bộ điều phối đa tác nhân | Thiết kế tác nhân, quản lý bộ nhớ, điều phối |
| **6** | Hệ thống định tuyến thông minh | Phát hiện ý định, lựa chọn mô hình, khả năng mở rộng |

### Ma trận năng lực

| Cấp độ kỹ năng | Buổi 1-2 | Buổi 3-4 | Buổi 5-6 |
|----------------|----------|----------|----------|
| **Người mới** | ✅ Cài đặt & cơ bản | ⚠️ Thách thức | ❌ Quá nâng cao |
| **Trung cấp** | ✅ Ôn tập nhanh | ✅ Học cốt lõi | ⚠️ Mục tiêu mở rộng |
| **Nâng cao** | ✅ Dễ dàng vượt qua | ✅ Tinh chỉnh | ✅ Mẫu sản xuất |

### Kỹ năng sẵn sàng cho nghề nghiệp

**Sau hội thảo này, bạn sẽ sẵn sàng để:**

✅ **Xây dựng Ứng dụng Ưu tiên Bảo mật**
- Ứng dụng chăm sóc sức khỏe xử lý PHI/PII tại chỗ
- Dịch vụ tài chính tuân thủ các yêu cầu pháp lý
- Hệ thống chính phủ với yêu cầu chủ quyền dữ liệu

✅ **Tối ưu hóa cho Môi trường Biên**
- Thiết bị IoT với tài nguyên hạn chế
- Ứng dụng di động ưu tiên ngoại tuyến
- Hệ thống thời gian thực với độ trễ thấp

✅ **Thiết kế Kiến trúc Thông minh**
- Hệ thống đa tác nhân cho quy trình làm việc phức tạp
- Triển khai kết hợp biên-đám mây
- Hạ tầng AI tối ưu hóa chi phí

✅ **Dẫn dắt Các Sáng kiến Edge AI**
- Đánh giá tính khả thi của Edge AI cho các dự án
- Lựa chọn mô hình và khung làm việc phù hợp
- Thiết kế các giải pháp AI cục bộ có thể mở rộng

---

## 🗺️ Cấu trúc hội thảo

### Tổng quan các buổi học (6 buổi × 30 phút = 3 giờ)

| Buổi học | Chủ đề | Trọng tâm | Thời lượng |
|----------|--------|-----------|------------|
| **1** | Bắt đầu với Foundry Local | Cài đặt, xác thực, hoàn thành đầu tiên | 30 phút |
| **2** | Xây dựng Giải pháp AI với RAG | Kỹ thuật gợi ý, embeddings, đánh giá | 30 phút |
| **3** | Mô hình Mã nguồn Mở | Khám phá mô hình, đánh giá, lựa chọn | 30 phút |
| **4** | Mô hình Tiên tiến | SLM vs LLM, tối ưu hóa, khung làm việc | 30 phút |
| **5** | Tác nhân AI | Thiết kế tác nhân, điều phối, bộ nhớ | 30 phút |
| **6** | Mô hình như Công cụ | Định tuyến, chuỗi, chiến lược mở rộng | 30 phút |

---

## 🚀 Bắt đầu nhanh

### Yêu cầu trước

**Yêu cầu hệ thống:**
- **Hệ điều hành**: Windows 10/11, macOS 11+, hoặc Linux (Ubuntu 20.04+)
- **RAM**: Tối thiểu 8GB, khuyến nghị 16GB+
- **Dung lượng lưu trữ**: Tối thiểu 10GB trống cho các mô hình
- **CPU**: Bộ xử lý hiện đại hỗ trợ AVX2
- **GPU** (tùy chọn): Tương thích CUDA hoặc Qualcomm NPU để tăng tốc

**Yêu cầu phần mềm:**
- **Python 3.8+** ([Tải xuống](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Hướng dẫn cài đặt](../../../Workshop))
- **Git** ([Tải xuống](https://git-scm.com/downloads))
- **Visual Studio Code** (khuyến nghị) ([Tải xuống](https://code.visualstudio.com/))

### Cài đặt trong 3 bước

#### 1. Cài đặt Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Xác thực cài đặt:**
```bash
foundry --version
foundry service status
```

**Đảm bảo Azure AI Foundry Local đang chạy với cổng cố định**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Xác thực hoạt động:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Tìm các mô hình có sẵn**
Để xem các mô hình có sẵn trong phiên bản Foundry Local của bạn, bạn có thể truy vấn endpoint mô hình:

```bash
# cmd/bash/powershell
foundry model list
```

Sử dụng Web Endpoint 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Sao chép Repository & Cài đặt Phụ thuộc

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Chạy Mẫu Đầu tiên của Bạn

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Thành công!** Bạn sẽ thấy một phản hồi theo luồng về edge AI.

---

## 📦 Tài nguyên hội thảo

### Mẫu Python

Các ví dụ thực hành tiến bộ minh họa từng khái niệm:

| Buổi học | Mẫu | Mô tả | Thời gian chạy |
|----------|------|-------|----------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Chat cơ bản & theo luồng | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG với embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Đánh giá chất lượng RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Đánh giá đa mô hình | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | So sánh SLM và LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Hệ thống đa tác nhân | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Định tuyến dựa trên ý định | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Chuỗi nhiều bước | ~60s |

### Jupyter Notebooks

Khám phá tương tác với giải thích và hình ảnh hóa:

| Buổi học | Notebook | Mô tả | Độ khó |
|----------|----------|-------|--------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Chat cơ bản & theo luồng | ⭐ Người mới |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Xây dựng hệ thống RAG | ⭐⭐ Trung cấp |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Đánh giá chất lượng RAG | ⭐⭐ Trung cấp |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Đánh giá mô hình | ⭐⭐ Trung cấp |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | So sánh mô hình | ⭐⭐ Trung cấp |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Điều phối tác nhân | ⭐⭐⭐ Nâng cao |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Định tuyến ý định | ⭐⭐⭐ Nâng cao |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Điều phối chuỗi | ⭐⭐⭐ Nâng cao |

### Tài liệu

Hướng dẫn và tham khảo toàn diện:

| Tài liệu | Mô tả | Sử dụng khi nào |
|---------|-------|-----------------|
| [QUICK_START.md](./QUICK_START.md) | Hướng dẫn cài đặt nhanh | Bắt đầu từ đầu |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Tóm tắt lệnh & API | Cần câu trả lời nhanh |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Mẫu & mẫu SDK | Viết mã |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Hướng dẫn biến môi trường | Cấu hình mẫu |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Các vấn đề thường gặp & cách khắc phục | Gỡ lỗi vấn đề |

---

## 🎓 Khuyến nghị lộ trình học tập

### Dành cho Người mới (3-4 giờ)
1. ✅ Buổi 1: Bắt đầu (tập trung vào cài đặt và chat cơ bản)
2. ✅ Buổi 2: RAG cơ bản (bỏ qua đánh giá ban đầu)
3. ✅ Buổi 3: Đánh giá đơn giản (chỉ 2 mô hình)
4. ⏭️ Bỏ qua Buổi 4-6 lúc này
5. 🔄 Quay lại Buổi 4-6 sau khi xây dựng ứng dụng đầu tiên

### Dành cho Nhà phát triển Trung cấp (3 giờ)
1. ⚡ Buổi 1: Xác thực cài đặt nhanh
2. ✅ Buổi 2: Hoàn thành pipeline RAG với đánh giá
3. ✅ Buổi 3: Bộ đánh giá đầy đủ
4. ✅ Buổi 4: Tối ưu hóa mô hình
5. ✅ Buổi 5-6: Tập trung vào mẫu kiến trúc

### Dành cho Người thực hành Nâng cao (2-3 giờ)
1. ⚡ Buổi 1-3: Ôn tập và xác thực nhanh
2. ✅ Buổi 4: Đi sâu vào tối ưu hóa
3. ✅ Buổi 5: Kiến trúc đa tác nhân
4. ✅ Buổi 6: Mẫu sản xuất và mở rộng
5. 🚀 Mở rộng: Xây dựng logic định tuyến tùy chỉnh và triển khai kết hợp

---

## Gói Buổi Hội Thảo (Phòng thí nghiệm tập trung 30 phút)

Nếu bạn đang theo định dạng hội thảo 6 buổi cô đọng, hãy sử dụng các hướng dẫn chuyên dụng này (mỗi hướng dẫn tương ứng và bổ sung cho tài liệu module rộng hơn ở trên):

| Buổi Hội Thảo | Hướng dẫn | Trọng tâm chính |
|---------------|-----------|-----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Cài đặt, xác thực, chạy phi & GPT-OSS-20B, tăng tốc |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Kỹ thuật gợi ý, mẫu RAG, nối CSV & tài liệu, di chuyển |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Tích hợp Hugging Face, đánh giá, lựa chọn mô hình |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, tăng tốc ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Vai trò tác nhân, bộ nhớ, công cụ, điều phối |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Định tuyến, chuỗi, mở rộng đường dẫn đến Azure |

Mỗi tệp phiên bao gồm: tóm tắt, mục tiêu học tập, luồng demo 30 phút, dự án khởi đầu, danh sách kiểm tra xác thực, xử lý sự cố và tham khảo SDK Python Foundry Local chính thức.

### Mẫu Script

Cài đặt các phụ thuộc của workshop (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Nếu chạy dịch vụ Foundry Local trên một máy (Windows) hoặc VM khác từ macOS, xuất điểm cuối:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Phiên | Script(s) | Mô tả |
|-------|-----------|-------|
| 1 | `samples/session01/chat_bootstrap.py` | Dịch vụ khởi động & trò chuyện trực tuyến |
| 2 | `samples/session02/rag_pipeline.py` | RAG tối giản (nhúng trong bộ nhớ) |
|   | `samples/session02/rag_eval_ragas.py` | Đánh giá RAG với các chỉ số ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Đánh giá độ trễ & thông lượng đa mô hình |
| 4 | `samples/session04/model_compare.py` | So sánh SLM và LLM (độ trễ & mẫu đầu ra) |
| 5 | `samples/session05/agents_orchestrator.py` | Nghiên cứu hai tác nhân → quy trình biên tập |
| 6 | `samples/session06/models_router.py` | Demo định tuyến dựa trên ý định |
|   | `samples/session06/models_pipeline.py` | Chuỗi lập kế hoạch/thực hiện/tinh chỉnh nhiều bước |

### Biến Môi Trường (Chung cho các mẫu)

| Biến | Mục đích | Ví dụ |
|------|----------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Bí danh mô hình đơn mặc định cho các mẫu cơ bản | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM rõ ràng so với mô hình lớn hơn để so sánh | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Danh sách bí danh để đánh giá | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Số lần lặp lại đánh giá cho mỗi mô hình | `3` |
| `BENCH_PROMPT` | Lời nhắc được sử dụng trong đánh giá | `Giải thích ngắn gọn về RAG.` |
| `EMBED_MODEL` | Mô hình nhúng của sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Ghi đè câu hỏi kiểm tra cho pipeline RAG | `Tại sao sử dụng RAG với suy luận cục bộ?` |
| `AGENT_QUESTION` | Ghi đè câu hỏi pipeline của tác nhân | `Giải thích tại sao AI biên lại quan trọng đối với tuân thủ.` |
| `AGENT_MODEL_PRIMARY` | Bí danh mô hình cho tác nhân nghiên cứu | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Bí danh mô hình cho tác nhân biên tập (có thể khác) | `gpt-oss-20b` |
| `SHOW_USAGE` | Khi `1`, in ra sử dụng token cho mỗi lần hoàn thành | `1` |
| `RETRY_ON_FAIL` | Khi `1`, thử lại một lần khi gặp lỗi trò chuyện tạm thời | `1` |
| `RETRY_BACKOFF` | Thời gian chờ trước khi thử lại | `1.0` |

Nếu một biến không được thiết lập, các script sẽ tự động sử dụng giá trị mặc định hợp lý. Đối với các demo mô hình đơn, bạn thường chỉ cần `FOUNDRY_LOCAL_ALIAS`.

### Module Tiện Ích

Tất cả các mẫu hiện chia sẻ một helper `samples/workshop_utils.py` cung cấp:

* Tạo `FoundryLocalManager` + client OpenAI được lưu trữ
* Helper `chat_once()` với tùy chọn thử lại + in sử dụng
* Báo cáo sử dụng token đơn giản (kích hoạt qua `SHOW_USAGE=1`)

Điều này giảm thiểu sự trùng lặp và làm nổi bật các thực hành tốt nhất cho việc điều phối mô hình cục bộ hiệu quả.

## Nâng Cấp Tùy Chọn (Xuyên Suốt Các Phiên)

| Chủ đề | Nâng cấp | Phiên | Env / Toggle |
|--------|----------|-------|--------------|
| Tính xác định | Nhiệt độ cố định + bộ lời nhắc ổn định | 1–6 | Đặt `temperature=0`, `top_p=1` |
| Hiển thị sử dụng token | Dạy về chi phí/hiệu quả một cách nhất quán | 1–6 | `SHOW_USAGE=1` |
| Phát trực tiếp token đầu tiên | Chỉ số độ trễ cảm nhận | 1,3,4,6 | `BENCH_STREAM=1` (đánh giá) |
| Khả năng thử lại | Xử lý khởi động lạnh tạm thời | Tất cả | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Tác nhân đa mô hình | Chuyên môn hóa vai trò không đồng nhất | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Định tuyến thích ứng | Ý định + heuristic chi phí | 6 | Mở rộng bộ định tuyến với logic leo thang |
| Bộ nhớ vector | Ghi nhớ ngữ nghĩa dài hạn | 2,5,6 | Tích hợp chỉ mục nhúng FAISS/Chroma |
| Xuất dấu vết | Kiểm toán & đánh giá | 2,5,6 | Thêm dòng JSON cho mỗi bước |
| Tiêu chí chất lượng | Theo dõi định tính | 3–6 | Lời nhắc chấm điểm thứ cấp |
| Kiểm tra nhanh | Xác thực trước workshop nhanh | Tất cả | `python Workshop/tests/smoke.py` |

### Bắt Đầu Nhanh Có Tính Xác Định

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Dự kiến số lượng token ổn định qua các đầu vào giống nhau lặp lại.

### Đánh Giá RAG (Phiên 2)

Sử dụng `rag_eval_ragas.py` để tính toán mức độ liên quan của câu trả lời, độ trung thực và độ chính xác ngữ cảnh trên một tập dữ liệu tổng hợp nhỏ:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Mở rộng bằng cách cung cấp một JSONL lớn hơn gồm các câu hỏi, ngữ cảnh và sự thật cơ bản, sau đó chuyển đổi thành một `Dataset` của Hugging Face.

## Phụ Lục Độ Chính Xác Lệnh CLI

Workshop chỉ sử dụng các lệnh CLI Foundry Local hiện được tài liệu hóa / ổn định.

### Các Lệnh Ổn Định Được Tham Chiếu

| Danh mục | Lệnh | Mục đích |
|----------|------|---------|
| Cốt lõi | `foundry --version` | Hiển thị phiên bản đã cài đặt |
| Dịch vụ | `foundry service start` | Khởi động dịch vụ cục bộ (nếu không tự động) |
| Dịch vụ | `foundry service status` | Hiển thị trạng thái dịch vụ |
| Mô hình | `foundry model list` | Liệt kê danh mục / các mô hình có sẵn |
| Mô hình | `foundry model download <alias>` | Tải trọng lượng mô hình vào bộ nhớ cache |
| Mô hình | `foundry model run <alias>` | Khởi chạy (tải) một mô hình cục bộ; kết hợp với `--prompt` cho một lần |
| Mô hình | `foundry model unload <alias>` / `foundry model stop <alias>` | Dỡ một mô hình khỏi bộ nhớ (nếu được hỗ trợ) |
| Bộ nhớ cache | `foundry cache list` | Liệt kê các mô hình đã lưu trong bộ nhớ cache |

### Mẫu Lời Nhắc Một Lần

Thay vì lệnh con `model chat` đã bị loại bỏ, sử dụng:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Điều này thực hiện một chu kỳ lời nhắc/phản hồi duy nhất sau đó thoát.

### Các Mẫu Bị Loại Bỏ / Tránh

| Bị loại bỏ / Không được tài liệu hóa | Thay thế / Hướng dẫn |
|-------------------------------------|----------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Sử dụng `foundry model list` + hoạt động gần đây / nhật ký |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Sử dụng script đánh giá Python + công cụ hệ điều hành (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Đánh Giá & Telemetry

- Độ trễ, p95, token/giây: `samples/session03/benchmark_oss_models.py`
- Độ trễ token đầu tiên (phát trực tiếp): đặt `BENCH_STREAM=1`
- Sử dụng tài nguyên: công cụ giám sát hệ điều hành (Task Manager, Activity Monitor, `nvidia-smi`).

Khi các lệnh telemetry CLI mới ổn định, chúng có thể được tích hợp với các chỉnh sửa tối thiểu vào các tệp markdown của phiên.

### Bảo Vệ Lint Tự Động

Một linter tự động ngăn chặn việc tái giới thiệu các mẫu CLI bị loại bỏ bên trong các khối mã của tệp markdown:

Script: `Workshop/scripts/lint_markdown_cli.py`

Các mẫu bị loại bỏ bị chặn bên trong các khối mã.

Các thay thế được khuyến nghị:
| Bị loại bỏ | Thay thế |
|-----------|----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Script đánh giá + công cụ hệ thống |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Chạy cục bộ:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` chạy trên mỗi lần đẩy & PR.

Hook pre-commit tùy chọn:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Bảng Di Chuyển Nhanh CLI → SDK

| Nhiệm vụ | Lệnh CLI Một Dòng | Tương đương SDK (Python) | Ghi chú |
|----------|-------------------|--------------------------|---------|
| Chạy một mô hình một lần (lời nhắc) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK tự động khởi động dịch vụ & bộ nhớ cache |
| Tải xuống (bộ nhớ cache) mô hình | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager chọn biến thể tốt nhất nếu bí danh ánh xạ đến nhiều bản dựng |
| Liệt kê danh mục | `foundry model list` | `# use manager for each alias or maintain known list` | CLI tổng hợp; SDK hiện tại khởi tạo từng bí danh |
| Liệt kê các mô hình đã lưu trong bộ nhớ cache | `foundry cache list` | `manager.list_cached_models()` | Sau khi khởi tạo manager (bất kỳ bí danh nào) |
| Lấy URL điểm cuối | (ngầm định) | `manager.endpoint` | Được sử dụng để tạo client tương thích OpenAI |
| Làm nóng một mô hình | `foundry model run <alias>` sau đó lời nhắc đầu tiên | `chat_once(alias, messages=[...])` (tiện ích) | Tiện ích xử lý khởi động lạnh ban đầu |
| Đo độ trễ | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (hoặc script xuất mới) | Ưu tiên script để có số liệu nhất quán |
| Dừng / dỡ mô hình | `foundry model unload <alias>` | (Không được hiển thị – khởi động lại dịch vụ / quy trình) | Thường không cần thiết cho luồng workshop |
| Lấy sử dụng token | (xem đầu ra) | `resp.usage.total_tokens` | Được cung cấp nếu backend trả về đối tượng sử dụng |

## Xuất Markdown Đánh Giá

Sử dụng script `Workshop/scripts/export_benchmark_markdown.py` để chạy một đánh giá mới (logic giống như `samples/session03/benchmark_oss_models.py`) và xuất một bảng Markdown thân thiện với GitHub cùng với JSON thô.

### Ví dụ

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Các tệp được tạo:
| Tệp | Nội dung |
|-----|----------|
| `benchmark_report.md` | Bảng Markdown + gợi ý diễn giải |
| `benchmark_report.json` | Mảng số liệu thô (để so sánh / theo dõi xu hướng) |

Đặt `BENCH_STREAM=1` trong môi trường để bao gồm độ trễ token đầu tiên nếu được hỗ trợ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->