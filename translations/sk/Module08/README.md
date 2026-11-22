# Modul 08: Praktická práca s Microsoft Foundry Local – Kompletná sada nástrojov pre vývojárov

## Prehľad

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) predstavuje ďalšiu generáciu vývoja edge AI, ktorá poskytuje vývojárom silné nástroje na lokálnu tvorbu, nasadzovanie a škálovanie AI aplikácií so zachovaním bezproblémovej integrácie s Azure AI Foundry. Tento modul poskytuje komplexné pokrytie Foundry Local od inštalácie po pokročilý vývoj agentov.

**Kľúčové technológie:**
- Microsoft Foundry Local CLI a SDK
- Integrácia Azure AI Foundry
- Inferencia modelov na zariadení
- Lokálne ukladanie vyrovnávacej pamäte a optimalizácia modelov
- Architektúry založené na agentoch

## Ciele učenia

Po dokončení tohto modulu budete:

- **Ovládať Foundry Local**: Inštalovať, konfigurovať a optimalizovať pre vývoj vo Windows 11
- **Nasadiť rôznorodé modely**: Spúšťať modely phi, qwen, deepseek a GPT lokálne pomocou príkazov CLI
- **Vytvárať produkčné riešenia**: Tvorba AI aplikácií s pokročilým prompt inžinierstvom a integráciou dát
- **Využívať open-source ekosystém**: Integrácia modelov Hugging Face a príspevkov komunity
- **Vyvíjať AI agentov**: Budovať inteligentných agentov s možnosťami uzemnenia a orchestrácie
- **Implementovať podnikové vzory**: Vytvárať modulárne, škálovateľné AI riešenia pre produkčné nasadenie

## Štruktúra kurzu

### [1: Začíname s Foundry Local](./01.FoundryLocalSetup.md)
**Zameranie**: Inštalácia, nastavenie CLI, nasadenie modelov a hardvérová optimalizácia

**Kľúčové témy**: Kompletná inštalácia • CLI príkazy • Ukladanie modelov do vyrovnávacej pamäte • Hardvérové zrýchlenie • Nasadenie viacerých modelov

**Ukážka**: [REST Chat Quickstart](./samples/01/README.md) • [Integrácia OpenAI SDK](./samples/02/README.md) • [Objavovanie a Benchmarking modelov](./samples/03/README.md)

**Trvanie**: 2-3 hodiny | **Úroveň**: Začiatočník

---

### [2: Vytváranie AI riešení s Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Zameranie**: Pokročilé prompt inžinierstvo, integrácia dát a cloudové prepojenie

**Kľúčové témy**: Prompt inžinierstvo • Integrácia dát • Azure workflow • Optimalizácia výkonu • Monitorovanie

**Ukážka**: [Chainlit RAG aplikácia](./samples/04/README.md)

**Trvanie**: 2-3 hodiny | **Úroveň**: Stredne pokročilý

---

### [3: Open-Source modely v Foundry Local](./03.OpenSourceModels.md)
**Zameranie**: Integrácia Hugging Face, stratégie BYOM a community modely

**Kľúčové témy**: Integrácia Hugging Face • Prineste si vlastný model • Model Mondays postrehy • Príspevky komunity • Výber modelov

**Ukážka**: [Orchestrácia viacerých agentov](./samples/05/README.md)

**Trvanie**: 2-3 hodiny | **Úroveň**: Stredne pokročilý

---

### [4: Preskúmanie špičkových modelov](./04.CuttingEdgeModels.md)
**Zameranie**: LLM vs SLM, implementácia EdgeAI a pokročilé ukážky

**Kľúčové témy**: Porovnanie modelov • Inferencia na edge vs v cloude • Phi + ONNX Runtime • Chainlit RAG app • WebGPU optimalizácia

**Ukážka**: [Router Modelov ako nástrojov](./samples/06/README.md)

**Trvanie**: 3-4 hodiny | **Úroveň**: Pokročilý

---

### [5: Rýchla tvorba AI-poháňaných agentov](./05.AIPoweredAgents.md)
**Zameranie**: Architektúry agentov, systémové prompty, uzemnenie a orchestrácia

**Kľúčové témy**: Dizajnové vzory agentov • Systémové prompt inžinierstvo • Uzemňovacie techniky • Multi-agentné systémy • Produkčné nasadenie

**Ukážka**: [Orchestrácia viacerých agentov](./samples/05/README.md) • [Pokročilý multi-agentný systém](./samples/09/README.md)

**Trvanie**: 3-4 hodiny | **Úroveň**: Pokročilý

---

### [6: Foundry Local – Modely ako nástroje](./06.ModelsAsTools.md)
**Zameranie**: Modulárne AI riešenia, podnikové škálovanie a produkčné vzory

