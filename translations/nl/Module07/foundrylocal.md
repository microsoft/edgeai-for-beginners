# Foundry Local op Windows & Mac

Deze handleiding helpt je bij het installeren, uitvoeren en integreren van Microsoft Foundry Local op Windows en Mac. Alle stappen en commando's zijn gevalideerd aan de hand van Microsoft Learn-documentatie.

- Aan de slag: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architectuur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-referentie: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK's integreren: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF-modellen compileren (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: lokaal vs cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Installeren / Upgraden op Windows

- Installeren:
```cmd
winget install Microsoft.FoundryLocal
```
- Upgraden:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versie controleren:
```cmd
foundry --version
```
     
**Installeren / Mac**

**MacOS**: 
Open een terminal en voer het volgende commando uit:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI Basisprincipes (Drie Categorieën)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Service:
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

Opmerkingen:
- De service biedt een OpenAI-compatibele REST API. De poort van de endpoint wordt dynamisch toegewezen; gebruik `foundry service status` om deze te ontdekken.
- Gebruik de SDK's voor gemak; zij regelen automatisch de ontdekking van endpoints waar ondersteund.

## 3) Ontdek de lokale endpoint (Dynamische Poort)

Foundry Local wijst elke keer dat de service start een dynamische poort toe:
```cmd
foundry service status
```
Gebruik de gerapporteerde `http://localhost:<PORT>` als je `base_url` met OpenAI-compatibele paden (bijvoorbeeld `/v1/chat/completions`).

## 4) Snel testen via OpenAI Python SDK

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
Referenties:
- SDK-integratie: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Eigen model gebruiken (Compileren met Olive)

Als je een model nodig hebt dat niet in de catalogus staat, compileer het dan naar ONNX voor Foundry Local met Olive.

Hoofdlijnen (zie documentatie voor stappen):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Documentatie:
- BYOM compileren: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Problemen oplossen

- Controleer de status en logs van de service:
```cmd
foundry service status
foundry service diag
```
- Cache wissen of verplaatsen:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Updaten naar de nieuwste preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Gerelateerde Windows Developer Ervaring

- Windows lokaal vs cloud AI-keuzes, inclusief Foundry Local en Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit met Foundry Local (gebruik `foundry service status` om de chat-endpoint URL te verkrijgen):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Volgende Windows Developer](./windowdeveloper.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.