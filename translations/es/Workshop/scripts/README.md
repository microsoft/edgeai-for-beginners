<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T20:08:30+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "es"
}
-->
# Scripts del Taller

Este directorio contiene scripts de automatización y soporte utilizados para mantener la calidad y consistencia en los materiales del Taller.

## Contenido

| Archivo | Propósito |
|---------|-----------|
| `lint_markdown_cli.py` | Revisa bloques de código en Markdown para identificar patrones obsoletos de comandos Foundry Local CLI. |
| `export_benchmark_markdown.py` | Ejecuta pruebas de latencia con múltiples modelos y genera informes en formato Markdown + JSON. |

## 1. Linter de Patrones CLI en Markdown

`lint_markdown_cli.py` escanea todos los archivos `.md` que no sean traducciones en busca de patrones obsoletos de Foundry Local CLI **dentro de bloques de código delimitados** (``` ... ```). La prosa informativa aún puede mencionar comandos obsoletos para contexto histórico.

### Patrones Obsoletos (Bloqueados Dentro de Bloques de Código)

El linter bloquea patrones CLI obsoletos. Utiliza alternativas modernas en su lugar.

### Reemplazos Requeridos
| Obsoleto | Usar en su lugar |
|----------|------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Script de benchmark + herramientas del sistema (`Administrador de tareas`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Códigos de Salida
| Código | Significado |
|--------|-------------|
| 0 | No se detectaron violaciones |
| 1 | Se encontraron uno o más patrones obsoletos |

### Ejecución Local
Desde la raíz del repositorio (recomendado):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Hook Pre-Commit (Opcional)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Esto bloquea commits que introducen patrones obsoletos.

### Integración en CI
Un flujo de trabajo de GitHub Action (`.github/workflows/markdown-cli-lint.yml`) ejecuta el linter en cada push y pull request a las ramas `main` y `Reactor`. Los trabajos fallidos deben corregirse antes de realizar el merge.

### Agregar Nuevos Patrones Obsoletos
1. Abre `lint_markdown_cli.py`.
2. Agrega una tupla `(regex, suggestion)` a la lista `DEPRECATED`. Usa una cadena raw e incluye límites de palabra `\b` donde sea apropiado.
3. Ejecuta el linter localmente para verificar la detección.
4. Haz commit y push; el CI aplicará la nueva regla.

Ejemplo de adición:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Permitir Menciones Explicativas
Dado que solo se aplican bloques de código delimitados, puedes describir comandos obsoletos en texto narrativo de forma segura. Si *debes* mostrarlos dentro de un bloque delimitado para contraste, agrega un bloque delimitado **sin** triple backticks (por ejemplo, indenta o cita) o reescribe en forma pseudo.

### Omitir Archivos Específicos (Avanzado)
Si es necesario, envuelve ejemplos antiguos en un archivo separado fuera del repositorio o renómbralo con una extensión diferente mientras lo redactas. Las omisiones intencionales para copias traducidas son automáticas (rutas que contienen `translations`).

### Solución de Problemas
| Problema | Causa | Resolución |
|----------|-------|------------|
| El linter marca una línea que actualizaste | Regex demasiado amplio | Ajusta el patrón con límites de palabra adicionales (`\b`) o anclajes |
| El CI falla pero localmente pasa | Diferente versión de Python o cambios no comprometidos | Reejecuta localmente, asegúrate de tener un árbol de trabajo limpio, verifica la versión de Python del flujo de trabajo (3.11) |
| Necesitas omitir temporalmente | Corrección urgente | Aplica la corrección inmediatamente después; considera usar una rama temporal y un PR de seguimiento (evita agregar interruptores de omisión) |

### Justificación
Mantener la documentación alineada con la superficie CLI *estable* actual evita fricciones en el taller, reduce la confusión de los participantes y centraliza la medición de rendimiento mediante scripts de Python mantenidos en lugar de comandos CLI desactualizados.

---
Mantenido como parte de la cadena de herramientas de calidad del taller. Para mejoras (por ejemplo, sugerencias de corrección automática o generación de informes HTML), abre un issue o envía un PR.

## 2. Script de Validación de Ejemplos

`validate_samples.py` valida todos los archivos de ejemplo en Python para verificar sintaxis, importaciones y cumplimiento de buenas prácticas.

### Uso
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### Qué verifica
- ✅ Validez de la sintaxis de Python
- ✅ Importaciones requeridas presentes
- ✅ Implementación de manejo de errores (modo detallado)
- ✅ Uso de anotaciones de tipo (modo detallado)
- ✅ Docstrings en funciones (modo detallado)
- ✅ Enlaces de referencia al SDK (modo detallado)

### Variables de Entorno
- `SKIP_IMPORT_CHECK=1` - Omitir validación de importaciones
- `SKIP_SYNTAX_CHECK=1` - Omitir validación de sintaxis

### Códigos de Salida
- `0` - Todos los ejemplos pasaron la validación
- `1` - Uno o más ejemplos fallaron

## 3. Ejecutor de Pruebas de Ejemplos

`test_samples.py` ejecuta pruebas rápidas en todos los ejemplos para verificar que se ejecuten sin errores.

### Uso
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### Prerrequisitos
- Servicio Foundry Local en ejecución: `foundry service start`
- Modelos cargados: `foundry model run phi-4-mini`
- Dependencias instaladas: `pip install -r requirements.txt`

### Qué prueba
- ✅ El ejemplo puede ejecutarse sin errores de tiempo de ejecución
- ✅ Se genera la salida requerida
- ✅ Manejo adecuado de errores en caso de fallos
- ✅ Rendimiento (tiempo de ejecución)

### Variables de Entorno
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modelo a usar para pruebas
- `TEST_TIMEOUT=30` - Tiempo límite por ejemplo en segundos

### Fallos Esperados
Algunas pruebas pueden fallar si no se instalan dependencias opcionales (por ejemplo, `ragas`, `sentence-transformers`). Instálalas con:
```bash
pip install sentence-transformers ragas datasets
```

### Códigos de Salida
- `0` - Todas las pruebas pasaron
- `1` - Una o más pruebas fallaron

## 4. Exportador de Benchmark en Markdown

Script: `export_benchmark_markdown.py`

Genera una tabla de rendimiento reproducible para un conjunto de modelos.

### Uso
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Salidas
| Archivo | Descripción |
|---------|-------------|
| `benchmark_report.md` | Tabla en Markdown (promedio, p95, tokens/segundo, primer token opcional) |
| `benchmark_report.json` | Matriz de métricas en bruto para comparación y registro histórico |

### Opciones
| Flag | Descripción | Predeterminado |
|------|-------------|---------------|
| `--models` | Alias de modelos separados por comas | (requerido) |
| `--prompt` | Prompt utilizado en cada ronda | (requerido) |
| `--rounds` | Rondas por modelo | 3 |
| `--output` | Archivo de salida en Markdown | `benchmark_report.md` |
| `--json` | Archivo de salida en JSON | `benchmark_report.json` |
| `--fail-on-empty` | Salida no cero si todos los benchmarks fallan | desactivado |

La variable de entorno `BENCH_STREAM=1` agrega la medición de latencia del primer token.

### Notas
- Reutiliza `workshop_utils` para un inicio y almacenamiento en caché de modelos consistente.
- Si se ejecuta desde un directorio de trabajo diferente, el script intenta rutas alternativas para localizar `workshop_utils`.
- Para comparación de GPU: ejecuta una vez, habilita la aceleración mediante configuración CLI, vuelve a ejecutar y compara el JSON.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.