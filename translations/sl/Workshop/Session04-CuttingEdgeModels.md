<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T23:29:45+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "sl"
}
-->
# Seja 4: Raziskovanje najsodobnejših modelov – LLM-ji, SLM-ji in inferenca na napravi

## Povzetek

Primerjajte velike jezikovne modele (LLM-ji) in majhne jezikovne modele (SLM-ji) za scenarije inferenc lokalno proti oblaku. Naučite se vzorcev uvajanja z uporabo pospeševanja ONNX Runtime, izvajanja WebGPU in hibridnih izkušenj RAG. Vključuje demonstracijo Chainlit RAG z lokalnim modelom ter opcijsko raziskovanje OpenWebUI. Prilagodili boste začetni projekt za inferenco WebGPU in ocenili zmogljivost ter razmerje med stroški in učinkovitostjo Phi proti GPT-OSS-20B.

## Cilji učenja

- **Primerjajte** SLM proti LLM glede na zakasnitve, pomnilnik in kakovost
- **Uvedite** modele z ONNXRuntime in (kjer je podprto) WebGPU
- **Izvedite** inferenco v brskalniku (interaktivna demonstracija, ki ohranja zasebnost)
- **Integrirajte** Chainlit RAG cevovod z lokalnim SLM zaledjem
- **Ocenite** z uporabo lahkih kakovostnih + stroškovnih heuristik

## Predpogoji

- Zaključene seje 1–3
- Nameščen `chainlit` (že v `requirements.txt` za Modul08)
- Brskalnik, združljiv z WebGPU (Edge / Chrome najnovejši na Windows 11)
- Delujoč Foundry Local (`foundry status`)

### Opombe za več platform

Windows ostaja primarno ciljno okolje. Za razvijalce na macOS, ki čakajo na izvorne binarne datoteke:
1. Zaženite Foundry Local v Windows 11 VM (Parallels / UTM) ALI na oddaljeni delovni postaji Windows.
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

### 1. Primerjava Phi (SLM) proti GPT-OSS-20B (LLM) (6 min)

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

### 2. Pospeševanje ONNX Runtime (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Opazujte spremembe prepustnosti po omogočitvi GPU proti samo CPU.

### 3. Inferenca WebGPU v brskalniku (6 min)

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

Rezultati:
- Zamenjajte logiko pridobivanja z mestom za pretakanje tokenov (uporabite različico `stream=True` endpointa, ko bo omogočena)
- Dodajte graf zakasnitve (na strani odjemalca) za preklop med phi in gpt-oss-20b
- Vdelajte kontekst RAG neposredno (besedilno polje za referenčne dokumente)

## Heuristika ocenjevanja

| Kategorija | Phi-4-mini | GPT-OSS-20B | Opazovanje |
|------------|------------|-------------|------------|
| Zakasnitev (hladno) | Hitro | Počasneje | SLM se hitro ogreje |
| Pomnilnik | Nizek | Visok | Ustreznost naprave |
| Upoštevanje konteksta | Dobro | Močno | Večji model je lahko bolj zgovoren |
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
| Pridobivanje spletne strani ne uspe | CORS ali storitev ne deluje | Uporabite `curl` za preverjanje endpointa; omogočite CORS proxy, če je potrebno |
| Chainlit prazen | Okolje ni aktivno | Aktivirajte venv in ponovno namestite odvisnosti |
| Visoka zakasnitev | Model je pravkar naložen | Ogrejte z majhnim zaporedjem pozivov |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Dokumentacija Chainlit: https://docs.chainlit.io
- Ocena RAG (Ragas): https://docs.ragas.io

---

**Trajanje seje**: 30 min  
**Težavnost**: Napredno

## Primer scenarija in povezava z delavnico

| Artefakti delavnice | Scenarij | Cilj | Vir podatkov / pozivov |
|---------------------|----------|------|------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Arhitekturna ekipa ocenjuje SLM proti LLM za generator povzetkov za vodstvo | Kvantificirajte zakasnitev + razliko v uporabi tokenov | En sam `COMPARE_PROMPT` okoljski spremenljiv |
| `chainlit_app.py` (RAG demo) | Prototip notranjega asistenta za znanje | Utemeljite kratke odgovore z minimalnim leksikalnim pridobivanjem | Vgrajen seznam `DOCS` v datoteki |
| `webgpu_demo.html` | Napredna inferenca v brskalniku na napravi | Prikaz lokalnega povratnega klica z nizko zakasnitvijo + UX narativ | Samo poziv v živo uporabnika |

### Narativ scenarija
Produktna organizacija želi generator povzetkov za vodstvo. Lahek SLM (phi‑4‑mini) pripravi osnutke povzetkov; večji LLM (gpt‑oss‑20b) lahko izpopolni le poročila z visoko prioriteto. Skripte seje zajamejo empirične metrike zakasnitve in tokenov za upravičenje hibridne zasnove, medtem ko demonstracija Chainlit prikazuje, kako utemeljeno pridobivanje ohranja odgovore majhnega modela dejanske. Konceptna stran WebGPU ponuja vizijo za popolnoma odjemalsko obdelavo, ko pospeševanje brskalnika dozori.

### Minimalni kontekst RAG (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hibridni tok Osnutek→Izpopolnitev (Psevdokoda)
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
|-------|-----------|-------|-------------------------|
| Primerjalne metrike | Sledite uporabi tokenov + zakasnitvi prvega tokena | Celovit pogled na zmogljivost | Uporabite izboljšano skripto za merjenje (Seja 3) z `BENCH_STREAM=1` |
| Hibridni cevovod | Osnutek SLM → Izpopolnitev LLM | Zmanjšajte zakasnitev in stroške | Ustvarite s phi-4-mini, izpopolnite povzetek z gpt-oss-20b |
| Pretakanje UI | Boljša UX v Chainlit | Postopne povratne informacije | Uporabite `stream=True`, ko bo lokalno pretakanje omogočeno; kopičite dele |
| Predpomnjenje WebGPU | Hitrejša JS inicializacija | Zmanjšajte režijske stroške ponovnega prevajanja | Predpomnite prevedene artefakte shaderjev (prihodnja zmogljivost izvajanja) |
| Deterministični QA set | Poštena primerjava modelov | Odstranite varianco | Fiksni seznam pozivov + `temperature=0` za ocenjevalne izvedbe |
| Ocena izhoda | Strukturna kakovostna leča | Premaknite se onkraj anekdot | Enostavna rubrika: koherenca / dejanskost / jedrnatost (1–5) |
| Opombe o energiji / virih | Razprava v učilnici | Prikaz kompromisov | Uporabite OS monitorje (`foundry system info`, Upravitelj opravil, `nvidia-smi`) + izhode skripte za merjenje |
| Simulacija stroškov | Predoblačna upravičenost | Načrtujte skaliranje | Preslikajte tokene v hipotetične oblačne cene za narativ TCO |
| Razčlenitev zakasnitve | Identificirajte ozka grla | Cilj optimizacije | Izmerite pripravo poziva, pošiljanje zahteve, prvi token, popolno dokončanje |
| RAG + LLM varnostna mreža | Varnostna mreža kakovosti | Izboljšajte zahtevne poizvedbe | Če je dolžina odgovora SLM < prag ali nizka zanesljivost → eskalirajte |

#### Primer hibridnega vzorca Osnutek/Izpopolnitev

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

Uporabite dosledno merilno ogrodje med modeli za poštene primerjave.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.