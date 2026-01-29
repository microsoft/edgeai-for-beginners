# Modul 08: Praktické skúsenosti s Microsoft Foundry Local - Kompletná vývojárska sada

## Prehľad

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) predstavuje novú generáciu vývoja AI na okraji, poskytujúc vývojárom výkonné nástroje na vytváranie, nasadzovanie a škálovanie AI aplikácií lokálne, pričom si zachováva bezproblémovú integráciu s Azure AI Foundry. Tento modul poskytuje komplexný prehľad o Foundry Local od inštalácie až po pokročilý vývoj agentov.

**Kľúčové technológie:**
- Microsoft Foundry Local CLI a SDK
- Integrácia s Azure AI Foundry
- Lokálna inferencia modelov
- Lokálne ukladanie a optimalizácia modelov
- Architektúry založené na agentoch

## Ciele učenia

Po absolvovaní tohto modulu budete schopní:

- **Ovládnuť Foundry Local**: Nainštalovať, nakonfigurovať a optimalizovať pre vývoj na Windows 11
- **Nasadzovať rôzne modely**: Spúšťať modely phi, qwen, deepseek a GPT lokálne pomocou CLI príkazov
- **Vytvárať produkčné riešenia**: Vytvárať AI aplikácie s pokročilým návrhom promptov a integráciou dát
- **Využívať open-source ekosystém**: Integrovať modely Hugging Face a príspevky komunity
- **Vyvíjať AI agentov**: Budovať inteligentných agentov s možnosťami ukotvenia a orchestrácie
- **Implementovať podnikové vzory**: Vytvárať modulárne, škálovateľné AI riešenia pre produkčné nasadenie

## Štruktúra relácie

### [1: Začíname s Foundry Local](./01.FoundryLocalSetup.md)
**Zameranie**: Inštalácia, nastavenie CLI, nasadzovanie modelov a optimalizácia hardvéru

**Kľúčové témy**: Kompletná inštalácia • CLI príkazy • Ukladanie modelov • Hardvérová akcelerácia • Nasadzovanie viacerých modelov

**Ukážka**: [REST Chat Quickstart](./samples/01/README.md) • [Integrácia OpenAI SDK](./samples/02/README.md) • [Objavovanie a benchmarking modelov](./samples/03/README.md)

**Trvanie**: 2-3 hodiny | **Úroveň**: Začiatočník

---

### [2: Vytváranie AI riešení s Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Zameranie**: Pokročilé návrhy promptov, integrácia dát a cloudová konektivita

**Kľúčové témy**: Návrh promptov • Integrácia dát • Azure pracovné postupy • Optimalizácia výkonu • Monitorovanie

**Ukážka**: [Chainlit RAG aplikácia](./samples/04/README.md)

**Trvanie**: 2-3 hodiny | **Úroveň**: Stredne pokročilý

---

### [3: Open-Source modely vo Foundry Local](./03.OpenSourceModels.md)
**Zameranie**: Integrácia Hugging Face, stratégie BYOM a komunitné modely

**Kľúčové témy**: Integrácia Hugging Face • Vlastné modely • Insights z Model Mondays • Príspevky komunity • Výber modelov

**Ukážka**: [Orchestrácia viacerých agentov](./samples/05/README.md)

**Trvanie**: 2-3 hodiny | **Úroveň**: Stredne pokročilý

---

### [4: Preskúmajte najmodernejšie modely](./04.CuttingEdgeModels.md)
**Zameranie**: Porovnanie LLMs vs SLMs, implementácia EdgeAI a pokročilé ukážky

**Kľúčové témy**: Porovnanie modelov • Inferencia na okraji vs v cloude • Phi + ONNX Runtime • Chainlit RAG aplikácia • Optimalizácia WebGPU

**Ukážka**: [Router modelov ako nástrojov](./samples/06/README.md)

**Trvanie**: 3-4 hodiny | **Úroveň**: Pokročilý

---

