<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-12T00:04:31+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "hu"
}
-->
# 1. szekció: Első lépések a Foundry Local használatával

## Összefoglaló

Tanulja meg, hogyan telepítse, konfigurálja és futtassa első AI modelljeit a Microsoft Foundry Local segítségével. Ez a gyakorlati szekció lépésről lépésre bemutatja a helyi inferencia folyamatát, a telepítéstől kezdve az első chat alkalmazás felépítéséig, olyan modellek használatával, mint a Phi-4, Qwen és DeepSeek.

## Tanulási célok

A szekció végére képes lesz:

- **Telepítés és konfiguráció**: A Foundry Local beállítása és a telepítés ellenőrzése
- **CLI műveletek elsajátítása**: A Foundry Local CLI használata modellek kezelésére és telepítésére
- **Első modell futtatása**: Helyi AI modell sikeres telepítése és interakciója
- **Chat alkalmazás készítése**: Alapvető chat alkalmazás létrehozása a Foundry Local Python SDK segítségével
- **Helyi AI megértése**: A helyi inferencia és modellkezelés alapjainak elsajátítása

## Előfeltételek

### Rendszerkövetelmények

- **Windows**: Windows 11 (22H2 vagy újabb) VAGY **macOS**: macOS 11+ (korlátozott támogatás)
- **RAM**: Minimum 8GB, ajánlott 16GB+
- **Tárhely**: Legalább 10GB szabad hely a modellek számára
- **Python**: Telepített 3.10 vagy újabb verzió
- **Adminisztrátori hozzáférés**: Telepítéshez szükséges jogosultság

### Fejlesztői környezet

- Visual Studio Code Python kiterjesztéssel (ajánlott)
- Parancssori hozzáférés (PowerShell Windows-on, Terminal macOS-en)
- Git a repozitóriumok klónozásához (opcionális)

## Workshop menete (30 perc)

### 1. lépés: Foundry Local telepítése (5 perc)

#### Windows telepítés

Telepítse a Foundry Local-t a Windows csomagkezelő segítségével:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatíva: Töltse le közvetlenül a [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install) oldalról.

#### macOS telepítés (korlátozott támogatás)

> [!NOTE] 
> A macOS támogatás jelenleg előzetes verzióban érhető el. Ellenőrizze a hivatalos dokumentációt a legfrissebb információkért.

Ha elérhető, telepítse a Homebrew segítségével:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternatíva macOS felhasználók számára:**
- Használjon Windows 11 virtuális gépet (Parallels/UTM) és kövesse a Windows lépéseit
- Futtassa konténeren keresztül, ha elérhető, és konfigurálja a `FOUNDRY_LOCAL_ENDPOINT`-t

### 2. lépés: Telepítés ellenőrzése (3 perc)

A telepítés után indítsa újra a terminált, és ellenőrizze, hogy a Foundry Local működik:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

A várt kimenetnek tartalmaznia kell a verzióinformációkat és az elérhető parancsokat.

### 3. lépés: Python környezet beállítása (5 perc)

Hozzon létre egy dedikált Python környezetet ehhez a workshophoz:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### 4. lépés: Első modell futtatása (7 perc)

Most futtassuk az első AI modellt helyben!

#### Kezdje a Phi-4 Mini modellel (ajánlott első modell)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Ez a parancs letölti a modellt (első alkalommal) és automatikusan elindítja a Foundry Local szolgáltatást.

#### Ellenőrizze, mi fut

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Próbáljon ki más modelleket

Miután a phi-4-mini működik, kísérletezzen más modellekkel:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### 5. lépés: Első chat alkalmazás készítése (10 perc)

Most hozzunk létre egy Python alkalmazást, amely használja az éppen elindított modelleket.

#### Chat script létrehozása

Hozzon létre egy új fájlt `my_first_chat.py` néven (vagy használja a mellékelt mintát):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Kapcsolódó példák**: További fejlett használathoz lásd:
>
> - **Python példa**: `Workshop/samples/session01/chat_bootstrap.py` - Streaming válaszokkal és hibakezeléssel
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktív verzió részletes magyarázatokkal

#### Chat alkalmazás tesztelése

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatíva: Használja közvetlenül a mellékelt mintákat

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Vagy fedezze fel az interaktív notebookot
Nyissa meg a Workshop/notebooks/session01_chat_bootstrap.ipynb fájlt a VS Code-ban

Próbálja ki ezeket a példabeszélgetéseket:

- "Mi az a Microsoft Foundry Local?"
- "Sorolj fel 3 előnyt a helyi AI modellek futtatásával kapcsolatban"
- "Segíts megérteni az edge AI-t"

## Amit elért

Gratulálunk! Sikeresen:

