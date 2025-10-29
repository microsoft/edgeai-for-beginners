<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:58:23+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "hu"
}
-->
# Workshop Minták - Foundry Local SDK Frissítési Összefoglaló

## Áttekintés

A `Workshop/samples` könyvtárban található összes Python minta frissítve lett, hogy kövesse a Foundry Local SDK legjobb gyakorlatait, és biztosítsa az egységességet a workshop során.

**Dátum**: 2025. október 8.  
**Hatókör**: 9 Python fájl 6 workshop szekcióban  
**Fő fókusz**: Hibakezelés, dokumentáció, SDK minták, felhasználói élmény

---

## Frissített fájlok

### 01. szekció: Első lépések
- ✅ `chat_bootstrap.py` - Alapvető chat és streaming példák

### 02. szekció: RAG Megoldások
- ✅ `rag_pipeline.py` - RAG megvalósítás beágyazásokkal
- ✅ `rag_eval_ragas.py` - RAG értékelés RAGAS metrikákkal

### 03. szekció: Nyílt Forráskódú Modellek
- ✅ `benchmark_oss_models.py` - Több modell összehasonlítása

### 04. szekció: Legújabb Modellek
- ✅ `model_compare.py` - SLM és LLM összehasonlítása

### 05. szekció: AI-Alapú Ügynökök
- ✅ `agents_orchestrator.py` - Több ügynök koordinációja

### 06. szekció: Modellek Eszközként
- ✅ `models_router.py` - Szándék-alapú modellirányítás
- ✅ `models_pipeline.py` - Többlépcsős irányított folyamat

### Támogató infrastruktúra
- ✅ `workshop_utils.py` - Már követi a legjobb gyakorlatokat (nincs szükség változtatásra)

---

## Főbb fejlesztések

### 1. Fejlettebb Hibakezelés

**Korábban:**
```python
manager, client, model_id = get_client(alias)
```

**Utána:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Előnyök:**
- Kifinomult hibakezelés egyértelmű hibaüzenetekkel
- Cselekvésre ösztönző hibaelhárítási tippek
- Megfelelő kilépési kódok szkriptekhez

### 2. Jobb Importkezelés

**Korábban:**
```python
from sentence_transformers import SentenceTransformer
```

**Utána:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Előnyök:**
- Egyértelmű útmutatás hiányzó függőségek esetén
- Rejtélyes import hibák elkerülése
- Felhasználóbarát telepítési utasítások

### 3. Átfogó Dokumentáció

**Minden mintához hozzáadva:**
- Környezeti változók dokumentációja docstringekben
- SDK referencia linkek
- Használati példák
- Részletes függvény/paraméter dokumentáció
- Típusjelölések a jobb IDE támogatás érdekében

**Példa:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Javított Felhasználói Visszajelzés

**Információs naplózás hozzáadva:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Haladásjelzők:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturált kimenet:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robusztus Összehasonlítás

**03. szekció fejlesztései:**
- Modellenkénti hibakezelés (folytatás hiba esetén)
- Részletes haladásjelentés
- Bemelegítő körök megfelelő végrehajtása
- Első token késleltetés mérésének támogatása
- Szakaszok egyértelmű szétválasztása

### 6. Egységes Típusjelölések

**Mindenhol hozzáadva:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Előnyök:**
- Jobb IDE automatikus kiegészítés
- Korai hibadetektálás
- Öndokumentáló kód

### 7. Fejlesztett Modellirányító

**06. szekció fejlesztései:**
- Átfogó szándékfelismerési dokumentáció
- Modellválasztási algoritmus magyarázata
- Részletes irányítási naplók
- Tesztkimenet formázása
- Hibahelyreállítás csoportos tesztelés során

### 8. Több Ügynök Orkesztrációja

**05. szekció fejlesztései:**
- Szakaszról szakaszra haladásjelentés
- Ügynökönkénti hibakezelés
- Egyértelmű folyamatstruktúra
- Jobb memória-kezelési dokumentáció

---

## Tesztelési Ellenőrzőlista

### Előfeltételek
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Minden Minta Tesztelése

#### 01. szekció
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### 02. szekció
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### 03. szekció
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### 04. szekció
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### 05. szekció
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### 06. szekció
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Környezeti Változók Referenciája

### Globális (Minden Minta)
| Változó | Leírás | Alapértelmezett |
|---------|--------|-----------------|
| `FOUNDRY_LOCAL_ALIAS` | Használt modell alias | Mintánként változó |
| `FOUNDRY_LOCAL_ENDPOINT` | Szolgáltatási végpont felülírása | Automatikusan észlelt |
| `SHOW_USAGE` | Tokenhasználat megjelenítése | `0` |
| `RETRY_ON_FAIL` | Újrapróbálkozási logika engedélyezése | `1` |
| `RETRY_BACKOFF` | Kezdeti újrapróbálkozási késleltetés | `1.0` |

