# Sesija 1: Pradžia su Foundry Local

## Santrauka

Sužinokite, kaip įdiegti, konfigūruoti ir paleisti pirmuosius AI modelius naudojant Microsoft Foundry Local. Ši praktinė sesija suteikia žingsnis po žingsnio įvadą į vietinį modelių naudojimą – nuo diegimo iki pirmosios pokalbių programos kūrimo naudojant tokius modelius kaip Phi-4, Qwen ir DeepSeek.

## Mokymosi tikslai

Po šios sesijos jūs:

- **Įdiegsite ir konfigūruosite**: Nustatysite Foundry Local su tinkamu diegimo patikrinimu
- **Įvaldysite CLI operacijas**: Naudosite Foundry Local CLI modelių valdymui ir diegimui
- **Paleisite pirmąjį modelį**: Sėkmingai paleisite ir sąveikausite su vietiniu AI modeliu
- **Sukursite pokalbių programą**: Sukursite pagrindinę pokalbių programą naudodami Foundry Local Python SDK
- **Suprasite vietinį AI**: Įgysite pagrindines žinias apie vietinį modelių naudojimą ir valdymą

## Reikalavimai

### Sistemos reikalavimai

- **Windows**: Windows 11 (22H2 ar naujesnė) ARBA **macOS**: macOS 11+ (ribota palaikymas)
- **RAM**: mažiausiai 8GB, rekomenduojama 16GB+
- **Saugykla**: mažiausiai 10GB laisvos vietos modeliams
- **Python**: įdiegta 3.10 ar naujesnė versija
- **Administratoriaus teisės**: administratoriaus teisės diegimui

### Kūrimo aplinka

- Visual Studio Code su Python plėtiniu (rekomenduojama)
- Komandinės eilutės prieiga (PowerShell Windows, Terminal macOS)
- Git, skirtas saugyklų klonavimui (neprivaloma)

## Seminaro eiga (30 minučių)

### 1 žingsnis: Foundry Local diegimas (5 minutės)

#### Windows diegimas

