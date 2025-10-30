<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T22:04:29+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "sv"
}
-->
# Session 1: Kom igång med Foundry Local

## Sammanfattning

Starta din resa med Foundry Local genom att installera och konfigurera det på Windows 11. Lär dig att ställa in CLI, aktivera hårdvaruacceleration och cachea modeller för snabb lokal inferens. Denna praktiska session går igenom hur man kör modeller som Phi, Qwen, DeepSeek och GPT-OSS-20B med reproducerbara CLI-kommandon.

## Lärandemål

I slutet av denna session kommer du att kunna:

- **Installera och konfigurera**: Ställa in Foundry Local på Windows 11 med optimala prestandainställningar
- **Behärska CLI-operationer**: Använda Foundry Local CLI för modellhantering och distribution
- **Aktivera hårdvaruacceleration**: Konfigurera GPU-acceleration med ONNXRuntime eller WebGPU
- **Distribuera flera modeller**: Köra phi-4, GPT-OSS-20B, Qwen och DeepSeek-modeller lokalt
- **Bygga din första app**: Anpassa befintliga exempel för att använda Foundry Local Python SDK

# Testa modellen (icke-interaktiv enkel prompt)
foundry model run phi-4-mini --prompt "Hej, presentera dig själv"

- Windows 11 (22H2 eller senare)
# Lista tillgängliga katalogmodeller (inlästa modeller visas efter körning)
foundry model list
## NOTE: Det finns för närvarande ingen dedikerad `--running` flagga; för att se vilka som är inlästa, starta en chatt eller inspektera serviceloggar.
- Python 3.10+ installerat
- Visual Studio Code med Python-tillägg
- Administratörsbehörighet för installation

### (Valfritt) Miljövariabler

Skapa en `.env` (eller ställ in i skalet) för att göra skript portabla:
# Jämför svar (icke-interaktivt)
foundry model run gpt-oss-20b --prompt "Förklara edge AI på ett enkelt sätt"
| Variabel | Syfte | Exempel |
|----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Föredragen modellalias (katalogen väljer automatiskt bästa variant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Åsidosätt endpoint (annars automatiskt från manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Aktivera streamingdemo | `true` |

> Om `FOUNDRY_LOCAL_ENDPOINT=auto` (eller inte inställd) härleds det från SDK-managern.

## Demo-flöde (30 minuter)

### 1. Installera Foundry Local och verifiera CLI-inställning (10 minuter)

# Lista cacheade modeller
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Förhandsvisning / Om stöds)**

Om ett inbyggt macOS-paket tillhandahålls (kontrollera officiell dokumentation för senaste):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Om macOS inbyggda binärer ännu inte är tillgängliga kan du fortfarande:
1. Använda en Windows 11 ARM/Intel VM (Parallels / UTM) och följa Windows-stegen.
2. Köra modeller via container (om containerbild publiceras) och ställa in `FOUNDRY_LOCAL_ENDPOINT` till den exponerade porten.

**Skapa Python-virtuell miljö (plattformoberoende)**

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

Uppgradera pip och installera kärnberoenden:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Steg 1.2: Verifiera installation

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Steg 1.3: Konfigurera miljö

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Rekommenderas)

Istället för att manuellt starta tjänsten och köra modeller kan **Foundry Local Python SDK** automatisera allt:

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

Om du föredrar explicit kontroll kan du fortfarande använda CLI + OpenAI-klienten som visas senare.

### 2. Kör modeller lokalt via CLI (10 minuter)

#### Steg 3.1: Distribuera Phi-4-modellen

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Steg 3.2: Distribuera GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Steg 3.3: Ladda ytterligare modeller

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Startprojekt: Anpassa 01-run-phi för Foundry Local (5 minuter)

#### Steg 4.1: Skapa grundläggande chattapplikation

Skapa `samples/01-foundry-quickstart/chat_quickstart.py` (uppdaterad för att använda manager om tillgänglig):

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

#### Steg 4.2: Testa applikationen

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Viktiga koncept som täcks

### 1. Foundry Local-arkitektur

- **Lokal inferensmotor**: Kör modeller helt på din enhet
- **OpenAI SDK-kompatibilitet**: Sömlös integration med befintlig OpenAI-kod
- **Modellhantering**: Ladda ner, cachea och kör flera modeller effektivt
- **Hårdvaruoptimering**: Utnyttja GPU-, NPU- och CPU-acceleration

