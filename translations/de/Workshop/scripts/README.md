# Workshop-Skripte

Dieses Verzeichnis enthält Automatisierungs- und Unterstützungsskripte, die verwendet werden, um die Qualität und Konsistenz der Workshop-Materialien zu gewährleisten.

## Inhalt

| Datei | Zweck |
|-------|-------|
| `lint_markdown_cli.py` | Überprüft Markdown-Codeblöcke auf veraltete Foundry Local CLI-Befehlsmuster. |
| `export_benchmark_markdown.py` | Führt Multi-Modell-Latenz-Benchmarks durch und erstellt Berichte in Markdown + JSON. |

## 1. Markdown CLI Pattern Linter

`lint_markdown_cli.py` durchsucht alle nicht übersetzten `.md`-Dateien nach nicht erlaubten Foundry Local CLI-Mustern **innerhalb von Codeblöcken** (``` ... ```). Informative Texte können weiterhin veraltete Befehle aus historischen Gründen erwähnen.

### Veraltete Muster (Innerhalb von Codeblöcken blockiert)

Der Linter blockiert veraltete CLI-Muster. Verwenden Sie stattdessen moderne Alternativen.

### Erforderliche Ersetzungen
| Veraltet | Stattdessen verwenden |
|----------|-----------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark-Skript + Systemtools (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Exit-Codes
| Code | Bedeutung |
|------|-----------|
| 0 | Keine Verstöße erkannt |
| 1 | Ein oder mehrere veraltete Muster gefunden |

### Lokale Ausführung
Vom Repository-Stammverzeichnis aus (empfohlen):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit-Hook (Optional)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Blockiert Commits, die veraltete Muster einführen.

### CI-Integration
Ein GitHub Action Workflow (`.github/workflows/markdown-cli-lint.yml`) führt den Linter bei jedem Push und Pull-Request zu den `main`- und `Reactor`-Branches aus. Fehlgeschlagene Jobs müssen vor dem Zusammenführen behoben werden.

### Hinzufügen neuer veralteter Muster
1. Öffnen Sie `lint_markdown_cli.py`.
2. Fügen Sie ein Tupel `(regex, suggestion)` zur Liste `DEPRECATED` hinzu. Verwenden Sie einen Raw-String und fügen Sie `\b` Wortgrenzen hinzu, wo erforderlich.
3. Führen Sie den Linter lokal aus, um die Erkennung zu überprüfen.
4. Committen und pushen Sie; die CI wird die neue Regel durchsetzen.

Beispiel für eine Ergänzung:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Erklärende Erwähnungen erlauben
Da nur Codeblöcke durchgesetzt werden, können Sie veraltete Befehle sicher in narrativen Texten beschreiben. Wenn Sie sie *unbedingt* in einem Codeblock zeigen müssen, verwenden Sie einen Block **ohne** dreifache Backticks (z. B. Einrückung oder Zitat) oder schreiben Sie sie in einer Pseudoform um.

### Bestimmte Dateien überspringen (Fortgeschritten)
Falls erforderlich, können Sie ältere Beispiele in einer separaten Datei außerhalb des Repos speichern oder während des Entwurfs mit einer anderen Erweiterung umbenennen. Übersetzte Kopien werden automatisch übersprungen (Pfade mit `translations`).

### Fehlerbehebung
| Problem | Ursache | Lösung |
|---------|---------|--------|
| Linter markiert eine von Ihnen aktualisierte Zeile | Regex zu allgemein | Muster mit zusätzlichen Wortgrenzen (`\b`) oder Ankern eingrenzen |
| CI schlägt fehl, aber lokal funktioniert es | Unterschiedliche Python-Version oder nicht übertragene Änderungen | Lokal erneut ausführen, sicherstellen, dass der Arbeitsbaum sauber ist, Python-Version des Workflows überprüfen (3.11) |
| Temporäres Umgehen erforderlich | Notfall-Hotfix | Fix sofort anwenden; erwägen Sie die Verwendung eines temporären Branches und eines Folge-PRs (vermeiden Sie das Hinzufügen von Umgehungsschaltern) |

### Begründung
Die Dokumentation auf die *aktuelle* stabile CLI-Oberfläche abzustimmen, verhindert Workshop-Probleme, vermeidet Verwirrung bei den Teilnehmern und zentralisiert die Leistungsbewertung durch gepflegte Python-Skripte anstelle von veralteten CLI-Unterbefehlen.

---
Wird als Teil der Workshop-Qualitäts-Toolchain gepflegt. Für Verbesserungen (z. B. automatische Vorschläge oder HTML-Berichtserstellung) öffnen Sie ein Issue oder reichen Sie einen PR ein.

## 2. Validierungsskript für Beispiele

`validate_samples.py` überprüft alle Python-Beispieldateien auf Syntax, Imports und Einhaltung von Best Practices.

### Verwendung
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### Was überprüft wird
- ✅ Python-Syntax-Gültigkeit
- ✅ Erforderliche Imports vorhanden
- ✅ Fehlerbehandlung implementiert (im ausführlichen Modus)
- ✅ Verwendung von Typ-Hinweisen (im ausführlichen Modus)
- ✅ Funktions-Dokumentationen (im ausführlichen Modus)
- ✅ SDK-Referenzlinks (im ausführlichen Modus)

### Umgebungsvariablen
- `SKIP_IMPORT_CHECK=1` - Überspringt die Import-Validierung
- `SKIP_SYNTAX_CHECK=1` - Überspringt die Syntax-Validierung

### Exit-Codes
- `0` - Alle Beispiele haben die Validierung bestanden
- `1` - Ein oder mehrere Beispiele sind durchgefallen

## 3. Test Runner für Beispiele

`test_samples.py` führt Smoke-Tests für alle Beispiele aus, um sicherzustellen, dass sie fehlerfrei ausgeführt werden.

### Verwendung
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### Voraussetzungen
- Foundry Local-Dienst läuft: `foundry service start`
- Modelle geladen: `foundry model run phi-4-mini`
- Abhängigkeiten installiert: `pip install -r requirements.txt`

### Was getestet wird
- ✅ Beispiel kann ohne Laufzeitfehler ausgeführt werden
- ✅ Erforderliche Ausgabe wird generiert
- ✅ Fehlerbehandlung bei Fehlern
- ✅ Leistung (Ausführungszeit)

### Umgebungsvariablen
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modell, das für Tests verwendet wird
- `TEST_TIMEOUT=30` - Timeout pro Beispiel in Sekunden

### Erwartete Fehler
Einige Tests können fehlschlagen, wenn optionale Abhängigkeiten nicht installiert sind (z. B. `ragas`, `sentence-transformers`). Installieren Sie diese mit:
```bash
pip install sentence-transformers ragas datasets
```

### Exit-Codes
- `0` - Alle Tests bestanden
- `1` - Ein oder mehrere Tests sind durchgefallen

## 4. Benchmark Markdown Exporter

Skript: `export_benchmark_markdown.py`

Generiert eine reproduzierbare Leistungstabelle für eine Reihe von Modellen.

### Verwendung
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Ausgaben
| Datei | Beschreibung |
|-------|--------------|
| `benchmark_report.md` | Markdown-Tabelle (Durchschnitt, p95, Tokens/Sekunde, optional erstes Token) |
| `benchmark_report.json` | Rohdaten-Metriken für Differenzierung & Historie |

### Optionen
| Flag | Beschreibung | Standard |
|------|--------------|----------|
| `--models` | Komma-separierte Modell-Aliase | (erforderlich) |
| `--prompt` | Prompt, der in jeder Runde verwendet wird | (erforderlich) |
| `--rounds` | Runden pro Modell | 3 |
| `--output` | Markdown-Ausgabedatei | `benchmark_report.md` |
| `--json` | JSON-Ausgabedatei | `benchmark_report.json` |
| `--fail-on-empty` | Nicht-Null-Exit, wenn alle Benchmarks fehlschlagen | aus |

Umgebungsvariable `BENCH_STREAM=1` fügt die Messung der Latenz des ersten Tokens hinzu.

### Hinweise
- Verwendet `workshop_utils` für konsistentes Modell-Bootstrap & Caching.
- Wenn aus einem anderen Arbeitsverzeichnis ausgeführt, versucht das Skript, Pfad-Alternativen zu finden, um `workshop_utils` zu lokalisieren.
- Für GPU-Vergleiche: einmal ausführen, Beschleunigung über CLI-Konfiguration aktivieren, erneut ausführen und die JSON vergleichen.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.