### [5: Rýchle budovanie AI agentov](./05.AIPoweredAgents.md)
**Zameranie**: Architektúry agentov, systémové prompty, ukotvenie a orchestrácia

**Kľúčové témy**: Vzory návrhu agentov • Návrh systémových promptov • Techniky ukotvenia • Systémy viacerých agentov • Produkčné nasadenie

**Ukážka**: [Orchestrácia viacerých agentov](./samples/05/README.md) • [Pokročilý systém viacerých agentov](./samples/09/README.md)

**Trvanie**: 3-4 hodiny | **Úroveň**: Pokročilý

---

### [6: Foundry Local - Modely ako nástroje](./06.ModelsAsTools.md)
**Zameranie**: Modulárne AI riešenia, podnikové škálovanie a produkčné vzory

**Kľúčové témy**: Modely ako nástroje • Nasadzovanie na zariadeniach • Integrácia SDK/API • Podnikové architektúry • Škálovacie stratégie

**Ukážka**: [Router modelov ako nástrojov](./samples/06/README.md) • [Rámec nástrojov Foundry](./samples/10/README.md)

**Trvanie**: 3-4 hodiny | **Úroveň**: Expert

---

### [7: Priame vzory integrácie API](./samples/07/README.md)
**Zameranie**: Čistá integrácia REST API bez závislostí na SDK pre maximálnu kontrolu

**Kľúčové témy**: Implementácia HTTP klienta • Vlastná autentifikácia • Monitorovanie zdravia modelov • Streamovanie odpovedí • Riešenie chýb v produkcii

**Ukážka**: [Priamy API klient](./samples/07/README.md)

**Trvanie**: 2-3 hodiny | **Úroveň**: Stredne pokročilý

---

### [8: Natívna chatovacia aplikácia pre Windows 11](./samples/08/README.md)
**Zameranie**: Vytváranie moderných natívnych chatovacích aplikácií s integráciou Foundry Local

**Kľúčové témy**: Vývoj v Electron • Fluent Design System • Natívna integrácia Windows • Streamovanie v reálnom čase • Návrh rozhrania chatu

**Ukážka**: [Chatovacia aplikácia pre Windows 11](./samples/08/README.md)

**Trvanie**: 3-4 hodiny | **Úroveň**: Pokročilý

---

### [9: Pokročilá orchestrácia viacerých agentov](./samples/09/README.md)
**Zameranie**: Sofistikovaná koordinácia agentov, špecializované delegovanie úloh a kolaboratívne AI pracovné postupy

**Kľúčové témy**: Inteligentná koordinácia agentov • Vzory volania funkcií • Komunikácia medzi agentmi • Orchestrácia pracovných postupov • Mechanizmy zabezpečenia kvality

**Ukážka**: [Pokročilý systém viacerých agentov](./samples/09/README.md)

**Trvanie**: 4-5 hodín | **Úroveň**: Expert

---

### [10: Foundry Local ako rámec nástrojov](./samples/10/README.md)
**Zameranie**: Architektúra orientovaná na nástroje pre integráciu Foundry Local do existujúcich aplikácií a rámcov

**Kľúčové témy**: Integrácia LangChain • Funkcie Semantic Kernel • Rámce REST API • CLI nástroje • Integrácia Jupyter • Produkčné vzory nasadenia

**Ukážka**: [Rámec nástrojov Foundry](./samples/10/README.md)

**Trvanie**: 4-5 hodín | **Úroveň**: Expert

## Predpoklady

### Požiadavky na systém
- **Operačný systém**: Windows 11 (22H2 alebo novší)
- **Pamäť**: 16GB RAM (32GB odporúčaných pre väčšie modely)
- **Úložisko**: 50GB voľného miesta na ukladanie modelov
- **Hardvér**: Odporúča sa zariadenie s podporou NPU (Copilot+ PC), GPU voliteľné
- **Sieť**: Rýchly internet na počiatočné sťahovanie modelov

