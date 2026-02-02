# Buku Catatan Workshop

> **Jupyter Notebook Interaktif untuk Pembelajaran Edge AI Praktis**
>
> Tutorial progresif yang dapat dipelajari secara mandiri, mulai dari penyelesaian obrolan dasar hingga sistem multi-agen tingkat lanjut menggunakan Microsoft Foundry Local dan Small Language Models.

---

## 📖 Pengantar

Selamat datang di koleksi **Workshop EdgeAI untuk Pemula**. Jupyter Notebook interaktif ini memberikan pengalaman belajar langsung di mana Anda akan menulis, menjalankan, dan bereksperimen dengan kode Edge AI secara real-time.

### Mengapa Jupyter Notebook?

Berbeda dengan tutorial tradisional, notebook ini menawarkan:

- **Pembelajaran Interaktif**: Jalankan sel kode dan lihat hasilnya secara langsung
- **Eksperimen**: Ubah parameter dan amati perubahan secara real-time
- **Dokumentasi**: Penjelasan langsung dan sel markdown yang memandu Anda melalui konsep-konsep
- **Reproduksi**: Contoh kerja lengkap yang dapat Anda referensi dan gunakan kembali
- **Visualisasi**: Lihat metrik kinerja, embedding, dan hasil langsung di dalam notebook

### Apa yang Membuat Notebook Ini Istimewa?

Setiap notebook dirancang mengikuti **praktik terbaik siap produksi**:

✅ **Penanganan Kesalahan yang Komprehensif** - Penurunan yang mulus dan pesan kesalahan yang informatif  
✅ **Petunjuk Tipe & Dokumentasi** - Tanda tangan fungsi yang jelas dan docstring  
✅ **Pemantauan Kinerja** - Pelacakan penggunaan token dan pengukuran latensi  
✅ **Desain Modular** - Pola yang dapat digunakan kembali untuk proyek Anda  
✅ **Kompleksitas Progresif** - Membangun sesi sebelumnya secara sistematis  

---

## 🎯 Tujuan Pembelajaran

### Keterampilan Inti yang Akan Anda Kuasai

Dengan menyelesaikan notebook ini, Anda akan menguasai:

1. **Manajemen Layanan AI Lokal**
   - Konfigurasi dan kelola layanan Microsoft Foundry Local
   - Pilih dan muat model yang sesuai untuk perangkat keras Anda
   - Pantau penggunaan sumber daya dan optimalkan kinerja
   - Tangani penemuan layanan dan pemeriksaan kesehatan

2. **Pengembangan Aplikasi AI**
   - Implementasikan penyelesaian obrolan yang kompatibel dengan OpenAI secara lokal
   - Bangun antarmuka streaming untuk pengalaman pengguna yang lebih baik
   - Rancang prompt yang efektif untuk Small Language Models
   - Integrasikan model lokal ke dalam aplikasi

3. **Retrieval Augmented Generation (RAG)**
   - Buat pencarian semantik dengan embedding vektor
   - Dasarkan respons LLM pada dokumen spesifik domain
   - Evaluasi kualitas RAG dengan metrik RAGAS
   - Skalakan dari prototipe ke produksi

4. **Optimasi Kinerja**
   - Benchmark beberapa model secara sistematis
   - Ukur latensi, throughput, dan waktu token pertama
   - Bandingkan Small Language Models vs Large Language Models
   - Pilih model optimal berdasarkan trade-off kinerja/kualitas

5. **Orkestrasi Multi-Agen**
   - Rancang agen khusus untuk tugas yang berbeda
   - Implementasikan memori agen dan manajemen konteks
   - Koordinasikan beberapa agen dalam alur kerja yang kompleks
   - Bangun pola koordinator untuk kolaborasi agen

6. **Routing Model Cerdas**
   - Implementasikan deteksi intent dan pencocokan pola
   - Rute kueri ke model yang sesuai secara otomatis
   - Bangun pipeline multi-langkah (rencana → eksekusi → penyempurnaan)
   - Rancang arsitektur model-as-tools yang skalabel

---

## 🎓 Hasil Pembelajaran

### Apa yang Akan Anda Bangun

