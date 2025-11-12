<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T23:17:16+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "da"
}
-->
# Session 1: Kom godt i gang med Foundry Local

## Resumé

Lær at installere, konfigurere og køre dine første AI-modeller ved hjælp af Microsoft Foundry Local. Denne praktiske session giver en trin-for-trin introduktion til lokal inferens, fra installation til opbygning af din første chatapplikation med modeller som Phi-4, Qwen og DeepSeek.

## Læringsmål

Ved afslutningen af denne session vil du:

- **Installere og konfigurere**: Opsætte Foundry Local med korrekt installationsverifikation
- **Beherske CLI-operationer**: Bruge Foundry Local CLI til modelstyring og implementering
- **Køre din første model**: Succesfuldt implementere og interagere med en lokal AI-model
- **Bygge en chatapplikation**: Oprette en grundlæggende chatapplikation ved hjælp af Foundry Local Python SDK
- **Forstå lokal AI**: Få indsigt i grundlæggende lokal inferens og modelstyring

## Forudsætninger

### Systemkrav

- **Windows**: Windows 11 (22H2 eller nyere) ELLER **macOS**: macOS 11+ (begrænset support)
- **RAM**: Minimum 8GB, anbefalet 16GB+
- **Lagring**: 10GB+ ledig plads til modeller
- **Python**: Installeret version 3.10 eller nyere
- **Admin-adgang**: Administratorrettigheder til installation

### Udviklingsmiljø

- Visual Studio Code med Python-udvidelse (anbefalet)
- Kommandolinjeadgang (PowerShell på Windows, Terminal på macOS)
- Git til kloning af repositories (valgfrit)

## Workshop Flow (30 minutter)

### Trin 1: Installer Foundry Local (5 minutter)

#### Installation på Windows

