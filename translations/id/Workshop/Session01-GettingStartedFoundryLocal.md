<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:24:15+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "id"
}
-->
# Sesi 1: Memulai dengan Foundry Local

## Abstrak

Mulailah perjalanan Anda dengan Foundry Local dengan menginstal dan mengonfigurasinya di Windows 11. Pelajari cara mengatur CLI, mengaktifkan akselerasi perangkat keras, dan menyimpan model untuk inferensi lokal yang cepat. Sesi praktis ini akan memandu Anda menjalankan model seperti Phi, Qwen, DeepSeek, dan GPT-OSS-20B menggunakan perintah CLI yang dapat direproduksi.

## Tujuan Pembelajaran

Pada akhir sesi ini, Anda akan:

- **Instalasi dan Konfigurasi**: Mengatur Foundry Local di Windows 11 dengan pengaturan performa optimal
- **Menguasai Operasi CLI**: Menggunakan Foundry Local CLI untuk manajemen dan penerapan model
- **Mengaktifkan Akselerasi Perangkat Keras**: Mengonfigurasi akselerasi GPU dengan ONNXRuntime atau WebGPU
- **Menjalankan Berbagai Model**: Menjalankan model phi-4, GPT-OSS-20B, Qwen, dan DeepSeek secara lokal
- **Membangun Aplikasi Pertama Anda**: Menyesuaikan sampel yang ada untuk menggunakan Foundry Local Python SDK

# Uji model (prompt tunggal non-interaktif)
foundry model run phi-4-mini --prompt "Halo, perkenalkan diri Anda"

- Windows 11 (22H2 atau lebih baru)
# Daftar model katalog yang tersedia (model yang dimuat muncul setelah dijalankan)
foundry model list
## NOTE: Saat ini tidak ada flag khusus `--running`; untuk melihat mana yang dimuat, mulai obrolan atau periksa log layanan.
- Python 3.10+ terinstal
- Visual Studio Code dengan ekstensi Python
- Hak administrator untuk instalasi

### (Opsional) Variabel Lingkungan

Buat `.env` (atau atur di shell) untuk membuat skrip lebih portabel:
# Bandingkan respons (non-interaktif)
foundry model run gpt-oss-20b --prompt "Jelaskan AI edge dengan istilah sederhana"
| Variabel | Tujuan | Contoh |
|----------|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Alias model yang diinginkan (katalog secara otomatis memilih varian terbaik) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Menimpa endpoint (jika tidak, otomatis dari manajer) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Mengaktifkan demo streaming | `true` |

> Jika `FOUNDRY_LOCAL_ENDPOINT=auto` (atau tidak diatur), kami mengambilnya dari manajer SDK.

## Alur Demo (30 menit)

### 1. Instal Foundry Local dan Verifikasi Pengaturan CLI (10 menit)

# Daftar model yang disimpan
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Pratinjau / Jika Didukung)**

Jika paket macOS asli tersedia (periksa dokumen resmi untuk versi terbaru):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Jika binari asli macOS belum tersedia, Anda masih dapat: 
1. Menggunakan VM Windows 11 ARM/Intel (Parallels / UTM) dan mengikuti langkah-langkah Windows. 
2. Menjalankan model melalui container (jika gambar container diterbitkan) dan mengatur `FOUNDRY_LOCAL_ENDPOINT` ke port yang diekspos. 

**Buat Lingkungan Virtual Python (Lintas Platform)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Perbarui pip dan instal dependensi inti:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Langkah 1.2: Verifikasi Instalasi

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Langkah 1.3: Konfigurasi Lingkungan

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Bootstrapping SDK (Direkomendasikan)

Alih-alih memulai layanan secara manual & menjalankan model, **Foundry Local Python SDK** dapat memulai semuanya:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Jika Anda lebih suka kontrol eksplisit, Anda masih dapat menggunakan CLI + klien OpenAI seperti yang ditunjukkan nanti.

### 2. Jalankan Model Secara Lokal melalui CLI (10 menit)

#### Langkah 3.1: Terapkan Model Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Langkah 3.2: Terapkan GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Langkah 3.3: Muat Model Tambahan

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Proyek Pemula: Sesuaikan 01-run-phi untuk Foundry Local (5 menit)

#### Langkah 4.1: Buat Aplikasi Obrolan Dasar

Buat `samples/01-foundry-quickstart/chat_quickstart.py` (diperbarui untuk menggunakan manajer jika tersedia):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Langkah 4.2: Uji Aplikasi

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Konsep Utama yang Dibahas

### 1. Arsitektur Foundry Local

- **Mesin Inferensi Lokal**: Menjalankan model sepenuhnya di perangkat Anda
- **Kompatibilitas SDK OpenAI**: Integrasi mulus dengan kode OpenAI yang ada
- **Manajemen Model**: Mengunduh, menyimpan, dan menjalankan beberapa model secara efisien
- **Optimasi Perangkat Keras**: Memanfaatkan akselerasi GPU, NPU, dan CPU

