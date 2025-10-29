<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-29T00:01:21+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "et"
}
-->
# Töötuba Näidised - Foundry Local SDK värskenduste kokkuvõte

## Ülevaade

Kõik Python näidised kataloogis `Workshop/samples` on uuendatud, et järgida Foundry Local SDK parimaid tavasid ja tagada järjepidevus kogu töötoas.

**Kuupäev**: 8. oktoober 2025  
**Ulatus**: 9 Python faili 6 töötoa sessioonis  
**Peamine fookus**: Vigade käsitlemine, dokumentatsioon, SDK mustrid, kasutajakogemus

---

## Uuendatud failid

### Sessioon 01: Alustamine
- ✅ `chat_bootstrap.py` - Põhilised vestluse ja voogesituse näited

### Sessioon 02: RAG lahendused
- ✅ `rag_pipeline.py` - RAG rakendamine koos sisseehitustega
- ✅ `rag_eval_ragas.py` - RAG hindamine RAGAS mõõdikutega

### Sessioon 03: Avatud lähtekoodiga mudelid
- ✅ `benchmark_oss_models.py` - Mitme mudeli võrdlus

### Sessioon 04: Tipptasemel mudelid
- ✅ `model_compare.py` - SLM vs LLM võrdlus

### Sessioon 05: AI-põhised agendid
- ✅ `agents_orchestrator.py` - Mitme agendi koordineerimine

### Sessioon 06: Mudelid tööriistadena
- ✅ `models_router.py` - Kavatsusel põhinev mudelite suunamine
- ✅ `models_pipeline.py` - Mitmeastmeline suunatud torustik

### Tugistruktuur
- ✅ `workshop_utils.py` - Juba järgib parimaid tavasid (muudatusi ei tehtud)

---

## Peamised täiustused

### 1. Täiustatud vigade käsitlemine

**Enne:**
```python
manager, client, model_id = get_client(alias)
```

**Pärast:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Eelised:**
- Sujuv vigade käsitlemine selgete veateadetega
- Tegutsemiseks vajalikud vihjed
- Skriptide jaoks õiged väljumiskoodid

### 2. Parem impordi haldamine

**Enne:**
```python
from sentence_transformers import SentenceTransformer
```

**Pärast:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Eelised:**
- Selged juhised, kui sõltuvused puuduvad
- Välditakse segaseid impordivigu
- Kasutajasõbralikud paigaldusjuhised

### 3. Põhjalik dokumentatsioon

**Lisatud kõikidele näidistele:**
- Keskkonnamuutujate dokumentatsioon docstringides
- SDK viited
- Kasutusnäited
- Üksikasjalik funktsiooni/parameetri dokumentatsioon
- Tüübiviited parema IDE toe jaoks

**Näide:**
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

### 4. Parendatud kasutajate tagasiside

**Lisatud informatiivne logimine:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Edenemise indikaatorid:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Struktureeritud väljund:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Tugev võrdlus

**Sessioon 03 täiustused:**
- Mudelitepõhine vigade käsitlemine (jätkab ebaõnnestumise korral)
- Üksikasjalik edenemise aruandlus
- Soojendusringid korralikult teostatud
- Esimese märgi latentsuse mõõtmise tugi
- Etappide selge eristamine

### 6. Järjepidevad tüübiviited

**Lisatud kõikjal:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Eelised:**
- Parem IDE automaatne täitmine
- Varajane vigade tuvastamine
- Ise dokumenteeriv kood

### 7. Täiustatud mudelite suunaja

**Sessioon 06 täiustused:**
- Põhjalik kavatsuste tuvastamise dokumentatsioon
- Mudeli valiku algoritmi selgitus
- Üksikasjalikud suunamislogid
- Testi väljundi vormindamine
- Vigade taastamine partii testimisel

### 8. Mitme agendi orkestreerimine

**Sessioon 05 täiustused:**
- Etappide kaupa edenemise aruandlus
- Agendipõhine vigade käsitlemine
- Selge torustiku struktuur
- Parem mäluhalduse dokumentatsioon

---

## Testimise kontrollnimekiri

### Eeltingimused
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testi iga näidist

#### Sessioon 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sessioon 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sessioon 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sessioon 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sessioon 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sessioon 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Keskkonnamuutujate viited

### Üldine (kõik näidised)
| Muutuja | Kirjeldus | Vaikimisi |
|---------|-----------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Kasutatava mudeli alias | Olenevalt näidisest |
| `FOUNDRY_LOCAL_ENDPOINT` | Teenuse lõpp-punkti ülekirjutamine | Automaatne tuvastamine |
| `SHOW_USAGE` | Näita tokenite kasutust | `0` |
| `RETRY_ON_FAIL` | Luba uuesti proovimise loogika | `1` |
| `RETRY_BACKOFF` | Esialgne uuesti proovimise viivitus | `1.0` |

