<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:04:26+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "it"
}
-->
# Applicazione Podcast

Un'applicazione da console per generare copioni per podcast utilizzando agenti AI.

## Uso

```bash
python podcast_app.py
```

## Flusso di lavoro

1. **Benvenuto** - L'applicazione accoglie l'utente
2. **Inserimento Argomento** - L'utente fornisce un argomento per il podcast
3. **Agente di Ricerca** - Cerca informazioni rilevanti
4. **Agente Generatore di Copione** - Crea un copione per il podcast
5. **Revisione** - L'utente rivede e approva/rifiuta il copione
6. **Salvataggio** - Il copione approvato viene salvato in `podcast.md`

## Requisiti

- Python 3.12+
- agent_framework
- Tutte le dipendenze da 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avvertenza**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l’accuratezza, si prega di tenere presente che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’utilizzo di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->