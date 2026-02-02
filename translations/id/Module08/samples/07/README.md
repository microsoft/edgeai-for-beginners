# Contoh Foundry Local sebagai API

Contoh ini menunjukkan cara menggunakan Microsoft Foundry Local sebagai layanan REST API tanpa bergantung pada OpenAI SDK. Ini memperlihatkan pola integrasi HTTP langsung untuk kontrol dan kustomisasi maksimal.

## Gambaran Umum

Berdasarkan pola resmi Microsoft Foundry Local, contoh ini menyediakan:
- Integrasi REST API langsung dengan FoundryLocalManager
- Implementasi klien HTTP kustom
- Pengelolaan model dan pemantauan kesehatan
- Penanganan respons streaming dan non-streaming
- Penanganan kesalahan dan logika retry yang siap produksi

## Prasyarat

1. **Instalasi Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Dependensi Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Arsitektur

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Fitur Utama

### 1. **Integrasi HTTP Langsung**
- Panggilan REST API murni tanpa ketergantungan SDK
- Autentikasi dan header kustom
- Kontrol penuh atas penanganan permintaan/respons

### 2. **Pengelolaan Model**
- Pemuatan dan pembongkaran model secara dinamis
- Pemantauan kesehatan dan pemeriksaan status
- Pengumpulan metrik kinerja

### 3. **Pola Produksi**
- Mekanisme retry dengan backoff eksponensial
- Circuit breaker untuk toleransi kesalahan
- Logging dan pemantauan yang komprehensif

### 4. **Penanganan Respons yang Fleksibel**
- Respons streaming untuk aplikasi real-time
- Pemrosesan batch untuk skenario throughput tinggi
- Parsing dan validasi respons kustom

## Contoh Penggunaan

### Integrasi API Dasar
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Integrasi Streaming
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Pemantauan Kesehatan
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Struktur File

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Integrasi Microsoft Foundry Local

Contoh ini mengikuti pola resmi Microsoft:

1. **Integrasi SDK**: Menggunakan `FoundryLocalManager` untuk pengelolaan layanan
2. **Endpoint REST**: Panggilan langsung ke `/v1/chat/completions` dan endpoint lainnya
3. **Autentikasi**: Penanganan kunci API yang tepat untuk layanan lokal
4. **Pengelolaan Model**: Daftar katalog, pengunduhan, dan pola pemuatan
5. **Penanganan Kesalahan**: Kode kesalahan dan respons yang direkomendasikan Microsoft

## Memulai

1. **Instal Dependensi**
   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan Contoh Dasar**
   ```bash
   python examples/basic_usage.py
   ```

3. **Coba Streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Pengaturan Produksi**
   ```bash
   python examples/production.py
   ```

## Konfigurasi

Variabel lingkungan untuk kustomisasi:
- `FOUNDRY_MODEL`: Model default yang digunakan (default: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Waktu tunggu permintaan dalam detik (default: 30)
- `FOUNDRY_RETRIES`: Jumlah upaya retry (default: 3)
- `FOUNDRY_LOG_LEVEL`: Tingkat logging (default: "INFO")

## Praktik Terbaik

1. **Manajemen Koneksi**: Gunakan kembali koneksi HTTP untuk kinerja yang lebih baik
2. **Penanganan Kesalahan**: Implementasikan logika retry yang tepat dengan backoff eksponensial
3. **Pemantauan Sumber Daya**: Lacak penggunaan memori model dan kinerja
4. **Keamanan**: Gunakan autentikasi yang tepat bahkan untuk layanan lokal
5. **Pengujian**: Sertakan pengujian unit dan integrasi

## Pemecahan Masalah

### Masalah Umum

**Layanan Tidak Berjalan**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Masalah Pemuatan Model**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Kesalahan Koneksi**
- Verifikasi Foundry Local berjalan di port yang benar
- Periksa pengaturan firewall
- Pastikan header autentikasi yang tepat

## Optimasi Kinerja

1. **Pooling Koneksi**: Gunakan objek sesi untuk beberapa permintaan
2. **Operasi Asinkron**: Manfaatkan asyncio untuk permintaan bersamaan
3. **Caching**: Cache respons model jika sesuai
4. **Pemantauan**: Lacak waktu respons dan sesuaikan waktu tunggu

## Hasil Pembelajaran

Setelah menyelesaikan contoh ini, Anda akan memahami:
- Integrasi REST API langsung dengan Foundry Local
- Pola implementasi klien HTTP kustom
- Penanganan kesalahan dan pemantauan yang siap produksi
- Arsitektur layanan Microsoft Foundry Local
- Teknik optimasi kinerja untuk layanan AI lokal

## Langkah Selanjutnya

- Jelajahi Contoh 08: Aplikasi Chat Windows 11
- Coba Contoh 09: Orkestrasi Multi-Agent
- Pelajari Contoh 10: Foundry Local sebagai Integrasi Alat

---

