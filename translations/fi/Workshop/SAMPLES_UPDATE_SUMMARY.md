<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:20:45+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "fi"
}
-->
# Workshop-näytteet - Foundry Local SDK -päivityksen yhteenveto

## Yleiskatsaus

Kaikki Python-näytteet `Workshop/samples` -hakemistossa on päivitetty noudattamaan Foundry Local SDK:n parhaita käytäntöjä ja varmistamaan johdonmukaisuus koko työpajassa.

**Päivämäärä**: 8. lokakuuta 2025  
**Laajuus**: 9 Python-tiedostoa 6 työpajasessiossa  
**Pääpainopiste**: Virheenkäsittely, dokumentaatio, SDK-mallit, käyttäjäkokemus

---

## Päivitetyt tiedostot

### Sessio 01: Aloittaminen
- ✅ `chat_bootstrap.py` - Peruschat- ja suoratoistoesimerkit

### Sessio 02: RAG-ratkaisut
- ✅ `rag_pipeline.py` - RAG-toteutus upotuksilla
- ✅ `rag_eval_ragas.py` - RAG-arviointi RAGAS-metriikoilla

### Sessio 03: Avoimen lähdekoodin mallit
- ✅ `benchmark_oss_models.py` - Monimallivertailu

### Sessio 04: Huippumallit
- ✅ `model_compare.py` - SLM vs LLM -vertailu

### Sessio 05: AI-pohjaiset agentit
- ✅ `agents_orchestrator.py` - Moniagenttien koordinointi

### Sessio 06: Mallit työkaluina
- ✅ `models_router.py` - Aikomuspohjainen mallien reititys
- ✅ `models_pipeline.py` - Monivaiheinen reititetty putkisto

### Tukirakenne
- ✅ `workshop_utils.py` - Noudattaa jo parhaita käytäntöjä (ei muutoksia tarvittu)

---

## Keskeiset parannukset

### 1. Parannettu virheenkäsittely

**Ennen:**
```python
manager, client, model_id = get_client(alias)
```

**Jälkeen:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Hyödyt:**
- Sulava virheenkäsittely selkeillä virheilmoituksilla
- Toimintakelpoiset vianetsintävinkit
- Asianmukaiset poistumiskoodit skriptauksessa

### 2. Parempi tuontien hallinta

**Ennen:**
```python
from sentence_transformers import SentenceTransformer
```

**Jälkeen:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Hyödyt:**
- Selkeät ohjeet, kun riippuvuudet puuttuvat
- Estää kryptiset tuontivirheet
- Käyttäjäystävälliset asennusohjeet

### 3. Kattava dokumentaatio

**Lisätty kaikkiin näytteisiin:**
- Ympäristömuuttujien dokumentaatio docstringeissä
- SDK-viitelinkit
- Käyttöesimerkit
- Yksityiskohtainen funktio-/parametridokumentaatio
- Tyyppivihjeet paremman IDE-tuen takaamiseksi

**Esimerkki:**
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

### 4. Parannettu käyttäjäpalaute

**Lisätty informatiivinen lokitus:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Edistymisen indikaattorit:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Rakenteellinen tulostus:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Vahva vertailu

**Sessio 03 parannukset:**
- Mallikohtainen virheenkäsittely (jatkuu epäonnistumisen jälkeen)
- Yksityiskohtainen edistymisraportointi
- Lämmittelykierrokset suoritettu asianmukaisesti
- Ensimmäisen tokenin viiveen mittaustuki
- Vaiheiden selkeä erottelu

### 6. Johdonmukaiset tyyppivihjeet

**Lisätty kaikkialle:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Hyödyt:**
- Parempi IDE:n automaattinen täydennys
- Varhainen virheiden havaitseminen
- Itse dokumentoiva koodi

### 7. Parannettu mallien reititys

**Sessio 06 parannukset:**
- Kattava aikomusten tunnistuksen dokumentaatio
- Mallin valinta-algoritmin selitys
- Yksityiskohtaiset reitityslokit
- Testitulosten muotoilu
- Virheiden korjaus erätestauksessa

### 8. Moniagenttien orkestrointi

**Sessio 05 parannukset:**
- Vaiheittainen edistymisraportointi
- Agenttikohtainen virheenkäsittely
- Selkeä putkistorakenne
- Parempi muistinhallinnan dokumentaatio

---

## Testauslista

### Esivaatimukset
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testaa jokainen näyte

#### Sessio 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sessio 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sessio 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sessio 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sessio 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sessio 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Ympäristömuuttujien viite

### Globaalit (kaikki näytteet)
| Muuttuja | Kuvaus | Oletus |
|----------|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Käytettävä mallialias | Vaihtelee näytteen mukaan |
| `FOUNDRY_LOCAL_ENDPOINT` | Palvelupisteen ohitus | Automaattisesti havaittu |
| `SHOW_USAGE` | Näytä tokenien käyttö | `0` |
| `RETRY_ON_FAIL` | Ota käyttöön uudelleenyritto | `1` |
| `RETRY_BACKOFF` | Alustava viive uudelleenyrittämisessä | `1.0` |

