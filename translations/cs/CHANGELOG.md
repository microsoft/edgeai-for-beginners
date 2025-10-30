<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T14:11:41+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "cs"
}
-->
# Změny

Všechny významné změny v EdgeAI pro začátečníky jsou zde zdokumentovány. Tento projekt používá záznamy založené na datech a styl Keep a Changelog (Přidáno, Změněno, Opraveno, Odstraněno, Dokumentace, Přesunuto).

## 2025-10-30

### Přidáno - Modul06 Komplexní vylepšení AI agentů
- **Integrace Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Kompletní sekce o Microsoft Agent Framework pro vývoj agentů připravených na produkci
  - Podrobné vzory integrace s Foundry Local pro nasazení na okraji
  - Příklady orchestrace více agentů se specializovanými SLM modely
  - Vzory nasazení v podnikovém prostředí s řízením zdrojů a monitorováním
  - Funkce zabezpečení a souladu pro systémy agentů na okraji
  - Příklady reálného použití (maloobchod, zdravotnictví, zákaznický servis)

- **Strategie nasazení produkčních SLM agentů**:
  - **Foundry Local**: Kompletní dokumentace pro podnikové nasazení AI na okraji s instalací, konfigurací a vzory pro produkci
  - **Ollama**: Rozšířené nasazení zaměřené na komunitu s komplexním monitorováním a správou modelů
  - **VLLM**: Vysoce výkonný inferenční engine s pokročilými optimalizačními technikami a funkcemi pro podnikové prostředí
  - Kontrolní seznamy pro nasazení v produkci a srovnávací tabulky pro všechny tři platformy

- **Vylepšení rámců optimalizovaných pro SLM na okraji**:
  - **ONNX Runtime**: Nová komplexní sekce pro nasazení SLM agentů napříč platformami
  - Univerzální vzory nasazení na Windows, Linux, macOS, iOS a Android
  - Možnosti hardwarové akcelerace (CPU, GPU, NPU) s automatickou detekcí
  - Funkce připravené na produkci a optimalizace specifické pro agenty
  - Kompletní příklady implementace s integrací Microsoft Agent Framework

- **Reference a další čtení**:
  - Komplexní knihovna zdrojů s více než 100 autoritativními zdroji
  - Základní výzkumné práce o AI agentech a malých jazykových modelech
  - Oficiální dokumentace pro všechny hlavní rámce a nástroje
  - Průmyslové zprávy, analýzy trhu a technické benchmarky
  - Vzdělávací zdroje, konference a komunitní fóra
  - Standardy, specifikace a rámce souladu

### Změněno - Modernizace obsahu Modul06
- **Vylepšené vzdělávací cíle**: Přidána znalost Microsoft Agent Framework a schopnosti nasazení na okraji
- **Zaměření na produkci**: Posun od konceptuálního k implementačně připravenému vedení s příklady z produkce
- **Příklady kódu**: Aktualizovány všechny příklady na moderní vzory SDK a osvědčené postupy
- **Architektonické vzory**: Přidány hierarchické architektury agentů a koordinace mezi okrajem a cloudem
- **Optimalizace výkonu**: Vylepšeno o doporučení pro řízení zdrojů a automatické škálování

### Dokumentace - Vylepšení struktury Modul06
- **Komplexní pokrytí rámce agentů**: Od základních konceptů po nasazení v podnikovém prostředí
- **Strategie nasazení v produkci**: Kompletní průvodce pro Foundry Local, Ollama a VLLM
- **Optimalizace napříč platformami**: Přidán ONNX Runtime pro univerzální nasazení
- **Knihovna zdrojů**: Rozsáhlé reference pro další učení a implementaci

### Přidáno - Aktualizace dokumentace Model Context Protocol (MCP) v Modul06
- **Modernizace úvodu MCP** (`Module06/03.IntroduceMCP.md`):
  - Aktualizováno nejnovějšími specifikacemi MCP z modelcontextprotocol.io (verze 2025-06-18)
  - Přidána oficiální analogie USB-C pro standardizované připojení AI aplikací
  - Aktualizována sekce architektury s oficiálním dvouvrstvým designem (Datová vrstva + Transportní vrstva)
  - Vylepšena dokumentace základních primitiv s primitivy serveru (Nástroje, Zdroje, Výzvy) a klienta (Vzorkování, Dotazování, Protokolování)