1. ✅ **Telepítette a Foundry Local-t** és ellenőrizte a működését
2. ✅ **Elindította az első AI modellt** (phi-4-mini) helyben
3. ✅ **Tesztelte különböző modelleket** parancssoron keresztül
4. ✅ **Készített egy chat alkalmazást**, amely csatlakozik a helyi AI-hoz
5. ✅ **Tapasztalatot szerzett a helyi AI inferenciában** felhőfüggőség nélkül

## Mi történt?

### Helyi AI inferencia

- Az AI modellek teljes mértékben az Ön számítógépén futnak
- Nem kerül adat a felhőbe
- A válaszok helyben, a CPU/GPU segítségével generálódnak
- A magánélet és a biztonság megőrzése biztosított

### Modellkezelés

- A `foundry model run` letölti és elindítja a modelleket
- A **FoundryLocalManager SDK** automatikusan kezeli a szolgáltatás indítását és a modellek betöltését
- A modellek helyben tárolódnak a későbbi használatra
- Több modell is letölthető, de általában egyszerre csak egy fut
- A szolgáltatás automatikusan kezeli a modellek életciklusát

### SDK vs CLI megközelítések

- **CLI megközelítés**: Manuális modellkezelés a `foundry model run <model>` parancs segítségével
- **SDK megközelítés**: Automatikus szolgáltatás- és modellkezelés a `FoundryLocalManager(alias)` használatával
- **Ajánlás**: Használja az SDK-t alkalmazásokhoz, a CLI-t teszteléshez és felfedezéshez

## Gyakori parancsok referenciája

### Alapvető CLI parancsok

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Modellajánlások

- **phi-4-mini**: Legjobb kezdő modell - gyors, könnyű, jó minőségű
- **qwen2.5-0.5b**: Leggyorsabb inferencia, minimális memóriahasználat
- **gpt-oss-20b**: Magasabb minőségű válaszok, több erőforrást igényel
- **deepseek-coder-1.3b**: Programozásra és kódolási feladatokra optimalizált

## Hibakeresés

### "Foundry parancs nem található"

**Megoldás:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "A modell betöltése sikertelen"

**Megoldás:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Kapcsolat megtagadva a localhoston"

**Megoldás:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Következő lépések

### Azonnali teendők

1. **Kísérletezzen** különböző modellekkel és kérdésekkel
2. **Módosítsa** a chat alkalmazását, hogy különböző modelleket próbáljon ki
3. **Hozzon létre** saját kérdéseket és tesztelje a válaszokat
4. **Fedezze fel** a 2. szekciót: RAG alkalmazások építése

### Haladó tanulási útvonal

1. **2. szekció**: AI megoldások építése RAG (Retrieval-Augmented Generation) segítségével
2. **3. szekció**: Különböző nyílt forráskódú modellek összehasonlítása
3. **4. szekció**: Legmodernebb modellek használata
4. **5. szekció**: Többügynökös AI rendszerek építése

## Környezeti változók (opcionális)

Haladó használathoz beállíthatja ezeket a környezeti változókat:

| Változó | Cél | Példa |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alapértelmezett modell használata | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Végpont URL felülírása | `http://localhost:5273/v1` |

Hozzon létre egy `.env` fájlt a projekt könyvtárában:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## További források

### Dokumentáció

- [Foundry Local Python SDK Referencia](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Telepítési Útmutató](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modellkatalógus](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Példakódok

- **Session01 Python Minta**: `Workshop/samples/session01/chat_bootstrap.py` - Teljes chat alkalmazás streaminggel
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktív oktatóanyag  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Gyorsindító
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK Integráció
- [Module08 Sample 03](../Module08/samples/03/README.md) - Modell felfedezés és teljesítménytesztelés

### Közösség

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Közösség](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Szekció időtartama**: 30 perc gyakorlati rész + 15 perc kérdések és válaszok  
**Nehézségi szint**: Kezdő  
**Előfeltételek**: Windows 11/macOS 11+, Python 3.10+, Adminisztrátori hozzáférés

## Workshop példa szcenárió

### Valós életbeli kontextus

**Szcenárió**: Egy vállalati IT csapatnak értékelnie kell az eszközön futó AI inferenciát, hogy érzékeny munkavállalói visszajelzéseket dolgozzon fel anélkül, hogy adatokat küldene külső szolgáltatásoknak.

**Célja**: Bizonyítsa be, hogy a helyi AI modellek minőségi válaszokat tudnak nyújtani másodpercek alatti késleltetéssel, miközben teljes adatvédelmet biztosítanak.

### Tesztkérdések

Használja ezeket a kérdéseket a beállítás ellenőrzéséhez:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Sikerességi kritériumok

- ✅ Minden kérdésre 2 másodpercen belül érkezik válasz
- ✅ Nem kerül adat ki a helyi gépről
- ✅ A válaszok relevánsak és hasznosak
- ✅ A chat alkalmazás zökkenőmentesen működik

Ez az ellenőrzés biztosítja, hogy a Foundry Local beállítása készen áll a 2-6. szekciók haladó workshopjaira.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->