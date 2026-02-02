# Workshop-muistikirjat

> **Interaktiiviset Jupyter-muistikirjat käytännön Edge AI -oppimiseen**
>
> Edistykselliset, omaan tahtiin etenevät opetusmateriaalit, jotka siirtyvät perus chat-vastauksista kehittyneisiin monen agentin järjestelmiin Microsoft Foundry Localin ja Small Language Models -mallien avulla.

---

## 📖 Johdanto

Tervetuloa **EdgeAI for Beginners Workshop Notebooks** -kokoelmaan. Nämä interaktiiviset Jupyter-muistikirjat tarjoavat käytännönläheisen oppimiskokemuksen, jossa voit kirjoittaa, suorittaa ja kokeilla Edge AI -koodia reaaliajassa.

### Miksi Jupyter-muistikirjat?

Perinteisistä opetusmateriaaleista poiketen nämä muistikirjat tarjoavat:

- **Interaktiivista oppimista**: Suorita koodisoluja ja näe tulokset heti
- **Kokeilua**: Muokkaa parametreja ja tarkkaile muutoksia reaaliajassa
- **Dokumentaatiota**: Sisäiset selitykset ja markdown-solut ohjaavat sinua käsitteiden läpi
- **Toistettavuutta**: Täydellisiä toimivia esimerkkejä, joita voit käyttää uudelleen
- **Visualisointia**: Näe suorituskykymittarit, upotukset ja tulokset suoraan muistikirjassa

### Mikä tekee näistä muistikirjoista erityisiä?

Jokainen muistikirja on suunniteltu **tuotantovalmiiden parhaiden käytäntöjen** mukaisesti:

✅ **Kattava virheenkäsittely** - Sulava toiminta ja informatiiviset virheilmoitukset  
✅ **Tyyppivihjeet ja dokumentaatio** - Selkeät funktiosignatuurit ja docstringit  
✅ **Suorituskyvyn seuranta** - Tokenien käytön seuranta ja viiveen mittaus  
✅ **Modulaarinen suunnittelu** - Uudelleenkäytettäviä malleja, joita voit mukauttaa projekteihisi  
✅ **Progressiivinen monimutkaisuus** - Rakentuu systemaattisesti aiempien sessioiden pohjalta  

---

## 🎯 Oppimistavoitteet

### Keskeiset taidot, joita kehität

Työskennellessäsi näiden muistikirjojen parissa opit hallitsemaan:

1. **Paikallisen AI-palvelun hallinta**
   - Konfiguroi ja hallitse Microsoft Foundry Local -palveluita
   - Valitse ja lataa sopivat mallit laitteistosi mukaan
   - Seuraa resurssien käyttöä ja optimoi suorituskykyä
   - Käsittele palveluiden etsintää ja tilan tarkistusta

2. **AI-sovellusten kehittäminen**
   - Toteuta OpenAI-yhteensopivia chat-vastauksia paikallisesti
   - Rakenna suoratoistokäyttöliittymiä paremman käyttäjäkokemuksen saavuttamiseksi
   - Suunnittele tehokkaita kehotteita Small Language Models -malleille
   - Integroi paikalliset mallit sovelluksiin

3. **Hakupohjainen generointi (RAG)**
   - Luo semanttinen haku vektoriupotuksilla
   - Perusta LLM-vastaukset alakohtaisiin dokumentteihin
   - Arvioi RAG:n laatua RAGAS-mittareilla
   - Skaalaa prototyypistä tuotantoon

4. **Suorituskyvyn optimointi**
   - Vertaa useita malleja systemaattisesti
   - Mittaa viive, läpäisykyky ja ensimmäisen tokenin aika
   - Vertaa Small Language Models -malleja Large Language Models -malleihin
   - Valitse optimaaliset mallit suorituskyvyn/laadun kompromissien perusteella

5. **Monen agentin orkestrointi**
   - Suunnittele erikoistuneita agentteja eri tehtäviin
   - Toteuta agenttimuisti ja kontekstinhallinta
   - Koordinoi useita agentteja monimutkaisissa työnkuluissa
   - Rakenna koordinaattorimalleja agenttien yhteistyöhön

