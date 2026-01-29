# Seja 1: Začetek z Foundry Local

## Povzetek

Naučite se namestiti, konfigurirati in zagnati svoje prve AI modele z uporabo Microsoft Foundry Local. Ta praktična seja ponuja korak za korakom uvod v lokalno sklepanje, od namestitve do izdelave vaše prve aplikacije za klepet z modeli, kot so Phi-4, Qwen in DeepSeek.

## Cilji učenja

Do konca te seje boste:

- **Namestili in konfigurirali**: Nastavili Foundry Local z ustrezno preveritvijo namestitve
- **Obvladali CLI operacije**: Uporabili Foundry Local CLI za upravljanje in uvajanje modelov
- **Zagnali svoj prvi model**: Uspešno uvedli in interagirali z lokalnim AI modelom
- **Izdelali aplikacijo za klepet**: Ustvarili osnovno aplikacijo za klepet z uporabo Foundry Local Python SDK
- **Razumeli lokalni AI**: Pridobili osnovno razumevanje lokalnega sklepanja in upravljanja modelov

## Predpogoji

### Zahteve sistema

- **Windows**: Windows 11 (22H2 ali novejši) ALI **macOS**: macOS 11+ (omejena podpora)
- **RAM**: najmanj 8GB, priporočeno 16GB+
- **Shramba**: najmanj 10GB prostega prostora za modele
- **Python**: nameščen 3.10 ali novejši
- **Dostop skrbnika**: Privilegiji skrbnika za namestitev

### Razvojno okolje

- Visual Studio Code z razširitvijo za Python (priporočeno)
- Dostop do ukazne vrstice (PowerShell na Windows, Terminal na macOS)
- Git za kloniranje repozitorijev (neobvezno)

## Potek delavnice (30 minut)

### Korak 1: Namestitev Foundry Local (5 minut)

#### Namestitev na Windows

