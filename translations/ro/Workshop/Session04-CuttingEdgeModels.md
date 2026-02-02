# Sesiunea 4: Explorarea modelelor de ultimă generație – LLM-uri, SLM-uri și inferență pe dispozitiv

## Rezumat

Comparați Modelele de Limbaj Extins (LLM-uri) și Modelele de Limbaj Redus (SLM-uri) pentru scenarii de inferență locală vs. în cloud. Aflați modele de implementare care utilizează accelerarea ONNX Runtime, execuția WebGPU și experiențe hibride RAG. Include o demonstrație Chainlit RAG cu un model local plus o explorare opțională OpenWebUI. Veți adapta un starter de inferență WebGPU și veți evalua capacitatea și compromisurile cost/performanță ale Phi vs GPT-OSS-20B.

## Obiective de învățare

- **Comparați** SLM vs LLM pe axele de latență, memorie, calitate
- **Implementați** modele cu ONNXRuntime și (unde este suportat) WebGPU
- **Rulați** inferență bazată pe browser (demonstrație interactivă care protejează confidențialitatea)
- **Integrați** un pipeline Chainlit RAG cu un backend SLM local
- **Evaluați** utilizând euristici ușoare de calitate + cost

## Cerințe preliminare

- Finalizarea sesiunilor 1–3
- `chainlit` instalat (deja inclus în `requirements.txt` pentru Modulul08)
- Browser compatibil WebGPU (Edge / Chrome ultima versiune pe Windows 11)
- Foundry Local activ (`foundry service status`)

### Note pentru platforme multiple

Windows rămâne mediul țintă principal. Pentru dezvoltatorii macOS care așteaptă binare native:
1. Rulați Foundry Local într-o mașină virtuală Windows 11 (Parallels / UTM) SAU pe o stație de lucru Windows la distanță.
2. Expuneți serviciul (port implicit 5273) și setați pe macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Utilizați aceleași pași pentru mediul virtual Python ca în sesiunile anterioare.

Instalare Chainlit (ambele platforme):
```bash
pip install chainlit
```

## Fluxul demonstrației (30 min)

### 1. Comparați Phi (SLM) vs GPT-OSS-20B (LLM) (6 min)

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

Urmăriți: profunzimea răspunsului, acuratețea factuală, bogăția stilistică, latența.

Observați schimbările de throughput după activarea GPU vs doar CPU.

### 3. Inferență WebGPU în browser (6 min)

Adaptați starterul `04-webgpu-inference` (creați `samples/04-cutting-edge/webgpu_demo.html`):

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

Deschideți fișierul într-un browser; observați latența redusă în procesarea locală.

### 4. Aplicație de chat Chainlit RAG (7 min)

Minimal `samples/04-cutting-edge/chainlit_app.py`:

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

Rulați:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Proiect starter: Adaptați `04-webgpu-inference` (6 min)

Livrabile:
- Înlocuiți logica de fetch placeholder cu tokenuri de streaming (utilizați varianta endpoint `stream=True` odată activată)
- Adăugați un grafic de latență (client-side) pentru comutările phi vs gpt-oss-20b
- Încorporați contextul RAG inline (textarea pentru documente de referință)

## Euristici de evaluare

| Categorie | Phi-4-mini | GPT-OSS-20B | Observație |
|-----------|------------|-------------|------------|
| Latență (rece) | Rapid | Mai lent | SLM se încălzește rapid |
| Memorie | Scăzută | Ridicată | Fezabilitate pe dispozitiv |
| Respectarea contextului | Bună | Puternică | Modelul mai mare poate fi mai detaliat |
| Cost (local) | Minim | Mai mare (resurse) | Compromis energie/timp |
| Cel mai bun caz de utilizare | Aplicații edge | Raționament profund | Pipeline hibrid posibil |

## Validarea mediului

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Depanare

| Simptom | Cauză | Acțiune |
|---------|-------|--------|
| Eșec la preluarea paginii web | CORS sau serviciu inactiv | Utilizați `curl` pentru a verifica endpoint-ul; activați proxy CORS dacă este necesar |
| Chainlit gol | Mediu inactiv | Activați venv și reinstalați dependențele |
| Latență ridicată | Modelul tocmai a fost încărcat | Încălziți cu o secvență de prompturi mici |

