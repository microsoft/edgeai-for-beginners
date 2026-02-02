# Foundry Local Windows ir Mac

Šis vadovas padės jums įdiegti, paleisti ir integruoti Microsoft Foundry Local Windows ir Mac operacinėse sistemose. Visi žingsniai ir komandos patikrinti pagal Microsoft Learn dokumentaciją.

- Pradėti: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektūra: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI nuoroda: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK integracija: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF modelių kompiliavimas (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: vietinis vs debesų sprendimas: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Diegimas / Atnaujinimas Windows

- Diegimas:
```cmd
winget install Microsoft.FoundryLocal
```
- Atnaujinimas:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versijos patikrinimas:
```cmd
foundry --version
```
     
**Diegimas / Mac**

**MacOS**: 
Atidarykite terminalą ir vykdykite šią komandą:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI pagrindai (Trys kategorijos)

- Modelis:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Paslauga:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Talpykla:
```cmd
foundry cache --help
foundry cache list
```

Pastabos:
- Paslauga teikia OpenAI suderinamą REST API. Prievado numeris priskiriamas dinamiškai; naudokite `foundry service status`, kad jį sužinotumėte.
- Naudokite SDK patogumui; jie automatiškai aptinka galinius taškus, kur tai palaikoma.

## 3) Vietinio galinio taško aptikimas (dinaminis prievadas)

Foundry Local kiekvieną kartą paleidžiant paslaugą priskiria dinaminį prievadą:
```cmd
foundry service status
```
Naudokite nurodytą `http://localhost:<PORT>` kaip savo `base_url` su OpenAI suderinamais keliais (pvz., `/v1/chat/completions`).

## 4) Greitas testas per OpenAI Python SDK

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
Nuorodos:
- SDK integracija: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Naudokite savo modelį (kompiliavimas su Olive)

Jei jums reikia modelio, kurio nėra kataloge, kompiliuokite jį į ONNX formatą Foundry Local naudodami Olive.

Aukšto lygio procesas (žr. dokumentaciją dėl žingsnių):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentacija:
- BYOM kompiliavimas: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Trikčių šalinimas

- Patikrinkite paslaugos būseną ir žurnalus:
```cmd
foundry service status
foundry service diag
```
- Išvalykite arba perkelkite talpyklą:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Atnaujinkite į naujausią peržiūrą:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Susijusi Windows kūrėjų patirtis

- Windows vietinio ir debesų AI pasirinkimai, įskaitant Foundry Local ir Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI įrankių rinkinys su Foundry Local (naudokite `foundry service status`, kad gautumėte pokalbio galinio taško URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Next Windows Developer](./windowdeveloper.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.