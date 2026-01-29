# Foundry Local på Windows & Mac

Denne guide hjælper dig med at installere, køre og integrere Microsoft Foundry Local på Windows og Mac. Alle trin og kommandoer er valideret mod Microsoft Learn-dokumentation.

- Kom godt i gang: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkitektur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrer SDK'er: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompiler HF-modeller (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokal vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Installation / Opgradering på Windows

- Installér:
```cmd
winget install Microsoft.FoundryLocal
```
- Opgrader:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versionskontrol:
```cmd
foundry --version
```
     
**Installation / Mac**

**MacOS**: 
Åbn en terminal og kør følgende kommando:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI-grundlæggende (Tre kategorier)

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

Bemærkninger:
- Servicen eksponerer en OpenAI-kompatibel REST API. Endepunktets port tildeles dynamisk; brug `foundry service status` for at finde den.
- Brug SDK'erne for nemhed; de håndterer automatisk opdagelse af endepunkter, hvor det er understøttet.

## 3) Find det lokale endepunkt (Dynamisk port)

Foundry Local tildeler en dynamisk port hver gang servicen starter:
```cmd
foundry service status
```
Brug den rapporterede `http://localhost:<PORT>` som din `base_url` med OpenAI-kompatible stier (for eksempel `/v1/chat/completions`).

## 4) Hurtig test via OpenAI Python SDK

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
Referencer:
- SDK-integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Medbring din egen model (Kompiler med Olive)

Hvis du har brug for en model, der ikke er i kataloget, kan du kompilere den til ONNX for Foundry Local ved hjælp af Olive.

Overordnet flow (se dokumentationen for trin):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentation:
- BYOM-kompilering: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Fejlfinding

- Tjek servicestatus og logfiler:
```cmd
foundry service status
foundry service diag
```
- Ryd eller flyt cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Opdater til den nyeste preview-version:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Relateret Windows-udvikleroplevelse

- Windows lokal vs cloud AI-valg, inklusive Foundry Local og Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit med Foundry Local (brug `foundry service status` for at få chat-endepunktets URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Next Windows Developer](./windowdeveloper.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.