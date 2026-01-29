# AGENTS.md

> **คู่มือสำหรับนักพัฒนาในการมีส่วนร่วมกับ EdgeAI สำหรับผู้เริ่มต้น**
> 
> เอกสารนี้ให้ข้อมูลที่ครอบคลุมสำหรับนักพัฒนา, ตัวแทน AI, และผู้มีส่วนร่วมที่ทำงานกับคลังข้อมูลนี้ ครอบคลุมการตั้งค่า, กระบวนการพัฒนา, การทดสอบ, และแนวปฏิบัติที่ดีที่สุด
> 
> **อัปเดตล่าสุด**: 30 ตุลาคม 2025 | **เวอร์ชันเอกสาร**: 3.0

## สารบัญ

- [ภาพรวมโครงการ](../..)
- [โครงสร้างคลังข้อมูล](../..)
- [ข้อกำหนดเบื้องต้น](../..)
- [คำสั่งการตั้งค่า](../..)
- [กระบวนการพัฒนา](../..)
- [คำแนะนำการทดสอบ](../..)
- [แนวทางการเขียนโค้ด](../..)
- [แนวทางการส่ง Pull Request](../..)
- [ระบบการแปล](../..)
- [การผสานรวม Foundry Local](../..)
- [การสร้างและการปรับใช้](../..)
- [ปัญหาทั่วไปและการแก้ไขปัญหา](../..)
- [ทรัพยากรเพิ่มเติม](../..)
- [หมายเหตุเฉพาะโครงการ](../..)
- [การขอความช่วยเหลือ](../..)

## ภาพรวมโครงการ

EdgeAI สำหรับผู้เริ่มต้นเป็นคลังข้อมูลการศึกษาที่ครอบคลุมการพัฒนา Edge AI ด้วย Small Language Models (SLMs) หลักสูตรครอบคลุมพื้นฐาน EdgeAI, การปรับใช้โมเดล, เทคนิคการปรับแต่ง, และการใช้งานที่พร้อมสำหรับการผลิตโดยใช้ Microsoft Foundry Local และเฟรมเวิร์ค AI ต่างๆ

**เทคโนโลยีสำคัญ:**
- Python 3.8+ (ภาษาเริ่มต้นสำหรับตัวอย่าง AI/ML)
- .NET C# (ตัวอย่าง AI/ML)
- JavaScript/Node.js กับ Electron (สำหรับแอปพลิเคชันเดสก์ท็อป)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- เฟรมเวิร์ค AI: LangChain, Semantic Kernel, Chainlit
- การปรับแต่งโมเดล: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**ประเภทคลังข้อมูล:** คลังข้อมูลเนื้อหาการศึกษาที่มี 8 โมดูลและตัวอย่างแอปพลิเคชันที่ครอบคลุม 10 ตัวอย่าง

**สถาปัตยกรรม:** เส้นทางการเรียนรู้แบบหลายโมดูลพร้อมตัวอย่างที่ใช้งานจริงที่แสดงรูปแบบการปรับใช้ Edge AI

## โครงสร้างคลังข้อมูล

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## ข้อกำหนดเบื้องต้น

### เครื่องมือที่จำเป็น

- **Python 3.8+** - สำหรับตัวอย่าง AI/ML และโน้ตบุ๊ก
- **Node.js 16+** - สำหรับแอปพลิเคชันตัวอย่าง Electron
- **Git** - สำหรับการควบคุมเวอร์ชัน
- **Microsoft Foundry Local** - สำหรับการรันโมเดล AI ในเครื่อง

### เครื่องมือที่แนะนำ

- **Visual Studio Code** - พร้อมส่วนขยาย Python, Jupyter, และ Pylance
- **Windows Terminal** - สำหรับประสบการณ์การใช้งานบรรทัดคำสั่งที่ดีกว่า (สำหรับผู้ใช้ Windows)
- **Docker** - สำหรับการพัฒนาแบบคอนเทนเนอร์ (ไม่บังคับ)

### ข้อกำหนดของระบบ

- **RAM**: ขั้นต่ำ 8GB, แนะนำ 16GB+ สำหรับสถานการณ์ที่ใช้หลายโมเดล
- **พื้นที่เก็บข้อมูล**: พื้นที่ว่าง 10GB+ สำหรับโมเดลและการพึ่งพา
- **ระบบปฏิบัติการ**: Windows 10/11, macOS 11+, หรือ Linux (Ubuntu 20.04+)
- **ฮาร์ดแวร์**: CPU ที่รองรับ AVX2; GPU (CUDA, Qualcomm NPU) ไม่บังคับแต่แนะนำ

