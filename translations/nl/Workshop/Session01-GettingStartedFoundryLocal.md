<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:23:01+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "nl"
}
-->
# Sessie 1: Aan de slag met Foundry Local

## Samenvatting

Begin je reis met Foundry Local door het te installeren en configureren op Windows 11. Leer hoe je de CLI instelt, hardwareversnelling inschakelt en modellen cachet voor snelle lokale inferentie. Deze praktische sessie laat zien hoe je modellen zoals Phi, Qwen, DeepSeek en GPT-OSS-20B uitvoert met reproduceerbare CLI-commando's.

## Leerdoelen

Aan het einde van deze sessie kun je:

- **Installeren en Configureren**: Foundry Local instellen op Windows 11 met optimale prestatie-instellingen
- **CLI Operaties Beheersen**: Foundry Local CLI gebruiken voor modelbeheer en implementatie
- **Hardwareversnelling Inschakelen**: GPU-versnelling configureren met ONNXRuntime of WebGPU
- **Meerdere Modellen Implementeren**: Modellen zoals phi-4, GPT-OSS-20B, Qwen en DeepSeek lokaal uitvoeren
- **Je Eerste App Bouwen**: Bestaande voorbeelden aanpassen om de Foundry Local Python SDK te gebruiken

# Test het model (niet-interactieve enkele prompt)
foundry model run phi-4-mini --prompt "Hallo, stel jezelf voor"

- Windows 11 (22H2 of later)
# Beschikbare catalogusmodellen weergeven (geladen modellen verschijnen na uitvoering)
foundry model list
## NOTE: Er is momenteel geen speciale `--running` vlag; om te zien welke geladen zijn, start een chat of inspecteer de servicelogboeken.
- Python 3.10+ geïnstalleerd
- Visual Studio Code met Python-extensie
- Beheerdersrechten voor installatie

### (Optioneel) Omgevingsvariabelen

Maak een `.env` (of stel in shell) om scripts draagbaar te maken:
# Vergelijk antwoorden (niet-interactief)
foundry model run gpt-oss-20b --prompt "Leg edge AI uit in eenvoudige termen"
| Variabele | Doel | Voorbeeld |
|-----------|------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Voorkeursmodelalias (catalogus selecteert automatisch de beste variant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Endpoint overschrijven (anders automatisch van manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Streamingdemo inschakelen | `true` |

> Als `FOUNDRY_LOCAL_ENDPOINT=auto` (of niet ingesteld) wordt dit afgeleid van de SDK-manager.

## Demo Flow (30 minuten)

### 1. Foundry Local installeren en CLI-instelling verifiëren (10 minuten)

# Cachemodellen weergeven
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Preview / Indien Ondersteund)**

Als een native macOS-pakket beschikbaar is (controleer officiële documentatie voor de nieuwste versie):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Als native macOS-binaries nog niet beschikbaar zijn, kun je alsnog: 
1. Een Windows 11 ARM/Intel VM gebruiken (Parallels / UTM) en de Windows-stappen volgen. 
2. Modellen uitvoeren via een container (indien containerafbeelding gepubliceerd) en `FOUNDRY_LOCAL_ENDPOINT` instellen op de blootgestelde poort. 

**Python Virtuele Omgeving Maken (Platformonafhankelijk)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade pip en installeer kernafhankelijkheden:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Stap 1.2: Installatie Verifiëren

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Stap 1.3: Omgeving Configureren

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Aanbevolen)

In plaats van de service handmatig te starten en modellen uit te voeren, kan de **Foundry Local Python SDK** alles bootstrappen:

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

Als je liever expliciete controle hebt, kun je nog steeds de CLI + OpenAI-client gebruiken zoals later wordt getoond.

### 2. Modellen Lokaal Uitvoeren via CLI (10 minuten)

#### Stap 3.1: Phi-4 Model Implementeren

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Stap 3.2: GPT-OSS-20B Implementeren

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Stap 3.3: Extra Modellen Laden

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Starter Project: Pas 01-run-phi aan voor Foundry Local (5 minuten)

#### Stap 4.1: Basis Chatapplicatie Maken

Maak `samples/01-foundry-quickstart/chat_quickstart.py` (bijgewerkt om de manager te gebruiken indien beschikbaar):

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

#### Stap 4.2: Test de Applicatie

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Belangrijke Concepten

### 1. Foundry Local Architectuur

- **Lokale Inferentie-Engine**: Voert modellen volledig op je apparaat uit
- **OpenAI SDK Compatibiliteit**: Naadloze integratie met bestaande OpenAI-code
- **Modelbeheer**: Download, cache en voer meerdere modellen efficiënt uit
- **Hardwareoptimalisatie**: Maak gebruik van GPU-, NPU- en CPU-versnelling

### 2. CLI Commandoreferentie

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK Integratie

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