| Notebook | Hasil | Keterampilan yang Ditunjukkan | Tingkat Kesulitan |
|----------|-------|------------------------------|-------------------|
| **Sesi 01** | Aplikasi obrolan dengan streaming | Pengaturan layanan, penyelesaian dasar, UX streaming | ⭐ Pemula |
| **Sesi 02 (RAG)** | Pipeline RAG dengan evaluasi | Embedding, pencarian semantik, metrik kualitas | ⭐⭐ Menengah |
| **Sesi 02 (Eval)** | Evaluator kualitas RAG | Metrik RAGAS, evaluasi sistematis | ⭐⭐ Menengah |
| **Sesi 03** | Benchmark multi-model | Pengukuran kinerja, perbandingan model | ⭐⭐ Menengah |
| **Sesi 04** | Perbandingan SLM vs LLM | Analisis trade-off, strategi optimasi | ⭐⭐⭐ Lanjutan |
| **Sesi 05** | Orkestrator multi-agen | Desain agen, memori, koordinasi | ⭐⭐⭐ Lanjutan |
| **Sesi 06 (Router)** | Sistem routing cerdas | Deteksi intent, pemilihan model | ⭐⭐⭐ Lanjutan |
| **Sesi 06 (Pipeline)** | Pipeline multi-langkah | Alur kerja rencana/eksekusi/penyempurnaan | ⭐⭐⭐ Lanjutan |

### Perkembangan Kompetensi

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Jadwal Workshop

### 🚀 Workshop Setengah Hari (3,5 jam)

**Cocok untuk: Sesi pelatihan tim, hackathon, workshop konferensi**

| Waktu | Durasi | Sesi | Topik | Aktivitas |
|-------|--------|------|-------|-----------|
| **0:00** | 30 menit | Pengaturan & Pengantar | Pengaturan lingkungan, instalasi Foundry Local | Instal dependensi, verifikasi pengaturan |
| **0:30** | 30 menit | Sesi 01 | Penyelesaian obrolan dasar, streaming | Jalankan notebook, modifikasi prompt |
| **1:00** | 45 menit | Sesi 02 | Pipeline RAG, embedding, evaluasi | Bangun sistem RAG, uji kueri |
| **1:45** | 15 menit | Istirahat | ☕ Kopi & pertanyaan | — |
| **2:00** | 30 menit | Sesi 03 | Benchmark multi-model | Bandingkan 3+ model |
| **2:30** | 30 menit | Sesi 04 | Trade-off SLM vs LLM | Analisis kinerja/kualitas |
| **3:00** | 30 menit | Sesi 05-06 | Sistem multi-agen & routing | Jelajahi pola lanjutan |

**Hasil**: Peserta meninggalkan workshop dengan 6 aplikasi Edge AI yang berfungsi dan pola kode siap produksi.

---

### 🎓 Workshop Sehari Penuh (6 jam)

**Cocok untuk: Pelatihan mendalam, bootcamp, kursus universitas**

| Waktu | Durasi | Sesi | Topik | Aktivitas |
|-------|--------|------|-------|-----------|
| **0:00** | 45 menit | Pengaturan & Teori | Pengaturan lingkungan, dasar-dasar Edge AI | Instal, verifikasi, diskusikan kasus penggunaan |
| **0:45** | 45 menit | Sesi 01 | Penyelesaian obrolan mendalam | Implementasi obrolan dasar & streaming |
| **1:30** | 30 menit | Istirahat | ☕ Kopi & networking | — |
| **2:00** | 60 menit | Sesi 02 (Keduanya) | Pipeline RAG + evaluasi RAGAS | Bangun sistem RAG lengkap |
| **3:00** | 30 menit | Lab Praktis 1 | RAG khusus untuk domain Anda | Terapkan ke dokumen Anda sendiri |
| **3:30** | 30 menit | Makan Siang | 🍽️ | — |
| **4:00** | 45 menit | Sesi 03 | Metodologi benchmarking | Perbandingan model sistematis |
| **4:45** | 45 menit | Sesi 04 | Strategi optimasi | Analisis SLM vs LLM |
| **5:30** | 60 menit | Sesi 05-06 | Orkestrasi lanjutan | Sistem multi-agen, routing |
| **6:30** | 30 menit | Lab Praktis 2 | Bangun sistem agen khusus | Rancang orkestrator Anda sendiri |

