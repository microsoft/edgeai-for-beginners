# EdgeAI untuk Pemula - Workshop

> **Jalur Pembelajaran Praktis untuk Membangun Aplikasi Edge AI Siap Produksi**
>
> Kuasai penerapan AI lokal dengan Microsoft Foundry Local, mulai dari penyelesaian percakapan pertama hingga orkestrasi multi-agen dalam 6 sesi progresif.

---

## 🎯 Pengantar

Selamat datang di **Workshop EdgeAI untuk Pemula** - panduan praktis untuk membangun aplikasi cerdas yang berjalan sepenuhnya di perangkat keras lokal. Workshop ini mengubah konsep teoretis Edge AI menjadi keterampilan dunia nyata melalui latihan yang semakin menantang menggunakan Microsoft Foundry Local dan Small Language Models (SLMs).

### Mengapa Workshop Ini?

**Revolusi Edge AI Telah Dimulai**

Organisasi di seluruh dunia beralih dari AI berbasis cloud ke komputasi edge karena tiga alasan utama:

1. **Privasi & Kepatuhan** - Memproses data sensitif secara lokal tanpa transmisi ke cloud (HIPAA, GDPR, regulasi keuangan)
2. **Performa** - Menghilangkan latensi jaringan (50-500ms lokal vs 500-2000ms perjalanan cloud)
3. **Kontrol Biaya** - Menghapus biaya API per-token dan skalabilitas tanpa biaya cloud

**Namun Edge AI Berbeda**

Menjalankan AI di perangkat lokal membutuhkan keterampilan baru:
- Pemilihan dan optimasi model untuk keterbatasan sumber daya
- Manajemen layanan lokal dan akselerasi perangkat keras
- Teknik prompt untuk model yang lebih kecil
- Pola penerapan produksi untuk perangkat edge

**Workshop Ini Memberikan Keterampilan Tersebut**

Dalam 6 sesi terfokus (~3 jam total), Anda akan berkembang dari "Hello World" hingga menerapkan sistem multi-agen siap produksi - semuanya berjalan secara lokal di mesin Anda.

---

## 📚 Tujuan Pembelajaran

Dengan menyelesaikan workshop ini, Anda akan mampu:

### Kompetensi Inti
1. **Menerapkan dan Mengelola Layanan AI Lokal**
   - Menginstal dan mengonfigurasi Microsoft Foundry Local
   - Memilih model yang sesuai untuk penerapan edge
   - Mengelola siklus hidup model (unduh, muat, cache)
   - Memantau penggunaan sumber daya dan mengoptimalkan performa

2. **Membangun Aplikasi Berbasis AI**
   - Mengimplementasikan penyelesaian percakapan kompatibel OpenAI secara lokal
   - Merancang prompt yang efektif untuk Small Language Models
   - Menangani respons streaming untuk pengalaman pengguna yang lebih baik
   - Mengintegrasikan model lokal ke dalam aplikasi yang ada

3. **Membuat Sistem RAG (Retrieval Augmented Generation)**
   - Membangun pencarian semantik dengan embeddings
   - Mengaitkan respons LLM dengan pengetahuan spesifik domain
   - Mengevaluasi kualitas RAG dengan metrik standar industri
   - Skalabilitas dari prototipe ke produksi

4. **Mengoptimalkan Performa Model**
   - Membandingkan beberapa model untuk kasus penggunaan Anda
   - Mengukur latensi, throughput, dan waktu token pertama
   - Memilih model optimal berdasarkan trade-off kecepatan/kualitas
   - Membandingkan trade-off SLM vs LLM dalam skenario nyata

5. **Mengorkestrasi Sistem Multi-Agen**
   - Merancang agen khusus untuk tugas yang berbeda
   - Mengimplementasikan memori agen dan manajemen konteks
   - Mengoordinasikan agen dalam alur kerja yang kompleks
   - Mengarahkan permintaan secara cerdas di antara beberapa model

6. **Menerapkan Solusi Siap Produksi**
   - Mengimplementasikan penanganan kesalahan dan logika pengulangan
   - Memantau penggunaan token dan sumber daya sistem
   - Membangun arsitektur yang skalabel dengan pola model-as-tools
   - Merencanakan jalur migrasi dari edge ke hybrid (edge + cloud)

---

## 🎓 Hasil Pembelajaran

### Apa yang Akan Anda Bangun

Pada akhir workshop ini, Anda akan membuat:

