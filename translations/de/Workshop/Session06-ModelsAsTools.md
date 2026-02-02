# Sitzung 6: Foundry Local – Modelle als Werkzeuge

## Zusammenfassung

Behandeln Sie Modelle als zusammensetzbare Werkzeuge innerhalb einer lokalen KI-Betriebsschicht. Diese Sitzung zeigt, wie man mehrere spezialisierte SLM/LLM-Aufrufe verknüpft, Aufgaben gezielt weiterleitet und eine einheitliche SDK-Oberfläche für Anwendungen bereitstellt. Sie werden einen leichtgewichtigen Modell-Router + Aufgabenplaner erstellen, ihn in ein App-Skript integrieren und den Skalierungspfad zu Azure AI Foundry für Produktionslasten skizzieren.

## Lernziele

- **Konzeptualisieren** von Modellen als atomare Werkzeuge mit definierten Fähigkeiten
- **Weiterleiten** von Anfragen basierend auf Absicht / heuristischer Bewertung
- **Verknüpfen** von Ausgaben über mehrstufige Aufgaben (zerlegen → lösen → verfeinern)
- **Integrieren** einer einheitlichen Client-API für nachgelagerte Anwendungen
- **Skalieren** des Designs in die Cloud (gleicher OpenAI-kompatibler Vertrag)

## Voraussetzungen

