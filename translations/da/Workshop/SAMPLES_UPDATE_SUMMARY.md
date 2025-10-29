<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:11:19+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "da"
}
-->
# Workshop Eksempler - Foundry Local SDK Opdateringsoversigt

## Oversigt

Alle Python-eksempler i `Workshop/samples`-mappen er blevet opdateret for at følge Foundry Local SDK bedste praksis og sikre konsistens på tværs af workshoppen.

**Dato**: 8. oktober 2025  
**Omfang**: 9 Python-filer på tværs af 6 workshop-sessioner  
**Primært fokus**: Fejlhåndtering, dokumentation, SDK-mønstre, brugeroplevelse

---

## Opdaterede Filer

### Session 01: Kom godt i gang
- ✅ `chat_bootstrap.py` - Grundlæggende chat- og streamingeksempler

### Session 02: RAG-løsninger
- ✅ `rag_pipeline.py` - RAG-implementering med embeddings
- ✅ `rag_eval_ragas.py` - RAG-evaluering med RAGAS-metrics

### Session 03: Open Source-modeller
- ✅ `benchmark_oss_models.py` - Multi-model benchmarking

### Session 04: Avancerede modeller
- ✅ `model_compare.py` - SLM vs LLM sammenligning

### Session 05: AI-drevne agenter
- ✅ `agents_orchestrator.py` - Koordinering af flere agenter

### Session 06: Modeller som værktøjer
- ✅ `models_router.py` - Intent-baseret model-routing
- ✅ `models_pipeline.py` - Multi-step routed pipeline

### Understøttende Infrastruktur
- ✅ `workshop_utils.py` - Følger allerede bedste praksis (ingen ændringer nødvendige)

---

## Centrale Forbedringer

### 1. Forbedret Fejlhåndtering

**Før:**
```python
manager, client, model_id = get_client(alias)
```

**Efter:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Fordele:**
- Elegant fejlhåndtering med klare fejlmeddelelser
- Handlingsrettede fejlfindingstips
- Korrekte exit-koder til scripting

### 2. Bedre Importhåndtering

**Før:**
```python
from sentence_transformers import SentenceTransformer
```

**Efter:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Fordele:**
- Klar vejledning, når afhængigheder mangler
- Forhindrer kryptiske importfejl
- Brugervenlige installationsinstruktioner

### 3. Omfattende Dokumentation

**Tilføjet til alle eksempler:**
- Dokumentation af miljøvariabler i docstrings
- SDK-referencelinks
- Brugsvejledninger
- Detaljeret funktion/parameterdokumentation
- Type hints for bedre IDE-support

**Eksempel:**
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

### 4. Forbedret Brugerfeedback

**Tilføjet informativ logning:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Fremskridtsindikatorer:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Struktureret output:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robust Benchmarking

**Forbedringer i Session 03:**
- Fejlhåndtering pr. model (fortsætter ved fejl)
- Detaljeret fremskridtsrapportering
- Korrekt udførelse af opvarmningsrunder
- Understøttelse af måling af første-token latenstid
- Klar adskillelse af stadier

### 6. Konsistente Type Hints

**Tilføjet overalt:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Fordele:**
- Bedre IDE-autocomplete
- Tidlig fejldetektion
- Selv-dokumenterende kode

### 7. Forbedret Model Router

**Forbedringer i Session 06:**
- Omfattende dokumentation af intent-detektion
- Forklaring af modeludvælgelsesalgoritme
- Detaljerede routing-logfiler
- Testoutput-formattering
- Fejlgenopretning i batch-testning

### 8. Multi-Agent Orkestrering

**Forbedringer i Session 05:**
- Fremskridtsrapportering trin for trin
- Fejlhåndtering pr. agent
- Klar pipeline-struktur
- Bedre dokumentation af hukommelseshåndtering

---

## Test Tjekliste

### Forudsætninger
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Test Hver Eksempel

#### Session 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Session 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Session 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Session 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Session 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Session 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Miljøvariabler Reference

### Globalt (Alle Eksempler)
| Variabel | Beskrivelse | Standard |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Modelalias der skal bruges | Varierer efter eksempel |
| `FOUNDRY_LOCAL_ENDPOINT` | Overstyr serviceendpoint | Auto-detekteret |
| `SHOW_USAGE` | Vis tokenforbrug | `0` |
| `RETRY_ON_FAIL` | Aktiver retry-logik | `1` |
| `RETRY_BACKOFF` | Indledende retry-forsinkelse | `1.0` |

