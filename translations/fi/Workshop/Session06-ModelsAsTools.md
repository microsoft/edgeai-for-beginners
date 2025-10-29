<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T22:20:16+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "fi"
}
-->
# Istunto 6: Foundry Local – Mallit työkaluina

## Tiivistelmä

Käsittele malleja yhdisteltävinä työkaluina paikallisessa AI-toimintakerroksessa. Tässä istunnossa näytetään, kuinka ketjutetaan useita erikoistuneita SLM/LLM-kutsuja, ohjataan tehtäviä valikoivasti ja tarjotaan yhtenäinen SDK-pinta sovelluksille. Rakennat kevyen malliohjaimen + tehtäväsuunnittelijan, integroit sen sovellusskriptiin ja hahmottelet skaalautumispolun Azure AI Foundryyn tuotantokuormituksia varten.

## Oppimistavoitteet

- **Hahmota** mallit atomisina työkaluina, joilla on määritellyt kyvykkyydet
- **Ohjaa** pyyntöjä aikomuksen / heuristisen pisteytyksen perusteella
- **Ketjuta** tuloksia monivaiheisissa tehtävissä (pilko → ratkaise → tarkenna)
- **Integroi** yhtenäinen asiakas-API jatkosovelluksille
- **Skaalaa** suunnittelu pilveen (sama OpenAI-yhteensopiva sopimus)

## Esivaatimukset

