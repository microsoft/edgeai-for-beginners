# AGENTS.md

> **Průvodce pro vývojáře přispívající do EdgeAI pro začátečníky**
> 
> Tento dokument poskytuje komplexní informace pro vývojáře, AI agenty a přispěvatele pracující s tímto repozitářem. Obsahuje nastavení, pracovní postupy vývoje, testování a osvědčené postupy.
> 
> **Poslední aktualizace**: 30. října 2025 | **Verze dokumentu**: 3.0

## Obsah

- [Přehled projektu](../..)
- [Struktura repozitáře](../..)
- [Předpoklady](../..)
- [Příkazy pro nastavení](../..)
- [Pracovní postup vývoje](../..)
- [Pokyny k testování](../..)
- [Pokyny ke stylu kódu](../..)
- [Pokyny pro pull requesty](../..)
- [Systém překladu](../..)
- [Integrace Foundry Local](../..)
- [Sestavení a nasazení](../..)
- [Běžné problémy a jejich řešení](../..)
- [Další zdroje](../..)
- [Poznámky specifické pro projekt](../..)
- [Získání pomoci](../..)

## Přehled projektu

EdgeAI pro začátečníky je komplexní vzdělávací repozitář zaměřený na výuku vývoje Edge AI s malými jazykovými modely (SLM). Kurz zahrnuje základy EdgeAI, nasazení modelů, optimalizační techniky a implementace připravené pro produkci pomocí Microsoft Foundry Local a různých AI frameworků.

**Klíčové technologie:**
- Python 3.8+ (hlavní jazyk pro AI/ML ukázky)
- .NET C# (AI/ML ukázky)
- JavaScript/Node.js s Electronem (pro desktopové aplikace)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI frameworky: LangChain, Semantic Kernel, Chainlit
- Optimalizace modelů: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Typ repozitáře:** Vzdělávací obsahový repozitář s 8 moduly a 10 komplexními ukázkovými aplikacemi

**Architektura:** Více modulová vzdělávací cesta s praktickými ukázkami demonstrujícími vzory nasazení Edge AI

## Struktura repozitáře

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Předpoklady

### Požadované nástroje

- **Python 3.8+** - Pro AI/ML ukázky a notebooky
- **Node.js 16+** - Pro ukázkovou aplikaci Electron
- **Git** - Pro správu verzí
- **Microsoft Foundry Local** - Pro lokální běh AI modelů

### Doporučené nástroje

- **Visual Studio Code** - S rozšířeními Python, Jupyter a Pylance
- **Windows Terminal** - Pro lepší zážitek z příkazového řádku (uživatelé Windows)
- **Docker** - Pro vývoj v kontejnerech (volitelné)

### Požadavky na systém

- **RAM**: Minimálně 8GB, doporučeno 16GB+ pro scénáře s více modely
- **Úložiště**: 10GB+ volného místa pro modely a závislosti
- **OS**: Windows 10/11, macOS 11+, nebo Linux (Ubuntu 20.04+)
- **Hardware**: CPU s podporou AVX2; GPU (CUDA, Qualcomm NPU) volitelné, ale doporučené

### Požadované znalosti

- Základní znalost programování v Pythonu
- Znalost příkazových řádků
- Porozumění konceptům AI/ML (pro vývoj ukázek)
- Práce s Gitem a procesy pull requestů

## Příkazy pro nastavení

