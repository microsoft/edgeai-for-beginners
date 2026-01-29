# Buku Panduan Bengkel - Panduan Penyelesaian Masalah

## Kandungan

- [Isu dan Penyelesaian Umum](../../../../Workshop/notebooks)
- [Isu Khusus Sesi 04](../../../../Workshop/notebooks)
- [Isu Khusus Sesi 05](../../../../Workshop/notebooks)
- [Isu Khusus Sesi 06](../../../../Workshop/notebooks)
- [Isu Khusus Perkakasan](../../../../Workshop/notebooks)
- [Perintah Diagnostik](../../../../Workshop/notebooks)
- [Mendapatkan Bantuan](../../../../Workshop/notebooks)

---

## Isu dan Penyelesaian Umum

### 🔴 CUDA Out of Memory

**Mesej Ralat:**
```
CUDA failure 2: out of memory
```

**Punca Utama:** GPU tidak mempunyai VRAM yang mencukupi untuk memuatkan model.

**Penyelesaian:**

#### Pilihan 1: Gunakan Varian CPU (Disyorkan)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Pilihan 2: Gunakan Model Lebih Kecil pada GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Pilihan 3: Kosongkan Memori GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Pilihan 4: Tingkatkan Memori GPU (jika boleh)
- Tutup tab pelayar, editor video, atau aplikasi GPU lain
- Kurangkan kesan visual Windows
- Gunakan GPU khusus jika anda mempunyai GPU bersepadu + khusus

---

### 🔴 APIConnectionError: Connection Error

**Mesej Ralat:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Punca Utama:** Perkhidmatan Foundry Local tidak berjalan atau tidak boleh diakses.

**Penyelesaian:**

#### Langkah 1: Periksa Status Perkhidmatan
```bash
foundry service status
```

#### Langkah 2: Mulakan Perkhidmatan jika Dihentikan
```bash
foundry service start
```

#### Langkah 3: Sahkan Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Langkah 4: Muatkan Model yang Diperlukan
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Langkah 5: Mulakan Semula Kernel Notebook
Selepas memulakan perkhidmatan dan memuatkan model, mulakan semula kernel notebook dan jalankan semula semua sel.

---

### 🔴 Model Tidak Ditemui dalam Katalog

**Mesej Ralat:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Punca Utama:** Model tidak dimuat turun atau dimuatkan dalam Foundry Local.

**Penyelesaian:**

#### Pilihan 1: Muat Turun dan Muatkan Model
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

