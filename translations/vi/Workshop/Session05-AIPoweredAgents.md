# Buổi 5: Xây dựng các tác nhân AI nhanh chóng với Foundry Local

## Tóm tắt

Thiết kế và điều phối các tác nhân AI đa vai trò bằng cách tận dụng runtime của Foundry Local với độ trễ thấp và bảo vệ quyền riêng tư. Bạn sẽ định nghĩa vai trò của tác nhân, chiến lược bộ nhớ, mẫu gọi công cụ và đồ thị thực thi. Buổi học giới thiệu các mẫu khung mà bạn có thể mở rộng với Chainlit hoặc LangGraph. Dự án khởi đầu mở rộng mẫu kiến trúc tác nhân hiện có để thêm khả năng lưu trữ bộ nhớ và các hook đánh giá.

## Mục tiêu học tập

- **Định nghĩa vai trò**: Lời nhắc hệ thống & giới hạn khả năng
- **Triển khai bộ nhớ**: Ngắn hạn (hội thoại), dài hạn (vector / file), bảng tạm tạm thời
- **Xây dựng quy trình làm việc**: Các bước tác nhân tuần tự, phân nhánh và song song
- **Tích hợp công cụ**: Mẫu gọi công cụ hàm nhẹ
- **Đánh giá**: Theo dõi cơ bản + chấm điểm kết quả dựa trên tiêu chí

## Yêu cầu trước

- Hoàn thành các buổi 1–4
- Python với `foundry-local-sdk`, `openai`, tùy chọn `chainlit`
- Các mô hình cục bộ đang chạy (ít nhất `phi-4-mini`)

### Đoạn mã môi trường đa nền tảng

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Nếu chạy các tác nhân từ macOS đối với dịch vụ máy chủ Windows từ xa:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Quy trình demo (30 phút)

### 1. Định nghĩa vai trò & bộ nhớ của tác nhân (7 phút)

Tạo `samples/05-agents/agents_core.py`:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. Mẫu xây dựng khung CLI (3 phút)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Thêm gọi công cụ (7 phút)

Mở rộng với `samples/05-agents/tools.py`:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```


Chỉnh sửa `agents_core.py` để cho phép cú pháp công cụ đơn giản: người dùng viết `#tool:get_time` và tác nhân mở rộng đầu ra của công cụ vào ngữ cảnh trước khi tạo.

### 4. Quy trình làm việc được điều phối (6 phút)

Tạo `samples/05-agents/orchestrator.py`:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. Dự án khởi đầu: Mở rộng `05-agent-architecture` (7 phút)

Thêm:
1. Lớp bộ nhớ bền vững (ví dụ: thêm dòng JSON của các cuộc hội thoại)
2. Tiêu chí đánh giá đơn giản: các tiêu chí về tính chính xác / rõ ràng / phong cách
3. Giao diện front-end tùy chọn của Chainlit (hai tab: hội thoại & theo dõi)
4. Máy trạng thái kiểu LangGraph tùy chọn (nếu thêm phụ thuộc) cho các quyết định phân nhánh

## Danh sách kiểm tra xác thực

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Kỳ vọng đầu ra của pipeline có cấu trúc với ghi chú về việc tiêm công cụ.

## Tổng quan về chiến lược bộ nhớ

| Lớp | Mục đích | Ví dụ |
|-----|----------|-------|
| Ngắn hạn | Liên tục hội thoại | N tin nhắn cuối cùng |
| Tập hợp | Nhớ lại phiên | JSON cho mỗi phiên |
| Ngữ nghĩa | Truy xuất dài hạn | Lưu trữ vector của các bản tóm tắt |
| Bảng tạm | Các bước suy luận | Chuỗi suy nghĩ nội tuyến (riêng tư) |

## Hook đánh giá (Khái niệm)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Xử lý sự cố

| Vấn đề | Nguyên nhân | Giải pháp |
|--------|-------------|-----------|
| Câu trả lời lặp lại | Cửa sổ ngữ cảnh quá lớn/nhỏ | Điều chỉnh tham số cửa sổ bộ nhớ |
| Công cụ không được gọi | Sai cú pháp | Sử dụng định dạng `#tool:tool_name` |
| Điều phối chậm | Nhiều mô hình lạnh | Chạy trước các lời nhắc khởi động |

