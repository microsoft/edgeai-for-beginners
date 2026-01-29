# Primjer 01: Brzi razgovor putem OpenAI SDK-a

Jednostavan primjer razgovora koji pokazuje kako koristiti OpenAI SDK s Microsoft Foundry Local za lokalnu AI inferenciju.

## Pregled

Ovaj primjer pokazuje kako:
- Koristiti OpenAI Python SDK s Foundry Local
- Rukovati konfiguracijama za Azure OpenAI i lokalni Foundry
- Implementirati pravilno rukovanje greškama i strategije za povratne opcije
- Koristiti FoundryLocalManager za upravljanje uslugama

## Preduvjeti

- **Foundry Local**: Instaliran i dostupan na PATH-u
- **Python**: Verzija 3.8 ili novija
- **Model**: Model učitan u Foundry Local (npr. `phi-4-mini`)

## Instalacija

1. **Postavite Python okruženje:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instalirajte ovisnosti:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Pokrenite Foundry Local uslugu i učitajte model:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Upotreba

### Foundry Local (Zadano)

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

## Značajke koda

### Integracija s FoundryLocalManager

Primjer koristi službeni Foundry Local SDK za pravilno upravljanje uslugama:

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

### Rukovanje greškama

Robusno rukovanje greškama s povratnim opcijama za ručnu konfiguraciju:
- Automatsko otkrivanje usluga
- Postupno smanjenje funkcionalnosti ako SDK nije dostupan
- Jasne poruke o greškama za lakše otklanjanje problema

## Varijable okruženja

| Varijabla | Opis | Zadano | Obavezno |
|-----------|------|--------|----------|
| `MODEL` | Alias ili naziv modela | `phi-4-mini` | Ne |
| `BASE_URL` | Osnovni URL za Foundry Local | `http://localhost:8000` | Ne |
| `API_KEY` | API ključ (obično nije potreban za lokalno) | `""` | Ne |
| `AZURE_OPENAI_ENDPOINT` | Endpoint za Azure OpenAI | - | Za Azure |
| `AZURE_OPENAI_API_KEY` | API ključ za Azure OpenAI | - | Za Azure |
| `AZURE_OPENAI_API_VERSION` | Verzija Azure API-ja | `2024-08-01-preview` | Ne |

## Otklanjanje problema

### Uobičajeni problemi

1. **Upozorenje "Nije moguće koristiti Foundry SDK":**
   - Instalirajte foundry-local-sdk: `pip install foundry-local-sdk`
   - Ili postavite varijable okruženja za ručnu konfiguraciju

2. **Odbijena veza:**
   - Provjerite je li Foundry Local pokrenut: `foundry service status`
   - Provjerite je li model učitan: `foundry service ps`

3. **Model nije pronađen:**
   - Popis dostupnih modela: `foundry model list`
   - Učitajte model: `foundry model run phi-4-mini`

### Provjera

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Reference

- [Foundry Local Dokumentacija](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Referenca za OpenAI-kompatibilni API](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

