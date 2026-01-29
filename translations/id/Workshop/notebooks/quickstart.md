# Panduan Cepat Workshop Notebooks

## Daftar Isi

- [Prasyarat](../../../../Workshop/notebooks)
- [Pengaturan Awal](../../../../Workshop/notebooks)
- [Sesi 04: Perbandingan Model](../../../../Workshop/notebooks)
- [Sesi 05: Orkestrator Multi-Agen](../../../../Workshop/notebooks)
- [Sesi 06: Routing Model Berbasis Intent](../../../../Workshop/notebooks)
- [Variabel Lingkungan](../../../../Workshop/notebooks)
- [Perintah Umum](../../../../Workshop/notebooks)

---

## Prasyarat

### 1. Instal Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifikasi Instalasi:**
```bash
foundry --version
```

### 2. Instal Dependensi Python

```bash
cd Workshop
pip install -r requirements.txt
```

Atau instal secara individual:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Pengaturan Awal

### Mulai Layanan Foundry Local

**Diperlukan sebelum menjalankan notebook apa pun:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Output yang diharapkan:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Unduh dan Muat Model

Notebook menggunakan model berikut secara default:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Verifikasi Pengaturan

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sesi 04: Perbandingan Model

### Tujuan
Membandingkan kinerja antara Small Language Models (SLM) dan Large Language Models (LLM).

### Pengaturan Cepat

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Menjalankan Notebook

1. **Buka** `session04_model_compare.ipynb` di VS Code atau Jupyter
2. **Restart kernel** (Kernel → Restart Kernel)
3. **Jalankan semua sel** secara berurutan

### Konfigurasi Utama

**Model Default:**
- **SLM:** `phi-4-mini` (~4GB RAM, lebih cepat)
- **LLM:** `qwen2.5-3b` (~3GB RAM, dioptimalkan untuk memori)

**Variabel Lingkungan (opsional):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Output yang Diharapkan

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Kustomisasi

**Gunakan model berbeda:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Prompt kustom:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Daftar Periksa Validasi

- [ ] Sel 12 menunjukkan model yang benar (phi-4-mini, qwen2.5-3b)
- [ ] Sel 12 menunjukkan endpoint yang benar (port 59959)
- [ ] Diagnostik Sel 16 berhasil (✅ Layanan berjalan)
- [ ] Pemeriksaan pra-penerbangan Sel 20 berhasil (kedua model ok)
- [ ] Perbandingan Sel 22 selesai dengan nilai latensi
- [ ] Validasi Sel 24 menunjukkan 🎉 SEMUA PEMERIKSAAN BERHASIL!

### Estimasi Waktu
- **Penggunaan pertama:** 5-10 menit (termasuk unduhan model)
- **Penggunaan berikutnya:** 1-2 menit

---

## Sesi 05: Orkestrator Multi-Agen

### Tujuan
Menunjukkan kolaborasi multi-agen menggunakan Foundry Local SDK - agen bekerja sama untuk menghasilkan output yang lebih baik.

### Pengaturan Cepat

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Menjalankan Notebook

1. **Buka** `session05_agents_orchestrator.ipynb`
2. **Restart kernel**
3. **Jalankan semua sel** secara berurutan

### Konfigurasi Utama

**Pengaturan Default (Model Sama untuk Kedua Agen):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Pengaturan Lanjutan (Model Berbeda):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arsitektur

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Output yang Diharapkan

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Ekstensi

**Tambahkan lebih banyak agen:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Pengujian batch:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Estimasi Waktu
- **Penggunaan pertama:** 3-5 menit
- **Penggunaan berikutnya:** 1-2 menit per pertanyaan

---

## Sesi 06: Routing Model Berbasis Intent

### Tujuan
Mengarahkan prompt secara cerdas ke model khusus berdasarkan intent yang terdeteksi.

### Pengaturan Cepat

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Catatan:** Sesi 06 menggunakan model CPU secara default untuk kompatibilitas maksimum.

### Menjalankan Notebook

1. **Buka** `session06_models_router.ipynb`
2. **Restart kernel**
3. **Jalankan semua sel** secara berurutan

### Konfigurasi Utama