| Sesi | Hasil | Keterampilan yang Ditunjukkan |
|------|-------|-------------------------------|
| **1** | Aplikasi chat dengan streaming | Pengaturan layanan, penyelesaian dasar, UX streaming |
| **2** | Sistem RAG dengan evaluasi | Embeddings, pencarian semantik, metrik kualitas |
| **3** | Suite benchmark multi-model | Pengukuran performa, perbandingan model |
| **4** | Perbandingan SLM vs LLM | Analisis trade-off, strategi optimasi |
| **5** | Orkestrator multi-agen | Desain agen, manajemen memori, koordinasi |
| **6** | Sistem routing cerdas | Deteksi intent, pemilihan model, skalabilitas |

### Matriks Kompetensi

| Tingkat Keterampilan | Sesi 1-2 | Sesi 3-4 | Sesi 5-6 |
|-----------------------|----------|----------|----------|
| **Pemula** | ✅ Pengaturan & dasar | ⚠️ Menantang | ❌ Terlalu sulit |
| **Menengah** | ✅ Tinjauan cepat | ✅ Pembelajaran inti | ⚠️ Tujuan tambahan |
| **Mahir** | ✅ Mudah | ✅ Penyempurnaan | ✅ Pola produksi |

### Keterampilan Siap Karier

**Setelah workshop ini, Anda akan siap untuk:**

✅ **Membangun Aplikasi Berbasis Privasi**
- Aplikasi kesehatan yang menangani PHI/PII secara lokal
- Layanan keuangan dengan persyaratan kepatuhan
- Sistem pemerintah dengan kebutuhan kedaulatan data

✅ **Optimasi untuk Lingkungan Edge**
- Perangkat IoT dengan sumber daya terbatas
- Aplikasi mobile yang mengutamakan offline
- Sistem real-time dengan latensi rendah

✅ **Merancang Arsitektur Cerdas**
- Sistem multi-agen untuk alur kerja kompleks
- Penerapan hybrid edge-cloud
- Infrastruktur AI yang dioptimalkan biaya

✅ **Memimpin Inisiatif Edge AI**
- Mengevaluasi kelayakan Edge AI untuk proyek
- Memilih model dan kerangka kerja yang sesuai
- Merancang solusi AI lokal yang skalabel

---

## 🗺️ Struktur Workshop

### Ikhtisar Sesi (6 Sesi × 30 Menit = 3 Jam)

| Sesi | Topik | Fokus | Durasi |
|------|-------|-------|--------|
| **1** | Memulai dengan Foundry Local | Instalasi, validasi, penyelesaian pertama | 30 menit |
| **2** | Membangun Solusi AI dengan RAG | Teknik prompt, embeddings, evaluasi | 30 menit |
| **3** | Model Open Source | Penemuan model, benchmarking, seleksi | 30 menit |
| **4** | Model Terkini | SLM vs LLM, optimasi, kerangka kerja | 30 menit |
| **5** | Agen Berbasis AI | Desain agen, orkestrasi, memori | 30 menit |
| **6** | Model sebagai Alat | Routing, chaining, strategi skalabilitas | 30 menit |

---

## 🚀 Memulai dengan Cepat

### Prasyarat

**Persyaratan Sistem:**
- **OS**: Windows 10/11, macOS 11+, atau Linux (Ubuntu 20.04+)
- **RAM**: Minimal 8GB, disarankan 16GB+
- **Penyimpanan**: Ruang kosong 10GB+ untuk model
- **CPU**: Prosesor modern dengan dukungan AVX2
- **GPU** (opsional): Kompatibel dengan CUDA atau Qualcomm NPU untuk akselerasi

