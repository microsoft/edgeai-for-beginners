# Workshop-skript

Denne katalogen inneholder automatiserings- og støtteskript som brukes for å opprettholde kvalitet og konsistens i Workshop-materialet.

## Innhold

| Fil | Formål |
|-----|--------|
| `lint_markdown_cli.py` | Kontrollerer markdown-kodeblokker for å blokkere utdaterte Foundry Local CLI-kommandomønstre. |
| `export_benchmark_markdown.py` | Utfører ytelsestesting med flere modeller og genererer rapporter i Markdown + JSON. |

## 1. Markdown CLI-mønsterkontroll

`lint_markdown_cli.py` skanner alle ikke-oversatte `.md`-filer for ikke-tillatte Foundry Local CLI-mønstre **inne i kodeblokker** (``` ... ```). Informativ tekst kan fortsatt nevne utdaterte kommandoer for historisk kontekst.

### Utdaterte mønstre (blokkert i kodeblokker)

Kontrollverktøyet blokkerer utdaterte CLI-mønstre. Bruk moderne alternativer i stedet.

### Nødvendige erstatninger
| Utdaterte | Bruk i stedet |
|-----------|---------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Ytelsesskript + systemverktøy (`Oppgavebehandling`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Avslutningskoder
| Kode | Betydning |
|------|-----------|
| 0 | Ingen brudd oppdaget |
| 1 | Ett eller flere utdaterte mønstre funnet |

### Kjøre lokalt
Fra rotkatalogen til depotet (anbefalt):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-commit hook (valgfritt)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Dette blokkerer commits som introduserer utdaterte mønstre.

### CI-integrasjon
En GitHub Action-arbeidsflyt (`.github/workflows/markdown-cli-lint.yml`) kjører kontrollverktøyet ved hver push og pull request til `main`- og `Reactor`-grenene. Feilende jobber må fikses før merging.

### Legge til nye utdaterte mønstre
1. Åpne `lint_markdown_cli.py`.
2. Legg til en tuple `(regex, suggestion)` i listen `DEPRECATED`. Bruk en rå streng og inkluder ordgrenser `\b` der det er passende.
3. Kjør kontrollverktøyet lokalt for å verifisere deteksjon.
4. Commit og push; CI vil håndheve den nye regelen.

Eksempel på tillegg:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Tillate forklarende omtaler
Siden kun kodeblokker håndheves, kan du trygt beskrive utdaterte kommandoer i narrativ tekst. Hvis du *må* vise dem i en kodeblokk for kontrast, legg til en blokk **uten** trippel backticks (f.eks. innrykk eller sitat) eller omskriv til en pseudoform.

### Hopp over spesifikke filer (avansert)
Hvis nødvendig, plasser eldre eksempler i en separat fil utenfor depotet eller gi dem et annet filnavn mens du jobber med utkast. Bevisste hopp over oversatte kopier skjer automatisk (stier som inneholder `translations`).

### Feilsøking
| Problem | Årsak | Løsning |
|---------|-------|---------|
| Kontrollverktøyet flagger en linje du oppdaterte | Regex for bred | Begrens mønsteret med ekstra ordgrense (`\b`) eller anker |
| CI feiler, men lokalt fungerer | Ulik Python-versjon eller ikke-committede endringer | Kjør på nytt lokalt, sørg for ren arbeidskopi, sjekk arbeidsflytens Python-versjon (3.11) |
| Må midlertidig omgå | Nødretting | Utfør retting umiddelbart etterpå; vurder å bruke en midlertidig gren og oppfølgings-PR (unngå å legge til omgåelsesbrytere) |

### Begrunnelse
Å holde dokumentasjonen i tråd med *nåværende* stabile CLI-grensesnitt forhindrer friksjon i workshop, unngår forvirring hos deltakerne, og sentraliserer ytelsesmåling gjennom vedlikeholdte Python-skript i stedet for utdaterte CLI-underkommandoer.

---
Vedlikeholdes som en del av workshopens kvalitetssystem. For forbedringer (f.eks. automatiske forslag eller HTML-rapportgenerering), åpne en sak eller send inn en PR.

## 2. Eksempelvalideringsskript

`validate_samples.py` validerer alle Python-eksempelfiler for syntaks, imports og samsvar med beste praksis.

### Bruk
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

### Hva det sjekker
- ✅ Python-syntaks gyldighet
- ✅ Nødvendige imports til stede
- ✅ Implementering av feilhåndtering (verbose-modus)
- ✅ Bruk av type hints (verbose-modus)
- ✅ Funksjonsdocstrings (verbose-modus)
- ✅ SDK-referanselenker (verbose-modus)

### Miljøvariabler
- `SKIP_IMPORT_CHECK=1` - Hopper over validering av imports
- `SKIP_SYNTAX_CHECK=1` - Hopper over validering av syntaks

### Avslutningskoder
- `0` - Alle eksempler bestod validering
- `1` - Ett eller flere eksempler feilet

## 3. Eksempeltestkjører

`test_samples.py` kjører enkle tester på alle eksempler for å verifisere at de kjører uten feil.

### Bruk
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

### Forutsetninger
- Foundry Local-tjeneste kjører: `foundry service start`
- Modeller lastet: `foundry model run phi-4-mini`
- Avhengigheter installert: `pip install -r requirements.txt`

### Hva det tester
- ✅ Eksempelet kan kjøre uten kjøretidsfeil
- ✅ Nødvendig output genereres
- ✅ Riktig feilhåndtering ved feil
- ✅ Ytelse (kjøretid)

### Miljøvariabler
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modell som skal brukes til testing
- `TEST_TIMEOUT=30` - Tidsgrense per eksempel i sekunder

### Forventede feil
Noen tester kan feile hvis valgfrie avhengigheter ikke er installert (f.eks. `ragas`, `sentence-transformers`). Installer med:
```bash
pip install sentence-transformers ragas datasets
```

### Avslutningskoder
- `0` - Alle tester bestod
- `1` - En eller flere tester feilet

## 4. Benchmark Markdown-eksportør

Skript: `export_benchmark_markdown.py`

Genererer en reproduserbar ytelsestabell for et sett med modeller.

### Bruk
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Utdata
| Fil | Beskrivelse |
|-----|-------------|
| `benchmark_report.md` | Markdown-tabell (gj.snitt, p95, tokens/sek, valgfri første token) |
| `benchmark_report.json` | Rå metrikker for differensiering og historikk |

### Valg
| Flag | Beskrivelse | Standard |
|------|-------------|----------|
| `--models` | Komma-separerte modellaliaser | (påkrevd) |
| `--prompt` | Prompt brukt hver runde | (påkrevd) |
| `--rounds` | Runder per modell | 3 |
| `--output` | Markdown-utdatafil | `benchmark_report.md` |
| `--json` | JSON-utdatafil | `benchmark_report.json` |
| `--fail-on-empty` | Ikke-null exit hvis alle tester feiler | av |

Miljøvariabelen `BENCH_STREAM=1` legger til måling av første token-latens.

### Notater
- Gjenbruker `workshop_utils` for konsistent modelloppsett og caching.
- Hvis skriptet kjøres fra en annen arbeidskatalog, forsøker det å finne `workshop_utils` via alternative stier.
- For GPU-sammenligning: kjør én gang, aktiver akselerasjon via CLI-konfigurasjon, kjør på nytt og sammenlign JSON.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.