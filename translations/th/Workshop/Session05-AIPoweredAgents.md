<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T21:59:03+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "th"
}
-->
# เซสชัน 5: สร้างตัวแทน AI ที่ทรงพลังได้อย่างรวดเร็วด้วย Foundry Local

## บทคัดย่อ

ออกแบบและจัดการตัวแทน AI หลายบทบาทโดยใช้ Foundry Local ที่มีการทำงานแบบเรียลไทม์และรักษาความเป็นส่วนตัว คุณจะได้กำหนดบทบาทของตัวแทน กลยุทธ์การจดจำรูปแบบ การเรียกใช้เครื่องมือ และกราฟการดำเนินการ เซสชันนี้จะแนะนำรูปแบบการสร้างโครงสร้างที่คุณสามารถขยายได้ด้วย Chainlit หรือ LangGraph โครงการเริ่มต้นจะขยายตัวอย่างสถาปัตยกรรมตัวแทนที่มีอยู่เพื่อเพิ่มการบันทึกความจำและการประเมินผล

## วัตถุประสงค์การเรียนรู้

- **กำหนดบทบาท**: คำแนะนำระบบและขอบเขตความสามารถ
- **การใช้งานความจำ**: ความจำระยะสั้น (การสนทนา), ความจำระยะยาว (เวกเตอร์ / ไฟล์), พื้นที่ชั่วคราว
- **สร้างโครงสร้างการทำงาน**: ขั้นตอนตัวแทนแบบลำดับ แบบแยกสาขา และแบบขนาน
- **รวมเครื่องมือ**: รูปแบบการเรียกใช้ฟังก์ชันเครื่องมือที่เบา
- **การประเมินผล**: การติดตามพื้นฐาน + การให้คะแนนผลลัพธ์ตามเกณฑ์

## ข้อกำหนดเบื้องต้น

- ผ่านเซสชัน 1–4 แล้ว
- Python พร้อม `foundry-local-sdk`, `openai`, และ `chainlit` (ตัวเลือก)
- โมเดลที่ทำงานในเครื่อง (อย่างน้อย `phi-4-mini`)

### ตัวอย่างการตั้งค่าสภาพแวดล้อมข้ามแพลตฟอร์ม

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

หากเรียกใช้ตัวแทนจาก macOS กับบริการโฮสต์ Windows ระยะไกล:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ลำดับการสาธิต (30 นาที)

### 1. กำหนดบทบาทตัวแทนและความจำ (7 นาที)

สร้าง `samples/05-agents/agents_core.py`:

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


### 2. รูปแบบการสร้างโครงสร้าง CLI (3 นาที)

```powershell
python samples/05-agents/agents_core.py
```


### 3. เพิ่มการเรียกใช้เครื่องมือ (7 นาที)

ขยายด้วย `samples/05-agents/tools.py`:

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

แก้ไข `agents_core.py` เพื่อให้สามารถใช้ไวยากรณ์เครื่องมือแบบง่าย: ผู้ใช้เขียน `#tool:get_time` และตัวแทนจะขยายผลลัพธ์ของเครื่องมือไปยังบริบทก่อนการสร้าง

### 4. การจัดการโครงสร้างการทำงาน (6 นาที)

สร้าง `samples/05-agents/orchestrator.py`:

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


### 5. โครงการเริ่มต้น: ขยาย `05-agent-architecture` (7 นาที)

เพิ่ม:
1. ชั้นความจำที่คงอยู่ (เช่น การเพิ่มบรรทัด JSON ของการสนทนา)
2. เกณฑ์การประเมินผลแบบง่าย: ความถูกต้อง / ความชัดเจน / ตัวแทนสไตล์
3. ส่วนหน้าของ Chainlit (สองแท็บ: การสนทนาและการติดตาม)
4. เครื่องจักรสถานะสไตล์ LangGraph (ถ้าเพิ่มการพึ่งพา) สำหรับการตัดสินใจแบบแยกสาขา

## รายการตรวจสอบการตรวจสอบ

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

คาดหวังผลลัพธ์ของกระบวนการที่มีโครงสร้างพร้อมหมายเหตุการฉีดเครื่องมือ

## ภาพรวมกลยุทธ์ความจำ

| ชั้น | วัตถุประสงค์ | ตัวอย่าง |
|------|--------------|----------|
| ระยะสั้น | ความต่อเนื่องของการสนทนา | ข้อความล่าสุด N ข้อความ |
| ระยะตอน | การจดจำเซสชัน | JSON ต่อเซสชัน |
| เชิงความหมาย | การดึงข้อมูลระยะยาว | การจัดเก็บเวกเตอร์ของสรุป |
| พื้นที่ชั่วคราว | ขั้นตอนการให้เหตุผล | การคิดแบบเชื่อมโยงในตัว (ส่วนตัว) |

## จุดเชื่อมต่อการประเมินผล (แนวคิด)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## การแก้ไขปัญหา

| ปัญหา | สาเหตุ | วิธีแก้ไข |
|-------|--------|-----------|
| คำตอบซ้ำซาก | หน้าต่างบริบทใหญ่/เล็กเกินไป | ปรับพารามิเตอร์หน้าต่างความจำ |
| เครื่องมือไม่ได้ถูกเรียกใช้ | ไวยากรณ์ผิด | ใช้รูปแบบ `#tool:tool_name` |
| การจัดการโครงสร้างช้า | โมเดลเย็นหลายตัว | เริ่มต้นคำแนะนำอุ่นเครื่องล่วงหน้า |

