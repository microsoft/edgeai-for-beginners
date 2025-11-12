<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:42:57+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "vi"
}
-->
# Buổi 3: Các Mô Hình Mã Nguồn Mở trong Foundry Local

## Tóm tắt

Khám phá cách đưa Hugging Face và các mô hình mã nguồn mở khác vào Foundry Local. Tìm hiểu chiến lược lựa chọn, quy trình đóng góp cộng đồng, phương pháp so sánh hiệu suất, và cách mở rộng Foundry với đăng ký mô hình tùy chỉnh. Buổi học này liên kết với chủ đề khám phá hàng tuần "Model Mondays" và trang bị cho bạn khả năng đánh giá và vận hành các mô hình mã nguồn mở tại chỗ trước khi mở rộng lên Azure.

## Mục tiêu học tập

Sau buổi học, bạn sẽ có thể:

- **Khám phá & Đánh giá**: Xác định các mô hình tiềm năng (mistral, gemma, qwen, deepseek) dựa trên sự cân bằng giữa chất lượng và tài nguyên.
- **Tải & Chạy**: Sử dụng Foundry Local CLI để tải xuống, lưu trữ và khởi chạy các mô hình cộng đồng.
- **Đánh giá hiệu suất**: Áp dụng các tiêu chí nhất quán về độ trễ, thông lượng token và chất lượng.
- **Mở rộng**: Đăng ký hoặc điều chỉnh một trình bao bọc mô hình tùy chỉnh theo các mẫu tương thích SDK.
- **So sánh**: Tạo các so sánh có cấu trúc để đưa ra quyết định lựa chọn giữa SLM và LLM cỡ trung.

## Điều kiện tiên quyết

- Hoàn thành buổi 1 & 2
- Môi trường Python với `foundry-local-sdk` đã được cài đặt
- Ít nhất 15GB dung lượng đĩa trống để lưu trữ nhiều mô hình

### Bắt đầu nhanh trên môi trường đa nền tảng

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

Khi đánh giá hiệu suất từ macOS đối với dịch vụ máy chủ Windows, thiết lập:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Quy trình demo (30 phút)

### 1. Tải các mô hình Hugging Face qua CLI (8 phút)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```

### 2. Chạy & Kiểm tra nhanh (5 phút)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. Kịch bản đánh giá hiệu suất (8 phút)