6. **Älykäs mallien reititys**
   - Toteuta tarkoituksen tunnistus ja mallien sovittaminen
   - Reititä kyselyt automaattisesti sopiville malleille
   - Rakenna monivaiheisia putkistoja (suunnittele → suorita → tarkenna)
   - Suunnittele skaalautuvia malli-työkalu-arkkitehtuureja

---

## 🎓 Oppimistulokset

### Mitä rakennat

| Muistikirja | Lopputulos | Osoitetut taidot | Vaikeusaste |
|-------------|------------|------------------|-------------|
| **Session 01** | Chat-sovellus suoratoistolla | Palvelun asennus, perusvastaukset, suoratoistokäyttöliittymä | ⭐ Aloittelija |
| **Session 02 (RAG)** | RAG-putkisto arvioinnilla | Upotukset, semanttinen haku, laatumittarit | ⭐⭐ Keskitaso |
| **Session 02 (Eval)** | RAG-laadun arvioija | RAGAS-mittarit, systemaattinen arviointi | ⭐⭐ Keskitaso |
| **Session 03** | Monimallivertailu | Suorituskyvyn mittaus, mallien vertailu | ⭐⭐ Keskitaso |
| **Session 04** | SLM vs LLM vertailija | Kompromissianalyysi, optimointistrategiat | ⭐⭐⭐ Edistynyt |
| **Session 05** | Monen agentin orkestroija | Agenttisuunnittelu, muisti, koordinointi | ⭐⭐⭐ Edistynyt |
| **Session 06 (Router)** | Älykäs reititysjärjestelmä | Tarkoituksen tunnistus, mallivalinta | ⭐⭐⭐ Edistynyt |
| **Session 06 (Pipeline)** | Monivaiheinen putkisto | Suunnittele/suorita/tarkenna työnkulut | ⭐⭐⭐ Edistynyt |

### Osaamisen eteneminen

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Workshop-aikataulu

### 🚀 Puolen päivän workshop (3,5 tuntia)

**Sopii: Tiimikoulutuksiin, hackathoneihin, konferenssityöpajoihin**

| Aika | Kesto | Sessio | Aiheet | Aktiviteetit |
|------|-------|--------|-------|-------------|
| **0:00** | 30 min | Asennus & Johdanto | Ympäristön asennus, Foundry Local -asennus | Asenna riippuvuudet, varmista asennus |
| **0:30** | 30 min | Session 01 | Perus chat-vastaukset, suoratoisto | Suorita muistikirja, muokkaa kehotteita |
| **1:00** | 45 min | Session 02 | RAG-putkisto, upotukset, arviointi | Rakenna RAG-järjestelmä, testaa kyselyitä |
| **1:45** | 15 min | Tauko | ☕ Kahvia & kysymyksiä | — |
| **2:00** | 30 min | Session 03 | Monimallivertailu | Vertaa 3+ mallia |
| **2:30** | 30 min | Session 04 | SLM vs LLM kompromissit | Analysoi suorituskyky/laatu |
| **3:00** | 30 min | Session 05-06 | Monen agentin järjestelmät & reititys | Tutki edistyneitä malleja |

**Lopputulos**: Osallistujat lähtevät 6 toimivan Edge AI -sovelluksen ja tuotantovalmiiden koodimallien kanssa.

---

### 🎓 Koko päivän workshop (6 tuntia)

**Sopii: Syvälliseen koulutukseen, bootcampiin, yliopistokursseihin**

