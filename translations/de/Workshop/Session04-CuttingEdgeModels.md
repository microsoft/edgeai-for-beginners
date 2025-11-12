<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T21:26:30+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "de"
}
-->
# Sitzung 4: Erkundung modernster Modelle – LLMs, SLMs & On-Device Inference

## Zusammenfassung

Vergleichen Sie Large Language Models (LLMs) und Small Language Models (SLMs) für lokale vs. Cloud-Inferenzszenarien. Lernen Sie Bereitstellungsmuster kennen, die ONNX Runtime-Beschleunigung, WebGPU-Ausführung und hybride RAG-Erfahrungen nutzen. Enthält eine Chainlit RAG-Demo mit einem lokalen Modell sowie eine optionale Erkundung von OpenWebUI. Sie passen einen WebGPU-Inferenz-Starter an und bewerten die Fähigkeiten sowie Kosten-/Leistungsabwägungen von Phi vs. GPT-OSS-20B.

## Lernziele

- **Vergleichen** Sie SLM und LLM hinsichtlich Latenz, Speicherbedarf und Qualität
- **Bereitstellen** von Modellen mit ONNXRuntime und (wo unterstützt) WebGPU
- **Ausführen** von browserbasierter Inferenz (datenschutzfreundliche interaktive Demo)
- **Integrieren** einer Chainlit RAG-Pipeline mit einem lokalen SLM-Backend
- **Bewerten** mit leichtgewichtigen Qualitäts- und Kostenheuristiken

## Voraussetzungen

- Sitzungen 1–3 abgeschlossen
- `chainlit` installiert (bereits in `requirements.txt` für Modul08 enthalten)
- WebGPU-fähiger Browser (Edge / Chrome, neueste Version auf Windows 11)
- Foundry Local läuft (`foundry service status`)

### Hinweise zur plattformübergreifenden Nutzung

Windows bleibt die primäre Zielumgebung. Für macOS-Entwickler, die auf native Binärdateien warten:
1. Führen Sie Foundry Local in einer Windows 11-VM (Parallels / UTM) ODER auf einer Remote-Windows-Workstation aus.
2. Stellen Sie den Dienst (Standardport 5273) bereit und konfigurieren Sie ihn auf macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Verwenden Sie die gleichen Schritte für die Python-virtuelle Umgebung wie in den vorherigen Sitzungen.

Chainlit-Installation (beide Plattformen):
```bash
pip install chainlit
```

## Demo-Ablauf (30 Minuten)

### 1. Vergleich von Phi (SLM) vs. GPT-OSS-20B (LLM) (6 Minuten)

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

Verfolgen: Antworttiefe, faktische Genauigkeit, stilistische Vielfalt, Latenz.

Beobachten Sie Durchsatzänderungen nach Aktivierung von GPU vs. nur CPU.

### 3. WebGPU-Inferenz im Browser (6 Minuten)

Passen Sie den Starter `04-webgpu-inference` an (erstellen Sie `samples/04-cutting-edge/webgpu_demo.html`):

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

Öffnen Sie die Datei im Browser; beobachten Sie die lokale Roundtrip-Latenz.

### 4. Chainlit RAG Chat App (7 Minuten)

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

Ausführen:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Starter-Projekt: Anpassung von `04-webgpu-inference` (6 Minuten)

Liefergegenstände:
- Ersetzen Sie die Platzhalter-Logik für das Abrufen durch Streaming-Tokens (verwenden Sie die Variante `stream=True` des Endpunkts, sobald aktiviert)
- Fügen Sie ein Latenzdiagramm (clientseitig) für Phi- vs. GPT-OSS-20B-Umschaltungen hinzu
- Betten Sie den RAG-Kontext inline ein (Textbereich für Referenzdokumente)

## Bewertungsheuristiken

| Kategorie | Phi-4-mini | GPT-OSS-20B | Beobachtung |
|-----------|------------|-------------|-------------|
| Latenz (kalt) | Schnell | Langsamer | SLM wird schnell warm |
| Speicher | Niedrig | Hoch | Geräte-Machbarkeit |
| Kontexttreue | Gut | Stark | Größeres Modell kann ausführlicher sein |
| Kosten (lokal) | Minimal | Höher (Ressourcen) | Energie-/Zeit-Abwägung |
| Beste Anwendungsfälle | Edge-Apps | Tiefgründiges Denken | Hybride Pipeline möglich |

## Validierung der Umgebung

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Fehlerbehebung

| Symptom | Ursache | Maßnahme |
|---------|---------|----------|
| Webseitenauswahl schlägt fehl | CORS oder Dienst nicht verfügbar | Verwenden Sie `curl`, um den Endpunkt zu überprüfen; aktivieren Sie bei Bedarf einen CORS-Proxy |
| Chainlit leer | Umgebung nicht aktiv | Aktivieren Sie die virtuelle Umgebung und installieren Sie die Abhängigkeiten erneut |
| Hohe Latenz | Modell gerade geladen | Wärmen Sie mit einer kleinen Eingabesequenz vor |

