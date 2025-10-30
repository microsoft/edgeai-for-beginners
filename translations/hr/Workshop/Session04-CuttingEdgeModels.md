<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T23:24:49+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "hr"
}
-->
# Sesija 4: Istraživanje najnovijih modela – LLM-ovi, SLM-ovi i lokalna inferencija

## Sažetak

Usporedite velike jezične modele (LLM-ove) i male jezične modele (SLM-ove) za scenarije lokalne i cloud inferencije. Naučite obrasce implementacije koristeći ubrzanje ONNX Runtime-a, izvršavanje putem WebGPU-a i hibridna RAG iskustva. Uključuje Chainlit RAG demo s lokalnim modelom i opcionalno istraživanje OpenWebUI-a. Prilagodit ćete početni projekt za WebGPU inferenciju i procijeniti sposobnosti Phi-a u usporedbi s GPT-OSS-20B, kao i omjere troškova i performansi.

## Ciljevi učenja

- **Usporedite** SLM i LLM prema latenciji, memoriji i kvaliteti
- **Implementirajte** modele koristeći ONNXRuntime i (gdje je podržano) WebGPU
- **Pokrenite** inferenciju u pregledniku (interaktivni demo koji čuva privatnost)
- **Integrirajte** Chainlit RAG pipeline s lokalnim SLM backendom
- **Procijenite** koristeći lagane heuristike kvalitete i troškova

## Preduvjeti

- Završene sesije 1–3
- Instaliran `chainlit` (već uključen u `requirements.txt` za Modul08)
- Preglednik s podrškom za WebGPU (najnoviji Edge / Chrome na Windows 11)
- Pokrenut Foundry Local (`foundry status`)

### Napomene za više platformi

Windows ostaje primarno ciljno okruženje. Za macOS developere koji čekaju native binarne datoteke:
1. Pokrenite Foundry Local u Windows 11 VM-u (Parallels / UTM) ILI na udaljenoj Windows radnoj stanici.
2. Izložite uslugu (zadani port 5273) i postavite na macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Koristite iste korake za Python virtualno okruženje kao u prethodnim sesijama.

Instalacija Chainlit-a (za obje platforme):
```bash
pip install chainlit
```

## Demo tijek (30 min)

### 1. Usporedba Phi (SLM) i GPT-OSS-20B (LLM) (6 min)

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

Pratite: dubinu odgovora, točnost činjenica, stilsku bogatost, latenciju.

### 2. Ubrzanje ONNX Runtime-a (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Promatrajte promjene u propusnosti nakon omogućavanja GPU-a u odnosu na samo CPU.

### 3. WebGPU inferencija u pregledniku (6 min)

Prilagodite početni projekt `04-webgpu-inference` (kreirajte `samples/04-cutting-edge/webgpu_demo.html`):

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

Otvorite datoteku u pregledniku; promatrajte lokalni povratni put s niskom latencijom.

### 4. Chainlit RAG aplikacija za chat (7 min)

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

Pokrenite:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Početni projekt: Prilagodite `04-webgpu-inference` (6 min)

Rezultati:
- Zamijenite logiku za dohvaćanje s placeholderom za streaming tokena (koristite varijantu endpointa `stream=True` kada bude omogućena)
- Dodajte grafikon latencije (na strani klijenta) za prebacivanje između phi i gpt-oss-20b
- Ugradite RAG kontekst unutar (tekstualno polje za referentne dokumente)

## Heuristika procjene

| Kategorija | Phi-4-mini | GPT-OSS-20B | Zapažanje |
|------------|------------|-------------|-----------|
| Latencija (hladno) | Brza | Sporija | SLM se brzo zagrijava |
| Memorija | Niska | Visoka | Izvedivost na uređaju |
| Pridržavanje konteksta | Dobro | Jako | Veći model može biti opširniji |
| Trošak (lokalno) | Minimalan | Viši (resursi) | Kompromis između energije i vremena |
| Najbolji slučaj upotrebe | Aplikacije na rubu | Duboko razmišljanje | Moguća hibridna pipeline |

## Provjera okruženja

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Rješavanje problema

