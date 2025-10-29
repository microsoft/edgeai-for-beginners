<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T22:25:52+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "nl"
}
-->
# Workshop Scripts

Deze map bevat automatiserings- en ondersteuningsscripts die worden gebruikt om de kwaliteit en consistentie van het Workshop-materiaal te waarborgen.

## Inhoud

| Bestand | Doel |
|---------|------|
| `lint_markdown_cli.py` | Controleert markdown-codeblokken op verouderde Foundry Local CLI-commandopatronen. |
| `export_benchmark_markdown.py` | Voert een multi-model latentiebenchmark uit en genereert Markdown + JSON-rapporten. |

## 1. Markdown CLI Pattern Linter

`lint_markdown_cli.py` scant alle niet-vertaalde `.md`-bestanden op niet-toegestane Foundry Local CLI-patronen **binnen afgebakende codeblokken** (``` ... ```). Informatieve tekst kan nog steeds verouderde commando's vermelden voor historische context.

### Verouderde Patronen (Geblokkeerd Binnen Codeblokken)

De linter blokkeert verouderde CLI-patronen. Gebruik moderne alternatieven.

### Vereiste Vervangingen
| Verouderd | Gebruik In plaats Van |
|-----------|------------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmarkscript + systeemtools (`Taakbeheer`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Exitcodes
| Code | Betekenis |
|------|-----------|
| 0 | Geen overtredingen gedetecteerd |
| 1 | Een of meer verouderde patronen gevonden |

### Lokaal Uitvoeren
Vanaf de root van de repository (aanbevolen):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (Optioneel)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Dit blokkeert commits die verouderde patronen introduceren.

### CI Integratie
Een GitHub Action workflow (`.github/workflows/markdown-cli-lint.yml`) voert de linter uit bij elke push en pull request naar de `main` en `Reactor` branches. Mislukte taken moeten worden opgelost voordat ze worden samengevoegd.

### Nieuwe Verouderde Patronen Toevoegen
1. Open `lint_markdown_cli.py`.
2. Voeg een tuple `(regex, suggestion)` toe aan de `DEPRECATED`-lijst. Gebruik een raw string en voeg waar nodig woordgrenzen (`\b`) toe.
3. Voer de linter lokaal uit om detectie te verifiëren.
4. Commit en push; CI zal de nieuwe regel afdwingen.

Voorbeeld toevoeging:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Toelaten van Uitleggende Vermeldingen
Omdat alleen afgebakende codeblokken worden gecontroleerd, kun je verouderde commando's veilig beschrijven in verhalende tekst. Als je ze *moet* tonen binnen een blok voor contrast, gebruik dan een afgebakend blok **zonder** drie backticks (bijv. inspringen of citeren) of herschrijf naar een pseudo-vorm.

### Specifieke Bestanden Overslaan (Geavanceerd)
Indien nodig, plaats legacyvoorbeelden in een apart bestand buiten de repository of hernoem met een andere extensie tijdens het opstellen. Opzettelijke overslagen voor vertaalde kopieën zijn automatisch (paden met `translations`).

### Problemen Oplossen
| Probleem | Oorzaak | Oplossing |
|----------|---------|-----------|
| Linter markeert een regel die je hebt bijgewerkt | Regex te breed | Verfijn patroon met extra woordgrens (`\b`) of ankers |
| CI faalt maar lokaal werkt het | Verschillende Python-versie of niet-gecommit wijzigingen | Voer lokaal opnieuw uit, zorg voor een schone werkmap, controleer de Python-versie van de workflow (3.11) |
| Tijdelijk omzeilen nodig | Noodfix | Pas fix onmiddellijk toe; overweeg een tijdelijke branch en follow-up PR (voorkom het toevoegen van omzeilopties) |

### Reden
Het documenteren van de *huidige* stabiele CLI-interface voorkomt frictie tijdens workshops, vermijdt verwarring bij deelnemers en centraliseert prestatiemeting via onderhouden Pythonscripts in plaats van verouderde CLI-subcommando's.

---
Onderhouden als onderdeel van de workshop kwaliteits-toolchain. Voor verbeteringen (bijv. automatische correctiesuggesties of HTML-rapportgeneratie), open een issue of dien een PR in.

## 2. Validatiescript voor Voorbeelden

`validate_samples.py` controleert alle Python-voorbeeldbestanden op syntax, imports en naleving van best practices.

### Gebruik
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

### Wat het controleert
- ✅ Geldigheid van Python-syntax
- ✅ Vereiste imports aanwezig
- ✅ Implementatie van foutafhandeling (verbose modus)
- ✅ Gebruik van type hints (verbose modus)
- ✅ Functiedocstrings (verbose modus)
- ✅ SDK-referentielinks (verbose modus)

### Omgevingsvariabelen
- `SKIP_IMPORT_CHECK=1` - Sla importvalidatie over
- `SKIP_SYNTAX_CHECK=1` - Sla syntaxvalidatie over

### Exitcodes
- `0` - Alle voorbeelden zijn gevalideerd
- `1` - Een of meer voorbeelden zijn niet gevalideerd

## 3. Testscript voor Voorbeelden

`test_samples.py` voert rooktests uit op alle voorbeelden om te verifiëren dat ze zonder fouten worden uitgevoerd.

### Gebruik
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

### Vereisten
- Foundry Local-service actief: `foundry service start`
- Modellen geladen: `foundry model run phi-4-mini`
- Afhankelijkheden geïnstalleerd: `pip install -r requirements.txt`

### Wat het test
- ✅ Voorbeeld kan worden uitgevoerd zonder runtimefouten
- ✅ Vereiste output wordt gegenereerd
- ✅ Correcte foutafhandeling bij falen
- ✅ Prestaties (uitvoeringstijd)

### Omgevingsvariabelen
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model dat wordt gebruikt voor testen
- `TEST_TIMEOUT=30` - Timeout per voorbeeld in seconden

### Verwachte Fouten
Sommige tests kunnen falen als optionele afhankelijkheden niet zijn geïnstalleerd (bijv. `ragas`, `sentence-transformers`). Installeer met:
```bash
pip install sentence-transformers ragas datasets
```

### Exitcodes
- `0` - Alle tests geslaagd
- `1` - Een of meer tests mislukt

## 4. Benchmark Markdown Exporter

Script: `export_benchmark_markdown.py`

Genereert een reproduceerbare prestatietabel voor een set modellen.

### Gebruik
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Uitvoer
| Bestand | Beschrijving |
|---------|--------------|
| `benchmark_report.md` | Markdown-tabel (gemiddelde, p95, tokens/sec, optioneel eerste token) |
| `benchmark_report.json` | Ruwe metrische array voor vergelijking & geschiedenis |

### Opties
| Vlag | Beschrijving | Standaard |
|------|--------------|-----------|
| `--models` | Komma-gescheiden modelaliassen | (vereist) |
| `--prompt` | Prompt gebruikt per ronde | (vereist) |
| `--rounds` | Ronden per model | 3 |
| `--output` | Markdown-uitvoerbestand | `benchmark_report.md` |
| `--json` | JSON-uitvoerbestand | `benchmark_report.json` |
| `--fail-on-empty` | Niet-nul exit als alle benchmarks falen | uit |

Omgevingsvariabele `BENCH_STREAM=1` voegt latentiemeting van het eerste token toe.

### Opmerkingen
- Hergebruikt `workshop_utils` voor consistente modelinitialisatie & caching.
- Als het script vanuit een andere werkmap wordt uitgevoerd, probeert het padfallbacks om `workshop_utils` te vinden.
- Voor GPU-vergelijking: voer één keer uit, schakel versnelling in via CLI-configuratie, voer opnieuw uit en vergelijk de JSON.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.