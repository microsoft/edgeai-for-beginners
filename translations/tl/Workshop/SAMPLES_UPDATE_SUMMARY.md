<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:47:39+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "tl"
}
-->
# Mga Halimbawa ng Workshop - Buod ng Update sa Foundry Local SDK

## Pangkalahatang-ideya

Ang lahat ng Python na halimbawa sa direktoryo ng `Workshop/samples` ay na-update upang sumunod sa mga pinakamahusay na kasanayan ng Foundry Local SDK at tiyakin ang pagkakapare-pareho sa buong workshop.

**Petsa**: Oktubre 8, 2025  
**Saklaw**: 9 na Python na file sa 6 na sesyon ng workshop  
**Pangunahing Pokus**: Pag-aasikaso ng error, dokumentasyon, mga pattern ng SDK, karanasan ng gumagamit

---

## Mga Na-update na File

### Sesyon 01: Pagsisimula
- ✅ `chat_bootstrap.py` - Mga pangunahing halimbawa ng chat at streaming

### Sesyon 02: Mga Solusyon sa RAG
- ✅ `rag_pipeline.py` - Implementasyon ng RAG gamit ang embeddings
- ✅ `rag_eval_ragas.py` - Pagsusuri ng RAG gamit ang mga sukatan ng RAGAS

### Sesyon 03: Mga Modelong Open Source
- ✅ `benchmark_oss_models.py` - Pagsusuri ng maraming modelo

### Sesyon 04: Mga Modelong Makabago
- ✅ `model_compare.py` - Paghahambing ng SLM at LLM

### Sesyon 05: Mga Ahenteng Pinapagana ng AI
- ✅ `agents_orchestrator.py` - Koordinasyon ng maraming ahente

### Sesyon 06: Mga Modelo bilang Kasangkapan
- ✅ `models_router.py` - Pag-ruta ng modelo batay sa layunin
- ✅ `models_pipeline.py` - Multi-step na routed pipeline

### Suportang Imprastraktura
- ✅ `workshop_utils.py` - Sumusunod na sa pinakamahusay na kasanayan (walang kailangang pagbabago)

---

## Mga Pangunahing Pagpapabuti

### 1. Pinahusay na Pag-aasikaso ng Error

**Dati:**
```python
manager, client, model_id = get_client(alias)
```

**Ngayon:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Mga Benepisyo:**
- Maayos na pag-aasikaso ng error na may malinaw na mensahe ng error
- Mga actionable na hint para sa troubleshooting
- Tamang exit codes para sa scripting

### 2. Mas Maayos na Pamamahala ng Import

**Dati:**
```python
from sentence_transformers import SentenceTransformer
```

**Ngayon:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Mga Benepisyo:**
- Malinaw na gabay kapag nawawala ang mga dependency
- Maiiwasan ang mga hindi malinaw na error sa import
- Mga user-friendly na tagubilin sa pag-install

### 3. Komprehensibong Dokumentasyon

**Idinagdag sa lahat ng halimbawa:**
- Dokumentasyon ng environment variable sa mga docstring
- Mga link sa reference ng SDK
- Mga halimbawa ng paggamit
- Detalyadong dokumentasyon ng function/parameter
- Mga type hint para sa mas mahusay na suporta sa IDE

**Halimbawa:**
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

### 4. Pinahusay na Feedback ng User

**Idinagdag na impormasyong logging:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Mga tagapagpahiwatig ng progreso:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Structured output:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Mas Matibay na Benchmarking

**Mga pagpapabuti sa Sesyon 03:**
- Pag-aasikaso ng error sa bawat modelo (nagpapatuloy kahit may pagkabigo)
- Detalyadong pag-uulat ng progreso
- Maayos na naipatupad ang mga warmup round
- Suporta sa pagsukat ng latency ng unang token
- Malinaw na paghihiwalay ng mga yugto

### 6. Pare-parehong Type Hints

**Idinagdag sa lahat:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Mga Benepisyo:**
- Mas mahusay na autocomplete sa IDE
- Maagang pagtuklas ng error
- Self-documenting na code

### 7. Pinahusay na Model Router

**Mga pagpapabuti sa Sesyon 06:**
- Komprehensibong dokumentasyon ng pagtuklas ng layunin
- Paliwanag ng algorithm sa pagpili ng modelo
- Detalyadong mga log ng pag-ruta
- Format ng output ng pagsubok
- Pag-recover ng error sa batch testing

### 8. Multi-Agent Orchestration

**Mga pagpapabuti sa Sesyon 05:**
- Pag-uulat ng progreso sa bawat yugto
- Pag-aasikaso ng error sa bawat ahente
- Malinaw na istruktura ng pipeline
- Mas mahusay na dokumentasyon sa pamamahala ng memorya

---

## Checklist sa Pagsubok

### Mga Kinakailangan
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Subukan ang Bawat Halimbawa

#### Sesyon 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sesyon 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sesyon 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sesyon 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sesyon 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sesyon 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Reference ng Environment Variables

### Global (Lahat ng Halimbawa)
| Variable | Deskripsyon | Default |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias ng modelo na gagamitin | Nag-iiba depende sa halimbawa |
| `FOUNDRY_LOCAL_ENDPOINT` | Override ng service endpoint | Auto-detected |
| `SHOW_USAGE` | Ipakita ang paggamit ng token | `0` |
| `RETRY_ON_FAIL` | Paganahin ang retry logic | `1` |
| `RETRY_BACKOFF` | Paunang delay sa retry | `1.0` |

