<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:58:45+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "hu"
}
-->
# Foundry Local SDK Migrációs Jegyzetek

## Áttekintés

A Workshop mappában található összes Python fájl frissítve lett, hogy kövesse a hivatalos [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) legújabb mintáit.

## Változások összefoglalása

### Alapvető infrastruktúra (`workshop_utils.py`)

#### Fejlesztett funkciók:
- **Végpont felülírás támogatása**: Hozzáadva a `FOUNDRY_LOCAL_ENDPOINT` környezeti változó támogatása
- **Fejlettebb hibakezelés**: Jobb kivételkezelés részletes hibaüzenetekkel
- **Fejlesztett gyorsítótárazás**: A gyorsítótár kulcsai mostantól tartalmazzák a végpontot több végpontú forgatókönyvekhez
- **Exponenciális visszalépés**: Az újrapróbálkozási logika mostantól exponenciális visszalépést használ a megbízhatóság érdekében
- **Típus annotációk**: Átfogó típusjelölések hozzáadva a jobb IDE támogatás érdekében

#### Új képességek:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Példa alkalmazások

#### 01. szekció: Chat Bootstrap (`chat_bootstrap.py`)
- Az alapértelmezett modell frissítve: `phi-3.5-mini` helyett `phi-4-mini`
- Végpont felülírás támogatás hozzáadva
- Dokumentáció bővítése SDK hivatkozásokkal

#### 02. szekció: RAG Pipeline (`rag_pipeline.py`)
- Frissítve, hogy alapértelmezés szerint a `phi-4-mini` modellt használja
- Végpont felülírás támogatás hozzáadva
- Dokumentáció bővítése a környezeti változók részleteivel

#### 02. szekció: RAG Értékelés (`rag_eval_ragas.py`)
- Modell alapértelmezések frissítése
- Végpont konfiguráció hozzáadva
- Fejlettebb hibakezelés

#### 03. szekció: Teljesítménytesztelés (`benchmark_oss_models.py`)
- Az alapértelmezett modell lista frissítése, beleértve a `phi-4-mini` modellt
- Átfogó környezeti változó dokumentáció hozzáadva
- Funkció dokumentáció javítása
- Végpont felülírás támogatás hozzáadva

#### 04. szekció: Modell összehasonlítás (`model_compare.py`)
- Az alapértelmezett LLM frissítése: `gpt-oss-20b` helyett `qwen2.5-7b`
- Végpont konfiguráció hozzáadva
- Dokumentáció bővítése

#### 05. szekció: Többügynökös Orkesztráció (`agents_orchestrator.py`)
- Típusjelölések hozzáadása (a `str | None` módosítva `Optional[str]`-re)
- Az Agent osztály dokumentációjának bővítése
- Végpont felülírás támogatás hozzáadva
- Javított inicializálási minta

#### 06. szekció: Modell Router (`models_router.py`)
- Végpont konfiguráció hozzáadva
- Szándékfelismerés dokumentációjának bővítése
- Javított útválasztási logika dokumentáció

#### 06. szekció: Pipeline (`models_pipeline.py`)
- Átfogó funkció dokumentáció hozzáadva
- Lépésről lépésre dokumentáció javítása
- Fejlettebb hibakezelés

### Szkriptek

#### Teljesítmény Exportálás (`export_benchmark_markdown.py`)
- Végpont felülírás támogatás hozzáadva
- Alapértelmezett modellek frissítése
- Funkció dokumentáció bővítése
- Hibakezelés javítása

#### CLI Linter (`lint_markdown_cli.py`)
- SDK hivatkozások hozzáadása
- Használati dokumentáció javítása

### Tesztek

#### Gyors tesztek (`smoke.py`)
- Végpont felülírás támogatás hozzáadva
- Dokumentáció bővítése
- Tesztesetek dokumentációjának javítása
- Jobb hiba jelentés

## Környezeti változók

Minden példa mostantól támogatja ezeket a környezeti változókat:

### Alapvető konfiguráció
- `FOUNDRY_LOCAL_ALIAS` - Használandó modell alias (alapértelmezés példánként változik)
- `FOUNDRY_LOCAL_ENDPOINT` - Szolgáltatási végpont felülírása (opcionális)
- `SHOW_USAGE` - Tokenhasználati statisztikák megjelenítése (alapértelmezés: "0")
- `RETRY_ON_FAIL` - Újrapróbálkozási logika engedélyezése (alapértelmezés: "1")
- `RETRY_BACKOFF` - Kezdeti újrapróbálkozási késleltetés másodpercben (alapértelmezés: "1.0")