| Aika | Kesto | Sessio | Aiheet | Aktiviteetit |
|------|-------|--------|-------|-------------|
| **0:00** | 45 min | Asennus & Teoria | Ympäristön asennus, Edge AI perusteet | Asenna, varmista, keskustele käyttötapauksista |
| **0:45** | 45 min | Session 01 | Chat-vastausten syväluotaus | Toteuta perus- ja suoratoistochat |
| **1:30** | 30 min | Tauko | ☕ Kahvia & verkostoitumista | — |
| **2:00** | 60 min | Session 02 (Molemmat) | RAG-putkisto + RAGAS-arviointi | Rakenna täydellinen RAG-järjestelmä |
| **3:00** | 30 min | Käytännön harjoitus 1 | Mukautettu RAG omalle alallesi | Sovella omiin dokumentteihin |
| **3:30** | 30 min | Lounas | 🍽️ | — |
| **4:00** | 45 min | Session 03 | Vertailumenetelmät | Systemaattinen mallivertailu |
| **4:45** | 45 min | Session 04 | Optimointistrategiat | SLM vs LLM analyysi |
| **5:30** | 60 min | Session 05-06 | Edistynyt orkestrointi | Monen agentin järjestelmät, reititys |
| **6:30** | 30 min | Käytännön harjoitus 2 | Rakenna mukautettu agenttijärjestelmä | Suunnittele oma orkestroija |

**Lopputulos**: Syvällinen ymmärrys Edge AI -malleista sekä 2 mukautettua projektia.

---

### 📚 Omaehtoinen oppiminen (2 viikkoa)

**Sopii: Yksilöoppijoille, verkkokursseille, itseopiskeluun**

#### Viikko 1: Perusteet (6 tuntia)

| Päivä | Painopiste | Kesto | Muistikirjat | Kotitehtävät |
|-------|------------|-------|--------------|-------------|
| **Ma** | Asennus & Perusteet | 1,5 h | Session 01 | Muokkaa kehotteita, testaa suoratoistoa |
| **Ke** | RAG-perusteet | 2 h | Session 02 (molemmat) | Lisää omia dokumentteja |
| **Pe** | Vertailu | 1,5 h | Session 03 | Vertaa lisämalleja |
| **La** | Kertaus & Harjoittelu | 1 h | Kaikki Viikko 1 | Tee harjoituksia, korjaa virheitä |

#### Viikko 2: Edistynyt (5 tuntia)

| Päivä | Painopiste | Kesto | Muistikirjat | Kotitehtävät |
|-------|------------|-------|--------------|-------------|
| **Ma** | Optimointi | 1,5 h | Session 04 | Dokumentoi kompromissit |
| **Ke** | Monen agentin järjestelmät | 2 h | Session 05 | Suunnittele mukautettuja agentteja |
| **Pe** | Älykäs reititys | 1,5 h | Session 06 (molemmat) | Rakenna reitityslogiikka |
| **La** | Lopullinen projekti | 2 h | Integraatio | Yhdistä useita malleja |

**Lopputulos**: Edge AI -mallien hallinta sekä portfolioprojekti.

---

## 📔 Muistikirjojen kuvaukset

### 📘 Session 01: Chat Bootstrap
**Tiedosto**: `session01_chat_bootstrap.ipynb`  
**Kesto**: 20-30 minuuttia  
**Edellytykset**: Ei mitään  
**Vaikeusaste**: ⭐ Aloittelija

**Mitä opit**:
- Asenna ja konfiguroi Foundry Local Python SDK
- Käytä `FoundryLocalManager`-työkalua automaattiseen palvelun etsintään
- Toteuta perus chat-vastaukset OpenAI-yhteensopivalla API:lla
- Rakenna suoratoistovastauksia paremman käyttäjäkokemuksen saavuttamiseksi
- Käsittele virheitä ja palvelun saatavuusongelmia sulavasti

**Keskeiset käsitteet**: Palvelun hallinta, chat-vastaukset, suoratoisto, virheenkäsittely

**Mitä rakennat**: Interaktiivinen chat-sovellus suoratoistotuella

---

### 📗 Session 02: RAG-putkisto
**Tiedosto**: `session02_rag_pipeline.ipynb`  
**Kesto**: 30-45 minuuttia  
**Edellytykset**: Session 01  
**Vaikeusaste**: ⭐⭐ Keskitaso

**Mitä opit**:
- Toteuta Retrieval Augmented Generation (RAG) -malli
- Luo vektoriupotuksia sentence-transformers-kirjastolla
- Rakenna semanttinen haku kosinisimilaarisuudella
- Perusta LLM-vastaukset alakohtaisiin dokumentteihin
- Käsittele valinnaisia riippuvuuksia import guards -menetelmällä

