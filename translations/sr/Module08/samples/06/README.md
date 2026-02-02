# Сесија 6 Пример: Модели као алати

Овај пример имплементира минимални рутер + регистар алата који бира модел на основу корисничког упита и позива OpenAI-компатибилни крајњи тачку Foundry Local-а.

## Фајлови
- `router.py`: једноставан регистар и хеуристичко рутирање; откривање крајњих тачака + провера здравља.

## Покретање (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Напомене
- Рутер користи једноставне хеуристике засноване на кључним речима за избор између алата `general`, `reasoning` и `code` и исписује `/v1/models` при покретању.
- Конфигуришите преко променљивих окружења:
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

## Референце
- Foundry Local (Учите): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Интеграција са SDK-овима за инференцију: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.