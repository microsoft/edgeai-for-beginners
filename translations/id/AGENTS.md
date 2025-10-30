<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T13:39:58+00:00",
  "source_file": "AGENTS.md",
  "language_code": "id"
}
-->
# AGENTS.md

> **Panduan Pengembang untuk Berkontribusi pada EdgeAI untuk Pemula**
> 
> Dokumen ini menyediakan informasi lengkap untuk pengembang, agen AI, dan kontributor yang bekerja dengan repositori ini. Dokumen ini mencakup pengaturan, alur kerja pengembangan, pengujian, dan praktik terbaik.
> 
> **Terakhir Diperbarui**: 30 Oktober 2025 | **Versi Dokumen**: 3.0

## Daftar Isi

- [Ikhtisar Proyek](../..)
- [Struktur Repositori](../..)
- [Prasyarat](../..)
- [Perintah Pengaturan](../..)
- [Alur Kerja Pengembangan](../..)
- [Instruksi Pengujian](../..)
- [Panduan Gaya Kode](../..)
- [Panduan Pull Request](../..)
- [Sistem Terjemahan](../..)
- [Integrasi Foundry Local](../..)
- [Pembangunan dan Penerapan](../..)
- [Masalah Umum dan Pemecahan Masalah](../..)
- [Sumber Daya Tambahan](../..)
- [Catatan Khusus Proyek](../..)
- [Mendapatkan Bantuan](../..)

## Ikhtisar Proyek

EdgeAI untuk Pemula adalah repositori edukasi yang komprehensif yang mengajarkan pengembangan Edge AI dengan Small Language Models (SLMs). Kursus ini mencakup dasar-dasar EdgeAI, penerapan model, teknik optimasi, dan implementasi siap produksi menggunakan Microsoft Foundry Local dan berbagai kerangka kerja AI.

