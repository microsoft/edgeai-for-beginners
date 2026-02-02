# Contoh 04: Aplikasi Chat Produksi dengan Chainlit

Contoh komprehensif yang menunjukkan pelbagai pendekatan untuk membina aplikasi chat siap produksi menggunakan Microsoft Foundry Local, dengan antara muka web moden, respons penstriman, dan teknologi pelayar terkini.

## Apa yang Disertakan

- **🚀 Aplikasi Chat Chainlit** (`app.py`): Aplikasi chat siap produksi dengan penstriman
- **🌐 Demo WebGPU** (`webgpu-demo/`): Inferens AI berasaskan pelayar dengan pecutan perkakasan
- **🎨 Integrasi Open WebUI** (`open-webui-guide.md`): Antara muka profesional seperti ChatGPT
- **📚 Notebook Pendidikan** (`chainlit_app.ipynb`): Bahan pembelajaran interaktif

## Permulaan Pantas

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

### 2. Demo Pelayar WebGPU

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Buka di: `http://localhost:5173`

### 3. Persediaan Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Buka di: `http://localhost:3000`

## Corak Seni Bina

### Matriks Keputusan Tempatan vs Awan

| Senario | Cadangan | Sebab |
|---------|----------|-------|
| **Data Sensitif Privasi** | 🏠 Tempatan (Foundry) | Data tidak pernah meninggalkan peranti |
| **Penaakulan Kompleks** | ☁️ Awan (Azure OpenAI) | Akses kepada model yang lebih besar |
| **Chat Masa Nyata** | 🏠 Tempatan (Foundry) | Latensi lebih rendah, respons lebih pantas |
| **Analisis Dokumen** | 🔄 Hibrid | Tempatan untuk pengekstrakan, awan untuk analisis |
| **Penjanaan Kod** | 🏠 Tempatan (Foundry) | Privasi + model khusus |
| **Tugas Penyelidikan** | ☁️ Awan (Azure OpenAI) | Memerlukan pangkalan pengetahuan yang luas |

### Perbandingan Teknologi

| Teknologi | Kes Penggunaan | Kelebihan | Kekurangan |
|-----------|----------------|-----------|------------|
| **Chainlit** | Pembangun Python, prototaip pantas | Persediaan mudah, sokongan penstriman | Hanya Python |
| **WebGPU** | Privasi maksimum, senario luar talian | Asli pelayar, tidak memerlukan pelayan | Saiz model terhad |
| **Open WebUI** | Penggunaan produksi, pasukan | UI profesional, pengurusan pengguna | Memerlukan Docker |

## Prasyarat

