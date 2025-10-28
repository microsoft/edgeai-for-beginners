<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:26:11+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "cs"
}
-->
# Sezení 1: Začínáme s Foundry Local

## Abstrakt

Začněte svou cestu s Foundry Local instalací a konfigurací na Windows 11. Naučte se nastavit CLI, povolit hardwarovou akceleraci a ukládat modely do mezipaměti pro rychlé lokální inferenční procesy. Toto praktické sezení vás provede spuštěním modelů jako Phi, Qwen, DeepSeek a GPT-OSS-20B pomocí reprodukovatelných příkazů CLI.

## Cíle učení

Na konci tohoto sezení budete schopni:

- **Instalovat a konfigurovat**: Nastavit Foundry Local na Windows 11 s optimálním výkonem
- **Ovládnout operace CLI**: Používat Foundry Local CLI pro správu a nasazení modelů
- **Povolit hardwarovou akceleraci**: Konfigurovat akceleraci GPU pomocí ONNXRuntime nebo WebGPU
- **Nasadit více modelů**: Spustit modely phi-4, GPT-OSS-20B, Qwen a DeepSeek lokálně
- **Vytvořit svou první aplikaci**: Přizpůsobit existující vzorky pro použití Foundry Local Python SDK

# Testování modelu (neinteraktivní jednorázový prompt)
foundry model run phi-4-mini --prompt "Ahoj, představ se"

- Windows 11 (22H2 nebo novější)
# Seznam dostupných modelů v katalogu (načtené modely se zobrazí po spuštění)
foundry model list
## NOTE: V současné době neexistuje žádný dedikovaný příznak `--running`; pro zjištění, které modely jsou načtené, zahajte chat nebo zkontrolujte logy služby.
- Nainstalovaný Python 3.10+
- Visual Studio Code s rozšířením pro Python
- Administrátorská práva pro instalaci

### (Volitelné) Proměnné prostředí

Vytvořte `.env` (nebo nastavte v shellu) pro zajištění přenositelnosti skriptů:
# Porovnání odpovědí (neinteraktivní)
foundry model run gpt-oss-20b --prompt "Vysvětli edge AI jednoduchými slovy"
| Proměnná | Účel | Příklad |
|----------|------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Preferovaný alias modelu (katalog automaticky vybere nejlepší variantu) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Přepsání endpointu (jinak automaticky z manageru) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Povolit ukázku streamování | `true` |

> Pokud je `FOUNDRY_LOCAL_ENDPOINT=auto` (nebo nenastaveno), odvodíme jej z SDK manageru.

## Průběh ukázky (30 minut)

### 1. Instalace Foundry Local a ověření nastavení CLI (10 minut)

# Seznam modelů v mezipaměti
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Preview / pokud podporováno)**

Pokud je k dispozici nativní balíček pro macOS (zkontrolujte oficiální dokumentaci pro nejnovější informace):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Pokud nativní binární soubory pro macOS ještě nejsou dostupné, můžete:
1. Použít Windows 11 ARM/Intel VM (Parallels / UTM) a postupovat podle kroků pro Windows.
2. Spustit modely přes kontejner (pokud je publikován obraz kontejneru) a nastavit `FOUNDRY_LOCAL_ENDPOINT` na vystavený port.

**Vytvoření virtuálního prostředí Python (napříč platformami)**

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

Aktualizujte pip a nainstalujte základní závislosti:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Krok 1.2: Ověření instalace

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Krok 1.3: Konfigurace prostředí

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (doporučeno)

Namísto ručního spouštění služby a modelů může **Foundry Local Python SDK** vše automaticky nastavit:

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

Pokud preferujete explicitní kontrolu, můžete stále používat CLI + OpenAI klienta, jak je ukázáno později.

### 2. Spuštění modelů lokálně přes CLI (10 minut)

#### Krok 3.1: Nasazení modelu Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Krok 3.2: Nasazení GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Krok 3.3: Načtení dalších modelů

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Startovací projekt: Přizpůsobení 01-run-phi pro Foundry Local (5 minut)

#### Krok 4.1: Vytvoření základní chatovací aplikace

Vytvořte `samples/01-foundry-quickstart/chat_quickstart.py` (aktualizováno pro použití manageru, pokud je dostupný):

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

#### Krok 4.2: Testování aplikace

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Klíčové koncepty

### 1. Architektura Foundry Local

- **Lokální inferenční engine**: Spouští modely přímo na vašem zařízení
- **Kompatibilita s OpenAI SDK**: Bezproblémová integrace s existujícím OpenAI kódem
- **Správa modelů**: Efektivní stahování, ukládání do mezipaměti a spouštění více modelů
- **Optimalizace hardwaru**: Využití akcelerace GPU, NPU a CPU

