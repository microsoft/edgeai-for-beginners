<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T21:29:29+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "de"
}
-->
# Sitzung 3: Open-Source-Modelle in Foundry Local

## Zusammenfassung

Erfahren Sie, wie Sie Hugging Face und andere Open-Source-Modelle in Foundry Local integrieren können. Lernen Sie Strategien zur Modellauswahl, Workflows für Community-Beiträge, Methoden zum Leistungsvergleich und wie Sie Foundry mit benutzerdefinierten Modellregistrierungen erweitern können. Diese Sitzung orientiert sich an den wöchentlichen "Model Mondays"-Erkundungsthemen und befähigt Sie, Open-Source-Modelle lokal zu bewerten und zu operationalisieren, bevor Sie auf Azure skalieren.

## Lernziele

Am Ende werden Sie in der Lage sein:

- **Entdecken & Bewerten**: Kandidatenmodelle (mistral, gemma, qwen, deepseek) anhand von Qualitäts- und Ressourcenausgleich zu identifizieren.
- **Laden & Ausführen**: Mit dem Foundry Local CLI Community-Modelle herunterladen, zwischenspeichern und starten.
- **Benchmarking**: Konsistente Heuristiken für Latenz, Token-Durchsatz und Qualität anwenden.
- **Erweitern**: Einen benutzerdefinierten Modell-Wrapper registrieren oder anpassen, der SDK-kompatible Muster verwendet.
- **Vergleichen**: Strukturierte Vergleiche für SLM- vs. mittelgroße LLM-Auswahlentscheidungen erstellen.

## Voraussetzungen

- Sitzungen 1 & 2 abgeschlossen
- Python-Umgebung mit installiertem `foundry-local-sdk`
- Mindestens 15 GB freier Speicherplatz für mehrere Modell-Caches

### Schnellstart für plattformübergreifende Umgebungen

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

Beim Benchmarking von macOS gegen einen Windows-Host-Service einstellen:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo-Ablauf (30 Minuten)

### 1. Hugging Face-Modelle über CLI laden (8 Minuten)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Ausführen & Schnelle Überprüfung (5 Minuten)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Benchmark-Skript (8 Minuten)

