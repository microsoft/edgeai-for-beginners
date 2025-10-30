<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T20:07:59+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "es"
}
-->
# Muestras del Taller - Resumen de Actualización del SDK Local de Foundry

## Resumen

Todas las muestras de Python en el directorio `Workshop/samples` han sido actualizadas para seguir las mejores prácticas del SDK Local de Foundry y garantizar la consistencia en todo el taller.

**Fecha**: 8 de octubre de 2025  
**Alcance**: 9 archivos de Python en 6 sesiones del taller  
**Enfoque Principal**: Manejo de errores, documentación, patrones del SDK, experiencia del usuario

---

## Archivos Actualizados

### Sesión 01: Introducción
- ✅ `chat_bootstrap.py` - Ejemplos básicos de chat y transmisión

### Sesión 02: Soluciones RAG
- ✅ `rag_pipeline.py` - Implementación de RAG con embeddings
- ✅ `rag_eval_ragas.py` - Evaluación de RAG con métricas RAGAS

### Sesión 03: Modelos de Código Abierto
- ✅ `benchmark_oss_models.py` - Comparación de múltiples modelos

### Sesión 04: Modelos de Última Generación
- ✅ `model_compare.py` - Comparación entre SLM y LLM

### Sesión 05: Agentes Impulsados por IA
- ✅ `agents_orchestrator.py` - Coordinación de múltiples agentes

### Sesión 06: Modelos como Herramientas
- ✅ `models_router.py` - Enrutamiento basado en intención
- ✅ `models_pipeline.py` - Pipeline enrutado de múltiples pasos

### Infraestructura de Soporte
- ✅ `workshop_utils.py` - Ya sigue las mejores prácticas (no se realizaron cambios)

---

## Mejoras Clave

### 1. Manejo de Errores Mejorado

**Antes:**
```python
manager, client, model_id = get_client(alias)
```

**Después:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Beneficios:**
- Manejo de errores más elegante con mensajes claros
- Pistas útiles para solucionar problemas
- Códigos de salida adecuados para scripts

### 2. Mejor Gestión de Importaciones

**Antes:**
```python
from sentence_transformers import SentenceTransformer
```

**Después:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Beneficios:**
- Orientación clara cuando faltan dependencias
- Prevención de errores de importación confusos
- Instrucciones amigables para la instalación

### 3. Documentación Integral

**Añadido a todas las muestras:**
- Documentación de variables de entorno en los docstrings
- Enlaces de referencia al SDK
- Ejemplos de uso
- Documentación detallada de funciones/parámetros
- Indicaciones de tipo para mejor soporte en IDE

**Ejemplo:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Mejor Retroalimentación al Usuario

**Añadido registro informativo:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indicadores de progreso:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Salida estructurada:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Benchmarking Robusto

**Mejoras en la Sesión 03:**
- Manejo de errores por modelo (continúa en caso de fallo)
- Informes detallados de progreso
- Ejecución adecuada de rondas de calentamiento
- Soporte para medición de latencia del primer token
- Separación clara de etapas

### 6. Indicaciones de Tipo Consistentes

**Añadido en todo el código:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Beneficios:**
- Autocompletado mejorado en IDE
- Detección temprana de errores
- Código auto-documentado

### 7. Enrutador de Modelos Mejorado

**Mejoras en la Sesión 06:**
- Documentación completa de detección de intención
- Explicación del algoritmo de selección de modelos
- Registros detallados de enrutamiento
- Formato de salida de pruebas
- Recuperación de errores en pruebas por lotes

### 8. Orquestación de Múltiples Agentes

**Mejoras en la Sesión 05:**
- Informes de progreso etapa por etapa
- Manejo de errores por agente
- Estructura clara del pipeline
- Documentación mejorada de gestión de memoria

---

## Lista de Verificación de Pruebas

### Requisitos Previos
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Probar Cada Muestra

#### Sesión 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sesión 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sesión 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sesión 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sesión 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sesión 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Referencia de Variables de Entorno

### Global (Todas las Muestras)
| Variable | Descripción | Predeterminado |
|----------|-------------|----------------|
| `FOUNDRY_LOCAL_ALIAS` | Alias del modelo a usar | Varía según la muestra |
| `FOUNDRY_LOCAL_ENDPOINT` | Sobrescribir el endpoint del servicio | Detectado automáticamente |
| `SHOW_USAGE` | Mostrar uso de tokens | `0` |
| `RETRY_ON_FAIL` | Habilitar lógica de reintento | `1` |
| `RETRY_BACKOFF` | Retraso inicial de reintento | `1.0` |

