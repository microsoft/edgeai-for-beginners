# Foundry Local på Windows og Mac

Denne veiledningen hjelper deg med å installere, kjøre og integrere Microsoft Foundry Local på Windows og Mac. Alle trinn og kommandoer er validert mot Microsoft Learn-dokumentasjon.

- Kom i gang: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkitektur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-referanse: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrer SDK-er: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompiler HF-modeller (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokalt vs sky: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Installere / Oppgradere på Windows

- Installere:
```cmd
winget install Microsoft.FoundryLocal
```
- Oppgradere:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versjonskontroll:
```cmd
foundry --version
```
     
**Installere / Mac**

**MacOS**: 
Åpne et terminalvindu og kjør følgende kommando:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI Grunnleggende (Tre kategorier)

- Modell:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Tjeneste:
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

Notater:
- Tjenesten eksponerer et OpenAI-kompatibelt REST API. Endepunktets port tildeles dynamisk; bruk `foundry service status` for å finne den.
- Bruk SDK-ene for enkelhet; de håndterer automatisk oppdagelse av endepunkt der det er støttet.

## 3) Oppdag det lokale endepunktet (Dynamisk port)

Foundry Local tildeler en dynamisk port hver gang tjenesten starter:
```cmd
foundry service status
```
Bruk det rapporterte `http://localhost:<PORT>` som din `base_url` med OpenAI-kompatible stier (for eksempel, `/v1/chat/completions`).

## 4) Rask test via OpenAI Python SDK

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
Referanser:
- SDK-integrasjon: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Ta med din egen modell (Kompiler med Olive)

Hvis du trenger en modell som ikke finnes i katalogen, kompiler den til ONNX for Foundry Local ved hjelp av Olive.

Overordnet flyt (se dokumentasjon for trinn):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentasjon:
- BYOM-kompilering: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Feilsøking

- Sjekk tjenestestatus og logger:
```cmd
foundry service status
foundry service diag
```
- Tøm eller flytt cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Oppdater til siste forhåndsvisning:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Relatert Windows-utvikleropplevelse

- Valg mellom lokal og skybasert AI på Windows, inkludert Foundry Local og Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit med Foundry Local (bruk `foundry service status` for å få chat-endepunktets URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Neste Windows-utvikler](./windowdeveloper.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.