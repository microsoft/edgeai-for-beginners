# Näidis 02: OpenAI SDK integreerimine

Näitab OpenAI Python SDK täiustatud integreerimist, toetades nii Microsoft Foundry Local kui ka Azure OpenAI teenuseid voogedastusega vastuste ja korrektse veakäsitlusega.

## Ülevaade

See näidis tutvustab:
- Sujuvat üleminekut Foundry Local ja Azure OpenAI vahel
- Voogedastusega vestluste lõpetamist parema kasutajakogemuse jaoks
- FoundryLocalManager SDK korrektset kasutamist
- Tugevat veakäsitlust ja varumehhanisme
- Tootmiskõlblikke koodimustreid

## Eeltingimused

- **Foundry Local**: Paigaldatud ja käivitatud (kohalikuks järeldamiseks)
- **Python**: Versioon 3.8 või uuem koos OpenAI SDK-ga
- **Azure OpenAI**: Kehtiv lõpp-punkt ja API võti (pilvepõhiseks järeldamiseks)

## Paigaldamine

1. **Seadista Python keskkond:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Paigalda sõltuvused:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Käivita Foundry Local (kohaliku režiimi jaoks):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Kasutusstsenaariumid

### Foundry Local (Vaikimisi)

**Valik 1: FoundryLocalManager kasutamine (soovitatav)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Valik 2: Käsitsi seadistamine**
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

## Koodi arhitektuur

### Kliendi tehase muster

Näidis kasutab tehase mustrit sobivate klientide loomiseks:

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

### Voogedastusega vastused

Näidis demonstreerib voogedastust reaalajas vastuste genereerimiseks:

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

## Keskkonnamuutujad

### Foundry Local konfiguratsioon

| Muutuja | Kirjeldus | Vaikimisi | Nõutav |
|---------|-----------|-----------|--------|
| `MODEL` | Kasutatava mudeli alias | `phi-4-mini` | Ei |
| `BASE_URL` | Foundry Local lõpp-punkt | `http://localhost:8000` | Ei |
| `API_KEY` | API võti (valikuline kohaliku jaoks) | `""` | Ei |

### Azure OpenAI konfiguratsioon

| Muutuja | Kirjeldus | Vaikimisi | Nõutav |
|---------|-----------|-----------|--------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI ressursi lõpp-punkt | - | Jah |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API võti | - | Jah |
| `AZURE_OPENAI_API_VERSION` | API versioon | `2024-08-01-preview` | Ei |
| `MODEL` | Azure juurutamise nimi | `your-deployment-name` | Jah |

## Täiustatud funktsioonid

### Automaatne teenuse avastamine

Näidis tuvastab automaatselt sobiva teenuse keskkonnamuutujate põhjal:

1. **Azure režiim**: Kui `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_API_KEY` on määratud
2. **Foundry SDK režiim**: Kui Foundry Local SDK on saadaval
3. **Käsitsi režiim**: Tagasipöördumine käsitsi konfiguratsioonile

### Veakäsitlus

- Sujuv üleminek SDK-lt käsitsi konfiguratsioonile
- Selged veateated tõrkeotsinguks
- Korralik erandite käsitlus võrguühenduse probleemide korral
- Nõutavate keskkonnamuutujate valideerimine

## Jõudluse kaalutlused

### Kohaliku ja pilve eelised

**Foundry Local eelised:**
- ✅ Puuduvad API kulud
- ✅ Andmete privaatsus (andmed ei lahku seadmest)
- ✅ Madal latentsus toetatud mudelite jaoks
- ✅ Töötab võrguühenduseta

**Azure OpenAI eelised:**
- ✅ Juurdepääs uusimatele suurtele mudelitele
- ✅ Kõrgem läbilaskevõime
- ✅ Puuduvad kohalikud arvutusnõuded
- ✅ Ettevõtte tasemel SLA

## Tõrkeotsing

### Levinud probleemid

1. **"Foundry SDK-d ei saanud kasutada" hoiatus:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure autentimisvead:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Mudel pole saadaval:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Tervisekontrollid

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Järgmised sammud

- **Näidis 03**: Mudelite avastamine ja võrdlusuuringud
- **Näidis 04**: Chainlit RAG rakenduse loomine
- **Näidis 05**: Mitme agendi orkestreerimine
- **Näidis 06**: Mudelite tööriistadena suunamine

## Viited

- [Azure OpenAI dokumentatsioon](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK viide](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK dokumentatsioon](https://github.com/openai/openai-python)
- [Voogedastusega lõpetuste juhend](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.