# เซสชัน 6: Foundry Local – โมเดลเป็นเครื่องมือ

## บทคัดย่อ

มองว่าโมเดลเป็นเครื่องมือที่สามารถประกอบกันได้ภายในชั้นปฏิบัติการ AI ท้องถิ่น เซสชันนี้จะแสดงวิธีการเชื่อมโยงการเรียกใช้ SLM/LLM เฉพาะทางหลายตัว การกำหนดเส้นทางงานอย่างเลือกสรร และการเปิดเผย SDK แบบรวมให้กับแอปพลิเคชัน คุณจะสร้างตัวกำหนดเส้นทางโมเดลน้ำหนักเบา + ตัววางแผนงาน รวมเข้ากับสคริปต์แอป และวางแผนการขยายไปยัง Azure AI Foundry สำหรับการทำงานในระดับการผลิต

## วัตถุประสงค์การเรียนรู้

- **เข้าใจแนวคิด** โมเดลเป็นเครื่องมือที่มีความสามารถที่ประกาศไว้
- **กำหนดเส้นทาง** คำขอโดยอิงตามเจตนา / การให้คะแนนแบบฮิวริสติก
- **เชื่อมโยง** ผลลัพธ์ในงานหลายขั้นตอน (แยก → แก้ไข → ปรับปรุง)
- **รวม** API ลูกค้าแบบรวมสำหรับแอปพลิเคชันปลายน้ำ
- **ขยาย** การออกแบบไปยังคลาวด์ (สัญญาที่เข้ากันได้กับ OpenAI)

## ความต้องการเบื้องต้น

