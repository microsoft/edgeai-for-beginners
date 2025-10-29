<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T23:13:01+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ro"
}
-->
# Note despre migrarea SDK-ului local Foundry

## Prezentare generală

Toate fișierele Python din folderul Workshop au fost actualizate pentru a respecta cele mai recente modele din [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Rezumatul modificărilor

### Infrastructura de bază (`workshop_utils.py`)

#### Funcționalități îmbunătățite:
- **Suport pentru suprascrierea endpoint-ului**: Adăugat suport pentru variabila de mediu `FOUNDRY_LOCAL_ENDPOINT`
- **Gestionarea erorilor îmbunătățită**: Gestionare mai bună a excepțiilor cu mesaje de eroare detaliate
- **Caching îmbunătățit**: Cheile de cache includ acum endpoint-ul pentru scenarii cu mai multe endpoint-uri
- **Backoff exponențial**: Logica de retry utilizează acum backoff exponențial pentru o fiabilitate mai mare
- **Adnotări de tip**: Adăugate indicații de tip cuprinzătoare pentru suport mai bun în IDE

#### Capabilități noi:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Aplicații exemplu

#### Sesiunea 01: Bootstrap Chat (`chat_bootstrap.py`)
- Modelul implicit actualizat de la `phi-3.5-mini` la `phi-4-mini`
- Adăugat suport pentru suprascrierea endpoint-ului
- Documentație îmbunătățită cu referințe la SDK

#### Sesiunea 02: Pipeline RAG (`rag_pipeline.py`)
- Actualizat pentru a utiliza `phi-4-mini` ca model implicit
- Adăugat suport pentru suprascrierea endpoint-ului
- Documentație îmbunătățită cu detalii despre variabilele de mediu

#### Sesiunea 02: Evaluare RAG (`rag_eval_ragas.py`)
- Actualizate setările implicite ale modelului
- Adăugat configurarea endpoint-ului
- Gestionarea erorilor îmbunătățită

#### Sesiunea 03: Benchmarking (`benchmark_oss_models.py`)
- Lista de modele implicite actualizată pentru a include `phi-4-mini`
- Documentație cuprinzătoare despre variabilele de mediu adăugată
- Documentația funcțiilor îmbunătățită
- Suport pentru suprascrierea endpoint-ului adăugat

#### Sesiunea 04: Compararea modelelor (`model_compare.py`)
- Modelul LLM implicit actualizat de la `gpt-oss-20b` la `qwen2.5-7b`
- Configurarea endpoint-ului adăugată
- Documentație îmbunătățită

#### Sesiunea 05: Orchestrarea multi-agent (`agents_orchestrator.py`)
- Adăugate indicații de tip (modificat `str | None` în `Optional[str]`)
- Documentația clasei Agent îmbunătățită
- Suport pentru suprascrierea endpoint-ului adăugat
- Model de inițializare îmbunătățit

#### Sesiunea 06: Router de modele (`models_router.py`)
- Configurarea endpoint-ului adăugată
- Documentația pentru detectarea intenției îmbunătățită
- Documentația logicii de rutare îmbunătățită

#### Sesiunea 06: Pipeline (`models_pipeline.py`)
- Documentație cuprinzătoare a funcțiilor adăugată
- Documentație pas cu pas îmbunătățită
- Gestionarea erorilor îmbunătățită

### Scripturi

#### Export Benchmark (`export_benchmark_markdown.py`)
- Suport pentru suprascrierea endpoint-ului adăugat
- Modele implicite actualizate
- Documentația funcțiilor îmbunătățită
- Gestionarea erorilor îmbunătățită

#### CLI Linter (`lint_markdown_cli.py`)
- Linkuri de referință la SDK adăugate
- Documentația de utilizare îmbunătățită

### Teste

#### Teste de funcționare (`smoke.py`)
- Suport pentru suprascrierea endpoint-ului adăugat
- Documentație îmbunătățită
- Documentația cazurilor de testare îmbunătățită
- Raportare mai bună a erorilor

## Variabile de mediu

Toate exemplele acceptă acum aceste variabile de mediu:

### Configurare de bază
- `FOUNDRY_LOCAL_ALIAS` - Alias-ul modelului utilizat (implicit variază în funcție de exemplu)
- `FOUNDRY_LOCAL_ENDPOINT` - Suprascrierea endpoint-ului serviciului (opțional)
- `SHOW_USAGE` - Afișează statistici despre utilizarea token-urilor (implicit: "0")
- `RETRY_ON_FAIL` - Activează logica de retry (implicit: "1")
- `RETRY_BACKOFF` - Întârzierea inițială pentru retry în secunde (implicit: "1.0")

### Specific pentru exemple
- `EMBED_MODEL` - Model de încorporare pentru exemplele RAG
- `BENCH_MODELS` - Modele separate prin virgulă pentru benchmarking
- `BENCH_ROUNDS` - Numărul de runde de benchmarking
- `BENCH_PROMPT` - Prompt de test pentru benchmarking
- `BENCH_STREAM` - Măsurarea latenței primului token
- `RAG_QUESTION` - Întrebare de test pentru exemplele RAG
- `AGENT_MODEL_PRIMARY` - Modelul principal al agentului
- `AGENT_MODEL_EDITOR` - Modelul editorului de agent
- `SLM_ALIAS` - Alias-ul modelului de limbaj mic
- `LLM_ALIAS` - Alias-ul modelului de limbaj mare

## Cele mai bune practici SDK implementate

### 1. Inițializarea corectă a clientului
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

### 2. Recuperarea informațiilor despre model
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Gestionarea erorilor
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logica de retry cu backoff exponențial
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

### 5. Suport pentru streaming
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

## Ghid de migrare pentru exemple personalizate

Dacă creați exemple noi sau actualizați pe cele existente:

1. **Utilizați ajutoarele din `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Suportați suprascrierea endpoint-ului**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Adăugați documentație cuprinzătoare**:
   - Variabile de mediu în docstring
   - Link de referință la SDK
   - Exemple de utilizare

4. **Utilizați indicații de tip**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementați gestionarea corectă a erorilor**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testare

Toate exemplele pot fi testate cu:

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

## Referințe de documentație SDK

- **Repository principal**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentație API**: Consultați repository-ul SDK pentru cele mai recente documentații API

## Modificări majore

### Nu se așteaptă modificări
Toate modificările sunt compatibile retroactiv. Actualizările în principal:
- Adaugă funcționalități opționale noi (suprascrierea endpoint-ului)
- Îmbunătățesc gestionarea erorilor
- Îmbunătățesc documentația
- Actualizează numele modelelor implicite conform recomandărilor actuale

### Îmbunătățiri opționale
Este posibil să doriți să vă actualizați codul pentru a utiliza:
- `FOUNDRY_LOCAL_ENDPOINT` pentru control explicit al endpoint-ului
- `SHOW_USAGE=1` pentru vizibilitatea utilizării token-urilor
- Modele implicite actualizate (`phi-4-mini` în loc de `phi-3.5-mini`)

## Probleme comune și soluții

### Problemă: "Inițializarea clientului a eșuat"
**Soluție**: Asigurați-vă că serviciul Foundry Local rulează:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problemă: "Modelul nu a fost găsit"
**Soluție**: Verificați modelele disponibile:
```bash
foundry model list
```

### Problemă: Erori de conexiune la endpoint
**Soluție**: Verificați endpoint-ul:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Pași următori

1. **Actualizați exemplele din Module08**: Aplicați modele similare pentru Module08/samples
2. **Adăugați teste de integrare**: Creați o suită de teste cuprinzătoare
3. **Benchmarking de performanță**: Comparați performanța înainte/după
4. **Actualizări de documentație**: Actualizați README-ul principal cu noile modele

## Ghid de contribuție

Când adăugați exemple noi:
1. Utilizați `workshop_utils.py` pentru consistență
2. Urmați modelul din exemplele existente
3. Adăugați docstring-uri cuprinzătoare
4. Includeți linkuri de referință la SDK
5. Suportați suprascrierea endpoint-ului
6. Adăugați indicații de tip corecte
7. Includeți exemple de utilizare în docstring

## Compatibilitate versiuni

Aceste actualizări sunt compatibile cu:
- `foundry-local-sdk` (cea mai recentă)
- `openai>=1.30.0`
- Python 3.8+

---

**Ultima actualizare**: 2025-01-08  
**Responsabil**: Echipa EdgeAI Workshop  
**Versiune SDK**: Foundry Local SDK (cea mai recentă 0.7.117+67073234e7)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.