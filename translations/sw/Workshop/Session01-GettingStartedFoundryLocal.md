<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T23:58:54+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "sw"
}
-->
# Kipindi cha 1: Kuanza na Foundry Local

## Muhtasari

Jifunze jinsi ya kusakinisha, kusanidi, na kuendesha mifano yako ya AI kwa kutumia Microsoft Foundry Local. Kipindi hiki cha vitendo kinatoa utangulizi wa hatua kwa hatua kuhusu utabiri wa ndani, kuanzia usakinishaji hadi kujenga programu yako ya mazungumzo kwa kutumia mifano kama Phi-4, Qwen, na DeepSeek.

## Malengo ya Kujifunza

Mwisho wa kipindi hiki, utaweza:

- **Kusakinisha na Kusanidi**: Kuanzisha Foundry Local na kuthibitisha usakinishaji sahihi
- **Kumudu Operesheni za CLI**: Kutumia Foundry Local CLI kwa usimamizi wa mifano na uendeshaji
- **Kuendesha Mfano Wako wa Kwanza**: Kufanikisha kuendesha na kuingiliana na mfano wa AI wa ndani
- **Kujenga Programu ya Mazungumzo**: Kuunda programu ya msingi ya mazungumzo kwa kutumia Foundry Local Python SDK
- **Kuelewa AI ya Ndani**: Kuelewa misingi ya utabiri wa ndani na usimamizi wa mifano

## Mahitaji ya Awali

### Mahitaji ya Mfumo

- **Windows**: Windows 11 (22H2 au baadaye) AU **macOS**: macOS 11+ (msaada mdogo)
- **RAM**: Angalau 8GB, inapendekezwa 16GB+
- **Uhifadhi**: Angalau 10GB nafasi ya bure kwa mifano
- **Python**: 3.10 au baadaye imewekwa
- **Ufikiaji wa Msimamizi**: Haki za msimamizi kwa usakinishaji

### Mazingira ya Maendeleo

- Visual Studio Code na kiendelezi cha Python (inapendekezwa)
- Ufikiaji wa mstari wa amri (PowerShell kwenye Windows, Terminal kwenye macOS)
- Git kwa kunakili hifadhi (hiari)

## Mtiririko wa Warsha (Dakika 30)

### Hatua ya 1: Kusakinisha Foundry Local (Dakika 5)

#### Usakinishaji wa Windows

