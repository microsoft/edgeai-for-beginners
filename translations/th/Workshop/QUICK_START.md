# คู่มือเริ่มต้นใช้งาน Workshop

## สิ่งที่ต้องเตรียม

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

**ทดสอบการทำงานของ routing logic** ด้วย intents หลายแบบ (code, summarize, classification)

### Session 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Pipeline หลายขั้นตอนที่ซับซ้อน** รวมถึงการวางแผน การดำเนินการ และการปรับปรุง

## สคริปต์

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

**วัตถุประสงค์**: ตรวจสอบ CLI patterns ที่ล้าสมัยในเอกสาร

## การทดสอบ

### Smoke Tests

```bash
cd Workshop
python -m tests.smoke
```

**การทดสอบ**: ฟังก์ชันพื้นฐานของตัวอย่างสำคัญ

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
| `FOUNDRY_LOCAL_ALIAS` | Varies | Alias ของโมเดลที่ใช้ |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | กำหนด endpoint ของ service |
| `SHOW_USAGE` | `0` | แสดงสถิติการใช้งาน token |
| `RETRY_ON_FAIL` | `1` | เปิดใช้งาน logic การ retry |
| `RETRY_BACKOFF` | `1.0` | ระยะเวลาหน่วงเริ่มต้นสำหรับ retry (วินาที) |

### เฉพาะ Session
| Variable | Default | Description |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | โมเดล embedding |
| `RAG_QUESTION` | ดูตัวอย่าง | คำถามทดสอบ RAG |
| `BENCH_MODELS` | Varies | โมเดลที่คั่นด้วยเครื่องหมายจุลภาค |
| `BENCH_ROUNDS` | `3` | จำนวนรอบการ benchmark |
| `BENCH_PROMPT` | ดูตัวอย่าง | prompt สำหรับ benchmark |
| `BENCH_STREAM` | `0` | วัด latency ของ first-token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | โมเดลหลักของ agent |
| `AGENT_MODEL_EDITOR` | Primary | โมเดล editor ของ agent |
| `SLM_ALIAS` | `phi-4-mini` | โมเดลภาษาแบบเล็ก |
| `LLM_ALIAS` | `qwen2.5-7b` | โมเดลภาษาแบบใหญ่ |
| `COMPARE_PROMPT` | ดูตัวอย่าง | prompt สำหรับการเปรียบเทียบ |

## โมเดลที่แนะนำ

### การพัฒนาและการทดสอบ
- **phi-4-mini** - คุณภาพและความเร็วที่สมดุล
- **qwen2.5-0.5b** - เร็วมากสำหรับการจัดประเภท
- **gemma-2-2b** - คุณภาพดี ความเร็วปานกลาง

### สถานการณ์การใช้งานจริง
- **phi-4-mini** - ใช้งานทั่วไป
- **deepseek-coder-1.3b** - การสร้างโค้ด
- **qwen2.5-7b** - การตอบกลับคุณภาพสูง

## เอกสาร SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## การขอความช่วยเหลือ

1. ตรวจสอบสถานะ service: `foundry service status`  
2. ดู logs: ตรวจสอบ logs ของ Foundry Local service  
3. ดูเอกสาร SDK: https://github.com/microsoft/Foundry-Local  
4. ตรวจสอบโค้ดตัวอย่าง: ตัวอย่างทั้งหมดมี docstrings ที่ละเอียด

## ขั้นตอนถัดไป

1. ทำทุก session ใน workshop ให้ครบตามลำดับ  
2. ทดลองใช้งานโมเดลต่าง ๆ  
3. ปรับเปลี่ยนตัวอย่างให้เหมาะกับการใช้งานของคุณ  

---

**อัปเดตล่าสุด**: 2025-01-08  
**เวอร์ชัน Workshop**: ล่าสุด  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->