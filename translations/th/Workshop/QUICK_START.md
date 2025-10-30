<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd656d9068e1459dae855bd47075f2fb",
  "translation_date": "2025-10-28T21:58:00+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "th"
}
-->
# คู่มือเริ่มต้นใช้งาน Workshop

## ข้อกำหนดเบื้องต้น

### 1. ติดตั้ง Foundry Local

ทำตามคู่มือการติดตั้งอย่างเป็นทางการ:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. ติดตั้ง Python Dependencies

จากไดเรกทอรี Workshop:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## การใช้งานตัวอย่างใน Workshop

### Session 01: Basic Chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Environment Variables:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Session 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Environment Variables:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Session 02: RAG Evaluation (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**หมายเหตุ**: ต้องติดตั้ง dependencies เพิ่มเติมผ่าน `requirements.txt`

### Session 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Environment Variables:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**ผลลัพธ์**: JSON ที่มีข้อมูล latency, throughput และ metrics ของ first-token

### Session 04: Model Comparison

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Environment Variables:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Session 05: Multi-Agent Orchestration

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Environment Variables:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Session 06: Model Router

```bash
cd Workshop/samples
python -m session06.models_router
```

**ทดสอบการทำงานของ routing logic** ด้วยหลาย intents (code, summarize, classification)

### Session 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Pipeline หลายขั้นตอนที่ซับซ้อน** รวมถึงการวางแผน การดำเนินการ และการปรับปรุง

## Scripts

### Export Benchmark Report

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**ผลลัพธ์**: ตาราง Markdown + JSON metrics

### Lint Markdown CLI Patterns

```bash
python lint_markdown_cli.py --verbose
```

**วัตถุประสงค์**: ตรวจสอบ CLI patterns ที่เลิกใช้งานในเอกสาร

## การทดสอบ

### Smoke Tests

```bash
cd Workshop
python -m tests.smoke
```

**การทดสอบ**: การทำงานพื้นฐานของตัวอย่างสำคัญ

## การแก้ไขปัญหา

### Service Not Running

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Module Import Errors

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Connection Errors

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model Not Found

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## อ้างอิง Environment Variable

### การตั้งค่าหลัก
| Variable | Default | Description |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Varies | Model alias ที่ใช้ |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | กำหนด service endpoint |
| `SHOW_USAGE` | `0` | แสดงสถิติการใช้งาน token |
| `RETRY_ON_FAIL` | `1` | เปิดใช้งาน retry logic |
| `RETRY_BACKOFF` | `1.0` | ความล่าช้าเริ่มต้นในการ retry (วินาที) |

### เฉพาะ Session
| Variable | Default | Description |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding model |
| `RAG_QUESTION` | ดูตัวอย่าง | คำถามทดสอบ RAG |
| `BENCH_MODELS` | Varies | รายชื่อ models แบบ comma-separated |
| `BENCH_ROUNDS` | `3` | จำนวนรอบ benchmark |
| `BENCH_PROMPT` | ดูตัวอย่าง | Benchmark prompt |
| `BENCH_STREAM` | `0` | วัด latency ของ first-token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primary agent model |
| `AGENT_MODEL_EDITOR` | Primary | Editor agent model |
| `SLM_ALIAS` | `phi-4-mini` | Small language model |
| `LLM_ALIAS` | `qwen2.5-7b` | Large language model |
| `COMPARE_PROMPT` | ดูตัวอย่าง | Comparison prompt |

## โมเดลที่แนะนำ

### การพัฒนาและการทดสอบ
- **phi-4-mini** - คุณภาพและความเร็วที่สมดุล
- **qwen2.5-0.5b** - เร็วมากสำหรับการจัดหมวดหมู่
- **gemma-2-2b** - คุณภาพดี ความเร็วปานกลาง

### การใช้งานในสถานการณ์จริง
- **phi-4-mini** - ใช้งานทั่วไป
- **deepseek-coder-1.3b** - การสร้างโค้ด
- **qwen2.5-7b** - การตอบกลับคุณภาพสูง

## เอกสาร SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## การขอความช่วยเหลือ

1. ตรวจสอบสถานะบริการ: `foundry service status`  
2. ดู log: ตรวจสอบ log ของ Foundry Local service  
3. ดูเอกสาร SDK: https://github.com/microsoft/Foundry-Local  
4. ตรวจสอบโค้ดตัวอย่าง: ตัวอย่างทั้งหมดมี docstrings ที่ละเอียด

## ขั้นตอนถัดไป

1. ทำทุก session ใน workshop ให้ครบตามลำดับ  
2. ทดลองใช้งานโมเดลต่าง ๆ  
3. ปรับเปลี่ยนตัวอย่างให้เหมาะกับการใช้งานของคุณ  
4. ทบทวน `SDK_MIGRATION_NOTES.md` สำหรับ patterns ขั้นสูง  

---

**อัปเดตล่าสุด**: 2025-01-08  
**เวอร์ชัน Workshop**: ล่าสุด  
**SDK**: Foundry Local Python SDK

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้