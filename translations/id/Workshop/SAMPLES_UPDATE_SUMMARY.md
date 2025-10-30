<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T22:39:19+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "id"
}
-->
# Contoh Workshop - Ringkasan Pembaruan Foundry Local SDK

## Ikhtisar

Semua contoh Python di direktori `Workshop/samples` telah diperbarui untuk mengikuti praktik terbaik Foundry Local SDK dan memastikan konsistensi di seluruh workshop.

**Tanggal**: 8 Oktober 2025  
**Lingkup**: 9 file Python di 6 sesi workshop  
**Fokus Utama**: Penanganan error, dokumentasi, pola SDK, pengalaman pengguna

---

## File yang Diperbarui

### Sesi 01: Memulai
- ✅ `chat_bootstrap.py` - Contoh dasar chat dan streaming

### Sesi 02: Solusi RAG
- ✅ `rag_pipeline.py` - Implementasi RAG dengan embeddings
- ✅ `rag_eval_ragas.py` - Evaluasi RAG dengan metrik RAGAS

### Sesi 03: Model Open Source
- ✅ `benchmark_oss_models.py` - Benchmarking multi-model

### Sesi 04: Model Terkini
- ✅ `model_compare.py` - Perbandingan SLM vs LLM

### Sesi 05: Agen Berbasis AI
- ✅ `agents_orchestrator.py` - Koordinasi multi-agen

### Sesi 06: Model sebagai Alat
- ✅ `models_router.py` - Routing model berbasis intent
- ✅ `models_pipeline.py` - Pipeline multi-langkah yang diarahkan

### Infrastruktur Pendukung
- ✅ `workshop_utils.py` - Sudah mengikuti praktik terbaik (tidak ada perubahan yang diperlukan)

---

## Peningkatan Utama

### 1. Penanganan Error yang Ditingkatkan

**Sebelumnya:**
```python
manager, client, model_id = get_client(alias)
```

**Setelah:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Manfaat:**
- Penanganan error yang lebih baik dengan pesan error yang jelas
- Petunjuk pemecahan masalah yang dapat ditindaklanjuti
- Kode keluar yang sesuai untuk scripting

### 2. Manajemen Import yang Lebih Baik

**Sebelumnya:**
```python
from sentence_transformers import SentenceTransformer
```

**Setelah:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Manfaat:**
- Panduan yang jelas saat dependensi hilang
- Mencegah error import yang membingungkan
- Instruksi instalasi yang ramah pengguna

### 3. Dokumentasi Komprehensif

**Ditambahkan ke semua contoh:**
- Dokumentasi variabel lingkungan dalam docstring
- Tautan referensi SDK
- Contoh penggunaan
- Dokumentasi fungsi/parameter yang mendetail
- Petunjuk tipe untuk dukungan IDE yang lebih baik

**Contoh:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Umpan Balik Pengguna yang Ditingkatkan

**Ditambahkan logging informatif:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indikator progres:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Output terstruktur:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Benchmarking yang Kuat

**Peningkatan Sesi 03:**
- Penanganan error per model (melanjutkan saat gagal)
- Pelaporan progres yang mendetail
- Pemanasan dilakukan dengan benar
- Dukungan pengukuran latensi token pertama
- Pemisahan tahap yang jelas

### 6. Petunjuk Tipe yang Konsisten

**Ditambahkan di seluruh:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Manfaat:**
- Autocomplete IDE yang lebih baik
- Deteksi error lebih awal
- Kode yang lebih mudah dipahami

### 7. Router Model yang Ditingkatkan

**Peningkatan Sesi 06:**
- Dokumentasi deteksi intent yang komprehensif
- Penjelasan algoritma pemilihan model
- Log routing yang mendetail
- Format output pengujian
- Pemulihan error dalam pengujian batch

### 8. Orkestrasi Multi-Agen

**Peningkatan Sesi 05:**
- Pelaporan progres tahap demi tahap
- Penanganan error per agen
- Struktur pipeline yang jelas
- Dokumentasi manajemen memori yang lebih baik

---

## Daftar Periksa Pengujian

### Prasyarat
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Uji Setiap Contoh

#### Sesi 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sesi 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sesi 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sesi 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sesi 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sesi 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Referensi Variabel Lingkungan

### Global (Semua Contoh)
| Variabel | Deskripsi | Default |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias model yang digunakan | Bervariasi sesuai contoh |
| `FOUNDRY_LOCAL_ENDPOINT` | Override endpoint layanan | Terdeteksi otomatis |
| `SHOW_USAGE` | Menampilkan penggunaan token | `0` |
| `RETRY_ON_FAIL` | Mengaktifkan logika retry | `1` |
| `RETRY_BACKOFF` | Penundaan retry awal | `1.0` |

