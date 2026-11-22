# Työpajan muistikirjat

> **Interaktiiviset Jupyter-muistikirjat käytännön Edge AI -oppimiseen**
>
> Progressiiviset, omaan tahtiin etenevät opastusohjelmat, jotka rakentuvat peruschatin täydennyksistä kehittyneisiin moniedustusjärjestelmiin käyttäen Microsoft Foundry Local- ja pieniä kielimalleja.

---

## 📖 Johdanto

Tervetuloa **EdgeAI aloittelijoille -työpajan muistikirjat** -kokoelmaan. Nämä interaktiiviset Jupyter-muistikirjat tarjoavat käytännön oppimiskokemuksen, jossa kirjoitat, suoritat ja kokeilet Edge AI -koodia reaaliajassa.

### Miksi Jupyter-muistikirjat?

Perinteisiin opastusohjelmiin verrattuna nämä muistikirjat tarjoavat:

- **Interaktiivinen oppiminen**: Suorita koodisoluja ja näe tulokset välittömästi
- **Kokeilu**: Muokkaa parametreja ja seuraa muutoksia reaaliajassa
- **Dokumentointi**: Riviselitteiset selitykset ja markdown-solut ohjaavat sinua konseptien läpi
- **Toistettavuus**: Täydelliset toimintavalmiit esimerkit, joita voit käyttää ja hyödyntää uudelleen
- **Visualisointi**: Näe suorituskykymittarit, upotukset ja tulokset sisällä

### Mikä tekee näistä muistikirjoista erityisiä?

Jokainen muistikirja on suunniteltu noudattaen **tuotantovalmiita parhaita käytäntöjä**:

✅ **Laaja virheiden käsittely** - Sileä alasajo ja informatiiviset virheilmoitukset  
✅ **Tyyppi- vihjeet & dokumentaatio** - Selkeät funktiosignatuurit ja docstringit  
✅ **Suorituskyvyn seuranta** - Token-käytön seuranta ja viiveen mittaukset  
✅ **Modulaarinen suunnittelu** - Uudelleenkäytettävät mallit, joita voit soveltaa projekteihisi  
✅ **Progressiivinen monimutkaisuus** - Rakentuu aiemmille istunnoille järjestelmällisesti

---

## 🎯 Oppimistavoitteet

### Keskeiset taidot, joita kehität

Näiden muistikirjojen avulla hallitset:

1. **Paikallisten AI-palveluiden hallinta**
   - Määritä ja hallitse Microsoft Foundry Local -palveluita
   - Valitse ja lataa sopivat mallit laitteistollesi
   - Seuraa resurssien käyttöä ja optimoi suorituskykyä
   - Hallitse palveluiden löytämistä ja tilan tarkistusta

2. **AI-sovellusten kehitys**
   - Toteuta OpenAI-yhteensopivia chat-täydennyksiä paikallisesti
   - Rakenna suoratoistoliittymiä paremman käyttäjäkokemuksen saavuttamiseksi
   - Suunnittele tehokkaita kehotteita pienille kielimalleille
   - Integroi paikalliset mallit sovelluksiin

3. **Hakuavusteinen generaation (RAG)**
   - Luo semanttinen haku vektoriupotuksilla
   - Perusta LLM-vastaukset omakohtaisiin asiakirjoihin
   - Arvioi RAG-laatua RAGAS-mittareilla
   - Skaalaa prototyypistä tuotantoon

4. **Suorituskyvyn optimointi**
   - Vertaa useita malleja järjestelmällisesti
   - Mittaa viivettä, läpimenonopeutta ja ensimmäisen tokenin aikaa
   - Vertaa pieniä kielimalleja suuriin kielimalleihin
   - Valitse optimaaliset mallit suorituskyvyn/laadun kompromisseihin perustuen