**Kľúčové témy**: Modely ako nástroje • Nasadenie na zariadení • Integrácia SDK/API • Podnikové architektúry • Škálovacie stratégie

**Ukážka**: [Router modelov ako nástrojov](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Trvanie**: 3-4 hodiny | **Úroveň**: Expert

---

### [7: Priame vzory integrácie API](./samples/07/README.md)
**Zameranie**: Čisto REST API integrácia bez závislostí SDK pre maximálnu kontrolu

**Kľúčové témy**: Implementácia HTTP klienta • Vlastná autentifikácia • Monitorovanie zdravia modelu • Streaming odpovede • Riešenie chýb v produkcii

**Ukážka**: [Priamy API klient](./samples/07/README.md)

**Trvanie**: 2-3 hodiny | **Úroveň**: Stredne pokročilý

---

### [8: Nativná chatová aplikácia pre Windows 11](./samples/08/README.md)
**Zameranie**: Tvorba moderných natívnych chatových aplikácií s integráciou Foundry Local

**Kľúčové témy**: Vývoj v Electron • Fluent Design System • Nativná integrácia Windows • Streaming v reálnom čase • Návrh chatového rozhrania

**Ukážka**: [Windows 11 Chat Application](./samples/08/README.md)

**Trvanie**: 3-4 hodiny | **Úroveň**: Pokročilý

---

### [9: Pokročilá orchestrácia multi-agentov](./samples/09/README.md)
**Zameranie**: Sofistikovaná koordinácia agentov, špecializované prideľovanie úloh a kolaboratívne AI workflowy

**Kľúčové témy**: Inteligentná koordinácia agentov • Vzory volania funkcií • Komunikácia medzi agentmi • Orchestrácia workflow • Mechanizmy zabezpečenia kvality

**Ukážka**: [Pokročilý multi-agentný systém](./samples/09/README.md)

**Trvanie**: 4-5 hodín | **Úroveň**: Expert

---

### [10: Foundry Local ako nástrojový framework](./samples/10/README.md)
**Zameranie**: Architektúra orientovaná na nástroje pre integráciu Foundry Local do existujúcich aplikácií a frameworkov

**Kľúčové témy**: Integrácia LangChain • Funkcie Semantic Kernel • REST API frameworky • CLI nástroje • Jupyter integrácia • Produkčné vzory nasadenia

**Ukážka**: [Foundry Tools Framework](./samples/10/README.md)

**Trvanie**: 4-5 hodín | **Úroveň**: Expert

## Predpoklady

### Systémové požiadavky
- **Operačný systém**: Windows 11 (22H2 alebo novší)
- **Pamäť**: 16 GB RAM (32 GB odporúčané pre väčšie modely)
- **Úložisko**: 50 GB voľného miesta pre vyrovnávaciu pamäť modelov
- **Hardvér**: Odporúčané zariadenie s NPU (Copilot+ PC), GPU voliteľné
- **Sieť**: Vysokorýchlostný internet pre počiatočné stiahnutie modelov

### Vývojové prostredie

- Visual Studio Code s rozšírením AI Toolkit
- Python 3.10+ a pip
- Git na správu verzií
- PowerShell alebo Príkazový riadok
- Azure CLI (voliteľné pre cloudovú integráciu)

### Predchádzajúce znalosti
- Základné pochopenie konceptov AI/ML
- Znalosť práce s príkazovým riadkom
- Základy programovania v Pythone
- Koncepty REST API
- Základné poznatky o promptovaní a inferencii modelov

## Časový harmonogram modulu

**Celkový odhadovaný čas**: 30-38 hodín

| Sedenie | Zameranie | Ukážky | Čas | Náročnosť |
|---------|------------|---------|------|------------|
|  1 | Nastavenie & základy | 01, 02, 03 | 2-3 hodiny | Začiatočník |
|  2 | Riešenia AI | 04 | 2-3 hodiny | Stredne pokročilý |
|  3 | Open Source | 05 | 2-3 hodiny | Stredne pokročilý |
|  4 | Pokročilé modely | 06 | 3-4 hodiny | Pokročilý |
|  5 | AI agenti | 05, 09 | 3-4 hodiny | Pokročilý |
|  6 | Podnikové nástroje | 06, 10 | 3-4 hodiny | Expert |
|  7 | Priama integrácia API | 07 | 2-3 hodiny | Stredne pokročilý |
|  8 | Windows 11 chat aplikácia | 08 | 3-4 hodiny | Pokročilý |
|  9 | Pokročilý multi-agent | 09 | 4-5 hodín | Expert |
| 10 | Rámec nástrojov | 10 | 4-5 hodín | Expert |

## Kľúčové zdroje

**Oficiálna dokumentácia:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Zdrojový kód a oficiálne ukážky
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Kompletný sprievodca inštaláciou a používaním
- [Model Mondays Series](https://aka.ms/model-mondays) - Týždenné zdôraznenie modelov a návody

**Komunita & Podpora:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - Otázky, odpovede a požiadavky na funkcie komunity
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Najnovšie správy a najlepšie postupy

## Výsledky učenia

Po dokončení tohto modulu budete schopní:

### Technická zručnosť
- **Nasadzovať a spravovať**: Inštalácie Foundry Local v prostredí vývoja a produkcie
- **Integrovať modely**: Bezproblémovo pracovať s rôznymi modelovými rodinami od Microsoft, Hugging Face a komunitných zdrojov
- **Vytvárať aplikácie**: Vytvárať produkčne pripravené AI aplikácie s pokročilými funkciami a optimalizáciami
- **Vyvíjať agentov**: Implementovať sofistikovaných AI agentov s podkladom, usudzovaním a integráciou nástrojov

### Strategické pochopenie
- **Rozhodnutia o architektúre**: Robiť informované rozhodnutia medzi lokálnym a cloudovým nasadením
- **Optimalizácia výkonu**: Optimalizovať výkon inferencie na rôznych hardvérových konfiguráciách
- **Škálovanie pre podniky**: Navrhovať aplikácie, ktoré škálujú od lokálnych prototypov po podnikové nasadenia
- **Súkromie a bezpečnosť**: Implementovať riešenia AI zachovávajúce súkromie s lokálnou inferenciou

### Inovačné schopnosti
- **Rýchle prototypovanie**: Rýchlo vytvárať a testovať koncepty AI aplikácií vo všetkých 10 ukážkových vzoroch
- **Integrácia komunity**: Využívať open-source modely a prispievať do ekosystému
- **Pokročilé vzory**: Implementovať špičkové AI vzory vrátane RAG, agentov a integrácie nástrojov
- **Znalosť rámcov**: Expertna integrácia s LangChain, Semantic Kernel, Chainlit a Electron
- **Produkčné nasadenie**: Nasadzovať škálovateľné AI riešenia od lokálnych prototypov po podnikové systémy
- **Vývoj pripravený na budúcnosť**: Vytvárať aplikácie pripravené na vznikajúce AI technológie a vzory

## Začnite

1. **Nastavenie prostredia**: Zaistite Windows 11 s odporúčaným hardvérom (pozri Predchádzajúce požiadavky)
2. **Inštalujte Foundry Local**: Postupujte podľa relácie 1 pre kompletnú inštaláciu a konfiguráciu
3. **Spustite ukážku 01**: Začnite s jednoduchou integráciou REST API na overenie nastavenia
4. **Prejdite ukážky**: Dokončite ukážky 01-10 pre komplexné osvojenie

## Metriky úspechu

Sledujte svoj pokrok cez všetkých 10 komplexných ukážok:

### Základná úroveň (Ukážky 01-03)
- [ ] Úspešne nainštalovať a nakonfigurovať Foundry Local
- [ ] Dokončiť integráciu REST API (Ukážka 01)
- [ ] Implementovať kompatibilitu OpenAI SDK (Ukážka 02)
- [ ] Vykonať objavovanie modelov a benchmarkovanie (Ukážka 03)

### Aplikačná úroveň (Ukážky 04-06)
- [ ] Nasadiť a spustiť minimálne 4 rôzne modelové rodiny
- [ ] Vytvoriť funkčnú RAG chat aplikáciu (Ukážka 04)
- [ ] Vytvoriť multi-agentný orchestráciový systém (Ukážka 05)
- [ ] Implementovať inteligentné smerovanie modelov (Ukážka 06)

### Pokročilá úroveň integrácie (Ukážky 07-10)
- [ ] Vytvoriť produkčne pripraveného API klienta (Ukážka 07)
- [ ] Vyvinúť natívnu chat aplikáciu pre Windows 11 (Ukážka 08)
- [ ] Implementovať pokročilý multi-agentný systém (Ukážka 09)
- [ ] Vytvoriť komplexný rámec nástrojov (Ukážka 10)

### Ukazovatele majstrovskej úrovne
- [ ] Úspešne spustiť všetkých 10 ukážok bez chýb
- [ ] Prispôsobiť aspoň 3 ukážky pre konkrétne použitia
- [ ] Nasadiť 2 a viac ukážok v prostredí podobnom produkcii
- [ ] Prispieť zlepšenia alebo rozšírenia kódov ukážok
- [ ] Integrovať vzory Foundry Local do osobných/profesionálnych projektov

## Rýchly úvod - Všetkých 10 ukážok

### Nastavenie prostredia (požadované pre všetky ukážky)

```powershell
# 1. Klonujte a prejdite do Module08
cd Module08

# 2. Vytvorte virtuálne prostredie Python
py -m venv .venv
.\.venv\Scripts\activate

# 3. Nainštalujte základné závislosti
pip install -r requirements.txt

# 4. Nainštalujte Foundry Local (ak ešte nie je nainštalovaný)
winget install Microsoft.FoundryLocal

# 5. Overte inštaláciu Foundry Local
foundry --version
foundry model list
```

### Základné vzorové ukážky (01-06)

**Ukážka 01: Rýchly štart REST chatu**
```powershell
# Spustite lokálnu službu Foundry
foundry model run phi-4-mini

# Spustiť ukážku chatovania REST
python samples/01/chat_quickstart.py
```

**Ukážka 02: Integrácia OpenAI SDK**
```powershell
# Uistite sa, že model beží
foundry status

# Spustite demo SDK
python samples/02/sdk_quickstart.py
```

**Ukážka 03: Objavovanie a benchmarkovanie modelov**
```powershell
# Spustiť komplexné testovanie modelu
samples/03/list_and_bench.cmd

# Alebo spustiť jednotlivé komponenty
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Ukážka 04: Chainlit RAG aplikácia**
```powershell
# Nainštalujte závislosti Chainlit
pip install chainlit langchain chromadb

# Spustite aplikáciu RAG chat
chainlit run samples/04/app.py -w
# Otvára prehliadač na http://localhost:8000
```

**Ukážka 05: Multi-agentná orchestrácia**
```powershell
# Spustiť demo koordinátora agenta
python -m samples.05.agents.coordinator

# Spustiť príklady konkrétnych agentov
python samples/05/examples/specialists_demo.py
```

**Ukážka 06: Router modelov ako nástrojov**
```powershell
# Konfigurovať prostredie
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Spustiť inteligentný smerovač
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Pokročilé integračné ukážky (07-10)

**Ukážka 07: Priamy API klient**
```powershell
# Prejdite do ukážkového adresára
cd samples/07

# Nainštalujte ďalšie závislosti
pip install -r requirements.txt

# Spustite základné API príklady
python examples/basic_usage.py

# Vyskúšajte streamovanie odpovedí
python examples/streaming.py

# Otestujte produkčné vzory
python examples/production.py
```

**Ukážka 08: Chat aplikácia Windows 11**
```powershell
# Prejdite do ukážkového adresára
cd samples/08

# Nainštalujte závislosti Node.js
npm install

# Spustite aplikáciu Electron
npm start

# Alebo zostavte pre produkciu
npm run build
```

**Ukážka 09: Pokročilý multi-agentný systém**
```powershell
# Prejdite do ukážkového priečinka
cd samples/09

# Nainštalujte systémové závislosti agenta
pip install -r requirements.txt

# Spustite základnú ukážku koordinácie
python examples/basic_coordination.py

# Vyskúšajte zložitý pracovný tok
python examples/complex_workflow.py

# Interaktívna ukážka agenta
python examples/interactive_demo.py
```

**Ukážka 10: Rámec nástrojov Foundry**
```powershell
# Prejdite do adresára vzoriek
cd samples/10

# Nainštalujte závislosti rámca
pip install -r requirements.txt

# Spustite ukážku základných nástrojov
python examples/basic_tools.py

# Spustite REST API server
python examples/rest_api_server.py
# API dostupné na http://localhost:8080

# Vyskúšajte CLI aplikáciu
python examples/cli_application.py --help

# Spustite Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Otestujte integráciu LangChainu
python examples/langchain_demo.py
```

### Riešenie bežných problémov

**Chyby pripojenia Foundry Local**
```powershell
# Skontrolujte stav služby
foundry status

# Reštartujte, ak je to potrebné
foundry restart

# Overte prístupnosť koncového bodu
curl http://localhost:5273/v1/models
```

**Problémy s načítavaním modelov**
```powershell
# Skontrolujte dostupné modely
foundry model list --cached

# Stiahnite chýbajúce modely
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Vynútiť opätovné načítanie, ak je to potrebné
foundry model unload --all
foundry model run phi-4-mini
```

**Problémy so závislosťami**
```powershell
# Aktualizujte pip a znova nainštalujte
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# Pre ukážky Node.js
npm cache clean --force
npm install
```

## Zhrnutie


Tento modul predstavuje špičku vývoja edge AI, kombinujúc nástroje Microsoftu na úrovni podnikov s flexibilitou a inováciami open-source ekosystému. Ovládnutím Foundry Local cez všetkých 10 komplexných príkladov budete na čele vývoja AI aplikácií.

**Kompletná výučbová cesta:**
- **Základy** (Príklady 01-03): Integrácia API a správa modelov
- **Aplikácie** (Príklady 04-06): RAG, agenti a inteligentné smerovanie
- **Pokročilé** (Príklady 07-10): Produkčné frameworky a podniková integrácia

Pre integráciu Azure OpenAI (časť 2) si pozrite README súbory jednotlivých príkladov pre požadované environmentálne premenné a nastavenia verzie API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->