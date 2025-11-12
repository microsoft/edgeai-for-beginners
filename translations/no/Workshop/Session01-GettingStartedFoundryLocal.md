<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T23:21:32+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "no"
}
-->
# Sesjon 1: Kom i gang med Foundry Local

## Sammendrag

Lær å installere, konfigurere og kjøre dine første AI-modeller ved hjelp av Microsoft Foundry Local. Denne praktiske sesjonen gir en trinnvis introduksjon til lokal inferens, fra installasjon til å bygge din første chat-applikasjon med modeller som Phi-4, Qwen og DeepSeek.

## Læringsmål

Ved slutten av denne sesjonen vil du:

- **Installere og konfigurere**: Sette opp Foundry Local med riktig installasjonsverifisering
- **Beherske CLI-operasjoner**: Bruke Foundry Local CLI for modelladministrasjon og distribusjon
- **Kjøre din første modell**: Lykkes med å distribuere og interagere med en lokal AI-modell
- **Bygge en chat-applikasjon**: Lage en enkel chat-applikasjon ved hjelp av Foundry Local Python SDK
- **Forstå lokal AI**: Få grunnleggende forståelse av lokal inferens og modelladministrasjon

## Forutsetninger

### Systemkrav

- **Windows**: Windows 11 (22H2 eller nyere) ELLER **macOS**: macOS 11+ (begrenset støtte)
- **RAM**: Minimum 8GB, anbefalt 16GB+
- **Lagring**: 10GB+ ledig plass for modeller
- **Python**: 3.10 eller nyere installert
- **Admin-tilgang**: Administratorrettigheter for installasjon

### Utviklingsmiljø

- Visual Studio Code med Python-utvidelse (anbefalt)
- Kommandolinjetilgang (PowerShell på Windows, Terminal på macOS)
- Git for kloning av repositorier (valgfritt)

## Workshop-flyt (30 minutter)

### Steg 1: Installer Foundry Local (5 minutter)

#### Windows-installasjon

