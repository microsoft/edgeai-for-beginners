# Modul 08: Praktik Langsung dengan Microsoft Foundry Local - Toolkit Pengembang Lengkap

## Ikhtisar

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) adalah generasi terbaru pengembangan AI di edge, memberikan alat yang kuat bagi pengembang untuk membangun, menerapkan, dan meningkatkan aplikasi AI secara lokal sambil tetap terintegrasi dengan Azure AI Foundry. Modul ini mencakup Foundry Local secara menyeluruh, mulai dari instalasi hingga pengembangan agen tingkat lanjut.

**Teknologi Utama:**
- Microsoft Foundry Local CLI dan SDK
- Integrasi Azure AI Foundry
- Inferensi model di perangkat
- Caching dan optimasi model lokal
- Arsitektur berbasis agen

## Tujuan Pembelajaran

Dengan menyelesaikan modul ini, Anda akan:

- **Menguasai Foundry Local**: Instal, konfigurasi, dan optimalkan untuk pengembangan di Windows 11
- **Menerapkan Berbagai Model**: Jalankan model phi, qwen, deepseek, dan GPT secara lokal dengan perintah CLI
- **Membangun Solusi Produksi**: Buat aplikasi AI dengan teknik prompt engineering dan integrasi data tingkat lanjut
- **Memanfaatkan Ekosistem Open-Source**: Integrasikan model Hugging Face dan kontribusi komunitas
- **Mengembangkan Agen AI**: Bangun agen cerdas dengan kemampuan grounding dan orkestrasi
- **Menerapkan Pola Perusahaan**: Ciptakan solusi AI modular dan skalabel untuk penerapan produksi

## Struktur Sesi

### [1: Memulai dengan Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Instalasi, pengaturan CLI, penerapan model, dan optimasi perangkat keras

**Topik Utama**: Instalasi lengkap • Perintah CLI • Caching model • Akselerasi perangkat keras • Penerapan multi-model

**Contoh**: [REST Chat Quickstart](./samples/01/README.md) • [Integrasi OpenAI SDK](./samples/02/README.md) • [Penemuan & Benchmarking Model](./samples/03/README.md)

**Durasi**: 2-3 jam | **Tingkat**: Pemula

---

### [2: Membangun Solusi AI dengan Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Teknik prompt engineering tingkat lanjut, integrasi data, dan konektivitas cloud

**Topik Utama**: Prompt engineering • Integrasi data • Alur kerja Azure • Optimasi kinerja • Pemantauan

**Contoh**: [Aplikasi Chainlit RAG](./samples/04/README.md)

**Durasi**: 2-3 jam | **Tingkat**: Menengah

---

### [3: Model Open-Source di Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Integrasi Hugging Face, strategi BYOM, dan model komunitas

**Topik Utama**: Integrasi HuggingFace • Bring-your-own-model • Wawasan Model Mondays • Kontribusi komunitas • Pemilihan model

**Contoh**: [Orkestrasi Multi-Agen](./samples/05/README.md)

**Durasi**: 2-3 jam | **Tingkat**: Menengah

---

### [4: Jelajahi Model Terkini](./04.CuttingEdgeModels.md)
**Fokus**: LLM vs SLM, implementasi EdgeAI, dan demo tingkat lanjut

**Topik Utama**: Perbandingan model • Inferensi edge vs cloud • Phi + ONNX Runtime • Aplikasi Chainlit RAG • Optimasi WebGPU

**Contoh**: [Router Model-as-Tools](./samples/06/README.md)

**Durasi**: 3-4 jam | **Tingkat**: Lanjutan

---

### [5: Bangun Agen AI dengan Cepat](./05.AIPoweredAgents.md)
**Fokus**: Arsitektur agen, sistem prompt, grounding, dan orkestrasi

**Topik Utama**: Pola desain agen • Teknik prompt sistem • Teknik grounding • Sistem multi-agen • Penerapan produksi

**Contoh**: [Orkestrasi Multi-Agen](./samples/05/README.md) • [Sistem Multi-Agen Tingkat Lanjut](./samples/09/README.md)

**Durasi**: 3-4 jam | **Tingkat**: Lanjutan

---

### [6: Foundry Local - Model sebagai Alat](./06.ModelsAsTools.md)
**Fokus**: Solusi AI modular, skalabilitas perusahaan, dan pola produksi

**Topik Utama**: Model sebagai alat • Penerapan di perangkat • Integrasi SDK/API • Arsitektur perusahaan • Strategi skalabilitas

**Contoh**: [Router Model-as-Tools](./samples/06/README.md) • [Kerangka Alat Foundry](./samples/10/README.md)

**Durasi**: 3-4 jam | **Tingkat**: Ahli

---

### [7: Pola Integrasi API Langsung](./samples/07/README.md)
**Fokus**: Integrasi API REST murni tanpa ketergantungan SDK untuk kontrol maksimal

**Topik Utama**: Implementasi klien HTTP • Autentikasi kustom • Pemantauan kesehatan model • Respon streaming • Penanganan kesalahan produksi

**Contoh**: [Klien API Langsung](./samples/07/README.md)

