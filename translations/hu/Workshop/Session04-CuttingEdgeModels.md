<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T22:54:11+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "hu"
}
-->
# 4. szekció: Fedezd fel a legmodernebb modelleket – LLM-ek, SLM-ek és eszközön futó inferencia

## Összefoglaló

Hasonlítsd össze a Nagy Nyelvi Modelleket (LLM-ek) és a Kis Nyelvi Modelleket (SLM-ek) helyi és felhőalapú inferencia szcenáriókban. Ismerd meg a telepítési mintákat az ONNX Runtime gyorsítás, WebGPU végrehajtás és hibrid RAG élmények kihasználásával. Tartalmaz egy Chainlit RAG demót helyi modellel, valamint opcionális OpenWebUI felfedezést. Alkalmazd a WebGPU inferencia kezdő projektet, és értékeld a Phi és GPT-OSS-20B képességeit, valamint a költség/teljesítmény kompromisszumokat.

## Tanulási célok

- **Összehasonlítás**: SLM vs LLM késleltetés, memória és minőség tengelyeken
- **Modellek telepítése** ONNXRuntime és (ahol támogatott) WebGPU segítségével
- **Futtatás** böngészőalapú inferencia (adatvédelmet biztosító interaktív demó)
- **Integráció** egy Chainlit RAG csővezetékkel helyi SLM háttérrel
- **Értékelés** könnyű minőségi + költségheurisztikák használatával

## Előfeltételek

- 1–3. szekciók teljesítve
- `chainlit` telepítve (már benne van a `requirements.txt` fájlban a Module08-hoz)
- WebGPU-képes böngésző (Edge / Chrome legújabb verziója Windows 11-en)
- Foundry Local futtatása (`foundry status`)

### Keresztplatformos megjegyzések

A Windows továbbra is az elsődleges célplatform. MacOS fejlesztők számára, akik natív binárisokat várnak:
1. Futtasd a Foundry Local-t Windows 11 VM-ben (Parallels / UTM) VAGY egy távoli Windows munkaállomáson.
2. Tedd elérhetővé a szolgáltatást (alapértelmezett port: 5273), és állítsd be macOS-en:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Használd ugyanazokat a Python virtuális környezet lépéseket, mint az előző szekciókban.

Chainlit telepítés (mindkét platformon):
```bash
pip install chainlit
```

## Demó menete (30 perc)

### 1. Phi (SLM) vs GPT-OSS-20B (LLM) összehasonlítása (6 perc)

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

Kövesd: válasz mélysége, tényszerű pontosság, stilisztikai gazdagság, késleltetés.

### 2. ONNX Runtime gyorsítás (5 perc)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Figyeld meg az áteresztőképesség változásait GPU engedélyezése után, szemben a csak CPU-val.

### 3. WebGPU inferencia böngészőben (6 perc)

Alkalmazd a kezdő `04-webgpu-inference` projektet (hozz létre `samples/04-cutting-edge/webgpu_demo.html` fájlt):

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

Nyisd meg a fájlt böngészőben; figyeld meg az alacsony késleltetésű helyi körforgást.

### 4. Chainlit RAG chat alkalmazás (7 perc)

Minimális `samples/04-cutting-edge/chainlit_app.py`:

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

Futtatás:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Kezdő projekt: Alkalmazd a `04-webgpu-inference` projektet (6 perc)

Szállítandók:
- Cseréld ki a helyettesítő fetch logikát streaming tokenekre (használd a `stream=True` végpont variánst, amint engedélyezve van)
- Adj hozzá késleltetési diagramot (kliensoldalon) a phi és gpt-oss-20b váltásokhoz
- Ágyazd be a RAG kontextust (szövegmező a referencia dokumentumokhoz)

## Értékelési heurisztikák

| Kategória | Phi-4-mini | GPT-OSS-20B | Megfigyelés |
|----------|------------|-------------|-------------|
| Késleltetés (hideg) | Gyors | Lassabb | SLM gyorsan felmelegszik |
| Memória | Alacsony | Magas | Eszközön való megvalósíthatóság |
| Kontextus betartása | Jó | Erős | Nagyobb modell lehet, hogy bőbeszédűbb |
| Költség (helyi) | Minimális | Magasabb (erőforrás) | Energia/idő kompromisszum |
| Legjobb felhasználási eset | Edge alkalmazások | Mélyebb érvelés | Hibrid csővezeték lehetséges |

## Környezet validálása

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Hibaelhárítás

