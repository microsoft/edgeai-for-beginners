# Buổi 6: Foundry Local – Mô hình như công cụ

## Tóm tắt

Xem mô hình như các công cụ có thể kết hợp bên trong lớp vận hành AI cục bộ. Buổi học này trình bày cách xâu chuỗi nhiều lần gọi SLM/LLM chuyên biệt, định tuyến nhiệm vụ chọn lọc và cung cấp giao diện SDK thống nhất cho các ứng dụng. Bạn sẽ xây dựng một bộ định tuyến mô hình nhẹ + bộ lập kế hoạch nhiệm vụ, tích hợp nó vào một script ứng dụng, và phác thảo con đường mở rộng lên Azure AI Foundry cho khối lượng công việc sản xuất.

## Mục tiêu học tập

- **Khái niệm hóa** mô hình như các công cụ nguyên tử với khả năng được tuyên bố
- **Định tuyến** yêu cầu dựa trên ý định / điểm heuristic
- **Xâu chuỗi** đầu ra qua các nhiệm vụ nhiều bước (phân rã → giải quyết → tinh chỉnh)
- **Tích hợp** API khách hàng thống nhất cho các ứng dụng hạ nguồn
- **Mở rộng** thiết kế lên đám mây (hợp đồng tương thích OpenAI giống nhau)

## Yêu cầu trước

