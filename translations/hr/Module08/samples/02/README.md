# Primjer 02: Integracija OpenAI SDK-a

Prikazuje naprednu integraciju s OpenAI Python SDK-om, podržavajući i Microsoft Foundry Local i Azure OpenAI uz streaming odgovore i pravilno rukovanje greškama.

## Pregled

Ovaj primjer prikazuje:
- Jednostavno prebacivanje između Foundry Local i Azure OpenAI
- Streaming chat odgovora za bolje korisničko iskustvo
- Pravilnu upotrebu FoundryLocalManager SDK-a
- Robusne mehanizme za rukovanje greškama i rezervne opcije
- Kodne obrasce spremne za produkciju

## Preduvjeti

- **Foundry Local**: Instaliran i pokrenut (za lokalnu inferenciju)
- **Python**: Verzija 3.8 ili novija s OpenAI SDK-om
- **Azure OpenAI**: Valjani endpoint i API ključ (za inferenciju u oblaku)

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

3. **Pokrenite Foundry Local (za lokalni način rada):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Scenariji korištenja

### Foundry Local (Zadano)

**Opcija 1: Korištenje FoundryLocalManager-a (Preporučeno)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Opcija 2: Ručna konfiguracija**
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

## Arhitektura koda

### Klijentski tvornički obrazac

Primjer koristi tvornički obrazac za kreiranje odgovarajućih klijenata:

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

### Streaming odgovori

Primjer prikazuje streaming za generiranje odgovora u stvarnom vremenu:

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

## Varijable okruženja

### Konfiguracija Foundry Local

| Varijabla | Opis | Zadano | Obavezno |
|-----------|------|--------|----------|
| `MODEL` | Alias modela koji se koristi | `phi-4-mini` | Ne |
| `BASE_URL` | Endpoint Foundry Local | `http://localhost:8000` | Ne |
| `API_KEY` | API ključ (opcionalno za lokalno) | `""` | Ne |

### Konfiguracija Azure OpenAI

| Varijabla | Opis | Zadano | Obavezno |
|-----------|------|--------|----------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint resursa Azure OpenAI | - | Da |
| `AZURE_OPENAI_API_KEY` | API ključ za Azure OpenAI | - | Da |
| `AZURE_OPENAI_API_VERSION` | Verzija API-ja | `2024-08-01-preview` | Ne |
| `MODEL` | Naziv implementacije na Azureu | `your-deployment-name` | Da |

## Napredne značajke

### Automatsko otkrivanje usluge

Primjer automatski otkriva odgovarajuću uslugu na temelju varijabli okruženja:

1. **Azure način rada**: Ako su postavljeni `AZURE_OPENAI_ENDPOINT` i `AZURE_OPENAI_API_KEY`
2. **Foundry SDK način rada**: Ako je Foundry Local SDK dostupan
3. **Ručni način rada**: Rezervna opcija za ručnu konfiguraciju

### Rukovanje greškama

- Graciozan prelazak s SDK-a na ručnu konfiguraciju
- Jasne poruke o greškama za otklanjanje problema
- Pravilno rukovanje iznimkama za mrežne probleme
- Validacija obaveznih varijabli okruženja

## Razmatranja o performansama

### Lokalno vs Oblak

**Prednosti Foundry Local:**
- ✅ Nema troškova API-ja
- ✅ Privatnost podataka (podaci ne napuštaju uređaj)
- ✅ Niska latencija za podržane modele
- ✅ Radi offline

**Prednosti Azure OpenAI:**
- ✅ Pristup najnovijim velikim modelima
- ✅ Veći kapacitet obrade
- ✅ Nema zahtjeva za lokalnim računalnim resursima
- ✅ SLA na razini poduzeća

## Otklanjanje problema

### Uobičajeni problemi

1. **Upozorenje "Nije moguće koristiti Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Pogreške autentifikacije na Azureu:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model nije dostupan:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Provjere zdravlja

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Sljedeći koraci

- **Primjer 03**: Otkrivanje modela i benchmarking
- **Primjer 04**: Izrada Chainlit RAG aplikacije
- **Primjer 05**: Orkestracija više agenata
- **Primjer 06**: Usmjeravanje modela kao alata

## Reference

- [Azure OpenAI Dokumentacija](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Referenca](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Dokumentacija](https://github.com/openai/openai-python)
- [Vodič za streaming odgovore](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

