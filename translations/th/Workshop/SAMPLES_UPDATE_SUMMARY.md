<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:02:18+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "th"
}
-->
# ตัวอย่างการอบรม - สรุปการอัปเดต Foundry Local SDK

## ภาพรวม

ตัวอย่าง Python ทั้งหมดในไดเรกทอรี `Workshop/samples` ได้รับการอัปเดตให้สอดคล้องกับแนวปฏิบัติที่ดีที่สุดของ Foundry Local SDK และเพื่อให้เกิดความสอดคล้องกันในเวิร์กช็อป

**วันที่**: 8 ตุลาคม 2025  
**ขอบเขต**: ไฟล์ Python 9 ไฟล์ใน 6 เซสชันของเวิร์กช็อป  
**จุดมุ่งเน้นหลัก**: การจัดการข้อผิดพลาด, เอกสารประกอบ, รูปแบบ SDK, ประสบการณ์ผู้ใช้

---

## ไฟล์ที่อัปเดต

### เซสชัน 01: เริ่มต้นใช้งาน
- ✅ `chat_bootstrap.py` - ตัวอย่างการแชทและการสตรีมพื้นฐาน

### เซสชัน 02: โซลูชัน RAG
- ✅ `rag_pipeline.py` - การใช้งาน RAG ด้วย embeddings
- ✅ `rag_eval_ragas.py` - การประเมิน RAG ด้วยเมตริก RAGAS

### เซสชัน 03: โมเดลโอเพ่นซอร์ส
- ✅ `benchmark_oss_models.py` - การเปรียบเทียบประสิทธิภาพหลายโมเดล

### เซสชัน 04: โมเดลล้ำสมัย
- ✅ `model_compare.py` - การเปรียบเทียบ SLM กับ LLM

### เซสชัน 05: เอเจนต์ที่ขับเคลื่อนด้วย AI
- ✅ `agents_orchestrator.py` - การประสานงานหลายเอเจนต์

### เซสชัน 06: โมเดลเป็นเครื่องมือ
- ✅ `models_router.py` - การกำหนดเส้นทางโมเดลตามเจตนา
- ✅ `models_pipeline.py` - ท่อส่งที่มีการกำหนดเส้นทางหลายขั้นตอน

### โครงสร้างพื้นฐานที่สนับสนุน
- ✅ `workshop_utils.py` - ปฏิบัติตามแนวปฏิบัติที่ดีที่สุดอยู่แล้ว (ไม่มีการเปลี่ยนแปลง)

---

## การปรับปรุงที่สำคัญ

### 1. การจัดการข้อผิดพลาดที่ดีขึ้น

**ก่อน:**
```python
manager, client, model_id = get_client(alias)
```

**หลัง:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**ประโยชน์:**
- การจัดการข้อผิดพลาดอย่างราบรื่นพร้อมข้อความข้อผิดพลาดที่ชัดเจน
- คำแนะนำการแก้ไขปัญหาที่สามารถนำไปปฏิบัติได้
- รหัสออกที่เหมาะสมสำหรับการเขียนสคริปต์

### 2. การจัดการการนำเข้าโมดูลที่ดีขึ้น

**ก่อน:**
```python
from sentence_transformers import SentenceTransformer
```

**หลัง:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**ประโยชน์:**
- คำแนะนำที่ชัดเจนเมื่อไม่มี dependencies
- ป้องกันข้อผิดพลาดการนำเข้าที่ไม่ชัดเจน
- คำแนะนำการติดตั้งที่เป็นมิตรต่อผู้ใช้

### 3. เอกสารประกอบที่ครอบคลุม

**เพิ่มในตัวอย่างทั้งหมด:**
- เอกสารประกอบตัวแปรสภาพแวดล้อมใน docstrings
- ลิงก์อ้างอิง SDK
- ตัวอย่างการใช้งาน
- เอกสารประกอบฟังก์ชัน/พารามิเตอร์อย่างละเอียด
- Type hints เพื่อการสนับสนุน IDE ที่ดีขึ้น

**ตัวอย่าง:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. ข้อเสนอแนะผู้ใช้ที่ดีขึ้น

**เพิ่มการล็อกข้อมูลที่ให้ข้อมูล:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**ตัวบ่งชี้ความคืบหน้า:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**ผลลัพธ์ที่มีโครงสร้าง:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. การเปรียบเทียบประสิทธิภาพที่แข็งแกร่ง

**การปรับปรุงเซสชัน 03:**
- การจัดการข้อผิดพลาดต่อโมเดล (ดำเนินการต่อเมื่อเกิดข้อผิดพลาด)
- รายงานความคืบหน้าอย่างละเอียด
- การดำเนินการรอบ warmup อย่างเหมาะสม
- รองรับการวัด latency ของ token แรก
- การแยกขั้นตอนที่ชัดเจน

