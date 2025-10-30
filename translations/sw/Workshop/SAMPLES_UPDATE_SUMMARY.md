<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:52:58+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "sw"
}
-->
# Sampuli za Warsha - Muhtasari wa Sasisho la Foundry Local SDK

## Muhtasari

Sampuli zote za Python katika saraka ya `Workshop/samples` zimesasishwa kufuata mazoea bora ya Foundry Local SDK na kuhakikisha uthabiti katika warsha.

**Tarehe**: Oktoba 8, 2025  
**Wigo**: Faili 9 za Python katika vipindi 6 vya warsha  
**Lengo Kuu**: Kushughulikia makosa, nyaraka, mifumo ya SDK, uzoefu wa mtumiaji

---

## Faili Zilizosasishwa

### Kipindi 01: Kuanza
- ✅ `chat_bootstrap.py` - Mifano ya msingi ya mazungumzo na utiririshaji

### Kipindi 02: Suluhisho za RAG
- ✅ `rag_pipeline.py` - Utekelezaji wa RAG na embeddings
- ✅ `rag_eval_ragas.py` - Tathmini ya RAG na vipimo vya RAGAS

### Kipindi 03: Miundo ya Chanzo Huria
- ✅ `benchmark_oss_models.py` - Upimaji wa miundo mingi

### Kipindi 04: Miundo ya Kisasa
- ✅ `model_compare.py` - Ulinganisho wa SLM dhidi ya LLM

### Kipindi 05: Mawakala Wanaotumia AI
- ✅ `agents_orchestrator.py` - Uratibu wa mawakala wengi

### Kipindi 06: Miundo kama Zana
- ✅ `models_router.py` - Uelekezaji wa miundo kulingana na nia
- ✅ `models_pipeline.py` - Njia ya hatua nyingi iliyopangwa

### Miundombinu ya Msaada
- ✅ `workshop_utils.py` - Tayari inafuata mazoea bora (hakuna mabadiliko yanayohitajika)

---

## Maboresho Muhimu

### 1. Kuboresha Kushughulikia Makosa

**Kabla:**
```python
manager, client, model_id = get_client(alias)
```

**Baada:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Faida:**
- Kushughulikia makosa kwa ustadi na ujumbe wa wazi wa makosa
- Vidokezo vya kutatua matatizo
- Nambari sahihi za kutoka kwa maandishi

### 2. Usimamizi Bora wa Uingizaji

**Kabla:**
```python
from sentence_transformers import SentenceTransformer
```

**Baada:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Faida:**
- Mwongozo wazi wakati utegemezi haupo
- Kuzuia makosa ya uingizaji yasiyoeleweka
- Maelekezo ya usakinishaji yanayofaa kwa mtumiaji

### 3. Nyaraka za Kina

**Imeongezwa kwa sampuli zote:**
- Nyaraka za mabadiliko ya mazingira katika docstrings
- Viungo vya marejeleo ya SDK
- Mifano ya matumizi
- Nyaraka za kina za kazi/parameta
- Vidokezo vya aina kwa msaada bora wa IDE

**Mfano:**
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

### 4. Maoni Bora ya Mtumiaji

**Imeongezwa ukumbusho wa taarifa:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Viashiria vya maendeleo:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Matokeo yaliyopangwa:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Upimaji Imara

**Maboresho ya Kipindi 03:**
- Kushughulikia makosa ya kila muundo (inaendelea hata ikishindwa)
- Kuripoti maendeleo kwa kina
- Raundi za kujiandaa zinatekelezwa ipasavyo
- Msaada wa kipimo cha ucheleweshaji wa tokeni ya kwanza
- Utenganisho wazi wa hatua

### 6. Vidokezo vya Aina Vinavyolingana

**Imeongezwa kote:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Faida:**
- Autocomplete bora ya IDE
- Kugundua makosa mapema
- Nambari inayojieleza yenyewe

### 7. Uelekezaji wa Muundo Ulioboreshwa

**Maboresho ya Kipindi 06:**
- Nyaraka za kina za kugundua nia
- Maelezo ya algorithimu ya kuchagua muundo
- Magogo ya uelekezaji wa kina
- Muundo wa matokeo ya majaribio
- Urejeshaji wa makosa katika majaribio ya kundi

### 8. Uratibu wa Mawakala Wengi

**Maboresho ya Kipindi 05:**
- Kuripoti maendeleo hatua kwa hatua
- Kushughulikia makosa ya kila wakala
- Muundo wazi wa njia
- Nyaraka bora za usimamizi wa kumbukumbu

---

## Orodha ya Ukaguzi wa Upimaji

### Mahitaji ya Awali
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Jaribu Kila Sampuli

#### Kipindi 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Kipindi 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Kipindi 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Kipindi 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Kipindi 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Kipindi 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Marejeleo ya Mabadiliko ya Mazingira

### Kwa Ujumla (Sampuli Zote)
| Kigezo | Maelezo | Chaguo-msingi |
|--------|---------|--------------|
| `FOUNDRY_LOCAL_ALIAS` | Jina la mfano wa kutumia | Inatofautiana kwa sampuli |
| `FOUNDRY_LOCAL_ENDPOINT` | Badilisha mwisho wa huduma | Inatambuliwa kiotomatiki |
| `SHOW_USAGE` | Onyesha matumizi ya tokeni | `0` |
| `RETRY_ON_FAIL` | Washa mantiki ya kujaribu tena | `1` |
| `RETRY_BACKOFF` | Muda wa kuchelewa kujaribu tena | `1.0` |

