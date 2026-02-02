# Zmeny

Všetky významné zmeny v EdgeAI pre začiatočníkov sú zdokumentované tu. Tento projekt používa záznamy založené na dátume a štýl Keep a Changelog (Pridané, Zmenené, Opravené, Odstránené, Dokumentácia, Presunuté).

## 2025-10-30

### Pridané - Modul06 Komplexné vylepšenie AI agentov
- **Integrácia Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Kompletná sekcia o Microsoft Agent Framework pre vývoj agentov pripravených na produkciu
  - Podrobné vzory integrácie s Foundry Local pre nasadenie na okraji
  - Príklady orchestrácie viacerých agentov so špecializovanými SLM modelmi
  - Vzory nasadenia v podnikoch s riadením zdrojov a monitorovaním
  - Funkcie zabezpečenia a súladu pre systémy agentov na okraji
  - Príklady z reálneho sveta (maloobchod, zdravotníctvo, zákaznícky servis)

- **Stratégie nasadenia produkčných SLM agentov**:
  - **Foundry Local**: Kompletná dokumentácia pre podnikové AI runtime na okraji s inštaláciou, konfiguráciou a vzormi pre produkciu
  - **Ollama**: Rozšírené nasadenie zamerané na komunitu s komplexným monitorovaním a správou modelov
  - **VLLM**: Výkonný inferenčný engine s pokročilými optimalizačnými technikami a podnikovými funkciami
  - Kontrolné zoznamy pre nasadenie v produkcii a porovnávacie tabuľky pre všetky tri platformy

- **Vylepšenie rámcov SLM optimalizovaných pre okraj**:
  - **ONNX Runtime**: Nová komplexná sekcia pre nasadenie SLM agentov na rôznych platformách
  - Univerzálne vzory nasadenia na Windows, Linux, macOS, iOS a Android
  - Možnosti hardvérovej akcelerácie (CPU, GPU, NPU) s automatickou detekciou
  - Funkcie pripravené na produkciu a optimalizácie špecifické pre agentov
  - Kompletné implementačné príklady s integráciou Microsoft Agent Framework

- **Referencie a ďalšie čítanie**:
  - Rozsiahla knižnica zdrojov s viac ako 100 autoritatívnymi zdrojmi
  - Základné výskumné práce o AI agentoch a malých jazykových modeloch
  - Oficiálna dokumentácia pre všetky hlavné rámce a nástroje
  - Priemyselné správy, analýzy trhu a technické benchmarky
  - Vzdelávacie zdroje, konferencie a komunitné fóra
  - Normy, špecifikácie a rámce súladu

### Zmenené - Modernizácia obsahu Modul06
- **Vylepšené vzdelávacie ciele**: Pridané zvládnutie Microsoft Agent Framework a schopnosti nasadenia na okraji
- **Zameranie na produkciu**: Posun od konceptuálneho k implementačne pripravenému sprievodcovi s príkladmi z produkcie
- **Príklady kódu**: Aktualizované všetky príklady na používanie moderných SDK vzorov a najlepších praktík
- **Architektonické vzory**: Pridané hierarchické architektúry agentov a koordinácia okraj-cloud
- **Optimalizácia výkonu**: Vylepšené odporúčaniami pre riadenie zdrojov a automatické škálovanie

### Dokumentácia - Vylepšenie štruktúry Modul06
- **Komplexné pokrytie rámca agentov**: Od základných konceptov po nasadenie v podnikoch
- **Stratégie nasadenia v produkcii**: Kompletné sprievodce pre Foundry Local, Ollama a VLLM
- **Optimalizácia na rôznych platformách**: Pridaný ONNX Runtime pre univerzálne nasadenie
- **Knižnica zdrojov**: Rozsiahle referencie pre ďalšie vzdelávanie a implementáciu

### Pridané - Aktualizácia dokumentácie Model Context Protocol (MCP) v Modul06
- **Modernizácia úvodu MCP** (`Module06/03.IntroduceMCP.md`):
  - Aktualizované najnovšími špecifikáciami MCP z modelcontextprotocol.io (verzia 2025-06-18)
  - Pridaná oficiálna analógia USB-C pre štandardizované AI aplikácie
  - Aktualizovaná sekcia architektúry s oficiálnym dvojvrstvovým dizajnom (Data Layer + Transport Layer)
  - Vylepšená dokumentácia základných primitív so serverovými primitívami (Nástroje, Zdroje, Výzvy) a klientskými primitívami (Sampling, Elicitation, Logging)

