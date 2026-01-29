# Primer 02: Integracija OpenAI SDK

Prikazuje napredno integracijo z OpenAI Python SDK, ki podpira tako Microsoft Foundry Local kot Azure OpenAI s pretočnimi odgovori in ustreznim ravnanjem z napakami.

## Pregled

Ta primer prikazuje:
- Enostavno preklapljanje med Foundry Local in Azure OpenAI
- Pretočne zaključke pogovorov za boljšo uporabniško izkušnjo
- Pravilno uporabo FoundryLocalManager SDK
- Zanesljivo ravnanje z napakami in mehanizmi za povratne ukrepe
- Vzorce kode, pripravljene za produkcijo

## Predpogoji

- **Foundry Local**: Nameščen in delujoč (za lokalno sklepanje)
- **Python**: Različica 3.8 ali novejša z OpenAI SDK
- **Azure OpenAI**: Veljaven končni točki in API ključ (za sklepanje v oblaku)

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

3. **Zaženite Foundry Local (za lokalni način):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Scenariji uporabe

### Foundry Local (privzeto)

**Možnost 1: Uporaba FoundryLocalManager (priporočeno)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Možnost 2: Ročna konfiguracija**
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

## Arhitektura kode

### Vzorec tovarniškega odjemalca

Primer uporablja vzorec tovarne za ustvarjanje ustreznih odjemalcev:

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

### Pretočni odgovori

Primer prikazuje pretočno generiranje odgovorov v realnem času:

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

## Spremenljivke okolja

### Konfiguracija Foundry Local

| Spremenljivka | Opis | Privzeto | Zahtevano |
|---------------|------|----------|-----------|
| `MODEL` | Alias modela za uporabo | `phi-4-mini` | Ne |
| `BASE_URL` | Končni točki Foundry Local | `http://localhost:8000` | Ne |
| `API_KEY` | API ključ (neobvezno za lokalno) | `""` | Ne |

### Konfiguracija Azure OpenAI

| Spremenljivka | Opis | Privzeto | Zahtevano |
|---------------|------|----------|-----------|
| `AZURE_OPENAI_ENDPOINT` | Končni točki Azure OpenAI | - | Da |
| `AZURE_OPENAI_API_KEY` | API ključ Azure OpenAI | - | Da |
| `AZURE_OPENAI_API_VERSION` | Različica API-ja | `2024-08-01-preview` | Ne |
| `MODEL` | Ime namestitve Azure | `your-deployment-name` | Da |

## Napredne funkcije

### Samodejno odkrivanje storitev

Primer samodejno zazna ustrezno storitev na podlagi spremenljivk okolja:

1. **Način Azure**: Če sta nastavljena `AZURE_OPENAI_ENDPOINT` in `AZURE_OPENAI_API_KEY`
2. **Način Foundry SDK**: Če je na voljo Foundry Local SDK
3. **Ročni način**: Povratna možnost za ročno konfiguracijo

### Ravnanje z napakami

- Eleganten prehod iz SDK na ročno konfiguracijo
- Jasna sporočila o napakah za odpravljanje težav
- Pravilno ravnanje z izjemami za težave z omrežjem
- Validacija zahtevanih spremenljivk okolja

## Premisleki o zmogljivosti

### Lokalno proti oblaku

**Prednosti Foundry Local:**
- ✅ Brez stroškov API-ja
- ✅ Zasebnost podatkov (podatki ne zapustijo naprave)
- ✅ Nizka zakasnitev za podprte modele
- ✅ Deluje brez povezave

**Prednosti Azure OpenAI:**
- ✅ Dostop do najnovejših velikih modelov
- ✅ Višja prepustnost
- ✅ Brez zahtev za lokalno računalniško moč
- ✅ SLA na ravni podjetja

## Odpravljanje težav

### Pogoste težave

1. **Opozorilo "Ni mogoče uporabiti Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Napake pri avtentikaciji Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model ni na voljo:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Preverjanje stanja

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Naslednji koraki

- **Primer 03**: Odkrivanje modelov in primerjalno testiranje
- **Primer 04**: Gradnja Chainlit RAG aplikacije
- **Primer 05**: Orkestracija več agentov
- **Primer 06**: Usmerjanje modelov kot orodij

## Reference

- [Dokumentacija Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Referenca Foundry Local SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Dokumentacija OpenAI Python SDK](https://github.com/openai/openai-python)
- [Vodnik za pretočne zaključke](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

