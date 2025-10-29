<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T23:07:56+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "sk"
}
-->
# Ukážky workshopu - Zhrnutie aktualizácie Foundry Local SDK

## Prehľad

Všetky ukážky v Pythone v adresári `Workshop/samples` boli aktualizované tak, aby dodržiavali najlepšie postupy Foundry Local SDK a zabezpečili konzistentnosť v rámci workshopu.

**Dátum**: 8. október 2025  
**Rozsah**: 9 súborov v Pythone v rámci 6 workshopových sekcií  
**Hlavné zameranie**: Spracovanie chýb, dokumentácia, vzory SDK, používateľská skúsenosť

---

## Aktualizované súbory

### Sekcia 01: Začíname
- ✅ `chat_bootstrap.py` - Základné ukážky chatu a streamovania

### Sekcia 02: RAG riešenia
- ✅ `rag_pipeline.py` - Implementácia RAG s embeddingami
- ✅ `rag_eval_ragas.py` - Hodnotenie RAG pomocou metrík RAGAS

### Sekcia 03: Open Source modely
- ✅ `benchmark_oss_models.py` - Porovnanie viacerých modelov

### Sekcia 04: Najmodernejšie modely
- ✅ `model_compare.py` - Porovnanie SLM a LLM

### Sekcia 05: Agenti poháňaní AI
- ✅ `agents_orchestrator.py` - Koordinácia viacerých agentov

### Sekcia 06: Modely ako nástroje
- ✅ `models_router.py` - Smerovanie modelov na základe zámeru
- ✅ `models_pipeline.py` - Viackroková smerovaná pipeline

### Podporná infraštruktúra
- ✅ `workshop_utils.py` - Už dodržiava najlepšie postupy (neboli potrebné žiadne zmeny)

---

## Kľúčové vylepšenia

### 1. Vylepšené spracovanie chýb

**Predtým:**
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
- Elegantné spracovanie chýb s jasnými chybovými hláseniami
- Praktické rady na riešenie problémov
- Správne výstupné kódy pre skriptovanie

### 2. Lepšie spravovanie importov

**Predtým:**
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
- Jasné pokyny pri chýbajúcich závislostiach
- Predchádzanie nejasným chybám pri importe
- Používateľsky prívetivé inštalačné pokyny

### 3. Komplexná dokumentácia

**Pridané do všetkých ukážok:**
- Dokumentácia environmentálnych premenných v docstringoch
- Odkazy na SDK dokumentáciu
- Príklady použitia
- Podrobná dokumentácia funkcií/parametrov
- Typové anotácie pre lepšiu podporu v IDE

**Príklad:**
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

### 4. Vylepšená spätná väzba používateľovi

**Pridané informatívne logovanie:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indikátory pokroku:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Štruktúrovaný výstup:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robustné porovnávanie výkonu

**Vylepšenia v sekcii 03:**
- Spracovanie chýb pre každý model (pokračuje po zlyhaní)
- Podrobné hlásenie pokroku
- Správne vykonanie zahrievacích kôl
- Podpora merania latencie prvého tokenu
- Jasné oddelenie fáz

### 6. Konzistentné typové anotácie

**Pridané všade:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Výhody:**
- Lepšie automatické dopĺňanie v IDE
- Včasná detekcia chýb
- Samodokumentujúci kód

### 7. Vylepšené smerovanie modelov

**Vylepšenia v sekcii 06:**
- Komplexná dokumentácia detekcie zámerov
- Vysvetlenie algoritmu výberu modelov
- Podrobné logy smerovania
- Formátovanie testovacích výstupov
- Obnova chýb pri hromadnom testovaní

### 8. Orchestrácia viacerých agentov

**Vylepšenia v sekcii 05:**
- Hlásenie pokroku po jednotlivých fázach
- Spracovanie chýb pre každého agenta
- Jasná štruktúra pipeline
- Lepšia dokumentácia správy pamäte

---

## Kontrolný zoznam testovania

### Predpoklady
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testovanie každej ukážky

#### Sekcia 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sekcia 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sekcia 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sekcia 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sekcia 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sekcia 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Referencia environmentálnych premenných

### Globálne (všetky ukážky)
| Premenná | Popis | Predvolená hodnota |
|----------|-------|--------------------|
| `FOUNDRY_LOCAL_ALIAS` | Alias modelu na použitie | Líši sa podľa ukážky |
| `FOUNDRY_LOCAL_ENDPOINT` | Prekrytie koncového bodu služby | Automaticky detekované |
| `SHOW_USAGE` | Zobraziť využitie tokenov | `0` |
| `RETRY_ON_FAIL` | Povoliť logiku opakovania | `1` |
| `RETRY_BACKOFF` | Počiatočné oneskorenie opakovania | `1.0` |

