<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T22:19:06+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "fi"
}
-->
# EdgeAI aloittelijoille - Työpaja

> **Käytännön oppimispolku tuotantovalmiiden Edge AI -sovellusten rakentamiseen**
>
> Hallitse paikallinen AI-järjestelmä Microsoft Foundry Localin avulla, ensimmäisestä keskustelusta monen agentin orkestrointiin kuudessa edistyneessä sessiossa.

---

## 🎯 Johdanto

Tervetuloa **EdgeAI aloittelijoille -työpajaan** – käytännönläheiseen oppaaseen älykkäiden sovellusten rakentamiseen, jotka toimivat täysin paikallisella laitteistolla. Tämä työpaja muuttaa teoreettiset Edge AI -konseptit todellisiksi taidoiksi haastavien harjoitusten kautta, joissa käytetään Microsoft Foundry Localia ja pieniä kielimalleja (SLM).

### Miksi tämä työpaja?

**Edge AI -vallankumous on täällä**

Organisaatiot ympäri maailmaa siirtyvät pilvipohjaisesta AI:sta reunalaskentaan kolmesta tärkeästä syystä:

1. **Tietosuoja ja vaatimustenmukaisuus** - Käsittele arkaluontoisia tietoja paikallisesti ilman pilviyhteyttä (HIPAA, GDPR, taloudelliset säädökset)
2. **Suorituskyky** - Poista verkkoviive (50-500ms paikallisesti vs. 500-2000ms pilvikierros)
3. **Kustannusten hallinta** - Poista per-token API-kustannukset ja skaalaa ilman pilvikuluja

**Mutta Edge AI on erilaista**

AI:n käyttö paikallisesti vaatii uusia taitoja:
- Mallien valinta ja optimointi resurssirajoituksia varten
- Paikallisten palveluiden hallinta ja laitteistokiihdytys
- Kehotusmuotoilu pienemmille malleille
- Tuotantokäyttöön liittyvät mallit reunalaitteille

**Tämä työpaja tarjoaa nämä taidot**

Kuudessa keskittyneessä sessiossa (~3 tuntia yhteensä) etenet "Hello World" -vaiheesta tuotantovalmiiden monen agentin järjestelmien käyttöönottoon – kaikki paikallisesti omalla koneellasi.

---

## 📚 Oppimistavoitteet

Työpajan suorittamisen jälkeen osaat:

### Keskeiset taidot
1. **Paikallisten AI-palveluiden käyttöönotto ja hallinta**
   - Asenna ja konfiguroi Microsoft Foundry Local
   - Valitse sopivat mallit reunakäyttöön
   - Hallitse mallien elinkaarta (lataus, käyttö, välimuisti)
   - Seuraa resurssien käyttöä ja optimoi suorituskykyä

2. **AI-pohjaisten sovellusten rakentaminen**
   - Toteuta OpenAI-yhteensopivia keskustelutoimintoja paikallisesti
   - Suunnittele tehokkaita kehotuksia pienille kielimalleille
   - Käsittele suoratoistovastauksia paremman käyttökokemuksen saavuttamiseksi
   - Integroi paikalliset mallit olemassa oleviin sovelluksiin

3. **RAG-järjestelmien (Retrieval Augmented Generation) luominen**
   - Rakenna semanttinen haku upotuksilla
   - Perusta LLM-vastaukset alakohtaisiin tietoihin
   - Arvioi RAG-laatua alan standardimittareilla
   - Skaalaa prototyypistä tuotantoon

4. **Mallien suorituskyvyn optimointi**
   - Testaa useita malleja käyttötapauksesi mukaan
   - Mittaa viive, läpimeno ja ensimmäisen tokenin aika
   - Valitse optimaaliset mallit nopeuden/laadun kompromissien perusteella
   - Vertaa SLM- ja LLM-mallien kompromisseja todellisissa tilanteissa

5. **Monen agentin järjestelmien orkestrointi**
   - Suunnittele erikoistuneita agentteja eri tehtäviin
   - Toteuta agenttien muisti ja kontekstinhallinta
   - Koordinoi agentteja monimutkaisissa työnkuluissa
   - Ohjaa pyyntöjä älykkäästi useiden mallien välillä

