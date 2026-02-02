# Minta 02: OpenAI SDK Integráció

Bemutatja az OpenAI Python SDK fejlett integrációját, amely támogatja a Microsoft Foundry Local és az Azure OpenAI szolgáltatásokat, streaming válaszokkal és megfelelő hibakezeléssel.

## Áttekintés

Ez a minta bemutatja:
- Zökkenőmentes váltás a Foundry Local és az Azure OpenAI között
- Streaming chat válaszok a jobb felhasználói élmény érdekében
- A FoundryLocalManager SDK helyes használata
- Robusztus hibakezelési és visszaállítási mechanizmusok
- Gyártásra kész kódminták

## Előfeltételek

- **Foundry Local**: Telepítve és futtatva (helyi inferenciához)
- **Python**: 3.8 vagy újabb OpenAI SDK-val
- **Azure OpenAI**: Érvényes végpont és API kulcs (felhőalapú inferenciához)

## Telepítés

1. **Python környezet beállítása:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Függőségek telepítése:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local indítása (helyi módhoz):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Használati forgatókönyvek

### Foundry Local (Alapértelmezett)

**1. opció: FoundryLocalManager használata (Ajánlott)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**2. opció: Manuális konfiguráció**
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

## Kódarchitektúra

### Ügyfélgyár mintázat

A minta gyári mintázatot használ a megfelelő ügyfelek létrehozásához:

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

### Streaming válaszok

A minta bemutatja a streaminget valós idejű válaszgeneráláshoz:

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

## Környezeti változók

### Foundry Local konfiguráció

| Változó | Leírás | Alapértelmezett | Kötelező |
|---------|--------|-----------------|----------|
| `MODEL` | Használandó modell alias | `phi-4-mini` | Nem |
| `BASE_URL` | Foundry Local végpont | `http://localhost:8000` | Nem |
| `API_KEY` | API kulcs (opcionális helyi használathoz) | `""` | Nem |

### Azure OpenAI konfiguráció

| Változó | Leírás | Alapértelmezett | Kötelező |
|---------|--------|-----------------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI erőforrás végpont | - | Igen |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API kulcs | - | Igen |
| `AZURE_OPENAI_API_VERSION` | API verzió | `2024-08-01-preview` | Nem |
| `MODEL` | Azure telepítési név | `your-deployment-name` | Igen |

## Fejlett funkciók

### Automatikus szolgáltatásfelismerés

A minta automatikusan felismeri a megfelelő szolgáltatást a környezeti változók alapján:

1. **Azure mód**: Ha `AZURE_OPENAI_ENDPOINT` és `AZURE_OPENAI_API_KEY` be van állítva
2. **Foundry SDK mód**: Ha a Foundry Local SDK elérhető
3. **Manuális mód**: Visszaállás manuális konfigurációra

### Hibakezelés

- Zökkenőmentes visszaállás az SDK-ról manuális konfigurációra
- Egyértelmű hibaüzenetek a hibaelhárításhoz
- Megfelelő kivételkezelés hálózati problémák esetén
- Kötelező környezeti változók validálása

## Teljesítmény szempontok

### Helyi vs Felhő előnyök

**Foundry Local előnyök:**
- ✅ Nincsenek API költségek
- ✅ Adatvédelem (az adatok nem hagyják el az eszközt)
- ✅ Alacsony késleltetés a támogatott modellekhez
- ✅ Offline működés

**Azure OpenAI előnyök:**
- ✅ Hozzáférés a legújabb nagy modellekhez
- ✅ Magasabb áteresztőképesség
- ✅ Nincsenek helyi számítási követelmények
- ✅ Vállalati szintű SLA

## Hibaelhárítás

### Gyakori problémák

1. **"Nem lehetett használni a Foundry SDK-t" figyelmeztetés:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure hitelesítési hibák:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modell nem elérhető:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Egészségügyi ellenőrzések

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Következő lépések

- **Minta 03**: Modellfelismerés és teljesítménytesztelés
- **Minta 04**: Chainlit RAG alkalmazás építése
- **Minta 05**: Többügynökös orkestráció
- **Minta 06**: Modellek eszközként történő irányítása

## Hivatkozások

- [Azure OpenAI Dokumentáció](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Referencia](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Dokumentáció](https://github.com/openai/openai-python)
- [Streaming válaszok útmutató](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

