# Sesija 4: Pažangiausių modelių tyrinėjimas – LLM, SLM ir įrenginių vidinė analizė

## Santrauka

Palyginkite didelius kalbos modelius (LLM) ir mažus kalbos modelius (SLM) vietinio ir debesų analizės scenarijams. Sužinokite apie diegimo modelius, naudojant ONNX Runtime pagreitį, WebGPU vykdymą ir hibridines RAG patirtis. Įtraukta Chainlit RAG demonstracija su vietiniu modeliu ir pasirinktinis OpenWebUI tyrinėjimas. Jūs pritaikysite WebGPU analizės pradžios projektą ir įvertinsite Phi bei GPT-OSS-20B galimybes, kaštų ir našumo kompromisus.

## Mokymosi tikslai

- **Palyginti** SLM ir LLM pagal vėlavimą, atmintį, kokybės ašis
- **Diegti** modelius su ONNXRuntime ir (kur palaikoma) WebGPU
- **Vykdyti** naršyklėje pagrįstą analizę (privatumą išsauganti interaktyvi demonstracija)
- **Integruoti** Chainlit RAG vamzdyną su vietiniu SLM pagrindu
- **Įvertinti** naudojant lengvas kokybės ir kaštų euristikas

## Reikalavimai

- Užbaigtos sesijos 1–3
- Įdiegtas `chainlit` (jau įtrauktas į `requirements.txt` Module08)
- Naršyklė, palaikanti WebGPU (Edge / Chrome naujausia versija Windows 11)
- Veikiantis Foundry Local (`foundry service status`)

### Pastabos apie skirtingas platformas

Windows išlieka pagrindinė tikslinė aplinka. macOS kūrėjams, laukiantiems vietinių dvejetainių failų:
1. Paleiskite Foundry Local Windows 11 virtualioje mašinoje (Parallels / UTM) ARBA nuotoliniame Windows darbo kompiuteryje.
2. Atidarykite paslaugą (numatytasis prievadas 5273) ir nustatykite macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Naudokite tuos pačius Python virtualios aplinkos veiksmus kaip ankstesnėse sesijose.

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

Stebėkite pralaidumo pokyčius įjungus GPU, palyginti su tik CPU.

### 3. WebGPU analizė naršyklėje (6 min)

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

Atidarykite failą naršyklėje; stebėkite mažo vėlavimo vietinį apsikeitimą.

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

### 5. Pradžios projektas: pritaikykite `04-webgpu-inference` (6 min)

Rezultatai:
- Pakeiskite vietos rezervavimo logiką srautiniais žetonais (naudokite `stream=True` galinio taško variantą, kai jis bus įjungtas)
- Pridėkite vėlavimo diagramą (kliento pusėje) Phi ir GPT-OSS-20B perjungimams
- Įterpkite RAG kontekstą tiesiogiai (teksto laukelis nuorodų dokumentams)

## Vertinimo euristikos

| Kategorija | Phi-4-mini | GPT-OSS-20B | Pastaba |
|------------|------------|-------------|---------|
| Vėlavimas (šaltas) | Greitas | Lėtesnis | SLM greitai sušyla |
| Atmintis | Maža | Didelė | Įrenginio galimybės |
| Konteksto laikymasis | Geras | Stiprus | Didesnis modelis gali būti išsamesnis |
| Kaštai (vietiniai) | Minimalūs | Didesni (išteklių) | Energijos/laiko kompromisas |
| Geriausias naudojimo atvejis | Kraštinės programos | Gilus samprotavimas | Galima hibridinė sistema |

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
| Tinklalapio užklausos nepavyksta | CORS arba paslauga neveikia | Naudokite `curl`, kad patikrintumėte galinį tašką; jei reikia, įjunkite CORS tarpinį serverį |
| Tuščias Chainlit | Aplinka neaktyvi | Aktyvuokite venv ir iš naujo įdiekite priklausomybes |
| Didelis vėlavimas | Modelis ką tik įkeltas | Sušildykite mažos apimties užklausų seka |

## Nuorodos

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit dokumentacija: https://docs.chainlit.io
- RAG vertinimas (Ragas): https://docs.ragas.io

---

**Sesijos trukmė**: 30 min  
**Sudėtingumas**: Pažengusiems