#### Pilihan 2: Gunakan Mod Pemilihan Automatik
Kemas kini CATALOG anda untuk menggunakan nama model asas (tanpa akhiran `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

SDK Foundry Local akan secara automatik memilih varian terbaik (CPU, GPU, atau NPU) untuk perkakasan anda.

---

### 🔴 HttpResponseError: 500 - Gagal Memuatkan Model

**Mesej Ralat:**
```
HttpResponseError: 500 - Failed loading model
```

**Punca Utama:** Fail model rosak atau tidak serasi dengan perkakasan.

**Penyelesaian:**

#### Muat Turun Semula Model
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Gunakan Varian Berbeza
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Mesej Ralat:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Punca Utama:** Pakej foundry-local-sdk tidak dipasang.

**Penyelesaian:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Permintaan Pertama Perlahan

**Simptom:** Penyelesaian pertama mengambil masa lebih daripada 30 saat, permintaan seterusnya lebih pantas.

**Punca Utama:** Ini adalah tingkah laku biasa - perkhidmatan sedang memuatkan model ke dalam memori pada permintaan pertama.

**Penyelesaian:**

#### Muatkan Model Awal
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Biarkan Perkhidmatan Berjalan
```bash
# Start service manually and leave it running
foundry service start
```

---

## Isu Khusus Sesi 04

### Konfigurasi Port Salah

**Isu:** Notebook menyambung ke port yang salah (55769 vs 59959 vs 57127)

**Penyelesaian:**

1. Periksa port mana yang digunakan oleh Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Kemas kini Sel 10 dalam notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Mulakan semula kernel dan jalankan semula sel 6, 8, 10, 12, 16, 20, 22

---

### Pemilihan Model Salah

**Isu:** Notebook menunjukkan gpt-oss-20b atau qwen2.5-7b bukannya qwen2.5-3b

**Penyelesaian:**

1. Mulakan semula kernel notebook (membersihkan keadaan pembolehubah lama)
2. Jalankan semula Sel 10 (Tetapkan Alias Model)
3. Jalankan semula Sel 12 (Paparkan Konfigurasi)
4. **Sahkan:** Sel 12 harus menunjukkan `LLM Model: qwen2.5-3b`

---

### Sel Diagnostik Gagal

**Isu:** Sel 16 menunjukkan "❌ Foundry Local service not found!"

**Penyelesaian:**

1. Sahkan perkhidmatan sedang berjalan:
```bash
foundry service status
```

2. Uji endpoint secara manual:
```bash
curl http://localhost:59959/v1/models
```

3. Jika curl berfungsi tetapi notebook tidak:
   - Mulakan semula kernel notebook
   - Jalankan semula sel mengikut urutan: 6, 8, 10, 12, 14, 16

4. Jika curl gagal:
   - Mulakan perkhidmatan: `foundry service start`
   - Muatkan model: `foundry model run phi-4-mini` dan `foundry model run qwen2.5-3b`

---

### Pemeriksaan Awal Gagal

**Isu:** Sel 20 menunjukkan ralat sambungan walaupun diagnostik lulus

**Penyelesaian:**

1. Periksa model telah dimuatkan:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Jika model tiada:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Jalankan semula Sel 20 selepas model dimuatkan

---

### Perbandingan Gagal dengan Nilai None

**Isu:** Sel 22 selesai tetapi menunjukkan latensi sebagai None

**Penyelesaian:**

1. Periksa bahawa pemeriksaan awal lulus dahulu (Sel 20)
2. Jalankan semula Sel 22 - model mungkin perlu dipanaskan pada permintaan pertama
3. Sahkan kedua-dua model telah dimuatkan: `foundry model ls`

---

## Isu Khusus Sesi 05

### Ejen Menggunakan Model Salah

**Isu:** Ejen tidak menggunakan model yang dijangka

**Penyelesaian:**

Sahkan konfigurasi:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Mulakan semula kernel jika model tidak betul.

---

### Lebihan Konteks Memori

**Isu:** Respons ejen semakin merosot dari masa ke masa

**Penyelesaian:** Sudah ditangani secara automatik - ejen hanya menyimpan 6 mesej terakhir dalam memori.

---

## Isu Khusus Sesi 06

### Kekeliruan Model CPU vs GPU

**Isu:** Mendapat ralat CUDA apabila menggunakan konfigurasi lalai

**Penyelesaian:** Konfigurasi lalai kini menggunakan model CPU. Jika anda melihat ralat CUDA:

1. Sahkan anda menggunakan katalog CPU lalai:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Mulakan semula kernel dan jalankan semula semua sel

---

### Pengesanan Niat Tidak Berfungsi

**Isu:** Prompt dihantar ke model yang salah

**Penyelesaian:**

Uji pengesanan niat:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Kemas kini RULES jika corak perlu disesuaikan.

---

## Isu Khusus Perkakasan

### GPU NVIDIA

**Periksa Status GPU:**
```bash
nvidia-smi
```

**Isu Umum:**
- **Pemacu ketinggalan zaman**: Kemas kini pemacu NVIDIA
- **Ketidakpadanan versi CUDA**: Pasang semula Foundry Local
- **Memori GPU terpecah-pecah**: Mulakan semula sistem

### Qualcomm NPU

**Periksa Status NPU:**
```bash
foundry device info
```

**Isu Umum:**
- **Pemacu NPU tidak dipasang**: Pasang pemacu Qualcomm NPU
- **Varian NPU tidak tersedia**: Gunakan varian CPU
- **Versi Windows terlalu lama**: Kemas kini ke Windows 11 terkini

### Sistem Hanya CPU

**Model Disyorkan:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Tip Prestasi:**
- Gunakan model terkecil
- Kurangkan max_tokens
- Tingkatkan kesabaran untuk permintaan pertama

---

## Perintah Diagnostik

### Periksa Segalanya
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

### 2. Isu GitHub
- Cari isu sedia ada: https://github.com/microsoft/Foundry-Local/issues
- Buat isu baru dengan:
  - Mesej ralat (teks penuh)
  - Output `foundry service status`
  - Output `foundry --version`
  - Info GPU/NPU (nvidia-smi, dll.)
  - Langkah untuk menghasilkan semula

### 3. Dokumentasi
- **Repositori Utama**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rujukan CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Penyelesaian Masalah**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Senarai Semak Penyelesaian Cepat

Apabila berlaku masalah, cuba langkah berikut mengikut urutan:

- [ ] Periksa perkhidmatan sedang berjalan: `foundry service status`
- [ ] Mulakan semula perkhidmatan: `foundry service stop && foundry service start`
- [ ] Sahkan model wujud: `foundry model ls | grep phi-4-mini`
- [ ] Muatkan model yang diperlukan: `foundry model run phi-4-mini`
- [ ] Periksa memori GPU: `nvidia-smi` (jika NVIDIA)
- [ ] Cuba varian CPU: Gunakan `phi-4-mini-cpu` bukannya `phi-4-mini`
- [ ] Mulakan semula kernel notebook
- [ ] Kosongkan output notebook dan jalankan semula semua sel
- [ ] Pasang semula SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Mulakan semula sistem (pilihan terakhir)

---

## Tip Pencegahan

### Amalan Terbaik

1. **Sentiasa periksa perkhidmatan dahulu:**
   ```bash
   foundry service status
   ```

2. **Gunakan varian CPU secara lalai:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Muatkan model sebelum menjalankan notebook:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Biarkan perkhidmatan berjalan:**
   - Jangan hentikan/mulakan perkhidmatan tanpa perlu
   - Biarkan ia berjalan di latar belakang antara sesi

5. **Pantau sumber:**
   - Periksa memori GPU sebelum menjalankan
   - Tutup aplikasi GPU yang tidak diperlukan
   - Gunakan Task Manager / nvidia-smi

6. **Kemas kini secara berkala:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Kemas Kini Terakhir:** 8 Oktober 2025

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.