### Spesifik Contoh
| Variabel | Digunakan Oleh | Deskripsi |
|----------|---------|-------------|
| `EMBED_MODEL` | Sesi 02 | Nama model embedding |
| `RAG_QUESTION` | Sesi 02 | Pertanyaan uji untuk RAG |
| `BENCH_MODELS` | Sesi 03 | Model yang akan di-benchmark (dipisahkan dengan koma) |
| `BENCH_ROUNDS` | Sesi 03 | Jumlah putaran benchmark |
| `BENCH_PROMPT` | Sesi 03 | Prompt uji untuk benchmark |
| `BENCH_STREAM` | Sesi 03 | Mengukur latensi token pertama |
| `SLM_ALIAS` | Sesi 04 | Model bahasa kecil |
| `LLM_ALIAS` | Sesi 04 | Model bahasa besar |
| `COMPARE_PROMPT` | Sesi 04 | Prompt uji perbandingan |
| `AGENT_MODEL_PRIMARY` | Sesi 05 | Model agen utama |
| `AGENT_MODEL_EDITOR` | Sesi 05 | Model agen editor |
| `AGENT_QUESTION` | Sesi 05 | Pertanyaan uji untuk agen |
| `PIPELINE_TASK` | Sesi 06 | Tugas untuk pipeline |

---

## Perubahan yang Mengganggu

**Tidak Ada** - Semua perubahan kompatibel dengan versi sebelumnya.

Script yang ada akan tetap berfungsi. Fitur baru meliputi:
- Variabel lingkungan opsional
- Pesan error yang ditingkatkan (tidak merusak fungsionalitas)
- Logging tambahan (dapat disembunyikan)
- Petunjuk tipe yang lebih baik (tidak berdampak pada runtime)

---

## Praktik Terbaik yang Diterapkan

### 1. Selalu Gunakan Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Pola Penanganan Error yang Tepat
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Logging Informatif
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Petunjuk Tipe
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstring Komprehensif
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Dukungan Variabel Lingkungan
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Degradasi yang Lancar
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Masalah Umum & Solusi

### Masalah: Error Import
**Solusi:** Instal dependensi yang hilang
```bash
pip install sentence-transformers ragas datasets numpy
```

### Masalah: Error Koneksi
**Solusi:** Pastikan Foundry Local berjalan
```bash
foundry service status
foundry model run phi-4-mini
```

### Masalah: Model Tidak Ditemukan
**Solusi:** Periksa model yang tersedia
```bash
foundry model ls
foundry model download <alias>
```

### Masalah: Performa Lambat
**Solusi:** Gunakan model yang lebih kecil atau sesuaikan parameter
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Langkah Selanjutnya

### 1. Uji Semua Contoh
Ikuti daftar periksa pengujian di atas untuk memastikan semua contoh berfungsi dengan benar.

### 2. Perbarui Dokumentasi
- Perbarui file markdown sesi dengan contoh baru
- Tambahkan bagian pemecahan masalah ke README utama
- Buat panduan referensi cepat

### 3. Buat Pengujian Integrasi
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Tambahkan Benchmark Performa
Lacak peningkatan performa dari peningkatan penanganan error.

### 5. Umpan Balik Pengguna
Kumpulkan umpan balik dari peserta workshop tentang:
- Kejelasan pesan error
- Kelengkapan dokumentasi
- Kemudahan penggunaan

---

## Sumber Daya

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referensi Cepat**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Catatan Migrasi**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Repositori Utama**: https://github.com/microsoft/Foundry-Local

---

## Pemeliharaan

### Menambahkan Contoh Baru
Ikuti pola ini saat membuat contoh baru:

1. Gunakan `workshop_utils` untuk manajemen klien
2. Tambahkan penanganan error yang komprehensif
3. Sertakan dukungan variabel lingkungan
4. Tambahkan petunjuk tipe dan docstring
5. Berikan logging informatif
6. Sertakan contoh penggunaan dalam docstring
7. Tautkan ke dokumentasi SDK

### Meninjau Pembaruan
Saat meninjau pembaruan contoh, periksa:
- [ ] Penanganan error pada semua operasi I/O
- [ ] Petunjuk tipe pada fungsi publik
- [ ] Docstring yang komprehensif
- [ ] Dokumentasi variabel lingkungan
- [ ] Umpan balik pengguna yang informatif
- [ ] Tautan referensi SDK
- [ ] Gaya kode yang konsisten

---

**Ringkasan**: Semua contoh Python Workshop kini mengikuti praktik terbaik Foundry Local SDK dengan penanganan error yang ditingkatkan, dokumentasi komprehensif, dan pengalaman pengguna yang lebih baik. Tidak ada perubahan yang mengganggu - semua fungsi yang ada tetap terjaga dan ditingkatkan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang salah yang timbul dari penggunaan terjemahan ini.