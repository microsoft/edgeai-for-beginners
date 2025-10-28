<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:13:12+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "de"
}
-->
# Sitzung 1: Einstieg in Foundry Local

## Zusammenfassung

Beginnen Sie Ihre Reise mit Foundry Local, indem Sie es unter Windows 11 installieren und konfigurieren. Lernen Sie, wie Sie die CLI einrichten, Hardware-Beschleunigung aktivieren und Modelle für schnelle lokale Inferenz zwischenspeichern. Diese praktische Sitzung zeigt, wie Modelle wie Phi, Qwen, DeepSeek und GPT-OSS-20B mit reproduzierbaren CLI-Befehlen ausgeführt werden.

## Lernziele

Am Ende dieser Sitzung werden Sie:

- **Installieren und Konfigurieren**: Foundry Local unter Windows 11 mit optimalen Leistungseinstellungen einrichten
- **CLI-Operationen meistern**: Foundry Local CLI für Modellverwaltung und -bereitstellung nutzen
- **Hardware-Beschleunigung aktivieren**: GPU-Beschleunigung mit ONNXRuntime oder WebGPU konfigurieren
- **Mehrere Modelle bereitstellen**: Modelle wie phi-4, GPT-OSS-20B, Qwen und DeepSeek lokal ausführen
- **Ihre erste App erstellen**: Bestehende Beispiele anpassen, um das Foundry Local Python SDK zu verwenden

# Modell testen (nicht-interaktive Einzelaufforderung)
foundry model run phi-4-mini --prompt "Hallo, stell dich vor"

- Windows 11 (22H2 oder später)
# Verfügbare Katalogmodelle auflisten (geladene Modelle erscheinen nach dem Ausführen)
foundry model list
## HINWEIS: Es gibt derzeit kein dediziertes `--running`-Flag; um zu sehen, welche geladen sind, starten Sie einen Chat oder prüfen Sie die Servicelogs.
- Python 3.10+ installiert
- Visual Studio Code mit Python-Erweiterung
- Administratorrechte für die Installation

### (Optional) Umgebungsvariablen

Erstellen Sie eine `.env`-Datei (oder setzen Sie sie in der Shell), um Skripte portabel zu machen:
# Antworten vergleichen (nicht-interaktiv)
foundry model run gpt-oss-20b --prompt "Erkläre Edge AI in einfachen Worten"
| Variable | Zweck | Beispiel |
|----------|-------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Bevorzugter Modellalias (Katalog wählt automatisch die beste Variante aus) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Endpunkt überschreiben (ansonsten automatisch vom Manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Streaming-Demo aktivieren | `true` |

> Wenn `FOUNDRY_LOCAL_ENDPOINT=auto` (oder nicht gesetzt) ist, wird es vom SDK-Manager abgeleitet.

## Demo-Ablauf (30 Minuten)

### 1. Foundry Local installieren und CLI-Einrichtung überprüfen (10 Minuten)

# Zwischengespeicherte Modelle auflisten
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Vorschau / falls unterstützt)**

Falls ein natives macOS-Paket bereitgestellt wird (offizielle Dokumentation für die neuesten Informationen prüfen):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Falls native macOS-Binärdateien noch nicht verfügbar sind, können Sie dennoch: 
1. Eine Windows 11 ARM/Intel VM (Parallels / UTM) verwenden und die Windows-Schritte befolgen. 
2. Modelle über Container ausführen (falls Container-Image veröffentlicht) und `FOUNDRY_LOCAL_ENDPOINT` auf den freigegebenen Port setzen. 

**Python-Virtual-Environment erstellen (plattformübergreifend)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Pip aktualisieren und Kernabhängigkeiten installieren:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Schritt 1.2: Installation überprüfen

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Schritt 1.3: Umgebung konfigurieren

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK-Bootstrapping (empfohlen)

Anstatt den Service manuell zu starten und Modelle auszuführen, kann das **Foundry Local Python SDK** alles automatisch starten:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Falls Sie die Kontrolle bevorzugen, können Sie weiterhin die CLI + OpenAI-Client wie später gezeigt verwenden.

### 2. Modelle lokal über CLI ausführen (10 Minuten)

#### Schritt 3.1: Phi-4-Modell bereitstellen

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Schritt 3.2: GPT-OSS-20B bereitstellen

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Schritt 3.3: Zusätzliche Modelle laden

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Starter-Projekt: 01-run-phi für Foundry Local anpassen (5 Minuten)

#### Schritt 4.1: Basis-Chat-Anwendung erstellen

Erstellen Sie `samples/01-foundry-quickstart/chat_quickstart.py` (aktualisiert zur Nutzung des Managers, falls verfügbar):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Schritt 4.2: Anwendung testen

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Wichtige behandelte Konzepte

### 1. Foundry Local Architektur

- **Lokale Inferenz-Engine**: Führt Modelle vollständig auf Ihrem Gerät aus
- **OpenAI SDK-Kompatibilität**: Nahtlose Integration mit bestehendem OpenAI-Code
- **Modellverwaltung**: Modelle effizient herunterladen, zwischenspeichern und ausführen
- **Hardware-Optimierung**: Nutzung von GPU-, NPU- und CPU-Beschleunigung

### 2. CLI-Befehlsreferenz

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK-Integration

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Häufige Probleme beheben

### Problem 1: "Foundry-Befehl nicht gefunden"