**Durasi**: 2-3 jam | **Tingkat**: Menengah

---

### [8: Aplikasi Chat Native Windows 11](./samples/08/README.md)
**Fokus**: Membangun aplikasi chat native modern dengan integrasi Foundry Local

**Topik Utama**: Pengembangan Electron • Fluent Design System • Integrasi native Windows • Streaming real-time • Desain antarmuka chat

**Contoh**: [Aplikasi Chat Windows 11](./samples/08/README.md)

**Durasi**: 3-4 jam | **Tingkat**: Lanjutan

---

### [9: Orkestrasi Multi-Agen Tingkat Lanjut](./samples/09/README.md)
**Fokus**: Koordinasi agen yang canggih, delegasi tugas khusus, dan alur kerja AI kolaboratif

**Topik Utama**: Koordinasi agen cerdas • Pola pemanggilan fungsi • Komunikasi antar-agen • Orkestrasi alur kerja • Mekanisme jaminan kualitas

**Contoh**: [Sistem Multi-Agen Tingkat Lanjut](./samples/09/README.md)

**Durasi**: 4-5 jam | **Tingkat**: Ahli

---

### [10: Foundry Local sebagai Kerangka Alat](./samples/10/README.md)
**Fokus**: Arsitektur berbasis alat untuk mengintegrasikan Foundry Local ke dalam aplikasi dan kerangka kerja yang ada

**Topik Utama**: Integrasi LangChain • Fungsi Semantic Kernel • Kerangka kerja API REST • Alat CLI • Integrasi Jupyter • Pola penerapan produksi

**Contoh**: [Kerangka Alat Foundry](./samples/10/README.md)

**Durasi**: 4-5 jam | **Tingkat**: Ahli

## Prasyarat

### Persyaratan Sistem
- **Sistem Operasi**: Windows 11 (22H2 atau lebih baru)
- **Memori**: RAM 16GB (32GB direkomendasikan untuk model yang lebih besar)
- **Penyimpanan**: Ruang kosong 50GB untuk caching model
- **Perangkat Keras**: Perangkat dengan NPU direkomendasikan (Copilot+ PC), GPU opsional
- **Jaringan**: Internet berkecepatan tinggi untuk unduhan model awal

### Lingkungan Pengembangan
- Visual Studio Code dengan ekstensi AI Toolkit
- Python 3.10+ dan pip
- Git untuk kontrol versi
- PowerShell atau Command Prompt
- Azure CLI (opsional untuk integrasi cloud)

### Pengetahuan Prasyarat
- Pemahaman dasar tentang konsep AI/ML
- Familiaritas dengan baris perintah
- Dasar-dasar pemrograman Python
- Konsep API REST
- Pengetahuan dasar tentang prompting dan inferensi model

## Garis Waktu Modul

**Total Waktu Perkiraan**: 30-38 jam

| Sesi | Area Fokus | Contoh | Waktu | Kompleksitas |
|------|------------|--------|-------|--------------|
|  1 | Pengaturan & Dasar | 01, 02, 03 | 2-3 jam | Pemula |
|  2 | Solusi AI | 04 | 2-3 jam | Menengah |
|  3 | Open Source | 05 | 2-3 jam | Menengah |
|  4 | Model Lanjutan | 06 | 3-4 jam | Lanjutan |
|  5 | Agen AI | 05, 09 | 3-4 jam | Lanjutan |
|  6 | Alat Perusahaan | 06, 10 | 3-4 jam | Ahli |
|  7 | Integrasi API Langsung | 07 | 2-3 jam | Menengah |
|  8 | Aplikasi Chat Windows 11 | 08 | 3-4 jam | Lanjutan |
|  9 | Multi-Agen Tingkat Lanjut | 09 | 4-5 jam | Ahli |
| 10 | Kerangka Alat | 10 | 4-5 jam | Ahli |

## Sumber Daya Utama

