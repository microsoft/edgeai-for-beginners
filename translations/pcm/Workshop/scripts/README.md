# Workshop Scripts

Dis folder get automation and support scripts wey dem dey use to keep quality and consistency for Workshop materials.

## Contents

| File | Purpose |
|------|---------|
| `lint_markdown_cli.py` | E dey check markdown code fences to block old Foundry Local CLI command patterns wey no dey use again. |
| `export_benchmark_markdown.py` | E dey run multi-model latency benchmark and e go create Markdown + JSON reports. |

## 1. Markdown CLI Pattern Linter

`lint_markdown_cli.py` dey scan all `.md` files wey no be translation for Foundry Local CLI patterns wey no dey allowed **inside fenced code blocks** (``` ... ```). You fit still mention old commands for normal text for historical reasons.

### Deprecated Patterns (Blocked Inside Code Fences)

Dis linter dey block old CLI patterns. Make you use the new ones instead.

### Required Replacements
| Deprecated | Use Instead |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark script + system tools (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Exit Codes
| Code | Meaning |
|------|---------|
| 0 | No bad patterns dey |
| 1 | One or more bad patterns dey |

### Running Locally
From di repository root (na di best way):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (Optional)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Dis one go block commits wey dey add old patterns.

### CI Integration
GitHub Action workflow (`.github/workflows/markdown-cli-lint.yml`) dey run di linter anytime person push or make pull request to `main` and `Reactor` branches. If e fail, you must fix am before you go fit merge.

### Adding New Deprecated Patterns
1. Open `lint_markdown_cli.py`.
2. Add tuple `(regex, suggestion)` to di `DEPRECATED` list. Use raw string and add `\b` word boundaries if e dey necessary.
3. Run di linter for your computer to make sure e dey detect am.
4. Commit and push; CI go enforce di new rule.

Example addition:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Allowing Explanatory Mentions
Because na only fenced code blocks dem dey check, you fit talk about old commands for normal text. If you *must* show dem inside fence for comparison, use fenced block wey no get triple backticks (e.g., indent or quote) or rewrite am to pseudo form.

### Skipping Specific Files (Advanced)
If e dey necessary, put old examples for separate file outside di repo or change di extension while you dey draft. Files wey dem translate go skip automatically (paths wey get `translations`).

### Troubleshooting
| Issue | Cause | Resolution |
|-------|-------|-----------|
| Linter dey flag line wey you update | Regex too broad | Make di pattern more specific with extra word boundary (`\b`) or anchors |
| CI dey fail but e dey pass for your computer | Different Python version or uncommitted changes | Run am again for your computer, make sure your working tree clean, check di workflow Python version (3.11) |
| You need bypass am for now | Emergency hotfix | Fix am immediately after; you fit use temporary branch and follow-up PR (no add bypass switches) |

### Rationale
To keep di documentation aligned with di *current* stable CLI surface, e go help avoid wahala for workshop, learners no go confuse, and e go centralize performance measurement through Python scripts wey dem dey maintain instead of CLI subcommands wey dey change anyhow.

---
Dem dey maintain dis one as part of di workshop quality toolchain. If you wan add new features (e.g., auto-fixing suggestions or HTML report generation), open issue or submit PR.

## 2. Sample Validation Script

`validate_samples.py` dey check all Python sample files for syntax, imports, and best practices compliance.

### Usage
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

### Wetin e dey check
- ✅ Python syntax dey correct
- ✅ Required imports dey
- ✅ Error handling dey (verbose mode)
- ✅ Type hints dey (verbose mode)
- ✅ Function docstrings dey (verbose mode)
- ✅ SDK reference links dey (verbose mode)

### Environment Variables
- `SKIP_IMPORT_CHECK=1` - Skip import validation
- `SKIP_SYNTAX_CHECK=1` - Skip syntax validation

### Exit Codes
- `0` - All samples pass validation
- `1` - One or more samples fail

## 3. Sample Test Runner

`test_samples.py` dey run smoke tests for all samples to make sure dem dey work without errors.

### Usage
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

### Prerequisites
- Foundry Local service dey run: `foundry service start`
- Models dey loaded: `foundry model run phi-4-mini`
- Dependencies dey installed: `pip install -r requirements.txt`

### Wetin e dey test
- ✅ Sample fit run without runtime errors
- ✅ Required output dey show
- ✅ Proper error handling dey if e fail
- ✅ Performance (execution time)

### Environment Variables
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model wey dem go use for testing
- `TEST_TIMEOUT=30` - Timeout per sample in seconds

### Expected Failures
Some tests fit fail if optional dependencies no dey installed (e.g., `ragas`, `sentence-transformers`). Install dem with:
```bash
pip install sentence-transformers ragas datasets
```

### Exit Codes
- `0` - All tests pass
- `1` - One or more tests fail

## 4. Benchmark Markdown Exporter

Script: `export_benchmark_markdown.py`

E dey create reproducible performance table for di models.

### Usage
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Outputs
| File | Description |
|------|-------------|
| `benchmark_report.md` | Markdown table (avg, p95, tokens/sec, optional first token) |
| `benchmark_report.json` | Raw metrics array for diffing & history |

### Options
| Flag | Description | Default |
|------|-------------|---------|
| `--models` | Comma-separated model aliases | (required) |
| `--prompt` | Prompt wey dem go use each round | (required) |
| `--rounds` | Rounds per model | 3 |
| `--output` | Markdown output file | `benchmark_report.md` |
| `--json` | JSON output file | `benchmark_report.json` |
| `--fail-on-empty` | Non-zero exit if all benchmarks fail | off |

Environment variable `BENCH_STREAM=1` go add first token latency measurement.

### Notes
- E dey reuse `workshop_utils` to make sure model bootstrap & caching dey consistent.
- If you run am from different working directory, script go try locate `workshop_utils` with path fallbacks.
- For GPU comparison: run am once, enable acceleration via CLI config, run am again and compare di JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important informate, e better make professional human transleto do am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->