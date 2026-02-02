# ตัวอย่างการทำ Workshop - บัตรอ้างอิงด่วน

**อัปเดตล่าสุด**: 8 ตุลาคม 2025

---

## 🚀 เริ่มต้นอย่างรวดเร็ว

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 ภาพรวมตัวอย่าง

| เซสชัน | ตัวอย่าง | วัตถุประสงค์ | เวลา |
|--------|----------|--------------|------|
| 01 | `chat_bootstrap.py` | แชทพื้นฐาน + สตรีมมิ่ง | ~30 วินาที |
| 02 | `rag_pipeline.py` | RAG พร้อม embeddings | ~45 วินาที |
| 02 | `rag_eval_ragas.py` | การประเมิน RAG | ~60 วินาที |
| 03 | `benchmark_oss_models.py` | การวัดประสิทธิภาพโมเดล | ~2 นาที |
| 04 | `model_compare.py` | SLM เทียบกับ LLM | ~45 วินาที |
| 05 | `agents_orchestrator.py` | ระบบหลายเอเจนต์ | ~60 วินาที |
| 06 | `models_router.py` | การจัดการเจตนา | ~45 วินาที |
| 06 | `models_pipeline.py` | การทำงานแบบหลายขั้นตอน | ~60 วินาที |

---

## 🛠️ ตัวแปรสภาพแวดล้อม

### จำเป็น
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### เฉพาะเซสชัน
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ การตรวจสอบและการทดสอบ

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 การแก้ไขปัญหา

### ข้อผิดพลาดการเชื่อมต่อ
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### ข้อผิดพลาดการนำเข้า
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### ไม่พบโมเดล
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### ประสิทธิภาพช้า
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 รูปแบบทั่วไป

### แชทพื้นฐาน
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### รับ Client
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### การจัดการข้อผิดพลาด
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### สตรีมมิ่ง
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 การเลือกโมเดล

| โมเดล | ขนาด | เหมาะสำหรับ | ความเร็ว |
|-------|------|-------------|----------|
| `qwen2.5-0.5b` | 0.5B | การจัดประเภทที่รวดเร็ว | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | การสร้างโค้ดอย่างรวดเร็ว | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | การเขียนเชิงสร้างสรรค์ | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | โค้ด, การปรับปรุงโค้ด | ⚡⚡ |
| `phi-4-mini` | 4B | การใช้งานทั่วไป, สรุป | ⚡⚡ |
| `qwen2.5-7b` | 7B | การวิเคราะห์ที่ซับซ้อน | ⚡ |

---

## 🔗 แหล่งข้อมูล

- **เอกสาร SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **อ้างอิงด่วน**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 เคล็ดลับ

1. **แคช Client**: `workshop_utils` จะช่วยแคชให้คุณ
2. **ใช้โมเดลขนาดเล็ก**: เริ่มต้นด้วย `qwen2.5-0.5b` สำหรับการทดสอบ
3. **เปิดการติดตามการใช้งาน**: ตั้งค่า `SHOW_USAGE=1` เพื่อดูการใช้โทเค็น
4. **การประมวลผลแบบแบทช์**: ประมวลผลคำถามหลายคำถามต่อเนื่องกัน
5. **ลด max_tokens**: ลดเวลาในการตอบกลับสำหรับคำตอบที่รวดเร็ว

---

## 🎯 เวิร์กโฟลว์ตัวอย่าง

### ทดสอบทุกอย่าง
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### วัดประสิทธิภาพโมเดล
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG Pipeline
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### ระบบหลายเอเจนต์
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**ความช่วยเหลือด่วน**: รันตัวอย่างใดๆ ด้วย `--help` จากไดเรกทอรี `samples` หรือดู docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**ตัวอย่างทั้งหมดอัปเดตในเดือนตุลาคม 2025 พร้อมแนวปฏิบัติที่ดีที่สุดของ Foundry Local SDK** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->