<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T23:40:20+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "my"
}
-->
# Workshop Scripts

ဒီ directory မှာ Workshop materials တွေမှာ အရည်အသွေးနဲ့ တိကျမှုကို ထိန်းသိမ်းဖို့ အသုံးပြုတဲ့ automation နဲ့ support scripts တွေ ပါဝင်ပါတယ်။

## အကြောင်းအရာများ

| ဖိုင် | ရည်ရွယ်ချက် |
|------|-------------|
| `lint_markdown_cli.py` | Markdown code fences တွေကို lint လုပ်ပြီး Foundry Local CLI command patterns ရဲ့ အဟောင်းတွေကို ပိတ်ပင်ပေးပါတယ်။ |
| `export_benchmark_markdown.py` | Multi-model latency benchmark ကို run လုပ်ပြီး Markdown + JSON reports ထုတ်ပေးပါတယ်။ |

## 1. Markdown CLI Pattern Linter

`lint_markdown_cli.py` က non-translation `.md` ဖိုင်တွေကို **fenced code blocks** (``` ... ```) အတွင်းမှာ Foundry Local CLI patterns အဟောင်းတွေကို scan လုပ်ပါတယ်။ သမိုင်းကြောင်းအနေနဲ့ deprecated commands တွေကို informational prose မှာ mention လုပ်နိုင်ပါတယ်။

### Deprecated Patterns (Blocked Inside Code Fences)

Linter က CLI patterns အဟောင်းတွေကို ပိတ်ပေးပါတယ်။ အခေတ်သစ် alternative တွေကို အသုံးပြုပါ။

