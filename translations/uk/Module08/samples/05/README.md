# Сесія 5: Зразок оркестрації багатьох агентів

Цей зразок демонструє шаблон координатора + спеціалістів, використовуючи сумісну з OpenAI кінцеву точку Foundry Local.

## Запуск (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Перевірка
```cmd
curl http://localhost:8000/v1/models
```

## Вирішення проблем
- Якщо VS Code позначає `import specialists` як нерозпізнаний у файлі `coordinator.py`, переконайтеся, що ви запускаєте як модуль і інтерпретатор вказує на `Module08/.venv`:
	- Запустіть: `python -m samples.05.agents.coordinator`
	- Виберіть інтерпретатор: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Посилання
- Foundry Local (Навчання): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Огляд агентів Azure AI: https://learn.microsoft.com/azure/ai-services/agents/overview
- Зразок виклику функцій (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

