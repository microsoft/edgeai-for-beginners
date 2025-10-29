<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T23:50:34+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "lt"
}
-->
# Foundry Local SDK Migracijos Pastabos

## Apžvalga

Visi Python failai Workshop aplanke buvo atnaujinti pagal naujausius oficialaus [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) šablonus.

## Pakeitimų Santrauka

### Pagrindinė infrastruktūra (`workshop_utils.py`)

#### Patobulintos funkcijos:
- **Endpoint Override Palaikymas**: Pridėtas `FOUNDRY_LOCAL_ENDPOINT` aplinkos kintamųjų palaikymas
- **Patobulintas Klaidų Tvarkymas**: Geresnis išimčių tvarkymas su išsamiais klaidų pranešimais
- **Patobulintas Kešavimas**: Kešo raktai dabar apima endpoint, skirtą kelių endpoint scenarijams
- **Eksponentinis Atidėjimas**: Pakartojimo logika dabar naudoja eksponentinį atidėjimą, siekiant geresnio patikimumo
- **Tipų Anotacijos**: Pridėtos išsamios tipų užuominos, skirtos geresniam IDE palaikymui

#### Naujos Galimybės:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Pavyzdinės Programos

#### Sesija 01: Chat Bootstrap (`chat_bootstrap.py`)
- Atnaujintas numatytasis modelis iš `phi-3.5-mini` į `phi-4-mini`
- Pridėtas endpoint override palaikymas
- Patobulinta dokumentacija su SDK nuorodomis

#### Sesija 02: RAG Pipeline (`rag_pipeline.py`)
- Atnaujinta, kad naudotų `phi-4-mini` kaip numatytąjį
- Pridėtas endpoint override palaikymas
- Patobulinta dokumentacija su aplinkos kintamųjų detalėmis

#### Sesija 02: RAG Vertinimas (`rag_eval_ragas.py`)
- Atnaujinti modelio numatymai
- Pridėta endpoint konfigūracija
- Patobulintas klaidų tvarkymas

#### Sesija 03: Benchmarking (`benchmark_oss_models.py`)
- Atnaujintas numatytasis modelių sąrašas, įtraukiant `phi-4-mini`
- Pridėta išsami aplinkos kintamųjų dokumentacija
- Patobulinta funkcijų dokumentacija
- Pridėtas endpoint override palaikymas visur

#### Sesija 04: Modelių Palyginimas (`model_compare.py`)
- Atnaujintas numatytasis LLM iš `gpt-oss-20b` į `qwen2.5-7b`
- Pridėta endpoint konfigūracija
- Patobulinta dokumentacija

#### Sesija 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- Pridėtos tipų užuominos (pakeista `str | None` į `Optional[str]`)
- Patobulinta Agent klasės dokumentacija
- Pridėtas endpoint override palaikymas
- Patobulintas inicializacijos šablonas

#### Sesija 06: Modelių Maršrutizatorius (`models_router.py`)
- Pridėta endpoint konfigūracija
- Patobulinta ketinimų aptikimo dokumentacija
- Patobulinta maršrutizavimo logikos dokumentacija

#### Sesija 06: Vamzdynas (`models_pipeline.py`)
- Pridėta išsami funkcijų dokumentacija
- Patobulinta žingsnis po žingsnio dokumentacija
- Patobulintas klaidų tvarkymas

### Skriptai

#### Benchmark Eksportas (`export_benchmark_markdown.py`)
- Pridėtas endpoint override palaikymas
- Atnaujinti numatytieji modeliai
- Patobulinta funkcijų dokumentacija
- Patobulintas klaidų tvarkymas

#### CLI Linteris (`lint_markdown_cli.py`)
- Pridėtos SDK nuorodos
- Patobulinta naudojimo dokumentacija

### Testai

#### Smoke Testai (`smoke.py`)
- Pridėtas endpoint override palaikymas
- Patobulinta dokumentacija
- Patobulinta testų atvejų dokumentacija
- Geresnis klaidų pranešimas

## Aplinkos Kintamieji

Visi pavyzdžiai dabar palaiko šiuos aplinkos kintamuosius:

### Pagrindinė Konfigūracija
- `FOUNDRY_LOCAL_ALIAS` - Modelio alias, kuris bus naudojamas (numatytasis priklauso nuo pavyzdžio)
- `FOUNDRY_LOCAL_ENDPOINT` - Paslaugos endpoint pakeitimas (neprivaloma)
- `SHOW_USAGE` - Rodyti token naudojimo statistiką (numatytasis: "0")
- `RETRY_ON_FAIL` - Įjungti pakartojimo logiką (numatytasis: "1")
- `RETRY_BACKOFF` - Pradinis pakartojimo vėlavimas sekundėmis (numatytasis: "1.0")