| Tünet | Ok | Teendő |
|-------|----|--------|
| Weboldal letöltése sikertelen | CORS vagy szolgáltatás leállt | Használj `curl`-t az végpont ellenőrzéséhez; engedélyezd a CORS proxyt, ha szükséges |
| Chainlit üres | Környezet nem aktív | Aktiváld a venv-t és telepítsd újra a függőségeket |
| Magas késleltetés | Modell éppen betöltve | Melegítsd fel egy kis prompt szekvenciával |

## Hivatkozások

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit dokumentáció: https://docs.chainlit.io
- RAG értékelés (Ragas): https://docs.ragas.io

---

**Szekció időtartama**: 30 perc  
**Nehézségi szint**: Haladó

## Példa szcenárió és workshop térkép

| Workshop anyagok | Szcenárió | Cél | Adat / Prompt forrás |
|------------------|-----------|-----|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Architektúra csapat, amely SLM-et és LLM-et értékel vezetői összefoglaló generálásához | Késleltetés + tokenhasználat különbség kvantifikálása | Egyetlen `COMPARE_PROMPT` környezeti változó |
| `chainlit_app.py` (RAG demó) | Belső tudásasszisztens prototípus | Rövid válaszok megalapozása minimális lexikai visszakereséssel | Fájlban található `DOCS` lista |
| `webgpu_demo.html` | Jövőbeli eszközön futó böngésző inferencia előnézet | Alacsony késleltetésű helyi körforgás + UX narratíva bemutatása | Csak élő felhasználói prompt |

### Szcenárió narratíva
A termékcsapat egy vezetői összefoglaló generátort szeretne. Egy könnyű SLM (phi‑4‑mini) vázlatokat készít; egy nagyobb LLM (gpt‑oss‑20b) csak a kiemelt jelentéseket finomítja. A szekció szkriptek empirikus késleltetési és token metrikákat rögzítenek a hibrid tervezés igazolására, míg a Chainlit demó bemutatja, hogyan tartja a megalapozott visszakeresés a kis modell válaszait tényszerűnek. A WebGPU koncepció oldal jövőképet nyújt a teljesen kliensoldali feldolgozáshoz, amikor a böngésző gyorsítás éretté válik.

### Minimális RAG kontextus (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hibrid Vázlat→Finomítás folyamat (Ál)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Kövesd mindkét késleltetési komponenst, hogy jelentést készíts az átlagos kevert költségről.

### Opcionális fejlesztések

| Fókusz | Fejlesztés | Miért | Megvalósítási tipp |
|--------|-----------|-------|--------------------|
| Összehasonlító metrikák | Kövesd a tokenhasználatot + első token késleltetést | Holisztikus teljesítmény nézet | Használj fejlett benchmark szkriptet (3. szekció) `BENCH_STREAM=1`-el |
| Hibrid csővezeték | SLM vázlat → LLM finomítás | Késleltetés és költség csökkentése | Generálj phi-4-mini-vel, finomítsd az összefoglalót gpt-oss-20b-vel |
| Streaming UI | Jobb UX a Chainlitben | Folyamatos visszajelzés | Használj `stream=True`-t, amint helyi streaming elérhető; halmozd fel a darabokat |
| WebGPU gyorsítótár | Gyorsabb JS inicializálás | Újrafordítási terhelés csökkentése | Gyorsítótárazd a lefordított shader artefaktumokat (jövőbeli futási képesség) |
| Determinisztikus QA készlet | Tisztességes modell összehasonlítás | Variancia eltávolítása | Fix prompt lista + `temperature=0` az értékelési futásokhoz |
| Kimeneti pontozás | Strukturált minőségi lencse | Túl az anekdotákon | Egyszerű rubrika: koherencia / tényszerűség / tömörség (1–5) |
| Energia / Erőforrás megjegyzések | Osztálytermi vita | Kompromisszumok bemutatása | Használj OS monitorokat (`foundry system info`, Feladatkezelő, `nvidia-smi`) + benchmark szkript kimeneteket |
| Költség emuláció | Felhő előtti igazolás | Skálázási terv | Térképezd a tokeneket hipotetikus felhő árazásra a TCO narratívához |
| Késleltetés lebontása | Szűk keresztmetszetek azonosítása | Optimalizációk célzása | Mérd a prompt előkészítést, kérés küldését, első token, teljes befejezés |
| RAG + LLM visszaesés | Minőségi biztonsági háló | Nehéz kérdések javítása | Ha az SLM válasz hossza < küszöbérték vagy alacsony bizalom → eszkaláció |

#### Példa hibrid Vázlat/Finomítás minta

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Késleltetés lebontás vázlat

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Használj következetes mérési keretet a modellek közötti tisztességes összehasonlítás érdekében.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.