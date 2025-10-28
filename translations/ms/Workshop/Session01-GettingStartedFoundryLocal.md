<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:24:37+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ms"
}
-->
# Sesi 1: Memulakan dengan Foundry Local

## Abstrak

Mulakan perjalanan anda dengan Foundry Local dengan memasang dan mengkonfigurasinya pada Windows 11. Pelajari cara menyediakan CLI, mengaktifkan pecutan perkakasan, dan cache model untuk inferens tempatan yang pantas. Sesi praktikal ini menunjukkan cara menjalankan model seperti Phi, Qwen, DeepSeek, dan GPT-OSS-20B menggunakan arahan CLI yang boleh diulang.

## Objektif Pembelajaran

Pada akhir sesi ini, anda akan:

- **Pasang dan Konfigurasi**: Sediakan Foundry Local pada Windows 11 dengan tetapan prestasi yang optimum
- **Kuasa Operasi CLI**: Gunakan Foundry Local CLI untuk pengurusan dan penyebaran model
- **Aktifkan Pecutan Perkakasan**: Konfigurasi pecutan GPU dengan ONNXRuntime atau WebGPU
- **Sebarkan Pelbagai Model**: Jalankan model phi-4, GPT-OSS-20B, Qwen, dan DeepSeek secara tempatan
- **Bina Aplikasi Pertama Anda**: Sesuaikan sampel sedia ada untuk menggunakan Foundry Local Python SDK

# Uji model (prompt tunggal tidak interaktif)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 atau lebih baru)
# Senaraikan model katalog yang tersedia (model yang dimuatkan muncul selepas dijalankan)
foundry model list
## NOTE: Tiada flag `--running` khusus buat masa ini; untuk melihat yang dimuatkan, mulakan chat atau periksa log perkhidmatan.
- Python 3.10+ dipasang
- Visual Studio Code dengan sambungan Python
- Keistimewaan pentadbir untuk pemasangan

### (Pilihan) Pembolehubah Persekitaran

Buat `.env` (atau tetapkan dalam shell) untuk menjadikan skrip mudah alih:
# Bandingkan respons (tidak interaktif)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| Pembolehubah | Tujuan | Contoh |
|--------------|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Alias model pilihan (katalog secara automatik memilih varian terbaik) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Ganti endpoint (jika tidak, auto dari pengurus) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Aktifkan demo streaming | `true` |

> Jika `FOUNDRY_LOCAL_ENDPOINT=auto` (atau tidak ditetapkan) ia akan diperoleh daripada pengurus SDK.

## Aliran Demo (30 minit)

### 1. Pasang Foundry Local dan Sahkan Persediaan CLI (10 minit)

# Senaraikan model yang di-cache
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Pratonton / Jika Disokong)**

Jika pakej macOS asli disediakan (periksa dokumen rasmi untuk yang terkini):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Jika binari asli macOS belum tersedia, anda masih boleh: 
1. Gunakan VM Windows 11 ARM/Intel (Parallels / UTM) dan ikuti langkah Windows. 
2. Jalankan model melalui container (jika imej container diterbitkan) dan tetapkan `FOUNDRY_LOCAL_ENDPOINT` ke port yang didedahkan. 

**Buat Persekitaran Maya Python (Merentas Platform)**

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

Naik taraf pip dan pasang kebergantungan teras:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Langkah 1.2: Sahkan Pemasangan

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Langkah 1.3: Konfigurasi Persekitaran

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Bootstrapping SDK (Disyorkan)

Daripada memulakan perkhidmatan secara manual & menjalankan model, **Foundry Local Python SDK** boleh bootstrap semuanya:

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

Jika anda lebih suka kawalan eksplisit, anda masih boleh menggunakan CLI + klien OpenAI seperti yang ditunjukkan kemudian.

### 2. Jalankan Model Secara Tempatan melalui CLI (10 minit)

#### Langkah 3.1: Sebarkan Model Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Langkah 3.2: Sebarkan GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Langkah 3.3: Muatkan Model Tambahan

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Projek Permulaan: Sesuaikan 01-run-phi untuk Foundry Local (5 minit)

#### Langkah 4.1: Buat Aplikasi Chat Asas

Buat `samples/01-foundry-quickstart/chat_quickstart.py` (dikemas kini untuk menggunakan pengurus jika tersedia):

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

## Konsep Utama yang Diliputi

### 1. Seni Bina Foundry Local

- **Enjin Inferens Tempatan**: Menjalankan model sepenuhnya pada peranti anda
- **Keserasian SDK OpenAI**: Integrasi lancar dengan kod OpenAI sedia ada
- **Pengurusan Model**: Muat turun, cache, dan jalankan pelbagai model dengan cekap
- **Pengoptimuman Perkakasan**: Manfaatkan pecutan GPU, NPU, dan CPU

### 2. Rujukan Arahan CLI

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

