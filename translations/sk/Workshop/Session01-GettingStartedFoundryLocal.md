<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-12T00:13:36+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "sk"
}
-->
# Session 1: Začíname s Foundry Local

## Abstrakt

Naučte sa nainštalovať, nakonfigurovať a spustiť svoje prvé AI modely pomocou Microsoft Foundry Local. Táto praktická relácia poskytuje krok za krokom úvod do lokálnej inferencie, od inštalácie až po vytvorenie vašej prvej chatovacej aplikácie s modelmi ako Phi-4, Qwen a DeepSeek.

## Ciele učenia

Na konci tejto relácie budete schopní:

- **Inštalovať a konfigurovať**: Nastaviť Foundry Local s overením správnej inštalácie
- **Ovládnuť CLI operácie**: Používať Foundry Local CLI na správu a nasadenie modelov
- **Spustiť svoj prvý model**: Úspešne nasadiť a interagovať s lokálnym AI modelom
- **Vytvoriť chatovaciu aplikáciu**: Vytvoriť základnú chatovaciu aplikáciu pomocou Foundry Local Python SDK
- **Pochopiť lokálne AI**: Získať základy lokálnej inferencie a správy modelov

## Predpoklady

### Požiadavky na systém

- **Windows**: Windows 11 (22H2 alebo novší) ALEBO **macOS**: macOS 11+ (obmedzená podpora)
- **RAM**: Minimálne 8GB, odporúčané 16GB+
- **Úložisko**: 10GB+ voľného miesta pre modely
- **Python**: Nainštalovaný vo verzii 3.10 alebo novšej
- **Admin prístup**: Administrátorské oprávnenia na inštaláciu

### Vývojové prostredie

- Visual Studio Code s rozšírením pre Python (odporúčané)
- Prístup k príkazovému riadku (PowerShell na Windows, Terminal na macOS)
- Git na klonovanie repozitárov (voliteľné)

## Priebeh workshopu (30 minút)

### Krok 1: Inštalácia Foundry Local (5 minút)

#### Inštalácia na Windows