## Referenzen

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit-Dokumentation: https://docs.chainlit.io
- RAG-Bewertung (Ragas): https://docs.ragas.io

---

**Sitzungsdauer**: 30 Minuten  
**Schwierigkeitsgrad**: Fortgeschritten

## Beispiel-Szenario & Workshop-Zuordnung

| Workshop-Artefakte | Szenario | Ziel | Daten-/Eingabequelle |
|---------------------|----------|------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Architekturteam bewertet SLM vs. LLM für Generator von Managementzusammenfassungen | Latenz- und Token-Nutzungsdifferenz quantifizieren | Einzelne Umgebungsvariable `COMPARE_PROMPT` |
| `chainlit_app.py` (RAG-Demo) | Prototyp eines internen Wissensassistenten | Kurze Antworten mit minimaler lexikalischer Suche untermauern | Inline-`DOCS`-Liste in Datei |
| `webgpu_demo.html` | Zukunftsvision für browserbasierte Inferenz auf Geräten | Lokale Roundtrip-Latenz + UX-Narrativ zeigen | Nur Live-Benutzereingabe |

### Szenario-Narrativ
Die Produktorganisation möchte einen Generator für Managementzusammenfassungen. Ein leichtgewichtiges SLM (phi‑4‑mini) erstellt Entwürfe; ein größeres LLM (gpt‑oss‑20b) kann nur hochpriorisierte Berichte verfeinern. Sitzungs-Skripte erfassen empirische Latenz- und Token-Metriken, um ein hybrides Design zu rechtfertigen, während die Chainlit-Demo zeigt, wie fundierte Suche kleine Modellantworten faktisch hält. Die WebGPU-Konzeptseite bietet einen Vision-Pfad für vollständig clientseitige Verarbeitung, wenn die Browserbeschleunigung ausgereift ist.

### Minimaler RAG-Kontext (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hybrider Entwurf→Verfeinerungsfluss (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Verfolgen Sie beide Latenzkomponenten, um den gemischten Durchschnittspreis zu berichten.

### Optionale Verbesserungen

| Fokus | Verbesserung | Warum | Implementierungshinweis |
|-------|-------------|------|-------------------------|
| Vergleichende Metriken | Token-Nutzung + Latenz des ersten Tokens verfolgen | Ganzheitliche Leistungsansicht | Verwenden Sie das erweiterte Benchmark-Skript (Sitzung 3) mit `BENCH_STREAM=1` |
| Hybride Pipeline | SLM-Entwurf → LLM-Verfeinerung | Latenz und Kosten reduzieren | Generieren mit phi-4-mini, Zusammenfassung mit gpt-oss-20b verfeinern |
| Streaming-UI | Bessere UX in Chainlit | Schrittweise Rückmeldung | Verwenden Sie `stream=True`, sobald lokales Streaming verfügbar ist; Stücke akkumulieren |
| WebGPU-Caching | Schnellere JS-Initialisierung | Neukompilierungsaufwand reduzieren | Kompilierte Shader-Artefakte zwischenspeichern (zukünftige Laufzeitfähigkeit) |
| Determinierter QA-Satz | Fairer Modellvergleich | Variabilität entfernen | Feste Eingabeliste + `temperature=0` für Bewertungsdurchläufe |
| Ausgabe-Bewertung | Strukturierte Qualitätsbewertung | Über Anekdoten hinausgehen | Einfache Rubrik: Kohärenz / Faktizität / Kürze (1–5) |
| Energie-/Ressourcenhinweise | Diskussion im Unterricht | Trade-offs zeigen | Verwenden Sie OS-Monitore (Task-Manager, `nvidia-smi`) + Benchmark-Skriptausgaben |
| Kosten-Emulation | Vorab-Rechtfertigung für Cloud | Skalierung planen | Tokens auf hypothetische Cloud-Preise für TCO-Narrativ abbilden |
| Latenz-Zerlegung | Engpässe identifizieren | Optimierungen anstreben | Eingabevorbereitung, Anforderungssendung, erstes Token, vollständige Fertigstellung messen |
| RAG + LLM-Fallback | Qualitätssicherheitsnetz | Schwierige Anfragen verbessern | Wenn SLM-Antwortlänge < Schwellenwert oder geringe Zuversicht → eskalieren |

#### Beispiel für hybrides Entwurf/Verfeinerungsmuster

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Skizze zur Latenz-Zerlegung

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Verwenden Sie konsistente Messgerüste über Modelle hinweg für faire Vergleiche.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->