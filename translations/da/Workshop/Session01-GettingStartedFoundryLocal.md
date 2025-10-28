<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:21:56+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "da"
}
-->
# Session 1: Kom godt i gang med Foundry Local

## Resumé

Start din rejse med Foundry Local ved at installere og konfigurere det på Windows 11. Lær at opsætte CLI, aktivere hardwareacceleration og cache modeller for hurtig lokal inferens. Denne praktiske session guider dig gennem kørsel af modeller som Phi, Qwen, DeepSeek og GPT-OSS-20B ved hjælp af reproducerbare CLI-kommandoer.

## Læringsmål

Ved afslutningen af denne session vil du:

- **Installere og konfigurere**: Opsætte Foundry Local på Windows 11 med optimale indstillinger
- **Beherske CLI-operationer**: Bruge Foundry Local CLI til modelstyring og implementering
- **Aktivere hardwareacceleration**: Konfigurere GPU-acceleration med ONNXRuntime eller WebGPU
- **Implementere flere modeller**: Køre phi-4, GPT-OSS-20B, Qwen og DeepSeek modeller lokalt
- **Bygge din første app**: Tilpasse eksisterende eksempler til at bruge Foundry Local Python SDK

# Test modellen (ikke-interaktiv enkelt prompt)
foundry model run phi-4-mini --prompt "Hej, introducer dig selv"

- Windows 11 (22H2 eller nyere)
# Liste over tilgængelige katalogmodeller (indlæste modeller vises efter kørsel)
foundry model list
## NOTE: Der er i øjeblikket ikke en dedikeret `--running` flag; for at se hvilke der er indlæst, start en chat eller inspicer servicelogfiler.
- Python 3.10+ installeret
- Visual Studio Code med Python-udvidelse
- Administratorrettigheder til installation

### (Valgfrit) Miljøvariabler

Opret en `.env` (eller sæt i shell) for at gøre scripts bærbare:
# Sammenlign svar (ikke-interaktiv)
foundry model run gpt-oss-20b --prompt "Forklar edge AI på en enkel måde"
| Variabel | Formål | Eksempel |
|----------|--------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Foretrukket modelalias (katalog vælger automatisk den bedste variant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Overstyr endpoint (ellers automatisk fra manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Aktiver streaming-demo | `true` |

> Hvis `FOUNDRY_LOCAL_ENDPOINT=auto` (eller ikke sat), afleder vi det fra SDK-manageren.

## Demo Flow (30 minutter)

### 1. Installer Foundry Local og verificer CLI-opsætning (10 minutter)

# Liste over cachede modeller
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Preview / Hvis understøttet)**

Hvis en native macOS-pakke er tilgængelig (tjek officielle dokumenter for seneste):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Hvis macOS native binære filer endnu ikke er tilgængelige, kan du stadig: 
1. Bruge en Windows 11 ARM/Intel VM (Parallels / UTM) og følge Windows-trinnene. 
2. Køre modeller via container (hvis containerbillede er offentliggjort) og sætte `FOUNDRY_LOCAL_ENDPOINT` til den eksponerede port. 

**Opret Python Virtual Environment (Platform-uafhængig)**

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

Opgrader pip og installer kerneafhængigheder:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Trin 1.2: Verificer installation

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Trin 1.3: Konfigurer miljø

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Anbefalet)

I stedet for manuelt at starte tjenesten og køre modeller, kan **Foundry Local Python SDK** bootstrappe alt:

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

Hvis du foretrækker eksplicit kontrol, kan du stadig bruge CLI + OpenAI-klienten som vist senere.

### 2. Kør modeller lokalt via CLI (10 minutter)

#### Trin 3.1: Implementer Phi-4 model

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Trin 3.2: Implementer GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Trin 3.3: Indlæs yderligere modeller

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Startprojekt: Tilpas 01-run-phi til Foundry Local (5 minutter)

#### Trin 4.1: Opret grundlæggende chatapplikation

Opret `samples/01-foundry-quickstart/chat_quickstart.py` (opdateret til at bruge manageren, hvis tilgængelig):

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

#### Trin 4.2: Test applikationen

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Centrale begreber dækket

### 1. Foundry Local Arkitektur

- **Lokal inferensmotor**: Kører modeller helt på din enhed
- **OpenAI SDK-kompatibilitet**: Problemfri integration med eksisterende OpenAI-kode
- **Modelstyring**: Download, cache og kør flere modeller effektivt
- **Hardwareoptimering**: Udnyt GPU-, NPU- og CPU-acceleration

