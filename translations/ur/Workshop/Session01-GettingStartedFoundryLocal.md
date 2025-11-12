<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T21:46:02+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ur"
}
-->
# سیشن 1: فاؤنڈری لوکل کے ساتھ شروعات

## خلاصہ

مائیکروسافٹ فاؤنڈری لوکل کے ذریعے اپنے پہلے AI ماڈلز کو انسٹال، ترتیب دیں اور چلائیں۔ یہ عملی سیشن مقامی انفرینس کا مرحلہ وار تعارف فراہم کرتا ہے، انسٹالیشن سے لے کر ماڈلز جیسے Phi-4، Qwen، اور DeepSeek کے ساتھ اپنی پہلی چیٹ ایپلیکیشن بنانے تک۔

## سیکھنے کے مقاصد

اس سیشن کے اختتام تک آپ:

- **انسٹال اور ترتیب دیں**: فاؤنڈری لوکل کو صحیح انسٹالیشن کی تصدیق کے ساتھ سیٹ اپ کریں گے
- **CLI آپریشنز میں مہارت حاصل کریں**: ماڈل مینجمنٹ اور ڈپلائمنٹ کے لیے فاؤنڈری لوکل CLI استعمال کریں گے
- **اپنا پہلا ماڈل چلائیں**: مقامی AI ماڈل کو کامیابی سے ڈپلائے اور انٹریکٹ کریں گے
- **چیٹ ایپ بنائیں**: فاؤنڈری لوکل پائتھون SDK استعمال کرتے ہوئے ایک بنیادی چیٹ ایپلیکیشن بنائیں گے
- **مقامی AI کو سمجھیں**: مقامی انفرینس اور ماڈل مینجمنٹ کی بنیادی باتوں کو سمجھیں گے

## ضروریات

### سسٹم کی ضروریات

- **ونڈوز**: ونڈوز 11 (22H2 یا بعد کا) یا **macOS**: macOS 11+ (محدود سپورٹ)
- **RAM**: کم از کم 8GB، 16GB+ تجویز کردہ
- **اسٹوریج**: ماڈلز کے لیے 10GB+ خالی جگہ
- **پائتھون**: 3.10 یا بعد کا انسٹال شدہ
- **ایڈمن رسائی**: انسٹالیشن کے لیے ایڈمنسٹریٹر کی مراعات

### ترقیاتی ماحول

- پائتھون ایکسٹینشن کے ساتھ ویژول اسٹوڈیو کوڈ (تجویز کردہ)
- کمانڈ لائن رسائی (ونڈوز پر پاور شیل، macOS پر ٹرمینل)
- ریپوزیٹریز کلون کرنے کے لیے گٹ (اختیاری)

## ورکشاپ کا بہاؤ (30 منٹ)

### مرحلہ 1: فاؤنڈری لوکل انسٹال کریں (5 منٹ)

#### ونڈوز انسٹالیشن

ونڈوز پیکیج مینیجر استعمال کرتے ہوئے فاؤنڈری لوکل انسٹال کریں:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

متبادل: [مائیکروسافٹ لرن](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install) سے براہ راست ڈاؤنلوڈ کریں

#### macOS انسٹالیشن (محدود سپورٹ)

> [!NOTE]  
> macOS سپورٹ فی الحال پریویو میں ہے۔ تازہ ترین دستیابی کے لیے آفیشل دستاویزات چیک کریں۔

اگر دستیاب ہو تو، ہوم بریو استعمال کرتے ہوئے انسٹال کریں:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**macOS صارفین کے لیے متبادل:**
- ونڈوز 11 VM (Parallels/UTM) استعمال کریں اور ونڈوز کے مراحل پر عمل کریں
- کنٹینر کے ذریعے چلائیں اگر دستیاب ہو اور `FOUNDRY_LOCAL_ENDPOINT` کو ترتیب دیں

### مرحلہ 2: انسٹالیشن کی تصدیق کریں (3 منٹ)

انسٹالیشن کے بعد، اپنا ٹرمینل دوبارہ شروع کریں اور تصدیق کریں کہ فاؤنڈری لوکل کام کر رہا ہے:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

متوقع آؤٹ پٹ ورژن کی معلومات اور دستیاب کمانڈز دکھائے گا۔

### مرحلہ 3: پائتھون ماحول ترتیب دیں (5 منٹ)

اس ورکشاپ کے لیے ایک مخصوص پائتھون ماحول بنائیں:

**ونڈوز:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```


### مرحلہ 4: اپنا پہلا ماڈل چلائیں (7 منٹ)

اب ہم اپنا پہلا AI ماڈل مقامی طور پر چلائیں گے!

#### Phi-4 Mini سے شروع کریں (تجویز کردہ پہلا ماڈل)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]  
> یہ کمانڈ ماڈل کو ڈاؤنلوڈ کرتی ہے (پہلی بار) اور فاؤنڈری لوکل سروس کو خود بخود شروع کرتی ہے۔

#### چیک کریں کہ کیا چل رہا ہے

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```


