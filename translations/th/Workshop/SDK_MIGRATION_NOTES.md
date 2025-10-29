<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:02:40+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "th"
}
-->
# หมายเหตุการย้าย SDK Local ของ Foundry

## ภาพรวม

ไฟล์ Python ทั้งหมดในโฟลเดอร์ Workshop ได้รับการอัปเดตให้สอดคล้องกับรูปแบบล่าสุดจาก [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) อย่างเป็นทางการ

## สรุปการเปลี่ยนแปลง

### โครงสร้างพื้นฐานหลัก (`workshop_utils.py`)

#### ฟีเจอร์ที่ปรับปรุง:
- **รองรับการแทนที่ Endpoint**: เพิ่มการรองรับตัวแปรสภาพแวดล้อม `FOUNDRY_LOCAL_ENDPOINT`
- **การจัดการข้อผิดพลาดที่ดีขึ้น**: ปรับปรุงการจัดการข้อยกเว้นพร้อมข้อความข้อผิดพลาดที่ละเอียดขึ้น
- **การแคชที่ปรับปรุง**: คีย์แคชตอนนี้รวม Endpoint สำหรับสถานการณ์ที่มีหลาย Endpoint
- **Exponential Backoff**: ลอจิกการลองใหม่ใช้ Exponential Backoff เพื่อความน่าเชื่อถือที่ดีขึ้น
- **Type Annotations**: เพิ่มคำแนะนำประเภทที่ครอบคลุมเพื่อการสนับสนุน IDE ที่ดีขึ้น

#### ความสามารถใหม่:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### ตัวอย่างแอปพลิเคชัน

#### Session 01: Chat Bootstrap (`chat_bootstrap.py`)
- อัปเดตรุ่นเริ่มต้นจาก `phi-3.5-mini` เป็น `phi-4-mini`
- เพิ่มการรองรับการแทนที่ Endpoint
- ปรับปรุงเอกสารด้วยการอ้างอิง SDK

#### Session 02: RAG Pipeline (`rag_pipeline.py`)
- อัปเดตให้ใช้ `phi-4-mini` เป็นค่าเริ่มต้น
- เพิ่มการรองรับการแทนที่ Endpoint
- ปรับปรุงเอกสารด้วยรายละเอียดตัวแปรสภาพแวดล้อม

#### Session 02: RAG Evaluation (`rag_eval_ragas.py`)
- อัปเดตรุ่นเริ่มต้น
- เพิ่มการตั้งค่า Endpoint
- ปรับปรุงการจัดการข้อผิดพลาด

#### Session 03: Benchmarking (`benchmark_oss_models.py`)
- อัปเดตรายการรุ่นเริ่มต้นเพื่อรวม `phi-4-mini`
- เพิ่มเอกสารตัวแปรสภาพแวดล้อมที่ครอบคลุม
- ปรับปรุงเอกสารฟังก์ชัน
- เพิ่มการรองรับการแทนที่ Endpoint ทั่วทั้งระบบ

#### Session 04: Model Comparison (`model_compare.py`)
- อัปเดต LLM เริ่มต้นจาก `gpt-oss-20b` เป็น `qwen2.5-7b`
- เพิ่มการตั้งค่า Endpoint
- ปรับปรุงเอกสาร

#### Session 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- เพิ่ม Type Hints (เปลี่ยน `str | None` เป็น `Optional[str]`)
- ปรับปรุงเอกสารคลาส Agent
- เพิ่มการรองรับการแทนที่ Endpoint
- ปรับปรุงรูปแบบการเริ่มต้น

#### Session 06: Model Router (`models_router.py`)
- เพิ่มการตั้งค่า Endpoint
- ปรับปรุงเอกสารการตรวจจับ Intent
- ปรับปรุงเอกสารลอจิกการกำหนดเส้นทาง

#### Session 06: Pipeline (`models_pipeline.py`)
- เพิ่มเอกสารฟังก์ชันที่ครอบคลุม
- ปรับปรุงเอกสารทีละขั้นตอน
- ปรับปรุงการจัดการข้อผิดพลาด

### สคริปต์

#### Benchmark Export (`export_benchmark_markdown.py`)
- เพิ่มการรองรับการแทนที่ Endpoint
- อัปเดตรุ่นเริ่มต้น
- ปรับปรุงเอกสารฟังก์ชัน
- ปรับปรุงการจัดการข้อผิดพลาด

#### CLI Linter (`lint_markdown_cli.py`)
- เพิ่มลิงก์อ้างอิง SDK
- ปรับปรุงเอกสารการใช้งาน

### การทดสอบ

#### Smoke Tests (`smoke.py`)
- เพิ่มการรองรับการแทนที่ Endpoint
- ปรับปรุงเอกสาร
- ปรับปรุงเอกสารกรณีทดสอบ
- รายงานข้อผิดพลาดที่ดีขึ้น

## ตัวแปรสภาพแวดล้อม

ตัวอย่างทั้งหมดตอนนี้รองรับตัวแปรสภาพแวดล้อมเหล่านี้:

### การตั้งค่าหลัก
- `FOUNDRY_LOCAL_ALIAS` - Alias รุ่นที่จะใช้ (ค่าเริ่มต้นแตกต่างกันไปตามตัวอย่าง)
- `FOUNDRY_LOCAL_ENDPOINT` - แทนที่ Endpoint บริการ (ไม่บังคับ)
- `SHOW_USAGE` - แสดงสถิติการใช้งานโทเค็น (ค่าเริ่มต้น: "0")
- `RETRY_ON_FAIL` - เปิดใช้งานลอจิกการลองใหม่ (ค่าเริ่มต้น: "1")
- `RETRY_BACKOFF` - ความล่าช้าเริ่มต้นของการลองใหม่ในวินาที (ค่าเริ่มต้น: "1.0")

