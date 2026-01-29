# Contoh 04: Aplikasi Chat Produksi dengan Chainlit

Contoh lengkap yang menunjukkan berbagai pendekatan untuk membangun aplikasi chat siap produksi menggunakan Microsoft Foundry Local, dengan antarmuka web modern, respons streaming, dan teknologi browser terkini.

## Apa yang Termasuk

- **🚀 Aplikasi Chat Chainlit** (`app.py`): Aplikasi chat siap produksi dengan streaming
- **🌐 Demo WebGPU** (`webgpu-demo/`): Inferensi AI berbasis browser dengan akselerasi perangkat keras
- **🎨 Integrasi Open WebUI** (`open-webui-guide.md`): Antarmuka profesional mirip ChatGPT
- **📚 Notebook Edukasi** (`chainlit_app.ipynb`): Materi pembelajaran interaktif

## Memulai dengan Cepat

### 1. Aplikasi Chat Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Buka di: `http://localhost:8080`

### 2. Demo Browser WebGPU

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Buka di: `http://localhost:5173`

### 3. Pengaturan Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Buka di: `http://localhost:3000`

## Pola Arsitektur

### Matriks Keputusan Lokal vs Cloud

| Skenario | Rekomendasi | Alasan |
|----------|-------------|--------|
| **Data Sensitif Privasi** | 🏠 Lokal (Foundry) | Data tidak pernah meninggalkan perangkat |
| **Penalaran Kompleks** | ☁️ Cloud (Azure OpenAI) | Akses ke model yang lebih besar |
| **Chat Real-time** | 🏠 Lokal (Foundry) | Latensi lebih rendah, respons lebih cepat |
| **Analisis Dokumen** | 🔄 Hybrid | Lokal untuk ekstraksi, cloud untuk analisis |
| **Generasi Kode** | 🏠 Lokal (Foundry) | Privasi + model khusus |
| **Tugas Penelitian** | ☁️ Cloud (Azure OpenAI) | Basis pengetahuan luas diperlukan |

### Perbandingan Teknologi

| Teknologi | Kasus Penggunaan | Kelebihan | Kekurangan |
|-----------|------------------|-----------|------------|
| **Chainlit** | Pengembang Python, prototipe cepat | Pengaturan mudah, dukungan streaming | Hanya Python |
| **WebGPU** | Privasi maksimal, skenario offline | Native browser, tidak perlu server | Ukuran model terbatas |
| **Open WebUI** | Penerapan produksi, tim | UI profesional, manajemen pengguna | Membutuhkan Docker |

## Prasyarat

