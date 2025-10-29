<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T22:31:29+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "vi"
}
-->
# Buổi 4: Khám phá các mô hình tiên tiến – LLMs, SLMs & Suy luận trên thiết bị

## Tóm tắt

So sánh các Mô hình Ngôn ngữ Lớn (LLMs) và Mô hình Ngôn ngữ Nhỏ (SLMs) trong các kịch bản suy luận tại chỗ và trên đám mây. Tìm hiểu các mẫu triển khai tận dụng tăng tốc ONNX Runtime, thực thi WebGPU, và trải nghiệm RAG lai. Bao gồm demo Chainlit RAG với mô hình cục bộ cùng với tùy chọn khám phá OpenWebUI. Bạn sẽ điều chỉnh một khởi đầu suy luận WebGPU và đánh giá khả năng của Phi so với GPT-OSS-20B cùng các đánh đổi về chi phí/hiệu suất.

## Mục tiêu học tập

- **So sánh** SLM và LLM về độ trễ, bộ nhớ, chất lượng
- **Triển khai** mô hình với ONNXRuntime và (nếu được hỗ trợ) WebGPU
- **Chạy** suy luận trên trình duyệt (demo tương tác bảo vệ quyền riêng tư)
- **Tích hợp** một pipeline Chainlit RAG với backend SLM cục bộ
- **Đánh giá** bằng các phương pháp nhẹ về chất lượng + chi phí

## Yêu cầu trước

- Hoàn thành các buổi 1–3
- Đã cài đặt `chainlit` (đã có trong `requirements.txt` của Module08)
- Trình duyệt hỗ trợ WebGPU (Edge / Chrome mới nhất trên Windows 11)
- Foundry Local đang chạy (`foundry status`)

### Ghi chú đa nền tảng

Windows vẫn là môi trường mục tiêu chính. Đối với các nhà phát triển macOS đang chờ các binary gốc:
1. Chạy Foundry Local trong một VM Windows 11 (Parallels / UTM) HOẶC một máy làm việc từ xa Windows.
2. Mở dịch vụ (cổng mặc định 5273) và thiết lập trên macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Sử dụng các bước môi trường ảo Python giống như các buổi trước.

Cài đặt Chainlit (cả hai nền tảng):
```bash
pip install chainlit
```

## Quy trình demo (30 phút)

### 1. So sánh Phi (SLM) và GPT-OSS-20B (LLM) (6 phút)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Theo dõi: độ sâu phản hồi, độ chính xác thực tế, sự phong phú về phong cách, độ trễ.

### 2. Tăng tốc ONNX Runtime (5 phút)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Quan sát sự thay đổi thông lượng sau khi kích hoạt GPU so với chỉ CPU.

### 3. Suy luận WebGPU trên trình duyệt (6 phút)

