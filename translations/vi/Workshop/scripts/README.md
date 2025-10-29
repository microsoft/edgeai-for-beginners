<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T22:35:40+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "vi"
}
-->
# Tập lệnh Workshop

Thư mục này chứa các tập lệnh tự động hóa và hỗ trợ được sử dụng để duy trì chất lượng và tính nhất quán cho tài liệu Workshop.

## Nội dung

| Tệp | Mục đích |
|------|---------|
| `lint_markdown_cli.py` | Kiểm tra các khối mã Markdown để ngăn chặn các mẫu lệnh Foundry Local CLI đã lỗi thời. |
| `export_benchmark_markdown.py` | Chạy benchmark độ trễ đa mô hình và xuất báo cáo dưới dạng Markdown + JSON. |

## 1. Công cụ kiểm tra mẫu CLI trong Markdown

`lint_markdown_cli.py` quét tất cả các tệp `.md` không phải bản dịch để tìm các mẫu lệnh Foundry Local CLI không được phép **bên trong các khối mã** (``` ... ```). Văn bản thông tin vẫn có thể đề cập đến các lệnh đã lỗi thời để cung cấp ngữ cảnh lịch sử.

### Mẫu đã lỗi thời (Bị chặn trong các khối mã)

Công cụ kiểm tra sẽ chặn các mẫu CLI đã lỗi thời. Hãy sử dụng các lựa chọn thay thế hiện đại.