- **Foundry Local**: Terinstal dan berjalan ([Unduh](https://aka.ms/foundry-local-installer))
- **Python**: Versi 3.10+ dengan lingkungan virtual
- **Model**: Setidaknya satu model dimuat (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge dengan dukungan WebGPU untuk demo
- **Docker**: Untuk Open WebUI (opsional)

## Instalasi & Pengaturan

### 1. Pengaturan Lingkungan Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Pengaturan Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Aplikasi Contoh

### Aplikasi Chat Chainlit

**Fitur:**
- 🚀 **Streaming Real-time**: Token muncul saat dihasilkan
- 🛡️ **Penanganan Kesalahan yang Kuat**: Penurunan dan pemulihan yang mulus
- 🎨 **UI Modern**: Antarmuka chat profesional siap pakai
- 🔧 **Konfigurasi Fleksibel**: Variabel lingkungan dan deteksi otomatis
- 📱 **Desain Responsif**: Berfungsi di perangkat desktop dan seluler

**Memulai dengan Cepat:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### Demo Browser WebGPU

**Fitur:**
- 🌐 **AI Native Browser**: Tidak memerlukan server, berjalan sepenuhnya di browser
- ⚡ **Akselerasi WebGPU**: Akselerasi perangkat keras jika tersedia
- 🔒 **Privasi Maksimal**: Data tidak pernah meninggalkan perangkat Anda
- 🎯 **Tanpa Instalasi**: Berfungsi di browser yang kompatibel
- 🔄 **Fallback yang Mulus**: Beralih ke CPU jika WebGPU tidak tersedia

**Menjalankan:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integrasi Open WebUI

**Fitur:**
- 🎨 **Antarmuka Mirip ChatGPT**: UI profesional yang familiar
- 👥 **Dukungan Multi-pengguna**: Akun pengguna dan riwayat percakapan
- 📁 **Pemrosesan File**: Unggah dan analisis dokumen
- 🔄 **Penggantian Model**: Mudah beralih antara model yang berbeda
- 🐳 **Penerapan Docker**: Pengaturan siap produksi yang terkontainerisasi

**Pengaturan Cepat:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Referensi Konfigurasi

### Variabel Lingkungan

| Variabel | Deskripsi | Default | Contoh |
|----------|-----------|---------|--------|
| `MODEL` | Alias model yang digunakan | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Endpoint Foundry Local | Terdeteksi otomatis | `http://localhost:51211` |
| `API_KEY` | API key (opsional untuk lokal) | `""` | `your-api-key` |

## Pemecahan Masalah

### Masalah Umum

**Aplikasi Chainlit:**

1. **Layanan tidak tersedia:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Konflik port:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Masalah lingkungan Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Demo WebGPU:**

1. **WebGPU tidak didukung:**
   - Perbarui ke Chrome/Edge 113+
   - Aktifkan WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Periksa status GPU: `chrome://gpu`
   - Demo akan otomatis beralih ke CPU

2. **Kesalahan pemuatan model:**
   - Pastikan koneksi internet untuk mengunduh model
   - Periksa konsol browser untuk kesalahan CORS
   - Verifikasi bahwa Anda melayani melalui HTTP (bukan file://)

**Open WebUI:**

1. **Koneksi ditolak:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Model tidak muncul:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Daftar Periksa Validasi

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Penggunaan Lanjutan

### Optimasi Performa

**Chainlit:**
- Gunakan streaming untuk performa yang lebih baik
- Implementasikan pooling koneksi untuk tingkat konkurensi tinggi
- Cache respons model untuk kueri yang berulang
- Pantau penggunaan memori dengan riwayat percakapan yang besar

**WebGPU:**
- Gunakan WebGPU untuk privasi dan kecepatan maksimal
- Implementasikan kuantisasi model untuk model yang lebih kecil
- Gunakan Web Workers untuk pemrosesan latar belakang
- Cache model yang dikompilasi di penyimpanan browser

**Open WebUI:**
- Gunakan volume persisten untuk riwayat percakapan
- Konfigurasikan batas sumber daya untuk kontainer Docker
- Implementasikan strategi pencadangan untuk data pengguna
- Atur proxy terbalik untuk terminasi SSL

### Pola Integrasi

**Hybrid Lokal/Cloud:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Pipeline Multi-Modal:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Penerapan Produksi

### Pertimbangan Keamanan

- **API Keys**: Gunakan variabel lingkungan, jangan pernah hardcode
- **Jaringan**: Gunakan HTTPS di produksi, pertimbangkan VPN untuk akses tim
- **Kontrol Akses**: Implementasikan autentikasi untuk Open WebUI
- **Privasi Data**: Audit data apa yang tetap lokal vs. yang dikirim ke cloud
- **Pembaruan**: Jaga Foundry Local dan kontainer tetap diperbarui

### Pemantauan dan Pemeliharaan

- **Pemeriksaan Kesehatan**: Implementasikan pemantauan endpoint
- **Logging**: Sentralisasi log dari semua komponen
- **Metrik**: Lacak waktu respons, tingkat kesalahan, penggunaan sumber daya
- **Pencadangan**: Pencadangan rutin data percakapan dan konfigurasi

## Referensi dan Sumber Daya

### Dokumentasi
- [Dokumentasi Chainlit](https://docs.chainlit.io/) - Panduan lengkap framework
- [Dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Dokumentasi resmi Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integrasi WebGPU
- [Dokumentasi Open WebUI](https://docs.openwebui.com/) - Konfigurasi lanjutan

### File Contoh
- [`app.py`](../../../../../Module08/samples/04/app.py) - Aplikasi Chainlit produksi
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Notebook edukasi
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Inferensi AI berbasis browser
- [`open-webui-guide.md`](./open-webui-guide.md) - Pengaturan lengkap Open WebUI

### Contoh Terkait
- [Dokumentasi Sesi 4](../../04.CuttingEdgeModels.md) - Panduan sesi lengkap
- [Contoh Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Contoh resmi

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.