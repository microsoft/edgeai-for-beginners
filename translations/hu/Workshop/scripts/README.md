# Workshop Szkriptek

Ez a könyvtár automatizálási és támogatási szkripteket tartalmaz, amelyek a Workshop anyagok minőségének és konzisztenciájának fenntartására szolgálnak.

## Tartalom

| Fájl | Cél |
|------|-----|
| `lint_markdown_cli.py` | Ellenőrzi a markdown kódfüggvényeket, hogy blokkolja az elavult Foundry Local CLI parancsmintákat. |
| `export_benchmark_markdown.py` | Több modell késleltetési benchmarkot futtat, és Markdown + JSON jelentéseket generál. |

## 1. Markdown CLI Minta Ellenőrző

A `lint_markdown_cli.py` szkenneli az összes nem fordított `.md` fájlt a nem engedélyezett Foundry Local CLI minták után **keretezett kódrészletekben** (``` ... ```). Az információs szöveg továbbra is említheti az elavult parancsokat történelmi kontextusban.

### Elavult minták (blokkolva a kódrészletekben)

Az ellenőrző blokkolja az elavult CLI mintákat. Használj modern alternatívákat helyettük.

### Kötelező cserék
| Elavult | Használj helyette |
|---------|-------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark szkript + rendszereszközök (`Feladatkezelő`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Kilépési kódok
| Kód | Jelentés |
|-----|----------|
| 0 | Nincs észlelt szabálysértés |
| 1 | Egy vagy több elavult minta található |

### Helyi futtatás
A repository gyökérkönyvtárából (ajánlott):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (Opcionális)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Ez blokkolja az elavult mintákat bevezető commitokat.

### CI Integráció
Egy GitHub Action munkafolyamat (`.github/workflows/markdown-cli-lint.yml`) futtatja az ellenőrzőt minden `main` és `Reactor` ágra történő push és pull request esetén. A hibás munkák javítása kötelező a merge előtt.

### Új elavult minták hozzáadása
1. Nyisd meg a `lint_markdown_cli.py` fájlt.
2. Adj hozzá egy tuple-t `(regex, suggestion)` a `DEPRECATED` listához. Használj nyers stringet, és tartalmazz `\b` szóhatárokat, ahol szükséges.
3. Futtasd az ellenőrzőt helyileg, hogy ellenőrizd a detektálást.
4. Commitolj és pusholj; a CI érvényesíti az új szabályt.

Példa hozzáadás:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Magyarázó említések engedélyezése
Mivel csak a keretezett kódrészletek vannak érvényesítve, elavult parancsokat biztonságosan leírhatsz narratív szövegben. Ha *muszáj* megmutatni őket keretben kontrasztként, adj meg egy keretezett blokkot **három backtick nélkül** (pl. behúzás vagy idézet), vagy írd át pszeudo formára.

### Specifikus fájlok kihagyása (Haladó)
Ha szükséges, helyezd el a régi példákat egy külön fájlban a repo-n kívül, vagy nevezd át más kiterjesztéssel a tervezés során. A fordított példányok szándékos kihagyása automatikus (az `translations` tartalmú útvonalak esetén).

### Hibakeresés
| Probléma | Ok | Megoldás |
|----------|----|----------|
| Az ellenőrző megjelöl egy általad frissített sort | Túl általános regex | Szűkítsd a mintát további szóhatárral (`\b`) vagy horgonyokkal |
| CI hibát jelez, de helyileg nem | Eltérő Python verzió vagy nem commitolt változások | Futtasd újra helyileg, győződj meg róla, hogy tiszta a munkaterület, ellenőrizd a munkafolyamat Python verzióját (3.11) |
| Ideiglenes megkerülés szükséges | Sürgős javítás | Azonnal alkalmazd a javítást; fontold meg egy ideiglenes branch és utólagos PR használatát (kerüld a megkerülő kapcsolók hozzáadását) |

### Indoklás
A dokumentáció *aktuális* stabil CLI felülethez való igazítása csökkenti a workshop frusztrációt, elkerüli a tanulók zavartságát, és központosítja a teljesítménymérést karbantartott Python szkripteken keresztül, a sodródó CLI alparancsok helyett.

---
A workshop minőségi eszközláncának részeként karbantartva. Fejlesztésekhez (pl. automatikus javítási javaslatok vagy HTML jelentés generálás), nyiss egy issue-t vagy küldj be egy PR-t.

## 2. Példa Ellenőrző Szkript

A `validate_samples.py` ellenőrzi az összes Python példa fájlt szintaxis, importok és legjobb gyakorlatok betartása szempontjából.

### Használat
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

### Mit ellenőriz
- ✅ Python szintaxis érvényessége
- ✅ Szükséges importok jelenléte
- ✅ Hibakezelés megvalósítása (részletes mód)
- ✅ Típusjelölések használata (részletes mód)
- ✅ Funkció docstringek (részletes mód)
- ✅ SDK referencia linkek (részletes mód)

### Környezeti változók
- `SKIP_IMPORT_CHECK=1` - Import ellenőrzés kihagyása
- `SKIP_SYNTAX_CHECK=1` - Szintaxis ellenőrzés kihagyása

### Kilépési kódok
- `0` - Minden példa megfelelt az ellenőrzésen
- `1` - Egy vagy több példa nem felelt meg

## 3. Példa Teszt Futtató

A `test_samples.py` füstteszteket futtat az összes példán, hogy ellenőrizze, hibamentesen végrehajthatók-e.

### Használat
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

### Előfeltételek
- Foundry Local szolgáltatás fut: `foundry service start`
- Modellek betöltve: `foundry model run phi-4-mini`
- Függőségek telepítve: `pip install -r requirements.txt`

### Mit tesztel
- ✅ A példa hibamentesen végrehajtható
- ✅ A szükséges kimenet generálva van
- ✅ Megfelelő hibakezelés hiba esetén
- ✅ Teljesítmény (végrehajtási idő)

### Környezeti változók
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Teszteléshez használt modell
- `TEST_TIMEOUT=30` - Időtúllépés mintánként másodpercben

### Várható hibák
Néhány teszt sikertelen lehet, ha opcionális függőségek nincsenek telepítve (pl. `ragas`, `sentence-transformers`). Telepítés:
```bash
pip install sentence-transformers ragas datasets
```

### Kilépési kódok
- `0` - Minden teszt sikeres
- `1` - Egy vagy több teszt sikertelen

## 4. Benchmark Markdown Exportáló

Szkript: `export_benchmark_markdown.py`

Reprodukálható teljesítménytáblázatot generál modellek számára.

### Használat
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Kimenetek
| Fájl | Leírás |
|------|--------|
| `benchmark_report.md` | Markdown táblázat (átlag, p95, tokenek/másodperc, opcionális első token) |
| `benchmark_report.json` | Nyers metrikák tömbje összehasonlításhoz és történethez |

### Opciók
| Flag | Leírás | Alapértelmezett |
|------|--------|-----------------|
| `--models` | Modell aliasok vesszővel elválasztva | (kötelező) |
| `--prompt` | Minden körben használt prompt | (kötelező) |
| `--rounds` | Körök száma modellenként | 3 |
| `--output` | Markdown kimeneti fájl | `benchmark_report.md` |
| `--json` | JSON kimeneti fájl | `benchmark_report.json` |
| `--fail-on-empty` | Nem nulla kilépés, ha minden benchmark sikertelen | kikapcsolva |

A `BENCH_STREAM=1` környezeti változó hozzáadja az első token késleltetési mérést.

### Megjegyzések
- Újrahasználja a `workshop_utils`-t a következetes modell bootstrap és cache érdekében.
- Ha más munkakönyvtárból futtatják, a szkript útvonal visszaeséseket próbál meg a `workshop_utils` megtalálásához.
- GPU összehasonlításhoz: futtasd egyszer, engedélyezd a gyorsítást a CLI konfigurációval, futtasd újra, és hasonlítsd össze a JSON-t.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.