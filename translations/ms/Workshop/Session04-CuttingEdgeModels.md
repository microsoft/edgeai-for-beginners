# Sesi 4: Terokai Model Terkini – LLM, SLM & Inferens Peranti

## Abstrak

Bandingkan Model Bahasa Besar (LLM) dan Model Bahasa Kecil (SLM) untuk senario inferens tempatan vs awan. Pelajari corak pengedaran menggunakan pecutan ONNX Runtime, pelaksanaan WebGPU, dan pengalaman hibrid RAG. Termasuk demo Chainlit RAG dengan model tempatan serta eksplorasi OpenWebUI pilihan. Anda akan menyesuaikan permulaan inferens WebGPU dan menilai keupayaan Phi vs GPT-OSS-20B serta pertimbangan kos/prestasi.

## Objektif Pembelajaran

- **Bandingkan** SLM vs LLM berdasarkan latensi, memori, dan kualiti
- **Sebarkan** model dengan ONNXRuntime dan (jika disokong) WebGPU
- **Jalankan** inferens berasaskan pelayar (demo interaktif yang melindungi privasi)
- **Integrasikan** saluran Chainlit RAG dengan backend SLM tempatan
- **Nilai** menggunakan heuristik kualiti + kos yang ringan

## Prasyarat

- Sesi 1–3 selesai
- `chainlit` dipasang (sudah ada dalam `requirements.txt` untuk Modul08)
- Pelayar yang menyokong WebGPU (Edge / Chrome terkini pada Windows 11)
- Foundry Local berjalan (`foundry service status`)

### Nota Lintas Platform

Windows kekal sebagai persekitaran sasaran utama. Untuk pembangun macOS yang menunggu binari asli:
1. Jalankan Foundry Local dalam VM Windows 11 (Parallels / UTM) ATAU stesen kerja Windows jauh.
2. Dedahkan perkhidmatan (port lalai 5273) dan tetapkan pada macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Gunakan langkah persekitaran maya Python yang sama seperti sesi sebelumnya.

Pemasangan Chainlit (kedua-dua platform):
```bash
pip install chainlit
```

## Aliran Demo (30 minit)

### 1. Bandingkan Phi (SLM) vs GPT-OSS-20B (LLM) (6 minit)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Jejak: kedalaman respons, ketepatan fakta, kekayaan gaya, latensi.

Perhatikan perubahan throughput selepas mengaktifkan GPU vs hanya CPU.

### 3. Inferens WebGPU dalam Pelayar (6 minit)