- **Komplexné referencie a zdroje MCP**:
  - Pridaný odkaz **MCP pre začiatočníkov** (https://aka.ms/mcp-for-beginners)
  - Oficiálna dokumentácia MCP a špecifikácie (modelcontextprotocol.io)
  - Vývojové zdroje vrátane MCP Inspector a referenčných implementácií
  - Technické normy (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Pridané - Modul04 Integrácia Qualcomm QNN
- **Nová sekcia 7: Qualcomm QNN Optimalizačný balík** (`Module04/05.QualcommQNN.md`):
  - Komplexný 400+ riadkový sprievodca pokrývajúci jednotný AI inferenčný rámec Qualcommu
  - Podrobné pokrytie heterogénneho výpočtu (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimalizácia zohľadňujúca hardvér pre platformy Snapdragon s inteligentným rozdelením záťaže
  - Pokročilé techniky kvantizácie (INT8, INT16, zmiešaná presnosť) pre mobilné nasadenie
  - Energeticky efektívna optimalizácia inferencie pre zariadenia na batérie a aplikácie v reálnom čase
  - Kompletný sprievodca inštaláciou s nastavením QNN SDK a konfiguráciou prostredia
  - Praktické príklady: Konverzia PyTorch na QNN, optimalizácia viacerých backendov, generovanie binárneho kontextu
  - Pokročilé vzory použitia: konfigurácia vlastného backendu, dynamická kvantizácia, profilovanie výkonu
  - Komplexná sekcia riešenia problémov a komunitné zdroje

- **Vylepšená štruktúra Modul04**:
  - Aktualizovaný README.md na zahrnutie 7 progresívnych sekcií (predtým 6)
  - Pridaný Qualcomm QNN do tabuľky benchmarkov výkonu (zlepšenie rýchlosti o 5-15x, zníženie pamäte o 50-80%)
  - Komplexné vzdelávacie výstupy pre mobilné AI nasadenie a optimalizáciu energie

### Zmenené - Aktualizácie dokumentácie Modul04
- **Vylepšenie dokumentácie Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Pridaná komplexná sekcia "Olive Recipes Repository" pokrývajúca viac ako 100 predpripravených optimalizačných receptov
  - Podrobné pokrytie podporovaných rodín modelov (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktické príklady použitia pre prispôsobenie receptov a príspevky komunity
  - Vylepšené benchmarky výkonu a pokyny na integráciu

- **Preusporiadanie sekcií v Modul04**:
  - Apple MLX presunuté na sekciu 5 (predtým sekcia 6)
  - Workflow Synthesis presunuté na sekciu 6 (predtým sekcia 7)
  - Qualcomm QNN umiestnené ako sekcia 7 (špecializované na mobilné/okrajové zameranie)
  - Aktualizované všetky referencie súborov a navigačné odkazy

### Opravené - Validácia vzoriek workshopu
- **Validácia a oprava chat_bootstrap.py**:
  - Opravený poškodený import (`util.util.workshop_utils` → `util.workshop_utils`)
  - Vytvorený chýbajúci `__init__.py` v balíku util pre správne rozpoznanie modulu Python
  - Nainštalované požadované závislosti (openai, foundry-local-sdk) v conda prostredí
  - Úspešne validované spustenie vzorky s predvolenými aj vlastnými výzvami
  - Potvrdená integrácia so službou Foundry Local a načítanie modelu (phi-4-mini s CUDA optimalizáciou)

### Dokumentácia - Aktualizácie komplexného sprievodcu
- **Kompletná reštrukturalizácia README.md Modul04**:
  - Pridaný Qualcomm QNN ako hlavný optimalizačný rámec vedľa OpenVINO, Olive, MLX
  - Aktualizované vzdelávacie výstupy kapitoly na zahrnutie mobilného AI nasadenia a optimalizácie energie
  - Vylepšená porovnávacia tabuľka výkonu s metrikami QNN a prípadmi použitia mobilného/okrajového nasadenia
  - Zachovaná logická postupnosť od podnikových riešení po optimalizácie špecifické pre platformu

- **Krížové odkazy a navigácia**:
  - Aktualizované všetky interné odkazy a referencie súborov pre nové číslovanie sekcií
  - Vylepšený popis Workflow Synthesis na zahrnutie mobilných, desktopových a cloudových prostredí
  - Pridané rozsiahle odkazy na zdroje pre ekosystém vývojárov Qualcomm

## 2025-10-08

### Pridané - Komplexná aktualizácia workshopu
- **Kompletné prepracovanie README.md workshopu**:
  - Pridaný komplexný úvod vysvetľujúci hodnotu Edge AI (súkromie, výkon, náklady)
  - Vytvorených 6 hlavných vzdelávacích cieľov s podrobnými kompetenciami
  - Pridaná tabuľka vzdelávacích výstupov s dodávkami a maticou kompetencií
  - Zahrnuté zručnosti pripravené na kariéru pre relevantnosť v priemysle
  - Pridaný rýchly sprievodca s predpokladmi a 3-krokovým nastavením
  - Vytvorené tabuľky zdrojov pre Python vzorky (8 súborov s časmi spustenia)
  - Pridaná tabuľka Jupyter notebookov (8 notebookov s hodnotením obtiažnosti)
  - Vytvorená tabuľka dokumentácie (7 kľúčových dokumentov s "Použiť kedy" odporúčaniami)
  - Pridané odporúčania pre vzdelávaciu cestu pre rôzne úrovne zručností

- **Validácia a testovacia infraštruktúra workshopu**:
  - Vytvorený `scripts/validate_samples.py` - Komplexný validačný nástroj pre syntax, importy a najlepšie praktiky
  - Vytvorený `scripts/test_samples.py` - Nástroj na rýchle testovanie všetkých Python vzoriek
  - Pridaná dokumentácia validácie do `scripts/README.md`

- **Komplexná dokumentácia**:
  - Vytvorený `SAMPLES_UPDATE_SUMMARY.md` - 400+ riadkový podrobný sprievodca pokrývajúci všetky vylepšenia
  - Vytvorený `UPDATE_COMPLETE.md` - Výkonný súhrn dokončenia aktualizácie
  - Vytvorený `QUICK_REFERENCE.md` - Rýchla referenčná karta pre workshop

### Zmenené - Modernizácia Python vzoriek workshopu
- **Všetkých 8 Python vzoriek aktualizovaných s najlepšími praktikami**:
  - Vylepšené spracovanie chýb s blokmi try-except okolo všetkých I/O operácií
  - Pridané typové náznaky a komplexné docstringy
  - Implementovaný konzistentný vzor logovania [INFO]/[ERROR]/[RESULT]
  - Chránené voliteľné importy s náznakmi inštalácie
  - Zlepšená spätná väzba používateľovi vo všetkých vzorkách

- **session01/chat_bootstrap.py**:
  - Vylepšená inicializácia klienta s komplexnými chybovými správami
  - Zlepšené spracovanie chýb pri streamovaní s validáciou blokov
  - Pridané lepšie spracovanie výnimiek pre nedostupnosť služby

- **session02/rag_pipeline.py**:
  - Pridané ochranné importy pre sentence-transformers s náznakmi inštalácie
  - Vylepšené spracovanie chýb pre operácie vkladania a generovania
  - Zlepšené formátovanie výstupu so štruktúrovanými výsledkami

- **session02/rag_eval_ragas.py**:
  - Chránené voliteľné importy (ragas, datasets) s priateľskými chybovými správami
  - Pridané spracovanie chýb pre hodnotiace metriky
  - Vylepšené formátovanie výstupu pre hodnotiace výsledky

- **session03/benchmark_oss_models.py**:
  - Implementovaná elegantná degradácia (pokračuje pri zlyhaní modelov)
  - Pridané podrobné hlásenie pokroku a spracovanie chýb pre každý model
  - Vylepšený výpočet štatistík s komplexným zotavením po chybách

- **session04/model_compare.py**:
  - Pridané typové náznaky (návratové typy Tuple)
  - Vylepšené formátovanie výstupu so štruktúrovanými JSON výsledkami
  - Implementované spracovanie chýb pre každý model so zotavením

- **session05/agents_orchestrator.py**:
  - Vylepšené Agent.act() s komplexnými docstringami
  - Pridané spracovanie chýb v pipeline s logovaním po jednotlivých etapách
  - Zlepšené riadenie pamäte a sledovanie stavu

- **session06/models_router.py**:
  - Vylepšená dokumentácia funkcií pre všetky komponenty smerovania
  - Pridané podrobné logovanie vo funkcii route()
  - Zlepšený testovací výstup so štruktúrovanými výsledkami

- **session06/models_pipeline.py**:
  - Pridané spracovanie chýb do pomocnej funkcie chat()
  - Vylepšené pipeline() s logovaním etáp a hlásením pokroku
  - Zlepšené main() s komplexným zotavením po chybách

### Dokumentácia - Vylepšenie dokumentácie workshopu
- Aktualizovaný hlavný README.md s sekciou workshopu zdôrazňujúcou praktickú vzdelávaciu cestu
- Vylepšený STUDY_GUIDE.md s komplexnou sekciou workshopu vrátane:
  - Vzdelávacích cieľov a oblastí zamerania štúdia
  - Otázok na sebahodnotenie
  - Praktických cvičení s odhadmi času
  - Časového rozvrhu pre koncentrované a čiastočné štúdium
  - Pridaný workshop do šablóny sledovania pokroku
- Aktualizovaný časový rozvrh z 20 hodín na 30 hodín (vrátane workshopu)
- Pridané popisy vzoriek workshopu a vzdelávacie výstupy do README

### Opravené
- Vyriešené nekonzistentné vzory spracovania chýb vo vzorkách workshopu
- Opravené chyby voliteľných importov s správnymi ochrannými mechanizmami
- Opravené chýbajúce typové náznaky v kritických funkciách
- Riešené nedostatočné spätné väzby používateľovi v scenároch chýb
- Opravené problémy validácie s komplexnou testovacou infraštruktúrou

---

## 2025-09-23

### Zmenené - Hlavná modernizácia Modul 08
- **Komplexné zosúladenie so vzormi úložiska Microsoft Foundry-Local**
  - Aktualizované všetky príklady kódu na používanie moderného `FoundryLocalManager` a integrácie OpenAI SDK
  - Nahradené zastarané manuálne volania `requests` správnym používaním SDK
  - Zosúladené implementačné vzory s oficiálnou dokumentáciou a vzorkami Microsoftu

- **Modernizácia 05.AIPoweredAgents.md**:
  - Aktualizovaná orchestrácia viacerých agentov na používanie moderných SDK vzorov
  - Vylep
  - Spustiteľné ukážky v `Module08/samples/01`–`06` s inštrukciami pre Windows cmd
    - `01` REST rýchly chat (`chat_quickstart.py`)
    - `02` SDK rýchly štart s podporou OpenAI/Foundry Local a Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI zoznam a testovanie (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orchestrácia viacerých agentov (`python -m samples.05.agents.coordinator`)
    - `06` Router Models-as-Tools (`router.py`)
- Podpora Azure OpenAI v SDK ukážke Session 2 s konfiguráciou environmentálnych premenných
- `.vscode/settings.json` nastavené na `Module08/.venv` pre zlepšenie analýzy Pythonu
- `.env` s nápovedou `PYTHONPATH` pre lepšiu orientáciu VS Code/Pylance

### Zmenené
- Predvolený model aktualizovaný na `phi-4-mini` v dokumentácii a ukážkach Module 08; odstránené zmienky o `phi-3.5` v Module 08
- Vylepšenia routera (`Module08/samples/06/router.py`):
  - Zisťovanie endpointov cez `foundry service status` s regex analýzou
  - Kontrola zdravia `/v1/models` pri štarte
  - Konfigurovateľný registrátor modelov cez environmentálne premenné (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizované požiadavky: `Module08/requirements.txt` teraz zahŕňa `openai` (spolu s `requests`, `chainlit`)
- Ujasnené pokyny k ukážke Chainlit a pridané riešenie problémov; vyriešenie importov cez nastavenia pracovného priestoru

### Opravené
- Vyriešené problémy s importom:
  - Router už nezávisí na neexistujúcom module `utils`; funkcie sú vložené
  - Koordinátor používa relatívny import (`from .specialists import ...`) a je spustený cez cestu modulu
  - Konfigurácia VS Code/Pylance na vyriešenie importov `chainlit` a balíkov
- Opravená drobná chyba v `STUDY_GUIDE.md` a pridané pokrytie Module 08

### Odstránené
- Vymazaný nepoužívaný `Module08/infra/obs.py` a odstránený prázdny adresár `infra/`; vzory pozorovateľnosti ponechané ako voliteľné v dokumentácii

### Presunuté
- Konsolidované ukážky Module 08 pod `Module08/samples` s priečinkami očíslovanými podľa relácií
  - Chainlit aplikácia presunutá do `samples/04`
  - Agenti presunutí do `samples/05` a pridané súbory `__init__.py` pre vyriešenie balíkov

### Dokumentácia
- Dokumentácia relácií Module 08 a všetky README ukážok obohatené o odkazy na Microsoft Learn a dôveryhodných dodávateľov
- `Module08/README.md` aktualizované s prehľadom ukážok, konfiguráciou routera a tipmi na validáciu
- `Module07/README.md` sekcia Windows Foundry Local overená voči dokumentácii Learn
- `STUDY_GUIDE.md` aktualizované:
  - Pridaný Module 08 do prehľadu, rozvrhov, sledovača pokroku
  - Pridaná komplexná sekcia Referencie (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historické (zhrnutie)
- Založená architektúra kurzu a moduly (Moduly 01–07)
- Iteratívna modernizácia obsahu, štandardizácia formátovania a pridanie prípadových štúdií
- Rozšírené pokrytie optimalizačných rámcov (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nezverejnené / Zásobník (návrhy)
- Voliteľné testy funkčnosti pre každú ukážku na overenie dostupnosti Foundry Local
- Preskúmanie prekladov na zosúladenie referencií modelov (napr. `phi-4-mini`) kde je to vhodné
- Pridanie minimálnej konfigurácie pyright, ak tímy preferujú prísnosť na úrovni pracovného priestoru

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.