### Sampuli Maalum
| Kigezo | Kinachotumiwa na | Maelezo |
|--------|------------------|---------|
| `EMBED_MODEL` | Kipindi 02 | Jina la mfano wa embedding |
| `RAG_QUESTION` | Kipindi 02 | Swali la majaribio kwa RAG |
| `BENCH_MODELS` | Kipindi 03 | Miundo iliyotenganishwa kwa koma ya kupima |
| `BENCH_ROUNDS` | Kipindi 03 | Idadi ya raundi za kupima |
| `BENCH_PROMPT` | Kipindi 03 | Kidokezo cha majaribio kwa upimaji |
| `BENCH_STREAM` | Kipindi 03 | Pima ucheleweshaji wa tokeni ya kwanza |
| `SLM_ALIAS` | Kipindi 04 | Mfano mdogo wa lugha |
| `LLM_ALIAS` | Kipindi 04 | Mfano mkubwa wa lugha |
| `COMPARE_PROMPT` | Kipindi 04 | Kidokezo cha majaribio ya kulinganisha |
| `AGENT_MODEL_PRIMARY` | Kipindi 05 | Mfano wa wakala mkuu |
| `AGENT_MODEL_EDITOR` | Kipindi 05 | Mfano wa wakala mhariri |
| `AGENT_QUESTION` | Kipindi 05 | Swali la majaribio kwa mawakala |
| `PIPELINE_TASK` | Kipindi 06 | Kazi ya njia |

---

## Mabadiliko Makubwa

**Hakuna** - Mabadiliko yote yanalingana na yaliyopita.

Skripti zilizopo zitaendelea kufanya kazi. Vipengele vipya ni:
- Vigezo vya mazingira vya hiari
- Ujumbe wa makosa ulioboreshwa (hauharibu utendaji)
- Magogo ya ziada (yanaweza kuzimwa)
- Vidokezo bora vya aina (hakuna athari ya wakati wa kukimbia)

---

## Mazoea Bora Yaliyotekelezwa

### 1. Tumia Workshop Utils Kila Wakati
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Muundo Sahihi wa Kushughulikia Makosa
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Magogo ya Taarifa
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Vidokezo vya Aina
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstrings za Kina
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

### 6. Msaada wa Vigezo vya Mazingira
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Kushuka kwa Neema
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

## Masuala ya Kawaida na Suluhisho

### Tatizo: Makosa ya Uingizaji
**Suluhisho:** Sakinisha utegemezi unaokosekana
```bash
pip install sentence-transformers ragas datasets numpy
```

### Tatizo: Makosa ya Muunganisho
**Suluhisho:** Hakikisha Foundry Local inaendesha
```bash
foundry service status
foundry model run phi-4-mini
```

### Tatizo: Mfano Haupatikani
**Suluhisho:** Angalia miundo inayopatikana
```bash
foundry model ls
foundry model download <alias>
```

### Tatizo: Utendaji Polepole
**Suluhisho:** Tumia miundo midogo au rekebisha vigezo
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Hatua Zifuatazo

### 1. Jaribu Sampuli Zote
Pitisha orodha ya ukaguzi ya majaribio hapo juu ili kuthibitisha sampuli zote zinafanya kazi ipasavyo.

### 2. Sasisha Nyaraka
- Sasisha faili za warsha za markdown na mifano mipya
- Ongeza sehemu ya kutatua matatizo kwenye README kuu
- Unda mwongozo wa rejeleo la haraka

### 3. Unda Majaribio ya Muunganisho
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Ongeza Upimaji wa Utendaji
Fuatilia maboresho ya utendaji kutoka kwa maboresho ya kushughulikia makosa.

### 5. Maoni ya Watumiaji
Kusanya maoni kutoka kwa washiriki wa warsha kuhusu:
- Uwazi wa ujumbe wa makosa
- Ukamilifu wa nyaraka
- Urahisi wa matumizi

---

## Rasilimali

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rejeleo la Haraka**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Vidokezo vya Uhamisho**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Hifadhi Kuu**: https://github.com/microsoft/Foundry-Local

---

## Matengenezo

### Kuongeza Sampuli Mpya
Fuata mifumo hii unapotengeneza sampuli mpya:

1. Tumia `workshop_utils` kwa usimamizi wa mteja
2. Ongeza kushughulikia makosa kwa kina
3. Jumuisha msaada wa vigezo vya mazingira
4. Ongeza vidokezo vya aina na docstrings
5. Toa magogo ya taarifa
6. Jumuisha mifano ya matumizi katika docstring
7. Unganisha na nyaraka za SDK

### Kukagua Sasisho
Unapokagua sasisho za sampuli, hakikisha:
- [ ] Kushughulikia makosa kwenye operesheni zote za I/O
- [ ] Vidokezo vya aina kwenye kazi za umma
- [ ] Docstrings za kina
- [ ] Nyaraka za vigezo vya mazingira
- [ ] Maoni ya mtumiaji yenye taarifa
- [ ] Viungo vya marejeleo ya SDK
- [ ] Mtindo wa nambari unaolingana

---

**Muhtasari**: Sampuli zote za Python za Warsha sasa zinafuata mazoea bora ya Foundry Local SDK na kushughulikia makosa kwa ustadi, nyaraka za kina, na uzoefu bora wa mtumiaji. Hakuna mabadiliko makubwa - utendaji wote uliopo umehifadhiwa na kuboreshwa.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.