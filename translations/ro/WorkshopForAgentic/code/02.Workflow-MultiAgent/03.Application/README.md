<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:09:05+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "ro"
}
-->
# Podcast Application

O aplicație de consolă pentru generarea de scripturi de podcast folosind agenți AI.

## Usage

```bash
python podcast_app.py
```

## Workflow

1. **Welcome** - Aplicația întâmpină utilizatorul
2. **Topic Input** - Utilizatorul oferă un subiect pentru podcast
3. **Search Agent** - Caută informații relevante
4. **Generate Script Agent** - Creează un script pentru podcast
5. **Review** - Utilizatorul revizuiește și aprobă/respinge scriptul
6. **Save** - Scriptul aprobat este salvat în `podcast.md`

## Requirements

- Python 3.12+
- agent_framework
- Toate dependențele din 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa oficială. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->