<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T22:13:18+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "no"
}
-->
# Sesjon 1: Komme i gang med Foundry Local

## Sammendrag

Start reisen med Foundry Local ved å installere og konfigurere det på Windows 11. Lær hvordan du setter opp CLI, aktiverer maskinvareakselerasjon og cacher modeller for rask lokal inferens. Denne praktiske sesjonen viser hvordan du kjører modeller som Phi, Qwen, DeepSeek og GPT-OSS-20B ved hjelp av reproducerbare CLI-kommandoer.

## Læringsmål

Ved slutten av denne sesjonen vil du:

- **Installere og konfigurere**: Sette opp Foundry Local på Windows 11 med optimale ytelsesinnstillinger
- **Beherske CLI-operasjoner**: Bruke Foundry Local CLI for modelladministrasjon og distribusjon
- **Aktivere maskinvareakselerasjon**: Konfigurere GPU-akselerasjon med ONNXRuntime eller WebGPU
- **Distribuere flere modeller**: Kjøre phi-4, GPT-OSS-20B, Qwen og DeepSeek-modeller lokalt
- **Bygge din første app**: Tilpasse eksisterende eksempler for å bruke Foundry Local Python SDK

# Test modellen (ikke-interaktiv enkeltprompt)
foundry model run phi-4-mini --prompt "Hei, kan du introdusere deg selv?"

- Windows 11 (22H2 eller nyere)
# Liste tilgjengelige katalogmodeller (lastede modeller vises etter kjøring)
foundry model list
## NOTE: Det finnes for øyeblikket ingen dedikert `--running` flagg; for å se hvilke som er lastet, start en chat eller inspiser tjenestelogger.
- Python 3.10+ installert
- Visual Studio Code med Python-utvidelse
- Administratorrettigheter for installasjon

### (Valgfritt) Miljøvariabler

Opprett en `.env` (eller sett i shell) for å gjøre skript bærbare:
# Sammenlign svar (ikke-interaktiv)
foundry model run gpt-oss-20b --prompt "Forklar edge AI på en enkel måte"
| Variabel | Formål | Eksempel |
|----------|--------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Foretrukket modellalias (katalogen velger automatisk beste variant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Overstyr endepunkt (ellers automatisk fra manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Aktiver streaming-demo | `true` |

> Hvis `FOUNDRY_LOCAL_ENDPOINT=auto` (eller ikke satt) henter vi det fra SDK-manageren.

## Demo-flyt (30 minutter)

### 1. Installer Foundry Local og verifiser CLI-oppsett (10 minutter)

# Liste cachede modeller
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Forhåndsvisning / Hvis støttet)**

Hvis en innfødt macOS-pakke er tilgjengelig (sjekk offisiell dokumentasjon for siste nytt):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Hvis macOS-innfødte binærfiler ikke er tilgjengelige ennå, kan du fortsatt: 
1. Bruke en Windows 11 ARM/Intel VM (Parallels / UTM) og følge Windows-trinnene. 
2. Kjøre modeller via container (hvis containerbilde er publisert) og sette `FOUNDRY_LOCAL_ENDPOINT` til den eksponerte porten. 

**Opprett Python Virtual Environment (Plattformuavhengig)**

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

Oppgrader pip og installer kjerneavhengigheter:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Trinn 1.2: Verifiser installasjon

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Trinn 1.3: Konfigurer miljø

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Anbefalt)

I stedet for å starte tjenesten manuelt og kjøre modeller, kan **Foundry Local Python SDK** bootstrappe alt:

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

Hvis du foretrekker eksplisitt kontroll, kan du fortsatt bruke CLI + OpenAI-klienten som vist senere.

### 2. Kjøre modeller lokalt via CLI (10 minutter)

#### Trinn 3.1: Distribuer Phi-4-modellen

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Trinn 3.2: Distribuer GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Trinn 3.3: Last inn flere modeller

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Startprosjekt: Tilpass 01-run-phi for Foundry Local (5 minutter)

#### Trinn 4.1: Opprett enkel chat-applikasjon

Opprett `samples/01-foundry-quickstart/chat_quickstart.py` (oppdatert for å bruke manager hvis tilgjengelig):

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

#### Trinn 4.2: Test applikasjonen

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Nøkkelkonsepter dekket

### 1. Foundry Local-arkitektur

- **Lokal inferensmotor**: Kjører modeller helt på din enhet
- **OpenAI SDK-kompatibilitet**: Sømløs integrasjon med eksisterende OpenAI-kode
- **Modelladministrasjon**: Last ned, cache og kjør flere modeller effektivt
- **Maskinvareoptimalisering**: Utnytt GPU-, NPU- og CPU-akselerasjon

