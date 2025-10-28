<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:27:59+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "hr"
}
-->
# Sesija 1: Početak rada s Foundry Local

## Sažetak

Započnite svoje putovanje s Foundry Local instalacijom i konfiguracijom na Windows 11. Naučite kako postaviti CLI, omogućiti hardversku akceleraciju i predmemorirati modele za brzu lokalnu inferenciju. Ova praktična sesija vodi vas kroz pokretanje modela poput Phi, Qwen, DeepSeek i GPT-OSS-20B koristeći reproducibilne CLI naredbe.

## Ciljevi učenja

Na kraju ove sesije, moći ćete:

- **Instalirati i konfigurirati**: Postaviti Foundry Local na Windows 11 s optimalnim postavkama performansi
- **Savladati CLI operacije**: Koristiti Foundry Local CLI za upravljanje modelima i njihovo postavljanje
- **Omogućiti hardversku akceleraciju**: Konfigurirati GPU akceleraciju s ONNXRuntime ili WebGPU
- **Postaviti više modela**: Pokrenuti phi-4, GPT-OSS-20B, Qwen i DeepSeek modele lokalno
- **Izraditi svoju prvu aplikaciju**: Prilagoditi postojeće primjere za korištenje Foundry Local Python SDK-a

# Testiranje modela (neinteraktivni pojedinačni upit)
foundry model run phi-4-mini --prompt "Pozdrav, predstavi se"

- Windows 11 (22H2 ili noviji)
# Popis dostupnih modela iz kataloga (učitani modeli se pojavljuju nakon pokretanja)
foundry model list
## NOTE: Trenutno ne postoji namjenska oznaka `--running`; da biste vidjeli koji su učitani, pokrenite chat ili pregledajte zapisnike usluge.
- Python 3.10+ instaliran
- Visual Studio Code s Python ekstenzijom
- Administratorske privilegije za instalaciju

### (Opcionalno) Varijable okruženja

Kreirajte `.env` (ili postavite u shell) kako biste skripte učinili prenosivima:
# Usporedba odgovora (neinteraktivno)
foundry model run gpt-oss-20b --prompt "Objasni edge AI jednostavnim riječima"
| Varijabla | Svrha | Primjer |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Preferirani alias modela (katalog automatski odabire najbolju varijantu) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Prekoračenje krajnje točke (inače automatski iz managera) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Omogućuje streaming demo | `true` |

> Ako je `FOUNDRY_LOCAL_ENDPOINT=auto` (ili nije postavljen), deriviramo ga iz SDK managera.

## Demo tijek (30 minuta)

### 1. Instalacija Foundry Local i provjera CLI postavki (10 minuta)

# Popis predmemoriranih modela
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Pregled / Ako je podržano)**

Ako je dostupan izvorni macOS paket (provjerite službenu dokumentaciju za najnovije):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Ako izvorni macOS binarni paketi još nisu dostupni, možete:
1. Koristiti Windows 11 ARM/Intel VM (Parallels / UTM) i slijediti korake za Windows. 
2. Pokrenuti modele putem kontejnera (ako je objavljena slika kontejnera) i postaviti `FOUNDRY_LOCAL_ENDPOINT` na izloženi port. 

**Kreiranje Python virtualnog okruženja (Cross‑Platform)**

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

Ažurirajte pip i instalirajte osnovne ovisnosti:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Korak 1.2: Provjera instalacije

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Korak 1.3: Konfiguracija okruženja

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Preporučeno)

Umjesto ručnog pokretanja usluge i modela, **Foundry Local Python SDK** može automatizirati sve:

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

Ako preferirate eksplicitnu kontrolu, i dalje možete koristiti CLI + OpenAI klijent kao što je prikazano kasnije.

### 2. Pokretanje modela lokalno putem CLI-a (10 minuta)

#### Korak 3.1: Postavljanje Phi-4 modela

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Korak 3.2: Postavljanje GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Korak 3.3: Učitavanje dodatnih modela

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Početni projekt: Prilagodba 01-run-phi za Foundry Local (5 minuta)

#### Korak 4.1: Kreiranje osnovne chat aplikacije

Kreirajte `samples/01-foundry-quickstart/chat_quickstart.py` (ažurirano za korištenje managera ako je dostupan):

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

## Ključni koncepti

### 1. Arhitektura Foundry Local

- **Lokalni inferencijski motor**: Pokreće modele u potpunosti na vašem uređaju
- **Kompatibilnost s OpenAI SDK-om**: Besprijekorna integracija s postojećim OpenAI kodom
- **Upravljanje modelima**: Preuzimanje, predmemoriranje i učinkovito pokretanje više modela
- **Optimizacija hardvera**: Iskoristite GPU, NPU i CPU akceleraciju

### 2. Referenca CLI naredbi

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integracija Python SDK-a

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

## Rješavanje uobičajenih problema

### Problem 1: "Foundry naredba nije pronađena"

