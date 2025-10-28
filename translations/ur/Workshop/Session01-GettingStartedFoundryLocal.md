<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:14:31+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ur"
}
-->
# سیشن 1: فاؤنڈری لوکل کے ساتھ شروعات

## خلاصہ

فاؤنڈری لوکل کے ساتھ اپنی سفر کا آغاز کریں، اسے ونڈوز 11 پر انسٹال اور کنفیگر کریں۔ سیکھیں کہ CLI کو کیسے سیٹ اپ کریں، ہارڈویئر ایکسیلیریشن کو فعال کریں، اور ماڈلز کو تیز لوکل انفرنس کے لیے کیش کریں۔ یہ عملی سیشن آپ کو Phi، Qwen، DeepSeek، اور GPT-OSS-20B جیسے ماڈلز کو قابل تکرار CLI کمانڈز کے ذریعے چلانے کا طریقہ دکھاتا ہے۔

## سیکھنے کے مقاصد

اس سیشن کے اختتام تک آپ:

- **انسٹال اور کنفیگر کریں**: فاؤنڈری لوکل کو ونڈوز 11 پر بہترین پرفارمنس سیٹنگز کے ساتھ سیٹ اپ کریں
- **CLI آپریشنز میں مہارت حاصل کریں**: ماڈل مینجمنٹ اور ڈیپلائمنٹ کے لیے فاؤنڈری لوکل CLI استعمال کریں
- **ہارڈویئر ایکسیلیریشن کو فعال کریں**: GPU ایکسیلیریشن کو ONNXRuntime یا WebGPU کے ساتھ کنفیگر کریں
- **متعدد ماڈلز کو ڈیپلائے کریں**: phi-4، GPT-OSS-20B، Qwen، اور DeepSeek ماڈلز کو لوکل طور پر چلائیں
- **اپنا پہلا ایپ بنائیں**: موجودہ نمونوں کو فاؤنڈری لوکل Python SDK استعمال کرنے کے لیے ایڈاپٹ کریں

# ماڈل کو ٹیسٹ کریں (غیر انٹرایکٹو سنگل پرامپٹ)
foundry model run phi-4-mini --prompt "ہیلو، اپنا تعارف کروائیں"

- ونڈوز 11 (22H2 یا بعد کا ورژن)
# دستیاب کیٹلاگ ماڈلز کی فہرست بنائیں (چلائے گئے ماڈلز ظاہر ہوں گے)
foundry model list
## نوٹ: فی الحال کوئی مخصوص `--running` فلیگ نہیں ہے؛ یہ دیکھنے کے لیے کہ کون سے لوڈ ہیں، چیٹ شروع کریں یا سروس لاگز کا معائنہ کریں۔
- Python 3.10+ انسٹال شدہ
- Visual Studio Code کے ساتھ Python ایکسٹینشن
- انسٹالیشن کے لیے ایڈمنسٹریٹر کی مراعات

### (اختیاری) ماحول کے متغیرات

اسکرپٹس کو پورٹیبل بنانے کے لیے `.env` بنائیں (یا شیل میں سیٹ کریں):
# جوابات کا موازنہ کریں (غیر انٹرایکٹو)
foundry model run gpt-oss-20b --prompt "ایج AI کو آسان الفاظ میں سمجھائیں"
| متغیر | مقصد | مثال |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | ترجیحی ماڈل عرف (کیٹلاگ خود بخود بہترین ورژن منتخب کرتا ہے) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | اینڈپوائنٹ کو اووررائیڈ کریں (ورنہ مینیجر سے خودکار) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | اسٹریمنگ ڈیمو کو فعال کریں | `true` |

> اگر `FOUNDRY_LOCAL_ENDPOINT=auto` (یا غیر سیٹ) ہے تو ہم اسے SDK مینیجر سے حاصل کرتے ہیں۔

## ڈیمو فلو (30 منٹ)

### 1. فاؤنڈری لوکل انسٹال کریں اور CLI سیٹ اپ کی تصدیق کریں (10 منٹ)

# کیش شدہ ماڈلز کی فہرست بنائیں
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (پریویو / اگر سپورٹڈ)**

اگر کوئی نیٹو macOS پیکیج فراہم کیا گیا ہو (تازہ ترین کے لیے آفیشل ڈاکس چیک کریں):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

اگر macOS نیٹو بائنریز ابھی دستیاب نہیں ہیں، تو آپ اب بھی:
1. ونڈوز 11 ARM/Intel VM (Parallels / UTM) استعمال کریں اور ونڈوز کے مراحل پر عمل کریں۔
2. ماڈلز کو کنٹینر کے ذریعے چلائیں (اگر کنٹینر امیج شائع ہو) اور `FOUNDRY_LOCAL_ENDPOINT` کو ایکسپوزڈ پورٹ پر سیٹ کریں۔

**Python ورچوئل ماحول بنائیں (کراس پلیٹ فارم)**

ونڈوز پاور شیل:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