### Specifiniai Pavyzdžiams
- `EMBED_MODEL` - Įterpimo modelis RAG pavyzdžiams
- `BENCH_MODELS` - Modeliai, atskirti kableliais, skirti benchmarking
- `BENCH_ROUNDS` - Benchmark raundų skaičius
- `BENCH_PROMPT` - Testo užklausa benchmarking
- `BENCH_STREAM` - Pirmojo token vėlavimo matavimas
- `RAG_QUESTION` - Testo klausimas RAG pavyzdžiams
- `AGENT_MODEL_PRIMARY` - Pirminis agento modelis
- `AGENT_MODEL_EDITOR` - Redaktoriaus agento modelis
- `SLM_ALIAS` - Mažo kalbos modelio alias
- `LLM_ALIAS` - Didelio kalbos modelio alias

## SDK Geriausios Praktikos Įgyvendintos

### 1. Tinkama Kliento Inicializacija
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

### 2. Modelio Informacijos Gavimas
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Klaidų Tvarkymas
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Pakartojimo Logika su Eksponentiniu Atidėjimu
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

### 5. Srautinio Perdavimo Palaikymas
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

## Migracijos Vadovas Individualiems Pavyzdžiams

Jei kuriate naujus pavyzdžius arba atnaujinate esamus:

1. **Naudokite `workshop_utils.py` pagalbininkus**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Palaikykite endpoint override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Pridėkite išsamią dokumentaciją**:
   - Aplinkos kintamuosius docstring
   - SDK nuorodą
   - Naudojimo pavyzdžius

4. **Naudokite tipų užuominas**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Įgyvendinkite tinkamą klaidų tvarkymą**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testavimas

Visi pavyzdžiai gali būti testuojami su:

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

## SDK Dokumentacijos Nuorodos

- **Pagrindinis Repozitorius**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokumentacija**: Žiūrėkite SDK repozitoriją naujausiems API dokumentams

## Kritiniai Pakeitimai

### Nėra Tikėtini
Visi pakeitimai yra suderinami atgal. Atnaujinimai daugiausia:
- Prideda naujas neprivalomas funkcijas (endpoint override)
- Patobulina klaidų tvarkymą
- Pagerina dokumentaciją
- Atnaujina numatytus modelių pavadinimus pagal dabartines rekomendacijas

### Neprivalomi Patobulinimai
Galite atnaujinti savo kodą, kad naudotumėte:
- `FOUNDRY_LOCAL_ENDPOINT` aiškiam endpoint valdymui
- `SHOW_USAGE=1` token naudojimo matomumui
- Atnaujintus modelių numatymus (`phi-4-mini` vietoj `phi-3.5-mini`)

## Dažnos Problemos ir Sprendimai

### Problema: "Kliento inicializacija nepavyko"
**Sprendimas**: Įsitikinkite, kad Foundry Local paslauga veikia:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problema: "Modelis nerastas"
**Sprendimas**: Patikrinkite galimus modelius:
```bash
foundry model list
```

### Problema: Endpoint ryšio klaidos
**Sprendimas**: Patikrinkite endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Tolimesni Žingsniai

1. **Atnaujinkite Module08 pavyzdžius**: Taikykite panašius šablonus Module08/samples
2. **Pridėkite integracijos testus**: Sukurkite išsamų testų rinkinį
3. **Veikimo benchmarking**: Palyginkite veikimą prieš/po
4. **Dokumentacijos atnaujinimai**: Atnaujinkite pagrindinį README su naujais šablonais

## Indėlio Gairės

Pridedant naujus pavyzdžius:
1. Naudokite `workshop_utils.py` nuoseklumui
2. Sekite esamų pavyzdžių šabloną
3. Pridėkite išsamius docstring
4. Įtraukite SDK nuorodas
5. Palaikykite endpoint override
6. Pridėkite tinkamas tipų užuominas
7. Įtraukite naudojimo pavyzdžius į docstring

## Versijų Suderinamumas

Šie atnaujinimai suderinami su:
- `foundry-local-sdk` (naujausia versija)
- `openai>=1.30.0`
- Python 3.8+

---

**Paskutinį kartą atnaujinta**: 2025-01-08  
**Prižiūrėtojas**: EdgeAI Workshop komanda  
**SDK Versija**: Foundry Local SDK (naujausia 0.7.117+67073234e7)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.