<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:11:34+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "da"
}
-->
# Foundry Local SDK Migrationsnoter

## Oversigt

Alle Python-filer i Workshop-mappen er blevet opdateret til at følge de nyeste mønstre fra den officielle [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Ændringsoversigt

### Kerneinfrastruktur (`workshop_utils.py`)

#### Forbedrede funktioner:
- **Support for endpoint-override**: Tilføjet understøttelse af miljøvariablen `FOUNDRY_LOCAL_ENDPOINT`
- **Forbedret fejlhåndtering**: Bedre undtagelseshåndtering med detaljerede fejlmeddelelser
- **Forbedret caching**: Cache-nøgler inkluderer nu endpoint for scenarier med flere endpoints
- **Eksponentiel backoff**: Retry-logik bruger nu eksponentiel backoff for bedre pålidelighed
- **Typeannoteringer**: Tilføjet omfattende type hints for bedre IDE-support

#### Nye funktioner:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Eksempelanvendelser

#### Session 01: Chat Bootstrap (`chat_bootstrap.py`)
- Opdateret standardmodel fra `phi-3.5-mini` til `phi-4-mini`
- Tilføjet support for endpoint-override
- Forbedret dokumentation med SDK-referencer

#### Session 02: RAG Pipeline (`rag_pipeline.py`)
- Opdateret til at bruge `phi-4-mini` som standard
- Tilføjet support for endpoint-override
- Forbedret dokumentation med detaljer om miljøvariabler

#### Session 02: RAG Evaluering (`rag_eval_ragas.py`)
- Opdateret modelstandarder
- Tilføjet endpoint-konfiguration
- Forbedret fejlhåndtering

#### Session 03: Benchmarking (`benchmark_oss_models.py`)
- Opdateret standardmodelliste til at inkludere `phi-4-mini`
- Tilføjet omfattende dokumentation om miljøvariabler
- Forbedret funktionsdokumentation
- Tilføjet support for endpoint-override overalt

#### Session 04: Model Sammenligning (`model_compare.py`)
- Opdateret standard LLM fra `gpt-oss-20b` til `qwen2.5-7b`
- Tilføjet endpoint-konfiguration
- Forbedret dokumentation

#### Session 05: Multi-Agent Orkestrering (`agents_orchestrator.py`)
- Tilføjet type hints (ændret `str | None` til `Optional[str]`)
- Forbedret dokumentation for Agent-klassen
- Tilføjet support for endpoint-override
- Forbedret initialiseringsmønster

#### Session 06: Model Router (`models_router.py`)
- Tilføjet endpoint-konfiguration
- Forbedret dokumentation for hensigtsdetektion
- Forbedret dokumentation for routing-logik

#### Session 06: Pipeline (`models_pipeline.py`)
- Tilføjet omfattende funktionsdokumentation
- Forbedret trin-for-trin dokumentation
- Forbedret fejlhåndtering

### Scripts

#### Benchmark Eksport (`export_benchmark_markdown.py`)
- Tilføjet support for endpoint-override
- Opdateret standardmodeller
- Forbedret funktionsdokumentation
- Forbedret fejlhåndtering

#### CLI Linter (`lint_markdown_cli.py`)
- Tilføjet SDK-referencelinks
- Forbedret brugsdokumentation

### Tests

#### Smoke Tests (`smoke.py`)
- Tilføjet support for endpoint-override
- Forbedret dokumentation
- Forbedret testcasedokumentation
- Bedre fejlrapportering

## Miljøvariabler

Alle eksempler understøtter nu disse miljøvariabler:

### Kernekonfiguration
- `FOUNDRY_LOCAL_ALIAS` - Modelalias der skal bruges (standard varierer efter eksempel)
- `FOUNDRY_LOCAL_ENDPOINT` - Overstyring af service-endpoint (valgfrit)
- `SHOW_USAGE` - Vis statistik for tokenforbrug (standard: "0")
- `RETRY_ON_FAIL` - Aktivér retry-logik (standard: "1")
- `RETRY_BACKOFF` - Initial retry-forsinkelse i sekunder (standard: "1.0")

### Eksempelspecifik
- `EMBED_MODEL` - Embedding-model for RAG-eksempler
- `BENCH_MODELS` - Kommaseparerede modeller til benchmarking
- `BENCH_ROUNDS` - Antal benchmark-runder
- `BENCH_PROMPT` - Testprompt til benchmarks
- `BENCH_STREAM` - Mål første-token latenstid
- `RAG_QUESTION` - Testspørgsmål til RAG-eksempler
- `AGENT_MODEL_PRIMARY` - Primær agentmodel
- `AGENT_MODEL_EDITOR` - Editor agentmodel
- `SLM_ALIAS` - Alias for lille sprogmodel
- `LLM_ALIAS` - Alias for stor sprogmodel

## Implementerede bedste praksis for SDK

### 1. Korrekt klientinitialisering
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Modelinfo-hentning
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Fejlhåndtering
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Retry-logik med eksponentiel backoff
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Streaming-support
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Migrationsvejledning for brugerdefinerede eksempler

Hvis du opretter nye eksempler eller opdaterer eksisterende:

1. **Brug `workshop_utils.py`-hjælpemidler**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Understøt endpoint-override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Tilføj omfattende dokumentation**:
   - Miljøvariabler i docstring
   - SDK-referencelink
   - Brugs-eksempler

4. **Brug type hints**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementer korrekt fejlhåndtering**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testning

Alle eksempler kan testes med:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK Dokumentationsreferencer

- **Hovedrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokumentation**: Se SDK-repository for seneste API-dokumentation

## Brudte ændringer

### Ingen forventet
Alle ændringer er bagudkompatible. Opdateringerne fokuserer primært på:
- Tilføjelse af nye valgfrie funktioner (endpoint-override)
- Forbedret fejlhåndtering
- Forbedret dokumentation
- Opdatering af standardmodelnavne til aktuelle anbefalinger

### Valgfrie forbedringer
Du kan opdatere din kode til at bruge:
- `FOUNDRY_LOCAL_ENDPOINT` for eksplicit endpoint-kontrol
- `SHOW_USAGE=1` for synlighed af tokenforbrug
- Opdaterede modelstandarder (`phi-4-mini` i stedet for `phi-3.5-mini`)

## Almindelige problemer og løsninger

### Problem: "Klientinitialisering mislykkedes"
**Løsning**: Sørg for, at Foundry Local-tjenesten kører:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problem: "Model ikke fundet"
**Løsning**: Tjek tilgængelige modeller:
```bash
foundry model list
```

### Problem: Fejl ved endpoint-forbindelse
**Løsning**: Bekræft endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Næste skridt

1. **Opdater Module08-eksempler**: Anvend lignende mønstre på Module08/samples
2. **Tilføj integrationstests**: Opret omfattende test-suite
3. **Performance benchmarking**: Sammenlign før/efter performance
4. **Dokumentationsopdateringer**: Opdater hoved-README med nye mønstre

## Retningslinjer for bidrag

Når du tilføjer nye eksempler:
1. Brug `workshop_utils.py` for konsistens
2. Følg mønsteret i eksisterende eksempler
3. Tilføj omfattende docstrings
4. Inkluder SDK-referencelinks
5. Understøt endpoint-override
6. Tilføj korrekte type hints
7. Inkluder brugs-eksempler i docstring

## Versionskompatibilitet

Disse opdateringer er kompatible med:
- `foundry-local-sdk` (seneste)
- `openai>=1.30.0`
- Python 3.8+

---

**Sidst opdateret**: 2025-01-08  
**Vedligeholder**: EdgeAI Workshop Team  
**SDK Version**: Foundry Local SDK (seneste 0.7.117+67073234e7)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.