پائپ کو اپگریڈ کریں اور بنیادی ڈیپینڈنسیز انسٹال کریں:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### مرحلہ 1.2: انسٹالیشن کی تصدیق کریں

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### مرحلہ 1.3: ماحول کو کنفیگر کریں

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK بوٹ اسٹریپنگ (تجویز کردہ)

سروس کو دستی طور پر شروع کرنے اور ماڈلز کو چلانے کے بجائے، **فاؤنڈری لوکل Python SDK** سب کچھ بوٹ اسٹریپ کر سکتا ہے:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

اگر آپ واضح کنٹرول کو ترجیح دیتے ہیں تو آپ CLI + OpenAI کلائنٹ کو بعد میں دکھائے گئے طریقے سے استعمال کر سکتے ہیں۔

### 2. ماڈلز کو لوکل طور پر CLI کے ذریعے چلائیں (10 منٹ)

#### مرحلہ 3.1: Phi-4 ماڈل کو ڈیپلائے کریں

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### مرحلہ 3.2: GPT-OSS-20B کو ڈیپلائے کریں

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### مرحلہ 3.3: اضافی ماڈلز کو لوڈ کریں

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. اسٹارٹر پروجیکٹ: 01-run-phi کو فاؤنڈری لوکل کے لیے ایڈاپٹ کریں (5 منٹ)

#### مرحلہ 4.1: بنیادی چیٹ ایپلیکیشن بنائیں

`samples/01-foundry-quickstart/chat_quickstart.py` بنائیں (اگر مینیجر دستیاب ہو تو اسے استعمال کرنے کے لیے اپڈیٹ کریں):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### مرحلہ 4.2: ایپلیکیشن کو ٹیسٹ کریں

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## کلیدی تصورات کا احاطہ

### 1. فاؤنڈری لوکل آرکیٹیکچر

- **لوکل انفرنس انجن**: ماڈلز کو مکمل طور پر آپ کے ڈیوائس پر چلاتا ہے
- **OpenAI SDK مطابقت**: موجودہ OpenAI کوڈ کے ساتھ آسان انٹیگریشن
- **ماڈل مینجمنٹ**: متعدد ماڈلز کو مؤثر طریقے سے ڈاؤنلوڈ، کیش، اور چلائیں
- **ہارڈویئر آپٹیمائزیشن**: GPU، NPU، اور CPU ایکسیلیریشن کا فائدہ اٹھائیں

### 2. CLI کمانڈ ریفرنس

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK انٹیگریشن

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## عام مسائل کا حل

### مسئلہ 1: "فاؤنڈری کمانڈ نہیں ملی"

**حل:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### مسئلہ 2: "ماڈل لوڈ کرنے میں ناکام"

**حل:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### مسئلہ 3: "localhost:5273 پر کنکشن ریفیوزڈ"

**حل:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## پرفارمنس آپٹیمائزیشن کے نکات

### 1. ماڈل سلیکشن اسٹریٹجی

- **Phi-4-mini**: عمومی کاموں کے لیے بہترین، کم میموری استعمال
- **Qwen2.5-0.5b**: تیز ترین انفرنس، کم وسائل
- **GPT-OSS-20B**: اعلیٰ معیار، زیادہ وسائل کی ضرورت
- **DeepSeek-Coder**: پروگرامنگ کاموں کے لیے بہتر

### 2. ہارڈویئر آپٹیمائزیشن

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. پرفارمنس کی نگرانی

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### اختیاری بہتریاں

| بہتری | کیا | کیسے |
|-------------|------|-----|
| مشترکہ یوٹیلیٹیز | کلائنٹ/بوٹ اسٹریپ لاجک کو دہرایا نہ کریں | `Workshop/samples/workshop_utils.py` استعمال کریں (`get_client`, `chat_once`) |
| ٹوکن استعمال کی وضاحت | ابتدائی طور پر لاگت/افادیت کی سوچ سکھائیں | `SHOW_USAGE=1` سیٹ کریں تاکہ پرامپٹ/کمپلیشن/کل ٹوکن پرنٹ ہوں |
| تعیناتی موازنہ | مستحکم بینچ مارکنگ اور ریگریشن چیکس | `temperature=0`, `top_p=1`, مستقل پرامپٹ ٹیکسٹ استعمال کریں |
| پہلا ٹوکن لیٹنسی | محسوس شدہ ردعمل میٹرک | اسٹریمنگ کے ساتھ بینچ مارک اسکرپٹ کو ایڈاپٹ کریں (`BENCH_STREAM=1`) |
| عارضی غلطیوں پر دوبارہ کوشش کریں | سرد آغاز پر مضبوط ڈیمو | `RETRY_ON_FAIL=1` (ڈیفالٹ) اور `RETRY_BACKOFF` کو ایڈجسٹ کریں |
| اسموک ٹیسٹنگ | کلیدی فلو پر فوری جانچ | ورکشاپ سے پہلے `python Workshop/tests/smoke.py` چلائیں |
| ماڈل عرف پروفائلز | مشینوں کے درمیان ماڈل سیٹ کو جلدی تبدیل کریں | `.env` برقرار رکھیں `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` کے ساتھ |
| کیشنگ کی کارکردگی | ملٹی سیمپل رن میں بار بار وارم اپ سے بچیں | یوٹیلیٹیز کیش مینیجرز؛ اسکرپٹس/نوٹ بکس کے درمیان دوبارہ استعمال کریں |
| پہلا رن وارم اپ | p95 لیٹنسی اسپائکس کو کم کریں | `FoundryLocalManager` تخلیق کے بعد ایک چھوٹا پرامپٹ فائر کریں |

