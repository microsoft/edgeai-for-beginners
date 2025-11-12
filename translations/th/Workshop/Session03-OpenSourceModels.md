<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:10:30+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "th"
}
-->
# เซสชัน 3: โมเดลโอเพ่นซอร์สใน Foundry Local

## บทคัดย่อ

เรียนรู้วิธีนำโมเดลจาก Hugging Face และโอเพ่นซอร์สอื่นๆ เข้าสู่ Foundry Local พร้อมกลยุทธ์การเลือกโมเดล, การทำงานร่วมกับชุมชน, วิธีเปรียบเทียบประสิทธิภาพ และการขยาย Foundry ด้วยการลงทะเบียนโมเดลแบบกำหนดเอง เซสชันนี้สอดคล้องกับธีมการสำรวจ "Model Mondays" รายสัปดาห์ และช่วยให้คุณประเมินและใช้งานโมเดลโอเพ่นซอร์สในพื้นที่ก่อนที่จะขยายไปยัง Azure

## วัตถุประสงค์การเรียนรู้

เมื่อจบเซสชันนี้ คุณจะสามารถ:

- **ค้นหาและประเมิน**: ระบุโมเดลที่เหมาะสม (mistral, gemma, qwen, deepseek) โดยพิจารณาจากคุณภาพและทรัพยากรที่ต้องใช้
- **โหลดและใช้งาน**: ใช้ Foundry Local CLI เพื่อดาวน์โหลด, แคช และเปิดใช้งานโมเดลจากชุมชน
- **วัดผล**: ใช้เกณฑ์การวัดผลที่สม่ำเสมอ เช่น ความหน่วงเวลา + อัตราการประมวลผลโทเค็น + คุณภาพ
- **ขยาย**: ลงทะเบียนหรือปรับแต่ง wrapper โมเดลแบบกำหนดเองตามรูปแบบที่เข้ากันได้กับ SDK
- **เปรียบเทียบ**: สร้างการเปรียบเทียบที่มีโครงสร้างสำหรับการตัดสินใจเลือก SLM กับ LLM ขนาดกลาง

## ข้อกำหนดเบื้องต้น

- ผ่านเซสชัน 1 และ 2
- สภาพแวดล้อม Python ที่ติดตั้ง `foundry-local-sdk`
- พื้นที่ดิสก์ว่างอย่างน้อย 15GB สำหรับแคชโมเดลหลายตัว

### การเริ่มต้นใช้งานข้ามแพลตฟอร์มอย่างรวดเร็ว

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

เมื่อทำการวัดผลจาก macOS กับบริการโฮสต์ Windows ให้ตั้งค่า:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ลำดับการสาธิต (30 นาที)

### 1. โหลดโมเดล Hugging Face ผ่าน CLI (8 นาที)

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


### 2. รันและตรวจสอบเบื้องต้น (5 นาที)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. สคริปต์วัดผล (8 นาที)

สร้าง `samples/03-oss-models/benchmark_models.py`:

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

รัน:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. เปรียบเทียบประสิทธิภาพ (5 นาที)

พูดคุยเกี่ยวกับข้อดีข้อเสีย: เวลาโหลด, การใช้หน่วยความจำ (สังเกต Task Manager / `nvidia-smi` / ตัวตรวจสอบทรัพยากรของระบบปฏิบัติการ), คุณภาพผลลัพธ์เทียบกับความเร็ว ใช้สคริปต์วัดผล Python (เซสชัน 3) สำหรับความหน่วงเวลาและอัตราการประมวลผลโทเค็น; ทำซ้ำหลังจากเปิดใช้งานการเร่งความเร็ว GPU

### 5. โครงการเริ่มต้น (4 นาที)

สร้างตัวสร้างรายงานเปรียบเทียบโมเดล (ขยายสคริปต์วัดผลด้วยการส่งออก markdown)

## โครงการเริ่มต้น: ขยาย `03-huggingface-models`

ปรับปรุงตัวอย่างที่มีอยู่โดย:

1. เพิ่มการรวมผลวัดผล + การส่งออก CSV/Markdown
2. ใช้การให้คะแนนเชิงคุณภาพแบบง่าย (ชุดคำถาม + ไฟล์การใส่คำอธิบายด้วยมือ)
3. เพิ่ม JSON config (`models.json`) สำหรับรายการโมเดลที่ปรับเปลี่ยนได้และชุดคำถาม

## เช็คลิสต์การตรวจสอบ

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

โมเดลเป้าหมายทั้งหมดควรปรากฏและตอบสนองต่อคำขอแชทสำรวจ

## ตัวอย่างสถานการณ์และการจับคู่เวิร์กช็อป

| สคริปต์เวิร์กช็อป | สถานการณ์ | เป้าหมาย | แหล่งที่มาของคำถาม/ชุดข้อมูล |
|--------------------|------------|----------|--------------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | ทีมแพลตฟอร์ม Edge เลือก SLM เริ่มต้นสำหรับฟีเจอร์สรุปแบบฝังตัว | สร้างการเปรียบเทียบความหน่วงเวลา + p95 + อัตราโทเค็นต่อวินาทีระหว่างโมเดลที่เป็นตัวเลือก | ตัวแปร `PROMPT` ในตัว + รายการ `BENCH_MODELS` ในสภาพแวดล้อม |

