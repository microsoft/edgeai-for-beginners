<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T22:53:38+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "sw"
}
-->
# Hati za Warsha

Hii saraka ina hati za kiotomatiki na msaada zinazotumika kudumisha ubora na uthabiti katika nyenzo za Warsha.

## Yaliyomo

| Faili | Kusudi |
|------|---------|
| `lint_markdown_cli.py` | Hukagua uzio wa nambari ya markdown ili kuzuia mifumo ya amri ya Foundry Local CLI iliyopitwa na wakati. |
| `export_benchmark_markdown.py` | Inaendesha kipimo cha muda wa modeli nyingi na kutoa ripoti za Markdown + JSON. |

## 1. Kagua Mifumo ya Markdown CLI

`lint_markdown_cli.py` huchunguza faili zote za `.md` zisizo za tafsiri kwa mifumo ya Foundry Local CLI iliyopitwa na wakati **ndani ya uzio wa nambari** (``` ... ```). Maandishi ya maelezo bado yanaweza kutaja amri zilizopitwa na wakati kwa muktadha wa kihistoria.

### Mifumo Iliyopitwa na Wakati (Imezuiwa Ndani ya Uzio wa Nambari)

Kagua inazuia mifumo ya CLI iliyopitwa na wakati. Tumia mbadala za kisasa badala yake.

