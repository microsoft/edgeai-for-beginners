# Foundry Local Windowsil ja Macil

See juhend aitab teil installida, käivitada ja integreerida Microsoft Foundry Locali Windowsil ja Macil. Kõik sammud ja käsud on valideeritud Microsoft Learn dokumentide alusel.

- Alustamine: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arhitektuur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI viide: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK-de integreerimine: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF mudelite kompileerimine (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: kohalik vs pilv: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Installimine / uuendamine Windowsil

- Installimine:
```cmd
winget install Microsoft.FoundryLocal
```
- Uuendamine:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versiooni kontroll:
```cmd
foundry --version
```
     
**Installimine / Mac**

**MacOS**: 
Avage terminal ja käivitage järgmine käsk:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI põhialused (kolm kategooriat)

- Mudel:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Teenus:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Vahemälu:
```cmd
foundry cache --help
foundry cache list
```

Märkused:
- Teenus pakub OpenAI-ga ühilduvat REST API-d. Lõpp-punkti port määratakse dünaamiliselt; kasutage `foundry service status`, et seda avastada.
- Kasutage SDK-sid mugavuse huvides; need avastavad lõpp-punkti automaatselt, kui see on toetatud.

## 3) Kohaliku lõpp-punkti avastamine (dünaamiline port)

Foundry Local määrab iga teenuse käivitamise korral dünaamilise pordi:
```cmd
foundry service status
```
Kasutage teatatud `http://localhost:<PORT>` oma `base_url`-ina koos OpenAI-ga ühilduvate radadega (näiteks `/v1/chat/completions`).

## 4) Kiirtest OpenAI Python SDK kaudu

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
Viited:
- SDK integreerimine: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Oma mudeli kasutamine (kompileerimine Olive'iga)

Kui vajate kataloogis mitteolevat mudelit, kompileerige see ONNX-iks Foundry Locali jaoks, kasutades Olive'i.

Kõrgetasemeline voog (vaadake dokumente sammude kohta):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumendid:
- BYOM kompileerimine: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Tõrkeotsing

- Kontrollige teenuse olekut ja logisid:
```cmd
foundry service status
foundry service diag
```
- Tühjendage või liigutage vahemälu:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Uuendage uusimale eelvaatele:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Seotud Windowsi arendajakogemus

- Windowsi kohalik vs pilve AI valikud, sealhulgas Foundry Local ja Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI tööriistakomplekt Foundry Localiga (kasutage `foundry service status`, et saada vestluse lõpp-punkti URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Järgmine Windowsi arendaja](./windowdeveloper.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.