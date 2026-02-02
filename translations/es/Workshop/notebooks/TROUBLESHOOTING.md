# Cuadernos del Taller - Guía de Solución de Problemas

## Tabla de Contenidos

- [Problemas Comunes y Soluciones](../../../../Workshop/notebooks)
- [Problemas Específicos de la Sesión 04](../../../../Workshop/notebooks)
- [Problemas Específicos de la Sesión 05](../../../../Workshop/notebooks)
- [Problemas Específicos de la Sesión 06](../../../../Workshop/notebooks)
- [Problemas Específicos de Hardware](../../../../Workshop/notebooks)
- [Comandos de Diagnóstico](../../../../Workshop/notebooks)
- [Obteniendo Ayuda](../../../../Workshop/notebooks)

---

## Problemas Comunes y Soluciones

### 🔴 CUDA Out of Memory

**Mensaje de Error:**
```
CUDA failure 2: out of memory
```
  
**Causa Principal:** La GPU no tiene suficiente VRAM para cargar el modelo.

**Soluciones:**

#### Opción 1: Usar Variantes de CPU (Recomendado)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### Opción 2: Usar Modelos Más Pequeños en GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### Opción 3: Limpiar Memoria de GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### Opción 4: Incrementar Memoria de GPU (si es posible)
- Cierra pestañas del navegador, editores de video u otras aplicaciones que usen GPU.
- Reduce los efectos visuales de Windows.
- Usa la GPU dedicada si tienes integrada + dedicada.

---

### 🔴 APIConnectionError: Error de Conexión

**Mensaje de Error:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**Causa Principal:** El servicio Foundry Local no está ejecutándose o no es accesible.

**Soluciones:**

#### Paso 1: Verificar Estado del Servicio
```bash
foundry service status
```
  
#### Paso 2: Iniciar el Servicio si está Detenido
```bash
foundry service start
```
  
#### Paso 3: Verificar el Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### Paso 4: Cargar los Modelos Requeridos
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### Paso 5: Reiniciar el Kernel del Cuaderno
Después de iniciar el servicio y cargar los modelos, reinicia el kernel del cuaderno y ejecuta todas las celdas nuevamente.

---

### 🔴 Modelo No Encontrado en el Catálogo

**Mensaje de Error:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**Causa Principal:** El modelo no está descargado o cargado en Foundry Local.

**Soluciones:**

