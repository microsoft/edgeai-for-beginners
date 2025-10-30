<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T23:47:07+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "lt"
}
-->
# Sesija 1: Pradžia su Foundry Local

## Santrauka

Pradėkite savo kelionę su Foundry Local įdiegdami ir sukonfigūruodami jį Windows 11 sistemoje. Sužinokite, kaip nustatyti CLI, įjungti aparatūros pagreitį ir talpinti modelius greitam vietiniam inferencijai. Ši praktinė sesija parodys, kaip paleisti tokius modelius kaip Phi, Qwen, DeepSeek ir GPT-OSS-20B naudojant atkuriamus CLI komandas.

## Mokymosi tikslai

Šios sesijos pabaigoje jūs:

- **Įdiegsite ir sukonfigūruosite**: Nustatysite Foundry Local Windows 11 sistemoje su optimaliomis našumo nuostatomis
- **Įvaldysite CLI operacijas**: Naudosite Foundry Local CLI modelių valdymui ir diegimui
- **Įjungsite aparatūros pagreitį**: Konfigūruosite GPU pagreitį su ONNXRuntime arba WebGPU
- **Diegsite kelis modelius**: Vietoje paleisite phi-4, GPT-OSS-20B, Qwen ir DeepSeek modelius
- **Sukursite pirmąją programą**: Pritaikysite esamus pavyzdžius naudodami Foundry Local Python SDK

# Testuokite modelį (neinteraktyvus vieno klausimo atsakymas)
foundry model run phi-4-mini --prompt "Sveiki, prisistatykite"

- Windows 11 (22H2 ar naujesnė versija)
# Peržiūrėkite galimus katalogo modelius (įkeltus modelius matysite po paleidimo)
foundry model list
## NOTE: Šiuo metu nėra specialaus `--running` parametro; norėdami pamatyti, kurie modeliai įkelti, pradėkite pokalbį arba patikrinkite paslaugos žurnalus.
- Įdiegta Python 3.10+
- Visual Studio Code su Python plėtiniu
- Administratoriaus teisės diegimui

### (Pasirinktinai) Aplinkos kintamieji

Sukurkite `.env` (arba nustatykite apvalkale), kad scenarijai būtų perkeliamieji:
# Palyginkite atsakymus (neinteraktyvus)
foundry model run gpt-oss-20b --prompt "Paaiškinkite edge AI paprastais terminais"
| Kintamasis | Paskirtis | Pavyzdys |
|------------|-----------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Pageidaujamas modelio alias (katalogas automatiškai parenka geriausią variantą) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Pakeisti galinį tašką (kitaip automatiškai iš valdytojo) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Įjungti srautinį demonstravimą | `true` |

> Jei `FOUNDRY_LOCAL_ENDPOINT=auto` (arba nenustatytas), mes jį gauname iš SDK valdytojo.

## Demonstracijos eiga (30 minučių)

### 1. Įdiekite Foundry Local ir patikrinkite CLI nustatymą (10 minučių)

# Peržiūrėkite talpintus modelius
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Peržiūra / Jei palaikoma)**

Jei pateikiamas natyvus macOS paketas (patikrinkite oficialią dokumentaciją dėl naujausios informacijos):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Jei macOS natyvių dvejetainių failų dar nėra, vis tiek galite: 
1. Naudoti Windows 11 ARM/Intel VM (Parallels / UTM) ir sekti Windows žingsnius. 
2. Paleisti modelius per konteinerį (jei konteinerio vaizdas paskelbtas) ir nustatyti `FOUNDRY_LOCAL_ENDPOINT` į atitinkamą prievadą. 

**Sukurkite Python virtualią aplinką (kryžminė platforma)**

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

Atnaujinkite pip ir įdiekite pagrindines priklausomybes:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### 1.2 žingsnis: Patikrinkite diegimą

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### 1.3 žingsnis: Konfigūruokite aplinką

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK paleidimas (rekomenduojama)

Užuot rankiniu būdu paleidę paslaugą ir modelius, **Foundry Local Python SDK** gali paleisti viską automatiškai:

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

Jei norite turėti aiškią kontrolę, vis tiek galite naudoti CLI + OpenAI klientą, kaip parodyta vėliau.

### 2. Paleiskite modelius vietoje per CLI (10 minučių)

#### 3.1 žingsnis: Diegti Phi-4 modelį

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### 3.2 žingsnis: Diegti GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### 3.3 žingsnis: Įkelti papildomus modelius

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Pradinis projektas: Pritaikyti 01-run-phi Foundry Local (5 minutės)

#### 4.1 žingsnis: Sukurti pagrindinę pokalbių programą

Sukurkite `samples/01-foundry-quickstart/chat_quickstart.py` (atnaujinta naudoti valdytoją, jei yra):

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

#### 4.2 žingsnis: Testuoti programą

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Pagrindinės aptartos sąvokos

### 1. Foundry Local architektūra

- **Vietinis inferencijos variklis**: Modeliai veikia visiškai jūsų įrenginyje
- **OpenAI SDK suderinamumas**: Sklandi integracija su esamu OpenAI kodu
- **Modelių valdymas**: Efektyvus modelių atsisiuntimas, talpinimas ir paleidimas
- **Aparatūros optimizavimas**: Naudojamas GPU, NPU ir CPU pagreitis

### 2. CLI komandų nuoroda

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK integracija

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

## Dažniausiai pasitaikančių problemų sprendimas

### Problema 1: "Foundry komanda nerasta"

**Sprendimas:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problema 2: "Modelis nepavyko įkelti"

