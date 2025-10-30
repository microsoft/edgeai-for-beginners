<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T23:57:09+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "et"
}
-->
# Sessioon 4: Uurige tipptasemel mudeleid – LLM-id, SLM-id ja seadmesisene järeldamine

## Kokkuvõte

Võrrelge suuri keelemudeleid (LLM) ja väikeseid keelemudeleid (SLM) kohalike ja pilvepõhiste järelduste stsenaariumide jaoks. Õppige juurutamismustreid, kasutades ONNX Runtime kiirendust, WebGPU täitmist ja hübriidseid RAG-kogemusi. Sisaldab Chainlit RAG-i demo koos kohaliku mudeliga ja valikulist OpenWebUI uurimist. Kohandate WebGPU järelduse algversiooni ja hindate Phi ja GPT-OSS-20B võimekust ning kulude/tõhususe kompromisse.

## Õpieesmärgid

- **Võrrelge** SLM-i ja LLM-i latentsuse, mälu ja kvaliteedi telgedel
- **Juurutage** mudeleid ONNXRuntime'iga ja (kui toetatud) WebGPU-ga
- **Käivitage** brauseripõhine järeldamine (privaatsust säilitav interaktiivne demo)
- **Integreerige** Chainlit RAG torujuhe kohaliku SLM-i taustsüsteemiga
- **Hinnake** kergete kvaliteedi- ja kulude heuristikate abil

## Eeltingimused

- Sessioonid 1–3 läbitud
- `chainlit` installitud (juba olemas `requirements.txt` failis Module08 jaoks)
- WebGPU-toega brauser (Edge / Chrome uusim versioon Windows 11 jaoks)
- Foundry Local töötab (`foundry status`)

### Platvormidevahelised märkused

Windows jääb peamiseks sihtkeskkonnaks. macOS-i arendajatele, kes ootavad natiivseid binaare:
1. Käivitage Foundry Local Windows 11 virtuaalmasinas (Parallels / UTM) VÕI kaug-Windowsi tööjaamas.
2. Avage teenus (vaikeport 5273) ja seadistage macOS-is:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Kasutage samu Python virtuaalkeskkonna samme nagu eelnevates sessioonides.

Chainlit installimine (mõlemal platvormil):
```bash
pip install chainlit
```

## Demo voog (30 min)

### 1. Võrdle Phi (SLM) ja GPT-OSS-20B (LLM) (6 min)

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

Jälgi: vastuse sügavust, faktilist täpsust, stiililist rikkust, latentsust.

### 2. ONNX Runtime kiirendus (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Jälgi läbilaskevõime muutusi pärast GPU lubamist võrreldes ainult CPU-ga.

### 3. WebGPU järeldamine brauseris (6 min)

Kohanda algversiooni `04-webgpu-inference` (loo `samples/04-cutting-edge/webgpu_demo.html`):

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

Ava fail brauseris; jälgi madala latentsusega kohalikku ringlust.

### 4. Chainlit RAG vestlusrakendus (7 min)

Minimalistlik `samples/04-cutting-edge/chainlit_app.py`:

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

Käivita:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Algprojekt: Kohanda `04-webgpu-inference` (6 min)

Tarnitavad:
- Asenda kohatäite andmete hankimise loogika voogedastuse tokenitega (kasuta `stream=True` lõpp-punkti varianti, kui see on lubatud)
- Lisa latentsuse diagramm (kliendipoolne) Phi ja GPT-OSS-20B lülituste jaoks
- Lisa RAG kontekst otse (tekstiala viitedokumentide jaoks)

## Hindamise heuristikad

| Kategooria | Phi-4-mini | GPT-OSS-20B | Tähelepanek |
|------------|------------|-------------|-------------|
| Latentsus (külm) | Kiire | Aeglasem | SLM soojeneb kiiresti |
| Mälu | Madal | Kõrge | Seadme teostatavus |
| Konteksti järgimine | Hea | Tugev | Suurem mudel võib olla sõnaohtram |
| Kulu (kohalik) | Minimaalne | Kõrgem (ressurss) | Energia/aja kompromiss |
| Parim kasutusjuhtum | Ääriserakendused | Sügav mõtlemine | Võimalik hübriidtorujuhe |

## Keskkonna valideerimine

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Tõrkeotsing

| Sümptom | Põhjus | Tegevus |
|---------|--------|---------|
| Veebilehe laadimine ebaõnnestub | CORS või teenus maas | Kasuta `curl`, et kontrollida lõpp-punkti; luba CORS proxy vajadusel |
| Chainlit tühi | Keskkond pole aktiivne | Aktiveeri venv ja installi uuesti sõltuvused |
| Kõrge latentsus | Mudel just laaditud | Soojenda väikese prompt-jadaga |

