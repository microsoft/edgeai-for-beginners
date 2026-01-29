# Contoh 01: Sembang Pantas melalui OpenAI SDK

Contoh sembang ringkas yang menunjukkan cara menggunakan OpenAI SDK dengan Microsoft Foundry Local untuk inferens AI secara tempatan.

## Gambaran Keseluruhan

Contoh ini menunjukkan cara untuk:
- Menggunakan OpenAI Python SDK dengan Foundry Local
- Mengendalikan konfigurasi Azure OpenAI dan Foundry tempatan
- Melaksanakan pengendalian ralat dan strategi sandaran yang betul
- Menggunakan FoundryLocalManager untuk pengurusan perkhidmatan

## Prasyarat

- **Foundry Local**: Dipasang dan tersedia dalam PATH
- **Python**: Versi 3.8 atau lebih baru
- **Model**: Model yang dimuatkan dalam Foundry Local (contohnya, `phi-4-mini`)

## Pemasangan

1. **Sediakan persekitaran Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Pasang kebergantungan:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Mulakan perkhidmatan Foundry Local dan muatkan model:**
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

## Ciri Kod

### Integrasi FoundryLocalManager

Contoh ini menggunakan SDK rasmi Foundry Local untuk pengurusan perkhidmatan yang betul:

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

### Pengendalian Ralat

Pengendalian ralat yang kukuh dengan sandaran kepada konfigurasi manual:
- Penemuan perkhidmatan automatik
- Penurunan fungsi secara beransur jika SDK tidak tersedia
- Mesej ralat yang jelas untuk penyelesaian masalah

## Pembolehubah Persekitaran

| Pembolehubah | Penerangan | Lalai | Diperlukan |
|--------------|------------|-------|------------|
| `MODEL` | Alias atau nama model | `phi-4-mini` | Tidak |
| `BASE_URL` | URL asas Foundry Local | `http://localhost:8000` | Tidak |
| `API_KEY` | Kunci API (biasanya tidak diperlukan untuk tempatan) | `""` | Tidak |
| `AZURE_OPENAI_ENDPOINT` | Endpoint Azure OpenAI | - | Untuk Azure |
| `AZURE_OPENAI_API_KEY` | Kunci API Azure OpenAI | - | Untuk Azure |
| `AZURE_OPENAI_API_VERSION` | Versi API Azure | `2024-08-01-preview` | Tidak |

## Penyelesaian Masalah

### Isu Biasa

1. **Amaran "Tidak dapat menggunakan Foundry SDK":**
   - Pasang foundry-local-sdk: `pip install foundry-local-sdk`
   - Atau tetapkan pembolehubah persekitaran untuk konfigurasi manual

2. **Sambungan ditolak:**
   - Pastikan Foundry Local sedang berjalan: `foundry service status`
   - Periksa jika model telah dimuatkan: `foundry service ps`

3. **Model tidak ditemui:**
   - Senaraikan model yang tersedia: `foundry model list`
   - Muatkan model: `foundry model run phi-4-mini`

### Pengesahan

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Rujukan

- [Dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [GitHub Foundry Local](https://github.com/microsoft/Foundry-Local)
- [Rujukan API Serasi OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

