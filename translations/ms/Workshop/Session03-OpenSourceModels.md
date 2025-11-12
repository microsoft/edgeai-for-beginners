<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:51:30+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "ms"
}
-->
# Sesi 3: Model Sumber Terbuka dalam Foundry Local

## Abstrak

Ketahui cara membawa model Hugging Face dan model sumber terbuka lain ke dalam Foundry Local. Pelajari strategi pemilihan, aliran kerja sumbangan komuniti, metodologi perbandingan prestasi, dan cara memperluaskan Foundry dengan pendaftaran model tersuai. Sesi ini selaras dengan tema eksplorasi mingguan "Model Mondays" dan melengkapkan anda untuk menilai dan mengoperasikan model sumber terbuka secara tempatan sebelum meningkatkan ke Azure.

## Objektif Pembelajaran

Pada akhir sesi, anda akan dapat:

- **Menemui & Menilai**: Mengenal pasti model calon (mistral, gemma, qwen, deepseek) menggunakan pertukaran antara kualiti dan sumber.
- **Memuat & Menjalankan**: Menggunakan Foundry Local CLI untuk memuat turun, menyimpan, dan melancarkan model komuniti.
- **Penanda Aras**: Mengaplikasikan heuristik konsisten untuk latensi + throughput token + kualiti.
- **Memperluaskan**: Mendaftar atau menyesuaikan pembungkus model tersuai mengikut pola yang serasi dengan SDK.
- **Membandingkan**: Menghasilkan perbandingan terstruktur untuk keputusan pemilihan SLM vs LLM bersaiz sederhana.

## Prasyarat

- Sesi 1 & 2 selesai
- Persekitaran Python dengan `foundry-local-sdk` dipasang
- Sekurang-kurangnya 15GB ruang cakera kosong untuk cache model pelbagai

### Permulaan Cepat Persekitaran Merentas Platform

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

Apabila melakukan penanda aras dari macOS terhadap perkhidmatan hos Windows, tetapkan:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Aliran Demo (30 minit)

### 1. Memuatkan Model Hugging Face melalui CLI (8 minit)

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


### 2. Menjalankan & Ujian Cepat (5 minit)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Skrip Penanda Aras (8 minit)

Cipta `samples/03-oss-models/benchmark_models.py`:

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


### 4. Membandingkan Prestasi (5 minit)

Bincangkan pertukaran: masa muat, jejak memori (perhatikan Task Manager / `nvidia-smi` / monitor sumber OS), kualiti output vs kelajuan. Gunakan skrip penanda aras Python (Sesi 3) untuk latensi & throughput; ulangi selepas mengaktifkan pecutan GPU.

### 5. Projek Permulaan (4 minit)

Cipta penjana laporan perbandingan model (perluaskan skrip penanda aras dengan eksport markdown).

## Projek Permulaan: Memperluaskan `03-huggingface-models`

Tingkatkan sampel sedia ada dengan:

1. Menambah pengagregatan penanda aras + output CSV/Markdown.
2. Melaksanakan penilaian kualitatif mudah (set pasangan prompt + fail stub anotasi manual).
3. Memperkenalkan konfigurasi JSON (`models.json`) untuk senarai model yang boleh dipasang & set prompt.

## Senarai Semak Pengesahan

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Semua model sasaran harus muncul dan memberi respons kepada permintaan chat probe.

## Senario Sampel & Pemetaan Bengkel

| Skrip Bengkel | Senario | Matlamat | Sumber Prompt / Dataset |
|---------------|---------|----------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Pasukan platform tepi memilih SLM lalai untuk penyimpul terbenam | Menghasilkan perbandingan latensi + p95 + token/sec di kalangan model calon | Var `PROMPT` dalam talian + senarai `BENCH_MODELS` persekitaran |

### Naratif Senario
Kejuruteraan produk mesti memilih model penyimpul ringan lalai untuk ciri nota mesyuarat luar talian. Mereka menjalankan penanda aras deterministik terkawal (temperature=0) di kalangan set prompt tetap (lihat contoh di bawah) dan mengumpulkan metrik latensi + throughput dengan dan tanpa pecutan GPU.

### Contoh Set Prompt JSON (boleh diperluaskan)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Ulang setiap prompt bagi setiap model, tangkap latensi per-prompt untuk mendapatkan metrik pengedaran dan mengesan nilai luar biasa.

## Kerangka Pemilihan Model

| Dimensi | Metrik | Mengapa Ia Penting |
|---------|--------|--------------------|
| Latensi | avg / p95 | Konsistensi pengalaman pengguna |
| Throughput | tokens/sec | Skalabiliti batch & streaming |
| Memori | saiz penduduk | Keserasian peranti & kebersamaan |
| Kualiti | rubric prompts | Kesesuaian tugas |
| Jejak | cache cakera | Pengedaran & kemas kini |
| Lesen | kebenaran penggunaan | Pematuhan komersial |

## Memperluaskan Dengan Model Tersuai

Pola tahap tinggi (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Rujuk repo rasmi untuk antara muka adapter yang berkembang:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Penyelesaian Masalah

| Isu | Punca | Penyelesaian |
|-----|-------|-------------|
| OOM pada mistral-7b | RAM/GPU tidak mencukupi | Hentikan model lain; cuba varian lebih kecil |
| Respons pertama perlahan | Muat sejuk | Kekalkan hangat dengan prompt ringan berkala |
| Muat turun tergendala | Ketidakstabilan rangkaian | Cuba semula; pra-muat semasa waktu tidak sibuk |

## Rujukan

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Penemuan Model Hugging Face: https://huggingface.co/models

---

**Tempoh Sesi**: 30 minit (+ pilihan mendalam)  
**Kesukaran**: Pertengahan

### Penambahbaikan Pilihan

| Penambahbaikan | Manfaat | Cara |
|----------------|---------|-----|
| Latensi Token Pertama Streaming | Mengukur responsiviti yang dirasakan | Jalankan penanda aras dengan `BENCH_STREAM=1` (skrip yang dipertingkatkan dalam `Workshop/samples/session03`) |
| Mod Deterministik | Perbandingan regresi stabil | `temperature=0`, set prompt tetap, tangkap output JSON di bawah kawalan versi |
| Penilaian Rubrik Kualiti | Menambah dimensi kualitatif | Kekalkan `prompts.json` dengan aspek yang dijangka; anotasi skor (1–5) secara manual atau melalui model sekunder |
| Eksport CSV / Markdown | Laporan yang boleh dikongsi | Perluaskan skrip untuk menulis `benchmark_report.md` dengan jadual & sorotan |
| Tag Keupayaan Model | Membantu penghalaan automatik kemudian | Kekalkan `models.json` dengan `{alias: {capabilities:[], size_mb:..}}` |
| Fasa Pemanasan Cache | Mengurangkan bias permulaan sejuk | Laksanakan satu pusingan hangat sebelum gelung masa (sudah dilaksanakan) |
| Ketepatan Peratusan | Latensi ekor yang kukuh | Gunakan numpy percentile (sudah dalam skrip yang diubah suai) |
| Anggaran Kos Token | Perbandingan ekonomi | Anggaran kos = (tokens/sec * purata token setiap permintaan) * heuristik tenaga |
| Melangkau Model Gagal Secara Automatik | Ketahanan dalam jalankan batch | Bungkus setiap penanda aras dalam try/except dan tandakan medan status |

#### Petikan Eksport Markdown Minimal

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

Ulang senarai statik dan bukannya prompt rawak untuk metrik yang boleh dibandingkan di kalangan komit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->