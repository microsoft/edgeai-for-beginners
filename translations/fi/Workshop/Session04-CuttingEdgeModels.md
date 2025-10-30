<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T22:16:43+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "fi"
}
-->
# Istunto 4: Tutustu huippumalleihin – LLM:t, SLM:t ja laitekohtainen inferenssi

## Tiivistelmä

Vertaa suuria kielimalleja (LLM) ja pieniä kielimalleja (SLM) paikallisen ja pilvipohjaisen inferenssin näkökulmasta. Opettele käyttöönoton malleja hyödyntäen ONNX Runtime -kiihdytystä, WebGPU-suoritusta ja hybridisiä RAG-kokemuksia. Sisältää Chainlit RAG -demon paikallisella mallilla sekä valinnaisen OpenWebUI-tutkimuksen. Mukautat WebGPU-inferenssin aloitusprojektin ja arvioit Phi:n ja GPT-OSS-20B:n kyvykkyyttä sekä kustannus/suorituskyky -kompromisseja.

## Oppimistavoitteet

- **Vertaa** SLM:ää ja LLM:ää viiveen, muistin ja laadun osalta
- **Ota käyttöön** malleja ONNXRuntime-ohjelmalla ja (jos tuettu) WebGPU:lla
- **Suorita** selaimen kautta tapahtuva inferenssi (yksityisyyttä suojaava interaktiivinen demo)
- **Integroi** Chainlit RAG -putki paikallisen SLM-taustajärjestelmän kanssa
- **Arvioi** kevyillä laatu- ja kustannusheuristiikoilla

## Esivaatimukset

- Istunnot 1–3 suoritettu
- `chainlit` asennettuna (jo mukana `requirements.txt`-tiedostossa Module08:ssa)
- WebGPU-yhteensopiva selain (Edge / Chrome uusin versio Windows 11:ssä)
- Foundry Local käynnissä (`foundry status`)

### Alustojen väliset huomiot

Windows on ensisijainen kohdeympäristö. macOS-kehittäjille, jotka odottavat natiivibinaareja:
1. Aja Foundry Local Windows 11 -virtuaalikoneessa (Parallels / UTM) TAI etä-Windows-työasemalla.
2. Avaa palvelu (oletusportti 5273) ja aseta macOS:lle:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Käytä samoja Python-virtuaaliympäristön asennusvaiheita kuin aiemmissa istunnoissa.

Chainlit-asennus (molemmilla alustoilla):
```bash
pip install chainlit
```

## Demo-prosessi (30 min)

### 1. Vertaa Phi (SLM) ja GPT-OSS-20B (LLM) (6 min)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Seuraa: vastausten syvyyttä, faktatarkkuutta, tyylillistä rikkautta, viivettä.

### 2. ONNX Runtime -kiihdytys (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Havainnoi läpimenomuutoksia GPU:n ja vain CPU:n käytön välillä.

### 3. WebGPU-inferenssi selaimessa (6 min)

