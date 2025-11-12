<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "04951692a100dcd716df01efca2d3f0d",
  "translation_date": "2025-11-11T21:24:15+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "es"
}
-->
# EdgeAI para Principiantes - Taller

> **Ruta de aprendizaje práctico para construir aplicaciones de Edge AI listas para producción**
>
> Domina el despliegue de IA local con Microsoft Foundry Local, desde la primera respuesta de chat hasta la orquestación de múltiples agentes en 6 sesiones progresivas.

---

## 🎯 Introducción

Bienvenido al **Taller de EdgeAI para Principiantes**: tu guía práctica para construir aplicaciones inteligentes que funcionan completamente en hardware local. Este taller transforma conceptos teóricos de Edge AI en habilidades del mundo real a través de ejercicios progresivamente desafiantes utilizando Microsoft Foundry Local y Modelos de Lenguaje Pequeños (SLMs).

### ¿Por qué este taller?

**La revolución de Edge AI está aquí**

Organizaciones de todo el mundo están cambiando de IA dependiente de la nube a computación en el borde por tres razones clave:

1. **Privacidad y Cumplimiento**: Procesa datos sensibles localmente sin transmisión a la nube (HIPAA, GDPR, regulaciones financieras).
2. **Rendimiento**: Elimina la latencia de red (50-500ms local vs 500-2000ms ida y vuelta en la nube).
3. **Control de Costos**: Elimina los costos por token de API y escala sin gastos en la nube.

**Pero Edge AI es diferente**

Ejecutar IA en instalaciones locales requiere nuevas habilidades:
- Selección y optimización de modelos para restricciones de recursos.
- Gestión de servicios locales y aceleración de hardware.
- Ingeniería de prompts para modelos más pequeños.
- Patrones de despliegue en producción para dispositivos en el borde.

**Este taller te proporciona esas habilidades**

En 6 sesiones enfocadas (~3 horas en total), avanzarás desde "Hola Mundo" hasta desplegar sistemas de múltiples agentes listos para producción, todo funcionando localmente en tu máquina.

---

## 📚 Objetivos de Aprendizaje

Al completar este taller, serás capaz de:

### Competencias Clave
1. **Desplegar y Gestionar Servicios de IA Locales**
   - Instalar y configurar Microsoft Foundry Local.
   - Seleccionar modelos apropiados para despliegue en el borde.
   - Gestionar el ciclo de vida de los modelos (descargar, cargar, almacenar en caché).
   - Monitorear el uso de recursos y optimizar el rendimiento.

2. **Construir Aplicaciones Impulsadas por IA**
   - Implementar respuestas de chat compatibles con OpenAI localmente.
   - Diseñar prompts efectivos para Modelos de Lenguaje Pequeños.
   - Manejar respuestas en streaming para una mejor experiencia de usuario.
   - Integrar modelos locales en aplicaciones existentes.

3. **Crear Sistemas RAG (Generación Aumentada por Recuperación)**
   - Construir búsqueda semántica con embeddings.
   - Fundamentar las respuestas de LLM en conocimiento específico del dominio.
   - Evaluar la calidad de RAG con métricas estándar de la industria.
   - Escalar de prototipo a producción.

4. **Optimizar el Rendimiento de Modelos**
   - Evaluar múltiples modelos para tu caso de uso.
   - Medir latencia, rendimiento y tiempo del primer token.
   - Seleccionar modelos óptimos basados en compensaciones de velocidad/calidad.
   - Comparar compensaciones entre SLM y LLM en escenarios reales.

5. **Orquestar Sistemas de Múltiples Agentes**
   - Diseñar agentes especializados para diferentes tareas.
   - Implementar memoria y gestión de contexto de agentes.
   - Coordinar agentes en flujos de trabajo complejos.
   - Enrutar solicitudes inteligentemente entre múltiples modelos.

6. **Desplegar Soluciones Listas para Producción**
   - Implementar manejo de errores y lógica de reintento.
   - Monitorear el uso de tokens y recursos del sistema.
   - Construir arquitecturas escalables con patrones de modelo como herramientas.
   - Planificar rutas de migración del borde a híbrido (borde + nube).

---

## 🎓 Resultados de Aprendizaje

### Lo que construirás

Al final de este taller, habrás creado:

