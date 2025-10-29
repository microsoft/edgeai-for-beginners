<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T23:50:11+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "lt"
}
-->
# Dirbtuvių Pavyzdžiai - Foundry Local SDK Atnaujinimo Santrauka

## Apžvalga

Visi Python pavyzdžiai kataloge `Workshop/samples` buvo atnaujinti, kad atitiktų Foundry Local SDK geriausią praktiką ir užtikrintų nuoseklumą visose dirbtuvėse.

**Data**: 2025 m. spalio 8 d.  
**Apimtis**: 9 Python failai per 6 dirbtuvių sesijas  
**Pagrindinis dėmesys**: Klaidų tvarkymas, dokumentacija, SDK šablonai, vartotojo patirtis

---

## Atnaujinti Failai

### Sesija 01: Pradžia
- ✅ `chat_bootstrap.py` - Pagrindiniai pokalbių ir srautinio perdavimo pavyzdžiai

### Sesija 02: RAG Sprendimai
- ✅ `rag_pipeline.py` - RAG įgyvendinimas su įterpimais
- ✅ `rag_eval_ragas.py` - RAG vertinimas naudojant RAGAS metrikas

### Sesija 03: Atviro Kodo Modeliai
- ✅ `benchmark_oss_models.py` - Daugelio modelių palyginimas

### Sesija 04: Pažangiausi Modeliai
- ✅ `model_compare.py` - SLM ir LLM palyginimas

### Sesija 05: AI Valdomi Agentai
- ✅ `agents_orchestrator.py` - Daugiaagentinė koordinacija

### Sesija 06: Modeliai kaip Įrankiai
- ✅ `models_router.py` - Modelių maršrutizavimas pagal ketinimus
- ✅ `models_pipeline.py` - Daugiapakopė maršrutizuota veiksmų seka

### Palaikomoji Infrastruktūra
- ✅ `workshop_utils.py` - Jau atitinka geriausią praktiką (pakeitimų nereikia)

---

## Pagrindiniai Patobulinimai

### 1. Patobulintas Klaidų Tvarkymas

**Prieš:**
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

**Privalumai:**
- Sklandus klaidų tvarkymas su aiškiomis klaidų žinutėmis
- Veiksmai problemų sprendimui
- Tinkami išėjimo kodai scenarijams

### 2. Geresnis Importų Valdymas

**Prieš:**
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

**Privalumai:**
- Aiškios instrukcijos, kai trūksta priklausomybių
- Išvengiama neaiškių importo klaidų
- Patogios diegimo instrukcijos vartotojui

### 3. Išsami Dokumentacija

**Pridėta prie visų pavyzdžių:**
- Aplinkos kintamųjų dokumentacija docstring'e
- SDK nuorodos
- Naudojimo pavyzdžiai
- Išsami funkcijų/parametrų dokumentacija
- Tipų užuominos geresniam IDE palaikymui

**Pavyzdys:**
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

### 4. Patobulintas Vartotojo Grįžtamasis Ryšys

**Pridėta informatyvi registracija:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Progreso indikatoriai:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Struktūrizuotas išvestis:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Patikimas Palyginimas

**Sesijos 03 patobulinimai:**
- Klaidų tvarkymas kiekvienam modeliui (tęsiama po nesėkmės)
- Išsami progreso ataskaita
- Tinkamai vykdomi apšilimo raundai
- Palaikymas pirmojo ženklo vėlavimo matavimui
- Aiškus etapų atskyrimas

### 6. Nuoseklios Tipų Užuominos

**Pridėta visur:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Privalumai:**
- Geresnis IDE automatinis užbaigimas
- Ankstyvas klaidų aptikimas
- Savarankiškai dokumentuojamas kodas

### 7. Patobulintas Modelių Maršrutizatorius

**Sesijos 06 patobulinimai:**
- Išsami ketinimų aptikimo dokumentacija
- Modelių pasirinkimo algoritmo paaiškinimas
- Išsami maršrutizavimo registracija
- Testavimo išvesties formatavimas
- Klaidų atkūrimas grupinio testavimo metu

### 8. Daugiaagentinė Orkestracija

**Sesijos 05 patobulinimai:**
- Progreso ataskaita etapais
- Klaidų tvarkymas kiekvienam agentui
- Aiški veiksmų sekos struktūra
- Geresnė atminties valdymo dokumentacija

---

## Testavimo Kontrolinis Sąrašas

### Būtinos Sąlygos
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testuokite Kiekvieną Pavyzdį

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

## Aplinkos Kintamųjų Nuoroda

### Globalūs (Visiems Pavyzdžiams)
| Kintamasis | Aprašymas | Numatytasis |
|------------|-----------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Naudojamas modelio pavadinimas | Skiriasi priklausomai nuo pavyzdžio |
| `FOUNDRY_LOCAL_ENDPOINT` | Paslaugos galinio taško pakeitimas | Automatiškai aptinkamas |
| `SHOW_USAGE` | Rodyti žetonų naudojimą | `0` |
| `RETRY_ON_FAIL` | Įjungti pakartotinio bandymo logiką | `1` |
| `RETRY_BACKOFF` | Pradinė pakartotinio bandymo delsimo trukmė | `1.0` |

