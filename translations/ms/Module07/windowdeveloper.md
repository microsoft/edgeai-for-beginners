# Panduan Pembangunan AI Edge Windows

## Pengenalan

Selamat datang ke Pembangunan AI Edge Windows - panduan lengkap anda untuk membina aplikasi pintar yang memanfaatkan kuasa AI pada peranti menggunakan platform Windows AI Foundry Microsoft. Panduan ini direka khusus untuk pembangun Windows yang ingin mengintegrasikan keupayaan AI Edge terkini ke dalam aplikasi mereka sambil memanfaatkan sepenuhnya pecutan perkakasan Windows.

### Kelebihan AI Windows

Windows AI Foundry mewakili platform yang bersatu, boleh dipercayai, dan selamat yang menyokong keseluruhan kitaran hayat pembangun AI - daripada pemilihan model dan penalaan kepada pengoptimuman dan penyebaran merentasi seni bina CPU, GPU, NPU, dan awan hibrid. Platform ini mendemokrasikan pembangunan AI dengan menyediakan:

- **Abstraksi Perkakasan**: Penyebaran lancar merentasi silikon AMD, Intel, NVIDIA, dan Qualcomm
- **Kecerdasan Pada Peranti**: AI yang melindungi privasi dan berjalan sepenuhnya pada perkakasan tempatan
- **Prestasi Dioptimumkan**: Model yang telah dioptimumkan untuk konfigurasi perkakasan Windows
- **Sedia Untuk Perusahaan**: Ciri keselamatan dan pematuhan gred pengeluaran

### Windows ML 
Windows Machine Learning (ML) membolehkan pembangun C#, C++, dan Python menjalankan model AI ONNX secara tempatan pada PC Windows melalui ONNX Runtime, dengan pengurusan penyedia pelaksanaan automatik untuk perkakasan yang berbeza (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) boleh digunakan dengan model daripada PyTorch, Tensorflow/Keras, TFLite, scikit-learn, dan rangka kerja lain.

