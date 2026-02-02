# Modul 08: Praktické zkušenosti s Microsoft Foundry Local - Kompletní sada nástrojů pro vývojáře

## Přehled

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) představuje novou generaci vývoje AI na okraji, která poskytuje vývojářům výkonné nástroje pro vytváření, nasazení a škálování AI aplikací lokálně, přičemž zajišťuje bezproblémovou integraci s Azure AI Foundry. Tento modul nabízí komplexní přehled Foundry Local od instalace až po pokročilý vývoj agentů.

**Klíčové technologie:**
- Microsoft Foundry Local CLI a SDK
- Integrace Azure AI Foundry
- Lokální inference modelů
- Lokální ukládání a optimalizace modelů
- Architektury založené na agentech

## Cíle učení

Po dokončení tohoto modulu budete schopni:

- **Ovládnout Foundry Local**: Instalovat, konfigurovat a optimalizovat pro vývoj na Windows 11
- **Nasazovat různé modely**: Spouštět modely phi, qwen, deepseek a GPT lokálně pomocí příkazů CLI
- **Vytvářet produkční řešení**: Vytvářet AI aplikace s pokročilým návrhem promptů a integrací dat
- **Využívat open-source ekosystém**: Integrovat modely Hugging Face a příspěvky komunity
- **Vyvíjet AI agenty**: Vytvářet inteligentní agenty s možnostmi uzemnění a orchestrace
- **Implementovat podnikové vzory**: Vytvářet modulární, škálovatelné AI řešení pro produkční nasazení

## Struktura lekcí

### [1: Začínáme s Foundry Local](./01.FoundryLocalSetup.md)
**Zaměření**: Instalace, nastavení CLI, nasazení modelů a optimalizace hardwaru

**Klíčová témata**: Kompletní instalace • Příkazy CLI • Ukládání modelů • Akcelerace hardwaru • Nasazení více modelů

**Ukázka**: [REST Chat Quickstart](./samples/01/README.md) • [Integrace OpenAI SDK](./samples/02/README.md) • [Objevování a benchmarking modelů](./samples/03/README.md)

**Délka**: 2-3 hodiny | **Úroveň**: Začátečník

---

### [2: Vytváření AI řešení s Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Zaměření**: Pokročilý návrh promptů, integrace dat a připojení ke cloudu

**Klíčová témata**: Návrh promptů • Integrace dat • Azure workflows • Optimalizace výkonu • Monitoring

**Ukázka**: [Chainlit RAG Application](./samples/04/README.md)

**Délka**: 2-3 hodiny | **Úroveň**: Středně pokročilý

---

### [3: Open-Source modely ve Foundry Local](./03.OpenSourceModels.md)
**Zaměření**: Integrace Hugging Face, strategie BYOM a komunitní modely

**Klíčová témata**: Integrace Hugging Face • Bring-your-own-model • Insights z Model Mondays • Příspěvky komunity • Výběr modelů

**Ukázka**: [Orchestrace více agentů](./samples/05/README.md)

**Délka**: 2-3 hodiny | **Úroveň**: Středně pokročilý

---

### [4: Prozkoumání špičkových modelů](./04.CuttingEdgeModels.md)
**Zaměření**: LLMs vs SLMs, implementace EdgeAI a pokročilé ukázky

**Klíčová témata**: Porovnání modelů • Inference na okraji vs v cloudu • Phi + ONNX Runtime • Chainlit RAG aplikace • Optimalizace WebGPU

**Ukázka**: [Router pro modely jako nástroje](./samples/06/README.md)

**Délka**: 3-4 hodiny | **Úroveň**: Pokročilý

---

### [5: Rychlá tvorba AI agentů](./05.AIPoweredAgents.md)
**Zaměření**: Architektury agentů, systémové prompty, uzemnění a orchestrace

**Klíčová témata**: Návrhové vzory agentů • Návrh systémových promptů • Techniky uzemnění • Systémy více agentů • Produkční nasazení

**Ukázka**: [Orchestrace více agentů](./samples/05/README.md) • [Pokročilý systém více agentů](./samples/09/README.md)

**Délka**: 3-4 hodiny | **Úroveň**: Pokročilý

---

### [6: Foundry Local - Modely jako nástroje](./06.ModelsAsTools.md)
**Zaměření**: Modulární AI řešení, podnikové škálování a produkční vzory

**Klíčová témata**: Modely jako nástroje • Nasazení na zařízení • Integrace SDK/API • Podnikové architektury • Strategie škálování