| Sesión | Entregable | Habilidades Demostradas |
|--------|------------|-------------------------|
| **1** | Aplicación de chat con streaming | Configuración del servicio, respuestas básicas, UX en streaming |
| **2** | Sistema RAG con evaluación | Embeddings, búsqueda semántica, métricas de calidad |
| **3** | Suite de evaluación de modelos múltiples | Medición de rendimiento, comparación de modelos |
| **4** | Comparador SLM vs LLM | Análisis de compensaciones, estrategias de optimización |
| **5** | Orquestador de múltiples agentes | Diseño de agentes, gestión de memoria, coordinación |
| **6** | Sistema de enrutamiento inteligente | Detección de intención, selección de modelos, escalabilidad |

### Matriz de Competencias

| Nivel de Habilidad | Sesión 1-2 | Sesión 3-4 | Sesión 5-6 |
|--------------------|------------|------------|------------|
| **Principiante** | ✅ Configuración y conceptos básicos | ⚠️ Desafiante | ❌ Demasiado avanzado |
| **Intermedio** | ✅ Revisión rápida | ✅ Aprendizaje central | ⚠️ Metas ambiciosas |
| **Avanzado** | ✅ Fácil de completar | ✅ Refinamiento | ✅ Patrones de producción |

### Habilidades Preparadas para el Trabajo

**Después de este taller, estarás preparado para:**

✅ **Construir Aplicaciones con Privacidad**
- Aplicaciones de salud que manejan PHI/PII localmente.
- Servicios financieros con requisitos de cumplimiento.
- Sistemas gubernamentales con necesidades de soberanía de datos.

✅ **Optimizar para Entornos en el Borde**
- Dispositivos IoT con recursos limitados.
- Aplicaciones móviles con enfoque offline.
- Sistemas en tiempo real de baja latencia.

✅ **Diseñar Arquitecturas Inteligentes**
- Sistemas de múltiples agentes para flujos de trabajo complejos.
- Despliegues híbridos borde-nube.
- Infraestructura de IA optimizada en costos.

✅ **Liderar Iniciativas de Edge AI**
- Evaluar la viabilidad de Edge AI para proyectos.
- Seleccionar modelos y frameworks apropiados.
- Arquitectar soluciones de IA locales escalables.

---

## 🗺️ Estructura del Taller

### Resumen de las Sesiones (6 Sesiones × 30 Minutos = 3 Horas)

| Sesión | Tema | Enfoque | Duración |
|-------|------|---------|----------|
| **1** | Introducción a Foundry Local | Instalación, validación, primeras respuestas | 30 min |
| **2** | Construcción de Soluciones de IA con RAG | Ingeniería de prompts, embeddings, evaluación | 30 min |
| **3** | Modelos de Código Abierto | Descubrimiento de modelos, evaluación, selección | 30 min |
| **4** | Modelos de Última Generación | SLM vs LLM, optimización, frameworks | 30 min |
| **5** | Agentes Impulsados por IA | Diseño de agentes, orquestación, memoria | 30 min |
| **6** | Modelos como Herramientas | Enrutamiento, encadenamiento, estrategias de escalabilidad | 30 min |

---

## 🚀 Inicio Rápido

### Requisitos Previos

**Requisitos del Sistema:**
- **OS**: Windows 10/11, macOS 11+ o Linux (Ubuntu 20.04+).
- **RAM**: Mínimo 8GB, recomendado 16GB+.
- **Almacenamiento**: 10GB+ de espacio libre para modelos.
- **CPU**: Procesador moderno con soporte AVX2.
- **GPU** (opcional): Compatible con CUDA o Qualcomm NPU para aceleración.

