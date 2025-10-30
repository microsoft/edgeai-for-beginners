<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T23:45:48+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "lt"
}
-->
# 4 sesija: Pažangiausių modelių tyrinėjimas – LLM, SLM ir įrenginio vidinė inferencija

## Santrauka

Palyginkite didelius kalbos modelius (LLM) ir mažus kalbos modelius (SLM) vietinės ir debesų inferencijos scenarijams. Sužinokite apie diegimo modelius, naudojant ONNX Runtime pagreitį, WebGPU vykdymą ir hibridines RAG patirtis. Įtraukta Chainlit RAG demonstracija su vietiniu modeliu ir papildoma OpenWebUI tyrinėjimo galimybė. Jūs pritaikysite WebGPU inferencijos pradžios projektą ir įvertinsite Phi bei GPT-OSS-20B galimybių ir kaštų/našumo kompromisus.

## Mokymosi tikslai

- **Palyginti** SLM ir LLM pagal vėlavimą, atminties naudojimą ir kokybę
- **Diegti** modelius su ONNXRuntime ir (jei palaikoma) WebGPU
- **Vykdyti** naršyklėje pagrįstą inferenciją (privatumą užtikrinanti interaktyvi demonstracija)
- **Integruoti** Chainlit RAG vamzdyną su vietiniu SLM pagrindu
- **Įvertinti** naudojant lengvus kokybės ir kaštų vertinimo kriterijus

## Būtinos sąlygos

- Užbaigtos 1–3 sesijos
- Įdiegtas `chainlit` (jau įtrauktas į `requirements.txt` Module08)
- Naršyklė, palaikanti WebGPU (naujausia Edge / Chrome versija Windows 11)
- Veikiantis Foundry Local (`foundry status`)

### Pastabos apie skirtingas platformas

Windows išlieka pagrindine tikslinė aplinka. macOS kūrėjams, laukiantiems vietinių dvejetainių failų:
1. Paleiskite Foundry Local Windows 11 virtualioje mašinoje (Parallels / UTM) ARBA nuotoliniame Windows darbo kompiuteryje.
2. Atidarykite paslaugą (numatytasis prievadas 5273) ir nustatykite macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Naudokite tuos pačius Python virtualios aplinkos veiksmus kaip ir ankstesnėse sesijose.

Chainlit diegimas (abi platformos):
```bash
pip install chainlit
```

## Demonstracijos eiga (30 min)

### 1. Palyginkite Phi (SLM) ir GPT-OSS-20B (LLM) (6 min)

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

Stebėkite: atsakymų gilumą, faktinį tikslumą, stilistinį turtingumą, vėlavimą.

### 2. ONNX Runtime pagreitis (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Stebėkite pralaidumo pokyčius įjungus GPU ir naudojant tik CPU.

### 3. WebGPU inferencija naršyklėje (6 min)

Pritaikykite pradžios projektą `04-webgpu-inference` (sukurkite `samples/04-cutting-edge/webgpu_demo.html`):

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

Atidarykite failą naršyklėje; stebėkite mažo vėlavimo vietinį atsakymą.

### 4. Chainlit RAG pokalbių programa (7 min)

Minimalus `samples/04-cutting-edge/chainlit_app.py`:

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

Paleiskite:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Pradinis projektas: pritaikykite `04-webgpu-inference` (6 min)

Pristatomi rezultatai:
- Pakeiskite laikinojo duomenų gavimo logiką į srautinius tokenus (naudokite `stream=True` galinę tašką, kai jis bus įjungtas)
- Pridėkite vėlavimo diagramą (kliento pusėje) Phi ir GPT-OSS-20B perjungimams
- Įterpkite RAG kontekstą tiesiogiai (teksto laukelis nuorodų dokumentams)

## Vertinimo kriterijai

| Kategorija | Phi-4-mini | GPT-OSS-20B | Pastabos |
|------------|------------|-------------|----------|
| Vėlavimas (šaltas) | Greitas | Lėtesnis | SLM greitai įšyla |
| Atmintis | Maža | Didelė | Įrenginio tinkamumas |
| Konteksto laikymasis | Geras | Stiprus | Didesnis modelis gali būti išsamesnis |
| Kaštai (vietiniai) | Minimalūs | Didesni (išteklių) | Energijos/laiko kompromisas |
| Geriausias naudojimo atvejis | Kraštinės programos | Gili analizė | Galima hibridinė sistema |

## Aplinkos patikrinimas

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Trikčių šalinimas

| Simptomas | Priežastis | Veiksmas |
|-----------|------------|----------|
| Nepavyksta įkelti tinklalapio | CORS arba paslauga neveikia | Naudokite `curl`, kad patikrintumėte galinį tašką; jei reikia, įjunkite CORS proxy |
| Chainlit tuščias | Aplinka neaktyvi | Aktyvuokite venv ir iš naujo įdiekite priklausomybes |
| Didelis vėlavimas | Modelis ką tik įkeltas | Įšildykite su mažu užklausos tekstu |