**Keskeiset käsitteet**: RAG-arkkitehtuuri, upotukset, semanttinen haku, vektorisimilaarisuus

**Mitä rakennat**: Dokumenttipohjainen kysymys-vastausjärjestelmä

---

### 📗 Session 02: RAG-arviointi RAGAS:lla
**Tiedosto**: `session02_rag_eval_ragas.ipynb`  
**Kesto**: 30-45 minuuttia  
**Edellytykset**: Session 02 RAG-putkisto  
**Vaikeusaste**: ⭐⭐ Keskitaso

**Mitä opit**:
- Arvioi RAG:n laatua alan standardimittareilla
- Mittaa kontekstin relevanssia, vastauksen relevanssia, uskottavuutta
- Käytä RAGAS-kehystä systemaattiseen arviointiin
- Tunnista ja korjaa RAG:n laatuongelmat
- Rakenna arviointidatasetit omalle alallesi

**Keskeiset käsitteet**: RAG-arviointi, RAGAS-mittarit, laadun mittaus, systemaattinen testaus

**Mitä rakennat**: RAG-laadun arviointikehys

---

### 📙 Session 03: OSS-mallien vertailu
**Tiedosto**: `session03_benchmark_oss_models.ipynb`  
**Kesto**: 30-45 minuuttia  
**Edellytykset**: Session 01  
**Vaikeusaste**: ⭐⭐ Keskitaso

**Mitä opit**:
- Vertaa useita malleja systemaattisesti
- Mittaa viive, läpäisykyky, ensimmäisen tokenin aika
- Toteuta sulava toiminta mallien epäonnistuessa
- Vertaa suorituskykyä eri malliperheiden välillä
- Visualisoi ja analysoi vertailutuloksia

**Keskeiset käsitteet**: Suorituskyvyn vertailu, viiveen mittaus, mallien vertailu, tilastollinen analyysi

**Mitä rakennat**: Monimallivertailuohjelmisto

---

### 📙 Session 04: Mallivertailu (SLM vs LLM)
**Tiedosto**: `session04_model_compare.ipynb`  
**Kesto**: 30-45 minuuttia  
**Edellytykset**: Session 01, 03  
**Vaikeusaste**: ⭐⭐⭐ Edistynyt

**Mitä opit**:
- Vertaa Small Language Models -malleja Large Language Models -malleihin
- Analysoi suorituskyvyn ja laadun kompromisseja
- Mittaa edge-soveltuvuuden mittareita
- Valitse optimaaliset mallit käyttöönoton rajoitteiden mukaan
- Dokumentoi päätöskriteerit mallivalinnalle

**Keskeiset käsitteet**: Mallivalinta, kompromissianalyysi, optimointistrategiat, käyttöönoton suunnittelu

**Mitä rakennat**: SLM vs LLM vertailukehys

---

### 📕 Session 05: Monen agentin orkestroija
**Tiedosto**: `session05_agents_orchestrator.ipynb`  
**Kesto**: 45-60 minuuttia  
**Edellytykset**: Session 01-02  
**Vaikeusaste**: ⭐⭐⭐ Edistynyt

**Mitä opit**:
- Suunnittele erikoistuneita agentteja eri tehtäviin
- Toteuta agenttimuisti ja kontekstinhallinta
- Rakenna koordinaattorimalleja agenttien yhteistyöhön
- Käsittele agenttien välistä viestintää ja siirtoja
- Seuraa monen agentin järjestelmän suorituskykyä

**Keskeiset käsitteet**: Agenttiarkkitehtuuri, koordinaattorimallit, muistinhallinta, agenttien orkestrointi

**Mitä rakennat**: Monen agentin järjestelmä koordinaattorilla ja erikoistuneilla agenteilla

---

### 📕 Session 06: Mallien reititys
**Tiedosto**: `session06_models_router.ipynb`  
**Kesto**: 30-45 minuuttia  
**Edellytykset**:
- Suunnittele skaalautuvia mallityökaluarkkitehtuureja

**Keskeiset käsitteet**: Putkistoarkkitehtuuri, monivaiheinen käsittely, virheiden korjaus, skaalautuvuuden mallit