### လိုအပ်တဲ့ အစားထိုးမှုများ
| အဟောင်း | အစားထိုးရန် |
|---------|--------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark script + system tools (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Exit Codes
| Code | အဓိပ္ပါယ် |
|------|-----------|
| 0 | အမှားတွေမတွေ့ရှိပါ |
| 1 | Deprecated patterns တစ်ခုခုတွေ့ရှိ |

### Local မှာ Run လုပ်ခြင်း
Repository root မှ (အကြံပြုထားသည့်နည်းလမ်း):

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
ဒီဟာက deprecated patterns တွေကို commit ထဲထည့်တာကို ပိတ်ပေးပါတယ်။

### CI Integration
GitHub Action workflow (`.github/workflows/markdown-cli-lint.yml`) က `main` နဲ့ `Reactor` branches မှာ push နဲ့ pull request တိုင်းမှာ linter ကို run လုပ်ပါတယ်။ Job fail ဖြစ်ရင် merge လုပ်ခွင့်မရှိပါ။

### Deprecated Patterns အသစ်တွေ ထည့်သွင်းခြင်း
1. `lint_markdown_cli.py` ကိုဖွင့်ပါ။
2. Tuple `(regex, suggestion)` ကို `DEPRECATED` list ထဲမှာ ထည့်ပါ။ Raw string ကိုအသုံးပြုပြီး `\b` word boundaries ပါဝင်စေပါ။
3. Local မှာ linter ကို run လုပ်ပြီး detection ကို verify လုပ်ပါ။
4. Commit နဲ့ push လုပ်ပါ။ CI က rule အသစ်ကို enforce လုပ်ပါလိမ့်မယ်။

ဥပမာထည့်သွင်းမှု:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Explanatory Mentions ကို ခွင့်ပြုခြင်း
Fenced code blocks တွေမှာပဲ enforce လုပ်တာဖြစ်လို့ narrative text မှာ deprecated commands တွေကို describe လုပ်နိုင်ပါတယ်။ Fence အတွင်းမှာ contrast ပြဖို့လိုအပ်ရင် triple backticks မပါတဲ့ fenced block (ဥပမာ indent သို့မဟုတ် quote) သို့မဟုတ် pseudo form ပြန်ရေးပါ။

### Specific Files ကို Skip လုပ်ခြင်း (Advanced)
လိုအပ်ပါက legacy examples တွေကို repo အပြင်မှာ သီးသန့်ဖိုင်ထဲမှာ ထည့်ပါ။ သို့မဟုတ် draft လုပ်နေစဉ်မှာ extension ကိုပြောင်းပါ။ Translated copies တွေအတွက် intentional skips တွေကို automatic လုပ်ထားပါတယ် (paths တွေမှာ `translations` ပါဝင်ပါက).

### Troubleshooting
| ပြဿနာ | အကြောင်းအရင်း | ဖြေရှင်းနည်း |
|-------|----------------|-------------|
| Linter က သင်ပြင်ထားတဲ့ line ကို flag လုပ်တယ် | Regex အကျယ်အဝန်းများလွန်း | Word boundary (`\b`) သို့မဟုတ် anchors တွေထည့်ပြီး pattern ကို ကျဉ်းစေပါ |
| CI fail ဖြစ်ပြီး local pass ဖြစ်တယ် | Python version ကွာခြားမှု သို့မဟုတ် uncommitted changes | Local မှာ ပြန် run လုပ်ပါ၊ clean working tree ရှိကြောင်းသေချာပါ၊ workflow Python version (3.11) ကိုစစ်ပါ |
| အချိန်ပေါ် bypass လုပ်ဖို့လိုအပ် | Emergency hotfix | Fix ကို ချက်ချင်းလုပ်ပါ၊ temporary branch နဲ့ follow-up PR ကိုအသုံးပြုပါ (bypass switches ထည့်တာကိုရှောင်ပါ) |

### Rationale
Documentation ကို *လက်ရှိ* stable CLI surface နဲ့ align လုပ်ထားခြင်းက workshop friction ကိုလျော့ကျစေပြီး၊ သင်ကြားသူတွေကို အရှုပ်အထွေးမဖြစ်စေဘဲ၊ maintained Python scripts တွေကို အသုံးပြုပြီး performance measurement ကို centralize လုပ်နိုင်စေပါတယ်။

---
Workshop quality toolchain ရဲ့ အစိတ်အပိုင်းအနေနဲ့ ထိန်းသိမ်းထားပါတယ်။ Enhancements (ဥပမာ auto-fixing suggestions သို့မဟုတ် HTML report generation) အတွက် issue တစ်ခုဖွင့်ပါ သို့မဟုတ် PR တင်ပါ။

## 2. Sample Validation Script

`validate_samples.py` က Python sample ဖိုင်တွေကို syntax, imports, နဲ့ best practices compliance အတွက် validate လုပ်ပါတယ်။

### အသုံးပြုနည်း
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

### စစ်ဆေးတာတွေ
- ✅ Python syntax မှန်ကန်မှု
- ✅ လိုအပ်တဲ့ imports ရှိမှု
- ✅ Error handling implementation (verbose mode)
- ✅ Type hints အသုံးပြုမှု (verbose mode)
- ✅ Function docstrings (verbose mode)
- ✅ SDK reference links (verbose mode)

### Environment Variables
- `SKIP_IMPORT_CHECK=1` - Import validation ကို skip လုပ်ပါ
- `SKIP_SYNTAX_CHECK=1` - Syntax validation ကို skip လုပ်ပါ

### Exit Codes
- `0` - Sample အားလုံး pass ဖြစ်
- `1` - Sample တစ်ခုခု fail ဖြစ်

## 3. Sample Test Runner

`test_samples.py` က sample တွေကို smoke tests run လုပ်ပြီး error မရှိဘဲ execute လုပ်နိုင်မှုကို verify လုပ်ပါတယ်။

### အသုံးပြုနည်း
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

### လိုအပ်ချက်များ
- Foundry Local service run နေ: `foundry service start`
- Models load လုပ်ထား: `foundry model run phi-4-mini`
- Dependencies install လုပ်ထား: `pip install -r requirements.txt`

### စစ်ဆေးတာတွေ
- ✅ Sample က runtime errors မရှိဘဲ execute လုပ်နိုင်မှု
- ✅ လိုအပ်တဲ့ output ထုတ်ပေးမှု
- ✅ Fail ဖြစ်ရင် error handling မှန်ကန်မှု
- ✅ Performance (execution time)

### Environment Variables
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Test အတွက် အသုံးပြုမယ့် model
- `TEST_TIMEOUT=30` - Sample တစ်ခုစီအတွက် timeout (seconds)

### မျှော်လင့်ရတဲ့ Failures
Optional dependencies မရှိရင် test တစ်ချို့ fail ဖြစ်နိုင်ပါတယ် (ဥပမာ `ragas`, `sentence-transformers`)။ Install လုပ်ရန်:
```bash
pip install sentence-transformers ragas datasets
```

### Exit Codes
- `0` - Test အားလုံး pass ဖြစ်
- `1` - Test တစ်ခုခု fail ဖြစ်

## 4. Benchmark Markdown Exporter

Script: `export_benchmark_markdown.py`

Models set တစ်ခုအတွက် reproducible performance table ကို generate လုပ်ပေးပါတယ်။

### အသုံးပြုနည်း
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Outputs
| ဖိုင် | ဖော်ပြချက် |
|------|------------|
| `benchmark_report.md` | Markdown table (avg, p95, tokens/sec, optional first token) |
| `benchmark_report.json` | Raw metrics array (diffing & history အတွက်) |

### Options
| Flag | ဖော်ပြချက် | Default |
|------|------------|---------|
| `--models` | Comma-separated model aliases | (required) |
| `--prompt` | Prompt used each round | (required) |
| `--rounds` | Rounds per model | 3 |
| `--output` | Markdown output file | `benchmark_report.md` |
| `--json` | JSON output file | `benchmark_report.json` |
| `--fail-on-empty` | Benchmarks အားလုံး fail ဖြစ်ရင် Non-zero exit | off |

Environment variable `BENCH_STREAM=1` က first token latency measurement ကိုထည့်ပေးပါတယ်။

### မှတ်ချက်များ
- `workshop_utils` ကို အသုံးပြုပြီး model bootstrap & caching ကို consistency ရှိအောင်လုပ်ပါတယ်။
- အခြား working directory မှ run လုပ်ရင် `workshop_utils` ကို ရှာဖွေဖို့ path fallbacks တွေကို script က လုပ်ပါလိမ့်မယ်။
- GPU comparison အတွက်: တစ်ခါ run လုပ်ပြီး CLI config မှာ acceleration ကို enable လုပ်ပါ၊ ပြန် run လုပ်ပြီး JSON ကို diff လုပ်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။