**Hasil**: Pemahaman mendalam tentang pola Edge AI plus 2 proyek khusus.

---

### 📚 Pembelajaran Mandiri (2 minggu)

**Cocok untuk: Pembelajar individu, kursus online, belajar mandiri**

#### Minggu 1: Dasar-Dasar (6 jam)

| Hari | Fokus | Durasi | Notebook | Pekerjaan Rumah |
|------|-------|--------|----------|-----------------|
| **Senin** | Pengaturan & Dasar | 1,5 jam | Sesi 01 | Modifikasi prompt, uji streaming |
| **Rabu** | Dasar-Dasar RAG | 2 jam | Sesi 02 (keduanya) | Tambahkan dokumen Anda sendiri |
| **Jumat** | Benchmarking | 1,5 jam | Sesi 03 | Bandingkan model tambahan |
| **Sabtu** | Tinjauan & Latihan | 1 jam | Semua Minggu 1 | Selesaikan latihan, debug |

#### Minggu 2: Lanjutan (5 jam)

| Hari | Fokus | Durasi | Notebook | Pekerjaan Rumah |
|------|-------|--------|----------|-----------------|
| **Senin** | Optimasi | 1,5 jam | Sesi 04 | Dokumentasikan trade-off |
| **Rabu** | Sistem Multi-Agen | 2 jam | Sesi 05 | Rancang agen khusus |
| **Jumat** | Routing Cerdas | 1,5 jam | Sesi 06 (keduanya) | Bangun logika routing |
| **Sabtu** | Proyek Akhir | 2 jam | Integrasi | Gabungkan beberapa pola |

**Hasil**: Penguasaan pola Edge AI plus proyek portofolio.

---

## 📔 Deskripsi Notebook

### 📘 Sesi 01: Chat Bootstrap
**File**: `session01_chat_bootstrap.ipynb`  
**Durasi**: 20-30 menit  
**Prasyarat**: Tidak ada  
**Tingkat Kesulitan**: ⭐ Pemula

**Apa yang Akan Anda Pelajari**:
- Instal dan konfigurasi Foundry Local Python SDK
- Gunakan `FoundryLocalManager` untuk penemuan layanan otomatis
- Implementasikan penyelesaian obrolan dasar dengan API yang kompatibel dengan OpenAI
- Bangun respons streaming untuk pengalaman pengguna yang lebih baik
- Tangani kesalahan dan ketidaktersediaan layanan dengan baik

**Konsep Utama**: Manajemen layanan, penyelesaian obrolan, streaming, penanganan kesalahan

**Yang Akan Anda Bangun**: Aplikasi obrolan interaktif dengan dukungan streaming

---

### 📗 Sesi 02: Pipeline RAG
**File**: `session02_rag_pipeline.ipynb`  
**Durasi**: 30-45 menit  
**Prasyarat**: Sesi 01  
**Tingkat Kesulitan**: ⭐⭐ Menengah

**Apa yang Akan Anda Pelajari**:
- Implementasikan pola Retrieval Augmented Generation (RAG)
- Buat embedding vektor dengan sentence-transformers
- Bangun pencarian semantik dengan kesamaan kosinus
- Dasarkan respons LLM pada dokumen domain
- Tangani dependensi opsional dengan import guards

**Konsep Utama**: Arsitektur RAG, embedding, pencarian semantik, kesamaan vektor

**Yang Akan Anda Bangun**: Sistem tanya jawab berbasis dokumen

---

### 📗 Sesi 02: Evaluasi RAG dengan RAGAS
**File**: `session02_rag_eval_ragas.ipynb`  
**Durasi**: 30-45 menit  
**Prasyarat**: Pipeline RAG Sesi 02  
**Tingkat Kesulitan**: ⭐⭐ Menengah

