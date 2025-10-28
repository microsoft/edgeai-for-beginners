<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:26:52+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ro"
}
-->
# Sesiunea 1: Începeți cu Foundry Local

## Rezumat

Începeți călătoria cu Foundry Local prin instalarea și configurarea acestuia pe Windows 11. Aflați cum să configurați CLI-ul, să activați accelerarea hardware și să cache-uiți modelele pentru inferență locală rapidă. Această sesiune practică vă ghidează prin rularea modelelor precum Phi, Qwen, DeepSeek și GPT-OSS-20B folosind comenzi CLI reproducibile.

## Obiective de învățare

Până la sfârșitul acestei sesiuni, veți putea:

- **Instala și Configura**: Configurați Foundry Local pe Windows 11 cu setări optime de performanță
- **Stăpâni Operațiunile CLI**: Utilizați CLI-ul Foundry Local pentru gestionarea și implementarea modelelor
- **Activa Accelerarea Hardware**: Configurați accelerarea GPU cu ONNXRuntime sau WebGPU
- **Implementa Mai Multe Modele**: Rulați modelele phi-4, GPT-OSS-20B, Qwen și DeepSeek local
- **Construiți Prima Aplicație**: Adaptați exemplele existente pentru a utiliza SDK-ul Python Foundry Local

# Testați modelul (prompt unic non-interactiv)
foundry model run phi-4-mini --prompt "Salut, prezintă-te"

- Windows 11 (22H2 sau mai recent)
# Listați modelele disponibile din catalog (modelele încărcate apar după rulare)
foundry model list
## NOTĂ: În prezent nu există un flag dedicat `--running`; pentru a vedea care sunt încărcate, inițiați un chat sau inspectați jurnalele serviciului.
- Python 3.10+ instalat
- Visual Studio Code cu extensia Python
- Privilegii de administrator pentru instalare

### (Opțional) Variabile de Mediu

Creați un fișier `.env` (sau setați în shell) pentru a face scripturile portabile:
# Comparați răspunsurile (non-interactiv)
foundry model run gpt-oss-20b --prompt "Explică AI edge în termeni simpli"
| Variabilă | Scop | Exemplu |
|-----------|------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias preferat pentru model (catalogul selectează automat cea mai bună variantă) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Suprascrie endpoint-ul (altfel se determină automat din manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Activează demonstrația de streaming | `true` |

> Dacă `FOUNDRY_LOCAL_ENDPOINT=auto` (sau nu este setat), acesta este derivat din managerul SDK.

## Fluxul Demo (30 minute)

### 1. Instalați Foundry Local și Verificați Configurarea CLI (10 minute)

# Listați modelele cache-uite
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Previzualizare / Dacă este Suportat)**

Dacă este disponibil un pachet nativ macOS (verificați documentația oficială pentru cele mai recente informații):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Dacă binarele native macOS nu sunt încă disponibile, puteți totuși: 
1. Utilizați o mașină virtuală Windows 11 ARM/Intel (Parallels / UTM) și urmați pașii pentru Windows. 
2. Rulați modelele prin container (dacă imaginea containerului este publicată) și setați `FOUNDRY_LOCAL_ENDPOINT` la portul expus. 

**Creați un Mediu Virtual Python (Cross‑Platform)**

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

Actualizați pip și instalați dependențele de bază:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Pasul 1.2: Verificați Instalarea

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Pasul 1.3: Configurați Mediul

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Bootstrap SDK (Recomandat)

În loc să porniți manual serviciul și să rulați modelele, **Foundry Local Python SDK** poate inițializa totul:

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

Dacă preferați control explicit, puteți utiliza în continuare CLI-ul + clientul OpenAI, așa cum este prezentat mai târziu.

### 2. Rulați Modele Local prin CLI (10 minute)

#### Pasul 3.1: Implementați Modelul Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Pasul 3.2: Implementați GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Pasul 3.3: Încărcați Modele Suplimentare

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Proiect de Start: Adaptați 01-run-phi pentru Foundry Local (5 minute)

#### Pasul 4.1: Creați o Aplicație de Chat de Bază

Creați `samples/01-foundry-quickstart/chat_quickstart.py` (actualizat pentru a utiliza managerul dacă este disponibil):

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

#### Pasul 4.2: Testați Aplicația

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Concepte Cheie Acoperite

### 1. Arhitectura Foundry Local

- **Motor de Inferență Locală**: Rulează modelele complet pe dispozitivul dvs.
- **Compatibilitate SDK OpenAI**: Integrare fără probleme cu codul OpenAI existent
- **Gestionarea Modelelor**: Descărcați, cache-uiți și rulați eficient mai multe modele
- **Optimizare Hardware**: Utilizați accelerarea GPU, NPU și CPU

### 2. Referință Comenzi CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integrarea SDK Python

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

## Rezolvarea Problemelor Comune

### Problema 1: "Comanda Foundry nu a fost găsită"

