# Sessie 5 Voorbeeld: Multi-Agent Orchestratie

Dit voorbeeld demonstreert een coördinator + specialisten patroon met behulp van Foundry Local's OpenAI-compatibele endpoint.

## Uitvoeren (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Valideren
```cmd
curl http://localhost:8000/v1/models
```

## Problemen oplossen
- Als VS Code `import specialists` als onopgelost markeert in `coordinator.py`, zorg er dan voor dat je het als een module uitvoert en dat de interpreter wijst naar `Module08/.venv`:
	- Uitvoeren: `python -m samples.05.agents.coordinator`
	- Interpreter selecteren: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referenties
- Foundry Local (Leer): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents overzicht: https://learn.microsoft.com/azure/ai-services/agents/overview
- Voorbeeld functieaanroep (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

