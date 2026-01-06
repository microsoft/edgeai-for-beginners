<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:08:36+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "cs"
}
-->
# Podcastová aplikace

Konzolová aplikace pro generování scénářů podcastů pomocí AI agentů.

## Použití

```bash
python podcast_app.py
```

## Pracovní postup

1. **Uvítání** - Aplikace pozdraví uživatele
2. **Zadání tématu** - Uživatel zadá téma podcastu
3. **Vyhledávací agent** - Vyhledává relevantní informace
4. **Agent pro generování scénáře** - Vytváří scénář podcastu
5. **Revize** - Uživatel zkontroluje a schválí/odmítne scénář
6. **Uložení** - Schválený scénář je uložen do `podcast.md`

## Požadavky

- Python 3.12+
- agent_framework
- Všechny závislosti z 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí služby automatického překladu AI [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace je doporučen profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo chybné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->