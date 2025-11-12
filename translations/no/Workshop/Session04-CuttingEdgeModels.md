<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T23:20:30+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "no"
}
-->
# Sesjon 4: Utforsk banebrytende modeller – LLMs, SLMs og lokal inferens

## Sammendrag

Sammenlign Large Language Models (LLMs) og Small Language Models (SLMs) for lokale vs skybaserte inferensscenarier. Lær distribusjonsmønstre som utnytter ONNX Runtime-akselerasjon, WebGPU-eksekvering og hybride RAG-opplevelser. Inkluderer en Chainlit RAG-demo med en lokal modell samt en valgfri utforskning av OpenWebUI. Du vil tilpasse en WebGPU-inferensstarter og evaluere Phi vs GPT-OSS-20B med hensyn til kapasitet og kostnad/ytelse.

## Læringsmål

- **Sammenligne** SLM vs LLM med hensyn til forsinkelse, minne og kvalitet
- **Distribuere** modeller med ONNXRuntime og (der det støttes) WebGPU
- **Kjøre** nettleserbasert inferens (personvernbevarende interaktiv demo)
- **Integrere** en Chainlit RAG-pipeline med en lokal SLM-backend
- **Evaluere** ved hjelp av lette kvalitets- og kostnadsheuristikker

## Forutsetninger

- Sesjonene 1–3 fullført
- `chainlit` installert (allerede i `requirements.txt` for Modul08)
- WebGPU-kompatibel nettleser (Edge / Chrome siste versjon på Windows 11)
- Foundry Local kjører (`foundry service status`)

### Tverrplattformnotater

Windows forblir det primære målet. For macOS-utviklere som venter på native binærfiler:
1. Kjør Foundry Local i en Windows 11 VM (Parallels / UTM) ELLER en ekstern Windows-arbeidsstasjon.
2. Eksponer tjenesten (standardport 5273) og sett opp på macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Bruk de samme Python-virtuelle miljøtrinnene som i tidligere sesjoner.

Chainlit-installasjon (begge plattformer):
```bash
pip install chainlit
```

## Demo-flyt (30 min)

### 1. Sammenlign Phi (SLM) vs GPT-OSS-20B (LLM) (6 min)

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

Spor: responsdybde, faktanøyaktighet, stilistisk rikdom, forsinkelse.

Observer endringer i gjennomstrømning etter aktivering av GPU vs kun CPU.

### 3. WebGPU-inferens i nettleser (6 min)

Tilpass starteren `04-webgpu-inference` (lag `samples/04-cutting-edge/webgpu_demo.html`):

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

Åpne filen i en nettleser; observer lav forsinkelse ved lokal rundtur.

### 4. Chainlit RAG Chat App (7 min)

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

Kjør:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Startprosjekt: Tilpass `04-webgpu-inference` (6 min)

Leveranser:
- Erstatt plassholderlogikk for henting med strømming av tokens (bruk `stream=True` endepunktvariant når aktivert)
- Legg til forsinkelsesdiagram (klientsiden) for Phi vs GPT-OSS-20B-alternativer
- Innebygg RAG-kontekst (tekstområde for referansedokumenter)

## Evalueringsheuristikker

| Kategori | Phi-4-mini | GPT-OSS-20B | Observasjon |
|----------|------------|-------------|-------------|
| Forsinkelse (kald) | Rask | Langsommere | SLM varmes raskt opp |
| Minne | Lavt | Høyt | Enhetsmulighet |
| Kontekstadhering | God | Sterk | Større modell kan være mer detaljert |
| Kostnad (lokalt) | Minimal | Høyere (ressurser) | Energi/tid-avveining |
| Beste bruksområde | Kantapper | Dyp resonnering | Hybrid pipeline mulig |

## Validering av miljø

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Feilsøking

| Symptom | Årsak | Handling |
|---------|-------|--------|
| Nettleserhenting mislykkes | CORS eller tjeneste nede | Bruk `curl` for å verifisere endepunkt; aktiver CORS-proxy hvis nødvendig |
| Chainlit blank | Miljø ikke aktivt | Aktiver venv og installer avhengigheter på nytt |
| Høy forsinkelse | Modell nettopp lastet | Varm opp med liten promptsekvens |

