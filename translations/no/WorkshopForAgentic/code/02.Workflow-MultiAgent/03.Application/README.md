<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:06:13+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "no"
}
-->
# Podcast-applikasjon

En konsollapplikasjon for å generere podkastmanus ved hjelp av AI-agenter.

## Bruk

```bash
python podcast_app.py
```

## Arbeidsflyt

1. **Velkommen** - Applikasjonen hilser brukeren
2. **Emneinnskriving** - Brukeren oppgir et emne for podkasten
3. **Søkeagent** - Søk etter relevant informasjon
4. **Generer manus-agent** - Lager et podkastmanus
5. **Gjennomgang** - Brukeren gjennomgår og godkjenner/avviser manuset
6. **Lagre** - Godkjent manus lagres til `podcast.md`

## Krav

- Python 3.12+
- agent_framework
- Alle avhengigheter fra 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på det opprinnelige språket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->