## Referințe

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentație Chainlit: https://docs.chainlit.io
- Evaluare RAG (Ragas): https://docs.ragas.io

---

**Durata sesiunii**: 30 min  
**Dificultate**: Avansat

## Scenariu exemplu și mapare workshop

| Artefacte workshop | Scenariu | Obiectiv | Sursă date / prompt |
|--------------------|----------|----------|---------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Echipa de arhitectură evaluează SLM vs LLM pentru generatorul de rezumate executive | Cuantificarea diferenței de latență + utilizare tokenuri | Variabilă de mediu unică `COMPARE_PROMPT` |
| `chainlit_app.py` (demo RAG) | Prototip asistent de cunoștințe intern | Răspunsuri scurte fundamentate cu recuperare lexicală minimă | Lista `DOCS` inline în fișier |
| `webgpu_demo.html` | Previzualizare inferență futuristă pe browser | Arată procesarea locală cu latență redusă + narațiune UX | Doar prompt utilizator live |

### Narațiunea scenariului
Organizația de produs dorește un generator de briefing-uri executive. Un SLM ușor (phi‑4‑mini) redactează rezumate; un LLM mai mare (gpt‑oss‑20b) poate rafina doar rapoartele de prioritate înaltă. Scripturile sesiunii capturează latența empirică și metricile tokenurilor pentru a justifica un design hibrid, în timp ce demonstrația Chainlit ilustrează cum recuperarea fundamentată menține răspunsurile modelului mic factuale. Pagina conceptuală WebGPU oferă o cale de viziune pentru procesarea complet client-side atunci când accelerarea browserului se maturizează.

### Context RAG minimal (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Flux hibrid Draft→Refine (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Urmăriți ambele componente de latență pentru a raporta costul mediu combinat.

### Îmbunătățiri opționale

| Focus | Îmbunătățire | Motiv | Indicație de implementare |
|-------|-------------|-------|---------------------------|
| Metrici comparative | Urmăriți utilizarea tokenurilor + latența primului token | Vedere holistică a performanței | Utilizați scriptul de benchmark îmbunătățit (Sesiunea 3) cu `BENCH_STREAM=1` |
| Pipeline hibrid | Draft SLM → Rafinat LLM | Reduceți latența și costul | Generați cu phi-4-mini, rafinați rezumatul cu gpt-oss-20b |
| UI de streaming | UX mai bun în Chainlit | Feedback incremental | Utilizați `stream=True` odată ce streaming-ul local este expus; acumulați fragmente |
| Caching WebGPU | Inițializare JS mai rapidă | Reduceți suprasarcina recompilării | Cache artefacte shader compilate (capacitate runtime viitoare) |
| Set QA determinist | Comparație echitabilă a modelelor | Eliminați variația | Listă de prompturi fixă + `temperature=0` pentru rulările de evaluare |
| Scorarea outputului | Lentilă de calitate structurată | Depășirea anecdoticelor | Rubrică simplă: coerență / factualitate / concizie (1–5) |
| Note energie / resurse | Discuție în clasă | Arătați compromisurile | Utilizați monitoare OS (Task Manager, `nvidia-smi`) + ieșiri script benchmark |
| Emulare cost | Justificare pre-cloud | Planificați scalarea | Maparea tokenurilor la prețuri ipotetice de cloud pentru narațiunea TCO |
| Decompoziția latenței | Identificați blocajele | Țintiți optimizările | Măsurați pregătirea promptului, trimiterea cererii, primul token, completarea totală |
| RAG + fallback LLM | Plasă de siguranță pentru calitate | Îmbunătățirea interogărilor dificile | Dacă lungimea răspunsului SLM < prag sau încrederea scăzută → escaladare |

#### Exemplu de model hibrid Draft/Refine

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Schiță decompoziție latență

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Utilizați o structură consistentă de măsurare între modele pentru comparații echitabile.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->