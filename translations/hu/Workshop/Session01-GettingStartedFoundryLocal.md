<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T22:55:25+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "hu"
}
-->
# 1. szekció: Bevezetés a Foundry Local használatába

## Összefoglaló

Kezdd el az utadat a Foundry Local használatával, telepítsd és konfiguráld Windows 11 rendszeren. Ismerd meg a CLI beállítását, a hardveres gyorsítás engedélyezését, valamint a modellek gyors helyi következtetéshez történő gyorsítótárazását. Ez a gyakorlati szekció bemutatja, hogyan futtathatók modellek, mint például Phi, Qwen, DeepSeek és GPT-OSS-20B reprodukálható CLI parancsok segítségével.

## Tanulási célok

A szekció végére képes leszel:

- **Telepítés és konfigurálás**: Állítsd be a Foundry Local-t Windows 11 rendszeren optimális teljesítménybeállításokkal
- **CLI műveletek elsajátítása**: Használd a Foundry Local CLI-t modellek kezelésére és telepítésére
- **Hardveres gyorsítás engedélyezése**: Konfiguráld a GPU gyorsítást ONNXRuntime vagy WebGPU segítségével
- **Több modell telepítése**: Futtasd helyben a phi-4, GPT-OSS-20B, Qwen és DeepSeek modelleket
- **Első alkalmazásod létrehozása**: Alkalmazd a meglévő mintákat a Foundry Local Python SDK használatával

# Modell tesztelése (nem interaktív, egyetlen prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 vagy újabb)
# Elérhető katalógusmodellek listázása (a betöltött modellek megjelennek futtatás után)
foundry model list
## MEGJEGYZÉS: Jelenleg nincs dedikált `--running` flag; a betöltött modellek megtekintéséhez indíts el egy chatet vagy ellenőrizd a szolgáltatás naplóit.
- Telepített Python 3.10+
- Visual Studio Code Python bővítménnyel
- Adminisztrátori jogosultságok a telepítéshez

### (Opcionális) Környezeti változók

Hozz létre egy `.env` fájlt (vagy állítsd be a shellben), hogy a szkriptek hordozhatóak legyenek:
# Válaszok összehasonlítása (nem interaktív)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| Változó | Cél | Példa |
|---------|-----|-------|
| `FOUNDRY_LOCAL_ALIAS` | Preferált modell alias (a katalógus automatikusan kiválasztja a legjobb változatot) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Végpont felülírása (egyébként automatikusan a menedzserből) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Streaming demó engedélyezése | `true` |

> Ha `FOUNDRY_LOCAL_ENDPOINT=auto` (vagy nincs beállítva), az SDK menedzserből származtatjuk.

## Demó menete (30 perc)

### 1. Foundry Local telepítése és CLI beállítás ellenőrzése (10 perc)

# Gyorsítótárazott modellek listázása
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Előzetes / Ha támogatott)**

Ha natív macOS csomag elérhető (ellenőrizd a hivatalos dokumentációt a legfrissebb információkért):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Ha a macOS natív binárisok még nem elérhetők, akkor:
1. Használj Windows 11 ARM/Intel VM-et (Parallels / UTM) és kövesd a Windows lépéseit.
2. Futtasd a modelleket konténeren keresztül (ha közzétett konténerkép elérhető), és állítsd be a `FOUNDRY_LOCAL_ENDPOINT`-ot az expozált portra.

**Python virtuális környezet létrehozása (platformfüggetlen)**

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

Frissítsd a pipet és telepítsd az alapvető függőségeket:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### 1.2 lépés: Telepítés ellenőrzése

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### 1.3 lépés: Környezet konfigurálása

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Ajánlott)

A szolgáltatás manuális indítása és a modellek futtatása helyett a **Foundry Local Python SDK** mindent automatikusan elindíthat:

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

Ha inkább explicit kontrollt szeretnél, továbbra is használhatod a CLI-t + OpenAI klienst, ahogy később bemutatjuk.

### 2. Modellek helyi futtatása CLI-n keresztül (10 perc)

#### 3.1 lépés: Phi-4 modell telepítése

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### 3.2 lépés: GPT-OSS-20B telepítése

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### 3.3 lépés: További modellek betöltése

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Kezdő projekt: 01-run-phi adaptálása Foundry Local-hoz (5 perc)

#### 4.1 lépés: Alapvető chat alkalmazás létrehozása

Hozz létre `samples/01-foundry-quickstart/chat_quickstart.py` fájlt (frissítve a menedzser használatára, ha elérhető):

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

#### 4.2 lépés: Az alkalmazás tesztelése

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Főbb fogalmak

### 1. Foundry Local architektúra

- **Helyi következtetési motor**: Teljesen a saját eszközödön futtatja a modelleket
- **OpenAI SDK kompatibilitás**: Zökkenőmentes integráció a meglévő OpenAI kóddal
- **Modellek kezelése**: Modellek letöltése, gyorsítótárazása és hatékony futtatása
- **Hardver optimalizálás**: GPU, NPU és CPU gyorsítás kihasználása

### 2. CLI parancs referencia

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK integráció

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

## Gyakori problémák elhárítása

### Probléma 1: "Foundry parancs nem található"

**Megoldás:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Probléma 2: "A modell betöltése sikertelen"