**Rješenje:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problem 2: "Model nije učitan"

**Rješenje:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problem 3: "Veza odbijena na localhost:5273"

**Rješenje:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Savjeti za optimizaciju performansi

### 1. Strategija odabira modela

- **Phi-4-mini**: Najbolji za opće zadatke, manja potrošnja memorije
- **Qwen2.5-0.5b**: Najbrža inferencija, minimalni resursi
- **GPT-OSS-20B**: Najviša kvaliteta, zahtijeva više resursa
- **DeepSeek-Coder**: Optimiziran za zadatke programiranja

### 2. Optimizacija hardvera

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Praćenje performansi

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

### Opcionalna poboljšanja

| Poboljšanje | Što | Kako |
|-------------|------|-----|
| Zajedničke korisne funkcije | Uklonite dupliciranu logiku klijenta/bootstrappinga | Koristite `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Vidljivost korištenja tokena | Naučite razmišljanje o troškovima/učinkovitosti rano | Postavite `SHOW_USAGE=1` za ispis prompt/completion/total tokena |
| Determinističke usporedbe | Stabilno testiranje performansi i regresije | Koristite `temperature=0`, `top_p=1`, dosljedan tekst prompta |
| Latencija prvog tokena | Metrika percepcije odziva | Prilagodite skriptu za benchmark sa streamingom (`BENCH_STREAM=1`) |
| Ponovno pokušavanje kod privremenih grešaka | Otpornost na hladni start | `RETRY_ON_FAIL=1` (zadano) i prilagodite `RETRY_BACKOFF` |
| Testiranje funkcionalnosti | Brza provjera ključnih tokova | Pokrenite `python Workshop/tests/smoke.py` prije radionice |
| Profili aliasa modela | Brza promjena skupa modela između uređaja | Održavajte `.env` s `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Učinkovitost predmemoriranja | Izbjegnite ponovljene zagrijavanja u višestrukim pokretanjima | Koristite predmemorirane managere; ponovno koristite između skripti/notebookova |
| Zagrijavanje pri prvom pokretanju | Smanjite p95 latencijske skokove | Pokrenite mali prompt nakon kreiranja `FoundryLocalManager`-a |

Primjer determinističkog toplog početnog stanja (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Trebali biste vidjeti sličan izlaz i identične brojeve tokena pri drugom pokretanju, što potvrđuje determinističnost.

## Sljedeći koraci

Nakon završetka ove sesije:

1. **Istražite Sesiju 2**: Izgradite AI rješenja s Azure AI Foundry RAG
2. **Isprobajte različite modele**: Eksperimentirajte s Qwen, DeepSeek i drugim obiteljima modela
3. **Optimizirajte performanse**: Fino prilagodite postavke za vaš specifični hardver
4. **Izradite prilagođene aplikacije**: Koristite Foundry Local SDK u vlastitim projektima

## Dodatni resursi

### Dokumentacija
- [Foundry Local Python SDK Referenca](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Vodič za instalaciju Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Katalog modela](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Primjeri koda
- [Modul08 Primjer 01](./samples/01/README.md) - REST Chat Quickstart
- [Modul08 Primjer 02](./samples/02/README.md) - Integracija s OpenAI SDK-om
- [Modul08 Primjer 03](./samples/03/README.md) - Otkriće modela i benchmarking

### Zajednica
- [Foundry Local GitHub Rasprave](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Zajednica](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Trajanje sesije**: 30 minuta praktičnog rada + 15 minuta pitanja i odgovora  
**Razina težine**: Početnik  
**Preduvjeti**: Windows 11, Python 3.10+, administratorski pristup  

## Primjer scenarija i mapiranje radionice

| Skripta radionice / Notebook | Scenarij | Cilj | Primjer unosa | Potrebni podaci |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Interni IT tim procjenjuje inferenciju na uređaju za portal procjene privatnosti | Dokazati da lokalni SLM odgovara unutar sub-sekundne latencije na standardne upite | "Navedite dvije prednosti lokalne inferencije." | Nema (pojedinačni upit) |
| Kodni blok za prilagodbu Quickstart-a | Programer migrira postojeću OpenAI skriptu na Foundry Local | Prikazati kompatibilnost bez izmjena | "Navedite dvije prednosti lokalne inferencije." | Samo inline prompt |

### Narativ scenarija
Tim za sigurnost i usklađenost mora potvrditi može li se osjetljivi prototipni podaci obrađivati lokalno. Pokreću bootstrap skriptu s nekoliko upita (privatnost, latencija, trošak) koristeći deterministički način temperature=0 kako bi zabilježili osnovne izlaze za kasniju usporedbu (benchmarking u Sesiji 3 i kontrast SLM vs LLM u Sesiji 4).

### Minimalni JSON skup upita (opcionalno)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Koristite ovaj popis za kreiranje reproducibilne petlje evaluacije ili za inicijalizaciju budućeg testnog okvira za regresiju.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.