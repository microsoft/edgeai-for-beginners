<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:15:45+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "no"
}
-->
# Workshop Eksempler - Oppsummering av oppdatering for Foundry Local SDK

## Oversikt

Alle Python-eksempler i `Workshop/samples`-katalogen er oppdatert for å følge beste praksis for Foundry Local SDK og sikre konsistens på tvers av workshoppen.

**Dato**: 8. oktober 2025  
**Omfang**: 9 Python-filer fordelt på 6 workshop-økter  
**Hovedfokus**: Feilhåndtering, dokumentasjon, SDK-mønstre, brukeropplevelse

---

## Oppdaterte filer

### Økt 01: Komme i gang
- ✅ `chat_bootstrap.py` - Grunnleggende eksempler på chat og streaming

### Økt 02: RAG-løsninger
- ✅ `rag_pipeline.py` - RAG-implementering med embeddings
- ✅ `rag_eval_ragas.py` - RAG-evaluering med RAGAS-metrikker

### Økt 03: Åpen kildekode-modeller
- ✅ `benchmark_oss_models.py` - Benchmarking av flere modeller

### Økt 04: Banebrytende modeller
- ✅ `model_compare.py` - Sammenligning mellom SLM og LLM

### Økt 05: AI-drevne agenter
- ✅ `agents_orchestrator.py` - Koordinering av flere agenter

### Økt 06: Modeller som verktøy
- ✅ `models_router.py` - Modellruting basert på intensjon
- ✅ `models_pipeline.py` - Flertrinns rutet pipeline

### Støttende infrastruktur
- ✅ `workshop_utils.py` - Følger allerede beste praksis (ingen endringer nødvendig)

---

## Viktige forbedringer

### 1. Forbedret feilhåndtering

**Før:**
```python
manager, client, model_id = get_client(alias)
```

**Etter:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Fordeler:**
- Smidig feilhåndtering med tydelige feilmeldinger
- Handlingsrettede feilsøkingshint
- Korrekte exit-koder for skripting

### 2. Bedre importhåndtering

**Før:**
```python
from sentence_transformers import SentenceTransformer
```

**Etter:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Fordeler:**
- Klar veiledning når avhengigheter mangler
- Forhindrer kryptiske importfeil
- Brukervennlige installasjonsinstruksjoner

### 3. Omfattende dokumentasjon

**Lagt til i alle eksempler:**
- Dokumentasjon av miljøvariabler i docstrings
- SDK-referanselenker
- Brukseksempler
- Detaljert funksjons-/parameterdokumentasjon
- Type hints for bedre IDE-støtte

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

### 4. Forbedret brukerfeedback

**Lagt til informativ logging:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Fremdriftsindikatorer:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturert output:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robust benchmarking

**Forbedringer i økt 03:**
- Feilhåndtering per modell (fortsetter ved feil)
- Detaljert fremdriftsrapportering
- Korrekt utførte oppvarmingsrunder
- Støtte for måling av første-token latens
- Klar separasjon av stadier

### 6. Konsistente type hints

**Lagt til overalt:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Fordeler:**
- Bedre IDE-autofullføring
- Tidlig feildeteksjon
- Selv-dokumenterende kode

### 7. Forbedret modellruter

**Forbedringer i økt 06:**
- Omfattende dokumentasjon for intensjonsdeteksjon
- Forklaring av modellutvalg-algoritme
- Detaljerte rutelogger
- Formatert testoutput
- Feilgjenoppretting i batch-testing

### 8. Orkestrering av flere agenter

**Forbedringer i økt 05:**
- Fremdriftsrapportering steg for steg
- Feilhåndtering per agent
- Klar pipeline-struktur
- Bedre dokumentasjon for minnehåndtering

---

## Testingsjekkliste

### Forutsetninger
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Test hver prøve

#### Økt 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Økt 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Økt 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Økt 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Økt 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Økt 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Referanse for miljøvariabler

### Globalt (alle eksempler)
| Variabel | Beskrivelse | Standard |
|----------|-------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Modellalias som skal brukes | Varierer per eksempel |
| `FOUNDRY_LOCAL_ENDPOINT` | Overstyr tjenesteendepunkt | Automatisk oppdaget |
| `SHOW_USAGE` | Vis tokenbruk | `0` |
| `RETRY_ON_FAIL` | Aktiver retry-logikk | `1` |
| `RETRY_BACKOFF` | Startforsinkelse for retry | `1.0` |