- Istunnot 1–5 suoritettu
- Useita paikallisia malleja välimuistissa (esim. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Monialustainen ympäristön koodinpätkä

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Etä-/VM-palvelimen käyttö macOS:sta:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Työkalujen kyvykkyyksien määrittely (5 min)

Luo `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Aikomuksen tunnistus ja ohjaus (8 min)

Luo `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Monivaiheinen tehtäväketjutus (7 min)

Luo `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Aloitusprojekti: Mukauta `06-models-as-tools` (5 min)

Parannukset:
- Lisää suoratoistotokenien tuki (progressiivinen käyttöliittymän päivitys)
- Lisää luottamuspisteytys: leksikaalinen päällekkäisyys tai kehotteen arviointikriteerit
- Vie jäljityksen JSON (aikomus → malli → viive → tokenien käyttö)
- Toteuta välimuistin uudelleenkäyttö toistuville alavaiheille

### 5. Skaalautumispolku Azureen (5 min)

| Kerros | Paikallinen (Foundry) | Pilvi (Azure AI Foundry) | Siirtymistrategia |
|--------|------------------------|--------------------------|-------------------|
| Ohjaus | Heuristinen Python | Kestävä mikropalvelu | Säilöi ja ota käyttöön API |
| Mallit | SLM:t välimuistissa | Hallinnoidut käyttöönotot | Kartta paikalliset nimet käyttöönotto-ID:ihin |
| Havainnointi | CLI-tilastot/manuaalinen | Keskitetty lokitus ja metrikat | Lisää rakenteelliset jäljitystapahtumat |
| Turvallisuus | Vain paikallinen isäntä | Azure-todennus / verkostoituminen | Ota käyttöön avainholvi salaisuuksille |
| Kustannukset | Laitteiston resurssi | Kulutuslaskutus | Lisää budjettivartijat |

## Vahvistuslista

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Odotetaan aikomukseen perustuvaa mallin valintaa ja lopullista tarkennettua tulosta.

## Vianetsintä

| Ongelma | Syynä | Korjaus |
|---------|-------|---------|
| Kaikki tehtävät ohjataan samaan malliin | Heikot säännöt | Rikkaampien INTENT_RULES regex-sääntöjen lisääminen |
| Putki epäonnistuu kesken vaiheen | Puuttuva malli ladattu | Suorita `foundry model run <model>` |
| Matala tulosten yhtenäisyys | Ei tarkennusvaihetta | Lisää tiivistämis-/tarkistusvaihe |

## Viitteet

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry -dokumentaatio: https://learn.microsoft.com/azure/ai-foundry
- Kehotelaadun mallit: Katso istunto 2

---

**Istunnon kesto**: 30 min  
**Vaikeustaso**: Vaativa

## Esimerkkiskenaario ja työpajan kartoitus

| Työpajan skriptit / muistikirjat | Skenaario | Tavoite | Datasetti / katalogin lähde |
|----------------------------------|-----------|---------|-----------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Kehittäjäassistentti, joka käsittelee sekalaisten aikomusten kehotteita (uudelleenjärjestely, tiivistäminen, luokittelu) | Heuristinen aikomus → mallin alias-ohjaus tokenien käytöllä | Sisäinen `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Monivaiheinen suunnittelu ja tarkennus monimutkaisessa koodausavustustehtävässä | Pilko → erikoistunut suoritus → tiivistämisen tarkennusvaihe | Sama `CATALOG`; vaiheet johdettu suunnitelman tuloksesta |

### Skenaarion kuvaus
Tuottavuustyökalu insinööreille vastaanottaa monenlaisia tehtäviä: koodin uudelleenjärjestely, arkkitehtuurimuistiinpanojen tiivistäminen, palautteen luokittelu. Viiveen ja resurssien käytön minimoimiseksi pieni yleismalli suunnittelee ja tiivistää, koodiin erikoistunut malli hoitaa uudelleenjärjestelyn, ja kevyt luokitteluun kykenevä malli merkitsee palautteen. Putkiskripti demonstroi ketjutusta + tarkennusta; ohjausskripti eristää mukautuvan yksittäisen kehotteen ohjauksen.

### Katalogin tilannekuva
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Esimerkkikehotteet
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Jäljityksen laajennus (valinnainen)
Lisää vaihekohtaiset jäljitys JSON-rivit `models_pipeline.py`-tiedostoon:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Eskalointiheuristiikka (idea)
Jos suunnitelmassa on avainsanoja kuten "optimoi", "turvallisuus" tai vaiheiden pituus > 280 merkkiä → eskaloi suurempaan malliin (esim. `gpt-oss-20b`) vain kyseistä vaihetta varten.

### Valinnaiset parannukset

| Alue | Parannus | Arvo | Vinkki |
|------|----------|------|--------|
| Välimuisti | Uudelleenkäytä hallinta- ja asiakasobjekteja | Alhaisempi viive, vähemmän kuormitusta | Käytä `workshop_utils.get_client` |
| Käyttömetriikat | Tallenna tokenit & vaihekohtainen viive | Profilointi & optimointi | Aika jokainen ohjattu kutsu; tallenna jäljityslistaan |
| Mukautuva ohjaus | Luottamus-/kustannustietoisuus | Parempi laatu-kustannus-suhde | Lisää pisteytys: jos kehotteen pituus > N merkkiä tai regex vastaa alaa → eskaloi suurempaan malliin |
| Dynaaminen kyvykkyysrekisteri | Katalogin kuuma lataus | Ei uudelleenkäynnistystä tai käyttöönottoa | Lataa `catalog.json` ajonaikaisesti; seuraa tiedoston aikaleimaa |
| Varautumisstrategia | Vikasietoisuus | Parempi saatavuus | Kokeile ensisijaista → poikkeustilanteessa varalias |
| Suoratoistoputki | Varhainen palaute | Käyttökokemuksen parannus | Suoratoista jokainen vaihe ja puskuroi lopullinen tarkennusinputti |
| Vektoriaikomusten upotukset | Tarkempi ohjaus | Korkeampi aikomustarkkuus | Upota kehotus, klusteroi & kartoita keskipiste → kyvykkyys |
| Jäljityksen vienti | Ketjun auditointi | Vaadittavuus/raportointi | Tuo JSON-rivit: vaihe, aikomus, malli, viive_ms, tokenit |
| Kustannussimulaatio | Pilviarviointi | Budjetin suunnittelu | Määritä mallikohtainen kustannus/token ja yhteenlasku tehtävää kohden |
| Deterministinen tila | Toistettavuus | Vakaa vertailu | Ympäristö: `temperature=0`, kiinteä vaiheiden määrä |

#### Jäljitysrakenteen esimerkki

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Mukautuvan eskaloinnin luonnos

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Mallikatalogin kuuma lataus

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.