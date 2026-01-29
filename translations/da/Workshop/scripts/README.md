# Workshop Scripts

Denne mappe indeholder automatiserings- og supportskripter, der bruges til at opretholde kvalitet og konsistens i Workshop-materialerne.

## Indhold

| Fil | Formål |
|-----|--------|
| `lint_markdown_cli.py` | Kontrollerer markdown-kodeblokke for forældede Foundry Local CLI-kommandoer. |
| `export_benchmark_markdown.py` | Kører multi-model latenstests og genererer Markdown + JSON-rapporter. |

## 1. Markdown CLI Pattern Linter

`lint_markdown_cli.py` scanner alle ikke-oversatte `.md`-filer for forbudte Foundry Local CLI-mønstre **inden for indhegnede kodeblokke** (``` ... ```). Informativ tekst kan stadig nævne forældede kommandoer for historisk kontekst.

### Forældede Mønstre (Blokeret i Kodeblokke)

Linteren blokerer forældede CLI-mønstre. Brug moderne alternativer i stedet.

### Nødvendige Erstatninger
| Forældet | Brug I stedet |
|----------|---------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark-skript + systemværktøjer (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Exit Codes
| Kode | Betydning |
|------|-----------|
| 0 | Ingen overtrædelser fundet |
| 1 | En eller flere forældede mønstre fundet |

### Lokal Kørsel
Fra repository-roden (anbefalet):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (Valgfrit)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Dette blokerer commits, der introducerer forældede mønstre.

### CI Integration
En GitHub Action workflow (`.github/workflows/markdown-cli-lint.yml`) kører linteren ved hver push og pull request til `main` og `Reactor` branches. Fejlende jobs skal rettes, før de kan merges.

### Tilføjelse af Nye Forældede Mønstre
1. Åbn `lint_markdown_cli.py`.
2. Tilføj en tuple `(regex, suggestion)` til `DEPRECATED`-listen. Brug en rå streng og inkluder `\b` ordgrænser, hvor det er relevant.
3. Kør linteren lokalt for at verificere detektion.
4. Commit og push; CI vil håndhæve den nye regel.

Eksempel på tilføjelse:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Tillad Forklarende Omtaler
Da kun indhegnede kodeblokke håndhæves, kan du sikkert beskrive forældede kommandoer i narrativ tekst. Hvis du *skal* vise dem i en blok for kontrast, tilføj en blok **uden** triple backticks (f.eks. indrykning eller citat) eller omskriv til pseudoform.

### Spring Over Specifikke Filer (Avanceret)
Hvis nødvendigt, placer legacy-eksempler i en separat fil uden for repoen eller omdøb med en anden filtype under udarbejdelse. Bevidste undtagelser for oversatte kopier er automatiske (stier, der indeholder `translations`).

### Fejlfinding
| Problem | Årsag | Løsning |
|---------|-------|---------|
| Linteren markerer en linje, du har opdateret | Regex for bred | Indsnævr mønsteret med yderligere ordgrænse (`\b`) eller ankre |
| CI fejler, men lokal kørsel passerer | Forskellig Python-version eller ikke-committede ændringer | Kør lokalt igen, sørg for ren arbejdsmappe, tjek workflow Python-version (3.11) |
| Behov for midlertidig omgåelse | Nødrettelse | Udfør rettelsen straks efter; overvej at bruge en midlertidig branch og opfølgende PR (undgå at tilføje omgåelsesmuligheder) |

### Begrundelse
At holde dokumentationen i tråd med den *nuværende* stabile CLI-overflade forhindrer problemer i workshoppen, undgår forvirring hos deltagerne og centraliserer præstationsmåling gennem vedligeholdte Python-skripter i stedet for forældede CLI-kommandoer.

---
Vedligeholdes som en del af workshop-kvalitetsværktøjskæden. For forbedringer (f.eks. automatiske rettelsesforslag eller HTML-rapportgenerering), opret en issue eller indsend en PR.

## 2. Eksempelvalideringsskript

`validate_samples.py` validerer alle Python-eksempelfiler for syntaks, imports og overholdelse af bedste praksis.

### Brug
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

### Hvad det kontrollerer
- ✅ Python-syntaks gyldighed
- ✅ Nødvendige imports til stede
- ✅ Implementering af fejlhåndtering (detaljeret tilstand)
- ✅ Brug af type hints (detaljeret tilstand)
- ✅ Funktionsdocstrings (detaljeret tilstand)
- ✅ SDK-referencelinks (detaljeret tilstand)

### Miljøvariabler
- `SKIP_IMPORT_CHECK=1` - Spring importvalidering over
- `SKIP_SYNTAX_CHECK=1` - Spring syntaksvalidering over

### Exit Codes
- `0` - Alle eksempler bestod validering
- `1` - Et eller flere eksempler fejlede

## 3. Eksempel Test Runner

`test_samples.py` kører test på alle eksempler for at verificere, at de kører uden fejl.

### Brug
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

### Forudsætninger
- Foundry Local service kører: `foundry service start`
- Modeller indlæst: `foundry model run phi-4-mini`
- Afhængigheder installeret: `pip install -r requirements.txt`

### Hvad det tester
- ✅ Eksempel kan køre uden runtime-fejl
- ✅ Nødvendig output genereres
- ✅ Korrekt fejlhåndtering ved fejl
- ✅ Ydeevne (eksekveringstid)

### Miljøvariabler
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model, der skal bruges til test
- `TEST_TIMEOUT=30` - Timeout pr. eksempel i sekunder

### Forventede Fejl
Nogle tests kan fejle, hvis valgfrie afhængigheder ikke er installeret (f.eks. `ragas`, `sentence-transformers`). Installer med:
```bash
pip install sentence-transformers ragas datasets
```

### Exit Codes
- `0` - Alle tests bestod
- `1` - Et eller flere tests fejlede

## 4. Benchmark Markdown Exporter

Skript: `export_benchmark_markdown.py`

Genererer en reproducerbar præstationstabel for et sæt modeller.

### Brug
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Outputs
| Fil | Beskrivelse |
|-----|-------------|
| `benchmark_report.md` | Markdown-tabel (gennemsnit, p95, tokens/sek, valgfri første token) |
| `benchmark_report.json` | Rå metrikker til sammenligning & historik |

### Valgmuligheder
| Flag | Beskrivelse | Standard |
|------|-------------|----------|
| `--models` | Kommaseparerede modelaliaser | (påkrævet) |
| `--prompt` | Prompt brugt hver runde | (påkrævet) |
| `--rounds` | Runder pr. model | 3 |
| `--output` | Markdown output-fil | `benchmark_report.md` |
| `--json` | JSON output-fil | `benchmark_report.json` |
| `--fail-on-empty` | Ikke-nul exit, hvis alle benchmarks fejler | off |

Miljøvariabel `BENCH_STREAM=1` tilføjer måling af første token latenstid.

### Noter
- Genbruger `workshop_utils` for konsistent model bootstrap & caching.
- Hvis kørt fra en anden arbejdsmappe, forsøger skriptet at finde `workshop_utils` via alternative stier.
- For GPU-sammenligning: kør én gang, aktiver acceleration via CLI-konfiguration, kør igen og sammenlign JSON.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.