### 2. CLI Kommando Reference

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK Integration

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

## Fejlfinding af almindelige problemer

### Problem 1: "Foundry command not found"

**Løsning:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problem 2: "Model failed to load"

**Løsning:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problem 3: "Connection refused on localhost:5273"

**Løsning:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tips til optimering af ydeevne

### 1. Modelvalgstrategi

- **Phi-4-mini**: Bedst til generelle opgaver, lavt hukommelsesforbrug
- **Qwen2.5-0.5b**: Hurtigste inferens, minimale ressourcer
- **GPT-OSS-20B**: Højeste kvalitet, kræver flere ressourcer
- **DeepSeek-Coder**: Optimeret til programmeringsopgaver

### 2. Hardwareoptimering

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Overvågning af ydeevne

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

### Valgfrie forbedringer

| Forbedring | Hvad | Hvordan |
|------------|------|--------|
| Delte værktøjer | Fjern duplikeret klient/bootstrap-logik | Brug `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Synlighed af tokenforbrug | Lær omkostnings-/effektivitetstankegang tidligt | Sæt `SHOW_USAGE=1` for at udskrive prompt/completion/totale tokens |
| Deterministiske sammenligninger | Stabil benchmarking & regressionstjek | Brug `temperature=0`, `top_p=1`, konsistent prompttekst |
| Første-token latenstid | Opfattet responsmetrik | Tilpas benchmark-script med streaming (`BENCH_STREAM=1`) |
| Genforsøg ved midlertidige fejl | Robust demo ved koldstart | `RETRY_ON_FAIL=1` (standard) & juster `RETRY_BACKOFF` |
| Røgtest | Hurtig sanity-check på nøgleflows | Kør `python Workshop/tests/smoke.py` før en workshop |
| Modelaliasprofiler | Hurtigt skifte mellem maskiner | Vedligehold `.env` med `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Cacheeffektivitet | Undgå gentagne opvarmninger i multi-sample kørsel | Værktøjer cache managers; genbrug på tværs af scripts/notebooks |
| Første kørsel opvarmning | Reducer p95 latenstidspikes | Send en lille prompt efter `FoundryLocalManager` oprettelse |

Eksempel på deterministisk varm baseline (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Du bør se lignende output og identiske tokenantal ved anden kørsel, hvilket bekræfter determinisme.

## Næste skridt

Efter at have afsluttet denne session:

1. **Udforsk Session 2**: Byg AI-løsninger med Azure AI Foundry RAG
2. **Prøv forskellige modeller**: Eksperimenter med Qwen, DeepSeek og andre modelfamilier
3. **Optimer ydeevne**: Finjuster indstillinger til din specifikke hardware
4. **Byg brugerdefinerede applikationer**: Brug Foundry Local SDK i dine egne projekter

## Yderligere ressourcer

### Dokumentation
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installationsvejledning](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modelkatalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Eksempelkode
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Fællesskab
- [Foundry Local GitHub Diskussioner](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sessionens varighed**: 30 minutters praktisk + 15 minutters Q&A
**Sværhedsgrad**: Begynder
**Forudsætninger**: Windows 11, Python 3.10+, Administratoradgang

## Eksempelscenarie & Workshop-kortlægning

| Workshop Script / Notebook | Scenarie | Mål | Eksempelinput | Nødvendigt datasæt |
|----------------------------|----------|-----|---------------|--------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Internt IT-team evaluerer on-device inferens til en portal for privatlivsvurdering | Bevis at lokal SLM reagerer inden for sub-sekund latenstid på standardprompter | "Nævn to fordele ved lokal inferens." | Ingen (enkelt prompt) |
| Quickstart tilpasningskodeblok | Udvikler migrerer et eksisterende OpenAI-script til Foundry Local | Vis drop-in kompatibilitet | "Nævn to fordele ved lokal inferens." | Kun inline prompt |

### Scenariefortælling
Sikkerheds- og compliance-teamet skal validere, om følsomme prototype-data kan behandles lokalt. De kører bootstrap-scriptet med flere prompter (privatliv, latenstid, omkostninger) ved hjælp af deterministisk temperatur=0 tilstand for at fange baseline-output til senere sammenligning (Session 3 benchmarking og Session 4 SLM vs LLM kontrast).

### Minimal Prompt Set JSON (valgfrit)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Brug denne liste til at oprette en reproducerbar evalueringssløjfe eller til at så en fremtidig regressionstest.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.