5. **Moniagenttien orkestrointi**
   - Suunnittele erikoistuneita agenteja eri tehtäviin
   - Toteuta agenttimuisti ja kontekstinhallinta
   - Koordinoi useita agenteja monimutkaisissa työtavoissa
   - Rakenna koordinaattorimalleja agenttiyhteistyöhön

6. **Älykäs mallin reititys**
   - Toteuta intentioiden tunnistus ja kaavojen sovitus
   - Reititä kyselyt automaattisesti oikeille malleille
   - Rakenna monivaihepipeliet (suunnittele → suorita → hioa)
   - Suunnittele skaalautuvia malli-työkaluina -arkkitehtuureja

---

## 🎓 Oppimistulokset

### Mitä rakennat

| Muistikirja | Tuotos | Osoitetut taidot | Vaikeustaso |
|----------|-------------|---------------------|------------|
| **Istunto 01** | Chat-sovellus suoratoistolla | Palvelun pystytys, perus täydennykset, suoratoisto UX | ⭐ Aloittelija |
| **Istunto 02 (RAG)** | RAG-pipeline arvioinnilla | Upotukset, semanttinen haku, laatumittarit | ⭐⭐ Keskitaso |
| **Istunto 02 (Eval)** | RAG-laadun arvioija | RAGAS-mittarit, järjestelmällinen arviointi | ⭐⭐ Keskitaso |
| **Istunto 03** | Monimallivertailu | Suorituskyvyn mittaaminen, mallien vertailu | ⭐⭐ Keskitaso |
| **Istunto 04** | SLM vs LLM vertailu | Kompromissianalyysi, optimointistrategiat | ⭐⭐⭐ Edistynyt |
| **Istunto 05** | Moniagenttien orkestroija | Agenttisuunnittelu, muisti, koordinointi | ⭐⭐⭐ Edistynyt |
| **Istunto 06 (Reititin)** | Älykäs reititysjärjestelmä | Intentiotunnistus, mallin valinta | ⭐⭐⭐ Edistynyt |
| **Istunto 06 (Pipeline)** | Monivaihepipelniit | Suunnittelu/suoritus/hionta-työt | ⭐⭐⭐ Edistynyt |

### Osaamisen eteneminen

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Työpajan aikataulu

### 🚀 Puolipäivän työpaja (3,5 tuntia)

**Täydellinen: Tiimikoulutukset, hackathonit, konferenssityöpajat**

| Aika | Kesto | Istunto | Aiheet | Aktiviteetit |
|------|----------|---------|--------|------------|
| **0:00** | 30 min | Asennus & Johdanto | Ympäristön asennus, Foundry Local -asennus | Asenna riippuvuudet, tarkista asennus |
| **0:30** | 30 min | Istunto 01 | Perus chat-täydennykset, suoratoisto | Suorita muistikirja, muokkaa kehotteita |
| **1:00** | 45 min | Istunto 02 | RAG-pipeline, upotukset, arviointi | Rakenna RAG-järjestelmä, testaa kyselyjä |
| **1:45** | 15 min | Tauko | ☕ Kahvi & kysymykset | — |
| **2:00** | 30 min | Istunto 03 | Monimallien vertailu | Vertaa 3+ mallia |
| **2:30** | 30 min | Istunto 04 | SLM vs LLM kompromissit | Analysoi suorituskyky/laatu |
| **3:00** | 30 min | Istunnot 05-06 | Moniagenttijärjestelmät & reititys | Tutki edistyneitä rakenteita |

**Tuloste**: Osallistujat saavat 6 toimivaa Edge AI -sovellusta ja tuotantovalmiita koodimalleja.

---

### 🎓 Koko päivän työpaja (6 tuntia)

**Täydellinen: Syvälliseen koulutukseen, bootcampeihin, yliopistokursseille**