### 6. Type Hints ที่สอดคล้องกัน

**เพิ่มทั่วทั้งตัวอย่าง:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**ประโยชน์:**
- การเติมข้อความอัตโนมัติใน IDE ที่ดีขึ้น
- การตรวจจับข้อผิดพลาดล่วงหน้า
- โค้ดที่อธิบายตัวเองได้

### 7. การกำหนดเส้นทางโมเดลที่ดีขึ้น

**การปรับปรุงเซสชัน 06:**
- เอกสารประกอบการตรวจจับเจตนาอย่างครอบคลุม
- คำอธิบายอัลกอริทึมการเลือกโมเดล
- บันทึกการกำหนดเส้นทางอย่างละเอียด
- การจัดรูปแบบผลลัพธ์การทดสอบ
- การกู้คืนข้อผิดพลาดในการทดสอบแบบแบตช์

### 8. การประสานงานหลายเอเจนต์

**การปรับปรุงเซสชัน 05:**
- รายงานความคืบหน้าตามขั้นตอน
- การจัดการข้อผิดพลาดต่อเอเจนต์
- โครงสร้างท่อส่งที่ชัดเจน
- เอกสารประกอบการจัดการหน่วยความจำที่ดีขึ้น

---

## รายการตรวจสอบการทดสอบ

### ข้อกำหนดเบื้องต้น
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### ทดสอบตัวอย่างแต่ละตัว

#### เซสชัน 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### เซสชัน 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### เซสชัน 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### เซสชัน 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### เซสชัน 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### เซสชัน 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## อ้างอิงตัวแปรสภาพแวดล้อม

### ทั่วไป (ตัวอย่างทั้งหมด)
| ตัวแปร | คำอธิบาย | ค่าเริ่มต้น |
|--------|-----------|--------------|
| `FOUNDRY_LOCAL_ALIAS` | ชื่อโมเดลที่จะใช้ | แตกต่างกันตามตัวอย่าง |
| `FOUNDRY_LOCAL_ENDPOINT` | บริการ endpoint ที่กำหนดเอง | ตรวจจับอัตโนมัติ |
| `SHOW_USAGE` | แสดงการใช้งาน token | `0` |
| `RETRY_ON_FAIL` | เปิดใช้งานการลองใหม่ | `1` |
| `RETRY_BACKOFF` | ความล่าช้าในการลองใหม่ครั้งแรก | `1.0` |

### เฉพาะตัวอย่าง
| ตัวแปร | ใช้โดย | คำอธิบาย |
|--------|--------|-----------|
| `EMBED_MODEL` | เซสชัน 02 | ชื่อโมเดล embedding |
| `RAG_QUESTION` | เซสชัน 02 | คำถามทดสอบสำหรับ RAG |
| `BENCH_MODELS` | เซสชัน 03 | โมเดลที่ต้องการเปรียบเทียบ (คั่นด้วยเครื่องหมายจุลภาค) |
| `BENCH_ROUNDS` | เซสชัน 03 | จำนวนรอบการเปรียบเทียบ |
| `BENCH_PROMPT` | เซสชัน 03 | คำสั่งทดสอบสำหรับการเปรียบเทียบ |
| `BENCH_STREAM` | เซสชัน 03 | วัด latency ของ token แรก |
| `SLM_ALIAS` | เซสชัน 04 | โมเดลภาษาเล็ก |
| `LLM_ALIAS` | เซสชัน 04 | โมเดลภาษาขนาดใหญ่ |
| `COMPARE_PROMPT` | เซสชัน 04 | คำสั่งทดสอบการเปรียบเทียบ |
| `AGENT_MODEL_PRIMARY` | เซสชัน 05 | โมเดลเอเจนต์หลัก |
| `AGENT_MODEL_EDITOR` | เซสชัน 05 | โมเดลเอเจนต์บรรณาธิการ |
| `AGENT_QUESTION` | เซสชัน 05 | คำถามทดสอบสำหรับเอเจนต์ |
| `PIPELINE_TASK` | เซสชัน 06 | งานสำหรับท่อส่ง |

---

## การเปลี่ยนแปลงที่ส่งผลกระทบ

**ไม่มี** - การเปลี่ยนแปลงทั้งหมดสามารถใช้งานร่วมกับเวอร์ชันก่อนหน้าได้

สคริปต์ที่มีอยู่จะยังคงทำงานต่อไป คุณสมบัติใหม่มีดังนี้:
- ตัวแปรสภาพแวดล้อมที่เป็นทางเลือก
- ข้อความข้อผิดพลาดที่ปรับปรุงแล้ว (ไม่ทำให้ฟังก์ชันการทำงานเสียหาย)
- การล็อกข้อมูลเพิ่มเติม (สามารถปิดได้)
- Type hints ที่ดีขึ้น (ไม่มีผลกระทบต่อการทำงาน)

