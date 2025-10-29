<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T23:05:34+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "sk"
}
-->
# Session 1: Začíname s Foundry Local

## Abstrakt

Začnite svoju cestu s Foundry Local inštaláciou a konfiguráciou na Windows 11. Naučte sa nastaviť CLI, povoliť hardvérovú akceleráciu a ukladať modely do vyrovnávacej pamäte pre rýchle lokálne inferencie. Táto praktická relácia vás prevedie spustením modelov ako Phi, Qwen, DeepSeek a GPT-OSS-20B pomocou reprodukovateľných príkazov CLI.

## Ciele učenia

Na konci tejto relácie budete schopní:

- **Inštalovať a konfigurovať**: Nastaviť Foundry Local na Windows 11 s optimálnymi nastaveniami výkonu
- **Ovládnuť operácie CLI**: Používať Foundry Local CLI na správu a nasadenie modelov
- **Povoliť hardvérovú akceleráciu**: Konfigurovať akceleráciu GPU pomocou ONNXRuntime alebo WebGPU
- **Nasadiť viacero modelov**: Lokálne spustiť modely phi-4, GPT-OSS-20B, Qwen a DeepSeek
- **Vytvoriť svoju prvú aplikáciu**: Prispôsobiť existujúce vzorky na použitie Foundry Local Python SDK

# Testovanie modelu (neinteraktívny jednorazový prompt)
foundry model run phi-4-mini --prompt "Ahoj, predstav sa"

- Windows 11 (22H2 alebo novší)
# Zobraziť dostupné modely v katalógu (načítané modely sa zobrazia po spustení)
foundry model list
## NOTE: Momentálne neexistuje špeciálny `--running` flag; na zobrazenie načítaných modelov iniciujte chat alebo skontrolujte logy služby.
- Nainštalovaný Python 3.10+
- Visual Studio Code s rozšírením Python
- Administrátorské práva na inštaláciu

### (Voliteľné) Premenné prostredia

Vytvorte `.env` (alebo nastavte v shelli) na zjednodušenie prenosu skriptov:
# Porovnanie odpovedí (neinteraktívne)
foundry model run gpt-oss-20b --prompt "Vysvetlite edge AI jednoduchými slovami"
| Premenná | Účel | Príklad |
|----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Preferovaný alias modelu (katalóg automaticky vyberie najlepší variant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Prekrytie endpointu (inak automaticky z manažéra) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Povoliť streamingovú ukážku | `true` |

> Ak je `FOUNDRY_LOCAL_ENDPOINT=auto` (alebo nenastavený), odvodíme ho z manažéra SDK.

## Priebeh ukážky (30 minút)

### 1. Inštalácia Foundry Local a overenie nastavenia CLI (10 minút)

# Zobraziť uložené modely
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Preview / Ak je podporovaný)**

Ak je k dispozícii natívny balík pre macOS (skontrolujte oficiálnu dokumentáciu pre najnovšie informácie):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Ak natívne binárne súbory pre macOS ešte nie sú dostupné, môžete:
1. Použiť Windows 11 ARM/Intel VM (Parallels / UTM) a postupovať podľa krokov pre Windows.
2. Spustiť modely cez kontajner (ak je publikovaný obraz kontajnera) a nastaviť `FOUNDRY_LOCAL_ENDPOINT` na vystavený port.

**Vytvorenie virtuálneho prostredia Python (Cross‑Platform)**

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

Aktualizujte pip a nainštalujte základné závislosti:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Krok 1.2: Overenie inštalácie

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Krok 1.3: Konfigurácia prostredia

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Odporúčané)

Namiesto manuálneho spúšťania služby a modelov môže **Foundry Local Python SDK** bootstrapovať všetko:

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

Ak preferujete explicitnú kontrolu, stále môžete použiť CLI + OpenAI klient, ako je ukázané neskôr.

### 2. Spustenie modelov lokálne cez CLI (10 minút)

#### Krok 3.1: Nasadenie modelu Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Krok 3.2: Nasadenie GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Krok 3.3: Načítanie ďalších modelov

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Začiatočný projekt: Prispôsobenie 01-run-phi pre Foundry Local (5 minút)

#### Krok 4.1: Vytvorenie základnej chatovacej aplikácie

Vytvorte `samples/01-foundry-quickstart/chat_quickstart.py` (aktualizované na použitie manažéra, ak je dostupný):

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

#### Krok 4.2: Testovanie aplikácie

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Kľúčové koncepty

### 1. Architektúra Foundry Local

- **Lokálny inferenčný engine**: Spúšťa modely úplne na vašom zariadení
- **Kompatibilita s OpenAI SDK**: Bezproblémová integrácia s existujúcim OpenAI kódom
- **Správa modelov**: Efektívne sťahovanie, ukladanie do vyrovnávacej pamäte a spúšťanie viacerých modelov
- **Optimalizácia hardvéru**: Využitie GPU, NPU a CPU akcelerácie

