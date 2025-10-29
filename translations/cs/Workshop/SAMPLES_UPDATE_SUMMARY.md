<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T23:03:24+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "cs"
}
-->
# Ukázky workshopu - Souhrn aktualizace Foundry Local SDK

## Přehled

Všechny ukázky v Pythonu v adresáři `Workshop/samples` byly aktualizovány, aby odpovídaly nejlepším postupům Foundry Local SDK a zajistily konzistenci napříč workshopem.

**Datum**: 8. října 2025  
**Rozsah**: 9 souborů v Pythonu napříč 6 workshopy  
**Hlavní zaměření**: Zpracování chyb, dokumentace, vzory SDK, uživatelská zkušenost

---

## Aktualizované soubory

### Workshop 01: Začínáme
- ✅ `chat_bootstrap.py` - Základní příklady chatu a streamování

### Workshop 02: RAG řešení
- ✅ `rag_pipeline.py` - Implementace RAG s embeddingy
- ✅ `rag_eval_ragas.py` - Hodnocení RAG pomocí metrik RAGAS

### Workshop 03: Open Source modely
- ✅ `benchmark_oss_models.py` - Benchmarking více modelů

### Workshop 04: Nejmodernější modely
- ✅ `model_compare.py` - Porovnání SLM vs LLM

### Workshop 05: Agenti pohánění AI
- ✅ `agents_orchestrator.py` - Koordinace více agentů

### Workshop 06: Modely jako nástroje
- ✅ `models_router.py` - Směrování modelů na základě záměru
- ✅ `models_pipeline.py` - Vícekroková směrovaná pipeline

### Podpůrná infrastruktura
- ✅ `workshop_utils.py` - Již odpovídá nejlepším postupům (nebyly potřeba žádné změny)

---

## Klíčová zlepšení

### 1. Vylepšené zpracování chyb

**Před:**
```python
manager, client, model_id = get_client(alias)
```

**Po:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Výhody:**
- Elegantní zpracování chyb s jasnými chybovými zprávami
- Praktické rady pro řešení problémů
- Správné výstupní kódy pro skriptování

### 2. Lepší správa importů

**Před:**
```python
from sentence_transformers import SentenceTransformer
```

**Po:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Výhody:**
- Jasné pokyny při chybějících závislostech
- Zamezení nejasným chybám při importu
- Uživatelsky přívětivé pokyny k instalaci

### 3. Komplexní dokumentace

**Přidáno do všech ukázek:**
- Dokumentace proměnných prostředí v docstringu
- Odkazy na SDK dokumentaci
- Příklady použití
- Podrobná dokumentace funkcí/parametrů
- Typové nápovědy pro lepší podporu v IDE

**Příklad:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Zlepšená zpětná vazba uživatele

**Přidáno informativní logování:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indikátory průběhu:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturovaný výstup:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robustní benchmarking

**Vylepšení workshopu 03:**
- Zpracování chyb pro každý model (pokračuje i při selhání)
- Podrobné hlášení průběhu
- Správné provedení zahřívacích kol
- Podpora měření latence prvního tokenu
- Jasné oddělení jednotlivých fází

### 6. Konzistentní typové nápovědy

**Přidáno všude:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Výhody:**
- Lepší automatické doplňování v IDE
- Včasná detekce chyb
- Samodokumentující kód

### 7. Vylepšený směrovač modelů

**Vylepšení workshopu 06:**
- Komplexní dokumentace detekce záměru
- Vysvětlení algoritmu výběru modelu
- Podrobné logy směrování
- Formátování výstupu testů
- Obnova chyb při batch testování

### 8. Orchestrace více agentů

**Vylepšení workshopu 05:**
- Hlášení průběhu po jednotlivých fázích
- Zpracování chyb pro každého agenta
- Jasná struktura pipeline
- Lepší dokumentace správy paměti

---

## Kontrolní seznam testování

### Předpoklady
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testování každé ukázky

#### Workshop 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Workshop 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Workshop 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Workshop 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Workshop 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Workshop 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Referenční proměnné prostředí

### Globální (všechny ukázky)
| Proměnná | Popis | Výchozí hodnota |
|----------|-------|-----------------|
| `FOUNDRY_LOCAL_ALIAS` | Alias modelu k použití | Liší se podle ukázky |
| `FOUNDRY_LOCAL_ENDPOINT` | Přepsání koncového bodu služby | Automaticky detekováno |
| `SHOW_USAGE` | Zobrazení využití tokenů | `0` |
| `RETRY_ON_FAIL` | Povolení logiky opakování | `1` |
| `RETRY_BACKOFF` | Počáteční zpoždění opakování | `1.0` |

