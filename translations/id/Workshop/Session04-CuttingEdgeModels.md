<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T23:44:17+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "id"
}
-->
# Sesi 4: Jelajahi Model Terkini – LLM, SLM & Inferensi di Perangkat

## Abstrak

Bandingkan Large Language Models (LLMs) dan Small Language Models (SLMs) untuk skenario inferensi lokal vs cloud. Pelajari pola penerapan yang memanfaatkan akselerasi ONNX Runtime, eksekusi WebGPU, dan pengalaman hybrid RAG. Termasuk demo Chainlit RAG dengan model lokal serta eksplorasi opsional OpenWebUI. Anda akan menyesuaikan starter inferensi WebGPU dan mengevaluasi kemampuan Phi vs GPT-OSS-20B serta trade-off biaya/kinerja.

## Tujuan Pembelajaran

- **Bandingkan** SLM vs LLM berdasarkan latensi, memori, dan kualitas
- **Terapkan** model dengan ONNXRuntime dan (jika didukung) WebGPU
- **Jalankan** inferensi berbasis browser (demo interaktif yang menjaga privasi)
- **Integrasikan** pipeline Chainlit RAG dengan backend SLM lokal
- **Evaluasi** menggunakan heuristik kualitas + biaya yang ringan

## Prasyarat

- Sesi 1–3 selesai
- `chainlit` terinstal (sudah ada di `requirements.txt` untuk Modul08)
- Browser yang mendukung WebGPU (Edge / Chrome terbaru di Windows 11)
- Foundry Local berjalan (`foundry service status`)

### Catatan Lintas Platform

Windows tetap menjadi lingkungan target utama. Untuk pengembang macOS yang menunggu binary native:
1. Jalankan Foundry Local di VM Windows 11 (Parallels / UTM) ATAU workstation Windows jarak jauh.
2. Ekspos layanan (port default 5273) dan atur di macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Gunakan langkah-langkah lingkungan virtual Python yang sama seperti sesi sebelumnya.

Instalasi Chainlit (kedua platform):
```bash
pip install chainlit
```

## Alur Demo (30 menit)

### 1. Bandingkan Phi (SLM) vs GPT-OSS-20B (LLM) (6 menit)

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

Pantau: kedalaman respons, akurasi faktual, kekayaan gaya, latensi.

Amati perubahan throughput setelah mengaktifkan GPU dibandingkan hanya CPU.

### 3. Inferensi WebGPU di Browser (6 menit)

Sesuaikan starter `04-webgpu-inference` (buat `samples/04-cutting-edge/webgpu_demo.html`):

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

Buka file di browser; amati roundtrip lokal dengan latensi rendah.

### 4. Aplikasi Chat Chainlit RAG (7 menit)

`samples/04-cutting-edge/chainlit_app.py` minimal:

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

### 5. Proyek Starter: Sesuaikan `04-webgpu-inference` (6 menit)

Hasil yang diharapkan:
- Ganti logika fetch placeholder dengan token streaming (gunakan varian endpoint `stream=True` setelah diaktifkan)
- Tambahkan grafik latensi (client-side) untuk toggle phi vs gpt-oss-20b
- Sematkan konteks RAG secara langsung (textarea untuk dokumen referensi)

## Heuristik Evaluasi

| Kategori | Phi-4-mini | GPT-OSS-20B | Pengamatan |
|----------|------------|-------------|-------------|
| Latensi (dingin) | Cepat | Lebih lambat | SLM cepat memanas |
| Memori | Rendah | Tinggi | Kelayakan perangkat |
| Kepatuhan konteks | Baik | Kuat | Model yang lebih besar mungkin lebih verbose |
| Biaya (lokal) | Minimal | Lebih tinggi (sumber daya) | Trade-off energi/waktu |
| Kasus penggunaan terbaik | Aplikasi edge | Penalaran mendalam | Pipeline hybrid memungkinkan |

## Validasi Lingkungan

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Pemecahan Masalah

| Gejala | Penyebab | Tindakan |
|--------|----------|----------|
| Fetch halaman web gagal | CORS atau layanan down | Gunakan `curl` untuk memverifikasi endpoint; aktifkan proxy CORS jika diperlukan |
| Chainlit kosong | Lingkungan tidak aktif | Aktifkan venv & instal ulang dependensi |
| Latensi tinggi | Model baru dimuat | Panaskan dengan urutan prompt kecil |