### Eksempelspesifikt
| Variabel | Brukes av | Beskrivelse |
|----------|-----------|-------------|
| `EMBED_MODEL` | Økt 02 | Navn på embedding-modell |
| `RAG_QUESTION` | Økt 02 | Testspørsmål for RAG |
| `BENCH_MODELS` | Økt 03 | Komma-separerte modeller for benchmarking |
| `BENCH_ROUNDS` | Økt 03 | Antall benchmark-runder |
| `BENCH_PROMPT` | Økt 03 | Testprompt for benchmarks |
| `BENCH_STREAM` | Økt 03 | Måle første-token latens |
| `SLM_ALIAS` | Økt 04 | Liten språkmodell |
| `LLM_ALIAS` | Økt 04 | Stor språkmodell |
| `COMPARE_PROMPT` | Økt 04 | Testprompt for sammenligning |
| `AGENT_MODEL_PRIMARY` | Økt 05 | Primær agentmodell |
| `AGENT_MODEL_EDITOR` | Økt 05 | Editor agentmodell |
| `AGENT_QUESTION` | Økt 05 | Testspørsmål for agenter |
| `PIPELINE_TASK` | Økt 06 | Oppgave for pipeline |

---

## Endringer som bryter kompatibilitet

**Ingen** - Alle endringer er bakoverkompatible.

Eksisterende skript vil fortsatt fungere. Nye funksjoner er:
- Valgfrie miljøvariabler
- Forbedrede feilmeldinger (bryter ikke funksjonalitet)
- Ekstra logging (kan undertrykkes)
- Bedre type hints (ingen påvirkning på runtime)

---

## Implementerte beste praksiser

### 1. Bruk alltid Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Korrekt mønster for feilhåndtering
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informativ logging
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Type hints
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Omfattende docstrings
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

### 6. Støtte for miljøvariabler
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Smidig degradering
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

## Vanlige problemer og løsninger

### Problem: Importfeil
**Løsning:** Installer manglende avhengigheter
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problem: Tilkoblingsfeil
**Løsning:** Sørg for at Foundry Local kjører
```bash
foundry service status
foundry model run phi-4-mini
```

### Problem: Modell ikke funnet
**Løsning:** Sjekk tilgjengelige modeller
```bash
foundry model ls
foundry model download <alias>
```

### Problem: Langsom ytelse
**Løsning:** Bruk mindre modeller eller juster parametere
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Neste steg

### 1. Test alle eksempler
Gå gjennom testingsjekklisten ovenfor for å verifisere at alle eksempler fungerer korrekt.

### 2. Oppdater dokumentasjon
- Oppdater markdown-filer for øktene med nye eksempler
- Legg til feilsøkingsseksjon i hoved-README
- Lag en hurtigreferanseguide

### 3. Lag integrasjonstester
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Legg til ytelsesbenchmarking
Følg opp ytelsesforbedringer fra forbedret feilhåndtering.

### 5. Brukerfeedback
Samle tilbakemeldinger fra workshop-deltakere om:
- Klarhet i feilmeldinger
- Fullstendighet i dokumentasjon
- Brukervennlighet

---

## Ressurser

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Hurtigreferanse**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migreringsnotater**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Hovedrepository**: https://github.com/microsoft/Foundry-Local

---

## Vedlikehold

### Legge til nye eksempler
Følg disse mønstrene når du lager nye eksempler:

1. Bruk `workshop_utils` for klienthåndtering
2. Legg til omfattende feilhåndtering
3. Inkluder støtte for miljøvariabler
4. Legg til type hints og docstrings
5. Gi informativ logging
6. Inkluder brukseksempler i docstring
7. Lenke til SDK-dokumentasjon

### Gjennomgang av oppdateringer
Når du gjennomgår oppdateringer av eksempler, sjekk for:
- [ ] Feilhåndtering på alle I/O-operasjoner
- [ ] Type hints på offentlige funksjoner
- [ ] Omfattende docstrings
- [ ] Dokumentasjon av miljøvariabler
- [ ] Informativ brukerfeedback
- [ ] SDK-referanselenker
- [ ] Konsistent kodestil

---

**Oppsummering**: Alle Workshop Python-eksempler følger nå beste praksis for Foundry Local SDK med forbedret feilhåndtering, omfattende dokumentasjon og forbedret brukeropplevelse. Ingen endringer som bryter kompatibilitet - all eksisterende funksjonalitet er bevart og forbedret.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.