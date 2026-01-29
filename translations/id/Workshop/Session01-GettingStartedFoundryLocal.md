# Sesi 1: Memulai dengan Foundry Local

## Abstrak

Pelajari cara menginstal, mengonfigurasi, dan menjalankan model AI pertama Anda menggunakan Microsoft Foundry Local. Sesi praktis ini memberikan pengenalan langkah demi langkah tentang inferensi lokal, mulai dari instalasi hingga membangun aplikasi chat pertama Anda menggunakan model seperti Phi-4, Qwen, dan DeepSeek.

## Tujuan Pembelajaran

Pada akhir sesi ini, Anda akan:

- **Menginstal dan Mengonfigurasi**: Menyiapkan Foundry Local dengan verifikasi instalasi yang tepat
- **Menguasai Operasi CLI**: Menggunakan Foundry Local CLI untuk manajemen dan penerapan model
- **Menjalankan Model Pertama Anda**: Berhasil menerapkan dan berinteraksi dengan model AI lokal
- **Membangun Aplikasi Chat**: Membuat aplikasi chat dasar menggunakan Foundry Local Python SDK
- **Memahami AI Lokal**: Memahami dasar-dasar inferensi lokal dan manajemen model

## Prasyarat

### Persyaratan Sistem

- **Windows**: Windows 11 (22H2 atau lebih baru) ATAU **macOS**: macOS 11+ (dukungan terbatas)
- **RAM**: Minimal 8GB, disarankan 16GB+
- **Penyimpanan**: Ruang kosong 10GB+ untuk model
- **Python**: Terinstal versi 3.10 atau lebih baru
- **Akses Admin**: Hak administrator untuk instalasi

### Lingkungan Pengembangan

- Visual Studio Code dengan ekstensi Python (disarankan)
- Akses command line (PowerShell di Windows, Terminal di macOS)
- Git untuk cloning repositori (opsional)

## Alur Workshop (30 menit)

### Langkah 1: Instal Foundry Local (5 menit)

#### Instalasi Windows

