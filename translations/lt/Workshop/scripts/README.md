<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T23:50:51+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "lt"
}
-->
# Dirbtuvių scenarijai

Šiame kataloge yra automatizavimo ir palaikymo scenarijai, naudojami siekiant užtikrinti kokybę ir nuoseklumą dirbtuvių medžiagoje.

## Turinys

| Failas | Paskirtis |
|--------|-----------|
| `lint_markdown_cli.py` | Tikrina Markdown kodų blokus, kad būtų išvengta pasenusių Foundry Local CLI komandų šablonų. |
| `export_benchmark_markdown.py` | Atlieka kelių modelių vėlinimo testą ir generuoja Markdown + JSON ataskaitas. |

## 1. Markdown CLI šablonų tikrintuvas

`lint_markdown_cli.py` tikrina visus nevertimo `.md` failus dėl neleistinų Foundry Local CLI šablonų **viduje kodų blokų** (``` ... ```). Informacinis tekstas vis dar gali paminėti pasenusias komandas istoriniais tikslais.

### Pasenę šablonai (užblokuoti kodų blokuose)

Tikrinimo įrankis blokuoja pasenusius CLI šablonus. Naudokite šiuolaikines alternatyvas.

### Reikalingi pakeitimai
| Pasenę | Naudokite vietoj |
|--------|------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Testavimo scenarijus + sistemos įrankiai (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Išeities kodai
| Kodas | Reikšmė |
|------|---------|
| 0 | Pažeidimų nerasta |
| 1 | Rasta vienas ar daugiau pasenusių šablonų |

### Paleidimas vietoje
Iš saugyklos šaknies (rekomenduojama):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit kabliukas (neprivaloma)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Tai blokuoja įsipareigojimus, kurie įveda pasenusius šablonus.

### CI integracija
GitHub Action darbo eiga (`.github/workflows/markdown-cli-lint.yml`) paleidžia tikrinimo įrankį kiekvieno stūmimo ir traukimo užklausos į `main` ir `Reactor` šakas metu. Nepavykę darbai turi būti pataisyti prieš sujungimą.

### Naujų pasenusių šablonų pridėjimas
1. Atidarykite `lint_markdown_cli.py`.
2. Pridėkite porą `(regex, suggestion)` į `DEPRECATED` sąrašą. Naudokite neapdorotą eilutę ir įtraukite žodžių ribas `\b`, kur tai tinkama.
3. Paleiskite tikrinimo įrankį vietoje, kad patikrintumėte aptikimą.
4. Įsipareigokite ir stumkite; CI užtikrins naują taisyklę.

Pavyzdys:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Leidžiami paaiškinimai
Kadangi tik kodų blokai yra tikrinami, galite saugiai aprašyti pasenusias komandas naratyviniame tekste. Jei *privalote* jas parodyti bloke kontrastui, pridėkite bloką **be** trigubų kabučių (pvz., įtraukite arba cituokite) arba perrašykite į pseudo formą.

### Konkretūs failų praleidimai (pažengusiems)
Jei reikia, įdėkite senus pavyzdžius į atskirą failą už saugyklos ribų arba pervadinkite kitokiu plėtiniu rengiant. Tyčiniai vertimų kopijų praleidimai yra automatiniai (keliai, kuriuose yra `translations`).

### Trikčių šalinimas
| Problema | Priežastis | Sprendimas |
|----------|------------|-----------|
| Tikrinimo įrankis pažymi eilutę, kurią atnaujinote | Regex per platus | Susiaurinkite šabloną su papildoma žodžio riba (`\b`) arba inkarais |
| CI nepavyksta, bet vietoje veikia | Skirtinga Python versija arba neįsipareigoti pakeitimai | Paleiskite vietoje, įsitikinkite, kad darbo aplinka švari, patikrinkite darbo eigos Python versiją (3.11) |
| Reikia laikinai apeiti | Skubus pataisymas | Nedelsiant pritaikykite pataisą; apsvarstykite laikinos šakos ir tolesnio PR naudojimą (vengti apeiti jungiklius) |

### Pagrindimas
Dokumentacijos suderinimas su *dabartiniu* stabiliu CLI paviršiumi padeda išvengti dirbtuvių trukdžių, užkerta kelią mokinių painiavai ir centralizuoja našumo matavimą per palaikomus Python scenarijus, o ne pasenusius CLI subkomandas.

---
Palaikoma kaip dirbtuvių kokybės įrankių grandinės dalis. Dėl patobulinimų (pvz., automatinio pataisymo pasiūlymų ar HTML ataskaitų generavimo) atidarykite problemą arba pateikite PR.

## 2. Pavyzdžių tikrinimo scenarijus

`validate_samples.py` tikrina visus Python pavyzdžių failus dėl sintaksės, importų ir geriausios praktikos laikymosi.

### Naudojimas
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

### Ką tikrina
- ✅ Python sintaksės galiojimas
- ✅ Reikalingi importai
- ✅ Klaidų tvarkymo įgyvendinimas (detalus režimas)
- ✅ Tipų užuominos naudojimas (detalus režimas)
- ✅ Funkcijų dokumentacija (detalus režimas)
- ✅ SDK nuorodos (detalus režimas)

### Aplinkos kintamieji
- `SKIP_IMPORT_CHECK=1` - Praleisti importų tikrinimą
- `SKIP_SYNTAX_CHECK=1` - Praleisti sintaksės tikrinimą

### Išeities kodai
- `0` - Visi pavyzdžiai praėjo tikrinimą
- `1` - Vienas ar daugiau pavyzdžių nepavyko

## 3. Pavyzdžių testavimo scenarijus

`test_samples.py` atlieka greitus testus visiems pavyzdžiams, kad patikrintų, ar jie vykdomi be klaidų.

### Naudojimas
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

### Reikalavimai
- Veikianti Foundry Local paslauga: `foundry service start`
- Įkelti modeliai: `foundry model run phi-4-mini`
- Įdiegtos priklausomybės: `pip install -r requirements.txt`

### Ką testuoja
- ✅ Pavyzdys gali būti vykdomas be vykdymo klaidų
- ✅ Sukuriamas reikalingas išvestis
- ✅ Tinkamas klaidų tvarkymas nesėkmės atveju
- ✅ Našumas (vykdymo laikas)

### Aplinkos kintamieji
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modelis, naudojamas testavimui
- `TEST_TIMEOUT=30` - Laiko limitas kiekvienam pavyzdžiui sekundėmis

### Tikėtinos nesėkmės
Kai kurie testai gali nepavykti, jei neprivalomos priklausomybės nėra įdiegtos (pvz., `ragas`, `sentence-transformers`). Įdiekite su:
```bash
pip install sentence-transformers ragas datasets
```

### Išeities kodai
- `0` - Visi testai praėjo
- `1` - Vienas ar daugiau testų nepavyko

## 4. Našumo ataskaitų eksportuotojas

Scenarijus: `export_benchmark_markdown.py`

Generuoja atkuriamą našumo lentelę modeliui rinkiniui.

### Naudojimas
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Išvestys
| Failas | Aprašymas |
|--------|-----------|
| `benchmark_report.md` | Markdown lentelė (vidurkis, p95, žodžiai/sek., pasirenkamas pirmas žodis) |
| `benchmark_report.json` | Neapdorotų metrikų masyvas skirtas palyginimui ir istorijai |

### Parinktys
| Vėliava | Aprašymas | Numatytasis |
|--------|-----------|-------------|
| `--models` | Modelių aliasai, atskirti kableliais | (privaloma) |
| `--prompt` | Kiekvieno raundo naudojamas tekstas | (privaloma) |
| `--rounds` | Raundų skaičius kiekvienam modeliui | 3 |
| `--output` | Markdown išvesties failas | `benchmark_report.md` |
| `--json` | JSON išvesties failas | `benchmark_report.json` |
| `--fail-on-empty` | Ne-nulinė išeitis, jei visi testai nepavyksta | išjungta |

Aplinkos kintamasis `BENCH_STREAM=1` prideda pirmo žodžio vėlinimo matavimą.

### Pastabos
- Naudoja `workshop_utils`, kad užtikrintų nuoseklų modelių paleidimą ir talpinimą.
- Jei paleidžiama iš kito darbo katalogo, scenarijus bando kelio alternatyvas, kad rastų `workshop_utils`.
- GPU palyginimui: paleiskite vieną kartą, įjunkite pagreitį per CLI konfigūraciją, paleiskite iš naujo ir palyginkite JSON.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.