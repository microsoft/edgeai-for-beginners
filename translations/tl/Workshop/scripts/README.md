<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T22:48:15+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "tl"
}
-->
# Mga Script ng Workshop

Ang direktoryong ito ay naglalaman ng mga automation at support script na ginagamit upang mapanatili ang kalidad at pagkakapare-pareho sa mga materyales ng Workshop.

## Nilalaman

| File | Layunin |
|------|---------|
| `lint_markdown_cli.py` | Sini-check ang mga markdown code fences upang harangan ang mga deprecated na Foundry Local CLI command patterns. |
| `export_benchmark_markdown.py` | Nagpapatakbo ng multi-model latency benchmark at naglalabas ng Markdown + JSON na ulat. |

## 1. Markdown CLI Pattern Linter

Ang `lint_markdown_cli.py` ay ini-scan ang lahat ng non-translation `.md` files para sa mga hindi pinapayagang Foundry Local CLI patterns **sa loob ng fenced code blocks** (``` ... ```). Ang mga impormasyon sa teksto ay maaari pa ring magbanggit ng mga deprecated na command para sa historical context.

### Mga Deprecated na Pattern (Hindi Pinapayagan sa Loob ng Code Fences)

Hinaharangan ng linter ang mga deprecated na CLI patterns. Gumamit ng mga modernong alternatibo.