---

## แนวปฏิบัติที่ดีที่สุดที่นำมาใช้

### 1. ใช้ Workshop Utils เสมอ
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. รูปแบบการจัดการข้อผิดพลาดที่เหมาะสม
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. การล็อกข้อมูลที่ให้ข้อมูล
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Type Hints
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstrings ที่ครอบคลุม
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. รองรับตัวแปรสภาพแวดล้อม
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. การลดผลกระทบอย่างราบรื่น
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## ปัญหาทั่วไปและวิธีแก้ไข

### ปัญหา: ข้อผิดพลาดการนำเข้า
**วิธีแก้ไข:** ติดตั้ง dependencies ที่ขาดหายไป
```bash
pip install sentence-transformers ragas datasets numpy
```

### ปัญหา: ข้อผิดพลาดการเชื่อมต่อ
**วิธีแก้ไข:** ตรวจสอบให้แน่ใจว่า Foundry Local กำลังทำงานอยู่
```bash
foundry service status
foundry model run phi-4-mini
```

### ปัญหา: ไม่พบโมเดล
**วิธีแก้ไข:** ตรวจสอบโมเดลที่มีอยู่
```bash
foundry model ls
foundry model download <alias>
```

### ปัญหา: ประสิทธิภาพช้า
**วิธีแก้ไข:** ใช้โมเดลที่เล็กลงหรือปรับพารามิเตอร์
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## ขั้นตอนถัดไป

### 1. ทดสอบตัวอย่างทั้งหมด
ดำเนินการตามรายการตรวจสอบการทดสอบด้านบนเพื่อยืนยันว่าตัวอย่างทั้งหมดทำงานได้อย่างถูกต้อง

### 2. อัปเดตเอกสารประกอบ
- อัปเดตไฟล์ markdown ของเซสชันด้วยตัวอย่างใหม่
- เพิ่มส่วนการแก้ไขปัญหาใน README หลัก
- สร้างคู่มืออ้างอิงด่วน

### 3. สร้างการทดสอบการรวม
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. เพิ่มการเปรียบเทียบประสิทธิภาพ
ติดตามการปรับปรุงประสิทธิภาพจากการปรับปรุงการจัดการข้อผิดพลาด

### 5. ข้อเสนอแนะจากผู้ใช้
รวบรวมข้อเสนอแนะจากผู้เข้าร่วมเวิร์กช็อปเกี่ยวกับ:
- ความชัดเจนของข้อความข้อผิดพลาด
- ความครบถ้วนของเอกสารประกอบ
- ความง่ายในการใช้งาน

---

## แหล่งข้อมูล

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **คู่มืออ้างอิงด่วน**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **บันทึกการย้ายข้อมูล**: `Workshop/SDK_MIGRATION_NOTES.md`
- **ที่เก็บหลัก**: https://github.com/microsoft/Foundry-Local

---

## การบำรุงรักษา

### การเพิ่มตัวอย่างใหม่
ปฏิบัติตามรูปแบบเหล่านี้เมื่อสร้างตัวอย่างใหม่:

1. ใช้ `workshop_utils` สำหรับการจัดการ client
2. เพิ่มการจัดการข้อผิดพลาดอย่างครอบคลุม
3. รวมการรองรับตัวแปรสภาพแวดล้อม
4. เพิ่ม type hints และ docstrings
5. ให้การล็อกข้อมูลที่ให้ข้อมูล
6. รวมตัวอย่างการใช้งานใน docstring
7. ลิงก์ไปยังเอกสาร SDK

### การตรวจสอบการอัปเดต
เมื่อตรวจสอบการอัปเดตตัวอย่าง ให้ตรวจสอบ:
- [ ] การจัดการข้อผิดพลาดในทุกการดำเนินการ I/O
- [ ] Type hints ในฟังก์ชันสาธารณะทั้งหมด
- [ ] Docstrings ที่ครอบคลุม
- [ ] เอกสารประกอบตัวแปรสภาพแวดล้อม
- [ ] ข้อเสนอแนะผู้ใช้ที่ให้ข้อมูล
- [ ] ลิงก์อ้างอิง SDK
- [ ] สไตล์โค้ดที่สอดคล้องกัน

---

**สรุป**: ตัวอย่าง Python ในเวิร์กช็อปทั้งหมดตอนนี้ปฏิบัติตามแนวปฏิบัติที่ดีที่สุดของ Foundry Local SDK พร้อมการจัดการข้อผิดพลาดที่ดีขึ้น เอกสารประกอบที่ครอบคลุม และประสบการณ์ผู้ใช้ที่ดีขึ้น ไม่มีการเปลี่ยนแปลงที่ส่งผลกระทบ - ฟังก์ชันการทำงานที่มีอยู่ยังคงถูกเก็บรักษาและปรับปรุงให้ดีขึ้น

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้