### Eksempel-specifikt
| Variabel | Bruges af | Beskrivelse |
|----------|-----------|-------------|
| `EMBED_MODEL` | Session 02 | Navn på embedding-model |
| `RAG_QUESTION` | Session 02 | Testspørgsmål til RAG |
| `BENCH_MODELS` | Session 03 | Kommaseparerede modeller til benchmarking |
| `BENCH_ROUNDS` | Session 03 | Antal benchmark-runder |
| `BENCH_PROMPT` | Session 03 | Testprompt til benchmarks |
| `BENCH_STREAM` | Session 03 | Mål første-token latenstid |
| `SLM_ALIAS` | Session 04 | Lille sprogmodel |
| `LLM_ALIAS` | Session 04 | Stor sprogmodel |
| `COMPARE_PROMPT` | Session 04 | Sammenligningstestprompt |
| `AGENT_MODEL_PRIMARY` | Session 05 | Primær agentmodel |
| `AGENT_MODEL_EDITOR` | Session 05 | Editor-agentmodel |
| `AGENT_QUESTION` | Session 05 | Testspørgsmål til agenter |
| `PIPELINE_TASK` | Session 06 | Opgave til pipeline |

---

## Brudte Ændringer

**Ingen** - Alle ændringer er bagudkompatible.

Eksisterende scripts vil fortsat fungere. Nye funktioner er:
- Valgfrie miljøvariabler
- Forbedrede fejlmeddelelser (bryder ikke funktionalitet)
- Yderligere logning (kan undertrykkes)
- Bedre type hints (ingen runtime-påvirkning)

---

## Implementerede Bedste Praksis

### 1. Brug Altid Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Korrekt Fejlhåndteringsmønster
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informativ Logning
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

### 5. Omfattende Docstrings
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

### 6. Understøttelse af Miljøvariabler
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Elegant Nedgradering
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

## Almindelige Problemer & Løsninger

### Problem: Importfejl
**Løsning:** Installer manglende afhængigheder
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problem: Forbindelsesfejl
**Løsning:** Sørg for, at Foundry Local kører
```bash
foundry service status
foundry model run phi-4-mini
```

### Problem: Model Ikke Fundet
**Løsning:** Tjek tilgængelige modeller
```bash
foundry model ls
foundry model download <alias>
```

### Problem: Langsom Ydeevne
**Løsning:** Brug mindre modeller eller juster parametre
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Næste Skridt

### 1. Test Alle Eksempler
Gennemgå test-tjeklisten ovenfor for at verificere, at alle eksempler fungerer korrekt.

### 2. Opdater Dokumentation
- Opdater sessionens markdown-filer med nye eksempler
- Tilføj fejlfinding-sektion til hoved-README
- Opret en hurtig referenceguide

### 3. Opret Integrationstests
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Tilføj Ydeevne Benchmarks
Spor ydeevneforbedringer fra fejlhåndteringsforbedringer.

### 5. Brugerfeedback
Indsaml feedback fra workshopdeltagere om:
- Klarhed i fejlmeddelelser
- Dokumentationens fuldstændighed
- Brugervenlighed

---

## Ressourcer

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Hurtig Reference**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migrationsnoter**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Hovedrepository**: https://github.com/microsoft/Foundry-Local

---

## Vedligeholdelse

### Tilføjelse af Nye Eksempler
Følg disse mønstre, når du opretter nye eksempler:

1. Brug `workshop_utils` til klienthåndtering
2. Tilføj omfattende fejlhåndtering
3. Inkluder understøttelse af miljøvariabler
4. Tilføj type hints og docstrings
5. Giv informativ logning
6. Inkluder brugsvejledninger i docstring
7. Link til SDK-dokumentation

### Gennemgang af Opdateringer
Når du gennemgår opdateringer af eksempler, skal du kontrollere:
- [ ] Fejlhåndtering på alle I/O-operationer
- [ ] Type hints på offentlige funktioner
- [ ] Omfattende docstrings
- [ ] Dokumentation af miljøvariabler
- [ ] Informativ brugerfeedback
- [ ] SDK-referencelinks
- [ ] Konsistent kodestil

---

**Opsummering**: Alle Workshop Python-eksempler følger nu Foundry Local SDK bedste praksis med forbedret fejlhåndtering, omfattende dokumentation og forbedret brugeroplevelse. Ingen brudte ændringer - al eksisterende funktionalitet er bevaret og forbedret.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.