<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:00:19+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "de"
}
-->
# Podcast-Anwendung

Eine Konsolenanwendung zur Erstellung von Podcast-Skripten mithilfe von KI-Agenten.

## Verwendung

```bash
python podcast_app.py
```

## Arbeitsablauf

1. **Begrüßung** – Die Anwendung begrüßt den Benutzer
2. **Themen-Eingabe** – Benutzer gibt ein Thema für den Podcast an
3. **Suchagent** – Sucht relevante Informationen
4. **Skript-Generierungsagent** – Erstellt ein Podcast-Skript
5. **Überprüfung** – Benutzer überprüft und genehmigt/lehnen das Skript ab
6. **Speichern** – Genehmigtes Skript wird in `podcast.md` gespeichert

## Anforderungen

- Python 3.12+
- agent_framework
- Alle Abhängigkeiten aus 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, können automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten. Das Originaldokument in seiner Ausgangssprache gilt als maßgebliche Quelle. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->