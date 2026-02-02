# Sezení 1: Začínáme s Foundry Local

## Abstrakt

Naučte se instalovat, konfigurovat a spouštět své první AI modely pomocí Microsoft Foundry Local. Toto praktické sezení poskytuje krok za krokem úvod do lokální inference, od instalace až po vytvoření vaší první chatovací aplikace s modely jako Phi-4, Qwen a DeepSeek.

## Cíle učení

Na konci tohoto sezení budete schopni:

- **Instalovat a konfigurovat**: Nastavit Foundry Local s ověřením správné instalace
- **Ovládnout CLI operace**: Používat Foundry Local CLI pro správu a nasazení modelů
- **Spustit svůj první model**: Úspěšně nasadit a interagovat s lokálním AI modelem
- **Vytvořit chatovací aplikaci**: Vytvořit základní chatovací aplikaci pomocí Foundry Local Python SDK
- **Porozumět lokálnímu AI**: Pochopit základy lokální inference a správy modelů

## Požadavky

### Systémové požadavky

- **Windows**: Windows 11 (22H2 nebo novější) NEBO **macOS**: macOS 11+ (omezená podpora)
- **RAM**: Minimálně 8GB, doporučeno 16GB+
- **Úložiště**: 10GB+ volného místa pro modely
- **Python**: Verze 3.10 nebo novější
- **Administrátorský přístup**: Práva administrátora pro instalaci

### Vývojové prostředí

- Visual Studio Code s rozšířením pro Python (doporučeno)
- Přístup k příkazovému řádku (PowerShell na Windows, Terminal na macOS)
- Git pro klonování repozitářů (volitelné)

## Průběh workshopu (30 minut)

### Krok 1: Instalace Foundry Local (5 minut)

#### Instalace na Windows