6. **Tuotantovalmiiden ratkaisujen käyttöönotto**
   - Toteuta virheenkäsittely ja uudelleenyrittämislogiikka
   - Seuraa tokenien käyttöä ja järjestelmäresursseja
   - Rakenna skaalautuvia arkkitehtuureja mallityökaluina
   - Suunnittele siirtymäpolut reunasta hybridiin (reuna + pilvi)

---

## 🎓 Oppimistulokset

### Mitä rakennat

Työpajan lopussa olet luonut:

| Sessio | Lopputulos | Osoitetut taidot |
|--------|------------|------------------|
| **1** | Keskustelusovellus suoratoistolla | Palvelun asennus, peruskeskustelut, suoratoistokäyttökokemus |
| **2** | RAG-järjestelmä arvioinnilla | Upotukset, semanttinen haku, laatumittarit |
| **3** | Monimallinen testauspaketti | Suorituskyvyn mittaus, mallien vertailu |
| **4** | SLM vs LLM vertailija | Kompromissianalyysi, optimointistrategiat |
| **5** | Monen agentin orkestroija | Agenttien suunnittelu, muistinhallinta, koordinointi |
| **6** | Älykäs reititysjärjestelmä | Tarkoituksen tunnistus, mallin valinta, skaalautuvuus |

### Taitomatriisi

| Taitotaso | Sessio 1-2 | Sessio 3-4 | Sessio 5-6 |
|-----------|------------|------------|------------|
| **Aloittelija** | ✅ Asennus & perusteet | ⚠️ Haastavaa | ❌ Liian edistynyttä |
| **Keskitaso** | ✅ Nopeasti läpi | ✅ Keskeinen oppiminen | ⚠️ Venytystavoitteet |
| **Edistynyt** | ✅ Helppo läpikäynti | ✅ Viimeistely | ✅ Tuotantokuvioita |

### Työelämätaitoja

**Työpajan jälkeen osaat:**

✅ **Rakentaa tietosuojaa korostavia sovelluksia**
- Terveydenhuollon sovellukset, jotka käsittelevät PHI/PII paikallisesti
- Talouspalvelut, joissa vaatimustenmukaisuus on tärkeää
- Valtion järjestelmät, joissa tietojen suvereniteetti on keskeistä

✅ **Optimoida reunaympäristöjä**
- IoT-laitteet, joissa on rajalliset resurssit
- Offline-ensimmäiset mobiilisovellukset
- Matala viive reaaliaikaisissa järjestelmissä

✅ **Suunnitella älykkäitä arkkitehtuureja**
- Monen agentin järjestelmät monimutkaisiin työnkulkuihin
- Hybridi reunapilvi-käyttöönotot
- Kustannusoptimoitu AI-infrastruktuuri

✅ **Johtaa Edge AI -hankkeita**
- Arvioi Edge AI:n toteutettavuutta projekteille
- Valitse sopivat mallit ja kehykset
- Suunnittele skaalautuvia paikallisia AI-ratkaisuja

---

## 🗺️ Työpajan rakenne

### Sessioiden yleiskatsaus (6 sessiota × 30 minuuttia = 3 tuntia)

| Sessio | Aihe | Painopiste | Kesto |
|--------|------|-----------|-------|
| **1** | Aloittaminen Foundry Localilla | Asennus, validointi, ensimmäiset keskustelut | 30 min |
| **2** | AI-ratkaisujen rakentaminen RAG:lla | Kehotusmuotoilu, upotukset, arviointi | 30 min |
| **3** | Avoimen lähdekoodin mallit | Mallien löytäminen, testaus, valinta | 30 min |
| **4** | Huippumallit | SLM vs LLM, optimointi, kehykset | 30 min |
| **5** | AI-agentit | Agenttien suunnittelu, orkestrointi, muisti | 30 min |
| **6** | Mallit työkaluina | Reititys, ketjutus, skaalautumisstrategiat | 30 min |

---

## 🚀 Nopea aloitus

### Esivaatimukset

**Järjestelmävaatimukset:**
- **OS**: Windows 10/11, macOS 11+ tai Linux (Ubuntu 20.04+)
- **RAM**: Vähintään 8GB, suositeltu 16GB+
- **Tallennustila**: Vähintään 10GB vapaata tilaa malleille
- **CPU**: Moderni prosessori, jossa AVX2-tuki
- **GPU** (valinnainen): CUDA-yhteensopiva tai Qualcomm NPU kiihdytykseen

