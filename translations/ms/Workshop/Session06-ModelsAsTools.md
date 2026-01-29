# Sesi 6: Foundry Local – Model Sebagai Alat

## Abstrak

Anggap model sebagai alat yang boleh digabungkan dalam lapisan operasi AI tempatan. Sesi ini menunjukkan cara untuk menghubungkan beberapa panggilan SLM/LLM khusus, mengarahkan tugas secara selektif, dan mendedahkan permukaan SDK yang disatukan kepada aplikasi. Anda akan membina router model ringan + perancang tugas, mengintegrasikannya ke dalam skrip aplikasi, dan menggariskan laluan penskalaan ke Azure AI Foundry untuk beban kerja pengeluaran.

## Objektif Pembelajaran

- **Konsepsikan** model sebagai alat atomik dengan keupayaan yang diisytiharkan
- **Arahkan** permintaan berdasarkan niat / penilaian heuristik
- **Rantai** output merentasi tugas berbilang langkah (pecahkan → selesaikan → perbaiki)
- **Integrasikan** API klien bersatu untuk aplikasi hiliran
- **Skalakan** reka bentuk ke awan (kontrak serasi OpenAI yang sama)

## Prasyarat

- Sesi 1–5 telah diselesaikan
- Beberapa model tempatan telah di-cache (contohnya, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Petikan Persekitaran Merentas Platform

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

Akses perkhidmatan Jauh/VM dari macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Aliran Demo (30 minit)

### 1. Pengisytiharan Keupayaan Alat (5 minit)

Cipta `samples/06-tools/models_catalog.py`:

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


### 2. Pengesanan Niat & Penghalaan (8 minit)

Cipta `samples/06-tools/router.py`:

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


### 3. Rantaian Tugas Berbilang Langkah (7 minit)

Cipta `samples/06-tools/pipeline.py`:

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


### 4. Projek Permulaan: Sesuaikan `06-models-as-tools` (5 minit)

Penambahbaikan:
- Tambah sokongan token penstriman (kemas kini UI progresif)
- Tambah penilaian keyakinan: pertindihan leksikal atau rubrik prompt
- Eksport JSON jejak (niat → model → latensi → penggunaan token)
- Laksanakan penggunaan semula cache untuk sublangkah berulang

### 5. Laluan Penskalaan ke Azure (5 minit)

| Lapisan | Tempatan (Foundry) | Awan (Azure AI Foundry) | Strategi Peralihan |
|---------|---------------------|-------------------------|---------------------|
| Penghalaan | Python Heuristik | Perkhidmatan mikro tahan lama | Bekas & gunakan API |
| Model | SLMs di-cache | Penggunaan terurus | Peta nama tempatan ke ID penggunaan |
| Pemerhatian | Statistik CLI/manual | Log pusat & metrik | Tambah acara jejak berstruktur |
| Keselamatan | Hanya hos tempatan | Pengesahan Azure / rangkaian | Perkenalkan peti kunci untuk rahsia |
| Kos | Sumber peranti | Penagihan penggunaan | Tambah pengawal belanjawan |

## Senarai Semak Pengesahan

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Jangka pemilihan model berdasarkan niat dan output akhir yang diperbaiki.

## Penyelesaian Masalah

| Masalah | Punca | Penyelesaian |
|---------|-------|--------------|
| Semua tugas diarahkan ke model yang sama | Peraturan lemah | Perkayakan set regex INTENT_RULES |
| Saluran gagal di pertengahan langkah | Model tidak dimuatkan | Jalankan `foundry model run <model>` |
| Kohesi output rendah | Tiada fasa pembaikan | Tambah langkah ringkasan/pengesahan |

## Rujukan

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Dokumen Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Corak Kualiti Prompt: Lihat Sesi 2

---

**Tempoh Sesi**: 30 minit  
**Kesukaran**: Pakar

## Senario Contoh & Pemetaan Bengkel

| Skrip / Buku Nota Bengkel | Senario | Objektif | Sumber Dataset / Katalog |
|---------------------------|---------|----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Pembantu pemaju yang mengendalikan prompt niat campuran (refaktor, ringkasan, klasifikasi) | Penghalaan niat heuristik → alias model dengan penggunaan token | `CATALOG` sebaris + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Perancangan & pembaikan berbilang langkah untuk tugas bantuan pengekodan kompleks | Pecahkan → pelaksanaan khusus → langkah pembaikan ringkasan | `CATALOG` yang sama; langkah-langkah diperoleh daripada output pelan |

### Naratif Senario
Alat produktiviti kejuruteraan menerima tugas heterogen: refaktor kod, ringkaskan nota seni bina, klasifikasikan maklum balas. Untuk meminimumkan latensi & penggunaan sumber, model umum kecil merancang dan meringkaskan, model khusus kod mengendalikan refaktor, dan model ringan yang mampu mengklasifikasikan melabelkan maklum balas. Skrip saluran menunjukkan rantaian + pembaikan; skrip penghala mengasingkan penghalaan prompt tunggal adaptif.

### Snapshot Katalog
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Contoh Prompt Ujian
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Sambungan Jejak (Pilihan)
Tambah baris JSON jejak per langkah untuk `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heuristik Eskalasi (Idea)
Jika pelan mengandungi kata kunci seperti "optimumkan", "keselamatan", atau panjang langkah > 280 aksara → eskalasi ke model lebih besar (contohnya, `gpt-oss-20b`) untuk langkah itu sahaja.

### Penambahbaikan Pilihan

| Kawasan | Penambahbaikan | Nilai | Petunjuk |
|---------|----------------|-------|----------|
| Cache | Penggunaan semula objek pengurus + klien | Latensi lebih rendah, kurang overhead | Gunakan `workshop_utils.get_client` |
| Metrik Penggunaan | Tangkap token & latensi per langkah | Profiling & pengoptimuman | Ukur setiap panggilan yang diarahkan; simpan dalam senarai jejak |
| Penghalaan Adaptif | Keyakinan / kesedaran kos | Perdagangan kualiti-kos yang lebih baik | Tambah penilaian: jika prompt > N aksara atau regex sepadan domain → eskalasi ke model lebih besar |
| Pendaftaran Keupayaan Dinamik | Katalog muat semula panas | Tiada keperluan untuk memulakan semula | Muatkan `catalog.json` semasa runtime; pantau cap masa fail |
| Strategi Sandaran | Ketahanan semasa kegagalan | Ketersediaan lebih tinggi | Cuba utama → pada pengecualian alias sandaran |
| Saluran Penstriman | Maklum balas awal | Penambahbaikan UX | Alirkan setiap langkah dan penampan input pembaikan akhir |
| Vektor Embedding Niat | Penghalaan lebih halus | Ketepatan niat lebih tinggi | Embed prompt, kluster & peta centroid → keupayaan |
| Eksport Jejak | Rantaian boleh diaudit | Pematuhan/pelaporan | Emit baris JSON: langkah, niat, model, latensi_ms, token |
| Simulasi Kos | Anggaran pra-awan | Perancangan belanjawan | Tetapkan kos/tokens notional per model & agregat per tugas |
| Mod Deterministik | Repro reprodusibiliti | Penanda aras stabil | Env: `temperature=0`, kiraan langkah tetap |

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


#### Lakaran Eskalasi Adaptif

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Muat Semula Panas Katalog Model

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
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.