| Aika | Kesto | Istunto | Aiheet | Aktiviteetit |
|------|----------|---------|--------|------------|
| **0:00** | 45 min | Asennus & Teoria | Ympäristön asennus, Edge AI perusteet | Asenna, tarkista, keskustele käyttötapauksista |
| **0:45** | 45 min | Istunto 01 | Chat-täydennysten syväsukellus | Toteuta perus- ja suoratoistochat |
| **1:30** | 30 min | Tauko | ☕ Kahvi & verkostoituminen | — |
| **2:00** | 60 min | Istunto 02 (molemmat) | RAG-pipeline + RAGAS-arviointi | Rakenna kokonainen RAG-järjestelmä |
| **3:00** | 30 min | Käytännön harjoitus 1 | Räätälöity RAG omalle alalle | Sovella omiin asiakirjoihin |
| **3:30** | 30 min | Lounas | 🍽️ | — |
| **4:00** | 45 min | Istunto 03 | Vertailumenetelmät | Järjestelmällinen mallien vertailu |
| **4:45** | 45 min | Istunto 04 | Optimointistrategiat | SLM vs LLM analyysi |
| **5:30** | 60 min | Istunnot 05-06 | Edistynyt orkestrointi | Moniagenttijärjestelmät, reititys |
| **6:30** | 30 min | Käytännön harjoitus 2 | Rakenna räätälöity agenttijärjestelmä | Suunnittele oma orkestroijasi |

**Tuloste**: Syvällinen ymmärrys Edge AI -malleista ja 2 räätälöityä projektia.

---

### 📚 Omaehtoinen oppiminen (2 viikkoa)

**Täydellinen: Yksittäisille oppijoille, verkkokursseille, itseopiskeluun**

#### 1. viikko: Perusteet (6 tuntia)

| Päivä | Painopiste | Kesto | Muistikirjat | Kotitehtävät |
|-----|-------|----------|-----------|----------|
| **Ma** | Asennus & Perusteet | 1,5 h | Istunto 01 | Muokkaa kehotteita, testaa suoratoistoa |
| **Ke** | RAG perusteet | 2 h | Istunto 02 (molemmat) | Lisää omat asiakirjasi |
| **Pe** | Vertailu | 1,5 h | Istunto 03 | Vertaa lisämalleja |
| **La** | Kertaus & Harjoittelu | 1 h | Kaikki 1. viikon | Suorita harjoituksia, korjaa virheitä |

#### 2. viikko: Edistynyt (5 tuntia)

| Päivä | Painopiste | Kesto | Muistikirjat | Kotitehtävät |
|-----|-------|----------|-----------|----------|
| **Ma** | Optimointi | 1,5 h | Istunto 04 | Dokumentoi kompromissit |
| **Ke** | Moniagenttijärjestelmät | 2 h | Istunto 05 | Suunnittele räätälöityjä agenteja |
| **Pe** | Älykäs reititys | 1,5 h | Istunto 06 (molemmat) | Rakenna reitityslogiikka |
| **La** | Lopputyö | 2 h | Integraatio | Yhdistä useita malleja |

**Tuloste**: Edge AI -mallien hallinta ja portfolioprojekti.

---

## 📔 Muistikirjojen kuvaukset

### 📘 Istunto 01: Chat käynnistys
**Tiedosto**: `session01_chat_bootstrap.ipynb`  
**Kesto**: 20-30 minuuttia  
**Esitiedot**: Ei mitään  
**Vaikeusaste**: ⭐ Aloittelija

**Mitä opit**:
- Asenna ja määritä Foundry Local Python SDK
- Käytä `FoundryLocalManager` -luokkaa automaattiseen palveluiden löytämiseen
- Toteuta perus chat-täydennyksiä OpenAI-yhteensopivalla API:lla
- Rakenna suoratoistovastauksia paremman käyttäjäkokemuksen saavuttamiseksi
- Käsittele virheitä ja palvelun poissaoloja hienovaraisesti

**Keskeiset konseptit**: Palvelun hallinta, chat-täydennykset, suoratoisto, virheiden käsittely

