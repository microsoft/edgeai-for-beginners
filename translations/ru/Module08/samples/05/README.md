# Сессия 5 Пример: Оркестрация нескольких агентов

Этот пример демонстрирует шаблон координатора + специалистов с использованием совместимого с OpenAI конечного пункта Foundry Local.

## Запуск (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Проверка
```cmd
curl http://localhost:8000/v1/models
```

## Устранение неполадок
- Если VS Code отмечает `import specialists` как неразрешенный в `coordinator.py`, убедитесь, что вы запускаете как модуль, а интерпретатор указывает на `Module08/.venv`:
	- Запуск: `python -m samples.05.agents.coordinator`
	- Выбор интерпретатора: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Ссылки
- Foundry Local (Учебные материалы): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Обзор Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Пример вызова функций (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

