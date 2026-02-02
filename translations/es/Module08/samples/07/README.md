# Ejemplo de Foundry Local como API

Este ejemplo demuestra cómo usar Microsoft Foundry Local como un servicio API REST sin depender del SDK de OpenAI. Muestra patrones de integración directa mediante HTTP para obtener el máximo control y personalización.

## Descripción General

Basado en los patrones oficiales de Microsoft Foundry Local, este ejemplo proporciona:
- Integración directa con la API REST de FoundryLocalManager
- Implementación personalizada de cliente HTTP
- Gestión de modelos y monitoreo de estado
- Manejo de respuestas en streaming y no streaming
- Lógica de manejo de errores y reintentos lista para producción

## Requisitos Previos

1. **Instalación de Foundry Local**  
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```
  
2. **Dependencias de Python**  
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```
  

## Arquitectura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```
  

## Características Clave

### 1. **Integración Directa con HTTP**
- Llamadas puras a la API REST sin dependencias del SDK
- Autenticación y encabezados personalizados
- Control total sobre el manejo de solicitudes y respuestas

### 2. **Gestión de Modelos**
- Carga y descarga dinámica de modelos
- Monitoreo de estado y comprobaciones de salud
- Recopilación de métricas de rendimiento

### 3. **Patrones de Producción**
- Mecanismos de reintento con retroceso exponencial
- Circuit breaker para tolerancia a fallos
- Registro y monitoreo exhaustivos

### 4. **Manejo Flexible de Respuestas**
- Respuestas en streaming para aplicaciones en tiempo real
- Procesamiento por lotes para escenarios de alto rendimiento
- Análisis y validación personalizada de respuestas

## Ejemplos de Uso

### Integración Básica con API  
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```
  

### Integración en Streaming  
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```
  

### Monitoreo de Salud  
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```
  

## Estructura de Archivos

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```
  

## Integración con Microsoft Foundry Local

Este ejemplo sigue los patrones oficiales de Microsoft:

1. **Integración con SDK**: Utiliza `FoundryLocalManager` para la gestión del servicio  
2. **Endpoints REST**: Llamadas directas a `/v1/chat/completions` y otros endpoints  
3. **Autenticación**: Manejo adecuado de claves API para servicios locales  
4. **Gestión de Modelos**: Listado de catálogo, descarga y patrones de carga  
5. **Manejo de Errores**: Códigos de error y respuestas recomendadas por Microsoft  

## Primeros Pasos

1. **Instalar Dependencias**  
   ```bash
   pip install -r requirements.txt
   ```
  
2. **Ejecutar Ejemplo Básico**  
   ```bash
   python examples/basic_usage.py
   ```
  
3. **Probar Streaming**  
   ```bash
   python examples/streaming.py
   ```
  
4. **Configuración para Producción**  
   ```bash
   python examples/production.py
   ```
  

## Configuración

Variables de entorno para personalización:
- `FOUNDRY_MODEL`: Modelo predeterminado a usar (por defecto: "phi-4-mini")  
- `FOUNDRY_TIMEOUT`: Tiempo de espera de solicitud en segundos (por defecto: 30)  
- `FOUNDRY_RETRIES`: Número de intentos de reintento (por defecto: 3)  
- `FOUNDRY_LOG_LEVEL`: Nivel de registro (por defecto: "INFO")  

## Mejores Prácticas

1. **Gestión de Conexiones**: Reutilizar conexiones HTTP para mejorar el rendimiento  
2. **Manejo de Errores**: Implementar lógica de reintento adecuada con retroceso exponencial  
3. **Monitoreo de Recursos**: Rastrear el uso de memoria y rendimiento de los modelos  
4. **Seguridad**: Usar autenticación adecuada incluso para servicios locales  
5. **Pruebas**: Incluir pruebas unitarias y de integración  

## Solución de Problemas

### Problemas Comunes

**Servicio No Ejecutándose**  
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```
  

**Problemas de Carga de Modelos**  
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```
  

**Errores de Conexión**
- Verificar que Foundry Local esté ejecutándose en el puerto correcto  
- Revisar configuraciones de firewall  
- Asegurarse de que los encabezados de autenticación sean correctos  

## Optimización de Rendimiento

1. **Agrupación de Conexiones**: Usar objetos de sesión para múltiples solicitudes  
2. **Operaciones Asíncronas**: Aprovechar asyncio para solicitudes concurrentes  
3. **Caché**: Almacenar en caché las respuestas de los modelos cuando sea apropiado  
4. **Monitoreo**: Rastrear tiempos de respuesta y ajustar los tiempos de espera  

## Resultados de Aprendizaje

Después de completar este ejemplo, comprenderás:
- Integración directa con la API REST de Foundry Local  
- Patrones de implementación de clientes HTTP personalizados  
- Manejo de errores y monitoreo listo para producción  
- Arquitectura del servicio Microsoft Foundry Local  
- Técnicas de optimización de rendimiento para servicios de IA locales  

## Próximos Pasos

- Explorar el Ejemplo 08: Aplicación de Chat en Windows 11  
- Probar el Ejemplo 09: Orquestación Multi-Agente  
- Aprender del Ejemplo 10: Foundry Local como Integración de Herramientas  

---

