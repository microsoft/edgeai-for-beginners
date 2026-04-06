# សម័យទី 1៖ ចាប់ផ្ដើមជាមួយ Foundry Local

## សេចក្តីសង្ខេប

រៀនដើម្បីតម្លើង កំណត់រចនាសម្ព័ន្ធ និងបើកដំណើរការម៉ូឌែល AI ដំបូងរបស់អ្នកដោយប្រើ Microsoft Foundry Local។ សម័យបង្គួរសកម្មនេះផ្តល់នូវការណែនាំជាជំហានដោយជំហានសម្រាប់ការវិភាគក្នុងតំបន់ស្រុក ចាប់ពីការតម្លើងរហូតដល់ការសាងសង់កម្មវិធីសន្ទនា ដំបូងដោយប្រើម៉ូឌែលដូចជា Phi-4, Qwen និង DeepSeek។

## លទ្ធផលការសិក្សា

នៅចុងបញ្ចប់សម័យនេះ អ្នកនឹងអាច៖

- **តម្លើង និងកំណត់រចនាសម្ព័ន្ធ**៖ ចាប់ផ្ដើម Foundry Local ជាមួយការបញ្ជាក់ការតម្លើងត្រឹមត្រូវ
- **ជំនាញប្រតិបត្តិការ CLI**៖ ប្រើ Foundry Local CLI សម្រាប់ការគ្រប់គ្រងម៉ូឌែល និងការចែកចាយ
- **បើកដំណើរការម៉ូឌែលដំបូងរបស់អ្នក**៖ ចេញម៉ូឌែល AI ក្នុងតំបន់ស្រុកបានជោគជ័យ និងមានអន្តរកម្ម
- **សាងសង់កម្មវិធីសន្ទនា**៖ បង្កើតកម្មវិធីសន្ទនាមូលដ្ឋានដោយប្រើ Foundry Local Python SDK
- **យល់ដឹងអំពី AI ក្នុងតំបន់ស្រុក**៖ ទទួលយកមូលដ្ឋាននៃការវិភាគក្នុងតំបន់ និងការគ្រប់គ្រងម៉ូឌែល

## តម្រូវការមុន

### តម្រូវការប្រព័ន្ធ

- **Windows**៖ Windows 11 (22H2 ឬក្រោយ) ឬ **macOS**៖ macOS 11+ (គាំទ្រពិបាក)
- **RAM**៖ យ៉ាងហោចណាស់ 8GB, ផ្ដល់អនុសាសន៍ 16GB ឡើង
- **ទំហំស្តុក**៖ មានទំហំទំនេរ 10GB+ សម្រាប់ម៉ូឌែល
- **Python**៖ បានដំឡើង 3.10 ឬក្រោយ
- **ការចូលដំណើរការ Admin**៖ អនុសិទ្ធិរបស់អ្នកគ្រប់គ្រងសម្រាប់ការតម្លើង

### ពហុបរិបទអភិវឌ្ឍន៍

- Visual Studio Code ជាមួយបន្ទាត់បន្ថែម Python (ផ្តល់អនុសាសន៍)
- ការចូលដំណើរការបញ្ជាជួរ (PowerShell លើ Windows, Terminal លើ macOS)
- Git សម្រាប់បញ្ចូលឃ្លាំង (ជាជម្រើស)

## ចលនាសិក្ខាសាលា (៣០ នាទី)

### ជំហានទី ១៖ តម្លើង Foundry Local (៥ នាទី)

#### តម្លើងលើ Windows

តម្លើង Foundry Local ដោយប្រើកម្មវិធីគ្រប់គ្រងកញ្ចប់ Windows៖

```powershell
# តម្លើងតាមរយៈ winget (បนะนำ)
winget install Microsoft.FoundryLocal
```
  
