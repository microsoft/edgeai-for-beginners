<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T22:02:55+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "th"
}
-->
# สคริปต์สำหรับ Workshop

ไดเรกทอรีนี้ประกอบด้วยสคริปต์อัตโนมัติและสนับสนุนที่ใช้เพื่อรักษาคุณภาพและความสม่ำเสมอในเนื้อหาของ Workshop

## เนื้อหา

| ไฟล์ | วัตถุประสงค์ |
|------|-------------|
| `lint_markdown_cli.py` | ตรวจสอบโค้ด Markdown เพื่อบล็อกรูปแบบคำสั่ง Foundry Local CLI ที่เลิกใช้แล้ว |
| `export_benchmark_markdown.py` | รันการวัดประสิทธิภาพหลายโมเดลและสร้างรายงานในรูปแบบ Markdown + JSON |

## 1. ตัวตรวจสอบรูปแบบ Markdown CLI

`lint_markdown_cli.py` สแกนไฟล์ `.md` ที่ไม่ใช่การแปลทั้งหมดเพื่อหาการใช้รูปแบบคำสั่ง Foundry Local CLI ที่ไม่อนุญาต **ภายในบล็อกโค้ดที่มีขอบเขต** (``` ... ```) ข้อความเชิงข้อมูลยังสามารถกล่าวถึงคำสั่งที่เลิกใช้แล้วเพื่อบริบททางประวัติศาสตร์ได้

### รูปแบบที่เลิกใช้ (บล็อกภายในบล็อกโค้ด)

ตัวตรวจสอบจะบล็อกรูปแบบ CLI ที่เลิกใช้แล้ว ควรใช้ทางเลือกที่ทันสมัยแทน

