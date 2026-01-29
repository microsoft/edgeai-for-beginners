# Сесія 6: Моделі як інструменти

Цей приклад реалізує мінімальний маршрутизатор + реєстр інструментів, який вибирає модель на основі запиту користувача та викликає сумісну з OpenAI кінцеву точку Foundry Local.

## Файли
- `router.py`: простий реєстр і маршрутизація за евристикою; виявлення кінцевої точки + перевірка стану.

## Запуск (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Примітки
- Маршрутизатор використовує прості евристики ключових слів для вибору між інструментами `general`, `reasoning` і `code` та виводить `/v1/models` при запуску.
- Налаштування через змінні середовища:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## Посилання
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Інтеграція з SDK для інференсу: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, зверніть увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.