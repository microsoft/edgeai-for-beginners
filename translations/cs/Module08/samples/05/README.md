# Ukázka ze Session 5: Orchestrace více agentů

Tato ukázka demonstruje vzor koordinátora + specialistů pomocí OpenAI-kompatibilního endpointu Foundry Local.

## Spuštění (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Ověření
```cmd
curl http://localhost:8000/v1/models
```

## Řešení problémů
- Pokud VS Code označí `import specialists` jako nevyřešený v souboru `coordinator.py`, ujistěte se, že spouštíte jako modul a že interpret ukazuje na `Module08/.venv`:
	- Spusťte: `python -m samples.05.agents.coordinator`
	- Vyberte interpret: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Odkazy
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Přehled Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Ukázka volání funkcí (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

