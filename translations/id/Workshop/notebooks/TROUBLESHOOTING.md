# Buku Panduan Pemecahan Masalah - Workshop Notebooks

## Daftar Isi

- [Masalah Umum dan Solusi](../../../../Workshop/notebooks)
- [Masalah Khusus Sesi 04](../../../../Workshop/notebooks)
- [Masalah Khusus Sesi 05](../../../../Workshop/notebooks)
- [Masalah Khusus Sesi 06](../../../../Workshop/notebooks)
- [Masalah Khusus Perangkat Keras](../../../../Workshop/notebooks)
- [Perintah Diagnostik](../../../../Workshop/notebooks)
- [Mendapatkan Bantuan](../../../../Workshop/notebooks)

---

## Masalah Umum dan Solusi

### 🔴 CUDA Out of Memory

**Pesan Kesalahan:**
```
CUDA failure 2: out of memory
```

**Penyebab Utama:** GPU tidak memiliki cukup VRAM untuk memuat model.

**Solusi:**

#### Opsi 1: Gunakan Varian CPU (Direkomendasikan)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Opsi 2: Gunakan Model yang Lebih Kecil di GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Opsi 3: Bersihkan Memori GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Opsi 4: Tingkatkan Memori GPU (jika memungkinkan)
- Tutup tab browser, editor video, atau aplikasi GPU lainnya
- Kurangi efek visual Windows
- Gunakan GPU khusus jika Anda memiliki GPU terintegrasi + khusus

---

### 🔴 APIConnectionError: Connection Error

**Pesan Kesalahan:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Penyebab Utama:** Layanan Foundry Local tidak berjalan atau tidak dapat diakses.

**Solusi:**

#### Langkah 1: Periksa Status Layanan
```bash
foundry service status
```

#### Langkah 2: Mulai Layanan jika Berhenti
```bash
foundry service start
```

#### Langkah 3: Verifikasi Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Langkah 4: Muat Model yang Diperlukan
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Langkah 5: Restart Kernel Notebook
Setelah memulai layanan dan memuat model, restart kernel notebook dan jalankan ulang semua sel.

---

### 🔴 Model Tidak Ditemukan di Katalog

**Pesan Kesalahan:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Penyebab Utama:** Model belum diunduh atau dimuat di Foundry Local.

**Solusi:**