### Partikular sa Halimbawa
| Variable | Ginagamit ng | Deskripsyon |
|----------|--------------|-------------|
| `EMBED_MODEL` | Sesyon 02 | Pangalan ng embedding model |
| `RAG_QUESTION` | Sesyon 02 | Tanong sa pagsubok para sa RAG |
| `BENCH_MODELS` | Sesyon 03 | Mga modelong isusuri, hiwalay ng comma |
| `BENCH_ROUNDS` | Sesyon 03 | Bilang ng mga round ng pagsusuri |
| `BENCH_PROMPT` | Sesyon 03 | Prompt sa pagsubok para sa pagsusuri |
| `BENCH_STREAM` | Sesyon 03 | Sukatin ang latency ng unang token |
| `SLM_ALIAS` | Sesyon 04 | Maliit na modelo ng wika |
| `LLM_ALIAS` | Sesyon 04 | Malaking modelo ng wika |
| `COMPARE_PROMPT` | Sesyon 04 | Prompt sa pagsubok para sa paghahambing |
| `AGENT_MODEL_PRIMARY` | Sesyon 05 | Pangunahing modelo ng ahente |
| `AGENT_MODEL_EDITOR` | Sesyon 05 | Modelo ng ahente para sa editor |
| `AGENT_QUESTION` | Sesyon 05 | Tanong sa pagsubok para sa mga ahente |
| `PIPELINE_TASK` | Sesyon 06 | Gawain para sa pipeline |

---

## Mga Pagbabagong Nakakaapekto

**Wala** - Ang lahat ng pagbabago ay backward compatible.

Ang mga umiiral na script ay patuloy na gagana. Ang mga bagong tampok ay:
- Opsyonal na environment variables
- Pinahusay na mga mensahe ng error (hindi nakakasira sa functionality)
- Karagdagang logging (maaaring i-suppress)
- Mas mahusay na type hints (walang epekto sa runtime)

---

## Mga Pinakamahusay na Kasanayan na Naipatupad

### 1. Laging Gamitin ang Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Tamang Pattern ng Pag-aasikaso ng Error
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Impormatibong Logging
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Type Hints
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Komprehensibong Docstrings
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

### 6. Suporta sa Environment Variable
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Maayos na Pagbaba ng Functionality
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

## Mga Karaniwang Isyu at Solusyon

### Isyu: Mga Error sa Import
**Solusyon:** I-install ang mga nawawalang dependency
```bash
pip install sentence-transformers ragas datasets numpy
```

### Isyu: Mga Error sa Koneksyon
**Solusyon:** Siguraduhing tumatakbo ang Foundry Local
```bash
foundry service status
foundry model run phi-4-mini
```

### Isyu: Hindi Natagpuan ang Modelo
**Solusyon:** Suriin ang mga available na modelo
```bash
foundry model ls
foundry model download <alias>
```

### Isyu: Mabagal na Performance
**Solusyon:** Gumamit ng mas maliit na mga modelo o ayusin ang mga parameter
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Mga Susunod na Hakbang

### 1. Subukan ang Lahat ng Halimbawa
Sundan ang checklist sa pagsubok sa itaas upang tiyakin na gumagana nang tama ang lahat ng halimbawa.

### 2. I-update ang Dokumentasyon
- I-update ang mga markdown file ng sesyon gamit ang mga bagong halimbawa
- Magdagdag ng seksyon ng troubleshooting sa pangunahing README
- Gumawa ng quick reference guide

### 3. Gumawa ng Integration Tests
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Magdagdag ng Performance Benchmarks
Subaybayan ang mga pagpapabuti sa performance mula sa mga enhancement sa pag-aasikaso ng error.

### 5. Feedback ng User
Kolektahin ang feedback mula sa mga kalahok ng workshop tungkol sa:
- Kalinawan ng mga mensahe ng error
- Kumpletong dokumentasyon
- Dali ng paggamit

---

## Mga Resources

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Quick Reference**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migration Notes**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Main Repository**: https://github.com/microsoft/Foundry-Local

---

## Pagpapanatili

### Pagdaragdag ng Bagong Halimbawa
Sundin ang mga pattern na ito kapag gumagawa ng bagong halimbawa:

1. Gamitin ang `workshop_utils` para sa pamamahala ng client
2. Magdagdag ng komprehensibong pag-aasikaso ng error
3. Isama ang suporta sa environment variable
4. Magdagdag ng type hints at docstrings
5. Magbigay ng impormatibong logging
6. Isama ang mga halimbawa ng paggamit sa docstring
7. Mag-link sa dokumentasyon ng SDK

### Pagsusuri ng Mga Update
Kapag sinusuri ang mga update sa halimbawa, suriin ang:
- [ ] Pag-aasikaso ng error sa lahat ng I/O operations
- [ ] Type hints sa mga pampublikong function
- [ ] Komprehensibong docstrings
- [ ] Dokumentasyon ng environment variable
- [ ] Impormatibong feedback ng user
- [ ] Mga link sa reference ng SDK
- [ ] Pare-parehong istilo ng code

---

**Buod**: Ang lahat ng Python na halimbawa sa Workshop ay sumusunod na sa mga pinakamahusay na kasanayan ng Foundry Local SDK na may pinahusay na pag-aasikaso ng error, komprehensibong dokumentasyon, at mas pinahusay na karanasan ng user. Walang mga pagbabago na nakakaapekto - ang lahat ng umiiral na functionality ay napanatili at pinahusay.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.