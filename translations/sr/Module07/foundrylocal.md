# Foundry Local на Windows и Mac

Овај водич вам помаже да инсталирате, покренете и интегришете Microsoft Foundry Local на Windows и Mac. Сви кораци и команде су проверени према Microsoft Learn документацији.

- Почетак: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Архитектура: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI референца: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Интеграција SDK-ова: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Компилација HF модела (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Локално vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Инсталација / Надоградња на Windows

- Инсталација:
```cmd
winget install Microsoft.FoundryLocal
```
- Надоградња:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Провера верзије:
```cmd
foundry --version
```
     
**Инсталација / Mac**

**MacOS**: 
Отворите терминал и покрените следећу команду:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Основе CLI (Три категорије)

- Модел:
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
- Кеш:
```cmd
foundry cache --help
foundry cache list
```

Напомене:
- Сервис пружа OpenAI-компатибилан REST API. Порт за приступ је динамички додељен; користите `foundry service status` да га откријете.
- Користите SDK-ове ради лакшег коришћења; они аутоматски откривају порт где је то подржано.

## 3) Откривање локалног ендпоинта (Динамички порт)

Foundry Local додељује динамички порт сваки пут када се сервис покрене:
```cmd
foundry service status
```
Користите пријављени `http://localhost:<PORT>` као ваш `base_url` са OpenAI-компатибилним путањама (на пример, `/v1/chat/completions`).

## 4) Брзи тест преко OpenAI Python SDK-а

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
Референце:
- Интеграција SDK-а: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Донесите свој модел (Компилација са Olive)

Ако вам је потребан модел који није у каталогу, компилирајте га у ONNX за Foundry Local користећи Olive.

Висок ниво процеса (погледајте документацију за кораке):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Документација:
- BYOM компилација: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Решавање проблема

- Провера статуса сервиса и логова:
```cmd
foundry service status
foundry service diag
```
- Брисање или премештање кеша:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Ажурирање на најновију прегледну верзију:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Повезано искуство за Windows програмере

- Избори за локалну и cloud AI на Windows-у, укључујући Foundry Local и Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit са Foundry Local (користите `foundry service status` да добијете URL за chat ендпоинт):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Следећи Windows програмер](./windowdeveloper.md)

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.