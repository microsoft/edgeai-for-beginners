<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T21:28:58+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "pa"
}
-->
# ਵਰਕਸ਼ਾਪ ਸਕ੍ਰਿਪਟਸ

ਇਹ ਡਾਇਰੈਕਟਰੀ ਵਰਕਸ਼ਾਪ ਸਮੱਗਰੀ ਵਿੱਚ ਗੁਣਵੱਤਾ ਅਤੇ ਸਥਿਰਤਾ ਨੂੰ ਬਣਾਈ ਰੱਖਣ ਲਈ ਵਰਤੇ ਜਾਣ ਵਾਲੇ ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਸਹਾਇਕ ਸਕ੍ਰਿਪਟਸ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦੀ ਹੈ।

## ਸਮੱਗਰੀ

| ਫਾਈਲ | ਉਦੇਸ਼ |
|------|---------|
| `lint_markdown_cli.py` | ਮਾਰਕਡਾਊਨ ਕੋਡ ਫੈਂਸਾਂ ਨੂੰ Deprecated Foundry Local CLI ਕਮਾਂਡ ਪੈਟਰਨਾਂ ਨੂੰ ਰੋਕਣ ਲਈ ਲਿੰਟ ਕਰਦਾ ਹੈ। |
| `export_benchmark_markdown.py` | ਮਲਟੀ-ਮਾਡਲ ਲੈਟੈਂਸੀ ਬੈਂਚਮਾਰਕ ਚਲਾਉਂਦਾ ਹੈ ਅਤੇ ਮਾਰਕਡਾਊਨ + JSON ਰਿਪੋਰਟਸ ਜਾਰੀ ਕਰਦਾ ਹੈ। |

## 1. ਮਾਰਕਡਾਊਨ CLI ਪੈਟਰਨ ਲਿੰਟਰ

`lint_markdown_cli.py` ਸਾਰੇ ਗੈਰ-ਅਨੁਵਾਦ `.md` ਫਾਈਲਾਂ ਨੂੰ **ਫੈਂਸਡ ਕੋਡ ਬਲਾਕਾਂ** (``` ... ```) ਦੇ ਅੰਦਰ ਅਣੁਮਤ Foundry Local CLI ਪੈਟਰਨਾਂ ਲਈ ਸਕੈਨ ਕਰਦਾ ਹੈ। ਜਾਣਕਾਰੀ ਪ੍ਰੋਜ਼ੇ ਵਿੱਚ ਇਤਿਹਾਸਕ ਸੰਦਰਭ ਲਈ Deprecated ਕਮਾਂਡਾਂ ਦਾ ਜ਼ਿਕਰ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

### Deprecated ਪੈਟਰਨ (ਕੋਡ ਫੈਂਸਾਂ ਦੇ ਅੰਦਰ ਰੋਕੇ ਗਏ)

ਲਿੰਟਰ Deprecated CLI ਪੈਟਰਨਾਂ ਨੂੰ ਰੋਕਦਾ ਹੈ। ਇਸ ਦੀ ਬਜਾਏ ਆਧੁਨਿਕ ਵਿਕਲਪਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।

