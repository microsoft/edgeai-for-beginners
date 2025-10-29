<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T20:04:43+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "es"
}
-->
# Sesión 4: Explora Modelos de Última Generación – LLMs, SLMs e Inferencia en Dispositivos

## Resumen

Compara Modelos de Lenguaje Grandes (LLMs) y Modelos de Lenguaje Pequeños (SLMs) para escenarios de inferencia local frente a la nube. Aprende patrones de implementación aprovechando la aceleración de ONNX Runtime, la ejecución de WebGPU y experiencias híbridas de RAG. Incluye una demostración de Chainlit RAG con un modelo local y una exploración opcional de OpenWebUI. Adaptarás un inicio de inferencia con WebGPU y evaluarás las capacidades y las compensaciones de costo/rendimiento entre Phi y GPT-OSS-20B.

## Objetivos de Aprendizaje

- **Contrastar** SLM frente a LLM en términos de latencia, memoria y calidad
- **Implementar** modelos con ONNXRuntime y (donde sea compatible) WebGPU
- **Ejecutar** inferencia basada en navegador (demostración interactiva que preserva la privacidad)
- **Integrar** una canalización RAG de Chainlit con un backend SLM local
- **Evaluar** utilizando heurísticas ligeras de calidad y costo

## Prerrequisitos

- Haber completado las sesiones 1–3
- `chainlit` instalado (ya incluido en `requirements.txt` para el Módulo08)
- Navegador compatible con WebGPU (Edge / Chrome más reciente en Windows 11)
- Foundry Local en ejecución (`foundry status`)

### Notas Multiplataforma

Windows sigue siendo el entorno objetivo principal. Para desarrolladores de macOS que esperan binarios nativos:
1. Ejecuta Foundry Local en una máquina virtual con Windows 11 (Parallels / UTM) O en una estación de trabajo remota con Windows.
2. Expón el servicio (puerto predeterminado 5273) y configúralo en macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Usa los mismos pasos del entorno virtual de Python que en las sesiones anteriores.

Instalación de Chainlit (ambas plataformas):
```bash
pip install chainlit
```

## Flujo de Demostración (30 min)

### 1. Comparar Phi (SLM) frente a GPT-OSS-20B (LLM) (6 min)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Seguimiento: profundidad de respuesta, precisión factual, riqueza estilística, latencia.

### 2. Aceleración con ONNX Runtime (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Observa los cambios en el rendimiento después de habilitar GPU frente a solo CPU.

### 3. Inferencia con WebGPU en el Navegador (6 min)