#### مختلف ماڈلز آزمائیں

ایک بار phi-4-mini کام کر رہا ہو، دوسرے ماڈلز کے ساتھ تجربہ کریں:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```


### مرحلہ 5: اپنی پہلی چیٹ ایپلیکیشن بنائیں (10 منٹ)

اب ہم ایک پائتھون ایپلیکیشن بنائیں گے جو ان ماڈلز کو استعمال کرے گی جو ہم نے ابھی شروع کیے ہیں۔

#### چیٹ اسکرپٹ بنائیں

`my_first_chat.py` نامی ایک نئی فائل بنائیں (یا فراہم کردہ نمونہ استعمال کریں):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]  
> **متعلقہ مثالیں**: مزید جدید استعمال کے لیے دیکھیں:
>
> - **پائتھون نمونہ**: `Workshop/samples/session01/chat_bootstrap.py` - اسٹریمنگ جوابات اور ایرر ہینڈلنگ شامل ہیں
> - **جوپیٹر نوٹ بک**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - تفصیلی وضاحتوں کے ساتھ انٹرایکٹو ورژن

#### اپنی چیٹ ایپلیکیشن کی جانچ کریں

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

متبادل: فراہم کردہ نمونوں کو براہ راست استعمال کریں

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

یا انٹرایکٹو نوٹ بک کو دریافت کریں  
Workshop/notebooks/session01_chat_bootstrap.ipynb کو VS کوڈ میں کھولیں

ان مثال گفتگو کو آزمائیں:

- "مائیکروسافٹ فاؤنڈری لوکل کیا ہے؟"
- "AI ماڈلز کو مقامی طور پر چلانے کے 3 فوائد بتائیں"
- "مجھے ایج AI کو سمجھنے میں مدد کریں"

## آپ نے کیا حاصل کیا

مبارک ہو! آپ نے کامیابی سے:

1. ✅ **فاؤنڈری لوکل انسٹال کیا** اور تصدیق کی کہ یہ کام کر رہا ہے
2. ✅ **اپنا پہلا AI ماڈل شروع کیا** (phi-4-mini) مقامی طور پر
3. ✅ **مختلف ماڈلز کو کمانڈ لائن کے ذریعے آزمایا**
4. ✅ **ایک چیٹ ایپلیکیشن بنائی** جو آپ کے مقامی AI سے جڑتی ہے
5. ✅ **مقامی AI انفرینس کا تجربہ کیا** بغیر کلاؤڈ انحصار کے

## جو کچھ ہوا اسے سمجھنا

### مقامی AI انفرینس

- آپ کے AI ماڈلز مکمل طور پر آپ کے کمپیوٹر پر چلتے ہیں
- کوئی ڈیٹا کلاؤڈ کو نہیں بھیجا جاتا
- جوابات آپ کے CPU/GPU کا استعمال کرتے ہوئے مقامی طور پر تیار کیے جاتے ہیں
- پرائیویسی اور سیکیورٹی برقرار رہتی ہے

### ماڈل مینجمنٹ

- `foundry model run` ماڈلز کو ڈاؤنلوڈ اور شروع کرتا ہے
- **FoundryLocalManager SDK** سروس اسٹارٹ اپ اور ماڈل لوڈنگ کو خود بخود ہینڈل کرتا ہے
- ماڈلز مستقبل کے استعمال کے لیے مقامی طور پر کیش کیے جاتے ہیں
- متعدد ماڈلز ڈاؤنلوڈ کیے جا سکتے ہیں لیکن عام طور پر ایک وقت میں ایک چلتا ہے
- سروس خود بخود ماڈل لائف سائیکل کو مینج کرتی ہے

### SDK بمقابلہ CLI طریقے

- **CLI طریقہ**: `foundry model run <model>` کے ساتھ دستی ماڈل مینجمنٹ
- **SDK طریقہ**: `FoundryLocalManager(alias)` کے ساتھ خودکار سروس + ماڈل مینجمنٹ
- **تجویز**: ایپلیکیشنز کے لیے SDK استعمال کریں، ٹیسٹنگ اور ایکسپلوریشن کے لیے CLI

## عام کمانڈز کا حوالہ

### ضروری CLI کمانڈز

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```


### ماڈل کی سفارشات

- **phi-4-mini**: بہترین ابتدائی ماڈل - تیز، ہلکا پھلکا، اچھی کوالٹی
- **qwen2.5-0.5b**: تیز ترین انفرینس، کم سے کم میموری استعمال
- **gpt-oss-20b**: اعلیٰ معیار کے جوابات، زیادہ وسائل کی ضرورت
- **deepseek-coder-1.3b**: پروگرامنگ اور کوڈ کے کاموں کے لیے بہتر