**Persyaratan Perangkat Lunak:**
- **Python 3.8+** ([Unduh](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Panduan Instalasi](../../../Workshop))
- **Git** ([Unduh](https://git-scm.com/downloads))
- **Visual Studio Code** (disarankan) ([Unduh](https://code.visualstudio.com/))

### Pengaturan dalam 3 Langkah

#### 1. Instal Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifikasi Instalasi:**
```bash
foundry --version
foundry service status
```

**Pastikan Azure AI Foundry Local berjalan dengan port tetap**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verifikasi Berfungsi:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Menemukan Model yang Tersedia**
Untuk melihat model yang tersedia di instance Foundry Local Anda, Anda dapat melakukan query ke endpoint model:

```bash
# cmd/bash/powershell
foundry model list
```

Menggunakan Endpoint Web 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Clone Repository & Instal Dependensi

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Jalankan Sampel Pertama Anda

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Sukses!** Anda seharusnya melihat respons streaming tentang edge AI.

---

## 📦 Sumber Daya Workshop

### Contoh Python

Contoh praktis progresif yang menunjukkan setiap konsep:

| Sesi | Contoh | Deskripsi | Waktu Jalankan |
|------|--------|-----------|----------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Chat dasar & streaming | ~30 detik |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG dengan embeddings | ~45 detik |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Evaluasi kualitas RAG | ~60 detik |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking multi-model | ~2-3 menit |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Perbandingan SLM vs LLM | ~45 detik |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sistem multi-agen | ~60 detik |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Routing berbasis intent | ~45 detik |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Pipeline multi-langkah | ~60 detik |

### Jupyter Notebooks

Eksplorasi interaktif dengan penjelasan dan visualisasi:

| Sesi | Notebook | Deskripsi | Tingkat Kesulitan |
|------|----------|-----------|-------------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Dasar chat & streaming | ⭐ Pemula |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Membangun sistem RAG | ⭐⭐ Menengah |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluasi kualitas RAG | ⭐⭐ Menengah |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking model | ⭐⭐ Menengah |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Perbandingan model | ⭐⭐ Menengah |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orkestrasi agen | ⭐⭐⭐ Mahir |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Routing intent | ⭐⭐⭐ Mahir |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orkestrasi pipeline | ⭐⭐⭐ Mahir |

### Dokumentasi

Panduan dan referensi lengkap:

| Dokumen | Deskripsi | Kapan Digunakan |
|---------|-----------|-----------------|
| [QUICK_START.md](./QUICK_START.md) | Panduan pengaturan cepat | Memulai dari awal |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Lembar referensi perintah & API | Membutuhkan jawaban cepat |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Pola & contoh SDK | Menulis kode |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Panduan variabel lingkungan | Mengonfigurasi contoh |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Masalah umum & solusinya | Memecahkan masalah |

---

## 🎓 Rekomendasi Jalur Pembelajaran

### Untuk Pemula (3-4 jam)
1. ✅ Sesi 1: Memulai (fokus pada pengaturan dan chat dasar)
2. ✅ Sesi 2: Dasar-dasar RAG (lewati evaluasi awalnya)
3. ✅ Sesi 3: Benchmarking sederhana (hanya 2 model)
4. ⏭️ Lewati Sesi 4-6 untuk sementara
5. 🔄 Kembali ke Sesi 4-6 setelah membangun aplikasi pertama

### Untuk Pengembang Menengah (3 jam)
1. ⚡ Sesi 1: Validasi pengaturan cepat
2. ✅ Sesi 2: Lengkapi pipeline RAG dengan evaluasi
3. ✅ Sesi 3: Suite benchmarking lengkap
4. ✅ Sesi 4: Optimasi model
5. ✅ Sesi 5-6: Fokus pada pola arsitektur

### Untuk Praktisi Mahir (2-3 jam)
1. ⚡ Sesi 1-3: Tinjauan cepat dan validasi
2. ✅ Sesi 4: Pendalaman optimasi
3. ✅ Sesi 5: Arsitektur multi-agen
4. ✅ Sesi 6: Pola produksi dan skalabilitas
5. 🚀 Perluas: Bangun logika routing khusus dan penerapan hybrid

---

## Paket Sesi Workshop (Lab Fokus 30‑Menit)

Jika Anda mengikuti format workshop 6 sesi yang dipadatkan, gunakan panduan khusus ini (masing-masing sesuai dan melengkapi dokumen modul yang lebih luas di atas):

| Sesi Workshop | Panduan | Fokus Inti |
|---------------|---------|------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalasi, validasi, menjalankan phi & GPT-OSS-20B, akselerasi |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Teknik prompt, pola RAG, grounding CSV & dokumen, migrasi |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrasi Hugging Face, benchmarking, seleksi model |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, akselerasi ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Peran agen, memori, alat, orkestrasi |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, chaining, scaling path to Azure |

Setiap file sesi mencakup: abstrak, tujuan pembelajaran, alur demo 30 menit, proyek awal, daftar periksa validasi, pemecahan masalah, dan referensi ke Foundry Local Python SDK resmi.

### Skrip Contoh

Instal dependensi workshop (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Jika menjalankan layanan Foundry Local di mesin atau VM (Windows) yang berbeda dari macOS, ekspor endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sesi | Skrip | Deskripsi |
|------|-------|-----------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap layanan & streaming chat |
| 2 | `samples/session02/rag_pipeline.py` | RAG minimal (embedding dalam memori) |
|   | `samples/session02/rag_eval_ragas.py` | Evaluasi RAG dengan metrik ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmark latensi & throughput multi-model |
| 4 | `samples/session04/model_compare.py` | Perbandingan SLM vs LLM (latensi & output sampel) |
| 5 | `samples/session05/agents_orchestrator.py` | Pipeline penelitian → editorial dengan dua agen |
| 6 | `samples/session06/models_router.py` | Demo routing berbasis intent |
|   | `samples/session06/models_pipeline.py` | Rantai plan/execute/refine multi-langkah |

### Variabel Lingkungan (Umum untuk Semua Contoh)

| Variabel | Tujuan | Contoh |
|----------|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Alias model tunggal default untuk contoh dasar | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM eksplisit vs model lebih besar untuk perbandingan | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Daftar alias model untuk benchmark | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Pengulangan benchmark per model | `3` |
| `BENCH_PROMPT` | Prompt yang digunakan dalam benchmark | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Model embedding sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Override query uji untuk pipeline RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Override query pipeline agen | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias model untuk agen penelitian | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias model untuk agen editor (bisa berbeda) | `gpt-oss-20b` |
| `SHOW_USAGE` | Jika `1`, mencetak penggunaan token per penyelesaian | `1` |
| `RETRY_ON_FAIL` | Jika `1`, mencoba ulang sekali pada kesalahan chat sementara | `1` |
| `RETRY_BACKOFF` | Waktu tunggu sebelum mencoba ulang (detik) | `1.0` |

Jika variabel tidak diatur, skrip akan menggunakan default yang masuk akal. Untuk demo model tunggal, biasanya hanya perlu `FOUNDRY_LOCAL_ALIAS`.

### Modul Utilitas

Semua contoh kini berbagi helper `samples/workshop_utils.py` yang menyediakan:

* Pembuatan klien `FoundryLocalManager` + OpenAI yang di-cache
* Helper `chat_once()` dengan opsi retry + pencetakan penggunaan
* Pelaporan penggunaan token sederhana (aktifkan dengan `SHOW_USAGE=1`)

Ini mengurangi duplikasi dan menyoroti praktik terbaik untuk orkestrasi model lokal yang efisien.

## Peningkatan Opsional (Lintas Sesi)

| Tema | Peningkatan | Sesi | Env / Toggle |
|------|-------------|------|--------------|
| Determinisme | Suhu tetap + set prompt stabil | 1–6 | Atur `temperature=0`, `top_p=1` |
| Visibilitas Penggunaan Token | Pengajaran biaya/efisiensi yang konsisten | 1–6 | `SHOW_USAGE=1` |
| Streaming Token Pertama | Metrik latensi yang dirasakan | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Ketahanan Retry | Menangani cold-start sementara | Semua | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Agen Multi-Model | Spesialisasi peran heterogen | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Routing Adaptif | Intent + heuristik biaya | 6 | Perluas router dengan logika eskalasi |
| Memori Vektor | Recall semantik jangka panjang | 2,5,6 | Integrasi indeks embedding FAISS/Chroma |
| Ekspor Trace | Audit & evaluasi | 2,5,6 | Tambahkan JSON lines per langkah |
| Rubrik Kualitas | Pelacakan kualitatif | 3–6 | Prompt penilaian sekunder |
| Tes Smoke | Validasi pra-workshop cepat | Semua | `python Workshop/tests/smoke.py` |

### Quick Start Deterministik

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Harapkan jumlah token yang stabil di seluruh input identik yang diulang.

### Evaluasi RAG (Sesi 2)

Gunakan `rag_eval_ragas.py` untuk menghitung relevansi jawaban, keakuratan, dan presisi konteks pada dataset sintetis kecil:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Perluas dengan menyediakan JSONL yang lebih besar berisi pertanyaan, konteks, dan kebenaran dasar, lalu konversi ke `Dataset` Hugging Face.

## Lampiran Akurasi Perintah CLI

Workshop sengaja hanya menggunakan perintah CLI Foundry Local yang terdokumentasi / stabil saat ini.

### Perintah Stabil yang Dirujuk

| Kategori | Perintah | Tujuan |
|----------|----------|--------|
| Inti | `foundry --version` | Menampilkan versi yang terinstal |
| Layanan | `foundry service start` | Memulai layanan lokal (jika tidak otomatis) |
| Layanan | `foundry service status` | Menampilkan status layanan |
| Model | `foundry model list` | Daftar katalog / model yang tersedia |
| Model | `foundry model download <alias>` | Mengunduh bobot model ke cache |
| Model | `foundry model run <alias>` | Meluncurkan (memuat) model secara lokal; gabungkan dengan `--prompt` untuk satu kali |
| Model | `foundry model unload <alias>` / `foundry model stop <alias>` | Menghapus model dari memori (jika didukung) |
| Cache | `foundry cache list` | Daftar model yang di-cache (diunduh) |

### Pola Prompt Satu Kali

Alih-alih subperintah `model chat` yang sudah usang, gunakan:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Ini menjalankan satu siklus prompt/respons lalu keluar.

### Pola yang Dihapus / Dihindari

| Usang / Tidak Terdokumentasi | Pengganti / Panduan |
|------------------------------|---------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Gunakan `foundry model list` biasa + aktivitas terbaru / log |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Gunakan skrip benchmark Python + alat OS (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetri

- Latensi, p95, token/detik: `samples/session03/benchmark_oss_models.py`
- Latensi token pertama (streaming): atur `BENCH_STREAM=1`
- Penggunaan sumber daya: monitor OS (Task Manager, Activity Monitor, `nvidia-smi`).

Saat perintah telemetri CLI baru stabil, mereka dapat diintegrasikan dengan sedikit pengeditan pada markdown sesi.

### Lint Guard Otomatis

Lint otomatis mencegah pengenalan kembali pola CLI yang usang di dalam blok kode markdown yang difens.

Skrip: `Workshop/scripts/lint_markdown_cli.py`

Pola usang diblokir di dalam blok kode.

Pengganti yang direkomendasikan:
| Usang | Pengganti |
|-------|-----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Skrip benchmark + alat sistem |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Jalankan secara lokal:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` dijalankan pada setiap push & PR.

Hook pre-commit opsional:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Tabel Migrasi CLI → SDK Cepat

| Tugas | Perintah CLI Satu Baris | Padanan SDK (Python) | Catatan |
|-------|-------------------------|----------------------|---------|
| Menjalankan model sekali (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK secara otomatis memulai layanan & caching |
| Mengunduh (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager memilih varian terbaik jika alias memetakan ke beberapa build |
| Daftar katalog | `foundry model list` | `# gunakan manager untuk setiap alias atau pertahankan daftar yang diketahui` | CLI mengagregasi; SDK saat ini per-alias instantiation |
| Daftar model yang di-cache | `foundry cache list` | `manager.list_cached_models()` | Setelah inisialisasi manager (alias apa pun) |
| Mendapatkan URL endpoint | (implisit) | `manager.endpoint` | Digunakan untuk membuat klien yang kompatibel dengan OpenAI |
| Memanaskan model | `foundry model run <alias>` lalu prompt pertama | `chat_once(alias, messages=[...])` (utilitas) | Utilitas menangani pemanasan latensi awal |
| Mengukur latensi | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (atau skrip ekspor baru) | Lebih baik menggunakan skrip untuk metrik yang konsisten |
| Menghentikan / menghapus model | `foundry model unload <alias>` | (Tidak tersedia – restart layanan / proses) | Biasanya tidak diperlukan untuk alur workshop |
| Mengambil penggunaan token | (lihat output) | `resp.usage.total_tokens` | Disediakan jika backend mengembalikan objek penggunaan |

## Ekspor Markdown Benchmark

Gunakan skrip `Workshop/scripts/export_benchmark_markdown.py` untuk menjalankan benchmark baru (logika yang sama seperti `samples/session03/benchmark_oss_models.py`) dan menghasilkan tabel Markdown yang ramah GitHub plus JSON mentah.

### Contoh

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

File yang dihasilkan:
| File | Isi |
|------|-----|
| `benchmark_report.md` | Tabel Markdown + petunjuk interpretasi |
| `benchmark_report.json` | Array metrik mentah (untuk perbandingan / pelacakan tren) |

Atur `BENCH_STREAM=1` di lingkungan untuk menyertakan latensi token pertama jika didukung.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->