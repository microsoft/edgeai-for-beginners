<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-12T01:02:26+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "et"
}
-->
# Sessioon 1: Alustamine Foundry Localiga

## Kokkuvõte

Õpi paigaldama, seadistama ja käivitama oma esimesi AI-mudeleid, kasutades Microsoft Foundry Locali. See praktiline sessioon pakub samm-sammulist juhendit lokaalse inferentsi kohta, alates paigaldamisest kuni esimese vestlusrakenduse loomiseni, kasutades mudeleid nagu Phi-4, Qwen ja DeepSeek.

## Õpieesmärgid

Sessiooni lõpuks oskad:

- **Paigaldada ja seadistada**: Seadista Foundry Local ja kontrolli paigaldamise õigsust
- **Valdada CLI operatsioone**: Kasuta Foundry Local CLI-d mudelite haldamiseks ja juurutamiseks
- **Käivitada oma esimese mudeli**: Juuruta ja suhtle lokaalse AI-mudeliga
- **Luua vestlusrakenduse**: Koosta lihtne vestlusrakendus, kasutades Foundry Local Python SDK-d
- **Mõista lokaalse AI olemust**: Saada ülevaade lokaalsest inferentsist ja mudelite haldamisest

## Eeltingimused

### Süsteeminõuded

- **Windows**: Windows 11 (22H2 või uuem) VÕI **macOS**: macOS 11+ (piiratud tugi)
- **RAM**: Minimaalselt 8GB, soovitatavalt 16GB+
- **Salvestusruum**: Vähemalt 10GB vaba ruumi mudelite jaoks
- **Python**: Paigaldatud versioon 3.10 või uuem
- **Administraatoriõigused**: Vajalikud paigaldamiseks

### Arenduskeskkond

- Visual Studio Code koos Python laiendusega (soovitatav)
- Juurdepääs käsureale (PowerShell Windowsis, Terminal macOS-is)
- Git repositooriumide kloonimiseks (valikuline)

## Töötuba (30 minutit)

### Samm 1: Foundry Locali paigaldamine (5 minutit)

#### Paigaldamine Windowsis

