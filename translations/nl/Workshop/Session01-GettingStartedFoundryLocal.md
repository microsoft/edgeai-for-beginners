<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T23:31:05+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "nl"
}
-->
# Sessie 1: Aan de slag met Foundry Local

## Samenvatting

Leer hoe je je eerste AI-modellen installeert, configureert en uitvoert met Microsoft Foundry Local. Deze praktische sessie biedt een stapsgewijze introductie tot lokale inferentie, van installatie tot het bouwen van je eerste chatapplicatie met modellen zoals Phi-4, Qwen en DeepSeek.

## Leerdoelen

Aan het einde van deze sessie kun je:

- **Installeren en configureren**: Foundry Local instellen en de installatie verifiëren
- **Beheersen van CLI-operaties**: Foundry Local CLI gebruiken voor modelbeheer en implementatie
- **Je eerste model uitvoeren**: Een lokaal AI-model succesvol implementeren en ermee interageren
- **Een chatapp bouwen**: Een eenvoudige chatapplicatie maken met de Foundry Local Python SDK
- **Lokale AI begrijpen**: De basisprincipes van lokale inferentie en modelbeheer begrijpen

## Vereisten

### Systeemvereisten

- **Windows**: Windows 11 (22H2 of later) OF **macOS**: macOS 11+ (beperkte ondersteuning)
- **RAM**: Minimaal 8GB, aanbevolen 16GB+
- **Opslag**: Minimaal 10GB vrije ruimte voor modellen
- **Python**: Versie 3.10 of later geïnstalleerd
- **Beheerdersrechten**: Vereist voor installatie

### Ontwikkelomgeving

- Visual Studio Code met Python-extensie (aanbevolen)
- Toegang tot de commandoregel (PowerShell op Windows, Terminal op macOS)
- Git voor het klonen van repositories (optioneel)

## Workshopverloop (30 minuten)

### Stap 1: Foundry Local installeren (5 minuten)

#### Installatie op Windows