**Ukázka**: [Router pro modely jako nástroje](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Délka**: 3-4 hodiny | **Úroveň**: Expert

---

### [7: Vzory přímé integrace API](./samples/07/README.md)
**Zaměření**: Čistá integrace REST API bez závislostí na SDK pro maximální kontrolu

**Klíčová témata**: Implementace HTTP klienta • Vlastní autentizace • Monitoring zdraví modelů • Streamování odpovědí • Řešení chyb v produkci

**Ukázka**: [Přímý API klient](./samples/07/README.md)

**Délka**: 2-3 hodiny | **Úroveň**: Středně pokročilý

---

### [8: Nativní chatovací aplikace pro Windows 11](./samples/08/README.md)
**Zaměření**: Vytváření moderních nativních chatovacích aplikací s integrací Foundry Local

**Klíčová témata**: Vývoj v Electronu • Fluent Design System • Nativní integrace Windows • Streamování v reálném čase • Návrh chatovacího rozhraní

**Ukázka**: [Chatovací aplikace pro Windows 11](./samples/08/README.md)

**Délka**: 3-4 hodiny | **Úroveň**: Pokročilý

---

### [9: Pokročilá orchestrace více agentů](./samples/09/README.md)
**Zaměření**: Sofistikovaná koordinace agentů, specializované delegování úkolů a spolupráce AI

**Klíčová témata**: Inteligentní koordinace agentů • Vzory volání funkcí • Komunikace mezi agenty • Orchestrace workflow • Mechanismy zajištění kvality

**Ukázka**: [Pokročilý systém více agentů](./samples/09/README.md)

**Délka**: 4-5 hodin | **Úroveň**: Expert

---

### [10: Foundry Local jako nástrojový rámec](./samples/10/README.md)
**Zaměření**: Architektura zaměřená na nástroje pro integraci Foundry Local do existujících aplikací a rámců

**Klíčová témata**: Integrace LangChain • Funkce Semantic Kernel • Rámce REST API • Nástroje CLI • Integrace Jupyter • Produkční vzory nasazení

**Ukázka**: [Foundry Tools Framework](./samples/10/README.md)

**Délka**: 4-5 hodin | **Úroveň**: Expert

## Požadavky

### Systémové požadavky
- **Operační systém**: Windows 11 (22H2 nebo novější)
- **Paměť**: 16GB RAM (doporučeno 32GB pro větší modely)
- **Úložiště**: 50GB volného místa pro ukládání modelů
- **Hardware**: Doporučeno zařízení s podporou NPU (Copilot+ PC), GPU volitelné
- **Síť**: Rychlé připojení k internetu pro počáteční stahování modelů

### Vývojové prostředí
- Visual Studio Code s rozšířením AI Toolkit
- Python 3.10+ a pip
- Git pro správu verzí
- PowerShell nebo Command Prompt
- Azure CLI (volitelné pro integraci s cloudem)

### Znalostní požadavky
- Základní porozumění konceptům AI/ML
- Znalost práce s příkazovým řádkem
- Základy programování v Pythonu
- Koncepty REST API
- Základní znalosti návrhu promptů a inference modelů

## Časový plán modulu

**Celkový odhadovaný čas**: 30-38 hodin

| Lekce | Oblast zaměření | Ukázky | Čas | Složitost |
|-------|-----------------|--------|------|-----------|
|  1 | Nastavení a základy | 01, 02, 03 | 2-3 hodiny | Začátečník |
|  2 | AI řešení | 04 | 2-3 hodiny | Středně pokročilý |
|  3 | Open Source | 05 | 2-3 hodiny | Středně pokročilý |
|  4 | Pokročilé modely | 06 | 3-4 hodiny | Pokročilý |
|  5 | AI agenti | 05, 09 | 3-4 hodiny | Pokročilý |
|  6 | Podnikové nástroje | 06, 10 | 3-4 hodiny | Expert |
|  7 | Přímá integrace API | 07 | 2-3 hodiny | Středně pokročilý |
|  8 | Chatovací aplikace pro Windows 11 | 08 | 3-4 hodiny | Pokročilý |
|  9 | Pokročilá orchestrace více agentů | 09 | 4-5 hodin | Expert |
| 10 | Nástrojový rámec | 10 | 4-5 hodin | Expert |

## Klíčové zdroje

**Oficiální dokumentace:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Zdrojový kód a oficiální ukázky
- [Dokumentace Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Kompletní průvodce nastavením a používáním
- [Model Mondays Series](https://aka.ms/model-mondays) - Týdenní přehledy modelů a tutoriály

**Komunita a podpora:**
- [Diskuze o Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Q&A a požadavky na funkce
- [Komunita vývojářů Microsoft AI](https://techcommunity.microsoft.com/category/artificialintelligence) - Nejnovější zprávy a osvědčené postupy

## Výsledky učení

Po dokončení tohoto modulu budete schopni:

### Technická zdatnost
- **Nasazovat a spravovat**: Instalace Foundry Local v prostředích pro vývoj i produkci
- **Integrovat modely**: Bezproblémová práce s různými rodinami modelů od Microsoftu, Hugging Face a komunity
- **Vytvářet aplikace**: Vytvářet produkčně připravené AI aplikace s pokročilými funkcemi a optimalizacemi
- **Vyvíjet agenty**: Implementovat sofistikované AI agenty s uzemněním, uvažováním a integrací nástrojů

### Strategické porozumění
- **Rozhodování o architektuře**: Dělat informovaná rozhodnutí mezi lokálním a cloudovým nasazením
- **Optimalizace výkonu**: Optimalizovat výkon inference na různých hardwarových konfiguracích
- **Podnikové škálování**: Navrhovat aplikace, které škálují od lokálních prototypů po podniková nasazení
- **Ochrana soukromí a bezpečnost**: Implementovat AI řešení zachovávající soukromí s lokální inferencí

### Inovační schopnosti
- **Rychlé prototypování**: Rychle vytvářet a testovat koncepty AI aplikací napříč všemi 10 vzory ukázek
- **Integrace komunity**: Využívat open-source modely a přispívat do ekosystému
- **Pokročilé vzory**: Implementovat špičkové AI vzory včetně RAG, agentů a integrace nástrojů
- **Ovládnutí rámců**: Expert na integraci s LangChain, Semantic Kernel, Chainlit a Electron
- **Produkční nasazení**: Nasazovat škálovatelné AI řešení od lokálních prototypů po podnikové systémy
- **Připravenost na budoucnost**: Vytvářet aplikace připravené na nové AI technologie a vzory

## Jak začít

1. **Nastavení prostředí**: Zajistěte Windows 11 s doporučeným hardwarem (viz Požadavky)
2. **Instalace Foundry Local**: Postupujte podle lekce 1 pro kompletní instalaci a konfiguraci
3. **Spuštění ukázky 01**: Začněte s jednoduchou integrací REST API pro ověření nastavení
4. **Postupujte přes ukázky**: Dokončete ukázky 01-10 pro komplexní zvládnutí

## Metriky úspěchu

Sledujte svůj pokrok přes všech 10 komplexních ukázek:

### Základní úroveň (Ukázky 01-03)
- [ ] Úspěšně nainstalovat a konfigurovat Foundry Local
- [ ] Dokončit integraci REST API (Ukázka 01)
- [ ] Implementovat kompatibilitu s OpenAI SDK (Ukázka 02)
- [ ] Provést objevování a benchmarking modelů (Ukázka 03)

### Úroveň aplikací (Ukázky 04-06)
- [ ] Nasadit a spustit alespoň 4 různé rodiny modelů
- [ ] Vytvořit funkční RAG chatovací aplikaci (Ukázka 04)
- [ ] Vytvořit systém orchestrace více agentů (Ukázka 05)
- [ ] Implementovat inteligentní směrování modelů (Ukázka 06)

### Pokročilá úroveň integrace (Ukázky 07-10)
- [ ] Vytvořit produkčně připraveného API klienta (Ukázka 07)
- [ ] Vyvinout nativní chatovací aplikaci pro Windows 11 (Ukázka 08)
- [ ] Implementovat pokročilý systém více agentů (Ukázka 09)
- [ ] Vytvořit komplexní nástrojový rámec (Ukázka 10)

### Indikátory zvládnutí
- [ ] Úspěšně spustit všech 10 ukázek bez chyb
- [ ] Přizpůsobit alespoň 3 ukázky pro specifické případy použití
- [ ] Nasadit 2+ ukázky v prostředích podobných produkci
- [ ] Přispět vylepšeními nebo rozšířeními do ukázkového kódu
- [ ] Integrovat vzory Foundry Local do osobních/profesních projektů

## Rychlý průvodce - Všech 10 ukázek

### Nastavení prostředí (Požadováno pro všechny ukázky)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Základní ukázky (01-06)

**Ukázka 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Ukázka 02: Integrace OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Ukázka 03: Objevování a benchmarking modelů**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Ukázka 04: Chainlit RAG Application**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Ukázka 05: Orchestrace více agentů**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Ukázka 06: Router pro modely jako nástroje**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Pokročilé ukázky (07-10)

**Ukázka 07: Přímý API klient**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Ukázka 08: Chatovací aplikace pro Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Ukázka 09: Pokročilý systém více agentů**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Ukázka 10: Foundry Tools Framework**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Řešení běžných problémů

**Chyby připojení Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problémy s načítáním modelů**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Problémy se závislostmi**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Shrnutí
Tento modul představuje špičku vývoje edge AI, spojuje podnikové nástroje Microsoftu s flexibilitou a inovací open-source ekosystému. Osvojením Foundry Local prostřednictvím všech 10 komplexních ukázek se dostanete do čela vývoje AI aplikací.

**Kompletní vzdělávací cesta:**
- **Základy** (Ukázky 01-03): Integrace API a správa modelů
- **Aplikace** (Ukázky 04-06): RAG, agenti a inteligentní směrování
- **Pokročilé** (Ukázky 07-10): Produkční rámce a podniková integrace

Pro integraci Azure OpenAI (Sezení 2) si prostudujte jednotlivé README soubory ukázek, kde najdete požadované proměnné prostředí a nastavení verzí API.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.