### ความรู้เบื้องต้น

- ความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรม Python
- ความคุ้นเคยกับอินเทอร์เฟซบรรทัดคำสั่ง
- ความเข้าใจเกี่ยวกับแนวคิด AI/ML (สำหรับการพัฒนาตัวอย่าง)
- กระบวนการ Git และ Pull Request

## คำสั่งการตั้งค่า

### การตั้งค่าคลังข้อมูล

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### การตั้งค่าตัวอย่าง Python (Module08 และตัวอย่าง Workshop)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### การตั้งค่าตัวอย่าง Node.js (ตัวอย่าง 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### การตั้งค่า Foundry Local

Foundry Local จำเป็นสำหรับการรันตัวอย่าง ดาวน์โหลดและติดตั้งจากคลังข้อมูลอย่างเป็นทางการ:

**การติดตั้ง:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: ดาวน์โหลดจาก [หน้าปล่อย](https://github.com/microsoft/Foundry-Local/releases)

**เริ่มต้นใช้งาน:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**หมายเหตุ**: Foundry Local จะเลือกตัวแปรโมเดลที่ดีที่สุดสำหรับฮาร์ดแวร์ของคุณโดยอัตโนมัติ (CUDA GPU, Qualcomm NPU, หรือ CPU)

## กระบวนการพัฒนา

### การพัฒนาเนื้อหา

คลังข้อมูลนี้ประกอบด้วย **เนื้อหาการศึกษาที่เป็น Markdown** เป็นหลัก เมื่อทำการเปลี่ยนแปลง:

1. แก้ไขไฟล์ `.md` ในไดเรกทอรีโมดูลที่เหมาะสม
2. ปฏิบัติตามรูปแบบการจัดรูปแบบที่มีอยู่
3. ตรวจสอบให้แน่ใจว่าตัวอย่างโค้ดถูกต้องและผ่านการทดสอบ
4. อัปเดตเนื้อหาที่แปลที่เกี่ยวข้องหากจำเป็น (หรือปล่อยให้ระบบอัตโนมัติจัดการ)

### การพัฒนาแอปพลิเคชันตัวอย่าง

สำหรับตัวอย่าง Python ใน Module08 (ตัวอย่าง 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

สำหรับตัวอย่าง Python ใน Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

สำหรับตัวอย่าง Electron (ตัวอย่าง 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### การทดสอบแอปพลิเคชันตัวอย่าง

ตัวอย่าง Python ไม่มีการทดสอบอัตโนมัติ แต่สามารถตรวจสอบได้โดยการรัน:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

ตัวอย่าง Electron มีโครงสร้างการทดสอบ:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## คำแนะนำการทดสอบ

### การตรวจสอบเนื้อหา

คลังข้อมูลใช้กระบวนการแปลอัตโนมัติ ไม่จำเป็นต้องทดสอบการแปลด้วยตนเอง

**การตรวจสอบด้วยตนเองสำหรับการเปลี่ยนแปลงเนื้อหา:**
1. ตรวจสอบการแสดงผล Markdown โดยการดูตัวอย่างไฟล์ `.md`
2. ตรวจสอบให้แน่ใจว่าลิงก์ทั้งหมดชี้ไปยังเป้าหมายที่ถูกต้อง
3. ทดสอบตัวอย่างโค้ดใดๆ ที่รวมอยู่ในเอกสาร
4. ตรวจสอบให้แน่ใจว่าภาพโหลดได้ถูกต้อง

### การทดสอบแอปพลิเคชันตัวอย่าง

**Module08/samples/08 (แอป Electron) มีการทดสอบที่ครอบคลุม:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**ตัวอย่าง Python ควรทดสอบด้วยตนเอง:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## แนวทางการเขียนโค้ด

### เนื้อหา Markdown

- ใช้ลำดับชั้นหัวข้อที่สอดคล้องกัน (# สำหรับชื่อเรื่อง, ## สำหรับส่วนหลัก, ### สำหรับส่วนย่อย)
- รวมบล็อกโค้ดพร้อมตัวระบุภาษา: ```python, ```bash, ```javascript
- ปฏิบัติตามรูปแบบที่มีอยู่สำหรับตาราง, รายการ, และการเน้น
- ทำให้บรรทัดอ่านง่าย (~80-100 ตัวอักษร แต่ไม่เข้มงวด)
- ใช้ลิงก์สัมพัทธ์สำหรับการอ้างอิงภายใน

### รูปแบบโค้ด Python

- ปฏิบัติตามข้อกำหนด PEP 8
- ใช้ type hints เมื่อเหมาะสม
- รวม docstrings สำหรับฟังก์ชันและคลาส
- ใช้ชื่อตัวแปรที่มีความหมาย
- ทำให้ฟังก์ชันมีจุดมุ่งหมายและกระชับ

### รูปแบบโค้ด JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**ข้อกำหนดสำคัญ:**
- การกำหนดค่า ESLint มีให้ในตัวอย่าง 08
- ใช้ Prettier สำหรับการจัดรูปแบบโค้ด
- ใช้ไวยากรณ์ ES6+ สมัยใหม่
- ปฏิบัติตามรูปแบบที่มีอยู่ในฐานโค้ด

## แนวทางการส่ง Pull Request

### กระบวนการมีส่วนร่วม

1. **Fork คลังข้อมูล** และสร้างสาขาใหม่จาก `main`
2. **ทำการเปลี่ยนแปลงของคุณ** โดยปฏิบัติตามแนวทางการเขียนโค้ด
3. **ทดสอบอย่างละเอียด** โดยใช้คำแนะนำการทดสอบด้านบน
4. **Commit พร้อมข้อความที่ชัดเจน** โดยปฏิบัติตามรูปแบบ Conventional Commits
5. **Push ไปยัง Fork ของคุณ** และสร้าง Pull Request
6. **ตอบกลับความคิดเห็น** จากผู้ดูแลระหว่างการตรวจสอบ

### รูปแบบการตั้งชื่อสาขา

- `feature/<module>-<description>` - สำหรับฟีเจอร์หรือเนื้อหาใหม่
- `fix/<module>-<description>` - สำหรับการแก้ไขข้อผิดพลาด
- `docs/<description>` - สำหรับการปรับปรุงเอกสาร
- `refactor/<description>` - สำหรับการปรับโครงสร้างโค้ด

### รูปแบบข้อความ Commit

ปฏิบัติตาม [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**ตัวอย่าง:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### รูปแบบหัวข้อ
```
[ModuleXX] Brief description of change
```
หรือ
```
[Module08/samples/XX] Description for sample changes
```

### จรรยาบรรณ

ผู้มีส่วนร่วมทุกคนต้องปฏิบัติตาม [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) โปรดตรวจสอบ [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ก่อนมีส่วนร่วม

### ก่อนส่ง

**สำหรับการเปลี่ยนแปลงเนื้อหา:**
- ดูตัวอย่างไฟล์ Markdown ที่แก้ไขทั้งหมด
- ตรวจสอบลิงก์และภาพทำงาน
- ตรวจสอบการสะกดผิดและข้อผิดพลาดทางไวยากรณ์

**สำหรับการเปลี่ยนแปลงโค้ดตัวอย่าง (Module08/samples/08):**
```bash
npm run lint
npm test
```

**สำหรับการเปลี่ยนแปลงตัวอย่าง Python:**
- ทดสอบตัวอย่างรันสำเร็จ
- ตรวจสอบการจัดการข้อผิดพลาดทำงาน
- ตรวจสอบความเข้ากันได้กับ Foundry Local

### กระบวนการตรวจสอบ

- การเปลี่ยนแปลงเนื้อหาการศึกษาจะถูกตรวจสอบเพื่อความถูกต้องและความชัดเจน
- ตัวอย่างโค้ดจะถูกทดสอบเพื่อการทำงาน
- การอัปเดตการแปลจะถูกจัดการโดยอัตโนมัติผ่าน GitHub Actions

## ระบบการแปล

**สำคัญ:** คลังข้อมูลนี้ใช้การแปลอัตโนมัติผ่าน GitHub Actions

- การแปลอยู่ในไดเรกทอรี `/translations/` (50+ ภาษา)
- อัตโนมัติผ่าน workflow `co-op-translator.yml`
- **ห้ามแก้ไขไฟล์การแปลด้วยตนเอง** - ไฟล์จะถูกเขียนทับ
- แก้ไขเฉพาะไฟล์ต้นฉบับภาษาอังกฤษในไดเรกทอรีรากและโมดูล
- การแปลจะถูกสร้างโดยอัตโนมัติเมื่อ push ไปยังสาขา `main`

## การผสานรวม Foundry Local

ตัวอย่างใน Module08 ส่วนใหญ่ต้องการ Microsoft Foundry Local เพื่อรัน

### การติดตั้งและการตั้งค่า

**ติดตั้ง Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**ติดตั้ง Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### การเริ่มต้น Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### การใช้งาน SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### การตรวจสอบ Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### ตัวแปรสภาพแวดล้อมสำหรับตัวอย่าง

ตัวอย่างส่วนใหญ่ใช้ตัวแปรสภาพแวดล้อมเหล่านี้:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**หมายเหตุ**: เมื่อใช้ `FoundryLocalManager`, SDK จะจัดการการค้นหาบริการและการโหลดโมเดลโดยอัตโนมัติ ชื่อเล่นโมเดล (เช่น `phi-3.5-mini`) ช่วยให้มั่นใจว่าตัวแปรที่ดีที่สุดถูกเลือกสำหรับฮาร์ดแวร์ของคุณ

## การสร้างและการปรับใช้

### การปรับใช้เนื้อหา

คลังข้อมูลนี้เป็นเอกสารเป็นหลัก - ไม่จำเป็นต้องมีขั้นตอนการสร้างสำหรับเนื้อหา

### การสร้างแอปพลิเคชันตัวอย่าง

**แอปพลิเคชัน Electron (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**ตัวอย่าง Python:**
ไม่มีขั้นตอนการสร้าง - ตัวอย่างจะถูกรันโดยตรงด้วย Python interpreter

## ปัญหาทั่วไปและการแก้ไขปัญหา

> **เคล็ดลับ**: ตรวจสอบ [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) สำหรับปัญหาและวิธีแก้ไขที่ทราบ

### ปัญหาสำคัญ (บล็อกการทำงาน)

#### Foundry Local ไม่ทำงาน
**ปัญหา:** ตัวอย่างล้มเหลวพร้อมข้อผิดพลาดการเชื่อมต่อ

**วิธีแก้ไข:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### ปัญหาทั่วไป (ปานกลาง)

#### ปัญหา Python Virtual Environment
**ปัญหา:** ข้อผิดพลาดการนำเข้าโมดูล

**วิธีแก้ไข:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### ปัญหาการสร้าง Electron
**ปัญหา:** npm install หรือการสร้างล้มเหลว

**วิธีแก้ไข:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### ปัญหากระบวนการทำงาน (เล็กน้อย)

#### ความขัดแย้งใน Workflow การแปล
**ปัญหา:** PR การแปลขัดแย้งกับการเปลี่ยนแปลงของคุณ

**วิธีแก้ไข:**
- แก้ไขเฉพาะไฟล์ต้นฉบับภาษาอังกฤษ
- ปล่อยให้ Workflow การแปลอัตโนมัติจัดการการแปล
- หากเกิดความขัดแย้ง ให้รวม `main` เข้ากับสาขาของคุณหลังจากการแปลถูกรวม

#### การดาวน์โหลดโมเดลล้มเหลว
**ปัญหา:** Foundry Local ล้มเหลวในการดาวน์โหลดโมเดล

**วิธีแก้ไข:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## ทรัพยากรเพิ่มเติม

### เส้นทางการเรียนรู้
- **เส้นทางผู้เริ่มต้น:** โมดูล 01-02 (7-9 ชั่วโมง)
- **เส้นทางระดับกลาง:** โมดูล 03-04 (9-11 ชั่วโมง)
- **เส้นทางขั้นสูง:** โมดูล 05-07 (12-15 ชั่วโมง)
- **เส้นทางผู้เชี่ยวชาญ:** โมดูล 08 (8-10 ชั่วโมง)
- **เวิร์กช็อปแบบลงมือทำ:** วัสดุเวิร์กช็อป (6-8 ชั่วโมง)

### เนื้อหาโมดูลสำคัญ
- **Module01:** พื้นฐาน EdgeAI และกรณีศึกษาในโลกจริง
- **Module02:** ครอบครัวและสถาปัตยกรรม Small Language Model (SLM)
- **Module03:** กลยุทธ์การปรับใช้ในเครื่องและคลาวด์
- **Module04:** การปรับแต่งโมเดลด้วยเฟรมเวิร์คหลายตัว (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - การดำเนินงานในระดับการผลิต
- **Module06:** ตัวแทน AI และการเรียกฟังก์ชัน
- **Module07:** การใช้งานเฉพาะแพลตฟอร์ม
- **Module08:** เครื่องมือ Foundry Local พร้อมตัวอย่างที่ครอบคลุม 10 ตัวอย่าง

### การพึ่งพาภายนอก
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime โมเดล AI ในเครื่องที่เข้ากันได้กับ OpenAI API
  - [เอกสาร](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - เฟรมเวิร์คการปรับแต่ง
- [Microsoft Olive](https://microsoft.github.io/Olive/) - เครื่องมือปรับแต่งโมเดล
- [OpenVINO
10. **10-Foundry Tools Framework** - การผสาน LangChain/Semantic Kernel

### ตัวอย่างแอปพลิเคชันในเวิร์กช็อป

เวิร์กช็อปประกอบด้วย 6 เซสชันที่มีการพัฒนาอย่างต่อเนื่องพร้อมการใช้งานจริง:

1. **เซสชัน 01** - การเริ่มต้นแชทด้วยการผสาน Foundry Local
2. **เซสชัน 02** - การประเมินและการสร้าง RAG pipeline ด้วย RAGAS
3. **เซสชัน 03** - การเปรียบเทียบประสิทธิภาพของโมเดลโอเพ่นซอร์ส
4. **เซสชัน 04** - การเปรียบเทียบและการเลือกโมเดล
5. **เซสชัน 05** - ระบบการจัดการหลายตัวแทน
6. **เซสชัน 06** - การจัดการเส้นทางโมเดลและ pipeline

ตัวอย่างแต่ละตัวแสดงให้เห็นถึงแง่มุมต่าง ๆ ของการพัฒนา Edge AI ด้วย Foundry Local

### ข้อควรพิจารณาด้านประสิทธิภาพ

- SLMs ถูกปรับแต่งเพื่อการใช้งานใน edge (RAM 2-16GB)
- การประมวลผลในเครื่องให้เวลาตอบสนอง 50-500ms
- เทคนิคการลดขนาดช่วยลดขนาดลง 75% พร้อมรักษาประสิทธิภาพไว้ 85%
- ความสามารถในการสนทนาแบบเรียลไทม์ด้วยโมเดลในเครื่อง

### ความปลอดภัยและความเป็นส่วนตัว

- การประมวลผลทั้งหมดเกิดขึ้นในเครื่อง - ไม่มีการส่งข้อมูลไปยังคลาวด์
- เหมาะสำหรับแอปพลิเคชันที่ต้องการความเป็นส่วนตัว (สุขภาพ, การเงิน)
- ตรงตามข้อกำหนดด้านอธิปไตยของข้อมูล
- Foundry Local ทำงานทั้งหมดบนฮาร์ดแวร์ในเครื่อง

## การขอความช่วยเหลือ

### เอกสาร

- **README หลัก**: [README.md](README.md) - ภาพรวมของ repository และเส้นทางการเรียนรู้
- **คู่มือการศึกษา**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - ทรัพยากรการเรียนรู้และไทม์ไลน์
- **การสนับสนุน**: [SUPPORT.md](SUPPORT.md) - วิธีการขอความช่วยเหลือ
- **ความปลอดภัย**: [SECURITY.md](SECURITY.md) - การรายงานปัญหาด้านความปลอดภัย

### การสนับสนุนจากชุมชน

- **GitHub Issues**: [รายงานบั๊กหรือขอฟีเจอร์](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [ถามคำถามและแบ่งปันไอเดีย](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [ปัญหาทางเทคนิคเกี่ยวกับ Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### ติดต่อ

- **ผู้ดูแล**: ดู [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **ปัญหาด้านความปลอดภัย**: ปฏิบัติตามการเปิดเผยอย่างรับผิดชอบใน [SECURITY.md](SECURITY.md)
- **การสนับสนุนจาก Microsoft**: สำหรับการสนับสนุนระดับองค์กร ติดต่อฝ่ายบริการลูกค้า Microsoft

### ทรัพยากรเพิ่มเติม

- **Microsoft Learn**: [เส้นทางการเรียนรู้ AI และ Machine Learning](https://learn.microsoft.com/training/browse/?products=ai-services)
- **เอกสาร Foundry Local**: [เอกสารอย่างเป็นทางการ](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **ตัวอย่างจากชุมชน**: ตรวจสอบ [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) สำหรับการมีส่วนร่วมจากชุมชน

---

**นี่คือ repository เพื่อการศึกษาโดยมุ่งเน้นการสอนการพัฒนา Edge AI รูปแบบการมีส่วนร่วมหลักคือการปรับปรุงเนื้อหาการศึกษาและการเพิ่ม/ปรับปรุงตัวอย่างแอปพลิเคชันที่แสดงแนวคิด Edge AI**

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้