### 2. Referensi Perintah CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integrasi Python SDK

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Pemecahan Masalah Umum

### Masalah 1: "Perintah Foundry tidak ditemukan"

**Solusi:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Masalah 2: "Model gagal dimuat"

**Solusi:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Masalah 3: "Koneksi ditolak di localhost:5273"

**Solusi:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tips Optimasi Performa

### 1. Strategi Pemilihan Model

- **Phi-4-mini**: Terbaik untuk tugas umum, penggunaan memori lebih rendah
- **Qwen2.5-0.5b**: Inferensi tercepat, sumber daya minimal
- **GPT-OSS-20B**: Kualitas tertinggi, membutuhkan lebih banyak sumber daya
- **DeepSeek-Coder**: Dioptimalkan untuk tugas pemrograman

### 2. Optimasi Perangkat Keras

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Pemantauan Performa

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Peningkatan Opsional

| Peningkatan | Apa | Bagaimana |
|-------------|-----|----------|
| Utilitas Bersama | Menghapus logika klien/bootstrap yang duplikat | Gunakan `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Visibilitas Penggunaan Token | Mengajarkan pemikiran biaya/efisiensi lebih awal | Atur `SHOW_USAGE=1` untuk mencetak prompt/penyelesaian/total token |
| Perbandingan Deterministik | Benchmarking stabil & pemeriksaan regresi | Gunakan `temperature=0`, `top_p=1`, teks prompt konsisten |
| Latensi Token Pertama | Metrik responsivitas yang dirasakan | Sesuaikan skrip benchmark dengan streaming (`BENCH_STREAM=1`) |
| Coba Ulang pada Kesalahan Sementara | Demo yang tangguh pada start dingin | `RETRY_ON_FAIL=1` (default) & sesuaikan `RETRY_BACKOFF` |
| Pengujian Awal | Pemeriksaan cepat di alur utama | Jalankan `python Workshop/tests/smoke.py` sebelum workshop |
| Profil Alias Model | Beralih cepat antara set model di berbagai mesin | Pertahankan `.env` dengan `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Efisiensi Caching | Hindari pemanasan berulang dalam menjalankan multi-sampel | Utilitas cache manajer; gunakan kembali di skrip/notebook |
| Pemanasan Awal | Kurangi lonjakan latensi p95 | Jalankan prompt kecil setelah pembuatan `FoundryLocalManager` |

Contoh baseline hangat deterministik (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Anda harus melihat output serupa & jumlah token identik pada pengujian kedua, mengonfirmasi determinisme.

## Langkah Selanjutnya

Setelah menyelesaikan sesi ini:

1. **Jelajahi Sesi 2**: Bangun solusi AI dengan Azure AI Foundry RAG
2. **Coba Model Berbeda**: Eksperimen dengan Qwen, DeepSeek, dan keluarga model lainnya
3. **Optimalkan Performa**: Sesuaikan pengaturan untuk perangkat keras spesifik Anda
4. **Bangun Aplikasi Kustom**: Gunakan Foundry Local SDK dalam proyek Anda sendiri

## Sumber Daya Tambahan

### Dokumentasi
- [Referensi Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Panduan Instalasi Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Katalog Model](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Kode Contoh
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - Integrasi SDK OpenAI
- [Module08 Sample 03](./samples/03/README.md) - Penemuan Model & Benchmarking

### Komunitas
- [Diskusi Foundry Local GitHub](https://github.com/microsoft/Foundry-Local/discussions)
- [Komunitas Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Durasi Sesi**: 30 menit praktik + 15 menit tanya jawab  
**Tingkat Kesulitan**: Pemula  
**Prasyarat**: Windows 11, Python 3.10+, akses Administrator  

## Skenario Contoh & Pemetaan Workshop

| Skrip Workshop / Notebook | Skenario | Tujuan | Contoh Input | Dataset yang Dibutuhkan |
|----------------------------|----------|-------|--------------|-------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Tim IT internal mengevaluasi inferensi di perangkat untuk portal penilaian privasi | Membuktikan SLM lokal merespons dalam latensi sub-detik pada prompt standar | "Sebutkan dua manfaat inferensi lokal." | Tidak ada (prompt tunggal) |
| Kode adaptasi quickstart | Pengembang yang memigrasi skrip OpenAI yang ada ke Foundry Local | Menunjukkan kompatibilitas langsung | "Sebutkan dua manfaat inferensi lokal." | Hanya prompt inline |

### Narasi Skenario
Tim keamanan & kepatuhan harus memvalidasi apakah data prototipe sensitif dapat diproses secara lokal. Mereka menjalankan skrip bootstrap dengan beberapa prompt (privasi, latensi, biaya) menggunakan mode deterministik temperature=0 untuk menangkap output baseline untuk perbandingan di kemudian hari (benchmarking Sesi 3 dan kontras Sesi 4 SLM vs LLM).

### Set Prompt Minimal JSON (opsional)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Gunakan daftar ini untuk membuat loop evaluasi yang dapat direproduksi atau untuk memulai kerangka pengujian regresi di masa depan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.