## Referanser

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit-dokumentasjon: https://docs.chainlit.io
- RAG-evaluering (Ragas): https://docs.ragas.io

---

**Sesjonsvarighet**: 30 min  
**Vanskelighetsgrad**: Avansert

## Eksempelscenario og workshopkartlegging

| Workshop-artefakter | Scenario | Mål | Data / promptkilde |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Arkitekturteam som evaluerer SLM vs LLM for generering av lederoppsummeringer | Kvantifisere forsinkelse + tokenbruk | Enkelt `COMPARE_PROMPT` miljøvariabel |
| `chainlit_app.py` (RAG-demo) | Intern kunnskapsassistentprototype | Grunnleggende korte svar med minimal leksikalsk henting | Innebygd `DOCS`-liste i filen |
| `webgpu_demo.html` | Fremtidsrettet lokal nettleserinferens | Vise lav forsinkelse ved lokal rundtur + UX-narrativ | Kun live brukerprompt |

### Scenarionarrativ
Produktorganisasjonen ønsker en generator for lederoppsummeringer. En lett SLM (phi-4-mini) lager utkast til oppsummeringer; en større LLM (gpt-oss-20b) kan kun finjustere høyprioriterte rapporter. Sesjonsskriptene fanger empiriske forsinkelses- og tokenmålinger for å rettferdiggjøre et hybriddesign, mens Chainlit-demoen illustrerer hvordan grunnlagt henting holder små modellers svar faktuelle. WebGPU-konseptet gir en visjonsvei for fullstendig klientsidebehandling når nettleserakselerasjon modnes.

### Minimal RAG-kontekst (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hybrid Utkast→Finjusteringsflyt (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Spor begge forsinkelseskomponentene for å rapportere blandet gjennomsnittskostnad.

### Valgfrie forbedringer

| Fokus | Forbedring | Hvorfor | Implementeringshint |
|-------|------------|-----|---------------------|
| Sammenligningsmetrikker | Spor tokenbruk + første-token forsinkelse | Helhetlig ytelsesoversikt | Bruk forbedret benchmark-skript (Sesjon 3) med `BENCH_STREAM=1` |
| Hybrid pipeline | SLM-utkast → LLM-finjustering | Redusere forsinkelse og kostnad | Generer med phi-4-mini, finjuster oppsummering med gpt-oss-20b |
| Strømmings-UI | Bedre UX i Chainlit | Inkrementell tilbakemelding | Bruk `stream=True` når lokal strømming er eksponert; akkumulere biter |
| WebGPU-caching | Raskere JS-initiering | Redusere omkompileringskostnader | Cache kompilerte shader-artefakter (fremtidig runtime-funksjonalitet) |
| Deterministisk QA-sett | Rettferdig modell-sammenligning | Fjern variasjon | Fast promptliste + `temperature=0` for evalueringskjøringer |
| Output-vurdering | Strukturert kvalitetslinse | Gå utover anekdoter | Enkel rubrikk: sammenheng / faktualitet / korthet (1–5) |
| Energi / ressursnotater | Klassediskusjon | Vise avveininger | Bruk OS-monitorer (Oppgavebehandling, `nvidia-smi`) + benchmark-skriptutganger |
| Kostnadsemulering | Pre-skybegrunnelse | Planlegg skalering | Kartlegg tokens til hypotetisk skyprissetting for TCO-narrativ |
| Forsinkelsesdekomponering | Identifisere flaskehalser | Målrettede optimaliseringer | Mål promptforberedelse, forespørselssending, første token, fullføring |
| RAG + LLM-fallback | Kvalitetssikkerhetsnett | Forbedre vanskelige spørsmål | Hvis SLM-svarlengde < terskel eller lav tillit → eskaler |

#### Eksempel på hybrid utkast/finjusteringsmønster

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Skisse for forsinkelsesnedbrytning

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Bruk konsistent målingsrammeverk på tvers av modeller for rettferdige sammenligninger.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->