**Megoldás:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Probléma 3: "Kapcsolat megtagadva a localhost:5273 címen"

**Megoldás:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Teljesítmény optimalizálási tippek

### 1. Modellválasztási stratégia

- **Phi-4-mini**: Általános feladatokra a legjobb, alacsony memóriahasználat
- **Qwen2.5-0.5b**: Leggyorsabb következtetés, minimális erőforrásigény
- **GPT-OSS-20B**: Legmagasabb minőség, több erőforrást igényel
- **DeepSeek-Coder**: Programozási feladatokra optimalizált

### 2. Hardver optimalizálás

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Teljesítmény monitorozása

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

### Opcionális fejlesztések

| Fejlesztés | Mi ez | Hogyan |
|------------|-------|--------|
| Megosztott segédprogramok | Távolítsd el az ismétlődő kliens/bootstrapping logikát | Használd a `Workshop/samples/workshop_utils.py` fájlt (`get_client`, `chat_once`) |
| Tokenhasználat láthatósága | Tanítsd meg a költség/hatékonyság gondolkodást korán | Állítsd be a `SHOW_USAGE=1` értéket, hogy megjelenítse a prompt/completion/összes tokeneket |
| Determinisztikus összehasonlítások | Stabil benchmarking és regresszió ellenőrzések | Használj `temperature=0`, `top_p=1`, következetes prompt szöveget |
| Első token késleltetés | Érzékelt válaszidő metrika | Alkalmazd a benchmark szkriptet streaminggel (`BENCH_STREAM=1`) |
| Újrapróbálkozás átmeneti hibák esetén | Ellenálló demók hidegindításkor | `RETRY_ON_FAIL=1` (alapértelmezett) és állítsd be a `RETRY_BACKOFF` értéket |
| Füsttesztelés | Gyors ellenőrzés a kulcsfolyamatokon | Futtasd a `python Workshop/tests/smoke.py` fájlt workshop előtt |
| Modell alias profilok | Gyorsan váltogatható modellkészlet gépek között | Tartsd fenn a `.env` fájlt `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` értékekkel |
| Gyorsítótárazási hatékonyság | Kerüld el az ismételt bemelegítéseket több minta futtatásakor | Segédprogramok gyorsítótár menedzserekhez; használd újra szkriptek/notebookok között |
| Első futtatás bemelegítése | Csökkentsd a p95 késleltetési csúcsokat | Indíts egy apró promptot a `FoundryLocalManager` létrehozása után |

Példa determinisztikus meleg alapvonal (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Hasonló kimenetet és azonos token számokat kell látnod a második futtatáskor, megerősítve a determinisztikusságot.

## Következő lépések

A szekció befejezése után:

1. **Fedezd fel a 2. szekciót**: AI megoldások építése Azure AI Foundry RAG segítségével
2. **Próbálj ki különböző modelleket**: Kísérletezz Qwen, DeepSeek és más modellcsaládokkal
3. **Optimalizáld a teljesítményt**: Finomhangold a beállításokat a saját hardveredhez
4. **Építs egyedi alkalmazásokat**: Használd a Foundry Local SDK-t saját projektjeidben

## További források

### Dokumentáció
- [Foundry Local Python SDK Referencia](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Telepítési Útmutató](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modellek katalógusa](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Példakód
- [Module08 Minta 01](./samples/01/README.md) - REST Chat Gyorsindítás
- [Module08 Minta 02](./samples/02/README.md) - OpenAI SDK Integráció
- [Module08 Minta 03](./samples/03/README.md) - Modell felfedezés és benchmarking

### Közösség
- [Foundry Local GitHub Beszélgetések](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Közösség](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Szekció időtartama**: 30 perc gyakorlati + 15 perc kérdések és válaszok
**Nehézségi szint**: Kezdő
**Előfeltételek**: Windows 11, Python 3.10+, Adminisztrátori hozzáférés

## Példa szcenárió és workshop térkép

| Workshop szkript / notebook | Szcenárió | Cél | Példa bemenet(ek) | Szükséges adatállomány |
|-----------------------------|-----------|-----|-------------------|------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Belső IT csapat, amely az eszközön történő következtetést értékeli egy adatvédelmi portálhoz | Bizonyítsd, hogy a helyi SLM szubszekundum késleltetéssel válaszol standard promptokra | "Sorolj fel két előnyt a helyi következtetésről." | Nincs (egyetlen prompt) |
| Gyorsindítás adaptációs kódblokk | Fejlesztő, aki egy meglévő OpenAI szkriptet migrál Foundry Local-ra | Mutasd meg a kompatibilitást | "Sorolj fel két előnyt a helyi következtetésről." | Csak inline prompt |

### Szcenárió narratíva
A biztonsági és megfelelőségi csapatnak validálnia kell, hogy érzékeny prototípusadatok helyben feldolgozhatók-e. Futtatják a bootstrap szkriptet több prompttal (adatvédelem, késleltetés, költség) determinisztikus `temperature=0` módban, hogy rögzítsék az alapvető kimeneteket későbbi összehasonlításhoz (3. szekció benchmarking és 4. szekció SLM vs LLM kontraszt).

### Minimális prompt készlet JSON (opcionális)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Használd ezt a listát reprodukálható értékelési ciklus létrehozásához vagy egy jövőbeli regressziós teszt keret magjának.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.