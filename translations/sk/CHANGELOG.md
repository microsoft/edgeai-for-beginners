# Zoznam zmien

Všetky významné zmeny v EdgeAI pre Začiatočníkov sú tu zdokumentované. Tento projekt používa zápisy založené na dátume a štýl Keep a Changelog (Pridané, Zmenené, Opravené, Odstránené, Dokumentácia, Presunuté).

## 2025-10-30

### Pridané - Modul06 AI Agentov komplexné vylepšenie
- **Integrácia Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Kompletná sekcia o Microsoft Agent Framework pre produkčne pripravený vývoj agentov
  - Podrobné integračné vzory s Foundry Local pre edge nasadenie
  - Príklady multi-agent orchestrácie so špecializovanými SLM modelmi
  - Podnikové vzory nasadenia s manažmentom zdrojov a monitorovaním
  - Funkcie zabezpečenia a dodržiavania predpisov pre edge agent systémy
  - Reálne príklady implementácie (retail, zdravotníctvo, zákaznícky servis)

- **Stratégie produkčného nasadenia SLM agentov**:
  - **Foundry Local**: Kompletná dokumentácia podnikovej úrovne edge AI runtime s inštaláciou, konfiguráciou a produkčnými vzormi
  - **Ollama**: Vylepšené komunitné nasadenie s komplexným monitorovaním a správou modelov
  - **VLLM**: Výkonný inference engine s pokročilými optimalizačnými technikami a podnikateľskými funkciami
  - Kontrolné zoznamy nasadenia a porovnávacie tabuľky pre všetky tri platformy

- **Vylepšenie edge-optimalizovaných SLM frameworkov**:
  - **ONNX Runtime**: Nová komplexná sekcia pre multiplatformové nasadenie SLM agentov
  - Univerzálne nasadzovacie vzory pre Windows, Linux, macOS, iOS a Android
  - Možnosti hardvérovej akcelerácie (CPU, GPU, NPU) s automatickou detekciou
  - Produkčne pripravené funkcie a agent-specifické optimalizácie
  - Kompletné príklady implementácie s integráciou Microsoft Agent Framework

- **Referencie a ďalšie čítanie**:
  - Komplexná knižnica zdrojov s viac než 100 autoritatívnymi zdrojmi
  - Kľúčové výskumné články o AI agentoch a malých jazykových modeloch
  - Oficiálna dokumentácia všetkých veľkých frameworkov a nástrojov
  - Priemyselné správy, analýzy trhu a technické benchmarky
  - Vzdelávacie zdroje, konferencie a komunitné fóra
  - Štandardy, špecifikácie a rámce dodržiavania predpisov

### Zmenené - Modernizácia obsahu Modulu06
- **Vylepšené vzdelávacie ciele**: Pridaná majstrovská znalosť Microsoft Agent Framework a schopnosti edge nasadenia
- **Produkčné zameranie**: Posun od konceptuálneho k implementačne pripravenému s produkčnými príkladmi
- **Príklady kódu**: Aktualizované všetky príklady na moderné vzory SDK a najlepšie praktiky
- **Architektonické vzory**: Pridané hierarchické agentové architektúry a koordinácia edge-to-cloud
- **Optimalizácia výkonu**: Vylepšené o manažment zdrojov a odporúčania pre automatické škálovanie

### Dokumentácia - Vylepšenie štruktúry Modulu06
- **Komplexné pokrytie Agent Frameworku**: Od základných konceptov po podnikové nasadenie
- **Stratégie produkčného nasadenia**: Kompletné návody pre Foundry Local, Ollama a VLLM
- **Optimalizácia naprieč platformami**: Pridaný ONNX Runtime pre univerzálne nasadenie
- **Knižnica zdrojov**: Rozsiahle odkazy pre pokračujúce učenie a implementáciu

### Pridané - Aktualizácia dokumentácie protokolu Model Context Protocol (MCP) v Module06
- **Modernizácia úvodu MCP** (`Module06/03.IntroduceMCP.md`):
  - Aktualizované podľa najnovších špecifikácií MCP z modelcontextprotocol.io (verzia 2025-06-18)
  - Pridaná oficiálna USB-C analógia pre štandardizované AI aplikácie
  - Aktualizovaná sekcia architektúry s oficiálnym dvojvrstvovým dizajnom (Data Layer + Transport Layer)
  - Vylepšená dokumentácia základných primitív so serverovými primitívmi (Nástroje, Zdroje, Výzvy) a klientskými primitívmi (Sampling, Elicitation, Logging)