### Các thay thế bắt buộc
| Đã lỗi thời | Sử dụng thay thế |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Tập lệnh benchmark + công cụ hệ thống (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Mã thoát
| Mã | Ý nghĩa |
|------|---------|
| 0 | Không phát hiện vi phạm |
| 1 | Một hoặc nhiều mẫu đã lỗi thời được tìm thấy |

### Chạy cục bộ
Từ thư mục gốc của kho lưu trữ (khuyến nghị):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Hook Pre-Commit (Tùy chọn)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Điều này chặn các commit có chứa mẫu đã lỗi thời.

### Tích hợp CI
Một workflow GitHub Action (`.github/workflows/markdown-cli-lint.yml`) chạy công cụ kiểm tra trên mỗi lần đẩy và yêu cầu kéo đến các nhánh `main` và `Reactor`. Các công việc thất bại phải được sửa trước khi hợp nhất.

### Thêm mẫu đã lỗi thời mới
1. Mở `lint_markdown_cli.py`.
2. Thêm một tuple `(regex, suggestion)` vào danh sách `DEPRECATED`. Sử dụng chuỗi thô và bao gồm các ranh giới từ `\b` khi thích hợp.
3. Chạy công cụ kiểm tra cục bộ để xác minh phát hiện.
4. Commit và đẩy; CI sẽ thực thi quy tắc mới.

Ví dụ thêm:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Cho phép đề cập giải thích
Vì chỉ các khối mã được thực thi, bạn có thể mô tả các lệnh đã lỗi thời trong văn bản tường thuật một cách an toàn. Nếu bạn *phải* hiển thị chúng trong một khối mã để so sánh, hãy thêm một khối mã **không** có ba dấu backtick (ví dụ: thụt lề hoặc trích dẫn) hoặc viết lại dưới dạng giả lập.

### Bỏ qua các tệp cụ thể (Nâng cao)
Nếu cần, hãy đặt các ví dụ cũ trong một tệp riêng ngoài kho lưu trữ hoặc đổi tên với phần mở rộng khác trong khi soạn thảo. Việc bỏ qua có chủ ý đối với các bản sao dịch được thực hiện tự động (các đường dẫn chứa `translations`).

### Xử lý sự cố
| Vấn đề | Nguyên nhân | Giải pháp |
|-------|-------|-----------|
| Công cụ kiểm tra đánh dấu một dòng bạn đã cập nhật | Regex quá rộng | Thu hẹp mẫu với ranh giới từ bổ sung (`\b`) hoặc điểm neo |
| CI thất bại nhưng cục bộ thành công | Phiên bản Python khác hoặc thay đổi chưa được commit | Chạy lại cục bộ, đảm bảo cây làm việc sạch, kiểm tra phiên bản Python của workflow (3.11) |
| Cần bỏ qua tạm thời | Sửa lỗi khẩn cấp | Áp dụng sửa lỗi ngay sau đó; cân nhắc sử dụng nhánh tạm thời và PR tiếp theo (tránh thêm các công tắc bỏ qua) |

### Lý do
Việc giữ tài liệu phù hợp với giao diện CLI *hiện tại* ổn định giúp tránh sự khó chịu trong workshop, tránh gây nhầm lẫn cho người học và tập trung đo lường hiệu suất thông qua các tập lệnh Python được duy trì thay vì các lệnh con CLI không đồng nhất.

---
Được duy trì như một phần của chuỗi công cụ chất lượng workshop. Để cải tiến (ví dụ: tự động sửa gợi ý hoặc tạo báo cáo HTML), hãy mở một vấn đề hoặc gửi PR.

## 2. Tập lệnh xác thực mẫu

`validate_samples.py` xác thực tất cả các tệp mẫu Python về tính hợp lệ cú pháp, nhập khẩu và tuân thủ các thực hành tốt nhất.

### Cách sử dụng
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### Những gì nó kiểm tra
- ✅ Tính hợp lệ cú pháp Python
- ✅ Nhập khẩu bắt buộc có mặt
- ✅ Triển khai xử lý lỗi (chế độ chi tiết)
- ✅ Sử dụng gợi ý kiểu (chế độ chi tiết)
- ✅ Chuỗi tài liệu hàm (chế độ chi tiết)
- ✅ Liên kết tham chiếu SDK (chế độ chi tiết)

### Biến môi trường
- `SKIP_IMPORT_CHECK=1` - Bỏ qua kiểm tra nhập khẩu
- `SKIP_SYNTAX_CHECK=1` - Bỏ qua kiểm tra cú pháp

### Mã thoát
- `0` - Tất cả các mẫu đã vượt qua xác thực
- `1` - Một hoặc nhiều mẫu không vượt qua

## 3. Trình chạy kiểm tra mẫu

`test_samples.py` chạy các kiểm tra nhanh trên tất cả các mẫu để xác minh chúng thực thi mà không có lỗi.

### Cách sử dụng
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### Yêu cầu trước
- Dịch vụ Foundry Local đang chạy: `foundry service start`
- Mô hình đã tải: `foundry model run phi-4-mini`
- Các phụ thuộc đã cài đặt: `pip install -r requirements.txt`

### Những gì nó kiểm tra
- ✅ Mẫu có thể thực thi mà không có lỗi runtime
- ✅ Đầu ra yêu cầu được tạo
- ✅ Xử lý lỗi đúng cách khi thất bại
- ✅ Hiệu suất (thời gian thực thi)

### Biến môi trường
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Mô hình sử dụng để kiểm tra
- `TEST_TIMEOUT=30` - Thời gian chờ mỗi mẫu tính bằng giây

### Các lỗi dự kiến
Một số kiểm tra có thể thất bại nếu các phụ thuộc tùy chọn chưa được cài đặt (ví dụ: `ragas`, `sentence-transformers`). Cài đặt với:
```bash
pip install sentence-transformers ragas datasets
```

### Mã thoát
- `0` - Tất cả các kiểm tra đã vượt qua
- `1` - Một hoặc nhiều kiểm tra không vượt qua

## 4. Trình xuất Benchmark Markdown

Tập lệnh: `export_benchmark_markdown.py`

Tạo bảng hiệu suất có thể tái tạo cho một tập hợp các mô hình.

### Cách sử dụng
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Đầu ra
| Tệp | Mô tả |
|------|-------------|
| `benchmark_report.md` | Bảng Markdown (trung bình, p95, tokens/giây, tùy chọn token đầu tiên) |
| `benchmark_report.json` | Mảng số liệu thô để so sánh & lịch sử |

### Tùy chọn
| Cờ | Mô tả | Mặc định |
|------|-------------|---------|
| `--models` | Các bí danh mô hình, phân tách bằng dấu phẩy | (bắt buộc) |
| `--prompt` | Prompt sử dụng mỗi vòng | (bắt buộc) |
| `--rounds` | Số vòng mỗi mô hình | 3 |
| `--output` | Tệp đầu ra Markdown | `benchmark_report.md` |
| `--json` | Tệp đầu ra JSON | `benchmark_report.json` |
| `--fail-on-empty` | Mã thoát khác 0 nếu tất cả các benchmark thất bại | tắt |

Biến môi trường `BENCH_STREAM=1` thêm đo lường độ trễ token đầu tiên.

### Ghi chú
- Tái sử dụng `workshop_utils` để khởi động mô hình & bộ nhớ đệm nhất quán.
- Nếu chạy từ thư mục làm việc khác, tập lệnh sẽ cố gắng tìm đường dẫn dự phòng để định vị `workshop_utils`.
- Để so sánh GPU: chạy một lần, bật tăng tốc qua cấu hình CLI, chạy lại và so sánh JSON.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.