## Nuorodos

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit dokumentacija: https://docs.chainlit.io
- RAG vertinimas (Ragas): https://docs.ragas.io

---

**Sesijos trukmė**: 30 min  
**Sudėtingumas**: Pažengęs

## Pavyzdinė situacija ir dirbtuvių susiejimas

| Dirbtuvių artefaktai | Situacija | Tikslas | Duomenų / užklausos šaltinis |
|----------------------|-----------|---------|-----------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Architektūros komanda, vertinanti SLM ir LLM vykdomojo santraukų generatoriui | Kiekybiškai įvertinti vėlavimo ir tokenų naudojimo skirtumus | Vienas `COMPARE_PROMPT` aplinkos kintamasis |
| `chainlit_app.py` (RAG demonstracija) | Vidinio žinių asistento prototipas | Pagrįsti trumpus atsakymus minimalia leksine paieška | Tiesioginis `DOCS` sąrašas faile |
| `webgpu_demo.html` | Ateities įrenginio naršyklės inferencijos peržiūra | Parodyti mažo vėlavimo vietinį atsakymą ir UX pasakojimą | Tik gyva vartotojo užklausa |

### Situacijos pasakojimas
Produktų organizacija nori vykdomojo santraukų generatoriaus. Lengvas SLM (phi‑4‑mini) rengia santraukas; didesnis LLM (gpt‑oss‑20b) gali tobulinti tik aukšto prioriteto ataskaitas. Sesijos scenarijai fiksuoja empirinį vėlavimą ir tokenų metriką, kad būtų galima pagrįsti hibridinį dizainą, o Chainlit demonstracija iliustruoja, kaip pagrįsta paieška užtikrina mažo modelio atsakymų tikslumą. WebGPU koncepcijos puslapis pateikia viziją visiškai kliento pusės apdorojimui, kai naršyklės pagreitis bus labiau išvystytas.

### Minimalus RAG kontekstas (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hibridinis juodraštis→tobulinimo srautas (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Sekite abu vėlavimo komponentus, kad pateiktumėte vidutinius mišrius kaštus.

### Pasirinktiniai patobulinimai

| Dėmesys | Patobulinimas | Kodėl | Įgyvendinimo užuomina |
|---------|---------------|-------|-----------------------|
| Palyginamos metrikos | Sekite tokenų naudojimą ir pirmojo tokeno vėlavimą | Holistinis našumo vaizdas | Naudokite patobulintą testavimo scenarijų (3 sesija) su `BENCH_STREAM=1` |
| Hibridinis vamzdynas | SLM juodraštis → LLM tobulinimas | Sumažinti vėlavimą ir kaštus | Generuokite su phi-4-mini, tobulinkite santrauką su gpt-oss-20b |
| Srautinė sąsaja | Geresnė UX Chainlit | Inkrementinis grįžtamasis ryšys | Naudokite `stream=True`, kai vietinis srautas bus įjungtas; kaupti dalis |
| WebGPU talpykla | Greitesnis JS inicijavimas | Sumažinti perkompiliavimo išlaidas | Talpykloje saugokite sukompiliuotus šeiderių artefaktus (būsima vykdymo galimybė) |
| Determinuotas QA rinkinys | Sąžiningas modelių palyginimas | Pašalinti variaciją | Fiksuotas užklausų sąrašas + `temperature=0` vertinimo paleidimams |
| Rezultatų vertinimas | Struktūrinis kokybės matas | Virš anekdotų | Paprasta rubrika: nuoseklumas / faktualumas / glaustumas (1–5) |
| Energijos / išteklių pastabos | Diskusija klasėje | Parodyti kompromisus | Naudokite OS monitorius (`foundry system info`, Task Manager, `nvidia-smi`) + testavimo scenarijų rezultatus |
| Kaštų emuliacija | Prieš debesų pagrindimą | Planavimo mastelis | Susiekite tokenus su hipotetinėmis debesų kainomis TCO pasakojimui |
| Vėlavimo skaidymas | Nustatyti kliūtis | Tikslinės optimizacijos | Matuokite užklausos paruošimą, užklausos siuntimą, pirmą tokeną, pilną užbaigimą |
| RAG + LLM atsarginis variantas | Kokybės saugumo tinklas | Pagerinti sudėtingus klausimus | Jei SLM atsakymo ilgis < slenkstis arba žemas pasitikėjimas → eskaluoti |

#### Pavyzdinis hibridinis juodraščio/tobulinimo modelis

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Vėlavimo skaidymo eskizas

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Naudokite nuoseklią matavimo struktūrą visiems modeliams, kad palyginimai būtų sąžiningi.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.