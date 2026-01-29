# Sesija 1: Početak rada s Foundry Local

## Sažetak

Naučite kako instalirati, konfigurirati i pokrenuti svoje prve AI modele koristeći Microsoft Foundry Local. Ova praktična sesija pruža korak-po-korak uvod u lokalnu inferenciju, od instalacije do izrade vaše prve aplikacije za chat koristeći modele poput Phi-4, Qwen i DeepSeek.

## Ciljevi učenja

Na kraju ove sesije, moći ćete:

- **Instalirati i konfigurirati**: Postaviti Foundry Local uz pravilnu provjeru instalacije
- **Savladati CLI operacije**: Koristiti Foundry Local CLI za upravljanje modelima i njihovo postavljanje
- **Pokrenuti svoj prvi model**: Uspješno postaviti i interaktirati s lokalnim AI modelom
- **Izraditi aplikaciju za chat**: Kreirati osnovnu aplikaciju za chat koristeći Foundry Local Python SDK
- **Razumjeti lokalni AI**: Shvatiti osnove lokalne inferencije i upravljanja modelima

## Preduvjeti

### Sistemski zahtjevi

- **Windows**: Windows 11 (22H2 ili noviji) ILI **macOS**: macOS 11+ (ograničena podrška)
- **RAM**: Minimalno 8GB, preporučeno 16GB+
- **Pohrana**: 10GB+ slobodnog prostora za modele
- **Python**: Verzija 3.10 ili novija
- **Administratorski pristup**: Privilegije administratora za instalaciju

### Razvojno okruženje

- Visual Studio Code s Python ekstenzijom (preporučeno)
- Pristup naredbenom retku (PowerShell na Windowsu, Terminal na macOS-u)
- Git za kloniranje repozitorija (opcionalno)

## Tijek radionice (30 minuta)

### Korak 1: Instalacija Foundry Local (5 minuta)

#### Instalacija na Windowsu

