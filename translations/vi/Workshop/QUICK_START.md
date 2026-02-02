# Hướng Dẫn Bắt Đầu Nhanh Cho Workshop

## Yêu Cầu Trước

### 1. Cài đặt Foundry Local

Làm theo hướng dẫn cài đặt chính thức:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Cài đặt Các Thư Viện Python

Từ thư mục Workshop:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Chạy Các Mẫu Workshop

### Phiên 01: Chat Cơ Bản

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Biến Môi Trường:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Phiên 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Biến Môi Trường:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Phiên 02: Đánh Giá RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Lưu ý**: Yêu cầu cài đặt thêm các thư viện qua `requirements.txt`

### Phiên 03: Đánh Giá Hiệu Năng

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Biến Môi Trường:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Kết Quả**: JSON với các chỉ số độ trễ, thông lượng, và thời gian tạo token đầu tiên

### Phiên 04: So Sánh Mô Hình

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Biến Môi Trường:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Phiên 05: Điều Phối Đa Tác Nhân

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Biến Môi Trường:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Phiên 06: Bộ Định Tuyến Mô Hình

```bash
cd Workshop/samples
python -m session06.models_router
```

**Kiểm tra logic định tuyến** với nhiều mục đích (code, tóm tắt, phân loại)

### Phiên 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Pipeline phức tạp nhiều bước** với lập kế hoạch, thực thi, và tinh chỉnh

## Scripts

### Xuất Báo Cáo Đánh Giá Hiệu Năng

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Kết Quả**: Bảng Markdown + các chỉ số JSON

### Kiểm Tra Các Mẫu CLI Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Mục Đích**: Phát hiện các mẫu CLI đã lỗi thời trong tài liệu

## Kiểm Tra

### Kiểm Tra Nhanh

```bash
cd Workshop
python -m tests.smoke
```

**Kiểm Tra**: Chức năng cơ bản của các mẫu chính

## Xử Lý Sự Cố

### Dịch Vụ Không Chạy

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Lỗi Nhập Module

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Lỗi Kết Nối

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Không Tìm Thấy Mô Hình

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Tham Chiếu Biến Môi Trường

### Cấu Hình Cốt Lõi
| Biến | Mặc Định | Mô Tả |
|------|----------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Thay đổi | Bí danh mô hình sử dụng |
| `FOUNDRY_LOCAL_ENDPOINT` | Tự động | Ghi đè điểm cuối dịch vụ |
| `SHOW_USAGE` | `0` | Hiển thị thống kê sử dụng token |
| `RETRY_ON_FAIL` | `1` | Bật logic thử lại |
| `RETRY_BACKOFF` | `1.0` | Độ trễ ban đầu khi thử lại (giây) |

### Cụ Thể Theo Phiên
| Biến | Mặc Định | Mô Tả |
|------|----------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Mô hình nhúng |
| `RAG_QUESTION` | Xem mẫu | Câu hỏi kiểm tra RAG |
| `BENCH_MODELS` | Thay đổi | Các mô hình phân tách bằng dấu phẩy |
| `BENCH_ROUNDS` | `3` | Số lần đánh giá hiệu năng |
| `BENCH_PROMPT` | Xem mẫu | Lời nhắc đánh giá hiệu năng |
| `BENCH_STREAM` | `0` | Đo độ trễ token đầu tiên |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Mô hình tác nhân chính |
| `AGENT_MODEL_EDITOR` | Chính | Mô hình tác nhân chỉnh sửa |
| `SLM_ALIAS` | `phi-4-mini` | Mô hình ngôn ngữ nhỏ |
| `LLM_ALIAS` | `qwen2.5-7b` | Mô hình ngôn ngữ lớn |
| `COMPARE_PROMPT` | Xem mẫu | Lời nhắc so sánh |

## Mô Hình Đề Xuất

### Phát Triển & Kiểm Tra
- **phi-4-mini** - Cân bằng giữa chất lượng và tốc độ
- **qwen2.5-0.5b** - Rất nhanh cho phân loại
- **gemma-2-2b** - Chất lượng tốt, tốc độ vừa phải

### Kịch Bản Sản Xuất
- **phi-4-mini** - Mục đích chung
- **deepseek-coder-1.3b** - Tạo mã
- **qwen2.5-7b** - Phản hồi chất lượng cao

## Tài Liệu SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Nhận Hỗ Trợ

1. Kiểm tra trạng thái dịch vụ: `foundry service status`  
2. Xem nhật ký: Kiểm tra nhật ký dịch vụ Foundry Local  
3. Xem tài liệu SDK: https://github.com/microsoft/Foundry-Local  
4. Xem mã mẫu: Tất cả các mẫu đều có docstring chi tiết  

## Các Bước Tiếp Theo

1. Hoàn thành tất cả các phiên workshop theo thứ tự  
2. Thử nghiệm với các mô hình khác nhau  
3. Chỉnh sửa các mẫu cho trường hợp sử dụng của bạn  

---

**Cập Nhật Lần Cuối**: 2025-01-08  
**Phiên Bản Workshop**: Mới nhất  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->