**Dokumentasi Resmi:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Kode sumber dan contoh resmi
- [Dokumentasi Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Panduan pengaturan dan penggunaan lengkap
- [Seri Model Mondays](https://aka.ms/model-mondays) - Sorotan model mingguan dan tutorial

**Komunitas & Dukungan:**
- [Diskusi Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Tanya jawab komunitas dan permintaan fitur
- [Komunitas Pengembang AI Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence) - Berita terbaru dan praktik terbaik

## Hasil Pembelajaran

Setelah menyelesaikan modul ini, Anda akan mampu:

### Penguasaan Teknis
- **Menerapkan dan Mengelola**: Instalasi Foundry Local di lingkungan pengembangan dan produksi
- **Mengintegrasikan Model**: Bekerja dengan berbagai keluarga model dari Microsoft, Hugging Face, dan sumber komunitas
- **Membangun Aplikasi**: Membuat aplikasi AI siap produksi dengan fitur dan optimasi tingkat lanjut
- **Mengembangkan Agen**: Mengimplementasikan agen AI canggih dengan grounding, penalaran, dan integrasi alat

### Pemahaman Strategis
- **Keputusan Arsitektur**: Membuat pilihan yang tepat antara penerapan lokal vs cloud
- **Optimasi Kinerja**: Mengoptimalkan kinerja inferensi di berbagai konfigurasi perangkat keras
- **Skalabilitas Perusahaan**: Merancang aplikasi yang dapat diskalakan dari prototipe lokal hingga penerapan perusahaan
- **Privasi dan Keamanan**: Mengimplementasikan solusi AI yang menjaga privasi dengan inferensi lokal

### Kemampuan Inovasi
- **Prototipe Cepat**: Dengan cepat membangun dan menguji konsep aplikasi AI di semua 10 pola contoh
- **Integrasi Komunitas**: Memanfaatkan model open-source dan berkontribusi pada ekosistem
- **Pola Lanjutan**: Mengimplementasikan pola AI terkini termasuk RAG, agen, dan integrasi alat
- **Penguasaan Kerangka Kerja**: Integrasi tingkat ahli dengan LangChain, Semantic Kernel, Chainlit, dan Electron
- **Penerapan Produksi**: Menerapkan solusi AI yang skalabel dari prototipe lokal hingga sistem perusahaan
- **Pengembangan Siap Masa Depan**: Membangun aplikasi yang siap untuk teknologi dan pola AI yang sedang berkembang

## Memulai

1. **Pengaturan Lingkungan**: Pastikan Windows 11 dengan perangkat keras yang direkomendasikan (lihat Prasyarat)
2. **Instal Foundry Local**: Ikuti Sesi 1 untuk instalasi dan konfigurasi lengkap
3. **Jalankan Contoh 01**: Mulai dengan integrasi API REST dasar untuk memverifikasi pengaturan
4. **Lanjutkan Melalui Contoh**: Selesaikan contoh 01-10 untuk penguasaan menyeluruh

## Metrik Keberhasilan

Lacak kemajuan Anda melalui semua 10 contoh komprehensif:

### Tingkat Dasar (Contoh 01-03)
- [ ] Berhasil menginstal dan mengonfigurasi Foundry Local
- [ ] Menyelesaikan integrasi API REST (Contoh 01)
- [ ] Mengimplementasikan kompatibilitas OpenAI SDK (Contoh 02)
- [ ] Melakukan penemuan dan benchmarking model (Contoh 03)

### Tingkat Aplikasi (Contoh 04-06)
- [ ] Menerapkan dan menjalankan setidaknya 4 keluarga model berbeda
- [ ] Membangun aplikasi chat RAG yang berfungsi (Contoh 04)
- [ ] Membuat sistem orkestrasi multi-agen (Contoh 05)
- [ ] Mengimplementasikan routing model cerdas (Contoh 06)

### Tingkat Integrasi Lanjutan (Contoh 07-10)
- [ ] Membangun klien API siap produksi (Contoh 07)
- [ ] Mengembangkan aplikasi chat native Windows 11 (Contoh 08)
- [ ] Mengimplementasikan sistem multi-agen tingkat lanjut (Contoh 09)
- [ ] Membuat kerangka alat yang komprehensif (Contoh 10)

### Indikator Penguasaan
- [ ] Berhasil menjalankan semua 10 contoh tanpa kesalahan
- [ ] Menyesuaikan setidaknya 3 contoh untuk kasus penggunaan spesifik
- [ ] Menerapkan 2+ contoh di lingkungan seperti produksi
- [ ] Berkontribusi pada peningkatan atau ekstensi kode contoh
- [ ] Mengintegrasikan pola Foundry Local ke dalam proyek pribadi/profesional

## Panduan Cepat - Semua 10 Contoh

### Pengaturan Lingkungan (Diperlukan untuk Semua Contoh)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Contoh Dasar Inti (01-06)

**Contoh 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Contoh 02: Integrasi OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Contoh 03: Penemuan & Benchmarking Model**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Contoh 04: Aplikasi Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Contoh 05: Orkestrasi Multi-Agen**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Contoh 06: Router Model-as-Tools**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Contoh Integrasi Lanjutan (07-10)

**Contoh 07: Klien API Langsung**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Contoh 08: Aplikasi Chat Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Contoh 09: Sistem Multi-Agen Tingkat Lanjut**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Contoh 10: Kerangka Alat Foundry**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Pemecahan Masalah Umum

**Kesalahan Koneksi Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Masalah Pemuatan Model**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Masalah Ketergantungan**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Ringkasan
Modul ini mewakili teknologi terkini dalam pengembangan AI di edge, menggabungkan alat kelas enterprise dari Microsoft dengan fleksibilitas dan inovasi ekosistem open-source. Dengan menguasai Foundry Local melalui 10 sampel komprehensif, Anda akan berada di garis depan pengembangan aplikasi AI.

**Jalur Pembelajaran Lengkap:**
- **Dasar** (Sampel 01-03): Integrasi API dan manajemen model
- **Aplikasi** (Sampel 04-06): RAG, agen, dan pengaturan rute cerdas
- **Lanjutan** (Sampel 07-10): Kerangka kerja produksi dan integrasi enterprise

Untuk integrasi Azure OpenAI (Sesi 2), lihat file README masing-masing sampel untuk variabel lingkungan yang diperlukan dan pengaturan versi API.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.