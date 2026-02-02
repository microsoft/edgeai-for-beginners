# Session 1: Komma igång med Foundry Local

## Sammanfattning

Lär dig att installera, konfigurera och köra dina första AI-modeller med Microsoft Foundry Local. Denna praktiska session ger en steg-för-steg introduktion till lokal inferens, från installation till att bygga din första chattapplikation med modeller som Phi-4, Qwen och DeepSeek.

## Lärandemål

Efter denna session kommer du att kunna:

- **Installera och konfigurera**: Ställa in Foundry Local med korrekt installationsverifiering
- **Behärska CLI-operationer**: Använda Foundry Local CLI för modellhantering och distribution
- **Köra din första modell**: Framgångsrikt distribuera och interagera med en lokal AI-modell
- **Bygga en chattapplikation**: Skapa en grundläggande chattapplikation med Foundry Local Python SDK
- **Förstå lokal AI**: Få en grundläggande förståelse för lokal inferens och modellhantering

## Förkunskapskrav

### Systemkrav

- **Windows**: Windows 11 (22H2 eller senare) ELLER **macOS**: macOS 11+ (begränsat stöd)
- **RAM**: Minst 8GB, rekommenderat 16GB+
- **Lagring**: Minst 10GB ledigt utrymme för modeller
- **Python**: Version 3.10 eller senare installerad
- **Adminåtkomst**: Administratörsbehörighet för installation

### Utvecklingsmiljö

- Visual Studio Code med Python-tillägg (rekommenderas)
- Kommandoradsåtkomst (PowerShell på Windows, Terminal på macOS)
- Git för att klona repositories (valfritt)

## Workshopflöde (30 minuter)

### Steg 1: Installera Foundry Local (5 minuter)

#### Installation på Windows

