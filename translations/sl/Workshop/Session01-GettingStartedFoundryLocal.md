<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T23:30:52+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "sl"
}
-->
# Seja 1: Začetek z Foundry Local

## Povzetek

Začnite svojo pot s Foundry Local tako, da ga namestite in konfigurirate na Windows 11. Naučite se nastaviti CLI, omogočiti strojno pospeševanje in predpomniti modele za hitro lokalno sklepanje. Ta praktična seja vas vodi skozi izvajanje modelov, kot so Phi, Qwen, DeepSeek in GPT-OSS-20B, z reproducibilnimi CLI ukazi.

## Cilji učenja

Do konca te seje boste:

- **Namestili in konfigurirali**: Nastavili Foundry Local na Windows 11 z optimalnimi nastavitvami zmogljivosti
- **Obvladali CLI operacije**: Uporabili Foundry Local CLI za upravljanje in uvajanje modelov
- **Omogočili strojno pospeševanje**: Konfigurirali GPU pospeševanje z ONNXRuntime ali WebGPU
- **Uvedli več modelov**: Lokalno izvajali modele phi-4, GPT-OSS-20B, Qwen in DeepSeek
- **Zgradili svojo prvo aplikacijo**: Prilagodili obstoječe vzorce za uporabo Foundry Local Python SDK

# Testiranje modela (neinteraktivni enojni poziv)
foundry model run phi-4-mini --prompt "Pozdravljeni, predstavite se"

- Windows 11 (22H2 ali novejši)
# Seznam razpoložljivih katalogskih modelov (naloženi modeli se prikažejo po zagonu)
foundry model list
## NOTE: Trenutno ni namenskega `--running` zastavka; za ogled naloženih modelov začnite klepet ali preglejte dnevnik storitev.
- Nameščen Python 3.10+
- Visual Studio Code z razširitvijo za Python
- Skrbniške pravice za namestitev

### (Neobvezno) Spremenljivke okolja

Ustvarite `.env` (ali nastavite v lupini), da bodo skripti prenosljivi:
# Primerjava odgovorov (neinteraktivno)
foundry model run gpt-oss-20b --prompt "Razložite edge AI na preprost način"
| Spremenljivka | Namen | Primer |
|---------------|-------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Prednostni vzdevek modela (katalog samodejno izbere najboljšo različico) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Prepiši končno točko (sicer samodejno iz upravitelja) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Omogoči pretočno predstavitev | `true` |

> Če je `FOUNDRY_LOCAL_ENDPOINT=auto` (ali ni nastavljena), jo pridobimo iz upravitelja SDK.

## Potek predstavitve (30 minut)

### 1. Namestitev Foundry Local in preverjanje nastavitve CLI (10 minut)

# Seznam predpomnjenih modelov
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Predogled / Če je podprt)**

Če je na voljo domači paket za macOS (preverite uradno dokumentacijo za najnovejše):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Če domači binarni programi za macOS še niso na voljo, lahko še vedno:
1. Uporabite Windows 11 ARM/Intel VM (Parallels / UTM) in sledite korakom za Windows.
2. Izvajate modele prek kontejnerja (če je objavljena slika kontejnerja) in nastavite `FOUNDRY_LOCAL_ENDPOINT` na izpostavljeni port.

**Ustvarjanje virtualnega okolja za Python (Cross‑Platform)**

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

Nadgradite pip in namestite osnovne odvisnosti:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Korak 1.2: Preverjanje namestitve

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Korak 1.3: Konfiguracija okolja

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Priporočeno)

Namesto ročnega zagona storitve in izvajanja modelov lahko **Foundry Local Python SDK** vse samodejno nastavi:

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

Če imate raje eksplicitni nadzor, lahko še vedno uporabite CLI + OpenAI odjemalca, kot je prikazano kasneje.

### 2. Lokalno izvajanje modelov prek CLI (10 minut)

#### Korak 3.1: Uvedba modela Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Korak 3.2: Uvedba GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Korak 3.3: Nalaganje dodatnih modelov

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Začetni projekt: Prilagoditev 01-run-phi za Foundry Local (5 minut)

#### Korak 4.1: Ustvarjanje osnovne klepetalne aplikacije

Ustvarite `samples/01-foundry-quickstart/chat_quickstart.py` (posodobljeno za uporabo upravitelja, če je na voljo):

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

#### Korak 4.2: Testiranje aplikacije

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Ključni koncepti, ki jih pokrivamo

### 1. Arhitektura Foundry Local

- **Lokalni sklepni motor**: Izvaja modele popolnoma na vaši napravi
- **Združljivost z OpenAI SDK**: Brezhibna integracija z obstoječo kodo OpenAI
- **Upravljanje modelov**: Prenos, predpomnjenje in učinkovito izvajanje več modelov
- **Optimizacija strojne opreme**: Izkoristite GPU, NPU in CPU pospeševanje

### 2. Referenca ukazov CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integracija Python SDK

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

## Reševanje pogostih težav

### Težava 1: "Foundry ukaz ni najden"

