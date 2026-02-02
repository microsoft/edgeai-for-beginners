# Ukázka 02: Integrace OpenAI SDK

Ukazuje pokročilou integraci s OpenAI Python SDK, podporující jak Microsoft Foundry Local, tak Azure OpenAI, včetně streamování odpovědí a správného zpracování chyb.

## Přehled

Tato ukázka demonstruje:
- Plynulé přepínání mezi Foundry Local a Azure OpenAI
- Streamování chatovacích odpovědí pro lepší uživatelský zážitek
- Správné použití FoundryLocalManager SDK
- Robustní zpracování chyb a záložní mechanismy
- Produkčně připravené vzory kódu

## Předpoklady

- **Foundry Local**: Nainstalováno a spuštěno (pro lokální inferenci)
- **Python**: Verze 3.8 nebo novější s OpenAI SDK
- **Azure OpenAI**: Platný endpoint a API klíč (pro cloudovou inferenci)

## Instalace

1. **Nastavení Python prostředí:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instalace závislostí:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Spuštění Foundry Local (pro lokální režim):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Scénáře použití

### Foundry Local (výchozí)

**Možnost 1: Použití FoundryLocalManager (doporučeno)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Možnost 2: Manuální konfigurace**
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

## Architektura kódu

### Vzor továrny klientů

Ukázka využívá vzor továrny pro vytvoření vhodných klientů:

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

### Streamování odpovědí

Ukázka demonstruje streamování pro generování odpovědí v reálném čase:

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

## Proměnné prostředí

### Konfigurace Foundry Local

| Proměnná | Popis | Výchozí | Povinné |
|----------|-------------|---------|----------|
| `MODEL` | Alias modelu k použití | `phi-4-mini` | Ne |
| `BASE_URL` | Endpoint Foundry Local | `http://localhost:8000` | Ne |
| `API_KEY` | API klíč (volitelné pro lokální použití) | `""` | Ne |

### Konfigurace Azure OpenAI

| Proměnná | Popis | Výchozí | Povinné |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint zdroje Azure OpenAI | - | Ano |
| `AZURE_OPENAI_API_KEY` | API klíč Azure OpenAI | - | Ano |
| `AZURE_OPENAI_API_VERSION` | Verze API | `2024-08-01-preview` | Ne |
| `MODEL` | Název nasazení Azure | `your-deployment-name` | Ano |

## Pokročilé funkce

### Automatické rozpoznání služby

Ukázka automaticky detekuje vhodnou službu na základě proměnných prostředí:

1. **Režim Azure**: Pokud jsou nastaveny `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_API_KEY`
2. **Režim Foundry SDK**: Pokud je dostupné Foundry Local SDK
3. **Manuální režim**: Záložní možnost manuální konfigurace

### Zpracování chyb

- Plynulý přechod z SDK na manuální konfiguraci
- Jasné chybové zprávy pro odstraňování problémů
- Správné zpracování výjimek pro síťové problémy
- Validace povinných proměnných prostředí

## Úvahy o výkonu

### Lokální vs cloudové kompromisy

**Výhody Foundry Local:**
- ✅ Žádné náklady na API
- ✅ Ochrana dat (data neopouští zařízení)
- ✅ Nízká latence pro podporované modely
- ✅ Funguje offline

**Výhody Azure OpenAI:**
- ✅ Přístup k nejnovějším velkým modelům
- ✅ Vyšší propustnost
- ✅ Žádné požadavky na lokální výpočetní výkon
- ✅ SLA na úrovni podnikových služeb

## Řešení problémů

### Běžné problémy

1. **Varování "Nelze použít Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Chyby autentizace Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model není dostupný:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Kontroly stavu

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Další kroky

- **Ukázka 03**: Objevování modelů a benchmarking
- **Ukázka 04**: Vytvoření Chainlit RAG aplikace
- **Ukázka 05**: Orchestrace více agentů
- **Ukázka 06**: Směrování modelů jako nástrojů

## Odkazy

- [Dokumentace Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Referenční příručka Foundry Local SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Dokumentace OpenAI Python SDK](https://github.com/openai/openai-python)
- [Průvodce streamováním odpovědí](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

