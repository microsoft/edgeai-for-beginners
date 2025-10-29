<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:25:20+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "nl"
}
-->
# Workshop Voorbeelden - Overzicht van Foundry Local SDK Updates

## Overzicht

Alle Python-voorbeelden in de map `Workshop/samples` zijn bijgewerkt om te voldoen aan de beste praktijken van de Foundry Local SDK en om consistentie binnen de workshop te waarborgen.

**Datum**: 8 oktober 2025  
**Omvang**: 9 Python-bestanden verspreid over 6 workshop-sessies  
**Hoofdfocus**: Foutafhandeling, documentatie, SDK-patronen, gebruikerservaring

---

## Bijgewerkte Bestanden

### Sessie 01: Aan de Slag
- ✅ `chat_bootstrap.py` - Basisvoorbeelden van chat en streaming

### Sessie 02: RAG-oplossingen
- ✅ `rag_pipeline.py` - RAG-implementatie met embeddings
- ✅ `rag_eval_ragas.py` - RAG-evaluatie met RAGAS-metrics

### Sessie 03: Open Source Modellen
- ✅ `benchmark_oss_models.py` - Benchmarking van meerdere modellen

### Sessie 04: Geavanceerde Modellen
- ✅ `model_compare.py` - Vergelijking tussen SLM en LLM

### Sessie 05: AI-aangedreven Agenten
- ✅ `agents_orchestrator.py` - Coördinatie van meerdere agenten

### Sessie 06: Modellen als Tools
- ✅ `models_router.py` - Intent-gebaseerde modelroutering
- ✅ `models_pipeline.py` - Meerstaps gerouteerde pipeline

### Ondersteunende Infrastructuur
- ✅ `workshop_utils.py` - Volgt al de beste praktijken (geen wijzigingen nodig)

---

## Belangrijke Verbeteringen

### 1. Verbeterde Foutafhandeling

**Voorheen:**
```python
manager, client, model_id = get_client(alias)
```

**Na:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Voordelen:**
- Vriendelijke foutafhandeling met duidelijke foutmeldingen
- Praktische tips voor probleemoplossing
- Correcte exitcodes voor scripting

### 2. Betere Importbeheer

**Voorheen:**
```python
from sentence_transformers import SentenceTransformer
```

**Na:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Voordelen:**
- Duidelijke instructies bij ontbrekende afhankelijkheden
- Voorkomt cryptische importfouten
- Gebruiksvriendelijke installatie-instructies

### 3. Uitgebreide Documentatie

**Toegevoegd aan alle voorbeelden:**
- Documentatie van omgevingsvariabelen in docstrings
- SDK-referentielinks
- Voorbeelden van gebruik
- Gedetailleerde documentatie van functies/parameters
- Type hints voor betere ondersteuning in IDE's

**Voorbeeld:**
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

### 4. Verbeterde Gebruikersfeedback

**Toegevoegd informatieve logging:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Voortgangsindicatoren:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Gestructureerde output:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robuuste Benchmarking

**Verbeteringen in Sessie 03:**
- Foutafhandeling per model (gaat door bij falen)
- Gedetailleerde voortgangsrapportage
- Correct uitgevoerde warming-up rondes
- Ondersteuning voor meting van eerste-token latentie
- Duidelijke scheiding van fasen

### 6. Consistente Type Hints

**Toegevoegd overal:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Voordelen:**
- Betere autocomplete in IDE's
- Vroegtijdige foutdetectie
- Zelfdocumenterende code

### 7. Verbeterde Modelroutering

**Verbeteringen in Sessie 06:**
- Uitgebreide documentatie voor intentdetectie
- Uitleg over modelselectie-algoritme
- Gedetailleerde routeringslogs
- Testoutputformattering
- Foutherstel bij batchtesten

### 8. Multi-Agent Orchestratie

**Verbeteringen in Sessie 05:**
- Voortgangsrapportage per fase
- Foutafhandeling per agent
- Duidelijke pipeline-structuur
- Betere documentatie over geheugengebruik

---

## Testchecklist

### Vereisten
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Test Elk Voorbeeld

#### Sessie 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sessie 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sessie 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sessie 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sessie 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sessie 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Referentie Omgevingsvariabelen

### Algemeen (Alle Voorbeelden)
| Variabele | Beschrijving | Standaard |
|-----------|--------------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Te gebruiken modelalias | Verschilt per voorbeeld |
| `FOUNDRY_LOCAL_ENDPOINT` | Service endpoint overschrijven | Automatisch gedetecteerd |
| `SHOW_USAGE` | Toon tokengebruik | `0` |
| `RETRY_ON_FAIL` | Retry-logica inschakelen | `1` |
| `RETRY_BACKOFF` | Initiële retry-vertraging | `1.0` |

