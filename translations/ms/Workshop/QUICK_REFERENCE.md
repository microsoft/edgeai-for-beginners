<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T22:43:12+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "ms"
}
-->
# Kad Rujukan Pantas - Contoh Bengkel

**Kemas Kini Terakhir**: 8 Oktober 2025

---

## 🚀 Permulaan Pantas

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 Gambaran Keseluruhan Contoh

| Sesi | Contoh | Tujuan | Masa |
|------|--------|--------|------|
| 01 | `chat_bootstrap.py` | Chat asas + penstriman | ~30s |
| 02 | `rag_pipeline.py` | RAG dengan embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | Penilaian RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Penanda aras model | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Sistem multi-ejen | ~60s |
| 06 | `models_router.py` | Penghalaan niat | ~45s |
| 06 | `models_pipeline.py` | Saluran berbilang langkah | ~60s |

---

## 🛠️ Pembolehubah Persekitaran

### Penting
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Khusus Sesi
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Pengesahan & Ujian

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Penyelesaian Masalah

### Ralat Sambungan
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Ralat Import
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Model Tidak Ditemui
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Prestasi Perlahan
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Corak Biasa

### Chat Asas
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Dapatkan Klien
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Pengendalian Ralat
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Penstriman
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Pemilihan Model

| Model | Saiz | Terbaik Untuk | Kelajuan |
|-------|------|---------------|----------|
| `qwen2.5-0.5b` | 0.5B | Klasifikasi pantas | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Penjanaan kod pantas | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Penulisan kreatif | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kod, penstrukturan semula | ⚡⚡ |
| `phi-4-mini` | 4B | Umum, ringkasan | ⚡⚡ |
| `qwen2.5-7b` | 7B | Penaakulan kompleks | ⚡ |

---

## 🔗 Sumber

- **Dokumen SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rujukan Pantas**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Ringkasan Kemas Kini**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Nota Migrasi**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Petua

1. **Cache klien**: `workshop_utils` akan cache untuk anda
2. **Gunakan model lebih kecil**: Mulakan dengan `qwen2.5-0.5b` untuk ujian
3. **Aktifkan statistik penggunaan**: Tetapkan `SHOW_USAGE=1` untuk menjejaki token
4. **Pemprosesan batch**: Proses beberapa arahan secara berturutan
5. **Kurangkan max_tokens**: Mengurangkan kependaman untuk respons pantas

---

## 🎯 Aliran Kerja Contoh

### Uji Segalanya
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Penanda Aras Model
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### Saluran RAG
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Sistem Multi-Ejen
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Bantuan Pantas**: Jalankan mana-mana contoh dengan `--help` dari direktori `samples` atau semak docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Semua contoh dikemas kini Oktober 2025 dengan amalan terbaik Foundry Local SDK** ✨

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.