**Rakennat**: Interaktiivisen chat-sovelluksen suoratoistolla

---

### 📗 Istunto 02: RAG-pipeline
**Tiedosto**: `session02_rag_pipeline.ipynb`  
**Kesto**: 30-45 minuuttia  
**Esitiedot**: Istunto 01  
**Vaikeusaste**: ⭐⭐ Keskitaso

**Mitä opit**:
- Toteuta Retrieval Augmented Generation (RAG) -malli
- Luo vektoriupotuksia käyttäen lauseiden muuntajia
- Rakenna semanttinen haku kosinietäisyydellä
- Perusta LLM-vastaukset toimialakohtaisiin asiakirjoihin
- Käsittele valinnaiset riippuvuudet import-tauluilla

**Keskeiset konseptit**: RAG-arkkitehtuuri, upotukset, semanttinen haku, vektorietäisyys

**Rakennat**: Asiakirjoihin perustuvan kysymys-vastausjärjestelmän

---

### 📗 Istunto 02: RAG arviointi RAGAS:lla
**Tiedosto**: `session02_rag_eval_ragas.ipynb`  
**Kesto**: 30-45 minuuttia  
**Esitiedot**: Istunto 02 RAG-pipeline  
**Vaikeusaste**: ⭐⭐ Keskitaso

**Mitä opit**:
- Arvioi RAG-laatu alan standardeilla
- Mittaa kontekstin relevanssia, vastauksen relevanssia, uskollisuutta
- Käytä RAGAS-kehystä järjestelmälliseen arviointiin
- Tunnista ja korjaa RAG-laadun ongelmia
- Rakenna arviointiaineistot omalle toimialallesi

**Keskeiset konseptit**: RAG-arviointi, RAGAS-mittarit, laadun mittaus, järjestelmällinen testaus

**Rakennat**: RAG-laadunarviointikehyksen

---

### 📙 Istunto 03: OSS-mallien vertailu
**Tiedosto**: `session03_benchmark_oss_models.ipynb`  
**Kesto**: 30-45 minuuttia  
**Esitiedot**: Istunto 01  
**Vaikeusaste**: ⭐⭐ Keskitaso

**Mitä opit**:
- Järjestelmällisesti vertaa useita malleja
- Mittaa viivettä, läpimenoaikaa, ensimmäisen tokenin aikaa
- Toteuta maltillinen virheensietomekanismi mallivirheille
- Vertaa suorituskykyä malliperheiden välillä
- Visualisoi ja analysoi vertailutuloksia

**Keskeiset konseptit**: Suorituskyvyn vertailu, viiveen mittaus, mallien vertailu, tilastollinen analyysi

**Rakennat**: Monimallien vertailutyökalun

---

### 📙 Istunto 04: Mallien vertailu (SLM vs LLM)
**Tiedosto**: `session04_model_compare.ipynb`  
**Kesto**: 30-45 minuuttia  
**Esitiedot**: Istunnot 01, 03  
**Vaikeusaste**: ⭐⭐⭐ Edistynyt

**Mitä opit**:
- Vertaa pieniä kielimalleja suuriin kielimalleihin
- Analysoi suorituskyvyn ja laadun välisiä kompromisseja
- Mittaa reunaolosuhteisiin sopivuuden mittareita
- Valitse optimaaliset mallit käyttöönoton vaatimusten mukaan
- Dokumentoi mallivalinnan päätöskriteerit

**Keskeiset konseptit**: Mallin valinta, kompromissianalyysi, optimointistrategiat, käyttöönoton suunnittelu

**Rakennat**: SLM vs LLM vertailukehyksen

---

### 📕 Istunto 05: Moniagenttien orkestroija
**Tiedosto**: `session05_agents_orchestrator.ipynb`  
**Kesto**: 45-60 minuuttia  
**Esitiedot**: Istunnot 01-02  
**Vaikeusaste**: ⭐⭐⭐ Edistynyt

