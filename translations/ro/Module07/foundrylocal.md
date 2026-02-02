# Foundry Local pe Windows și Mac

Acest ghid te ajută să instalezi, rulezi și integrezi Microsoft Foundry Local pe Windows și Mac. Toți pașii și comenzile sunt validate conform documentației Microsoft Learn.

- Începe: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arhitectură: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referință CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrare SDK-uri: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Compilează modele HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Instalare / Upgrade pe Windows

- Instalare:
```cmd
winget install Microsoft.FoundryLocal
```
- Upgrade:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Verificare versiune:
```cmd
foundry --version
```
     
**Instalare / Mac**

**MacOS**: 
Deschide un terminal și rulează următoarea comandă:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Bazele CLI (Trei Categorii)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Serviciu:
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

Note:
- Serviciul expune o API REST compatibilă cu OpenAI. Portul endpoint-ului este alocat dinamic; folosește `foundry service status` pentru a-l descoperi.
- Folosește SDK-urile pentru comoditate; acestea gestionează automat descoperirea endpoint-ului acolo unde este suportat.

## 3) Descoperă Endpoint-ul Local (Port Dinamic)

Foundry Local alocă un port dinamic de fiecare dată când serviciul pornește:
```cmd
foundry service status
```
Folosește `http://localhost:<PORT>` raportat ca `base_url` cu căi compatibile OpenAI (de exemplu, `/v1/chat/completions`).

## 4) Test Rapid prin SDK-ul Python OpenAI

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
Referințe:
- Integrare SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Adu Propriul Model (Compilează cu Olive)

Dacă ai nevoie de un model care nu este în catalog, compilează-l în ONNX pentru Foundry Local folosind Olive.

Flux de nivel înalt (vezi documentația pentru pași):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Documentație:
- Compilare BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Depanare

- Verifică starea serviciului și jurnalele:
```cmd
foundry service status
foundry service diag
```
- Șterge sau mută cache-ul:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Actualizează la cea mai recentă versiune preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Experiența Dezvoltatorului Windows Asociată

- Alegeri AI local vs cloud pe Windows, inclusiv Foundry Local și Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- Toolkit AI VS Code cu Foundry Local (folosește `foundry service status` pentru a obține URL-ul endpoint-ului de chat):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Următorul Dezvoltator Windows](./windowdeveloper.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.