**Ohjelmistovaatimukset:**
- **Python 3.8+** ([Lataa](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Asennusohje](../../../Workshop))
- **Git** ([Lataa](https://git-scm.com/downloads))
- **Visual Studio Code** (suositeltu) ([Lataa](https://code.visualstudio.com/))

### Asennus 3 vaiheessa

#### 1. Asenna Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Vahvista asennus:**
```bash
foundry --version
foundry service status
```

**Varmista, että Azure AI Foundry Local toimii kiinteällä portilla**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Vahvista toimivuus:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Saatavilla olevien mallien löytäminen**
Voit tarkistaa, mitkä mallit ovat saatavilla Foundry Local -instanssissasi, kysymällä mallien päätepistettä:

```bash
# cmd/bash/powershell
foundry model list
```

Käyttämällä verkkopäätepistettä 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Kloonaa arkisto ja asenna riippuvuudet

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Suorita ensimmäinen esimerkki

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Onnistui!** Näet suoratoistovastauksen liittyen Edge AI:hin.

---

## 📦 Työpajan materiaalit

### Python-esimerkit

Progressiiviset käytännön esimerkit, jotka havainnollistavat jokaista konseptia:

| Sessio | Esimerkki | Kuvaus | Suoritusaika |
|--------|-----------|--------|--------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Perus- ja suoratoistokeskustelu | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG upotuksilla | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG-laadun arviointi | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Monimallinen testaus | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM vertailu | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Monen agentin järjestelmä | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Tarkoituspohjainen reititys | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Monivaiheinen putkisto | ~60s |

### Jupyter-muistikirjat

Interaktiivinen tutkimus selityksillä ja visualisoinneilla:

| Sessio | Muistikirja | Kuvaus | Vaikeustaso |
|--------|-------------|--------|-------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Keskustelun perusteet & suoratoisto | ⭐ Aloittelija |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | RAG-järjestelmän rakentaminen | ⭐⭐ Keskitaso |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | RAG-laadun arviointi | ⭐⭐ Keskitaso |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Mallien testaus | ⭐⭐ Keskitaso |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Mallien vertailu | ⭐⭐ Keskitaso |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Agenttien orkestrointi | ⭐⭐⭐ Edistynyt |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Tarkoitusreititys | ⭐⭐⭐ Edistynyt |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Putkiston orkestrointi | ⭐⭐⭐ Edistynyt |

### Dokumentaatio

Kattavat oppaat ja viitemateriaalit:

| Dokumentti | Kuvaus | Käytä kun |
|------------|--------|-----------|
| [QUICK_START.md](./QUICK_START.md) | Nopea aloitusopas | Aloitat alusta |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Komento- ja API-pikaopas | Tarvitset nopeita vastauksia |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK-kuviot ja esimerkit | Kirjoitat koodia |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Ympäristömuuttujien opas | Konfiguroit esimerkkejä |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Viimeisimmät parannukset esimerkkeihin | Ymmärrät muutoksia |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Siirtymäopas | Päivität koodia |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Yleiset ongelmat ja ratkaisut | Vianetsintä |

---

## 🎓 Oppimispolun suositukset

### Aloittelijoille (3-4 tuntia)
1. ✅ Sessio 1: Aloittaminen (keskity asennukseen ja peruskeskusteluun)
2. ✅ Sessio 2: RAG-perusteet (ohita aluksi arviointi)
3. ✅ Sessio 3: Yksinkertainen testaus (vain 2 mallia)
4. ⏭️ Ohita aluksi sessiot 4-6
5. 🔄 Palaa sessioihin 4-6 ensimmäisen sovelluksen rakentamisen jälkeen

### Keskitasoisille kehittäjille (3 tuntia)
1. ⚡ Sessio 1: Nopea asennuksen validointi
2. ✅ Sessio 2: Täydellinen RAG-putkisto arvioinnilla
3. ✅ Sessio 3: Täysi testauspaketti
4. ✅ Sessio 4: Mallien optimointi
5. ✅ Sessio 5-6: Keskity arkkitehtuurikuvioihin

### Edistyneille asiantuntijoille (2-3 tuntia)
1. ⚡ Sessio 1-3: Nopeasti läpi ja validointi
2. ✅ Sessio 4: Syvällinen optimointi
3. ✅ Sessio 5: Monen agentin arkkitehtuuri
4. ✅ Sessio 6: Tuotantokuvioita ja skaalautuvuus
5. 🚀 Laajenna: Rakenna mukautettu reitityslogiikka ja hybridikäyttöönotot

---

## Työpajan sessiopaketti (keskittyneet 30 minuutin laboratoriot)

Jos seuraat tiivistettyä 6-session työpajamuotoa, käytä näitä omistettuja oppaita (jokainen vastaa ja täydentää laajempia moduulidokumentteja yllä):

| Työpajasessio | Opas | Keskeinen painopiste |
|---------------|------|----------------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Asenna, validoi, suorita phi & GPT-OSS-20B, kiihdytys |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Kehotusmuotoilu, RAG-kuviot, CSV & dokumenttien perustaminen, siirtyminen |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face -integraatio, testaus, mallin valinta |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX-kiihdytys |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Agenttien roolit, muisti, työkalut, orkestrointi |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Reititys, ketjutus, skaalautuminen Azureen |

Jokainen istuntotiedosto sisältää: tiivistelmän, oppimistavoitteet, 30 minuutin demokulun, aloitusprojektin, validointitarkistuslistan, vianmäärityksen ja viittaukset viralliseen Foundry Local Python SDK:hon.

### Esimerkkiskriptit

Workshopin riippuvuuksien asennus (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Jos Foundry Local -palvelua ajetaan eri (Windows) koneella tai virtuaalikoneella macOS:sta, määritä päätepiste:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Istunto | Skripti(t) | Kuvaus |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Palvelun käynnistys & suoratoistochat |
| 2 | `samples/session02/rag_pipeline.py` | Minimaalinen RAG (muistissa olevat upotukset) |
|   | `samples/session02/rag_eval_ragas.py` | RAG-arviointi ragas-metriikoilla |
| 3 | `samples/session03/benchmark_oss_models.py` | Monimallin viive- ja läpimenovertailu |
| 4 | `samples/session04/model_compare.py` | SLM vs LLM vertailu (viive & näyteulostulo) |
| 5 | `samples/session05/agents_orchestrator.py` | Kaksi agenttia: tutkimus → toimitusketju |
| 6 | `samples/session06/models_router.py` | Aikomusperusteinen reititysdemo |
|   | `samples/session06/models_pipeline.py` | Monivaiheinen suunnittelu/suoritus/tarkennusketju |

### Ympäristömuuttujat (Yhteiset kaikille esimerkeille)

| Muuttuja | Tarkoitus | Esimerkki |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Oletusmallialias perusesimerkeille | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Selkeä SLM vs suurempi malli vertailuun | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Pilkulla eroteltu lista aliasista vertailuun | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Vertailukierrosten määrä per malli | `3` |
| `BENCH_PROMPT` | Vertailussa käytetty kehotus | `Selitä lyhyesti retrieval augmented generation.` |
| `EMBED_MODEL` | Sentence-transformers upotusmalli | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Testikysymyksen ohitus RAG-putkelle | `Miksi käyttää RAG:ia paikallisessa päättelyssä?` |
| `AGENT_QUESTION` | Agenttien putkikysymyksen ohitus | `Selitä, miksi edge AI on tärkeä vaatimustenmukaisuudelle.` |
| `AGENT_MODEL_PRIMARY` | Mallialias tutkimusagentille | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Mallialias editoriagentille (voi olla eri) | `gpt-oss-20b` |
| `SHOW_USAGE` | Kun `1`, tulostaa tokenien käytön per suoritus | `1` |
| `RETRY_ON_FAIL` | Kun `1`, yrittää uudelleen hetkellisten chat-virheiden kohdalla | `1` |
| `RETRY_BACKOFF` | Sekuntien odotusaika ennen uudelleenyritystä | `1.0` |

Jos muuttujaa ei ole asetettu, skriptit käyttävät järkeviä oletusarvoja. Yksimallin demoissa tarvitset yleensä vain `FOUNDRY_LOCAL_ALIAS`.

### Apumoduuli

Kaikki esimerkit jakavat nyt apuskriptin `samples/workshop_utils.py`, joka tarjoaa:

* Välimuistissa olevan `FoundryLocalManager` + OpenAI-asiakasluonnin
* `chat_once()`-apuohjelman, jossa valinnainen uudelleenyritys + käyttöraportointi
* Yksinkertainen tokenien käyttöraportointi (aktivoidaan `SHOW_USAGE=1` avulla)

Tämä vähentää toistoa ja korostaa parhaita käytäntöjä tehokkaalle paikallismallin orkestroinnille.

## Valinnaiset parannukset (Istuntojen välillä)

| Teema | Parannus | Istunnot | Ympäristö / Kytkin |
|-------|-------------|----------|--------------|
| Determinismi | Kiinteä lämpötila + vakaat kehotusjoukot | 1–6 | Aseta `temperature=0`, `top_p=1` |
| Tokenien käytön näkyvyys | Johdonmukainen kustannus/tehokkuusopetus | 1–6 | `SHOW_USAGE=1` |
| Ensimmäinen token suoratoistossa | Koettu viivemittari | 1,3,4,6 | `BENCH_STREAM=1` (vertailu) |
| Uudelleenyrityksen kestävyys | Käsittelee hetkelliset kylmäkäynnistykset | Kaikki | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Monimalliset agentit | Heterogeeninen roolien erikoistuminen | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Mukautuva reititys | Aikomus + kustannusheuristiikka | 6 | Laajenna reititin eskalointilogiikalla |
| Vektorimuisti | Pitkäaikainen semanttinen muistaminen | 2,5,6 | Integroi FAISS/Chroma upotusindeksi |
| Jäljen vienti | Auditointi & arviointi | 2,5,6 | Lisää JSON-rivit per vaihe |
| Laaturubriikit | Laadullinen seuranta | 3–6 | Toissijaiset pisteytyskehotukset |
| Savutestit | Nopea workshopin ennakkovarmistus | Kaikki | `python Workshop/tests/smoke.py` |

### Deterministinen pikakäynnistys

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Odota vakaita tokenimääriä toistuvilla identtisillä syötteillä.

### RAG-arviointi (Istunto 2)

Käytä `rag_eval_ragas.py`-skriptiä laskemaan vastausten relevanssia, paikkansapitävyyttä ja kontekstin tarkkuutta pienellä synteettisellä datasetillä:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Laajenna toimittamalla suurempi JSONL-tiedosto kysymyksistä, konteksteista ja totuuksista, ja muunna se Hugging Face `Dataset`-muotoon.

## CLI-komentojen tarkkuusliite

Workshop käyttää tarkoituksella vain tällä hetkellä dokumentoituja / vakaita Foundry Local CLI-komentoja.

### Viitatut vakaa komennot

| Kategoria | Komento | Tarkoitus |
|----------|---------|---------|
| Ydin | `foundry --version` | Näytä asennettu versio |
| Ydin | `foundry init` | Alusta konfiguraatio |
| Palvelu | `foundry service start` | Käynnistä paikallinen palvelu (jos ei automaattinen) |
| Palvelu | `foundry status` | Näytä palvelun tila |
| Mallit | `foundry model list` | Näytä katalogi / saatavilla olevat mallit |
| Mallit | `foundry model download <alias>` | Lataa mallin painot välimuistiin |
| Mallit | `foundry model run <alias>` | Käynnistä (lataa) malli paikallisesti; yhdistä `--prompt` yhden kerran suoritukseen |
| Mallit | `foundry model unload <alias>` / `foundry model stop <alias>` | Poista malli muistista (jos tuettu) |
| Välimuisti | `foundry cache list` | Näytä välimuistissa olevat (ladatut) mallit |
| Järjestelmä | `foundry system info` | Laitteiston & kiihdytysominaisuuksien tilannekuva |
| Järjestelmä | `foundry system gpu-info` | GPU-diagnostiikkatiedot |
| Konfiguraatio | `foundry config list` | Näytä nykyiset konfiguraatioarvot |
| Konfiguraatio | `foundry config set <key> <value>` | Päivitä konfiguraatio |

### Yhden kerran kehotusmalli

Käytä vanhentuneen `model chat`-alakomennon sijaan:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Tämä suorittaa yhden kehotus/vastaus-syklin ja sulkeutuu.

### Poistetut / Vältetyt mallit

| Vanhentunut / Dokumentoimaton | Korvaava / Ohjeistus |
|---------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Käytä tavallista `foundry model list` + viimeaikainen toiminta / lokit |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Käytä vertailuskriptiä + käyttöjärjestelmän työkaluja (Tehtävienhallinta / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Vertailu & Telemetria

- Viive, p95, tokenit/sekunti: `samples/session03/benchmark_oss_models.py`
- Ensimmäisen tokenin viive (suoratoisto): aseta `BENCH_STREAM=1`
- Resurssien käyttö: Käyttöjärjestelmän monitorit (Tehtävienhallinta, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Kun uudet CLI-telemetriakomennot vakautuvat, ne voidaan sisällyttää pienillä muokkauksilla istuntojen markdown-tiedostoihin.

### Automaattinen lint-suoja

Automaattinen linter estää vanhentuneiden CLI-mallien uudelleenkäyttöä markdown-tiedostojen koodilohkojen sisällä:

Skripti: `Workshop/scripts/lint_markdown_cli.py`

Vanhentuneet mallit estetään koodilohkojen sisällä.

Suositellut korvaukset:
| Vanhentunut | Korvaava |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Vertailuskripti + järjestelmätyökalut |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Aja paikallisesti:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub-toiminto: `.github/workflows/markdown-cli-lint.yml` suoritetaan jokaisella pushilla & PR:llä.

Valinnainen pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Nopea CLI → SDK-siirtymätaulukko

| Tehtävä | CLI-yhden rivin komento | SDK (Python) vastaava | Huomautukset |
|------|---------------|-------------------------|-------|
| Aja malli kerran (kehotus) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK käynnistää palvelun & välimuistin automaattisesti |
| Lataa (välimuistiin) malli | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # käynnistää latauksen/latauksen` | Manager valitsee parhaan vaihtoehdon, jos alias viittaa useisiin versioihin |
| Näytä katalogi | `foundry model list` | `# käytä manageria jokaiselle aliasille tai ylläpidä tunnettua listaa` | CLI yhdistää; SDK tällä hetkellä per-alias-initialisointi |
| Näytä välimuistissa olevat mallit | `foundry cache list` | `manager.list_cached_models()` | Managerin alustuksen jälkeen (mikä tahansa alias) |
| Ota GPU-kiihdytys käyttöön | `foundry config set compute.onnx.enable_gpu true` | `# CLI-toiminto; SDK olettaa, että konfiguraatio on jo sovellettu` | Konfiguraatio on ulkoinen sivuvaikutus |
| Hae päätepisteen URL | (implisiittinen) | `manager.endpoint` | Käytetään OpenAI-yhteensopivan asiakkaan luomiseen |
| Lämmitä malli | `foundry model run <alias>` ja ensimmäinen kehotus | `chat_once(alias, messages=[...])` (apuohjelma) | Apuohjelmat käsittelevät alkuperäisen kylmäkäynnistysviiveen |
| Mittaa viive | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (tai uusi vientiskripti) | Suosi skriptiä johdonmukaisten mittareiden saamiseksi |
| Lopeta / poista malli | `foundry model unload <alias>` | (Ei saatavilla – käynnistä palvelu / prosessi uudelleen) | Yleensä ei tarpeen workshopin kulussa |
| Hae tokenien käyttö | (katso ulostulo) | `resp.usage.total_tokens` | Tarjotaan, jos taustajärjestelmä palauttaa käyttöobjektin |

## Vertailun markdown-vienti

Käytä skriptiä `Workshop/scripts/export_benchmark_markdown.py` ajaaksesi tuoreen vertailun (sama logiikka kuin `samples/session03/benchmark_oss_models.py`) ja tuottaaksesi GitHub-yhteensopivan markdown-taulukon sekä raaka JSON-tiedoston.

### Esimerkki

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Luodut tiedostot:
| Tiedosto | Sisältö |
|------|----------|
| `benchmark_report.md` | Markdown-taulukko + tulkintavihjeet |
| `benchmark_report.json` | Raakametriikkataulukko (vertailuun / trendiseurantaan) |

Aseta `BENCH_STREAM=1` ympäristöön sisällyttääksesi ensimmäisen tokenin viiveen, jos tuettu.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.