Installera Foundry Local med Windows paketmanager:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativ: Ladda ner direkt från [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Installation på macOS (begränsat stöd)

> [!NOTE] 
> macOS-stöd är för närvarande i förhandsgranskning. Kontrollera officiell dokumentation för senaste tillgänglighet.

Om tillgängligt, installera med Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativ för macOS-användare:**
- Använd en Windows 11 VM (Parallels/UTM) och följ Windows-stegen
- Kör via container om tillgängligt och konfigurera `FOUNDRY_LOCAL_ENDPOINT`

### Steg 2: Verifiera installationen (3 minuter)

Efter installationen, starta om din terminal och verifiera att Foundry Local fungerar:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Förväntad output bör visa versionsinformation och tillgängliga kommandon.

### Steg 3: Ställ in Python-miljö (5 minuter)

Skapa en dedikerad Python-miljö för denna workshop:

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

### Steg 4: Kör din första modell (7 minuter)

Nu ska vi köra vår första AI-modell lokalt!

#### Börja med Phi-4 Mini (Rekommenderad första modell)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Detta kommando laddar ner modellen (första gången) och startar automatiskt Foundry Local-tjänsten.

#### Kontrollera vad som körs

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Testa olika modeller

När phi-4-mini fungerar, experimentera med andra modeller:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Steg 5: Bygg din första chattapplikation (10 minuter)

Nu ska vi skapa en Python-applikation som använder de modeller vi just startade.

#### Skapa chattskriptet

Skapa en ny fil som heter `my_first_chat.py` (eller använd det medföljande exemplet):

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
> **Relaterade exempel**: För mer avancerad användning, se:
>
> - **Python-exempel**: `Workshop/samples/session01/chat_bootstrap.py` - Inkluderar strömmande svar och felhantering
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiv version med detaljerade förklaringar

#### Testa din chattapplikation

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativ: Använd de medföljande exemplen direkt

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Eller utforska den interaktiva notebooken
Öppna Workshop/notebooks/session01_chat_bootstrap.ipynb i VS Code

Testa dessa exempelkonversationer:

- "Vad är Microsoft Foundry Local?"
- "Lista 3 fördelar med att köra AI-modeller lokalt"
- "Hjälp mig förstå edge AI"

## Vad du har åstadkommit

Grattis! Du har framgångsrikt:

1. ✅ **Installerat Foundry Local** och verifierat att det fungerar
2. ✅ **Startat din första AI-modell** (phi-4-mini) lokalt
3. ✅ **Testat olika modeller** via kommandoraden
4. ✅ **Byggt en chattapplikation** som ansluter till din lokala AI
5. ✅ **Upplevt lokal AI-inferens** utan molnberoenden

## Förstå vad som hände

### Lokal AI-inferens

- Dina AI-modeller körs helt på din dator
- Ingen data skickas till molnet
- Svar genereras lokalt med din CPU/GPU
- Integritet och säkerhet upprätthålls

### Modellhantering

- `foundry model run` laddar ner och startar modeller
- **FoundryLocalManager SDK** hanterar automatiskt tjänststart och modellinläsning
- Modeller cachas lokalt för framtida användning
- Flera modeller kan laddas ner, men vanligtvis körs en åt gången
- Tjänsten hanterar automatiskt modellens livscykel

### SDK vs CLI-metoder

- **CLI-metod**: Manuell modellhantering med `foundry model run <model>`
- **SDK-metod**: Automatisk tjänst + modellhantering med `FoundryLocalManager(alias)`
- **Rekommendation**: Använd SDK för applikationer, CLI för testning och utforskning

## Referens för vanliga kommandon

### Viktiga CLI-kommandon

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

### Modellrekommendationer

- **phi-4-mini**: Bästa startmodellen - snabb, lättviktig, bra kvalitet
- **qwen2.5-0.5b**: Snabbaste inferensen, minimal minnesanvändning
- **gpt-oss-20b**: Högre kvalitet på svar, kräver mer resurser
- **deepseek-coder-1.3b**: Optimerad för programmering och koduppgifter

## Felsökning

### "Foundry command not found"

**Lösning:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model failed to load"

**Lösning:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connection refused on localhost"

**Lösning:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Nästa steg

### Omedelbara nästa åtgärder

1. **Experimentera** med olika modeller och frågor
2. **Modifiera** din chattapplikation för att testa olika modeller
3. **Skapa** egna frågor och testa svar
4. **Utforska** Session 2: Bygga RAG-applikationer

### Avancerad lärväg

1. **Session 2**: Bygg AI-lösningar med RAG (Retrieval-Augmented Generation)
2. **Session 3**: Jämför olika open-source-modeller
3. **Session 4**: Arbeta med de senaste modellerna
4. **Session 5**: Bygg multi-agent AI-system

## Miljövariabler (valfritt)

För mer avancerad användning kan du ställa in dessa miljövariabler:

| Variabel | Syfte | Exempel |
|----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Standardmodell att använda | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Åsidosätt URL för endpoint | `http://localhost:5273/v1` |

Skapa en `.env`-fil i din projektmapp:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Ytterligare resurser

### Dokumentation

- [Foundry Local Python SDK Referens](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installationsguide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modellkatalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Exempelkod

- **Session01 Python-exempel**: `Workshop/samples/session01/chat_bootstrap.py` - Komplett chattapp med strömning
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiv handledning  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Snabbstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](../Module08/samples/03/README.md) - Modellupptäckt & Benchmarking

### Community

- [Foundry Local GitHub Diskussioner](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sessionens längd**: 30 minuter praktiskt arbete + 15 minuter Q&A  
**Svårighetsnivå**: Nybörjare  
**Förkunskapskrav**: Windows 11/macOS 11+, Python 3.10+, Adminåtkomst

## Workshop Exempelscenario

### Verklig kontext

**Scenario**: Ett företags IT-team behöver utvärdera AI-inferens på enheten för att bearbeta känslig feedback från anställda utan att skicka data till externa tjänster.

**Ditt mål**: Visa att lokala AI-modeller kan ge kvalitativa svar med sub-sekund latens samtidigt som fullständig dataintegritet upprätthålls.

### Testfrågor

Använd dessa frågor för att validera din installation:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Framgångskriterier

- ✅ Alla frågor får svar inom 2 sekunder
- ✅ Ingen data lämnar din lokala maskin
- ✅ Svaren är relevanta och hjälpsamma
- ✅ Din chattapplikation fungerar smidigt

Denna validering säkerställer att din Foundry Local-installation är redo för de avancerade workshops i Sessionerna 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->