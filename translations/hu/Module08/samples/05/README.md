# 5. munkamenet minta: Többügynökös összehangolás

Ez a minta bemutatja egy koordinátor + szakértők mintát a Foundry Local OpenAI-kompatibilis végpontjának használatával.

## Futtatás (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Ellenőrzés
```cmd
curl http://localhost:8000/v1/models
```

## Hibakeresés
- Ha a VS Code az `import specialists`-et nem találja meg a `coordinator.py` fájlban, győződj meg róla, hogy modulként futtatod, és az interpreter a `Module08/.venv`-re mutat:
	- Futtatás: `python -m samples.05.agents.coordinator`
	- Interpreter kiválasztása: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Hivatkozások
- Foundry Local (Tanulás): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents áttekintés: https://learn.microsoft.com/azure/ai-services/agents/overview
- Funkcióhívás minta (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

