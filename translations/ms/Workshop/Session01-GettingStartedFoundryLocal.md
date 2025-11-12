<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T23:49:21+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ms"
}
-->
# Sesi 1: Memulakan dengan Foundry Local

## Abstrak

Pelajari cara memasang, mengkonfigurasi, dan menjalankan model AI pertama anda menggunakan Microsoft Foundry Local. Sesi praktikal ini memberikan pengenalan langkah demi langkah kepada inferens tempatan, dari pemasangan hingga membina aplikasi sembang pertama anda menggunakan model seperti Phi-4, Qwen, dan DeepSeek.

## Objektif Pembelajaran

Pada akhir sesi ini, anda akan:

- **Pasang dan Konfigurasi**: Menyediakan Foundry Local dengan pengesahan pemasangan yang betul
- **Kuasi Operasi CLI**: Menggunakan Foundry Local CLI untuk pengurusan dan penyebaran model
- **Jalankan Model Pertama Anda**: Berjaya menyebarkan dan berinteraksi dengan model AI tempatan
- **Bina Aplikasi Sembang**: Membuat aplikasi sembang asas menggunakan Foundry Local Python SDK
- **Fahami AI Tempatan**: Memahami asas inferens tempatan dan pengurusan model

## Prasyarat

### Keperluan Sistem

- **Windows**: Windows 11 (22H2 atau lebih baru) ATAU **macOS**: macOS 11+ (sokongan terhad)
- **RAM**: Minimum 8GB, disarankan 16GB+
- **Storan**: Ruang kosong 10GB+ untuk model
- **Python**: Versi 3.10 atau lebih baru dipasang
- **Akses Admin**: Keistimewaan pentadbir untuk pemasangan

### Persekitaran Pembangunan

- Visual Studio Code dengan sambungan Python (disarankan)
- Akses baris perintah (PowerShell di Windows, Terminal di macOS)
- Git untuk mengklon repositori (pilihan)

## Aliran Bengkel (30 minit)

### Langkah 1: Pasang Foundry Local (5 minit)

#### Pemasangan Windows

