# Сессия 6 Пример: Модели как инструменты

Этот пример реализует минимальный маршрутизатор + реестр инструментов, который выбирает модель на основе пользовательского запроса и вызывает совместимый с OpenAI конечный пункт Foundry Local.

## Файлы
- `router.py`: простой реестр и маршрутизация на основе эвристики; обнаружение конечного пункта + проверка работоспособности.

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

## Примечания
- Маршрутизатор использует простую эвристику ключевых слов для выбора между инструментами `general`, `reasoning` и `code` и выводит `/v1/models` при запуске.
- Настройка через переменные окружения:
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

## Ссылки
- Foundry Local (Учебный материал): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Интеграция с SDK для вывода: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.