## Veelvoorkomende Problemen Oplossen

### Probleem 1: "Foundry command not found"

**Oplossing:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Probleem 2: "Model failed to load"

**Oplossing:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Probleem 3: "Connection refused on localhost:5273"

**Oplossing:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tips voor Prestatieoptimalisatie

### 1. Modelselectiestrategie

- **Phi-4-mini**: Beste voor algemene taken, laag geheugengebruik
- **Qwen2.5-0.5b**: Snelste inferentie, minimale middelen
- **GPT-OSS-20B**: Hoogste kwaliteit, vereist meer middelen
- **DeepSeek-Coder**: Geoptimaliseerd voor programmeertaken

### 2. Hardwareoptimalisatie

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Prestaties Monitoren

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

### Optionele Verbeteringen

| Verbetering | Wat | Hoe |
|-------------|-----|-----|
| Gedeelde Hulpprogramma's | Verwijder dubbele client/bootstrap-logica | Gebruik `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Zichtbaarheid Tokengebruik | Leer kosten/efficiëntie vroeg | Stel `SHOW_USAGE=1` in om prompt/completion/totaal tokens af te drukken |
| Deterministische Vergelijkingen | Stabiele benchmarking & regressiecontroles | Gebruik `temperature=0`, `top_p=1`, consistente prompttekst |
| Eerste-Token Latentie | Waargenomen responsiviteitsmetriek | Pas benchmarkscript aan met streaming (`BENCH_STREAM=1`) |
| Herhalen bij Tijdelijke Fouten | Veerkrachtige demo's bij koude start | `RETRY_ON_FAIL=1` (standaard) & pas `RETRY_BACKOFF` aan |
| Smoke Testing | Snelle controle over belangrijke flows | Voer `python Workshop/tests/smoke.py` uit vóór een workshop |
| Modelalias Profielen | Snel schakelen tussen machines | Behoud `.env` met `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Cache-efficiëntie | Vermijd herhaalde opwarmingen in multi-sample run | Hulpprogramma's cachemanagers; hergebruik tussen scripts/notebooks |
| Eerste Run Opwarming | Verminder p95 latentiepieken | Voer een kleine prompt uit na `FoundryLocalManager` creatie |

Voorbeeld deterministische warme basislijn (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Je zou vergelijkbare output en identieke tokenaantallen moeten zien bij de tweede run, wat determinisme bevestigt.

## Volgende Stappen

Na het voltooien van deze sessie:

1. **Verken Sessie 2**: Bouw AI-oplossingen met Azure AI Foundry RAG
2. **Probeer Verschillende Modellen**: Experimenteer met Qwen, DeepSeek en andere modelfamilies
3. **Optimaliseer Prestaties**: Pas instellingen aan voor jouw specifieke hardware
4. **Bouw Eigen Applicaties**: Gebruik de Foundry Local SDK in je eigen projecten

## Aanvullende Bronnen

### Documentatie
- [Foundry Local Python SDK Referentie](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installatiehandleiding](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modelcatalogus](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Voorbeeldcode
- [Module08 Voorbeeld 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Voorbeeld 02](./samples/02/README.md) - OpenAI SDK Integratie
- [Module08 Voorbeeld 03](./samples/03/README.md) - Modelontdekking & Benchmarking

### Community
- [Foundry Local GitHub Discussies](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sessieduur**: 30 minuten hands-on + 15 minuten Q&A  
**Moeilijkheidsgraad**: Beginner  
**Vereisten**: Windows 11, Python 3.10+, Beheerdersrechten  

## Voorbeeldscenario & Workshop Mapping

| Workshop Script / Notebook | Scenario | Doel | Voorbeeldinput(s) | Nodige Dataset |
|----------------------------|----------|------|-------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Intern IT-team evalueert on-device inferentie voor een privacy-assessmentportaal | Bewijs dat lokale SLM binnen sub-seconde latentie reageert op standaardprompts | "Noem twee voordelen van lokale inferentie." | Geen (enkele prompt) |
| Quickstart aanpassingscodeblok | Ontwikkelaar migreert een bestaande OpenAI-script naar Foundry Local | Toon drop-in compatibiliteit | "Noem twee voordelen van lokale inferentie." | Alleen inline prompt |

### Scenarioverhaal
Het beveiligings- en compliance-team moet valideren of gevoelige prototypegegevens lokaal kunnen worden verwerkt. Ze voeren het bootstrap-script uit met verschillende prompts (privacy, latentie, kosten) met een deterministische temperatuur=0 modus om basisuitvoer vast te leggen voor latere vergelijking (Sessie 3 benchmarking en Sessie 4 SLM vs LLM contrast).

### Minimale Prompt Set JSON (optioneel)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Gebruik deze lijst om een reproduceerbare evaluatielus te maken of om een toekomstige regressietestharnas te voeden.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.