Paigalda Foundry Local, kasutades Windowsi pakihaldurit:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatiiv: Laadi otse alla [Microsoft Learnist](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Paigaldamine macOS-is (piiratud tugi)

> [!NOTE] 
> macOS-i tugi on hetkel eelvaates. Kontrolli ametlikku dokumentatsiooni, et saada värskeimat infot.

Kui saadaval, paigalda Homebrew abil:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternatiiv macOS-i kasutajatele:**
- Kasuta Windows 11 virtuaalmasinat (Parallels/UTM) ja järgi Windowsi juhiseid
- Käivita konteineris, kui saadaval, ja konfigureeri `FOUNDRY_LOCAL_ENDPOINT`

### Samm 2: Paigaldamise kontrollimine (3 minutit)

Pärast paigaldamist taaskäivita terminal ja kontrolli, kas Foundry Local töötab:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Oodatav väljund peaks näitama versiooni infot ja saadaval olevaid käske.

### Samm 3: Python keskkonna seadistamine (5 minutit)

Loo selle töötoa jaoks eraldi Python keskkond:

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

### Samm 4: Käivita oma esimene mudel (7 minutit)

Nüüd käivitame oma esimese AI-mudeli lokaalselt!

#### Alusta Phi-4 Mini mudeliga (soovitatav esimene mudel)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> See käsk laadib mudeli alla (esmakordsel kasutamisel) ja käivitab Foundry Local teenuse automaatselt.

#### Kontrolli, mis töötab

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Proovi erinevaid mudeleid

Kui phi-4-mini töötab, katseta teisi mudeleid:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Samm 5: Loo oma esimene vestlusrakendus (10 minutit)

Nüüd loome Python rakenduse, mis kasutab just käivitatud mudeleid.

#### Loo vestluse skript

Loo uus fail nimega `my_first_chat.py` (või kasuta etteantud näidist):

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
> **Seotud näited**: Täpsemaks kasutamiseks vaata:
>
> - **Python näidis**: `Workshop/samples/session01/chat_bootstrap.py` - Sisaldab voogesituse vastuseid ja veakäsitlust
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiivne versioon koos detailsete selgitustega

#### Testi oma vestlusrakendust

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatiiv: Kasuta otse etteantud näidiseid

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Või avasta interaktiivset märkmikku
Ava Workshop/notebooks/session01_chat_bootstrap.ipynb VS Code'is

Proovi neid näitevestlusi:

- "Mis on Microsoft Foundry Local?"
- "Loetle 3 eelist AI-mudelite lokaalsel käitamisel"
- "Aita mul mõista edge AI-d"

## Mida oled saavutanud

Palju õnne! Oled edukalt:

1. ✅ **Paigaldanud Foundry Locali** ja kontrollinud selle toimimist
2. ✅ **Käivitanud oma esimese AI-mudeli** (phi-4-mini) lokaalselt
3. ✅ **Testinud erinevaid mudeleid** käsureal
4. ✅ **Loonud vestlusrakenduse**, mis ühendub sinu lokaalse AI-ga
5. ✅ **Kogenud lokaalse AI inferentsi**, ilma pilveteenusteta

## Mis toimus

### Lokaalne AI inferents

- Sinu AI-mudelid töötavad täielikult sinu arvutis
- Andmeid ei saadeta pilve
- Vastused genereeritakse lokaalselt, kasutades sinu CPU/GPU-d
- Privaatsus ja turvalisus on tagatud

### Mudelite haldamine

- `foundry model run` laadib ja käivitab mudeleid
- **FoundryLocalManager SDK** haldab automaatselt teenuse käivitamist ja mudelite laadimist
- Mudelid salvestatakse lokaalselt tulevaseks kasutamiseks
- Mitmeid mudeleid saab alla laadida, kuid tavaliselt töötab korraga üks
- Teenus haldab automaatselt mudelite elutsüklit

### SDK vs CLI lähenemised

- **CLI lähenemine**: Mudelite käsitsi haldamine `foundry model run <model>` abil
- **SDK lähenemine**: Automaatne teenuse ja mudelite haldamine `FoundryLocalManager(alias)` abil
- **Soovitus**: Kasuta SDK-d rakenduste jaoks, CLI-d testimiseks ja uurimiseks

## Oluliste käskude viide

### Põhilised CLI käsud

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

### Mudelisoovitused

- **phi-4-mini**: Parim algusmudel - kiire, kerge, hea kvaliteet
- **qwen2.5-0.5b**: Kiireim inferents, minimaalne mälukasutus
- **gpt-oss-20b**: Kõrgema kvaliteediga vastused, vajab rohkem ressursse
- **deepseek-coder-1.3b**: Optimeeritud programmeerimise ja koodiga seotud ülesannete jaoks

## Tõrkeotsing

### "Foundry käsku ei leitud"

**Lahendus:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Mudel ei laaditud"

**Lahendus:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Ühendus localhostiga keelatud"

**Lahendus:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Järgmised sammud

### Kohesed tegevused

1. **Katseta** erinevaid mudeleid ja küsimusi
2. **Muuda** oma vestlusrakendust, et proovida erinevaid mudeleid
3. **Loo** oma küsimused ja testi vastuseid
4. **Uuri** Sessiooni 2: RAG rakenduste loomine

### Täiustatud õppeprogramm

1. **Sessioon 2**: AI lahenduste loomine RAG-ga (Retrieval-Augmented Generation)
2. **Sessioon 3**: Erinevate avatud lähtekoodiga mudelite võrdlemine
3. **Sessioon 4**: Töötamine tipptasemel mudelitega
4. **Sessioon 5**: Multi-agent AI süsteemide loomine

## Keskkonnamuutujad (valikuline)

Täpsemaks kasutamiseks saad määrata järgmised keskkonnamuutujad:

| Muutuja | Eesmärk | Näide |
|---------|---------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Vaikimisi kasutatav mudel | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Ülekirjutatud endpoint URL | `http://localhost:5273/v1` |

Loo `.env` fail oma projekti kausta:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Lisamaterjalid

### Dokumentatsioon

- [Foundry Local Python SDK viide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local paigaldusjuhend](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Mudelikataloog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Näidiskood

- **Sessioon01 Python näidis**: `Workshop/samples/session01/chat_bootstrap.py` - Täielik vestlusrakendus voogesitusega
- **Sessioon01 märkmik**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiivne õpetus  
- [Moodul08 Näidis 01](../Module08/samples/01/README.md) - REST vestluse kiirjuhend
- [Moodul08 Näidis 02](../Module08/samples/02/README.md) - OpenAI SDK integratsioon
- [Moodul08 Näidis 03](../Module08/samples/03/README.md) - Mudelite avastamine ja võrdlemine

### Kogukond

- [Foundry Local GitHub arutelud](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI kogukond](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sessiooni kestus**: 30 minutit praktilist tööd + 15 minutit küsimusi ja vastuseid  
**Raskusaste**: Algaja  
**Eeltingimused**: Windows 11/macOS 11+, Python 3.10+, Administraatoriõigused

## Töötuba: Näidissituatsioon

### Reaalne kontekst

**Situatsioon**: Ettevõtte IT-tiim peab hindama seadmesisese AI-inferentsi kasutamist tundliku töötajate tagasiside töötlemiseks, ilma andmeid välisteenustesse saatmata.

**Sinu eesmärk**: Näidata, et lokaalsed AI-mudelid suudavad pakkuda kvaliteetseid vastuseid alla sekundi pikkuse viivitusega, säilitades samal ajal täieliku andmete privaatsuse.

### Testküsimused

Kasuta neid küsimusi, et oma seadistust kontrollida:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Edukuse kriteeriumid

- ✅ Kõigile küsimustele saadakse vastused alla 2 sekundi
- ✅ Ühtegi andmeid ei saadeta sinu arvutist välja
- ✅ Vastused on asjakohased ja kasulikud
- ✅ Sinu vestlusrakendus töötab sujuvalt

See valideerimine kinnitab, et sinu Foundry Local seadistus on valmis edasisteks töötubadeks Sessioonides 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->