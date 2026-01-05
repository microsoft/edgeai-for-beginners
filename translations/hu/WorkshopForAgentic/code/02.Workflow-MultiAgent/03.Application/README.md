<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:08:21+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "hu"
}
-->
# Podcast Alkalmazás

Egy konzolalkalmazás podcast forgatókönyvek generálására AI ügynökök segítségével.

## Használat

```bash
python podcast_app.py
```

## Munkafolyamat

1. **Üdvözlés** - Az alkalmazás üdvözli a felhasználót
2. **Téma megadása** - A felhasználó megadja a podcast témáját
3. **Kereső ügynök** - Megkeresi a releváns információkat
4. **Forgatókönyv generáló ügynök** - Létrehozza a podcast forgatókönyvet
5. **Áttekintés** - A felhasználó átnézi és jóváhagyja/elutasítja a forgatókönyvet
6. **Mentés** - A jóváhagyott forgatókönyvet a `podcast.md` fájlba menti

## Követelmények

- Python 3.12+
- agent_framework
- Az összes függőség a 02.WorkflowDevUI-ból

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk pontos fordítást biztosítani, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén szakmai humán fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->