پاور شیل میں مثال کے طور پر مستحکم وارم بیس لائن:

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

آپ کو دوسرے رن پر اسی طرح کا آؤٹ پٹ اور ایک جیسے ٹوکن کاؤنٹس نظر آنے چاہئیں، جو تعیناتی کی تصدیق کرتا ہے۔

## اگلے مراحل

اس سیشن کو مکمل کرنے کے بعد:

1. **سیشن 2 کو دریافت کریں**: Azure AI Foundry RAG کے ساتھ AI حل بنائیں
2. **مختلف ماڈلز آزمائیں**: Qwen، DeepSeek، اور دیگر ماڈل فیملیز کے ساتھ تجربہ کریں
3. **پرفارمنس کو بہتر بنائیں**: اپنے مخصوص ہارڈویئر کے لیے سیٹنگز کو بہتر بنائیں
4. **کسٹم ایپلیکیشنز بنائیں**: فاؤنڈری لوکل SDK کو اپنے پروجیکٹس میں استعمال کریں

## اضافی وسائل

### دستاویزات
- [فاؤنڈری لوکل Python SDK ریفرنس](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [فاؤنڈری لوکل انسٹالیشن گائیڈ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [ماڈل کیٹلاگ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### نمونہ کوڈ
- [ماڈیول08 نمونہ 01](./samples/01/README.md) - REST چیٹ کوئیک اسٹارٹ
- [ماڈیول08 نمونہ 02](./samples/02/README.md) - OpenAI SDK انٹیگریشن
- [ماڈیول08 نمونہ 03](./samples/03/README.md) - ماڈل دریافت اور بینچ مارکنگ

### کمیونٹی
- [فاؤنڈری لوکل GitHub ڈسکشنز](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI کمیونٹی](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**سیشن کا دورانیہ**: 30 منٹ عملی + 15 منٹ سوال و جواب
**مشکل کی سطح**: ابتدائی
**ضروریات**: ونڈوز 11، Python 3.10+, ایڈمنسٹریٹر رسائی

## نمونہ منظرنامہ اور ورکشاپ میپنگ

| ورکشاپ اسکرپٹ / نوٹ بک | منظرنامہ | مقصد | مثال ان پٹ | مطلوبہ ڈیٹاسیٹ |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | اندرونی IT ٹیم جو پرائیویسی اسیسمنٹ پورٹل کے لیے آن ڈیوائس انفرنس کا جائزہ لے رہی ہے | ثابت کریں کہ لوکل SLM معیاری پرامپٹس پر سب سیکنڈ لیٹنسی کے اندر جواب دیتا ہے | "لوکل انفرنس کے دو فوائد بتائیں۔" | کوئی نہیں (سنگل پرامپٹ) |
| کوئیک اسٹارٹ ایڈاپٹیشن کوڈ بلاک | ڈویلپر جو موجودہ OpenAI اسکرپٹ کو فاؤنڈری لوکل میں منتقل کر رہا ہے | ڈراپ ان مطابقت دکھائیں | "لوکل انفرنس کے دو فوائد بتائیں۔" | صرف ان لائن پرامپٹ |

### منظرنامہ بیانیہ
سیکیورٹی اور کمپلائنس اسکواڈ کو یہ تصدیق کرنی ہوگی کہ حساس پروٹوٹائپ ڈیٹا کو لوکل طور پر پروسیس کیا جا سکتا ہے۔ وہ بوٹ اسٹریپ اسکرپٹ کو کئی پرامپٹس (پرائیویسی، لیٹنسی، لاگت) کے ساتھ چلاتے ہیں، ڈیٹرمینیٹک temperature=0 موڈ استعمال کرتے ہوئے بیس لائن آؤٹ پٹس کو بعد میں موازنہ کے لیے کیپچر کرتے ہیں (سیشن 3 بینچ مارکنگ اور سیشن 4 SLM بمقابلہ LLM تضاد)۔

### کم سے کم پرامپٹ سیٹ JSON (اختیاری)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

اس فہرست کو قابل تکرار تشخیصی لوپ بنانے یا مستقبل کے ریگریشن ٹیسٹ ہارنس کو سیڈ کرنے کے لیے استعمال کریں۔

---

**اعلان**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