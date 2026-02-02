# Session 5 Eksempel: Multi-Agent Orkestrering

Dette eksempel demonstrerer et koordinator + specialister mønster ved brug af Foundry Locals OpenAI-kompatible endpoint.

## Kør (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Valider
```cmd
curl http://localhost:8000/v1/models
```

## Fejlfinding
- Hvis VS Code markerer `import specialists` som uløst i `coordinator.py`, skal du sikre dig, at du kører som et modul, og at interpreter peger på `Module08/.venv`:
	- Kør: `python -m samples.05.agents.coordinator`
	- Vælg interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referencer
- Foundry Local (Lær): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents oversigt: https://learn.microsoft.com/azure/ai-services/agents/overview
- Eksempel på funktionskald (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