**Mitä opit**:
- Suunnittele erikoistuneita agenteja eri tehtäviin
- Toteuta agentin muisti ja kontekstinhallinta
- Rakenna koordinaattorimalleja agenttiyhteistyöhön
- Käsittele agenttien välistä viestintää ja tehtävien siirtoja
- Seuraa moniagenttijärjestelmän suorituskykyä

**Keskeiset konseptit**: Agenttiarkkitehtuuri, koordinaattorimallit, muistin hallinta, agenttien orkestrointi

**Rakennat**: Moniagenttijärjestelmän koordinaattorilla ja erikoisasiantuntijoilla

---

### 📕 Istunto 06: Mallin reititin
**Tiedosto**: `session06_models_router.ipynb`  
**Kesto**: 30-45 minuuttia  
**Esitiedot**: Istunnot 01, 03  
**Vaikeusaste**: ⭐⭐⭐ Edistynyt

**Mitä opit**:
- Toteuta intentiotunnistus ja kaavojen sovitus
- Rakenna avainsanoihin perustuva mallin reititys
- Reititä kyselyt automaattisesti sopiville malleille
- Määritä monimallirekisterit
- Seuraa reitityspäätöksiä ja suorituskykyä

**Keskeiset konseptit**: Intentiotunnistus, mallin reititys, kaavojen sovitus, älykäs valinta

**Rakennat**: Älykkään mallin reititysjärjestelmän

---

### 📕 Istunto 06: Monivaihepipeline
**Tiedosto**: `session06_models_pipeline.ipynb`  
**Kesto**: 30-45 minuuttia  
**Esitiedot**: Istunnot 01, 06 Reititin  
**Vaikeusaste**: ⭐⭐⭐ Edistynyt

**Mitä opit**:
- Rakenna monivaiheisia AI-pipelineja (suunnittele → suorita → hio)
- Integroi reititin älykkääseen mallin valintaan
- Toteuta pipeline-virheiden käsittely ja palautuminen
- Seuraa pipelinen suorituskykyä ja vaiheita
- Suunnittele skaalautuvia malli-työkaluina -arkkitehtuureja


**Keskeiset käsitteet**: Putkistoarkkitehtuuri, monivaiheinen käsittely, virheiden korjaus, skaalautuvuusmallit

**Rakennat**: Monivaiheinen älykäs putkisto reitityksellä

---

## 🚀 Aloittaminen

### Vaatimukset

**Järjestelmävaatimukset**:
- **Käyttöjärjestelmä**: Windows 10/11, macOS 11+ tai Linux (Ubuntu 20.04+)
- **RAM-muisti**: Vähintään 8GB, suositus 16GB+
- **Tallennustila**: 10GB+ vapaata tilaa malleille
- **Laitteisto**: CPU, jossa AVX2; GPU (CUDA, Qualcomm NPU) valinnainen

**Ohjelmistovaatimukset**:
- **Python 3.8+** pipillä
- **Jupyter Notebook** tai **VS Code** Jupyter-laajennuksella
- **Microsoft Foundry Local** asennettuna ja konfiguroituna
- **Git** (repositoriokloonausta varten)

### Asennusvaiheet

#### 1. Asenna Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Tarkista asennus**:
```bash
foundry --version
```

#### 2. Määritä Python-ympäristö

```bash
# Siirry Workshop-hakemistoon
cd Workshop

# Luo virtuaaliympäristö
python -m venv .venv

# Aktivoi virtuaaliympäristö
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Asenna riippuvuudet
pip install -r requirements.txt
```

#### 3. Käynnistä Foundry Local

```bash
# Lataa malli (lataa automaattisesti tarvittaessa)
foundry model run phi-4-mini

# Varmista, että palvelu on käynnissä
foundry service status
```

#### 4. Käynnistä Jupyter

