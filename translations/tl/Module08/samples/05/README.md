# Session 5 Sample: Multi-Agent Orchestration

Ang sample na ito ay nagpapakita ng pattern na coordinator + specialists gamit ang OpenAI-compatible endpoint ng Foundry Local.

## Patakbuhin (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Beripikahin
```cmd
curl http://localhost:8000/v1/models
```

## Pag-aayos ng Problema
- Kung ang VS Code ay nag-flag ng `import specialists` bilang hindi mahanap sa `coordinator.py`, siguraduhing patakbuhin ito bilang module at ang interpreter ay nakaturo sa `Module08/.venv`:
	- Patakbuhin: `python -m samples.05.agents.coordinator`
	- Piliin ang interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Mga Sanggunian
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents overview: https://learn.microsoft.com/azure/ai-services/agents/overview
- Function calling sample (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

