<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-11T23:43:45+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "id"
}
-->
# Panduan Cepat Workshop

## Prasyarat

### 1. Instal Foundry Local

Ikuti panduan instalasi resmi:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Instal Dependensi Python

Dari direktori Workshop:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Menjalankan Contoh Workshop

### Sesi 01: Chat Dasar

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Variabel Lingkungan:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sesi 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Variabel Lingkungan:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sesi 02: Evaluasi RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Catatan**: Membutuhkan dependensi tambahan yang diinstal melalui `requirements.txt`

### Sesi 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Variabel Lingkungan:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Output**: JSON dengan metrik latensi, throughput, dan token pertama

### Sesi 04: Perbandingan Model

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Variabel Lingkungan:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sesi 05: Orkestrasi Multi-Agent

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Variabel Lingkungan:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sesi 06: Model Router

```bash
cd Workshop/samples
python -m session06.models_router
```

**Menguji logika routing** dengan berbagai intent (kode, ringkasan, klasifikasi)

### Sesi 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Pipeline multi-langkah yang kompleks** dengan perencanaan, eksekusi, dan penyempurnaan

## Skrip

### Ekspor Laporan Benchmark

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Output**: Tabel Markdown + metrik JSON

### Lint Pola CLI Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Tujuan**: Mendeteksi pola CLI yang sudah usang dalam dokumentasi

## Pengujian

### Pengujian Awal

```bash
cd Workshop
python -m tests.smoke
```

**Pengujian**: Fungsi dasar dari contoh utama

## Pemecahan Masalah

### Layanan Tidak Berjalan

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Kesalahan Impor Modul

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Kesalahan Koneksi

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model Tidak Ditemukan

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referensi Variabel Lingkungan

### Konfigurasi Inti
| Variabel | Default | Deskripsi |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Bervariasi | Alias model yang digunakan |
| `FOUNDRY_LOCAL_ENDPOINT` | Otomatis | Menimpa endpoint layanan |
| `SHOW_USAGE` | `0` | Menampilkan statistik penggunaan token |
| `RETRY_ON_FAIL` | `1` | Mengaktifkan logika retry |
| `RETRY_BACKOFF` | `1.0` | Penundaan retry awal (detik) |

### Spesifik Sesi
| Variabel | Default | Deskripsi |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model embedding |
| `RAG_QUESTION` | Lihat contoh | Pertanyaan uji RAG |
| `BENCH_MODELS` | Bervariasi | Model yang dipisahkan dengan koma |
| `BENCH_ROUNDS` | `3` | Iterasi benchmark |
| `BENCH_PROMPT` | Lihat contoh | Prompt benchmark |
| `BENCH_STREAM` | `0` | Mengukur latensi token pertama |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model agen utama |
| `AGENT_MODEL_EDITOR` | Utama | Model agen editor |
| `SLM_ALIAS` | `phi-4-mini` | Model bahasa kecil |
| `LLM_ALIAS` | `qwen2.5-7b` | Model bahasa besar |
| `COMPARE_PROMPT` | Lihat contoh | Prompt perbandingan |

## Model yang Direkomendasikan

### Pengembangan & Pengujian
- **phi-4-mini** - Kualitas dan kecepatan seimbang
- **qwen2.5-0.5b** - Sangat cepat untuk klasifikasi
- **gemma-2-2b** - Kualitas baik, kecepatan sedang

### Skenario Produksi
- **phi-4-mini** - Tujuan umum
- **deepseek-coder-1.3b** - Generasi kode
- **qwen2.5-7b** - Respons berkualitas tinggi

## Dokumentasi SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Mendapatkan Bantuan

1. Periksa status layanan: `foundry service status`
2. Lihat log: Periksa log layanan Foundry Local
3. Periksa dokumen SDK: https://github.com/microsoft/Foundry-Local
4. Tinjau kode contoh: Semua contoh memiliki docstring yang terperinci

## Langkah Selanjutnya

1. Selesaikan semua sesi workshop secara berurutan
2. Bereksperimen dengan berbagai model
3. Modifikasi contoh untuk kasus penggunaan Anda

---

**Terakhir Diperbarui**: 2025-01-08  
**Versi Workshop**: Terbaru  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->