### Vývojové prostredie
- Visual Studio Code s rozšírením AI Toolkit
- Python 3.10+ a pip
- Git na správu verzií
- PowerShell alebo Command Prompt
- Azure CLI (voliteľné pre cloudovú integráciu)

### Predpoklady znalostí
- Základné pochopenie konceptov AI/ML
- Znalosť príkazového riadku
- Základy programovania v Pythone
- Koncepty REST API
- Základné znalosti návrhu promptov a inferencie modelov

## Časový harmonogram modulu

**Celkový odhadovaný čas**: 30-38 hodín

| Relácia | Oblasť zamerania | Ukážky | Čas | Náročnosť |
|---------|------------------|--------|------|-----------|
|  1 | Nastavenie a základy | 01, 02, 03 | 2-3 hodiny | Začiatočník |
|  2 | AI riešenia | 04 | 2-3 hodiny | Stredne pokročilý |
|  3 | Open Source | 05 | 2-3 hodiny | Stredne pokročilý |
|  4 | Pokročilé modely | 06 | 3-4 hodiny | Pokročilý |
|  5 | AI agenti | 05, 09 | 3-4 hodiny | Pokročilý |
|  6 | Podnikové nástroje | 06, 10 | 3-4 hodiny | Expert |
|  7 | Priama integrácia API | 07 | 2-3 hodiny | Stredne pokročilý |
|  8 | Chatovacia aplikácia pre Windows 11 | 08 | 3-4 hodiny | Pokročilý |
|  9 | Pokročilá orchestrácia viacerých agentov | 09 | 4-5 hodín | Expert |
| 10 | Rámec nástrojov | 10 | 4-5 hodín | Expert |

## Kľúčové zdroje

