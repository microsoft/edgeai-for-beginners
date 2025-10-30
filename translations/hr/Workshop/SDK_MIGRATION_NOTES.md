<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T23:28:57+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "hr"
}
-->
# Bilješke o migraciji lokalnog SDK-a Foundry

## Pregled

Svi Python datoteke u mapi Workshop ažurirane su kako bi slijedile najnovije obrasce iz službenog [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Sažetak promjena

### Osnovna infrastruktura (`workshop_utils.py`)

#### Poboljšane značajke:
- **Podrška za promjenu krajnje točke**: Dodana podrška za varijablu okruženja `FOUNDRY_LOCAL_ENDPOINT`
- **Poboljšano rukovanje greškama**: Bolje rukovanje iznimkama s detaljnim porukama o greškama
- **Poboljšano predmemoriranje**: Ključevi predmemorije sada uključuju krajnju točku za scenarije s više krajnjih točaka
- **Eksponencijalno odgađanje**: Logika ponovnog pokušaja sada koristi eksponencijalno odgađanje za bolju pouzdanost
- **Tipne anotacije**: Dodane sveobuhvatne oznake tipova za bolju podršku u IDE-u

#### Nove mogućnosti:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Primjeri aplikacija

#### Sesija 01: Pokretanje chata (`chat_bootstrap.py`)
- Ažuriran zadani model s `phi-3.5-mini` na `phi-4-mini`
- Dodana podrška za promjenu krajnje točke
- Poboljšana dokumentacija s referencama na SDK

#### Sesija 02: RAG cjevovod (`rag_pipeline.py`)
- Ažurirano za korištenje `phi-4-mini` kao zadanog modela
- Dodana podrška za promjenu krajnje točke
- Poboljšana dokumentacija s detaljima o varijablama okruženja

#### Sesija 02: Procjena RAG-a (`rag_eval_ragas.py`)
- Ažurirani zadani modeli
- Dodana konfiguracija krajnje točke
- Poboljšano rukovanje greškama

#### Sesija 03: Benchmarking (`benchmark_oss_models.py`)
- Ažuriran popis zadanih modela kako bi uključivao `phi-4-mini`
- Dodana sveobuhvatna dokumentacija o varijablama okruženja
- Poboljšana dokumentacija funkcija
- Dodana podrška za promjenu krajnje točke

#### Sesija 04: Usporedba modela (`model_compare.py`)
- Ažuriran zadani LLM s `gpt-oss-20b` na `qwen2.5-7b`
- Dodana konfiguracija krajnje točke
- Poboljšana dokumentacija

#### Sesija 05: Orkestracija više agenata (`agents_orchestrator.py`)
- Dodane oznake tipova (promijenjeno `str | None` u `Optional[str]`)
- Poboljšana dokumentacija klase Agent
- Dodana podrška za promjenu krajnje točke
- Poboljšan obrazac inicijalizacije

#### Sesija 06: Usmjerivač modela (`models_router.py`)
- Dodana konfiguracija krajnje točke
- Poboljšana dokumentacija o detekciji namjere
- Poboljšana dokumentacija logike usmjeravanja

#### Sesija 06: Cjevovod (`models_pipeline.py`)
- Dodana sveobuhvatna dokumentacija funkcija
- Poboljšana dokumentacija korak-po-korak
- Poboljšano rukovanje greškama

### Skripte

#### Izvoz benchmarka (`export_benchmark_markdown.py`)
- Dodana podrška za promjenu krajnje točke
- Ažurirani zadani modeli
- Poboljšana dokumentacija funkcija
- Poboljšano rukovanje greškama

#### CLI Linter (`lint_markdown_cli.py`)
- Dodane poveznice na SDK reference
- Poboljšana dokumentacija o korištenju

### Testovi

#### Testovi dima (`smoke.py`)
- Dodana podrška za promjenu krajnje točke
- Poboljšana dokumentacija
- Poboljšana dokumentacija testnih slučajeva
- Bolje izvještavanje o greškama

## Varijable okruženja

Svi primjeri sada podržavaju ove varijable okruženja:

### Osnovna konfiguracija
- `FOUNDRY_LOCAL_ALIAS` - Alias modela koji se koristi (zadano varira po primjeru)
- `FOUNDRY_LOCAL_ENDPOINT` - Promjena krajnje točke usluge (opcionalno)
- `SHOW_USAGE` - Prikaz statistike korištenja tokena (zadano: "0")
- `RETRY_ON_FAIL` - Omogućavanje logike ponovnog pokušaja (zadano: "1")
- `RETRY_BACKOFF` - Početno kašnjenje ponovnog pokušaja u sekundama (zadano: "1.0")

### Specifično za primjer
- `EMBED_MODEL` - Model za ugrađivanje za RAG primjere
- `BENCH_MODELS` - Modeli odvojeni zarezom za benchmarking
- `BENCH_ROUNDS` - Broj rundi benchmarkinga
- `BENCH_PROMPT` - Testni prompt za benchmarking
- `BENCH_STREAM` - Mjerenje kašnjenja prvog tokena
- `RAG_QUESTION` - Testno pitanje za RAG primjere
- `AGENT_MODEL_PRIMARY` - Primarni model agenta
- `AGENT_MODEL_EDITOR` - Model agenta urednika
- `SLM_ALIAS` - Alias malog jezičnog modela
- `LLM_ALIAS` - Alias velikog jezičnog modela

## Implementirane najbolje prakse za SDK

### 1. Ispravna inicijalizacija klijenta
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

### 2. Dohvaćanje informacija o modelu
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Rukovanje greškama
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logika ponovnog pokušaja s eksponencijalnim odgađanjem
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

### 5. Podrška za streaming
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

## Vodič za migraciju prilagođenih primjera

Ako stvarate nove primjere ili ažurirate postojeće:

1. **Koristite pomoćne funkcije iz `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Podržite promjenu krajnje točke**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Dodajte sveobuhvatnu dokumentaciju**:
   - Varijable okruženja u docstringu
   - Poveznica na SDK reference
   - Primjeri korištenja

4. **Koristite oznake tipova**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementirajte ispravno rukovanje greškama**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testiranje

Svi primjeri mogu se testirati pomoću:

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

## Reference za dokumentaciju SDK-a

- **Glavni repozitorij**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentacija**: Provjerite najnoviju dokumentaciju API-ja u repozitoriju SDK-a

## Prekid kompatibilnosti

### Nisu očekivani
Sve promjene su unatrag kompatibilne. Ažuriranja prvenstveno:
- Dodaju nove opcionalne značajke (promjena krajnje točke)
- Poboljšavaju rukovanje greškama
- Poboljšavaju dokumentaciju
- Ažuriraju zadane nazive modela prema trenutnim preporukama

### Opcionalna poboljšanja
Možda ćete htjeti ažurirati svoj kod kako biste koristili:
- `FOUNDRY_LOCAL_ENDPOINT` za eksplicitnu kontrolu krajnje točke
- `SHOW_USAGE=1` za vidljivost korištenja tokena
- Ažurirane zadane modele (`phi-4-mini` umjesto `phi-3.5-mini`)

## Uobičajeni problemi i rješenja

### Problem: "Inicijalizacija klijenta nije uspjela"
**Rješenje**: Provjerite je li usluga Foundry Local pokrenuta:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problem: "Model nije pronađen"
**Rješenje**: Provjerite dostupne modele:
```bash
foundry model list
```

### Problem: Pogreške povezivanja s krajnjom točkom
**Rješenje**: Provjerite krajnju točku:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Sljedeći koraci

1. **Ažurirajte Module08 primjere**: Primijenite slične obrasce na Module08/samples
2. **Dodajte integracijske testove**: Kreirajte sveobuhvatan testni paket
3. **Benchmarking performansi**: Usporedite performanse prije i poslije
4. **Ažuriranja dokumentacije**: Ažurirajte glavni README s novim obrascima

## Smjernice za doprinos

Kada dodajete nove primjere:
1. Koristite `workshop_utils.py` za dosljednost
2. Slijedite obrazac iz postojećih primjera
3. Dodajte sveobuhvatne docstringove
4. Uključite poveznice na SDK reference
5. Podržite promjenu krajnje točke
6. Dodajte ispravne oznake tipova
7. Uključite primjere korištenja u docstringu

## Kompatibilnost verzija

Ova ažuriranja su kompatibilna s:
- `foundry-local-sdk` (najnovija verzija)
- `openai>=1.30.0`
- Python 3.8+

---

**Posljednje ažuriranje**: 2025-01-08  
**Održavatelj**: EdgeAI Workshop Team  
**Verzija SDK-a**: Foundry Local SDK (najnovija 0.7.117+67073234e7)

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.