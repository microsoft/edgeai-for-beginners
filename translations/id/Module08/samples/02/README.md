# Contoh 02: Integrasi SDK OpenAI

Menunjukkan integrasi lanjutan dengan OpenAI Python SDK, mendukung Microsoft Foundry Local dan Azure OpenAI dengan respons streaming dan penanganan kesalahan yang tepat.

## Gambaran Umum

Contoh ini menampilkan:
- Pergantian yang mulus antara Foundry Local dan Azure OpenAI
- Streaming chat completions untuk pengalaman pengguna yang lebih baik
- Penggunaan yang tepat dari FoundryLocalManager SDK
- Penanganan kesalahan yang tangguh dan mekanisme fallback
- Pola kode siap produksi

## Prasyarat

- **Foundry Local**: Terinstal dan berjalan (untuk inferensi lokal)
- **Python**: Versi 3.8 atau lebih baru dengan OpenAI SDK
- **Azure OpenAI**: Endpoint dan API key yang valid (untuk inferensi cloud)

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

3. **Mulai Foundry Local (untuk mode lokal):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Skenario Penggunaan

### Foundry Local (Default)

**Opsi 1: Menggunakan FoundryLocalManager (Direkomendasikan)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Opsi 2: Konfigurasi Manual**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## Arsitektur Kode

### Pola Client Factory

Contoh ini menggunakan pola factory untuk membuat klien yang sesuai:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### Respons Streaming

Contoh ini menunjukkan streaming untuk menghasilkan respons secara real-time:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## Variabel Lingkungan

### Konfigurasi Foundry Local

| Variabel | Deskripsi | Default | Wajib |
|----------|-------------|---------|----------|
| `MODEL` | Alias model yang digunakan | `phi-4-mini` | Tidak |
| `BASE_URL` | Endpoint Foundry Local | `http://localhost:8000` | Tidak |
| `API_KEY` | API key (opsional untuk lokal) | `""` | Tidak |

### Konfigurasi Azure OpenAI

| Variabel | Deskripsi | Default | Wajib |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint resource Azure OpenAI | - | Ya |
| `AZURE_OPENAI_API_KEY` | API key Azure OpenAI | - | Ya |
| `AZURE_OPENAI_API_VERSION` | Versi API | `2024-08-01-preview` | Tidak |
| `MODEL` | Nama deployment Azure | `your-deployment-name` | Ya |

## Fitur Lanjutan

### Penemuan Layanan Otomatis

Contoh ini secara otomatis mendeteksi layanan yang sesuai berdasarkan variabel lingkungan:

1. **Mode Azure**: Jika `AZURE_OPENAI_ENDPOINT` dan `AZURE_OPENAI_API_KEY` diatur
2. **Mode Foundry SDK**: Jika Foundry Local SDK tersedia
3. **Mode Manual**: Fallback ke konfigurasi manual

### Penanganan Kesalahan

- Fallback yang mulus dari SDK ke konfigurasi manual
- Pesan kesalahan yang jelas untuk pemecahan masalah
- Penanganan pengecualian yang tepat untuk masalah jaringan
- Validasi variabel lingkungan yang diperlukan

## Pertimbangan Performa

### Perbandingan Lokal vs Cloud

**Keunggulan Foundry Local:**
- ✅ Tidak ada biaya API
- ✅ Privasi data (data tidak keluar dari perangkat)
- ✅ Latensi rendah untuk model yang didukung
- ✅ Berfungsi secara offline

**Keunggulan Azure OpenAI:**
- ✅ Akses ke model besar terbaru
- ✅ Throughput lebih tinggi
- ✅ Tidak memerlukan komputasi lokal
- ✅ SLA tingkat perusahaan

## Pemecahan Masalah

### Masalah Umum

1. **Peringatan "Tidak dapat menggunakan Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Kesalahan autentikasi Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model tidak tersedia:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Pemeriksaan Kesehatan

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Langkah Selanjutnya

- **Contoh 03**: Penemuan model dan benchmarking
- **Contoh 04**: Membangun aplikasi Chainlit RAG
- **Contoh 05**: Orkestrasi multi-agent
- **Contoh 06**: Routing model-as-tools

## Referensi

- [Dokumentasi Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Referensi SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Dokumentasi OpenAI Python SDK](https://github.com/openai/openai-python)
- [Panduan Streaming Completions](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

