# Foundry Local på Windows och Mac

Den här guiden hjälper dig att installera, köra och integrera Microsoft Foundry Local på Windows och Mac. Alla steg och kommandon är validerade mot Microsoft Learn-dokumentation.

- Kom igång: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkitektur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-referens: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrera SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompilera HF-modeller (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokalt vs moln: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Installera / Uppgradera på Windows

- Installera:
```cmd
winget install Microsoft.FoundryLocal
```
- Uppgradera:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versionskontroll:
```cmd
foundry --version
```
     
**Installera / Mac**

**MacOS**: 
Öppna en terminal och kör följande kommando:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI-grunder (Tre kategorier)

- Modell:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Tjänst:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Anteckningar:
- Tjänsten exponerar ett OpenAI-kompatibelt REST API. Porten för endpointen tilldelas dynamiskt; använd `foundry service status` för att upptäcka den.
- Använd SDK:erna för bekvämlighet; de hanterar endpoint-upptäckt automatiskt där det stöds.

## 3) Upptäck den lokala endpointen (Dynamisk port)

Foundry Local tilldelar en dynamisk port varje gång tjänsten startas:
```cmd
foundry service status
```
Använd den rapporterade `http://localhost:<PORT>` som din `base_url` med OpenAI-kompatibla sökvägar (till exempel `/v1/chat/completions`).

## 4) Snabbtest via OpenAI Python SDK

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
Referenser:
- SDK-integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Ta med din egen modell (Kompilera med Olive)

Om du behöver en modell som inte finns i katalogen, kompilera den till ONNX för Foundry Local med Olive.

Hög nivå-flöde (se dokumentationen för steg):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentation:
- BYOM-kompilering: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Felsökning

- Kontrollera tjänstens status och loggar:
```cmd
foundry service status
foundry service diag
```
- Rensa eller flytta cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Uppdatera till senaste förhandsversion:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Relaterad Windows-utvecklarupplevelse

- Windows lokala vs molnbaserade AI-val, inklusive Foundry Local och Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit med Foundry Local (använd `foundry service status` för att få chat-endpointens URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Nästa Windows-utvecklare](./windowdeveloper.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.