### Mbadala Unaohitajika
| Iliyopitwa na Wakati | Tumia Badala Yake |
|-----------------------|-------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Hati ya kipimo + zana za mfumo (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Nambari za Kutoka
| Nambari | Maana |
|--------|-------|
| 0 | Hakuna ukiukaji uliogunduliwa |
| 1 | Mifumo moja au zaidi iliyopitwa na wakati imepatikana |

### Kuendesha Kwa Nje
Kutoka kwenye mzizi wa hazina (inapendekezwa):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Kifaa cha Pre-Commit (Hiari)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Hii inazuia ahadi zinazoanzisha mifumo iliyopitwa na wakati.

### Ujumuishaji wa CI
Mfumo wa kazi wa GitHub Action (`.github/workflows/markdown-cli-lint.yml`) huendesha kagua kwenye kila kushinikiza na ombi la kuvuta kwa matawi ya `main` na `Reactor`. Kazi zilizoshindwa lazima zirekebishwe kabla ya kuunganishwa.

### Kuongeza Mifumo Mpya Iliyopitwa na Wakati
1. Fungua `lint_markdown_cli.py`.
2. Ongeza jozi `(regex, suggestion)` kwenye orodha ya `DEPRECATED`. Tumia kamba mbichi na ujumuisha mipaka ya neno `\b` inapofaa.
3. Endesha kagua kwa nje ili kuthibitisha kugundua.
4. Ahidi na kushinikiza; CI itatekeleza sheria mpya.

Mfano wa nyongeza:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Kuruhusu Kutajwa kwa Maelezo
Kwa sababu uzio wa nambari pekee unatekelezwa, unaweza kuelezea amri zilizopitwa na wakati katika maandishi ya maelezo kwa usalama. Ikiwa *lazima* uonyeshe ndani ya uzio kwa kulinganisha, ongeza uzio wa nambari **bila** alama tatu za nyuma (mfano, weka nafasi au nukuu) au andika upya kwa fomu ya bandia.

### Kuruka Faili Maalum (Juu)
Ikiwa inahitajika, weka mifano ya urithi kwenye faili tofauti nje ya hazina au ubadilishe jina na kiendelezi tofauti wakati wa kuandika. Kuruka kwa makusudi kwa nakala za tafsiri ni kiotomatiki (njia zinazojumuisha `translations`).

### Utatuzi wa Matatizo
| Tatizo | Sababu | Suluhisho |
|--------|--------|-----------|
| Kagua inaonyesha mstari uliosasishwa | Regex pana sana | Punguza muundo na mipaka ya neno ya ziada (`\b`) au nanga |
| CI inashindwa lakini nje inafaulu | Toleo tofauti la Python au mabadiliko yasiyoshinikizwa | Endesha tena kwa nje, hakikisha mti wa kazi safi, angalia toleo la Python la mfumo wa kazi (3.11) |
| Haja ya kupita kwa muda | Marekebisho ya dharura | Tumia marekebisho mara moja baada ya; fikiria kutumia tawi la muda na PR ya kufuatilia (epuka kuongeza swichi za kupita) |

### Sababu
Kudumisha nyaraka zinazolingana na uso wa CLI *wa sasa* thabiti huzuia msuguano wa warsha, kuepuka mkanganyiko wa wanafunzi, na kuimarisha kipimo cha utendaji kupitia hati za Python zinazodumishwa badala ya amri za CLI zinazobadilika.

---
Inadumishwa kama sehemu ya mnyororo wa zana za ubora wa warsha. Kwa maboresho (mfano, mapendekezo ya kurekebisha kiotomatiki au kizazi cha ripoti ya HTML), fungua suala au wasilisha PR.

## 2. Hati ya Uthibitishaji wa Mfano

`validate_samples.py` inathibitisha faili zote za mfano za Python kwa uhalali wa sintaksia, uagizaji, na uzingatiaji wa mazoea bora.

### Matumizi
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

### Kile Inachokagua
- ✅ Uhalali wa sintaksia ya Python
- ✅ Uagizaji unaohitajika upo
- ✅ Utekelezaji wa kushughulikia makosa (hali ya maelezo)
- ✅ Matumizi ya vidokezo vya aina (hali ya maelezo)
- ✅ Maelezo ya kazi (hali ya maelezo)
- ✅ Viungo vya marejeleo ya SDK (hali ya maelezo)

### Vigezo vya Mazingira
- `SKIP_IMPORT_CHECK=1` - Ruka uthibitishaji wa uagizaji
- `SKIP_SYNTAX_CHECK=1` - Ruka uthibitishaji wa sintaksia

### Nambari za Kutoka
- `0` - Sampuli zote zimepita uthibitishaji
- `1` - Sampuli moja au zaidi zimeshindwa

## 3. Hati ya Mtihani wa Mfano

`test_samples.py` inaendesha majaribio ya moshi kwenye sampuli zote ili kuthibitisha zinafanya kazi bila makosa.

### Matumizi
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

### Mahitaji ya Awali
- Huduma ya Foundry Local inayoendesha: `foundry service start`
- Miundo imepakiwa: `foundry model run phi-4-mini`
- Mahitaji yamewekwa: `pip install -r requirements.txt`

### Kile Inachojaribu
- ✅ Mfano unaweza kutekelezwa bila makosa ya wakati wa kukimbia
- ✅ Pato linalohitajika linazalishwa
- ✅ Kushughulikia makosa ipasavyo wakati wa kushindwa
- ✅ Utendaji (muda wa utekelezaji)

### Vigezo vya Mazingira
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Mfano wa kutumia kwa majaribio
- `TEST_TIMEOUT=30` - Muda wa kusubiri kwa kila sampuli kwa sekunde

### Kushindwa Kunakotarajiwa
Baadhi ya majaribio yanaweza kushindwa ikiwa utegemezi wa hiari haujawekwa (mfano, `ragas`, `sentence-transformers`). Weka kwa:
```bash
pip install sentence-transformers ragas datasets
```

### Nambari za Kutoka
- `0` - Majaribio yote yamepita
- `1` - Majaribio moja au zaidi yameshindwa

## 4. Mzalishaji wa Markdown ya Kipimo

Hati: `export_benchmark_markdown.py`

Inazalisha jedwali la utendaji linaloweza kurudiwa kwa seti ya miundo.

### Matumizi
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Matokeo
| Faili | Maelezo |
|-------|---------|
| `benchmark_report.md` | Jedwali la Markdown (wastani, p95, tokeni/sec, tokeni ya kwanza ya hiari) |
| `benchmark_report.json` | Mfululizo wa vipimo ghafi kwa kulinganisha & historia |

### Chaguo
| Bendera | Maelezo | Chaguo-msingi |
|---------|---------|--------------|
| `--models` | Majina ya modeli yaliyotenganishwa kwa koma | (inayohitajika) |
| `--prompt` | Swali linalotumika kila raundi | (inayohitajika) |
| `--rounds` | Raundi kwa kila modeli | 3 |
| `--output` | Faili ya pato la Markdown | `benchmark_report.md` |
| `--json` | Faili ya pato la JSON | `benchmark_report.json` |
| `--fail-on-empty` | Kutoka isiyo ya sifuri ikiwa vipimo vyote vinashindwa | imezimwa |

Kigezo cha mazingira `BENCH_STREAM=1` kinaongeza kipimo cha muda wa tokeni ya kwanza.

### Vidokezo
- Inatumia tena `workshop_utils` kwa kuanzisha modeli na kuhifadhi kwa uthabiti.
- Ikiwa imeendeshwa kutoka saraka tofauti ya kazi, hati inajaribu njia za kurudi nyuma ili kupata `workshop_utils`.
- Kwa kulinganisha GPU: endesha mara moja, wezesha kasi kupitia usanidi wa CLI, endesha tena na linganisha JSON.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.