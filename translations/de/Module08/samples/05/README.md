# Sitzung 5 Beispiel: Multi-Agenten-Orchestrierung

Dieses Beispiel demonstriert ein Koordinator- + Spezialisten-Muster unter Verwendung des OpenAI-kompatiblen Endpunkts von Foundry Local.

## Ausführen (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validieren
```cmd
curl http://localhost:8000/v1/models
```

## Fehlerbehebung
- Falls VS Code `import specialists` in `coordinator.py` als nicht aufgelöst markiert, stellen Sie sicher, dass Sie das Modul ausführen und der Interpreter auf `Module08/.venv` zeigt:
	- Ausführen: `python -m samples.05.agents.coordinator`
	- Interpreter auswählen: `Module08/.venv/Scripts/python.exe` (Strg+Umschalt+P → Python: Interpreter auswählen)

## Referenzen
- Foundry Local (Lernen): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Übersicht Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Beispiel für Funktionsaufrufe (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