### Nastavení repozitáře

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Nastavení Python ukázek (Modul08 a ukázky workshopu)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Nastavení Node.js ukázek (Ukázka 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Nastavení Foundry Local

Foundry Local je nutné pro spuštění ukázek. Stáhněte a nainstalujte z oficiálního repozitáře:

**Instalace:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Ruční instalace**: Stáhněte z [stránky s verzemi](https://github.com/microsoft/Foundry-Local/releases)

**Rychlý start:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Poznámka**: Foundry Local automaticky vybírá nejlepší variantu modelu pro váš hardware (CUDA GPU, Qualcomm NPU, nebo CPU).

## Pracovní postup vývoje

### Vývoj obsahu

Tento repozitář obsahuje primárně **Markdown vzdělávací obsah**. Při provádění změn:

1. Upravte `.md` soubory v odpovídajících adresářích modulů
2. Dodržujte existující formátovací vzory
3. Zajistěte, že ukázky kódu jsou přesné a otestované
4. Aktualizujte odpovídající překlady, pokud je to nutné (nebo nechte automatizaci, aby to zařídila)

### Vývoj ukázkových aplikací

Pro Python ukázky Modulu08 (ukázky 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Pro Python ukázky workshopu:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Pro ukázku Electron (ukázka 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testování ukázkových aplikací

Python ukázky nemají automatizované testy, ale lze je ověřit jejich spuštěním:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Ukázka Electron má testovací infrastrukturu:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Pokyny k testování

### Validace obsahu

Repozitář používá automatizované překladové pracovní postupy. Manuální testování překladů není nutné.

**Manuální validace změn obsahu:**
1. Zkontrolujte vykreslení Markdownu náhledem `.md` souborů
2. Ověřte, že všechny odkazy směřují na platné cíle
3. Otestujte jakékoli ukázky kódu zahrnuté v dokumentaci
4. Zkontrolujte, že obrázky se načítají správně

### Testování ukázkových aplikací

**Modul08/ukázky/08 (Electron aplikace) má komplexní testování:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python ukázky by měly být testovány manuálně:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Pokyny ke stylu kódu

### Markdown obsah

- Používejte konzistentní hierarchii nadpisů (# pro titul, ## pro hlavní sekce, ### pro podsekce)
- Zahrnujte bloky kódu s určením jazyka: ```python, ```bash, ```javascript
- Dodržujte existující formátování pro tabulky, seznamy a zvýraznění
- Udržujte čitelné řádky (cílem je ~80-100 znaků, ale není to striktní)
- Používejte relativní odkazy pro interní reference

### Styl kódu v Pythonu

- Dodržujte konvence PEP 8
- Používejte typové anotace, kde je to vhodné
- Zahrnujte docstringy pro funkce a třídy
- Používejte smysluplné názvy proměnných
- Udržujte funkce zaměřené a stručné

### Styl kódu v JavaScriptu/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Klíčové konvence:**
- Konfigurace ESLint je poskytována v ukázce 08
- Prettier pro formátování kódu
- Používejte moderní syntaxi ES6+
- Dodržujte existující vzory v kódu

## Pokyny pro pull requesty

### Pracovní postup přispívání

1. **Forkněte repozitář** a vytvořte novou větev z `main`
2. **Proveďte změny** podle pokynů ke stylu kódu
3. **Důkladně otestujte** podle výše uvedených pokynů k testování
4. **Commitujte s jasnými zprávami** podle formátu konvenčních commitů
5. **Pushněte do svého forku** a vytvořte pull request
6. **Reagujte na zpětnou vazbu** od správců během recenze

### Konvence pojmenování větví

- `feature/<modul>-<popis>` - Pro nové funkce nebo obsah
- `fix/<modul>-<popis>` - Pro opravy chyb
- `docs/<popis>` - Pro vylepšení dokumentace
- `refactor/<popis>` - Pro refaktoring kódu

### Formát zpráv commitů

Dodržujte [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Příklady:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Formát názvu
```
[ModuleXX] Brief description of change
```
nebo
```
[Module08/samples/XX] Description for sample changes
```

### Kodex chování

Všichni přispěvatelé musí dodržovat [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Před přispěním si prosím přečtěte [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

### Před odesláním

**Pro změny obsahu:**
- Náhled všech upravených souborů Markdown
- Ověřte funkčnost odkazů a obrázků
- Zkontrolujte překlepy a gramatické chyby

**Pro změny ukázkového kódu (Modul08/ukázky/08):**
```bash
npm run lint
npm test
```

**Pro změny Python ukázek:**
- Otestujte, zda ukázka úspěšně běží
- Ověřte funkčnost zpracování chyb
- Zkontrolujte kompatibilitu s Foundry Local

### Proces recenze

- Změny vzdělávacího obsahu jsou kontrolovány z hlediska přesnosti a srozumitelnosti
- Ukázky kódu jsou testovány z hlediska funkčnosti
- Aktualizace překladů jsou automaticky zpracovány pomocí GitHub Actions

## Systém překladu

**DŮLEŽITÉ:** Tento repozitář používá automatizovaný překlad prostřednictvím GitHub Actions.

- Překlady jsou v adresáři `/translations/` (50+ jazyků)
- Automatizováno pomocí workflow `co-op-translator.yml`
- **NEUPRAVUJTE ručně soubory s překlady** - budou přepsány
- Upravujte pouze anglické zdrojové soubory v kořenovém adresáři a adresářích modulů
- Překlady jsou automaticky generovány při pushi do větve `main`

## Integrace Foundry Local

Většina ukázek Modulu08 vyžaduje spuštění Microsoft Foundry Local.

### Instalace a nastavení

**Instalace Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Instalace Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Spuštění Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Použití SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Ověření Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Proměnné prostředí pro ukázky

Většina ukázek používá tyto proměnné prostředí:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Poznámka**: Při použití `FoundryLocalManager` SDK automaticky zajišťuje objevování služeb a načítání modelů. Alias modelů (např. `phi-3.5-mini`) zajišťuje výběr nejlepší varianty pro váš hardware.

## Sestavení a nasazení

### Nasazení obsahu

Tento repozitář je primárně dokumentace - není nutný žádný proces sestavení pro obsah.

### Sestavení ukázkových aplikací

**Electron aplikace (Modul08/ukázky/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python ukázky:**
Žádný proces sestavení - ukázky se spouštějí přímo pomocí Python interpreteru.

## Běžné problémy a jejich řešení

> **Tip**: Zkontrolujte [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) pro známé problémy a jejich řešení.

### Kritické problémy (blokující)

#### Foundry Local neběží
**Problém:** Ukázky selhávají s chybami připojení

**Řešení:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Běžné problémy (střední závažnost)

#### Problémy s virtuálním prostředím Pythonu
**Problém:** Chyby při importu modulů

**Řešení:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problémy se sestavením Electronu
**Problém:** Selhání npm install nebo sestavení

**Řešení:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problémy s pracovním postupem (menší závažnost)

#### Konflikty v překladovém workflow
**Problém:** Konflikty PR překladu s vašimi změnami

**Řešení:**
- Upravujte pouze anglické zdrojové soubory
- Nechte automatizovaný překladový workflow zpracovat překlady
- Pokud dojde ke konfliktům, sloučte `main` do své větve po sloučení překladů

#### Selhání stahování modelů
**Problém:** Foundry Local selhává při stahování modelů

**Řešení:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Další zdroje

### Vzdělávací cesty
- **Cesta pro začátečníky:** Moduly 01-02 (7-9 hodin)
- **Cesta pro pokročilé:** Moduly 03-04 (9-11 hodin)
- **Cesta pro zkušené:** Moduly 05-07 (12-15 hodin)
- **Cesta pro experty:** Modul 08 (8-10 hodin)
- **Praktický workshop:** Materiály workshopu (6-8 hodin)

### Klíčový obsah modulů
- **Modul01:** Základy EdgeAI a příklady z reálného světa
- **Modul02:** Rodiny a architektury malých jazykových modelů (SLM)
- **Modul03:** Strategie nasazení na lokální a cloudové prostředí
- **Modul04:** Optimalizace modelů s různými frameworky (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modul05:** SLMOps - provozní operace v produkci
- **Modul06:** AI agenti a volání funkcí
- **Modul07:** Implementace specifické pro platformu
- **Modul08:** Nástroje Foundry Local s 10 komplexními ukázkami

### Externí závislosti
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokální runtime AI modelů s API kompatibilním s OpenAI
  - [Dokumentace](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimalizační framework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Nástroj pro optimalizaci modelů
- [OpenVINO](https://docs.openvino.ai/) - Intelův optimalizační nástroj

## Poznámky specifické pro projekt

### Ukázkové aplikace Modulu08

Repozitář obsahuje 10 komplexních ukázkových aplikací:

1. **01-REST Chat Quickstart** - Základní integrace OpenAI SDK
2. **02-OpenAI SDK Integration** - Pokročilé funkce SDK
3. **03-Model Discovery & Benchmarking** - Nástroje pro porovnání modelů
4. **04-Chainlit RAG Application** - Generace s podporou vyhledávání
5. **05-Multi-Agent Orchestration** - Základní koordinace agentů
6. **06-Models-as-Tools Router** - Inteligentní směrování modelů
7. **07-Direct API Client** - Nízká úroveň integrace API
8. **08-Windows 11 Chat App** - Nativní desktopová aplikace Electron
9. **09-Advanced Multi-Agent System** - Komplexní orchestrace agentů
10. **10-Nástroje Foundry Framework** - Integrace LangChain/Semantic Kernel

### Ukázkové aplikace workshopu

Workshop zahrnuje 6 postupných lekcí s praktickými implementacemi:

1. **Lekce 01** - Základní nastavení chatu s integrací Foundry Local
2. **Lekce 02** - RAG pipeline a hodnocení pomocí RAGAS
3. **Lekce 03** - Benchmarking open-source modelů
4. **Lekce 04** - Porovnání a výběr modelů
5. **Lekce 05** - Systémy pro orchestraci více agentů
6. **Lekce 06** - Směrování modelů a správa pipeline

Každý příklad ukazuje různé aspekty vývoje Edge AI s Foundry Local.

### Výkonnostní aspekty

- SLMs jsou optimalizovány pro nasazení na okraji (2-16GB RAM)
- Lokální inference poskytuje odezvu 50-500ms
- Kvantizační techniky dosahují 75% snížení velikosti při zachování 85% výkonu
- Schopnosti pro konverzaci v reálném čase s lokálními modely

### Bezpečnost a soukromí

- Veškeré zpracování probíhá lokálně - žádná data nejsou odesílána do cloudu
- Vhodné pro aplikace citlivé na soukromí (zdravotnictví, finance)
- Splňuje požadavky na suverenitu dat
- Foundry Local běží kompletně na lokálním hardwaru

## Získání pomoci

### Dokumentace

- **Hlavní README**: [README.md](README.md) - Přehled repozitáře a učební cesty
- **Studijní průvodce**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Učební zdroje a časový plán
- **Podpora**: [SUPPORT.md](SUPPORT.md) - Jak získat pomoc
- **Bezpečnost**: [SECURITY.md](SECURITY.md) - Nahlášení bezpečnostních problémů

### Podpora komunity

- **GitHub Issues**: [Nahlásit chyby nebo požádat o funkce](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Pokládejte otázky a sdílejte nápady](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Technické problémy s Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Správci**: Viz [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Bezpečnostní problémy**: Postupujte podle odpovědného zveřejnění v [SECURITY.md](SECURITY.md)
- **Podpora od Microsoftu**: Pro podporu podniků kontaktujte zákaznický servis Microsoftu

### Další zdroje

- **Microsoft Learn**: [Učební cesty AI a strojového učení](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Dokumentace Foundry Local**: [Oficiální dokumentace](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Ukázky od komunity**: Podívejte se na [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) pro příspěvky od komunity

---

**Toto je vzdělávací repozitář zaměřený na výuku vývoje Edge AI. Hlavním cílem je zlepšování vzdělávacího obsahu a přidávání/zdokonalování ukázkových aplikací, které demonstrují koncepty Edge AI.**

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.