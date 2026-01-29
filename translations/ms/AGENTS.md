# AGENTS.md

> **Panduan Pembangun untuk Menyumbang kepada EdgeAI untuk Pemula**
> 
> Dokumen ini menyediakan maklumat menyeluruh untuk pembangun, ejen AI, dan penyumbang yang bekerja dengan repositori ini. Ia merangkumi persediaan, aliran kerja pembangunan, ujian, dan amalan terbaik.
> 
> **Kemas Kini Terakhir**: 30 Oktober 2025 | **Versi Dokumen**: 3.0

## Kandungan

- [Gambaran Keseluruhan Projek](../..)
- [Struktur Repositori](../..)
- [Keperluan](../..)
- [Arahan Persediaan](../..)
- [Aliran Kerja Pembangunan](../..)
- [Arahan Ujian](../..)
- [Panduan Gaya Kod](../..)
- [Panduan Permintaan Tarik](../..)
- [Sistem Terjemahan](../..)
- [Integrasi Foundry Local](../..)
- [Pembinaan dan Penghantaran](../..)
- [Isu Umum dan Penyelesaian Masalah](../..)
- [Sumber Tambahan](../..)
- [Nota Khusus Projek](../..)
- [Mendapatkan Bantuan](../..)

## Gambaran Keseluruhan Projek

EdgeAI untuk Pemula adalah repositori pendidikan yang komprehensif yang mengajar pembangunan Edge AI dengan Model Bahasa Kecil (SLM). Kursus ini merangkumi asas EdgeAI, penghantaran model, teknik pengoptimuman, dan pelaksanaan siap produksi menggunakan Microsoft Foundry Local dan pelbagai rangka kerja AI.