Adapta el inicio `04-webgpu-inference` (crea `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Abre el archivo en un navegador; observa el intercambio local de baja latencia.

### 4. Aplicación de Chat RAG con Chainlit (7 min)

`samples/04-cutting-edge/chainlit_app.py` mínimo:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Ejecuta:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Proyecto Inicial: Adaptar `04-webgpu-inference` (6 min)

Entregables:
- Sustituir la lógica de obtención de datos por tokens en streaming (usar la variante del endpoint `stream=True` una vez habilitada)
- Añadir gráfico de latencia (en el cliente) para alternar entre phi y gpt-oss-20b
- Incluir contexto RAG en línea (área de texto para documentos de referencia)

## Heurísticas de Evaluación

| Categoría | Phi-4-mini | GPT-OSS-20B | Observación |
|-----------|------------|-------------|-------------|
| Latencia (frío) | Rápida | Más lenta | SLM se calienta rápidamente |
| Memoria | Baja | Alta | Factibilidad en dispositivos |
| Adherencia al contexto | Buena | Fuerte | El modelo más grande puede ser más detallado |
| Costo (local) | Mínimo | Mayor (recursos) | Compensación energía/tiempo |
| Mejor caso de uso | Apps en el borde | Razonamiento profundo | Es posible una canalización híbrida |

## Validando el Entorno

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Resolución de Problemas

| Síntoma | Causa | Acción |
|---------|-------|--------|
| Falla al obtener página web | CORS o servicio caído | Usa `curl` para verificar el endpoint; habilita proxy CORS si es necesario |
| Chainlit en blanco | Entorno no activo | Activa venv y reinstala dependencias |
| Alta latencia | Modelo recién cargado | Calienta con una secuencia de prompts pequeños |

## Referencias

- SDK de Foundry Local: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentación de Chainlit: https://docs.chainlit.io
- Evaluación RAG (Ragas): https://docs.ragas.io

---

**Duración de la Sesión**: 30 min  
**Dificultad**: Avanzada

## Escenario de Ejemplo y Mapeo del Taller

| Artefactos del Taller | Escenario | Objetivo | Fuente de Datos / Prompt |
|------------------------|-----------|----------|--------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Equipo de arquitectura evaluando SLM frente a LLM para generador de resumen ejecutivo | Cuantificar la diferencia de latencia + uso de tokens | Variable de entorno única `COMPARE_PROMPT` |
| `chainlit_app.py` (demostración RAG) | Prototipo de asistente de conocimiento interno | Respuestas cortas fundamentadas con recuperación léxica mínima | Lista `DOCS` en línea en el archivo |
| `webgpu_demo.html` | Vista previa futurista de inferencia en navegador en dispositivos | Mostrar intercambio local de baja latencia + narrativa UX | Solo prompt de usuario en vivo |

### Narrativa del Escenario
La organización de producto quiere un generador de informes ejecutivos. Un SLM ligero (phi‑4‑mini) redacta resúmenes; un LLM más grande (gpt‑oss‑20b) puede refinar solo los informes de alta prioridad. Los scripts de la sesión capturan métricas empíricas de latencia y tokens para justificar un diseño híbrido, mientras que la demostración de Chainlit ilustra cómo la recuperación fundamentada mantiene las respuestas del modelo pequeño factuales. La página conceptual de WebGPU proporciona un camino de visión para el procesamiento completamente en el cliente cuando la aceleración del navegador madure.

### Contexto RAG Mínimo (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Flujo Híbrido Borrador→Refinamiento (Pseudocódigo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Rastrea ambos componentes de latencia para informar el costo promedio combinado.

### Mejoras Opcionales

| Enfoque | Mejora | Razón | Pista de Implementación |
|---------|--------|-------|-------------------------|
| Métricas Comparativas | Rastrear uso de tokens + latencia del primer token | Vista holística del rendimiento | Usa el script de evaluación mejorado (Sesión 3) con `BENCH_STREAM=1` |
| Canalización Híbrida | Borrador con SLM → Refinamiento con LLM | Reducir latencia y costo | Generar con phi-4-mini, refinar resumen con gpt-oss-20b |
| Interfaz de Usuario en Streaming | Mejor UX en Chainlit | Retroalimentación incremental | Usa `stream=True` una vez que el streaming local esté habilitado; acumula fragmentos |
| Caché de WebGPU | Inicio más rápido de JS | Reducir la sobrecarga de recompilación | Cachear artefactos de shaders compilados (capacidad futura del runtime) |
| Conjunto de QA Determinista | Comparación justa de modelos | Eliminar variabilidad | Lista de prompts fija + `temperature=0` para ejecuciones de evaluación |
| Evaluación de Resultados | Lente estructurada de calidad | Ir más allá de las anécdotas | Rubrica simple: coherencia / factualidad / brevedad (1–5) |
| Notas de Energía / Recursos | Discusión en clase | Mostrar compensaciones | Usa monitores del sistema operativo (`foundry system info`, Administrador de Tareas, `nvidia-smi`) + salidas de scripts de evaluación |
| Emulación de Costos | Justificación previa a la nube | Planificar escalabilidad | Mapear tokens a precios hipotéticos en la nube para narrativa de TCO |
| Descomposición de Latencia | Identificar cuellos de botella | Apuntar a optimizaciones | Medir preparación de prompt, envío de solicitud, primer token, finalización completa |
| RAG + Respaldo LLM | Red de seguridad de calidad | Mejorar consultas difíciles | Si la longitud de la respuesta SLM < umbral o baja confianza → escalar |

#### Ejemplo de Patrón Híbrido Borrador/Refinamiento

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Esbozo de Desglose de Latencia

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Usa una estructura de medición consistente entre modelos para comparaciones justas.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.