### Specifické pro ukázky
| Proměnná | Používá | Popis |
|----------|---------|-------|
| `EMBED_MODEL` | Workshop 02 | Název embedding modelu |
| `RAG_QUESTION` | Workshop 02 | Testovací otázka pro RAG |
| `BENCH_MODELS` | Workshop 03 | Modely pro benchmarking, oddělené čárkou |
| `BENCH_ROUNDS` | Workshop 03 | Počet kol benchmarkingu |
| `BENCH_PROMPT` | Workshop 03 | Testovací prompt pro benchmarking |
| `BENCH_STREAM` | Workshop 03 | Měření latence prvního tokenu |
| `SLM_ALIAS` | Workshop 04 | Malý jazykový model |
| `LLM_ALIAS` | Workshop 04 | Velký jazykový model |
| `COMPARE_PROMPT` | Workshop 04 | Testovací prompt pro porovnání |
| `AGENT_MODEL_PRIMARY` | Workshop 05 | Primární model agenta |
| `AGENT_MODEL_EDITOR` | Workshop 05 | Model editoru agenta |
| `AGENT_QUESTION` | Workshop 05 | Testovací otázka pro agenty |
| `PIPELINE_TASK` | Workshop 06 | Úkol pro pipeline |

---

## Změny, které mohou ovlivnit kompatibilitu

**Žádné** - Všechny změny jsou zpětně kompatibilní.

Existující skripty budou nadále fungovat. Nové funkce zahrnují:
- Volitelné proměnné prostředí
- Vylepšené chybové zprávy (neovlivňují funkčnost)
- Další logování (lze potlačit)
- Lepší typové nápovědy (bez dopadu na runtime)

---

## Implementované nejlepší postupy

### 1. Vždy používejte Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Správný vzor zpracování chyb
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informativní logování
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Typové nápovědy
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Komplexní docstringy
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Podpora proměnných prostředí
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Elegantní degradace
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Běžné problémy a jejich řešení

### Problém: Chyby při importu
**Řešení:** Nainstalujte chybějící závislosti
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problém: Chyby připojení
**Řešení:** Ujistěte se, že Foundry Local běží
```bash
foundry service status
foundry model run phi-4-mini
```

### Problém: Model nebyl nalezen
**Řešení:** Zkontrolujte dostupné modely
```bash
foundry model ls
foundry model download <alias>
```

### Problém: Pomalý výkon
**Řešení:** Použijte menší modely nebo upravte parametry
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Další kroky

### 1. Otestujte všechny ukázky
Projděte kontrolní seznam testování výše a ověřte, že všechny ukázky fungují správně.

### 2. Aktualizujte dokumentaci
- Aktualizujte markdown soubory workshopů s novými příklady
- Přidejte sekci řešení problémů do hlavního README
- Vytvořte rychlého průvodce

### 3. Vytvořte integrační testy
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Přidejte benchmarky výkonu
Sledujte zlepšení výkonu díky vylepšenému zpracování chyb.

### 5. Zpětná vazba od uživatelů
Sbírejte zpětnou vazbu od účastníků workshopu na:
- Jasnost chybových zpráv
- Úplnost dokumentace
- Snadnost použití

---

## Zdroje

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rychlý průvodce**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Poznámky k migraci**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Hlavní repozitář**: https://github.com/microsoft/Foundry-Local

---

## Údržba

### Přidávání nových ukázek
Dodržujte tyto postupy při vytváření nových ukázek:

1. Používejte `workshop_utils` pro správu klientů
2. Přidejte komplexní zpracování chyb
3. Zahrňte podporu proměnných prostředí
4. Přidejte typové nápovědy a docstringy
5. Poskytněte informativní logování
6. Zahrňte příklady použití v docstringu
7. Odkazujte na dokumentaci SDK

### Kontrola aktualizací
Při kontrole aktualizací ukázek zkontrolujte:
- [ ] Zpracování chyb u všech operací I/O
- [ ] Typové nápovědy u veřejných funkcí
- [ ] Komplexní docstringy
- [ ] Dokumentaci proměnných prostředí
- [ ] Informativní zpětnou vazbu uživatele
- [ ] Odkazy na dokumentaci SDK
- [ ] Konzistentní styl kódu

---

**Shrnutí**: Všechny ukázky v Pythonu pro workshop nyní odpovídají nejlepším postupům Foundry Local SDK s vylepšeným zpracováním chyb, komplexní dokumentací a zlepšenou uživatelskou zkušeností. Žádné změny neovlivňující kompatibilitu - veškerá stávající funkčnost byla zachována a vylepšena.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.