**Teknologi Utama:**
- Python 3.8+ (bahasa utama untuk sampel AI/ML)
- .NET C# (Sampel AI/ML)
- JavaScript/Node.js dengan Electron (untuk aplikasi desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Kerangka Kerja AI: LangChain, Semantic Kernel, Chainlit
- Optimasi Model: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Jenis Repositori:** Repositori konten edukasi dengan 8 modul dan 10 aplikasi sampel yang komprehensif

**Arsitektur:** Jalur pembelajaran multi-modul dengan sampel praktis yang menunjukkan pola penerapan Edge AI

## Struktur Repositori

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Prasyarat

### Alat yang Diperlukan

- **Python 3.8+** - Untuk sampel AI/ML dan notebook
- **Node.js 16+** - Untuk aplikasi sampel Electron
- **Git** - Untuk kontrol versi
- **Microsoft Foundry Local** - Untuk menjalankan model AI secara lokal

### Alat yang Direkomendasikan

- **Visual Studio Code** - Dengan ekstensi Python, Jupyter, dan Pylance
- **Windows Terminal** - Untuk pengalaman baris perintah yang lebih baik (pengguna Windows)
- **Docker** - Untuk pengembangan dalam kontainer (opsional)

### Persyaratan Sistem

- **RAM**: Minimal 8GB, direkomendasikan 16GB+ untuk skenario multi-model
- **Penyimpanan**: Ruang kosong 10GB+ untuk model dan dependensi
- **OS**: Windows 10/11, macOS 11+, atau Linux (Ubuntu 20.04+)
- **Perangkat Keras**: CPU dengan dukungan AVX2; GPU (CUDA, Qualcomm NPU) opsional tetapi direkomendasikan

### Prasyarat Pengetahuan

- Pemahaman dasar tentang pemrograman Python
- Familiaritas dengan antarmuka baris perintah
- Pemahaman konsep AI/ML (untuk pengembangan sampel)
- Alur kerja Git dan proses pull request

## Perintah Pengaturan

### Pengaturan Repositori

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Pengaturan Sampel Python (Modul08 dan sampel Workshop)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Pengaturan Sampel Node.js (Sampel 08 - Aplikasi Chat Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Pengaturan Foundry Local

Foundry Local diperlukan untuk menjalankan sampel. Unduh dan instal dari repositori resmi:

**Instalasi:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: Unduh dari [halaman rilis](https://github.com/microsoft/Foundry-Local/releases)

**Panduan Cepat:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Catatan**: Foundry Local secara otomatis memilih varian model terbaik untuk perangkat keras Anda (GPU CUDA, NPU Qualcomm, atau CPU).

## Alur Kerja Pengembangan

### Pengembangan Konten

Repositori ini terutama berisi **konten edukasi Markdown**. Saat melakukan perubahan:

1. Edit file `.md` di direktori modul yang sesuai
2. Ikuti pola format yang ada
3. Pastikan contoh kode akurat dan telah diuji
4. Perbarui konten terjemahan yang sesuai jika diperlukan (atau biarkan otomatisasi menangani)

### Pengembangan Aplikasi Sampel

Untuk sampel Python Modul08 (sampel 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Untuk sampel Python Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Untuk sampel Electron (sampel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Pengujian Aplikasi Sampel

Sampel Python tidak memiliki pengujian otomatis tetapi dapat divalidasi dengan menjalankannya:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Sampel Electron memiliki infrastruktur pengujian:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instruksi Pengujian

### Validasi Konten

Repositori menggunakan alur kerja terjemahan otomatis. Tidak diperlukan pengujian manual untuk terjemahan.

**Validasi manual untuk perubahan konten:**
1. Tinjau rendering Markdown dengan melihat pratinjau file `.md`
2. Verifikasi semua tautan mengarah ke target yang valid
3. Uji cuplikan kode yang disertakan dalam dokumentasi
4. Periksa apakah gambar dimuat dengan benar

### Pengujian Aplikasi Sampel

**Module08/samples/08 (aplikasi Electron) memiliki pengujian yang komprehensif:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Sampel Python harus diuji secara manual:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Panduan Gaya Kode

### Konten Markdown

- Gunakan hierarki judul yang konsisten (# untuk judul, ## untuk bagian utama, ### untuk subbagian)
- Sertakan blok kode dengan spesifikasi bahasa: ```python, ```bash, ```javascript
- Ikuti format yang ada untuk tabel, daftar, dan penekanan
- Jaga agar baris tetap mudah dibaca (usahakan ~80-100 karakter, tetapi tidak ketat)
- Gunakan tautan relatif untuk referensi internal

### Gaya Kode Python

- Ikuti konvensi PEP 8
- Gunakan petunjuk tipe jika sesuai
- Sertakan docstring untuk fungsi dan kelas
- Gunakan nama variabel yang bermakna
- Jaga agar fungsi tetap fokus dan ringkas

### Gaya Kode JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Konvensi utama:**
- Konfigurasi ESLint disediakan dalam sampel 08
- Prettier untuk format kode
- Gunakan sintaks modern ES6+
- Ikuti pola yang ada dalam basis kode

## Panduan Pull Request

### Alur Kerja Kontribusi

1. **Fork repositori** dan buat cabang baru dari `main`
2. **Lakukan perubahan Anda** mengikuti panduan gaya kode
3. **Uji secara menyeluruh** menggunakan instruksi pengujian di atas
4. **Commit dengan pesan yang jelas** mengikuti format commit konvensional
5. **Push ke fork Anda** dan buat pull request
6. **Tanggapi umpan balik** dari pemelihara selama tinjauan

### Konvensi Penamaan Cabang

- `feature/<modul>-<deskripsi>` - Untuk fitur atau konten baru
- `fix/<modul>-<deskripsi>` - Untuk perbaikan bug
- `docs/<deskripsi>` - Untuk perbaikan dokumentasi
- `refactor/<deskripsi>` - Untuk refaktor kode

### Format Pesan Commit

Ikuti [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Contoh:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Format Judul
```
[ModuleXX] Brief description of change
```
atau
```
[Module08/samples/XX] Description for sample changes
```

### Kode Etik

Semua kontributor harus mengikuti [Kode Etik Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/). Harap tinjau [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) sebelum berkontribusi.

### Sebelum Mengirimkan

**Untuk perubahan konten:**
- Pratinjau semua file Markdown yang dimodifikasi
- Verifikasi tautan dan gambar berfungsi
- Periksa kesalahan ketik dan tata bahasa

**Untuk perubahan kode sampel (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Untuk perubahan sampel Python:**
- Uji sampel berjalan dengan sukses
- Verifikasi penanganan kesalahan berfungsi
- Periksa kompatibilitas dengan Foundry Local

### Proses Tinjauan

- Perubahan konten edukasi ditinjau untuk akurasi dan kejelasan
- Sampel kode diuji untuk fungsionalitas
- Pembaruan terjemahan ditangani secara otomatis oleh GitHub Actions

## Sistem Terjemahan

**PENTING:** Repositori ini menggunakan terjemahan otomatis melalui GitHub Actions.

- Terjemahan berada di direktori `/translations/` (50+ bahasa)
- Otomatis melalui alur kerja `co-op-translator.yml`
- **JANGAN mengedit file terjemahan secara manual** - file tersebut akan ditimpa
- Edit hanya file sumber bahasa Inggris di direktori root dan modul
- Terjemahan secara otomatis dihasilkan saat push ke cabang `main`

## Integrasi Foundry Local

Sebagian besar sampel Modul08 memerlukan Microsoft Foundry Local untuk berjalan.

### Instalasi & Pengaturan

**Instal Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Instal Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Memulai Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Penggunaan SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Verifikasi Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Variabel Lingkungan untuk Sampel

Sebagian besar sampel menggunakan variabel lingkungan berikut:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Catatan**: Saat menggunakan `FoundryLocalManager`, SDK secara otomatis menangani penemuan layanan dan pemuatan model. Alias model (seperti `phi-3.5-mini`) memastikan varian terbaik dipilih untuk perangkat keras Anda.

## Pembangunan dan Penerapan

### Penerapan Konten

Repositori ini terutama dokumentasi - tidak diperlukan proses pembangunan untuk konten.

### Pembangunan Aplikasi Sampel

**Aplikasi Electron (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Sampel Python:**
Tidak ada proses pembangunan - sampel dijalankan langsung dengan interpreter Python.

## Masalah Umum dan Pemecahan Masalah

> **Tip**: Periksa [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) untuk masalah dan solusi yang diketahui.

### Masalah Kritis (Menghambat)

#### Foundry Local Tidak Berjalan
**Masalah:** Sampel gagal dengan kesalahan koneksi

**Solusi:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Masalah Umum (Sedang)

#### Masalah Lingkungan Virtual Python
**Masalah:** Kesalahan impor modul

**Solusi:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Masalah Pembangunan Electron
**Masalah:** npm install atau kegagalan pembangunan

**Solusi:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Masalah Alur Kerja (Ringan)

#### Konflik Alur Kerja Terjemahan
**Masalah:** PR terjemahan konflik dengan perubahan Anda

**Solusi:**
- Edit hanya file sumber bahasa Inggris
- Biarkan alur kerja terjemahan otomatis menangani terjemahan
- Jika terjadi konflik, gabungkan `main` ke cabang Anda setelah terjemahan digabungkan

#### Kegagalan Unduhan Model
**Masalah:** Foundry Local gagal mengunduh model

**Solusi:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Sumber Daya Tambahan

### Jalur Pembelajaran
- **Jalur Pemula:** Modul 01-02 (7-9 jam)
- **Jalur Menengah:** Modul 03-04 (9-11 jam)
- **Jalur Lanjutan:** Modul 05-07 (12-15 jam)
- **Jalur Ahli:** Modul 08 (8-10 jam)
- **Workshop Praktis:** Materi workshop (6-8 jam)

### Konten Modul Utama
- **Modul01:** Dasar-dasar EdgeAI dan studi kasus dunia nyata
- **Modul02:** Keluarga dan arsitektur Small Language Model (SLM)
- **Modul03:** Strategi penerapan lokal dan cloud
- **Modul04:** Optimasi model dengan berbagai kerangka kerja (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modul05:** SLMOps - operasi produksi
- **Modul06:** Agen AI dan pemanggilan fungsi
- **Modul07:** Implementasi spesifik platform
- **Modul08:** Toolkit Foundry Local dengan 10 sampel komprehensif

### Dependensi Eksternal
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime model AI lokal dengan API kompatibel OpenAI
  - [Dokumentasi](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Kerangka kerja optimasi
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit optimasi model
- [OpenVINO](https://docs.openvino.ai/) - Toolkit optimasi Intel

## Catatan Khusus Proyek

### Aplikasi Sampel Modul08

Repositori ini mencakup 10 aplikasi sampel yang komprehensif:

1. **01-REST Chat Quickstart** - Integrasi SDK OpenAI dasar
2. **02-OpenAI SDK Integration** - Fitur SDK lanjutan
3. **03-Model Discovery & Benchmarking** - Alat perbandingan model
4. **04-Chainlit RAG Application** - Generasi berbasis pengambilan
5. **05-Multi-Agent Orchestration** - Koordinasi agen dasar
6. **06-Models-as-Tools Router** - Pengarahan model cerdas
7. **07-Direct API Client** - Integrasi API tingkat rendah
8. **08-Windows 11 Chat App** - Aplikasi desktop Electron native
9. **09-Advanced Multi-Agent System** - Orkestrasi agen kompleks
10. **10-Kerangka Alat Foundry** - Integrasi LangChain/Semantic Kernel

### Aplikasi Contoh Workshop

Workshop ini mencakup 6 sesi progresif dengan implementasi praktis:

1. **Sesi 01** - Memulai chat dengan integrasi Foundry Local
2. **Sesi 02** - Pipeline RAG dan evaluasi dengan RAGAS
3. **Sesi 03** - Benchmarking model open-source
4. **Sesi 04** - Perbandingan dan pemilihan model
5. **Sesi 05** - Sistem orkestrasi multi-agen
6. **Sesi 06** - Pengaturan routing model dan manajemen pipeline

Setiap contoh menunjukkan berbagai aspek pengembangan AI edge dengan Foundry Local.

### Pertimbangan Performa

- SLM dioptimalkan untuk penerapan edge (2-16GB RAM)
- Inferensi lokal memberikan waktu respons 50-500ms
- Teknik kuantisasi mencapai pengurangan ukuran 75% dengan retensi performa 85%
- Kemampuan percakapan real-time dengan model lokal

### Keamanan dan Privasi

- Semua pemrosesan dilakukan secara lokal - tidak ada data yang dikirim ke cloud
- Cocok untuk aplikasi yang sensitif terhadap privasi (kesehatan, keuangan)
- Memenuhi persyaratan kedaulatan data
- Foundry Local sepenuhnya berjalan di perangkat keras lokal

## Mendapatkan Bantuan

### Dokumentasi

- **README Utama**: [README.md](README.md) - Gambaran umum repositori dan jalur pembelajaran
- **Panduan Studi**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Sumber daya pembelajaran dan timeline
- **Dukungan**: [SUPPORT.md](SUPPORT.md) - Cara mendapatkan bantuan
- **Keamanan**: [SECURITY.md](SECURITY.md) - Melaporkan masalah keamanan

### Dukungan Komunitas

- **GitHub Issues**: [Laporkan bug atau minta fitur](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Diskusi GitHub**: [Ajukan pertanyaan dan bagikan ide](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Masalah Foundry Local**: [Masalah teknis dengan Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontak

- **Pemelihara**: Lihat [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Masalah Keamanan**: Ikuti pengungkapan yang bertanggung jawab di [SECURITY.md](SECURITY.md)
- **Dukungan Microsoft**: Untuk dukungan perusahaan, hubungi layanan pelanggan Microsoft

### Sumber Daya Tambahan

- **Microsoft Learn**: [Jalur Pembelajaran AI dan Machine Learning](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Dokumentasi Foundry Local**: [Dokumentasi Resmi](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Contoh Komunitas**: Lihat [Diskusi GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) untuk kontribusi komunitas

---

**Ini adalah repositori edukasi yang berfokus pada pengajaran pengembangan AI Edge. Pola kontribusi utama adalah meningkatkan konten edukasi dan menambahkan/mengembangkan aplikasi contoh yang menunjukkan konsep AI Edge.**

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.