## อ้างอิง

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (แนวคิดเพิ่มเติม): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**ระยะเวลาเซสชัน**: 30 นาที  
**ระดับความยาก**: ขั้นสูง

## ตัวอย่างสถานการณ์และการจับคู่เวิร์กช็อป

| สคริปต์เวิร์กช็อป | สถานการณ์ | วัตถุประสงค์ | ตัวอย่างคำถาม |
|--------------------|------------|---------------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | บอทวิจัยความรู้ที่สร้างสรุปสำหรับผู้บริหาร | ท่อส่งตัวแทนสองตัว (วิจัย → ขัดเกลาเนื้อหา) พร้อมโมเดลที่แตกต่างกัน | อธิบายว่าทำไมการวิเคราะห์แบบ edge inference จึงสำคัญต่อการปฏิบัติตามข้อกำหนด |
| แนวคิด `tools.py` (ขยาย) | เพิ่มเครื่องมือประมาณเวลาและโทเค็น | สาธิตรูปแบบการเรียกใช้เครื่องมือที่เบา | #tool:get_time |

### เรื่องราวสถานการณ์
ทีมเอกสารการปฏิบัติตามข้อกำหนดต้องการบทสรุปภายในที่รวดเร็วซึ่งมาจากความรู้ในท้องถิ่นโดยไม่ต้องส่งร่างไปยังบริการคลาวด์ ตัวแทนวิจัยรวบรวมข้อมูลข้อเท็จจริงที่กระชับ; ตัวแทนบรรณาธิการเขียนใหม่เพื่อความชัดเจนสำหรับผู้บริหาร สามารถกำหนดชื่อโมเดลที่แตกต่างกันเพื่อเพิ่มประสิทธิภาพความเร็ว (SLM ที่เร็ว) กับการปรับแต่งสไตล์ (โมเดลที่ใหญ่กว่าเมื่อจำเป็น)

### ตัวอย่างสภาพแวดล้อมหลายโมเดล
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### โครงสร้างการติดตาม (ตัวเลือก)
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

บันทึกแต่ละขั้นตอนลงในไฟล์ JSONL เพื่อการให้คะแนนตามเกณฑ์ในภายหลัง

### การปรับปรุงเพิ่มเติม (ตัวเลือก)

| ธีม | การปรับปรุง | ประโยชน์ | ร่างการดำเนินการ |
|-----|-------------|----------|-------------------|
| บทบาทหลายโมเดล | โมเดลที่แตกต่างกันต่อตัวแทน (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | ความเชี่ยวชาญและความเร็ว | เลือกตัวแปรแวดล้อม alias, เรียก `chat_once` ด้วย alias ต่อบทบาท |
| การติดตามที่มีโครงสร้าง | การติดตาม JSON ของแต่ละการกระทำ (เครื่องมือ, อินพุต, เวลาแฝง, โทเค็น) | การดีบักและการประเมินผล | เพิ่ม dict ลงในรายการ; เขียน `.jsonl` เมื่อสิ้นสุด |
| ความจำที่คงอยู่ | บริบทการสนทนาที่โหลดใหม่ได้ | ความต่อเนื่องของเซสชัน | บันทึก `Agent.memory` ไปยัง `sessions/<ts>.json` |
| การลงทะเบียนเครื่องมือ | การค้นพบเครื่องมือแบบไดนามิก | ความสามารถในการขยาย | รักษา dict `TOOLS` และตรวจสอบชื่อ/คำอธิบาย |
| การลองใหม่และการถอยกลับ | โซ่ยาวที่แข็งแกร่ง | ลดความล้มเหลวชั่วคราว | ห่อ `act` ด้วย try/except + การถอยกลับแบบเอ็กซ์โพเนนเชียล |
| การให้คะแนนตามเกณฑ์ | ป้ายกำกับเชิงคุณภาพอัตโนมัติ | ติดตามการปรับปรุง | การกระตุ้นรอบที่สองของโมเดล: "ให้คะแนนความชัดเจน 1-5" |
| ความจำเวกเตอร์ | การดึงข้อมูลเชิงความหมาย | บริบทระยะยาวที่สมบูรณ์ | ฝังสรุป ดึง top-k ไปยังข้อความระบบ |
| การตอบกลับแบบสตรีม | การตอบสนองที่เร็วขึ้น | การปรับปรุง UX | ใช้การสตรีมเมื่อพร้อมใช้งานและล้างโทเค็นบางส่วน |
| การทดสอบแบบกำหนด | การควบคุมการถดถอย | CI ที่เสถียร | เรียกใช้ด้วย `temperature=0`, เมล็ดคำแนะนำคงที่ |
| การแยกสาขาแบบขนาน | การสำรวจที่เร็วขึ้น | ประสิทธิภาพ | ใช้ `concurrent.futures` สำหรับขั้นตอนตัวแทนที่เป็นอิสระ |

#### ตัวอย่างบันทึกการติดตาม

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### คำถามการประเมินผลแบบง่าย

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

บันทึกคู่ (`answer`, `rating`) เพื่อสร้างกราฟคุณภาพในประวัติศาสตร์

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้