Nainštalujte Foundry Local pomocou balíkového manažéra pre Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatíva: Stiahnite priamo z [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Inštalácia na macOS (obmedzená podpora)

> [!NOTE] 
> Podpora pre macOS je momentálne v náhľade. Skontrolujte oficiálnu dokumentáciu pre najnovšiu dostupnosť.

Ak je dostupná, nainštalujte pomocou Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternatíva pre používateľov macOS:**
- Použite Windows 11 VM (Parallels/UTM) a postupujte podľa krokov pre Windows
- Spustite cez kontajner, ak je dostupný, a nakonfigurujte `FOUNDRY_LOCAL_ENDPOINT`

### Krok 2: Overenie inštalácie (3 minúty)

Po inštalácii reštartujte svoj terminál a overte, či Foundry Local funguje:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Očakávaný výstup by mal ukázať informácie o verzii a dostupné príkazy.

### Krok 3: Nastavenie Python prostredia (5 minút)

Vytvorte dedikované Python prostredie pre tento workshop:

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

### Krok 4: Spustenie vášho prvého modelu (7 minút)

Teraz spustíme náš prvý AI model lokálne!

#### Začnite s Phi-4 Mini (Odporúčaný prvý model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Tento príkaz stiahne model (prvýkrát) a automaticky spustí službu Foundry Local.

#### Skontrolujte, čo beží

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Vyskúšajte rôzne modely

Keď phi-4-mini funguje, experimentujte s inými modelmi:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Krok 5: Vytvorenie vašej prvej chatovacej aplikácie (10 minút)

Teraz vytvoríme Python aplikáciu, ktorá používa modely, ktoré sme práve spustili.

#### Vytvorenie chatovacieho skriptu

Vytvorte nový súbor s názvom `my_first_chat.py` (alebo použite poskytnutý vzor):

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
> **Súvisiace príklady**: Pre pokročilejšie použitie pozrite:
>
> - **Python vzor**: `Workshop/samples/session01/chat_bootstrap.py` - Zahŕňa streamovanie odpovedí a spracovanie chýb
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktívna verzia s podrobnými vysvetleniami

#### Testovanie vašej chatovacej aplikácie

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatíva: Použite priamo poskytnuté vzory

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Alebo preskúmajte interaktívny notebook
Otvorte Workshop/notebooks/session01_chat_bootstrap.ipynb vo VS Code

Vyskúšajte tieto príklady konverzácií:

- "Čo je Microsoft Foundry Local?"
- "Vymenuj 3 výhody spúšťania AI modelov lokálne"
- "Pomôž mi pochopiť edge AI"

## Čo ste dosiahli

Gratulujeme! Úspešne ste:

1. ✅ **Nainštalovali Foundry Local** a overili jeho funkčnosť
2. ✅ **Spustili svoj prvý AI model** (phi-4-mini) lokálne
3. ✅ **Otestovali rôzne modely** cez príkazový riadok
4. ✅ **Vytvorili chatovaciu aplikáciu**, ktorá sa pripája k vášmu lokálnemu AI
5. ✅ **Zažili lokálnu AI inferenciu** bez závislosti na cloude

## Pochopenie, čo sa stalo

### Lokálna AI inferencia

- Vaše AI modely bežia úplne na vašom počítači
- Žiadne dáta sa neposielajú do cloudu
- Odpovede sú generované lokálne pomocou vášho CPU/GPU
- Ochrana súkromia a bezpečnosť sú zachované

### Správa modelov

- `foundry model run` sťahuje a spúšťa modely
- **FoundryLocalManager SDK** automaticky spravuje spustenie služby a načítanie modelov
- Modely sú uložené lokálne pre budúce použitie
- Viacero modelov môže byť stiahnutých, ale zvyčajne beží iba jeden naraz
- Služba automaticky spravuje životný cyklus modelu

### SDK vs CLI prístupy

- **CLI prístup**: Manuálna správa modelov pomocou `foundry model run <model>`
- **SDK prístup**: Automatická správa služby + modelov pomocou `FoundryLocalManager(alias)`
- **Odporúčanie**: Používajte SDK pre aplikácie, CLI na testovanie a prieskum

## Referencia bežných príkazov

### Základné CLI príkazy

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

### Odporúčania modelov

- **phi-4-mini**: Najlepší model na začiatok - rýchly, nenáročný, dobrá kvalita
- **qwen2.5-0.5b**: Najrýchlejšia inferencia, minimálne využitie pamäte
- **gpt-oss-20b**: Kvalitnejšie odpovede, vyžaduje viac zdrojov
- **deepseek-coder-1.3b**: Optimalizovaný na programovanie a úlohy s kódom

## Riešenie problémov

### "Foundry command not found"

**Riešenie:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model sa nepodarilo načítať"

**Riešenie:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Spojenie odmietnuté na localhost"

**Riešenie:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Ďalšie kroky

### Okamžité ďalšie akcie

1. **Experimentujte** s rôznymi modelmi a otázkami
2. **Upravte** svoju chatovaciu aplikáciu na vyskúšanie rôznych modelov
3. **Vytvorte** vlastné otázky a testujte odpovede
4. **Preskúmajte** Session 2: Vytváranie RAG aplikácií

### Pokročilá cesta učenia

1. **Session 2**: Vytváranie AI riešení s RAG (Retrieval-Augmented Generation)
2. **Session 3**: Porovnanie rôznych open-source modelov
3. **Session 4**: Práca s najmodernejšími modelmi
4. **Session 5**: Vytváranie multi-agentových AI systémov

## Premenné prostredia (voliteľné)

Pre pokročilejšie použitie môžete nastaviť tieto premenné prostredia:

| Premenná | Účel | Príklad |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Predvolený model na použitie | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Prekrytie URL adresy endpointu | `http://localhost:5273/v1` |

Vytvorte súbor `.env` vo vašom projektovom adresári:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Ďalšie zdroje

### Dokumentácia

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Ukážkový kód

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Kompletná chatovacia aplikácia so streamovaním
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktívny tutoriál  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - Integrácia OpenAI SDK
- [Module08 Sample 03](../Module08/samples/03/README.md) - Objavovanie modelov a benchmarking

### Komunita

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Trvanie relácie**: 30 minút prakticky + 15 minút otázky a odpovede  
**Úroveň obtiažnosti**: Začiatočník  
**Predpoklady**: Windows 11/macOS 11+, Python 3.10+, Admin prístup

## Príklad scenára workshopu

### Kontext z reálneho sveta

**Scenár**: Tím IT v podniku potrebuje vyhodnotiť inferenciu AI na zariadení na spracovanie citlivej spätnej väzby zamestnancov bez odosielania údajov do externých služieb.

**Váš cieľ**: Ukázať, že lokálne AI modely dokážu poskytovať kvalitné odpovede s latenciou pod jednu sekundu pri zachovaní úplnej ochrany údajov.

### Testovacie otázky

Použite tieto otázky na overenie vášho nastavenia:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Kritériá úspechu

- ✅ Všetky otázky dostanú odpovede do 2 sekúnd
- ✅ Žiadne údaje neopustia váš lokálny počítač
- ✅ Odpovede sú relevantné a užitočné
- ✅ Vaša chatovacia aplikácia funguje bez problémov

Táto validácia zabezpečí, že vaše nastavenie Foundry Local je pripravené na pokročilé workshopy v reláciách 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->