**Apa yang Akan Anda Pelajari**:
- Evaluasi kualitas RAG dengan metrik standar industri
- Ukur relevansi konteks, relevansi jawaban, dan keakuratan
- Gunakan kerangka kerja RAGAS untuk evaluasi sistematis
- Identifikasi dan perbaiki masalah kualitas RAG
- Bangun dataset evaluasi untuk domain Anda

**Konsep Utama**: Evaluasi RAG, metrik RAGAS, pengukuran kualitas, pengujian sistematis

**Yang Akan Anda Bangun**: Kerangka evaluasi kualitas RAG

---

### 📙 Sesi 03: Benchmark Model OSS
**File**: `session03_benchmark_oss_models.ipynb`  
**Durasi**: 30-45 menit  
**Prasyarat**: Sesi 01  
**Tingkat Kesulitan**: ⭐⭐ Menengah

**Apa yang Akan Anda Pelajari**:
- Benchmark beberapa model secara sistematis
- Ukur latensi, throughput, waktu token pertama
- Implementasikan penurunan yang mulus untuk kegagalan model
- Bandingkan kinerja antar keluarga model
- Visualisasikan dan analisis hasil benchmark

**Konsep Utama**: Benchmarking kinerja, pengukuran latensi, perbandingan model, analisis statistik

**Yang Akan Anda Bangun**: Suite benchmarking multi-model

---

### 📙 Sesi 04: Perbandingan Model (SLM vs LLM)
**File**: `session04_model_compare.ipynb`  
**Durasi**: 30-45 menit  
**Prasyarat**: Sesi 01, 03  
**Tingkat Kesulitan**: ⭐⭐⭐ Lanjutan

**Apa yang Akan Anda Pelajari**:
- Bandingkan Small Language Models vs Large Language Models
- Analisis trade-off kinerja vs kualitas
- Ukur metrik kesesuaian edge
- Pilih model optimal untuk kendala penerapan
- Dokumentasikan kriteria keputusan untuk pemilihan model

**Konsep Utama**: Pemilihan model, analisis trade-off, strategi optimasi, perencanaan penerapan

**Yang Akan Anda Bangun**: Kerangka perbandingan SLM vs LLM

---

### 📕 Sesi 05: Orkestrator Multi-Agen
**File**: `session05_agents_orchestrator.ipynb`  
**Durasi**: 45-60 menit  
**Prasyarat**: Sesi 01-02  
**Tingkat Kesulitan**: ⭐⭐⭐ Lanjutan

**Apa yang Akan Anda Pelajari**:
- Rancang agen khusus untuk tugas yang berbeda
- Implementasikan memori agen dan manajemen konteks
- Bangun pola koordinator untuk kolaborasi agen
- Tangani komunikasi dan pengalihan antar agen
- Pantau kinerja sistem multi-agen

**Konsep Utama**: Arsitektur agen, pola koordinator, manajemen memori, orkestrasi agen

**Yang Akan Anda Bangun**: Sistem multi-agen dengan koordinator dan spesialis

---

### 📕 Sesi 06: Router Model
**File**: `session06_models_router.ipynb`  
**Durasi**: 30-45 menit  
**Prasyarat**: Sesi 01, 03  
**Tingkat Kesulitan**: ⭐⭐⭐ Lanjutan

**Apa yang Akan Anda Pelajari**:
- Implementasikan deteksi intent dan pencocokan pola
- Bangun routing model berbasis kata kunci
- Rute kueri ke model yang sesuai secara otomatis
- Konfigurasi registri multi-model
- Pantau keputusan routing dan kinerja

**Konsep Utama**: Deteksi intent, routing model, pencocokan pola, pemilihan cerdas

**Yang Akan Anda Bangun**: Sistem routing model cerdas

---

### 📕 Sesi 06: Pipeline Multi-Langkah
**File**: `session06_models_pipeline.ipynb`  
**Durasi**: 30-45 menit  
**Prasyarat**: Sesi 01, Router Sesi 06  
**Tingkat Kesulitan**: ⭐⭐⭐ Lanjutan

**Apa yang Akan Anda Pelajari**:
- Bangun pipeline AI multi-langkah (rencana → eksekusi → penyempurnaan)
- Integrasikan router untuk pemilihan model cerdas
- Implementasikan penanganan kesalahan dan pemulihan pipeline
- Pantau kinerja dan tahap pipeline
- Merancang arsitektur model-as-tools yang skalabel

