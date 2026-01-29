# Buku Panduan Pantas - Buku Nota Bengkel

## Kandungan

- [Prasyarat](../../../../Workshop/notebooks)
- [Persediaan Awal](../../../../Workshop/notebooks)
- [Sesi 04: Perbandingan Model](../../../../Workshop/notebooks)
- [Sesi 05: Orkestrator Multi-Ejen](../../../../Workshop/notebooks)
- [Sesi 06: Penghalaan Model Berdasarkan Niat](../../../../Workshop/notebooks)
- [Pembolehubah Persekitaran](../../../../Workshop/notebooks)
- [Perintah Biasa](../../../../Workshop/notebooks)

---

## Prasyarat

### 1. Pasang Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Sahkan Pemasangan:**
```bash
foundry --version
```

### 2. Pasang Kebergantungan Python

```bash
cd Workshop
pip install -r requirements.txt
```

Atau pasang secara individu:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Persediaan Awal

### Mulakan Perkhidmatan Foundry Local

**Diperlukan sebelum menjalankan sebarang buku nota:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Output yang dijangka:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Muat Turun dan Muatkan Model

Buku nota menggunakan model berikut secara lalai:

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

### Sahkan Persediaan

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sesi 04: Perbandingan Model

### Tujuan
Bandingkan prestasi antara Model Bahasa Kecil (SLM) dan Model Bahasa Besar (LLM).

### Persediaan Pantas

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Menjalankan Buku Nota

1. **Buka** `session04_model_compare.ipynb` dalam VS Code atau Jupyter
2. **Mulakan semula kernel** (Kernel → Restart Kernel)
3. **Jalankan semua sel** mengikut urutan

### Konfigurasi Utama

**Model Lalai:**
- **SLM:** `phi-4-mini` (~4GB RAM, lebih pantas)
- **LLM:** `qwen2.5-3b` (~3GB RAM, dioptimumkan untuk memori)

**Pembolehubah Persekitaran (pilihan):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Output yang Dijangka

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

### Penyesuaian

**Gunakan model lain:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Prompt tersuai:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Senarai Semak Pengesahan

- [ ] Sel 12 menunjukkan model yang betul (phi-4-mini, qwen2.5-3b)
- [ ] Sel 12 menunjukkan titik akhir yang betul (port 59959)
- [ ] Diagnostik Sel 16 lulus (✅ Perkhidmatan sedang berjalan)
- [ ] Pemeriksaan awal Sel 20 lulus (kedua-dua model ok)
- [ ] Perbandingan Sel 22 selesai dengan nilai kependaman
- [ ] Pengesahan Sel 24 menunjukkan 🎉 SEMUA SEMAKAN LULUS!

### Anggaran Masa
- **Larian pertama:** 5-10 minit (termasuk muat turun model)
- **Larian seterusnya:** 1-2 minit

---

## Sesi 05: Orkestrator Multi-Ejen

### Tujuan
Menunjukkan kerjasama multi-ejen menggunakan Foundry Local SDK - ejen bekerjasama untuk menghasilkan output yang diperhalusi.

### Persediaan Pantas

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Menjalankan Buku Nota

1. **Buka** `session05_agents_orchestrator.ipynb`
2. **Mulakan semula kernel**
3. **Jalankan semua sel** mengikut urutan

### Konfigurasi Utama

**Persediaan Lalai (Model Sama untuk Kedua-dua Ejen):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Persediaan Lanjutan (Model Berbeza):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Seni Bina

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

### Output yang Dijangka

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

### Sambungan

**Tambah lebih banyak ejen:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Ujian kelompok:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Anggaran Masa
- **Larian pertama:** 3-5 minit
- **Larian seterusnya:** 1-2 minit setiap soalan

---

## Sesi 06: Penghalaan Model Berdasarkan Niat

### Tujuan
Menghala prompt secara bijak kepada model khusus berdasarkan niat yang dikesan.

### Persediaan Pantas

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Nota:** Sesi 06 menggunakan model CPU secara lalai untuk keserasian maksimum.

### Menjalankan Buku Nota

1. **Buka** `session06_models_router.ipynb`
2. **Mulakan semula kernel**
3. **Jalankan semua sel** mengikut urutan

### Konfigurasi Utama

**Katalog Lalai (Model CPU):**
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

