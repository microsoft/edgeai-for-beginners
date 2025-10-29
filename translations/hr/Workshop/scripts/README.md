<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T23:29:15+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "hr"
}
-->
# Skripte za radionicu

Ovaj direktorij sadrži skripte za automatizaciju i podršku koje se koriste za održavanje kvalitete i dosljednosti materijala za radionicu.

## Sadržaj

| Datoteka | Namjena |
|----------|---------|
| `lint_markdown_cli.py` | Provjerava ispravnost kodnih blokova u Markdownu kako bi se spriječilo korištenje zastarjelih naredbi Foundry Local CLI. |
| `export_benchmark_markdown.py` | Pokreće benchmark testiranje latencije za više modela i generira izvještaje u Markdown i JSON formatu. |

## 1. Provjera uzoraka Markdown CLI

`lint_markdown_cli.py` skenira sve `.md` datoteke koje nisu prijevodi kako bi pronašao zabranjene Foundry Local CLI uzorke **unutar ograničenih kodnih blokova** (``` ... ```). Informativni tekst i dalje može spominjati zastarjele naredbe radi povijesnog konteksta.

### Zastarjeli uzorci (blokirani unutar kodnih blokova)

Provjera blokira zastarjele CLI uzorke. Koristite moderne alternative.

### Potrebne zamjene
| Zastarjelo | Koristite umjesto |
|------------|-------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Skripta za benchmark + sistemski alati (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Izlazni kodovi
| Kod | Značenje |
|-----|----------|
| 0 | Nema pronađenih kršenja |
| 1 | Pronađen je jedan ili više zastarjelih uzoraka |

### Pokretanje lokalno
Iz korijena repozitorija (preporučeno):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (Opcionalno)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Ovo blokira commitove koji uvode zastarjele uzorke.

### Integracija s CI
GitHub Action workflow (`.github/workflows/markdown-cli-lint.yml`) pokreće provjeru pri svakom pushu i pull requestu na grane `main` i `Reactor`. Neuspjeli zadaci moraju se ispraviti prije spajanja.

### Dodavanje novih zastarjelih uzoraka
1. Otvorite `lint_markdown_cli.py`.
2. Dodajte tuple `(regex, suggestion)` u listu `DEPRECATED`. Koristite raw string i uključite granice riječi `\b` gdje je to prikladno.
3. Pokrenite provjeru lokalno kako biste provjerili detekciju.
4. Commitajte i pushajte; CI će provjeriti novo pravilo.

Primjer dodavanja:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Dopuštanje objašnjenja zastarjelih naredbi
Budući da se provjera odnosi samo na ograničene kodne blokove, možete sigurno opisati zastarjele naredbe u narativnom tekstu. Ako ih *morate* prikazati unutar kodnog bloka radi usporedbe, dodajte blok **bez** trostrukih backtickova (npr. uvucite ili citirajte) ili preoblikujte u pseudo oblik.

### Preskakanje određenih datoteka (Napredno)
Ako je potrebno, stavite primjere u zasebnu datoteku izvan repozitorija ili preimenujte s drugačijim ekstenzijama dok radite na nacrtu. Namjerno preskakanje za prevedene kopije je automatsko (putanje koje sadrže `translations`).

### Rješavanje problema
| Problem | Uzrok | Rješenje |
|---------|-------|----------|
| Provjera označava liniju koju ste ažurirali | Regex preširok | Sužite uzorak dodavanjem dodatne granice riječi (`\b`) ili sidra |
| CI ne uspijeva, ali lokalno prolazi | Različita verzija Pythona ili nekompletne promjene | Ponovno pokrenite lokalno, osigurajte čisto radno okruženje, provjerite verziju Pythona u workflowu (3.11) |
| Potrebno privremeno zaobići | Hitni popravak | Odmah primijenite popravak; razmislite o korištenju privremene grane i naknadnom PR-u (izbjegavajte dodavanje bypass opcija) |

### Razlozi
Održavanje dokumentacije usklađene s *trenutnim* stabilnim CLI sučeljem sprječava probleme na radionicama, izbjegava zbunjenost sudionika i centralizira mjerenje performansi kroz održavane Python skripte umjesto zastarjelih CLI podnaredbi.

---
Održava se kao dio alata za kvalitetu radionice. Za poboljšanja (npr. automatske zamjene prijedloga ili generiranje HTML izvještaja), otvorite problem ili pošaljite PR.

## 2. Skripta za validaciju uzoraka

`validate_samples.py` provjerava sve Python uzorke za sintaksu, uvoze i usklađenost s najboljim praksama.

### Upotreba
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

### Što provjerava
- ✅ Valjanost Python sintakse
- ✅ Prisutnost potrebnih uvoza
- ✅ Implementaciju rukovanja greškama (detaljan način rada)
- ✅ Korištenje tipova (detaljan način rada)
- ✅ Dokumentaciju funkcija (detaljan način rada)
- ✅ Reference na SDK (detaljan način rada)

### Varijable okruženja
- `SKIP_IMPORT_CHECK=1` - Preskoči provjeru uvoza
- `SKIP_SYNTAX_CHECK=1` - Preskoči provjeru sintakse

### Izlazni kodovi
- `0` - Svi uzorci su prošli validaciju
- `1` - Jedan ili više uzoraka nije prošlo

## 3. Skripta za testiranje uzoraka

`test_samples.py` provodi osnovne testove na svim uzorcima kako bi se provjerilo da se izvršavaju bez grešaka.

### Upotreba
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

### Preduvjeti
- Pokrenuta usluga Foundry Local: `foundry service start`
- Učitani modeli: `foundry model run phi-4-mini`
- Instalirane ovisnosti: `pip install -r requirements.txt`

### Što testira
- ✅ Uzorak se može izvršiti bez grešaka u radu
- ✅ Generira se potreban izlaz
- ✅ Ispravno rukovanje greškama u slučaju neuspjeha
- ✅ Performanse (vrijeme izvršavanja)

### Varijable okruženja
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model koji se koristi za testiranje
- `TEST_TIMEOUT=30` - Vrijeme izvršavanja po uzorku u sekundama

### Očekivani neuspjesi
Neki testovi mogu ne uspjeti ako opcionalne ovisnosti nisu instalirane (npr. `ragas`, `sentence-transformers`). Instalirajte s:
```bash
pip install sentence-transformers ragas datasets
```

### Izlazni kodovi
- `0` - Svi testovi su prošli
- `1` - Jedan ili više testova nije prošlo

## 4. Izvoz benchmarka u Markdown

Skripta: `export_benchmark_markdown.py`

Generira reproducibilnu tablicu performansi za skup modela.

### Upotreba
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Izlazi
| Datoteka | Opis |
|----------|------|
| `benchmark_report.md` | Tablica u Markdownu (prosjek, p95, tokeni/sek, opcionalno prvi token) |
| `benchmark_report.json` | Niz sirovih metrika za usporedbu i povijest |

### Opcije
| Zastavica | Opis | Zadano |
|-----------|------|--------|
| `--models` | Alias modela odvojen zarezima | (obavezno) |
| `--prompt` | Prompt korišten u svakoj rundi | (obavezno) |
| `--rounds` | Broj rundi po modelu | 3 |
| `--output` | Izlazna datoteka u Markdownu | `benchmark_report.md` |
| `--json` | Izlazna datoteka u JSON formatu | `benchmark_report.json` |
| `--fail-on-empty` | Ne-nulti izlaz ako svi benchmark testovi ne uspiju | isključeno |

Varijabla okruženja `BENCH_STREAM=1` dodaje mjerenje latencije prvog tokena.

### Napomene
- Koristi `workshop_utils` za dosljedno pokretanje modela i keširanje.
- Ako se pokreće iz drugog radnog direktorija, skripta pokušava pronaći alternativne putanje za lociranje `workshop_utils`.
- Za usporedbu GPU-a: pokrenite jednom, omogućite ubrzanje putem CLI konfiguracije, ponovno pokrenite i usporedite JSON.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.