## Referensi

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Dokumentasi Chainlit: https://docs.chainlit.io
- Evaluasi RAG (Ragas): https://docs.ragas.io

---

**Durasi Sesi**: 30 menit  
**Tingkat Kesulitan**: Lanjutan

## Skenario Contoh & Pemetaan Workshop

| Artefak Workshop | Skenario | Tujuan | Sumber Data / Prompt |
|------------------|----------|--------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Tim arsitektur mengevaluasi SLM vs LLM untuk generator ringkasan eksekutif | Kuantifikasi delta latensi + penggunaan token | Variabel lingkungan `COMPARE_PROMPT` tunggal |
| `chainlit_app.py` (demo RAG) | Prototipe asisten pengetahuan internal | Memberikan jawaban singkat dengan pengambilan leksikal minimal | Daftar `DOCS` langsung dalam file |
| `webgpu_demo.html` | Pratinjau inferensi browser di perangkat masa depan | Menunjukkan roundtrip lokal berlatensi rendah + narasi UX | Hanya prompt pengguna langsung |

### Narasi Skenario
Organisasi produk menginginkan generator ringkasan eksekutif. SLM ringan (phi‑4‑mini) membuat draft ringkasan; LLM yang lebih besar (gpt‑oss‑20b) mungkin hanya menyempurnakan laporan prioritas tinggi. Skrip sesi menangkap metrik latensi & token empiris untuk membenarkan desain hybrid, sementara demo Chainlit menggambarkan bagaimana pengambilan yang terarah menjaga jawaban model kecil tetap faktual. Halaman konsep WebGPU memberikan jalur visi untuk pemrosesan sepenuhnya di sisi klien saat akselerasi browser matang.

### Konteks RAG Minimal (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Alur Hybrid Draft→Refine (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Lacak kedua komponen latensi untuk melaporkan rata-rata biaya gabungan.

### Peningkatan Opsional

| Fokus | Peningkatan | Mengapa | Petunjuk Implementasi |
|-------|------------|---------|-----------------------|
| Metrik Perbandingan | Lacak penggunaan token + latensi token pertama | Pandangan kinerja holistik | Gunakan skrip benchmark yang ditingkatkan (Sesi 3) dengan `BENCH_STREAM=1` |
| Pipeline Hybrid | Draft SLM → Refine LLM | Kurangi latensi & biaya | Buat dengan phi-4-mini, sempurnakan ringkasan dengan gpt-oss-20b |
| UI Streaming | UX lebih baik di Chainlit | Umpan balik bertahap | Gunakan `stream=True` setelah streaming lokal diaktifkan; kumpulkan potongan |
| Caching WebGPU | Inisialisasi JS lebih cepat | Kurangi overhead kompilasi ulang | Cache artefak shader yang dikompilasi (kemampuan runtime masa depan) |
| Set QA Deterministik | Perbandingan model yang adil | Hilangkan variansi | Daftar prompt tetap + `temperature=0` untuk evaluasi |
| Penilaian Output | Lensa kualitas terstruktur | Melampaui anekdot | Rubrik sederhana: koherensi / faktualitas / singkat (1–5) |
| Catatan Energi / Sumber Daya | Diskusi kelas | Tunjukkan trade-off | Gunakan monitor OS (Task Manager, `nvidia-smi`) + output skrip benchmark |
| Emulasi Biaya | Justifikasi pra-cloud | Rencana skalabilitas | Peta token ke harga cloud hipotetis untuk narasi TCO |
| Dekonstruksi Latensi | Identifikasi hambatan | Targetkan optimasi | Ukur persiapan prompt, pengiriman permintaan, token pertama, penyelesaian penuh |
| RAG + LLM Fallback | Jaring pengaman kualitas | Tingkatkan kueri sulit | Jika panjang jawaban SLM < ambang batas atau kepercayaan rendah → eskalasi |

#### Pola Hybrid Draft/Refine Contoh

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Sketsa Pemecahan Latensi

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
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->