- **Komplexné MCP referencie a zdroje**:
  - Pridaný odkaz na **MCP pre začiatočníkov** (https://aka.ms/mcp-for-beginners) 
  - Oficiálna MCP dokumentácia a špecifikácie (modelcontextprotocol.io)
  - Vývojové zdroje vrátane MCP Inspector a referenčných implementácií
  - Technické štandardy (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Pridané - Integrácia Qualcomm QNN v Module04
- **Nová Sekcia 7: Qualcomm QNN Optimalizačný balík** (`Module04/05.QualcommQNN.md`):
  - Kompletný 400+ riadkový návod pokrývajúci Qualcomm unified AI inference framework
  - Podrobný prehľad heterogénneho výpočtu (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardvérový-aware optimalizácie pre Snapdragon platformy s inteligentným rozdelením záťaže
  - Pokročilé kvantizačné techniky (INT8, INT16, mixed-precision) pre mobilné nasadenie
  - Energeticky efektívna optimalizácia inferencie pre batériou napájané zariadenia a realtime aplikácie
  - Kompletný inštalačný návod s nastavením QNN SDK a konfiguráciou prostredia
  - Praktické príklady: konverzia PyTorch na QNN, multi-backend optimalizácia, generovanie kontextového binárneho súboru
  - Pokročilé vzory použitia: vlastná konfigurácia backendu, dynamická kvantizácia, profilovanie výkonu
  - Komplexná sekcia riešenia problémov a komunitné zdroje

- **Vylepšená štruktúra Modulu04**:
  - Aktualizovaný README.md s 7 progresívnymi sekciami (predtým 6)
  - Pridaný Qualcomm QNN do tabuľky benchmarkov výkonu (5-15x zrýchlenie, 50-80% zníženie pamäte)
  - Komplexné vzdelávacie výsledky pre mobilné AI nasadenie a optimalizáciu spotreby energie

### Zmenené - Aktualizácie dokumentácie Modulu04
- **Vylepšenie dokumentácie Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Pridaná kompletná sekcia "Olive Recipes Repository" s viac než 100 predpripravenými optimalizačnými receptami
  - Podrobný prehľad podporovaných rodín modelov (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktické príklady použitia na prispôsobovanie receptov a komunitné príspevky
  - Vylepšené benchmarky výkonu a integračné návody

- **Premiestnenie sekcií v Module04**:
  - Apple MLX presunutý na Sekciu 5 (predtým Sekcia 6)
  - Workflow Synthesis presunutý na Sekciu 6 (predtým Sekcia 7)  
  - Qualcomm QNN zaradený ako Sekcia 7 (špecializované zameranie na mobilné/edge)
  - Aktualizované všetky odkazy na súbory a navigačné linky podľa zmien

### Opravené - Validácia vzoriek Workshopu
- **Validácia a oprava chat_bootstrap.py**:
  - Opravený poškodený import (`util.util.workshop_utils` → `util.workshop_utils`)
  - Vytvorený chýbajúci `__init__.py` v balíku util pre správne rozpoznanie Python modulu
  - Nainštalované potrebné závislosti (openai, foundry-local-sdk) v conda prostredí
  - Úspešná validácia spustenia vzorky s použitím predvolených aj vlastných promptov
  - Potvrdená integrácia so službou Foundry Local a načítanie modelu (phi-4-mini s CUDA optimalizáciou)

### Dokumentácia - Komplexné aktualizácie navigácie
- **Kompletná rekonštrukcia README.md Modulu04**:
  - Pridaný Qualcomm QNN ako hlavný optimalizačný framework vedľa OpenVINO, Olive, MLX
  - Aktualizované výukové výsledky kapitol s mobilným AI nasadením a optimalizáciou spotreby
  - Vylepšená tabuľka porovnania výkonu s metrikami QNN a prípadmi použitia na mobilné/edge
  - Zachovaná logická postupnosť od podnikových riešení po platformovo špecifické optimalizácie

- **Krížové odkazy a navigácia**:
  - Aktualizované všetky interné odkazy a referencie súborov na nové číslovanie sekcií
  - Rozšírený popis workflow synthesis o mobilné, desktopové a cloudové prostredia
  - Pridané komplexné odkazy na Qualcomm developerský ekosystém

## 2025-10-08

### Pridané - Komplexná aktualizácia Workshopu
- **Kompletné prepísanie README.md Workshopu**:
  - Pridané komplexné predstavenie vysvetľujúce hodnotovú ponuku Edge AI (súkromie, výkon, náklady)
  - Vytvorených 6 základných vzdelávacích cieľov s detailnými kompetenciami
  - Pridaná tabuľka výsledkov učenia s výstupmi a maticou kompetencií
  - Zaradená sekcia zručností pripravených na kariéru pre priemyselnú relevantnosť
  - Pridaný rýchly úvod s predpokladmi a nastavením v 3 krokoch
  - Vytvorené tabuľky zdrojov pre Python vzorky (8 súborov s časmi spustenia)
  - Pridaná tabuľka Jupyter notebookov (8 notebookov s hodnoteniami náročnosti)
  - Vytvorená tabuľka dokumentácie (7 kľúčových dokumentov s "Použiť keď" odporúčaniami)
  - Pridané odporúčania študijných ciest pre rozličné úrovne zručností

- **Validácia a testovacia infraštruktúra Workshopu**:
  - Vytvorený `scripts/validate_samples.py` - Komplexný nástroj na validáciu syntaxe, importov a najlepších praktík
  - Vytvorený `scripts/test_samples.py` - Smoke test pre všetky Python vzorky
  - Pridaná dokumentácia validácie do `scripts/README.md`

- **Komplexná dokumentácia**:
  - Vytvorený `SAMPLES_UPDATE_SUMMARY.md` - 400+ riadkový detailný návod pokrývajúci všetky vylepšenia
  - Vytvorený `UPDATE_COMPLETE.md` - Výkonný súhrn dokončenia aktualizácie
  - Vytvorený `QUICK_REFERENCE.md` - Rýchla referenčná karta Workshopu

### Zmenené - Modernizácia Python vzoriek Workshopu
- **Aktualizované všetky 8 Python vzoriek podľa najlepších praktík**:
  - Vylepšené zachytávanie chýb pomocou try-except blokov okolo všetkých I/O operácií
  - Pridané typové anotácie a komplexné docstringy
  - Implementovaný konzistentný vzor logovania [INFO]/[ERROR]/[RESULT]
  - Ochrana voliteľných importov s inštalačnými nápovedami
  - Zlepšená spätná väzba používateľovi vo všetkých vzorkách

- **session01/chat_bootstrap.py**:
  - Vylepšená inicializácia klienta s komplexnými chybovými správami
  - Vylepšené zachytávanie chýb pri streamovaní s validáciou chunkov
  - Pridané lepšie spracovanie výnimiek pri nedostupnosti služby

- **session02/rag_pipeline.py**:
  - Pridané obmedzenia importu pre sentence-transformers s inštalačnými nápovedami
  - Vylepšené zachytávanie chýb pre embedding a generovanie
  - Zlepšené formátovanie výstupu so štruktúrovanými výsledkami

- **session02/rag_eval_ragas.py**:
  - Ochrana voliteľných importov (ragas, datasets) s užívateľsky prívetivými chybovými správami
  - Pridané spracovanie chýb pri vyhodnocovacích metriách
  - Vylepšené formátovanie výstupu hodnotiacich výsledkov

- **session03/benchmark_oss_models.py**:
  - Implementované elegantné zlyhanie (pokračovanie napriek chybám modelu)
  - Pridané detailné reportovanie priebehu a spracovanie chýb na model
  - Vylepšený výpočet štatistík s komplexným zotavením z chýb

- **session04/model_compare.py**:
  - Pridané typové hinty (návratové typy Tuple)
  - Vylepšené formátovanie výstupu so štruktúrovanými JSON výsledkami
  - Implementované spracovanie chýb na model s obnovou

- **session05/agents_orchestrator.py**:
  - Vylepšená metóda Agent.act() s komplexnými docstringami
  - Pridané spracovanie chýb pipeline s logovaním na jednotlivých fázach
  - Zlepšená správa pamäte a sledovanie stavu

- **session06/models_router.py**:
  - Vylepšená dokumentácia funkcií pre všetky komponenty routovania
  - Pridané detailné logovanie vo funkcii route()
  - Zlepšený testovací výstup so štruktúrovanými výsledkami

- **session06/models_pipeline.py**:
  - Pridané spracovanie chýb do pomocnej funkcie chat()
  - Vylepšená pipeline() s logovaním fáz a reportovaním priebehu
  - Zlepšená main() s komplexným zotavením z chýb

### Dokumentácia - Vylepšenie Workshop dokumentácie
- Aktualizovaný hlavný README.md so sekciou Workshop zdôrazňujúcou praktickú študijnú cestu
- Vylepšený STUDY_GUIDE.md s komplexnou sekciou Workshop vrátane:
  - vzdelávacích cieľov a zameraných oblastí štúdia
  - otázok na sebahodnotenie
  - praktických cvičení s odhadmi času
  - časového rozvrhnutia pre intenzívne a čiastočné štúdium
  - Pridaný Workshop do šablóny sledovania pokroku
- Aktualizovaný návod na rozdelenie času z 20 hodín na 30 hodín (vrátane Workshopu)
- Pridané popisy vzoriek Workshopu a vzdelávacie výsledky do README

### Opravené
- Riešenie nekonzistentných vzorov spracovania chýb vo vzorkách Workshopu
- Opravené chyby s voliteľnými závislosťami importu s adekvátnymi ochranami
- Opravené chýbajúce typové hinty v kritických funkciách
- Vylepšená spätná väzba používateľovi pri chybových scenároch
- Opravené problémy validácie s komplexnou testovacou infraštruktúrou

---

## 2025-09-23

### Zmenené - Veľká modernizácia Modulu 08
- **Komplexné zosúladenie s repozitárom Microsoft Foundry-Local**
  - Aktualizované všetky príklady kódu na použitie moderného `FoundryLocalManager` a integrácie OpenAI SDK
  - Nahradené zastarané manuálne volania `requests` správnym použitím SDK
  - Zosúladené implementačné vzory s oficiálnou Microsoft dokumentáciou a príkladmi

- **Modernizácia 05.AIPoweredAgents.md**:
  - Aktualizovaná multi-agent orchestrácia na použitie moderných SDK vzorov
  - Vylepšená implementácia koordinátora s pokročilými funkciami (smyčky spätnej väzby, monitorovanie výkonu)
  - Pridané komplexné spracovanie chýb a kontrola stavu služieb
  - Integrované správne odkazy na lokálne vzorky (`samples/05/multi_agent_orchestration.ipynb`)
  - Aktualizované príklady volania funkcií na použitie moderného parametra `tools` namiesto zastaraného `functions`
  - Pridané produkčne pripravené vzory s monitorovaním a sledovaním štatistík

- **Kompletné prepísanie 06.ModelsAsTools.md**:
  - Nahradený základný registrovací nástroj inteligentnou implementáciou routera modelov
  - Pridaný výber modelu na základe kľúčových slov pre rôzne typy úloh (všeobecné, odôvodňovanie, kód, kreativita)
  - Integrovaná konfigurácia založená na prostredí s flexibilným priraďovaním modelov
  - Vylepšené o komplexné monitorovanie stavu služieb a spracovanie chýb
  - Pridané produkčné vzory nasadenia s monitorovaním požiadaviek a sledovaním výkonu
  - Zosúladené s lokálnou implementáciou v `samples/06/router.py` a `samples/06/model_router.ipynb`

- **Zlepšenia štruktúry dokumentácie**:
  - Pridané prehľadové sekcie zdôrazňujúce modernizáciu a zosúladenie so SDK
  - Vylepšené pomocou emotikonov a lepšieho formátovania pre lepšiu čitateľnosť
  - Pridané správne odkazy na lokálne vzorky v celej dokumentácii
  - Zahrnuté pokyny pre produkčne pripravené implementácie a najlepšie praktiky

### Pridané
- Komplexné prehľadové sekcie v súboroch Modulu 08 zdôrazňujúce modernú integráciu SDK
- Architektonické zvýraznenie pokročilých funkcií (multi-agent systémy, inteligentné routovanie)
- Priame odkazy na lokálne implementácie vzorov pre praktickú skúsenosť
- Pokyny pre produkčné nasadenie s monitorovaním a vzormi spracovania chýb
- Interaktívne Jupyter notebook príklady s pokročilými funkciami a benchmarkami

### Opravené
- Nesúlady medzi dokumentáciou a skutočnými implementáciami vzoriek
- Zastaralé vzory používania SDK v celom Module 08
- Chýbajúce odkazy na komplexnú miestnu knižnicu vzoriek
- Nekonzistentné prístupy v implementácii v rôznych sekciách

---

## 2025-09-18

### Pridané
- Modul 08: Microsoft Foundry Local – Kompletný vývojársky toolkit
  - Šesť sekcií: nastavenie, integrácia Azure AI Foundry, open-source modely, moderné demo, agenti a modely ako nástroje
  - Spustiteľné vzorky pod `Module08/samples/01`–`06` s inštrukciami pre Windows cmd
    - `01` Rýchly REST chat (`chat_quickstart.py`)

    - `02` Rýchly štart SDK s podporou OpenAI/Foundry Local a Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orchestrácia viacerých agentov (`python -m samples.05.agents.coordinator`)
    - `06` Router typu Models-as-Tools (`router.py`)
- Podpora Azure OpenAI v ukážke Session 2 SDK s konfiguráciou cez premenné prostredia
- `.vscode/settings.json` nasmerované na `Module08/.venv` pre lepšie vyhodnocovanie Python analyzátorom
- `.env` s náznakom `PYTHONPATH` pre podporu vo VS Code/Pylance

### Zmenené
- Predvolený model aktualizovaný na `phi-4-mini` v dokumentácii a ukážkach Modulu 08; odstránené posledné zmienky o `phi-3.5` v rámci Modulu 08
- Vylepšenia routera (`Module08/samples/06/router.py`):
  - Objavovanie endpointov cez `foundry service status` s regex parsovaním
  - Kontrola zdravia `/v1/models` pri štarte
  - Registrácia modelov konfigurovateľná cez prostredie (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizované požiadavky: `Module08/requirements.txt` teraz obsahuje `openai` (spolu s `requests`, `chainlit`)
- Upravené usmernenie pre Chainlit ukážku a pridané riešenie problémov; vyriešenie importov cez nastavenia pracovného priestoru

### Opravené
- Riešené problémy s importmi:
  - Router už nezávisí na neexistujúcom module `utils`; funkcie sú vložené priamo
  - Koordinátor používa relatívny import (`from .specialists import ...`) a je spúšťaný cez cestu modulu
  - Konfigurácia VS Code/Pylance pre vyriešenie importov `chainlit` a balíčkov
- Opravená drobná preklep v `STUDY_GUIDE.md` a pridané pokrytie Modulu 08

### Odstránené
- Vymazaný nepoužívaný súbor `Module08/infra/obs.py` a odstránený prázdny adresár `infra/`; vzory sledovania zostávajú voliteľné v dokumentácii

### Presunuté
- Demo ukážky Modulu 08 zlúčené pod `Module08/samples` zoradené podľa čísla session
  - Chainlit aplikácia presunutá do `samples/04`
  - Agenti presunutí do `samples/05` a pridané súbory `__init__.py` pre vyriešenie balíkov

### Dokumentácia
- Dokumenty Modulu 08 a všetky sample README rozšírené o odkazy na Microsoft Learn a dôveryhodných dodávateľov
- `Module08/README.md` aktualizované s prehľadom sample, konfiguráciou routera a tipmi na validáciu
- Sekcia Windows Foundry Local v `Module07/README.md` overená podľa Learn dokumentácie
- `STUDY_GUIDE.md` aktualizovaný:
  - Pridaný Modul 08 do prehľadu, harmonogramov, sledovača pokroku
  - Pridaná komplexná sekcia Referencie (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## História (zhrnutie)
- Stanovená architektúra kurzu a moduly (Moduly 01–07)
- Iteratívna modernizácia obsahu, štandardizácia formátovania a pridanie prípadových štúdií
- Rozšírené pokrytie optimalizačných rámcov (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nezverejnené / backlog (návrhy)
- Voliteľné základné testy pre každý sample na overenie dostupnosti Foundry Local
- Prekontrolovať preklady na zladenie odkazov na modely (napr. `phi-4-mini`), kde je to vhodné
- Pridať minimálnu pyright konfiguráciu, ak tímy uprednostnia prísnosť v celom pracovnom priestore

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->