### Específicas de Muestras
| Variable | Usada Por | Descripción |
|----------|-----------|-------------|
| `EMBED_MODEL` | Sesión 02 | Nombre del modelo de embeddings |
| `RAG_QUESTION` | Sesión 02 | Pregunta de prueba para RAG |
| `BENCH_MODELS` | Sesión 03 | Modelos separados por comas para benchmarking |
| `BENCH_ROUNDS` | Sesión 03 | Número de rondas de benchmarking |
| `BENCH_PROMPT` | Sesión 03 | Prompt de prueba para benchmarks |
| `BENCH_STREAM` | Sesión 03 | Medir latencia del primer token |
| `SLM_ALIAS` | Sesión 04 | Modelo de lenguaje pequeño |
| `LLM_ALIAS` | Sesión 04 | Modelo de lenguaje grande |
| `COMPARE_PROMPT` | Sesión 04 | Prompt de prueba para comparación |
| `AGENT_MODEL_PRIMARY` | Sesión 05 | Modelo principal del agente |
| `AGENT_MODEL_EDITOR` | Sesión 05 | Modelo editor del agente |
| `AGENT_QUESTION` | Sesión 05 | Pregunta de prueba para agentes |
| `PIPELINE_TASK` | Sesión 06 | Tarea para el pipeline |

---

## Cambios Importantes

**Ninguno** - Todos los cambios son compatibles hacia atrás.

Los scripts existentes seguirán funcionando. Las nuevas características son:
- Variables de entorno opcionales
- Mensajes de error mejorados (no rompen la funcionalidad)
- Registro adicional (puede ser suprimido)
- Indicaciones de tipo mejoradas (sin impacto en tiempo de ejecución)

---

## Mejores Prácticas Implementadas

### 1. Siempre Usar Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Patrón de Manejo de Errores Adecuado
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Registro Informativo
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Indicaciones de Tipo
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstrings Completos
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Soporte para Variables de Entorno
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Degradación Elegante
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Problemas Comunes y Soluciones

### Problema: Errores de Importación
**Solución:** Instalar dependencias faltantes
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problema: Errores de Conexión
**Solución:** Asegurarse de que Foundry Local esté ejecutándose
```bash
foundry service status
foundry model run phi-4-mini
```

### Problema: Modelo No Encontrado
**Solución:** Verificar modelos disponibles
```bash
foundry model ls
foundry model download <alias>
```

### Problema: Rendimiento Lento
**Solución:** Usar modelos más pequeños o ajustar parámetros
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Próximos Pasos

### 1. Probar Todas las Muestras
Recorrer la lista de verificación de pruebas anterior para verificar que todas las muestras funcionen correctamente.

### 2. Actualizar Documentación
- Actualizar los archivos markdown de las sesiones con nuevos ejemplos
- Añadir sección de solución de problemas al README principal
- Crear una guía de referencia rápida

### 3. Crear Pruebas de Integración
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Añadir Benchmarks de Rendimiento
Rastrear mejoras de rendimiento derivadas de las mejoras en el manejo de errores.

### 5. Retroalimentación del Usuario
Recopilar comentarios de los participantes del taller sobre:
- Claridad de los mensajes de error
- Integridad de la documentación
- Facilidad de uso

---

## Recursos

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referencia Rápida**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Notas de Migración**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Repositorio Principal**: https://github.com/microsoft/Foundry-Local

---

## Mantenimiento

### Añadir Nuevas Muestras
Siga estos patrones al crear nuevas muestras:

1. Usar `workshop_utils` para la gestión del cliente
2. Añadir manejo de errores integral
3. Incluir soporte para variables de entorno
4. Añadir indicaciones de tipo y docstrings
5. Proporcionar registro informativo
6. Incluir ejemplos de uso en el docstring
7. Enlazar a la documentación del SDK

### Revisar Actualizaciones
Al revisar actualizaciones de muestras, verificar:
- [ ] Manejo de errores en todas las operaciones de I/O
- [ ] Indicaciones de tipo en funciones públicas
- [ ] Docstrings completos
- [ ] Documentación de variables de entorno
- [ ] Retroalimentación informativa al usuario
- [ ] Enlaces de referencia al SDK
- [ ] Estilo de código consistente

---

**Resumen**: Todas las muestras de Python del taller ahora siguen las mejores prácticas del SDK Local de Foundry con manejo de errores mejorado, documentación integral y experiencia de usuario optimizada. Sin cambios disruptivos: toda la funcionalidad existente se conserva y mejora.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.