# Exemplu 02: Integrarea SDK OpenAI

Demonstrează integrarea avansată cu SDK-ul OpenAI pentru Python, suportând atât Microsoft Foundry Local, cât și Azure OpenAI, cu răspunsuri în flux și gestionarea corectă a erorilor.

## Prezentare generală

Acest exemplu evidențiază:
- Comutarea fără probleme între Foundry Local și Azure OpenAI
- Completări de chat în flux pentru o experiență mai bună a utilizatorului
- Utilizarea corectă a SDK-ului FoundryLocalManager
- Mecanisme robuste de gestionare a erorilor și soluții de rezervă
- Modele de cod pregătite pentru producție

## Cerințe preliminare

- **Foundry Local**: Instalată și funcțională (pentru inferență locală)
- **Python**: Versiunea 3.8 sau mai recentă cu SDK OpenAI
- **Azure OpenAI**: Endpoint valid și cheie API (pentru inferență în cloud)

## Instalare

1. **Configurarea mediului Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instalarea dependențelor:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Pornirea Foundry Local (pentru modul local):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Scenarii de utilizare

### Foundry Local (Implicit)

**Opțiunea 1: Utilizarea FoundryLocalManager (Recomandată)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Opțiunea 2: Configurare manuală**
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

## Arhitectura codului

### Modelul Factory pentru clienți

Exemplul utilizează un model factory pentru a crea clienți adecvați:

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

### Răspunsuri în flux

Exemplul demonstrează utilizarea fluxului pentru generarea răspunsurilor în timp real:

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

## Variabile de mediu

### Configurare Foundry Local

| Variabilă | Descriere | Implicit | Obligatoriu |
|-----------|-----------|----------|-------------|
| `MODEL` | Alias-ul modelului utilizat | `phi-4-mini` | Nu |
| `BASE_URL` | Endpoint-ul Foundry Local | `http://localhost:8000` | Nu |
| `API_KEY` | Cheie API (opțional pentru local) | `""` | Nu |

### Configurare Azure OpenAI

| Variabilă | Descriere | Implicit | Obligatoriu |
|-----------|-----------|----------|-------------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint-ul resursei Azure OpenAI | - | Da |
| `AZURE_OPENAI_API_KEY` | Cheia API Azure OpenAI | - | Da |
| `AZURE_OPENAI_API_VERSION` | Versiunea API | `2024-08-01-preview` | Nu |
| `MODEL` | Numele implementării Azure | `your-deployment-name` | Da |

## Funcționalități avansate

### Descoperirea automată a serviciilor

Exemplul detectează automat serviciul adecvat pe baza variabilelor de mediu:

1. **Mod Azure**: Dacă `AZURE_OPENAI_ENDPOINT` și `AZURE_OPENAI_API_KEY` sunt setate
2. **Mod SDK Foundry**: Dacă SDK-ul Foundry Local este disponibil
3. **Mod manual**: Soluție de rezervă pentru configurare manuală

### Gestionarea erorilor

- Soluție de rezervă grațioasă de la SDK la configurare manuală
- Mesaje de eroare clare pentru depanare
- Gestionarea corectă a excepțiilor pentru probleme de rețea
- Validarea variabilelor de mediu necesare

## Considerații de performanță

### Compromisuri între local și cloud

**Avantajele Foundry Local:**
- ✅ Fără costuri API
- ✅ Confidențialitatea datelor (datele nu părăsesc dispozitivul)
- ✅ Latență redusă pentru modelele suportate
- ✅ Funcționează offline

**Avantajele Azure OpenAI:**
- ✅ Acces la cele mai recente modele mari
- ✅ Debit mai mare
- ✅ Fără cerințe de calcul local
- ✅ SLA de nivel enterprise

## Depanare

### Probleme comune

1. **Avertisment "Nu s-a putut utiliza SDK-ul Foundry":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Erori de autentificare Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modelul nu este disponibil:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```

### Verificări de sănătate

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Pași următori

- **Exemplu 03**: Descoperirea și evaluarea modelelor
- **Exemplu 04**: Construirea unei aplicații Chainlit RAG
- **Exemplu 05**: Orchestrarea multi-agent
- **Exemplu 06**: Rutarea modelelor ca instrumente

## Referințe

- [Documentația Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Referința SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Documentația SDK OpenAI pentru Python](https://github.com/openai/openai-python)
- [Ghidul completărilor în flux](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