### เรื่องราวสถานการณ์
ทีมวิศวกรรมผลิตภัณฑ์ต้องเลือกโมเดลสรุปน้ำหนักเบาเริ่มต้นสำหรับฟีเจอร์บันทึกการประชุมแบบออฟไลน์ พวกเขาทำการวัดผลแบบควบคุมและกำหนดค่าได้ (temperature=0) บนชุดคำถามที่กำหนดไว้ (ดูตัวอย่างด้านล่าง) และรวบรวมเมตริกความหน่วงเวลา + อัตราการประมวลผลโทเค็นทั้งแบบมีและไม่มีการเร่งความเร็ว GPU

### ตัวอย่างชุดคำถาม JSON (ขยายได้)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

วนลูปแต่ละคำถามต่อโมเดล จับเวลาความหน่วงต่อคำถามเพื่อคำนวณเมตริกการกระจายและตรวจจับค่าผิดปกติ

## กรอบการเลือกโมเดล

| มิติ | เมตริก | เหตุผลที่สำคัญ |
|------|--------|----------------|
| ความหน่วงเวลา | avg / p95 | ความสม่ำเสมอของประสบการณ์ผู้ใช้ |
| อัตราการประมวลผล | โทเค็น/วินาที | ความสามารถในการปรับขนาดแบบแบทช์และสตรีม |
| หน่วยความจำ | ขนาดที่ใช้งาน | ความเหมาะสมกับอุปกรณ์และการทำงานพร้อมกัน |
| คุณภาพ | คำถามตามเกณฑ์ | ความเหมาะสมของงาน |
| ขนาด | แคชดิสก์ | การกระจายและการอัปเดต |
| ใบอนุญาต | การอนุญาตใช้งาน | การปฏิบัติตามข้อกำหนดเชิงพาณิชย์ |

## การขยายด้วยโมเดลแบบกำหนดเอง

รูปแบบระดับสูง (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

ดูที่ repo อย่างเป็นทางการสำหรับอินเทอร์เฟซอะแดปเตอร์ที่พัฒนา:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## การแก้ไขปัญหา

| ปัญหา | สาเหตุ | วิธีแก้ไข |
|-------|--------|----------|
| OOM บน mistral-7b | RAM/GPU ไม่เพียงพอ | หยุดโมเดลอื่น; ลองใช้ตัวแปรที่เล็กกว่า |
| การตอบสนองครั้งแรกช้า | โหลดเย็น | รักษาความร้อนด้วยคำถามเบาๆ เป็นระยะ |
| การดาวน์โหลดหยุดชะงัก | ความไม่เสถียรของเครือข่าย | ลองใหม่; ดาวน์โหลดล่วงหน้าในช่วงเวลาที่ไม่ใช่ช่วงพีค |

## อ้างอิง

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**ระยะเวลาเซสชัน**: 30 นาที (+ การเจาะลึกเพิ่มเติม)  
**ระดับความยาก**: ระดับกลาง

### การปรับปรุงเพิ่มเติม (ตัวเลือก)

| การปรับปรุง | ประโยชน์ | วิธี |
|-------------|----------|-----|
| ความหน่วงเวลาของโทเค็นแรกแบบสตรีม | วัดการตอบสนองที่รับรู้ | รันการวัดผลด้วย `BENCH_STREAM=1` (สคริปต์ที่ปรับปรุงใน `Workshop/samples/session03`) |
| โหมดกำหนดค่า | การเปรียบเทียบการถดถอยที่เสถียร | `temperature=0`, ชุดคำถามที่กำหนด, จับ JSON outputs ภายใต้การควบคุมเวอร์ชัน |
| การให้คะแนนตามเกณฑ์คุณภาพ | เพิ่มมิติข้อมูลเชิงคุณภาพ | รักษา `prompts.json` พร้อมแง่มุมที่คาดหวัง; ใส่คะแนน (1–5) ด้วยมือหรือผ่านโมเดลรอง |
| การส่งออก CSV / Markdown | รายงานที่แชร์ได้ | ขยายสคริปต์เพื่อเขียน `benchmark_report.md` พร้อมตารางและไฮไลต์ |
| แท็กความสามารถของโมเดล | ช่วยการกำหนดเส้นทางอัตโนมัติในภายหลัง | รักษา `models.json` พร้อม `{alias: {capabilities:[], size_mb:..}}` |
| เฟสอุ่นเครื่องแคช | ลดอคติการเริ่มต้นเย็น | รันรอบอุ่นเครื่องหนึ่งครั้งก่อนลูปจับเวลา (มีการใช้งานแล้ว) |
| ความแม่นยำเปอร์เซ็นไทล์ | ความหน่วงปลายที่แข็งแกร่ง | ใช้ numpy percentile (มีอยู่ในสคริปต์ที่ปรับปรุงแล้ว) |
| การประมาณต้นทุนโทเค็น | การเปรียบเทียบทางเศรษฐกิจ | ต้นทุนโดยประมาณ = (โทเค็น/วินาที * โทเค็นเฉลี่ยต่อคำขอ) * การประมาณพลังงาน |
| การข้ามโมเดลที่ล้มเหลวอัตโนมัติ | ความยืดหยุ่นในการรันแบบแบทช์ | ห่อการวัดผลแต่ละรายการใน try/except และทำเครื่องหมายสถานะ |

#### ตัวอย่างการส่งออก Markdown ขั้นต่ำ

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### ตัวอย่างชุดคำถามแบบกำหนดค่า

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

วนลูปรายการแบบคงที่แทนคำถามแบบสุ่มเพื่อให้ได้เมตริกที่เปรียบเทียบได้ในแต่ละ commit

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->