Pasang Foundry Local menggunakan pengurus pakej Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatif: Muat turun terus dari [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Pemasangan macOS (Sokongan Terhad)

> [!NOTE] 
> Sokongan macOS kini dalam pratonton. Semak dokumentasi rasmi untuk ketersediaan terkini.

Jika tersedia, pasang menggunakan Homebrew:

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
- Gunakan VM Windows 11 (Parallels/UTM) dan ikuti langkah Windows
- Jalankan melalui kontena jika tersedia dan konfigurasikan `FOUNDRY_LOCAL_ENDPOINT`

### Langkah 2: Sahkan Pemasangan (3 minit)

Selepas pemasangan, mulakan semula terminal anda dan sahkan Foundry Local berfungsi:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Output yang dijangkakan harus menunjukkan maklumat versi dan arahan yang tersedia.

### Langkah 3: Sediakan Persekitaran Python (5 minit)

Buat persekitaran Python khusus untuk bengkel ini:

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

### Langkah 4: Jalankan Model Pertama Anda (7 minit)

Sekarang mari kita jalankan model AI pertama kita secara tempatan!

#### Mulakan dengan Phi-4 Mini (Model Pertama yang Disarankan)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Perintah ini memuat turun model (kali pertama) dan secara automatik memulakan perkhidmatan Foundry Local.

#### Periksa Apa yang Sedang Berjalan

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Cuba Model Lain

Setelah phi-4-mini berfungsi, cuba model lain:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Langkah 5: Bina Aplikasi Sembang Pertama Anda (10 minit)

Sekarang mari kita buat aplikasi Python yang menggunakan model yang baru kita mulakan.

#### Buat Skrip Sembang

Buat fail baru bernama `my_first_chat.py` (atau gunakan sampel yang disediakan):

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
> **Contoh Berkaitan**: Untuk penggunaan yang lebih maju, lihat:
>
> - **Sampel Python**: `Workshop/samples/session01/chat_bootstrap.py` - Termasuk respons streaming dan pengendalian ralat
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Versi interaktif dengan penjelasan terperinci

#### Uji Aplikasi Sembang Anda

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatif: Gunakan sampel yang disediakan secara langsung

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Atau terokai notebook interaktif
Buka Workshop/notebooks/session01_chat_bootstrap.ipynb di VS Code

Cuba perbualan contoh ini:

- "Apa itu Microsoft Foundry Local?"
- "Senaraikan 3 manfaat menjalankan model AI secara tempatan"
- "Bantu saya memahami AI tepi"

## Apa yang Telah Anda Capai

Tahniah! Anda telah berjaya:

1. ✅ **Memasang Foundry Local** dan mengesahkan ia berfungsi
2. ✅ **Memulakan model AI pertama anda** (phi-4-mini) secara tempatan
3. ✅ **Menguji model yang berbeza** melalui baris perintah
4. ✅ **Membina aplikasi sembang** yang berhubung dengan AI tempatan anda
5. ✅ **Mengalami inferens AI tempatan** tanpa kebergantungan awan

## Memahami Apa yang Berlaku

### Inferens AI Tempatan

- Model AI anda berjalan sepenuhnya di komputer anda
- Tiada data dihantar ke awan
- Respons dihasilkan secara tempatan menggunakan CPU/GPU anda
- Privasi dan keselamatan terjamin

### Pengurusan Model

- `foundry model run` memuat turun dan memulakan model
- **FoundryLocalManager SDK** secara automatik mengendalikan permulaan perkhidmatan dan pemuatan model
- Model disimpan secara tempatan untuk penggunaan masa depan
- Beberapa model boleh dimuat turun tetapi biasanya satu berjalan pada satu masa
- Perkhidmatan secara automatik menguruskan kitaran hayat model

### Pendekatan SDK vs CLI

- **Pendekatan CLI**: Pengurusan model manual dengan `foundry model run <model>`
- **Pendekatan SDK**: Pengurusan perkhidmatan + model automatik dengan `FoundryLocalManager(alias)`
- **Rekomendasi**: Gunakan SDK untuk aplikasi, CLI untuk ujian dan penerokaan

## Rujukan Perintah Biasa

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

- **phi-4-mini**: Model permulaan terbaik - pantas, ringan, kualiti baik
- **qwen2.5-0.5b**: Inferens terpantas, penggunaan memori minimum
- **gpt-oss-20b**: Respons berkualiti tinggi, memerlukan lebih banyak sumber
- **deepseek-coder-1.3b**: Dioptimumkan untuk tugas pengaturcaraan dan kod

## Penyelesaian Masalah

### "Foundry command not found"

**Penyelesaian:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model failed to load"

**Penyelesaian:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connection refused on localhost"

**Penyelesaian:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Langkah Seterusnya

### Tindakan Segera Seterusnya

1. **Eksperimen** dengan model dan arahan yang berbeza
2. **Ubah** aplikasi sembang anda untuk mencuba model yang berbeza
3. **Cipta** arahan anda sendiri dan uji respons
4. **Terokai** Sesi 2: Membina aplikasi RAG

### Laluan Pembelajaran Lanjutan

1. **Sesi 2**: Bina penyelesaian AI dengan RAG (Retrieval-Augmented Generation)
2. **Sesi 3**: Bandingkan model sumber terbuka yang berbeza
3. **Sesi 4**: Bekerja dengan model terkini
4. **Sesi 5**: Bina sistem AI multi-agen

## Pembolehubah Persekitaran (Pilihan)

Untuk penggunaan yang lebih maju, anda boleh menetapkan pembolehubah persekitaran ini:

| Pembolehubah | Tujuan | Contoh |
|--------------|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Model lalai untuk digunakan | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Ganti URL endpoint | `http://localhost:5273/v1` |

Buat fail `.env` dalam direktori projek anda:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Sumber Tambahan

### Dokumentasi

- [Rujukan Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Panduan Pemasangan Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Katalog Model](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Kod Sampel

- **Sampel Python Sesi01**: `Workshop/samples/session01/chat_bootstrap.py` - Aplikasi sembang lengkap dengan streaming
- **Notebook Sesi01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Tutorial interaktif  
- [Sampel Modul08 01](../Module08/samples/01/README.md) - Pantas REST Chat
- [Sampel Modul08 02](../Module08/samples/02/README.md) - Integrasi OpenAI SDK
- [Sampel Modul08 03](../Module08/samples/03/README.md) - Penemuan & Penanda Aras Model

### Komuniti

- [Perbincangan GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Komuniti Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Tempoh Sesi**: 30 minit praktikal + 15 minit Q&A  
**Tahap Kesukaran**: Pemula  
**Prasyarat**: Windows 11/macOS 11+, Python 3.10+, Akses Admin

## Senario Contoh Bengkel

### Konteks Dunia Nyata

**Senario**: Pasukan IT perusahaan perlu menilai inferens AI pada peranti untuk memproses maklum balas pekerja yang sensitif tanpa menghantar data ke perkhidmatan luaran.

**Matlamat Anda**: Menunjukkan bahawa model AI tempatan dapat memberikan respons berkualiti dengan latensi kurang dari satu saat sambil mengekalkan privasi data sepenuhnya.

### Arahan Ujian

Gunakan arahan ini untuk mengesahkan persediaan anda:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Kriteria Kejayaan

- ✅ Semua arahan mendapat respons dalam masa kurang dari 2 saat
- ✅ Tiada data meninggalkan mesin tempatan anda
- ✅ Respons adalah relevan dan berguna
- ✅ Aplikasi sembang anda berfungsi dengan lancar

Pengesahan ini memastikan persediaan Foundry Local anda sedia untuk bengkel lanjutan dalam Sesi 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->