- ผ่านเซสชัน 1–5 แล้ว
- มีโมเดลท้องถิ่นหลายตัวที่แคชไว้ (เช่น `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### ตัวอย่างสภาพแวดล้อมข้ามแพลตฟอร์ม

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

การเข้าถึงบริการระยะไกล/VM จาก macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ลำดับการสาธิต (30 นาที)

### 1. การประกาศความสามารถของเครื่องมือ (5 นาที)

สร้าง `samples/06-tools/models_catalog.py`:

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


### 2. การตรวจจับเจตนาและการกำหนดเส้นทาง (8 นาที)

สร้าง `samples/06-tools/router.py`:

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


### 3. การเชื่อมโยงงานหลายขั้นตอน (7 นาที)

สร้าง `samples/06-tools/pipeline.py`:

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


### 4. โครงการเริ่มต้น: ปรับ `06-models-as-tools` (5 นาที)

การปรับปรุง:
- เพิ่มการสนับสนุนโทเค็นแบบสตรีม (อัปเดต UI แบบก้าวหน้า)
- เพิ่มการให้คะแนนความมั่นใจ: การทับซ้อนทางศัพท์หรือเกณฑ์คำสั่ง
- ส่งออก JSON การติดตาม (เจตนา → โมเดล → เวลาแฝง → การใช้โทเค็น)
- ใช้แคชซ้ำสำหรับขั้นตอนย่อยที่ซ้ำกัน

### 5. เส้นทางการขยายไปยัง Azure (5 นาที)

| ชั้น | ท้องถิ่น (Foundry) | คลาวด์ (Azure AI Foundry) | กลยุทธ์การเปลี่ยนผ่าน |
|------|---------------------|---------------------------|-------------------------|
| การกำหนดเส้นทาง | Python ฮิวริสติก | บริการไมโครที่ทนทาน | คอนเทนเนอร์และปรับใช้ API |
| โมเดล | SLMs ที่แคชไว้ | การปรับใช้ที่จัดการ | แมปชื่อท้องถิ่นกับ ID การปรับใช้ |
| การสังเกตการณ์ | สถิติ CLI/ด้วยมือ | การบันทึกและเมตริกแบบรวมศูนย์ | เพิ่มเหตุการณ์การติดตามที่มีโครงสร้าง |
| ความปลอดภัย | โฮสต์ท้องถิ่นเท่านั้น | การรับรองความถูกต้องของ Azure / เครือข่าย | เพิ่ม key vault สำหรับความลับ |
| ค่าใช้จ่าย | ทรัพยากรอุปกรณ์ | การเรียกเก็บเงินตามการใช้งาน | เพิ่มการป้องกันงบประมาณ |

## รายการตรวจสอบการตรวจสอบ

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

คาดหวังการเลือกโมเดลตามเจตนาและผลลัพธ์ที่ปรับปรุงขั้นสุดท้าย

## การแก้ไขปัญหา

| ปัญหา | สาเหตุ | วิธีแก้ไข |
|-------|--------|----------|
| งานทั้งหมดถูกกำหนดเส้นทางไปยังโมเดลเดียวกัน | กฎอ่อนแอ | เพิ่มชุด regex INTENT_RULES |
| ท่อส่งล้มเหลวในขั้นตอนกลาง | โมเดลที่โหลดหายไป | รัน `foundry model run <model>` |
| ความสอดคล้องของผลลัพธ์ต่ำ | ไม่มีขั้นตอนการปรับปรุง | เพิ่มขั้นตอนการสรุป/การตรวจสอบ |

## อ้างอิง

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- เอกสาร Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- รูปแบบคุณภาพคำสั่ง: ดูเซสชัน 2

---

**ระยะเวลาเซสชัน**: 30 นาที  
**ระดับความยาก**: ผู้เชี่ยวชาญ

## ตัวอย่างสถานการณ์และการจับคู่เวิร์กช็อป

| สคริปต์ / โน้ตบุ๊กเวิร์กช็อป | สถานการณ์ | วัตถุประสงค์ | แหล่งข้อมูล / แคตตาล็อก |
|-------------------------------|------------|---------------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | ผู้ช่วยนักพัฒนาที่จัดการคำสั่งเจตนาผสม (ปรับโครงสร้าง, สรุป, จัดประเภท) | เจตนาฮิวริสติก → การกำหนดเส้นทางชื่อโมเดลพร้อมการใช้โทเค็น | `CATALOG` แบบอินไลน์ + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | การวางแผนหลายขั้นตอนและการปรับปรุงสำหรับงานช่วยเหลือการเขียนโค้ดที่ซับซ้อน | แยก → การดำเนินการเฉพาะทาง → ขั้นตอนการปรับปรุงการสรุป | `CATALOG` เดียวกัน; ขั้นตอนที่ได้มาจากผลลัพธ์แผน |

### เรื่องราวสถานการณ์
เครื่องมือเพิ่มประสิทธิภาพวิศวกรรมได้รับงานที่หลากหลาย: ปรับโครงสร้างโค้ด สรุปบันทึกสถาปัตยกรรม จัดประเภทความคิดเห็น เพื่อให้ลดเวลาแฝงและการใช้ทรัพยากร โมเดลทั่วไปขนาดเล็กจะวางแผนและสรุป โมเดลเฉพาะทางด้านโค้ดจะจัดการการปรับโครงสร้าง และโมเดลที่มีความสามารถในการจัดประเภทน้ำหนักเบาจะติดป้ายความคิดเห็น สคริปต์ท่อส่งแสดงการเชื่อมโยง + การปรับปรุง; สคริปต์ตัวกำหนดเส้นทางแยกการกำหนดเส้นทางคำสั่งเดียวที่ปรับเปลี่ยนได้

### สแนปชอตแคตตาล็อก
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### ตัวอย่างคำสั่งทดสอบ
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### การขยายการติดตาม (ตัวเลือก)
เพิ่มบรรทัด JSON การติดตามต่อขั้นตอนสำหรับ `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### ฮิวริสติกการยกระดับ (แนวคิด)
หากแผนมีคำสำคัญเช่น "ปรับปรุง", "ความปลอดภัย" หรือความยาวขั้นตอน > 280 ตัวอักษร → ยกระดับไปยังโมเดลที่ใหญ่กว่า (เช่น `gpt-oss-20b`) สำหรับขั้นตอนนั้นเท่านั้น

### การปรับปรุงตัวเลือก

| ด้าน | การปรับปรุง | คุณค่า | คำแนะนำ |
|------|-------------|--------|---------|
| การแคช | ใช้ตัวจัดการ + วัตถุลูกค้าใหม่ | ลดเวลาแฝง ลดค่าใช้จ่าย | ใช้ `workshop_utils.get_client` |
| เมตริกการใช้งาน | จับโทเค็น & เวลาแฝงต่อขั้นตอน | การวิเคราะห์และการปรับปรุง | วัดเวลาการเรียกแต่ละครั้ง; เก็บในรายการติดตาม |
| การกำหนดเส้นทางแบบปรับตัว | ความมั่นใจ / ต้นทุนที่รับรู้ | การแลกเปลี่ยนคุณภาพ-ต้นทุนที่ดีขึ้น | เพิ่มการให้คะแนน: หากคำสั่ง > N ตัวอักษรหรือ regex ตรงกับโดเมน → ยกระดับไปยังโมเดลที่ใหญ่ขึ้น |
| การลงทะเบียนความสามารถแบบไดนามิก | แคตตาล็อกโหลดใหม่แบบทันที | ไม่ต้องรีสตาร์ทหรือปรับใช้ใหม่ | โหลด `catalog.json` ขณะรัน; ตรวจสอบ timestamp ไฟล์ |
| กลยุทธ์สำรอง | ความทนทานต่อความล้มเหลว | ความพร้อมใช้งานสูงขึ้น | ลองใช้ตัวหลัก → หากเกิดข้อผิดพลาดให้ใช้ตัวสำรอง |
| ท่อส่งแบบสตรีม | ข้อเสนอแนะล่วงหน้า | การปรับปรุง UX | สตรีมแต่ละขั้นตอนและบัฟเฟอร์อินพุตการปรับปรุงขั้นสุดท้าย |
| การฝังเจตนาแบบเวกเตอร์ | การกำหนดเส้นทางที่ละเอียดขึ้น | ความแม่นยำของเจตนาสูงขึ้น | ฝังคำสั่ง, จัดกลุ่ม & แมปเซนทรอยด์ → ความสามารถ |
| การส่งออกการติดตาม | เชนที่ตรวจสอบได้ | การปฏิบัติตาม/การรายงาน | ส่งออก JSON บรรทัด: ขั้นตอน, เจตนา, โมเดล, เวลาแฝง_ms, โทเค็น |
| การจำลองต้นทุน | การประมาณการก่อนคลาวด์ | การวางแผนงบประมาณ | กำหนดต้นทุน/โทเค็นโดยประมาณต่อโมเดล & รวมต่องาน |
| โหมดกำหนดค่า | การทำซ้ำที่สามารถทำซ้ำได้ | การวัดผลที่เสถียร | Env: `temperature=0`, จำนวนขั้นตอนคงที่ |

#### ตัวอย่างโครงสร้างการติดตาม

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### สเก็ตช์การยกระดับแบบปรับตัว

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### การโหลดแคตตาล็อกโมเดลแบบทันที

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

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้