### Kinakailangang Palitan
| Deprecated | Gamitin sa Halip |
|------------|------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark script + system tools (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Mga Exit Code
| Code | Kahulugan |
|------|-----------|
| 0 | Walang nakitang paglabag |
| 1 | May isa o higit pang deprecated na pattern na natagpuan |

### Paano Patakbuhin Lokal
Mula sa repository root (inirerekomenda):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (Opsyonal)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Ito ay humaharang sa mga commit na nagdadala ng mga deprecated na pattern.

### Integrasyon sa CI
Ang workflow ng GitHub Action (`.github/workflows/markdown-cli-lint.yml`) ay nagpapatakbo ng linter sa bawat push at pull request sa `main` at `Reactor` branches. Ang mga nabigong trabaho ay kailangang ayusin bago mag-merge.

### Pagdaragdag ng Bagong Deprecated na Pattern
1. Buksan ang `lint_markdown_cli.py`.
2. Idagdag ang tuple `(regex, suggestion)` sa `DEPRECATED` list. Gumamit ng raw string at isama ang `\b` word boundaries kung kinakailangan.
3. Patakbuhin ang linter lokal upang tiyakin ang detection.
4. I-commit at i-push; ang CI ay magpapatupad ng bagong patakaran.

Halimbawa ng karagdagang entry:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Pahintulot sa Pagbanggit ng Paliwanag
Dahil ang enforcement ay para lamang sa fenced code blocks, maaari mong ilarawan ang mga deprecated na command sa narrative text nang ligtas. Kung *kailangan* mong ipakita ang mga ito sa loob ng fence para sa pagkakaiba, magdagdag ng fenced block **nang walang** triple backticks (hal., indent o quote) o i-rewrite sa pseudo form.

### Pag-skip ng Partikular na File (Advanced)
Kung kinakailangan, ilagay ang mga legacy na halimbawa sa isang hiwalay na file sa labas ng repo o palitan ang pangalan gamit ang ibang extension habang nagda-draft. Ang mga sinadyang pag-skip para sa mga isinaling kopya ay awtomatiko (mga path na naglalaman ng `translations`).

### Pag-troubleshoot
| Isyu | Sanhi | Solusyon |
|------|-------|----------|
| Ang linter ay nag-flag ng linya na binago mo | Masyadong malawak ang regex | Palawakin ang pattern gamit ang karagdagang word boundary (`\b`) o anchors |
| Nabigo ang CI ngunit pumasa lokal | Iba't ibang bersyon ng Python o hindi na-commit na mga pagbabago | Patakbuhin muli lokal, tiyakin ang malinis na working tree, suriin ang workflow Python version (3.11) |
| Kailangang pansamantalang i-bypass | Emergency hotfix | Agad na ayusin pagkatapos; isaalang-alang ang paggamit ng pansamantalang branch at follow-up PR (iwasan ang pagdaragdag ng bypass switches) |

### Rationale
Ang pagpapanatili ng dokumentasyon na naka-align sa *kasalukuyang* stable CLI surface ay pumipigil sa workshop friction, iniiwasan ang pagkalito ng mga learner, at sentralisado ang performance measurement sa pamamagitan ng maintained Python scripts sa halip na drifting CLI subcommands.

---
Pinapanatili bilang bahagi ng workshop quality toolchain. Para sa mga pagpapahusay (hal., auto-fixing suggestions o HTML report generation), magbukas ng isyu o magsumite ng PR.

## 2. Sample Validation Script

Ang `validate_samples.py` ay nagva-validate ng lahat ng Python sample files para sa syntax, imports, at pagsunod sa best practices.

### Paggamit
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

### Ano ang Sini-check
- ✅ Validity ng Python syntax
- ✅ Presensya ng kinakailangang imports
- ✅ Implementasyon ng error handling (verbose mode)
- ✅ Paggamit ng type hints (verbose mode)
- ✅ Function docstrings (verbose mode)
- ✅ Mga link sa SDK reference (verbose mode)

### Mga Environment Variable
- `SKIP_IMPORT_CHECK=1` - I-skip ang import validation
- `SKIP_SYNTAX_CHECK=1` - I-skip ang syntax validation

### Mga Exit Code
- `0` - Lahat ng samples ay pumasa sa validation
- `1` - Isa o higit pang samples ang nabigo

## 3. Sample Test Runner

Ang `test_samples.py` ay nagpapatakbo ng smoke tests sa lahat ng samples upang tiyakin na ito ay tumatakbo nang walang error.

### Paggamit
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

### Mga Kinakailangan
- Foundry Local service na tumatakbo: `foundry service start`
- Mga modelong naka-load: `foundry model run phi-4-mini`
- Mga dependency na naka-install: `pip install -r requirements.txt`

### Ano ang Tini-test
- ✅ Ang sample ay maaaring tumakbo nang walang runtime errors
- ✅ Ang kinakailangang output ay nalilikha
- ✅ Tamang error handling sa failure
- ✅ Performance (execution time)

### Mga Environment Variable
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modelong gagamitin para sa testing
- `TEST_TIMEOUT=30` - Timeout kada sample sa segundo

### Mga Inaasahang Pagkabigo
Ang ilang tests ay maaaring mabigo kung ang mga opsyonal na dependency ay hindi naka-install (hal., `ragas`, `sentence-transformers`). I-install gamit ang:
```bash
pip install sentence-transformers ragas datasets
```

### Mga Exit Code
- `0` - Lahat ng tests ay pumasa
- `1` - Isa o higit pang tests ang nabigo

## 4. Benchmark Markdown Exporter

Script: `export_benchmark_markdown.py`

Nag-generate ng reproducible performance table para sa isang set ng mga modelo.

### Paggamit
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Mga Output
| File | Deskripsyon |
|------|-------------|
| `benchmark_report.md` | Markdown table (avg, p95, tokens/sec, optional first token) |
| `benchmark_report.json` | Raw metrics array para sa diffing & history |

### Mga Opsyon
| Flag | Deskripsyon | Default |
|------|-------------|---------|
| `--models` | Comma-separated na model aliases | (required) |
| `--prompt` | Prompt na ginamit bawat round | (required) |
| `--rounds` | Rounds bawat modelo | 3 |
| `--output` | Markdown output file | `benchmark_report.md` |
| `--json` | JSON output file | `benchmark_report.json` |
| `--fail-on-empty` | Non-zero exit kung lahat ng benchmarks ay nabigo | off |

Ang environment variable na `BENCH_STREAM=1` ay nagdadagdag ng first token latency measurement.

### Mga Tala
- Ginagamit ang `workshop_utils` para sa consistent na model bootstrap & caching.
- Kung patatakbuhin mula sa ibang working directory, sinusubukan ng script ang path fallbacks upang mahanap ang `workshop_utils`.
- Para sa GPU comparison: patakbuhin nang isang beses, i-enable ang acceleration sa pamamagitan ng CLI config, i-re-run at i-diff ang JSON.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na awtoritatibong pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.