### Specifiniai Pavyzdžiams
| Kintamasis | Naudojamas | Aprašymas |
|------------|-----------|-----------|
| `EMBED_MODEL` | Sesija 02 | Įterpimo modelio pavadinimas |
| `RAG_QUESTION` | Sesija 02 | Testavimo klausimas RAG |
| `BENCH_MODELS` | Sesija 03 | Modeliai, kuriuos reikia palyginti (atskirti kableliais) |
| `BENCH_ROUNDS` | Sesija 03 | Palyginimo raundų skaičius |
| `BENCH_PROMPT` | Sesija 03 | Testavimo užklausa palyginimams |
| `BENCH_STREAM` | Sesija 03 | Pirmojo ženklo vėlavimo matavimas |
| `SLM_ALIAS` | Sesija 04 | Mažas kalbos modelis |
| `LLM_ALIAS` | Sesija 04 | Didelis kalbos modelis |
| `COMPARE_PROMPT` | Sesija 04 | Palyginimo testavimo užklausa |
| `AGENT_MODEL_PRIMARY` | Sesija 05 | Pagrindinis agento modelis |
| `AGENT_MODEL_EDITOR` | Sesija 05 | Redaktoriaus agento modelis |
| `AGENT_QUESTION` | Sesija 05 | Testavimo klausimas agentams |
| `PIPELINE_TASK` | Sesija 06 | Veiksmų sekos užduotis |

---

## Esminiai Pakeitimai

**Nėra** - Visi pakeitimai yra suderinami su ankstesnėmis versijomis.

Esami scenarijai veiks toliau. Naujos funkcijos:
- Pasirenkami aplinkos kintamieji
- Patobulintos klaidų žinutės (nepažeidžia funkcionalumo)
- Papildoma registracija (gali būti išjungta)
- Geresnės tipų užuominos (neturi įtakos vykdymui)

---

## Įgyvendintos Geriausios Praktikos

### 1. Visada Naudokite Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Tinkamas Klaidų Tvarkymo Šablonas
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informatyvi Registracija
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Tipų Užuominos
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Išsamūs Docstring'ai
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

### 6. Aplinkos Kintamųjų Palaikymas
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Sklandus Degradavimas
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

## Dažnos Problemos ir Sprendimai

### Problema: Importo Klaidos
**Sprendimas:** Įdiekite trūkstamas priklausomybes
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problema: Ryšio Klaidos
**Sprendimas:** Įsitikinkite, kad Foundry Local veikia
```bash
foundry service status
foundry model run phi-4-mini
```

### Problema: Modelis Nerastas
**Sprendimas:** Patikrinkite galimus modelius
```bash
foundry model ls
foundry model download <alias>
```

### Problema: Lėtas Veikimas
**Sprendimas:** Naudokite mažesnius modelius arba koreguokite parametrus
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Tolimesni Žingsniai

### 1. Testuokite Visus Pavyzdžius
Atlikite testavimo kontrolinį sąrašą, kad patikrintumėte visų pavyzdžių veikimą.

### 2. Atnaujinkite Dokumentaciją
- Atnaujinkite sesijų markdown failus su naujais pavyzdžiais
- Pridėkite problemų sprendimo skyrių į pagrindinį README
- Sukurkite greitos nuorodos vadovą

### 3. Sukurkite Integracijos Testus
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Pridėkite Našumo Palyginimus
Sekite našumo patobulinimus, atsiradusius dėl klaidų tvarkymo patobulinimų.

### 5. Vartotojų Grįžtamasis Ryšys
Surinkite dirbtuvių dalyvių atsiliepimus apie:
- Klaidų žinučių aiškumą
- Dokumentacijos išsamumą
- Naudojimo paprastumą

---

## Ištekliai

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Greita Nuoroda**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migracijos Pastabos**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Pagrindinis Saugykla**: https://github.com/microsoft/Foundry-Local

---

## Priežiūra

### Nauji Pavyzdžiai
Kuriant naujus pavyzdžius, laikykitės šių šablonų:

1. Naudokite `workshop_utils` klientų valdymui
2. Pridėkite išsamų klaidų tvarkymą
3. Įtraukite aplinkos kintamųjų palaikymą
4. Pridėkite tipų užuominas ir docstring'us
5. Suteikite informatyvią registraciją
6. Įtraukite naudojimo pavyzdžius docstring'e
7. Pridėkite nuorodas į SDK dokumentaciją

### Atnaujinimų Peržiūra
Peržiūrint pavyzdžių atnaujinimus, patikrinkite:
- [ ] Klaidų tvarkymą visose I/O operacijose
- [ ] Tipų užuominas viešose funkcijose
- [ ] Išsamius docstring'us
- [ ] Aplinkos kintamųjų dokumentaciją
- [ ] Informatyvų vartotojo grįžtamąjį ryšį
- [ ] SDK nuorodas
- [ ] Nuoseklų kodo stilių

---

**Santrauka**: Visi dirbtuvių Python pavyzdžiai dabar atitinka Foundry Local SDK geriausią praktiką su patobulintu klaidų tvarkymu, išsamia dokumentacija ir pagerinta vartotojo patirtimi. Nėra esminių pakeitimų - visa esama funkcionalumas išsaugotas ir patobulintas.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.