Namestite Foundry Local z uporabo upravitelja paketov za Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativa: Prenesite neposredno z [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Namestitev na macOS (omejena podpora)

> [!NOTE] 
> Podpora za macOS je trenutno v predogledu. Preverite uradno dokumentacijo za najnovejšo razpoložljivost.

Če je na voljo, namestite z uporabo Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativa za uporabnike macOS:**
- Uporabite Windows 11 VM (Parallels/UTM) in sledite korakom za Windows
- Zaženite prek kontejnerja, če je na voljo, in konfigurirajte `FOUNDRY_LOCAL_ENDPOINT`

### Korak 2: Preverjanje namestitve (3 minute)

Po namestitvi znova zaženite terminal in preverite, ali Foundry Local deluje:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Pričakovani izhod naj prikazuje informacije o različici in razpoložljive ukaze.

### Korak 3: Nastavitev Python okolja (5 minut)

Ustvarite namensko Python okolje za to delavnico:

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

### Korak 4: Zagon vašega prvega modela (7 minut)

Zdaj zaženimo naš prvi AI model lokalno!

#### Začnite s Phi-4 Mini (priporočen prvi model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Ta ukaz prenese model (prvič) in samodejno zažene storitev Foundry Local.

#### Preverite, kaj deluje

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Preizkusite različne modele

Ko phi-4-mini deluje, eksperimentirajte z drugimi modeli:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Korak 5: Izdelava vaše prve aplikacije za klepet (10 minut)

Zdaj ustvarimo Python aplikacijo, ki uporablja modele, ki smo jih pravkar zagnali.

#### Ustvarite skripto za klepet

Ustvarite novo datoteko z imenom `my_first_chat.py` (ali uporabite priložen vzorec):

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
> **Povezani primeri**: Za bolj napredno uporabo si oglejte:
>
> - **Python vzorec**: `Workshop/samples/session01/chat_bootstrap.py` - Vključuje pretakanje odgovorov in obravnavo napak
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktivna različica s podrobnimi razlagami

#### Preizkusite svojo aplikacijo za klepet

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativa: Neposredno uporabite priložene vzorce

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Ali raziščite interaktivni zvezek
Odprite Workshop/notebooks/session01_chat_bootstrap.ipynb v VS Code

Preizkusite te primerne pogovore:

- "Kaj je Microsoft Foundry Local?"
- "Naštej 3 prednosti izvajanja AI modelov lokalno"
- "Pomagaj mi razumeti edge AI"

## Kaj ste dosegli

Čestitke! Uspešno ste:

1. ✅ **Namestili Foundry Local** in preverili, da deluje
2. ✅ **Zagnali svoj prvi AI model** (phi-4-mini) lokalno
3. ✅ **Preizkusili različne modele** prek ukazne vrstice
4. ✅ **Izdelali aplikacijo za klepet**, ki se povezuje z vašim lokalnim AI
5. ✅ **Izkusili lokalno sklepanje AI** brez odvisnosti od oblaka

## Razumevanje, kaj se je zgodilo

### Lokalno sklepanje AI

- Vaši AI modeli delujejo popolnoma na vašem računalniku
- Nobeni podatki se ne pošiljajo v oblak
- Odgovori se generirajo lokalno z uporabo vašega CPU/GPU
- Zasebnost in varnost sta ohranjeni

### Upravljanje modelov

- `foundry model run` prenese in zažene modele
- **FoundryLocalManager SDK** samodejno upravlja zagon storitev in nalaganje modelov
- Modeli so predpomnjeni lokalno za prihodnjo uporabo
- Več modelov je mogoče prenesti, vendar običajno deluje le eden naenkrat
- Storitev samodejno upravlja življenjski cikel modela

### SDK proti CLI pristopom

- **CLI pristop**: Ročno upravljanje modelov z `foundry model run <model>`
- **SDK pristop**: Samodejno upravljanje storitev + modelov z `FoundryLocalManager(alias)`
- **Priporočilo**: Uporabite SDK za aplikacije, CLI za testiranje in raziskovanje

## Referenca pogostih ukazov

### Osnovni CLI ukazi

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

### Priporočila za modele

- **phi-4-mini**: Najboljši začetni model - hiter, lahek, dobra kakovost
- **qwen2.5-0.5b**: Najhitrejše sklepanje, minimalna poraba pomnilnika
- **gpt-oss-20b**: Višja kakovost odgovorov, potrebuje več virov
- **deepseek-coder-1.3b**: Optimiziran za programiranje in naloge s kodo

## Odpravljanje težav

### "Foundry ukaz ni najden"

**Rešitev:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Modela ni uspelo naložiti"

**Rešitev:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Povezava zavrnjena na localhost"

**Rešitev:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Naslednji koraki

### Takojšnje naslednje akcije

1. **Eksperimentirajte** z različnimi modeli in pozivi
2. **Spremenite** svojo aplikacijo za klepet, da preizkusite različne modele
3. **Ustvarite** svoje pozive in preizkusite odgovore
4. **Raziščite** Seja 2: Izdelava RAG aplikacij

### Napredna pot učenja

1. **Seja 2**: Izdelava AI rešitev z RAG (Retrieval-Augmented Generation)
2. **Seja 3**: Primerjava različnih odprtokodnih modelov
3. **Seja 4**: Delo z najsodobnejšimi modeli
4. **Seja 5**: Izdelava večagentnih AI sistemov

## Okoljske spremenljivke (neobvezno)

Za bolj napredno uporabo lahko nastavite te okoljske spremenljivke:

| Spremenljivka | Namen | Primer |
|---------------|-------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Privzeti model za uporabo | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Prepiši URL končne točke | `http://localhost:5273/v1` |

Ustvarite `.env` datoteko v svojem projektnem direktoriju:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Dodatni viri

### Dokumentacija

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Vzorec kode

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Popolna aplikacija za klepet s pretakanjem
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktivni vodič  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](../Module08/samples/03/README.md) - Model Discovery & Benchmarking

### Skupnost

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Trajanje seje**: 30 minut praktičnega dela + 15 minut vprašanj in odgovorov  
**Stopnja težavnosti**: Začetnik  
**Predpogoji**: Windows 11/macOS 11+, Python 3.10+, dostop skrbnika

## Primer scenarija delavnice

### Kontekst iz resničnega sveta

**Scenarij**: IT ekipa v podjetju mora oceniti sklepanje AI na napravi za obdelavo občutljivih povratnih informacij zaposlenih brez pošiljanja podatkov zunanjim storitvam.

**Vaš cilj**: Pokažite, da lokalni AI modeli lahko zagotovijo kakovostne odgovore z manj kot sekundo zakasnitve, hkrati pa ohranjajo popolno zasebnost podatkov.

### Testni pozivi

Uporabite te pozive za preverjanje vaše nastavitve:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Merila uspeha

- ✅ Vsi pozivi dobijo odgovore v manj kot 2 sekundah
- ✅ Nobeni podatki ne zapustijo vašega lokalnega računalnika
- ✅ Odgovori so ustrezni in koristni
- ✅ Vaša aplikacija za klepet deluje gladko

Ta validacija zagotavlja, da je vaša nastavitev Foundry Local pripravljena za napredne delavnice v sejah 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->