**Rakennat**: Monivaiheinen älykäs putkisto reitityksellä

---

## 🚀 Aloitus

### Esivaatimukset

**Järjestelmävaatimukset**:
- **Käyttöjärjestelmä**: Windows 10/11, macOS 11+ tai Linux (Ubuntu 20.04+)
- **RAM**: Vähintään 8GB, suositus 16GB+
- **Tallennustila**: Vähintään 10GB vapaata tilaa malleille
- **Laitteisto**: CPU, jossa AVX2; GPU (CUDA, Qualcomm NPU) valinnainen

**Ohjelmistovaatimukset**:
- **Python 3.8+** ja pip
- **Jupyter Notebook** tai **VS Code** Jupyter-laajennuksella
- **Microsoft Foundry Local** asennettuna ja konfiguroituna
- **Git** (repositoryn kloonaamiseen)

### Asennusohjeet

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

**Varmista asennus**:
```bash
foundry --version
```

#### 2. Määritä Python-ympäristö

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Käynnistä Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Käynnistä Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Nopea tarkistus

Suorita tämä Python-solussa varmistaaksesi asennuksen:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Odotettu tulos**: Tervehdysviesti paikalliselta mallilta.

---

## 📝 Työpajan parhaat käytännöt

### Ohjaajille

**Ennen työpajaa**:
- ✅ Lähetä asennusohjeet viikkoa etukäteen
- ✅ Testaa kaikki notebookit kohdelaitteistolla
- ✅ Valmistele vianetsintäopas yleisille ongelmille
- ✅ Pidä varamallit valmiina (phi-3.5-mini, jos phi-4-mini epäonnistuu)
- ✅ Perusta yhteinen keskustelukanava kysymyksille

**Työpajan aikana**:
- ✅ Aloita nopealla ympäristön tarkistuksella (5 minuuttia)
- ✅ Jaa vianetsintäresurssit heti
- ✅ Kannusta kokeiluun ja muokkauksiin
- ✅ Hyödynnä taukoja strategisesti (joka toinen sessio)
- ✅ Pidä apuohjaajia saatavilla henkilökohtaiseen tukeen

**Työpajan jälkeen**:
- ✅ Jaa täydelliset toimivat notebookit ja ratkaisut
- ✅ Tarjoa linkkejä lisäresursseihin
- ✅ Luo palautekysely parannuksia varten
- ✅ Tarjoa toimistoaikoja jatkokysymyksille

### Oppijoille

**Maksimoi oppimisesi**:
- ✅ Suorita asennus ennen työpajan alkua
- ✅ Suorita jokainen koodisolu itse (älä vain lue)
- ✅ Kokeile parametreja ja kehotteita
- ✅ Kirjaa ylös oivallukset ja haasteet
- ✅ Kysy kysymyksiä, kun jäät jumiin (muillakin voi olla sama kysymys)

**Vältä yleisiä virheitä**:
- ❌ Solujen suoritusjärjestyksen ohittaminen (suorita järjestyksessä)
- ❌ Virheilmoitusten huomiotta jättäminen
- ❌ Kiirehtiminen ilman ymmärrystä
- ❌ Markdown-selitysten sivuuttaminen
- ❌ Muokattujen notebookien tallentamatta jättäminen

**Vianetsintävinkit**:
1. **Palvelu ei käynnissä**: Tarkista `foundry service status`
2. **Tuontivirheet**: Varmista, että virtuaaliympäristö on aktivoitu
3. **Mallia ei löydy**: Suorita `foundry model ls` ladattujen mallien listaamiseksi
4. **Hidas suorituskyky**: Tarkista RAM-käyttö, sulje muita sovelluksia
5. **Odottamattomat tulokset**: Käynnistä kernel uudelleen ja suorita kaikki solut alusta

---

## 🔗 Lisäresurssit

### Työpajamateriaalit

