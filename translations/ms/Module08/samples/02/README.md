# Contoh 02: Integrasi SDK OpenAI

Menunjukkan integrasi lanjutan dengan OpenAI Python SDK, menyokong kedua-dua Microsoft Foundry Local dan Azure OpenAI dengan respons penstriman serta pengendalian ralat yang betul.

## Gambaran Keseluruhan

Contoh ini mempamerkan:
- Peralihan lancar antara Foundry Local dan Azure OpenAI
- Penstriman penyelesaian chat untuk pengalaman pengguna yang lebih baik
- Penggunaan SDK FoundryLocalManager yang betul
- Mekanisme pengendalian ralat dan fallback yang kukuh
- Corak kod yang sedia untuk pengeluaran

## Prasyarat

- **Foundry Local**: Dipasang dan berjalan (untuk inferens tempatan)
- **Python**: Versi 3.8 atau lebih baru dengan OpenAI SDK
- **Azure OpenAI**: Endpoint dan kunci API yang sah (untuk inferens awan)

## Pemasangan

1. **Tetapkan persekitaran Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Pasang kebergantungan:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Mulakan Foundry Local (untuk mod tempatan):**
   ```cmd
   foundry model run phi-4-mini
   ```

## Senario Penggunaan

### Foundry Local (Default)

**Pilihan 1: Menggunakan FoundryLocalManager (Disyorkan)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Pilihan 2: Konfigurasi Manual**
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

## Seni Bina Kod

### Corak Kilang Klien

Contoh ini menggunakan corak kilang untuk mencipta klien yang sesuai:

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

### Respons Penstriman

Contoh ini menunjukkan penstriman untuk penjanaan respons masa nyata:

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

## Pembolehubah Persekitaran

### Konfigurasi Foundry Local

| Pembolehubah | Penerangan | Lalai | Diperlukan |
|--------------|------------|-------|------------|
| `MODEL` | Alias model untuk digunakan | `phi-4-mini` | Tidak |
| `BASE_URL` | Endpoint Foundry Local | `http://localhost:8000` | Tidak |
| `API_KEY` | Kunci API (pilihan untuk tempatan) | `""` | Tidak |

### Konfigurasi Azure OpenAI

| Pembolehubah | Penerangan | Lalai | Diperlukan |
|--------------|------------|-------|------------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint sumber Azure OpenAI | - | Ya |
| `AZURE_OPENAI_API_KEY` | Kunci API Azure OpenAI | - | Ya |
| `AZURE_OPENAI_API_VERSION` | Versi API | `2024-08-01-preview` | Tidak |
| `MODEL` | Nama deployment Azure | `your-deployment-name` | Ya |

## Ciri Lanjutan

### Penemuan Perkhidmatan Automatik

Contoh ini secara automatik mengesan perkhidmatan yang sesuai berdasarkan pembolehubah persekitaran:

1. **Mod Azure**: Jika `AZURE_OPENAI_ENDPOINT` dan `AZURE_OPENAI_API_KEY` ditetapkan
2. **Mod SDK Foundry**: Jika SDK Foundry Local tersedia
3. **Mod Manual**: Fallback kepada konfigurasi manual

### Pengendalian Ralat

- Fallback yang lancar dari SDK ke konfigurasi manual
- Mesej ralat yang jelas untuk penyelesaian masalah
- Pengendalian pengecualian yang betul untuk isu rangkaian
- Pengesahan pembolehubah persekitaran yang diperlukan

## Pertimbangan Prestasi

### Perbandingan Tempatan vs Awan

**Kelebihan Foundry Local:**
- ✅ Tiada kos API
- ✅ Privasi data (tiada data meninggalkan peranti)
- ✅ Latensi rendah untuk model yang disokong
- ✅ Berfungsi secara offline

**Kelebihan Azure OpenAI:**
- ✅ Akses kepada model besar terkini
- ✅ Throughput lebih tinggi
- ✅ Tiada keperluan pengkomputeran tempatan
- ✅ SLA gred perusahaan

## Penyelesaian Masalah

### Isu Biasa

1. **Amaran "Tidak dapat menggunakan SDK Foundry":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Kesalahan pengesahan Azure:**
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

### Pemeriksaan Kesihatan

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```

## Langkah Seterusnya

- **Contoh 03**: Penemuan model dan penanda aras
- **Contoh 04**: Membina aplikasi Chainlit RAG
- **Contoh 05**: Orkestrasi multi-agent
- **Contoh 06**: Penghalaan model-sebagai-alat

## Rujukan

- [Dokumentasi Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Rujukan SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Dokumentasi OpenAI Python SDK](https://github.com/openai/openai-python)
- [Panduan Penstriman Penyelesaian](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

