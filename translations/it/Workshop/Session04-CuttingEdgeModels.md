<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T22:48:48+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "it"
}
-->
# Sessione 4: Esplora Modelli All'Avanguardia – LLM, SLM e Inferenza Locale

## Abstract

Confronta i Large Language Models (LLM) e i Small Language Models (SLM) per scenari di inferenza locale vs cloud. Scopri i modelli di distribuzione che sfruttano l'accelerazione di ONNX Runtime, l'esecuzione WebGPU e le esperienze ibride RAG. Include una demo di Chainlit RAG con un modello locale e un'esplorazione opzionale di OpenWebUI. Adatterai un starter per l'inferenza WebGPU e valuterai le capacità e i compromessi tra costo/prestazioni di Phi e GPT-OSS-20B.

## Obiettivi di Apprendimento

- **Confrontare** SLM e LLM in termini di latenza, memoria e qualità
- **Distribuire** modelli con ONNXRuntime e (dove supportato) WebGPU
- **Eseguire** inferenza basata su browser (demo interattiva che preserva la privacy)
- **Integrare** una pipeline Chainlit RAG con un backend SLM locale
- **Valutare** utilizzando metriche leggere di qualità e costo

## Prerequisiti

- Completamento delle sessioni 1–3
- `chainlit` installato (già incluso in `requirements.txt` per il Modulo08)
- Browser compatibile con WebGPU (Edge / Chrome aggiornati su Windows 11)
- Foundry Local in esecuzione (`foundry service status`)

### Note Cross-Platform

Windows rimane l'ambiente target principale. Per gli sviluppatori macOS in attesa di binari nativi:
1. Esegui Foundry Local in una VM Windows 11 (Parallels / UTM) O su una workstation Windows remota.
2. Esporre il servizio (porta predefinita 5273) e configurare su macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Usa gli stessi passaggi per l'ambiente virtuale Python delle sessioni precedenti.

Installazione di Chainlit (entrambi i sistemi):
```bash
pip install chainlit
```

## Flusso Demo (30 min)

### 1. Confronta Phi (SLM) vs GPT-OSS-20B (LLM) (6 min)

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

Traccia: profondità delle risposte, accuratezza fattuale, ricchezza stilistica, latenza.

Osserva i cambiamenti di throughput dopo aver abilitato GPU rispetto a solo CPU.

### 3. Inferenza WebGPU nel Browser (6 min)

Adatta lo starter `04-webgpu-inference` (crea `samples/04-cutting-edge/webgpu_demo.html`):

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

Apri il file in un browser; osserva il roundtrip locale a bassa latenza.

### 4. App Chat Chainlit RAG (7 min)

`samples/04-cutting-edge/chainlit_app.py` minimale:

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

Esegui:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Progetto Starter: Adatta `04-webgpu-inference` (6 min)

Deliverables:
- Sostituisci la logica di fetch placeholder con token in streaming (usa la variante endpoint `stream=True` una volta abilitata)
- Aggiungi un grafico di latenza (lato client) per i toggle phi vs gpt-oss-20b
- Incorpora il contesto RAG inline (textarea per documenti di riferimento)

## Metriche di Valutazione

| Categoria | Phi-4-mini | GPT-OSS-20B | Osservazione |
|----------|------------|-------------|-------------|
| Latenza (fredda) | Veloce | Più lenta | SLM si riscalda rapidamente |
| Memoria | Bassa | Alta | Fattibilità sul dispositivo |
| Adesione al contesto | Buona | Forte | Modello più grande può essere più prolisso |
| Costo (locale) | Minimo | Più alto (risorse) | Compromesso energia/tempo |
| Miglior caso d'uso | App edge | Ragionamento profondo | Pipeline ibrida possibile |

## Validazione dell'Ambiente

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Risoluzione dei Problemi

