# Sesión 6: Foundry Local – Modelos como Herramientas

## Resumen

Trata los modelos como herramientas componibles dentro de una capa operativa de IA local. Esta sesión muestra cómo encadenar múltiples llamadas especializadas a SLM/LLM, enrutar tareas de manera selectiva y exponer una superficie unificada de SDK a las aplicaciones. Construirás un enrutador de modelos ligero + planificador de tareas, lo integrarás en un script de aplicación y delinearás el camino de escalado hacia Azure AI Foundry para cargas de trabajo en producción.

## Objetivos de Aprendizaje

- **Conceptualizar** los modelos como herramientas atómicas con capacidades declaradas
- **Enrutar** solicitudes basadas en intención/puntuación heurística
- **Encadenar** salidas a través de tareas de múltiples pasos (descomponer → resolver → refinar)
- **Integrar** una API de cliente unificada para aplicaciones posteriores
- **Escalar** el diseño a la nube (mismo contrato compatible con OpenAI)

## Prerrequisitos

- Haber completado las sesiones 1–5
- Tener múltiples modelos locales almacenados en caché (por ejemplo, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Fragmento de Entorno Multiplataforma

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Acceso remoto/VM desde macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Flujo de Demostración (30 min)

### 1. Declaración de Capacidades de Herramientas (5 min)

Crear `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Detección de Intención y Enrutamiento (8 min)

Crear `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Encadenamiento de Tareas de Múltiples Pasos (7 min)

Crear `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Proyecto Inicial: Adaptar `06-models-as-tools` (5 min)

Mejoras:
- Agregar soporte para transmisión de tokens (actualización progresiva de la interfaz)
- Agregar puntuación de confianza: superposición léxica o rúbrica de indicaciones
- Exportar JSON de trazas (intención → modelo → latencia → uso de tokens)
- Implementar reutilización de caché para subpasos repetidos

### 5. Camino de Escalado hacia Azure (5 min)

| Capa | Local (Foundry) | Nube (Azure AI Foundry) | Estrategia de Transición |
|------|-----------------|-------------------------|--------------------------|
| Enrutamiento | Python heurístico | Microservicio duradero | Contenerizar y desplegar API |
| Modelos | SLMs almacenados en caché | Despliegues gestionados | Mapear nombres locales a IDs de despliegue |
| Observabilidad | Estadísticas CLI/manual | Registro centralizado y métricas | Agregar eventos de trazas estructuradas |
| Seguridad | Solo host local | Autenticación/redes de Azure | Introducir Key Vault para secretos |
| Costos | Recursos del dispositivo | Facturación por consumo | Agregar límites presupuestarios |

## Lista de Verificación de Validación

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Esperar selección de modelo basada en intención y salida final refinada.

## Resolución de Problemas

| Problema | Causa | Solución |
|----------|-------|----------|
| Todas las tareas se enrutan al mismo modelo | Reglas débiles | Enriquecer el conjunto de regex INTENT_RULES |
| La tubería falla a mitad de paso | Modelo no cargado | Ejecutar `foundry model run <model>` |
| Baja cohesión en la salida | Sin fase de refinamiento | Agregar paso de resumen/validación |

## Referencias

- SDK de Foundry Local: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentación de Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Patrones de Calidad de Indicaciones: Ver Sesión 2

---

**Duración de la Sesión**: 30 min  
**Dificultad**: Experto

## Escenario de Ejemplo y Mapeo del Taller

| Scripts / Notebooks del Taller | Escenario | Objetivo | Fuente de Dataset / Catálogo |
|--------------------------------|-----------|----------|------------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Asistente de desarrollo manejando indicaciones de intención mixta (refactorizar, resumir, clasificar) | Enrutamiento heurístico de intención → alias de modelo con uso de tokens | `CATALOG` en línea + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Planificación y refinamiento de múltiples pasos para una tarea compleja de asistencia de codificación | Descomponer → ejecución especializada → paso de refinamiento de resumen | Mismo `CATALOG`; pasos derivados de la salida del plan |

### Narrativa del Escenario
Una herramienta de productividad para ingenieros recibe tareas heterogéneas: refactorizar código, resumir notas arquitectónicas, clasificar comentarios. Para minimizar la latencia y el uso de recursos, un modelo pequeño y general planifica y resume, un modelo especializado en código maneja la refactorización, y un modelo ligero capaz de clasificación etiqueta los comentarios. El script de la tubería demuestra encadenamiento + refinamiento; el script del enrutador aísla el enrutamiento adaptativo de una sola indicación.

### Instantánea del Catálogo
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Ejemplos de Indicaciones de Prueba
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Extensión de Trazas (Opcional)
Agregar líneas JSON de trazas por paso para `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heurística de Escalamiento (Idea)
Si el plan contiene palabras clave como "optimizar", "seguridad", o la longitud del paso > 280 caracteres → escalar a un modelo más grande (por ejemplo, `gpt-oss-20b`) solo para ese paso.

### Mejoras Opcionales

| Área | Mejora | Valor | Pista |
|------|--------|-------|-------|
| Caché | Reutilizar objetos de gestor + cliente | Menor latencia, menos sobrecarga | Usar `workshop_utils.get_client` |
| Métricas de Uso | Capturar tokens y latencia por paso | Perfilado y optimización | Cronometrar cada llamada enrutada; almacenar en lista de trazas |
| Enrutamiento Adaptativo | Consciente de confianza/costo | Mejor equilibrio calidad-costo | Agregar puntuación: si la indicación > N caracteres o el regex coincide con el dominio → escalar a un modelo más grande |
| Registro Dinámico de Capacidades | Recarga dinámica del catálogo | Sin reinicio ni redepliegue | Cargar `catalog.json` en tiempo de ejecución; observar la marca de tiempo del archivo |
| Estrategia de Respaldo | Robustez ante fallos | Mayor disponibilidad | Intentar primario → en caso de excepción, alias de respaldo |
| Tubería de Transmisión | Retroalimentación temprana | Mejora de UX | Transmitir cada paso y almacenar en búfer la entrada final de refinamiento |
| Embeddings de Intención Vectorial | Enrutamiento más matizado | Mayor precisión de intención | Incrustar indicación, agrupar y mapear centroides → capacidad |
| Exportación de Trazas | Cadena auditable | Cumplimiento/informes | Emitir líneas JSON: paso, intención, modelo, latencia_ms, tokens |
| Simulación de Costos | Estimación previa a la nube | Planificación presupuestaria | Asignar costo nocional/token por modelo y agregar por tarea |
| Modo Determinista | Reproducibilidad | Benchmarking estable | Entorno: `temperature=0`, número fijo de pasos |

#### Ejemplo de Estructura de Trazas

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Esquema de Escalamiento Adaptativo

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Recarga Dinámica del Catálogo de Modelos

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.