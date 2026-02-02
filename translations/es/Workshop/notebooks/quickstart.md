# Guía Rápida de los Cuadernos del Taller

## Tabla de Contenidos

- [Requisitos Previos](../../../../Workshop/notebooks)
- [Configuración Inicial](../../../../Workshop/notebooks)
- [Sesión 04: Comparación de Modelos](../../../../Workshop/notebooks)
- [Sesión 05: Orquestador Multi-Agente](../../../../Workshop/notebooks)
- [Sesión 06: Enrutamiento de Modelos Basado en Intenciones](../../../../Workshop/notebooks)
- [Variables de Entorno](../../../../Workshop/notebooks)
- [Comandos Comunes](../../../../Workshop/notebooks)

---

## Requisitos Previos

### 1. Instalar Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verificar Instalación:**
```bash
foundry --version
```

### 2. Instalar Dependencias de Python

```bash
cd Workshop
pip install -r requirements.txt
```

O instalar individualmente:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Configuración Inicial

### Iniciar el Servicio Foundry Local

**Requerido antes de ejecutar cualquier cuaderno:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Salida esperada:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Descargar y Cargar Modelos

Los cuadernos utilizan estos modelos por defecto:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Verificar Configuración

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sesión 04: Comparación de Modelos

### Propósito
Comparar el rendimiento entre Modelos de Lenguaje Pequeños (SLM) y Modelos de Lenguaje Grandes (LLM).

### Configuración Rápida

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Ejecutar el Cuaderno

1. **Abrir** `session04_model_compare.ipynb` en VS Code o Jupyter
2. **Reiniciar el kernel** (Kernel → Reiniciar Kernel)
3. **Ejecutar todas las celdas** en orden

### Configuración Clave

**Modelos por Defecto:**
- **SLM:** `phi-4-mini` (~4GB RAM, más rápido)
- **LLM:** `qwen2.5-3b` (~3GB RAM, optimizado para memoria)

**Variables de Entorno (opcional):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Salida Esperada

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Personalización

**Usar modelos diferentes:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Prompt personalizado:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Lista de Verificación de Validación

- [ ] La celda 12 muestra los modelos correctos (phi-4-mini, qwen2.5-3b)
- [ ] La celda 12 muestra el endpoint correcto (puerto 59959)
- [ ] La celda 16 pasa el diagnóstico (✅ Servicio en ejecución)
- [ ] La celda 20 pasa la verificación previa (ambos modelos ok)
- [ ] La celda 22 completa la comparación con valores de latencia
- [ ] La celda 24 muestra 🎉 ¡TODAS LAS VERIFICACIONES PASADAS!

### Estimación de Tiempo
- **Primera ejecución:** 5-10 minutos (incluyendo descargas de modelos)
- **Ejecuciones posteriores:** 1-2 minutos

---

## Sesión 05: Orquestador Multi-Agente

### Propósito
Demostrar colaboración multi-agente utilizando el SDK de Foundry Local: los agentes trabajan juntos para producir resultados refinados.

### Configuración Rápida

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Ejecutar el Cuaderno

1. **Abrir** `session05_agents_orchestrator.ipynb`
2. **Reiniciar el kernel**
3. **Ejecutar todas las celdas** en orden

### Configuración Clave

**Configuración por Defecto (Mismo Modelo para Ambos Agentes):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Configuración Avanzada (Modelos Diferentes):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arquitectura

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Salida Esperada

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Extensiones

**Agregar más agentes:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Pruebas en lote:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Estimación de Tiempo
- **Primera ejecución:** 3-5 minutos
- **Ejecuciones posteriores:** 1-2 minutos por pregunta

---

## Sesión 06: Enrutamiento de Modelos Basado en Intenciones

### Propósito
Dirigir inteligentemente los prompts a modelos especializados según la intención detectada.

### Configuración Rápida

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Nota:** La sesión 06 utiliza modelos CPU por defecto para máxima compatibilidad.

### Ejecutar el Cuaderno

1. **Abrir** `session06_models_router.ipynb`
2. **Reiniciar el kernel**
3. **Ejecutar todas las celdas** en orden

### Configuración Clave