Điều chỉnh khởi đầu `04-webgpu-inference` (tạo `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Mở tệp trong trình duyệt; quan sát vòng lặp cục bộ với độ trễ thấp.

### 4. Ứng dụng trò chuyện Chainlit RAG (7 phút)

`samples/04-cutting-edge/chainlit_app.py` tối giản:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Chạy:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Dự án khởi đầu: Điều chỉnh `04-webgpu-inference` (6 phút)

Các sản phẩm cần giao:
- Thay thế logic fetch placeholder bằng các token streaming (sử dụng biến thể endpoint `stream=True` khi được kích hoạt)
- Thêm biểu đồ độ trễ (phía client) cho các tùy chọn phi và gpt-oss-20b
- Nhúng ngữ cảnh RAG trực tiếp (textarea cho tài liệu tham khảo)

## Phương pháp đánh giá

| Danh mục | Phi-4-mini | GPT-OSS-20B | Quan sát |
|----------|------------|-------------|-------------|
| Độ trễ (lạnh) | Nhanh | Chậm hơn | SLM khởi động nhanh |
| Bộ nhớ | Thấp | Cao | Khả năng trên thiết bị |
| Tuân thủ ngữ cảnh | Tốt | Mạnh | Mô hình lớn hơn có thể chi tiết hơn |
| Chi phí (cục bộ) | Tối thiểu | Cao hơn (tài nguyên) | Đánh đổi năng lượng/thời gian |
| Trường hợp sử dụng tốt nhất | Ứng dụng tại chỗ | Lý luận sâu | Có thể pipeline lai |

## Xác thực môi trường

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Xử lý sự cố

| Triệu chứng | Nguyên nhân | Hành động |
|---------|-------|--------|
| Trang web không tải được | CORS hoặc dịch vụ ngừng hoạt động | Sử dụng `curl` để xác minh endpoint; kích hoạt proxy CORS nếu cần |
| Chainlit trống | Môi trường không hoạt động | Kích hoạt venv & cài đặt lại các phụ thuộc |
| Độ trễ cao | Mô hình vừa được tải | Khởi động với chuỗi prompt nhỏ |

## Tài liệu tham khảo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Tài liệu Chainlit: https://docs.chainlit.io
- Đánh giá RAG (Ragas): https://docs.ragas.io

---

**Thời lượng buổi học**: 30 phút  
**Độ khó**: Nâng cao

## Kịch bản mẫu & ánh xạ workshop

| Tài liệu workshop | Kịch bản | Mục tiêu | Nguồn dữ liệu / prompt |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Đội kiến trúc đánh giá SLM và LLM cho trình tạo tóm tắt báo cáo | Định lượng độ trễ + sự khác biệt sử dụng token | Biến môi trường `COMPARE_PROMPT` duy nhất |
| `chainlit_app.py` (demo RAG) | Nguyên mẫu trợ lý kiến thức nội bộ | Cung cấp câu trả lời ngắn với truy xuất từ ngữ tối thiểu | Danh sách `DOCS` trực tiếp trong tệp |
| `webgpu_demo.html` | Xem trước suy luận trên trình duyệt thiết bị | Hiển thị vòng lặp cục bộ với độ trễ thấp + câu chuyện UX | Chỉ prompt người dùng trực tiếp |

### Câu chuyện kịch bản
Tổ chức sản phẩm muốn một trình tạo tóm tắt báo cáo điều hành. Một SLM nhẹ (phi‑4‑mini) tạo bản nháp tóm tắt; một LLM lớn hơn (gpt‑oss‑20b) có thể chỉ tinh chỉnh các báo cáo ưu tiên cao. Các script buổi học ghi lại độ trễ thực nghiệm & số liệu token để biện minh cho thiết kế lai, trong khi demo Chainlit minh họa cách truy xuất có căn cứ giữ cho câu trả lời của mô hình nhỏ chính xác. Trang khái niệm WebGPU cung cấp lộ trình tầm nhìn cho xử lý hoàn toàn phía client khi tăng tốc trình duyệt trưởng thành.

### Ngữ cảnh RAG tối giản (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Quy trình lai Nháp→Tinh chỉnh (Giả lập)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Theo dõi cả hai thành phần độ trễ để báo cáo chi phí trung bình kết hợp.

### Các cải tiến tùy chọn

| Trọng tâm | Cải tiến | Tại sao | Gợi ý triển khai |
|-------|------------|-----|---------------------|
| Số liệu so sánh | Theo dõi sử dụng token + độ trễ token đầu tiên | Góc nhìn hiệu suất toàn diện | Sử dụng script benchmark nâng cao (Buổi 3) với `BENCH_STREAM=1` |
| Pipeline lai | Nháp SLM → Tinh chỉnh LLM | Giảm độ trễ & chi phí | Tạo với phi-4-mini, tinh chỉnh tóm tắt bằng gpt-oss-20b |
| Giao diện streaming | UX tốt hơn trong Chainlit | Phản hồi từng phần | Sử dụng `stream=True` khi streaming cục bộ được kích hoạt; tích lũy các phần |
| Bộ nhớ đệm WebGPU | Khởi tạo JS nhanh hơn | Giảm chi phí biên dịch lại | Bộ nhớ đệm các artifact shader đã biên dịch (khả năng runtime tương lai) |
| Bộ QA xác định | So sánh mô hình công bằng | Loại bỏ biến đổi | Danh sách prompt cố định + `temperature=0` cho các lần chạy đánh giá |
| Chấm điểm đầu ra | Lăng kính chất lượng có cấu trúc | Vượt qua các giai thoại | Thang điểm đơn giản: mạch lạc / thực tế / ngắn gọn (1–5) |
| Ghi chú năng lượng / tài nguyên | Thảo luận trong lớp học | Hiển thị các đánh đổi | Sử dụng các công cụ giám sát hệ điều hành (`foundry system info`, Task Manager, `nvidia-smi`) + đầu ra script benchmark |
| Mô phỏng chi phí | Biện minh trước đám mây | Lập kế hoạch mở rộng | Ánh xạ token tới giá giả định trên đám mây cho câu chuyện TCO |
| Phân tích độ trễ | Xác định nút thắt cổ chai | Nhắm mục tiêu tối ưu hóa | Đo lường chuẩn bị prompt, gửi yêu cầu, token đầu tiên, hoàn thành đầy đủ |
| RAG + LLM dự phòng | Lưới an toàn chất lượng | Cải thiện các truy vấn khó | Nếu độ dài câu trả lời SLM < ngưỡng hoặc độ tin cậy thấp → nâng cấp |

#### Mẫu Nháp/Tinh chỉnh Lai

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Phác thảo Phân tích Độ trễ

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Sử dụng khung đo lường nhất quán trên các mô hình để so sánh công bằng.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.