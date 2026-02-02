# Pavyzdys 02: OpenAI SDK integracija

Parodo pažangią integraciją su OpenAI Python SDK, palaikančią tiek Microsoft Foundry Local, tiek Azure OpenAI su srautiniu atsakymų pateikimu ir tinkamu klaidų tvarkymu.

## Apžvalga

Šiame pavyzdyje demonstruojama:
- Sklandus perjungimas tarp Foundry Local ir Azure OpenAI
- Srautinis pokalbių užbaigimas geresnei naudotojo patirčiai
- Tinkamas FoundryLocalManager SDK naudojimas
- Patikimi klaidų tvarkymo ir atsarginiai mechanizmai
- Kodavimo šablonai, tinkami naudoti gamyboje

## Reikalavimai

- **Foundry Local**: Įdiegta ir veikianti (vietinei analizei)
- **Python**: 3.8 ar naujesnė versija su OpenAI SDK
- **Azure OpenAI**: Galiojantis galinis taškas ir API raktas (debesų analizei)

## Įdiegimas

1. **Sukurkite Python aplinką:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Įdiekite priklausomybes:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Paleiskite Foundry Local (vietiniam režimui):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Naudojimo scenarijai

### Foundry Local (numatytasis)

**1 variantas: Naudojant FoundryLocalManager (rekomenduojama)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**2 variantas: Rankinis konfigūravimas**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```

### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```

## Kodo architektūra

### Kliento gamyklos šablonas

Pavyzdyje naudojamas gamyklos šablonas tinkamiems klientams sukurti:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```

### Srautinis atsakymų pateikimas

Pavyzdyje demonstruojamas srautinis atsakymų generavimas realiuoju laiku:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## Aplinkos kintamieji

### Foundry Local konfigūracija

| Kintamasis | Aprašymas | Numatytoji reikšmė | Privaloma |
|------------|-----------|--------------------|-----------|
| `MODEL` | Naudojamas modelio aliasas | `phi-4-mini` | Ne |
| `BASE_URL` | Foundry Local galinis taškas | `http://localhost:8000` | Ne |
| `API_KEY` | API raktas (neprivalomas vietiniam režimui) | `""` | Ne |

### Azure OpenAI konfigūracija

| Kintamasis | Aprašymas | Numatytoji reikšmė | Privaloma |
|------------|-----------|--------------------|-----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI resurso galinis taškas | - | Taip |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API raktas | - | Taip |
| `AZURE_OPENAI_API_VERSION` | API versija | `2024-08-01-preview` | Ne |
| `MODEL` | Azure diegimo pavadinimas | `your-deployment-name` | Taip |

## Pažangios funkcijos

### Automatinis paslaugų aptikimas

Pavyzdyje automatiškai aptinkama tinkama paslauga pagal aplinkos kintamuosius:

1. **Azure režimas**: Jei nustatyti `AZURE_OPENAI_ENDPOINT` ir `AZURE_OPENAI_API_KEY`
2. **Foundry SDK režimas**: Jei Foundry Local SDK yra prieinamas
3. **Rankinis režimas**: Atsarginis rankinis konfigūravimas

### Klaidų tvarkymas

- Sklandus perėjimas nuo SDK prie rankinio konfigūravimo
- Aiškūs klaidų pranešimai problemų sprendimui
- Tinkamas išimčių tvarkymas tinklo problemoms
- Privalomų aplinkos kintamųjų validacija

## Našumo aspektai

### Vietinio ir debesų režimų palyginimas

**Foundry Local privalumai:**
- ✅ Nėra API išlaidų
- ✅ Duomenų privatumas (duomenys neišeina iš įrenginio)
- ✅ Maža delsimo trukmė palaikomiems modeliams
- ✅ Veikia neprisijungus

**Azure OpenAI privalumai:**
- ✅ Prieiga prie naujausių didelių modelių
- ✅ Didesnis pralaidumas
- ✅ Nereikia vietinių skaičiavimo išteklių
- ✅ Įmonės lygio SLA

## Problemų sprendimas

### Dažnos problemos

1. **"Negalima naudoti Foundry SDK" įspėjimas:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure autentifikacijos klaidos:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modelis nepasiekiamas:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Sveikatos patikrinimai

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Kiti žingsniai

- **Pavyzdys 03**: Modelių aptikimas ir našumo testavimas
- **Pavyzdys 04**: Chainlit RAG aplikacijos kūrimas
- **Pavyzdys 05**: Daugiaveiksnių agentų koordinavimas
- **Pavyzdys 06**: Modelių kaip įrankių maršrutizavimas

## Nuorodos

- [Azure OpenAI dokumentacija](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK nuoroda](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK dokumentacija](https://github.com/openai/openai-python)
- [Srautinių užbaigimų vadovas](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

