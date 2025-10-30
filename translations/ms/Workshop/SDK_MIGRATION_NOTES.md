<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T22:43:38+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ms"
}
-->
# Nota Migrasi SDK Tempatan Foundry

## Gambaran Keseluruhan

Semua fail Python dalam folder Workshop telah dikemas kini untuk mengikuti corak terkini daripada [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Ringkasan Perubahan

### Infrastruktur Teras (`workshop_utils.py`)

#### Ciri Dipertingkatkan:
- **Sokongan Override Endpoint**: Menambah sokongan untuk pembolehubah persekitaran `FOUNDRY_LOCAL_ENDPOINT`
- **Pengendalian Ralat Dipertingkatkan**: Pengendalian pengecualian yang lebih baik dengan mesej ralat terperinci
- **Caching Dipertingkatkan**: Kunci cache kini termasuk endpoint untuk senario multi-endpoint
- **Exponential Backoff**: Logik ulang cuba kini menggunakan exponential backoff untuk kebolehpercayaan yang lebih baik
- **Anotasi Jenis**: Menambah petunjuk jenis yang komprehensif untuk sokongan IDE yang lebih baik

#### Keupayaan Baru:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Aplikasi Contoh

#### Sesi 01: Chat Bootstrap (`chat_bootstrap.py`)
- Model lalai dikemas kini daripada `phi-3.5-mini` kepada `phi-4-mini`
- Menambah sokongan override endpoint
- Dokumentasi dipertingkatkan dengan rujukan SDK

#### Sesi 02: RAG Pipeline (`rag_pipeline.py`)
- Dikemas kini untuk menggunakan `phi-4-mini` sebagai lalai
- Menambah sokongan override endpoint
- Dokumentasi dipertingkatkan dengan butiran pembolehubah persekitaran

#### Sesi 02: RAG Evaluation (`rag_eval_ragas.py`)
- Lalai model dikemas kini
- Menambah konfigurasi endpoint
- Pengendalian ralat dipertingkatkan

#### Sesi 03: Benchmarking (`benchmark_oss_models.py`)
- Senarai model lalai dikemas kini untuk termasuk `phi-4-mini`
- Dokumentasi pembolehubah persekitaran yang komprehensif ditambah
- Dokumentasi fungsi dipertingkatkan
- Menambah sokongan override endpoint di seluruh

#### Sesi 04: Perbandingan Model (`model_compare.py`)
- LLM lalai dikemas kini daripada `gpt-oss-20b` kepada `qwen2.5-7b`
- Menambah konfigurasi endpoint
- Dokumentasi dipertingkatkan

#### Sesi 05: Orkestrasi Multi-Agent (`agents_orchestrator.py`)
- Menambah petunjuk jenis (menukar `str | None` kepada `Optional[str]`)
- Dokumentasi kelas Agent dipertingkatkan
- Menambah sokongan override endpoint
- Pola inisialisasi dipertingkatkan

#### Sesi 06: Model Router (`models_router.py`)
- Menambah konfigurasi endpoint
- Dokumentasi pengesanan niat dipertingkatkan
- Dokumentasi logik penghalaan dipertingkatkan

#### Sesi 06: Pipeline (`models_pipeline.py`)
- Dokumentasi fungsi yang komprehensif ditambah
- Dokumentasi langkah demi langkah dipertingkatkan
- Pengendalian ralat dipertingkatkan

### Skrip

#### Eksport Benchmark (`export_benchmark_markdown.py`)
- Menambah sokongan override endpoint
- Model lalai dikemas kini
- Dokumentasi fungsi dipertingkatkan
- Pengendalian ralat dipertingkatkan

#### CLI Linter (`lint_markdown_cli.py`)
- Menambah pautan rujukan SDK
- Dokumentasi penggunaan dipertingkatkan

### Ujian

#### Ujian Asap (`smoke.py`)
- Menambah sokongan override endpoint
- Dokumentasi dipertingkatkan
- Dokumentasi kes ujian dipertingkatkan
- Laporan ralat yang lebih baik

## Pembolehubah Persekitaran

Semua contoh kini menyokong pembolehubah persekitaran berikut:

### Konfigurasi Teras
- `FOUNDRY_LOCAL_ALIAS` - Alias model untuk digunakan (lalai berbeza mengikut contoh)
- `FOUNDRY_LOCAL_ENDPOINT` - Override endpoint perkhidmatan (pilihan)
- `SHOW_USAGE` - Paparkan statistik penggunaan token (lalai: "0")
- `RETRY_ON_FAIL` - Aktifkan logik ulang cuba (lalai: "1")
- `RETRY_BACKOFF` - Kelewatan ulang cuba awal dalam saat (lalai: "1.0")

### Khusus Contoh
- `EMBED_MODEL` - Model embedding untuk contoh RAG
- `BENCH_MODELS` - Model yang dipisahkan dengan koma untuk benchmarking
- `BENCH_ROUNDS` - Bilangan pusingan benchmark
- `BENCH_PROMPT` - Prompt ujian untuk benchmark
- `BENCH_STREAM` - Ukur latensi token pertama
- `RAG_QUESTION` - Soalan ujian untuk contoh RAG
- `AGENT_MODEL_PRIMARY` - Model agen utama
- `AGENT_MODEL_EDITOR` - Model agen editor
- `SLM_ALIAS` - Alias model bahasa kecil
- `LLM_ALIAS` - Alias model bahasa besar

## Amalan Terbaik SDK yang Dilaksanakan

### 1. Inisialisasi Klien yang Betul
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

### 2. Pengambilan Maklumat Model
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Pengendalian Ralat
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logik Ulang Cuba dengan Exponential Backoff
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

### 5. Sokongan Penstriman
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

## Panduan Migrasi untuk Contoh Tersuai

Jika anda mencipta contoh baru atau mengemas kini yang sedia ada:

1. **Gunakan pembantu `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Sokong override endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Tambah dokumentasi yang komprehensif**:
   - Pembolehubah persekitaran dalam docstring
   - Pautan rujukan SDK
   - Contoh penggunaan

4. **Gunakan petunjuk jenis**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Laksanakan pengendalian ralat yang betul**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Ujian

Semua contoh boleh diuji dengan:

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

## Rujukan Dokumentasi SDK

- **Repositori Utama**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Dokumentasi API**: Semak repositori SDK untuk dokumentasi API terkini

## Perubahan Besar

### Tiada Dijangka
Semua perubahan adalah serasi ke belakang. Kemas kini ini terutamanya:
- Menambah ciri pilihan baru (override endpoint)
- Meningkatkan pengendalian ralat
- Memperbaiki dokumentasi
- Mengemas kini nama model lalai kepada cadangan semasa

### Peningkatan Pilihan
Anda mungkin ingin mengemas kini kod anda untuk menggunakan:
- `FOUNDRY_LOCAL_ENDPOINT` untuk kawalan endpoint yang eksplisit
- `SHOW_USAGE=1` untuk keterlihatan penggunaan token
- Model lalai yang dikemas kini (`phi-4-mini` dan bukannya `phi-3.5-mini`)

## Isu Biasa & Penyelesaian

### Isu: "Inisialisasi klien gagal"
**Penyelesaian**: Pastikan perkhidmatan Foundry Local sedang berjalan:
```bash
foundry service start
foundry model run phi-4-mini
```

### Isu: "Model tidak ditemui"
**Penyelesaian**: Semak model yang tersedia:
```bash
foundry model list
```

### Isu: Kesalahan sambungan endpoint
**Penyelesaian**: Sahkan endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Langkah Seterusnya

1. **Kemas kini contoh Module08**: Terapkan corak serupa kepada Module08/samples
2. **Tambah ujian integrasi**: Cipta suite ujian yang komprehensif
3. **Benchmarking prestasi**: Bandingkan prestasi sebelum/selepas
4. **Kemas kini dokumentasi**: Kemas kini README utama dengan corak baru

## Garis Panduan Sumbangan

Apabila menambah contoh baru:
1. Gunakan `workshop_utils.py` untuk konsistensi
2. Ikuti corak dalam contoh sedia ada
3. Tambah docstring yang komprehensif
4. Sertakan pautan rujukan SDK
5. Sokong override endpoint
6. Tambah petunjuk jenis yang betul
7. Sertakan contoh penggunaan dalam docstring

## Keserasian Versi

Kemas kini ini serasi dengan:
- `foundry-local-sdk` (terkini)
- `openai>=1.30.0`
- Python 3.8+

---

**Kemas Kini Terakhir**: 2025-01-08  
**Penyelenggara**: Pasukan Bengkel EdgeAI  
**Versi SDK**: Foundry Local SDK (terkini 0.7.117+67073234e7)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.