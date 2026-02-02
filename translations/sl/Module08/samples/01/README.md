# Primer 01: Hitri klepet prek OpenAI SDK

Preprost primer klepeta, ki prikazuje uporabo OpenAI SDK z Microsoft Foundry Local za lokalno AI inferenco.

## Pregled

Ta primer prikazuje, kako:
- Uporabiti OpenAI Python SDK z Foundry Local
- Upravljati konfiguracije za Azure OpenAI in lokalni Foundry
- Implementirati ustrezno obravnavo napak in strategije za preklop
- Uporabiti FoundryLocalManager za upravljanje storitev

## Predpogoji

- **Foundry Local**: Nameščen in dostopen v PATH
- **Python**: Različica 3.8 ali novejša
- **Model**: Model naložen v Foundry Local (npr. `phi-4-mini`)

## Namestitev

1. **Nastavite Python okolje:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Namestite odvisnosti:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Zaženite storitev Foundry Local in naložite model:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Uporaba

### Foundry Local (Privzeto)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## Značilnosti kode

### Integracija FoundryLocalManager

Primer uporablja uradni Foundry Local SDK za ustrezno upravljanje storitev:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### Obravnava napak

Zanesljiva obravnava napak z možnostjo preklopa na ročno konfiguracijo:
- Samodejno odkrivanje storitev
- Postopno zmanjševanje funkcionalnosti, če SDK ni na voljo
- Jasna sporočila o napakah za odpravljanje težav

## Okoljske spremenljivke

| Spremenljivka | Opis | Privzeto | Zahtevano |
|---------------|------|----------|-----------|
| `MODEL` | Alias ali ime modela | `phi-4-mini` | Ne |
| `BASE_URL` | Osnovni URL za Foundry Local | `http://localhost:8000` | Ne |
| `API_KEY` | API ključ (običajno ni potreben za lokalno uporabo) | `""` | Ne |
| `AZURE_OPENAI_ENDPOINT` | Končna točka za Azure OpenAI | - | Za Azure |
| `AZURE_OPENAI_API_KEY` | API ključ za Azure OpenAI | - | Za Azure |
| `AZURE_OPENAI_API_VERSION` | Različica Azure API | `2024-08-01-preview` | Ne |

## Odpravljanje težav

### Pogoste težave

1. **Opozorilo "Ni mogoče uporabiti Foundry SDK":**
   - Namestite foundry-local-sdk: `pip install foundry-local-sdk`
   - Ali nastavite okoljske spremenljivke za ročno konfiguracijo

2. **Povezava zavrnjena:**
   - Preverite, ali Foundry Local deluje: `foundry service status`
   - Preverite, ali je model naložen: `foundry service ps`

3. **Model ni najden:**
   - Prikažite razpoložljive modele: `foundry model list`
   - Naložite model: `foundry model run phi-4-mini`

### Preverjanje

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Reference

- [Dokumentacija Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Referenca za OpenAI-kompatibilni API](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