**Konsep Utama**: Arsitektur pipeline, pemrosesan multi-tahap, pemulihan kesalahan, pola skalabilitas

**Yang Akan Anda Bangun**: Pipeline cerdas multi-langkah dengan routing

---

## 🚀 Memulai

### Prasyarat

**Persyaratan Sistem**:
- **OS**: Windows 10/11, macOS 11+, atau Linux (Ubuntu 20.04+)
- **RAM**: Minimal 8GB, disarankan 16GB+
- **Penyimpanan**: Ruang kosong 10GB+ untuk model
- **Perangkat Keras**: CPU dengan AVX2; GPU (CUDA, Qualcomm NPU) opsional

**Persyaratan Perangkat Lunak**:
- **Python 3.8+** dengan pip
- **Jupyter Notebook** atau **VS Code** dengan ekstensi Jupyter
- **Microsoft Foundry Local** terinstal dan dikonfigurasi
- **Git** (untuk mengkloning repositori)

### Langkah Instalasi

#### 1. Instal Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifikasi Instalasi**:
```bash
foundry --version
```

#### 2. Siapkan Lingkungan Python

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Mulai Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Luncurkan Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Verifikasi Cepat

Jalankan ini di sel Python untuk memverifikasi pengaturan:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Output yang Diharapkan**: Respons sapaan dari model lokal.

---

## 📝 Praktik Terbaik Workshop

### Untuk Instruktur

**Sebelum Workshop**:
- ✅ Kirim instruksi instalasi 1 minggu sebelumnya
- ✅ Uji semua notebook pada perangkat keras target
- ✅ Siapkan panduan pemecahan masalah untuk masalah umum
- ✅ Siapkan model cadangan (phi-3.5-mini jika phi-4-mini gagal)
- ✅ Buat saluran obrolan bersama untuk pertanyaan

**Selama Workshop**:
- ✅ Mulai dengan pemeriksaan lingkungan cepat (5 menit)
- ✅ Bagikan sumber daya pemecahan masalah segera
- ✅ Dorong eksperimen dan modifikasi
- ✅ Gunakan jeda secara strategis (setelah setiap 2 sesi)
- ✅ Sediakan TA untuk bantuan satu-satu

**Setelah Workshop**:
- ✅ Bagikan notebook kerja lengkap dan solusinya
- ✅ Berikan tautan ke sumber daya tambahan
- ✅ Buat survei umpan balik untuk perbaikan
- ✅ Tawarkan jam kantor untuk pertanyaan lanjutan

### Untuk Peserta

**Maksimalkan Pembelajaran Anda**:
- ✅ Selesaikan pengaturan sebelum workshop dimulai
- ✅ Jalankan setiap sel kode sendiri (jangan hanya membaca)
- ✅ Bereksperimen dengan parameter dan prompt
- ✅ Catat wawasan dan hal-hal penting
- ✅ Ajukan pertanyaan saat mengalami kesulitan (kemungkinan orang lain memiliki pertanyaan yang sama)

**Kesalahan Umum yang Harus Dihindari**:
- ❌ Melewatkan urutan eksekusi sel (jalankan secara berurutan)
- ❌ Tidak membaca pesan kesalahan dengan cermat
- ❌ Terburu-buru tanpa memahami
- ❌ Mengabaikan penjelasan markdown
- ❌ Tidak menyimpan notebook yang telah dimodifikasi

**Tips Debugging**:
1. **Layanan Tidak Berjalan**: Periksa `foundry service status`
2. **Kesalahan Impor**: Verifikasi bahwa lingkungan virtual telah diaktifkan
3. **Model Tidak Ditemukan**: Jalankan `foundry model ls` untuk daftar model yang dimuat
4. **Performa Lambat**: Periksa penggunaan RAM, tutup aplikasi lain
5. **Hasil Tidak Terduga**: Restart kernel dan jalankan semua sel dari atas

---

## 🔗 Sumber Daya Tambahan

### Materi Workshop