### 2. Referenční příkazy CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integrace Python SDK

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

## Řešení běžných problémů

### Problém 1: "Foundry command not found"

**Řešení:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problém 2: "Model failed to load"

**Řešení:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problém 3: "Connection refused on localhost:5273"

**Řešení:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tipy pro optimalizaci výkonu

### 1. Strategie výběru modelu

- **Phi-4-mini**: Nejlepší pro obecné úkoly, nižší využití paměti
- **Qwen2.5-0.5b**: Nejrychlejší inferenční proces, minimální zdroje
- **GPT-OSS-20B**: Nejvyšší kvalita, vyžaduje více zdrojů
- **DeepSeek-Coder**: Optimalizováno pro programovací úkoly

### 2. Optimalizace hardwaru

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Monitorování výkonu

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

### Volitelná vylepšení

| Vylepšení | Co | Jak |
|-----------|----|-----|
| Sdílené utility | Odstranění duplicitní logiky klienta/bootstrapu | Použijte `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Viditelnost využití tokenů | Naučte se přemýšlet o nákladech/efektivitě | Nastavte `SHOW_USAGE=1` pro tisk prompt/completion/celkových tokenů |
| Deterministické porovnání | Stabilní benchmarking a regresní kontroly | Použijte `temperature=0`, `top_p=1`, konzistentní text promptu |
| Latence prvního tokenu | Metrika vnímané odezvy | Přizpůsobte benchmark skript se streamováním (`BENCH_STREAM=1`) |
| Opakování při přechodných chybách | Odolné ukázky při studeném startu | `RETRY_ON_FAIL=1` (výchozí) a upravte `RETRY_BACKOFF` |
| Smoke Testing | Rychlá kontrola klíčových toků | Spusťte `python Workshop/tests/smoke.py` před workshopem |
| Profily aliasů modelů | Rychlé přepínání modelů mezi stroji | Udržujte `.env` s `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Efektivita mezipaměti | Vyhněte se opakovaným zahříváním při více vzorcích | Utility cache managerů; znovu použijte napříč skripty/notebooky |
| Zahřívání při prvním spuštění | Snížení p95 latence | Spusťte malý prompt po vytvoření `FoundryLocalManager`

Příklad deterministického zahřívacího základu (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Měli byste vidět podobný výstup a identické počty tokenů při druhém spuštění, což potvrzuje determinismus.

## Další kroky

Po dokončení tohoto sezení:

1. **Prozkoumejte Sezení 2**: Vytváření AI řešení s Azure AI Foundry RAG
2. **Vyzkoušejte různé modely**: Experimentujte s Qwen, DeepSeek a dalšími modelovými rodinami
3. **Optimalizujte výkon**: Doladění nastavení pro váš specifický hardware
4. **Vytvářejte vlastní aplikace**: Použijte Foundry Local SDK ve svých vlastních projektech

## Další zdroje

### Dokumentace
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Ukázkový kód
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Komunita
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Délka sezení**: 30 minut praktické části + 15 minut Q&A  
**Úroveň obtížnosti**: Začátečník  
**Předpoklady**: Windows 11, Python 3.10+, Administrátorský přístup  

## Ukázkový scénář a mapování workshopu

| Skript workshopu / Notebook | Scénář | Cíl | Příklad vstupů | Potřebný dataset |
|-----------------------------|--------|-----|----------------|------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Interní IT tým hodnotící inferenci na zařízení pro portál posuzování ochrany soukromí | Prokázat, že lokální SLM odpovídá s latencí pod sekundu na standardní prompty | "Uveďte dvě výhody lokální inference." | Žádný (jednorázový prompt) |
| Kódový blok pro adaptaci quickstartu | Vývojář migrující existující OpenAI skript na Foundry Local | Ukázat kompatibilitu | "Uveďte dvě výhody lokální inference." | Pouze inline prompt |

### Narativ scénáře
Tým pro bezpečnost a shodu musí ověřit, zda lze citlivá data prototypu zpracovávat lokálně. Spouští bootstrap skript s několika prompty (soukromí, latence, náklady) pomocí deterministického režimu temperature=0, aby zachytili základní výstupy pro pozdější porovnání (benchmarking v sezení 3 a kontrast SLM vs LLM v sezení 4).

### Minimální sada promptů JSON (volitelné)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Použijte tento seznam k vytvoření reprodukovatelné evaluační smyčky nebo k nasazení budoucího regresního testovacího nástroje.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.