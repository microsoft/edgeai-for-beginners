<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:00:06+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "es"
}
-->
# Aplicación de Podcast

Una aplicación de consola para generar guiones de podcast utilizando agentes de IA.

## Uso

```bash
python podcast_app.py
```

## Flujo de trabajo

1. **Bienvenida** - La aplicación saluda al usuario
2. **Entrada de tema** - El usuario proporciona un tema para el podcast
3. **Agente de búsqueda** - Busca información relevante
4. **Agente para generar guion** - Crea un guion de podcast
5. **Revisión** - El usuario revisa y aprueba/rechaza el guion
6. **Guardar** - El guion aprobado se guarda en `podcast.md`

## Requisitos

- Python 3.12+
- agent_framework
- Todas las dependencias de 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->