### Pengesanan Niat

Router menggunakan corak regex untuk mengesan niat:

| Niat | Contoh Corak | Dihala Ke |
|------|--------------|-----------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Semua yang lain | phi-4-mini-cpu |

### Output yang Dijangka

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

### Penyesuaian

**Tambah niat tersuai:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Aktifkan penjejakan token:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Beralih ke Model GPU

Jika anda mempunyai VRAM 8GB+:

1. Dalam **Sel #6**, komen katalog CPU
2. Nyahkomen katalog GPU
3. Muatkan model GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Mulakan semula kernel dan jalankan semula buku nota

### Anggaran Masa
- **Larian pertama:** 5-10 minit (pemuatan model)
- **Larian seterusnya:** 30-60 saat setiap ujian

---

## Pembolehubah Persekitaran

### Konfigurasi Global

Tetapkan sebelum memulakan Jupyter/VS Code:

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

### Konfigurasi Dalam Buku Nota

Tetapkan pada permulaan mana-mana buku nota:

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

## Perintah Biasa

### Pengurusan Perkhidmatan

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

### Pengurusan Model

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

### Ujian Titik Akhir

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

## Amalan Terbaik

### Sebelum Memulakan Sebarang Buku Nota

1. **Periksa perkhidmatan sedang berjalan:**
   ```bash
   foundry service status
   ```

2. **Sahkan model dimuatkan:**
   ```bash
   foundry model ls
   ```

3. **Mulakan semula kernel buku nota** jika menjalankan semula

4. **Kosongkan semua output** untuk larian bersih

### Pengurusan Sumber

1. **Gunakan model CPU secara lalai** untuk keserasian
2. **Beralih ke model GPU** hanya jika anda mempunyai VRAM 8GB+
3. **Tutup aplikasi GPU lain** sebelum menjalankan
4. **Pastikan perkhidmatan berjalan** antara sesi buku nota
5. **Pantau penggunaan sumber** dengan Task Manager / nvidia-smi

### Penyelesaian Masalah

1. **Sentiasa periksa perkhidmatan dahulu** sebelum menyahpepijat kod
2. **Mulakan semula kernel** jika anda melihat konfigurasi lama
3. **Jalankan semula sel diagnostik** selepas sebarang perubahan
4. **Periksa nama model** sepadan dengan yang dimuatkan
5. **Sahkan port titik akhir** sepadan dengan status perkhidmatan

---

## Rujukan Pantas: Alias Model

### Model Biasa

| Alias | Saiz | Terbaik Untuk | RAM/VRAM | Varian |
|-------|------|---------------|----------|--------|
| `phi-4-mini` | ~4B | Sembang umum, ringkasan | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Penjanaan kod, penstrukturan semula | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Tugas umum, cekap | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Pantas, sumber rendah | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Pengelasan, sumber minimum | 1-2GB | `-cpu`, `-cuda-gpu` |

### Penamaan Varian

- **Nama asas** (contoh: `phi-4-mini`): Memilih varian terbaik secara automatik untuk perkakasan anda
- **`-cpu`**: Dioptimumkan untuk CPU, berfungsi di mana-mana
- **`-cuda-gpu`**: Dioptimumkan untuk GPU NVIDIA, memerlukan VRAM 8GB+
- **`-npu`**: Dioptimumkan untuk Qualcomm NPU, memerlukan pemacu NPU

**Cadangan:** Gunakan nama asas (tanpa akhiran) dan biarkan Foundry Local memilih varian terbaik secara automatik.

---

## Petunjuk Kejayaan

Anda bersedia apabila anda melihat:

✅ `foundry service status` menunjukkan "running"
✅ `foundry model ls` menunjukkan model yang diperlukan
✅ Perkhidmatan boleh diakses di titik akhir yang betul
✅ Pemeriksaan kesihatan mengembalikan 200 OK
✅ Sel diagnostik buku nota lulus
✅ Tiada ralat sambungan dalam output

---

## Mendapatkan Bantuan

### Dokumentasi
- **Repositori Utama**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rujukan CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Penyelesaian Masalah**: Lihat `troubleshooting.md` dalam direktori ini

### Isu GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Tarikh Dikemas Kini:** 8 Oktober 2025  
**Versi:** Buku Nota Bengkel 2.0

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.