Installeer Foundry Local met de Windows package manager:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatief: Download direct van [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Installatie op macOS (Beperkte ondersteuning)

> [!NOTE] 
> Ondersteuning voor macOS is momenteel in preview. Raadpleeg de officiële documentatie voor de meest recente beschikbaarheid.

Indien beschikbaar, installeer via Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternatief voor macOS-gebruikers:**
- Gebruik een Windows 11 VM (Parallels/UTM) en volg de stappen voor Windows
- Voer uit via een container indien beschikbaar en configureer `FOUNDRY_LOCAL_ENDPOINT`

### Stap 2: Installatie verifiëren (3 minuten)

Na installatie, herstart je terminal en controleer of Foundry Local werkt:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

De verwachte uitvoer moet versie-informatie en beschikbare commando's tonen.

### Stap 3: Python-omgeving instellen (5 minuten)

Maak een speciale Python-omgeving voor deze workshop:

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

### Stap 4: Je eerste model uitvoeren (7 minuten)

Laten we nu ons eerste AI-model lokaal uitvoeren!

#### Begin met Phi-4 Mini (Aanbevolen eerste model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Dit commando downloadt het model (eerste keer) en start automatisch de Foundry Local-service.

#### Controleer wat er draait

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Probeer verschillende modellen

Zodra phi-4-mini werkt, kun je experimenteren met andere modellen:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Stap 5: Je eerste chatapplicatie bouwen (10 minuten)

Laten we nu een Python-applicatie maken die gebruikmaakt van de modellen die we zojuist hebben gestart.

#### Maak het chatscript

Maak een nieuw bestand genaamd `my_first_chat.py` (of gebruik het meegeleverde voorbeeld):

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
> **Gerelateerde voorbeelden**: Voor meer geavanceerd gebruik, zie:
>
> - **Python Voorbeeld**: `Workshop/samples/session01/chat_bootstrap.py` - Inclusief streamingreacties en foutafhandeling
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interactieve versie met gedetailleerde uitleg

#### Test je chatapplicatie

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatief: Gebruik direct de meegeleverde voorbeelden

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Of verken de interactieve notebook  
Open Workshop/notebooks/session01_chat_bootstrap.ipynb in VS Code

Probeer deze voorbeeldgesprekken:

- "Wat is Microsoft Foundry Local?"
- "Noem 3 voordelen van het lokaal uitvoeren van AI-modellen"
- "Help me edge AI te begrijpen"

## Wat je hebt bereikt

Gefeliciteerd! Je hebt succesvol:

1. ✅ **Foundry Local geïnstalleerd** en gecontroleerd of het werkt
2. ✅ **Je eerste AI-model gestart** (phi-4-mini) lokaal
3. ✅ **Verschillende modellen getest** via de commandoregel
4. ✅ **Een chatapplicatie gebouwd** die verbinding maakt met je lokale AI
5. ✅ **Lokale AI-inferentie ervaren** zonder afhankelijkheid van de cloud

## Begrijpen wat er is gebeurd

### Lokale AI-inferentie

- Je AI-modellen draaien volledig op je eigen computer
- Er wordt geen data naar de cloud gestuurd
- Reacties worden lokaal gegenereerd met je CPU/GPU
- Privacy en beveiliging blijven gewaarborgd

### Modelbeheer

- `foundry model run` downloadt en start modellen
- **FoundryLocalManager SDK** start automatisch de service en laadt modellen
- Modellen worden lokaal gecached voor toekomstig gebruik
- Meerdere modellen kunnen worden gedownload, maar meestal draait er één tegelijk
- De service beheert automatisch de levenscyclus van het model

### SDK versus CLI-benaderingen

- **CLI-benadering**: Handmatig modelbeheer met `foundry model run <model>`
- **SDK-benadering**: Automatische service + modelbeheer met `FoundryLocalManager(alias)`
- **Aanbeveling**: Gebruik SDK voor applicaties, CLI voor testen en verkenning

## Referentie voor veelgebruikte commando's

### Essentiële CLI-commando's

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

### Modelaanbevelingen

- **phi-4-mini**: Beste startmodel - snel, lichtgewicht, goede kwaliteit
- **qwen2.5-0.5b**: Snelste inferentie, minimaal geheugenverbruik
- **gpt-oss-20b**: Hogere kwaliteit reacties, vereist meer middelen
- **deepseek-coder-1.3b**: Geoptimaliseerd voor programmeren en codetaken

## Problemen oplossen

### "Foundry command not found"

**Oplossing:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model failed to load"

**Oplossing:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connection refused on localhost"

**Oplossing:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Volgende stappen

### Directe vervolgstappen

1. **Experimenteer** met verschillende modellen en prompts
2. **Pas aan** je chatapplicatie om verschillende modellen te proberen
3. **Creëer** je eigen prompts en test reacties
4. **Verken** Sessie 2: RAG-applicaties bouwen

### Geavanceerd leerpad

1. **Sessie 2**: AI-oplossingen bouwen met RAG (Retrieval-Augmented Generation)
2. **Sessie 3**: Vergelijk verschillende open-source modellen
3. **Sessie 4**: Werken met geavanceerde modellen
4. **Sessie 5**: Multi-agent AI-systemen bouwen

## Omgevingsvariabelen (Optioneel)

Voor meer geavanceerd gebruik kun je deze omgevingsvariabelen instellen:

| Variabele | Doel | Voorbeeld |
|-----------|------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Standaardmodel om te gebruiken | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Endpoint-URL overschrijven | `http://localhost:5273/v1` |

Maak een `.env`-bestand in je projectmap:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Aanvullende bronnen

### Documentatie

- [Foundry Local Python SDK Referentie](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installatiehandleiding](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modelcatalogus](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Voorbeeldcode

- **Session01 Python Voorbeeld**: `Workshop/samples/session01/chat_bootstrap.py` - Complete chatapp met streaming
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interactieve tutorial  
- [Module08 Voorbeeld 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Voorbeeld 02](../Module08/samples/02/README.md) - OpenAI SDK Integratie
- [Module08 Voorbeeld 03](../Module08/samples/03/README.md) - Modelontdekking & Benchmarking

### Community

- [Foundry Local GitHub Discussies](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Duur van de sessie**: 30 minuten hands-on + 15 minuten Q&A  
**Niveau**: Beginner  
**Vereisten**: Windows 11/macOS 11+, Python 3.10+, Beheerdersrechten

## Workshopvoorbeeldscenario

### Praktijkcontext

**Scenario**: Een IT-team van een bedrijf moet on-device AI-inferentie evalueren om gevoelige feedback van medewerkers te verwerken zonder data naar externe diensten te sturen.

**Jouw doel**: Demonstreer dat lokale AI-modellen kwalitatieve reacties kunnen bieden met een sub-seconde latentie terwijl volledige gegevensprivacy wordt gehandhaafd.

### Testprompts

Gebruik deze prompts om je setup te valideren:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Succescriteria

- ✅ Alle prompts krijgen reacties binnen 2 seconden
- ✅ Er wordt geen data van je lokale machine verzonden
- ✅ Reacties zijn relevant en nuttig
- ✅ Je chatapplicatie werkt soepel

Deze validatie zorgt ervoor dat je Foundry Local setup klaar is voor de geavanceerde workshops in Sessies 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->