# Změny

Veškeré významné změny v EdgeAI for Beginners jsou zde zdokumentovány. Tento projekt používá zápisy uspořádané podle data a styl Keep a Changelog (Přidáno, Změněno, Opraveno, Odebráno, Dokumentace, Přesunuto).

## 2025-10-30

### Přidáno - Rozsáhlé rozšíření modulu06 AI agentů
- **Integrace Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Kompletní sekce o Microsoft Agent Framework pro vývoj agentů připravených do produkce
  - Podrobné vzory integrace s Foundry Local pro edge nasazení
  - Příklady orchestrací více agentů se specializovanými modely SLM
  - Vzory nasazení ve firmách s řízením zdrojů a monitorováním
  - Bezpečnostní a dodržovací prvky pro edge agentní systémy
  - Skutečné příklady implementací (maloobchod, zdravotnictví, zákaznický servis)

- **Strategie nasazení produkčních SLM agentů**:
  - **Foundry Local**: Kompletní dokumentace podnikové třídy edge AI runtime s instalací, konfigurací a produkčními vzory
  - **Ollama**: Vylepšené komunitní nasazení s komplexním monitorováním a správou modelů
  - **VLLM**: Vysoce výkonný inference engine s pokročilými optimalizačními technikami a podnikových funkcemi
  - Kontrolní seznamy a tabulky porovnání pro produkční nasazení na všech třech platformách

- **Vylepšení edge-optimalizovaných rámců SLM**:
  - **ONNX Runtime**: Nová komplexní sekce pro multiplatformní nasazení agentů SLM
  - Univerzální vzory nasazení na Windows, Linux, macOS, iOS a Android
  - Možnosti hardwarové akcelerace (CPU, GPU, NPU) s automatickou detekcí
  - Funkce připravené do produkce a optimalizace specifické pro agenty
  - Kompletní příklady implementace s integrací Microsoft Agent Framework

- **Reference a další čtení**:
  - Komplexní knihovna zdrojů s více než 100 autoritativními zdroji
  - Klíčové výzkumné články o AI agentech a modelech Small Language Models
  - Oficiální dokumentace všech hlavních rámců a nástrojů
  - Průmyslové zprávy, analýza trhu a technické benchmarky
  - Vzdělávací zdroje, konference a komunitní fóra
  - Standardy, specifikace a rámce dodržování předpisů

### Změněno - Modernizace obsahu modulu06
- **Vylepšené vzdělávací cíle**: Přidáno zvládnutí Microsoft Agent Framework a schopnosti edge nasazení
- **Zaměření na produkci**: Přechod od konceptu k praktickému průvodci s produkčními příklady
- **Příklady kódu**: Aktualizovány všechny příklady pro použití moderních vzorů SDK a osvědčených postupů
- **Architektonické vzory**: Přidány hierarchické architektury agentů a koordinace edge-to-cloud
- **Optimalizace výkonu**: Vylepšena s řízením zdrojů a doporučeními pro automatické škálování

### Dokumentace - Vylepšení struktury modulu06
- **Komplexní pokrytí Agent Frameworku**: Od základních konceptů po podnikové nasazení
- **Strategie produkčního nasazení**: Kompletní průvodce pro Foundry Local, Ollama a VLLM
- **Optimalizace multiplatformního prostředí**: Přidán ONNX Runtime pro univerzální nasazení
- **Knihovna zdrojů**: Rozsáhlé reference pro další vzdělávání a implementaci

### Přidáno - Aktualizace dokumentace Model Context Protocol (MCP) v modulu06
- **Modernizace úvodu MCP** (`Module06/03.IntroduceMCP.md`):
  - Aktualizováno dle nejnovějších specifikací MCP z modelcontextprotocol.io (verze 2025-06-18)
  - Přidána oficiální analogie USB-C pro standardizovaná AI připojení aplikací
  - Aktualizována část architektury s oficiálním dvouvrstvým návrhem (Datová vrstva + Transportní vrstva)
  - Vylepšená dokumentace základních primitiv se serverovými (Nástroje, Zdroje, Výzvy) a klientskými primitivy (Vzorkování, Elicita, Logování)

