<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:47:05+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "id"
}
-->
# Sesi 3: Model Open-Source di Foundry Local

## Abstrak

Pelajari cara membawa model Hugging Face dan model open-source lainnya ke Foundry Local. Temukan strategi pemilihan, alur kerja kontribusi komunitas, metodologi perbandingan kinerja, dan cara memperluas Foundry dengan registrasi model kustom. Sesi ini sesuai dengan tema eksplorasi mingguan "Model Mondays" dan membantu Anda mengevaluasi serta mengoperasionalkan model open-source secara lokal sebelum skalabilitas ke Azure.

## Tujuan Pembelajaran

Pada akhir sesi, Anda akan dapat:

- **Menemukan & Mengevaluasi**: Mengidentifikasi model kandidat (mistral, gemma, qwen, deepseek) menggunakan pertimbangan kualitas vs sumber daya.
- **Memuat & Menjalankan**: Menggunakan Foundry Local CLI untuk mengunduh, menyimpan, dan menjalankan model komunitas.
- **Benchmark**: Menerapkan heuristik konsisten untuk latensi + throughput token + kualitas.
- **Memperluas**: Mendaftarkan atau menyesuaikan pembungkus model kustom sesuai pola yang kompatibel dengan SDK.
- **Membandingkan**: Menghasilkan perbandingan terstruktur untuk keputusan pemilihan SLM vs LLM ukuran menengah.

## Prasyarat

- Sesi 1 & 2 telah selesai
- Lingkungan Python dengan `foundry-local-sdk` terinstal
- Setidaknya 15GB ruang disk kosong untuk cache beberapa model

### Panduan Memulai Cepat di Lingkungan Lintas Platform

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

Saat melakukan benchmark dari macOS terhadap layanan host Windows, atur:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Alur Demo (30 menit)

### 1. Memuat Model Hugging Face melalui CLI (8 menit)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Menjalankan & Uji Cepat (5 menit)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Skrip Benchmark (8 menit)

Buat `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Jalankan:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Membandingkan Kinerja (5 menit)

Diskusikan pertimbangan: waktu pemuatan, penggunaan memori (amati Task Manager / `nvidia-smi` / monitor sumber daya OS), kualitas output vs kecepatan. Gunakan skrip benchmark Python (Sesi 3) untuk latensi & throughput; ulangi setelah mengaktifkan akselerasi GPU.

### 5. Proyek Awal (4 menit)

Buat generator laporan perbandingan model (perluas skrip benchmark dengan ekspor markdown).

## Proyek Awal: Memperluas `03-huggingface-models`

Tingkatkan sampel yang ada dengan:

1. Menambahkan agregasi benchmark + output CSV/Markdown.
2. Mengimplementasikan penilaian kualitatif sederhana (set pasangan prompt + file stub anotasi manual).
3. Memperkenalkan konfigurasi JSON (`models.json`) untuk daftar model yang dapat dihubungkan & set prompt.

## Daftar Periksa Validasi

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Semua model target harus muncul dan merespons permintaan chat probe.

## Skenario Contoh & Pemetaan Workshop

| Skrip Workshop | Skenario | Tujuan | Sumber Prompt / Dataset |
|-----------------|----------|--------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Tim platform edge memilih SLM default untuk summarizer tersemat | Menghasilkan perbandingan latensi + p95 + tokens/detik di antara model kandidat | Variabel `PROMPT` inline + daftar `BENCH_MODELS` lingkungan |

### Narasi Skenario
Tim rekayasa produk harus memilih model summarization ringan default untuk fitur catatan rapat offline. Mereka menjalankan benchmark deterministik yang terkontrol (temperature=0) pada set prompt tetap (lihat contoh di bawah) dan mengumpulkan metrik latensi + throughput dengan dan tanpa akselerasi GPU.

### Contoh Set Prompt JSON (dapat diperluas)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Loop setiap prompt per model, tangkap latensi per-prompt untuk menghitung metrik distribusi dan mendeteksi outlier.

## Kerangka Kerja Pemilihan Model

| Dimensi | Metrik | Mengapa Penting |
|---------|--------|-----------------|
| Latensi | rata-rata / p95 | Konsistensi pengalaman pengguna |
| Throughput | tokens/detik | Skalabilitas batch & streaming |
| Memori | ukuran residensi | Kesesuaian perangkat & konkurensi |
| Kualitas | prompt rubrik | Kesesuaian tugas |
| Jejak | cache disk | Distribusi & pembaruan |
| Lisensi | izin penggunaan | Kepatuhan komersial |

## Memperluas dengan Model Kustom

Pola tingkat tinggi (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konsultasikan repo resmi untuk antarmuka adapter yang terus berkembang:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Pemecahan Masalah

| Masalah | Penyebab | Solusi |
|---------|----------|--------|
| OOM pada mistral-7b | RAM/GPU tidak mencukupi | Hentikan model lain; coba varian yang lebih kecil |
| Respons pertama lambat | Pemuatan dingin | Tetap hangat dengan prompt ringan berkala |
| Unduhan terhenti | Ketidakstabilan jaringan | Coba lagi; prefetch saat jam tidak sibuk |

## Referensi

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Penemuan Model Hugging Face: https://huggingface.co/models

---

**Durasi Sesi**: 30 menit (+ pendalaman opsional)  
**Kesulitan**: Menengah

### Peningkatan Opsional

| Peningkatan | Manfaat | Cara |
|-------------|---------|------|
| Latensi Token Pertama Streaming | Mengukur responsivitas yang dirasakan | Jalankan benchmark dengan `BENCH_STREAM=1` (skrip yang ditingkatkan di `Workshop/samples/session03`) |
| Mode Deterministik | Perbandingan regresi yang stabil | `temperature=0`, set prompt tetap, tangkap output JSON di bawah kontrol versi |
| Penilaian Rubrik Kualitas | Menambahkan dimensi kualitatif | Kelola `prompts.json` dengan aspek yang diharapkan; anotasi skor (1–5) secara manual atau melalui model sekunder |
| Ekspor CSV / Markdown | Laporan yang dapat dibagikan | Perluas skrip untuk menulis `benchmark_report.md` dengan tabel & sorotan |
| Tag Kemampuan Model | Membantu perutean otomatis di masa depan | Kelola `models.json` dengan `{alias: {capabilities:[], size_mb:..}}` |
| Fase Pemanasan Cache | Mengurangi bias pemuatan dingin | Jalankan satu putaran hangat sebelum loop pengukuran waktu (sudah diimplementasikan) |
| Akurasi Persentil | Latensi tail yang kuat | Gunakan numpy percentile (sudah dalam skrip yang direfaktor) |
| Perkiraan Biaya Token | Perbandingan ekonomi | Perkiraan biaya = (tokens/detik * rata-rata token per permintaan) * heuristik energi |
| Auto-Skipping Model Gagal | Ketahanan dalam batch run | Bungkus setiap benchmark dalam try/except dan tandai status field |

#### Cuplikan Ekspor Markdown Minimal

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Contoh Set Prompt Deterministik

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Loop daftar statis alih-alih prompt acak untuk metrik yang dapat dibandingkan di antara commit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->