# Sesión 5 Ejemplo: Orquestación Multi-Agente

Este ejemplo demuestra un patrón de coordinador + especialistas utilizando el endpoint compatible con OpenAI de Foundry Local.

## Ejecutar (cmd.exe)
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

## Solución de problemas
- Si VS Code marca `import specialists` como no resuelto en `coordinator.py`, asegúrate de ejecutarlo como un módulo y que el intérprete apunte a `Module08/.venv`:
	- Ejecutar: `python -m samples.05.agents.coordinator`
	- Seleccionar intérprete: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referencias
- Foundry Local (Aprender): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Descripción general de Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Ejemplo de llamada a funciones (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