**Teknologi Utama:**
- Python 3.8+ (bahasa utama untuk sampel AI/ML)
- .NET C# (Sampel AI/ML)
- JavaScript/Node.js dengan Electron (untuk aplikasi desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Rangka Kerja AI: LangChain, Semantic Kernel, Chainlit
- Pengoptimuman Model: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Jenis Repositori:** Repositori kandungan pendidikan dengan 8 modul dan 10 aplikasi sampel yang komprehensif

**Arkitektur:** Laluan pembelajaran pelbagai modul dengan sampel praktikal yang menunjukkan corak penghantaran Edge AI

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

## Keperluan

### Alat Diperlukan

- **Python 3.8+** - Untuk sampel AI/ML dan buku nota
- **Node.js 16+** - Untuk aplikasi sampel Electron
- **Git** - Untuk kawalan versi
- **Microsoft Foundry Local** - Untuk menjalankan model AI secara tempatan

### Alat Disyorkan

- **Visual Studio Code** - Dengan sambungan Python, Jupyter, dan Pylance
- **Windows Terminal** - Untuk pengalaman baris perintah yang lebih baik (pengguna Windows)
- **Docker** - Untuk pembangunan dalam kontena (pilihan)

### Keperluan Sistem

- **RAM**: Minimum 8GB, disyorkan 16GB+ untuk senario pelbagai model
- **Storan**: Ruang kosong 10GB+ untuk model dan kebergantungan
- **OS**: Windows 10/11, macOS 11+, atau Linux (Ubuntu 20.04+)
- **Perkakasan**: CPU dengan sokongan AVX2; GPU (CUDA, Qualcomm NPU) pilihan tetapi disyorkan

### Pengetahuan Diperlukan

- Pemahaman asas tentang pengaturcaraan Python
- Kefahaman tentang antara muka baris perintah
- Pemahaman konsep AI/ML (untuk pembangunan sampel)
- Aliran kerja Git dan proses permintaan tarik

## Arahan Persediaan

### Persediaan Repositori

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Persediaan Sampel Python (Modul08 dan sampel Bengkel)

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

### Persediaan Sampel Node.js (Sampel 08 - Aplikasi Chat Windows)

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

### Persediaan Foundry Local

Foundry Local diperlukan untuk menjalankan sampel. Muat turun dan pasang dari repositori rasmi:

**Pemasangan:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: Muat turun dari [halaman pelepasan](https://github.com/microsoft/Foundry-Local/releases)

**Permulaan Cepat:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Nota**: Foundry Local secara automatik memilih varian model terbaik untuk perkakasan anda (GPU CUDA, NPU Qualcomm, atau CPU).

## Aliran Kerja Pembangunan

### Pembangunan Kandungan

Repositori ini terutamanya mengandungi **kandungan pendidikan Markdown**. Apabila membuat perubahan:

1. Edit fail `.md` dalam direktori modul yang sesuai
2. Ikuti corak format yang sedia ada
3. Pastikan contoh kod adalah tepat dan telah diuji
4. Kemas kini kandungan terjemahan yang sepadan jika perlu (atau biarkan automasi mengendalikannya)

### Pembangunan Aplikasi Sampel

Untuk sampel Python Modul08 (sampel 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Untuk sampel Python Bengkel:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Untuk sampel Electron (sampel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Ujian Aplikasi Sampel

Sampel Python tidak mempunyai ujian automatik tetapi boleh disahkan dengan menjalankannya:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Sampel Electron mempunyai infrastruktur ujian:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Arahan Ujian

### Pengesahan Kandungan

Repositori menggunakan aliran kerja terjemahan automatik. Tiada ujian manual diperlukan untuk terjemahan.

**Pengesahan manual untuk perubahan kandungan:**
1. Semak rendering Markdown dengan pratonton fail `.md`
2. Pastikan semua pautan menuju ke sasaran yang sah
3. Uji sebarang petikan kod yang disertakan dalam dokumentasi
4. Periksa bahawa imej dimuatkan dengan betul

### Ujian Aplikasi Sampel

**Module08/samples/08 (aplikasi Electron) mempunyai ujian yang komprehensif:**
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

**Sampel Python perlu diuji secara manual:**
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

## Panduan Gaya Kod

### Kandungan Markdown

- Gunakan hierarki tajuk yang konsisten (# untuk tajuk, ## untuk bahagian utama, ### untuk subbahagian)
- Sertakan blok kod dengan penentu bahasa: ```python, ```bash, ```javascript
- Ikuti format sedia ada untuk jadual, senarai, dan penekanan
- Pastikan baris mudah dibaca (sasaran ~80-100 aksara, tetapi tidak ketat)
- Gunakan pautan relatif untuk rujukan dalaman

### Gaya Kod Python

- Ikuti konvensyen PEP 8
- Gunakan petunjuk jenis jika sesuai
- Sertakan docstring untuk fungsi dan kelas
- Gunakan nama pemboleh ubah yang bermakna
- Pastikan fungsi fokus dan ringkas

### Gaya Kod JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Konvensyen Utama:**
- Konfigurasi ESLint disediakan dalam sampel 08
- Prettier untuk format kod
- Gunakan sintaks ES6+ moden
- Ikuti corak sedia ada dalam pangkalan kod

## Panduan Permintaan Tarik

### Aliran Kerja Sumbangan

1. **Fork repositori** dan buat cawangan baru dari `main`
2. **Buat perubahan anda** mengikut panduan gaya kod
3. **Uji dengan teliti** menggunakan arahan ujian di atas
4. **Komit dengan mesej yang jelas** mengikut format komit konvensional
5. **Push ke fork anda** dan buat permintaan tarik
6. **Balas maklum balas** daripada penyelenggara semasa semakan

### Konvensyen Penamaan Cawangan

- `feature/<module>-<description>` - Untuk ciri atau kandungan baru
- `fix/<module>-<description>` - Untuk pembaikan pepijat
- `docs/<description>` - Untuk penambahbaikan dokumentasi
- `refactor/<description>` - Untuk penstrukturan semula kod

### Format Mesej Komit

Ikuti [Komit Konvensional](https://www.conventionalcommits.org/):

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

### Format Tajuk
```
[ModuleXX] Brief description of change
```
atau
```
[Module08/samples/XX] Description for sample changes
```

### Kod Etika

Semua penyumbang mesti mengikuti [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/). Sila semak [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) sebelum menyumbang.

### Sebelum Menghantar

**Untuk perubahan kandungan:**
- Pratonton semua fail Markdown yang diubah
- Pastikan pautan dan imej berfungsi
- Periksa kesalahan ejaan dan tatabahasa

**Untuk perubahan kod sampel (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Untuk perubahan sampel Python:**
- Uji sampel berjalan dengan berjaya
- Pastikan pengendalian ralat berfungsi
- Periksa keserasian dengan Foundry Local

### Proses Semakan

- Perubahan kandungan pendidikan disemak untuk ketepatan dan kejelasan
- Sampel kod diuji untuk fungsi
- Kemas kini terjemahan dikendalikan secara automatik oleh GitHub Actions

## Sistem Terjemahan

**PENTING:** Repositori ini menggunakan terjemahan automatik melalui GitHub Actions.

- Terjemahan berada dalam direktori `/translations/` (50+ bahasa)
- Automatik melalui aliran kerja `co-op-translator.yml`
- **JANGAN edit fail terjemahan secara manual** - ia akan ditulis semula
- Edit hanya fail sumber bahasa Inggeris dalam direktori akar dan modul
- Terjemahan dijana secara automatik apabila push ke cawangan `main`

## Integrasi Foundry Local

Kebanyakan sampel Modul08 memerlukan Microsoft Foundry Local untuk berjalan.

### Pemasangan & Persediaan

**Pasang Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Pasang Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Memulakan Foundry Local
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

### Pengesahan Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Pembolehubah Persekitaran untuk Sampel

Kebanyakan sampel menggunakan pembolehubah persekitaran ini:
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

**Nota**: Apabila menggunakan `FoundryLocalManager`, SDK secara automatik mengendalikan penemuan perkhidmatan dan pemuatan model. Alias model (seperti `phi-3.5-mini`) memastikan varian terbaik dipilih untuk perkakasan anda.

## Pembinaan dan Penghantaran

### Penghantaran Kandungan

Repositori ini terutamanya dokumentasi - tiada proses pembinaan diperlukan untuk kandungan.

### Pembinaan Aplikasi Sampel

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
Tiada proses pembinaan - sampel dijalankan terus dengan interpreter Python.

## Isu Umum dan Penyelesaian Masalah

> **Tip**: Semak [Isu GitHub](https://github.com/microsoft/edgeai-for-beginners/issues) untuk masalah dan penyelesaian yang diketahui.

### Isu Kritikal (Menghalang)

#### Foundry Local Tidak Berjalan
**Isu:** Sampel gagal dengan ralat sambungan

**Penyelesaian:**
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

### Isu Umum (Sederhana)

#### Isu Persekitaran Maya Python
**Isu:** Ralat import modul

**Penyelesaian:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Isu Pembinaan Electron
**Isu:** Kegagalan pemasangan npm atau pembinaan

**Penyelesaian:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Isu Aliran Kerja (Kecil)

#### Konflik Aliran Kerja Terjemahan
**Isu:** PR terjemahan bertentangan dengan perubahan anda

**Penyelesaian:**
- Edit hanya fail sumber bahasa Inggeris
- Biarkan aliran kerja terjemahan automatik mengendalikan terjemahan
- Jika konflik berlaku, gabungkan `main` ke cawangan anda selepas terjemahan digabungkan

#### Kegagalan Muat Turun Model
**Isu:** Foundry Local gagal memuat turun model

**Penyelesaian:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Sumber Tambahan

### Laluan Pembelajaran
- **Laluan Pemula:** Modul 01-02 (7-9 jam)
- **Laluan Pertengahan:** Modul 03-04 (9-11 jam)
- **Laluan Lanjutan:** Modul 05-07 (12-15 jam)
- **Laluan Pakar:** Modul 08 (8-10 jam)
- **Bengkel Praktikal:** Bahan bengkel (6-8 jam)

### Kandungan Modul Utama
- **Modul01:** Asas EdgeAI dan kajian kes dunia sebenar
- **Modul02:** Keluarga dan seni bina Model Bahasa Kecil (SLM)
- **Modul03:** Strategi penghantaran tempatan dan awan
- **Modul04:** Pengoptimuman model dengan pelbagai rangka kerja (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modul05:** SLMOps - operasi pengeluaran
- **Modul06:** Ejen AI dan panggilan fungsi
- **Modul07:** Pelaksanaan khusus platform
- **Modul08:** Alat Foundry Local dengan 10 sampel komprehensif

### Kebergantungan Luaran
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime model AI tempatan dengan API serasi OpenAI
  - [Dokumentasi](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Rangka kerja pengoptimuman
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Alat pengoptimuman model
- [OpenVINO](https://docs.openvino.ai/) - Alat pengoptimuman Intel

## Nota Khusus Projek

### Aplikasi Sampel Modul08

Repositori ini termasuk 10 aplikasi sampel yang komprehensif:

1. **01-REST Chat Quickstart** - Integrasi SDK OpenAI asas
2. **02-Integrasi SDK OpenAI** - Ciri SDK lanjutan
3. **03-Penemuan & Penanda Aras Model** - Alat perbandingan model
4. **04-Aplikasi Chainlit RAG** - Penjanaan yang diperkaya dengan pengambilan
5. **05-Orkestrasi Pelbagai Ejen** - Koordinasi ejen asas
6. **06-Router Alat Model** - Penghalaan model pintar
7. **07-Pelanggan API Langsung** - Integrasi API tahap rendah
8. **08-Aplikasi Chat Windows 11** - Aplikasi desktop Electron asli
9. **09-Sistem Pelbagai Ejen Lanjutan** - Orkestrasi ejen kompleks
10. **10-Alat Rangka Kerja Foundry** - Integrasi LangChain/Semantic Kernel

### Aplikasi Contoh Bengkel

Bengkel ini merangkumi 6 sesi progresif dengan pelaksanaan praktikal:

1. **Sesi 01** - Permulaan chat dengan integrasi Foundry Local
2. **Sesi 02** - Saluran RAG dan penilaian dengan RAGAS
3. **Sesi 03** - Penanda aras model sumber terbuka
4. **Sesi 04** - Perbandingan dan pemilihan model
5. **Sesi 05** - Sistem orkestrasi multi-ejen
6. **Sesi 06** - Penghalaan model dan pengurusan saluran

Setiap contoh menunjukkan aspek berbeza pembangunan AI tepi dengan Foundry Local.

### Pertimbangan Prestasi

- SLM dioptimumkan untuk pelaksanaan tepi (2-16GB RAM)
- Inferens tempatan memberikan masa tindak balas 50-500ms
- Teknik kuantisasi mencapai pengurangan saiz 75% dengan pengekalan prestasi 85%
- Keupayaan perbualan masa nyata dengan model tempatan

### Keselamatan dan Privasi

- Semua pemprosesan berlaku secara tempatan - tiada data dihantar ke awan
- Sesuai untuk aplikasi sensitif privasi (kesihatan, kewangan)
- Memenuhi keperluan kedaulatan data
- Foundry Local beroperasi sepenuhnya pada perkakasan tempatan

## Mendapatkan Bantuan

### Dokumentasi

- **README Utama**: [README.md](README.md) - Gambaran keseluruhan repositori dan laluan pembelajaran
- **Panduan Pembelajaran**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Sumber pembelajaran dan garis masa
- **Sokongan**: [SUPPORT.md](SUPPORT.md) - Cara mendapatkan bantuan
- **Keselamatan**: [SECURITY.md](SECURITY.md) - Melaporkan isu keselamatan

### Sokongan Komuniti

- **Isu GitHub**: [Laporkan pepijat atau minta ciri](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Perbincangan GitHub**: [Ajukan soalan dan kongsi idea](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Isu Foundry Local**: [Isu teknikal dengan Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Hubungi

- **Penyelenggara**: Lihat [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Isu Keselamatan**: Ikuti pendedahan bertanggungjawab dalam [SECURITY.md](SECURITY.md)
- **Sokongan Microsoft**: Untuk sokongan perusahaan, hubungi perkhidmatan pelanggan Microsoft

### Sumber Tambahan

- **Microsoft Learn**: [Laluan Pembelajaran AI dan Pembelajaran Mesin](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Dokumentasi Foundry Local**: [Dokumen Rasmi](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Contoh Komuniti**: Semak [Perbincangan GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) untuk sumbangan komuniti

---

**Ini adalah repositori pendidikan yang fokus pada pengajaran pembangunan AI tepi. Corak sumbangan utama adalah meningkatkan kandungan pendidikan dan menambah/meningkatkan aplikasi contoh yang menunjukkan konsep AI tepi.**

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.