- **Komplexní reference a zdroje MCP**:
  - Přidán odkaz **MCP for Beginners** (https://aka.ms/mcp-for-beginners) 
  - Oficiální dokumentace a specifikace MCP (modelcontextprotocol.io)
  - Vývojové zdroje včetně MCP Inspector a referenčních implementací
  - Technické standardy (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Přidáno - Integrace Qualcomm QNN v modulu04
- **Nová sekce 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Rozsáhlý průvodce o více než 400 řádcích pokrývající sjednocený AI inference framework Qualcomm
  - Detailní pokrytí heterogenního výpočtu (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardwarově uvědomělá optimalizace pro platformy Snapdragon s inteligentním rozdělením zátěže
  - Pokročilé techniky kvantizace (INT8, INT16, smíšená přesnost) pro mobilní nasazení
  - Optimalizace inference úsporné na energii pro bateriová zařízení a reálné aplikace
  - Kompletní instalační průvodce s nastavením QNN SDK a konfigurací prostředí
  - Praktické příklady: konverze PyTorch na QNN, vícenásobná optimalizace backendů, generování kontextového binárního souboru
  - Pokročilé vzory použití: vlastní konfigurace backendu, dynamická kvantizace, profilování výkonu
  - Komplexní sekce řešení problémů a komunitní zdroje

- **Vylepšení struktury modulu04**:
  - Aktualizován README.md, nyní 7 pokročilých sekcí (předtím 6)
  - Přidán Qualcomm QNN do tabulky benchmarků výkonu (5-15x zrychlení, 50-80% snížení paměti)
  - Komplexní výstupy učení pro mobilní AI nasazení a optimalizaci energie

### Změněno - Aktualizace dokumentace v modulu04
- **Vylepšení dokumentace Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Přidána rozsáhlá sekce "Olive Recipes Repository" pokrývající 100+ předpřipravených optimalizačních receptů
  - Podrobné pokrytí podporovaných rodin modelů (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktické příklady pro přizpůsobení receptů a příspěvky komunity
  - Doplněno o benchmarky výkonu a návod na integraci

- **Přesun sekcí v modulu04**:
  - Apple MLX přesunut do sekce 5 (předtím sekce 6)
  - Workflow Synthesis přesunut do sekce 6 (předtím sekce 7)  
  - Qualcomm QNN zařazen jako sekce 7 (specializace zaměřená na mobilní/edge)
  - Všechny odkazy na soubory a navigace aktualizovány odpovídajícím způsobem

### Opraveno - Validace ukázky Workshopu
- **Validace a oprava chat_bootstrap.py**:
  - Opraven poškozený import (`util.util.workshop_utils` → `util.workshop_utils`)
  - Vytvořen chybějící `__init__.py` v balíčku util pro správné rozpoznání Python modulu
  - Nainstalovány požadované závislosti (openai, foundry-local-sdk) v conda prostředí
  - Úspěšná validace provedení ukázek s výchozími i vlastními výzvami
  - Potvrzena integrace se službou Foundry Local a načítání modelů (phi-4-mini s CUDA optimalizací)

### Dokumentace - Komplexní aktualizace průvodce
- **Kompletní restrukturalizace README.md modulu04**:
  - Přidán Qualcomm QNN jako hlavní optimalizační rámec vedle OpenVINO, Olive, MLX
  - Aktualizovány výukové výstupy kapitol s přidáním mobilního AI nasazení a optimalizace energie
  - Vylepšena tabulka porovnání výkonu s metrikami QNN a případy použití pro mobilní/edge
  - Zachována logická posloupnost od podnikových řešení po platformově specifické optimalizace

- **Křížové odkazy a navigace**:
  - Aktualizovány všechny interní odkazy a reference souborů na nové číslování sekcí
  - Rozšířen popis workflow synthesis o mobilní, desktopová a cloudová prostředí
  - Přidány komplexní odkazy na zdroje vývojářského ekosystému Qualcomm

## 2025-10-08

### Přidáno - Rozsáhlá aktualizace Workshopu
- **Kompletní přepis README.md Workshopu**:
  - Přidán rozsáhlý úvod vysvětlující hodnotu Edge AI (soukromí, výkon, náklady)
  - Vytvořeno 6 základních vzdělávacích cílů s podrobnými kompetencemi
  - Přidána tabulka výstupů učení s výstupy a maticí kompetencí
  - Zahrnuta sekce dovedností připravených pro kariéru a relevantnost v průmyslu
  - Přidán průvodce rychlým startem s předpoklady a nastavením ve 3 krocích
  - Vytvořeny tabulky zdrojů pro Python ukázky (8 souborů s časy spuštění)
  - Přidána tabulka Jupyter poznámkových bloků (8 notebooků s hodnocením obtížnosti)
  - Vytvořena tabulka dokumentace (7 klíčových dokumentů s doporučením "Použijte, kdy")
  - Přidána doporučení studijních cest pro různé úrovně dovedností

- **Infrastruktura validace a testování Workshopu**:
  - Vytvořen `scripts/validate_samples.py` - Komplexní validační nástroj pro syntaxi, importy a osvědčené postupy
  - Vytvořen `scripts/test_samples.py` - Test spouštění smoke testů pro všechny Python ukázky
  - Přidána dokumentace validace do `scripts/README.md`

- **Komplexní dokumentace**:
  - Vytvořen `SAMPLES_UPDATE_SUMMARY.md` - Detailní průvodce přes 400 řádků pokrývající všechna vylepšení
  - Vytvořen `UPDATE_COMPLETE.md` - Výkonný souhrn dokončení aktualizace
  - Vytvořen `QUICK_REFERENCE.md` - Rychlý referenční list pro Workshop

### Změněno - Modernizace Python ukázek Workshopu
- **Všechny 8 Python ukázek aktualizovány s nejlepšími postupy**:
  - Vylepšeno zacházení s chybami pomocí bloků try-except kolem všech I/O operací
  - Přidány typové anotace a komplexní docstringy
  - Implementován konzistentní zápis [INFO]/[ERROR]/[RESULT]
  - Ochrana volitelných importů s nápovědou k instalaci
  - Zlepšená zpětná vazba uživatelům ve všech ukázkách

- **session01/chat_bootstrap.py**:
  - Vylepšena inicializace klienta s komplexními zprávami o chybách
  - Vylepšena správa chyb při streamování s validací chunků
  - Přidáno lepší zacházení s výjimkami při nedostupnosti služby

- **session02/rag_pipeline.py**:
  - Přidány ochrany importů sentence-transformers s nápovědou k instalaci
  - Vylepšeno zacházení s chybami při embedování a generování
  - Vylepšeno formátování výstupu s strukturovanými výsledky

- **session02/rag_eval_ragas.py**:
  - Ochrana volitelných importů (ragas, datasets) s přívětivými zprávami o chybách
  - Přidáno zacházení s chybami u evaluačních metrik
  - Vylepšeno formátování výstupu evaluačních výsledků

- **session03/benchmark_oss_models.py**:
  - Implementováno elegantní degradační chování (pokračuje při selhání modelů)
  - Přidáno detailní hlášení postupu a zacházení s chybami per model
  - Vylepšeno počítání statistik s komplexním zotavením po chybách

- **session04/model_compare.py**:
  - Přidány typové anotace (návratové typy Tuple)
  - Vylepšeno formátování výstupu se strukturovanými JSON výsledky
  - Implementováno zacházení s chybami per model s možností zotavení

- **session05/agents_orchestrator.py**:
  - Vylepšená metoda Agent.act() s komplexní dokumentací
  - Přidáno zacházení s chybami pipeline se logováním po jednotlivých fázích
  - Vylepšeno řízení paměti a sledování stavů

- **session06/models_router.py**:
  - Vylepšena dokumentace funkcí u všech směrovacích komponent
  - Přidáno detailní protokolování ve funkci route()
  - Vylepšený testovací výstup se strukturovanými výsledky

- **session06/models_pipeline.py**:
  - Přidáno zacházení s chybami do pomocné funkce chat()
  - Vylepšena pipeline() se záznamy o fázích a hlášením postupu
  - Vylepšena hlavní funkce main() s komplexním zotavením po chybách

### Dokumentace - Vylepšení dokumentace Workshopu
- Aktualizován hlavní README.md s sekcí Workshopu zdůrazňující praktickou vzdělávací cestu
- Rozšířen STUDY_GUIDE.md o komplexní sekci Workshopu zahrnující:
  - Výukové cíle a zaměření studia
  - Otázky pro sebehodnocení
  - Praktická cvičení s odhady časové náročnosti
  - Rozvržení času pro intenzivní a částečné studium
  - Přidán Workshop do šablony sledování pokroku
- Aktualizován průvodce časovým rozvržením z 20 hodin na 30 hodin (včetně Workshopu)
- Přidány popisy ukázek Workshopu a výstupy učení do README

### Opraveno
- Vyřešeny nekonzistentní vzory zacházení s chybami napříč ukázkami Workshopu
- Opraveny chyby importu volitelných závislostí s odpovídající ochranou
- Doplněny chybějící typové anotace v klíčových funkcích
- Vyřešena nedostatečná zpětná vazba uživateli v chybových scénářích
- Opraveny problémy s validací pomocí komplexní testovací infrastruktury

---

## 2025-09-23

### Změněno - Hlavní modernizace modulu 08
- **Komplexní sladění s Microsoft Foundry-Local repozitářovými vzory**
  - Aktualizovány všechny příklady kódu pro použití moderní integrace `FoundryLocalManager` a OpenAI SDK
  - Nahrazeny zastaralé manuální volání `requests` správným použitím SDK
  - Sladění implementačních vzorů s oficiální dokumentací a ukázkami Microsoft

- **Modernizace 05.AIPoweredAgents.md**:
  - Aktualizována orchestrace více agentů pro použití moderních SDK vzorů
  - Vylepšena implementace koordinátora s pokročilými funkcemi (zpětná vazba, monitorování výkonu)
  - Přidáno komplexní zacházení s chybami a kontrola stavu služby
  - Integrované relevantní odkazy na lokální ukázky (`samples/05/multi_agent_orchestration.ipynb`)
  - Aktualizovány příklady volání funkcí s použitím moderního parametru `tools` místo zastaralého `functions`
  - Přidány produkční vzory se sledováním a statistikami monitorování

- **Kompletní přepis 06.ModelsAsTools.md**:
  - Nahrazen základní registr nástrojů inteligentní implementací routeru modelů
  - Přidán výběr modelů na základě klíčových slov pro různé typy úkolů (obecné, uvažování, kód, kreativní)
  - Integrovaná konfigurace založená na prostředí s flexibilním přiřazováním modelů
  - Vylepšeno o komplexní monitorování stavu služby a zacházení s chybami
  - Přidány produkční vzory s monitorováním požadavků a výkonu
  - Sladění s lokální implementací v `samples/06/router.py` a `samples/06/model_router.ipynb`

- **Vylepšení struktury dokumentace**:
  - Přidány přehledové sekce zdůrazňující modernizaci a sladění s SDK
  - Vylepšeno pomocí emoji a lepšího formátování pro lepší čitelnost
  - Přidány správné odkazy na lokální ukázkové soubory v celé dokumentaci
  - Zařazeno vedení k produkční implementaci a osvědčené postupy

### Přidáno
- Rozsáhlé přehledové sekce v souborech modulu 08 zdůrazňující moderní integraci SDK
- Architektonická vyzdvihnutí prezentující pokročilé funkce (systémy více agentů, inteligentní směrování)
- Přímé odkazy na lokální vzory implementací pro praktické zkušenosti
- Pokyny pro produkční nasazení s monitorováním a vzory zacházení s chybami
- Interaktivní Jupyter notebook příklady s pokročilými funkcemi a benchmarky

### Opraveno
- Nesoulady mezi dokumentací a aktuálními ukázkovými implementacemi
- Zastaralé vzory použití SDK v celém modulu 08
- Chybějící odkazy na komplexní lokální knihovnu ukázek
- Nekonzistentní přístupy k implementaci napříč různými sekcemi

---

## 2025-09-18

### Přidáno
- Modul 08: Microsoft Foundry Local – Kompletní sada vývojářských nástrojů
  - Šest částí: nastavení, integrace Azure AI Foundry, modely open source, špičkové demo ukázky, agenti a modely jako nástroje
  - Spustitelné ukázky pod `Module08/samples/01`–`06` s příkazy pro Windows cmd
    - `01` Rychlý chat REST (`chat_quickstart.py`)

    - `02` Rychlý start SDK s podporou OpenAI/Foundry Local a Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam a test výkonu (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orchestrace více agentů (`python -m samples.05.agents.coordinator`)
    - `06` Router Models-as-Tools (`router.py`)
- Podpora Azure OpenAI v ukázce Session 2 SDK s konfigurací pomocí proměnných prostředí
- `.vscode/settings.json` nasměrován na `Module08/.venv` a zlepšení rozpoznání Python analýzy
- `.env` s náznakem `PYTHONPATH` pro povědomí VS Code/Pylance

### Změněno
- Výchozí model aktualizován na `phi-4-mini` napříč dokumentací a ukázkami v Module 08; odstraněny zbývající zmínky `phi-3.5` v Module 08
- Vylepšení Routeru (`Module08/samples/06/router.py`):
  - Objevování endpointů přes `foundry service status` s parsováním regexem
  - Kontrola stavu `/v1/models` při spuštění
  - Registry modelů konfigurované přes prostředí (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizace požadavků: `Module08/requirements.txt` nyní obsahuje `openai` (vedle `requests`, `chainlit`)
- Upřesněn návod u Chainlit příkladu a přidáno řešení problémů; řešení importů přes nastavení workspace

### Opraveno
- Vyřešené problémy s importy:
  - Router již nezávisí na neexistujícím modulu `utils`; funkce jsou vložené přímo
  - Koordinátor používá relativní import (`from .specialists import ...`) a je spouštěn přes cestu modulu
  - Konfigurace VS Code/Pylance k vyřešení importů `chainlit` a balíčků
- Opravená drobná chyba v `STUDY_GUIDE.md` a přidáno pokrytí pro Module 08

### Odstraněno
- Smazán nepoužitý `Module08/infra/obs.py` a odstraněn prázdný adresář `infra/`; vzory pro observabilitu zůstávají jako volitelné v dokumentaci

### Přesunuto
- Konsolidována demo Module 08 pod `Module08/samples` s adresáři podle čísla sezení
  - Přesunutá aplikace Chainlit do `samples/04`
  - Přesunuti agenti do `samples/05` a přidány soubory `__init__.py` pro rozpoznání balíčku

### Dokumentace
- Dokumentace session Module 08 a všechny README ukázek obohaceny o reference Microsoft Learn a ověřených dodavatelů
- `Module08/README.md` aktualizován o Přehled vzorků, konfiguraci routeru a tipy pro validaci
- Sekce Windows Foundry Local v `Module07/README.md` ověřena podle Learn dokumentace
- Aktualizován `STUDY_GUIDE.md`:
  - Přidán Module 08 do přehledu, plánů a sledování pokroku
  - Přidána podrobná sekce Reference (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historie (shrnutí)
- Architektura kurzu a moduly ustanoveny (Moduly 01–07)
- Iterativní modernizace obsahu, standardizace formátování a přidány případové studie
- Rozšířeno pokrytí optimalizačních rámců (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nevydáno / Poznámky (návrhy)
- Volitelné smoke testy pro každý příklad k ověření dostupnosti Foundry Local
- Revize překladů k sladění odkazů na modely (např. `phi-4-mini`) tam, kde vhodné
- Přidání minimální konfigurace pyright pokud týmy preferují přísnější pravidla pro celý workspace

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->