Mukauta aloitusprojektia `04-webgpu-inference` (luo `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Avaa tiedosto selaimessa; havainnoi matalan viiveen paikallinen kierros.

### 4. Chainlit RAG -chat-sovellus (7 min)

Minimaalinen `samples/04-cutting-edge/chainlit_app.py`:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Suorita:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Aloitusprojekti: Mukauta `04-webgpu-inference` (6 min)

Toimitettavat:
- Korvaa paikkamerkkien hakulogiikka suoratoistotokenilla (käytä `stream=True` -päätepisteen varianttia, kun se on käytössä)
- Lisää viivekaavio (asiakaspuolella) Phi:n ja GPT-OSS-20B:n vaihtojen osalta
- Upota RAG-konteksti suoraan (tekstialue viitedokumenteille)

## Arviointiheuristiikat

| Kategoria | Phi-4-mini | GPT-OSS-20B | Havainnot |
|-----------|------------|-------------|-----------|
| Viive (kylmä) | Nopea | Hitaampi | SLM lämpenee nopeasti |
| Muisti | Matala | Korkea | Laitteen toteutettavuus |
| Kontekstin noudattaminen | Hyvä | Vahva | Suurempi malli voi olla sanallisempi |
| Kustannukset (paikallinen) | Vähäinen | Korkeampi (resurssit) | Energia-/aikakompromissi |
| Paras käyttötapaus | Reuna-sovellukset | Syvällinen päättely | Mahdollinen hybridiputki |

## Ympäristön validointi

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Vianetsintä

| Oire | Syy | Toimenpide |
|------|-----|-----------|
| Verkkosivun haku epäonnistuu | CORS tai palvelu ei toimi | Käytä `curl` varmistaaksesi päätepisteen; ota käyttöön CORS-välityspalvelin tarvittaessa |
| Chainlit tyhjä | Ympäristö ei aktiivinen | Aktivoi venv ja asenna riippuvuudet uudelleen |
| Korkea viive | Malli juuri ladattu | Lämmitä pienellä kehotussekvenssillä |

## Viitteet

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit-dokumentaatio: https://docs.chainlit.io
- RAG-arviointi (Ragas): https://docs.ragas.io

---

**Istunnon kesto**: 30 min  
**Vaikeustaso**: Edistynyt

## Esimerkkiskenaario ja työpajan kartoitus

| Työpajan artefaktit | Skenaario | Tavoite | Data / Kehotuslähde |
|---------------------|-----------|---------|---------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Arkkitehtitiimi arvioi SLM:ää ja LLM:ää johtoryhmän yhteenvetogeneraattorille | Määritä viiveen ja tokenien käytön ero | Yksi `COMPARE_PROMPT` ympäristömuuttuja |
| `chainlit_app.py` (RAG-demo) | Sisäinen tietämysassistentin prototyyppi | Perustele lyhyet vastaukset minimaalisella leksikaalisella haulla | Tiedoston sisäinen `DOCS`-lista |
| `webgpu_demo.html` | Tulevaisuuden laitekohtainen selaimen inferenssin esikatselu | Näytä matalan viiveen paikallinen kierros + UX-narratiivi | Vain käyttäjän live-kehotus |

### Skenaarion narratiivi
Tuotanto-organisaatio haluaa johtoryhmän yhteenvetogeneraattorin. Kevyt SLM (phi‑4‑mini) laatii yhteenvedot; suurempi LLM (gpt‑oss‑20b) voi tarkentaa vain korkean prioriteetin raportteja. Istuntoskriptit tallentavat empiiriset viive- ja tokenimittarit perustellakseen hybridisuunnittelun, kun taas Chainlit-demo havainnollistaa, kuinka perusteltu haku pitää pienen mallin vastaukset faktapohjaisina. WebGPU-konseptisivu tarjoaa visiointipolun täysin asiakaspuolen käsittelyyn, kun selaimen kiihdytys kehittyy.

### Minimaalinen RAG-konteksti (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hybridiluonnos→Tarkennusvirtaus (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Seuraa molempia viivekomponentteja raportoidaksesi keskimääräiset yhdistetyt kustannukset.

### Valinnaiset parannukset

| Painopiste | Parannus | Miksi | Toteutusvinkki |
|------------|----------|-------|----------------|
| Vertailumetriikat | Seuraa tokenien käyttöä + ensimmäisen tokenin viivettä | Kokonaisvaltainen suorituskykykuva | Käytä parannettua vertailuskriptiä (Istunto 3) `BENCH_STREAM=1` kanssa |
| Hybridiputki | SLM-luonnos → LLM-tarkennus | Vähennä viivettä ja kustannuksia | Luo phi-4-mini:llä, tarkenna yhteenveto gpt-oss-20b:llä |
| Suoratoisto-UI | Parempi UX Chainlitissä | Jatkuva palaute | Käytä `stream=True`, kun paikallinen suoratoisto on käytössä; kerää osia |
| WebGPU-välimuisti | Nopeampi JS-initialisointi | Vähennä uudelleenkääntämisen ylikuormitusta | Välimuistiin käännetyt shader-artefaktit (tuleva runtime-ominaisuus) |
| Deterministinen QA-setti | Reilu mallivertailu | Poista vaihtelu | Kiinteä kehotuslista + `temperature=0` arviointiajoille |
| Tulosten pisteytys | Rakenteellinen laatulinsse | Siirry anekdooteista eteenpäin | Yksinkertainen rubriikki: johdonmukaisuus / faktapohjaisuus / tiiviys (1–5) |
| Energia-/resurssimuistiinpanot | Luokkahuonekeskustelu | Näytä kompromissit | Käytä käyttöjärjestelmän seurantatyökaluja (`foundry system info`, Tehtävienhallinta, `nvidia-smi`) + vertailuskriptin tuloksia |
| Kustannusten emulointi | Pilven perustelu | Suunnittele skaalaus | Kartuta tokenit hypoteettiseen pilvihinnoitteluun TCO-narratiivin osalta |
| Viiveen erittely | Tunnista pullonkaulat | Kohdista optimoinnit | Mittaa kehotuksen valmistelu, pyynnön lähetys, ensimmäinen token, täydellinen valmistuminen |
| RAG + LLM-varajärjestelmä | Laadun turvaverkko | Paranna vaikeita kyselyitä | Jos SLM-vastaus pituus < kynnysarvo tai matala luottamus → eskaloi |

#### Esimerkki hybridiluonnos/tarkennusmallista

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Viiveen erittelyluonnos

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Käytä johdonmukaista mittauskehystä mallien välillä reilujen vertailujen varmistamiseksi.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.