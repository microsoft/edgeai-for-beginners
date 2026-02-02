# Foundry Local на Windows и Mac

Этот гид поможет вам установить, запустить и интегрировать Microsoft Foundry Local на Windows и Mac. Все шаги и команды проверены в соответствии с документацией Microsoft Learn.

- Начало работы: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Архитектура: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Справочник CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Интеграция SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Компиляция моделей HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: локально vs облако: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Установка / обновление на Windows

- Установка:
```cmd
winget install Microsoft.FoundryLocal
```
- Обновление:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Проверка версии:
```cmd
foundry --version
```
     
**Установка / Mac**

**MacOS**: 
Откройте терминал и выполните следующую команду:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Основы CLI (три категории)

- Модель:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Сервис:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Кэш:
```cmd
foundry cache --help
foundry cache list
```

Примечания:
- Сервис предоставляет REST API, совместимый с OpenAI. Порт конечной точки выделяется динамически; используйте `foundry service status`, чтобы узнать его.
- Для удобства используйте SDK; они автоматически определяют конечную точку там, где это поддерживается.

## 3) Определение локальной конечной точки (динамический порт)

Foundry Local назначает динамический порт каждый раз при запуске сервиса:
```cmd
foundry service status
```
Используйте указанный `http://localhost:<PORT>` как ваш `base_url` с путями, совместимыми с OpenAI (например, `/v1/chat/completions`).

## 4) Быстрая проверка через OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Ссылки:
- Интеграция SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Использование собственной модели (компиляция с Olive)

Если вам нужна модель, которой нет в каталоге, скомпилируйте её в ONNX для Foundry Local с помощью Olive.

Общий процесс (см. документацию для шагов):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Документация:
- Компиляция BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Устранение неполадок

- Проверка статуса сервиса и логов:
```cmd
foundry service status
foundry service diag
```
- Очистка или перемещение кэша:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Обновление до последней версии:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Связанный опыт разработчиков Windows

- Выбор между локальным и облачным AI для Windows, включая Foundry Local и Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- AI Toolkit для VS Code с Foundry Local (используйте `foundry service status`, чтобы получить URL конечной точки для чата):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Следующий разработчик Windows](./windowdeveloper.md)

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.