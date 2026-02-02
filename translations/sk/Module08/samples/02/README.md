# Ukážka 02: Integrácia OpenAI SDK

Ukazuje pokročilú integráciu s OpenAI Python SDK, podporujúcu Microsoft Foundry Local aj Azure OpenAI so streamovanými odpoveďami a správnym spracovaním chýb.

## Prehľad

Táto ukážka demonštruje:
- Plynulé prepínanie medzi Foundry Local a Azure OpenAI
- Streamovanie odpovedí pre lepší používateľský zážitok
- Správne použitie FoundryLocalManager SDK
- Robustné spracovanie chýb a záložné mechanizmy
- Produkčne pripravené vzory kódu

## Predpoklady

- **Foundry Local**: Nainštalovaný a spustený (pre lokálnu inferenciu)
- **Python**: Verzia 3.8 alebo novšia s OpenAI SDK
- **Azure OpenAI**: Platný endpoint a API kľúč (pre cloudovú inferenciu)

## Inštalácia

1. **Nastavte Python prostredie:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Nainštalujte závislosti:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Spustite Foundry Local (pre lokálny režim):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Scenáre použitia

### Foundry Local (predvolené)

**Možnosť 1: Použitie FoundryLocalManager (odporúčané)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Možnosť 2: Manuálna konfigurácia**
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


## Architektúra kódu

### Vzor klientského továrenského vzoru

Ukážka používa továrenský vzor na vytvorenie vhodných klientov:

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


### Streamované odpovede

Ukážka demonštruje streamovanie pre generovanie odpovedí v reálnom čase:

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


## Premenné prostredia

### Konfigurácia Foundry Local

| Premenná | Popis | Predvolené | Povinné |
|----------|-------|------------|---------|
| `MODEL` | Alias modelu na použitie | `phi-4-mini` | Nie |
| `BASE_URL` | Endpoint Foundry Local | `http://localhost:8000` | Nie |
| `API_KEY` | API kľúč (voliteľný pre lokálne použitie) | `""` | Nie |

### Konfigurácia Azure OpenAI

| Premenná | Popis | Predvolené | Povinné |
|----------|-------|------------|---------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint zdroja Azure OpenAI | - | Áno |
| `AZURE_OPENAI_API_KEY` | API kľúč Azure OpenAI | - | Áno |
| `AZURE_OPENAI_API_VERSION` | Verzia API | `2024-08-01-preview` | Nie |
| `MODEL` | Názov nasadenia Azure | `your-deployment-name` | Áno |

## Pokročilé funkcie

### Automatické zisťovanie služieb

Ukážka automaticky detekuje vhodnú službu na základe premenných prostredia:

1. **Režim Azure**: Ak sú nastavené `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_API_KEY`
2. **Režim Foundry SDK**: Ak je dostupný Foundry Local SDK
3. **Manuálny režim**: Záložné riešenie manuálnej konfigurácie

### Spracovanie chýb

- Plynulý prechod z SDK na manuálnu konfiguráciu
- Jasné chybové hlásenia pre riešenie problémov
- Správne spracovanie výnimiek pri sieťových problémoch
- Validácia povinných premenných prostredia

## Úvahy o výkone

### Porovnanie lokálneho a cloudového režimu

**Výhody Foundry Local:**
- ✅ Žiadne náklady na API
- ✅ Ochrana údajov (údaje neopúšťajú zariadenie)
- ✅ Nízka latencia pre podporované modely
- ✅ Funguje offline

**Výhody Azure OpenAI:**
- ✅ Prístup k najnovším veľkým modelom
- ✅ Vyššia priepustnosť
- ✅ Žiadne požiadavky na lokálny výpočtový výkon
- ✅ SLA na úrovni podniku

## Riešenie problémov

### Bežné problémy

1. **Varovanie "Nie je možné použiť Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Chyby autentifikácie Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model nie je dostupný:**
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


## Ďalšie kroky

- **Ukážka 03**: Zisťovanie modelov a benchmarking
- **Ukážka 04**: Vytvorenie Chainlit RAG aplikácie
- **Ukážka 05**: Orchestrácia viacerých agentov
- **Ukážka 06**: Smerovanie modelov ako nástrojov

## Referencie

- [Dokumentácia Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Referenčná príručka Foundry Local SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Dokumentácia OpenAI Python SDK](https://github.com/openai/openai-python)
- [Príručka streamovaných odpovedí](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