### ਲਾਜ਼ਮੀ ਬਦਲਾਅ
| Deprecated | ਇਸ ਦੀ ਬਜਾਏ ਵਰਤੋਂ ਕਰੋ |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | ਬੈਂਚਮਾਰਕ ਸਕ੍ਰਿਪਟ + ਸਿਸਟਮ ਟੂਲਸ (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### ਐਗਜ਼ਿਟ ਕੋਡਸ
| ਕੋਡ | ਅਰਥ |
|------|---------|
| 0 | ਕੋਈ ਉਲੰਘਣਾ ਨਹੀਂ ਪਾਈ ਗਈ |
| 1 | ਇੱਕ ਜਾਂ ਵੱਧ Deprecated ਪੈਟਰਨ ਪਾਏ ਗਏ |

### ਲੋਕਲ ਚਲਾਉਣਾ
ਰਿਪੋਜ਼ਟਰੀ ਰੂਟ ਤੋਂ (ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### ਪ੍ਰੀ-ਕਮਿਟ ਹੂਕ (ਵਿਕਲਪਿਕ)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
ਇਹ ਉਹ ਕਮਿਟਸ ਨੂੰ ਰੋਕਦਾ ਹੈ ਜੋ Deprecated ਪੈਟਰਨਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦੇ ਹਨ।

### CI ਇੰਟੀਗ੍ਰੇਸ਼ਨ
GitHub Action ਵਰਕਫਲੋ (`.github/workflows/markdown-cli-lint.yml`) ਹਰ ਪੁਸ਼ ਅਤੇ ਪੁਲ ਰਿਕਵੈਸਟ ਨੂੰ `main` ਅਤੇ `Reactor` ਬ੍ਰਾਂਚਾਂ 'ਤੇ ਲਿੰਟਰ ਚਲਾਉਂਦਾ ਹੈ। ਫੇਲ੍ਹ ਹੋਣ ਵਾਲੇ ਕੰਮਾਂ ਨੂੰ ਮਰਜ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਠੀਕ ਕਰਨਾ ਪਵੇਗਾ।

### ਨਵੇਂ Deprecated ਪੈਟਰਨ ਸ਼ਾਮਲ ਕਰਨਾ
1. `lint_markdown_cli.py` ਖੋਲ੍ਹੋ।
2. `DEPRECATED` ਲਿਸਟ ਵਿੱਚ ਇੱਕ ਟਿਊਪਲ `(regex, suggestion)` ਸ਼ਾਮਲ ਕਰੋ। ਇੱਕ ਰਾਅ ਸਟ੍ਰਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰੋ ਅਤੇ ਜਿੱਥੇ ਜ਼ਰੂਰੀ ਹੋਵੇ `\b` ਵਰਡ ਬਾਊਂਡਰੀ ਸ਼ਾਮਲ ਕਰੋ।
3. ਪਤਾ ਲਗਾਉਣ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ ਲੋਕਲ ਲਿੰਟਰ ਚਲਾਓ।
4. ਕਮਿਟ ਅਤੇ ਪੁਸ਼ ਕਰੋ; CI ਨਵੇਂ ਨਿਯਮ ਨੂੰ ਲਾਗੂ ਕਰੇਗਾ।

ਉਦਾਹਰਨ ਸ਼ਾਮਲ:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### ਵਿਆਖਿਆਤਮਕ ਜ਼ਿਕਰ ਦੀ ਆਗਿਆ ਦੇਣਾ
ਕਿਉਂਕਿ ਸਿਰਫ਼ ਫੈਂਸਡ ਕੋਡ ਬਲਾਕਾਂ ਨੂੰ ਲਾਗੂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਤੁਸੀਂ ਕਹਾਣਾਤਮਕ ਟੈਕਸਟ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਤੌਰ 'ਤੇ Deprecated ਕਮਾਂਡਾਂ ਦਾ ਵਰਣਨ ਕਰ ਸਕਦੇ ਹੋ। ਜੇ ਤੁਸੀਂ **ਫੈਂਸਡ ਬਲਾਕ** ਵਿੱਚ ਉਹਨਾਂ ਨੂੰ ਦਿਖਾਉਣਾ ਲਾਜ਼ਮੀ ਹੈ ਤਾਂ ਤਿੰਨ ਬੈਕਟਿਕਸ ਤੋਂ ਬਿਨਾਂ ਫੈਂਸਡ ਬਲਾਕ ਸ਼ਾਮਲ ਕਰੋ (ਜਿਵੇਂ ਕਿ ਇੰਡੈਂਟ ਜਾਂ ਕੋਟ) ਜਾਂ ਪਸੰਦੀਦਾ ਰੂਪ ਵਿੱਚ ਦੁਬਾਰਾ ਲਿਖੋ।

### ਖਾਸ ਫਾਈਲਾਂ ਨੂੰ ਸਕਿਪ ਕਰਨਾ (ਐਡਵਾਂਸਡ)
ਜੇਕਰ ਲੋੜ ਹੋਵੇ, ਤਾਂ ਲੈਗੇਸੀ ਉਦਾਹਰਣਾਂ ਨੂੰ ਰਿਪੋ ਤੋਂ ਬਾਹਰ ਇੱਕ ਵੱਖਰੀ ਫਾਈਲ ਵਿੱਚ ਰੱਖੋ ਜਾਂ ਡਰਾਫਟ ਕਰਦੇ ਸਮੇਂ ਵੱਖਰੇ ਐਕਸਟੈਂਸ਼ਨ ਨਾਲ ਰੀਨਾਮ ਕਰੋ। ਅਨੁਵਾਦ ਕੀਤੀਆਂ ਕਾਪੀਆਂ ਲਈ ਇਰਾਦਾ ਸਕਿਪਸ ਆਟੋਮੈਟਿਕ ਹਨ (ਪਾਥਾਂ ਵਿੱਚ `translations` ਸ਼ਾਮਲ ਹਨ)।

### ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ
| ਸਮੱਸਿਆ | ਕਾਰਨ | ਹੱਲ |
|-------|-------|-----------|
| ਲਿੰਟਰ ਤੁਹਾਡੇ ਦੁਆਰਾ ਅਪਡੇਟ ਕੀਤੀ ਲਾਈਨ ਨੂੰ ਫਲੈਗ ਕਰਦਾ ਹੈ | Regex ਬਹੁਤ ਵਿਆਪਕ | ਵਧੇਰੇ ਵਰਡ ਬਾਊਂਡਰੀ (`\b`) ਜਾਂ ਐਂਕਰਸ ਨਾਲ ਪੈਟਰਨ ਨੂੰ ਸੰਕੁਚਿਤ ਕਰੋ |
| CI ਫੇਲ੍ਹ ਹੋ ਜਾਂਦਾ ਹੈ ਪਰ ਲੋਕਲ ਪਾਸ ਕਰਦਾ ਹੈ | ਵੱਖਰੇ Python ਵਰਜਨ ਜਾਂ ਅਣਕਮਿਟ ਕੀਤੇ ਬਦਲਾਅ | ਲੋਕਲ ਦੁਬਾਰਾ ਚਲਾਓ, ਸਾਫ਼ ਵਰਕਿੰਗ ਟਰੀ ਨੂੰ ਯਕੀਨੀ ਬਣਾਓ, ਵਰਕਫਲੋ Python ਵਰਜਨ (3.11) ਦੀ ਜਾਂਚ ਕਰੋ |
| ਅਸਥਾਈ ਤੌਰ 'ਤੇ ਬਾਈਪਾਸ ਕਰਨ ਦੀ ਲੋੜ ਹੈ | ਐਮਰਜੈਂਸੀ ਹੌਟਫਿਕਸ | ਤੁਰੰਤ ਫਿਕਸ ਲਾਗੂ ਕਰੋ; ਅਸਥਾਈ ਬ੍ਰਾਂਚ ਅਤੇ ਫਾਲੋਅਪ PR ਦੀ ਵਰਤੋਂ ਕਰਨ ਬਾਰੇ ਸੋਚੋ (ਬਾਈਪਾਸ ਸਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨ ਤੋਂ ਬਚੋ) |

### ਕਾਰਨ
*ਮੌਜੂਦਾ* ਸਥਿਰ CLI ਸਤਹ ਨਾਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਸਥਿਤ ਰੱਖਣਾ ਵਰਕਸ਼ਾਪ ਵਿੱਚ ਰੁਕਾਵਟਾਂ ਨੂੰ ਰੋਕਦਾ ਹੈ, ਸਿੱਖਣ ਵਾਲਿਆਂ ਨੂੰ ਗੁੰਝਲ ਵਿੱਚ ਪਾਉਣ ਤੋਂ ਬਚਾਉਂਦਾ ਹੈ, ਅਤੇ Python ਸਕ੍ਰਿਪਟਸ ਦੁਆਰਾ ਪ੍ਰਦਰਸ਼ਨ ਮਾਪਣ ਨੂੰ ਕੇਂਦਰੀਕ੍ਰਿਤ ਕਰਦਾ ਹੈ ਬਜਾਏ ਕਿ CLI ਸਬਕਮਾਂਡਾਂ ਦੇ ਡ੍ਰਿਫਟ ਕਰਨ।

---
ਵਰਕਸ਼ਾਪ ਗੁਣਵੱਤਾ ਟੂਲਚੇਨ ਦੇ ਹਿੱਸੇ ਵਜੋਂ ਰੱਖਿਆ ਗਿਆ। ਸੁਧਾਰਾਂ ਲਈ (ਜਿਵੇਂ ਕਿ ਸੁਝਾਅਾਂ ਨੂੰ ਆਟੋ-ਫਿਕਸ ਕਰਨਾ ਜਾਂ HTML ਰਿਪੋਰਟ ਜਨਰੇਸ਼ਨ), ਇੱਕ ਇਸ਼ੂ ਖੋਲ੍ਹੋ ਜਾਂ PR ਜਮ੍ਹਾਂ ਕਰੋ।

## 2. ਸੈਂਪਲ ਵੈਲੀਡੇਸ਼ਨ ਸਕ੍ਰਿਪਟ

`validate_samples.py` ਸਾਰੇ Python ਸੈਂਪਲ ਫਾਈਲਾਂ ਨੂੰ syntax, imports, ਅਤੇ best practices ਦੀ ਪਾਲਣਾ ਲਈ ਵੈਲੀਡੇਟ ਕਰਦਾ ਹੈ।

### ਵਰਤੋਂ
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

### ਇਹ ਕੀ ਚੈੱਕ ਕਰਦਾ ਹੈ
- ✅ Python syntax ਦੀ ਵੈਧਤਾ
- ✅ ਲਾਜ਼ਮੀ imports ਮੌਜੂਦ
- ✅ Error handling ਦੀ ਲਾਗੂਅਤ (verbose mode)
- ✅ Type hints ਦੀ ਵਰਤੋਂ (verbose mode)
- ✅ Function docstrings (verbose mode)
- ✅ SDK ਰਿਫਰੈਂਸ ਲਿੰਕਸ (verbose mode)

### ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲਸ
- `SKIP_IMPORT_CHECK=1` - Import ਵੈਲੀਡੇਸ਼ਨ ਸਕਿਪ ਕਰੋ
- `SKIP_SYNTAX_CHECK=1` - Syntax ਵੈਲੀਡੇਸ਼ਨ ਸਕਿਪ ਕਰੋ

### ਐਗਜ਼ਿਟ ਕੋਡਸ
- `0` - ਸਾਰੇ ਸੈਂਪਲ ਵੈਲੀਡੇਸ਼ਨ ਪਾਸ ਕਰਦੇ ਹਨ
- `1` - ਇੱਕ ਜਾਂ ਵੱਧ ਸੈਂਪਲ ਫੇਲ੍ਹ ਹੋਏ

## 3. ਸੈਂਪਲ ਟੈਸਟ ਰਨਰ

`test_samples.py` ਸਾਰੇ ਸੈਂਪਲਾਂ 'ਤੇ ਸਮੋਕ ਟੈਸਟ ਚਲਾਉਂਦਾ ਹੈ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਉਹ ਬਿਨਾਂ ਗਲਤੀਆਂ ਦੇ ਚੱਲਦੇ ਹਨ।

### ਵਰਤੋਂ
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

### ਪੂਰਵ ਸ਼ਰਤਾਂ
- Foundry Local ਸੇਵਾ ਚਲ ਰਹੀ: `foundry service start`
- ਮਾਡਲ ਲੋਡ ਕੀਤੇ ਗਏ: `foundry model run phi-4-mini`
- Dependencies ਇੰਸਟਾਲ ਕੀਤੇ ਗਏ: `pip install -r requirements.txt`

### ਇਹ ਕੀ ਟੈਸਟ ਕਰਦਾ ਹੈ
- ✅ ਸੈਂਪਲ runtime errors ਤੋਂ ਬਿਨਾਂ ਚੱਲ ਸਕਦਾ ਹੈ
- ✅ ਲਾਜ਼ਮੀ ਆਉਟਪੁੱਟ ਜਨਰੇਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ
- ✅ ਫੇਲ੍ਹ ਹੋਣ 'ਤੇ ਸਹੀ error handling
- ✅ ਪ੍ਰਦਰਸ਼ਨ (execution time)

### ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲਸ
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - ਟੈਸਟਿੰਗ ਲਈ ਮਾਡਲ ਦੀ ਵਰਤੋਂ
- `TEST_TIMEOUT=30` - ਪ੍ਰਤੀ ਸੈਂਪਲ ਟਾਈਮਆਉਟ ਸੈਕੰਡਾਂ ਵਿੱਚ

### ਉਮੀਦ ਕੀਤੀਆਂ ਗਲਤੀਆਂ
ਕੁਝ ਟੈਸਟ ਫੇਲ੍ਹ ਹੋ ਸਕਦੇ ਹਨ ਜੇਕਰ ਵਿਕਲਪਿਕ Dependencies ਇੰਸਟਾਲ ਨਹੀਂ ਕੀਤੇ ਗਏ (ਜਿਵੇਂ ਕਿ `ragas`, `sentence-transformers`)। ਇੰਸਟਾਲ ਕਰਨ ਲਈ:
```bash
pip install sentence-transformers ragas datasets
```

### ਐਗਜ਼ਿਟ ਕੋਡਸ
- `0` - ਸਾਰੇ ਟੈਸਟ ਪਾਸ ਹੋਏ
- `1` - ਇੱਕ ਜਾਂ ਵੱਧ ਟੈਸਟ ਫੇਲ੍ਹ ਹੋਏ

## 4. ਬੈਂਚਮਾਰਕ ਮਾਰਕਡਾਊਨ ਐਕਸਪੋਰਟਰ

ਸਕ੍ਰਿਪਟ: `export_benchmark_markdown.py`

ਮਾਡਲਾਂ ਦੇ ਸੈੱਟ ਲਈ ਇੱਕ ਦੁਬਾਰਾ ਬਣਾਉਣ ਯੋਗ ਪ੍ਰਦਰਸ਼ਨ ਟੇਬਲ ਜਨਰੇਟ ਕਰਦਾ ਹੈ।

### ਵਰਤੋਂ
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### ਆਉਟਪੁੱਟ
| ਫਾਈਲ | ਵੇਰਵਾ |
|------|-------------|
| `benchmark_report.md` | ਮਾਰਕਡਾਊਨ ਟੇਬਲ (avg, p95, tokens/sec, optional first token) |
| `benchmark_report.json` | ਕੱਚੇ ਮੈਟ੍ਰਿਕਸ ਐਰੇ ਡਿਫਿੰਗ ਅਤੇ ਇਤਿਹਾਸ ਲਈ |

### ਵਿਕਲਪ
| Flag | ਵੇਰਵਾ | ਡਿਫਾਲਟ |
|------|-------------|---------|
| `--models` | ਕਾਮਾ-ਵੱਖਰੇ ਮਾਡਲ aliases | (ਲਾਜ਼ਮੀ) |
| `--prompt` | ਹਰ ਰਾਊਂਡ ਵਿੱਚ ਵਰਤਿਆ ਗਿਆ ਪ੍ਰਸ਼ਨ | (ਲਾਜ਼ਮੀ) |
| `--rounds` | ਪ੍ਰਤੀ ਮਾਡਲ ਰਾਊਂਡ | 3 |
| `--output` | ਮਾਰਕਡਾਊਨ ਆਉਟਪੁੱਟ ਫਾਈਲ | `benchmark_report.md` |
| `--json` | JSON ਆਉਟਪੁੱਟ ਫਾਈਲ | `benchmark_report.json` |
| `--fail-on-empty` | ਜੇਕਰ ਸਾਰੇ ਬੈਂਚਮਾਰਕ ਫੇਲ੍ਹ ਹੋਣ ਤਾਂ ਨਾਨ-ਜ਼ੀਰੋ ਐਗਜ਼ਿਟ | ਬੰਦ |

ਐਨਵਾਇਰਮੈਂਟ ਵੈਰੀਏਬਲ `BENCH_STREAM=1` ਪਹਿਲੇ ਟੋਕਨ ਲੈਟੈਂਸੀ ਮਾਪਣ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ।

### ਨੋਟਸ
- ਮਾਡਲ ਬੂਟਸਟ੍ਰੈਪ ਅਤੇ ਕੈਸ਼ਿੰਗ ਵਿੱਚ ਸਥਿਰਤਾ ਲਈ `workshop_utils` ਦੀ ਦੁਬਾਰਾ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।
- ਜੇਕਰ ਵੱਖਰੇ ਵਰਕਿੰਗ ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਚਲਾਇਆ ਜਾਵੇ, ਤਾਂ ਸਕ੍ਰਿਪਟ `workshop_utils` ਨੂੰ ਲੱਭਣ ਲਈ ਪਾਥ ਫਾਲਬੈਕ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ।
- GPU ਤੁਲਨਾ ਲਈ: ਇੱਕ ਵਾਰ ਚਲਾਓ, CLI ਕਨਫਿਗ ਦੁਆਰਾ ਐਕਸਲੇਰੇਸ਼ਨ ਨੂੰ ਐਨਬਲ ਕਰੋ, ਦੁਬਾਰਾ ਚਲਾਓ ਅਤੇ JSON ਨੂੰ ਡਿਫ ਕਰੋ।

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।