## Menyelesaikan Masalah Biasa

### Isu 1: "Foundry command not found"

**Penyelesaian:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Isu 2: "Model failed to load"

**Penyelesaian:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Isu 3: "Connection refused on localhost:5273"

**Penyelesaian:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Petua Pengoptimuman Prestasi

### 1. Strategi Pemilihan Model

- **Phi-4-mini**: Terbaik untuk tugas umum, penggunaan memori rendah
- **Qwen2.5-0.5b**: Inferens terpantas, sumber minimum
- **GPT-OSS-20B**: Kualiti tertinggi, memerlukan lebih banyak sumber
- **DeepSeek-Coder**: Dioptimumkan untuk tugas pengaturcaraan

### 2. Pengoptimuman Perkakasan

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Pemantauan Prestasi

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

### Peningkatan Pilihan

| Peningkatan | Apa | Bagaimana |
|-------------|-----|----------|
| Utiliti Berkongsi | Buang logik klien/bootstrap yang berulang | Gunakan `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Penglihatan Penggunaan Token | Ajarkan pemikiran kos/kecekapan lebih awal | Tetapkan `SHOW_USAGE=1` untuk mencetak prompt/penyelesaian/total token |
| Perbandingan Deterministik | Penanda aras stabil & pemeriksaan regresi | Gunakan `temperature=0`, `top_p=1`, teks prompt yang konsisten |
| Latensi Token Pertama | Metrik responsif yang dirasakan | Sesuaikan skrip penanda aras dengan streaming (`BENCH_STREAM=1`) |
| Ulang pada Kesalahan Sementara | Demo tahan lasak pada permulaan sejuk | `RETRY_ON_FAIL=1` (lalai) & sesuaikan `RETRY_BACKOFF` |
| Ujian Asap | Sanity cepat merentas aliran utama | Jalankan `python Workshop/tests/smoke.py` sebelum bengkel |
| Profil Alias Model | Berpindah set model dengan cepat antara mesin | Kekalkan `.env` dengan `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Kecekapan Cache | Elakkan pemanasan berulang dalam larian multi-sampel | Pengurus cache utiliti; gunakan semula merentas skrip/notebook |
| Pemanasan Larian Pertama | Kurangkan lonjakan latensi p95 | Jalankan prompt kecil selepas penciptaan `FoundryLocalManager` |

Contoh asas hangat deterministik (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Anda sepatutnya melihat output serupa & jumlah token yang sama pada larian kedua, mengesahkan determinisme.

## Langkah Seterusnya

Selepas melengkapkan sesi ini:

1. **Terokai Sesi 2**: Bina penyelesaian AI dengan Azure AI Foundry RAG
2. **Cuba Model Berbeza**: Eksperimen dengan Qwen, DeepSeek, dan keluarga model lain
3. **Optimumkan Prestasi**: Laraskan tetapan untuk perkakasan spesifik anda
4. **Bina Aplikasi Tersuai**: Gunakan Foundry Local SDK dalam projek anda sendiri

## Sumber Tambahan

### Dokumentasi
- [Rujukan Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Panduan Pemasangan Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Katalog Model](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Kod Sampel
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - Integrasi SDK OpenAI
- [Module08 Sample 03](./samples/03/README.md) - Penemuan & Penanda Aras Model

### Komuniti
- [Perbincangan GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Komuniti Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Tempoh Sesi**: 30 minit praktikal + 15 minit Q&A
**Tahap Kesukaran**: Pemula
**Prasyarat**: Windows 11, Python 3.10+, akses Pentadbir

## Senario Sampel & Pemetaan Bengkel

| Skrip Bengkel / Notebook | Senario | Matlamat | Input Contoh | Dataset Diperlukan |
|--------------------------|---------|---------|-------------|--------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Pasukan IT dalaman menilai inferens pada peranti untuk portal penilaian privasi | Buktikan SLM tempatan bertindak balas dalam latensi sub-saat pada prompt standard | "Senaraikan dua manfaat inferens tempatan." | Tiada (prompt tunggal) |
| Kod adaptasi quickstart | Pembangun memindahkan skrip OpenAI sedia ada ke Foundry Local | Tunjukkan keserasian drop-in | "Berikan dua manfaat inferens tempatan." | Hanya prompt dalam talian |

### Naratif Senario
Pasukan keselamatan & pematuhan mesti mengesahkan sama ada data prototaip sensitif boleh diproses secara tempatan. Mereka menjalankan skrip bootstrap dengan beberapa prompt (privasi, latensi, kos) menggunakan mod deterministik temperature=0 untuk menangkap output asas untuk perbandingan kemudian (penanda aras Sesi 3 dan kontras Sesi 4 SLM vs LLM).

### Set Prompt Minimum JSON (pilihan)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Gunakan senarai ini untuk mencipta gelung penilaian yang boleh diulang atau untuk memulakan harness ujian regresi masa depan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.