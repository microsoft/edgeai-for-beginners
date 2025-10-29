<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:08:15+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "es"
}
-->
# Notas de Migración del SDK Local de Foundry

## Resumen

Todos los archivos Python en la carpeta Workshop han sido actualizados para seguir los últimos patrones del [SDK Local de Python de Foundry](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Resumen de Cambios

### Infraestructura Principal (`workshop_utils.py`)

#### Funcionalidades Mejoradas:
- **Soporte para Sobrescribir Endpoint**: Se agregó soporte para la variable de entorno `FOUNDRY_LOCAL_ENDPOINT`
- **Manejo de Errores Mejorado**: Mejor manejo de excepciones con mensajes de error detallados
- **Caché Mejorado**: Las claves de caché ahora incluyen el endpoint para escenarios con múltiples endpoints
- **Retroceso Exponencial**: La lógica de reintento ahora utiliza retroceso exponencial para mayor confiabilidad
- **Anotaciones de Tipos**: Se añadieron sugerencias de tipos completas para mejor soporte en IDEs

#### Nuevas Capacidades:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Aplicaciones de Ejemplo

#### Sesión 01: Inicio de Chat (`chat_bootstrap.py`)
- Modelo predeterminado actualizado de `phi-3.5-mini` a `phi-4-mini`
- Se agregó soporte para sobrescribir el endpoint
- Documentación mejorada con referencias al SDK

#### Sesión 02: Pipeline RAG (`rag_pipeline.py`)
- Actualizado para usar `phi-4-mini` como predeterminado
- Se agregó soporte para sobrescribir el endpoint
- Documentación mejorada con detalles sobre variables de entorno

#### Sesión 02: Evaluación RAG (`rag_eval_ragas.py`)
- Modelos predeterminados actualizados
- Configuración de endpoint añadida
- Manejo de errores mejorado

#### Sesión 03: Benchmarking (`benchmark_oss_models.py`)
- Lista de modelos predeterminados actualizada para incluir `phi-4-mini`
- Documentación completa sobre variables de entorno añadida
- Documentación de funciones mejorada
- Soporte para sobrescribir el endpoint añadido

#### Sesión 04: Comparación de Modelos (`model_compare.py`)
- LLM predeterminado actualizado de `gpt-oss-20b` a `qwen2.5-7b`
- Configuración de endpoint añadida
- Documentación mejorada

#### Sesión 05: Orquestación Multi-Agente (`agents_orchestrator.py`)
- Se añadieron sugerencias de tipos (cambiado de `str | None` a `Optional[str]`)
- Documentación de la clase Agent mejorada
- Soporte para sobrescribir el endpoint añadido
- Patrón de inicialización mejorado

#### Sesión 06: Enrutador de Modelos (`models_router.py`)
- Configuración de endpoint añadida
- Documentación mejorada sobre detección de intención
- Documentación de lógica de enrutamiento mejorada

#### Sesión 06: Pipeline (`models_pipeline.py`)
- Documentación completa de funciones añadida
- Documentación paso a paso mejorada
- Manejo de errores mejorado

### Scripts

#### Exportación de Benchmark (`export_benchmark_markdown.py`)
- Soporte para sobrescribir el endpoint añadido
- Modelos predeterminados actualizados
- Documentación de funciones mejorada
- Manejo de errores mejorado

#### Linter CLI (`lint_markdown_cli.py`)
- Enlaces de referencia al SDK añadidos
- Documentación de uso mejorada

### Pruebas

#### Pruebas de Humo (`smoke.py`)
- Soporte para sobrescribir el endpoint añadido
- Documentación mejorada
- Documentación de casos de prueba mejorada
- Reporte de errores mejorado

## Variables de Entorno

Todos los ejemplos ahora soportan estas variables de entorno:

### Configuración Principal
- `FOUNDRY_LOCAL_ALIAS` - Alias del modelo a usar (predeterminado varía según el ejemplo)
- `FOUNDRY_LOCAL_ENDPOINT` - Sobrescribir el endpoint del servicio (opcional)
- `SHOW_USAGE` - Mostrar estadísticas de uso de tokens (predeterminado: "0")
- `RETRY_ON_FAIL` - Habilitar lógica de reintento (predeterminado: "1")
- `RETRY_BACKOFF` - Retraso inicial de reintento en segundos (predeterminado: "1.0")

### Específicas de Ejemplo
- `EMBED_MODEL` - Modelo de embeddings para ejemplos RAG
- `BENCH_MODELS` - Modelos separados por comas para benchmarking
- `BENCH_ROUNDS` - Número de rondas de benchmarking
- `BENCH_PROMPT` - Prompt de prueba para benchmarks
- `BENCH_STREAM` - Medir latencia del primer token
- `RAG_QUESTION` - Pregunta de prueba para ejemplos RAG
- `AGENT_MODEL_PRIMARY` - Modelo principal del agente
- `AGENT_MODEL_EDITOR` - Modelo editor del agente
- `SLM_ALIAS` - Alias de modelo de lenguaje pequeño
- `LLM_ALIAS` - Alias de modelo de lenguaje grande

## Mejores Prácticas del SDK Implementadas

### 1. Inicialización Correcta del Cliente
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Recuperación de Información del Modelo
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Manejo de Errores
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Lógica de Reintento con Retroceso Exponencial
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Soporte para Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Guía de Migración para Ejemplos Personalizados

Si estás creando nuevos ejemplos o actualizando los existentes:

1. **Usa los ayudantes de `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Soporta sobrescribir el endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Añade documentación completa**:
   - Variables de entorno en el docstring
   - Enlace de referencia al SDK
   - Ejemplos de uso

4. **Usa sugerencias de tipos**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementa un manejo de errores adecuado**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Pruebas

Todos los ejemplos pueden ser probados con:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## Referencias de Documentación del SDK

- **Repositorio Principal**: https://github.com/microsoft/Foundry-Local
- **SDK de Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentación de API**: Consulta el repositorio del SDK para la documentación más reciente

## Cambios Importantes

### No se Esperan
Todos los cambios son compatibles hacia atrás. Las actualizaciones principalmente:
- Añaden nuevas características opcionales (sobrescribir endpoint)
- Mejoran el manejo de errores
- Mejoran la documentación
- Actualizan los nombres de modelos predeterminados según las recomendaciones actuales

### Mejoras Opcionales
Es posible que desees actualizar tu código para usar:
- `FOUNDRY_LOCAL_ENDPOINT` para control explícito del endpoint
- `SHOW_USAGE=1` para visibilidad del uso de tokens
- Modelos predeterminados actualizados (`phi-4-mini` en lugar de `phi-3.5-mini`)

## Problemas Comunes y Soluciones

### Problema: "Falló la inicialización del cliente"
**Solución**: Asegúrate de que el servicio Foundry Local esté ejecutándose:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problema: "Modelo no encontrado"
**Solución**: Verifica los modelos disponibles:
```bash
foundry model list
```

### Problema: Errores de conexión al endpoint
**Solución**: Verifica el endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Próximos Pasos

1. **Actualizar ejemplos de Module08**: Aplicar patrones similares a Module08/samples
2. **Añadir pruebas de integración**: Crear un conjunto de pruebas completo
3. **Benchmarking de rendimiento**: Comparar el rendimiento antes y después
4. **Actualizaciones de documentación**: Actualizar el README principal con los nuevos patrones

## Directrices para Contribuciones

Al añadir nuevos ejemplos:
1. Usa `workshop_utils.py` para consistencia
2. Sigue el patrón de los ejemplos existentes
3. Añade docstrings completos
4. Incluye enlaces de referencia al SDK
5. Soporta sobrescribir el endpoint
6. Añade sugerencias de tipos adecuadas
7. Incluye ejemplos de uso en el docstring

## Compatibilidad de Versiones

Estas actualizaciones son compatibles con:
- `foundry-local-sdk` (última versión)
- `openai>=1.30.0`
- Python 3.8+

---

**Última Actualización**: 08-01-2025  
**Responsable**: Equipo EdgeAI Workshop  
**Versión del SDK**: Foundry Local SDK (última 0.7.117+67073234e7)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.