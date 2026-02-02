# Sessione 5 Esempio: Orchestrazione Multi-Agente

Questo esempio dimostra un modello di coordinatore + specialisti utilizzando l'endpoint compatibile con OpenAI di Foundry Local.

## Esegui (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Valida
```cmd
curl http://localhost:8000/v1/models
```

## Risoluzione dei problemi
- Se VS Code segnala `import specialists` come non risolto in `coordinator.py`, assicurati di eseguire come modulo e che l'interprete punti a `Module08/.venv`:
	- Esegui: `python -m samples.05.agents.coordinator`
	- Seleziona interprete: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Riferimenti
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Panoramica di Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Esempio di chiamata di funzione (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

