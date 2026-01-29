# Sesi 6: Foundry Lokal – Model sebagai Alat

## Abstrak

Perlakukan model sebagai alat yang dapat dikomposisi di dalam lapisan operasi AI lokal. Sesi ini menunjukkan cara menghubungkan beberapa panggilan SLM/LLM khusus, mengarahkan tugas secara selektif, dan menyediakan permukaan SDK terpadu untuk aplikasi. Anda akan membangun router model ringan + perencana tugas, mengintegrasikannya ke dalam skrip aplikasi, dan merancang jalur skala ke Azure AI Foundry untuk beban kerja produksi.

## Tujuan Pembelajaran

- **Memahami** model sebagai alat atom dengan kemampuan yang dideklarasikan
- **Mengalihkan** permintaan berdasarkan niat / penilaian heuristik
- **Menghubungkan** output dalam tugas multi-langkah (uraikan → selesaikan → perbaiki)
- **Mengintegrasikan** API klien terpadu untuk aplikasi hilir
- **Menskalakan** desain ke cloud (kontrak kompatibel OpenAI yang sama)

## Prasyarat

- Sesi 1–5 selesai
- Beberapa model lokal telah di-cache (misalnya, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Cuplikan Lingkungan Lintas Platform

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Akses layanan Remote/VM dari macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Alur Demo (30 menit)

### 1. Deklarasi Kemampuan Alat (5 menit)

Buat `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Deteksi Niat & Pengalihan (8 menit)

Buat `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Penghubungan Tugas Multi-Langkah (7 menit)

Buat `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Proyek Awal: Adaptasi `06-models-as-tools` (5 menit)

Peningkatan:
- Tambahkan dukungan token streaming (pembaruan UI progresif)
- Tambahkan penilaian kepercayaan: tumpang tindih leksikal atau rubrik prompt
- Ekspor JSON jejak (niat → model → latensi → penggunaan token)
- Implementasikan penggunaan ulang cache untuk sublangkah yang berulang

### 5. Jalur Skala ke Azure (5 menit)

| Lapisan | Lokal (Foundry) | Cloud (Azure AI Foundry) | Strategi Transisi |
|---------|-----------------|--------------------------|---------------------|
| Pengalihan | Python Heuristik | Mikroservis yang tahan lama | Containerize & deploy API |
| Model | SLMs di-cache | Penerapan yang dikelola | Peta nama lokal ke ID penerapan |
| Observabilitas | Statistik CLI/manual | Logging & metrik terpusat | Tambahkan peristiwa jejak terstruktur |
| Keamanan | Hanya host lokal | Autentikasi Azure / jaringan | Perkenalkan key vault untuk rahasia |
| Biaya | Sumber daya perangkat | Penagihan konsumsi | Tambahkan pengendali anggaran |

## Daftar Periksa Validasi

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Harapkan pemilihan model berbasis niat dan output akhir yang telah diperbaiki.

## Pemecahan Masalah

| Masalah | Penyebab | Solusi |
|---------|----------|--------|
| Semua tugas dialihkan ke model yang sama | Aturan lemah | Perkaya set regex INTENT_RULES |
| Pipeline gagal di tengah langkah | Model yang dimuat hilang | Jalankan `foundry model run <model>` |
| Kohesi output rendah | Tidak ada fase perbaikan | Tambahkan langkah peringkasan/pemvalidasian |

## Referensi

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Dokumentasi Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Pola Kualitas Prompt: Lihat Sesi 2

---

**Durasi Sesi**: 30 menit  
**Tingkat Kesulitan**: Ahli

## Skenario Contoh & Pemetaan Workshop

| Skrip Workshop / Notebook | Skenario | Tujuan | Sumber Dataset / Katalog |
|----------------------------|----------|--------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Asisten pengembang yang menangani prompt niat campuran (refactor, ringkasan, klasifikasi) | Pengalihan alias model berbasis niat heuristik dengan penggunaan token | `CATALOG` inline + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Perencanaan multi-langkah & perbaikan untuk tugas bantuan pengkodean kompleks | Uraikan → eksekusi khusus → langkah perbaikan peringkasan | `CATALOG` yang sama; langkah-langkah berasal dari output rencana |

### Narasi Skenario
Alat produktivitas teknik menerima tugas heterogen: refactor kode, ringkasan catatan arsitektur, klasifikasi umpan balik. Untuk meminimalkan latensi & penggunaan sumber daya, model umum kecil merencanakan dan merangkum, model khusus kode menangani refactor, dan model klasifikasi ringan melabeli umpan balik. Skrip pipeline menunjukkan penghubungan + perbaikan; skrip router mengisolasi pengalihan satu-prompt adaptif.

### Cuplikan Katalog
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Contoh Prompt Uji
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Ekstensi Jejak (Opsional)
Tambahkan baris JSON jejak per langkah untuk `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heuristik Eskalasi (Ide)
Jika rencana berisi kata kunci seperti "optimalkan", "keamanan", atau panjang langkah > 280 karakter → eskalasi ke model yang lebih besar (misalnya, `gpt-oss-20b`) hanya untuk langkah tersebut.

### Peningkatan Opsional

| Area | Peningkatan | Nilai | Petunjuk |
|------|-------------|-------|----------|
| Caching | Gunakan kembali objek manajer + klien | Latensi lebih rendah, overhead lebih sedikit | Gunakan `workshop_utils.get_client` |
| Metrik Penggunaan | Tangkap token & latensi per langkah | Profiling & optimasi | Waktu setiap panggilan yang dialihkan; simpan dalam daftar jejak |
| Pengalihan Adaptif | Kesadaran kepercayaan / biaya | Perdagangan kualitas-biaya yang lebih baik | Tambahkan penilaian: jika prompt > N karakter atau regex cocok dengan domain → eskalasi ke model yang lebih besar |
| Registri Kemampuan Dinamis | Katalog muat ulang langsung | Tidak perlu restart redeploy | Muat `catalog.json` saat runtime; pantau stempel waktu file |
| Strategi Cadangan | Ketahanan saat kegagalan | Ketersediaan lebih tinggi | Coba utama → pada pengecualian alias cadangan |
| Pipeline Streaming | Umpan balik awal | Peningkatan UX | Streaming setiap langkah dan buffer input perbaikan akhir |
| Embedding Niat Vektor | Pengalihan lebih bernuansa | Akurasi niat lebih tinggi | Embed prompt, cluster & peta centroid → kemampuan |
| Ekspor Jejak | Rantai yang dapat diaudit | Kepatuhan/pelaporan | Emit baris JSON: langkah, niat, model, latensi_ms, token |
| Simulasi Biaya | Estimasi pra-cloud | Perencanaan anggaran | Tetapkan biaya/token notional per model & agregat per tugas |
| Mode Deterministik | Repro reproduktibilitas | Benchmarking stabil | Env: `temperature=0`, jumlah langkah tetap |

#### Contoh Struktur Jejak

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Sketsa Eskalasi Adaptif

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Muat Ulang Katalog Model

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.