- Sitzungen 1–5 abgeschlossen
- Mehrere lokale Modelle zwischengespeichert (z. B. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Plattformübergreifender Umgebungs-Schnipsel

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Remote-/VM-Dienstzugriff von macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo-Ablauf (30 Minuten)

### 1. Erklärung der Werkzeugfähigkeiten (5 Minuten)

Erstellen Sie `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Absichtserkennung & Weiterleitung (8 Minuten)

Erstellen Sie `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Mehrstufige Aufgabenverknüpfung (7 Minuten)

Erstellen Sie `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Starter-Projekt: Anpassung von `06-models-as-tools` (5 Minuten)

Verbesserungen:
- Unterstützung für Streaming-Token hinzufügen (progressive UI-Aktualisierung)
- Vertrauensbewertung hinzufügen: lexikalische Übereinstimmung oder Prompt-Richtlinie
- Trace-JSON exportieren (Absicht → Modell → Latenz → Token-Nutzung)
- Cache-Wiederverwendung für wiederholte Teilaufgaben implementieren

### 5. Skalierungspfad zu Azure (5 Minuten)

| Ebene | Lokal (Foundry) | Cloud (Azure AI Foundry) | Übergangsstrategie |
|-------|-----------------|--------------------------|---------------------|
| Weiterleitung | Heuristische Python | Dauerhafter Microservice | API containerisieren & bereitstellen |
| Modelle | SLMs zwischengespeichert | Verwaltete Bereitstellungen | Lokale Namen auf Bereitstellungs-IDs abbilden |
| Beobachtbarkeit | CLI-Statistiken/manuell | Zentrales Logging & Metriken | Strukturierte Trace-Ereignisse hinzufügen |
| Sicherheit | Nur lokaler Host | Azure-Authentifizierung / Netzwerk | Key Vault für Geheimnisse einführen |
| Kosten | Geräte-Ressourcen | Verbrauchsabrechnung | Budget-Schutzmaßnahmen hinzufügen |

## Validierungs-Checkliste

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Erwarten Sie eine absichtsbasierte Modellauswahl und eine abschließend verfeinerte Ausgabe.

## Fehlerbehebung

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Alle Aufgaben werden an dasselbe Modell weitergeleitet | Schwache Regeln | INTENT_RULES-Regelsatz erweitern |
| Pipeline scheitert mitten im Schritt | Fehlendes Modell geladen | Führen Sie `foundry model run <model>` aus |
| Niedrige Kohäsion der Ausgabe | Keine Verfeinerungsphase | Zusammenfassungs-/Validierungsschritt hinzufügen |

## Referenzen

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry-Dokumentation: https://learn.microsoft.com/azure/ai-foundry
- Prompt-Qualitätsmuster: Siehe Sitzung 2

---

**Sitzungsdauer**: 30 Minuten  
**Schwierigkeitsgrad**: Experte

## Beispiel-Szenario & Workshop-Zuordnung

| Workshop-Skripte / Notebooks | Szenario | Ziel | Datensatz / Katalogquelle |
|------------------------------|----------|------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Entwicklerassistent, der gemischte Absichtsprompts bearbeitet (refaktorieren, zusammenfassen, klassifizieren) | Heuristische Absicht → Modell-Alias-Weiterleitung mit Token-Nutzung | Inline `CATALOG` + Regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Mehrstufige Planung & Verfeinerung für komplexe Aufgaben der Codeunterstützung | Zerlegen → spezialisierte Ausführung → Zusammenfassungs-Verfeinerungsschritt | Gleicher `CATALOG`; Schritte abgeleitet aus Plan-Ausgabe |

### Szenario-Erzählung
Ein Tool zur Produktivitätssteigerung für Ingenieure erhält heterogene Aufgaben: Code refaktorieren, architektonische Notizen zusammenfassen, Feedback klassifizieren. Um Latenz und Ressourcenverbrauch zu minimieren, plant und fasst ein kleines allgemeines Modell zusammen, ein auf Code spezialisiertes Modell übernimmt die Refaktorisierung, und ein leichtgewichtiges Modell mit Klassifikationsfähigkeiten etikettiert Feedback. Das Pipeline-Skript demonstriert Verknüpfung + Verfeinerung; das Router-Skript isoliert adaptive Einzel-Prompt-Weiterleitung.

### Katalog-Snapshot
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Beispiel-Test-Prompts
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Trace-Erweiterung (Optional)
Fügen Sie pro Schritt Trace-JSON-Zeilen für `models_pipeline.py` hinzu:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Eskalationsheuristik (Idee)
Wenn der Plan Schlüsselwörter wie "optimieren", "Sicherheit" enthält oder die Schrittlänge > 280 Zeichen beträgt → eskalieren Sie für diesen Schritt nur zu einem größeren Modell (z. B. `gpt-oss-20b`).

### Optionale Verbesserungen

| Bereich | Verbesserung | Wert | Hinweis |
|---------|--------------|------|---------|
| Caching | Wiederverwendung von Manager- + Client-Objekten | Niedrigere Latenz, weniger Overhead | Verwenden Sie `workshop_utils.get_client` |
| Nutzungsmetriken | Erfassen von Tokens & Latenz pro Schritt | Profilierung & Optimierung | Zeit für jeden weitergeleiteten Aufruf messen; in Trace-Liste speichern |
| Adaptive Weiterleitung | Vertrauens-/kostenbewusst | Bessere Qualitäts-Kosten-Abwägung | Bewertung hinzufügen: Wenn Prompt > N Zeichen oder Regex passt zur Domäne → eskalieren zu größerem Modell |
| Dynamisches Fähigkeitsregister | Katalog im laufenden Betrieb neu laden | Kein Neustart erforderlich | `catalog.json` zur Laufzeit laden; Dateizeitstempel überwachen |
| Fallback-Strategie | Robustheit bei Ausfällen | Höhere Verfügbarkeit | Primär versuchen → bei Ausnahme Fallback-Alias verwenden |
| Streaming-Pipeline | Frühzeitiges Feedback | UX-Verbesserung | Jeden Schritt streamen und endgültige Verfeinerungseingabe puffern |
| Vektor-Absichts-Einbettungen | Nuanciertere Weiterleitung | Höhere Absichtsgenauigkeit | Prompt einbetten, clustern & Schwerpunkt → Fähigkeit zuordnen |
| Trace-Export | Auditierbare Kette | Compliance/Reporting | JSON-Zeilen ausgeben: Schritt, Absicht, Modell, Latenz_ms, Tokens |
| Kosten-Simulation | Vorabschätzung für die Cloud | Budgetplanung | Fiktive Kosten/Token pro Modell zuweisen & pro Aufgabe aggregieren |
| Deterministischer Modus | Reproduzierbarkeit | Stabiles Benchmarking | Env: `temperature=0`, feste Schrittanzahl |

#### Beispiel für Trace-Struktur

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Adaptive Eskalations-Skizze

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Hot Reload des Modellkatalogs

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.