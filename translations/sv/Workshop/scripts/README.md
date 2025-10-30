<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T22:07:28+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "sv"
}
-->
# Workshop-skript

Den här katalogen innehåller automatiserings- och stödskript som används för att upprätthålla kvalitet och konsekvens i Workshop-materialet.

## Innehåll

| Fil | Syfte |
|------|---------|
| `lint_markdown_cli.py` | Kontrollerar markdown-kodblock för att blockera föråldrade Foundry Local CLI-kommandomönster. |
| `export_benchmark_markdown.py` | Kör latensbenchmark för flera modeller och genererar Markdown + JSON-rapporter. |

## 1. Markdown CLI-mönsterkontroll

`lint_markdown_cli.py` skannar alla icke-översatta `.md`-filer efter otillåtna Foundry Local CLI-mönster **inuti kodblock** (``` ... ```). Informativ text kan fortfarande nämna föråldrade kommandon för historisk kontext.

### Föråldrade mönster (blockerade inuti kodblock)

Kontrollverktyget blockerar föråldrade CLI-mönster. Använd moderna alternativ istället.

### Obligatoriska ersättningar
| Föråldrat | Använd istället |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark-skript + systemverktyg (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Exit-koder
| Kod | Betydelse |
|------|---------|
| 0 | Inga överträdelser upptäckta |
| 1 | En eller flera föråldrade mönster hittades |

### Kör lokalt
Från repositoryns rot (rekommenderas):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-commit-hook (valfritt)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Detta blockerar commits som introducerar föråldrade mönster.

### CI-integrering
Ett GitHub Action-arbetsflöde (`.github/workflows/markdown-cli-lint.yml`) kör kontrollverktyget vid varje push och pull request till `main` och `Reactor`-brancherna. Misslyckade jobb måste åtgärdas innan sammanslagning.

### Lägga till nya föråldrade mönster
1. Öppna `lint_markdown_cli.py`.
2. Lägg till en tuple `(regex, suggestion)` i listan `DEPRECATED`. Använd en rå sträng och inkludera ordgränser `\b` där det är lämpligt.
3. Kör kontrollverktyget lokalt för att verifiera upptäckt.
4. Commit och push; CI kommer att upprätthålla den nya regeln.

Exempel på tillägg:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Tillåta förklarande omnämnanden
Eftersom endast kodblock kontrolleras kan du beskriva föråldrade kommandon i narrativ text utan problem. Om du *måste* visa dem i ett kodblock för kontrast, använd ett kodblock **utan** tre backticks (t.ex. indrag eller citat) eller skriv om till en pseudoform.

### Hoppa över specifika filer (avancerat)
Om det behövs, placera äldre exempel i en separat fil utanför repositoryn eller byt namn med en annan filändelse under utarbetandet. Avsiktliga undantag för översatta kopior är automatiska (sökvägar som innehåller `translations`).

### Felsökning
| Problem | Orsak | Lösning |
|-------|-------|-----------|
| Kontrollverktyget flaggar en rad du har uppdaterat | Regex för bred | Begränsa mönstret med ytterligare ordgräns (`\b`) eller ankare |
| CI misslyckas men lokalt fungerar | Olika Python-version eller ocommiterade ändringar | Kör om lokalt, säkerställ en ren arbetskatalog, kontrollera arbetsflödets Python-version (3.11) |
| Behöver tillfälligt kringgå | Akut fix | Åtgärda omedelbart efteråt; överväg att använda en tillfällig branch och uppföljande PR (undvik att lägga till kringgångsalternativ) |

### Motivering
Att hålla dokumentationen i linje med *nuvarande* stabil CLI-yta förhindrar friktion i workshoppen, undviker förvirring hos deltagare och centraliserar prestandamätning genom underhållna Python-skript istället för föråldrade CLI-kommandon.

---
Underhålls som en del av workshopens kvalitetssäkringsverktyg. För förbättringar (t.ex. automatiska korrigeringsförslag eller HTML-rapportgenerering), öppna ett ärende eller skicka en PR.

## 2. Exempelskript för validering

`validate_samples.py` validerar alla Python-exempelfiler för syntax, imports och efterlevnad av bästa praxis.

### Användning
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

### Vad det kontrollerar
- ✅ Python-syntax giltighet
- ✅ Nödvändiga imports finns
- ✅ Implementering av felhantering (verbose-läge)
- ✅ Användning av typanvisningar (verbose-läge)
- ✅ Funktionsdocstrings (verbose-läge)
- ✅ SDK-referenslänkar (verbose-läge)

### Miljövariabler
- `SKIP_IMPORT_CHECK=1` - Hoppa över validering av imports
- `SKIP_SYNTAX_CHECK=1` - Hoppa över syntaxvalidering

### Exit-koder
- `0` - Alla exempel klarade valideringen
- `1` - Ett eller flera exempel misslyckades

## 3. Testkörning av exempel

`test_samples.py` kör snabba tester på alla exempel för att verifiera att de körs utan fel.

### Användning
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

### Förutsättningar
- Foundry Local-tjänst igång: `foundry service start`
- Modeller laddade: `foundry model run phi-4-mini`
- Beroenden installerade: `pip install -r requirements.txt`

### Vad det testar
- ✅ Exempel kan köras utan runtime-fel
- ✅ Nödvändig output genereras
- ✅ Korrekt felhantering vid fel
- ✅ Prestanda (exekveringstid)

### Miljövariabler
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modell att använda för testning
- `TEST_TIMEOUT=30` - Timeout per exempel i sekunder

### Förväntade fel
Vissa tester kan misslyckas om valfria beroenden inte är installerade (t.ex. `ragas`, `sentence-transformers`). Installera med:
```bash
pip install sentence-transformers ragas datasets
```

### Exit-koder
- `0` - Alla tester klarade
- `1` - Ett eller flera tester misslyckades

## 4. Benchmark Markdown-exportör

Skript: `export_benchmark_markdown.py`

Genererar en reproducerbar prestandatabell för en uppsättning modeller.

### Användning
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Utdata
| Fil | Beskrivning |
|------|-------------|
| `benchmark_report.md` | Markdown-tabell (medelvärde, p95, tokens/sek, valfritt första token) |
| `benchmark_report.json` | Rå metrisk array för jämförelse & historik |

### Alternativ
| Flagga | Beskrivning | Standard |
|------|-------------|---------|
| `--models` | Komma-separerade modellalias | (obligatoriskt) |
| `--prompt` | Prompt som används varje omgång | (obligatoriskt) |
| `--rounds` | Omgångar per modell | 3 |
| `--output` | Markdown-utdatafil | `benchmark_report.md` |
| `--json` | JSON-utdatafil | `benchmark_report.json` |
| `--fail-on-empty` | Exit-kod som inte är noll om alla benchmarks misslyckas | av |

Miljövariabeln `BENCH_STREAM=1` lägger till latensmätning för första token.

### Anteckningar
- Återanvänder `workshop_utils` för konsekvent modellbootstrap & caching.
- Om det körs från en annan arbetskatalog försöker skriptet sökvägsfall tillbaka för att hitta `workshop_utils`.
- För GPU-jämförelse: kör en gång, aktivera acceleration via CLI-konfiguration, kör om och jämför JSON.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.