- **Foundry Local**: Dipasang dan berjalan ([Muat Turun](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ dengan persekitaran maya
- **Model**: Sekurang-kurangnya satu dimuatkan (`foundry model run phi-4-mini`)
- **Pelayar**: Chrome/Edge dengan sokongan WebGPU untuk demo
- **Docker**: Untuk Open WebUI (pilihan)

## Pemasangan & Persediaan

### 1. Persediaan Persekitaran Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Persediaan Foundry Local

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

**Ciri-ciri:**
- 🚀 **Penstriman Masa Nyata**: Token muncul semasa ia dijana
- 🛡️ **Pengendalian Ralat Kukuh**: Kemerosotan dan pemulihan yang lancar
- 🎨 **UI Moden**: Antara muka chat profesional sedia ada
- 🔧 **Konfigurasi Fleksibel**: Pembolehubah persekitaran dan pengesanan automatik
- 📱 **Reka Bentuk Responsif**: Berfungsi pada peranti desktop dan mudah alih

**Permulaan Pantas:**
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

### Demo Pelayar WebGPU

**Ciri-ciri:**
- 🌐 **AI Asli Pelayar**: Tidak memerlukan pelayan, berjalan sepenuhnya dalam pelayar
- ⚡ **Pecutan WebGPU**: Pecutan perkakasan apabila tersedia
- 🔒 **Privasi Maksimum**: Tiada data meninggalkan peranti anda
- 🎯 **Pemasangan Sifar**: Berfungsi dalam mana-mana pelayar yang serasi
- 🔄 **Kemerosotan Lancar**: Beralih kepada CPU jika WebGPU tidak tersedia

**Menjalankan:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integrasi Open WebUI

**Ciri-ciri:**
- 🎨 **Antara Muka Seperti ChatGPT**: UI profesional, biasa digunakan
- 👥 **Sokongan Berbilang Pengguna**: Akaun pengguna dan sejarah perbualan
- 📁 **Pemprosesan Fail**: Muat naik dan analisis dokumen
- 🔄 **Pertukaran Model**: Pertukaran mudah antara model yang berbeza
- 🐳 **Penggunaan Docker**: Persediaan kontena siap produksi

**Persediaan Pantas:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Rujukan Konfigurasi

### Pembolehubah Persekitaran

| Pembolehubah | Penerangan | Lalai | Contoh |
|--------------|------------|-------|--------|
| `MODEL` | Alias model untuk digunakan | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Titik akhir Foundry Local | Dikesan secara automatik | `http://localhost:51211` |
| `API_KEY` | Kunci API (pilihan untuk tempatan) | `""` | `your-api-key` |

## Penyelesaian Masalah

### Isu Biasa

**Aplikasi Chainlit:**

1. **Perkhidmatan tidak tersedia:**
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

3. **Isu persekitaran Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Demo WebGPU:**

1. **WebGPU tidak disokong:**
   - Kemas kini kepada Chrome/Edge 113+
   - Aktifkan WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Semak status GPU: `chrome://gpu`
   - Demo akan beralih kepada CPU secara automatik

2. **Ralat pemuatan model:**
   - Pastikan sambungan internet untuk muat turun model
   - Semak konsol pelayar untuk ralat CORS
   - Sahkan anda melayani melalui HTTP (bukan file://)

**Open WebUI:**

1. **Sambungan ditolak:**
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

### Senarai Semak Pengesahan

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

### Pengoptimuman Prestasi

**Chainlit:**
- Gunakan penstriman untuk prestasi yang lebih baik
- Laksanakan pengumpulan sambungan untuk kebolehserentakan tinggi
- Cache respons model untuk pertanyaan berulang
- Pantau penggunaan memori dengan sejarah perbualan yang besar

**WebGPU:**
- Gunakan WebGPU untuk privasi dan kelajuan maksimum
- Laksanakan kuantisasi model untuk model yang lebih kecil
- Gunakan Web Workers untuk pemprosesan latar belakang
- Cache model yang telah disusun dalam storan pelayar

**Open WebUI:**
- Gunakan volum berterusan untuk sejarah perbualan
- Konfigurasi had sumber untuk kontena Docker
- Laksanakan strategi sandaran untuk data pengguna
- Sediakan proksi terbalik untuk penamatan SSL

### Corak Integrasi

**Hibrid Tempatan/Awan:**
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

**Saluran Multi-Mod:**
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

## Penggunaan Produksi

### Pertimbangan Keselamatan

- **Kunci API**: Gunakan pembolehubah persekitaran, jangan kodkan secara langsung
- **Rangkaian**: Gunakan HTTPS dalam produksi, pertimbangkan VPN untuk akses pasukan
- **Kawalan Akses**: Laksanakan pengesahan untuk Open WebUI
- **Privasi Data**: Audit data yang kekal tempatan vs. dihantar ke awan
- **Kemas Kini**: Pastikan Foundry Local dan kontena dikemas kini

### Pemantauan dan Penyelenggaraan

- **Semakan Kesihatan**: Laksanakan pemantauan titik akhir
- **Log**: Pusatkan log dari semua komponen
- **Metrik**: Jejak masa respons, kadar ralat, penggunaan sumber
- **Sandaran**: Sandaran berkala untuk data perbualan dan konfigurasi

## Rujukan dan Sumber

### Dokumentasi
- [Dokumentasi Chainlit](https://docs.chainlit.io/) - Panduan rangka kerja lengkap
- [Dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Dokumentasi rasmi Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integrasi WebGPU
- [Dokumentasi Open WebUI](https://docs.openwebui.com/) - Konfigurasi lanjutan

### Fail Contoh
- [`app.py`](../../../../../Module08/samples/04/app.py) - Aplikasi Chainlit produksi
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Notebook pendidikan
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Inferens AI berasaskan pelayar
- [`open-webui-guide.md`](./open-webui-guide.md) - Persediaan Open WebUI lengkap

### Contoh Berkaitan
- [Dokumentasi Sesi 4](../../04.CuttingEdgeModels.md) - Panduan sesi lengkap
- [Contoh Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Contoh rasmi

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.