- **[Panduan Utama Workshop](../Readme.md)** - Ikhtisar, tujuan pembelajaran, hasil karier
- **[Contoh Python](../../../../Workshop/samples)** - Skrip Python yang sesuai untuk setiap sesi
- **[Panduan Sesi](../../../../Workshop)** - Panduan markdown terperinci (Session01-06)
- **[Skrip](../../../../Workshop/scripts)** - Utilitas validasi dan pengujian
- **[Pemecahan Masalah](./TROUBLESHOOTING.md)** - Masalah umum dan solusinya
- **[Panduan Cepat](./quickstart.md)** - Panduan memulai dengan cepat

### Dokumentasi

- **[Dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Dokumentasi resmi Microsoft
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Referensi SDK OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentasi model embedding
- **[Kerangka RAGAS](https://docs.ragas.io/)** - Metode evaluasi RAG

### Komunitas

- **[Diskusi GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Ajukan pertanyaan, bagikan proyek
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Dukungan komunitas real-time
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Tanya jawab teknis

---

## 🎯 Rekomendasi Jalur Pembelajaran

### Jalur Pemula (Mulai di Sini)

1. **Sesi 01** - Chat Bootstrap
2. **Sesi 02** - Pipeline RAG
3. **Sesi 03** - Benchmark Model

**Waktu**: ~2 jam | **Fokus**: Pola dasar

---

### Jalur Menengah

1. Selesaikan Jalur Pemula
2. **Sesi 02** - Evaluasi RAG
3. **Sesi 04** - Perbandingan Model

**Waktu**: ~4 jam | **Fokus**: Kualitas dan optimasi

---

### Jalur Lanjutan (Workshop Lengkap)

1. Selesaikan Jalur Menengah
2. **Sesi 05** - Orkestrator Multi-Agent
3. **Sesi 06** - Router Model
4. **Sesi 06** - Pipeline Multi-Langkah

**Waktu**: ~6 jam | **Fokus**: Pola produksi

---

### Jalur Proyek Kustom

1. Selesaikan Jalur Pemula (Sesi 01-03)
2. Pilih SATU sesi lanjutan berdasarkan tujuan Anda:
   - **Membangun aplikasi RAG?** → Evaluasi Sesi 02
   - **Mengoptimalkan performa?** → Perbandingan Sesi 04
   - **Alur kerja kompleks?** → Orkestrator Sesi 05
   - **Arsitektur skalabel?** → Router + Pipeline Sesi 06

**Waktu**: ~3 jam | **Fokus**: Keterampilan spesifik proyek

---

## 📊 Metrik Keberhasilan

Lacak kemajuan Anda dengan pencapaian berikut:

- [ ] **Pengaturan Selesai** - Foundry Local berjalan, semua dependensi terinstal
- [ ] **Chat Pertama** - Sesi 01 selesai, chat streaming berfungsi
- [ ] **RAG Dibangun** - Sesi 02 selesai, sistem QA dokumen berfungsi
- [ ] **Model Dibandingkan** - Sesi 03 selesai, data performa terkumpul
- [ ] **Analisis Trade-off** - Sesi 04 selesai, kriteria pemilihan model terdokumentasi
- [ ] **Agen Diorkestrasi** - Sesi 05 selesai, sistem multi-agent berfungsi
- [ ] **Routing Diimplementasikan** - Sesi 06 selesai, pemilihan model cerdas berfungsi
- [ ] **Proyek Kustom** - Pola workshop diterapkan pada kasus penggunaan Anda sendiri

---

## 🤝 Kontribusi

Menemukan masalah atau memiliki saran? Kami menyambut kontribusi Anda!

- **Laporkan Masalah**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Usulkan Perbaikan**: [Diskusi GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Kirim PR**: Ikuti [Panduan Kontribusi](../../AGENTS.md)

---

## 📄 Lisensi

Workshop ini adalah bagian dari repositori [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) dan dilisensikan di bawah [Lisensi MIT](../../../../LICENSE).

---

**Siap membangun aplikasi Edge AI yang siap produksi?**  
**Mulai dengan [Sesi 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Terakhir Diperbarui: 8 Oktober 2025 | Versi Workshop: 2.0*

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.