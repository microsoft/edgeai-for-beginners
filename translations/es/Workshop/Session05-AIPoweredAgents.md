<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T20:05:28+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "es"
}
-->
# Sesión 5: Construye Agentes Potenciados por IA Rápidamente con Foundry Local

## Resumen

Diseña y orquesta agentes de IA con múltiples roles utilizando el entorno de ejecución de baja latencia y preservación de privacidad de Foundry Local. Definirás roles de agentes, estrategias de memoria, patrones de invocación de herramientas y gráficos de ejecución. La sesión introduce patrones de estructura que puedes ampliar con Chainlit o LangGraph. El proyecto inicial amplía el ejemplo de arquitectura de agentes existente para añadir persistencia de memoria y ganchos de evaluación.

## Objetivos de Aprendizaje

- **Definir Roles**: Indicaciones del sistema y límites de capacidades
- **Implementar Memoria**: Corto plazo (conversación), largo plazo (vector / archivo), notas efímeras
- **Estructurar Flujos de Trabajo**: Pasos secuenciales, ramificados y paralelos de los agentes
- **Integrar Herramientas**: Patrón ligero de llamada a funciones como herramientas
- **Evaluar**: Trazabilidad básica + puntuación de resultados basada en rúbricas

## Requisitos Previos

- Haber completado las sesiones 1–4
- Python con `foundry-local-sdk`, `openai`, opcional `chainlit`
- Modelos locales en ejecución (al menos `phi-4-mini`)

### Fragmento de Entorno Multiplataforma

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Si ejecutas agentes desde macOS contra un servicio remoto en Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Flujo de Demostración (30 min)

### 1. Definir Roles de Agentes y Memoria (7 min)

Crea `samples/05-agents/agents_core.py`:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. Patrón de Estructuración CLI (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Añadir Invocación de Herramientas (7 min)

Amplía con `samples/05-agents/tools.py`:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```

Modifica `agents_core.py` para permitir una sintaxis simple de herramientas: el usuario escribe `#tool:get_time` y el agente expande la salida de la herramienta en el contexto antes de la generación.

### 4. Flujo de Trabajo Orquestado (6 min)

Crea `samples/05-agents/orchestrator.py`:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. Proyecto Inicial: Ampliar `05-agent-architecture` (7 min)

Añade:
1. Capa de memoria persistente (por ejemplo, añadir líneas JSON de conversaciones)
2. Rúbrica de evaluación simple: marcadores de factualidad / claridad / estilo
3. Front-end opcional con Chainlit (dos pestañas: conversación y trazas)
4. Máquina de estados estilo LangGraph opcional (si se añade dependencia) para decisiones ramificadas

## Lista de Verificación de Validación

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Espera una salida estructurada de la canalización con una nota de inyección de herramientas.

## Resumen de Estrategias de Memoria

| Capa       | Propósito             | Ejemplo               |
|------------|-----------------------|-----------------------|
| Corto plazo | Continuidad del diálogo | Últimos N mensajes    |
| Episódica   | Recuerdo de la sesión | JSON por sesión       |
| Semántica   | Recuperación a largo plazo | Almacén vectorial de resúmenes |
| Scratchpad  | Pasos de razonamiento | Cadena de pensamiento en línea (privada) |

## Ganchos de Evaluación (Conceptual)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Resolución de Problemas

| Problema            | Causa                  | Resolución                     |
|---------------------|------------------------|---------------------------------|
| Respuestas repetitivas | Ventana de contexto demasiado grande/pequeña | Ajustar el parámetro de ventana de memoria |
| Herramienta no invocada | Sintaxis incorrecta | Usar formato `#tool:tool_name` |
| Orquestación lenta  | Múltiples modelos fríos | Ejecutar prompts de calentamiento previamente |

## Referencias

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (concepto opcional): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Duración de la Sesión**: 30 min  
**Dificultad**: Avanzada

## Escenario de Ejemplo y Mapeo del Taller

| Script del Taller | Escenario | Objetivo | Ejemplo de Prompt |
|-------------------|-----------|----------|-------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot de investigación de conocimiento que produce resúmenes aptos para ejecutivos | Canalización de dos agentes (investigación → pulido editorial) con modelos opcionales distintos | Explica por qué la inferencia en el borde es importante para el cumplimiento. |
| Concepto ampliado de `tools.py` | Añadir herramientas de estimación de tiempo y tokens | Demostrar patrón ligero de invocación de herramientas | #tool:get_time |

### Narrativa del Escenario
El equipo de documentación de cumplimiento necesita resúmenes internos rápidos obtenidos de conocimiento local sin enviar borradores a servicios en la nube. Un agente investigador reúne puntos factuales concisos; un agente editor los reescribe para mayor claridad ejecutiva. Se pueden asignar alias de modelos distintos para optimizar la latencia (SLM rápido) frente al refinamiento estilístico (modelo más grande solo cuando sea necesario).

### Ejemplo de Entorno Multi-Modelo
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Estructura de Trazas (Opcional)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

Persiste cada paso en un archivo JSONL para puntuación de rúbrica posterior.

### Mejoras Opcionales

| Tema              | Mejora                     | Beneficio              | Esbozo de Implementación       |
|-------------------|----------------------------|------------------------|--------------------------------|
| Roles Multi-Modelo | Modelos distintos por agente (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Especialización y velocidad | Seleccionar alias de variables de entorno, llamar a `chat_once` con alias por rol |
| Trazas Estructuradas | Trazas JSON de cada acción (herramienta, entrada, latencia, tokens) | Depuración y evaluación | Añadir diccionario a una lista; escribir `.jsonl` al final |
| Persistencia de Memoria | Contexto de diálogo recargable | Continuidad de la sesión | Volcar `Agent.memory` en `sessions/<ts>.json` |
| Registro de Herramientas | Descubrimiento dinámico de herramientas | Extensibilidad | Mantener un diccionario `TOOLS` e inspeccionar nombres/descripciones |
| Reintentos y Retrocesos | Cadenas largas robustas | Reducir fallos transitorios | Envolver `act` con try/except + retroceso exponencial |
| Puntuación de Rúbrica | Etiquetas cualitativas automatizadas | Seguimiento de mejoras | Segunda pasada con el modelo: "Califica claridad 1-5" |
| Memoria Vectorial | Recuperación semántica | Contexto rico a largo plazo | Incorporar resúmenes, recuperar los mejores k en el mensaje del sistema |
| Respuestas en Streaming | Respuesta percibida más rápida | Mejora de UX | Usar streaming cuando esté disponible y vaciar tokens parciales |
| Pruebas Deterministas | Control de regresión | CI estable | Ejecutar con `temperature=0`, semillas de prompt fijas |
| Ramificación Paralela | Exploración más rápida | Rendimiento | Usar `concurrent.futures` para pasos independientes de agentes |

#### Ejemplo de Registro de Trazas

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Prompt de Evaluación Simple

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Persiste pares (`answer`, `rating`) para construir un gráfico histórico de calidad.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.