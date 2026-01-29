# Seja 4: Raziskovanje najsodobnejših modelov – LLM-ji, SLM-ji in inferenca na napravi

## Povzetek

Primerjajte velike jezikovne modele (LLM-ji) in majhne jezikovne modele (SLM-ji) za scenarije lokalne in oblačne inference. Spoznajte vzorce uvajanja z uporabo pospeševanja ONNX Runtime, izvajanja WebGPU in hibridnih RAG izkušenj. Vključuje Chainlit RAG demo z lokalnim modelom ter opcijsko raziskovanje OpenWebUI. Prilagodili boste začetni projekt za WebGPU inferenco in ocenili zmogljivost ter stroškovno/zmogljivostne kompromise med Phi in GPT-OSS-20B.

## Cilji učenja

- **Primerjajte** SLM in LLM glede na zakasnitve, pomnilnik in kakovost
- **Uvedite** modele z ONNXRuntime in (kjer podprto) WebGPU
- **Izvedite** inferenco v brskalniku (interaktivni demo, ki ohranja zasebnost)
- **Integrirajte** Chainlit RAG cevovod z lokalnim SLM zaledjem
- **Ocenite** z uporabo lahkih kakovostnih + stroškovnih hevristik

## Predpogoji

- Zaključene seje 1–3
- Nameščen `chainlit` (že v `requirements.txt` za Modul08)
- Brskalnik, ki podpira WebGPU (Edge / Chrome najnovejša različica na Windows 11)
- Zagnan Foundry Local (`foundry service status`)

### Opombe za več platform

Windows ostaja primarno ciljno okolje. Za razvijalce na macOS, ki čakajo na izvorne binarne datoteke:
1. Zaženite Foundry Local v Windows 11 VM (Parallels / UTM) ALI na oddaljeni Windows delovni postaji.
2. Omogočite storitev (privzeti port 5273) in nastavite na macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Uporabite iste korake za Python virtualno okolje kot v prejšnjih sejah.

Namestitev Chainlit (obe platformi):
```bash
pip install chainlit
```

## Potek demonstracije (30 min)

### 1. Primerjava Phi (SLM) in GPT-OSS-20B (LLM) (6 min)

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

Sledite: globina odgovora, dejanska natančnost, slogovna bogatost, zakasnitev.

Opazujte spremembe prepustnosti po omogočitvi GPU v primerjavi z uporabo samo CPU.

### 3. WebGPU inferenca v brskalniku (6 min)

Prilagodite začetni projekt `04-webgpu-inference` (ustvarite `samples/04-cutting-edge/webgpu_demo.html`):

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

Odprite datoteko v brskalniku; opazujte lokalni povratni klic z nizko zakasnitvijo.

### 4. Chainlit RAG aplikacija za klepet (7 min)

Minimalni `samples/04-cutting-edge/chainlit_app.py`:

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

Zaženite:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Začetni projekt: Prilagodite `04-webgpu-inference` (6 min)

Dostave:
- Zamenjajte logiko pridobivanja z nadomestnim pretokom tokov (uporabite `stream=True` različico končne točke, ko bo omogočena)
- Dodajte graf zakasnitve (na strani odjemalca) za preklop med phi in gpt-oss-20b
- Vdelajte RAG kontekst neposredno (besedilno polje za referenčne dokumente)

## Hevristike ocenjevanja

| Kategorija | Phi-4-mini | GPT-OSS-20B | Opazovanje |
|------------|------------|-------------|------------|
| Zakasnitev (hladno) | Hitro | Počasneje | SLM se hitro ogreje |
| Pomnilnik | Nizek | Visok | Ustreznost naprave |
| Upoštevanje konteksta | Dobro | Močno | Večji model je lahko bolj obširen |
| Stroški (lokalno) | Minimalni | Višji (viri) | Kompromis med energijo/časom |
| Najboljša uporaba | Aplikacije na robu | Globoko razmišljanje | Možna hibridna rešitev |

## Validacija okolja

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Odpravljanje težav

| Simptom | Vzrok | Ukrep |
|---------|-------|-------|
| Pridobivanje spletne strani ne uspe | CORS ali storitev ne deluje | Uporabite `curl` za preverjanje končne točke; omogočite CORS proxy, če je potrebno |
| Chainlit prazen | Okolje ni aktivno | Aktivirajte venv in ponovno namestite odvisnosti |
| Visoka zakasnitev | Model je pravkar naložen | Ogrejte z majhnim zaporedjem pozivov |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit dokumentacija: https://docs.chainlit.io
- RAG ocenjevanje (Ragas): https://docs.ragas.io