**Oficiálna dokumentácia:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Zdrojový kód a oficiálne ukážky
- [Dokumentácia Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Kompletný návod na nastavenie a používanie
- [Séria Model Mondays](https://aka.ms/model-mondays) - Týždenné zvýraznenia modelov a tutoriály

**Komunita a podpora:**
- [Diskusie o Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Q&A komunity a požiadavky na funkcie
- [Komunita vývojárov Microsoft AI](https://techcommunity.microsoft.com/category/artificialintelligence) - Najnovšie správy a osvedčené postupy

## Výsledky učenia

Po absolvovaní tohto modulu budete schopní:

### Technická zručnosť
- **Nasadzovať a spravovať**: Inštalácie Foundry Local v prostrediach vývoja a produkcie
- **Integrovať modely**: Bezproblémovo pracovať s rôznymi rodinami modelov od Microsoftu, Hugging Face a komunity
- **Vytvárať aplikácie**: Vytvárať produkčne pripravené AI aplikácie s pokročilými funkciami a optimalizáciami
- **Vyvíjať agentov**: Implementovať sofistikovaných AI agentov s ukotvením, uvažovaním a integráciou nástrojov

### Strategické pochopenie
- **Rozhodnutia o architektúre**: Robiť informované rozhodnutia medzi lokálnym a cloudovým nasadením
- **Optimalizácia výkonu**: Optimalizovať výkon inferencie na rôznych hardvérových konfiguráciách
- **Podnikové škálovanie**: Navrhovať aplikácie, ktoré sa škálujú od lokálnych prototypov po podnikové nasadenia
- **Ochrana súkromia a bezpečnosť**: Implementovať AI riešenia zachovávajúce súkromie s lokálnou inferenciou

### Inovačné schopnosti
- **Rýchle prototypovanie**: Rýchlo vytvárať a testovať koncepty AI aplikácií naprieč všetkými 10 vzormi ukážok
- **Integrácia komunity**: Využívať open-source modely a prispievať do ekosystému
- **Pokročilé vzory**: Implementovať najmodernejšie AI vzory vrátane RAG, agentov a integrácie nástrojov
- **Ovládanie rámcov**: Expertne integrovať LangChain, Semantic Kernel, Chainlit a Electron
- **Produkčné nasadenie**: Nasadzovať škálovateľné AI riešenia od lokálnych prototypov po podnikové systémy
- **Pripravenosť na budúcnosť**: Vytvárať aplikácie pripravené na nové AI technológie a vzory

## Začíname

1. **Nastavenie prostredia**: Uistite sa, že máte Windows 11 s odporúčaným hardvérom (pozrite Predpoklady)
2. **Inštalácia Foundry Local**: Postupujte podľa relácie 1 na kompletnú inštaláciu a konfiguráciu
3. **Spustite ukážku 01**: Začnite so základnou integráciou REST API na overenie nastavenia
4. **Postupujte cez ukážky**: Dokončite ukážky 01-10 pre komplexné zvládnutie

## Metriky úspechu

Sledujte svoj pokrok cez všetkých 10 komplexných ukážok:

### Základná úroveň (Ukážky 01-03)
- [ ] Úspešne nainštalovať a nakonfigurovať Foundry Local
- [ ] Dokončiť integráciu REST API (Ukážka 01)
- [ ] Implementovať kompatibilitu OpenAI SDK (Ukážka 02)
- [ ] Vykonať objavovanie a benchmarking modelov (Ukážka 03)

### Úroveň aplikácie (Ukážky 04-06)
- [ ] Nasadiť a spustiť aspoň 4 rôzne rodiny modelov
- [ ] Vytvoriť funkčnú RAG chatovaciu aplikáciu (Ukážka 04)
- [ ] Vytvoriť systém orchestrácie viacerých agentov (Ukážka 05)
- [ ] Implementovať inteligentné smerovanie modelov (Ukážka 06)

### Pokročilá úroveň integrácie (Ukážky 07-10)
- [ ] Vytvoriť produkčne pripraveného API klienta (Ukážka 07)
- [ ] Vyvinúť natívnu chatovaciu aplikáciu pre Windows 11 (Ukážka 08)
- [ ] Implementovať pokročilý systém viacerých agentov (Ukážka 09)
- [ ] Vytvoriť komplexný rámec nástrojov (Ukážka 10)

### Indikátory zvládnutia
- [ ] Úspešne spustiť všetkých 10 ukážok bez chýb
- [ ] Prispôsobiť aspoň 3 ukážky pre konkrétne použitia
- [ ] Nasadiť 2+ ukážky v produkčne podobných prostrediach
- [ ] Prispieť vylepšeniami alebo rozšíreniami do ukážkového kódu
- [ ] Integrovať vzory Foundry Local do osobných/profesionálnych projektov

## Rýchly sprievodca - Všetkých 10 ukážok

### Nastavenie prostredia (Povinné pre všetky ukážky)

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

### Základné ukážky (01-06)

**Ukážka 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Ukážka 02: Integrácia OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Ukážka 03: Objavovanie a benchmarking modelov**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Ukážka 04: Chainlit RAG aplikácia**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Ukážka 05: Orchestrácia viacerých agentov**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Ukážka 06: Router modelov ako nástrojov**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Pokročilé ukážky (07-10)

**Ukážka 07: Priamy API klient**
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

**Ukážka 08: Chatovacia aplikácia pre Windows 11**
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

**Ukážka 09: Pokročilý systém viacer
Tento modul predstavuje špičku vo vývoji edge AI, spájajúc podnikové nástroje od Microsoftu s flexibilitou a inováciou open-source ekosystému. Ovládnutím Foundry Local prostredníctvom všetkých 10 komplexných príkladov sa dostanete na čelo vývoja AI aplikácií.

**Kompletná vzdelávacia cesta:**
- **Základy** (Príklady 01-03): Integrácia API a správa modelov
- **Aplikácie** (Príklady 04-06): RAG, agenti a inteligentné smerovanie
- **Pokročilé** (Príklady 07-10): Produkčné rámce a podniková integrácia

Pre integráciu Azure OpenAI (Session 2) si pozrite jednotlivé README súbory príkladov, kde nájdete požadované premenné prostredia a nastavenia verzie API.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.