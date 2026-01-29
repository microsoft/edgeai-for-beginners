# Ejemplo 04: Aplicaciones de Chat de Producción con Chainlit

Un ejemplo completo que demuestra múltiples enfoques para construir aplicaciones de chat listas para producción utilizando Microsoft Foundry Local, con interfaces web modernas, respuestas en streaming y tecnologías avanzadas de navegador.

## Qué Incluye

- **🚀 Aplicación de Chat Chainlit** (`app.py`): Aplicación de chat lista para producción con streaming
- **🌐 Demo WebGPU** (`webgpu-demo/`): Inferencia de IA basada en navegador con aceleración por hardware
- **🎨 Integración Open WebUI** (`open-webui-guide.md`): Interfaz profesional similar a ChatGPT
- **📚 Notebook Educativo** (`chainlit_app.ipynb`): Materiales interactivos de aprendizaje

## Inicio Rápido

### 1. Aplicación de Chat Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Se abre en: `http://localhost:8080`

### 2. Demo de Navegador WebGPU

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Se abre en: `http://localhost:5173`

### 3. Configuración de Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Se abre en: `http://localhost:3000`

## Patrones de Arquitectura

### Matriz de Decisión Local vs Nube

| Escenario | Recomendación | Razón |
|-----------|---------------|-------|
| **Datos Sensibles** | 🏠 Local (Foundry) | Los datos nunca salen del dispositivo |
| **Razonamiento Complejo** | ☁️ Nube (Azure OpenAI) | Acceso a modelos más grandes |
| **Chat en Tiempo Real** | 🏠 Local (Foundry) | Menor latencia, respuestas más rápidas |
| **Análisis de Documentos** | 🔄 Híbrido | Local para extracción, nube para análisis |
| **Generación de Código** | 🏠 Local (Foundry) | Privacidad + modelos especializados |
| **Tareas de Investigación** | ☁️ Nube (Azure OpenAI) | Se necesita una base de conocimiento amplia |

### Comparación de Tecnologías

| Tecnología | Caso de Uso | Ventajas | Desventajas |
|------------|-------------|----------|-------------|
| **Chainlit** | Desarrolladores Python, prototipado rápido | Configuración sencilla, soporte de streaming | Solo Python |
| **WebGPU** | Máxima privacidad, escenarios offline | Nativo del navegador, no requiere servidor | Tamaño de modelo limitado |
| **Open WebUI** | Despliegue en producción, equipos | UI profesional, gestión de usuarios | Requiere Docker |

## Requisitos Previos