### การเปลี่ยนแปลงที่จำเป็น
| รูปแบบที่เลิกใช้ | ใช้แทนที่ |
|------------------|-----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | สคริปต์วัดประสิทธิภาพ + เครื่องมือระบบ (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### รหัสออก
| รหัส | ความหมาย |
|------|----------|
| 0 | ไม่พบการละเมิด |
| 1 | พบรูปแบบที่เลิกใช้แล้วหนึ่งรายการหรือมากกว่า |

### การรันในเครื่อง
จากรากของ repository (แนะนำ):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### ฮุก Pre-Commit (ตัวเลือก)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
บล็อกการ commit ที่แนะนำรูปแบบที่เลิกใช้แล้ว

### การรวม CI
เวิร์กโฟลว์ GitHub Action (`.github/workflows/markdown-cli-lint.yml`) จะรันตัวตรวจสอบทุกครั้งที่มีการ push และ pull request ไปยังสาขา `main` และ `Reactor` งานที่ล้มเหลวต้องแก้ไขก่อนการรวม

### การเพิ่มรูปแบบที่เลิกใช้ใหม่
1. เปิด `lint_markdown_cli.py`
2. เพิ่ม tuple `(regex, suggestion)` ไปยังรายการ `DEPRECATED` ใช้ raw string และรวม `\b` ขอบเขตคำที่เหมาะสม
3. รันตัวตรวจสอบในเครื่องเพื่อยืนยันการตรวจจับ
4. Commit และ push; CI จะบังคับใช้กฎใหม่

ตัวอย่างการเพิ่ม:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### การอนุญาตการกล่าวถึงเพื่ออธิบาย
เนื่องจากบล็อกโค้ดที่มีขอบเขตเท่านั้นที่ถูกบังคับใช้ คุณสามารถอธิบายคำสั่งที่เลิกใช้แล้วในข้อความบรรยายได้อย่างปลอดภัย หากคุณ *จำเป็น* ต้องแสดงคำสั่งเหล่านี้ในบล็อก ให้เพิ่มบล็อกที่ไม่มี backticks สามตัว (เช่น การเยื้องหรือการอ้างอิง) หรือเขียนใหม่ในรูปแบบเทียม

### การข้ามไฟล์เฉพาะ (ขั้นสูง)
หากจำเป็น ให้ห่อหุ้มตัวอย่างที่เป็นมรดกในไฟล์แยกนอก repository หรือเปลี่ยนชื่อด้วยนามสกุลที่แตกต่างกันขณะร่าง การข้ามโดยเจตนาสำหรับสำเนาที่แปลจะเป็นไปโดยอัตโนมัติ (เส้นทางที่มี `translations`)

### การแก้ไขปัญหา
| ปัญหา | สาเหตุ | วิธีแก้ไข |
|-------|--------|----------|
| ตัวตรวจสอบระบุบรรทัดที่คุณอัปเดต | Regex กว้างเกินไป | จำกัดรูปแบบด้วยขอบเขตคำเพิ่มเติม (`\b`) หรือจุดยึด |
| CI ล้มเหลวแต่ในเครื่องผ่าน | เวอร์ชัน Python ต่างกันหรือมีการเปลี่ยนแปลงที่ไม่ได้ commit | รันใหม่ในเครื่อง ตรวจสอบให้แน่ใจว่า tree ทำงานสะอาด ตรวจสอบเวอร์ชัน Python ของ workflow (3.11) |
| ต้องการข้ามชั่วคราว | การแก้ไขด่วนฉุกเฉิน | ใช้การแก้ไขทันทีหลังจากนั้น พิจารณาใช้สาขาชั่วคราวและ PR ติดตามผล (หลีกเลี่ยงการเพิ่มสวิตช์ข้าม) |

### เหตุผล
การรักษาเอกสารให้สอดคล้องกับพื้นผิว CLI ที่ *เสถียร* ในปัจจุบันช่วยลดความยุ่งยากใน Workshop หลีกเลี่ยงความสับสนของผู้เรียน และรวมการวัดประสิทธิภาพผ่านสคริปต์ Python ที่ดูแลรักษาแทนคำสั่งย่อย CLI ที่เปลี่ยนแปลง

---
ดูแลรักษาเป็นส่วนหนึ่งของเครื่องมือคุณภาพ Workshop สำหรับการปรับปรุง (เช่น การแก้ไขอัตโนมัติหรือการสร้างรายงาน HTML) เปิด issue หรือส่ง PR

## 2. สคริปต์ตรวจสอบตัวอย่าง

`validate_samples.py` ตรวจสอบไฟล์ตัวอย่าง Python ทั้งหมดเพื่อความถูกต้องของไวยากรณ์ การนำเข้า และการปฏิบัติตามแนวทางปฏิบัติที่ดีที่สุด

### การใช้งาน
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### สิ่งที่ตรวจสอบ
- ✅ ความถูกต้องของไวยากรณ์ Python
- ✅ การนำเข้าที่จำเป็น
- ✅ การจัดการข้อผิดพลาด (โหมด verbose)
- ✅ การใช้ type hints (โหมด verbose)
- ✅ docstrings ของฟังก์ชัน (โหมด verbose)
- ✅ ลิงก์อ้างอิง SDK (โหมด verbose)

### ตัวแปรสภาพแวดล้อม
- `SKIP_IMPORT_CHECK=1` - ข้ามการตรวจสอบการนำเข้า
- `SKIP_SYNTAX_CHECK=1` - ข้ามการตรวจสอบไวยากรณ์

### รหัสออก
- `0` - ตัวอย่างทั้งหมดผ่านการตรวจสอบ
- `1` - ตัวอย่างหนึ่งหรือมากกว่าล้มเหลว

## 3. ตัวรันทดสอบตัวอย่าง

`test_samples.py` รันการทดสอบเบื้องต้นในตัวอย่างทั้งหมดเพื่อยืนยันว่ารันได้โดยไม่มีข้อผิดพลาด

### การใช้งาน
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### ข้อกำหนดเบื้องต้น
- บริการ Foundry Local กำลังทำงาน: `foundry service start`
- โหลดโมเดล: `foundry model run phi-4-mini`
- ติดตั้ง dependencies: `pip install -r requirements.txt`

### สิ่งที่ทดสอบ
- ✅ ตัวอย่างสามารถรันได้โดยไม่มีข้อผิดพลาดขณะรัน
- ✅ สร้างผลลัพธ์ที่จำเป็น
- ✅ การจัดการข้อผิดพลาดที่เหมาะสมเมื่อเกิดข้อผิดพลาด
- ✅ ประสิทธิภาพ (เวลาในการรัน)

### ตัวแปรสภาพแวดล้อม
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - โมเดลที่ใช้สำหรับการทดสอบ
- `TEST_TIMEOUT=30` - เวลารอสูงสุดต่อหนึ่งตัวอย่างในวินาที

### ความล้มเหลวที่คาดไว้
การทดสอบบางอย่างอาจล้มเหลวหากไม่ได้ติดตั้ง dependencies ที่เป็นตัวเลือก (เช่น `ragas`, `sentence-transformers`) ติดตั้งด้วย:
```bash
pip install sentence-transformers ragas datasets
```

### รหัสออก
- `0` - การทดสอบทั้งหมดผ่าน
- `1` - การทดสอบหนึ่งหรือมากกว่าล้มเหลว

## 4. ตัวส่งออก Markdown สำหรับ Benchmark

สคริปต์: `export_benchmark_markdown.py`

สร้างตารางประสิทธิภาพที่สามารถทำซ้ำได้สำหรับชุดโมเดล

### การใช้งาน
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### ผลลัพธ์
| ไฟล์ | คำอธิบาย |
|------|----------|
| `benchmark_report.md` | ตาราง Markdown (ค่าเฉลี่ย, p95, tokens/sec, ตัวเลือก first token) |
| `benchmark_report.json` | อาร์เรย์เมตริกดิบสำหรับการเปรียบเทียบและประวัติ |

### ตัวเลือก
| Flag | คำอธิบาย | ค่าเริ่มต้น |
|------|----------|-------------|
| `--models` | ชื่อโมเดลที่คั่นด้วยเครื่องหมายจุลภาค | (จำเป็น) |
| `--prompt` | Prompt ที่ใช้ในแต่ละรอบ | (จำเป็น) |
| `--rounds` | รอบต่อโมเดล | 3 |
| `--output` | ไฟล์ Markdown ที่ส่งออก | `benchmark_report.md` |
| `--json` | ไฟล์ JSON ที่ส่งออก | `benchmark_report.json` |
| `--fail-on-empty` | ออกไม่เป็นศูนย์หาก benchmark ทั้งหมดล้มเหลว | ปิด |

ตัวแปรสภาพแวดล้อม `BENCH_STREAM=1` เพิ่มการวัดเวลา latency ของ first token

### หมายเหตุ
- ใช้ `workshop_utils` เพื่อการบูตโมเดลและการแคชที่สอดคล้องกัน
- หากรันจากไดเรกทอรีทำงานที่แตกต่างกัน สคริปต์จะพยายาม fallback เส้นทางเพื่อค้นหา `workshop_utils`
- สำหรับการเปรียบเทียบ GPU: รันครั้งหนึ่ง เปิดใช้งานการเร่งความเร็วผ่านการตั้งค่า CLI รันใหม่และเปรียบเทียบ JSON

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้