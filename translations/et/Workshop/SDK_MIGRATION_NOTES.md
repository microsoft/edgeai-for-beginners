<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-29T00:01:42+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "et"
}
-->
# Foundry Local SDK-i migreerimise märkmed

## Ülevaade

Kõik Python-failid Workshop kaustas on uuendatud, et järgida uusimaid mustreid ametlikust [Foundry Local Python SDK-st](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Muudatuste kokkuvõte

### Põhiinfrastruktuur (`workshop_utils.py`)

#### Täiustatud funktsioonid:
- **Lõpp-punkti ülekirjutamise tugi**: Lisatud `FOUNDRY_LOCAL_ENDPOINT` keskkonnamuutuja tugi
- **Parendatud veakäsitlus**: Parem erandite käsitlus koos üksikasjalike veateadetega
- **Täiustatud vahemälu**: Vahemälu võtmed sisaldavad nüüd lõpp-punkti mitme lõpp-punkti stsenaariumide jaoks
- **Eksponentsiaalne tagasipõrge**: Kordusloogika kasutab nüüd eksponentsiaalset tagasipõrget usaldusväärsuse parandamiseks
- **Tüüpannotatsioonid**: Lisatud ulatuslikud tüüpviited parema IDE toe jaoks

#### Uued võimalused:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Näidisrakendused

#### Sessioon 01: Vestluse alglaadimine (`chat_bootstrap.py`)
- Vaikemudel uuendatud `phi-3.5-mini` pealt `phi-4-mini` peale
- Lisatud lõpp-punkti ülekirjutamise tugi
- Täiustatud dokumentatsioon SDK viidetega

#### Sessioon 02: RAG torujuhe (`rag_pipeline.py`)
- Uuendatud kasutama `phi-4-mini` vaikemudelina
- Lisatud lõpp-punkti ülekirjutamise tugi
- Täiustatud dokumentatsioon keskkonnamuutujate detailidega

#### Sessioon 02: RAG hindamine (`rag_eval_ragas.py`)
- Uuendatud mudeli vaikeseaded
- Lisatud lõpp-punkti konfiguratsioon
- Täiustatud veakäsitlus

#### Sessioon 03: Võrdlusuuringud (`benchmark_oss_models.py`)
- Uuendatud vaikemudelite loend, lisatud `phi-4-mini`
- Lisatud ulatuslik keskkonnamuutujate dokumentatsioon
- Täiustatud funktsioonide dokumentatsioon
- Lisatud lõpp-punkti ülekirjutamise tugi kogu ulatuses

#### Sessioon 04: Mudelite võrdlus (`model_compare.py`)
- Vaikimisi LLM uuendatud `gpt-oss-20b` pealt `qwen2.5-7b` peale
- Lisatud lõpp-punkti konfiguratsioon
- Täiustatud dokumentatsioon

#### Sessioon 05: Multi-agent orkestreerimine (`agents_orchestrator.py`)
- Lisatud tüüpviited (muudetud `str | None` `Optional[str]` peale)
- Täiustatud Agent klassi dokumentatsioon
- Lisatud lõpp-punkti ülekirjutamise tugi
- Täiustatud algatamise muster

#### Sessioon 06: Mudelite suunaja (`models_router.py`)
- Lisatud lõpp-punkti konfiguratsioon
- Täiustatud kavatsuste tuvastamise dokumentatsioon
- Täiustatud suunamisloogika dokumentatsioon

#### Sessioon 06: Torujuhe (`models_pipeline.py`)
- Lisatud ulatuslik funktsioonide dokumentatsioon
- Täiustatud samm-sammult dokumentatsioon
- Täiustatud veakäsitlus

### Skriptid

#### Võrdlusuuringu eksport (`export_benchmark_markdown.py`)
- Lisatud lõpp-punkti ülekirjutamise tugi
- Uuendatud vaikemudelid
- Täiustatud funktsioonide dokumentatsioon
- Täiustatud veakäsitlus

#### CLI linter (`lint_markdown_cli.py`)
- Lisatud SDK viite lingid
- Täiustatud kasutusdokumentatsioon

### Testid

#### Suitsu testid (`smoke.py`)
- Lisatud lõpp-punkti ülekirjutamise tugi
- Täiustatud dokumentatsioon
- Täiustatud testjuhtumite dokumentatsioon
- Parem veateadete esitamine

## Keskkonnamuutujad

Kõik näidised toetavad nüüd järgmisi keskkonnamuutujaid:

### Põhikonfiguratsioon
- `FOUNDRY_LOCAL_ALIAS` - Mudeli alias, mida kasutada (vaikeseade sõltub näidisest)
- `FOUNDRY_LOCAL_ENDPOINT` - Teenuse lõpp-punkti ülekirjutamine (valikuline)
- `SHOW_USAGE` - Näita tokeni kasutusstatistikat (vaikimisi: "0")
- `RETRY_ON_FAIL` - Luba kordusloogika (vaikimisi: "1")
- `RETRY_BACKOFF` - Esialgne kordusviivitus sekundites (vaikimisi: "1.0")

### Näidise-spetsiifiline
- `EMBED_MODEL` - RAG-näidiste jaoks mõeldud sisumudeli alias
- `BENCH_MODELS` - Komaga eraldatud mudelid võrdlusuuringuteks
- `BENCH_ROUNDS` - Võrdlusuuringu voorude arv
- `BENCH_PROMPT` - Testi küsimus võrdlusuuringuteks
- `BENCH_STREAM` - Esimese tokeni latentsuse mõõtmine
- `RAG_QUESTION` - Testi küsimus RAG-näidiste jaoks
- `AGENT_MODEL_PRIMARY` - Peamine agent mudel
- `AGENT_MODEL_EDITOR` - Toimetaja agent mudel
- `SLM_ALIAS` - Väikese keelemudeli alias
- `LLM_ALIAS` - Suure keelemudeli alias

## Rakendatud SDK parimad praktikad

### 1. Kliendi korrektne algatamine
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

### 2. Mudeli info päring
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Veakäsitlus
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Kordusloogika eksponentsiaalse tagasipõrkega
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

### 5. Voogedastuse tugi
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

## Migreerimisjuhend kohandatud näidiste jaoks

Kui loote uusi näidiseid või uuendate olemasolevaid:

1. **Kasutage `workshop_utils.py` abivahendeid**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Toetage lõpp-punkti ülekirjutamist**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Lisage ulatuslik dokumentatsioon**:
   - Keskkonnamuutujad dokumendi kommentaarides
   - SDK viite link
   - Kasutusnäited

4. **Kasutage tüüpviiteid**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Rakendage korrektne veakäsitlus**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testimine

Kõiki näidiseid saab testida järgmiselt:

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

## SDK dokumentatsiooni viited

- **Peamine repositoorium**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentatsioon**: Vaadake SDK repositooriumi uusimate API dokumentide jaoks

## Muutused, mis võivad funktsionaalsust mõjutada

### Ei ole oodata
Kõik muudatused on tagasiühilduvad. Uuendused peamiselt:
- Lisavad uusi valikulisi funktsioone (lõpp-punkti ülekirjutamine)
- Parendavad veakäsitlust
- Täiustavad dokumentatsiooni
- Uuendavad vaikemudelite nimesid vastavalt praegustele soovitustele

### Valikulised täiustused
Võite oma koodi uuendada, et kasutada:
- `FOUNDRY_LOCAL_ENDPOINT` lõpp-punkti kontrollimiseks
- `SHOW_USAGE=1` tokeni kasutuse nähtavuse jaoks
- Uuendatud mudeli vaikeseaded (`phi-4-mini` asemel `phi-3.5-mini`)

## Levinud probleemid ja lahendused

### Probleem: "Kliendi algatamine ebaõnnestus"
**Lahendus**: Veenduge, et Foundry Local teenus töötab:
```bash
foundry service start
foundry model run phi-4-mini
```

### Probleem: "Mudel ei leitud"
**Lahendus**: Kontrollige saadaolevaid mudeleid:
```bash
foundry model list
```

### Probleem: Lõpp-punkti ühenduse vead
**Lahendus**: Kontrollige lõpp-punkti:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Järgmised sammud

1. **Uuendage Module08 näidiseid**: Rakendage sarnaseid mustreid Module08/samples kaustas
2. **Lisage integratsioonitestid**: Looge ulatuslik testikomplekt
3. **Jõudluse võrdlusuuringud**: Võrrelge enne/pärast jõudlust
4. **Dokumentatsiooni uuendused**: Uuendage peamist README-d uute mustritega

## Kaastöö juhised

Uute näidiste lisamisel:
1. Kasutage `workshop_utils.py` järjepidevuse tagamiseks
2. Järgige olemasolevate näidiste mustrit
3. Lisage ulatuslikud dokumendikommentaarid
4. Lisage SDK viite lingid
5. Toetage lõpp-punkti ülekirjutamist
6. Lisage korrektsed tüüpviited
7. Lisage kasutusnäited dokumendikommentaarides

## Versiooni ühilduvus

Need uuendused on ühilduvad:
- `foundry-local-sdk` (viimane)
- `openai>=1.30.0`
- Python 3.8+

---

**Viimati uuendatud**: 2025-01-08  
**Hooldaja**: EdgeAI Workshop Team  
**SDK versioon**: Foundry Local SDK (viimane 0.7.117+67073234e7)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.