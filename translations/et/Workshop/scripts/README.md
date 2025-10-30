<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-29T00:02:00+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "et"
}
-->
# Töötuba Skriptid

See kataloog sisaldab automatiseerimis- ja tugiskripte, mis aitavad säilitada kvaliteeti ja järjepidevust töötuba materjalides.

## Sisu

| Fail | Eesmärk |
|------|---------|
| `lint_markdown_cli.py` | Kontrollib markdowni koodiplokke, et vältida vananenud Foundry Local CLI käsumustrite kasutamist. |
| `export_benchmark_markdown.py` | Käitab mitme mudeli latentsuse võrdlusuuringut ja genereerib Markdown + JSON aruandeid. |

## 1. Markdown CLI mustrite kontrollija

`lint_markdown_cli.py` skaneerib kõiki mitte-tõlke `.md` faile keelatud Foundry Local CLI mustrite osas **fenceeritud koodiplokkides** (``` ... ```). Informatiivses tekstis võib endiselt mainida vananenud käske ajaloolise konteksti jaoks.

### Vananenud mustrid (blokeeritud koodiplokkides)

Kontrollija blokeerib vananenud CLI mustrid. Kasuta kaasaegseid alternatiive.

### Nõutavad asendused
| Vananenud | Kasuta Selle Asemel |
|-----------|---------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Võrdlusuuringu skript + süsteemi tööriistad (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Väljumiskoodid
| Kood | Tähendus |
|------|----------|
| 0 | Rikkumisi ei tuvastatud |
| 1 | Leiti üks või mitu vananenud mustrit |

### Kohalik käitamine
Käita repo juurest (soovitatav):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Eelkommiti konks (valikuline)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
See blokeerib kommid, mis sisaldavad vananenud mustreid.

### CI integratsioon
GitHub Action töövoog (`.github/workflows/markdown-cli-lint.yml`) käitab kontrollija iga `main` ja `Reactor` haru pushi ja pull request'i korral. Ebaõnnestunud tööd tuleb parandada enne ühendamist.

### Uute vananenud mustrite lisamine
1. Ava `lint_markdown_cli.py`.
2. Lisa tuple `(regex, suggestion)` `DEPRECATED` nimekirja. Kasuta raw stringi ja lisa `\b` sõna piirid, kui vajalik.
3. Käita kontrollija kohalikult, et veenduda tuvastamises.
4. Kommiti ja pushi; CI rakendab uue reegli.

Näide lisamisest:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Selgitavate mainimiste lubamine
Kuna ainult fenceeritud koodiplokke kontrollitakse, võib vananenud käske kirjeldada narratiivses tekstis turvaliselt. Kui *pead* neid näitama plokis kontrasti jaoks, lisa plokk **ilma** kolmekordsete tagurpidi jutumärkideta (nt. indent või tsitaat) või kirjuta ümber pseudo vormi.

### Konkreetsete failide vahelejätmine (edasijõudnutele)
Kui vaja, paiguta vananenud näited eraldi faili väljaspool repo või nimeta ümber teise laiendiga koostamise ajal. Tõlgitud koopiate tahtlik vahelejätmine toimub automaatselt (teed, mis sisaldavad `translations`).

### Tõrkeotsing
| Probleem | Põhjus | Lahendus |
|----------|--------|---------|
| Kontrollija märgib rea, mida uuendasid | Regex liiga lai | Kitsenda mustrit täiendava sõna piiriga (`\b`) või ankruga |
| CI ebaõnnestub, kuid kohalikult läbib | Erinev Python versioon või salvestamata muudatused | Käita uuesti kohalikult, veendu puhtas tööpuus, kontrolli töövoo Python versiooni (3.11) |
| Vajad ajutist möödumist | Kiirparandus | Rakenda parandus kohe pärast; kaalu ajutise haru ja järgneva PR-i kasutamist (väldi möödumisnuppude lisamist) |

### Põhjendus
Dokumentatsiooni joondamine *praeguse* stabiilse CLI pinnaga väldib töötuba takistusi, hoiab ära õppijate segaduse ja tsentraliseerib jõudluse mõõtmise hooldatud Python skriptide kaudu, mitte hajutatud CLI alamkäskude kaudu.

---
Hooldatud osana töötuba kvaliteedi tööriistaketist. Täienduste jaoks (nt. automaatne paranduste pakkumine või HTML aruande genereerimine) ava probleem või esita PR.

## 2. Näidiste valideerimise skript

`validate_samples.py` valideerib kõik Python näidiste failid süntaksi, importide ja parimate praktikate järgimise osas.

### Kasutamine
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

### Mida see kontrollib
- ✅ Python süntaksi kehtivus
- ✅ Vajalikud importid olemas
- ✅ Veakäsitluse rakendamine (detailne režiim)
- ✅ Tüüpide vihjete kasutamine (detailne režiim)
- ✅ Funktsioonide docstringid (detailne režiim)
- ✅ SDK viited (detailne režiim)

### Keskkonnamuutujad
- `SKIP_IMPORT_CHECK=1` - Jäta importide valideerimine vahele
- `SKIP_SYNTAX_CHECK=1` - Jäta süntaksi valideerimine vahele

### Väljumiskoodid
- `0` - Kõik näidised läbisid valideerimise
- `1` - Üks või mitu näidist ebaõnnestus

## 3. Näidiste testimise skript

`test_samples.py` käitab suitsuteste kõigil näidistel, et kontrollida nende veatult käivitamist.

### Kasutamine
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

### Eeltingimused
- Foundry Local teenus töötab: `foundry service start`
- Mudelid laaditud: `foundry model run phi-4-mini`
- Sõltuvused paigaldatud: `pip install -r requirements.txt`

### Mida see testib
- ✅ Näidis saab käivituda ilma käitusvigadeta
- ✅ Vajalik väljund genereeritakse
- ✅ Õige veakäsitlus tõrke korral
- ✅ Jõudlus (käitusaeg)

### Keskkonnamuutujad
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Mudel, mida testimiseks kasutada
- `TEST_TIMEOUT=30` - Aegumine näidise kohta sekundites

### Oodatavad ebaõnnestumised
Mõned testid võivad ebaõnnestuda, kui valikulised sõltuvused pole paigaldatud (nt. `ragas`, `sentence-transformers`). Paigalda:
```bash
pip install sentence-transformers ragas datasets
```

### Väljumiskoodid
- `0` - Kõik testid läbisid
- `1` - Üks või mitu testi ebaõnnestus

## 4. Võrdlusuuringu Markdown eksportija

Skript: `export_benchmark_markdown.py`

Genereerib korduvkasutatava jõudlustabeli mudelite komplekti jaoks.

### Kasutamine
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Väljundid
| Fail | Kirjeldus |
|------|-----------|
| `benchmark_report.md` | Markdown tabel (keskmine, p95, tokenid/sekundis, valikuline esimene token) |
| `benchmark_report.json` | Toormõõdikute massiiv võrdlemiseks ja ajaloo jaoks |

### Valikud
| Lipp | Kirjeldus | Vaikimisi |
|------|-----------|----------|
| `--models` | Komaga eraldatud mudelite aliased | (nõutav) |
| `--prompt` | Iga vooru jaoks kasutatav prompt | (nõutav) |
| `--rounds` | Voorude arv mudeli kohta | 3 |
| `--output` | Markdown väljundfail | `benchmark_report.md` |
| `--json` | JSON väljundfail | `benchmark_report.json` |
| `--fail-on-empty` | Mitte-null väljumine, kui kõik võrdlusuuringud ebaõnnestuvad | välja lülitatud |

Keskkonnamuutuja `BENCH_STREAM=1` lisab esimese tokeni latentsuse mõõtmise.

### Märkused
- Kasutab `workshop_utils` mudeli alglaadimise ja vahemälu järjepidevuse tagamiseks.
- Kui käitatakse teisest töökaustast, proovib skript leida `workshop_utils` alternatiivseid teid.
- GPU võrdluse jaoks: käita üks kord, lubada kiirendus CLI konfiguratsiooni kaudu, käitada uuesti ja võrrelda JSON-i.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.