### Näytekohtaiset
| Muuttuja | Käytössä | Kuvaus |
|----------|----------|--------|
| `EMBED_MODEL` | Sessio 02 | Upotusmallin nimi |
| `RAG_QUESTION` | Sessio 02 | Testikysymys RAG:lle |
| `BENCH_MODELS` | Sessio 03 | Pilkulla erotetut mallit vertailua varten |
| `BENCH_ROUNDS` | Sessio 03 | Vertailukierrosten määrä |
| `BENCH_PROMPT` | Sessio 03 | Testikehotus vertailuille |
| `BENCH_STREAM` | Sessio 03 | Mittaa ensimmäisen tokenin viive |
| `SLM_ALIAS` | Sessio 04 | Pieni kielimalli |
| `LLM_ALIAS` | Sessio 04 | Suuri kielimalli |
| `COMPARE_PROMPT` | Sessio 04 | Vertailutestin kehotus |
| `AGENT_MODEL_PRIMARY` | Sessio 05 | Ensisijainen agenttimalli |
| `AGENT_MODEL_EDITOR` | Sessio 05 | Editorin agenttimalli |
| `AGENT_QUESTION` | Sessio 05 | Testikysymys agenteille |
| `PIPELINE_TASK` | Sessio 06 | Putkiston tehtävä |

---

## Rikkovat muutokset

**Ei mitään** - Kaikki muutokset ovat taaksepäin yhteensopivia.

Olemassa olevat skriptit toimivat edelleen. Uudet ominaisuudet ovat:
- Valinnaiset ympäristömuuttujat
- Parannetut virheilmoitukset (eivät riko toiminnallisuutta)
- Lisätty lokitus (voidaan hiljentää)
- Paremmat tyyppivihjeet (ei vaikutusta suoritusaikaan)

---

## Toteutetut parhaat käytännöt

### 1. Käytä aina Workshop Utils -kirjastoa
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Asianmukainen virheenkäsittelymalli
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informatiivinen lokitus
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Tyyppivihjeet
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Kattavat docstringit
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

### 6. Ympäristömuuttujien tuki
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Sulava heikentyminen
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

## Yleiset ongelmat ja ratkaisut

### Ongelma: Tuontivirheet
**Ratkaisu:** Asenna puuttuvat riippuvuudet
```bash
pip install sentence-transformers ragas datasets numpy
```

### Ongelma: Yhteysvirheet
**Ratkaisu:** Varmista, että Foundry Local on käynnissä
```bash
foundry service status
foundry model run phi-4-mini
```

### Ongelma: Mallia ei löydy
**Ratkaisu:** Tarkista saatavilla olevat mallit
```bash
foundry model ls
foundry model download <alias>
```

### Ongelma: Hidas suorituskyky
**Ratkaisu:** Käytä pienempiä malleja tai säädä parametreja
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Seuraavat askeleet

### 1. Testaa kaikki näytteet
Käy läpi yllä oleva testauslista varmistaaksesi, että kaikki näytteet toimivat oikein.

### 2. Päivitä dokumentaatio
- Päivitä session markdown-tiedostot uusilla esimerkeillä
- Lisää vianetsintäosio pääasialliseen README-tiedostoon
- Luo pikaopas

### 3. Luo integraatiotestit
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Lisää suorituskykyvertailut
Seuraa suorituskyvyn parannuksia virheenkäsittelyn parannusten ansiosta.

### 5. Käyttäjäpalaute
Kerää palautetta työpajan osallistujilta koskien:
- Virheilmoitusten selkeyttä
- Dokumentaation kattavuutta
- Käytön helppoutta

---

## Resurssit

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Pikaopas**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Siirtymismuistiinpanot**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Pääasiallinen arkisto**: https://github.com/microsoft/Foundry-Local

---

## Ylläpito

### Uusien näytteiden lisääminen
Noudata näitä malleja luodessasi uusia näytteitä:

1. Käytä `workshop_utils` asiakashallintaan
2. Lisää kattava virheenkäsittely
3. Sisällytä ympäristömuuttujien tuki
4. Lisää tyyppivihjeet ja docstringit
5. Tarjoa informatiivinen lokitus
6. Sisällytä käyttöesimerkit docstringiin
7. Linkitä SDK-dokumentaatioon

### Päivitysten tarkistaminen
Kun tarkistat näytepäivityksiä, varmista seuraavat asiat:
- [ ] Virheenkäsittely kaikissa I/O-toiminnoissa
- [ ] Tyyppivihjeet julkisissa funktioissa
- [ ] Kattavat docstringit
- [ ] Ympäristömuuttujien dokumentaatio
- [ ] Informatiivinen käyttäjäpalaute
- [ ] SDK-viitelinkit
- [ ] Johdonmukainen koodityyli

---

**Yhteenveto**: Kaikki Workshop Python -näytteet noudattavat nyt Foundry Local SDK:n parhaita käytäntöjä parannetulla virheenkäsittelyllä, kattavalla dokumentaatiolla ja parannetulla käyttäjäkokemuksella. Ei rikkovia muutoksia - kaikki olemassa oleva toiminnallisuus säilytetty ja parannettu.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.