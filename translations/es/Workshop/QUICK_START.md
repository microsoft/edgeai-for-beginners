# Guía Rápida del Taller

## Requisitos Previos

### 1. Instalar Foundry Local

Sigue la guía oficial de instalación:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Instalar Dependencias de Python

Desde el directorio del Taller:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Ejecución de Ejemplos del Taller

### Sesión 01: Chat Básico

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Variables de Entorno:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sesión 02: Pipeline RAG

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Variables de Entorno:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sesión 02: Evaluación RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Nota**: Requiere dependencias adicionales instaladas mediante `requirements.txt`

### Sesión 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Variables de Entorno:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Salida**: JSON con métricas de latencia, rendimiento y primer token

### Sesión 04: Comparación de Modelos

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Variables de Entorno:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sesión 05: Orquestación Multi-Agente

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Variables de Entorno:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sesión 06: Enrutador de Modelos

```bash
cd Workshop/samples
python -m session06.models_router
```

**Prueba lógica de enrutamiento** con múltiples intenciones (código, resumen, clasificación)

### Sesión 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Pipeline complejo de múltiples pasos** con planificación, ejecución y refinamiento

## Scripts

### Exportar Informe de Benchmark

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Salida**: Tabla en Markdown + métricas en JSON

### Lint de Patrones CLI en Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Propósito**: Detectar patrones CLI obsoletos en la documentación

## Pruebas

### Pruebas Básicas

```bash
cd Workshop
python -m tests.smoke
```

**Pruebas**: Funcionalidad básica de ejemplos clave

## Solución de Problemas

### Servicio No Funciona

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Errores de Importación de Módulos

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Errores de Conexión

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modelo No Encontrado

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referencia de Variables de Entorno

### Configuración Principal
| Variable | Predeterminado | Descripción |
|----------|----------------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Varía | Alias del modelo a usar |
| `FOUNDRY_LOCAL_ENDPOINT` | Automático | Sobrescribir el endpoint del servicio |
| `SHOW_USAGE` | `0` | Mostrar estadísticas de uso de tokens |
| `RETRY_ON_FAIL` | `1` | Habilitar lógica de reintento |
| `RETRY_BACKOFF` | `1.0` | Retraso inicial de reintento (segundos) |

### Específico de Sesión
| Variable | Predeterminado | Descripción |
|----------|----------------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Modelo de embeddings |
| `RAG_QUESTION` | Ver ejemplo | Pregunta de prueba RAG |
| `BENCH_MODELS` | Varía | Modelos separados por comas |
| `BENCH_ROUNDS` | `3` | Iteraciones de benchmark |
| `BENCH_PROMPT` | Ver ejemplo | Prompt de benchmark |
| `BENCH_STREAM` | `0` | Medir latencia del primer token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modelo principal del agente |
| `AGENT_MODEL_EDITOR` | Principal | Modelo editor del agente |
| `SLM_ALIAS` | `phi-4-mini` | Modelo de lenguaje pequeño |
| `LLM_ALIAS` | `qwen2.5-7b` | Modelo de lenguaje grande |
| `COMPARE_PROMPT` | Ver ejemplo | Prompt de comparación |

## Modelos Recomendados

### Desarrollo y Pruebas
- **phi-4-mini** - Calidad y velocidad equilibradas
- **qwen2.5-0.5b** - Muy rápido para clasificación
- **gemma-2-2b** - Buena calidad, velocidad moderada

### Escenarios de Producción
- **phi-4-mini** - Propósito general
- **deepseek-coder-1.3b** - Generación de código
- **qwen2.5-7b** - Respuestas de alta calidad

## Documentación del SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Obtener Ayuda

1. Verifica el estado del servicio: `foundry service status`  
2. Revisa los registros: Consulta los registros del servicio Foundry Local  
3. Consulta la documentación del SDK: https://github.com/microsoft/Foundry-Local  
4. Revisa el código de ejemplo: Todos los ejemplos tienen docstrings detallados  

## Próximos Pasos

1. Completa todas las sesiones del taller en orden  
2. Experimenta con diferentes modelos  
3. Modifica los ejemplos para tus casos de uso  

---

**Última Actualización**: 2025-01-08  
**Versión del Taller**: Última  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->