Erstellen Sie `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Ausführen:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Leistung vergleichen (5 Minuten)

Diskutieren Sie Kompromisse: Ladezeit, Speicherbedarf (beobachten Sie Task-Manager / `nvidia-smi` / OS-Ressourcenmonitor), Ausgabequalität vs. Geschwindigkeit. Verwenden Sie das Python-Benchmark-Skript (Sitzung 3) für Latenz und Durchsatz; wiederholen Sie dies nach Aktivierung der GPU-Beschleunigung.

### 5. Starter-Projekt (4 Minuten)

Erstellen Sie einen Generator für Modellvergleichsberichte (Benchmark-Skript mit Markdown-Export erweitern).

## Starter-Projekt: Erweiterung von `03-huggingface-models`

Verbessern Sie das bestehende Beispiel durch:

1. Hinzufügen von Benchmark-Aggregation + CSV/Markdown-Ausgabe.
2. Implementierung einer einfachen qualitativen Bewertung (Prompt-Paar-Set + manuelle Annotationsdatei).
3. Einführung einer JSON-Konfiguration (`models.json`) für eine anpassbare Modellauswahl und Prompt-Set.

## Validierungs-Checkliste

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Alle Zielmodelle sollten erscheinen und auf eine Probe-Chat-Anfrage reagieren.

## Beispiel-Szenario & Workshop-Zuordnung

| Workshop-Skript | Szenario | Ziel | Prompt-/Datensatzquelle |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge-Plattform-Team wählt Standard-SLM für eingebetteten Summarizer | Latenz + p95 + Token/Sekunden-Vergleich zwischen Kandidatenmodellen erstellen | Inline-Variable `PROMPT` + Umgebungsvariable `BENCH_MODELS` Liste |

### Szenario-Erzählung

Das Produktentwicklungsteam muss ein Standard-Leichtgewicht-Summarizer-Modell für eine Offline-Meeting-Notiz-Funktion auswählen. Sie führen kontrollierte deterministische Benchmarks (temperature=0) über ein festes Prompt-Set (siehe Beispiel unten) durch und sammeln Latenz- und Durchsatzmetriken mit und ohne GPU-Beschleunigung.

### Beispiel-Prompt-Set JSON (erweiterbar)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Schleifen Sie jeden Prompt pro Modell, erfassen Sie die Latenz pro Prompt, um Verteilungsmetriken abzuleiten und Ausreißer zu erkennen.

## Modell-Auswahlrahmen

| Dimension | Metrik | Warum es wichtig ist |
|----------|--------|-----------------------|
| Latenz | Durchschnitt / p95 | Konsistenz der Benutzererfahrung |
| Durchsatz | Token/Sekunde | Skalierbarkeit für Batch- und Streaming |
| Speicher | Residentgröße | Gerätekompatibilität & Gleichzeitigkeit |
| Qualität | Rubrik-Prompts | Aufgaben-Eignung |
| Speicherbedarf | Cache-Größe | Verteilung & Updates |
| Lizenz | Nutzungsberechtigung | Kommerzielle Konformität |

## Erweiterung mit benutzerdefiniertem Modell

Hochrangiges Muster (Pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konsultieren Sie das offizielle Repository für sich entwickelnde Adapter-Schnittstellen:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Fehlerbehebung

| Problem | Ursache | Lösung |
|---------|---------|--------|
| OOM bei mistral-7b | Unzureichender RAM/GPU | Andere Modelle stoppen; kleinere Variante ausprobieren |
| Langsame erste Antwort | Kalter Start | Mit einem periodischen leichten Prompt warmhalten |
| Download bleibt hängen | Netzwerkinstabilität | Wiederholen; während Nebenzeiten vorab abrufen |

## Referenzen

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Sitzungsdauer**: 30 Minuten (+ optionaler Deep Dive)  
**Schwierigkeitsgrad**: Mittel

### Optionale Verbesserungen

| Verbesserung | Vorteil | Wie |
|--------------|---------|-----|
| Streaming-Ersttoken-Latenz | Misst wahrgenommene Reaktionsfähigkeit | Benchmark mit `BENCH_STREAM=1` ausführen (erweitertes Skript in `Workshop/samples/session03`) |
| Deterministischer Modus | Stabile Regression-Vergleiche | `temperature=0`, festes Prompt-Set, JSON-Ausgaben unter Versionskontrolle erfassen |
| Qualitäts-Rubrik-Bewertung | Fügt qualitative Dimension hinzu | `prompts.json` mit erwarteten Facetten pflegen; Bewertungen (1–5) manuell oder über sekundäres Modell annotieren |
| CSV-/Markdown-Export | Teilbarer Bericht | Skript erweitern, um `benchmark_report.md` mit Tabelle & Highlights zu schreiben |
| Modell-Fähigkeits-Tags | Hilft bei späterer automatisierter Weiterleitung | `models.json` mit `{alias: {capabilities:[], size_mb:..}}` pflegen |
| Cache-Warmup-Phase | Reduziert Bias durch kalten Start | Eine warme Runde vor der Timing-Schleife ausführen (bereits implementiert) |
| Perzentil-Genauigkeit | Robuste Latenz am Rand | Numpy-Perzentil verwenden (bereits im refaktorierten Skript enthalten) |
| Token-Kosten-Schätzung | Wirtschaftlicher Vergleich | Geschätzte Kosten = (Token/Sekunde * durchschnittliche Token pro Anfrage) * Energie-Heuristik |
| Automatisches Überspringen fehlgeschlagener Modelle | Resilienz bei Batch-Läufen | Jeden Benchmark in try/except einwickeln und Statusfeld markieren |

#### Minimaler Markdown-Export-Schnipsel

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Beispiel für deterministisches Prompt-Set

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Schleifen Sie die statische Liste anstelle von zufälligen Prompts für vergleichbare Metriken über Commits hinweg.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->