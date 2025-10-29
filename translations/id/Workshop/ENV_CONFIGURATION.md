<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T22:36:23+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "id"
}
-->
# Panduan Konfigurasi Lingkungan

## Ikhtisar

Contoh Workshop menggunakan variabel lingkungan untuk konfigurasi, yang terpusat dalam file `.env` di root repositori. Hal ini memungkinkan penyesuaian yang mudah tanpa perlu mengubah kode.

## Panduan Cepat

### 1. Verifikasi Prasyarat

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigurasi Lingkungan

File `.env` sudah dikonfigurasi dengan nilai default yang sesuai. Sebagian besar pengguna tidak perlu mengubah apa pun.

**Opsional**: Tinjau dan sesuaikan pengaturan:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Terapkan Konfigurasi

**Untuk Skrip Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Untuk Notebook:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referensi Variabel Lingkungan

### Konfigurasi Inti

| Variabel | Default | Deskripsi |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Model default untuk contoh |
| `FOUNDRY_LOCAL_ENDPOINT` | (kosong) | Menimpa endpoint layanan |
| `PYTHONPATH` | Jalur Workshop | Jalur pencarian modul Python |

**Kapan harus mengatur FOUNDRY_LOCAL_ENDPOINT:**
- Instance Foundry Local jarak jauh
- Konfigurasi port khusus
- Pemisahan pengembangan/produksi

**Contoh:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Variabel Khusus Sesi

#### Sesi 02: RAG Pipeline
| Variabel | Default | Tujuan |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model embedding |
| `RAG_QUESTION` | Sudah dikonfigurasi | Pertanyaan uji |

#### Sesi 03: Benchmarking
| Variabel | Default | Tujuan |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Model untuk benchmarking |
| `BENCH_ROUNDS` | `3` | Iterasi per model |
| `BENCH_PROMPT` | Sudah dikonfigurasi | Prompt uji |
| `BENCH_STREAM` | `0` | Mengukur latensi token pertama |

#### Sesi 04: Perbandingan Model
| Variabel | Default | Tujuan |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | Model bahasa kecil |
| `LLM_ALIAS` | `qwen2.5-7b` | Model bahasa besar |
| `COMPARE_PROMPT` | Sudah dikonfigurasi | Prompt perbandingan |
| `COMPARE_RETRIES` | `2` | Upaya ulang |

#### Sesi 05: Orkestrasi Multi-Agen
| Variabel | Default | Tujuan |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model agen peneliti |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Model agen editor |
| `AGENT_QUESTION` | Sudah dikonfigurasi | Pertanyaan uji |

### Konfigurasi Keandalan

| Variabel | Default | Tujuan |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | Menampilkan penggunaan token |
| `RETRY_ON_FAIL` | `1` | Mengaktifkan logika ulang |
| `RETRY_BACKOFF` | `1.0` | Penundaan ulang (detik) |

## Konfigurasi Umum

### Pengaturan Pengembangan (Iterasi Cepat)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Pengaturan Produksi (Fokus Kualitas)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Pengaturan Benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Spesialisasi Multi-Agen
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Pengembangan Jarak Jauh
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Model yang Direkomendasikan

### Berdasarkan Kasus Penggunaan

**Tujuan Umum:**
- `phi-4-mini` - Keseimbangan kualitas dan kecepatan

**Respon Cepat:**
- `qwen2.5-0.5b` - Sangat cepat, baik untuk klasifikasi
- `phi-4-mini` - Cepat dengan kualitas baik

**Kualitas Tinggi:**
- `qwen2.5-7b` - Kualitas terbaik, penggunaan sumber daya lebih tinggi
- `phi-4-mini` - Kualitas baik, sumber daya lebih rendah

**Generasi Kode:**
- `deepseek-coder-1.3b` - Spesialisasi untuk kode
- `phi-4-mini` - Tujuan umum untuk pengkodean

### Berdasarkan Ketersediaan Sumber Daya

**Sumber Daya Rendah (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Sumber Daya Sedang (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Sumber Daya Tinggi (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Konfigurasi Lanjutan

### Endpoint Khusus

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatur & Sampling (Menimpa di Kode)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Pengaturan Hybrid Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Pemecahan Masalah

### Variabel Lingkungan Tidak Dimuat

**Gejala:**
- Skrip menggunakan model yang salah
- Kesalahan koneksi
- Variabel tidak dikenali

**Solusi:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Masalah Koneksi Layanan

**Gejala:**
- Kesalahan "Connection refused"
- "Layanan tidak tersedia"
- Kesalahan waktu habis

**Solusi:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Model Tidak Ditemukan

**Gejala:**
- Kesalahan "Model tidak ditemukan"
- "Alias tidak dikenali"

**Solusi:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Kesalahan Impor

**Gejala:**
- Kesalahan "Module not found"

**Solusi:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Pengujian Konfigurasi

### Verifikasi Pemuatan Lingkungan

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Uji Koneksi Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## Praktik Keamanan Terbaik

### 1. Jangan Pernah Menyimpan Rahasia

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Gunakan File .env Terpisah

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Putar Ulang Kunci API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Gunakan Konfigurasi Khusus Lingkungan

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Dokumentasi SDK

- **Repositori Utama**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Dokumentasi API**: Periksa repositori SDK untuk versi terbaru

## Sumber Daya Tambahan

- `QUICK_START.md` - Panduan memulai
- `SDK_MIGRATION_NOTES.md` - Detail pembaruan SDK
- `Workshop/samples/*/README.md` - Panduan khusus contoh

---

**Terakhir Diperbarui**: 2025-01-08  
**Versi**: 2.0  
**SDK**: Foundry Local Python SDK (terbaru)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.