### Špecifické pre ukážky
| Premenná | Používa sa v | Popis |
|----------|-------------|-------|
| `EMBED_MODEL` | Sekcia 02 | Názov embedding modelu |
| `RAG_QUESTION` | Sekcia 02 | Testovacia otázka pre RAG |
| `BENCH_MODELS` | Sekcia 03 | Modely na porovnanie, oddelené čiarkou |
| `BENCH_ROUNDS` | Sekcia 03 | Počet kôl porovnania |
| `BENCH_PROMPT` | Sekcia 03 | Testovací prompt pre porovnania |
| `BENCH_STREAM` | Sekcia 03 | Meranie latencie prvého tokenu |
| `SLM_ALIAS` | Sekcia 04 | Malý jazykový model |
| `LLM_ALIAS` | Sekcia 04 | Veľký jazykový model |
| `COMPARE_PROMPT` | Sekcia 04 | Testovací prompt na porovnanie |
| `AGENT_MODEL_PRIMARY` | Sekcia 05 | Primárny model agenta |
| `AGENT_MODEL_EDITOR` | Sekcia 05 | Model agenta editoru |
| `AGENT_QUESTION` | Sekcia 05 | Testovacia otázka pre agentov |
| `PIPELINE_TASK` | Sekcia 06 | Úloha pre pipeline |

---

## Zmeny, ktoré môžu narušiť kompatibilitu

**Žiadne** - Všetky zmeny sú spätne kompatibilné.

Existujúce skripty budú naďalej fungovať. Nové funkcie sú:
- Voliteľné environmentálne premenné
- Vylepšené chybové hlásenia (neporušujú funkčnosť)
- Dodatočné logovanie (možno potlačiť)
- Lepšie typové anotácie (bez dopadu na runtime)

---

## Implementované najlepšie postupy

### 1. Vždy používať Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Správny vzor spracovania chýb
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informatívne logovanie
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Typové anotácie
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Komplexné docstringy
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

### 6. Podpora environmentálnych premenných
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Elegantná degradácia
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

## Bežné problémy a riešenia

### Problém: Chyby pri importe
**Riešenie:** Nainštalujte chýbajúce závislosti
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problém: Chyby pripojenia
**Riešenie:** Uistite sa, že Foundry Local beží
```bash
foundry service status
foundry model run phi-4-mini
```

### Problém: Model nebol nájdený
**Riešenie:** Skontrolujte dostupné modely
```bash
foundry model ls
foundry model download <alias>
```

### Problém: Pomalý výkon
**Riešenie:** Použite menšie modely alebo upravte parametre
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Ďalšie kroky

### 1. Otestovať všetky ukážky
Prejdite kontrolný zoznam testovania vyššie, aby ste overili správnosť všetkých ukážok.

### 2. Aktualizovať dokumentáciu
- Aktualizovať markdown súbory sekcií s novými príkladmi
- Pridať sekciu riešenia problémov do hlavného README
- Vytvoriť rýchlu referenčnú príručku

### 3. Vytvoriť integračné testy
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Pridať porovnania výkonu
Sledovať zlepšenia výkonu z vylepšeného spracovania chýb.

### 5. Spätná väzba od používateľov
Získať spätnú väzbu od účastníkov workshopu na:
- Jasnosť chybových hlásení
- Kompletnosť dokumentácie
- Jednoduchosť použitia

---

## Zdroje

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rýchla referencia**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Poznámky k migrácii**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Hlavné úložisko**: https://github.com/microsoft/Foundry-Local

---

## Údržba

### Pridávanie nových ukážok
Pri vytváraní nových ukážok dodržiavajte tieto vzory:

1. Používajte `workshop_utils` na správu klientov
2. Pridajte komplexné spracovanie chýb
3. Zahrňte podporu environmentálnych premenných
4. Pridajte typové anotácie a docstringy
5. Poskytnite informatívne logovanie
6. Zahrňte príklady použitia v docstringu
7. Odkazujte na dokumentáciu SDK

### Kontrola aktualizácií
Pri kontrole aktualizácií ukážok skontrolujte:
- [ ] Spracovanie chýb pri všetkých I/O operáciách
- [ ] Typové anotácie pri verejných funkciách
- [ ] Komplexné docstringy
- [ ] Dokumentáciu environmentálnych premenných
- [ ] Informatívnu spätnú väzbu používateľovi
- [ ] Odkazy na SDK dokumentáciu
- [ ] Konzistentný štýl kódu

---

**Zhrnutie**: Všetky ukážky v Pythone pre workshop teraz dodržiavajú najlepšie postupy Foundry Local SDK s vylepšeným spracovaním chýb, komplexnou dokumentáciou a zlepšenou používateľskou skúsenosťou. Žiadne zmeny, ktoré by narušili kompatibilitu - všetka existujúca funkcionalita je zachovaná a vylepšená.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.