- **Foundry Local**: Instalado y ejecutándose ([Descargar](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ con entorno virtual
- **Modelo**: Al menos uno cargado (`foundry model run phi-4-mini`)
- **Navegador**: Chrome/Edge con soporte WebGPU para demos
- **Docker**: Para Open WebUI (opcional)

## Instalación y Configuración

### 1. Configuración del Entorno Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuración de Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Aplicaciones de Ejemplo

### Aplicación de Chat Chainlit

**Características:**
- 🚀 **Streaming en Tiempo Real**: Los tokens aparecen a medida que se generan
- 🛡️ **Manejo Robusto de Errores**: Degradación y recuperación elegantes
- 🎨 **UI Moderna**: Interfaz de chat profesional lista para usar
- 🔧 **Configuración Flexible**: Variables de entorno y detección automática
- 📱 **Diseño Responsivo**: Funciona en dispositivos de escritorio y móviles

**Inicio Rápido:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### Demo de Navegador WebGPU

**Características:**
- 🌐 **IA Nativa del Navegador**: No requiere servidor, se ejecuta completamente en el navegador
- ⚡ **Aceleración WebGPU**: Aceleración por hardware cuando está disponible
- 🔒 **Máxima Privacidad**: Los datos nunca salen de tu dispositivo
- 🎯 **Instalación Cero**: Funciona en cualquier navegador compatible
- 🔄 **Fallback Elegante**: Cambia automáticamente a CPU si WebGPU no está disponible

**Ejecución:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integración Open WebUI

**Características:**
- 🎨 **Interfaz Similar a ChatGPT**: UI profesional y familiar
- 👥 **Soporte Multiusuario**: Cuentas de usuario e historial de conversaciones
- 📁 **Procesamiento de Archivos**: Subir y analizar documentos
- 🔄 **Cambio de Modelos**: Cambio fácil entre diferentes modelos
- 🐳 **Despliegue con Docker**: Configuración lista para producción en contenedores

**Configuración Rápida:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Referencia de Configuración

### Variables de Entorno

| Variable | Descripción | Predeterminado | Ejemplo |
|----------|-------------|----------------|---------|
| `MODEL` | Alias del modelo a usar | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Endpoint de Foundry Local | Detectado automáticamente | `http://localhost:51211` |
| `API_KEY` | Clave API (opcional para local) | `""` | `your-api-key` |

## Solución de Problemas

### Problemas Comunes

**Aplicación Chainlit:**

1. **Servicio no disponible:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Conflictos de puertos:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problemas con el entorno Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Demo WebGPU:**

1. **WebGPU no soportado:**
   - Actualiza a Chrome/Edge 113+
   - Habilita WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Verifica el estado de la GPU: `chrome://gpu`
   - El demo cambiará automáticamente a CPU

2. **Errores de carga de modelos:**
   - Asegúrate de tener conexión a internet para descargar el modelo
   - Revisa la consola del navegador para errores CORS
   - Verifica que estés sirviendo vía HTTP (no file://)

**Open WebUI:**

1. **Conexión rechazada:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modelos no aparecen:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Lista de Verificación de Validación

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Uso Avanzado

### Optimización de Rendimiento

**Chainlit:**
- Usa streaming para mejorar la percepción de rendimiento
- Implementa agrupación de conexiones para alta concurrencia
- Cachea respuestas de modelos para consultas repetidas
- Monitorea el uso de memoria con historiales de conversación grandes

**WebGPU:**
- Usa WebGPU para máxima privacidad y velocidad
- Implementa cuantización de modelos para modelos más pequeños
- Usa Web Workers para procesamiento en segundo plano
- Cachea modelos compilados en el almacenamiento del navegador

**Open WebUI:**
- Usa volúmenes persistentes para historial de conversaciones
- Configura límites de recursos para el contenedor Docker
- Implementa estrategias de respaldo para datos de usuarios
- Configura un proxy inverso para terminación SSL

### Patrones de Integración

**Híbrido Local/Nube:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Pipeline Multimodal:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Despliegue en Producción

### Consideraciones de Seguridad

- **Claves API**: Usa variables de entorno, nunca las codifiques directamente
- **Red**: Usa HTTPS en producción, considera VPN para acceso del equipo
- **Control de Acceso**: Implementa autenticación para Open WebUI
- **Privacidad de Datos**: Audita qué datos permanecen locales y cuáles van a la nube
- **Actualizaciones**: Mantén Foundry Local y los contenedores actualizados

### Monitoreo y Mantenimiento

- **Verificaciones de Salud**: Implementa monitoreo de endpoints
- **Registro**: Centraliza los registros de todos los componentes
- **Métricas**: Rastrea tiempos de respuesta, tasas de error, uso de recursos
- **Respaldo**: Realiza respaldos regulares de datos de conversaciones y configuraciones

## Referencias y Recursos

### Documentación
- [Documentación de Chainlit](https://docs.chainlit.io/) - Guía completa del framework
- [Documentación de Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Documentos oficiales de Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integración WebGPU
- [Documentación de Open WebUI](https://docs.openwebui.com/) - Configuración avanzada

### Archivos de Ejemplo
- [`app.py`](../../../../../Module08/samples/04/app.py) - Aplicación Chainlit de producción
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Notebook educativo
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Inferencia de IA basada en navegador
- [`open-webui-guide.md`](./open-webui-guide.md) - Configuración completa de Open WebUI

### Ejemplos Relacionados
- [Documentación de la Sesión 4](../../04.CuttingEdgeModels.md) - Guía completa de la sesión
- [Ejemplos de Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Ejemplos oficiales

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.