<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:07:13+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "sv"
}
-->
# Foundry Local SDK Migreringsanteckningar

## Översikt

Alla Python-filer i Workshop-mappen har uppdaterats för att följa de senaste mönstren från den officiella [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Sammanfattning av ändringar

### Kärninfrastruktur (`workshop_utils.py`)

#### Förbättrade funktioner:
- **Stöd för att åsidosätta endpoint**: Lagt till stöd för miljövariabeln `FOUNDRY_LOCAL_ENDPOINT`
- **Förbättrad felhantering**: Bättre undantagshantering med detaljerade felmeddelanden
- **Förbättrad caching**: Cache-nycklar inkluderar nu endpoint för scenarier med flera endpoints
- **Exponentiell backoff**: Återförsökslogik använder nu exponentiell backoff för bättre tillförlitlighet
- **Typannoteringar**: Lagt till omfattande typmarkeringar för bättre stöd i IDE

#### Nya funktioner:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Exempelapplikationer

#### Session 01: Chat Bootstrap (`chat_bootstrap.py`)
- Uppdaterad standardmodell från `phi-3.5-mini` till `phi-4-mini`
- Lagt till stöd för att åsidosätta endpoint
- Förbättrad dokumentation med SDK-referenser

#### Session 02: RAG Pipeline (`rag_pipeline.py`)
- Uppdaterad för att använda `phi-4-mini` som standard
- Lagt till stöd för att åsidosätta endpoint
- Förbättrad dokumentation med detaljer om miljövariabler

#### Session 02: RAG Utvärdering (`rag_eval_ragas.py`)
- Uppdaterade standardmodeller
- Lagt till endpoint-konfiguration
- Förbättrad felhantering

#### Session 03: Benchmarking (`benchmark_oss_models.py`)
- Uppdaterad standardmodellista för att inkludera `phi-4-mini`
- Lagt till omfattande dokumentation om miljövariabler
- Förbättrad funktionsdokumentation
- Lagt till stöd för att åsidosätta endpoint överallt

#### Session 04: Modelljämförelse (`model_compare.py`)
- Uppdaterad standard-LLM från `gpt-oss-20b` till `qwen2.5-7b`
- Lagt till endpoint-konfiguration
- Förbättrad dokumentation

#### Session 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- Lagt till typmarkeringar (ändrat `str | None` till `Optional[str]`)
- Förbättrad dokumentation för Agent-klassen
- Lagt till stöd för att åsidosätta endpoint
- Förbättrat initialiseringsmönster

#### Session 06: Modellrouter (`models_router.py`)
- Lagt till endpoint-konfiguration
- Förbättrad dokumentation för avsiktsdetektering
- Förbättrad dokumentation för routinglogik

#### Session 06: Pipeline (`models_pipeline.py`)
- Lagt till omfattande funktionsdokumentation
- Förbättrad steg-för-steg-dokumentation
- Förbättrad felhantering

### Skript

#### Benchmark Export (`export_benchmark_markdown.py`)
- Lagt till stöd för att åsidosätta endpoint
- Uppdaterade standardmodeller
- Förbättrad funktionsdokumentation
- Förbättrad felhantering

#### CLI Linter (`lint_markdown_cli.py`)
- Lagt till SDK-referenslänkar
- Förbättrad användningsdokumentation

### Tester

#### Röktester (`smoke.py`)
- Lagt till stöd för att åsidosätta endpoint
- Förbättrad dokumentation
- Förbättrad dokumentation för testfall
- Bättre felrapportering

## Miljövariabler

Alla exempel stöder nu dessa miljövariabler:

### Kärnkonfiguration
- `FOUNDRY_LOCAL_ALIAS` - Modellalias att använda (standard varierar beroende på exempel)
- `FOUNDRY_LOCAL_ENDPOINT` - Åsidosätt tjänstendpoint (valfritt)
- `SHOW_USAGE` - Visa statistik för tokenanvändning (standard: "0")
- `RETRY_ON_FAIL` - Aktivera återförsökslogik (standard: "1")
- `RETRY_BACKOFF` - Initial återförsöksfördröjning i sekunder (standard: "1.0")

### Exempelspecifika
- `EMBED_MODEL` - Inbäddningsmodell för RAG-exempel
- `BENCH_MODELS` - Kommaseparerade modeller för benchmarking
- `BENCH_ROUNDS` - Antal benchmark-rundor
- `BENCH_PROMPT` - Testprompt för benchmarks
- `BENCH_STREAM` - Mäta latens för första token
- `RAG_QUESTION` - Testfråga för RAG-exempel
- `AGENT_MODEL_PRIMARY` - Primär agentmodell
- `AGENT_MODEL_EDITOR` - Redigeringsagentmodell
- `SLM_ALIAS` - Alias för liten språkmodell
- `LLM_ALIAS` - Alias för stor språkmodell

## Implementerade bästa praxis för SDK

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

### 2. Modellinformationshämtning
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Felhantering
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Återförsökslogik med exponentiell backoff
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

### 5. Stöd för streaming
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

## Migreringsguide för anpassade exempel

Om du skapar nya exempel eller uppdaterar befintliga:

1. **Använd hjälpfunktioner från `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Stöd för att åsidosätta endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Lägg till omfattande dokumentation**:
   - Miljövariabler i docstring
   - SDK-referenslänk
   - Användningsexempel

4. **Använd typmarkeringar**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementera korrekt felhantering**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testning

Alla exempel kan testas med:

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

## SDK-dokumentationsreferenser

- **Huvudrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API-dokumentation**: Se SDK-repository för senaste API-dokumentation

## Störande ändringar

### Inga förväntade
Alla ändringar är bakåtkompatibla. Uppdateringarna handlar främst om att:
- Lägga till nya valfria funktioner (åsidosättning av endpoint)
- Förbättra felhantering
- Förbättra dokumentation
- Uppdatera standardmodellnamn till aktuella rekommendationer

### Valfria förbättringar
Du kanske vill uppdatera din kod för att använda:
- `FOUNDRY_LOCAL_ENDPOINT` för explicit endpoint-kontroll
- `SHOW_USAGE=1` för synlighet av tokenanvändning
- Uppdaterade standardmodeller (`phi-4-mini` istället för `phi-3.5-mini`)

## Vanliga problem och lösningar

### Problem: "Klientinitialisering misslyckades"
**Lösning**: Kontrollera att Foundry Local-tjänsten körs:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problem: "Modell hittades inte"
**Lösning**: Kontrollera tillgängliga modeller:
```bash
foundry model list
```

### Problem: Fel vid anslutning till endpoint
**Lösning**: Verifiera endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Nästa steg

1. **Uppdatera Module08-exempel**: Tillämpa liknande mönster på Module08/samples
2. **Lägg till integrationstester**: Skapa omfattande testsvit
3. **Prestandabenchmarking**: Jämför prestanda före/efter
4. **Dokumentationsuppdateringar**: Uppdatera huvud-README med nya mönster

## Riktlinjer för bidrag

När du lägger till nya exempel:
1. Använd `workshop_utils.py` för konsekvens
2. Följ mönstret i befintliga exempel
3. Lägg till omfattande docstrings
4. Inkludera SDK-referenslänkar
5. Stöd för att åsidosätta endpoint
6. Lägg till korrekta typmarkeringar
7. Inkludera användningsexempel i docstring

## Versionskompatibilitet

Dessa uppdateringar är kompatibla med:
- `foundry-local-sdk` (senaste)
- `openai>=1.30.0`
- Python 3.8+

---

**Senast uppdaterad**: 2025-01-08  
**Ansvarig**: EdgeAI Workshop Team  
**SDK-version**: Foundry Local SDK (senaste 0.7.117+67073234e7)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.