Installer Foundry Local ved hjelp av Windows-pakkebehandler:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativ: Last ned direkte fra [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### macOS-installasjon (begrenset støtte)

> [!NOTE] 
> macOS-støtte er for øyeblikket i forhåndsvisning. Sjekk offisiell dokumentasjon for siste oppdateringer.

Hvis tilgjengelig, installer med Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativ for macOS-brukere:**
- Bruk en Windows 11 VM (Parallels/UTM) og følg Windows-trinnene
- Kjør via container hvis tilgjengelig og konfigurer `FOUNDRY_LOCAL_ENDPOINT`

### Steg 2: Verifiser installasjon (3 minutter)

Etter installasjon, start terminalen på nytt og verifiser at Foundry Local fungerer:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Forventet utdata skal vise versjonsinformasjon og tilgjengelige kommandoer.

### Steg 3: Sett opp Python-miljø (5 minutter)

Opprett et dedikert Python-miljø for denne workshopen:

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

### Steg 4: Kjør din første modell (7 minutter)

La oss nå kjøre vår første AI-modell lokalt!

#### Start med Phi-4 Mini (anbefalt første modell)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Denne kommandoen laster ned modellen (første gang) og starter Foundry Local-tjenesten automatisk.

#### Sjekk hva som kjører

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Prøv forskjellige modeller

Når phi-4-mini fungerer, kan du eksperimentere med andre modeller:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Steg 5: Bygg din første chat-applikasjon (10 minutter)

La oss nå lage en Python-applikasjon som bruker modellene vi nettopp startet.

#### Lag chat-skriptet

Opprett en ny fil kalt `my_first_chat.py` (eller bruk den medfølgende eksempelfilen):

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
> **Relaterte eksempler**: For mer avansert bruk, se:
>
> - **Python-eksempel**: `Workshop/samples/session01/chat_bootstrap.py` - Inkluderer streaming-responser og feilhåndtering
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiv versjon med detaljerte forklaringer

#### Test din chat-applikasjon

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativ: Bruk de medfølgende eksemplene direkte

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Eller utforsk den interaktive notebooken
Åpne Workshop/notebooks/session01_chat_bootstrap.ipynb i VS Code

Prøv disse eksempelsamtalene:

- "Hva er Microsoft Foundry Local?"
- "List opp 3 fordeler med å kjøre AI-modeller lokalt"
- "Hjelp meg å forstå edge AI"

## Hva du har oppnådd

Gratulerer! Du har med suksess:

1. ✅ **Installert Foundry Local** og verifisert at det fungerer
2. ✅ **Startet din første AI-modell** (phi-4-mini) lokalt
3. ✅ **Testet forskjellige modeller** via kommandolinjen
4. ✅ **Bygget en chat-applikasjon** som kobler til din lokale AI
5. ✅ **Opplevd lokal AI-inferens** uten avhengighet til skyen

## Forstå hva som skjedde

### Lokal AI-inferens

- Dine AI-modeller kjører helt på din egen datamaskin
- Ingen data sendes til skyen
- Responser genereres lokalt ved hjelp av din CPU/GPU
- Personvern og sikkerhet opprettholdes

### Modelladministrasjon

- `foundry model run` laster ned og starter modeller
- **FoundryLocalManager SDK** håndterer automatisk tjenestestart og modelllasting
- Modeller lagres lokalt for fremtidig bruk
- Flere modeller kan lastes ned, men vanligvis kjører én om gangen
- Tjenesten administrerer automatisk modellens livssyklus

### SDK vs CLI-tilnærminger

- **CLI-tilnærming**: Manuell modelladministrasjon med `foundry model run <model>`
- **SDK-tilnærming**: Automatisk tjeneste- og modelladministrasjon med `FoundryLocalManager(alias)`
- **Anbefaling**: Bruk SDK for applikasjoner, CLI for testing og utforskning

## Referanse for vanlige kommandoer

### Essensielle CLI-kommandoer

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

### Modellanbefalinger

- **phi-4-mini**: Beste startmodell - rask, lettvekt, god kvalitet
- **qwen2.5-0.5b**: Raskest inferens, minimal minnebruk
- **gpt-oss-20b**: Høyere kvalitet på responser, krever mer ressurser
- **deepseek-coder-1.3b**: Optimalisert for programmering og kodeoppgaver

## Feilsøking

### "Foundry command not found"

**Løsning:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model failed to load"

**Løsning:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connection refused on localhost"

**Løsning:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Neste steg

### Umiddelbare neste handlinger

1. **Eksperimenter** med forskjellige modeller og spørsmål
2. **Modifiser** din chat-applikasjon for å prøve forskjellige modeller
3. **Lag** dine egne spørsmål og test responser
4. **Utforsk** Sesjon 2: Bygg RAG-applikasjoner

### Avansert læringsvei

1. **Sesjon 2**: Bygg AI-løsninger med RAG (Retrieval-Augmented Generation)
2. **Sesjon 3**: Sammenlign forskjellige open-source modeller
3. **Sesjon 4**: Arbeid med banebrytende modeller
4. **Sesjon 5**: Bygg multi-agent AI-systemer

## Miljøvariabler (valgfritt)

For mer avansert bruk kan du sette disse miljøvariablene:

| Variabel | Formål | Eksempel |
|----------|--------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Standardmodell som skal brukes | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Overstyr endepunkt-URL | `http://localhost:5273/v1` |

Opprett en `.env`-fil i prosjektmappen din:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Tilleggsressurser

### Dokumentasjon

- [Foundry Local Python SDK Referanse](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installasjonsveiledning](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modellkatalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Eksempelkode

- **Session01 Python-eksempel**: `Workshop/samples/session01/chat_bootstrap.py` - Komplett chat-app med streaming
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiv veiledning  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK-integrasjon
- [Module08 Sample 03](../Module08/samples/03/README.md) - Modelloppdagelse og benchmarking

### Felleskap

- [Foundry Local GitHub Diskusjoner](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Varighet på sesjonen**: 30 minutter praktisk + 15 minutter Q&A  
**Vanskelighetsgrad**: Nybegynner  
**Forutsetninger**: Windows 11/macOS 11+, Python 3.10+, Admin-tilgang

## Workshop Eksempelscenario

### Virkelighetsnær kontekst

**Scenario**: Et IT-team i en bedrift trenger å evaluere AI-inferens på enheten for å behandle sensitiv tilbakemelding fra ansatte uten å sende data til eksterne tjenester.

**Ditt mål**: Demonstrere at lokale AI-modeller kan gi kvalitetsresponser med sub-sekund latens samtidig som fullstendig databeskyttelse opprettholdes.

### Testspørsmål

Bruk disse spørsmålene for å validere oppsettet ditt:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Suksesskriterier

- ✅ Alle spørsmål får svar på under 2 sekunder
- ✅ Ingen data forlater din lokale maskin
- ✅ Responser er relevante og nyttige
- ✅ Din chat-applikasjon fungerer problemfritt

Denne valideringen sikrer at ditt Foundry Local-oppsett er klart for de avanserte workshopene i Sesjonene 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->