## Tài liệu tham khảo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (khái niệm tùy chọn): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Thời lượng buổi học**: 30 phút  
**Độ khó**: Nâng cao

## Kịch bản mẫu & ánh xạ workshop

| Kịch bản workshop | Kịch bản | Mục tiêu | Lời nhắc ví dụ |
|--------------------|----------|----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot nghiên cứu kiến thức tạo ra các bản tóm tắt thân thiện với lãnh đạo | Pipeline hai tác nhân (nghiên cứu → chỉnh sửa) với các mô hình tùy chọn khác biệt | Giải thích tại sao suy luận biên lại quan trọng đối với tuân thủ. |
| (Mở rộng) khái niệm `tools.py` | Thêm công cụ ước tính thời gian & token | Minh họa mẫu gọi công cụ nhẹ | #tool:get_time |

### Tường thuật kịch bản

Nhóm tài liệu tuân thủ cần các bản tóm tắt nội bộ nhanh chóng được lấy từ kiến thức cục bộ mà không gửi bản nháp lên các dịch vụ đám mây. Một tác nhân nghiên cứu thu thập các điểm chính xác ngắn gọn; một tác nhân biên tập viết lại để rõ ràng hơn cho lãnh đạo. Các bí danh mô hình khác biệt có thể được gán để tối ưu hóa độ trễ (SLM nhanh) so với tinh chỉnh phong cách (mô hình lớn hơn chỉ khi cần thiết).

### Môi trường đa mô hình ví dụ

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Cấu trúc theo dõi (Tùy chọn)

```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

Lưu từng bước vào tệp JSONL để chấm điểm tiêu chí sau này.

### Cải tiến tùy chọn

| Chủ đề | Cải tiến | Lợi ích | Phác thảo triển khai |
|--------|----------|---------|-----------------------|
| Vai trò đa mô hình | Các mô hình khác biệt cho mỗi tác nhân (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Chuyên môn hóa & tốc độ | Chọn biến môi trường bí danh, gọi `chat_once` với bí danh theo vai trò |
| Theo dõi có cấu trúc | Theo dõi JSON của mỗi hành động (công cụ, đầu vào, độ trễ, token) | Gỡ lỗi & đánh giá | Thêm dict vào danh sách; ghi `.jsonl` khi kết thúc |
| Lưu trữ bộ nhớ | Ngữ cảnh hội thoại có thể tải lại | Liên tục phiên | Xuất `Agent.memory` ra `sessions/<ts>.json` |
| Đăng ký công cụ | Khám phá công cụ động | Khả năng mở rộng | Duy trì dict `TOOLS` & kiểm tra tên/mô tả |
| Thử lại & lùi lại | Chuỗi dài mạnh mẽ | Giảm lỗi tạm thời | Bao bọc `act` với try/except + lùi lại theo cấp số nhân |
| Chấm điểm tiêu chí | Nhãn định tính tự động | Theo dõi cải tiến | Lượt thứ hai nhắc mô hình: "Đánh giá độ rõ ràng 1-5" |
| Bộ nhớ vector | Nhớ lại ngữ nghĩa | Ngữ cảnh dài hạn phong phú | Nhúng các bản tóm tắt, truy xuất top-k vào thông điệp hệ thống |
| Phản hồi trực tuyến | Cảm nhận phản hồi nhanh hơn | Cải thiện UX | Sử dụng phản hồi trực tuyến khi có sẵn và xả các token từng phần |
| Kiểm tra xác định | Kiểm soát hồi quy | CI ổn định | Chạy với `temperature=0`, hạt giống lời nhắc cố định |
| Phân nhánh song song | Khám phá nhanh hơn | Tăng thông lượng | Sử dụng `concurrent.futures` cho các bước tác nhân độc lập |

#### Ví dụ ghi lại theo dõi

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Lời nhắc đánh giá đơn giản

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Lưu cặp (`answer`, `rating`) để xây dựng biểu đồ chất lượng lịch sử.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.