| Simptom | Uzrok | Akcija |
|---------|-------|--------|
| Neuspješno dohvaćanje web stranice | CORS ili usluga ne radi | Koristite `curl` za provjeru endpointa; omogućite CORS proxy ako je potrebno |
| Chainlit prazan | Okruženje nije aktivno | Aktivirajte venv i ponovno instalirajte ovisnosti |
| Visoka latencija | Model je upravo učitan | Zagrijte s malom sekvencom upita |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit dokumentacija: https://docs.chainlit.io
- RAG evaluacija (Ragas): https://docs.ragas.io

---

**Trajanje sesije**: 30 min  
**Težina**: Napredno

## Primjer scenarija i mapiranje radionice

| Artefakti radionice | Scenarij | Cilj | Izvor podataka / upita |
|---------------------|----------|------|------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Tim za arhitekturu procjenjuje SLM i LLM za generator sažetaka za izvršne funkcije | Kvantificirajte latenciju + razliku u korištenju tokena | Jedna varijabla okruženja `COMPARE_PROMPT` |
| `chainlit_app.py` (RAG demo) | Prototip internog asistenta za znanje | Utemeljite kratke odgovore s minimalnim leksičkim dohvatom | Ugrađena lista `DOCS` u datoteci |
| `webgpu_demo.html` | Pregled inferencije u pregledniku na uređaju u budućnosti | Prikaz lokalnog povratnog puta s niskom latencijom + narativ UX-a | Samo živi korisnički upit |

### Narativ scenarija
Organizacija proizvoda želi generator sažetaka za izvršne funkcije. Lagani SLM (phi‑4‑mini) izrađuje nacrte sažetaka; veći LLM (gpt‑oss‑20b) može doraditi samo izvješća visokog prioriteta. Skripte sesije bilježe empirijsku latenciju i metrike tokena kako bi opravdale hibridni dizajn, dok Chainlit demo ilustrira kako utemeljeni dohvat održava odgovore malog modela točnima. Konceptna stranica za WebGPU pruža viziju za potpuno obradu na strani klijenta kada ubrzanje preglednika sazrije.

### Minimalni RAG kontekst (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hibridni tijek Nacrt→Dorada (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Pratite obje komponente latencije kako biste prijavili prosječne troškove.

### Opcionalna poboljšanja

| Fokus | Poboljšanje | Zašto | Savjet za implementaciju |
|-------|------------|------|--------------------------|
| Usporedne metrike | Pratite korištenje tokena + latenciju prvog tokena | Holistički pregled performansi | Koristite poboljšanu skriptu za benchmark (Sesija 3) s `BENCH_STREAM=1` |
| Hibridna pipeline | Nacrt SLM → Dorada LLM | Smanjite latenciju i troškove | Generirajte s phi-4-mini, doradite sažetak s gpt-oss-20b |
| Streaming UI | Bolji UX u Chainlit-u | Postupne povratne informacije | Koristite `stream=True` kada lokalni streaming bude dostupan; akumulirajte dijelove |
| WebGPU predmemorija | Brži JS inicijalizacija | Smanjite troškove ponovne kompilacije | Predmemorirajte artefakte kompajliranih shadera (buduća sposobnost runtime-a) |
| Deterministički QA set | Pravedna usporedba modela | Uklonite varijabilnost | Fiksni popis upita + `temperature=0` za evaluacijske pokuse |
| Ocjenjivanje izlaza | Strukturalna kvalitativna analiza | Izađite iz anegdota | Jednostavna rubrika: koherentnost / točnost / sažetost (1–5) |
| Bilješke o energiji / resursima | Diskusija u učionici | Prikaz kompromisa | Koristite OS monitore (`foundry system info`, Task Manager, `nvidia-smi`) + izlaze skripti za benchmark |
| Simulacija troškova | Opravdanje prije oblaka | Planiranje skaliranja | Mapirajte tokene na hipotetske cijene oblaka za narativ TCO-a |
| Razlaganje latencije | Identificirajte uska grla | Ciljajte optimizacije | Mjerite pripremu upita, slanje zahtjeva, prvi token, potpuno dovršenje |
| RAG + LLM rezervna opcija | Sigurnosna mreža kvalitete | Poboljšajte teške upite | Ako je duljina odgovora SLM-a < prag ili niska pouzdanost → eskalirajte |

#### Primjer hibridnog uzorka Nacrt/Dorada

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Skica razlaganja latencije

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Koristite dosljedne okvire za mjerenje između modela za pravedne usporedbe.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.