### Näidise-spetsiifiline
| Muutuja | Kasutaja | Kirjeldus |
|---------|----------|-----------|
| `EMBED_MODEL` | Sessioon 02 | Sisseehitatud mudeli nimi |
| `RAG_QUESTION` | Sessioon 02 | RAG-i testküsimus |
| `BENCH_MODELS` | Sessioon 03 | Võrdluseks kasutatavad mudelid (komaga eraldatud) |
| `BENCH_ROUNDS` | Sessioon 03 | Võrdlusringide arv |
| `BENCH_PROMPT` | Sessioon 03 | Testi küsimus võrdluseks |
| `BENCH_STREAM` | Sessioon 03 | Esimese märgi latentsuse mõõtmine |
| `SLM_ALIAS` | Sessioon 04 | Väike keelemudel |
| `LLM_ALIAS` | Sessioon 04 | Suur keelemudel |
| `COMPARE_PROMPT` | Sessioon 04 | Võrdluse testküsimus |
| `AGENT_MODEL_PRIMARY` | Sessioon 05 | Peamine agendi mudel |
| `AGENT_MODEL_EDITOR` | Sessioon 05 | Toimetaja agendi mudel |
| `AGENT_QUESTION` | Sessioon 05 | Testküsimus agentidele |
| `PIPELINE_TASK` | Sessioon 06 | Torustiku ülesanne |

---

## Muutused

**Puuduvad** - Kõik muudatused on tagasiühilduvad.

Olemasolevad skriptid töötavad endiselt. Uued funktsioonid on:
- Valikulised keskkonnamuutujad
- Täiustatud veateated (ei riku funktsionaalsust)
- Lisatud logimine (saab maha suruda)
- Paremad tüübiviited (ei mõjuta käitusaega)

---

## Rakendatud parimad tavad

### 1. Kasuta alati Workshop Utilsi
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Õige vigade käsitlemise muster
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informatiivne logimine
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Tüübiviited
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Põhjalikud docstringid
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

### 6. Keskkonnamuutujate tugi
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Sujuv degradeerumine
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

## Levinud probleemid ja lahendused

### Probleem: Impordivead
**Lahendus:** Paigalda puuduvad sõltuvused
```bash
pip install sentence-transformers ragas datasets numpy
```

### Probleem: Ühenduse vead
**Lahendus:** Veendu, et Foundry Local töötab
```bash
foundry service status
foundry model run phi-4-mini
```

### Probleem: Mudelit ei leitud
**Lahendus:** Kontrolli saadaolevaid mudeleid
```bash
foundry model ls
foundry model download <alias>
```

### Probleem: Aeglane jõudlus
**Lahendus:** Kasuta väiksemaid mudeleid või kohanda parameetreid
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Järgmised sammud

### 1. Testi kõiki näidiseid
Läbi ülaltoodud testimise kontrollnimekiri, et veenduda kõigi näidiste korrektses töös.

### 2. Uuenda dokumentatsiooni
- Uuenda sessiooni markdown-faile uute näidetega
- Lisa tõrkeotsingu sektsioon peamisesse README-sse
- Loo kiirviite juhend

### 3. Loo integratsioonitestid
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Lisa jõudluse võrdlused
Jälgi jõudluse parandusi vigade käsitlemise täiustustest.

### 5. Kasutajate tagasiside
Kogu tagasisidet töötoa osalejatelt:
- Veateadete selguse kohta
- Dokumentatsiooni täielikkuse kohta
- Kasutamise lihtsuse kohta

---

## Ressursid

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Kiirviide**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migratsiooni märkmed**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Peamine repositoorium**: https://github.com/microsoft/Foundry-Local

---

## Hooldus

### Uute näidiste lisamine
Järgi neid mustreid uute näidiste loomisel:

1. Kasuta `workshop_utils` kliendi haldamiseks
2. Lisa põhjalik vigade käsitlemine
3. Toeta keskkonnamuutujaid
4. Lisa tüübiviited ja docstringid
5. Paku informatiivset logimist
6. Lisa kasutusnäited docstringi
7. Linki SDK dokumentatsioonile

### Uuenduste ülevaatamine
Uuenduste ülevaatamisel kontrolli:
- [ ] Vigade käsitlemist kõigil I/O operatsioonidel
- [ ] Tüübiviiteid avalikel funktsioonidel
- [ ] Põhjalikke docstringe
- [ ] Keskkonnamuutujate dokumentatsiooni
- [ ] Informatiivset kasutajate tagasisidet
- [ ] SDK viiteid
- [ ] Järjepidevat koodistiili

---

**Kokkuvõte**: Kõik töötoa Python-näidised järgivad nüüd Foundry Local SDK parimaid tavasid, pakkudes täiustatud vigade käsitlemist, põhjalikku dokumentatsiooni ja parendatud kasutajakogemust. Muutusi, mis rikuksid olemasolevat funktsionaalsust, ei ole - kõik olemasolev funktsionaalsus on säilinud ja täiustatud.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.