Instalirajte Foundry Local koristeći Windows upravitelj paketa:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativa: Preuzmite direktno s [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Instalacija na macOS-u (ograničena podrška)

> [!NOTE] 
> Podrška za macOS trenutno je u fazi pregleda. Provjerite službenu dokumentaciju za najnovije informacije.

Ako je dostupno, instalirajte koristeći Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativa za korisnike macOS-a:**
- Koristite Windows 11 VM (Parallels/UTM) i slijedite korake za Windows
- Pokrenite putem kontejnera ako je dostupno i konfigurirajte `FOUNDRY_LOCAL_ENDPOINT`

### Korak 2: Provjera instalacije (3 minute)

Nakon instalacije, ponovno pokrenite terminal i provjerite radi li Foundry Local:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Očekivani izlaz trebao bi prikazati informacije o verziji i dostupnim naredbama.

### Korak 3: Postavljanje Python okruženja (5 minuta)

Kreirajte posvećeno Python okruženje za ovu radionicu:

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

### Korak 4: Pokrenite svoj prvi model (7 minuta)

Sada pokrenimo naš prvi AI model lokalno!

#### Početak s Phi-4 Mini (preporučeni prvi model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Ova naredba preuzima model (prvi put) i automatski pokreće Foundry Local uslugu.

#### Provjerite što je pokrenuto

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Isprobajte različite modele

Kada phi-4-mini radi, eksperimentirajte s drugim modelima:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Korak 5: Izradite svoju prvu aplikaciju za chat (10 minuta)

Sada kreirajmo Python aplikaciju koja koristi modele koje smo upravo pokrenuli.

#### Kreirajte skriptu za chat

Kreirajte novu datoteku pod nazivom `my_first_chat.py` (ili koristite priloženi uzorak):

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
> **Povezani primjeri**: Za naprednije korištenje, pogledajte:
>
> - **Python uzorak**: `Workshop/samples/session01/chat_bootstrap.py` - Uključuje streaming odgovora i rukovanje greškama
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktivna verzija s detaljnim objašnjenjima

#### Testirajte svoju aplikaciju za chat

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativa: Koristite priložene uzorke direktno

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Ili istražite interaktivni notebook
Otvorite Workshop/notebooks/session01_chat_bootstrap.ipynb u VS Code

Isprobajte ove primjere razgovora:

- "Što je Microsoft Foundry Local?"
- "Navedite 3 prednosti pokretanja AI modela lokalno"
- "Pomozite mi razumjeti edge AI"

## Što ste postigli

Čestitamo! Uspješno ste:

1. ✅ **Instalirali Foundry Local** i provjerili da radi
2. ✅ **Pokrenuli svoj prvi AI model** (phi-4-mini) lokalno
3. ✅ **Testirali različite modele** putem naredbenog retka
4. ✅ **Izradili aplikaciju za chat** koja se povezuje s vašim lokalnim AI-jem
5. ✅ **Iskusili lokalnu AI inferenciju** bez ovisnosti o oblaku

## Razumijevanje što se dogodilo

### Lokalna AI inferencija

- Vaši AI modeli rade potpuno na vašem računalu
- Nijedni podaci se ne šalju u oblak
- Odgovori se generiraju lokalno koristeći vaš CPU/GPU
- Privatnost i sigurnost su očuvani

### Upravljanje modelima

- `foundry model run` preuzima i pokreće modele
- **FoundryLocalManager SDK** automatski upravlja pokretanjem usluge i učitavanjem modela
- Modeli se lokalno pohranjuju za buduću upotrebu
- Više modela može biti preuzeto, ali obično se pokreće samo jedan odjednom
- Usluga automatski upravlja životnim ciklusom modela

### SDK vs CLI pristupi

- **CLI pristup**: Ručno upravljanje modelima s `foundry model run <model>`
- **SDK pristup**: Automatsko upravljanje uslugom i modelima s `FoundryLocalManager(alias)`
- **Preporuka**: Koristite SDK za aplikacije, CLI za testiranje i istraživanje

## Referenca za uobičajene naredbe

### Osnovne CLI naredbe

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

### Preporuke za modele

- **phi-4-mini**: Najbolji početni model - brz, lagan, dobre kvalitete
- **qwen2.5-0.5b**: Najbrža inferencija, minimalna potrošnja memorije
- **gpt-oss-20b**: Kvalitetniji odgovori, zahtijeva više resursa
- **deepseek-coder-1.3b**: Optimiziran za programiranje i zadatke vezane uz kod

## Rješavanje problema

### "Foundry naredba nije pronađena"

**Rješenje:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model nije uspio učitati"

**Rješenje:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Veza odbijena na localhostu"

**Rješenje:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Sljedeći koraci

### Neposredne sljedeće akcije

1. **Eksperimentirajte** s različitim modelima i upitima
2. **Modificirajte** svoju aplikaciju za chat kako biste isprobali različite modele
3. **Kreirajte** vlastite upite i testirajte odgovore
4. **Istražite** Sesiju 2: Izrada RAG aplikacija

### Napredni put učenja

1. **Sesija 2**: Izradite AI rješenja s RAG (Retrieval-Augmented Generation)
2. **Sesija 3**: Usporedite različite open-source modele
3. **Sesija 4**: Radite s najnovijim modelima
4. **Sesija 5**: Izradite AI sustave s više agenata

## Varijable okruženja (opcionalno)

Za naprednije korištenje, možete postaviti ove varijable okruženja:

| Varijabla | Svrha | Primjer |
|-----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Zadani model za korištenje | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Prekoračenje URL-a za endpoint | `http://localhost:5273/v1` |

Kreirajte `.env` datoteku u direktoriju vašeg projekta:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Dodatni resursi

### Dokumentacija

- [Foundry Local Python SDK Referenca](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Vodič za instalaciju Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Katalog modela](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Uzorci koda

- **Session01 Python uzorak**: `Workshop/samples/session01/chat_bootstrap.py` - Kompletna aplikacija za chat sa streamingom
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktivni vodič  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - Integracija OpenAI SDK-a
- [Module08 Sample 03](../Module08/samples/03/README.md) - Otkriće modela i benchmarking

### Zajednica

- [Foundry Local GitHub Rasprave](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Zajednica](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Trajanje sesije**: 30 minuta praktičnog rada + 15 minuta pitanja i odgovora  
**Razina težine**: Početnik  
**Preduvjeti**: Windows 11/macOS 11+, Python 3.10+, administratorski pristup

## Primjer scenarija radionice

### Kontekst iz stvarnog svijeta

**Scenarij**: IT tim u poduzeću treba procijeniti AI inferenciju na uređaju za obradu osjetljivih povratnih informacija zaposlenika bez slanja podataka vanjskim servisima.

**Vaš cilj**: Demonstrirati da lokalni AI modeli mogu pružiti kvalitetne odgovore s latencijom manjom od sekunde uz potpuno očuvanje privatnosti podataka.

### Testni upiti

Koristite ove upite za validaciju vašeg postava:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Kriteriji uspjeha

- ✅ Svi upiti dobivaju odgovore u manje od 2 sekunde
- ✅ Nijedni podaci ne napuštaju vaše lokalno računalo
- ✅ Odgovori su relevantni i korisni
- ✅ Vaša aplikacija za chat radi glatko

Ova validacija osigurava da je vaš Foundry Local postav spreman za napredne radionice u Sesijama 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->