Įdiekite Foundry Local naudodami Windows paketų tvarkyklę:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatyva: Atsisiųskite tiesiogiai iš [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### macOS diegimas (ribota palaikymas)

> [!NOTE] 
> macOS palaikymas šiuo metu yra peržiūros stadijoje. Patikrinkite oficialią dokumentaciją dėl naujausios informacijos.

Jei įmanoma, įdiekite naudodami Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternatyva macOS vartotojams:**
- Naudokite Windows 11 VM (Parallels/UTM) ir sekite Windows diegimo žingsnius
- Paleiskite per konteinerį, jei įmanoma, ir konfigūruokite `FOUNDRY_LOCAL_ENDPOINT`

### 2 žingsnis: Diegimo patikrinimas (3 minutės)

Po diegimo, iš naujo paleiskite terminalą ir patikrinkite, ar Foundry Local veikia:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Tikėtinas rezultatas turėtų rodyti versijos informaciją ir galimus komandas.

### 3 žingsnis: Python aplinkos nustatymas (5 minutės)

Sukurkite dedikuotą Python aplinką šiam seminarui:

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

### 4 žingsnis: Pirmojo modelio paleidimas (7 minutės)

Dabar paleiskime pirmąjį AI modelį vietoje!

#### Pradėkite nuo Phi-4 Mini (rekomenduojamas pirmasis modelis)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Ši komanda atsisiunčia modelį (pirmą kartą) ir automatiškai paleidžia Foundry Local paslaugą.

#### Patikrinkite, kas veikia

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Išbandykite kitus modelius

Kai phi-4-mini veikia, eksperimentuokite su kitais modeliais:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### 5 žingsnis: Sukurkite pirmąją pokalbių programą (10 minučių)

Dabar sukurkime Python programą, kuri naudoja ką tik paleistus modelius.

#### Sukurkite pokalbių scenarijų

Sukurkite naują failą pavadinimu `my_first_chat.py` (arba naudokite pateiktą pavyzdį):

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
> **Susiję pavyzdžiai**: Dėl sudėtingesnio naudojimo žr.:
>
> - **Python pavyzdys**: `Workshop/samples/session01/chat_bootstrap.py` - Apima srautinį atsakymą ir klaidų tvarkymą
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktyvi versija su išsamiais paaiškinimais

#### Išbandykite savo pokalbių programą

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatyva: Naudokite pateiktus pavyzdžius tiesiogiai

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Arba tyrinėkite interaktyvų užrašų knygelę
Atidarykite Workshop/notebooks/session01_chat_bootstrap.ipynb VS Code

Išbandykite šiuos pokalbių pavyzdžius:

- "Kas yra Microsoft Foundry Local?"
- "Išvardinkite 3 privalumus, kai AI modeliai veikia vietoje"
- "Padėkite man suprasti edge AI"

## Ką pasiekėte

Sveikiname! Jūs sėkmingai:

1. ✅ **Įdiegėte Foundry Local** ir patikrinote, kad jis veikia
2. ✅ **Paleidote pirmąjį AI modelį** (phi-4-mini) vietoje
3. ✅ **Išbandėte skirtingus modelius** per komandų eilutę
4. ✅ **Sukūrėte pokalbių programą**, kuri jungiasi prie jūsų vietinio AI
5. ✅ **Patyrėte vietinį AI naudojimą** be debesų priklausomybės

## Supratimas, kas įvyko

### Vietinis AI naudojimas

- Jūsų AI modeliai veikia visiškai jūsų kompiuteryje
- Duomenys nėra siunčiami į debesį
- Atsakymai generuojami vietoje naudojant jūsų CPU/GPU
- Užtikrinamas privatumas ir saugumas

### Modelių valdymas

- `foundry model run` atsisiunčia ir paleidžia modelius
- **FoundryLocalManager SDK** automatiškai tvarko paslaugos paleidimą ir modelių įkrovimą
- Modeliai saugomi vietoje, kad būtų galima naudoti ateityje
- Galima atsisiųsti kelis modelius, tačiau paprastai vienu metu veikia tik vienas
- Paslauga automatiškai valdo modelių gyvavimo ciklą

### SDK ir CLI metodai

- **CLI metodas**: Rankinis modelių valdymas su `foundry model run <model>`
- **SDK metodas**: Automatinis paslaugos ir modelių valdymas su `FoundryLocalManager(alias)`
- **Rekomendacija**: Naudokite SDK programoms, CLI testavimui ir tyrinėjimui

## Dažniausiai naudojamos komandos

### Esminės CLI komandos

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

### Modelių rekomendacijos

- **phi-4-mini**: Geriausias pradinis modelis – greitas, lengvas, gera kokybė
- **qwen2.5-0.5b**: Greičiausias atsakymų generavimas, minimalus atminties naudojimas
- **gpt-oss-20b**: Aukštesnės kokybės atsakymai, reikalauja daugiau resursų
- **deepseek-coder-1.3b**: Optimizuotas programavimui ir kodavimo užduotims

## Trikčių šalinimas

### "Foundry komanda nerasta"

**Sprendimas:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Modelio įkrovimas nepavyko"

**Sprendimas:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Ryšys su localhost atmestas"

**Sprendimas:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Kiti žingsniai

### Tiesioginiai veiksmai

1. **Eksperimentuokite** su skirtingais modeliais ir užklausomis
2. **Modifikuokite** savo pokalbių programą, kad išbandytumėte skirtingus modelius
3. **Sukurkite** savo užklausas ir testuokite atsakymus
4. **Tyrinėkite** 2 sesiją: RAG programų kūrimas

### Pažangus mokymosi kelias

1. **Sesija 2**: AI sprendimų kūrimas su RAG (Retrieval-Augmented Generation)
2. **Sesija 3**: Skirtingų atvirojo kodo modelių palyginimas
3. **Sesija 4**: Darbas su pažangiausiais modeliais
4. **Sesija 5**: Daugiaagentinių AI sistemų kūrimas

## Aplinkos kintamieji (neprivaloma)

Dėl pažangesnio naudojimo galite nustatyti šiuos aplinkos kintamuosius:

| Kintamasis | Paskirtis | Pavyzdys |
|------------|-----------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Numatytojo modelio naudojimas | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Pakeisti endpoint URL | `http://localhost:5273/v1` |

Sukurkite `.env` failą savo projekto kataloge:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Papildomi ištekliai

### Dokumentacija

- [Foundry Local Python SDK nuoroda](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local diegimo vadovas](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modelių katalogas](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Pavyzdinis kodas

- **Session01 Python pavyzdys**: `Workshop/samples/session01/chat_bootstrap.py` - Pilna pokalbių programa su srautu
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktyvus vadovas  
- [Module08 Pavyzdys 01](../Module08/samples/01/README.md) - REST pokalbių greitas startas
- [Module08 Pavyzdys 02](../Module08/samples/02/README.md) - OpenAI SDK integracija
- [Module08 Pavyzdys 03](../Module08/samples/03/README.md) - Modelių atradimas ir palyginimas

### Bendruomenė

- [Foundry Local GitHub diskusijos](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI bendruomenė](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sesijos trukmė**: 30 minučių praktika + 15 minučių klausimai ir atsakymai  
**Sudėtingumo lygis**: Pradedantysis  
**Reikalavimai**: Windows 11/macOS 11+, Python 3.10+, administratoriaus teisės

## Seminaro pavyzdinė situacija

### Realus kontekstas

**Situacija**: Įmonės IT komanda turi įvertinti AI modelių naudojimą įrenginiuose, kad galėtų apdoroti jautrius darbuotojų atsiliepimus, nesiunčiant duomenų į išorines paslaugas.

**Jūsų tikslas**: Pademonstruoti, kad vietiniai AI modeliai gali pateikti kokybiškus atsakymus su mažesne nei sekundės vėlinimu, išlaikant visišką duomenų privatumą.

### Testavimo užklausos

Naudokite šias užklausas, kad patikrintumėte savo nustatymus:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Sėkmės kriterijai

- ✅ Visi užklausų atsakymai pateikiami per mažiau nei 2 sekundes
- ✅ Duomenys nepalieka jūsų vietinio kompiuterio
- ✅ Atsakymai yra aktualūs ir naudingi
- ✅ Jūsų pokalbių programa veikia sklandžiai

Šis patikrinimas užtikrina, kad jūsų Foundry Local nustatymai yra pasiruošę pažangiems seminarams 2–6 sesijose.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->