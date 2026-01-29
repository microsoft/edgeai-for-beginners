# Eksempel 02: OpenAI SDK-integrasjon

Demonstrerer avansert integrasjon med OpenAI Python SDK, som støtter både Microsoft Foundry Local og Azure OpenAI med strømmende svar og korrekt feilhåndtering.

## Oversikt

Dette eksempelet viser:
- Sømløs veksling mellom Foundry Local og Azure OpenAI
- Strømmende chat-svar for bedre brukeropplevelse
- Riktig bruk av FoundryLocalManager SDK
- Robust feilhåndtering og fallback-mekanismer
- Produksjonsklare kodeeksempler

## Forutsetninger

- **Foundry Local**: Installert og kjører (for lokal inferens)
- **Python**: Versjon 3.8 eller nyere med OpenAI SDK
- **Azure OpenAI**: Gyldig endepunkt og API-nøkkel (for skybasert inferens)

## Installasjon

1. **Sett opp Python-miljø:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Installer avhengigheter:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Start Foundry Local (for lokal modus):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Bruksscenarier

### Foundry Local (Standard)

**Alternativ 1: Bruke FoundryLocalManager (Anbefalt)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Alternativ 2: Manuell konfigurasjon**
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

## Kodearkitektur

### Klientfabrikkmønster

Eksempelet bruker et fabrikkmønster for å opprette passende klienter:

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

### Strømmende svar

Eksempelet demonstrerer strømming for sanntidsgenerering av svar:

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

## Miljøvariabler

### Foundry Local-konfigurasjon

| Variabel | Beskrivelse | Standard | Påkrevd |
|----------|-------------|----------|---------|
| `MODEL` | Modellalias som skal brukes | `phi-4-mini` | Nei |
| `BASE_URL` | Foundry Local-endepunkt | `http://localhost:8000` | Nei |
| `API_KEY` | API-nøkkel (valgfritt for lokal) | `""` | Nei |

### Azure OpenAI-konfigurasjon

| Variabel | Beskrivelse | Standard | Påkrevd |
|----------|-------------|----------|---------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI-ressursendepunkt | - | Ja |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-nøkkel | - | Ja |
| `AZURE_OPENAI_API_VERSION` | API-versjon | `2024-08-01-preview` | Nei |
| `MODEL` | Azure distribusjonsnavn | `your-deployment-name` | Ja |

## Avanserte funksjoner

### Automatisk tjenesteoppdagelse

Eksempelet oppdager automatisk riktig tjeneste basert på miljøvariabler:

1. **Azure-modus**: Hvis `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_API_KEY` er satt
2. **Foundry SDK-modus**: Hvis Foundry Local SDK er tilgjengelig
3. **Manuell modus**: Fallback til manuell konfigurasjon

### Feilhåndtering

- Smidig fallback fra SDK til manuell konfigurasjon
- Klare feilmeldinger for feilsøking
- Korrekt unntakshåndtering for nettverksproblemer
- Validering av nødvendige miljøvariabler

## Ytelseshensyn

### Lokal vs skybasert avveining

**Fordeler med Foundry Local:**
- ✅ Ingen API-kostnader
- ✅ Datapersonvern (ingen data forlater enheten)
- ✅ Lav ventetid for støttede modeller
- ✅ Fungerer offline

**Fordeler med Azure OpenAI:**
- ✅ Tilgang til de nyeste store modellene
- ✅ Høyere gjennomstrømning
- ✅ Ingen lokale maskinvarekrav
- ✅ SLA på bedriftsnivå

## Feilsøking

### Vanlige problemer

1. **Advarsel: "Kunne ikke bruke Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure-autentiseringsfeil:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modell ikke tilgjengelig:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Helsesjekker

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Neste steg

- **Eksempel 03**: Modelloppdagelse og benchmarking
- **Eksempel 04**: Bygge en Chainlit RAG-applikasjon
- **Eksempel 05**: Orkestrering av flere agenter
- **Eksempel 06**: Ruting av modeller som verktøy

## Referanser

- [Azure OpenAI-dokumentasjon](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK-referanse](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK-dokumentasjon](https://github.com/openai/openai-python)
- [Guide til strømmende svar](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