### Specifiek voor Voorbeelden
| Variabele | Gebruikt Door | Beschrijving |
|-----------|--------------|-------------|
| `EMBED_MODEL` | Sessie 02 | Naam van embedding model |
| `RAG_QUESTION` | Sessie 02 | Testvraag voor RAG |
| `BENCH_MODELS` | Sessie 03 | Komma-gescheiden modellen voor benchmarking |
| `BENCH_ROUNDS` | Sessie 03 | Aantal benchmarkrondes |
| `BENCH_PROMPT` | Sessie 03 | Testprompt voor benchmarks |
| `BENCH_STREAM` | Sessie 03 | Meet eerste-token latentie |
| `SLM_ALIAS` | Sessie 04 | Klein taalmodel |
| `LLM_ALIAS` | Sessie 04 | Groot taalmodel |
| `COMPARE_PROMPT` | Sessie 04 | Vergelijkingsprompt voor testen |
| `AGENT_MODEL_PRIMARY` | Sessie 05 | Primair agentmodel |
| `AGENT_MODEL_EDITOR` | Sessie 05 | Editor agentmodel |
| `AGENT_QUESTION` | Sessie 05 | Testvraag voor agenten |
| `PIPELINE_TASK` | Sessie 06 | Taak voor pipeline |

---

## Breaking Changes

**Geen** - Alle wijzigingen zijn achterwaarts compatibel.

Bestaande scripts blijven werken. Nieuwe functies zijn:
- Optionele omgevingsvariabelen
- Verbeterde foutmeldingen (breken functionaliteit niet)
- Extra logging (kan worden onderdrukt)
- Betere type hints (geen impact op runtime)

---

## Geïmplementeerde Beste Praktijken

### 1. Gebruik Altijd Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Correct Foutafhandelingspatroon
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informatieve Logging
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

### 5. Uitgebreide Docstrings
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

### 6. Ondersteuning voor Omgevingsvariabelen
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Gracieus Degradatiegedrag
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

## Veelvoorkomende Problemen & Oplossingen

### Probleem: Importfouten
**Oplossing:** Installeer ontbrekende afhankelijkheden
```bash
pip install sentence-transformers ragas datasets numpy
```

### Probleem: Verbindingsfouten
**Oplossing:** Zorg ervoor dat Foundry Local actief is
```bash
foundry service status
foundry model run phi-4-mini
```

### Probleem: Model Niet Gevonden
**Oplossing:** Controleer beschikbare modellen
```bash
foundry model ls
foundry model download <alias>
```

### Probleem: Trage Prestaties
**Oplossing:** Gebruik kleinere modellen of pas parameters aan
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Volgende Stappen

### 1. Test Alle Voorbeelden
Doorloop de testchecklist hierboven om te verifiëren dat alle voorbeelden correct werken.

### 2. Update Documentatie
- Update markdown-bestanden van sessies met nieuwe voorbeelden
- Voeg een probleemoplossingssectie toe aan de hoofd-README
- Maak een snelreferentiegids

### 3. Maak Integratietests
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Voeg Prestatiebenchmarks Toe
Volg prestatieverbeteringen door verbeteringen in foutafhandeling.

### 5. Gebruikersfeedback
Verzamel feedback van workshopdeelnemers over:
- Duidelijkheid van foutmeldingen
- Volledigheid van documentatie
- Gebruiksgemak

---

## Bronnen

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Snelreferentie**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migratienotities**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Hoofdrepository**: https://github.com/microsoft/Foundry-Local

---

## Onderhoud

### Nieuwe Voorbeelden Toevoegen
Volg deze patronen bij het maken van nieuwe voorbeelden:

1. Gebruik `workshop_utils` voor clientbeheer
2. Voeg uitgebreide foutafhandeling toe
3. Ondersteun omgevingsvariabelen
4. Voeg type hints en docstrings toe
5. Zorg voor informatieve logging
6. Voeg gebruiksvoorbeelden toe in de docstring
7. Link naar SDK-documentatie

### Updates Beoordelen
Bij het beoordelen van updates voor voorbeelden, controleer:
- [ ] Foutafhandeling bij alle I/O-bewerkingen
- [ ] Type hints bij openbare functies
- [ ] Uitgebreide docstrings
- [ ] Documentatie van omgevingsvariabelen
- [ ] Informatieve gebruikersfeedback
- [ ] SDK-referentielinks
- [ ] Consistente codestijl

---

**Samenvatting**: Alle Python-voorbeelden van de workshop volgen nu de beste praktijken van de Foundry Local SDK met verbeterde foutafhandeling, uitgebreide documentatie en een verbeterde gebruikerservaring. Geen breaking changes - alle bestaande functionaliteit is behouden en verbeterd.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.