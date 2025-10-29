<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T22:17:35+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "fi"
}
-->
# Istunto 5: Rakenna AI-pohjaisia agentteja nopeasti Foundry Localilla

## Tiivistelmä

Suunnittele ja orkestroi moniroolisia AI-agentteja hyödyntäen Foundry Localin matalan viiveen ja yksityisyyttä suojaavaa suoritusympäristöä. Määrität agenttien roolit, muististrategiat, työkalujen kutsumismallit ja suorituskaaviot. Istunto esittelee kehysrakenteita, joita voit laajentaa Chainlitilla tai LangGraphilla. Aloitusprojekti laajentaa olemassa olevaa agenttiarkkitehtuuriesimerkkiä lisäämällä muistinpysyvyys ja arviointikoukut.

## Oppimistavoitteet

- **Määritä roolit**: Järjestelmän kehotteet ja kyvykkyyden rajat
- **Toteuta muisti**: Lyhytaikainen (keskustelu), pitkäaikainen (vektori / tiedosto), tilapäiset muistikirjat
- **Rakenna työnkulkuja**: Peräkkäiset, haarautuvat ja rinnakkaiset agenttivaiheet
- **Integroi työkalut**: Kevyt funktiotyökalujen kutsumismalli
- **Arvioi**: Perusjälki + rubriikkipohjainen tulosten pisteytys

## Esivaatimukset

- Istunnot 1–4 suoritettu
- Python ja `foundry-local-sdk`, `openai`, valinnainen `chainlit`
- Paikalliset mallit käynnissä (vähintään `phi-4-mini`)

### Monialustainen ympäristön pätkä

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Jos agentteja ajetaan macOS:sta etä-Windows-palvelua vastaan:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Määritä agenttien roolit ja muisti (7 min)

Luo `samples/05-agents/agents_core.py`:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. CLI-kehysrakenne (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Lisää työkalujen kutsuminen (7 min)

Laajenna `samples/05-agents/tools.py`:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```

Muokkaa `agents_core.py` sallimaan yksinkertainen työkalusyntaksi: käyttäjä kirjoittaa `#tool:get_time` ja agentti laajentaa työkalun tuloksen kontekstiin ennen generointia.

### 4. Orkestroitu työnkulku (6 min)

Luo `samples/05-agents/orchestrator.py`:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. Aloitusprojekti: Laajenna `05-agent-architecture` (7 min)

Lisää:
1. Pysyvä muistikerros (esim. JSON-rivien lisäys keskusteluista)
2. Yksinkertainen arviointirubriikki: faktuaalisuus / selkeys / tyylin paikat
3. Valinnainen Chainlit-etupää (kaksi välilehteä: keskustelu & jäljet)
4. Valinnainen LangGraph-tyylinen tilakone (jos lisätään riippuvuus) haarautuville päätöksille

## Vahvistuslista

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Odota rakenteellista putkistotulosta työkalujen injektiomerkinnällä.

## Muististrategioiden yleiskatsaus

| Kerros | Tarkoitus | Esimerkki |
|-------|----------|----------|
| Lyhytaikainen | Keskustelun jatkuvuus | Viimeiset N viestit |
| Episodinen | Istunnon muistaminen | JSON per istunto |
| Semanttinen | Pitkäaikainen haku | Yhteenvetojen vektorivarasto |
| Muistikirja | Päättelyvaiheet | Ketjun ajatus (yksityinen) |

## Arviointikoukut (Konseptuaalinen)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Vianetsintä

| Ongelma | Syynä | Ratkaisu |
|--------|-------|---------|
| Toistuvat vastaukset | Kontekstin ikkuna liian suuri/pieni | Säädä muistikkunan parametri |
| Työkalua ei kutsuta | Väärä syntaksi | Käytä `#tool:tool_name` -muotoa |
| Hidas orkestrointi | Useita kylmiä malleja | Esikäynnistä lämpimät kehotteet |

## Viitteet

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (valinnainen konsepti): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Istunnon kesto**: 30 min  
**Vaikeustaso**: Edistynyt

## Esimerkkiskenaario & työpajan kartoitus

| Työpajan skripti | Skenaario | Tavoite | Esimerkkikehote |
|------------------|----------|---------|-----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Tietotutkimusbot tuottaa johtajaystävällisiä yhteenvetoja | Kaksi agenttiputkea (tutkimus → toimituksellinen viimeistely) valinnaisilla erillisillä malleilla | Selitä, miksi reunainferenssi on tärkeää vaatimustenmukaisuudelle. |
| (Laajennettu) `tools.py` -konsepti | Lisää aika- ja token-arviointityökalut | Demonstroi kevyt työkalujen kutsumismalli | #tool:get_time |

### Skenaarion narratiivi
Vaatimustenmukaisuusdokumentaatiotiimi tarvitsee nopeita sisäisiä tiivistelmiä, jotka on kerätty paikallisesta tiedosta ilman luonnosten lähettämistä pilvipalveluihin. Tutkimusagentti kerää tiiviitä faktapisteitä; toimittajaagentti muotoilee ne johtajille selkeäksi. Erilliset mallialiasit voidaan määrittää optimoimaan viive (nopea SLM) vs tyylillinen viimeistely (suurempi malli vain tarvittaessa).

### Esimerkki monimalliympäristöstä
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Jälkirakenne (Valinnainen)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

Tallenna jokainen vaihe JSONL-tiedostoon myöhempää rubriikkipisteytystä varten.

### Valinnaiset parannukset

| Teema | Parannus | Hyöty | Toteutussuunnitelma |
|-------|----------|-------|--------------------|
| Monimalliroolit | Erilliset mallit per agentti (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Erikoistuminen & nopeus | Valitse alias-ympäristömuuttujat, kutsu `chat_once` roolikohtaisella aliasilla |
| Rakenteelliset jäljet | Jokaisen toiminnon (työkalu, syöte, viive, tokenit) JSON-jälki | Vianetsintä & arviointi | Lisää sanakirja listaan; kirjoita `.jsonl` lopussa |
| Muistin pysyvyys | Latautuva keskustelukonteksti | Istunnon jatkuvuus | Tallenna `Agent.memory` tiedostoon `sessions/<ts>.json` |
| Työkalurekisteri | Dynaaminen työkalujen haku | Laajennettavuus | Ylläpidä `TOOLS`-sanakirjaa ja tarkista nimet/kuvaukset |
| Uudelleenyritä & viive | Kestävä pitkissä ketjuissa | Vähennä tilapäisiä virheitä | Kääri `act` try/except + eksponentiaalinen viive |
| Rubriikkipisteytys | Automaattiset laadulliset merkinnät | Seuraa parannuksia | Toissijainen kehotusmalli: "Arvioi selkeys 1-5" |
| Vektori-muisti | Semanttinen haku | Rikas pitkäaikainen konteksti | Upota yhteenvedot, hae top-k järjestelmäsanomaan |
| Suoratoistovastaukset | Nopeampi koettu vastaus | Käyttökokemuksen parannus | Käytä suoratoistoa, kun saatavilla, ja tyhjennä osittaiset tokenit |
| Deterministiset testit | Regressioiden hallinta | Vakaa CI | Aja `temperature=0`, kiinteät kehotteet |
| Rinnakkaiset haarautumat | Nopeampi tutkimus | Läpäisykyky | Käytä `concurrent.futures` itsenäisille agenttivaiheille |

#### Jälkitietueen esimerkki

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Yksinkertainen arviointikehote

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Tallenna (`answer`, `rating`) -parit rakentaaksesi historiallisen laatukäyrän.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.