<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T22:34:43+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "vi"
}
-->
# Buổi 6: Foundry Local – Mô hình như công cụ

## Tóm tắt

Xem các mô hình như những công cụ có thể kết hợp trong một lớp vận hành AI cục bộ. Buổi học này sẽ hướng dẫn cách kết nối nhiều cuộc gọi SLM/LLM chuyên biệt, định tuyến nhiệm vụ một cách chọn lọc, và cung cấp một giao diện SDK thống nhất cho các ứng dụng. Bạn sẽ xây dựng một bộ định tuyến mô hình nhẹ + lập kế hoạch nhiệm vụ, tích hợp nó vào một kịch bản ứng dụng, và phác thảo lộ trình mở rộng lên Azure AI Foundry cho khối lượng công việc sản xuất.

## Mục tiêu học tập

- **Hình dung** các mô hình như những công cụ nguyên tử với khả năng được khai báo
- **Định tuyến** yêu cầu dựa trên ý định / điểm số heuristic
- **Kết nối** đầu ra qua các nhiệm vụ nhiều bước (phân tích → giải quyết → tinh chỉnh)
- **Tích hợp** API khách hàng thống nhất cho các ứng dụng hạ nguồn
- **Mở rộng** thiết kế lên đám mây (hợp đồng tương thích OpenAI)

## Yêu cầu trước

- Hoàn thành các buổi 1–5
- Lưu trữ nhiều mô hình cục bộ (ví dụ: `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Đoạn mã môi trường đa nền tảng

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Truy cập dịch vụ từ xa/VM từ macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Quy trình demo (30 phút)

### 1. Khai báo khả năng công cụ (5 phút)

Tạo `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Phát hiện ý định & định tuyến (8 phút)

Tạo `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Kết nối nhiệm vụ nhiều bước (7 phút)

Tạo `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Dự án khởi đầu: Điều chỉnh `06-models-as-tools` (5 phút)

Cải tiến:
- Thêm hỗ trợ token streaming (cập nhật giao diện người dùng theo tiến trình)
- Thêm điểm số độ tin cậy: trùng lặp từ vựng hoặc tiêu chí gợi ý
- Xuất JSON trace (ý định → mô hình → độ trễ → sử dụng token)
- Thực hiện tái sử dụng bộ nhớ cache cho các bước lặp lại

### 5. Lộ trình mở rộng lên Azure (5 phút)

| Lớp | Cục bộ (Foundry) | Đám mây (Azure AI Foundry) | Chiến lược chuyển đổi |
|-----|------------------|---------------------------|-----------------------|
| Định tuyến | Python heuristic | Microservice bền vững | Đóng gói & triển khai API |
| Mô hình | SLMs lưu trữ | Triển khai được quản lý | Ánh xạ tên cục bộ sang ID triển khai |
| Khả năng quan sát | Thống kê CLI/thủ công | Nhật ký & số liệu trung tâm | Thêm sự kiện trace có cấu trúc |
| Bảo mật | Chỉ host cục bộ | Xác thực Azure / mạng | Thêm key vault cho thông tin bảo mật |
| Chi phí | Tài nguyên thiết bị | Thanh toán theo mức tiêu thụ | Thêm giới hạn ngân sách |

## Danh sách kiểm tra xác thực

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Kỳ vọng lựa chọn mô hình dựa trên ý định và đầu ra cuối cùng được tinh chỉnh.

## Xử lý sự cố

| Vấn đề | Nguyên nhân | Cách khắc phục |
|--------|-------------|----------------|
| Tất cả nhiệm vụ được định tuyến đến cùng một mô hình | Quy tắc yếu | Làm phong phú bộ regex INTENT_RULES |
| Pipeline thất bại giữa chừng | Mô hình chưa được tải | Chạy `foundry model run <model>` |
| Đầu ra không đồng nhất | Không có giai đoạn tinh chỉnh | Thêm bước tóm tắt/xác thực |

## Tài liệu tham khảo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Tài liệu Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Mẫu chất lượng gợi ý: Xem Buổi 2

---

**Thời lượng buổi học**: 30 phút  
**Độ khó**: Chuyên gia

## Kịch bản mẫu & ánh xạ workshop

| Tập lệnh Workshop / Notebook | Kịch bản | Mục tiêu | Nguồn dữ liệu / Danh mục |
|------------------------------|----------|----------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Trợ lý phát triển xử lý các gợi ý ý định hỗn hợp (tái cấu trúc, tóm tắt, phân loại) | Ý định heuristic → định tuyến alias mô hình với sử dụng token | `CATALOG` nội tuyến + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Lập kế hoạch & tinh chỉnh nhiều bước cho nhiệm vụ hỗ trợ mã hóa phức tạp | Phân tích → thực thi chuyên biệt → bước tinh chỉnh tóm tắt | Cùng `CATALOG`; các bước được dẫn xuất từ đầu ra kế hoạch |

### Tường thuật kịch bản
Một công cụ tăng năng suất kỹ thuật nhận các nhiệm vụ không đồng nhất: tái cấu trúc mã, tóm tắt ghi chú kiến trúc, phân loại phản hồi. Để giảm độ trễ & sử dụng tài nguyên, một mô hình nhỏ tổng quát lập kế hoạch và tóm tắt, một mô hình chuyên về mã xử lý tái cấu trúc, và một mô hình nhẹ có khả năng phân loại gắn nhãn phản hồi. Tập lệnh pipeline minh họa việc kết nối + tinh chỉnh; tập lệnh router cô lập định tuyến gợi ý đơn thích ứng.

### Ảnh chụp danh mục
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Ví dụ gợi ý kiểm tra
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Mở rộng trace (Tùy chọn)
Thêm các dòng JSON trace từng bước cho `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Phác thảo Heuristic nâng cấp

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


### Tải lại danh mục mô hình động

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.