### 2. CLI-kommandoreferanse

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK-integrasjon

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

## Feilsøking av vanlige problemer

### Problem 1: "Foundry-kommando ikke funnet"

**Løsning:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problem 2: "Modellen klarte ikke å laste"

**Løsning:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problem 3: "Tilkobling nektet på localhost:5273"

**Løsning:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tips for ytelsesoptimalisering

### 1. Strategi for modellvalg

- **Phi-4-mini**: Best for generelle oppgaver, lavere minnebruk
- **Qwen2.5-0.5b**: Raskest inferens, minimale ressurser
- **GPT-OSS-20B**: Høyeste kvalitet, krever mer ressurser
- **DeepSeek-Coder**: Optimalisert for programmeringsoppgaver

### 2. Maskinvareoptimalisering

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Overvåking av ytelse

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

### Valgfrie forbedringer

| Forbedring | Hva | Hvordan |
|------------|-----|---------|
| Delte verktøy | Fjern duplisert klient/bootstrap-logikk | Bruk `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Synlighet for tokenbruk | Lær kostnad/effektivitet tidlig | Sett `SHOW_USAGE=1` for å skrive ut prompt/fullføring/totale tokens |
| Deterministiske sammenligninger | Stabil benchmarking og regresjonstester | Bruk `temperature=0`, `top_p=1`, konsistent prompttekst |
| Første-token-latens | Oppfattet responsivitet | Tilpass benchmark-skript med streaming (`BENCH_STREAM=1`) |
| Gjenta ved midlertidige feil | Robust demo ved kaldstart | `RETRY_ON_FAIL=1` (standard) og juster `RETRY_BACKOFF` |
| Røyktesting | Rask sanity-sjekk på nøkkelflyter | Kjør `python Workshop/tests/smoke.py` før en workshop |
| Modellaliasprofiler | Raskt bytte av modellsett mellom maskiner | Vedlikehold `.env` med `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Cache-effektivitet | Unngå gjentatte oppvarminger i multi-sample kjøring | Verktøy cache-managers; gjenbruk på tvers av skript/notebooks |
| Oppvarming ved første kjøring | Reduser p95-latens | Kjør en liten prompt etter opprettelse av `FoundryLocalManager` |

Eksempel på deterministisk varm baseline (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Du bør se lignende utdata og identiske token-tellinger ved andre kjøring, som bekrefter determinisme.

## Neste steg

Etter å ha fullført denne sesjonen:

1. **Utforsk sesjon 2**: Bygg AI-løsninger med Azure AI Foundry RAG
2. **Prøv forskjellige modeller**: Eksperimenter med Qwen, DeepSeek og andre modelfamilier
3. **Optimaliser ytelse**: Finjuster innstillinger for din spesifikke maskinvare
4. **Bygg egne applikasjoner**: Bruk Foundry Local SDK i dine egne prosjekter

## Tilleggsressurser

### Dokumentasjon
- [Foundry Local Python SDK Referanse](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installasjonsveiledning](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modellkatalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Eksempelkode
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK-integrasjon
- [Module08 Sample 03](./samples/03/README.md) - Modelloppdagelse og benchmarking

### Felleskap
- [Foundry Local GitHub Diskusjoner](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Varighet på sesjonen**: 30 minutter praktisk + 15 minutter Q&A  
**Vanskelighetsnivå**: Nybegynner  
**Forutsetninger**: Windows 11, Python 3.10+, Administratorrettigheter  

## Eksempelscenario og workshopkartlegging

| Workshop-skript / Notebook | Scenario | Mål | Eksempelinput | Dataset nødvendig |
|----------------------------|----------|-----|---------------|-------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Internt IT-team som evaluerer lokal inferens for en personvernvurderingsportal | Bevise at lokal SLM svarer innen sub-sekund latens på standardprompter | "List opp to fordeler med lokal inferens." | Ingen (enkeltprompt) |
| Tilpasningskodeblokk for hurtigstart | Utvikler som migrerer et eksisterende OpenAI-skript til Foundry Local | Vise drop-in-kompatibilitet | "Gi to fordeler med lokal inferens." | Kun inline-prompt |

### Scenariofortelling
Sikkerhets- og samsvarsgruppen må validere om sensitiv prototypedata kan behandles lokalt. De kjører bootstrap-skriptet med flere promter (personvern, latens, kostnad) ved bruk av deterministisk temperatur=0-modus for å fange baseline-utdata for senere sammenligning (Sesjon 3 benchmarking og Sesjon 4 SLM vs LLM-kontrast).

### Minimal prompt-sett JSON (valgfritt)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Bruk denne listen for å lage en reproducerbar evalueringssløyfe eller for å forberede en fremtidig regresjonstest-harness.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.