- Hoàn thành các buổi 1–5
- Nhiều mô hình cục bộ được lưu cache (vd: `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

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

Truy cập dịch vụ Remote/VM từ macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Luồng demo (30 phút)

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

### 2. Phát hiện ý định & Định tuyến (8 phút)

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
    # Chấm điểm danh mục: ưu tiên khớp năng lực trước, sau đó ưu tiên
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sắp xếp: khớp True trước, sau đó giá trị ưu tiên thấp nhất
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

### 3. Xâu chuỗi nhiệm vụ nhiều bước (7 phút)

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

Các cải tiến:
- Thêm hỗ trợ phát token theo luồng (cập nhật giao diện người dùng tiến triển)
- Thêm điểm đánh giá độ tin cậy: trùng lặp từ vựng hoặc rubric prompt
- Xuất trace JSON (ý định → mô hình → độ trễ → sử dụng token)
- Thực hiện tái sử dụng cache cho các bước con lặp lại

### 5. Lộ trình mở rộng lên Azure (5 phút)

| Lớp | Cục bộ (Foundry) | Đám mây (Azure AI Foundry) | Chiến lược chuyển đổi |
|-------|-----------------|--------------------------|---------------------|
| Định tuyến | Python heuristic | Microservice bền vững | Đóng gói container & triển khai API |
| Mô hình | SLM lưu cache | Triển khai quản lý | Ánh xạ tên cục bộ sang ID triển khai |
| Quan sát | Thống kê CLI/thủ công | Ghi log trung tâm & số liệu | Thêm sự kiện trace có cấu trúc |
| Bảo mật | Chỉ máy chủ cục bộ | Xác thực Azure / mạng | Giới thiệu kho khóa cho bí mật |
| Chi phí | Tài nguyên thiết bị | Thanh toán theo mức sử dụng | Thêm giới hạn ngân sách |

## Danh sách kiểm tra xác thực

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Dự kiến lựa chọn mô hình dựa trên ý định và đầu ra cuối cùng được tinh chỉnh.

## Khắc phục sự cố

| Vấn đề | Nguyên nhân | Sửa lỗi |
|---------|-------|-----|
| Tất cả nhiệm vụ định tuyến đến cùng một mô hình | Quy tắc yếu | Mở rộng tập regex INTENT_RULES |
| Pipeline thất bại giữa chừng | Mô hình chưa được tải | Chạy `foundry model run <model>` |
| Đầu ra kém kết dính | Thiếu bước tinh chỉnh | Thêm bước tóm tắt/xác thực |

## Tham khảo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Tài liệu Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Mẫu chất lượng prompt: Xem Buổi 2

---

**Thời lượng buổi học**: 30 phút  
**Độ khó**: Chuyên gia

## Kịch bản mẫu & bản đồ Workshop

| Script / Notebook Workshop | Kịch bản | Mục tiêu | Dataset / Nguồn Catalog |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Trợ lý lập trình viên xử lý prompt đa ý định (refactor, tóm tắt, phân loại) | Định tuyến ý định heuristic → bí danh mô hình với sử dụng token | `CATALOG` inline + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Lập kế hoạch nhiều bước & tinh chỉnh cho nhiệm vụ hỗ trợ lập trình phức tạp | Phân rã → thực thi chuyên biệt → bước tinh chỉnh tóm tắt | Cùng `CATALOG`; các bước lấy từ kết quả kế hoạch |

### Tường thuật Kịch bản
Một công cụ tăng năng suất kỹ thuật nhận nhiệm vụ đa dạng: tái cấu trúc code, tóm tắt ghi chú kiến trúc, phân loại phản hồi. Để giảm độ trễ & sử dụng tài nguyên, một mô hình tổng quát nhỏ lên kế hoạch và tóm tắt, một mô hình chuyên code xử lý tái cấu trúc, và một mô hình nhẹ có khả năng phân loại gán nhãn phản hồi. Script pipeline minh họa xâu chuỗi + tinh chỉnh; script router tách biệt định tuyến prompt đơn thích ứng.

### Ảnh chụp catalog
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```

### Ví dụ prompt kiểm thử
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```

### Mở rộng Trace (tùy chọn)
Thêm dòng trace JSON mỗi bước cho `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```

### Heuristic leo thang (Ý tưởng)
Nếu kế hoạch chứa từ khóa như "optimize", "security", hoặc độ dài bước > 280 ký tự → leo thang lên mô hình lớn hơn (vd: `gpt-oss-20b`) chỉ cho bước đó.

### Các cải tiến tùy chọn

| Lĩnh vực | Cải tiến | Giá trị | Gợi ý |
|------|-------------|-------|------|
| Caching | Tái sử dụng manager + client objects | Giảm độ trễ, ít overhead hơn | Dùng `workshop_utils.get_client` |
| Metrics sử dụng | Ghi nhận token & độ trễ mỗi bước | Phân tích & tối ưu | Đo thời gian mỗi gọi định tuyến; lưu vào danh sách trace |
| Định tuyến thích ứng | Ý thức độ tin cậy / chi phí | Cân bằng chất lượng - chi phí tốt hơn | Thêm điểm số: nếu prompt > N ký tự hoặc regex trùng domain → leo thang mô hình to hơn |
| Registry năng lực động | Tải lại catalog nóng | Không cần khởi động lại triển khai lại | Tải `catalog.json` lúc chạy; theo dõi dấu thời gian file |
| Chiến lược dự phòng | Độ bền khi lỗi | Tăng tính sẵn sàng | Thử chính → khi lỗi dùng bí danh dự phòng |
| Pipeline streaming | Feedback sớm | Cải tiến UX | Phát stream từng bước, đệm đầu vào tinh chỉnh cuối |
| Embedding ý định vector | Định tuyến tinh tế hơn | Chính xác ý định cao hơn | Nhúng prompt, phân nhóm & ánh xạ tâm cụm → năng lực |
| Xuất trace | Chuỗi có thể kiểm toán | Tuân thủ/báo cáo | Xuất dòng JSON: bước, ý định, mô hình, độ trễ_ms, token |
| Mô phỏng chi phí | Ước tính trước đám mây | Lập kế hoạch ngân sách | Gán chi phí tượng trưng/token mỗi mô hình & tổng hợp mỗi nhiệm vụ |
| Chế độ xác định | Lặp lại được tái tạo | Đánh giá ổn định | Env: `temperature=0`, số bước cố định |

#### Ví dụ cấu trúc Trace

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```

#### Phác thảo leo thang thích ứng

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # nâng cấp lên mô hình suy luận lớn hơn nếu có sẵn
    alias = 'gpt-oss-20b'
```

#### Tải lại nóng Catalog mô hình

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

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->