Nainstalujte Foundry Local pomocí správce balíčků pro Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativa: Stáhněte přímo z [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Instalace na macOS (omezená podpora)

> [!NOTE] 
> Podpora macOS je aktuálně v preview. Zkontrolujte oficiální dokumentaci pro nejnovější dostupnost.

Pokud je dostupná, nainstalujte pomocí Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativa pro uživatele macOS:**
- Použijte Windows 11 VM (Parallels/UTM) a postupujte podle kroků pro Windows
- Spusťte přes kontejner, pokud je dostupný, a nakonfigurujte `FOUNDRY_LOCAL_ENDPOINT`

### Krok 2: Ověření instalace (3 minuty)

Po instalaci restartujte svůj terminál a ověřte, že Foundry Local funguje:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Očekávaný výstup by měl zobrazit informace o verzi a dostupné příkazy.

### Krok 3: Nastavení Python prostředí (5 minut)

Vytvořte dedikované Python prostředí pro tento workshop:

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

### Krok 4: Spuštění vašeho prvního modelu (7 minut)

Nyní spustíme náš první AI model lokálně!

#### Začněte s Phi-4 Mini (doporučený první model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Tento příkaz stáhne model (poprvé) a automaticky spustí službu Foundry Local.

#### Zkontrolujte, co běží

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Vyzkoušejte různé modely

Jakmile phi-4-mini funguje, experimentujte s dalšími modely:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Krok 5: Vytvoření vaší první chatovací aplikace (10 minut)

Nyní vytvoříme Python aplikaci, která využívá modely, které jsme právě spustili.

#### Vytvoření chatovacího skriptu

Vytvořte nový soubor nazvaný `my_first_chat.py` (nebo použijte poskytnutý vzorek):

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
> **Související příklady**: Pro pokročilejší použití viz:
>
> - **Python vzorek**: `Workshop/samples/session01/chat_bootstrap.py` - Zahrnuje streamování odpovědí a zpracování chyb
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktivní verze s podrobnými vysvětleními

#### Testování vaší chatovací aplikace

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativa: Použijte přímo poskytnuté vzorky

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Nebo prozkoumejte interaktivní notebook
Otevřete Workshop/notebooks/session01_chat_bootstrap.ipynb ve VS Code

Vyzkoušejte tyto příklady konverzací:

- "Co je Microsoft Foundry Local?"
- "Vyjmenuj 3 výhody provozování AI modelů lokálně"
- "Pomoz mi pochopit edge AI"

## Co jste dosáhli

Gratulujeme! Úspěšně jste:

1. ✅ **Nainstalovali Foundry Local** a ověřili jeho funkčnost
2. ✅ **Spustili svůj první AI model** (phi-4-mini) lokálně
3. ✅ **Otestovali různé modely** přes příkazový řádek
4. ✅ **Vytvořili chatovací aplikaci**, která se připojuje k vašemu lokálnímu AI
5. ✅ **Zažili lokální AI inference** bez závislosti na cloudu

## Porozumění tomu, co se stalo

### Lokální AI inference

- Vaše AI modely běží zcela na vašem počítači
- Žádná data nejsou odesílána do cloudu
- Odpovědi jsou generovány lokálně pomocí vašeho CPU/GPU
- Soukromí a bezpečnost jsou zachovány

### Správa modelů

- `foundry model run` stahuje a spouští modely
- **FoundryLocalManager SDK** automaticky spravuje spuštění služby a načítání modelů
- Modely jsou ukládány lokálně pro budoucí použití
- Může být staženo více modelů, ale obvykle běží jeden najednou
- Služba automaticky spravuje životní cyklus modelů

### SDK vs CLI přístupy

- **CLI přístup**: Manuální správa modelů pomocí `foundry model run <model>`
- **SDK přístup**: Automatická správa služby + modelů pomocí `FoundryLocalManager(alias)`
- **Doporučení**: Používejte SDK pro aplikace, CLI pro testování a průzkum

## Referenční příkazy

### Základní CLI příkazy

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

### Doporučení modelů

- **phi-4-mini**: Nejlepší startovací model - rychlý, lehký, dobrá kvalita
- **qwen2.5-0.5b**: Nejrychlejší inference, minimální využití paměti
- **gpt-oss-20b**: Vyšší kvalita odpovědí, vyžaduje více zdrojů
- **deepseek-coder-1.3b**: Optimalizováno pro programování a úkoly s kódem

## Řešení problémů

### "Foundry command not found"

**Řešení:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model failed to load"

**Řešení:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connection refused on localhost"

**Řešení:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Další kroky

### Okamžité další akce

1. **Experimentujte** s různými modely a dotazy
2. **Upravte** svou chatovací aplikaci a vyzkoušejte různé modely
3. **Vytvořte** vlastní dotazy a testujte odpovědi
4. **Prozkoumejte** Sezení 2: Vytváření RAG aplikací

### Pokročilá vzdělávací cesta

1. **Sezení 2**: Vytváření AI řešení s RAG (Retrieval-Augmented Generation)
2. **Sezení 3**: Porovnání různých open-source modelů
3. **Sezení 4**: Práce s nejmodernějšími modely
4. **Sezení 5**: Vytváření multi-agentních AI systémů

## Proměnné prostředí (volitelné)

Pro pokročilejší použití můžete nastavit tyto proměnné prostředí:

| Proměnná | Účel | Příklad |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Výchozí model k použití | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Přepsání URL endpointu | `http://localhost:5273/v1` |

Vytvořte soubor `.env` ve vašem projektovém adresáři:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Další zdroje

### Dokumentace

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Ukázkový kód

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Kompletní chatovací aplikace se streamováním
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktivní tutoriál  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - Integrace OpenAI SDK
- [Module08 Sample 03](../Module08/samples/03/README.md) - Objevování modelů a benchmarking

### Komunita

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Délka sezení**: 30 minut prakticky + 15 minut Q&A  
**Úroveň obtížnosti**: Začátečník  
**Požadavky**: Windows 11/macOS 11+, Python 3.10+, administrátorský přístup

## Příklad scénáře workshopu

### Kontext z reálného světa

**Scénář**: IT tým v podniku potřebuje vyhodnotit inference AI na zařízení pro zpracování citlivé zpětné vazby zaměstnanců bez odesílání dat do externích služeb.

**Váš cíl**: Demonstrovat, že lokální AI modely mohou poskytovat kvalitní odpovědi s latencí pod jednu sekundu při zachování úplného soukromí dat.

### Testovací dotazy

Použijte tyto dotazy k ověření vašeho nastavení:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Kritéria úspěchu

- ✅ Všechny dotazy obdrží odpovědi do 2 sekund
- ✅ Žádná data neopustí váš lokální počítač
- ✅ Odpovědi jsou relevantní a užitečné
- ✅ Vaše chatovací aplikace funguje hladce

Toto ověření zajistí, že vaše nastavení Foundry Local je připraveno na pokročilé workshopy v sezeních 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->