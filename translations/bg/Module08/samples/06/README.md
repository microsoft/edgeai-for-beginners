# Сесия 6 Пример: Модели като инструменти

Този пример реализира минимален рутер + регистър на инструменти, който избира модел въз основа на потребителския въпрос и извиква OpenAI-съвместимия крайна точка на Foundry Local.

## Файлове
- `router.py`: прост регистър и евристично маршрутизиране; откриване на крайна точка + проверка на състоянието.

## Стартиране (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Бележки
- Рутерът използва прости евристики на ключови думи, за да избере между инструменти `general`, `reasoning` и `code` и отпечатва `/v1/models` при стартиране.
- Конфигуриране чрез променливи на средата:
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

## Референции
- Foundry Local (Научете): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Интеграция с SDK за изводи: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.