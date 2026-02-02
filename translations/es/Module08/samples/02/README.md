# Ejemplo 02: Integración con el SDK de OpenAI

Demuestra una integración avanzada con el SDK de Python de OpenAI, compatible tanto con Microsoft Foundry Local como con Azure OpenAI, incluyendo respuestas en streaming y manejo adecuado de errores.

## Descripción General

Este ejemplo muestra:
- Cambio fluido entre Foundry Local y Azure OpenAI
- Respuestas de chat en streaming para una mejor experiencia de usuario
- Uso adecuado del SDK FoundryLocalManager
- Mecanismos robustos de manejo de errores y alternativas
- Patrones de código listos para producción

## Requisitos Previos

- **Foundry Local**: Instalado y en ejecución (para inferencia local)
- **Python**: Versión 3.8 o posterior con el SDK de OpenAI
- **Azure OpenAI**: Endpoint válido y clave API (para inferencia en la nube)

## Instalación

1. **Configurar el entorno de Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instalar dependencias:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Iniciar Foundry Local (para modo local):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Escenarios de Uso

### Foundry Local (Predeterminado)

**Opción 1: Usar FoundryLocalManager (Recomendado)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Opción 2: Configuración Manual**
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


## Arquitectura del Código

### Patrón de Fábrica de Clientes

El ejemplo utiliza un patrón de fábrica para crear clientes adecuados:

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


### Respuestas en Streaming

El ejemplo demuestra cómo generar respuestas en tiempo real mediante streaming:

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


## Variables de Entorno

### Configuración de Foundry Local

| Variable | Descripción | Predeterminado | Requerido |
|----------|-------------|----------------|-----------|
| `MODEL` | Alias del modelo a usar | `phi-4-mini` | No |
| `BASE_URL` | Endpoint de Foundry Local | `http://localhost:8000` | No |
| `API_KEY` | Clave API (opcional para local) | `""` | No |

### Configuración de Azure OpenAI

| Variable | Descripción | Predeterminado | Requerido |
|----------|-------------|----------------|-----------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint del recurso Azure OpenAI | - | Sí |
| `AZURE_OPENAI_API_KEY` | Clave API de Azure OpenAI | - | Sí |
| `AZURE_OPENAI_API_VERSION` | Versión de la API | `2024-08-01-preview` | No |
| `MODEL` | Nombre del despliegue en Azure | `your-deployment-name` | Sí |

## Funcionalidades Avanzadas

### Descubrimiento Automático de Servicios

El ejemplo detecta automáticamente el servicio adecuado basado en las variables de entorno:

1. **Modo Azure**: Si `AZURE_OPENAI_ENDPOINT` y `AZURE_OPENAI_API_KEY` están configurados
2. **Modo SDK Foundry**: Si el SDK de Foundry Local está disponible
3. **Modo Manual**: Alternativa en caso de configuración manual

### Manejo de Errores

- Alternativa fluida del SDK a la configuración manual
- Mensajes de error claros para facilitar la resolución de problemas
- Manejo adecuado de excepciones para problemas de red
- Validación de las variables de entorno requeridas

## Consideraciones de Rendimiento

### Comparación entre Local y Nube

**Ventajas de Foundry Local:**
- ✅ Sin costos de API
- ✅ Privacidad de datos (los datos no salen del dispositivo)
- ✅ Baja latencia para modelos compatibles
- ✅ Funciona sin conexión

**Ventajas de Azure OpenAI:**
- ✅ Acceso a los últimos modelos grandes
- ✅ Mayor capacidad de procesamiento
- ✅ Sin requisitos de computación local
- ✅ SLA de nivel empresarial

## Resolución de Problemas

### Problemas Comunes

1. **Advertencia: "No se pudo usar el SDK de Foundry":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Errores de autenticación en Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modelo no disponible:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Verificaciones de Salud

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Próximos Pasos

- **Ejemplo 03**: Descubrimiento y evaluación de modelos
- **Ejemplo 04**: Construcción de una aplicación RAG con Chainlit
- **Ejemplo 05**: Orquestación de múltiples agentes
- **Ejemplo 06**: Enrutamiento de modelos como herramientas

## Referencias

- [Documentación de Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Referencia del SDK de Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Documentación del SDK de Python de OpenAI](https://github.com/openai/openai-python)
- [Guía de Respuestas en Streaming](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