Instal Foundry Local menggunakan pengelola paket Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatif: Unduh langsung dari [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Instalasi macOS (Dukungan Terbatas)

> [!NOTE] 
> Dukungan macOS saat ini dalam tahap pratinjau. Periksa dokumentasi resmi untuk ketersediaan terbaru.

Jika tersedia, instal menggunakan Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternatif untuk pengguna macOS:**
- Gunakan VM Windows 11 (Parallels/UTM) dan ikuti langkah-langkah Windows
- Jalankan melalui container jika tersedia dan konfigurasikan `FOUNDRY_LOCAL_ENDPOINT`

### Langkah 2: Verifikasi Instalasi (3 menit)

Setelah instalasi, restart terminal Anda dan verifikasi Foundry Local berfungsi:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Output yang diharapkan harus menunjukkan informasi versi dan perintah yang tersedia.

### Langkah 3: Siapkan Lingkungan Python (5 menit)

Buat lingkungan Python khusus untuk workshop ini:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Langkah 4: Jalankan Model Pertama Anda (7 menit)

Sekarang mari kita jalankan model AI pertama kita secara lokal!

#### Mulai dengan Phi-4 Mini (Model Pertama yang Direkomendasikan)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Perintah ini mengunduh model (pertama kali) dan secara otomatis memulai layanan Foundry Local.

#### Periksa Apa yang Sedang Berjalan

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Coba Model Lain

Setelah phi-4-mini berfungsi, coba model lainnya:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Langkah 5: Bangun Aplikasi Chat Pertama Anda (10 menit)

Sekarang mari kita buat aplikasi Python yang menggunakan model yang baru saja kita mulai.

#### Buat Skrip Chat

Buat file baru bernama `my_first_chat.py` (atau gunakan sampel yang disediakan):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Contoh Terkait**: Untuk penggunaan yang lebih lanjut, lihat:
>
> - **Contoh Python**: `Workshop/samples/session01/chat_bootstrap.py` - Termasuk respons streaming dan penanganan error
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Versi interaktif dengan penjelasan rinci

#### Uji Aplikasi Chat Anda

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatif: Gunakan sampel yang disediakan langsung

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Atau jelajahi notebook interaktif
Buka Workshop/notebooks/session01_chat_bootstrap.ipynb di VS Code

Coba percakapan contoh berikut:

- "Apa itu Microsoft Foundry Local?"
- "Sebutkan 3 manfaat menjalankan model AI secara lokal"
- "Bantu saya memahami edge AI"

## Apa yang Telah Anda Capai

Selamat! Anda telah berhasil:

1. ✅ **Menginstal Foundry Local** dan memverifikasi bahwa itu berfungsi
2. ✅ **Memulai model AI pertama Anda** (phi-4-mini) secara lokal
3. ✅ **Menguji model yang berbeda** melalui command line
4. ✅ **Membangun aplikasi chat** yang terhubung ke AI lokal Anda
5. ✅ **Mengalami inferensi AI lokal** tanpa ketergantungan cloud

## Memahami Apa yang Terjadi

### Inferensi AI Lokal

- Model AI Anda berjalan sepenuhnya di komputer Anda
- Tidak ada data yang dikirim ke cloud
- Respons dihasilkan secara lokal menggunakan CPU/GPU Anda
- Privasi dan keamanan terjaga

### Manajemen Model

- `foundry model run` mengunduh dan memulai model
- **FoundryLocalManager SDK** secara otomatis menangani startup layanan dan pemuatan model
- Model disimpan secara lokal untuk penggunaan di masa depan
- Beberapa model dapat diunduh tetapi biasanya hanya satu yang berjalan pada satu waktu
- Layanan secara otomatis mengelola siklus hidup model

### Pendekatan SDK vs CLI

- **Pendekatan CLI**: Manajemen model manual dengan `foundry model run <model>`
- **Pendekatan SDK**: Manajemen layanan + model otomatis dengan `FoundryLocalManager(alias)`
- **Rekomendasi**: Gunakan SDK untuk aplikasi, CLI untuk pengujian dan eksplorasi

## Referensi Perintah Umum

### Perintah CLI Penting

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Rekomendasi Model

- **phi-4-mini**: Model pemula terbaik - cepat, ringan, kualitas baik
- **qwen2.5-0.5b**: Inferensi tercepat, penggunaan memori minimal
- **gpt-oss-20b**: Respons berkualitas lebih tinggi, membutuhkan lebih banyak sumber daya
- **deepseek-coder-1.3b**: Dioptimalkan untuk tugas pemrograman dan kode

## Pemecahan Masalah

### "Foundry command not found"

**Solusi:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model failed to load"

**Solusi:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connection refused on localhost"

**Solusi:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Langkah Selanjutnya

### Tindakan Langsung Berikutnya

1. **Eksperimen** dengan model dan prompt yang berbeda
2. **Modifikasi** aplikasi chat Anda untuk mencoba model yang berbeda
3. **Buat** prompt Anda sendiri dan uji responsnya
4. **Jelajahi** Sesi 2: Membangun aplikasi RAG

### Jalur Pembelajaran Lanjutan

1. **Sesi 2**: Bangun solusi AI dengan RAG (Retrieval-Augmented Generation)
2. **Sesi 3**: Bandingkan model open-source yang berbeda
3. **Sesi 4**: Bekerja dengan model mutakhir
4. **Sesi 5**: Bangun sistem AI multi-agen

## Variabel Lingkungan (Opsional)

Untuk penggunaan yang lebih lanjut, Anda dapat mengatur variabel lingkungan berikut:

| Variabel | Tujuan | Contoh |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Model default yang digunakan | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Override URL endpoint | `http://localhost:5273/v1` |

Buat file `.env` di direktori proyek Anda:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Sumber Daya Tambahan

### Dokumentasi

- [Referensi Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Panduan Instalasi Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Katalog Model](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Contoh Kode

- **Contoh Python Sesi01**: `Workshop/samples/session01/chat_bootstrap.py` - Aplikasi chat lengkap dengan streaming
- **Notebook Sesi01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Tutorial interaktif  
- [Contoh Modul08 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Contoh Modul08 02](../Module08/samples/02/README.md) - Integrasi OpenAI SDK
- [Contoh Modul08 03](../Module08/samples/03/README.md) - Penemuan & Benchmarking Model

### Komunitas

- [Diskusi GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Komunitas Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Durasi Sesi**: 30 menit praktik + 15 menit tanya jawab  
**Tingkat Kesulitan**: Pemula  
**Prasyarat**: Windows 11/macOS 11+, Python 3.10+, Akses Admin

## Contoh Skenario Workshop

### Konteks Dunia Nyata

**Skenario**: Tim IT perusahaan perlu mengevaluasi inferensi AI di perangkat untuk memproses umpan balik karyawan yang sensitif tanpa mengirim data ke layanan eksternal.

**Tujuan Anda**: Menunjukkan bahwa model AI lokal dapat memberikan respons berkualitas dengan latensi di bawah satu detik sambil menjaga privasi data sepenuhnya.

### Prompt Pengujian

Gunakan prompt ini untuk memvalidasi pengaturan Anda:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Kriteria Keberhasilan

- ✅ Semua prompt mendapatkan respons dalam waktu kurang dari 2 detik
- ✅ Tidak ada data yang meninggalkan mesin lokal Anda
- ✅ Respons relevan dan membantu
- ✅ Aplikasi chat Anda berjalan dengan lancar

Validasi ini memastikan pengaturan Foundry Local Anda siap untuk workshop lanjutan di Sesi 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->