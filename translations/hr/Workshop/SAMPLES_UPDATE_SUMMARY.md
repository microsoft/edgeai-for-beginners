<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T23:28:37+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "hr"
}
-->
# Uzorci radionice - Sažetak ažuriranja Foundry Local SDK-a

## Pregled

Svi Python uzorci u direktoriju `Workshop/samples` ažurirani su kako bi slijedili najbolje prakse Foundry Local SDK-a i osigurali dosljednost u cijeloj radionici.

**Datum**: 8. listopada 2025.  
**Opseg**: 9 Python datoteka kroz 6 sesija radionice  
**Primarni fokus**: Rukovanje pogreškama, dokumentacija, obrasci SDK-a, korisničko iskustvo

---

## Ažurirane datoteke

### Sesija 01: Početak
- ✅ `chat_bootstrap.py` - Osnovni primjeri za chat i streaming

### Sesija 02: RAG rješenja
- ✅ `rag_pipeline.py` - Implementacija RAG-a s ugrađivanjem
- ✅ `rag_eval_ragas.py` - Evaluacija RAG-a s RAGAS metrikama

### Sesija 03: Open Source modeli
- ✅ `benchmark_oss_models.py` - Benchmarking više modela

### Sesija 04: Najnoviji modeli
- ✅ `model_compare.py` - Usporedba SLM-a i LLM-a

### Sesija 05: Agenti pokretani umjetnom inteligencijom
- ✅ `agents_orchestrator.py` - Koordinacija više agenata

### Sesija 06: Modeli kao alati
- ✅ `models_router.py` - Usmjeravanje modela na temelju namjere
- ✅ `models_pipeline.py` - Višekorak cjevovod s usmjeravanjem

### Pomoćna infrastruktura
- ✅ `workshop_utils.py` - Već slijedi najbolje prakse (nije potrebno mijenjati)

---

## Ključna poboljšanja

### 1. Poboljšano rukovanje pogreškama

**Prije:**
```python
manager, client, model_id = get_client(alias)
```

**Poslije:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Prednosti:**
- Elegantno rukovanje pogreškama s jasnim porukama
- Korisni savjeti za rješavanje problema
- Ispravni izlazni kodovi za skriptiranje

### 2. Bolje upravljanje uvozom

**Prije:**
```python
from sentence_transformers import SentenceTransformer
```

**Poslije:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Prednosti:**
- Jasne upute kada nedostaju ovisnosti
- Sprječavanje nejasnih pogrešaka pri uvozu
- Korisničke upute za instalaciju

### 3. Sveobuhvatna dokumentacija

**Dodano svim uzorcima:**
- Dokumentacija o varijablama okruženja u docstringovima
- Poveznice na SDK referencu
- Primjeri korištenja
- Detaljna dokumentacija funkcija/parametara
- Tipovi podataka za bolju podršku u IDE-u

**Primjer:**
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

### 4. Poboljšana povratna informacija korisnika

**Dodano informativno logiranje:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indikatori napretka:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturirani izlaz:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robusno testiranje performansi

**Poboljšanja u sesiji 03:**
- Rukovanje pogreškama po modelu (nastavlja se nakon neuspjeha)
- Detaljno izvještavanje o napretku
- Ispravno izvršavanje zagrijavanja
- Podrška za mjerenje latencije prvog tokena
- Jasno razdvajanje faza

### 6. Dosljedni tipovi podataka

**Dodano svugdje:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Prednosti:**
- Bolja automatska dopuna u IDE-u
- Rano otkrivanje pogrešaka
- Samodokumentirajući kod

### 7. Poboljšano usmjeravanje modela

**Poboljšanja u sesiji 06:**
- Sveobuhvatna dokumentacija o detekciji namjere
- Objašnjenje algoritma za odabir modela
- Detaljni zapisi o usmjeravanju
- Formatiranje testnog izlaza
- Oporavak od pogrešaka u grupnom testiranju

### 8. Orkestracija više agenata

**Poboljšanja u sesiji 05:**
- Izvještavanje o napretku po fazama
- Rukovanje pogreškama po agentu
- Jasna struktura cjevovoda
- Bolja dokumentacija o upravljanju memorijom

---

## Popis za provjeru testiranja

### Preduvjeti
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testirajte svaki uzorak

#### Sesija 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sesija 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sesija 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sesija 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sesija 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sesija 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Referenca varijabli okruženja

### Globalno (svi uzorci)
| Varijabla | Opis | Zadano |
|-----------|-------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Alias modela za korištenje | Razlikuje se po uzorku |
| `FOUNDRY_LOCAL_ENDPOINT` | Zamjenski krajnji servis | Automatski otkriven |
| `SHOW_USAGE` | Prikaz potrošnje tokena | `0` |
| `RETRY_ON_FAIL` | Omogućuje logiku ponovnog pokušaja | `1` |
| `RETRY_BACKOFF` | Početno kašnjenje ponovnog pokušaja | `1.0` |