#### Opción 1: Descargar y Cargar Modelos
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### Opción 2: Usar el Modo de Selección Automática
Actualiza tu CATALOG para usar nombres base de modelos (sin el sufijo `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
El SDK de Foundry Local seleccionará automáticamente la mejor variante (CPU, GPU o NPU) para tu hardware.

---

### 🔴 HttpResponseError: 500 - Error al Cargar Modelo

**Mensaje de Error:**
```
HttpResponseError: 500 - Failed loading model
```
  
**Causa Principal:** El archivo del modelo está corrupto o es incompatible con el hardware.

**Soluciones:**

#### Volver a Descargar el Modelo
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```
  
#### Usar una Variante Diferente
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```
  
---

### 🔴 ImportError: No se Encontró el Módulo

**Mensaje de Error:**
```
ModuleNotFoundError: No module named 'foundry_local'
```
  
**Causa Principal:** El paquete foundry-local-sdk no está instalado.

**Soluciones:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  
---

### � Solicitud Inicial Lenta

**Síntoma:** La primera respuesta tarda más de 30 segundos, las solicitudes posteriores son rápidas.

**Causa Principal:** Esto es un comportamiento normal: el servicio está cargando el modelo en memoria en la primera solicitud.

**Soluciones:**

#### Pre-cargar Modelos
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### Mantener el Servicio Activo
```bash
# Start service manually and leave it running
foundry service start
```
  
---

## Problemas Específicos de la Sesión 04

### Configuración de Puerto Incorrecta

**Problema:** El cuaderno se conecta al puerto incorrecto (55769 vs 59959 vs 57127).

**Solución:**

1. Verifica qué puerto está usando Foundry Local:
```bash
foundry service status
# Note the port number displayed
```
  
2. Actualiza la Celda 10 en el cuaderno:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. Reinicia el kernel y ejecuta nuevamente las celdas 6, 8, 10, 12, 16, 20, 22.

---

### Selección Incorrecta de Modelo

**Problema:** El cuaderno muestra gpt-oss-20b o qwen2.5-7b en lugar de qwen2.5-3b.

**Solución:**

1. Reinicia el kernel del cuaderno (limpia el estado de las variables antiguas).
2. Ejecuta nuevamente la Celda 10 (Establecer Alias de Modelos).
3. Ejecuta nuevamente la Celda 12 (Mostrar Configuración).
4. **Verifica:** La Celda 12 debería mostrar `LLM Model: qwen2.5-3b`.

---

### Falla en la Celda de Diagnóstico

**Problema:** La Celda 16 muestra "❌ Foundry Local service not found!"

**Solución:**

1. Verifica que el servicio esté ejecutándose:
```bash
foundry service status
```
  
2. Prueba el endpoint manualmente:
```bash
curl http://localhost:59959/v1/models
```
  
3. Si curl funciona pero el cuaderno no:
   - Reinicia el kernel del cuaderno.
   - Ejecuta las celdas en orden: 6, 8, 10, 12, 14, 16.

4. Si curl falla:
   - Inicia el servicio: `foundry service start`.
   - Carga los modelos: `foundry model run phi-4-mini` y `foundry model run qwen2.5-3b`.

---

### Falla en la Verificación Previa

**Problema:** La Celda 20 muestra errores de conexión aunque el diagnóstico pasó.

**Solución:**

1. Verifica que los modelos estén cargados:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. Si faltan modelos:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. Ejecuta nuevamente la Celda 20 después de cargar los modelos.

---

### Falla en la Comparación con Valores None

**Problema:** La Celda 22 se completa pero muestra latencia como None.

**Solución:**

1. Verifica que la verificación previa haya pasado primero (Celda 20).
2. Ejecuta nuevamente la Celda 22: los modelos pueden necesitar calentarse en la primera solicitud.
3. Verifica que ambos modelos estén cargados: `foundry model ls`.

---

## Problemas Específicos de la Sesión 05

### Agente Usando el Modelo Incorrecto

**Problema:** El agente no está usando el modelo esperado.

**Solución:**

Verifica la configuración:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
Reinicia el kernel si los modelos son incorrectos.

---

### Desbordamiento de Contexto de Memoria

**Problema:** Las respuestas del agente se degradan con el tiempo.

**Solución:** Ya está manejado automáticamente: los agentes mantienen solo los últimos 6 mensajes en memoria.

---

## Problemas Específicos de la Sesión 06

### Confusión entre Modelos de CPU y GPU

**Problema:** Aparecen errores de CUDA al usar la configuración predeterminada.

**Solución:** La configuración predeterminada ahora usa modelos de CPU. Si ves errores de CUDA:

1. Verifica que estás usando el catálogo predeterminado de CPU:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. Reinicia el kernel y ejecuta todas las celdas nuevamente.

---

### Detección de Intención No Funciona

**Problema:** Las indicaciones se están dirigiendo a modelos incorrectos.

**Solución:**

Prueba la detección de intención:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
Actualiza las RULES si los patrones necesitan ajustes.

---

## Problemas Específicos de Hardware

### GPU NVIDIA

**Verificar Estado de la GPU:**
```bash
nvidia-smi
```
  
**Problemas Comunes:**
- **Controlador desactualizado:** Actualiza los controladores de NVIDIA.
- **Incompatibilidad de versión de CUDA:** Reinstala Foundry Local.
- **Memoria de GPU fragmentada:** Reinicia el sistema.

### NPU Qualcomm

**Verificar Estado de la NPU:**
```bash
foundry device info
```
  
**Problemas Comunes:**
- **Controladores de NPU no instalados:** Instala los controladores de NPU de Qualcomm.
- **Variante de NPU no disponible:** Usa la variante de CPU.
- **Versión de Windows muy antigua:** Actualiza a la última versión de Windows 11.

### Sistemas Solo con CPU

**Modelos Recomendados:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**Consejos de Rendimiento:**
- Usa modelos más pequeños.
- Reduce max_tokens.
- Ten paciencia con la primera solicitud.

---

## Comandos de Diagnóstico

### Verificar Todo
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```
  
### En Python
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```
  
---

## Obteniendo Ayuda

### 1. Verificar Registros
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. Problemas en GitHub
- Busca problemas existentes: https://github.com/microsoft/Foundry-Local/issues
- Crea un nuevo problema con:
  - Mensaje de error (texto completo).
  - Salida de `foundry service status`.
  - Salida de `foundry --version`.
  - Información de GPU/NPU (nvidia-smi, etc.).
  - Pasos para reproducir.

### 3. Documentación
- **Repositorio Principal:** https://github.com/microsoft/Foundry-Local
- **SDK de Python:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referencia CLI:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Solución de Problemas:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Lista de Verificación de Soluciones Rápidas

Cuando algo falla, prueba esto en orden:

- [ ] Verifica que el servicio esté ejecutándose: `foundry service status`.
- [ ] Reinicia el servicio: `foundry service stop && foundry service start`.
- [ ] Verifica que el modelo exista: `foundry model ls | grep phi-4-mini`.
- [ ] Carga los modelos requeridos: `foundry model run phi-4-mini`.
- [ ] Verifica la memoria de GPU: `nvidia-smi` (si usas NVIDIA).
- [ ] Prueba la variante de CPU: Usa `phi-4-mini-cpu` en lugar de `phi-4-mini`.
- [ ] Reinicia el kernel del cuaderno.
- [ ] Limpia las salidas del cuaderno y ejecuta todas las celdas nuevamente.
- [ ] Reinstala el SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`.
- [ ] Reinicia el sistema (como último recurso).

---

## Consejos de Prevención

### Mejores Prácticas

1. **Siempre verifica el servicio primero:**
   ```bash
   foundry service status
   ```
  
2. **Usa variantes de CPU por defecto:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```
  
3. **Pre-carga modelos antes de ejecutar cuadernos:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```
  
4. **Mantén el servicio activo:**
   - No detengas/inicies el servicio innecesariamente.
   - Déjalo ejecutándose en segundo plano entre sesiones.

5. **Monitorea recursos:**
   - Verifica la memoria de GPU antes de ejecutar.
   - Cierra aplicaciones innecesarias que usen GPU.
   - Usa el Administrador de Tareas / nvidia-smi.

6. **Actualiza regularmente:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  
---

**Última Actualización:** 8 de octubre de 2025

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.