## Pavyzdinė situacija ir dirbtuvių susiejimas

| Dirbtuvių artefaktai | Situacija | Tikslas | Duomenų / užklausų šaltinis |
|----------------------|-----------|---------|----------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Architektūros komanda, vertinanti SLM ir LLM vykdomojo santraukų generatoriui | Kiekybiškai įvertinti vėlavimo ir žetonų naudojimo skirtumą | Vienas `COMPARE_PROMPT` aplinkos kintamasis |
| `chainlit_app.py` (RAG demonstracija) | Vidinis žinių asistento prototipas | Pagrįsti trumpus atsakymus minimalia leksine paieška | Tiesioginis `DOCS` sąrašas faile |
| `webgpu_demo.html` | Ateities įrenginių naršyklės analizės peržiūra | Parodyti mažo vėlavimo vietinį apsikeitimą + UX pasakojimą | Tik gyvas vartotojo užklausos tekstas |

### Situacijos pasakojimas
Produktų organizacija nori vykdomojo santraukų generatoriaus. Lengvas SLM (phi‑4‑mini) rengia santraukas; didesnis LLM (gpt‑oss‑20b) gali tobulinti tik aukšto prioriteto ataskaitas. Sesijos scenarijai fiksuoja empirinį vėlavimo ir žetonų metriką, kad pateisintų hibridinį dizainą, o Chainlit demonstracija iliustruoja, kaip pagrįsta paieška padeda mažo modelio atsakymams išlikti faktiniais. WebGPU koncepcijos puslapis pateikia vizijos kelią visiškai klientų pusės apdorojimui, kai naršyklės pagreitis subręs.

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

Stebėkite abu vėlavimo komponentus, kad praneštumėte apie mišrius vidutinius kaštus.

### Pasirinktiniai patobulinimai

| Fokusas | Patobulinimas | Kodėl | Įgyvendinimo užuomina |
|---------|--------------|-------|-----------------------|
| Lyginamosios metrikos | Stebėkite žetonų naudojimą + pirmojo žetono vėlavimą | Holistinis našumo vaizdas | Naudokite patobulintą testavimo scenarijų (Sesija 3) su `BENCH_STREAM=1` |
| Hibridinis vamzdynas | SLM juodraštis → LLM tobulinimas | Sumažinti vėlavimą ir kaštus | Generuokite su phi-4-mini, tobulinkite santrauką su gpt-oss-20b |
| Srautinė sąsaja | Geresnis UX Chainlit | Inkrementinis grįžtamasis ryšys | Naudokite `stream=True`, kai vietinis srautas bus įjungtas; kaupti fragmentus |
| WebGPU talpykla | Greitesnis JS inicijavimas | Sumažinti perkompiliavimo sąnaudas | Talpykloje saugokite sukompiliuotus šešėlių artefaktus (būsima vykdymo galimybė) |
| Deterministiniai QA rinkiniai | Sąžiningas modelių palyginimas | Pašalinti variaciją | Fiksuotas užklausų sąrašas + `temperature=0` vertinimo paleidimams |
| Rezultatų vertinimas | Struktūrinė kokybės perspektyva | Peržengti anekdotus | Paprasta rubrika: nuoseklumas / faktualumas / trumpumas (1–5) |
| Energijos / išteklių pastabos | Klasės diskusija | Parodyti kompromisus | Naudokite OS monitorius (Task Manager, `nvidia-smi`) + testavimo scenarijų rezultatus |
| Kaštų emuliacija | Prieš debesų pateisinimą | Planuoti mastelį | Susiekite žetonus su hipotetinėmis debesų kainomis TCO pasakojimui |
| Vėlavimo skaidymas | Identifikuoti kliūtis | Tikslinės optimizacijos | Išmatuokite užklausų paruošimą, siuntimą, pirmąjį žetoną, pilną užbaigimą |
| RAG + LLM atsarginė kopija | Kokybės saugumo tinklas | Pagerinti sudėtingus užklausimus | Jei SLM atsakymo ilgis < slenkstis arba mažas pasitikėjimas → eskaluoti |

#### Pavyzdinis hibridinis juodraštis/tobulinimo modelis

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

Naudokite nuoseklią matavimo struktūrą visiems modeliams, kad užtikrintumėte sąžiningą palyginimą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->