ជម្រើសជំនួស៖ ទាញយកโดยផ្ទាល់ពី [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### តម្លើងលើ macOS (គាំទ្រពិបាក)

> [!NOTE]  
> ការគាំទ្រមាននៅ macOS កំពុងសាកល្បង។ សូមពិនិត្យឯកសារផ្លូវការសម្រាប់ភាពមានស្រេចថ្មីបំផុត។

បើមាន សូមតម្លើងដោយប្រើ Homebrew៖

```bash
# ប្រសិនបើមានរូបមន្ត Homebrew
brew update
brew install foundry-local

# ឬទាញយកដោយដៃ (ពិនិត្យលិខិតណែនាំផ្លូវការសម្រាប់ចុងក្រោយ)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```
  
**ជម្រើសជំនួសសម្រាប់អ្នកប្រើ macOS៖**  
- ប្រើ VM Windows 11 (Parallels/UTM) ហើយបន្តតាមជំហាន Windows  
- បើកដោយប្រើ container បើអាចរកបាន និងកំណត់ `FOUNDRY_LOCAL_ENDPOINT`

### ជំហានទី ២៖ ផ្ទៀងផ្ទាត់ការតម្លើង (៣ នាទី)

បន្ទាប់ពីតម្លើង សូមបើកបន្ត Terminal របស់អ្នកឡើងវិញ និងផ្ទៀងផ្ទាត់ថា Foundry Local កំពុងដំណើរការ៖

```powershell
# ពិនិត្យមើលថា Foundry Local ត្រូវបានដំឡើងយ៉ាងត្រឹមត្រូវទេ
foundry --version

# មើលពាក្យបញ្ជាដែលមានស្រាប់
foundry --help
```
  
លទ្ធផលដែលរំពឹងទុកគឺបង្ហាញព័ត៌មានជំនាន់ និងពាក្យបញ្ជាច្រើនដែលអាចប្រើបាន។

### ជំហានទី ៣៖ កំណត់បរិបទ Python (៥ នាទី)

បង្កើតបរិបទ Python ផ្តាច់មុខសម្រាប់សិក្ខាសាលានេះ៖

**Windows:**  
```powershell
# បង្កើតបរិយាកាសវេរុចជាលក្ខណៈ
py -m venv .venv

# បើកបរិយាកាស
.\.venv\Scripts\Activate.ps1

# ធ្វើបច្ចុប្បន្នភាព pip និងដំឡើងការពាក់ព័ន្ធ
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
**macOS/Linux:**  
```bash
# បង្កើតបរិយាកាសវីរុយ
python3 -m venv .venv

# បើកបរិយាកាស
source .venv/bin/activate

# ធ្វើឲ្យ pip ឡើងកំពូល និងដំឡើងការពឹងផ្អែក
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```


### ជំហានទី ៤៖ បើកដំណើរការម៉ូឌែលដំបូងរបស់អ្នក (៧ នាទី)

ឥឡូវនេះចាប់ផ្ដើមបើកដំណើរការម៉ូឌែល AI ដំបូងរបស់យើងក្នុងតំបន់ស្រុក!

#### ចាប់ផ្ដើមជាមួយ Phi-4 Mini (ម៉ូឌែលដំបូងដែលផ្ដល់អនុសាសន៍)

```powershell
# ទាញយកនិងចាប់ផ្ដើម phi-4-mini (ស្រាល, លឿន)
foundry model run phi-4-mini

# សាកល្បងម៉ូដែលជាមួយការបញ្ចូលងាយៗមួយ
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```
  
> [!TIP]  
> ពាក្យបញ្ជានេះទាញយកម៉ូឌែល (នៅពេលដំបូង) ហើយចាប់ផ្ដើមសេវាកម្ម Foundry Local ដោយស្វ័យប្រវត្តិ។

#### ពិនិត្យអ្វីដែលកំពុងដំណើរការ

```powershell
# បញ្ជីម៉ូដែលដែលអាចប្រើបាន (បង្ហាញម៉ូដែលដែលបានទាញយក)
foundry model list

# ពិនិត្យស្ថានភាពសេវាកម្ម
foundry service status

# មើលម៉ូដែលដែលបានរក្សាទុកក្នុងម៉ាស៊ីនក្នុងស្រុក
foundry cache list
```
  
#### សាកល្បងម៉ូឌែលផ្សេងទៀត

បន្ទាប់ពី phi-4-mini ដំណើរការបាន សូមសាកល្បងម៉ូឌែលផ្សេងៗ៖

```powershell
# ម៉ូឌែលធំជាងមានសមត្ថភាពល្អប្រសើរជាង
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# ម៉ូឌែលលឿន និងមានប្រសិទ្ធភាព
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```


### ជំហានទី ៥៖ សាងសង់កម្មវិធីសន្ទនាដំបូងរបស់អ្នក (១០ នាទី)

ឥឡូវនេះចាប់ផ្ដើមបង្កើតកម្មវិធី Python ដែលប្រើម៉ូឌែលដែលយើងទើបបើកដំណើរការ។

#### បង្កើតស្គ្រីបសន្ទនា

បង្កើតឯកសារថ្មីឈ្មោះ `my_first_chat.py` (ឬប្រើឧទាហរណ៍ដែលបានផ្តល់):

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
    # ទទួលយកឈ្មោះម៉ូដែលពីបរិបទបរិយាកាស ឬប្រើលំនាំដើម
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # រាប់បញ្ចូល Foundry Local Manager (ចាប់ផ្តើមសេវាដោយស្វ័យប្រវត្តិ, ទាញយកម៉ូដែល)
        manager = FoundryLocalManager(alias)
        
        # បង្កើតអតិថិជន OpenAI ដែលបញ្ជូនទៅកាន់ចំណុចបញ្ចប់ក្នុងស្រុក
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # ទទួលយក ID ម៉ូដែលពិតសម្រាប់ឈ្មោះនេះ
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
        # ទទួលបានការបញ្ចូលពីអ្នកប្រើ
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # ផ្ញើសារទៅកាន់ម៉ូដែល AI ក្នុងស្រុក
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # បង្ហាញចម្លើយ
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```
  
> [!TIP]  
> **ឧទាហរណ៍ទាក់ទង**៖ សម្រាប់ការប្រើប្រាស់កម្រិតខ្ពស់បន្ថែម សូមមើល៖  
>  
> - **ឧទាហរណ៍ Python**៖ `Workshop/samples/session01/chat_bootstrap.py` - រួមមានចម្លើយធ្លាយជាស្ទ្រីម និងការពិនិត្យកំហុស  
> - **សៀវភៅបញ្ជា Jupyter**៖ `Workshop/notebooks/session01_chat_bootstrap.ipynb` - ជាទម្រង់អន្តរកម្មមានការពណ៌នាពីលម្អិត  

#### សាកល្បងកម្មវិធីសន្ទនារបស់អ្នក

```powershell
# មិនចាំបាច់ចាប់ផ្ដើមម៉ូដែលដោយដៃទេ - FoundryLocalManager គ្រប់គ្រងនេះ!
# គ្រាន់តែដំណើរការកម្មវិធីផ្ទាល់ខ្លួនរបស់អ្នក saja
python my_first_chat.py
```
  
ជម្រើសជំនួស៖ ប្រើឧទាហរណ៍ដែលបានផ្តល់ដោយផ្ទាល់

```powershell
# ព្យាយាមឧទាហរណ៍ពេញលេញជាមួយការគាំទ្រចាក់បញ្ចាំង
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```
  
ឬសាកល្បងសៀវភៅបញ្ជាអន្តរកម្ម  
បើក Workshop/notebooks/session01_chat_bootstrap.ipynb នៅក្នុង VS Code

សាកល្បងពាក្យសំណួរខាងក្រោម៖

- "Microsoft Foundry Local ជាអ្វី?"
- "រាយបញ្ជី 3 អត្ថប្រយោជន៍នៃការរត់ម៉ូឌែល AI ក្នុងតំបន់ស្រុក"
- "ជួយខ្ញុំដឹងអំពី edge AI"

## អ្វីដែលអ្នកបានសម្រេច

សូមអបអរសាទរ! អ្នកបានជោគជ័យក្នុងការប្រតិបត្តិ៖

1. ✅ **បានតម្លើង Foundry Local** ហើយបញ្ជាក់ថាវាដំណើរការ
2. ✅ **បានបើកដំណើរការម៉ូឌែល AI ដំបូង** (phi-4-mini) ក្នុងតំបន់ស្រុក
3. ✅ **បានសាកល្បងម៉ូឌែលផ្សេងៗ** តាមរយៈបញ្ជាជួរ
4. ✅ **បានសាងសង់កម្មវិធីសន្ទនា** ដែលភ្ជាប់ជាមួយ AI ក្នុងតំបន់ស្រុក
5. ✅ **បានប្រើប្រាស់ការវិភាគ AI ក្នុងតំបន់** ដោយគ្មានការពឹងផ្អែកលើផ្លតថ័រ Cloud

## យល់ដឹងពីអ្វីដែលបានកើតឡើង

### ការវិភាគ AI ក្នុងតំបន់ស្រុក

- ម៉ូឌែល AI របស់អ្នកដំណើរការជាប់នៅលើកុំព្យូទ័ររបស់អ្នកទាំងស្រុង
- មិនមានទិន្នន័យបញ្ចូនទៅ Cloud ទេ
- ចម្លើយត្រូវបានបង្កើតឡើងក្នុងតំបន់ស្រុកដោយប្រើ CPU/GPU របស់អ្នក
- រក្សាទុកភាពឯកជន និងសុវត្ថិភាព

### ការគ្រប់គ្រងម៉ូឌែល

- `foundry model run` ទាញយក និងចាប់ផ្តើមម៉ូឌែល
- **FoundryLocalManager SDK** គ្រប់គ្រងការចាប់ផ្តើមសេវា និងការផ្ទុកម៉ូឌែលដោយស្វ័យប្រវត្តិ
- ម៉ូឌែលត្រូវបានរក្សាទុកក្នុងតំបន់ស្រុកសម្រាប់ការប្រើប្រាស់បន្ទាប់
- អាចទាញយកម៉ូឌែលជាច្រើនបាន ប៉ុន្តែធម្មតាដំណើរការតែមួយម៉ូឌែលក្នុងពេលតែមួយ
- សេវាកម្មគ្រប់គ្រងរថយន្តជីវិតរបស់ម៉ូឌែលដោយស្វ័យប្រវត្តិ

### វិធាន SDK និង CLI

- **វិធាន CLI**៖ គ្រប់គ្រងម៉ូឌែលដោយដៃជាមួយ `foundry model run <model>`
- **វិធាន SDK**៖ គ្រប់គ្រងសេវាកម្ម និងម៉ូឌែលដោយស្វ័យប្រវត្តិជាមួយ `FoundryLocalManager(alias)`
- **ការផ្តល់អនុសាសន៍**៖ ប្រើ SDK សម្រាប់កម្មវិធី, CLI សម្រាប់សាកល្បង និងស្វែងយល់

## គន្លឹះពាក្យបញ្ជាដែលប្រើប្រាស់ជាញឹកញាប់

### ពាក្យបញ្ជា CLI សំខាន់ៗ

```powershell
# ការដំឡើង និងការតំឡើង
foundry --version              # ពិនិត្យការដំឡើង
foundry --help                 # មើលបញ្ជារទាំងអស់

# ការគ្រប់គ្រងម៉ូដែល
foundry model list             # បញ្ជីម៉ូដែលដែលមាន
foundry model run <model>      # ទាញយក និងចាប់ផ្តើមម៉ូដែលមួយ
foundry model run <model> --prompt "text"  # ប្រាក់បញ្ចូលមួយដង
foundry cache list             # បង្ហាញម៉ូដែលដែលបានទាញយក

# ការគ្រប់គ្រងសេវាកម្ម
foundry service status         # ពិនិត្យថា សេវាកម្មកំពុងដំណើរការឬអត់
foundry service start          # ចាប់ផ្តើមសេវាកម្មដោយដៃ
foundry service stop           # បញ្ឈប់សេវាកម្ម
```


### ការផ្តល់អនុសាសន៍ម៉ូឌែល

- **phi-4-mini**៖ ម៉ូឌែលសាកល្បងល្អបំផុត - លឿន ងាយស្រួល ប្រើប្រាស់ទាប និងគុណភាពល្អ
- **qwen2.5-0.5b**៖ ជោគជ័យលឿនបំផុត សំរាប់ប្រើប្រាស់អង្គចម្រាស់តិច
- **gpt-oss-20b**៖ ចម្លើយគុណភាពខ្ពស់ ត្រូវការទំនាក់ទំនងធនធានច្រើន
- **deepseek-coder-1.3b**៖ ថាត្បាតសម្រាប់កម្មវិធី និងកូដកម្មវិធី

## ដោះស្រាយបញ្ហា

### "ពាក្យបញ្ជា Foundry មិនបានរកឃើញ"

**ដំណោះស្រាយ៖**

```powershell
# ចាប់ផ្តើមប្រើទ терминលរបស់អ្នកម្តងទៀតបន្ទាប់ពីការតំឡើង
# ឬបន្ថែមទៅ PATH ដោយដៃ (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```


### "ម៉ូឌែលបរាជ័យក្នុងការផ្ទុក"

**ដំណោះស្រាយ៖**

```powershell
# ពិនិត្យមើលអនុស្សាវរីយ៍ប្រព័ន្ធដែលមានស្រាប់
foundry service status

# សាកល្បងម៉ូដែលតូចជាងគេទៅមុន
foundry model run phi-4-mini

# ពិនិត្យមើលទំហំឌីសសម្រាប់ការទាញយកម៉ូដែល
# ម៉ូដែលត្រូវបានផ្ទុកនៅក្នុង៖ %USERPROFILE%\.foundry\models (Windows)
```


### "ការតភ្ជាប់ត្រូវបានបដិសេធនៅ localhost"

**ដំណោះស្រាយ៖**

```powershell
# ពិនិត្យមើលថាតើសេវាកម្មកំពុងដំណើរការឬទេ
foundry service status

# ចាប់ផ្តើមសេវាកម្ម ប្រសិនបើចាំបាច់
foundry service start

# ពិនិត្យច្រក (លំនាំដើមគឺ 5273)
# ពិនិត្យ conflictos ច្រកជាមួយ: netstat -an | findstr 5273
```


## ជំហានបន្ទាប់

### សកម្មភាពបន្ទាន់បន្ទាប់

1. **សាកល្បង** ម៉ូឌែល និងបញ្ចូលបញ្ហាប្រកួតផ្សេងៗ
2. **កែប្រែ**កម្មវិធីសន្ទនារបស់អ្នកសម្រាប់សាកល្បងម៉ូឌែលផ្សេងៗ
3. **បង្កើត**បញ្ហាប្រកួតរបស់អ្នកដោយផ្ទាល់ និងសាកល្បងចម្លើយ
4. **ស្វែងយល់** សម័យទី 2៖ សាងសង់កម្មវិធី RAG

### ផ្លូវការសិក្សាខ្ពស់

1. **សម័យទី 2**៖ សាងសង់ដំណោះស្រាយ AI ជាមួយ RAG (Retrieval-Augmented Generation)
2. **សម័យទី 3**៖ ប្រៀបធៀបម៉ូឌែល open-source ផ្សេងៗ
3. **សម័យទី 4**៖ ធ្វើការជាមួយម៉ូឌែលទំនើប
4. **សម័យទី 5**៖ សាងសង់ប្រពន្ធ័ AI អ្នកប្រតិបត្តិការច្រើនជីវិត

## មូលដ្ឋានបរិយាកាស (ជាជម្រើស)

សម្រាប់ការប្រើប្រាស់កម្រិតខ្ពស់ បើកតម្លើងអថេរបរិយាកាសខាងក្រោម៖

| អថេរ | គោលបំណង | ឧទាហរណ៍ |
|----------|-------------|------------|
| `FOUNDRY_LOCAL_ALIAS` | ម៉ូឌែលលំនាំដើមសម្រាប់ប្រើ | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | ប្តូរអាសយដ្ឋាន endpoint | `http://localhost:5273/v1` |

បង្កើតឯកសារ `.env` នៅក្នុងថតគម្រោងរបស់អ្នក៖  
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```


## ប្រភពបន្ថែម

### ឯកសារយោង

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)  
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)  
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)  

### ឧទាហរណ៍កូដ

- **ឧទាហរណ៍ Python សម័យទី 01**៖ `Workshop/samples/session01/chat_bootstrap.py` - កម្មវិធីសន្ទនាពេញលេញជាមួយចម្លើយធ្លាយស្ទ្រីម  
- **សៀវភៅបញ្ជាសម័យទី 01**៖ `Workshop/notebooks/session01_chat_bootstrap.ipynb` - មេរៀនអន្តរកម្ម  
- [Module08 ឧទាហរណ៍ 01](../Module08/samples/01/README.md) - REST Chat Quickstart  
- [Module08 ឧទាហរណ៍ 02](../Module08/samples/02/README.md) - ការរួមបញ្ចូល OpenAI SDK  
- [Module08 ឧទាហរណ៍ 03](../Module08/samples/03/README.md) - ការស្វែងរកម៉ូឌែល និងវាយតម្លៃសមត្ថភាព  

### សហគមន៍

- [សហគមន៍ Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)  
- [សហគមន៍ AI Azure](https://techcommunity.microsoft.com/category/artificialintelligence)  

---

**រយៈពេលសម័យ**៖ ៣០ នាទីបង្គួរដោយហត្ថ + ១៥ នាទីសំណួរ និងចម្លើយ  
**កម្រិតលំបាក**៖ អ្នកចាប់ផ្ដើម  
**តម្រូវការមុន**៖ Windows 11/macOS 11+, Python 3.10+, អនុសិទ្ធិ Admin

## ស្ថានភាពឧទាហរណ៍សិក្ខាសាលា

### ស្ថានភាពពិត

**ស្ថានភាព**៖ ក្រុម IT អង្គការមួយត្រូវការ វាយតម្លៃការវិភាគ AI នៅលើឧបករណ៍សម្រាប់ដំណើរការពត៌មានមតិកម្មការងារសម្ងាត់ ដោយមិនផ្ញើទិន្នន័យទៅសេវាកម្មខាងក្រៅ។

**គោលបំណងរបស់អ្នក**៖ បង្ហាញថាម៉ូឌែល AI ក្នុងតំបន់ស្រុកអាចផ្តល់ចម្លើយគុណភាពល្អជាមួយពេលសង្ស័យក្រោមមួយវិនាទីជាមួយការរក្សាទុកភាពឯកជនទិន្នន័យពេញលេញ។

### ពាក្យសាកល្បង

ប្រើពាក្យសំណួរខាងក្រោមដើម្បីបញ្ជាក់ការកំណត់របស់អ្នក៖

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```


### វិសាលភាពជោគជ័យ

- ✅ ពាក្យសំណួរទាំងអស់ទទួលបានចម្លើយក្រោម 2 វិនាទី  
- ✅ គ្មានទិន្នន័យចេញពីកុំព្យូទ័ររបស់អ្នក  
- ✅ ចម្លើយពិតជា សមរម្យ និងមានប្រយោជន៍  
- ✅ កម្មវិធីសន្ទនារបស់អ្នកដំណើរការទៀងទាត់

ការត្រួតពិនិត្យនេះធានាថាការកំណត់ Foundry Local របស់អ្នករួចរាល់សម្រាប់សិក្ខាសាលាកម្រិតខ្ពស់នៅ សម័យទី 2-6។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាតំបន់របស់វាគួរត្រូវបានចាត់ទុកថាជា ប្រភពផ្លូវការ។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយមនុស្សជំនាញគឺត្រូវបានផ្ដល់អាទិភាព។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបម្លែងការបកប្រែដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->