Installer Foundry Local ved hjælp af Windows pakkehåndtering:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativ: Download direkte fra [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Installation på macOS (Begrænset support)

> [!NOTE] 
> macOS-support er i øjeblikket i preview. Tjek den officielle dokumentation for den nyeste tilgængelighed.

Hvis tilgængelig, installer med Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativ for macOS-brugere:**
- Brug en Windows 11 VM (Parallels/UTM) og følg Windows-trinene
- Kør via container, hvis tilgængelig, og konfigurer `FOUNDRY_LOCAL_ENDPOINT`

### Trin 2: Verificer installationen (3 minutter)

Efter installationen skal du genstarte din terminal og verificere, at Foundry Local fungerer:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Forventet output skal vise versionsinformation og tilgængelige kommandoer.

### Trin 3: Opsæt Python-miljø (5 minutter)

Opret et dedikeret Python-miljø til denne workshop:

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

### Trin 4: Kør din første model (7 minutter)

Nu skal vi køre vores første AI-model lokalt!

#### Start med Phi-4 Mini (Anbefalet første model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Denne kommando downloader modellen (første gang) og starter automatisk Foundry Local-tjenesten.

#### Tjek hvad der kører

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Prøv forskellige modeller

Når phi-4-mini fungerer, kan du eksperimentere med andre modeller:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Trin 5: Byg din første chatapplikation (10 minutter)

Nu skal vi oprette en Python-applikation, der bruger de modeller, vi lige har startet.

#### Opret chat-scriptet

Opret en ny fil kaldet `my_first_chat.py` (eller brug det medfølgende eksempel):

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
> **Relaterede eksempler**: For mere avanceret brug, se:
>
> - **Python-eksempel**: `Workshop/samples/session01/chat_bootstrap.py` - Indeholder streaming-svar og fejlhåndtering
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiv version med detaljerede forklaringer

#### Test din chatapplikation

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativ: Brug de medfølgende eksempler direkte

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Eller udforsk den interaktive notebook
Åbn Workshop/notebooks/session01_chat_bootstrap.ipynb i VS Code

Prøv disse eksempelsamtaler:

- "Hvad er Microsoft Foundry Local?"
- "Nævn 3 fordele ved at køre AI-modeller lokalt"
- "Hjælp mig med at forstå edge AI"

## Hvad du har opnået

Tillykke! Du har succesfuldt:

1. ✅ **Installeret Foundry Local** og verificeret, at det fungerer
2. ✅ **Startet din første AI-model** (phi-4-mini) lokalt
3. ✅ **Testet forskellige modeller** via kommandolinjen
4. ✅ **Bygget en chatapplikation**, der forbinder til din lokale AI
5. ✅ **Oplevet lokal AI-inferens** uden afhængighed af cloud

## Forstå hvad der skete

### Lokal AI-inferens

- Dine AI-modeller kører udelukkende på din computer
- Ingen data sendes til skyen
- Svar genereres lokalt ved hjælp af din CPU/GPU
- Privatliv og sikkerhed opretholdes

### Modelstyring

- `foundry model run` downloader og starter modeller
- **FoundryLocalManager SDK** håndterer automatisk tjenestestart og modelloading
- Modeller gemmes lokalt til fremtidig brug
- Flere modeller kan downloades, men typisk kører én ad gangen
- Tjenesten styrer automatisk modellivscyklussen

### SDK vs CLI-metoder

- **CLI-metode**: Manuel modelstyring med `foundry model run <model>`
- **SDK-metode**: Automatisk tjeneste + modelstyring med `FoundryLocalManager(alias)`
- **Anbefaling**: Brug SDK til applikationer, CLI til test og udforskning

## Reference til almindelige kommandoer

### Vigtige CLI-kommandoer

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

### Modelanbefalinger

- **phi-4-mini**: Bedste startmodel - hurtig, letvægts, god kvalitet
- **qwen2.5-0.5b**: Hurtigste inferens, minimal hukommelsesbrug
- **gpt-oss-20b**: Højere kvalitetssvar, kræver flere ressourcer
- **deepseek-coder-1.3b**: Optimeret til programmering og kodningsopgaver

## Fejlfinding

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

## Næste skridt

### Umiddelbare næste handlinger

1. **Eksperimenter** med forskellige modeller og prompts
2. **Modificer** din chatapplikation for at prøve forskellige modeller
3. **Opret** dine egne prompts og test svar
4. **Udforsk** Session 2: Opbygning af RAG-applikationer

### Avanceret læringssti

1. **Session 2**: Byg AI-løsninger med RAG (Retrieval-Augmented Generation)
2. **Session 3**: Sammenlign forskellige open-source modeller
3. **Session 4**: Arbejd med avancerede modeller
4. **Session 5**: Byg multi-agent AI-systemer

## Miljøvariabler (valgfrit)

For mere avanceret brug kan du indstille disse miljøvariabler:

| Variabel | Formål | Eksempel |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Standardmodel at bruge | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Overstyr endpoint-URL | `http://localhost:5273/v1` |

Opret en `.env`-fil i din projektmappe:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Yderligere ressourcer

### Dokumentation

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installationsvejledning](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modelkatalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Eksempelkode

- **Session01 Python-eksempel**: `Workshop/samples/session01/chat_bootstrap.py` - Komplet chatapp med streaming
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiv tutorial  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](../Module08/samples/03/README.md) - Model Discovery & Benchmarking

### Community

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sessionsvarighed**: 30 minutters praktisk arbejde + 15 minutters Q&A  
**Sværhedsgrad**: Begynder  
**Forudsætninger**: Windows 11/macOS 11+, Python 3.10+, Admin-adgang

## Workshop Eksempelscenarie

### Virkelighedsnær kontekst

**Scenarie**: Et IT-team i en virksomhed skal evaluere AI-inferens på enheden for at behandle følsom medarbejderfeedback uden at sende data til eksterne tjenester.

**Dit mål**: Demonstrere, at lokale AI-modeller kan levere kvalitetsbesvarelser med under-sekunds latenstid, samtidig med at fuld databeskyttelse opretholdes.

### Testprompts

Brug disse prompts til at validere din opsætning:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Succeskriterier

- ✅ Alle prompts får svar på under 2 sekunder
- ✅ Ingen data forlader din lokale maskine
- ✅ Svarene er relevante og nyttige
- ✅ Din chatapplikation fungerer problemfrit

Denne validering sikrer, at din Foundry Local-opsætning er klar til de avancerede workshops i Sessioner 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->