**Requisitos de Software:**
- **Python 3.8+** ([Descargar](https://www.python.org/downloads/)).
- **Microsoft Foundry Local** ([Guía de Instalación](../../../Workshop)).
- **Git** ([Descargar](https://git-scm.com/downloads)).
- **Visual Studio Code** (recomendado) ([Descargar](https://code.visualstudio.com/)).

### Configuración en 3 Pasos

#### 1. Instalar Foundry Local

**Windows:**
```powershell
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
foundry service status
```

**Asegúrate de que Azure AI Foundry Local esté funcionando con un puerto fijo**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verificar que funciona:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Encontrar Modelos Disponibles**
Para ver qué modelos están disponibles en tu instancia de Foundry Local, puedes consultar el endpoint de modelos:

```bash
# cmd/bash/powershell
foundry model list
```

Usando el Endpoint Web 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Clonar el Repositorio e Instalar Dependencias

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Ejecutar tu Primer Ejemplo

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ ¡Éxito!** Deberías ver una respuesta en streaming sobre Edge AI.

---

## 📦 Recursos del Taller

### Ejemplos en Python

Ejemplos prácticos progresivos que demuestran cada concepto:

| Sesión | Ejemplo | Descripción | Tiempo de Ejecución |
|--------|---------|-------------|----------------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Chat básico y en streaming | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG con embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Evaluación de calidad RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Evaluación de modelos múltiples | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Comparación SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sistema de múltiples agentes | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Enrutamiento basado en intención | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Pipeline de múltiples pasos | ~60s |

### Jupyter Notebooks

Exploración interactiva con explicaciones y visualizaciones:

| Sesión | Notebook | Descripción | Dificultad |
|--------|----------|-------------|------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Conceptos básicos de chat y streaming | ⭐ Principiante |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Construir sistema RAG | ⭐⭐ Intermedio |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluar calidad de RAG | ⭐⭐ Intermedio |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Evaluación de modelos | ⭐⭐ Intermedio |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Comparación de modelos | ⭐⭐ Intermedio |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orquestación de agentes | ⭐⭐⭐ Avanzado |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Enrutamiento por intención | ⭐⭐⭐ Avanzado |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orquestación de pipeline | ⭐⭐⭐ Avanzado |

### Documentación

Guías y referencias completas:

| Documento | Descripción | Usar Cuando |
|-----------|-------------|-------------|
| [QUICK_START.md](./QUICK_START.md) | Guía de configuración rápida | Comenzando desde cero |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Hoja de trucos de comandos y API | Necesitas respuestas rápidas |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Patrones y ejemplos de SDK | Escribiendo código |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Guía de variables de entorno | Configurando ejemplos |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Problemas comunes y soluciones | Solucionando problemas |

---

## 🎓 Recomendaciones de Ruta de Aprendizaje

### Para Principiantes (3-4 horas)
1. ✅ Sesión 1: Introducción (enfócate en la configuración y chat básico).
2. ✅ Sesión 2: Conceptos básicos de RAG (omite la evaluación inicialmente).
3. ✅ Sesión 3: Evaluación simple (solo 2 modelos).
4. ⏭️ Omite las Sesiones 4-6 por ahora.
5. 🔄 Regresa a las Sesiones 4-6 después de construir tu primera aplicación.

### Para Desarrolladores Intermedios (3 horas)
1. ⚡ Sesión 1: Validación rápida de configuración.
2. ✅ Sesión 2: Completa el pipeline RAG con evaluación.
3. ✅ Sesión 3: Suite completa de evaluación.
4. ✅ Sesión 4: Optimización de modelos.
5. ✅ Sesiones 5-6: Enfócate en patrones de arquitectura.

### Para Practicantes Avanzados (2-3 horas)
1. ⚡ Sesiones 1-3: Revisión rápida y validación.
2. ✅ Sesión 4: Profundización en optimización.
3. ✅ Sesión 5: Arquitectura de múltiples agentes.
4. ✅ Sesión 6: Patrones de producción y escalabilidad.
5. 🚀 Extiende: Construye lógica de enrutamiento personalizada y despliegues híbridos.

---

## Paquete de Sesiones del Taller (Laboratorios Enfocados de 30 Minutos)

Si estás siguiendo el formato condensado de taller de 6 sesiones, utiliza estas guías dedicadas (cada una se relaciona y complementa los módulos más amplios mencionados arriba):

| Sesión del Taller | Guía | Enfoque Principal |
|-------------------|------|-------------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalación, validación, ejecución phi & GPT-OSS-20B, aceleración |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Ingeniería de prompts, patrones RAG, grounding con CSV y documentos, migración |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integración con Hugging Face, evaluación, selección de modelos |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, aceleración ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Roles de agentes, memoria, herramientas, orquestación |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Enrutamiento, encadenamiento, escalado hacia Azure |

Cada archivo de sesión incluye: resumen, objetivos de aprendizaje, flujo de demostración de 30 minutos, proyecto inicial, lista de verificación de validación, solución de problemas y referencias al SDK oficial de Foundry Local Python.

### Scripts de Ejemplo

Instalar dependencias del taller (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Si ejecutas el servicio Foundry Local en una máquina o VM diferente (Windows) desde macOS, exporta el endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sesión | Script(s) | Descripción |
|--------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Servicio inicial y chat en streaming |
| 2 | `samples/session02/rag_pipeline.py` | RAG mínimo (embeddings en memoria) |
|   | `samples/session02/rag_eval_ragas.py` | Evaluación de RAG con métricas de ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Evaluación de latencia y rendimiento de múltiples modelos |
| 4 | `samples/session04/model_compare.py` | Comparación SLM vs LLM (latencia y salida de muestra) |
| 5 | `samples/session05/agents_orchestrator.py` | Investigación de dos agentes → pipeline editorial |
| 6 | `samples/session06/models_router.py` | Demostración de enrutamiento basado en intención |
|   | `samples/session06/models_pipeline.py` | Cadena de planificación/ejecución/refinamiento en múltiples pasos |

### Variables de Entorno (Comunes en los Ejemplos)

| Variable | Propósito | Ejemplo |
|----------|-----------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias de modelo único predeterminado para ejemplos básicos | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM explícito vs modelo más grande para comparación | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Lista de alias para evaluación | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Repeticiones de evaluación por modelo | `3` |
| `BENCH_PROMPT` | Prompt utilizado en la evaluación | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Modelo de embeddings de sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Consulta de prueba para el pipeline RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Consulta para el pipeline de agentes | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias del modelo para el agente de investigación | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias del modelo para el agente editor (puede ser diferente) | `gpt-oss-20b` |
| `SHOW_USAGE` | Cuando es `1`, imprime el uso de tokens por cada respuesta | `1` |
| `RETRY_ON_FAIL` | Cuando es `1`, reintenta una vez en caso de errores transitorios en el chat | `1` |
| `RETRY_BACKOFF` | Segundos de espera antes de reintentar | `1.0` |

Si una variable no está configurada, los scripts recurren a valores predeterminados razonables. Para demostraciones de un solo modelo, normalmente solo necesitas `FOUNDRY_LOCAL_ALIAS`.

### Módulo de Utilidad

Todos los ejemplos ahora comparten un archivo auxiliar `samples/workshop_utils.py` que proporciona:

* Creación en caché de `FoundryLocalManager` + cliente OpenAI
* Función auxiliar `chat_once()` con opción de reintento + impresión de uso
* Informes simples de uso de tokens (habilitar con `SHOW_USAGE=1`)

Esto reduce la duplicación y destaca las mejores prácticas para una orquestación eficiente de modelos locales.

## Mejoras Opcionales (Entre Sesiones)

| Tema | Mejora | Sesiones | Entorno / Alternador |
|------|--------|----------|-----------------------|
| Determinismo | Temperatura fija + conjuntos de prompts estables | 1–6 | Configurar `temperature=0`, `top_p=1` |
| Visibilidad del Uso de Tokens | Enseñanza consistente de costos/eficiencia | 1–6 | `SHOW_USAGE=1` |
| Primer Token en Streaming | Métrica de latencia percibida | 1,3,4,6 | `BENCH_STREAM=1` (evaluación) |
| Resiliencia de Reintento | Maneja arranques en frío transitorios | Todas | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Agentes Multi-Modelo | Especialización de roles heterogéneos | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Enrutamiento Adaptativo | Heurísticas de intención + costo | 6 | Extender el enrutador con lógica de escalamiento |
| Memoria Vectorial | Recuperación semántica a largo plazo | 2,5,6 | Integrar índice de embeddings FAISS/Chroma |
| Exportación de Trazas | Auditoría y evaluación | 2,5,6 | Agregar líneas JSON por paso |
| Rúbricas de Calidad | Seguimiento cualitativo | 3–6 | Prompts de puntuación secundaria |
| Pruebas de Validación | Validación rápida previa al taller | Todas | `python Workshop/tests/smoke.py` |

### Inicio Rápido Determinista

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Espera conteos de tokens estables en entradas idénticas repetidas.

### Evaluación de RAG (Sesión 2)

Usa `rag_eval_ragas.py` para calcular relevancia de respuestas, fidelidad y precisión de contexto en un pequeño conjunto de datos sintético:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Amplía suministrando un JSONL más grande de preguntas, contextos y verdades base, luego conviértelo en un `Dataset` de Hugging Face.

## Apéndice de Precisión de Comandos CLI

El taller utiliza deliberadamente solo comandos CLI documentados/estables de Foundry Local.

### Comandos Estables Referenciados

| Categoría | Comando | Propósito |
|-----------|---------|----------|
| Núcleo | `foundry --version` | Mostrar versión instalada |
| Servicio | `foundry service start` | Iniciar servicio local (si no es automático) |
| Servicio | `foundry service status` | Mostrar estado del servicio |
| Modelos | `foundry model list` | Listar catálogo/modelos disponibles |
| Modelos | `foundry model download <alias>` | Descargar pesos del modelo en caché |
| Modelos | `foundry model run <alias>` | Ejecutar (cargar) un modelo localmente; combinar con `--prompt` para una sola ejecución |
| Modelos | `foundry model unload <alias>` / `foundry model stop <alias>` | Descargar un modelo de la memoria (si es compatible) |
| Caché | `foundry cache list` | Listar modelos en caché (descargados) |

### Patrón de Prompt de Una Sola Ejecución

En lugar del comando `model chat` obsoleto, usa:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Esto ejecuta un ciclo de prompt/respuesta único y luego se cierra.

### Patrones Eliminados/Evitados

| Obsoleto/No Documentado | Reemplazo/Guía |
|--------------------------|---------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Usa `foundry model list` + actividad reciente/registros |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Usa script de evaluación Python + herramientas del sistema (Administrador de Tareas / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Evaluación y Telemetría

- Latencia, p95, tokens/segundo: `samples/session03/benchmark_oss_models.py`
- Latencia del primer token (streaming): configurar `BENCH_STREAM=1`
- Uso de recursos: monitores del sistema (Administrador de Tareas, Activity Monitor, `nvidia-smi`).

A medida que se estabilicen nuevos comandos de telemetría CLI, se podrán incorporar con ediciones mínimas a los archivos markdown de las sesiones.

### Control Automático de Estilo

Un linter automatizado previene la reintroducción de patrones CLI obsoletos dentro de bloques de código en archivos markdown:

Script: `Workshop/scripts/lint_markdown_cli.py`

Los patrones obsoletos están bloqueados dentro de bloques de código.

Reemplazos recomendados:
| Obsoleto | Reemplazo |
|----------|-----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Script de evaluación + herramientas del sistema |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Ejecutar localmente:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

Acción de GitHub: `.github/workflows/markdown-cli-lint.yml` se ejecuta en cada push y PR.

Hook opcional de pre-commit:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Tabla Rápida de Migración CLI → SDK

| Tarea | Comando CLI | Equivalente SDK (Python) | Notas |
|-------|-------------|--------------------------|-------|
| Ejecutar un modelo una vez (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | El SDK inicia automáticamente el servicio y la caché |
| Descargar (caché) modelo | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | El administrador elige la mejor variante si el alias se asigna a múltiples versiones |
| Listar catálogo | `foundry model list` | `# usar manager para cada alias o mantener lista conocida` | El CLI agrega; el SDK actualmente instancia por alias |
| Listar modelos en caché | `foundry cache list` | `manager.list_cached_models()` | Después de iniciar el administrador (cualquier alias) |
| Obtener URL del endpoint | (implícito) | `manager.endpoint` | Usado para crear un cliente compatible con OpenAI |
| Calentar un modelo | `foundry model run <alias>` luego primer prompt | `chat_once(alias, messages=[...])` (utilidad) | Las utilidades manejan el calentamiento inicial de latencia en frío |
| Medir latencia | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (o nuevo script exportador) | Preferir script para métricas consistentes |
| Detener/descargar modelo | `foundry model unload <alias>` | (No expuesto – reiniciar servicio/proceso) | Normalmente no es necesario para el flujo del taller |
| Recuperar uso de tokens | (ver salida) | `resp.usage.total_tokens` | Proporcionado si el backend devuelve un objeto de uso |

## Exportación de Evaluación en Markdown

Usa el script `Workshop/scripts/export_benchmark_markdown.py` para ejecutar una nueva evaluación (misma lógica que `samples/session03/benchmark_oss_models.py`) y generar una tabla Markdown amigable para GitHub más un JSON sin procesar.

### Ejemplo

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Archivos generados:
| Archivo | Contenido |
|---------|-----------|
| `benchmark_report.md` | Tabla Markdown + sugerencias de interpretación |
| `benchmark_report.json` | Array de métricas sin procesar (para comparación/seguimiento de tendencias) |

Configura `BENCH_STREAM=1` en el entorno para incluir latencia del primer token si es compatible.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->