## خرابیوں کا ازالہ

### "فاؤنڈری کمانڈ نہیں ملی"

**حل:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```


### "ماڈل لوڈ کرنے میں ناکام"

**حل:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```


### "لوکل ہوسٹ پر کنکشن ریفیوزڈ"

**حل:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```


## اگلے اقدامات

### فوری اگلے ایکشنز

1. **مختلف ماڈلز اور پرامپٹس کے ساتھ تجربہ کریں**
2. **اپنی چیٹ ایپلیکیشن میں ترمیم کریں تاکہ مختلف ماڈلز آزمائے جا سکیں**
3. **اپنے پرامپٹس بنائیں اور جوابات آزمائیں**
4. **سیشن 2: RAG ایپلیکیشنز بنانے کو دریافت کریں**

### ایڈوانسڈ لرننگ پاتھ

1. **سیشن 2**: RAG (Retrieval-Augmented Generation) کے ساتھ AI حل بنائیں
2. **سیشن 3**: مختلف اوپن سورس ماڈلز کا موازنہ کریں
3. **سیشن 4**: جدید ترین ماڈلز کے ساتھ کام کریں
4. **سیشن 5**: ملٹی ایجنٹ AI سسٹمز بنائیں

## ماحول کے متغیرات (اختیاری)

زیادہ جدید استعمال کے لیے، آپ یہ ماحول کے متغیرات سیٹ کر سکتے ہیں:

| متغیر | مقصد | مثال |
|-------|-------|-------|
| `FOUNDRY_LOCAL_ALIAS` | استعمال کرنے کے لیے ڈیفالٹ ماڈل | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | اینڈ پوائنٹ URL کو اووررائیڈ کریں | `http://localhost:5273/v1` |

اپنے پروجیکٹ ڈائریکٹری میں `.env` فائل بنائیں:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```


## اضافی وسائل

### دستاویزات

- [فاؤنڈری لوکل پائتھون SDK حوالہ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [فاؤنڈری لوکل انسٹالیشن گائیڈ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [ماڈل کیٹلاگ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### نمونہ کوڈ

- **سیشن01 پائتھون نمونہ**: `Workshop/samples/session01/chat_bootstrap.py` - اسٹریمنگ کے ساتھ مکمل چیٹ ایپ
- **سیشن01 نوٹ بک**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - انٹرایکٹو ٹیوٹوریل  
- [ماڈیول08 نمونہ 01](../Module08/samples/01/README.md) - REST چیٹ کوئیک اسٹارٹ
- [ماڈیول08 نمونہ 02](../Module08/samples/02/README.md) - OpenAI SDK انٹیگریشن
- [ماڈیول08 نمونہ 03](../Module08/samples/03/README.md) - ماڈل ڈسکوری اور بینچ مارکنگ

### کمیونٹی

- [فاؤنڈری لوکل گٹ ہب ڈسکشنز](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI کمیونٹی](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**سیشن کا دورانیہ**: 30 منٹ عملی + 15 منٹ سوال و جواب  
**مشکل کی سطح**: ابتدائی  
**ضروریات**: ونڈوز 11/macOS 11+, پائتھون 3.10+, ایڈمن رسائی

## ورکشاپ کی مثال منظرنامہ

### حقیقی دنیا کا سیاق و سباق

**منظرنامہ**: ایک انٹرپرائز IT ٹیم کو حساس ملازم کی رائے کو پروسیس کرنے کے لیے ڈیوائس پر AI انفرینس کا جائزہ لینے کی ضرورت ہے، بغیر ڈیٹا کو بیرونی سروسز پر بھیجے۔

**آپ کا مقصد**: یہ ظاہر کریں کہ مقامی AI ماڈلز معیاری جوابات فراہم کر سکتے ہیں، سب سیکنڈ لیٹنسی کے ساتھ، جبکہ مکمل ڈیٹا پرائیویسی برقرار رکھتے ہیں۔

### ٹیسٹ پرامپٹس

اپنے سیٹ اپ کی تصدیق کے لیے ان پرامپٹس کا استعمال کریں:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```


### کامیابی کے معیار

- ✅ تمام پرامپٹس 2 سیکنڈ سے کم وقت میں جوابات حاصل کرتے ہیں
- ✅ کوئی ڈیٹا آپ کی مقامی مشین سے باہر نہیں جاتا
- ✅ جوابات متعلقہ اور مددگار ہیں
- ✅ آپ کی چیٹ ایپلیکیشن ہموار طریقے سے کام کرتی ہے

یہ تصدیق یقینی بناتی ہے کہ آپ کا فاؤنڈری لوکل سیٹ اپ سیشنز 2-6 میں ایڈوانسڈ ورکشاپس کے لیے تیار ہے۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->