### 2. Referencia príkazov CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integrácia Python SDK

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

## Riešenie bežných problémov

### Problém 1: "Foundry príkaz nebol nájdený"

**Riešenie:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problém 2: "Model sa nepodarilo načítať"

**Riešenie:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problém 3: "Spojenie odmietnuté na localhost:5273"

**Riešenie:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tipy na optimalizáciu výkonu

### 1. Stratégia výberu modelu

- **Phi-4-mini**: Najlepší pre všeobecné úlohy, nižšia spotreba pamäte
- **Qwen2.5-0.5b**: Najrýchlejšia inferencia, minimálne zdroje
- **GPT-OSS-20B**: Najvyššia kvalita, vyžaduje viac zdrojov
- **DeepSeek-Coder**: Optimalizovaný pre programovacie úlohy

### 2. Optimalizácia hardvéru

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Monitorovanie výkonu

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

### Voliteľné vylepšenia

| Vylepšenie | Čo | Ako |
|------------|----|-----|
| Zdieľané utility | Odstránenie duplicity klienta/bootstrap logiky | Použite `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Viditeľnosť používania tokenov | Naučte sa myslenie o nákladoch/efektivite | Nastavte `SHOW_USAGE=1` na zobrazenie prompt/completion/celkových tokenov |
| Deterministické porovnania | Stabilné benchmarky a regresné kontroly | Použite `temperature=0`, `top_p=1`, konzistentný text promptu |
| Latencia prvého tokenu | Metrika vnímaného výkonu | Prispôsobte benchmark skript so streamingom (`BENCH_STREAM=1`) |
| Opakovanie pri prechodných chybách | Odolné ukážky pri studenom štarte | `RETRY_ON_FAIL=1` (predvolené) a upravte `RETRY_BACKOFF` |
| Smoke testovanie | Rýchla kontrola kľúčových tokov | Spustite `python Workshop/tests/smoke.py` pred workshopom |
| Profily aliasov modelov | Rýchle prepínanie sady modelov medzi zariadeniami | Udržujte `.env` s `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Efektivita ukladania do vyrovnávacej pamäte | Vyhnite sa opakovaným zahrievaniam pri viacerých vzorkách | Utility cache manažérov; opätovné použitie medzi skriptami/notebookmi |
| Zahrievanie pri prvom spustení | Zníženie p95 latencie | Spustite malý prompt po vytvorení `FoundryLocalManager`

Príklad deterministického zahrievacieho základu (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Mali by ste vidieť podobný výstup a identické počty tokenov pri druhom spustení, čo potvrdzuje deterministiku.

## Ďalšie kroky

Po dokončení tejto relácie:

1. **Preskúmajte reláciu 2**: Vytváranie AI riešení s Azure AI Foundry RAG
2. **Vyskúšajte rôzne modely**: Experimentujte s Qwen, DeepSeek a ďalšími rodinami modelov
3. **Optimalizujte výkon**: Jemne doladte nastavenia pre váš konkrétny hardvér
4. **Vytvorte vlastné aplikácie**: Použite Foundry Local SDK vo svojich vlastných projektoch

## Dodatočné zdroje

### Dokumentácia
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Ukážkový kód
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Komunita
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Trvanie relácie**: 30 minút prakticky + 15 minút Q&A  
**Úroveň obtiažnosti**: Začiatočník  
**Predpoklady**: Windows 11, Python 3.10+, Administrátorský prístup  

## Ukážkový scenár a mapovanie workshopu

| Skript workshopu / Notebook | Scenár | Cieľ | Príklad vstupov | Potrebný dataset |
|-----------------------------|--------|------|-----------------|------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Interný IT tím hodnotí inferenciu na zariadení pre portál hodnotenia súkromia | Dokázať, že lokálny SLM odpovedá v sub-sekundovej latencii na štandardné prompty | "Uveďte dve výhody lokálnej inferencie." | Žiadny (jednorazový prompt) |
| Kódový blok adaptácie Quickstart | Vývojár migrujúci existujúci OpenAI skript na Foundry Local | Ukázať kompatibilitu | "Uveďte dve výhody lokálnej inferencie." | Iba inline prompt |

### Naratív scenára
Tím pre bezpečnosť a súlad musí overiť, či citlivé prototypové dáta môžu byť spracované lokálne. Spúšťajú bootstrap skript s niekoľkými promptmi (súkromie, latencia, náklady) pomocou deterministického režimu temperature=0 na zachytenie základných výstupov pre neskoršie porovnanie (benchmarking relácie 3 a kontrast SLM vs LLM relácie 4).

### Minimálny JSON prompt set (voliteľné)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Použite tento zoznam na vytvorenie reprodukovateľnej evaluačnej slučky alebo na inicializáciu budúceho regresného testovacieho nástroja.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.