## Viited

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit dokumendid: https://docs.chainlit.io
- RAG hindamine (Ragas): https://docs.ragas.io

---

**Sessiooni kestus**: 30 min  
**Raskusaste**: Edasijõudnud

## Näidisstsenaarium ja töötoa kaardistamine

| Töötoa artefaktid | Stsenaarium | Eesmärk | Andmed / prompti allikas |
|-------------------|------------|---------|-------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Arhitektuurimeeskond hindab SLM-i ja LLM-i juhtkonna kokkuvõtete generaatori jaoks | Koguse latentsuse ja tokenite kasutuse erinevuse kvantifitseerimine | Üksik `COMPARE_PROMPT` keskkonnamuutuja |
| `chainlit_app.py` (RAG demo) | Sisemine teadmiste assistendi prototüüp | Lühivastuste aluseks minimaalne leksikaalne otsing | Faili sisemine `DOCS` loend |
| `webgpu_demo.html` | Tulevikku suunatud seadmesisese brauseri järelduse eelvaade | Näita madala latentsusega kohalikku ringlust + UX narratiivi | Ainult reaalajas kasutaja prompt |

### Stsenaariumi narratiiv
Tooteorganisatsioon soovib juhtkonna kokkuvõtete generaatorit. Kerge SLM (phi-4-mini) koostab kokkuvõtteid; suurem LLM (gpt-oss-20b) võib täiustada ainult kõrge prioriteediga aruandeid. Sessiooniskriptid koguvad empiirilisi latentsuse ja tokenite mõõdikuid, et õigustada hübriidset disaini, samas kui Chainlit demo illustreerib, kuidas põhjendatud otsing hoiab väikese mudeli vastused faktilised. WebGPU kontseptsioonileht pakub visioonirada täielikult kliendipoolseks töötlemiseks, kui brauseri kiirendus küpseb.

### Minimaalne RAG kontekst (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hübriidne mustand→täiustamise voog (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Jälgi mõlemat latentsuskomponenti, et raporteerida segatud keskmist kulu.

### Valikulised täiustused

| Fookus | Täiustus | Miks | Rakendamise vihje |
|--------|----------|------|-------------------|
| Võrdlevad mõõdikud | Jälgi tokenite kasutust + esimese tokeni latentsust | Holistiline jõudluse ülevaade | Kasuta täiustatud võrdlusskripti (Sessioon 3) koos `BENCH_STREAM=1` |
| Hübriidtorujuhe | SLM mustand → LLM täiustus | Vähenda latentsust ja kulu | Loo phi-4-mini abil, täiusta kokkuvõte gpt-oss-20b-ga |
| Voogedastuse UI | Parem UX Chainlitis | Järk-järguline tagasiside | Kasuta `stream=True`, kui kohalik voogedastus on lubatud; koguge tükid |
| WebGPU vahemälu | Kiirem JS algus | Vähenda ümberkompileerimise koormust | Vahemälu kompileeritud shaderi artefaktid (tulevane runtime võimekus) |
| Deterministlik QA komplekt | Õiglane mudelivõrdlus | Eemalda variatsioon | Fikseeritud prompt-loend + `temperature=0` hindamisjooksude jaoks |
| Väljundi hindamine | Struktureeritud kvaliteedi analüüs | Liigu anekdootidest kaugemale | Lihtne rubriik: sidusus / faktilisus / lühidus (1–5) |
| Energia / ressursi märkmed | Klassiruumi arutelu | Näita kompromisse | Kasuta OS-i monitooringut (`foundry system info`, Task Manager, `nvidia-smi`) + võrdlusskripti väljundeid |
| Kulu emulatsioon | Pilve-eelne õigustus | Plaani skaleerimist | Kaardista tokenid hüpoteetilise pilve hinna jaoks TCO narratiivi loomiseks |
| Latentsuse jaotus | Kitsaskohtade tuvastamine | Optimeerimise sihtimine | Mõõda prompti ettevalmistust, päringu saatmist, esimest tokenit, täielikku lõpetamist |
| RAG + LLM varuvariant | Kvaliteedi turvavõrk | Paranda keerulisi päringuid | Kui SLM-i vastuse pikkus < lävi või madal usaldus → eskaleeri |

#### Näide hübriidse mustandi/täiustamise mustrist

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Latentsuse jaotuse visand

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Kasuta järjepidevat mõõtmise raamistikku mudelite vahel õiglaselt võrdlemiseks.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.