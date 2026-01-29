# Sesión 3: Modelos de Código Abierto en Foundry Local

## Resumen

Descubre cómo integrar modelos de Hugging Face y otros de código abierto en Foundry Local. Aprende estrategias de selección, flujos de contribución comunitaria, metodología de comparación de rendimiento y cómo extender Foundry con registros personalizados de modelos. Esta sesión se alinea con los temas de exploración semanales de "Model Mondays" y te prepara para evaluar y operacionalizar modelos de código abierto localmente antes de escalar a Azure.

## Objetivos de Aprendizaje

Al finalizar, serás capaz de:

- **Descubrir y Evaluar**: Identificar modelos candidatos (mistral, gemma, qwen, deepseek) utilizando el equilibrio entre calidad y recursos.
- **Cargar y Ejecutar**: Usar Foundry Local CLI para descargar, almacenar en caché y lanzar modelos comunitarios.
- **Evaluar Rendimiento**: Aplicar heurísticas consistentes de latencia + rendimiento de tokens + calidad.
- **Extender**: Registrar o adaptar un envoltorio de modelo personalizado siguiendo patrones compatibles con el SDK.
- **Comparar**: Generar comparaciones estructuradas para decisiones de selección entre SLM y LLM de tamaño medio.

## Prerrequisitos

- Haber completado las sesiones 1 y 2
- Entorno Python con `foundry-local-sdk` instalado
- Al menos 15GB de espacio libre en disco para múltiples cachés de modelos

### Inicio Rápido en Entornos Multiplataforma

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

Al realizar evaluaciones de rendimiento desde macOS contra un servicio host en Windows, configura:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Flujo de Demostración (30 min)

### 1. Cargar Modelos de Hugging Face mediante CLI (8 min)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Ejecutar y Realizar una Prueba Rápida (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Script de Evaluación de Rendimiento (8 min)

Crea `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Ejecuta:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Comparar Rendimiento (5 min)

Discute los compromisos: tiempo de carga, uso de memoria (observa el Administrador de Tareas / `nvidia-smi` / monitor de recursos del sistema operativo), calidad de salida frente a velocidad. Usa el script de evaluación de rendimiento en Python (Sesión 3) para medir latencia y rendimiento; repite después de habilitar la aceleración GPU.

### 5. Proyecto Inicial (4 min)

Crea un generador de informes de comparación de modelos (extiende el script de evaluación de rendimiento con exportación en formato markdown).

## Proyecto Inicial: Extender `03-huggingface-models`

Mejora el ejemplo existente mediante:

1. Agregar agregación de evaluaciones de rendimiento + salida en formato CSV/Markdown.
2. Implementar puntuación cualitativa simple (conjunto de pares de prompts + archivo de anotación manual).
3. Introducir una configuración JSON (`models.json`) para una lista de modelos y conjunto de prompts personalizables.

## Lista de Verificación de Validación

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Todos los modelos objetivo deben aparecer y responder a una solicitud de chat de prueba.

## Escenario de Ejemplo y Mapeo del Taller

| Script del Taller | Escenario | Objetivo | Fuente de Prompt / Dataset |
|-------------------|-----------|----------|----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Equipo de plataforma Edge seleccionando SLM predeterminado para un resumidor integrado | Generar comparación de latencia + p95 + tokens/segundo entre modelos candidatos | Variable `PROMPT` en línea + lista `BENCH_MODELS` en el entorno |

### Narrativa del Escenario

El equipo de ingeniería de producto debe elegir un modelo de resumen ligero predeterminado para una función de notas de reuniones offline. Realizan evaluaciones de rendimiento controladas y deterministas (temperature=0) en un conjunto fijo de prompts (ver ejemplo abajo) y recopilan métricas de latencia y rendimiento con y sin aceleración GPU.

### Ejemplo de Conjunto de Prompts en JSON (expandible)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Itera cada prompt por modelo, captura la latencia por prompt para derivar métricas de distribución y detectar valores atípicos.

## Marco de Selección de Modelos

| Dimensión | Métrica | Por qué es importante |
|-----------|---------|-----------------------|
| Latencia | promedio / p95 | Consistencia en la experiencia del usuario |
| Rendimiento | tokens/segundo | Escalabilidad en lotes y streaming |
| Memoria | tamaño residente | Ajuste al dispositivo y concurrencia |
| Calidad | prompts de evaluación | Adecuación a la tarea |
| Huella | caché en disco | Distribución y actualizaciones |
| Licencia | permiso de uso | Cumplimiento comercial |

## Extender con un Modelo Personalizado

Patrón de alto nivel (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Consulta el repositorio oficial para interfaces de adaptadores en evolución:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Solución de Problemas

| Problema | Causa | Solución |
|----------|-------|----------|
| OOM en mistral-7b | RAM/GPU insuficiente | Detén otros modelos; prueba una variante más pequeña |
| Respuesta inicial lenta | Carga en frío | Mantén activo con un prompt ligero periódico |
| Descarga se detiene | Inestabilidad de red | Reintenta; predescarga en horarios de baja actividad |

## Referencias

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Descubrimiento de Modelos en Hugging Face: https://huggingface.co/models

---

**Duración de la Sesión**: 30 min (+ inmersión opcional)  
**Dificultad**: Intermedia

### Mejoras Opcionales

| Mejora | Beneficio | Cómo |
|--------|-----------|------|
| Latencia del Primer Token en Streaming | Mide la percepción de respuesta | Ejecuta evaluación con `BENCH_STREAM=1` (script mejorado en `Workshop/samples/session03`) |
| Modo Determinista | Comparaciones de regresión estables | `temperature=0`, conjunto de prompts fijo, captura salidas JSON bajo control de versiones |
| Puntuación con Rubrica de Calidad | Añade dimensión cualitativa | Mantén `prompts.json` con facetas esperadas; anota puntuaciones (1–5) manualmente o mediante un modelo secundario |
| Exportación en CSV / Markdown | Informe compartible | Extiende el script para escribir `benchmark_report.md` con tabla y destacados |
| Etiquetas de Capacidades de Modelos | Ayuda en el enrutamiento automatizado posterior | Mantén `models.json` con `{alias: {capabilities:[], size_mb:..}}` |
| Fase de Calentamiento de Caché | Reduce sesgo de inicio en frío | Ejecuta una ronda inicial antes del bucle de tiempo (ya implementado) |
| Precisión Percentil | Latencia robusta en extremos | Usa percentil de numpy (ya en el script refactorizado) |
| Aproximación de Costo por Token | Comparación económica | Costo aprox = (tokens/seg * promedio de tokens por solicitud) * heurística de energía |
| Saltar Automáticamente Modelos Fallidos | Resiliencia en ejecuciones por lotes | Envuelve cada evaluación en try/except y marca el campo de estado |

#### Fragmento Mínimo de Exportación en Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Ejemplo de Conjunto de Prompts Determinista

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Itera la lista estática en lugar de prompts aleatorios para métricas comparables entre commits.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->