**Rešitev:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Težava 2: "Modela ni uspelo naložiti"

**Rešitev:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Težava 3: "Povezava zavrnjena na localhost:5273"

**Rešitev:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Nasveti za optimizacijo zmogljivosti

### 1. Strategija izbire modela

- **Phi-4-mini**: Najboljši za splošne naloge, manjša poraba pomnilnika
- **Qwen2.5-0.5b**: Najhitrejše sklepanje, minimalni viri
- **GPT-OSS-20B**: Najvišja kakovost, zahteva več virov
- **DeepSeek-Coder**: Optimiziran za programerske naloge

### 2. Optimizacija strojne opreme

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Spremljanje zmogljivosti

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

### Neobvezne izboljšave

| Izboljšava | Kaj | Kako |
|------------|-----|------|
| Skupne pripomočke | Odstranite podvojeno logiko odjemalca/bootstrappinga | Uporabite `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Vidnost uporabe žetonov | Naučite razmišljanje o stroških/učinkovitosti zgodaj | Nastavite `SHOW_USAGE=1`, da natisnete poziv/odgovor/skupne žetone |
| Deterministične primerjave | Stabilno primerjanje in regresijski pregledi | Uporabite `temperature=0`, `top_p=1`, dosledno besedilo poziva |
| Latenca prvega žetona | Merilo zaznane odzivnosti | Prilagodite skript za merjenje s pretočnostjo (`BENCH_STREAM=1`) |
| Ponovni poskus pri prehodnih napakah | Odporne predstavitve ob hladnem zagonu | `RETRY_ON_FAIL=1` (privzeto) in prilagodite `RETRY_BACKOFF` |
| Testiranje delovanja | Hitro preverjanje ključnih tokov | Zaženite `python Workshop/tests/smoke.py` pred delavnico |
| Profili vzdevkov modelov | Hitro preklapljanje med nabori modelov na različnih napravah | Vzdržujte `.env` z `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Učinkovitost predpomnjenja | Izogibanje ponovnemu ogrevanju pri večkratnem zagonu vzorcev | Pripomočki za upravljanje predpomnilnika; ponovno uporabite med skripti/zvezki |
| Ogrevanje prvega zagona | Zmanjšanje p95 konic latence | Po ustvarjanju `FoundryLocalManager` izvedite majhen poziv |

Primer determinističnega toplega zagonskega osnova (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Videti bi morali podobne rezultate in identične števce žetonov pri drugem zagonu, kar potrjuje determinističnost.

## Naslednji koraki

Po zaključku te seje:

1. **Raziskujte sejo 2**: Gradnja AI rešitev z Azure AI Foundry RAG
2. **Preizkusite različne modele**: Eksperimentirajte z modeli Qwen, DeepSeek in drugimi družinami modelov
3. **Optimizirajte zmogljivost**: Prilagodite nastavitve za vašo specifično strojno opremo
4. **Zgradite prilagojene aplikacije**: Uporabite Foundry Local SDK v svojih projektih

## Dodatni viri

### Dokumentacija
- [Referenca Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Navodila za namestitev Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Katalog modelov](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Vzorčna koda
- [Modul08 Vzorec 01](./samples/01/README.md) - REST Chat Quickstart
- [Modul08 Vzorec 02](./samples/02/README.md) - Integracija OpenAI SDK
- [Modul08 Vzorec 03](./samples/03/README.md) - Odkritje modelov in primerjava zmogljivosti

### Skupnost
- [Foundry Local GitHub Razprave](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Skupnost](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Trajanje seje**: 30 minut praktično + 15 minut Q&A
**Stopnja težavnosti**: Začetnik
**Predpogoji**: Windows 11, Python 3.10+, Skrbniški dostop

## Vzorčni scenarij in preslikava delavnice

| Skript delavnice / Zvezek | Scenarij | Cilj | Primer vnosa | Potrebna podatkovna zbirka |
|---------------------------|----------|------|--------------|----------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Interna IT ekipa ocenjuje sklepanje na napravi za portal za oceno zasebnosti | Dokazati, da lokalni SLM odgovarja z latenco pod sekundo na standardne pozive | "Naštejte dve prednosti lokalnega sklepanja." | Brez (enojni poziv) |
| Koda za prilagoditev hitrega zagona | Razvijalec, ki migrira obstoječi OpenAI skript na Foundry Local | Pokažite združljivost brez sprememb | "Naštejte dve prednosti lokalnega sklepanja." | Samo inline poziv |

### Narativ scenarija
Ekipa za varnost in skladnost mora potrditi, ali je mogoče občutljive prototipne podatke obdelati lokalno. Zaženejo bootstrap skript z več pozivi (zasebnost, latenca, stroški) z determinističnim načinom temperature=0, da zajamejo osnovne izhode za kasnejšo primerjavo (benchmarking v seji 3 in kontrast SLM proti LLM v seji 4).

### Minimalni nabor pozivov JSON (neobvezno)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Uporabite ta seznam za ustvarjanje reproducibilne zanke ocenjevanja ali za seme prihodnjega regresijskega testnega orodja.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.