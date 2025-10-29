<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:39:34+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "id"
}
-->
# Catatan Migrasi SDK Lokal Foundry

## Ikhtisar

Semua file Python di folder Workshop telah diperbarui untuk mengikuti pola terbaru dari [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Ringkasan Perubahan

### Infrastruktur Inti (`workshop_utils.py`)

#### Fitur yang Ditingkatkan:
- **Dukungan Override Endpoint**: Menambahkan dukungan variabel lingkungan `FOUNDRY_LOCAL_ENDPOINT`
- **Penanganan Kesalahan yang Lebih Baik**: Penanganan pengecualian yang lebih baik dengan pesan kesalahan yang lebih rinci
- **Caching yang Ditingkatkan**: Kunci cache sekarang mencakup endpoint untuk skenario multi-endpoint
- **Exponential Backoff**: Logika retry sekarang menggunakan exponential backoff untuk meningkatkan keandalan
- **Type Annotations**: Menambahkan petunjuk tipe yang komprehensif untuk mendukung IDE dengan lebih baik

#### Kemampuan Baru:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Aplikasi Contoh

#### Sesi 01: Chat Bootstrap (`chat_bootstrap.py`)
- Model default diperbarui dari `phi-3.5-mini` ke `phi-4-mini`
- Menambahkan dukungan override endpoint
- Dokumentasi ditingkatkan dengan referensi SDK

#### Sesi 02: RAG Pipeline (`rag_pipeline.py`)
- Diperbarui untuk menggunakan `phi-4-mini` sebagai default
- Menambahkan dukungan override endpoint
- Dokumentasi ditingkatkan dengan detail variabel lingkungan

#### Sesi 02: RAG Evaluation (`rag_eval_ragas.py`)
- Model default diperbarui
- Menambahkan konfigurasi endpoint
- Penanganan kesalahan ditingkatkan

#### Sesi 03: Benchmarking (`benchmark_oss_models.py`)
- Daftar model default diperbarui untuk menyertakan `phi-4-mini`
- Dokumentasi variabel lingkungan yang komprehensif ditambahkan
- Dokumentasi fungsi ditingkatkan
- Menambahkan dukungan override endpoint di seluruh bagian

#### Sesi 04: Perbandingan Model (`model_compare.py`)
- LLM default diperbarui dari `gpt-oss-20b` ke `qwen2.5-7b`
- Menambahkan konfigurasi endpoint
- Dokumentasi ditingkatkan

#### Sesi 05: Orkestrasi Multi-Agent (`agents_orchestrator.py`)
- Menambahkan petunjuk tipe (mengubah `str | None` menjadi `Optional[str]`)
- Dokumentasi kelas Agent ditingkatkan
- Menambahkan dukungan override endpoint
- Pola inisialisasi ditingkatkan

#### Sesi 06: Model Router (`models_router.py`)
- Menambahkan konfigurasi endpoint
- Dokumentasi deteksi intent ditingkatkan
- Dokumentasi logika routing ditingkatkan

#### Sesi 06: Pipeline (`models_pipeline.py`)
- Dokumentasi fungsi yang komprehensif ditambahkan
- Dokumentasi langkah demi langkah ditingkatkan
- Penanganan kesalahan ditingkatkan

### Skrip

#### Ekspor Benchmark (`export_benchmark_markdown.py`)
- Menambahkan dukungan override endpoint
- Model default diperbarui
- Dokumentasi fungsi ditingkatkan
- Penanganan kesalahan ditingkatkan

#### CLI Linter (`lint_markdown_cli.py`)
- Menambahkan tautan referensi SDK
- Dokumentasi penggunaan ditingkatkan

### Pengujian

#### Pengujian Smoke (`smoke.py`)
- Menambahkan dukungan override endpoint
- Dokumentasi ditingkatkan
- Dokumentasi kasus pengujian ditingkatkan
- Pelaporan kesalahan yang lebih baik

## Variabel Lingkungan

Semua contoh sekarang mendukung variabel lingkungan berikut:

### Konfigurasi Inti
- `FOUNDRY_LOCAL_ALIAS` - Alias model yang digunakan (default bervariasi berdasarkan contoh)
- `FOUNDRY_LOCAL_ENDPOINT` - Override endpoint layanan (opsional)
- `SHOW_USAGE` - Menampilkan statistik penggunaan token (default: "0")
- `RETRY_ON_FAIL` - Mengaktifkan logika retry (default: "1")
- `RETRY_BACKOFF` - Penundaan awal retry dalam detik (default: "1.0")

### Khusus Contoh
- `EMBED_MODEL` - Model embedding untuk contoh RAG
- `BENCH_MODELS` - Model yang dipisahkan dengan koma untuk benchmarking
- `BENCH_ROUNDS` - Jumlah putaran benchmarking
- `BENCH_PROMPT` - Prompt uji untuk benchmarking
- `BENCH_STREAM` - Mengukur latensi token pertama
- `RAG_QUESTION` - Pertanyaan uji untuk contoh RAG
- `AGENT_MODEL_PRIMARY` - Model agen utama
- `AGENT_MODEL_EDITOR` - Model agen editor
- `SLM_ALIAS` - Alias model bahasa kecil
- `LLM_ALIAS` - Alias model bahasa besar

## Praktik Terbaik SDK yang Diimplementasikan

### 1. Inisialisasi Klien yang Tepat
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Pengambilan Informasi Model
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Penanganan Kesalahan
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logika Retry dengan Exponential Backoff
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Dukungan Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Panduan Migrasi untuk Contoh Kustom

Jika Anda membuat contoh baru atau memperbarui yang sudah ada:

1. **Gunakan helper `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Dukung override endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Tambahkan dokumentasi yang komprehensif**:
   - Variabel lingkungan dalam docstring
   - Tautan referensi SDK
   - Contoh penggunaan

4. **Gunakan petunjuk tipe**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementasikan penanganan kesalahan yang tepat**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Pengujian

Semua contoh dapat diuji dengan:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## Referensi Dokumentasi SDK

- **Repositori Utama**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Dokumentasi API**: Periksa repositori SDK untuk dokumentasi API terbaru

## Perubahan yang Mengganggu

### Tidak Ada yang Diharapkan
Semua perubahan kompatibel dengan versi sebelumnya. Pembaruan ini terutama:
- Menambahkan fitur opsional baru (override endpoint)
- Meningkatkan penanganan kesalahan
- Meningkatkan dokumentasi
- Memperbarui nama model default sesuai rekomendasi terbaru

### Peningkatan Opsional
Anda mungkin ingin memperbarui kode Anda untuk menggunakan:
- `FOUNDRY_LOCAL_ENDPOINT` untuk kontrol endpoint eksplisit
- `SHOW_USAGE=1` untuk visibilitas penggunaan token
- Model default yang diperbarui (`phi-4-mini` alih-alih `phi-3.5-mini`)

## Masalah Umum & Solusi

### Masalah: "Inisialisasi klien gagal"
**Solusi**: Pastikan layanan Foundry Local berjalan:
```bash
foundry service start
foundry model run phi-4-mini
```

### Masalah: "Model tidak ditemukan"
**Solusi**: Periksa model yang tersedia:
```bash
foundry model list
```

### Masalah: Kesalahan koneksi endpoint
**Solusi**: Verifikasi endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Langkah Selanjutnya

1. **Perbarui contoh Module08**: Terapkan pola serupa pada Module08/samples
2. **Tambahkan pengujian integrasi**: Buat suite pengujian yang komprehensif
3. **Benchmarking kinerja**: Bandingkan kinerja sebelum/sesudah
4. **Pembaruan dokumentasi**: Perbarui README utama dengan pola baru

## Panduan Kontribusi

Saat menambahkan contoh baru:
1. Gunakan `workshop_utils.py` untuk konsistensi
2. Ikuti pola dalam contoh yang ada
3. Tambahkan docstring yang komprehensif
4. Sertakan tautan referensi SDK
5. Dukung override endpoint
6. Tambahkan petunjuk tipe yang tepat
7. Sertakan contoh penggunaan dalam docstring

## Kompatibilitas Versi

Pembaruan ini kompatibel dengan:
- `foundry-local-sdk` (terbaru)
- `openai>=1.30.0`
- Python 3.8+

---

**Terakhir Diperbarui**: 2025-01-08  
**Pemelihara**: Tim Workshop EdgeAI  
**Versi SDK**: Foundry Local SDK (terbaru 0.7.117+67073234e7)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.