### เฉพาะตัวอย่าง
- `EMBED_MODEL` - รุ่น Embedding สำหรับตัวอย่าง RAG
- `BENCH_MODELS` - รุ่นที่คั่นด้วยเครื่องหมายจุลภาคสำหรับ Benchmarking
- `BENCH_ROUNDS` - จำนวนรอบ Benchmark
- `BENCH_PROMPT` - Prompt ทดสอบสำหรับ Benchmark
- `BENCH_STREAM` - วัดความล่าช้าของโทเค็นแรก
- `RAG_QUESTION` - คำถามทดสอบสำหรับตัวอย่าง RAG
- `AGENT_MODEL_PRIMARY` - รุ่น Agent หลัก
- `AGENT_MODEL_EDITOR` - รุ่น Agent Editor
- `SLM_ALIAS` - Alias รุ่นภาษาเล็ก
- `LLM_ALIAS` - Alias รุ่นภาษาขนาดใหญ่

## แนวปฏิบัติที่ดีที่สุดของ SDK ที่นำมาใช้

### 1. การเริ่มต้น Client อย่างเหมาะสม
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. การดึงข้อมูลรุ่น
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. การจัดการข้อผิดพลาด
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. ลอจิกการลองใหม่ด้วย Exponential Backoff
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. การรองรับการสตรีม
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## คู่มือการย้ายสำหรับตัวอย่างที่กำหนดเอง

หากคุณกำลังสร้างตัวอย่างใหม่หรืออัปเดตตัวอย่างที่มีอยู่:

1. **ใช้ตัวช่วย `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **รองรับการแทนที่ Endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **เพิ่มเอกสารที่ครอบคลุม**:
   - ตัวแปรสภาพแวดล้อมใน docstring
   - ลิงก์อ้างอิง SDK
   - ตัวอย่างการใช้งาน

4. **ใช้ Type Hints**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **นำการจัดการข้อผิดพลาดที่เหมาะสมมาใช้**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## การทดสอบ

ตัวอย่างทั้งหมดสามารถทดสอบได้ด้วย:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## การอ้างอิงเอกสาร SDK

- **Repository หลัก**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **เอกสาร API**: ตรวจสอบ Repository SDK สำหรับเอกสาร API ล่าสุด

## การเปลี่ยนแปลงที่ทำให้เกิดปัญหา

### ไม่มีที่คาดไว้
การเปลี่ยนแปลงทั้งหมดเข้ากันได้กับเวอร์ชันก่อนหน้า การอัปเดตส่วนใหญ่:
- เพิ่มฟีเจอร์ใหม่ที่ไม่บังคับ (การแทนที่ Endpoint)
- ปรับปรุงการจัดการข้อผิดพลาด
- ปรับปรุงเอกสาร
- อัปเดตชื่อรุ่นเริ่มต้นให้เป็นคำแนะนำปัจจุบัน

### การปรับปรุงเพิ่มเติมที่เป็นทางเลือก
คุณอาจต้องการอัปเดตโค้ดของคุณเพื่อใช้:
- `FOUNDRY_LOCAL_ENDPOINT` สำหรับการควบคุม Endpoint อย่างชัดเจน
- `SHOW_USAGE=1` เพื่อดูการใช้งานโทเค็น
- รุ่นเริ่มต้นที่อัปเดต (`phi-4-mini` แทน `phi-3.5-mini`)

## ปัญหาทั่วไปและวิธีแก้ไข

### ปัญหา: "การเริ่มต้น Client ล้มเหลว"
**วิธีแก้ไข**: ตรวจสอบให้แน่ใจว่า Foundry Local service กำลังทำงาน:
```bash
foundry service start
foundry model run phi-4-mini
```

### ปัญหา: "ไม่พบรุ่น"
**วิธีแก้ไข**: ตรวจสอบรุ่นที่มีอยู่:
```bash
foundry model list
```

### ปัญหา: ข้อผิดพลาดการเชื่อมต่อ Endpoint
**วิธีแก้ไข**: ตรวจสอบ Endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## ขั้นตอนถัดไป

1. **อัปเดตตัวอย่าง Module08**: ใช้รูปแบบที่คล้ายกันกับ Module08/samples
2. **เพิ่มการทดสอบการรวม**: สร้างชุดการทดสอบที่ครอบคลุม
3. **การวัดประสิทธิภาพ**: เปรียบเทียบประสิทธิภาพก่อน/หลัง
4. **อัปเดตเอกสาร**: อัปเดต README หลักด้วยรูปแบบใหม่

## แนวทางการมีส่วนร่วม

เมื่อเพิ่มตัวอย่างใหม่:
1. ใช้ `workshop_utils.py` เพื่อความสอดคล้อง
2. ปฏิบัติตามรูปแบบในตัวอย่างที่มีอยู่
3. เพิ่ม docstring ที่ครอบคลุม
4. รวมลิงก์อ้างอิง SDK
5. รองรับการแทนที่ Endpoint
6. เพิ่ม Type Hints ที่เหมาะสม
7. รวมตัวอย่างการใช้งานใน docstring

## ความเข้ากันได้ของเวอร์ชัน

การอัปเดตเหล่านี้เข้ากันได้กับ:
- `foundry-local-sdk` (ล่าสุด)
- `openai>=1.30.0`
- Python 3.8+

---

**อัปเดตล่าสุด**: 2025-01-08  
**ผู้ดูแล**: ทีม EdgeAI Workshop  
**เวอร์ชัน SDK**: Foundry Local SDK (ล่าสุด 0.7.117+67073234e7)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้