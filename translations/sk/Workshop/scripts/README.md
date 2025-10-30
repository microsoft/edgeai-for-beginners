<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T23:08:33+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "sk"
}
-->
# Skripty workshopu

Tento adresár obsahuje automatizačné a podporné skripty používané na udržanie kvality a konzistencie materiálov workshopu.

## Obsah

| Súbor | Účel |
|-------|------|
| `lint_markdown_cli.py` | Kontroluje bloky kódu v markdown súboroch, aby zabránil používanie zastaraných príkazových vzorov Foundry Local CLI. |
| `export_benchmark_markdown.py` | Spúšťa benchmark latencie pre viacero modelov a generuje správy vo formáte Markdown + JSON. |

## 1. Kontrola vzorov Markdown CLI

`lint_markdown_cli.py` prehľadáva všetky `.md` súbory, ktoré nie sú prekladmi, a hľadá nepovolené vzory príkazov Foundry Local CLI **v rámci ohraničených blokov kódu** (``` ... ```). Informačný text môže stále spomínať zastarané príkazy pre historický kontext.

### Zastarané vzory (blokované v rámci blokov kódu)

Kontrola blokuje zastarané vzory CLI. Používajte moderné alternatívy.

### Požadované náhrady
| Zastarané | Používajte namiesto |
|-----------|---------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Skript benchmarku + systémové nástroje (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Výstupné kódy
| Kód | Význam |
|-----|--------|
| 0 | Neboli zistené žiadne porušenia |
| 1 | Boli nájdené jeden alebo viac zastaraných vzorov |

### Spustenie lokálne
Z koreňového adresára repozitára (odporúčané):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-commit hook (voliteľné)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Toto blokuje commity, ktoré zavádzajú zastarané vzory.

### Integrácia CI
Workflow GitHub Action (`.github/workflows/markdown-cli-lint.yml`) spúšťa kontrolu pri každom pushi a pull requeste do vetiev `main` a `Reactor`. Zlyhané úlohy musia byť opravené pred zlúčením.

### Pridanie nových zastaraných vzorov
1. Otvorte `lint_markdown_cli.py`.
2. Pridajte dvojicu `(regex, suggestion)` do zoznamu `DEPRECATED`. Použite surový reťazec a zahrňte hranice slov `\b`, kde je to vhodné.
3. Spustite kontrolu lokálne na overenie detekcie.
4. Commitnite a pushnite; CI bude vynucovať nové pravidlo.

Príklad pridania:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Povolenie vysvetľujúcich zmienok
Keďže sa kontrolujú iba ohraničené bloky kódu, môžete bezpečne popísať zastarané príkazy v naratívnom texte. Ak *musíte* ukázať príkazy v ohraničenom bloku pre kontrast, pridajte blok bez trojitých spätných úvodzoviek (napr. odsadenie alebo citáciu) alebo ich prepíšte do pseudo formy.

### Preskočenie konkrétnych súborov (pokročilé)
Ak je to potrebné, umiestnite staršie príklady do samostatného súboru mimo repozitára alebo ich premenujte na iné rozšírenie počas prípravy. Úmyselné preskočenia pre preložené kópie sú automatické (cesty obsahujúce `translations`).

### Riešenie problémov
| Problém | Príčina | Riešenie |
|---------|---------|----------|
| Kontrola označí riadok, ktorý ste upravili | Regex je príliš všeobecný | Zúžte vzor pridaním ďalších hraníc slov (`\b`) alebo kotiev |
| CI zlyhá, ale lokálne prejde | Rôzna verzia Pythonu alebo neuložené zmeny | Spustite lokálne znova, uistite sa, že pracovný strom je čistý, skontrolujte verziu Pythonu vo workflow (3.11) |
| Potrebujete dočasne obísť | Núdzová oprava | Aplikujte opravu okamžite po tom; zvážte použitie dočasnej vetvy a následný PR (vyhnite sa pridávaniu obchádzkových prepínačov) |

### Dôvody
Udržiavanie dokumentácie v súlade s *aktuálnym* stabilným rozhraním CLI zabraňuje problémom na workshope, vyhýba sa zmätku účastníkov a centralizuje meranie výkonu prostredníctvom udržiavaných Python skriptov namiesto zastaraných príkazov CLI.

---
Udržiavané ako súčasť nástrojového reťazca kvality workshopu. Pre vylepšenia (napr. automatické opravy návrhov alebo generovanie HTML správ) otvorte issue alebo odošlite PR.

## 2. Skript na validáciu vzoriek

`validate_samples.py` overuje všetky Python súbory vzoriek z hľadiska syntaxe, importov a dodržiavania najlepších praktík.

### Použitie
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

### Čo kontroluje
- ✅ Platnosť syntaxe Pythonu
- ✅ Prítomnosť požadovaných importov
- ✅ Implementáciu spracovania chýb (podrobný režim)
- ✅ Použitie typových anotácií (podrobný režim)
- ✅ Dokumentáciu funkcií (podrobný režim)
- ✅ Odkazy na SDK (podrobný režim)

### Environmentálne premenné
- `SKIP_IMPORT_CHECK=1` - Preskočiť validáciu importov
- `SKIP_SYNTAX_CHECK=1` - Preskočiť validáciu syntaxe

### Výstupné kódy
- `0` - Všetky vzorky prešli validáciou
- `1` - Jedna alebo viac vzoriek zlyhala

## 3. Skript na testovanie vzoriek

`test_samples.py` spúšťa testy na všetkých vzorkách, aby overil, že sa vykonávajú bez chýb.

### Použitie
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

### Predpoklady
- Spustená služba Foundry Local: `foundry service start`
- Načítané modely: `foundry model run phi-4-mini`
- Nainštalované závislosti: `pip install -r requirements.txt`

### Čo testuje
- ✅ Vzorka sa môže vykonať bez runtime chýb
- ✅ Generuje požadovaný výstup
- ✅ Správne spracovanie chýb pri zlyhaní
- ✅ Výkon (čas vykonania)

### Environmentálne premenné
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model na testovanie
- `TEST_TIMEOUT=30` - Časový limit na vzorku v sekundách

### Očakávané zlyhania
Niektoré testy môžu zlyhať, ak nie sú nainštalované voliteľné závislosti (napr. `ragas`, `sentence-transformers`). Nainštalujte ich pomocou:
```bash
pip install sentence-transformers ragas datasets
```

### Výstupné kódy
- `0` - Všetky testy prešli
- `1` - Jeden alebo viac testov zlyhalo

## 4. Exportér benchmarkov do Markdownu

Skript: `export_benchmark_markdown.py`

Generuje reprodukovateľnú tabuľku výkonu pre sadu modelov.

### Použitie
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Výstupy
| Súbor | Popis |
|-------|-------|
| `benchmark_report.md` | Tabuľka vo formáte Markdown (priemer, p95, tokeny/sekunda, voliteľne prvý token) |
| `benchmark_report.json` | Surové metriky pre porovnanie a históriu |

### Možnosti
| Parameter | Popis | Predvolená hodnota |
|-----------|-------|--------------------|
| `--models` | Modelové aliasy oddelené čiarkou | (povinné) |
| `--prompt` | Prompt použitý v každom kole | (povinné) |
| `--rounds` | Počet kôl na model | 3 |
| `--output` | Výstupný súbor Markdown | `benchmark_report.md` |
| `--json` | Výstupný súbor JSON | `benchmark_report.json` |
| `--fail-on-empty` | Ne-nulový výstup, ak všetky benchmarky zlyhajú | vypnuté |

Environmentálna premenná `BENCH_STREAM=1` pridáva meranie latencie prvého tokenu.

### Poznámky
- Používa `workshop_utils` na konzistentné spúšťanie modelov a cachovanie.
- Ak je spustený z iného pracovného adresára, skript sa pokúsi nájsť `workshop_utils` pomocou alternatívnych ciest.
- Pre porovnanie GPU: spustite raz, aktivujte akceleráciu cez CLI konfiguráciu, spustite znova a porovnajte JSON.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.