### 2. CLI-kommandoreferens

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK-integration

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

## Felsökning av vanliga problem

### Problem 1: "Foundry command not found"

**Lösning:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problem 2: "Model failed to load"

**Lösning:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problem 3: "Connection refused on localhost:5273"

**Lösning:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tips för prestandaoptimering

### 1. Strategi för modellval

- **Phi-4-mini**: Bäst för allmänna uppgifter, lägre minnesanvändning
- **Qwen2.5-0.5b**: Snabbast inferens, minimala resurser
- **GPT-OSS-20B**: Högsta kvalitet, kräver mer resurser
- **DeepSeek-Coder**: Optimerad för programmeringsuppgifter

### 2. Hårdvaruoptimering

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Övervakning av prestanda

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### Valfria förbättringar

| Förbättring | Vad | Hur |
|-------------|-----|-----|
| Delade verktyg | Ta bort duplicerad klient/bootstrap-logik | Använd `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Synlighet för tokenanvändning | Lär ut kostnads-/effektivitetstänkande tidigt | Ställ in `SHOW_USAGE=1` för att skriva ut prompt/slutförande/totalt antal tokens |
| Deterministiska jämförelser | Stabil benchmarking och regressionskontroller | Använd `temperature=0`, `top_p=1`, konsekvent prompttext |
| Första-token-latens | Upplevd responsivitet | Anpassa benchmark-skript med streaming (`BENCH_STREAM=1`) |
| Försök igen vid tillfälliga fel | Robust demo vid kallstart | `RETRY_ON_FAIL=1` (standard) & justera `RETRY_BACKOFF` |
| Röktestning | Snabb kontroll av nyckelflöden | Kör `python Workshop/tests/smoke.py` före en workshop |
| Modellaliasprofiler | Snabbt byta modelluppsättning mellan maskiner | Underhåll `.env` med `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Cacheeffektivitet | Undvik upprepade uppvärmningar vid körning av flera exempel | Verktyg för cachehantering; återanvänd över skript/notebooks |
| Första körningens uppvärmning | Minska p95-latensspikar | Skicka en liten prompt efter att `FoundryLocalManager` skapats |

Exempel på deterministisk varm baslinje (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Du bör se liknande output och identiska tokenräkningar vid andra körningen, vilket bekräftar determinism.

## Nästa steg

Efter att ha avslutat denna session:

1. **Utforska Session 2**: Bygg AI-lösningar med Azure AI Foundry RAG
2. **Prova olika modeller**: Experimentera med Qwen, DeepSeek och andra modellfamiljer
3. **Optimera prestanda**: Finjustera inställningar för din specifika hårdvara
4. **Bygg egna applikationer**: Använd Foundry Local SDK i dina egna projekt

## Ytterligare resurser

### Dokumentation
- [Foundry Local Python SDK Referens](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installationsguide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modellkatalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Exempelkod
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Modellupptäckt och benchmarking

### Community
- [Foundry Local GitHub Diskussioner](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sessionens längd**: 30 minuter praktiskt arbete + 15 minuter Q&A  
**Svårighetsgrad**: Nybörjare  
**Förkunskaper**: Windows 11, Python 3.10+, Administratörsbehörighet  

## Exempelscenario & Workshopkartläggning

| Workshop-skript / Notebook | Scenario | Mål | Exempelinput | Dataset behövs |
|----------------------------|----------|-----|--------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Intern IT-grupp som utvärderar lokal inferens för en sekretessbedömningsportal | Bevisa att lokal SLM svarar inom sub-sekund latens på standardprompter | "Lista två fördelar med lokal inferens." | Ingen (enkel prompt) |
| Anpassningskodblock för snabbstart | Utvecklare som migrerar ett befintligt OpenAI-skript till Foundry Local | Visa drop-in-kompatibilitet | "Ge två fördelar med lokal inferens." | Endast inline-prompt |

### Scenarionarrativ
Säkerhets- och efterlevnadsgruppen måste validera om känslig prototypdata kan bearbetas lokalt. De kör bootstrap-skriptet med flera prompter (sekretess, latens, kostnad) med deterministiskt läge `temperature=0` för att fånga baslinjeutdata för senare jämförelse (Session 3 benchmarking och Session 4 SLM vs LLM-kontrast).

### Minimal promptuppsättning JSON (valfritt)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Använd denna lista för att skapa en reproducerbar utvärderingsloop eller för att så ett framtida regressions-testverktyg.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.