Sakinisha Foundry Local kwa kutumia msimamizi wa kifurushi cha Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Njia mbadala: Pakua moja kwa moja kutoka [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Usakinishaji wa macOS (Msaada Mdogo)

> [!NOTE] 
> Msaada wa macOS kwa sasa uko katika majaribio. Angalia nyaraka rasmi kwa upatikanaji wa hivi karibuni.

Ikiwa inapatikana, sakinisha kwa kutumia Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Njia mbadala kwa watumiaji wa macOS:**
- Tumia Windows 11 VM (Parallels/UTM) na fuata hatua za Windows
- Endesha kupitia kontena ikiwa inapatikana na usanidi `FOUNDRY_LOCAL_ENDPOINT`

### Hatua ya 2: Thibitisha Usakinishaji (Dakika 3)

Baada ya usakinishaji, anzisha tena terminal yako na thibitisha Foundry Local inafanya kazi:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Matokeo yanayotarajiwa yanapaswa kuonyesha taarifa za toleo na amri zinazopatikana.

### Hatua ya 3: Sanidi Mazingira ya Python (Dakika 5)

Unda mazingira maalum ya Python kwa warsha hii:

**Windows:**
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

### Hatua ya 4: Endesha Mfano Wako wa Kwanza (Dakika 7)

Sasa tuendeshe mfano wetu wa kwanza wa AI ndani!

#### Anza na Phi-4 Mini (Mfano wa Kwanza Unaopendekezwa)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Amri hii inapakua mfano (mara ya kwanza) na kuanzisha huduma ya Foundry Local moja kwa moja.

#### Angalia Kinachoendesha

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Jaribu Mifano Tofauti

Mara phi-4-mini inapofanya kazi, jaribu mifano mingine:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Hatua ya 5: Jenga Programu Yako ya Kwanza ya Mazungumzo (Dakika 10)

Sasa tuunde programu ya Python inayotumia mifano tuliyoanzisha.

#### Unda Script ya Mazungumzo

Unda faili mpya inayoitwa `my_first_chat.py` (au tumia sampuli iliyotolewa):

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
> **Mifano Inayohusiana**: Kwa matumizi ya hali ya juu zaidi, angalia:
>
> - **Sampuli ya Python**: `Workshop/samples/session01/chat_bootstrap.py` - Inajumuisha majibu ya mtiririko na utunzaji wa makosa
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Toleo la maingiliano na maelezo ya kina

#### Jaribu Programu Yako ya Mazungumzo

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Njia mbadala: Tumia sampuli zilizotolewa moja kwa moja

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Au chunguza daftari la maingiliano
Fungua Workshop/notebooks/session01_chat_bootstrap.ipynb kwenye VS Code

Jaribu mazungumzo haya ya mfano:

- "Microsoft Foundry Local ni nini?"
- "Taja faida 3 za kuendesha mifano ya AI ndani"
- "Nisaidie kuelewa AI ya ukingo"

## Uliyofanikiwa

Hongera! Umefanikiwa:

1. ✅ **Kusakinisha Foundry Local** na kuthibitisha inafanya kazi
2. ✅ **Kuanzisha mfano wako wa kwanza wa AI** (phi-4-mini) ndani
3. ✅ **Kujaribu mifano tofauti** kupitia mstari wa amri
4. ✅ **Kujenga programu ya mazungumzo** inayounganisha na AI yako ya ndani
5. ✅ **Kujifunza utabiri wa AI wa ndani** bila utegemezi wa wingu

## Kuelewa Kilichotokea

### Utabiri wa AI wa Ndani

- Mifano yako ya AI inaendeshwa kikamilifu kwenye kompyuta yako
- Hakuna data inayotumwa kwenye wingu
- Majibu yanazalishwa ndani kwa kutumia CPU/GPU yako
- Faragha na usalama vinahifadhiwa

### Usimamizi wa Mifano

- `foundry model run` hupakua na kuanzisha mifano
- **FoundryLocalManager SDK** hushughulikia kuanzisha huduma na kupakia mifano moja kwa moja
- Mifano huhifadhiwa ndani kwa matumizi ya baadaye
- Mifano mingi inaweza kupakuliwa lakini kawaida moja huendeshwa kwa wakati mmoja
- Huduma hushughulikia mzunguko wa maisha wa mfano moja kwa moja

### Njia ya SDK vs CLI

- **Njia ya CLI**: Usimamizi wa mifano kwa mikono na `foundry model run <model>`
- **Njia ya SDK**: Huduma ya moja kwa moja + usimamizi wa mifano na `FoundryLocalManager(alias)`
- **Pendekezo**: Tumia SDK kwa programu, CLI kwa majaribio na uchunguzi

## Marejeleo ya Amri za Kawaida

### Amri Muhimu za CLI

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

### Mapendekezo ya Mifano

- **phi-4-mini**: Mfano bora wa kuanza - haraka, mwepesi, ubora mzuri
- **qwen2.5-0.5b**: Utabiri wa haraka zaidi, matumizi madogo ya kumbukumbu
- **gpt-oss-20b**: Majibu ya ubora wa juu, inahitaji rasilimali zaidi
- **deepseek-coder-1.3b**: Imeboreshwa kwa kazi za programu na msimbo

## Utatuzi wa Shida

### "Amri ya Foundry haikupatikana"

**Suluhisho:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Mfano umeshindwa kupakia"

**Suluhisho:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Muunganisho umekataliwa kwenye localhost"

**Suluhisho:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Hatua Zifuatazo

### Hatua za Haraka Zifuatazo

1. **Jaribu** mifano tofauti na maelekezo
2. **Badilisha** programu yako ya mazungumzo ili kujaribu mifano tofauti
3. **Unda** maelekezo yako mwenyewe na jaribu majibu
4. **Chunguza** Kipindi cha 2: Kujenga programu za RAG

### Njia ya Kujifunza ya Juu

1. **Kipindi cha 2**: Jenga suluhisho za AI na RAG (Retrieval-Augmented Generation)
2. **Kipindi cha 3**: Linganisha mifano tofauti ya chanzo huria
3. **Kipindi cha 4**: Fanya kazi na mifano ya kisasa
4. **Kipindi cha 5**: Jenga mifumo ya AI yenye mawakala wengi

## Vigezo vya Mazingira (Hiari)

Kwa matumizi ya hali ya juu zaidi, unaweza kuweka vigezo hivi vya mazingira:

| Kigezo | Kusudi | Mfano |
|--------|--------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Mfano wa chaguo-msingi wa kutumia | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Badilisha URL ya mwisho | `http://localhost:5273/v1` |

Unda faili `.env` kwenye saraka ya mradi wako:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Rasilimali za Ziada

### Nyaraka

- [Rejeleo la Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Mwongozo wa Usakinishaji wa Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Katalogi ya Mifano](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Msimbo wa Sampuli

- **Sampuli ya Python ya Kipindi cha 01**: `Workshop/samples/session01/chat_bootstrap.py` - Programu kamili ya mazungumzo na mtiririko
- **Daftari la Kipindi cha 01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Mafunzo ya maingiliano  
- [Sampuli ya Moduli08 01](../Module08/samples/01/README.md) - Mwanzo wa Haraka wa Mazungumzo ya REST
- [Sampuli ya Moduli08 02](../Module08/samples/02/README.md) - Ushirikiano wa OpenAI SDK
- [Sampuli ya Moduli08 03](../Module08/samples/03/README.md) - Ugunduzi wa Mfano & Upimaji

### Jamii

- [Majadiliano ya Foundry Local GitHub](https://github.com/microsoft/Foundry-Local/discussions)
- [Jamii ya Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Muda wa Kipindi**: Dakika 30 za vitendo + Dakika 15 za Maswali na Majibu  
**Kiwango cha Ugumu**: Mwanzoni  
**Mahitaji ya Awali**: Windows 11/macOS 11+, Python 3.10+, Ufikiaji wa Msimamizi

## Mfano wa Hali ya Warsha

### Muktadha wa Ulimwengu Halisi

**Hali**: Timu ya IT ya shirika inahitaji kutathmini utabiri wa AI kwenye kifaa kwa kuchakata maoni nyeti ya wafanyakazi bila kutuma data kwa huduma za nje.

**Lengo Lako**: Onyesha kwamba mifano ya AI ya ndani inaweza kutoa majibu ya ubora na latency ya chini ya sekunde moja huku ikihifadhi faragha kamili ya data.

### Maelekezo ya Mtihani

Tumia maelekezo haya kuthibitisha usanidi wako:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Vigezo vya Mafanikio

- ✅ Maelekezo yote yanapata majibu chini ya sekunde 2
- ✅ Hakuna data inayotoka kwenye mashine yako ya ndani
- ✅ Majibu ni muhimu na ya msaada
- ✅ Programu yako ya mazungumzo inafanya kazi vizuri

Uthibitisho huu unahakikisha usanidi wako wa Foundry Local uko tayari kwa warsha za hali ya juu katika Vipindi vya 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->