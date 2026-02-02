# Sessão 5 Exemplo: Orquestração Multi-Agente

Este exemplo demonstra um padrão de coordenador + especialistas utilizando o endpoint compatível com OpenAI do Foundry Local.

## Executar (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validar
```cmd
curl http://localhost:8000/v1/models
```

## Resolução de Problemas
- Se o VS Code indicar que `import specialists` não está resolvido em `coordinator.py`, certifique-se de que está a executar como um módulo e que o interpretador aponta para `Module08/.venv`:
	- Executar: `python -m samples.05.agents.coordinator`
	- Selecionar interpretador: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referências
- Foundry Local (Aprender): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Visão geral dos Agentes Azure AI: https://learn.microsoft.com/azure/ai-services/agents/overview
- Exemplo de chamada de função (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

