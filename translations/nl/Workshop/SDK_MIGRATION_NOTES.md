<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:25:37+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "nl"
}
-->
# Foundry Local SDK Migratienotities

## Overzicht

Alle Python-bestanden in de Workshop-map zijn bijgewerkt om de nieuwste patronen van de officiële [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) te volgen.

## Samenvatting van wijzigingen

### Kerninfrastructuur (`workshop_utils.py`)

#### Verbeterde functies:
- **Ondersteuning voor Endpoint Override**: Toegevoegd ondersteuning voor de omgevingsvariabele `FOUNDRY_LOCAL_ENDPOINT`
- **Verbeterde foutafhandeling**: Betere uitzonderingafhandeling met gedetailleerde foutmeldingen
- **Verbeterde caching**: Cache-sleutels bevatten nu de endpoint voor scenario's met meerdere endpoints
- **Exponentiële Backoff**: Retry-logica maakt nu gebruik van exponentiële backoff voor betere betrouwbaarheid
- **Typeannotaties**: Uitgebreide type hints toegevoegd voor betere ondersteuning in IDE's

#### Nieuwe mogelijkheden:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Voorbeeldtoepassingen

#### Sessie 01: Chat Bootstrap (`chat_bootstrap.py`)
- Standaardmodel bijgewerkt van `phi-3.5-mini` naar `phi-4-mini`
- Toegevoegd ondersteuning voor endpoint override
- Documentatie verbeterd met SDK-referenties

#### Sessie 02: RAG Pipeline (`rag_pipeline.py`)
- Bijgewerkt om `phi-4-mini` als standaard te gebruiken
- Toegevoegd ondersteuning voor endpoint override
- Documentatie verbeterd met details over omgevingsvariabelen

#### Sessie 02: RAG Evaluatie (`rag_eval_ragas.py`)
- Standaardmodellen bijgewerkt
- Endpointconfiguratie toegevoegd
- Foutafhandeling verbeterd

#### Sessie 03: Benchmarking (`benchmark_oss_models.py`)
- Standaardmodellijst bijgewerkt om `phi-4-mini` op te nemen
- Uitgebreide documentatie over omgevingsvariabelen toegevoegd
- Functiedocumentatie verbeterd
- Endpoint override ondersteuning toegevoegd

#### Sessie 04: Modelvergelijking (`model_compare.py`)
- Standaard LLM bijgewerkt van `gpt-oss-20b` naar `qwen2.5-7b`
- Endpointconfiguratie toegevoegd
- Documentatie verbeterd

#### Sessie 05: Multi-Agent Orchestratie (`agents_orchestrator.py`)
- Type hints toegevoegd (veranderd van `str | None` naar `Optional[str]`)
- Documentatie van de Agent-klasse verbeterd
- Endpoint override ondersteuning toegevoegd
- Verbeterd initialisatiepatroon

#### Sessie 06: Modelrouter (`models_router.py`)
- Endpointconfiguratie toegevoegd
- Documentatie over intentdetectie verbeterd
- Documentatie over routeringslogica verbeterd

#### Sessie 06: Pipeline (`models_pipeline.py`)
- Uitgebreide functiedocumentatie toegevoegd
- Stapsgewijze documentatie verbeterd
- Foutafhandeling verbeterd

### Scripts

#### Benchmark Export (`export_benchmark_markdown.py`)
- Endpoint override ondersteuning toegevoegd
- Standaardmodellen bijgewerkt
- Functiedocumentatie verbeterd
- Foutafhandeling verbeterd

#### CLI Linter (`lint_markdown_cli.py`)
- SDK-referentielinks toegevoegd
- Gebruiksdocumentatie verbeterd

### Tests

#### Smoke Tests (`smoke.py`)
- Endpoint override ondersteuning toegevoegd
- Documentatie verbeterd
- Testcase-documentatie verbeterd
- Betere foutrapportage

## Omgevingsvariabelen

Alle voorbeelden ondersteunen nu deze omgevingsvariabelen:

### Kernconfiguratie
- `FOUNDRY_LOCAL_ALIAS` - Modelalias om te gebruiken (standaard verschilt per voorbeeld)
- `FOUNDRY_LOCAL_ENDPOINT` - Service-endpoint overschrijven (optioneel)
- `SHOW_USAGE` - Statistieken over tokengebruik weergeven (standaard: "0")
- `RETRY_ON_FAIL` - Retry-logica inschakelen (standaard: "1")
- `RETRY_BACKOFF` - Initiële retry-vertraging in seconden (standaard: "1.0")

