# Contoh 01: Obrolan Cepat dengan OpenAI SDK

Contoh sederhana obrolan yang menunjukkan cara menggunakan OpenAI SDK dengan Microsoft Foundry Local untuk inferensi AI lokal.

## Gambaran Umum

Contoh ini menunjukkan cara:
- Menggunakan OpenAI Python SDK dengan Foundry Local
- Menangani konfigurasi Azure OpenAI dan Foundry lokal
- Menerapkan penanganan kesalahan yang tepat dan strategi cadangan
- Menggunakan FoundryLocalManager untuk manajemen layanan

## Prasyarat

- **Foundry Local**: Terinstal dan tersedia di PATH
- **Python**: Versi 3.8 atau lebih baru
- **Model**: Model yang dimuat di Foundry Local (misalnya, `phi-4-mini`)

## Instalasi

1. **Siapkan lingkungan Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instal dependensi:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Mulai layanan Foundry Local dan muat model:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Penggunaan

### Foundry Local (Default)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```

## Fitur Kode

### Integrasi FoundryLocalManager

Contoh ini menggunakan Foundry Local SDK resmi untuk manajemen layanan yang tepat:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```

### Penanganan Kesalahan

Penanganan kesalahan yang kuat dengan cadangan ke konfigurasi manual:
- Penemuan layanan otomatis
- Penurunan layanan secara bertahap jika SDK tidak tersedia
- Pesan kesalahan yang jelas untuk pemecahan masalah

## Variabel Lingkungan

| Variabel | Deskripsi | Default | Wajib |
|----------|-------------|---------|----------|
| `MODEL` | Alias atau nama model | `phi-4-mini` | Tidak |
| `BASE_URL` | URL dasar Foundry Local | `http://localhost:8000` | Tidak |
| `API_KEY` | Kunci API (biasanya tidak diperlukan untuk lokal) | `""` | Tidak |
| `AZURE_OPENAI_ENDPOINT` | Endpoint Azure OpenAI | - | Untuk Azure |
| `AZURE_OPENAI_API_KEY` | Kunci API Azure OpenAI | - | Untuk Azure |
| `AZURE_OPENAI_API_VERSION` | Versi API Azure | `2024-08-01-preview` | Tidak |

## Pemecahan Masalah

### Masalah Umum

1. **Peringatan "Tidak dapat menggunakan Foundry SDK":**
   - Instal foundry-local-sdk: `pip install foundry-local-sdk`
   - Atau atur variabel lingkungan untuk konfigurasi manual

2. **Koneksi ditolak:**
   - Pastikan Foundry Local berjalan: `foundry service status`
   - Periksa apakah model telah dimuat: `foundry service ps`

3. **Model tidak ditemukan:**
   - Daftar model yang tersedia: `foundry model list`
   - Muat model: `foundry model run phi-4-mini`

### Verifikasi

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Referensi

- [Dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Referensi API yang Kompatibel dengan OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

