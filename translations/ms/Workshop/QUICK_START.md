<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd656d9068e1459dae855bd47075f2fb",
  "translation_date": "2025-10-28T22:40:02+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ms"
}
-->
# Panduan Pantas Bengkel

## Prasyarat

### 1. Pasang Foundry Local

Ikuti panduan pemasangan rasmi:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Pasang Kebergantungan Python

Dari direktori Bengkel:

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

## Menjalankan Sampel Bengkel

### Sesi 01: Chat Asas

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Pembolehubah Persekitaran:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sesi 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Pembolehubah Persekitaran:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sesi 02: Penilaian RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Nota**: Memerlukan kebergantungan tambahan dipasang melalui `requirements.txt`

### Sesi 03: Penanda Aras

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Pembolehubah Persekitaran:**
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

**Pembolehubah Persekitaran:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sesi 05: Orkestrasi Multi-Ejen

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Pembolehubah Persekitaran:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sesi 06: Penghala Model

```bash
cd Workshop/samples
python -m session06.models_router
```

**Menguji logik penghalaan** dengan pelbagai niat (kod, ringkasan, klasifikasi)

### Sesi 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Pipeline pelbagai langkah yang kompleks** dengan perancangan, pelaksanaan, dan penambahbaikan

## Skrip

### Eksport Laporan Penanda Aras

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Output**: Jadual Markdown + metrik JSON

### Lint Corak CLI Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Tujuan**: Mengesan corak CLI yang tidak lagi digunakan dalam dokumentasi

## Ujian

### Ujian Asap

```bash
cd Workshop
python -m tests.smoke
```

**Ujian**: Fungsi asas sampel utama

## Penyelesaian Masalah

### Perkhidmatan Tidak Berjalan

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Ralat Import Modul

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Ralat Sambungan

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model Tidak Ditemui

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Rujukan Pembolehubah Persekitaran

### Konfigurasi Teras
| Pembolehubah | Lalai | Penerangan |
|--------------|-------|------------|
| `FOUNDRY_LOCAL_ALIAS` | Berbeza | Alias model untuk digunakan |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Menimpa titik akhir perkhidmatan |
| `SHOW_USAGE` | `0` | Paparkan statistik penggunaan token |
| `RETRY_ON_FAIL` | `1` | Aktifkan logik percubaan semula |
| `RETRY_BACKOFF` | `1.0` | Kelewatan percubaan semula awal (saat) |

### Khusus Sesi
| Pembolehubah | Lalai | Penerangan |
|--------------|-------|------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model embedding |
| `RAG_QUESTION` | Lihat sampel | Soalan ujian RAG |
| `BENCH_MODELS` | Berbeza | Model dipisahkan dengan koma |
| `BENCH_ROUNDS` | `3` | Iterasi penanda aras |
| `BENCH_PROMPT` | Lihat sampel | Prompt penanda aras |
| `BENCH_STREAM` | `0` | Ukur latensi token pertama |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model ejen utama |
| `AGENT_MODEL_EDITOR` | Utama | Model ejen editor |
| `SLM_ALIAS` | `phi-4-mini` | Model bahasa kecil |
| `LLM_ALIAS` | `qwen2.5-7b` | Model bahasa besar |
| `COMPARE_PROMPT` | Lihat sampel | Prompt perbandingan |

## Model Disyorkan

### Pembangunan & Ujian
- **phi-4-mini** - Kualiti dan kelajuan seimbang
- **qwen2.5-0.5b** - Sangat pantas untuk klasifikasi
- **gemma-2-2b** - Kualiti baik, kelajuan sederhana

### Senario Pengeluaran
- **phi-4-mini** - Tujuan umum
- **deepseek-coder-1.3b** - Penjanaan kod
- **qwen2.5-7b** - Respons berkualiti tinggi

## Dokumentasi SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Mendapatkan Bantuan

1. Periksa status perkhidmatan: `foundry service status`
2. Lihat log: Periksa log perkhidmatan Foundry Local
3. Semak dokumen SDK: https://github.com/microsoft/Foundry-Local
4. Semak kod sampel: Semua sampel mempunyai docstring terperinci

## Langkah Seterusnya

1. Lengkapkan semua sesi bengkel mengikut urutan
2. Bereksperimen dengan model yang berbeza
3. Ubah suai sampel untuk kes penggunaan anda
4. Semak `SDK_MIGRATION_NOTES.md` untuk corak lanjutan

---

**Tarikh Dikemas Kini**: 2025-01-08  
**Versi Bengkel**: Terkini  
**SDK**: Foundry Local Python SDK

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.