### Specifično za uzorak
| Varijabla | Koristi | Opis |
|-----------|---------|------|
| `EMBED_MODEL` | Sesija 02 | Naziv modela za ugrađivanje |
| `RAG_QUESTION` | Sesija 02 | Testno pitanje za RAG |
| `BENCH_MODELS` | Sesija 03 | Modeli za benchmarking, odvojeni zarezom |
| `BENCH_ROUNDS` | Sesija 03 | Broj rundi benchmarkinga |
| `BENCH_PROMPT` | Sesija 03 | Testni prompt za benchmarking |
| `BENCH_STREAM` | Sesija 03 | Mjerenje latencije prvog tokena |
| `SLM_ALIAS` | Sesija 04 | Mali jezični model |
| `LLM_ALIAS` | Sesija 04 | Veliki jezični model |
| `COMPARE_PROMPT` | Sesija 04 | Testni prompt za usporedbu |
| `AGENT_MODEL_PRIMARY` | Sesija 05 | Primarni model agenta |
| `AGENT_MODEL_EDITOR` | Sesija 05 | Model agenta urednika |
| `AGENT_QUESTION` | Sesija 05 | Testno pitanje za agente |
| `PIPELINE_TASK` | Sesija 06 | Zadatak za cjevovod |

---

## Promjene koje prekidaju kompatibilnost

**Nema** - Sve promjene su unatrag kompatibilne.

Postojeći skripti će i dalje raditi. Nove značajke su:
- Opcionalne varijable okruženja
- Poboljšane poruke o pogreškama (ne prekidaju funkcionalnost)
- Dodatno logiranje (može se isključiti)
- Bolji tipovi podataka (bez utjecaja na vrijeme izvođenja)

---

## Implementirane najbolje prakse

### 1. Uvijek koristite Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Ispravan obrazac za rukovanje pogreškama
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informativno logiranje
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Tipovi podataka
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Sveobuhvatni docstringovi
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

### 6. Podrška za varijable okruženja
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Elegantno degradiranje
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

## Uobičajeni problemi i rješenja

### Problem: Pogreške pri uvozu
**Rješenje:** Instalirajte nedostajuće ovisnosti
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problem: Pogreške povezivanja
**Rješenje:** Provjerite radi li Foundry Local
```bash
foundry service status
foundry model run phi-4-mini
```

### Problem: Model nije pronađen
**Rješenje:** Provjerite dostupne modele
```bash
foundry model ls
foundry model download <alias>
```

### Problem: Sporo izvođenje
**Rješenje:** Koristite manje modele ili prilagodite parametre
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Sljedeći koraci

### 1. Testirajte sve uzorke
Prođite kroz popis za provjeru testiranja iznad kako biste provjerili rade li svi uzorci ispravno.

### 2. Ažurirajte dokumentaciju
- Ažurirajte markdown datoteke sesija s novim primjerima
- Dodajte odjeljak za rješavanje problema u glavni README
- Izradite vodič za brzu referencu

### 3. Izradite integracijske testove
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Dodajte testove performansi
Pratite poboljšanja performansi od poboljšanja rukovanja pogreškama.

### 5. Povratne informacije korisnika
Prikupite povratne informacije od sudionika radionice o:
- Jasnoći poruka o pogreškama
- Potpunosti dokumentacije
- Jednostavnosti korištenja

---

## Resursi

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Brza referenca**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Bilješke o migraciji**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Glavni repozitorij**: https://github.com/microsoft/Foundry-Local

---

## Održavanje

### Dodavanje novih uzoraka
Slijedite ove obrasce prilikom izrade novih uzoraka:

1. Koristite `workshop_utils` za upravljanje klijentima
2. Dodajte sveobuhvatno rukovanje pogreškama
3. Uključite podršku za varijable okruženja
4. Dodajte tipove podataka i docstringove
5. Osigurajte informativno logiranje
6. Uključite primjere korištenja u docstring
7. Povežite se na dokumentaciju SDK-a

### Pregled ažuriranja
Prilikom pregleda ažuriranja uzoraka, provjerite:
- [ ] Rukovanje pogreškama na svim I/O operacijama
- [ ] Tipovi podataka na javnim funkcijama
- [ ] Sveobuhvatni docstringovi
- [ ] Dokumentacija o varijablama okruženja
- [ ] Informativna povratna informacija korisnika
- [ ] Poveznice na SDK referencu
- [ ] Dosljedan stil koda

---

**Sažetak**: Svi Python uzorci radionice sada slijede najbolje prakse Foundry Local SDK-a s poboljšanim rukovanjem pogreškama, sveobuhvatnom dokumentacijom i poboljšanim korisničkim iskustvom. Nema promjena koje prekidaju kompatibilnost - sva postojeća funkcionalnost je očuvana i poboljšana.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.