| Sintomo | Causa | Azione |
|---------|-------|--------|
| Fallimento fetch pagina web | CORS o servizio non disponibile | Usa `curl` per verificare l'endpoint; abilita proxy CORS se necessario |
| Chainlit vuoto | Env non attivo | Attiva venv e reinstalla le dipendenze |
| Alta latenza | Modello appena caricato | Riscalda con una sequenza di prompt breve |

## Riferimenti

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentazione Chainlit: https://docs.chainlit.io
- Valutazione RAG (Ragas): https://docs.ragas.io

---

**Durata della Sessione**: 30 min  
**Difficoltà**: Avanzata

## Scenario di Esempio e Mappatura Workshop

| Artefatti Workshop | Scenario | Obiettivo | Fonte Dati / Prompt |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Team di architettura che valuta SLM vs LLM per generatore di sintesi esecutiva | Quantificare latenza + delta utilizzo token | Variabile env `COMPARE_PROMPT` singola |
| `chainlit_app.py` (demo RAG) | Prototipo assistente di conoscenza interno | Risposte brevi basate su recupero lessicale minimo | Lista `DOCS` inline nel file |
| `webgpu_demo.html` | Anteprima inferenza browser futuristica sul dispositivo | Mostra roundtrip locale a bassa latenza + narrativa UX | Solo prompt utente live |

### Narrazione dello Scenario
L'organizzazione prodotto desidera un generatore di briefing esecutivo. Un SLM leggero (phi‑4‑mini) redige sintesi; un LLM più grande (gpt‑oss‑20b) può affinare solo i report ad alta priorità. Gli script della sessione catturano metriche empiriche di latenza e token per giustificare un design ibrido, mentre la demo Chainlit illustra come il recupero basato su fonti mantiene le risposte del modello piccolo fattuali. La pagina concettuale WebGPU fornisce un percorso di visione per l'elaborazione completamente client-side quando l'accelerazione del browser maturerà.

### Contesto RAG Minimo (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Flusso Ibrido Bozza→Affinamento (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Traccia entrambi i componenti di latenza per riportare il costo medio misto.

### Miglioramenti Opzionali

| Focus | Miglioramento | Perché | Suggerimento Implementazione |
|-------|------------|-----|---------------------|
| Metriche Comparative | Traccia utilizzo token + latenza primo token | Vista prestazioni olistica | Usa script di benchmark migliorato (Sessione 3) con `BENCH_STREAM=1` |
| Pipeline Ibrida | Bozza SLM → Affinamento LLM | Riduci latenza e costo | Genera con phi-4-mini, affina sintesi con gpt-oss-20b |
| UI Streaming | Migliore UX in Chainlit | Feedback incrementale | Usa `stream=True` una volta esposto lo streaming locale; accumula chunk |
| Caching WebGPU | Inizializzazione JS più veloce | Riduci overhead di ricompilazione | Cache artefatti shader compilati (capacità runtime futura) |
| Set QA Deterministico | Confronto equo tra modelli | Rimuovi variabilità | Lista prompt fissa + `temperature=0` per esecuzioni di valutazione |
| Scoring Output | Lente di qualità strutturata | Supera gli aneddoti | Rubrica semplice: coerenza / factualità / brevità (1–5) |
| Note Energia / Risorse | Discussione in aula | Mostra compromessi | Usa monitor OS (Task Manager, `nvidia-smi`) + output script benchmark |
| Emulazione Costo | Giustificazione pre-cloud | Pianifica scalabilità | Mappa token a prezzi cloud ipotetici per narrativa TCO |
| Decomposizione Latenza | Identifica colli di bottiglia | Ottimizza target | Misura preparazione prompt, invio richiesta, primo token, completamento completo |
| RAG + LLM Fallback | Rete di sicurezza qualità | Migliora query difficili | Se lunghezza risposta SLM < soglia o bassa fiducia → escalation |

#### Esempio Pattern Bozza/Affinamento Ibrido

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Schizzo Decomposizione Latenza

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Usa una struttura di misurazione coerente tra i modelli per confronti equi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->