![WindowsML Diagram yang menggambarkan model ONNX melalui Windows ML untuk mencapai NPU, GPU, dan CPU.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML menyediakan salinan ONNX Runtime yang dikongsi di seluruh Windows, serta keupayaan untuk memuat turun penyedia pelaksanaan (EP) secara dinamik.

### Mengapa Windows untuk AI Edge?

**Sokongan Perkakasan Universal**
Windows ML menyediakan pengoptimuman perkakasan automatik di seluruh ekosistem Windows, memastikan aplikasi AI anda berprestasi secara optimum tanpa mengira seni bina silikon yang mendasari.

**Runtime AI Terintegrasi**
Enjin inferens Windows ML terbina dalam menghapuskan keperluan persediaan yang kompleks, membolehkan pembangun memberi tumpuan kepada logik aplikasi dan bukannya kebimbangan infrastruktur.

**Pengoptimuman PC Copilot+**
API yang direka khas untuk peranti Windows generasi akan datang dengan Unit Pemprosesan Neural (NPU) khusus yang memberikan prestasi luar biasa setiap watt.

**Ekosistem Pembangun**
Alat yang kaya termasuk integrasi Visual Studio, dokumentasi komprehensif, dan aplikasi sampel yang mempercepatkan kitaran pembangunan.

## Objektif Pembelajaran

Dengan melengkapkan panduan pembangunan AI Edge Windows ini, anda akan menguasai kemahiran penting untuk membina aplikasi AI yang sedia untuk pengeluaran pada platform Windows.

### Kompetensi Teknikal Teras

**Penguasaan Windows AI Foundry**
- Memahami seni bina dan komponen platform Windows AI Foundry
- Menavigasi keseluruhan kitaran hayat pembangunan AI dalam ekosistem Windows
- Melaksanakan amalan terbaik keselamatan untuk aplikasi AI pada peranti
- Mengoptimumkan aplikasi untuk konfigurasi perkakasan Windows yang berbeza

**Kepakaran Integrasi API**
- Menguasai API AI Windows untuk aplikasi teks, visi, dan multimodal
- Melaksanakan integrasi model bahasa Phi Silica untuk penjanaan teks dan penaakulan
- Menyebarkan keupayaan penglihatan komputer menggunakan API pemprosesan imej terbina dalam
- Menyesuaikan model yang telah dilatih menggunakan teknik LoRA (Low-Rank Adaptation)

**Pelaksanaan Tempatan Foundry**
- Melayari, menilai, dan menyebarkan model bahasa sumber terbuka menggunakan CLI Foundry Local
- Memahami pengoptimuman model dan kuantisasi untuk penyebaran tempatan
- Melaksanakan keupayaan AI luar talian yang berfungsi tanpa sambungan internet
- Mengurus kitaran hayat model dan kemas kini dalam persekitaran pengeluaran

**Penyebaran Windows ML**
- Membawa model ONNX tersuai ke aplikasi Windows menggunakan Windows ML
- Memanfaatkan pecutan perkakasan automatik merentasi seni bina CPU, GPU, dan NPU
- Melaksanakan inferens masa nyata dengan penggunaan sumber yang optimum
- Mereka bentuk aplikasi AI yang boleh diskalakan untuk kategori peranti Windows yang pelbagai

### Kemahiran Pembangunan Aplikasi

**Pembangunan Windows Merentas Platform**
- Membina aplikasi berkuasa AI menggunakan .NET MAUI untuk penyebaran Windows universal
- Mengintegrasikan keupayaan AI ke dalam aplikasi Win32, UWP, dan Aplikasi Web Progresif
- Melaksanakan reka bentuk UI responsif yang menyesuaikan diri dengan keadaan pemprosesan AI
- Mengendalikan operasi AI asinkron dengan corak pengalaman pengguna yang betul

**Pengoptimuman Prestasi**
- Profil dan mengoptimumkan prestasi inferens AI merentasi konfigurasi perkakasan yang berbeza
- Melaksanakan pengurusan memori yang cekap untuk model bahasa besar
- Mereka bentuk aplikasi yang merosot dengan anggun berdasarkan keupayaan perkakasan yang tersedia
- Mengaplikasikan strategi caching untuk operasi AI yang sering digunakan

**Kesediaan Pengeluaran**
- Melaksanakan pengendalian ralat yang komprehensif dan mekanisme sandaran
- Mereka bentuk telemetri dan pemantauan untuk prestasi aplikasi AI
- Mengaplikasikan amalan terbaik keselamatan untuk penyimpanan dan pelaksanaan model AI tempatan
- Merancang strategi penyebaran untuk aplikasi perusahaan dan pengguna

### Pemahaman Perniagaan dan Strategik

**Seni Bina Aplikasi AI**
- Mereka bentuk seni bina hibrid yang mengoptimumkan antara pemprosesan AI tempatan dan awan
- Menilai pertukaran antara saiz model, ketepatan, dan kelajuan inferens
- Merancang seni bina aliran data yang mengekalkan privasi sambil membolehkan kecerdasan
- Melaksanakan penyelesaian AI yang kos efektif yang boleh diskalakan dengan permintaan pengguna

**Kedudukan Pasaran**
- Memahami kelebihan kompetitif aplikasi AI asli Windows
- Mengenal pasti kes penggunaan di mana AI pada peranti memberikan pengalaman pengguna yang unggul
- Membangunkan strategi go-to-market untuk aplikasi Windows yang dipertingkatkan AI
- Memposisikan aplikasi untuk memanfaatkan faedah ekosistem Windows

## Sampel SDK Aplikasi Windows AI

SDK Aplikasi Windows menyediakan sampel komprehensif yang menunjukkan integrasi AI merentasi pelbagai rangka kerja dan senario penyebaran. Sampel ini adalah rujukan penting untuk memahami corak pembangunan AI Windows.

### Sampel Windows AI Foundry

| Sampel | Rangka Kerja | Kawasan Fokus | Ciri Utama |
|--------|--------------|---------------|------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integrasi API AI Windows | Aplikasi WinUI lengkap yang menunjukkan API AI Windows, pengoptimuman ARM64, penyebaran yang dibungkus |

**Teknologi Utama:**
- API AI Windows
- Rangka kerja WinUI 3
- Pengoptimuman platform ARM64
- Keserasian PC Copilot+
- Penyebaran aplikasi yang dibungkus

**Prasyarat:**
- Windows 11 dengan PC Copilot+ disyorkan
- Visual Studio 2022
- Konfigurasi binaan ARM64
- SDK Aplikasi Windows 1.8.1+

### Sampel Windows ML

#### Sampel C++

| Sampel | Jenis | Kawasan Fokus | Ciri Utama |
|--------|-------|---------------|------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikasi Konsol | Windows ML Asas | Penemuan EP, pilihan baris arahan, penyusunan model |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikasi Konsol | Penyebaran Rangka Kerja | Runtime yang dikongsi, jejak penyebaran yang lebih kecil |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikasi Konsol | Penyebaran Berdiri Sendiri | Penyebaran mandiri, tiada pergantungan runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Penggunaan Perpustakaan | WindowsML dalam perpustakaan yang dikongsi, pengurusan memori |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Tutorial ResNet | Penukaran model, penyusunan EP, tutorial Build 2025 |

#### Sampel C#

**Aplikasi Konsol**

| Sampel | Jenis | Kawasan Fokus | Ciri Utama |
|--------|-------|---------------|------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Aplikasi Konsol | Integrasi C# Asas | Penggunaan pembantu yang dikongsi, antara muka baris arahan |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Tutorial ResNet | Penukaran model, penyusunan EP, tutorial Build 2025 |

**Aplikasi GUI**

| Sampel | Rangka Kerja | Kawasan Fokus | Ciri Utama |
|--------|--------------|---------------|------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI Desktop | Pengelasan imej dengan antara muka WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI Tradisional | Pengelasan imej dengan Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI Moden | Pengelasan imej dengan antara muka WinUI 3 |

#### Sampel Python

| Sampel | Bahasa | Kawasan Fokus | Ciri Utama |
|--------|--------|---------------|------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Pengelasan Imej | Pengikatan Python WinML, pemprosesan imej secara batch |

### Prasyarat Sampel

**Keperluan Sistem:**
- PC Windows 11 yang menjalankan versi 24H2 (binaan 26100) atau lebih tinggi
- Visual Studio 2022 dengan beban kerja C++ dan .NET
- SDK Aplikasi Windows 1.8.1 atau lebih baru
- Python 3.10-3.13 untuk sampel Python pada peranti x64 dan ARM64

**Spesifik Windows AI Foundry:**
- PC Copilot+ disyorkan untuk prestasi optimum
- Konfigurasi binaan ARM64 untuk sampel AI Windows
- Identiti pakej diperlukan (aplikasi yang tidak dibungkus tidak lagi disokong)

### Aliran Kerja Sampel Biasa

Kebanyakan sampel Windows ML mengikuti corak standard ini:

1. **Inisialisasi Persekitaran** - Cipta persekitaran ONNX Runtime
2. **Daftar Penyedia Pelaksanaan** - Temui dan daftar pecutan perkakasan yang tersedia (CPU, GPU, NPU)
3. **Muatkan Model** - Muatkan model ONNX, secara opsional menyusun untuk perkakasan sasaran
4. **Praproses Input** - Tukarkan imej/data kepada format input model
5. **Jalankan Inferens** - Laksanakan model dan dapatkan ramalan
6. **Proses Hasil** - Terapkan softmax dan paparkan ramalan teratas

### Fail Model Digunakan

| Model | Tujuan | Disertakan | Nota |
|-------|--------|-----------|------|
| SqueezeNet | Pengelasan imej ringan | ✅ Disertakan | Telah dilatih, sedia untuk digunakan |
| ResNet-50 | Pengelasan imej ketepatan tinggi | ❌ Memerlukan penukaran | Gunakan [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) untuk penukaran |

### Sokongan Perkakasan

Semua sampel secara automatik mengesan dan menggunakan perkakasan yang tersedia:
- **CPU** - Sokongan universal di semua peranti Windows
- **GPU** - Pengesanan dan pengoptimuman automatik untuk perkakasan grafik yang tersedia
- **NPU** - Memanfaatkan Unit Pemprosesan Neural pada peranti yang disokong (PC Copilot+)

## Komponen Platform Windows AI Foundry

### 1. API AI Windows

API AI Windows menyediakan keupayaan AI yang sedia digunakan yang dikuasakan oleh model pada peranti, dioptimumkan untuk kecekapan dan prestasi pada peranti PC Copilot+ dengan persediaan minimum yang diperlukan.

#### Kategori API Teras

**Model Bahasa Phi Silica**
- Model bahasa kecil tetapi berkuasa untuk penjanaan teks dan penaakulan
- Dioptimumkan untuk inferens masa nyata dengan penggunaan kuasa minimum
- Sokongan untuk penalaan tersuai menggunakan teknik LoRA
- Integrasi dengan carian semantik Windows dan pengambilan pengetahuan

**API Penglihatan Komputer**
- **Pengecaman Teks (OCR)**: Ekstrak teks daripada imej dengan ketepatan tinggi
- **Resolusi Super Imej**: Tingkatkan imej menggunakan model AI tempatan
- **Segmentasi Imej**: Kenal pasti dan asingkan objek tertentu dalam imej
- **Penerangan Imej**: Hasilkan penerangan teks terperinci untuk kandungan visual
- **Padam Objek**: Buang objek yang tidak diingini daripada imej dengan inpainting berkuasa AI

**Keupayaan Multimodal**
- **Integrasi Visi-Bahasa**: Gabungkan pemahaman teks dan imej
- **Carian Semantik**: Benarkan pertanyaan bahasa semula jadi merentasi kandungan multimedia
- **Pengambilan Pengetahuan**: Bina pengalaman carian pintar dengan data tempatan

### 2. Foundry Local

Foundry Local menyediakan pembangun akses cepat kepada model bahasa sumber terbuka yang sedia digunakan pada Windows Silicon, menawarkan keupayaan untuk melayari, menguji, berinteraksi, dan menyebarkan model dalam aplikasi tempatan.

#### Aplikasi Sampel Foundry Local

Repositori [Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) menyediakan sampel komprehensif merentasi pelbagai bahasa pengaturcaraan dan rangka kerja, menunjukkan pelbagai corak integrasi dan kes penggunaan.

| Sampel | Bahasa/Rangka Kerja | Kawasan Fokus | Ciri Utama |
|--------|----------------------|---------------|------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Pelaksanaan RAG | Integrasi Kernel Semantik, stor vektor Qdrant, embedding JINA, pengambilan dokumen, sembang penstriman |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Aplikasi Sembang Desktop | Sembang merentas platform, penukaran model tempatan/awan, integrasi SDK OpenAI, penstriman masa nyata |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Integrasi Asas | Penggunaan SDK mudah, inisialisasi model, fungsi sembang asas |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Integrasi Asas | Penggunaan SDK Python, respons penstriman, API serasi OpenAI |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integrasi Sistem | Penggunaan SDK peringkat rendah, operasi async, klien HTTP reqwest |

#### Kategori Sampel Berdasarkan Kes Penggunaan

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Pelaksanaan RAG lengkap menggunakan Semantic Kernel, pangkalan data vektor Qdrant, dan JINA embeddings
- **Arkitektur**: Pengambilan dokumen → Pemecahan teks → Embedding vektor → Carian keserupaan → Respons yang peka konteks
- **Teknologi**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, penyelesaian sembang secara streaming

**Aplikasi Desktop**
- **electron/foundry-chat**: Aplikasi sembang sedia untuk pengeluaran dengan penukaran model tempatan/awan
- **Ciri-ciri**: Pemilih model, respons streaming, pengendalian ralat, penyebaran merentas platform
- **Arkitektur**: Proses utama Electron, komunikasi IPC, skrip preload yang selamat

**Contoh Integrasi SDK**
- **JavaScript (Node.js)**: Interaksi model asas dan respons streaming
- **Python**: Penggunaan API serasi OpenAI dengan streaming async
- **Rust**: Integrasi peringkat rendah dengan reqwest dan tokio untuk operasi async

#### Prasyarat untuk Sampel Foundry Local

**Keperluan Sistem:**
- Windows 11 dengan Foundry Local dipasang
- Node.js v16+ untuk sampel JavaScript/Electron
- .NET 8.0+ untuk sampel C#
- Python 3.10+ untuk sampel Python
- Rust 1.70+ untuk sampel Rust

**Pemasangan:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Persediaan Khusus Sampel

**Sampel dotNET RAG:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Sampel Sembang Electron:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**Sampel JavaScript/Python/Rust:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Ciri Utama

**Katalog Model**
- Koleksi menyeluruh model sumber terbuka yang telah dioptimumkan
- Model dioptimumkan merentas CPU, GPU, dan NPU untuk penyebaran segera
- Sokongan untuk keluarga model popular termasuk Llama, Mistral, Phi, dan model khusus domain

**Integrasi CLI**
- Antara muka baris arahan untuk pengurusan dan penyebaran model
- Aliran kerja pengoptimuman dan kuantisasi automatik
- Integrasi dengan persekitaran pembangunan popular dan saluran CI/CD

**Penyebaran Tempatan**
- Operasi luar talian sepenuhnya tanpa pergantungan awan
- Sokongan untuk format dan konfigurasi model tersuai
- Penyajian model yang cekap dengan pengoptimuman perkakasan automatik

### 3. Windows ML

Windows ML berfungsi sebagai platform AI teras dan runtime inferensi bersepadu pada Windows, membolehkan pembangun menyebarkan model tersuai dengan cekap merentas ekosistem perkakasan Windows yang luas.

#### Kelebihan Arkitektur

**Sokongan Perkakasan Universal**
- Pengoptimuman automatik untuk silikon AMD, Intel, NVIDIA, dan Qualcomm
- Sokongan untuk pelaksanaan CPU, GPU, dan NPU dengan penukaran yang telus
- Abstraksi perkakasan yang menghapuskan kerja pengoptimuman khusus platform

**Fleksibiliti Model**
- Sokongan untuk format model ONNX dengan penukaran automatik daripada rangka kerja popular
- Penyebaran model tersuai dengan prestasi gred pengeluaran
- Integrasi dengan arkitektur aplikasi Windows sedia ada

**Integrasi Perusahaan**
- Serasi dengan rangka kerja keselamatan dan pematuhan Windows
- Sokongan untuk alat penyebaran dan pengurusan perusahaan
- Integrasi dengan sistem pengurusan dan pemantauan peranti Windows

## Aliran Kerja Pembangunan

### Fasa 1: Persediaan Persekitaran dan Konfigurasi Alat

**Persediaan Persekitaran Pembangunan**
1. Pasang Visual Studio 2022 dengan beban kerja C++ dan .NET
2. Pasang Windows App SDK 1.8.1 atau lebih baru
3. Konfigurasikan alat CLI Windows AI Foundry
4. Sediakan sambungan AI Toolkit untuk Visual Studio Code
5. Tetapkan alat profil prestasi dan pemantauan
6. Pastikan konfigurasi binaan ARM64 untuk pengoptimuman PC Copilot+

**Persediaan Repositori Sampel**
1. Klon repositori [Windows App SDK Samples](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Navigasi ke `Samples/WindowsAIFoundry/cs-winui` untuk contoh API AI Windows
3. Navigasi ke `Samples/WindowsML` untuk contoh Windows ML yang komprehensif
4. Semak [keperluan binaan](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) untuk platform sasaran anda

**Penerokaan Galeri Pembangunan AI**
- Terokai aplikasi sampel dan pelaksanaan rujukan
- Uji API AI Windows dengan demonstrasi interaktif
- Semak kod sumber untuk amalan terbaik dan corak
- Kenal pasti sampel yang relevan untuk kes penggunaan khusus anda

### Fasa 2: Pemilihan dan Integrasi Model

**Analisis Keperluan**
- Tentukan keperluan fungsional untuk keupayaan AI
- Tetapkan kekangan prestasi dan sasaran pengoptimuman
- Nilai keperluan privasi dan keselamatan
- Rancang seni bina penyebaran dan strategi penskalaan

**Penilaian Model**
- Gunakan Foundry Local untuk menguji model sumber terbuka untuk kes penggunaan anda
- Penanda aras API AI Windows terhadap keperluan model tersuai
- Nilai pertukaran antara saiz model, ketepatan, dan kelajuan inferensi
- Prototip pendekatan integrasi dengan model terpilih

### Fasa 3: Pembangunan Aplikasi

**Integrasi Teras**
- Laksanakan integrasi API AI Windows dengan pengendalian ralat yang betul
- Reka bentuk antara muka pengguna yang menampung aliran kerja pemprosesan AI
- Laksanakan strategi caching dan pengoptimuman untuk inferensi model
- Tambahkan telemetri dan pemantauan untuk prestasi operasi AI

**Ujian dan Pengesahan**
- Uji aplikasi merentas konfigurasi perkakasan Windows yang berbeza
- Sahkan metrik prestasi di bawah pelbagai keadaan beban
- Laksanakan ujian automatik untuk kebolehpercayaan fungsi AI
- Lakukan ujian pengalaman pengguna dengan ciri yang dipertingkatkan AI

### Fasa 4: Pengoptimuman dan Penyebaran

**Pengoptimuman Prestasi**
- Profil prestasi aplikasi merentas konfigurasi perkakasan sasaran
- Optimumkan penggunaan memori dan strategi pemuatan model
- Laksanakan tingkah laku adaptif berdasarkan keupayaan perkakasan yang tersedia
- Haluskan pengalaman pengguna untuk senario prestasi yang berbeza

**Penyebaran Pengeluaran**
- Pek aplikasi dengan kebergantungan model AI yang betul
- Laksanakan mekanisme kemas kini untuk model dan logik aplikasi
- Konfigurasikan pemantauan dan analitik untuk persekitaran pengeluaran
- Rancang strategi pelancaran untuk penyebaran perusahaan dan pengguna

## Contoh Pelaksanaan Praktikal

### Contoh 1: Aplikasi Pemprosesan Dokumen Pintar

Bina aplikasi Windows yang memproses dokumen menggunakan pelbagai keupayaan AI:

**Teknologi Digunakan:**
- Phi Silica untuk penjumlahan dokumen dan menjawab soalan
- API OCR untuk pengekstrakan teks daripada dokumen yang diimbas
- API Penerangan Imej untuk analisis carta dan rajah
- Model ONNX tersuai untuk pengelasan dokumen

**Pendekatan Pelaksanaan:**
- Reka bentuk seni bina modular dengan komponen AI yang boleh dipasang
- Laksanakan pemprosesan async untuk kumpulan dokumen besar
- Tambahkan penunjuk kemajuan dan sokongan pembatalan untuk operasi jangka panjang
- Sertakan keupayaan luar talian untuk pemprosesan dokumen sensitif

### Contoh 2: Sistem Pengurusan Inventori Runcit

Cipta sistem inventori berkuasa AI untuk aplikasi runcit:

**Teknologi Digunakan:**
- Segmentasi Imej untuk pengenalan produk
- Model penglihatan tersuai untuk pengelasan jenama dan kategori
- Penyebaran Foundry Local model bahasa runcit khusus
- Integrasi dengan sistem POS dan inventori sedia ada

**Pendekatan Pelaksanaan:**
- Bina integrasi kamera untuk pengimbasan produk masa nyata
- Laksanakan pengenalan produk kod bar dan visual
- Tambahkan pertanyaan inventori bahasa semula jadi menggunakan model bahasa tempatan
- Reka bentuk seni bina yang boleh diskalakan untuk penyebaran berbilang kedai

### Contoh 3: Pembantu Dokumentasi Penjagaan Kesihatan

Bangunkan alat dokumentasi penjagaan kesihatan yang memelihara privasi:

**Teknologi Digunakan:**
- Phi Silica untuk penjanaan nota perubatan dan sokongan keputusan klinikal
- OCR untuk mendigitalkan rekod perubatan tulisan tangan
- Model bahasa perubatan tersuai yang disebarkan melalui Windows ML
- Penyimpanan vektor tempatan untuk pengambilan pengetahuan perubatan

**Pendekatan Pelaksanaan:**
- Pastikan operasi luar talian sepenuhnya untuk privasi pesakit
- Laksanakan pengesahan dan cadangan terminologi perubatan
- Tambahkan log audit untuk pematuhan peraturan
- Reka bentuk integrasi dengan sistem Rekod Kesihatan Elektronik sedia ada

## Strategi Pengoptimuman Prestasi

### Pembangunan Sedar Perkakasan

**Pengoptimuman NPU**
- Reka bentuk aplikasi untuk memanfaatkan keupayaan NPU pada PC Copilot+
- Laksanakan fallback yang lancar kepada GPU/CPU pada peranti tanpa NPU
- Optimumkan format model untuk pecutan khusus NPU
- Pantau penggunaan NPU dan ciri termal

**Pengurusan Memori**
- Laksanakan strategi pemuatan dan caching model yang cekap
- Gunakan pemetaan memori untuk model besar bagi mengurangkan masa permulaan
- Reka bentuk aplikasi yang sedar memori untuk peranti dengan sumber terhad
- Laksanakan kuantisasi model untuk pengoptimuman memori

**Kecekapan Bateri**
- Optimumkan operasi AI untuk penggunaan kuasa minimum
- Laksanakan pemprosesan adaptif berdasarkan status bateri
- Reka bentuk pemprosesan latar belakang yang cekap untuk operasi AI berterusan
- Gunakan alat profil kuasa untuk mengoptimumkan penggunaan tenaga

### Pertimbangan Skalabiliti

**Multi-Threading**
- Reka bentuk operasi AI yang selamat benang untuk pemprosesan serentak
- Laksanakan pengagihan kerja yang cekap merentas teras yang tersedia
- Gunakan corak async/await untuk operasi AI yang tidak menyekat
- Rancang pengoptimuman kolam benang untuk konfigurasi perkakasan yang berbeza

**Strategi Caching**
- Laksanakan caching pintar untuk operasi AI yang sering digunakan
- Reka bentuk strategi pembatalan cache untuk kemas kini model
- Gunakan caching berterusan untuk operasi prapemprosesan yang mahal
- Laksanakan caching teragih untuk senario berbilang pengguna

## Amalan Terbaik Keselamatan dan Privasi

### Perlindungan Data

**Pemprosesan Tempatan**
- Pastikan data sensitif tidak pernah meninggalkan peranti tempatan
- Laksanakan penyimpanan selamat untuk model AI dan data sementara
- Gunakan ciri keselamatan Windows untuk sandboxing aplikasi
- Terapkan penyulitan untuk model yang disimpan dan hasil pemprosesan sementara

**Keselamatan Model**
- Sahkan integriti model sebelum pemuatan dan pelaksanaan
- Laksanakan mekanisme kemas kini model yang selamat
- Gunakan model yang ditandatangani untuk mencegah gangguan
- Terapkan kawalan akses untuk fail model dan konfigurasi

### Pertimbangan Pematuhan

**Penyelarasan Peraturan**
- Reka bentuk aplikasi untuk memenuhi GDPR, HIPAA, dan keperluan peraturan lain
- Laksanakan log audit untuk proses membuat keputusan AI
- Sediakan ciri ketelusan untuk hasil yang dijana AI
- Benarkan kawalan pengguna ke atas pemprosesan data AI

**Keselamatan Perusahaan**
- Integrasi dengan dasar keselamatan perusahaan Windows
- Sokongan penyebaran terurus melalui alat pengurusan perusahaan
- Laksanakan kawalan akses berdasarkan peranan untuk ciri AI
- Sediakan kawalan pentadbiran untuk fungsi AI

## Penyelesaian Masalah dan Debugging

### Cabaran Pembangunan Biasa

**Isu Konfigurasi Binaan**
- Pastikan konfigurasi platform ARM64 untuk sampel API AI Windows
- Sahkan keserasian versi Windows App SDK (1.8.1+ diperlukan)
- Periksa bahawa identiti pakej dikonfigurasi dengan betul (diperlukan untuk API AI Windows)
- Sahkan bahawa alat binaan menyokong versi rangka kerja sasaran

**Isu Pemuatan Model**
- Sahkan keserasian model ONNX dengan Windows ML
- Periksa integriti fail model dan keperluan format
- Sahkan keperluan keupayaan perkakasan untuk model tertentu
- Debug isu peruntukan memori semasa pemuatan model
- Pastikan pendaftaran penyedia pelaksanaan untuk pecutan perkakasan

**Pertimbangan Mod Penyebaran**
- **Mod Berdiri Sendiri**: Disokong sepenuhnya dengan saiz penyebaran yang lebih besar
- **Mod Bergantung Rangka Kerja**: Jejak lebih kecil tetapi memerlukan runtime yang dikongsi
- **Aplikasi Tidak Dikemas**: Tidak lagi disokong untuk API AI Windows
- Gunakan `dotnet run -p:Platform=ARM64 -p:SelfContained=true` untuk penyebaran ARM64 berdiri sendiri

**Masalah Prestasi**
- Profil prestasi aplikasi merentas konfigurasi perkakasan yang berbeza
- Kenal pasti halangan dalam saluran pemprosesan AI
- Optimumkan operasi prapemprosesan dan pascapemprosesan data
- Laksanakan pemantauan prestasi dan amaran

**Kesukaran Integrasi**
- Debug isu integrasi API dengan pengendalian ralat yang betul
- Sahkan format data input dan keperluan prapemprosesan
- Uji kes tepi dan keadaan ralat dengan teliti
- Laksanakan log yang komprehensif untuk debugging isu pengeluaran

### Alat dan Teknik Debugging

**Integrasi Visual Studio**
- Gunakan debugger AI Toolkit untuk analisis pelaksanaan model
- Laksanakan profil prestasi untuk operasi AI
- Debug operasi AI async dengan pengendalian pengecualian yang betul
- Gunakan alat profil memori untuk pengoptimuman

**Alat Windows AI Foundry**
- Manfaatkan CLI Foundry Local untuk ujian dan pengesahan model
- Gunakan alat ujian API AI Windows untuk pengesahan integrasi
- Laksanakan log tersuai untuk pemantauan operasi AI
- Cipta ujian automatik untuk kebolehpercayaan fungsi AI

## Menyediakan Aplikasi Anda untuk Masa Depan

### Teknologi Baru

**Perkakasan Generasi Seterusnya**
- Reka bentuk aplikasi untuk memanfaatkan keupayaan NPU masa depan
- Rancang untuk saiz dan kerumitan model yang meningkat
- Laksanakan seni bina adaptif untuk perkakasan yang berkembang
- Pertimbangkan algoritma sedia kuantum untuk keserasian masa depan

**Keupayaan AI Lanjutan**
- Bersedia untuk integrasi AI multimodal merentas lebih banyak jenis data
- Rancang untuk AI kolaboratif masa nyata antara pelbagai peranti
- Reka bentuk untuk keupayaan pembelajaran teragih
- Pertimbangkan seni bina kecerdasan hibrid tepi-awan

### Pembelajaran dan Penyesuaian Berterusan

**Kemas Kini Model**
- Laksanakan mekanisme kemas kini model yang lancar
- Reka bentuk aplikasi untuk menyesuaikan diri dengan keupayaan model yang dipertingkatkan
- Rancang untuk keserasian ke belakang dengan model sedia ada
- Laksanakan ujian A/B untuk penilaian prestasi model

**Evolusi Ciri**
- Reka bentuk seni bina modular yang menampung keupayaan AI baharu
- Rancang untuk integrasi API AI Windows yang muncul
- Laksanakan bendera ciri untuk pelancaran keupayaan secara beransur-ansur
- Reka bentuk antara muka pengguna yang menyesuaikan diri dengan ciri AI yang dipertingkatkan

## Kesimpulan

Pembangunan Windows Edge AI mewakili pertemuan keupayaan AI yang kuat dengan platform Windows yang kukuh, selamat, dan boleh diskalakan. Dengan menguasai ekosistem Windows AI Foundry, pembangun boleh mencipta aplikasi pintar yang memberikan pengalaman pengguna yang luar biasa sambil mengekalkan piawaian tertinggi privasi, keselamatan, dan prestasi.

Gabungan API AI Windows, Foundry Local, dan Windows ML menyediakan asas yang tiada tandingan untuk membina generasi seterusnya aplikasi Windows pintar. Apabila AI terus berkembang, platform Windows memastikan aplikasi anda akan berkembang dengan teknologi yang muncul sambil mengekalkan keserasian dan prestasi merentas ekosistem perkakasan Windows yang pelbagai.

Sama ada anda membina aplikasi pengguna, penyelesaian perusahaan, atau alat industri khusus, pembangunan Windows Edge AI memberi kuasa kepada anda untuk mencipta pengalaman yang pintar, responsif, dan sangat terintegrasi yang memanfaatkan sepenuhnya potensi peranti Windows moden.

## Sumber Tambahan

### Dokumentasi dan Pembelajaran
- [Dokumentasi Windows AI Foundry](https://learn.microsoft.com/windows/ai/)
- [Rujukan API AI Windows](https://learn.microsoft.com/windows/ai/apis/)
- [Mulakan membina aplikasi dengan API AI Windows](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local Getting Started](https://learn.microsoft.com
- [Gambaran Keseluruhan Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Keperluan Sistem Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Persediaan Persekitaran Pembangunan Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Repositori Contoh dan Kod
- [Contoh Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Contoh Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Contoh Inferens ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Repositori Contoh Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Alat Pembangunan
- [Toolkit AI untuk Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galeri Pembangunan AI](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Contoh Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Alat Penukaran Model](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Sokongan Teknikal
- [Dokumentasi Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentasi ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentasi Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Laporkan Isu - Contoh Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Komuniti dan Sokongan
- [Komuniti Pembangun Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Latihan AI Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Panduan ini direka untuk berkembang seiring dengan ekosistem Windows AI yang pesat maju. Kemas kini secara berkala memastikan keselarasan dengan keupayaan platform terkini dan amalan terbaik pembangunan.*

[08. Praktikal Dengan Microsoft Foundry Local - Toolkit Pembangun Lengkap](../Module08/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.