- **[Työpajan pääopas](../Readme.md)** - Yleiskatsaus, oppimistavoitteet, uratulokset
- **[Python-esimerkit](../../../../Workshop/samples)** - Vastaavat Python-skriptit jokaiselle sessiolle
- **[Sessio-oppaat](../../../../Workshop)** - Yksityiskohtaiset markdown-oppaat (Session01-06)
- **[Skriptit](../../../../Workshop/scripts)** - Validointi- ja testausapuvälineet
- **[Vianetsintä](./TROUBLESHOOTING.md)** - Yleiset ongelmat ja ratkaisut
- **[Pikaopas](./quickstart.md)** - Nopean aloituksen opas

### Dokumentaatio

- **[Foundry Local -dokumentaatio](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Microsoftin virallinen dokumentaatio
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK:n viite
- **[Sentence Transformers](https://www.sbert.net/)** - Upotusmallien dokumentaatio
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG-arviointimetriikat

### Yhteisö

- **[GitHub-keskustelut](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Kysy kysymyksiä, jaa projekteja
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Reaaliaikainen yhteisötuki
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Tekninen Q&A

---

## 🎯 Oppimispolun suositukset

### Aloittelijapolku (Aloita tästä)

1. **Sessio 01** - Chat Bootstrap
2. **Sessio 02** - RAG-putkisto
3. **Sessio 03** - Mallien vertailu

**Aika**: ~2 tuntia | **Painopiste**: Perusmallit

---

### Keskitaso

1. Suorita aloittelijapolku
2. **Sessio 02** - RAG-arviointi
3. **Sessio 04** - Mallien vertailu

**Aika**: ~4 tuntia | **Painopiste**: Laatu ja optimointi

---

### Edistynyt polku (Koko työpaja)

1. Suorita keskitaso
2. **Sessio 05** - Multi-Agent Orchestrator
3. **Sessio 06** - Mallireititin
4. **Sessio 06** - Monivaiheinen putkisto

**Aika**: ~6 tuntia | **Painopiste**: Tuotantomallit

---

### Räätälöity projektipolku

1. Suorita aloittelijapolku (Sessionit 01-03)
2. Valitse YKSI edistynyt sessio tavoitteesi mukaan:
   - **RAG-sovelluksen rakentaminen?** → Sessio 02 Arviointi
   - **Suorituskyvyn optimointi?** → Sessio 04 Vertailu
   - **Monimutkaiset työnkulut?** → Sessio 05 Orchestrator
   - **Skaalautuva arkkitehtuuri?** → Sessio 06 Reititin + Putkisto

**Aika**: ~3 tuntia | **Painopiste**: Projektikohtaiset taidot

---

## 📊 Menestysmittarit

Seuraa edistymistäsi näillä virstanpylväillä:

- [ ] **Asennus valmis** - Foundry Local käynnissä, kaikki riippuvuudet asennettu
- [ ] **Ensimmäinen chat** - Sessio 01 suoritettu, chat-virtaus toimii
- [ ] **RAG rakennettu** - Sessio 02 suoritettu, dokumentti-QA-järjestelmä toiminnassa
- [ ] **Mallit vertailtu** - Sessio 03 suoritettu, suorituskykytiedot kerätty
- [ ] **Kaupan analysointi** - Sessio 04 suoritettu, mallin valintakriteerit dokumentoitu
- [ ] **Agentit orkestroitu** - Sessio 05 suoritettu, monen agentin järjestelmä toimii
- [ ] **Reititys toteutettu** - Sessio 06 suoritettu, älykäs mallin valinta toiminnassa
- [ ] **Räätälöity projekti** - Työpajan mallit sovellettu omaan käyttötapaukseen

---

## 🤝 Osallistuminen

Huomasitko ongelman tai sinulla on ehdotus? Otamme mielellämme vastaan parannuksia!

- **Ilmoita ongelmista**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Ehdota parannuksia**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Lähetä PR:t**: Noudata [Osallistumisohjeita](../../AGENTS.md)

---

## 📄 Lisenssi

Tämä työpaja on osa [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) -repositorya ja lisensoitu [MIT-lisenssillä](../../../../LICENSE).

---

**Valmis rakentamaan tuotantovalmiita Edge AI -sovelluksia?**  
**Aloita [Sessio 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Viimeksi päivitetty: 8. lokakuuta 2025 | Työpajan versio: 2.0*

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.