**Sprendimas:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problema 3: "Ryšys atmestas localhost:5273"

**Sprendimas:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Našumo optimizavimo patarimai

### 1. Modelio pasirinkimo strategija

- **Phi-4-mini**: Geriausias bendroms užduotims, mažesnis atminties naudojimas
- **Qwen2.5-0.5b**: Greičiausias inferencijos laikas, minimalūs resursai
- **GPT-OSS-20B**: Aukščiausia kokybė, reikalauja daugiau resursų
- **DeepSeek-Coder**: Optimizuotas programavimo užduotims

### 2. Aparatūros optimizavimas

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Našumo stebėjimas

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

### Pasirinktiniai patobulinimai

| Patobulinimas | Kas tai | Kaip |
|---------------|---------|------|
| Bendros priemonės | Pašalinti pasikartojančią kliento/paleidimo logiką | Naudokite `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Žetonų naudojimo matomumas | Mokykite apie kaštus/efektyvumą anksti | Nustatykite `SHOW_USAGE=1`, kad būtų rodomi klausimai/atsakymai/bendras žetonų skaičius |
| Deterministiniai palyginimai | Stabilus našumo testavimas ir regresijos patikrinimai | Naudokite `temperature=0`, `top_p=1`, nuoseklų klausimo tekstą |
| Pirmojo žetono vėlavimas | Matomas atsako greičio rodiklis | Pritaikykite našumo testavimo scenarijų su srautu (`BENCH_STREAM=1`) |
| Pakartotinis bandymas dėl laikinų klaidų | Patikimi demonstravimai šalto paleidimo metu | `RETRY_ON_FAIL=1` (numatytasis) ir koreguokite `RETRY_BACKOFF` |
| Greitas testavimas | Greitas pagrindinių funkcijų patikrinimas | Paleiskite `python Workshop/tests/smoke.py` prieš dirbtuves |
| Modelio alias profiliai | Greitas modelių rinkinio keitimas tarp mašinų | Išlaikykite `.env` su `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Talpinimo efektyvumas | Venkite pakartotinių įkaitimų daugybės pavyzdžių paleidime | Naudokite talpinimo valdytojus; pakartotinai naudokite scenarijuose/užrašuose |
| Pirmojo paleidimo įkaitimas | Sumažinkite p95 vėlavimo šuolius | Paleiskite trumpą klausimą po `FoundryLocalManager` sukūrimo |

Pavyzdys deterministinio šilto paleidimo (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Turėtumėte matyti panašų rezultatą ir identišką žetonų skaičių antrame paleidime, patvirtinant deterministiškumą.

## Kiti žingsniai

Baigę šią sesiją:

1. **Išbandykite 2 sesiją**: Kurkite AI sprendimus su Azure AI Foundry RAG
2. **Išbandykite skirtingus modelius**: Eksperimentuokite su Qwen, DeepSeek ir kitomis modelių šeimomis
3. **Optimizuokite našumą**: Tobulinkite nustatymus pagal savo specifinę aparatūrą
4. **Kurkite pritaikytas programas**: Naudokite Foundry Local SDK savo projektuose

## Papildomi ištekliai

### Dokumentacija
- [Foundry Local Python SDK nuoroda](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local diegimo vadovas](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modelių katalogas](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Pavyzdinis kodas
- [Module08 Pavyzdys 01](./samples/01/README.md) - REST pokalbių greitas startas
- [Module08 Pavyzdys 02](./samples/02/README.md) - OpenAI SDK integracija
- [Module08 Pavyzdys 03](./samples/03/README.md) - Modelių atradimas ir našumo testavimas

### Bendruomenė
- [Foundry Local GitHub diskusijos](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI bendruomenė](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sesijos trukmė**: 30 minučių praktika + 15 minučių klausimai ir atsakymai  
**Sudėtingumo lygis**: Pradedantysis  
**Būtinos sąlygos**: Windows 11, Python 3.10+, administratoriaus prieiga  

## Pavyzdinė situacija ir dirbtuvių susiejimas

| Dirbtuvių scenarijus / užrašų knygelė | Situacija | Tikslas | Pavyzdiniai įvesties duomenys | Reikalingas duomenų rinkinys |
|--------------------------------------|-----------|--------|-----------------------------|-----------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Vidinė IT komanda vertina vietinę inferenciją privatumo vertinimo portale | Įrodyti, kad vietinis SLM atsako per mažiau nei sekundę į standartinius klausimus | "Išvardinkite dvi vietinės inferencijos naudas." | Nėra (vienas klausimas) |
| Greito starto adaptacijos kodo blokas | Kūrėjas, perkeliantis esamą OpenAI scenarijų į Foundry Local | Parodyti lengvą suderinamumą | "Išvardinkite dvi vietinės inferencijos naudas." | Tik įterptas klausimas |

### Situacijos pasakojimas
Saugumo ir atitikties komanda turi patikrinti, ar jautri prototipų duomenų apdorojimas gali būti atliekamas vietoje. Jie paleidžia paleidimo scenarijų su keliais klausimais (privatumas, vėlavimas, kaštai), naudodami deterministinį temperature=0 režimą, kad užfiksuotų pradinius rezultatus vėlesniam palyginimui (3 sesijos našumo testavimas ir 4 sesijos SLM vs LLM kontrastas).

### Minimalus klausimų rinkinys JSON (pasirinktinai)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Naudokite šį sąrašą, kad sukurtumėte atkuriamą vertinimo ciklą arba inicijuotumėte būsimą regresijos testavimo sistemą.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.