### Minta-specifikus
| Változó | Használja | Leírás |
|---------|-----------|--------|
| `EMBED_MODEL` | 02. szekció | Beágyazási modell neve |
| `RAG_QUESTION` | 02. szekció | Tesztkérdés RAG-hez |
| `BENCH_MODELS` | 03. szekció | Összehasonlítandó modellek vesszővel elválasztva |
| `BENCH_ROUNDS` | 03. szekció | Összehasonlítási körök száma |
| `BENCH_PROMPT` | 03. szekció | Teszt prompt az összehasonlításhoz |
| `BENCH_STREAM` | 03. szekció | Első token késleltetés mérése |
| `SLM_ALIAS` | 04. szekció | Kis nyelvi modell |
| `LLM_ALIAS` | 04. szekció | Nagy nyelvi modell |
| `COMPARE_PROMPT` | 04. szekció | Összehasonlítási teszt prompt |
| `AGENT_MODEL_PRIMARY` | 05. szekció | Elsődleges ügynök modell |
| `AGENT_MODEL_EDITOR` | 05. szekció | Szerkesztő ügynök modell |
| `AGENT_QUESTION` | 05. szekció | Tesztkérdés ügynökökhöz |
| `PIPELINE_TASK` | 06. szekció | Feladat a folyamatban |

---

## Jelentős Változások

**Nincsenek** - Minden változás visszafelé kompatibilis.

A meglévő szkriptek továbbra is működnek. Az új funkciók:
- Opcionális környezeti változók
- Fejlettebb hibaüzenetek (nem törik meg a funkcionalitást)
- További naplózás (elnyomható)
- Jobb típusjelölések (nincs futásidejű hatás)

---

## Bevezetett Legjobb Gyakorlatok

### 1. Mindig Használja a Workshop Utils-t
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Megfelelő Hibakezelési Minta
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Információs Naplózás
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Típusjelölések
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Átfogó Docstringek
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Környezeti Változók Támogatása
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Kifinomult Degradáció
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Gyakori Problémák és Megoldások

### Probléma: Import Hibák
**Megoldás:** Hiányzó függőségek telepítése
```bash
pip install sentence-transformers ragas datasets numpy
```

### Probléma: Kapcsolódási Hibák
**Megoldás:** Győződjön meg róla, hogy a Foundry Local fut
```bash
foundry service status
foundry model run phi-4-mini
```

### Probléma: Modell Nem Található
**Megoldás:** Ellenőrizze az elérhető modelleket
```bash
foundry model ls
foundry model download <alias>
```

### Probléma: Lassú Teljesítmény
**Megoldás:** Használjon kisebb modelleket vagy állítsa be a paramétereket
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Következő Lépések

### 1. Minden Minta Tesztelése
Futtassa végig a fenti tesztelési ellenőrzőlistát, hogy megbizonyosodjon arról, hogy minden minta helyesen működik.

### 2. Dokumentáció Frissítése
- Frissítse a szekció markdown fájlokat új példákkal
- Adjon hozzá hibaelhárítási szekciót a fő README-hez
- Készítsen gyors referencia útmutatót

### 3. Integrációs Tesztek Készítése
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Teljesítmény Összehasonlítások Hozzáadása
Kövesse nyomon a hibakezelési fejlesztésekből származó teljesítményjavulásokat.

### 5. Felhasználói Visszajelzés
Gyűjtsön visszajelzést a workshop résztvevőitől a következőkről:
- Hibaüzenetek egyértelműsége
- Dokumentáció teljessége
- Használhatóság

---

## Források

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Gyors Referencia**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migrációs Jegyzetek**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Fő Tároló**: https://github.com/microsoft/Foundry-Local

---

## Karbantartás

### Új Minták Hozzáadása
Kövesse ezeket a mintákat új minták létrehozásakor:

1. Használja a `workshop_utils`-t az ügyfélkezeléshez
2. Adjon hozzá átfogó hibakezelést
3. Támogassa a környezeti változókat
4. Adjon hozzá típusjelöléseket és docstringeket
5. Biztosítson információs naplózást
6. Adjon hozzá használati példákat a docstringben
7. Linkeljen az SDK dokumentációhoz

### Frissítések Áttekintése
Frissítések áttekintésekor ellenőrizze:
- [ ] Hibakezelés minden I/O műveleten
- [ ] Típusjelölések nyilvános függvényeken
- [ ] Átfogó docstringek
- [ ] Környezeti változók dokumentációja
- [ ] Információs felhasználói visszajelzés
- [ ] SDK referencia linkek
- [ ] Egységes kódstílus

---

**Összefoglaló**: Minden Workshop Python minta mostantól követi a Foundry Local SDK legjobb gyakorlatait, fejlettebb hibakezeléssel, átfogó dokumentációval és javított felhasználói élménnyel. Nincsenek jelentős változások - minden meglévő funkcionalitás megmaradt és továbbfejlesztett.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.