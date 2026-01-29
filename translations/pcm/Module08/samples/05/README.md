# Session 5 Sample: Multi-Agent Orchestration

Dis sample dey show how coordinator + specialists pattern dey work wit Foundry Local wey dey compatible wit OpenAI endpoint.

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
- If VS Code dey show `import specialists` as unresolved for `coordinator.py`, make sure say you dey run am as module and the interpreter dey point to `Module08/.venv`:
	- Run: `python -m samples.05.agents.coordinator`
	- Select interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## References
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents overview: https://learn.microsoft.com/azure/ai-services/agents/overview
- Function calling sample (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say machine transleshion fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong meaning wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->