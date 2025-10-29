<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T23:34:02+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "sl"
}
-->
# Opombe o migraciji lokalnega SDK Foundry

## Pregled

Vse datoteke Python v mapi Workshop so bile posodobljene, da sledijo najnovejšim vzorcem uradnega [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Povzetek sprememb

### Osnovna infrastruktura (`workshop_utils.py`)

#### Izboljšane funkcije:
- **Podpora za preglasitev končne točke**: Dodana podpora za okoljsko spremenljivko `FOUNDRY_LOCAL_ENDPOINT`
- **Izboljšano obravnavanje napak**: Boljša obravnava izjem z natančnimi sporočili o napakah
- **Izboljšano predpomnjenje**: Ključi predpomnilnika zdaj vključujejo končno točko za scenarije z več končnimi točkami
- **Eksponentno povratno odštevanje**: Logika ponovnega poskusa zdaj uporablja eksponentno povratno odštevanje za večjo zanesljivost
- **Tipne anotacije**: Dodane obsežne tipne oznake za boljšo podporo IDE

#### Nove zmogljivosti:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Vzorčne aplikacije

#### Seja 01: Zagon klepeta (`chat_bootstrap.py`)
- Posodobljen privzeti model iz `phi-3.5-mini` na `phi-4-mini`
- Dodana podpora za preglasitev končne točke
- Izboljšana dokumentacija s sklici na SDK

#### Seja 02: RAG cevovod (`rag_pipeline.py`)
- Posodobljeno za uporabo `phi-4-mini` kot privzeti model
- Dodana podpora za preglasitev končne točke
- Izboljšana dokumentacija s podrobnostmi o okoljskih spremenljivkah

#### Seja 02: Ocena RAG (`rag_eval_ragas.py`)
- Posodobljeni privzeti modeli
- Dodana konfiguracija končne točke
- Izboljšano obravnavanje napak

#### Seja 03: Primerjava zmogljivosti (`benchmark_oss_models.py`)
- Posodobljen privzeti seznam modelov, vključno z `phi-4-mini`
- Dodana obsežna dokumentacija o okoljskih spremenljivkah
- Izboljšana dokumentacija funkcij
- Dodana podpora za preglasitev končne točke povsod

#### Seja 04: Primerjava modelov (`model_compare.py`)
- Posodobljen privzeti LLM iz `gpt-oss-20b` na `qwen2.5-7b`
- Dodana konfiguracija končne točke
- Izboljšana dokumentacija

#### Seja 05: Orkestracija več agentov (`agents_orchestrator.py`)
- Dodane tipne oznake (spremenjeno `str | None` v `Optional[str]`)
- Izboljšana dokumentacija razreda Agent
- Dodana podpora za preglasitev končne točke
- Izboljšan vzorec inicializacije

#### Seja 06: Usmerjevalnik modelov (`models_router.py`)
- Dodana konfiguracija končne točke
- Izboljšana dokumentacija zaznavanja namena
- Izboljšana dokumentacija logike usmerjanja

#### Seja 06: Cevovod (`models_pipeline.py`)
- Dodana obsežna dokumentacija funkcij
- Izboljšana dokumentacija korak za korakom
- Izboljšano obravnavanje napak

### Skripte

#### Izvoz primerjalnih podatkov (`export_benchmark_markdown.py`)
- Dodana podpora za preglasitev končne točke
- Posodobljeni privzeti modeli
- Izboljšana dokumentacija funkcij
- Izboljšano obravnavanje napak

#### CLI Linter (`lint_markdown_cli.py`)
- Dodani sklici na SDK
- Izboljšana dokumentacija uporabe

### Testi

#### Hitri testi (`smoke.py`)
- Dodana podpora za preglasitev končne točke
- Izboljšana dokumentacija
- Izboljšana dokumentacija testnih primerov
- Boljše poročanje o napakah

## Okoljske spremenljivke

Vsi vzorci zdaj podpirajo te okoljske spremenljivke:

### Osnovna konfiguracija
- `FOUNDRY_LOCAL_ALIAS` - Alias modela za uporabo (privzeto se razlikuje glede na vzorec)
- `FOUNDRY_LOCAL_ENDPOINT` - Preglasitev končne točke storitve (neobvezno)
- `SHOW_USAGE` - Prikaz statistike uporabe žetonov (privzeto: "0")
- `RETRY_ON_FAIL` - Omogoči logiko ponovnega poskusa (privzeto: "1")
- `RETRY_BACKOFF` - Začetna zamuda pri ponovnem poskusu v sekundah (privzeto: "1.0")

### Specifično za vzorce
- `EMBED_MODEL` - Model vdelave za vzorce RAG
- `BENCH_MODELS` - Seznam modelov, ločen z vejicami, za primerjavo zmogljivosti
- `BENCH_ROUNDS` - Število krogov primerjave zmogljivosti
- `BENCH_PROMPT` - Testni poziv za primerjave zmogljivosti
- `BENCH_STREAM` - Merjenje zakasnitve prvega žetona
- `RAG_QUESTION` - Testno vprašanje za vzorce RAG
- `AGENT_MODEL_PRIMARY` - Primarni model agenta
- `AGENT_MODEL_EDITOR` - Model agenta urednika
- `SLM_ALIAS` - Alias majhnega jezikovnega modela
- `LLM_ALIAS` - Alias velikega jezikovnega modela

## Uveljavljene najboljše prakse SDK

### 1. Pravilna inicializacija odjemalca
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

### 2. Pridobivanje informacij o modelu
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Obravnavanje napak
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logika ponovnega poskusa z eksponentnim povratnim odštevanjem
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

### 5. Podpora za pretakanje
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

## Vodnik za migracijo za prilagojene vzorce

Če ustvarjate nove vzorce ali posodabljate obstoječe:

1. **Uporabite pripomočke `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Podprite preglasitev končne točke**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Dodajte obsežno dokumentacijo**:
   - Okoljske spremenljivke v docstring
   - Sklic na SDK
   - Primeri uporabe

4. **Uporabite tipne oznake**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Uvedite pravilno obravnavanje napak**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testiranje

Vse vzorce je mogoče testirati z:

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

## Sklici na dokumentacijo SDK

- **Glavno skladišče**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentacija**: Preverite skladišče SDK za najnovejšo dokumentacijo API

## Prelomne spremembe

### Ni pričakovano
Vse spremembe so združljive nazaj. Posodobitve predvsem:
- Dodajajo nove neobvezne funkcije (preglasitev končne točke)
- Izboljšujejo obravnavanje napak
- Izboljšujejo dokumentacijo
- Posodabljajo privzeta imena modelov na trenutna priporočila

### Neobvezne izboljšave
Morda boste želeli posodobiti svojo kodo za uporabo:
- `FOUNDRY_LOCAL_ENDPOINT` za eksplicitno upravljanje končne točke
- `SHOW_USAGE=1` za vidnost uporabe žetonov
- Posodobljene privzete modele (`phi-4-mini` namesto `phi-3.5-mini`)

## Pogoste težave in rešitve

### Težava: "Inicializacija odjemalca ni uspela"
**Rešitev**: Prepričajte se, da storitev Foundry Local deluje:
```bash
foundry service start
foundry model run phi-4-mini
```

### Težava: "Model ni najden"
**Rešitev**: Preverite razpoložljive modele:
```bash
foundry model list
```

### Težava: Napake pri povezovanju s končno točko
**Rešitev**: Preverite končno točko:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Naslednji koraki

1. **Posodobite vzorce Module08**: Uporabite podobne vzorce za Module08/samples
2. **Dodajte integracijske teste**: Ustvarite obsežen testni paket
3. **Primerjava zmogljivosti**: Primerjajte zmogljivost pred/po posodobitvi
4. **Posodobitve dokumentacije**: Posodobite glavni README z novimi vzorci

## Smernice za prispevanje

Pri dodajanju novih vzorcev:
1. Uporabite `workshop_utils.py` za doslednost
2. Sledite vzorcu obstoječih vzorcev
3. Dodajte obsežne docstringe
4. Vključite sklice na SDK
5. Podprite preglasitev končne točke
6. Dodajte ustrezne tipne oznake
7. Vključite primere uporabe v docstring

## Združljivost različic

Te posodobitve so združljive z:
- `foundry-local-sdk` (najnovejša)
- `openai>=1.30.0`
- Python 3.8+

---

**Zadnja posodobitev**: 8. januar 2025  
**Vzdrževalec**: Ekipa EdgeAI Workshop  
**Različica SDK**: Foundry Local SDK (najnovejša 0.7.117+67073234e7)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.