<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T09:45:39+00:00",
  "source_file": "README.md",
  "language_code": "id"
}
-->
# EdgeAI untuk Pemula 


![Gambar sampul kursus](../../translated_images/cover.eb18d1b9605d754b.id.png)

[![Kontributor GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Isu GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Permintaan penggabungan GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Disambut](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Pengamat GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Bintang GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ikuti langkah-langkah berikut untuk memulai menggunakan sumber daya ini:

1. **Fork Repositori**: Klik [![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone Repositori**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Bergabung dengan Azure AI Foundry Discord dan temui para ahli serta pengembang lain**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Dukungan Multi-Bahasa

#### Didukung melalui GitHub Action (Otomatis & Selalu Terbaru)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Cina (Sederhana)](../zh/README.md) | [Cina (Tradisional, Hong Kong)](../hk/README.md) | [Cina (Tradisional, Macau)](../mo/README.md) | [Cina (Tradisional, Taiwan)](../tw/README.md) | [Kroasia](../hr/README.md) | [Ceko](../cs/README.md) | [Denmark](../da/README.md) | [Belanda](../nl/README.md) | [Estonia](../et/README.md) | [Finlandia](../fi/README.md) | [Prancis](../fr/README.md) | [Jerman](../de/README.md) | [Yunani](../el/README.md) | [Ibrani](../he/README.md) | [Hindi](../hi/README.md) | [Hungaria](../hu/README.md) | [Indonesia](./README.md) | [Italia](../it/README.md) | [Jepang](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Lituania](../lt/README.md) | [Melayu](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Pidgin Nigeria](../pcm/README.md) | [Norwegia](../no/README.md) | [Persia (Farsi)](../fa/README.md) | [Polandia](../pl/README.md) | [Portugis (Brasil)](../br/README.md) | [Portugis (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumania](../ro/README.md) | [Rusia](../ru/README.md) | [Serbia (Sirilik)](../sr/README.md) | [Slovakia](../sk/README.md) | [Slovenia](../sl/README.md) | [Spanyol](../es/README.md) | [Swahili](../sw/README.md) | [Swedia](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailand](../th/README.md) | [Turki](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)

> **Lebih suka Clone Lokal?**

> Repositori ini mencakup lebih dari 50 terjemahan bahasa yang secara signifikan meningkatkan ukuran unduhan. Untuk meng-clone tanpa terjemahan, gunakan sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Ini memberikan semua yang Anda butuhkan untuk menyelesaikan kursus dengan unduhan yang jauh lebih cepat.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jika Anda ingin dukungan bahasa terjemahan tambahan, yang didukung tercantum [di sini](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Pendahuluan

Selamat datang di **EdgeAI untuk Pemula** – perjalanan komprehensif Anda ke dalam dunia Transformasi Kecerdasan Buatan Edge. Kursus ini menjembatani kesenjangan antara kemampuan AI yang kuat dan penerapan praktis di dunia nyata pada perangkat edge, memberdayakan Anda memanfaatkan potensi AI langsung di tempat data dihasilkan dan keputusan harus dibuat.

### Apa Yang Akan Anda Kuasai

Kursus ini membawa Anda dari konsep dasar hingga implementasi siap produksi, meliputi:
- **Model Bahasa Kecil (SLM)** yang dioptimalkan untuk penerapan edge
- **Optimasi sadar perangkat keras** di berbagai platform
- **Inferensi waktu nyata** dengan kemampuan pelindung privasi
- **Strategi penerapan produksi** untuk aplikasi perusahaan

### Mengapa EdgeAI Penting

Edge AI mewakili pergeseran paradigma yang menangani tantangan modern penting:
- **Privasi & Keamanan**: Memproses data sensitif secara lokal tanpa paparan cloud
- **Kinerja Waktu Nyata**: Menghilangkan latensi jaringan untuk aplikasi kritis waktu
- **Efisiensi Biaya**: Mengurangi biaya bandwidth dan komputasi cloud
- **Operasi Tangguh**: Mempertahankan fungsi selama gangguan jaringan
- **Kepatuhan Regulasi**: Memenuhi persyaratan kedaulatan data

### Edge AI

Edge AI merujuk pada menjalankan algoritma AI dan model bahasa secara lokal pada perangkat keras, dekat dengan tempat data dihasilkan tanpa bergantung pada sumber daya cloud untuk inferensi. Ini mengurangi latensi, meningkatkan privasi, dan memungkinkan pengambilan keputusan waktu nyata.

### Prinsip Inti:
- **Inferensi di perangkat**: Model AI berjalan pada perangkat edge (telepon, router, mikrokontroler, PC industri)
- **Kemampuan offline**: Berfungsi tanpa konektivitas internet yang persisten
- **Latensi rendah**: Respon segera sesuai untuk sistem waktu nyata
- **Kedaulatan data**: Menjaga data sensitif tetap lokal, meningkatkan keamanan dan kepatuhan

### Model Bahasa Kecil (SLMs)

SLM seperti Phi-4, Mistral-7B, dan Gemma adalah versi optimal dari LLM besar—dilatih atau didistilasi untuk:
- **Jejak memori berkurang**: Penggunaan memori perangkat edge yang terbatas secara efisien
- **Permintaan komputasi rendah**: Dioptimalkan untuk kinerja CPU dan GPU edge
- **Waktu startup lebih cepat**: Inisialisasi cepat untuk aplikasi responsif

Mereka membuka kemampuan NLP yang kuat sekaligus memenuhi keterbatasan:
- **Sistem tertanam**: Perangkat IoT dan pengendali industri
- **Perangkat seluler**: Smartphone dan tablet dengan kemampuan offline
- **Perangkat IoT**: Sensor dan perangkat pintar dengan sumber daya terbatas
- **Server edge**: Unit pemrosesan lokal dengan sumber daya GPU terbatas
- **Komputer pribadi**: Skenario penerapan desktop dan laptop

## Modul Kursus & Navigasi

| Modul | Topik | Area Fokus | Isi Utama | Tingkat | Durasi |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Pendahuluan ke EdgeAI](./introduction.md) | Dasar & Konteks | Ikhtisar EdgeAI • Aplikasi Industri • Pengenalan SLM • Tujuan Pembelajaran | Pemula | 1-2 jam |
| [📚 01](../../Module01) | [Dasar-dasar EdgeAI](./Module01/README.md) | Perbandingan Cloud vs Edge AI | Dasar-dasar EdgeAI • Studi Kasus Dunia Nyata • Panduan Implementasi • Penerapan Edge | Pemula | 3-4 jam |
| [🧠 02](../../Module02) | [Dasar Model SLM](./Module02/README.md) | Keluarga model & arsitektur | Keluarga Phi • Keluarga Qwen • Keluarga Gemma • BitNET • μModel • Phi-Silica | Pemula | 4-5 jam |
| [🚀 03](../../Module03) | [Praktik Penerapan SLM](./Module03/README.md) | Penerapan lokal & cloud | Pembelajaran Lanjutan • Lingkungan Lokal • Penerapan Cloud | Menengah | 4-5 jam |
| [⚙️ 04](../../Module04) | [Toolkit Optimasi Model](./Module04/README.md) | Optimasi lintas platform | Pengenalan • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sintesis Alur Kerja | Menengah | 5-6 jam |
| [🔧 05](../../Module05) | [Produksi SLMOps](./Module05/README.md) | Operasi produksi | Pengenalan SLMOps • Distilasi Model • Fine-tuning • Penerapan Produksi | Lanjutan | 5-6 jam |
| [🤖 06](../../Module06) | [Agen AI & Pemanggilan Fungsi](./Module06/README.md) | Kerangka kerja agen & MCP | Pengenalan Agen • Pemanggilan Fungsi • Protokol Konteks Model | Lanjutan | 4-5 jam |
| [💻 07](../../Module07) | [Implementasi Platform](./Module07/README.md) | Sampel lintas platform | Toolkit AI • Foundry Lokal • Pengembangan Windows | Lanjutan | 3-4 jam |
| [🏭 08](../../Module08) | [Toolkit Foundry Lokal](./Module08/README.md) | Sampel siap produksi | Aplikasi sampel (lihat rincian di bawah) | Ahli | 8-10 jam |

### 🏭 **Modul 08: Aplikasi Sampel**

- [01: Mulai Cepat Chat REST](./Module08/samples/01/README.md)
- [02: Integrasi SDK OpenAI](./Module08/samples/02/README.md)
- [03: Penemuan Model & Benchmarking](./Module08/samples/03/README.md)
- [04: Aplikasi Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orkestrasi Multi-Agen](./Module08/samples/05/README.md)
- [06: Router Models-as-Tools](./Module08/samples/06/README.md)
- [07: Klien API Langsung](./Module08/samples/07/README.md)
- [08: Aplikasi Chat Windows 11](./Module08/samples/08/README.md)
- [09: Sistem Multi-Agen Lanjutan](./Module08/samples/09/README.md)
- [10: Kerangka Kerja Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Workshop: Jalur Pembelajaran Praktik**

Materi workshop praktis komprehensif dengan implementasi siap produksi:

- **[Panduan Workshop](./Workshop/Readme.md)** - Tujuan pembelajaran lengkap, hasil, dan navigasi sumber daya
- **Contoh Python** (6 sesi) - Diperbarui dengan praktik terbaik, penanganan kesalahan, dan dokumentasi lengkap
- **Notebook Jupyter** (8 interaktif) - Tutorial langkah demi langkah dengan benchmark dan pemantauan kinerja
- **Panduan Sesi** - Panduan markdown rinci untuk setiap sesi workshop
- **Alat Validasi** - Skrip untuk memverifikasi kualitas kode dan menjalankan pengujian dasar

**Apa yang Akan Anda Bangun:**
- Aplikasi chat AI lokal dengan dukungan streaming
- Pipeline RAG dengan evaluasi kualitas (RAGAS)
- Alat benchmarking dan perbandingan multi-model
- Sistem orkestrasi multi-agen
- Routing model cerdas dengan seleksi berbasis tugas

### 🎙️ **Workshop Untuk Agentic: Praktik - Studio Podcast AI**

Bangun pipeline produksi podcast bertenaga AI dari nol! Workshop imersif ini mengajarkan Anda membuat sistem multi-agen lengkap yang mengubah ide menjadi episode podcast profesional.
**[🎬 Mulai Workshop Studio Podcast AI](./WorkshopForAgentic/README.md)**

**Misi Anda**: Luncurkan "Future Bytes" — podcast teknologi yang sepenuhnya digerakkan oleh agen AI yang akan Anda bangun sendiri. Tanpa ketergantungan cloud, tanpa biaya API — semuanya berjalan lokal di mesin Anda.

**Apa yang Membuat Ini Unik:**
- **🤖 Orkestrasi Multi-Agen Nyata** - Bangun agen AI khusus yang melakukan riset, menulis, dan memproduksi audio
- **🎯 Jalur Produksi Lengkap** - Dari pemilihan topik hingga output audio podcast akhir
- **💻 Penempatan 100% Lokal** - Menggunakan Ollama dan model lokal (Qwen-3-8B) untuk privasi dan kontrol penuh
- **🎤 Integrasi Text-to-Speech** - Mengubah skrip menjadi percakapan multi-pembicara dengan suara alami
- **✋ Alur Kerja Human-in-the-Loop** - Gerbang persetujuan memastikan kualitas sambil mempertahankan otomatisasi

**Perjalanan Pembelajaran Tiga Babak:**

| Babak | Fokus | Keahlian Utama | Durasi |
|-----|-------|------------|----------|
| **[Babak 1: Kenali Asisten AI Anda](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Bangun agen AI pertama Anda | Integrasi alat • Pencarian web • Pemecahan masalah • Penalaran agen | 2-3 jam |
| **[Babak 2: Rakit Tim Produksi Anda](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestrasi beberapa agen | Koordinasi tim • Alur persetujuan • Antarmuka DevUI • Pengawasan manusia | 3-4 jam |
| **[Babak 3: Hidupkan Podcast Anda](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Hasilkan audio podcast | Text-to-speech • Sintesis multi-pembicara • Audio format panjang • Otomatisasi penuh | 2-3 jam |

**Teknologi yang Digunakan:**
- **Microsoft Agent Framework** - Orkestrasi dan koordinasi multi-agen
- **Ollama** - Runtime model AI lokal (tanpa cloud)
- **Qwen-3-8B** - Model bahasa open-source yang dioptimalkan untuk tugas agen
- **API Text-to-Speech** - Sintesis suara alami untuk pembuatan podcast

**Dukungan Perangkat Keras:**
- ✅ **Mode CPU** - Bekerja di komputer modern mana pun (disarankan RAM 8GB+)
- 🚀 **Akselerasi GPU** - Inferensi jauh lebih cepat dengan GPU NVIDIA/AMD
- ⚡ **Dukungan NPU** - Akselerasi unit proses neural generasi berikutnya

**Sangat Cocok Untuk:**
- Pengembang yang belajar sistem AI multi-agen
- Siapa saja yang tertarik dengan otomatisasi AI dan alur kerja
- Kreator konten yang mengeksplor AI untuk produksi
- Mahasiswa yang mempelajari pola orkestrasi AI praktis

**Mulai Membangun**: [🎙️ Workshop Studio Podcast AI →](./WorkshopForAgentic/README.md)

### 📊 **Ringkasan Jalur Pembelajaran**
- **Durasi Total**: 36-45 jam
- **Jalur Pemula**: Modul 01-02 (7-9 jam)  
- **Jalur Menengah**: Modul 03-04 (9-11 jam)
- **Jalur Lanjutan**: Modul 05-07 (12-15 jam)
- **Jalur Ahli**: Modul 08 (8-10 jam)

## Apa yang Akan Anda Bangun

### 🎯 Kompetensi Inti
- **Arsitektur Edge AI**: Rancang sistem AI lokal-pertama dengan integrasi cloud
- **Optimasi Model**: Kuantisasi dan kompresi model untuk penempatan di edge (peningkatan kecepatan 85%, pengurangan ukuran 75%)
- **Penempatan Multi-Platform**: Windows, mobile, embedded, dan sistem hybrid cloud-edge
- **Operasi Produksi**: Pemantauan, penskalaan, dan pemeliharaan edge AI dalam produksi

### 🏗️ Proyek Praktis
- **Aplikasi Chat Foundry Lokal**: Aplikasi native Windows 11 dengan pengalih model
- **Sistem Multi-Agen**: Koordinator dengan agen spesialis untuk alur kerja kompleks  
- **Aplikasi RAG**: Pemrosesan dokumen lokal dengan pencarian vektor
- **Router Model**: Pemilihan cerdas antar model berdasarkan analisis tugas
- **Framework API**: Klien siap produksi dengan streaming dan pemantauan kesehatan
- **Alat Lintas Platform**: Pola integrasi LangChain/Semantic Kernel

### 🏢 Aplikasi Industri
**Manufaktur** • **Kesehatan** • **Kendaraan Otonom** • **Kota Pintar** • **Aplikasi Mobile**

## Mulai Cepat

**Jalur Pembelajaran yang Disarankan** (total 20-30 jam):

0. **📖 Pengenalan** ([Introduction.md](./introduction.md)): Dasar EdgeAI + konteks industri + kerangka pembelajaran
1. **📚 Fondasi** (Modul 01-02): Konsep EdgeAI + keluarga model SLM
2. **⚙️ Optimasi** (Modul 03-04): Kerangka penempatan + kuantisasi  
3. **🚀 Produksi** (Modul 05-06): SLMOps + agen AI + pemanggilan fungsi
4. **💻 Implementasi** (Modul 07-08): Contoh platform + toolkit Foundry Local

Setiap modul mencakup teori, latihan langsung, dan contoh kode siap produksi.

## Dampak Karir

**Peran Teknis**: Arsitek Solusi EdgeAI • Insinyur ML (Edge) • Pengembang AI IoT • Pengembang AI Mobile

**Sektor Industri**: Manufaktur 4.0 • Teknologi Kesehatan • Sistem Otonom • FinTech • Elektronik Konsumen

**Proyek Portofolio**: Sistem multi-agen • Aplikasi produksi RAG • Penempatan lintas platform • Optimasi performa

## Struktur Repositori

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Sorotan Kursus

✅ **Pembelajaran Progresif**: Teori → Praktik → Penempatan produksi  
✅ **Studi Kasus Nyata**: Microsoft, Japan Airlines, implementasi perusahaan  
✅ **Contoh Praktis**: 50+ contoh, 10 demo Foundry Local komprehensif  
✅ **Fokus Performa**: Peningkatan kecepatan 85%, pengurangan ukuran 75%  
✅ **Multi-Platform**: Windows, mobile, embedded, hybrid cloud-edge  
✅ **Siap Produksi**: Pemantauan, penskalaan, keamanan, kerangka kepatuhan

📖 **[Panduan Studi Tersedia](STUDY_GUIDE.md)**: Jalur pembelajaran terstruktur 20 jam dengan panduan alokasi waktu dan alat penilaian mandiri.

---

**EdgeAI adalah masa depan penempatan AI**: lokal-pertama, menjaga privasi, dan efisien. Kuasai keahlian ini untuk membangun generasi aplikasi cerdas berikutnya.

## Kursus Lain

Tim kami menghasilkan kursus lain! Lihat:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j untuk Pemula](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js untuk Pemula](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agen
[![AZD untuk Pemula](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI untuk Pemula](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP untuk Pemula](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agen AI untuk Pemula](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seri AI Generatif
[![AI Generatif untuk Pemula](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Generatif (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![AI Generatif (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![AI Generatif (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Pembelajaran Inti
[![ML untuk Pemula](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science untuk Pemula](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI untuk Pemula](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Keamanan Siber untuk Pemula](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Pengembangan Web untuk Pemula](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT untuk Pemula](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Pengembangan XR untuk Pemula](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seri Copilot
[![Copilot untuk Pemrograman Berpasangan AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Mendapatkan Bantuan

Jika Anda mengalami kesulitan atau memiliki pertanyaan tentang membangun aplikasi AI, bergabunglah dengan:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jika Anda memiliki masukan produk atau menemukan kesalahan saat membangun, kunjungi:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya mencapai ketepatan, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->