**Lösung:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problem 2: "Modell konnte nicht geladen werden"

**Lösung:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problem 3: "Verbindung zu localhost:5273 verweigert"

**Lösung:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tipps zur Leistungsoptimierung

### 1. Modell-Auswahlstrategie

- **Phi-4-mini**: Am besten für allgemeine Aufgaben, geringer Speicherbedarf
- **Qwen2.5-0.5b**: Schnellste Inferenz, minimale Ressourcen
- **GPT-OSS-20B**: Höchste Qualität, benötigt mehr Ressourcen
- **DeepSeek-Coder**: Optimiert für Programmieraufgaben

### 2. Hardware-Optimierung

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Leistung überwachen

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Optionale Verbesserungen

| Verbesserung | Was | Wie |
|--------------|-----|-----|
| Gemeinsame Utilities | Duplizierte Client-/Bootstrapping-Logik entfernen | Verwenden Sie `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Token-Nutzungsanzeige | Kosten-/Effizienzdenken früh vermitteln | Setzen Sie `SHOW_USAGE=1`, um Prompt-/Completion-/Gesamttoken anzuzeigen |
| Deterministische Vergleiche | Stabile Benchmarking- und Regressionstests | Verwenden Sie `temperature=0`, `top_p=1`, konsistenten Prompt-Text |
| Erste-Token-Latenz | Wahrgenommene Reaktionszeit messen | Benchmark-Skript mit Streaming anpassen (`BENCH_STREAM=1`) |
| Wiederholungen bei vorübergehenden Fehlern | Resiliente Demos bei Kaltstart | `RETRY_ON_FAIL=1` (Standard) & `RETRY_BACKOFF` anpassen |
| Smoke-Tests | Schnelle Überprüfung wichtiger Abläufe | Führen Sie `python Workshop/tests/smoke.py` vor einem Workshop aus |
| Modell-Alias-Profile | Schnelles Wechseln zwischen Modellsätzen auf verschiedenen Maschinen | `.env` mit `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` pflegen |
| Caching-Effizienz | Wiederholte Warmups bei mehreren Beispielausführungen vermeiden | Utilities-Cache-Manager; Wiederverwendung über Skripte/Notebooks hinweg |
| Warmup beim ersten Lauf | Reduzierung von p95-Latenzspitzen | Kleinen Prompt nach Erstellung von `FoundryLocalManager` ausführen |

Beispiel für deterministische Warmup-Basis (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Sie sollten ähnliche Ausgaben und identische Token-Zahlen beim zweiten Lauf sehen, was die Determinismus bestätigt.

## Nächste Schritte

Nach Abschluss dieser Sitzung:

1. **Session 2 erkunden**: KI-Lösungen mit Azure AI Foundry RAG erstellen
2. **Andere Modelle ausprobieren**: Mit Qwen, DeepSeek und anderen Modellfamilien experimentieren
3. **Leistung optimieren**: Einstellungen für Ihre spezifische Hardware feinabstimmen
4. **Eigene Anwendungen erstellen**: Das Foundry Local SDK in Ihren eigenen Projekten verwenden

## Zusätzliche Ressourcen

### Dokumentation
- [Foundry Local Python SDK Referenz](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installationsanleitung](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modellkatalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Beispielcode
- [Modul08 Beispiel 01](./samples/01/README.md) - REST Chat Quickstart
- [Modul08 Beispiel 02](./samples/02/README.md) - OpenAI SDK Integration
- [Modul08 Beispiel 03](./samples/03/README.md) - Modellentdeckung & Benchmarking

### Community
- [Foundry Local GitHub Diskussionen](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sitzungsdauer**: 30 Minuten Praxis + 15 Minuten Q&A  
**Schwierigkeitsgrad**: Anfänger  
**Voraussetzungen**: Windows 11, Python 3.10+, Administratorzugriff

## Beispiel-Szenario & Workshop-Zuordnung

| Workshop-Skript / Notebook | Szenario | Ziel | Beispiel-Eingaben | Benötigtes Dataset |
|----------------------------|----------|------|-------------------|--------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Internes IT-Team bewertet On-Device-Inferenz für ein Datenschutzbewertungsportal | Lokale SLM-Antworten innerhalb von Sub-Sekunden-Latenz auf Standard-Prompts nachweisen | "Nennen Sie zwei Vorteile der lokalen Inferenz." | Keines (Einzelaufforderung) |
| Quickstart-Anpassungscodeblock | Entwickler migriert ein bestehendes OpenAI-Skript zu Foundry Local | Drop-in-Kompatibilität zeigen | "Nennen Sie zwei Vorteile der lokalen Inferenz." | Nur Inline-Prompt |

### Szenario-Erzählung
Das Sicherheits- und Compliance-Team muss validieren, ob sensible Prototypdaten lokal verarbeitet werden können. Sie führen das Bootstrap-Skript mit mehreren Prompts (Datenschutz, Latenz, Kosten) im deterministischen Modus `temperature=0` aus, um Basis-Ausgaben für spätere Vergleiche (Session 3 Benchmarking und Session 4 SLM vs LLM Kontrast) zu erfassen.

### Minimaler Prompt-Set JSON (optional)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Verwenden Sie diese Liste, um eine reproduzierbare Bewertungsrunde zu erstellen oder einen zukünftigen Regressionstest-Harness zu starten.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.