```bash
# Käynnistä Jupyter Notebook
jupyter notebook notebooks/

# Tai käytä VS Codea Jupyter-laajennuksella
code notebooks/
```

### Pikainen tarkistus

Suorita tämä Python-solu varmistaaksesi asetukset:

```python
from foundry_local import FoundryLocalManager
import openai

# Alusta hallinnoija (löytää palvelun automaattisesti)
manager = FoundryLocalManager("phi-4-mini")

# Määritä OpenAI-asiakas
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Testaa chatin täydennys
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Odotettu tulos**: Tervehdysvastaus paikalliselta mallilta.

---

## 📝 Työpajan parhaat käytännöt

### Ohjaajille

**Ennen työpajaa**:
- ✅ Lähetä asennusohjeet 1 viikkoa etukäteen
- ✅ Testaa kaikki notebookit kohdelaitteistolla
- ✅ Valmistele vianmääritysohje yleisiin ongelmiin
- ✅ Varaa varamalleja valmiiksi (phi-3.5-mini, jos phi-4-mini epäonnistuu)
- ✅ Perusta yhteinen chat-kanava kysymyksiä varten

**Työpajan aikana**:
- ✅ Aloita nopealla ympäristötarkistuksella (5 minuuttia)
- ✅ Jaa vianmääritysmateriaalit heti
- ✅ Kannusta kokeiluihin ja muokkauksiin
- ✅ Käytä taukoja strategisesti (jokaisen kahden istunnon jälkeen)
- ✅ TAs (oppaiden avustajat) valmiina yksilöapuun

**Työpajan jälkeen**:
- ✅ Jaa valmiit notebookit ja ratkaisut
- ✅ Tarjoa linkkejä lisäresursseihin
- ✅ Luo palaute-kysely parannuksia varten
- ✅ Tarjoa toimistoaikoja jatkokysymyksiä varten

### Oppijoille

**Optimoi oppimisesi**:
- ✅ Suorita asennus valmiiksi ennen työpajan alkua
- ✅ Suorita jokainen koodisolu itse (älä pelkästään lue)
- ✅ Kokeile parametreja ja kehotteita
- ✅ Tee muistiinpanoja oivalluksista ja huomioista
- ✅ Kysy apua, jos jumitut (muutkin voivat olla samassa tilanteessa)

**Yleiset sudenkuopat**:
- ❌ Ohita solujen suoritusjärjestys (suorita järjestyksessä)
- ❌ Älä jätä virheilmoituksia huomiotta
- ❌ Älä kiirehdi ymmärtämättä
- ❌ Älä jätä markdown-selityksiä lukematta
- ❌ Älä unohda tallentaa muokattuja notebookejasi

**Virheenkorjausvinkkejä**:
1. **Palvelu ei käynnissä**: Tarkista `foundry service status`
2. **Tuontivirheet**: Varmista, että virtuaaliympäristö on aktivoitu
3. **Mallia ei löydy**: Suorita `foundry model ls` ladattujen mallien listaamiseksi
4. **Hidas suorituskyky**: Tarkista RAM-käyttö, sulje muut sovellukset
5. **Odottamattomat tulokset**: Käynnistä kernel uudelleen ja suorita kaikki solut alusta alkaen

---

## 🔗 Lisäresurssit

### Työpajamateriaalit

- **[Työpajan pääopas](../Readme.md)** - Yleiskatsaus, oppimistavoitteet, uratulokset
- **[Python-esimerkit](../../../../Workshop/samples)** - Vastaavat Python-skriptit kuhunkin istuntoon
- **[Istunto-oppaat](../../../../Workshop)** - Yksityiskohtaiset markdown-oppaat (Session01-06)
- **[Skriptit](../../../../Workshop/scripts)** - Vahvistus- ja testausvälineet
- **[Vianmääritys](./TROUBLESHOOTING.md)** - Yleiset ongelmat ja ratkaisut
- **[Pika-aloitus](./quickstart.md)** - Nopeutettu aloitusopas

### Dokumentaatio

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Virallinen Microsoftin dokumentaatio
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK -viite
- **[Sentence Transformers](https://www.sbert.net/)** - Upotemallien dokumentaatio
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG-arviointimittarit

### Yhteisö

- **[GitHub Keskustelut](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Kysy kysymyksiä, jaa projekteja
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Reaaliaikainen yhteisötuki
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Tekninen Q&A

---

## 🎯 Oppimispolun suositukset

### Aloittelijan polku (aloita tästä)

1. **Istunto 01** - Chat Bootstrap
2. **Istunto 02** - RAG-putkisto
3. **Istunto 03** - Vertailumallit

**Aika**: ~2 tuntia | **Painotus**: Peruskuviot

---

### Keskitaso-polku

1. Suorita aloittelijan polku
2. **Istunto 02** - RAG-arviointi
3. **Istunto 04** - Mallien vertailu

**Aika**: ~4 tuntia | **Painotus**: Laatu ja optimointi

---

### Edistynyt polku (kokonainen työpaja)

1. Suorita keskitason polku
2. **Istunto 05** - Moni-agenttien orkestroija
3. **Istunto 06** - Mallien reititin
4. **Istunto 06** - Monivaiheinen putkisto

**Aika**: ~6 tuntia | **Painotus**: Tuotantokuviot

---

### Räätälöity projektipolku

1. Suorita aloittelijan polku (Istunnot 01-03)
2. Valitse YKSI edistynyt istunto tavoitteesi mukaan:
   - **RAG-sovelluksen rakentaminen?** → Istunto 02 Arviointi
   - **Suorituskyvyn optimointi?** → Istunto 04 Vertailu
   - **Monimutkaiset työnkulut?** → Istunto 05 Orkestroija
   - **Skaalautuva arkkitehtuuri?** → Istunto 06 Reititin + Putkisto

**Aika**: ~3 tuntia | **Painotus**: Projektikohtaiset taidot

---

## 📊 Menestyksen mittarit

Seuraa etenemistäsi näillä virstanpylväillä:

- [ ] **Asennus valmis** - Foundry Local käynnissä, kaikki riippuvuudet asennettu
- [ ] **Ensimmäinen chat** - Istunto 01 suoritettu, suoratoistokeskustelu toimii
- [ ] **RAG rakennettu** - Istunto 02 suoritettu, dokumenttien QA-järjestelmä toiminnassa
- [ ] **Mallit vertailtu** - Istunto 03 suoritettu, suorituskykytiedot kerätty
- [ ] **Kompromissit analysoitu** - Istunto 04 suoritettu, mallien valintakriteerit dokumentoitu
- [ ] **Agentit orkestroitu** - Istunto 05 suoritettu, moni-agenttijärjestelmä toimii
- [ ] **Reititys toteutettu** - Istunto 06 suoritettu, älykäs mallinvalinta toiminnassa
- [ ] **Räätälöity projekti** - Sovellettu työpajan kuviot omaan käyttötapaukseen

---

## 🤝 Osallistuminen

Löysitkö ongelman tai onko sinulla ehdotus? Otamme mielellämme vastaan osallistumisia!

- **Raportoi ongelmista**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Ehdota parannuksia**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Lähetä PR:itä**: Noudata [Osallistumisohjeita](../../AGENTS.md)

---

## 📄 Lisenssi

Tämä työpaja on osa [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) -repositorion kokonaisuutta ja on lisensoitu [MIT-lisenssillä](../../../../LICENSE).

---

**Valmis rakentamaan tuotantovalmiita reunalaskenta-AI-sovelluksia?**  
**Aloita [Istunnosta 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Viimeksi päivitetty: 8. lokakuuta 2025 | Työpajan versio: 2.0*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->