**Soluție:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problema 2: "Modelul nu a reușit să se încarce"

**Soluție:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problema 3: "Conexiune refuzată pe localhost:5273"

**Soluție:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Sfaturi pentru Optimizarea Performanței

### 1. Strategia de Selectare a Modelului

- **Phi-4-mini**: Cel mai bun pentru sarcini generale, consum redus de memorie
- **Qwen2.5-0.5b**: Inferență rapidă, resurse minime
- **GPT-OSS-20B**: Cea mai înaltă calitate, necesită mai multe resurse
- **DeepSeek-Coder**: Optimizat pentru sarcini de programare

### 2. Optimizare Hardware

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Monitorizarea Performanței

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

### Îmbunătățiri Opționale

| Îmbunătățire | Ce | Cum |
|--------------|----|-----|
| Utilități Partajate | Eliminarea logicii duplicate client/bootstrap | Utilizați `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Vizibilitatea Utilizării Token-urilor | Predați gândirea cost/eficiență devreme | Setați `SHOW_USAGE=1` pentru a afișa prompt/completare/token-uri totale |
| Comparații Deterministe | Benchmarking stabil și verificări de regresie | Utilizați `temperature=0`, `top_p=1`, text prompt consistent |
| Latența Primului Token | Metrică de receptivitate percepută | Adaptați scriptul de benchmark cu streaming (`BENCH_STREAM=1`) |
| Retry la Erori Tranzitorii | Demonstrații rezistente la pornire rece | `RETRY_ON_FAIL=1` (implicit) și ajustați `RETRY_BACKOFF` |
| Testare Fum | Verificare rapidă a fluxurilor cheie | Rulați `python Workshop/tests/smoke.py` înainte de un workshop |
| Profiluri Alias Model | Pivotare rapidă între seturi de modele pe mașini diferite | Mențineți `.env` cu `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Eficiența Cache-ului | Evitați încălzirea repetată în rulările multi-sample | Managerii de cache utilități; reutilizați între scripturi/notebook-uri |
| Încălzirea la Prima Rulare | Reduceți vârfurile de latență p95 | Lansați un prompt mic după crearea `FoundryLocalManager`

Exemplu de bază determinist cald (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Ar trebui să vedeți o ieșire similară și număr identic de token-uri la a doua rulare, confirmând determinismul.

## Pași Următori

După finalizarea acestei sesiuni:

1. **Explorați Sesiunea 2**: Construiți soluții AI cu Azure AI Foundry RAG
2. **Încercați Modele Diferite**: Experimentați cu Qwen, DeepSeek și alte familii de modele
3. **Optimizați Performanța**: Ajustați setările pentru hardware-ul dvs. specific
4. **Construiți Aplicații Personalizate**: Utilizați SDK-ul Foundry Local în propriile proiecte

## Resurse Suplimentare

### Documentație
- [Referință SDK Python Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Ghid de Instalare Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catalog de Modele](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Cod Exemplu
- [Exemplu Modulul08 01](./samples/01/README.md) - REST Chat Quickstart
- [Exemplu Modulul08 02](./samples/02/README.md) - Integrare SDK OpenAI
- [Exemplu Modulul08 03](./samples/03/README.md) - Descoperirea și Benchmarking-ul Modelului

### Comunitate
- [Discuții Foundry Local pe GitHub](https://github.com/microsoft/Foundry-Local/discussions)
- [Comunitatea Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Durata Sesiunii**: 30 minute practică + 15 minute Q&A  
**Nivel de Dificultate**: Începător  
**Cerințe Prealabile**: Windows 11, Python 3.10+, Acces de Administrator

## Scenariu Exemplu & Mapare Workshop

| Script / Notebook Workshop | Scenariu | Obiectiv | Exemplu Input-uri | Dataset Necesitat |
|----------------------------|----------|----------|--------------------|-------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Echipa IT internă evaluează inferența pe dispozitiv pentru un portal de evaluare a confidențialității | Demonstrați că SLM local răspunde cu o latență sub o secundă la prompturi standard | "Enumerați două beneficii ale inferenței locale." | Niciunul (prompt unic) |
| Cod de adaptare quickstart | Dezvoltator care migrează un script OpenAI existent la Foundry Local | Arătați compatibilitatea directă | "Oferiți două beneficii ale inferenței locale." | Doar prompt inline |

### Narațiunea Scenariului
Echipa de securitate și conformitate trebuie să valideze dacă datele sensibile ale prototipului pot fi procesate local. Ei rulează scriptul bootstrap cu mai multe prompturi (confidențialitate, latență, cost) folosind un mod determinist temperature=0 pentru a captura ieșirile de bază pentru comparații ulterioare (benchmarking în Sesiunea 3 și contrast SLM vs LLM în Sesiunea 4).

### Set Minimal de Prompturi JSON (opțional)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Utilizați această listă pentru a crea un ciclu de evaluare reproducibil sau pentru a inițializa un viitor sistem de testare regresivă.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.