---

**Trajanje seje**: 30 min  
**Težavnost**: Napredno

## Primer scenarija in povezava z delavnico

| Artefakti delavnice | Scenarij | Cilj | Vir podatkov / pozivov |
|---------------------|----------|------|------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Arhitekturna ekipa ocenjuje SLM v primerjavi z LLM za generator povzetkov za vodstvo | Kvantificirajte zakasnitev + razliko v uporabi žetonov | En sam `COMPARE_PROMPT` okoljski spremenljiv |
| `chainlit_app.py` (RAG demo) | Prototip notranjega asistenta za znanje | Utemeljite kratke odgovore z minimalnim leksikalnim pridobivanjem | Vgrajen seznam `DOCS` v datoteki |
| `webgpu_demo.html` | Vizija futuristične inferenčne obdelave v brskalniku na napravi | Prikaz lokalnega povratnega klica z nizko zakasnitvijo + UX narativ | Samo poziv v živo uporabnika |

### Narativ scenarija
Produktna organizacija želi generator povzetkov za vodstvo. Lahek SLM (phi‑4‑mini) pripravi osnutke povzetkov; večji LLM (gpt‑oss‑20b) lahko izpopolni le poročila z visoko prioriteto. Skripte seje zajamejo empirične zakasnitve in metrike žetonov za utemeljitev hibridne zasnove, medtem ko Chainlit demo prikazuje, kako utemeljeno pridobivanje ohranja odgovore majhnega modela dejanske. Konceptna stran WebGPU ponuja vizijo za popolnoma odjemalsko obdelavo, ko se pospeševanje brskalnika razvije.

### Minimalni RAG kontekst (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hibridni tok osnutek→izpopolnitev (psevdokoda)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Sledite obema komponentama zakasnitve za poročanje o povprečnih stroških.

### Opcijske izboljšave

| Fokus | Izboljšava | Zakaj | Namig za implementacijo |
|-------|------------|-------|-------------------------|
| Primerjalne metrike | Sledite uporabi žetonov + zakasnitvi prvega žetona | Celovit pogled na zmogljivost | Uporabite izboljšano skripto za primerjavo (Seja 3) z `BENCH_STREAM=1` |
| Hibridni cevovod | Osnutek SLM → izpopolnitev LLM | Zmanjšajte zakasnitev in stroške | Ustvarite z phi-4-mini, izpopolnite povzetek z gpt-oss-20b |
| UI za pretok | Boljša UX v Chainlit | Postopne povratne informacije | Uporabite `stream=True`, ko bo lokalno pretakanje omogočeno; zbirajte dele |
| WebGPU predpomnjenje | Hitrejša inicializacija JS | Zmanjšajte režijske stroške ponovnega prevajanja | Predpomnite artefakte prevedenih senčil (prihodnja zmogljivost izvajanja) |
| Determiniran nabor QA | Poštena primerjava modelov | Odstranite variabilnost | Fiksni seznam pozivov + `temperature=0` za ocenjevalne izvedbe |
| Ocena izhodov | Strukturiran kakovostni pogled | Premaknite se onkraj anekdot | Enostavna rubrika: koherenca / dejanskost / jedrnatost (1–5) |
| Opombe o energiji / virih | Razprava v učilnici | Prikaz kompromisov | Uporabite OS monitorje (Task Manager, `nvidia-smi`) + izhode skripte za primerjavo |
| Simulacija stroškov | Predoblačna utemeljitev | Načrtujte skaliranje | Preslikajte žetone v hipotetične oblačne cene za narativ TCO |
| Razčlenitev zakasnitve | Identificirajte ozka grla | Ciljne optimizacije | Izmerite pripravo poziva, pošiljanje zahteve, prvi žeton, popolno dokončanje |
| RAG + LLM varnostna mreža | Varnostna mreža kakovosti | Izboljšajte zahtevne poizvedbe | Če je dolžina odgovora SLM < prag ali nizka zanesljivost → nadgradite |

#### Primer hibridnega vzorca osnutek/izpopolnitev

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Skica razčlenitve zakasnitve

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Uporabite dosledne merilne okvire med modeli za poštene primerjave.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->