- **Komplexní reference a zdroje MCP**:
  - Přidán odkaz **MCP pro začátečníky** (https://aka.ms/mcp-for-beginners)
  - Oficiální dokumentace a specifikace MCP (modelcontextprotocol.io)
  - Vývojové zdroje včetně MCP Inspector a referenčních implementací
  - Technické standardy (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Přidáno - Modul04 Integrace Qualcomm QNN
- **Nová sekce 7: Qualcomm QNN Optimalizační sada** (`Module04/05.QualcommQNN.md`):
  - Komplexní průvodce o 400+ řádcích pokrývající jednotný rámec inference AI od Qualcommu
  - Podrobné pokrytí heterogenního výpočtu (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimalizace zaměřená na hardware pro platformy Snapdragon s inteligentním rozdělením zátěže
  - Pokročilé techniky kvantizace (INT8, INT16, smíšená přesnost) pro mobilní nasazení
  - Optimalizace inference s nízkou spotřebou energie pro zařízení na baterii a aplikace v reálném čase
  - Kompletní průvodce instalací s nastavením QNN SDK a konfigurací prostředí
  - Praktické příklady: Konverze PyTorch na QNN, optimalizace více backendů, generování binárního kontextu
  - Pokročilé vzory použití: konfigurace vlastního backendu, dynamická kvantizace, profilování výkonu
  - Komplexní sekce pro řešení problémů a komunitní zdroje

- **Vylepšená struktura Modul04**:
  - Aktualizován README.md na 7 progresivních sekcí (bylo 6)
  - Přidán Qualcomm QNN do tabulky benchmarků výkonu (zlepšení rychlosti 5-15x, snížení paměti o 50-80 %)
  - Komplexní vzdělávací cíle pro mobilní nasazení AI a optimalizaci spotřeby energie

### Změněno - Aktualizace dokumentace Modul04
- **Vylepšení dokumentace Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Přidána komplexní sekce "Olive Recipes Repository" pokrývající více než 100 předpřipravených optimalizačních receptů
  - Podrobné pokrytí podporovaných rodin modelů (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktické příklady použití pro přizpůsobení receptů a příspěvky komunity
  - Vylepšeno o benchmarky výkonu a pokyny pro integraci

- **Přeuspořádání sekcí v Modul04**:
  - Apple MLX přesunuto na sekci 5 (bylo sekce 6)
  - Workflow Synthesis přesunuto na sekci 6 (bylo sekce 7)
  - Qualcomm QNN umístěno jako sekce 7 (specializované zaměření na mobilní/okrajové nasazení)
  - Aktualizovány všechny odkazy na soubory a navigační odkazy

### Opraveno - Validace vzorků workshopu
- **Oprava a validace chat_bootstrap.py**:
  - Opraven poškozený import (`util.util.workshop_utils` → `util.workshop_utils`)
  - Vytvořen chybějící `__init__.py` v balíčku util pro správné rozpoznání Python modulů
  - Nainstalovány požadované závislosti (openai, foundry-local-sdk) v conda prostředí
  - Úspěšně ověřeno spuštění vzorku s výchozími i vlastními výzvami
  - Potvrzena integrace se službou Foundry Local a načítání modelu (phi-4-mini s CUDA optimalizací)

### Dokumentace - Aktualizace komplexních průvodců
- **Kompletní restrukturalizace README.md Modul04**:
  - Přidán Qualcomm QNN jako hlavní optimalizační rámec vedle OpenVINO, Olive, MLX
  - Aktualizovány výsledky kapitol, aby zahrnovaly mobilní nasazení AI a optimalizaci spotřeby energie
  - Vylepšena tabulka srovnání výkonu s metrikami QNN a případy použití na mobilních/okrajových zařízeních
  - Zachována logická posloupnost od podnikových řešení po optimalizace specifické pro platformy

- **Křížové odkazy a navigace**:
  - Aktualizovány všechny interní odkazy a reference na soubory pro nové číslování sekcí
  - Vylepšen popis Workflow Synthesis, aby zahrnoval mobilní, desktopové a cloudové prostředí
  - Přidány komplexní odkazy na zdroje pro ekosystém Qualcomm vývojářů

## 2025-10-08

### Přidáno - Komplexní aktualizace workshopu
- **Kompletní přepis README.md workshopu**:
  - Přidán komplexní úvod vysvětlující hodnotu Edge AI (soukromí, výkon, náklady)
  - Vytvořeno 6 hlavních vzdělávacích cílů s podrobnými kompetencemi
  - Přidána tabulka výsledků učení s výstupy a maticí kompetencí
  - Zahrnuta sekce dovedností připravených na kariéru pro průmyslovou relevanci
  - Přidán rychlý průvodce s předpoklady a 3-krokovým nastavením
  - Vytvořeny tabulky zdrojů pro Python vzorky (8 souborů s dobou běhu)
  - Přidána tabulka Jupyter notebooků (8 notebooků s hodnocením obtížnosti)
  - Vytvořena tabulka dokumentace (7 klíčových dokumentů s doporučením "Použít kdy")
  - Přidána doporučení pro vzdělávací cestu pro různé úrovně dovedností

- **Validace a testovací infrastruktura workshopu**:
  - Vytvořen `scripts/validate_samples.py` - Komplexní nástroj pro validaci syntaxe, importů a osvědčených postupů
  - Vytvořen `scripts/test_samples.py` - Nástroj pro rychlé testování všech Python vzorků
  - Přidána dokumentace validace do `scripts/README.md`

- **Komplexní dokumentace**:
  - Vytvořen `SAMPLES_UPDATE_SUMMARY.md` - Podrobný průvodce o 400+ řádcích pokrývající všechny vylepšení
  - Vytvořen `UPDATE_COMPLETE.md` - Výkonný souhrn dokončení aktualizace
  - Vytvořen `QUICK_REFERENCE.md` - Rychlá referenční karta pro workshop

### Změněno - Modernizace Python vzorků workshopu
- **Vylepšení všech 8 Python vzorků osvědčenými postupy**:
  - Vylepšeno zpracování chyb pomocí bloků try-except kolem všech I/O operací
  - Přidány typové náznaky a komplexní docstringy
  - Implementován konzistentní vzor logování [INFO]/[ERROR]/[RESULT]
  - Ochráněny volitelné importy s náznaky instalace
  - Zlepšena zpětná vazba uživatele ve všech vzorcích

- **session01/chat_bootstrap.py**:
  - Vylepšena inicializace klienta s komplexními chybovými zprávami
  - Zlepšeno zpracování chyb při streamování s validací bloků
  - Přidáno lepší zpracování výjimek pro nedostupnost služby

- **session02/rag_pipeline.py**:
  - Přidány ochranné importy pro sentence-transformers s náznaky instalace
  - Vylepšeno zpracování chyb pro operace embeddingu a generování
  - Zlepšeno formátování výstupu se strukturovanými výsledky

- **session02/rag_eval_ragas.py**:
  - Ochráněny volitelné importy (ragas, datasets) s uživatelsky přívětivými chybovými zprávami
  - Přidáno zpracování chyb pro metriky hodnocení
  - Zlepšeno formátování výstupu pro výsledky hodnocení

- **session03/benchmark_oss_models.py**:
  - Implementováno elegantní degradování (pokračuje při selhání modelů)
  - Přidáno podrobné hlášení průběhu a zpracování chyb pro jednotlivé modely
  - Vylepšeno výpočty statistik s komplexním zotavením z chyb

- **session04/model_compare.py**:
  - Přidány typové náznaky (návratové typy Tuple)
  - Zlepšeno formátování výstupu se strukturovanými JSON výsledky
  - Implementováno zpracování chyb pro jednotlivé modely se zotavením

- **session05/agents_orchestrator.py**:
  - Vylepšeno Agent.act() s komplexními docstringy
  - Přidáno zpracování chyb pipeline s logováním po jednotlivých fázích
  - Zlepšeno řízení paměti a sledování stavu

- **session06/models_router.py**:
  - Vylepšena dokumentace funkcí pro všechny komponenty směrování
  - Přidáno podrobné logování ve funkci route()
  - Zlepšeno testování výstupu se strukturovanými výsledky

- **session06/models_pipeline.py**:
  - Přidáno zpracování chyb do pomocné funkce chat()
  - Vylepšeno pipeline() s logováním fází a hlášením průběhu
  - Zlepšeno main() s komplexním zotavením z chyb

### Dokumentace - Vylepšení dokumentace workshopu
- Aktualizován hlavní README.md s sekcí workshopu zdůrazňující praktickou vzdělávací cestu
- Vylepšen STUDY_GUIDE.md s komplexní sekcí workshopu včetně:
  - Vzdělávací cíle a oblasti zaměření studia
  - Otázky pro sebehodnocení
  - Praktická cvičení s odhady času
  - Časové rozvržení pro intenzivní a částečné studium
  - Přidán workshop do šablony sledování pokroku
- Aktualizován průvodce časovým rozvržením z 20 hodin na 30 hodin (včetně workshopu)
- Přidány popisy vzorků workshopu a výsledky učení do README

### Opraveno
- Vyřešeny nekonzistentní vzory zpracování chyb napříč vzorky workshopu
- Opraveny chyby volitelných importů s správnými ochrannými mechanismy
- Opraveny chybějící typové náznaky v kritických funkcích
- Řešena nedostatečná zpětná vazba uživatele v chybových scénářích
- Opraveny problémy s validací pomocí komplexní testovací infrastruktury

---

## 2025-09-23

### Změněno - Hlavní modernizace Modul 08
- **Komplexní sladění s vzory úložiště Microsoft Foundry-Local**
  - Aktualizovány všechny příklady kódu na moderní integraci `FoundryLocalManager` a OpenAI SDK
  - Nahrazeny zastaralé manuální volání `requests` správným použitím SDK
  - Sladěny vzory implementace s oficiální dokumentací a vzorky Microsoftu

- **Modernizace 05.AIPoweredAgents.md**:
  - Aktualizována orchestrace více agentů na moderní vzory SDK
  - Vylepšena implementace koordinátoru s pokročilými funkcemi (zpětné vazby, monitorování výkonu)
  - Přidáno komplexní zpracování chyb a kontrola zdraví služby
  - Integrované správné reference na místní vzorky (`samples/05/multi_agent_orchestration.ipynb`)
  - Aktualizovány příklady volání funkcí na moderní parametr `tools` místo zastaralého `functions`
  - Př
  - Spustitelné ukázky v `Module08/samples/01`–`06` s instrukcemi pro Windows cmd
    - `01` REST rychlý chat (`chat_quickstart.py`)
    - `02` SDK rychlý start s podporou OpenAI/Foundry Local a Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam a testování (`list_and_bench.cmd`)
    - `04` Ukázka Chainlit (`app.py`)
    - `05` Orchestrace více agentů (`python -m samples.05.agents.coordinator`)
    - `06` Router Models-as-Tools (`router.py`)
- Podpora Azure OpenAI v ukázce SDK Session 2 s konfigurací proměnných prostředí
- `.vscode/settings.json` nastaveno na `Module08/.venv` pro zlepšení analýzy Pythonu
- `.env` s nápovědou `PYTHONPATH` pro povědomí VS Code/Pylance

### Změněno
- Výchozí model aktualizován na `phi-4-mini` napříč dokumentací a ukázkami Module 08; odstraněny zbývající zmínky o `phi-3.5` v Module 08
- Vylepšení routeru (`Module08/samples/06/router.py`):
  - Zjišťování endpointů pomocí `foundry service status` s parsováním regexu
  - Kontrola zdraví `/v1/models` při spuštění
  - Konfigurovatelný registr modelů prostředím (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizovány požadavky: `Module08/requirements.txt` nyní zahrnuje `openai` (spolu s `requests`, `chainlit`)
- Zpřesněny pokyny k ukázce Chainlit a přidáno řešení problémů; vyřešení importů pomocí nastavení pracovního prostoru

### Opraveno
- Vyřešeny problémy s importem:
  - Router již nezávisí na neexistujícím modulu `utils`; funkce jsou vloženy přímo
  - Koordinátor používá relativní import (`from .specialists import ...`) a je spuštěn přes cestu modulu
  - Konfigurace VS Code/Pylance pro vyřešení importů `chainlit` a balíčků
- Opraven drobný překlep v `STUDY_GUIDE.md` a přidáno pokrytí Module 08

### Odstraněno
- Smazán nepoužívaný `Module08/infra/obs.py` a odstraněn prázdný adresář `infra/`; vzory pro observabilitu zachovány jako volitelné v dokumentaci

### Přesunuto
- Konsolidovány ukázky Module 08 pod `Module08/samples` s adresáři očíslovanými podle relací
  - Chainlit aplikace přesunuta do `samples/04`
  - Agenti přesunuti do `samples/05` a přidány soubory `__init__.py` pro vyřešení balíčků

### Dokumentace
- Dokumentace relací Module 08 a všechny README ukázky obohaceny o odkazy na Microsoft Learn a důvěryhodné dodavatele
- `Module08/README.md` aktualizováno s přehledem ukázek, konfigurací routeru a tipy pro validaci
- `Module07/README.md` sekce Windows Foundry Local ověřena proti dokumentaci Learn
- `STUDY_GUIDE.md` aktualizováno:
  - Přidán Module 08 do přehledu, rozvrhů, sledovače pokroku
  - Přidána komplexní sekce Referencí (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historické (shrnutí)
- Založena architektura kurzu a moduly (Moduly 01–07)
- Iterativní modernizace obsahu, standardizace formátování a přidání případových studií
- Rozšířené pokrytí optimalizačních rámců (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nevydáno / Zásobník (návrhy)
- Volitelné testy pro každou ukázku k ověření dostupnosti Foundry Local
- Revize překladů pro sladění odkazů na modely (např. `phi-4-mini`) tam, kde je to vhodné
- Přidání minimální konfigurace pyright, pokud týmy preferují přísnost na úrovni pracovního prostoru

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.