### Példákhoz specifikus
- `EMBED_MODEL` - Beágyazási modell RAG példákhoz
- `BENCH_MODELS` - Teljesítményteszteléshez használt modellek vesszővel elválasztva
- `BENCH_ROUNDS` - Teljesítménytesztelési körök száma
- `BENCH_PROMPT` - Tesztelő kérdés a teljesítménytesztekhez
- `BENCH_STREAM` - Első token késleltetés mérése
- `RAG_QUESTION` - Tesztkérdés RAG példákhoz
- `AGENT_MODEL_PRIMARY` - Elsődleges ügynök modell
- `AGENT_MODEL_EDITOR` - Szerkesztő ügynök modell
- `SLM_ALIAS` - Kis nyelvi modell alias
- `LLM_ALIAS` - Nagy nyelvi modell alias

## Implementált SDK legjobb gyakorlatok

### 1. Helyes kliens inicializálás
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

### 2. Modell információk lekérése
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Hibakezelés
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Újrapróbálkozási logika exponenciális visszalépéssel
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

### 5. Streaming támogatás
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

## Migrációs útmutató egyedi példákhoz

Ha új példákat hoz létre vagy meglévőket frissít:

1. **Használja a `workshop_utils.py` segédeszközeit**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Támogassa a végpont felülírást**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Adjon hozzá átfogó dokumentációt**:
   - Környezeti változók a docstringben
   - SDK hivatkozási link
   - Használati példák

4. **Használjon típusjelöléseket**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Valósítson meg megfelelő hibakezelést**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Tesztelés

Minden példa tesztelhető a következővel:

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

## SDK Dokumentációs Hivatkozások

- **Fő Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokumentáció**: Az SDK repository-ban található legfrissebb API dokumentációt tekintse meg

## Kompatibilitási problémák

### Nem várható
Minden változtatás visszafelé kompatibilis. A frissítések elsősorban:
- Új opcionális funkciókat adnak hozzá (végpont felülírás)
- Javítják a hibakezelést
- Bővítik a dokumentációt
- Frissítik az alapértelmezett modellek neveit az aktuális ajánlások szerint

### Opcionális fejlesztések
Érdemes lehet frissíteni a kódot az alábbiak használatára:
- `FOUNDRY_LOCAL_ENDPOINT` az explicit végpontvezérléshez
- `SHOW_USAGE=1` a tokenhasználat láthatóságához
- Frissített modell alapértelmezések (`phi-4-mini` a `phi-3.5-mini` helyett)

## Gyakori problémák és megoldások

### Probléma: "Kliens inicializálása sikertelen"
**Megoldás**: Győződjön meg róla, hogy a Foundry Local szolgáltatás fut:
```bash
foundry service start
foundry model run phi-4-mini
```

### Probléma: "Modell nem található"
**Megoldás**: Ellenőrizze az elérhető modelleket:
```bash
foundry model list
```

### Probléma: Végpont csatlakozási hibák
**Megoldás**: Ellenőrizze a végpontot:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Következő lépések

1. **Frissítse a Module08 példákat**: Alkalmazza a hasonló mintákat a Module08/samples mappában
2. **Adjon hozzá integrációs teszteket**: Hozzon létre átfogó tesztkészletet
3. **Teljesítménytesztelés**: Hasonlítsa össze a frissítés előtti és utáni teljesítményt
4. **Dokumentáció frissítések**: Frissítse a fő README fájlt az új mintákkal

## Hozzájárulási irányelvek

Új példák hozzáadásakor:
1. Használja a `workshop_utils.py`-t a konzisztencia érdekében
2. Kövesse a meglévő példák mintáját
3. Adjon hozzá átfogó docstringeket
4. Tartalmazzon SDK hivatkozási linkeket
5. Támogassa a végpont felülírást
6. Adjon hozzá megfelelő típusjelöléseket
7. Tartalmazzon használati példákat a docstringben

## Verziókompatibilitás

Ezek a frissítések kompatibilisek:
- `foundry-local-sdk` (legújabb)
- `openai>=1.30.0`
- Python 3.8+

---

**Utolsó frissítés**: 2025-01-08  
**Karbantartó**: EdgeAI Workshop Team  
**SDK verzió**: Foundry Local SDK (legújabb 0.7.117+67073234e7)

---

**Felelősség kizárása**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.