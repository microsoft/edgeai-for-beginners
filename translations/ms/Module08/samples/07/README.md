# Foundry Local sebagai Contoh API

Contoh ini menunjukkan cara menggunakan Microsoft Foundry Local sebagai perkhidmatan REST API tanpa bergantung pada OpenAI SDK. Ia memaparkan corak integrasi HTTP langsung untuk kawalan dan penyesuaian maksimum.

## Gambaran Keseluruhan

Berdasarkan corak rasmi Microsoft Foundry Local, contoh ini menyediakan:
- Integrasi REST API langsung dengan FoundryLocalManager
- Pelaksanaan klien HTTP tersuai
- Pengurusan model dan pemantauan kesihatan
- Pengendalian respons penstriman dan bukan penstriman
- Pengendalian ralat dan logik ulang cuba yang sedia untuk produksi

## Prasyarat

1. **Pemasangan Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Kebergantungan Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Seni Bina

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Ciri Utama

### 1. **Integrasi HTTP Langsung**
- Panggilan REST API tulen tanpa kebergantungan SDK
- Pengesahan dan header tersuai
- Kawalan penuh terhadap pengendalian permintaan/respons

### 2. **Pengurusan Model**
- Pemuatan dan pemunggahan model secara dinamik
- Pemantauan kesihatan dan pemeriksaan status
- Pengumpulan metrik prestasi

### 3. **Corak Produksi**
- Mekanisme ulang cuba dengan backoff eksponen
- Circuit breaker untuk toleransi kesalahan
- Log dan pemantauan yang komprehensif

### 4. **Pengendalian Respons Fleksibel**
- Respons penstriman untuk aplikasi masa nyata
- Pemprosesan batch untuk senario throughput tinggi
- Penguraian dan pengesahan respons tersuai

## Contoh Penggunaan

### Integrasi API Asas
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

### Integrasi Penstriman
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Pemantauan Kesihatan
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Struktur Fail

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

Contoh ini mengikuti corak rasmi Microsoft:

1. **Integrasi SDK**: Menggunakan `FoundryLocalManager` untuk pengurusan perkhidmatan
2. **Endpoint REST**: Panggilan langsung ke `/v1/chat/completions` dan endpoint lain
3. **Pengesahan**: Pengendalian kunci API yang betul untuk perkhidmatan tempatan
4. **Pengurusan Model**: Penyenaraian katalog, muat turun, dan corak pemuatan
5. **Pengendalian Ralat**: Kod ralat dan respons yang disyorkan oleh Microsoft

## Memulakan

1. **Pasang Kebergantungan**
   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan Contoh Asas**
   ```bash
   python examples/basic_usage.py
   ```

3. **Cuba Penstriman**
   ```bash
   python examples/streaming.py
   ```

4. **Persediaan Produksi**
   ```bash
   python examples/production.py
   ```

## Konfigurasi

Pembolehubah persekitaran untuk penyesuaian:
- `FOUNDRY_MODEL`: Model lalai untuk digunakan (lalai: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Tempoh tamat permintaan dalam saat (lalai: 30)
- `FOUNDRY_RETRIES`: Bilangan percubaan ulang (lalai: 3)
- `FOUNDRY_LOG_LEVEL`: Tahap log (lalai: "INFO")

## Amalan Terbaik

1. **Pengurusan Sambungan**: Gunakan semula sambungan HTTP untuk prestasi yang lebih baik
2. **Pengendalian Ralat**: Laksanakan logik ulang cuba yang betul dengan backoff eksponen
3. **Pemantauan Sumber**: Jejaki penggunaan memori model dan prestasi
4. **Keselamatan**: Gunakan pengesahan yang betul walaupun untuk perkhidmatan tempatan
5. **Ujian**: Sertakan ujian unit dan integrasi

## Penyelesaian Masalah

### Isu Biasa

**Perkhidmatan Tidak Berjalan**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Isu Pemuatan Model**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Kesalahan Sambungan**
- Sahkan Foundry Local berjalan pada port yang betul
- Periksa tetapan firewall
- Pastikan header pengesahan yang betul

## Pengoptimuman Prestasi

1. **Pengumpulan Sambungan**: Gunakan objek sesi untuk permintaan berganda
2. **Operasi Asinkron**: Manfaatkan asyncio untuk permintaan serentak
3. **Caching**: Cache respons model di mana sesuai
4. **Pemantauan**: Jejaki masa respons dan sesuaikan tempoh tamat

## Hasil Pembelajaran

Selepas melengkapkan contoh ini, anda akan memahami:
- Integrasi REST API langsung dengan Foundry Local
- Corak pelaksanaan klien HTTP tersuai
- Pengendalian ralat dan pemantauan yang sedia untuk produksi
- Seni bina perkhidmatan Microsoft Foundry Local
- Teknik pengoptimuman prestasi untuk perkhidmatan AI tempatan

## Langkah Seterusnya

- Terokai Contoh 08: Aplikasi Chat Windows 11
- Cuba Contoh 09: Orkestrasi Multi-Agent
- Pelajari Contoh 10: Foundry Local sebagai Integrasi Alat

---

