# Session 5 Sample: Multi-Agent Orchestration

This sample showcases a coordinator + specialists pattern using Foundry Local’s OpenAI-compatible endpoint.

## Run (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validate
```cmd
curl http://localhost:8000/v1/models
```

## Troubleshooting
- If VS Code marks `import specialists` as unresolved in `coordinator.py`, make sure to run it as a module and verify that the interpreter is set to `Module08/.venv`:
	- Run: `python -m samples.05.agents.coordinator`
	- Select interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## References
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents overview: https://learn.microsoft.com/azure/ai-services/agents/overview
- Function calling sample (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