Tạo `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Chạy:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. So sánh hiệu suất (5 phút)

Thảo luận về các yếu tố đánh đổi: thời gian tải, dung lượng bộ nhớ (quan sát Task Manager / `nvidia-smi` / trình quản lý tài nguyên hệ điều hành), chất lượng đầu ra so với tốc độ. Sử dụng kịch bản đánh giá hiệu suất Python (Buổi 3) để đo độ trễ và thông lượng; lặp lại sau khi kích hoạt tăng tốc GPU.

### 5. Dự án khởi đầu (4 phút)

Tạo một trình tạo báo cáo so sánh mô hình (mở rộng kịch bản đánh giá hiệu suất với xuất markdown).

## Dự án khởi đầu: Mở rộng `03-huggingface-models`

Nâng cấp mẫu hiện có bằng cách:

1. Thêm tổng hợp đánh giá hiệu suất + xuất CSV/Markdown.
2. Triển khai đánh giá định tính đơn giản (bộ cặp prompt + tệp chú thích thủ công).
3. Giới thiệu cấu hình JSON (`models.json`) cho danh sách mô hình có thể cắm và bộ prompt.

## Danh sách kiểm tra xác thực

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Tất cả các mô hình mục tiêu phải xuất hiện và phản hồi yêu cầu trò chuyện thử nghiệm.

## Kịch bản mẫu & Liên kết với Workshop

| Kịch bản Workshop | Kịch bản | Mục tiêu | Nguồn Prompt / Dataset |
|-------------------|----------|----------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Đội ngũ nền tảng biên chọn SLM mặc định cho trình tóm tắt nhúng | Tạo so sánh độ trễ + p95 + token/giây giữa các mô hình tiềm năng | Biến `PROMPT` nội tuyến + danh sách `BENCH_MODELS` môi trường |

### Tường thuật kịch bản
Đội ngũ kỹ thuật sản phẩm cần chọn một mô hình tóm tắt nhẹ mặc định cho tính năng ghi chú cuộc họp ngoại tuyến. Họ thực hiện các đánh giá hiệu suất xác định có kiểm soát (temperature=0) trên một bộ prompt cố định (xem ví dụ bên dưới) và thu thập các chỉ số độ trễ + thông lượng với và không có tăng tốc GPU.

### Ví dụ bộ prompt JSON (có thể mở rộng)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Lặp lại mỗi prompt cho từng mô hình, ghi lại độ trễ từng prompt để tính toán các chỉ số phân phối và phát hiện các giá trị ngoại lệ.

## Khung lựa chọn mô hình

| Khía cạnh | Chỉ số | Tại sao quan trọng |
|----------|--------|--------------------|
| Độ trễ | trung bình / p95 | Tính nhất quán trải nghiệm người dùng |
| Thông lượng | token/giây | Khả năng mở rộng theo lô & streaming |
| Bộ nhớ | kích thước cư trú | Phù hợp thiết bị & đồng thời |
| Chất lượng | rubric prompts | Phù hợp nhiệm vụ |
| Dấu chân | bộ nhớ đĩa | Phân phối & cập nhật |
| Giấy phép | quyền sử dụng | Tuân thủ thương mại |

## Mở rộng với mô hình tùy chỉnh

Mẫu cấp cao (giả lập):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Tham khảo kho chính thức để cập nhật giao diện adapter:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Xử lý sự cố

| Vấn đề | Nguyên nhân | Cách khắc phục |
|--------|-------------|----------------|
| Hết bộ nhớ trên mistral-7b | RAM/GPU không đủ | Dừng các mô hình khác; thử biến thể nhỏ hơn |
| Phản hồi đầu tiên chậm | Tải lạnh | Giữ ấm bằng một prompt nhẹ định kỳ |
| Tải xuống bị treo | Mạng không ổn định | Thử lại; tải trước vào thời gian thấp điểm |

## Tài liệu tham khảo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Khám phá mô hình Hugging Face: https://huggingface.co/models

---

**Thời lượng buổi học**: 30 phút (+ phần mở rộng tùy chọn)  
**Độ khó**: Trung cấp

### Nâng cấp tùy chọn

| Nâng cấp | Lợi ích | Cách thực hiện |
|----------|---------|----------------|
| Độ trễ token đầu tiên khi streaming | Đo lường độ phản hồi cảm nhận | Chạy đánh giá hiệu suất với `BENCH_STREAM=1` (kịch bản nâng cấp trong `Workshop/samples/session03`) |
| Chế độ xác định | So sánh hồi quy ổn định | `temperature=0`, bộ prompt cố định, ghi lại đầu ra JSON dưới kiểm soát phiên bản |
| Chấm điểm rubric chất lượng | Thêm khía cạnh định tính | Duy trì `prompts.json` với các khía cạnh mong đợi; chú thích điểm (1–5) thủ công hoặc qua mô hình thứ cấp |
| Xuất CSV / Markdown | Báo cáo có thể chia sẻ | Mở rộng kịch bản để ghi `benchmark_report.md` với bảng & điểm nổi bật |
| Thẻ khả năng mô hình | Hỗ trợ định tuyến tự động sau này | Duy trì `models.json` với `{alias: {capabilities:[], size_mb:..}}` |
| Giai đoạn làm ấm bộ nhớ cache | Giảm thiên vị khởi động lạnh | Thực hiện một vòng làm ấm trước vòng lặp đo thời gian (đã triển khai) |
| Độ chính xác phần trăm | Độ trễ đuôi mạnh mẽ | Sử dụng numpy percentile (đã có trong kịch bản được tái cấu trúc) |
| Ước tính chi phí token | So sánh kinh tế | Ước tính chi phí = (token/giây * trung bình token mỗi yêu cầu) * hệ số năng lượng |
| Tự động bỏ qua các mô hình lỗi | Tăng khả năng phục hồi trong các lần chạy theo lô | Bao mỗi đánh giá hiệu suất trong try/except và đánh dấu trường trạng thái |

#### Đoạn mã xuất Markdown tối thiểu

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Ví dụ bộ prompt xác định

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Lặp lại danh sách tĩnh thay vì các prompt ngẫu nhiên để có các chỉ số so sánh giữa các lần commit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->