### Specifiek voor voorbeelden
- `EMBED_MODEL` - Embeddingmodel voor RAG-voorbeelden
- `BENCH_MODELS` - Komma-gescheiden modellen voor benchmarking
- `BENCH_ROUNDS` - Aantal benchmarkrondes
- `BENCH_PROMPT` - Testprompt voor benchmarks
- `BENCH_STREAM` - Latentie van eerste token meten
- `RAG_QUESTION` - Testvraag voor RAG-voorbeelden
- `AGENT_MODEL_PRIMARY` - Primair agentmodel
- `AGENT_MODEL_EDITOR` - Editor-agentmodel
- `SLM_ALIAS` - Alias voor klein taalmodel
- `LLM_ALIAS` - Alias voor groot taalmodel

## Geïmplementeerde SDK Best Practices

### 1. Correcte Client Initialisatie
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

### 2. Modelinformatie ophalen
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Foutafhandeling
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Retry-logica met exponentiële backoff
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

### 5. Ondersteuning voor streaming
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

## Migratiehandleiding voor aangepaste voorbeelden

Als je nieuwe voorbeelden maakt of bestaande bijwerkt:

1. **Gebruik `workshop_utils.py` helpers**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Ondersteuning voor endpoint override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Voeg uitgebreide documentatie toe**:
   - Omgevingsvariabelen in docstring
   - SDK-referentielink
   - Gebruik voorbeelden

4. **Gebruik type hints**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementeer correcte foutafhandeling**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testen

Alle voorbeelden kunnen worden getest met:

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

## SDK Documentatiereferenties

- **Hoofdrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Documentatie**: Bekijk de SDK-repository voor de nieuwste API-documentatie

## Breaking Changes

### Geen verwacht
Alle wijzigingen zijn achterwaarts compatibel. De updates voegen voornamelijk toe:
- Nieuwe optionele functies (endpoint override)
- Verbeterde foutafhandeling
- Verbeterde documentatie
- Bijgewerkte standaardmodelnamen volgens huidige aanbevelingen

### Optionele verbeteringen
Je kunt je code bijwerken om gebruik te maken van:
- `FOUNDRY_LOCAL_ENDPOINT` voor expliciete endpointcontrole
- `SHOW_USAGE=1` voor zichtbaarheid van tokengebruik
- Bijgewerkte standaardmodellen (`phi-4-mini` in plaats van `phi-3.5-mini`)

## Veelvoorkomende problemen & oplossingen

### Probleem: "Client initialisatie mislukt"
**Oplossing**: Zorg ervoor dat de Foundry Local-service actief is:
```bash
foundry service start
foundry model run phi-4-mini
```

### Probleem: "Model niet gevonden"
**Oplossing**: Controleer beschikbare modellen:
```bash
foundry model list
```

### Probleem: Endpoint verbindingsfouten
**Oplossing**: Controleer de endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Volgende stappen

1. **Update Module08 voorbeelden**: Pas vergelijkbare patronen toe op Module08/samples
2. **Voeg integratietests toe**: Maak een uitgebreide testset
3. **Prestatiebenchmarking**: Vergelijk prestaties voor en na
4. **Documentatie-updates**: Werk de hoofd-README bij met nieuwe patronen

## Richtlijnen voor bijdragen

Bij het toevoegen van nieuwe voorbeelden:
1. Gebruik `workshop_utils.py` voor consistentie
2. Volg het patroon in bestaande voorbeelden
3. Voeg uitgebreide docstrings toe
4. Voeg SDK-referentielinks toe
5. Ondersteun endpoint override
6. Voeg correcte type hints toe
7. Voeg gebruiksvoorbeelden toe in de docstring

## Versiecompatibiliteit

Deze updates zijn compatibel met:
- `foundry-local-sdk` (laatste versie)
- `openai>=1.30.0`
- Python 3.8+

---

**Laatst bijgewerkt**: 2025-01-08  
**Beheerder**: EdgeAI Workshop Team  
**SDK Versie**: Foundry Local SDK (laatste 0.7.117+67073234e7)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.