Sesuaikan permulaan `04-webgpu-inference` (buat `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Buka fail dalam pelayar; perhatikan pusingan tempatan berlatensi rendah.

### 4. Aplikasi Chat Chainlit RAG (7 minit)

`samples/04-cutting-edge/chainlit_app.py` minimum:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Jalankan:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Projek Permulaan: Sesuaikan `04-webgpu-inference` (6 minit)

Hasil:
- Gantikan logik pengambilan placeholder dengan token streaming (gunakan varian endpoint `stream=True` setelah diaktifkan)
- Tambahkan carta latensi (klien) untuk togol phi vs gpt-oss-20b
- Tanamkan konteks RAG secara langsung (textarea untuk dokumen rujukan)

## Heuristik Penilaian

| Kategori | Phi-4-mini | GPT-OSS-20B | Pemerhatian |
|----------|------------|-------------|-------------|
| Latensi (sejuk) | Pantas | Lebih perlahan | SLM cepat panas |
| Memori | Rendah | Tinggi | Kebolehlaksanaan peranti |
| Pematuhan konteks | Baik | Kuat | Model lebih besar mungkin lebih verbose |
| Kos (tempatan) | Minimum | Lebih tinggi (sumber) | Pertukaran tenaga/masa |
| Kes penggunaan terbaik | Aplikasi tepi | Penalaran mendalam | Saluran hibrid mungkin |

## Mengesahkan Persekitaran

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Penyelesaian Masalah

| Gejala | Punca | Tindakan |
|--------|-------|---------|
| Pengambilan halaman web gagal | CORS atau perkhidmatan tidak aktif | Gunakan `curl` untuk mengesahkan endpoint; aktifkan proksi CORS jika diperlukan |
| Chainlit kosong | Persekitaran tidak aktif | Aktifkan venv & pasang semula keperluan |
| Latensi tinggi | Model baru dimuat | Panaskan dengan urutan prompt kecil |

## Rujukan

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Dokumentasi Chainlit: https://docs.chainlit.io
- Penilaian RAG (Ragas): https://docs.ragas.io

---

**Tempoh Sesi**: 30 minit  
**Kesukaran**: Lanjutan

## Senario Contoh & Pemetaan Bengkel

| Artifak Bengkel | Senario | Objektif | Sumber Data / Prompt |
|------------------|---------|----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Pasukan seni bina menilai SLM vs LLM untuk penjana ringkasan eksekutif | Kuantifikasi latensi + delta penggunaan token | Satu pembolehubah persekitaran `COMPARE_PROMPT` |
| `chainlit_app.py` (demo RAG) | Prototaip pembantu pengetahuan dalaman | Menyokong jawapan pendek dengan pengambilan leksikal minimum | Senarai `DOCS` dalam fail |
| `webgpu_demo.html` | Pratonton inferens pelayar pada peranti masa depan | Tunjukkan pusingan tempatan berlatensi rendah + naratif UX | Hanya prompt pengguna langsung |

### Naratif Senario
Organisasi produk mahukan penjana taklimat eksekutif. SLM ringan (phi‑4‑mini) merangka ringkasan; LLM yang lebih besar (gpt‑oss‑20b) mungkin hanya memperhalusi laporan keutamaan tinggi. Skrip sesi menangkap metrik latensi & token empirikal untuk membenarkan reka bentuk hibrid, sementara demo Chainlit menggambarkan bagaimana pengambilan yang berasas memastikan jawapan model kecil adalah fakta. Halaman konsep WebGPU menyediakan laluan visi untuk pemprosesan sepenuhnya di sisi klien apabila pecutan pelayar matang.

### Konteks RAG Minimum (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Aliran Hibrid Draf→Perhalusi (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Jejak kedua-dua komponen latensi untuk melaporkan kos purata gabungan.

### Penambahbaikan Pilihan

| Fokus | Penambahbaikan | Sebab | Petunjuk Pelaksanaan |
|-------|----------------|-------|-----------------------|
| Metrik Perbandingan | Jejak penggunaan token + latensi token pertama | Pandangan prestasi holistik | Gunakan skrip penanda aras yang dipertingkatkan (Sesi 3) dengan `BENCH_STREAM=1` |
| Saluran Hibrid | Draf SLM → Perhalusi LLM | Kurangkan latensi & kos | Hasilkan dengan phi-4-mini, perhalusi ringkasan dengan gpt-oss-20b |
| UI Streaming | UX lebih baik dalam Chainlit | Maklum balas secara beransur-ansur | Gunakan `stream=True` setelah streaming tempatan didedahkan; kumpulkan pecahan |
| Cache WebGPU | Permulaan JS lebih pantas | Kurangkan overhead penyusunan semula | Cache artifak shader yang disusun (keupayaan runtime masa depan) |
| Set QA Deterministik | Perbandingan model yang adil | Hilangkan variasi | Senarai prompt tetap + `temperature=0` untuk larian penilaian |
| Pemarkahan Output | Lensa kualiti berstruktur | Bergerak melangkaui anekdot | Rubrik ringkas: koherensi / fakta / ringkas (1–5) |
| Nota Tenaga / Sumber | Perbincangan kelas | Tunjukkan pertukaran | Gunakan monitor OS (Task Manager, `nvidia-smi`) + output skrip penanda aras |
| Simulasi Kos | Justifikasi pra-awan | Rancang penskalaan | Peta token kepada harga awan hipotesis untuk naratif TCO |
| Penguraian Latensi | Kenal pasti halangan | Sasarkan pengoptimuman | Ukur persediaan prompt, penghantaran permintaan, token pertama, penyelesaian penuh |
| RAG + LLM Fallback | Jaring keselamatan kualiti | Tingkatkan pertanyaan sukar | Jika panjang jawapan SLM < ambang atau keyakinan rendah → tingkatkan |

#### Contoh Corak Draf/Perhalusi Hibrid

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Lakaran Penguraian Latensi

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Gunakan kerangka pengukuran yang konsisten di seluruh model untuk perbandingan yang adil.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->