**Katalog Default (Model CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternatif (Model GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Deteksi Intent

Router menggunakan pola regex untuk mendeteksi intent:

| Intent | Contoh Pola | Dialihkan Ke |
|--------|-------------|--------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Semua lainnya | phi-4-mini-cpu |

### Output yang Diharapkan

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Kustomisasi

**Tambahkan intent kustom:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Aktifkan pelacakan token:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Beralih ke Model GPU

Jika Anda memiliki VRAM 8GB+:

1. Di **Sel #6**, komentari katalog CPU
2. Hapus komentar katalog GPU
3. Muat model GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Restart kernel dan jalankan ulang notebook

### Estimasi Waktu
- **Penggunaan pertama:** 5-10 menit (pemuatan model)
- **Penggunaan berikutnya:** 30-60 detik per pengujian

---

## Variabel Lingkungan

### Konfigurasi Global

Setel sebelum memulai Jupyter/VS Code:

**Windows (Command Prompt):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Konfigurasi Dalam Notebook

Setel di awal notebook apa pun:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Perintah Umum

### Manajemen Layanan

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Manajemen Model

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Pengujian Endpoint

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Perintah Diagnostik

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Praktik Terbaik

### Sebelum Memulai Notebook Apa Pun

1. **Periksa layanan berjalan:**
   ```bash
   foundry service status
   ```

2. **Verifikasi model telah dimuat:**
   ```bash
   foundry model ls
   ```

3. **Restart kernel notebook** jika menjalankan ulang

4. **Hapus semua output** untuk menjalankan bersih

### Manajemen Sumber Daya

1. **Gunakan model CPU secara default** untuk kompatibilitas
2. **Beralih ke model GPU** hanya jika Anda memiliki VRAM 8GB+
3. **Tutup aplikasi GPU lainnya** sebelum menjalankan
4. **Biarkan layanan tetap berjalan** di antara sesi notebook
5. **Pantau penggunaan sumber daya** dengan Task Manager / nvidia-smi

### Pemecahan Masalah

1. **Selalu periksa layanan terlebih dahulu** sebelum debugging kode
2. **Restart kernel** jika Anda melihat konfigurasi lama
3. **Jalankan ulang sel diagnostik** setelah ada perubahan
4. **Periksa nama model** sesuai dengan yang dimuat
5. **Verifikasi port endpoint** sesuai dengan status layanan

---

## Referensi Cepat: Alias Model

### Model Umum

| Alias | Ukuran | Terbaik Untuk | RAM/VRAM | Varian |
|-------|--------|---------------|----------|--------|
| `phi-4-mini` | ~4B | Obrolan umum, ringkasan | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Generasi kode, refactoring | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Tugas umum, efisien | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Cepat, sumber daya rendah | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klasifikasi, sumber daya minimal | 1-2GB | `-cpu`, `-cuda-gpu` |

### Penamaan Varian

- **Nama dasar** (misalnya, `phi-4-mini`): Memilih varian terbaik secara otomatis untuk perangkat keras Anda
- **`-cpu`**: Dioptimalkan untuk CPU, bekerja di mana saja
- **`-cuda-gpu`**: Dioptimalkan untuk GPU NVIDIA, membutuhkan VRAM 8GB+
- **`-npu`**: Dioptimalkan untuk Qualcomm NPU, membutuhkan driver NPU

**Rekomendasi:** Gunakan nama dasar (tanpa akhiran) dan biarkan Foundry Local memilih varian terbaik secara otomatis.

---

## Indikator Keberhasilan

Anda siap ketika melihat:

✅ `foundry service status` menunjukkan "running"
✅ `foundry model ls` menunjukkan model yang Anda butuhkan
✅ Layanan dapat diakses di endpoint yang benar
✅ Pemeriksaan kesehatan mengembalikan 200 OK
✅ Sel diagnostik notebook berhasil
✅ Tidak ada kesalahan koneksi di output

---

## Mendapatkan Bantuan

### Dokumentasi
- **Repositori Utama**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referensi CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Pemecahan Masalah**: Lihat `troubleshooting.md` di direktori ini

### Masalah GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Terakhir Diperbarui:** 8 Oktober 2025  
**Versi:** Workshop Notebooks 2.0

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.