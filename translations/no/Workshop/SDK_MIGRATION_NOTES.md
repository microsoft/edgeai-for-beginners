<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:16:01+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "no"
}
-->
# Foundry Local SDK Migreringsnotater

## Oversikt

Alle Python-filer i Workshop-mappen har blitt oppdatert for å følge de nyeste mønstrene fra den offisielle [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Endringsoppsummering

### Kjerneinfrastruktur (`workshop_utils.py`)

#### Forbedrede funksjoner:
- **Støtte for endepunkt-override**: Lagt til støtte for miljøvariabelen `FOUNDRY_LOCAL_ENDPOINT`
- **Forbedret feilhåndtering**: Bedre håndtering av unntak med detaljerte feilmeldinger
- **Forbedret caching**: Cache-nøkler inkluderer nå endepunkt for scenarier med flere endepunkter
- **Eksponentiell tilbakefall**: Retry-logikk bruker nå eksponentiell tilbakefall for bedre pålitelighet
- **Typeannotasjoner**: Lagt til omfattende typehint for bedre støtte i IDE

#### Nye funksjoner:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Eksempelsøknader

#### Sesjon 01: Chat Bootstrap (`chat_bootstrap.py`)
- Oppdatert standardmodell fra `phi-3.5-mini` til `phi-4-mini`
- Lagt til støtte for endepunkt-override
- Forbedret dokumentasjon med SDK-referanser

#### Sesjon 02: RAG Pipeline (`rag_pipeline.py`)
- Oppdatert til å bruke `phi-4-mini` som standard
- Lagt til støtte for endepunkt-override
- Forbedret dokumentasjon med detaljer om miljøvariabler

#### Sesjon 02: RAG Evaluering (`rag_eval_ragas.py`)
- Oppdatert standardmodeller
- Lagt til konfigurasjon for endepunkt
- Forbedret feilhåndtering

#### Sesjon 03: Benchmarking (`benchmark_oss_models.py`)
- Oppdatert standardmodelliste til å inkludere `phi-4-mini`
- Lagt til omfattende dokumentasjon om miljøvariabler
- Forbedret funksjonsdokumentasjon
- Lagt til støtte for endepunkt-override gjennomgående

#### Sesjon 04: Modell-sammenligning (`model_compare.py`)
- Oppdatert standard LLM fra `gpt-oss-20b` til `qwen2.5-7b`
- Lagt til konfigurasjon for endepunkt
- Forbedret dokumentasjon

#### Sesjon 05: Multi-Agent Orkestrering (`agents_orchestrator.py`)
- Lagt til typehint (endret `str | None` til `Optional[str]`)
- Forbedret dokumentasjon for Agent-klassen
- Lagt til støtte for endepunkt-override
- Forbedret initialiseringsmønster

#### Sesjon 06: Modell-router (`models_router.py`)
- Lagt til konfigurasjon for endepunkt
- Forbedret dokumentasjon for intensjonsdeteksjon
- Forbedret dokumentasjon for rutingslogikk

#### Sesjon 06: Pipeline (`models_pipeline.py`)
- Lagt til omfattende funksjonsdokumentasjon
- Forbedret trinn-for-trinn dokumentasjon
- Forbedret feilhåndtering

### Skript

#### Benchmark-eksport (`export_benchmark_markdown.py`)
- Lagt til støtte for endepunkt-override
- Oppdatert standardmodeller
- Forbedret funksjonsdokumentasjon
- Forbedret feilhåndtering

#### CLI Linter (`lint_markdown_cli.py`)
- Lagt til SDK-referanselenker
- Forbedret bruksdokumentasjon

### Tester

#### Røyktester (`smoke.py`)
- Lagt til støtte for endepunkt-override
- Forbedret dokumentasjon
- Forbedret dokumentasjon for testtilfeller
- Bedre feilmeldinger

## Miljøvariabler

Alle eksempler støtter nå disse miljøvariablene:

### Kjernekonfigurasjon
- `FOUNDRY_LOCAL_ALIAS` - Modellalias som skal brukes (standard varierer etter eksempel)
- `FOUNDRY_LOCAL_ENDPOINT` - Overstyr tjenesteendepunkt (valgfritt)
- `SHOW_USAGE` - Vis statistikk for tokenbruk (standard: "0")
- `RETRY_ON_FAIL` - Aktiver retry-logikk (standard: "1")
- `RETRY_BACKOFF` - Startforsinkelse for retry i sekunder (standard: "1.0")

### Eksempelspesifikk
- `EMBED_MODEL` - Innebyggingsmodell for RAG-eksempler
- `BENCH_MODELS` - Kommaseparerte modeller for benchmarking
- `BENCH_ROUNDS` - Antall benchmark-runder
- `BENCH_PROMPT` - Testprompt for benchmarking
- `BENCH_STREAM` - Måling av første-token latens
- `RAG_QUESTION` - Testspørsmål for RAG-eksempler
- `AGENT_MODEL_PRIMARY` - Primær agentmodell
- `AGENT_MODEL_EDITOR` - Redaktør agentmodell
- `SLM_ALIAS` - Alias for liten språkmodell
- `LLM_ALIAS` - Alias for stor språkmodell

## Beste praksis for SDK implementert

### 1. Riktig initialisering av klient
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

### 2. Hente modellinformasjon
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Feilhåndtering
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Retry-logikk med eksponentiell tilbakefall
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

### 5. Støtte for streaming
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

## Migreringsveiledning for egendefinerte eksempler

Hvis du lager nye eksempler eller oppdaterer eksisterende:

1. **Bruk hjelpemidler fra `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Støtt endepunkt-override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Legg til omfattende dokumentasjon**:
   - Miljøvariabler i docstring
   - SDK-referanselenke
   - Brukseksempler

4. **Bruk typehint**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementer riktig feilhåndtering**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testing

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

## SDK-dokumentasjonsreferanser

- **Hovedrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API-dokumentasjon**: Se SDK-repository for siste API-dokumentasjon

## Brudd på kompatibilitet

### Ingen forventet
Alle endringer er bakoverkompatible. Oppdateringene innebærer hovedsakelig:
- Legge til nye valgfrie funksjoner (endepunkt-override)
- Forbedre feilhåndtering
- Forbedre dokumentasjon
- Oppdatere standard modellnavn til gjeldende anbefalinger

### Valgfrie forbedringer
Du kan vurdere å oppdatere koden din til å bruke:
- `FOUNDRY_LOCAL_ENDPOINT` for eksplisitt kontroll over endepunkt
- `SHOW_USAGE=1` for synlighet av tokenbruk
- Oppdaterte standardmodeller (`phi-4-mini` i stedet for `phi-3.5-mini`)

## Vanlige problemer og løsninger

### Problem: "Klientinitialisering mislyktes"
**Løsning**: Sørg for at Foundry Local-tjenesten kjører:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problem: "Modell ikke funnet"
**Løsning**: Sjekk tilgjengelige modeller:
```bash
foundry model list
```

### Problem: Feil med tilkobling til endepunkt
**Løsning**: Verifiser endepunkt:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Neste steg

1. **Oppdater Module08-eksempler**: Bruk lignende mønstre på Module08/samples
2. **Legg til integrasjonstester**: Lag omfattende testpakke
3. **Benchmarking av ytelse**: Sammenlign ytelse før/etter
4. **Oppdater dokumentasjon**: Oppdater hoved-README med nye mønstre

## Retningslinjer for bidrag

Når du legger til nye eksempler:
1. Bruk `workshop_utils.py` for konsistens
2. Følg mønsteret i eksisterende eksempler
3. Legg til omfattende docstrings
4. Inkluder SDK-referanselenker
5. Støtt endepunkt-override
6. Legg til riktige typehint
7. Inkluder brukseksempler i docstring

## Versjonskompatibilitet

Disse oppdateringene er kompatible med:
- `foundry-local-sdk` (siste)
- `openai>=1.30.0`
- Python 3.8+

---

**Sist oppdatert**: 2025-01-08  
**Vedlikeholder**: EdgeAI Workshop Team  
**SDK-versjon**: Foundry Local SDK (siste 0.7.117+67073234e7)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.