#### Opsi 1: Unduh dan Muat Model
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Opsi 2: Gunakan Mode Pemilihan Otomatis
Perbarui CATALOG Anda untuk menggunakan nama model dasar (tanpa akhiran `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK akan secara otomatis memilih varian terbaik (CPU, GPU, atau NPU) untuk perangkat keras Anda.

---

### 🔴 HttpResponseError: 500 - Gagal Memuat Model

**Pesan Kesalahan:**
```
HttpResponseError: 500 - Failed loading model
```

**Penyebab Utama:** File model rusak atau tidak kompatibel dengan perangkat keras.

**Solusi:**

#### Unduh Ulang Model
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Gunakan Varian yang Berbeda
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Pesan Kesalahan:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Penyebab Utama:** Paket foundry-local-sdk tidak terinstal.

**Solusi:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Permintaan Pertama Lambat

**Gejala:** Penyelesaian pertama membutuhkan waktu lebih dari 30 detik, permintaan berikutnya lebih cepat.

**Penyebab Utama:** Ini adalah perilaku normal - layanan sedang memuat model ke dalam memori pada permintaan pertama.

**Solusi:**

#### Muat Model Sebelumnya
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Biarkan Layanan Berjalan
```bash
# Start service manually and leave it running
foundry service start
```

---

## Masalah Khusus Sesi 04

### Konfigurasi Port Salah

**Masalah:** Notebook terhubung ke port yang salah (55769 vs 59959 vs 57127)

**Solusi:**

1. Periksa port mana yang digunakan Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Perbarui Sel 10 di notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Restart kernel dan jalankan ulang sel 6, 8, 10, 12, 16, 20, 22

---

### Pemilihan Model Salah

**Masalah:** Notebook menunjukkan gpt-oss-20b atau qwen2.5-7b alih-alih qwen2.5-3b

**Solusi:**

1. Restart kernel notebook (membersihkan status variabel lama)
2. Jalankan ulang Sel 10 (Set Model Aliases)
3. Jalankan ulang Sel 12 (Tampilkan Konfigurasi)
4. **Verifikasi:** Sel 12 harus menunjukkan `LLM Model: qwen2.5-3b`

---

### Sel Diagnostik Gagal

**Masalah:** Sel 16 menunjukkan "❌ Foundry Local service not found!"

**Solusi:**

1. Verifikasi layanan berjalan:
```bash
foundry service status
```

2. Uji endpoint secara manual:
```bash
curl http://localhost:59959/v1/models
```

3. Jika curl berfungsi tetapi notebook tidak:
   - Restart kernel notebook
   - Jalankan ulang sel secara berurutan: 6, 8, 10, 12, 14, 16

4. Jika curl gagal:
   - Mulai layanan: `foundry service start`
   - Muat model: `foundry model run phi-4-mini` dan `foundry model run qwen2.5-3b`

---

### Pemeriksaan Awal Gagal

**Masalah:** Sel 20 menunjukkan kesalahan koneksi meskipun diagnostik berhasil

**Solusi:**

1. Periksa model sudah dimuat:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Jika model hilang:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Jalankan ulang Sel 20 setelah model dimuat

---

### Perbandingan Gagal dengan Nilai None

**Masalah:** Sel 22 selesai tetapi menunjukkan latensi sebagai None

**Solusi:**

1. Periksa bahwa pemeriksaan awal berhasil terlebih dahulu (Sel 20)
2. Jalankan ulang Sel 22 - model mungkin perlu pemanasan pada permintaan pertama
3. Verifikasi kedua model sudah dimuat: `foundry model ls`

---

## Masalah Khusus Sesi 05

### Agen Menggunakan Model yang Salah

**Masalah:** Agen tidak menggunakan model yang diharapkan

**Solusi:**

Verifikasi konfigurasi:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Restart kernel jika model tidak benar.

---

### Overflow Konteks Memori

**Masalah:** Respons agen menurun seiring waktu

**Solusi:** Sudah ditangani secara otomatis - agen hanya menyimpan 6 pesan terakhir dalam memori.

---

## Masalah Khusus Sesi 06

### Kebingungan Model CPU vs GPU

**Masalah:** Mendapatkan kesalahan CUDA saat menggunakan konfigurasi default

**Solusi:** Konfigurasi default sekarang menggunakan model CPU. Jika Anda melihat kesalahan CUDA:

1. Verifikasi Anda menggunakan katalog CPU default:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Restart kernel dan jalankan ulang semua sel

---

### Deteksi Intent Tidak Berfungsi

**Masalah:** Prompt diarahkan ke model yang salah

**Solusi:**

Uji deteksi intent:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Perbarui RULES jika pola perlu disesuaikan.

---

## Masalah Khusus Perangkat Keras

### NVIDIA GPU

**Periksa Status GPU:**
```bash
nvidia-smi
```

**Masalah Umum:**
- **Driver usang**: Perbarui driver NVIDIA
- **Ketidaksesuaian versi CUDA**: Instal ulang Foundry Local
- **Memori GPU terfragmentasi**: Restart sistem

### Qualcomm NPU

**Periksa Status NPU:**
```bash
foundry device info
```

**Masalah Umum:**
- **Driver NPU tidak terinstal**: Instal driver Qualcomm NPU
- **Varian NPU tidak tersedia**: Gunakan varian CPU
- **Versi Windows terlalu lama**: Perbarui ke Windows 11 terbaru

### Sistem Hanya CPU

**Model yang Direkomendasikan:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Tips Performa:**
- Gunakan model terkecil
- Kurangi max_tokens
- Tingkatkan kesabaran untuk permintaan pertama

---

## Perintah Diagnostik

### Periksa Semua
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### Dalam Python
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## Mendapatkan Bantuan

### 1. Periksa Log
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. Masalah GitHub
- Cari masalah yang ada: https://github.com/microsoft/Foundry-Local/issues
- Buat masalah baru dengan:
  - Pesan kesalahan (teks lengkap)
  - Output dari `foundry service status`
  - Output dari `foundry --version`
  - Info GPU/NPU (nvidia-smi, dll.)
  - Langkah-langkah untuk mereproduksi

### 3. Dokumentasi
- **Repositori Utama**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referensi CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Pemecahan Masalah**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Daftar Perbaikan Cepat

Ketika terjadi masalah, coba langkah-langkah ini secara berurutan:

- [ ] Periksa layanan berjalan: `foundry service status`
- [ ] Restart layanan: `foundry service stop && foundry service start`
- [ ] Verifikasi model ada: `foundry model ls | grep phi-4-mini`
- [ ] Muat model yang diperlukan: `foundry model run phi-4-mini`
- [ ] Periksa memori GPU: `nvidia-smi` (jika NVIDIA)
- [ ] Coba varian CPU: Gunakan `phi-4-mini-cpu` alih-alih `phi-4-mini`
- [ ] Restart kernel notebook
- [ ] Bersihkan output notebook dan jalankan ulang semua sel
- [ ] Instal ulang SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Restart sistem (upaya terakhir)

---

## Tips Pencegahan

### Praktik Terbaik

1. **Selalu periksa layanan terlebih dahulu:**
   ```bash
   foundry service status
   ```

2. **Gunakan varian CPU secara default:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Muat model sebelum menjalankan notebook:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Biarkan layanan berjalan:**
   - Jangan hentikan/mulai layanan secara tidak perlu
   - Biarkan berjalan di latar belakang antara sesi

5. **Pantau sumber daya:**
   - Periksa memori GPU sebelum menjalankan
   - Tutup aplikasi GPU yang tidak diperlukan
   - Gunakan Task Manager / nvidia-smi

6. **Perbarui secara berkala:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Terakhir Diperbarui:** 8 Oktober 2025

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.