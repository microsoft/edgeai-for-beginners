<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T23:48:46+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "ms"
}
-->
# Panduan Konfigurasi Persekitaran

## Gambaran Keseluruhan

Contoh Workshop menggunakan pembolehubah persekitaran untuk konfigurasi, yang disentralisasi dalam fail `.env` di akar repositori. Ini membolehkan penyesuaian mudah tanpa mengubah kod.

## Permulaan Cepat

### 1. Sahkan Prasyarat

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Konfigurasi Persekitaran

Fail `.env` telah dikonfigurasi dengan tetapan lalai yang sesuai. Kebanyakan pengguna tidak perlu mengubah apa-apa.

**Pilihan**: Semak dan sesuaikan tetapan:
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

## Rujukan Pembolehubah Persekitaran

### Konfigurasi Teras

| Pembolehubah | Lalai | Penerangan |
|--------------|-------|------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Model lalai untuk contoh |
| `FOUNDRY_LOCAL_ENDPOINT` | (kosong) | Menimpa titik akhir perkhidmatan |
| `PYTHONPATH` | Laluan Workshop | Laluan carian modul Python |

**Bila untuk menetapkan FOUNDRY_LOCAL_ENDPOINT:**
- Instance Foundry Local jauh
- Konfigurasi port tersuai
- Pemisahan pembangunan/pengeluaran

**Contoh:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Pembolehubah Khusus Sesi

#### Sesi 02: RAG Pipeline
| Pembolehubah | Lalai | Tujuan |
|--------------|-------|--------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model embedding |
| `RAG_QUESTION` | Pra-konfigurasi | Soalan ujian |

#### Sesi 03: Penanda Aras
| Pembolehubah | Lalai | Tujuan |
|--------------|-------|--------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Model untuk penanda aras |
| `BENCH_ROUNDS` | `3` | Iterasi setiap model |
| `BENCH_PROMPT` | Pra-konfigurasi | Prompt ujian |
| `BENCH_STREAM` | `0` | Ukur latensi token pertama |

#### Sesi 04: Perbandingan Model
| Pembolehubah | Lalai | Tujuan |
|--------------|-------|--------|
| `SLM_ALIAS` | `phi-4-mini` | Model bahasa kecil |
| `LLM_ALIAS` | `qwen2.5-7b` | Model bahasa besar |
| `COMPARE_PROMPT` | Pra-konfigurasi | Prompt perbandingan |
| `COMPARE_RETRIES` | `2` | Percubaan semula |

#### Sesi 05: Orkestrasi Multi-Ejen
| Pembolehubah | Lalai | Tujuan |
|--------------|-------|--------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model ejen penyelidik |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Model ejen editor |
| `AGENT_QUESTION` | Pra-konfigurasi | Soalan ujian |

### Konfigurasi Kebolehpercayaan

| Pembolehubah | Lalai | Tujuan |
|--------------|-------|--------|
| `SHOW_USAGE` | `1` | Cetak penggunaan token |
| `RETRY_ON_FAIL` | `1` | Aktifkan logik percubaan semula |
| `RETRY_BACKOFF` | `1.0` | Kelewatan percubaan semula (saat) |

## Konfigurasi Biasa

### Persediaan Pembangunan (Iterasi Cepat)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Persediaan Pengeluaran (Fokus Kualiti)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Persediaan Penanda Aras
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Pengkhususan Multi-Ejen
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Pembangunan Jauh
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Model yang Disyorkan

### Mengikut Kes Penggunaan

**Tujuan Umum:**
- `phi-4-mini` - Keseimbangan kualiti dan kelajuan

**Respons Cepat:**
- `qwen2.5-0.5b` - Sangat pantas, baik untuk klasifikasi
- `phi-4-mini` - Pantas dengan kualiti baik

**Kualiti Tinggi:**
- `qwen2.5-7b` - Kualiti terbaik, penggunaan sumber lebih tinggi
- `phi-4-mini` - Kualiti baik, sumber lebih rendah

**Penjanaan Kod:**
- `deepseek-coder-1.3b` - Khusus untuk kod
- `phi-4-mini` - Penjanaan kod tujuan umum

### Mengikut Ketersediaan Sumber

**Sumber Rendah (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Sumber Sederhana (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Sumber Tinggi (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Konfigurasi Lanjutan

### Titik Akhir Tersuai

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Suhu & Pensampelan (Menimpa dalam Kod)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Persediaan Hibrid Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Penyelesaian Masalah

### Pembolehubah Persekitaran Tidak Dimuatkan

**Gejala:**
- Skrip menggunakan model yang salah
- Ralat sambungan
- Pembolehubah tidak dikenali

**Penyelesaian:**
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

### Masalah Sambungan Perkhidmatan

**Gejala:**
- Ralat "Connection refused"
- "Perkhidmatan tidak tersedia"
- Ralat tamat masa

**Penyelesaian:**
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

### Model Tidak Ditemui

**Gejala:**
- Ralat "Model tidak ditemui"
- "Alias tidak dikenali"

**Penyelesaian:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Ralat Import

**Gejala:**
- Ralat "Modul tidak ditemui"

**Penyelesaian:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Ujian Konfigurasi

### Sahkan Pemuatan Persekitaran

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

### Uji Sambungan Foundry Local

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

## Amalan Terbaik Keselamatan

### 1. Jangan Komit Rahsia

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Gunakan Fail .env Berasingan

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Putar Kunci API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Gunakan Konfigurasi Khusus Persekitaran

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Dokumentasi SDK

- **Repositori Utama**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Dokumentasi API**: Semak repositori SDK untuk yang terkini

## Sumber Tambahan

- `QUICK_START.md` - Panduan memulakan
- `Workshop/samples/*/README.md` - Panduan khusus contoh

---

**Tarikh Dikemas Kini**: 2025-01-08  
**Versi**: 2.0  
**SDK**: Foundry Local Python SDK (terkini)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->