**Catálogo por Defecto (Modelos CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternativa (Modelos GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Detección de Intenciones

El enrutador utiliza patrones regex para detectar intenciones:

| Intención | Ejemplos de Patrones | Dirigido a |
|-----------|-----------------------|------------|
| `code` | "refactorizar", "implementar función" | phi-3.5-mini-cpu |
| `classification` | "categorizar", "clasificar esto" | qwen2.5-0.5b-cpu |
| `summarize` | "resumir", "tl;dr" | phi-4-mini-cpu |
| `general` | Todo lo demás | phi-4-mini-cpu |

### Salida Esperada

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Personalización

**Agregar intención personalizada:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Habilitar seguimiento de tokens:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Cambiar a Modelos GPU

Si tienes más de 8GB de VRAM:

1. En **Celda #6**, comenta el catálogo CPU
2. Descomenta el catálogo GPU
3. Carga los modelos GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Reinicia el kernel y vuelve a ejecutar el cuaderno

### Estimación de Tiempo
- **Primera ejecución:** 5-10 minutos (carga de modelos)
- **Ejecuciones posteriores:** 30-60 segundos por prueba

---

## Variables de Entorno

### Configuración Global

Configurar antes de iniciar Jupyter/VS Code:

**Windows (Command Prompt):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Configuración en el Cuaderno

Configurar al inicio de cualquier cuaderno:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Comandos Comunes

### Gestión del Servicio

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Gestión de Modelos

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Pruebas de Endpoints

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Comandos de Diagnóstico

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Mejores Prácticas

### Antes de Iniciar Cualquier Cuaderno

1. **Verificar que el servicio esté en ejecución:**
   ```bash
   foundry service status
   ```

2. **Confirmar que los modelos estén cargados:**
   ```bash
   foundry model ls
   ```

3. **Reiniciar el kernel del cuaderno** si se vuelve a ejecutar

4. **Limpiar todas las salidas** para una ejecución limpia

### Gestión de Recursos

1. **Usar modelos CPU por defecto** para compatibilidad
2. **Cambiar a modelos GPU** solo si tienes más de 8GB de VRAM
3. **Cerrar otras aplicaciones GPU** antes de ejecutar
4. **Mantener el servicio en ejecución** entre sesiones de cuadernos
5. **Monitorear el uso de recursos** con el Administrador de Tareas / nvidia-smi

### Solución de Problemas

1. **Siempre verificar el servicio primero** antes de depurar el código
2. **Reiniciar el kernel** si ves configuraciones obsoletas
3. **Re-ejecutar las celdas de diagnóstico** después de cualquier cambio
4. **Confirmar que los nombres de los modelos** coincidan con los cargados
5. **Verificar que el puerto del endpoint** coincida con el estado del servicio

---

## Referencia Rápida: Alias de Modelos

### Modelos Comunes

| Alias | Tamaño | Mejor Para | RAM/VRAM | Variantes |
|-------|--------|------------|----------|-----------|
| `phi-4-mini` | ~4B | Chat general, resumen | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Generación de código, refactorización | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Tareas generales, eficiente | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Rápido, pocos recursos | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Clasificación, mínimos recursos | 1-2GB | `-cpu`, `-cuda-gpu` |

### Nomenclatura de Variantes

- **Nombre base** (e.g., `phi-4-mini`): Selecciona automáticamente la mejor variante para tu hardware
- **`-cpu`**: Optimizado para CPU, funciona en todas partes
- **`-cuda-gpu`**: Optimizado para GPU NVIDIA, requiere más de 8GB de VRAM
- **`-npu`**: Optimizado para NPU Qualcomm, requiere drivers NPU

**Recomendación:** Usa nombres base (sin sufijo) y permite que Foundry Local seleccione automáticamente la mejor variante.

---

## Indicadores de Éxito

Estás listo cuando veas:

✅ `foundry service status` muestra "running"  
✅ `foundry model ls` muestra los modelos requeridos  
✅ Servicio accesible en el endpoint correcto  
✅ Verificación de salud devuelve 200 OK  
✅ Las celdas de diagnóstico del cuaderno pasan  
✅ Sin errores de conexión en la salida  

---

## Obtener Ayuda

### Documentación
- **Repositorio Principal**: https://github.com/microsoft/Foundry-Local
- **SDK de Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referencia CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Solución de Problemas**: Ver `troubleshooting.md` en este directorio

### Problemas en GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Última Actualización:** 8 de octubre de 2025  
**Versión:** Cuadernos del Taller 2.0

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.