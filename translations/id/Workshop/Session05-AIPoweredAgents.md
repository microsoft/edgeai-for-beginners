<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T22:36:49+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "id"
}
-->
# Sesi 5: Bangun Agen AI dengan Cepat menggunakan Foundry Local

## Abstrak

Rancang dan orkestrasi agen AI multi-peran dengan memanfaatkan runtime Foundry Local yang memiliki latensi rendah dan menjaga privasi. Anda akan mendefinisikan peran agen, strategi memori, pola pemanggilan alat, dan grafik eksekusi. Sesi ini memperkenalkan pola scaffolding yang dapat Anda kembangkan dengan Chainlit atau LangGraph. Proyek awal memperluas sampel arsitektur agen yang ada untuk menambahkan persistensi memori + pengait evaluasi.

## Tujuan Pembelajaran

- **Definisikan Peran**: Prompt sistem & batas kemampuan
- **Implementasikan Memori**: Jangka pendek (percakapan), jangka panjang (vektor / file), scratchpad sementara
- **Scaffold Alur Kerja**: Langkah agen berurutan, bercabang, dan paralel
- **Integrasikan Alat**: Pola pemanggilan alat fungsi ringan
- **Evaluasi**: Jejak dasar + penilaian hasil berbasis rubrik

## Prasyarat

- Sesi 1–4 selesai
- Python dengan `foundry-local-sdk`, `openai`, opsional `chainlit`
- Model lokal berjalan (minimal `phi-4-mini`)

### Cuplikan Lingkungan Lintas Platform

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Jika menjalankan agen dari macOS terhadap layanan host Windows jarak jauh:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Alur Demo (30 menit)

### 1. Definisikan Peran Agen & Memori (7 menit)

Buat `samples/05-agents/agents_core.py`:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. Pola Scaffolding CLI (3 menit)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Tambahkan Pemanggilan Alat (7 menit)

Perluas dengan `samples/05-agents/tools.py`:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```

Modifikasi `agents_core.py` untuk memungkinkan sintaks alat sederhana: pengguna menulis `#tool:get_time` dan agen memperluas output alat ke dalam konteks sebelum generasi.

### 4. Alur Kerja yang Diorkestrasi (6 menit)

Buat `samples/05-agents/orchestrator.py`:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. Proyek Awal: Perluas `05-agent-architecture` (7 menit)

Tambahkan:
1. Lapisan memori yang persisten (misalnya, penambahan baris JSON dari percakapan)
2. Rubrik evaluasi sederhana: placeholder faktualitas / kejelasan / gaya
3. Front-end Chainlit opsional (dua tab: percakapan & jejak)
4. Mesin keadaan gaya LangGraph opsional (jika menambahkan dependensi) untuk keputusan bercabang

## Daftar Periksa Validasi

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Harapkan output pipeline terstruktur dengan catatan injeksi alat.

## Ikhtisar Strategi Memori

| Lapisan | Tujuan | Contoh |
|---------|--------|--------|
| Jangka pendek | Kelanjutan dialog | Pesan terakhir N |
| Episodik | Ingatan sesi | JSON per sesi |
| Semantik | Pengambilan jangka panjang | Penyimpanan vektor dari ringkasan |
| Scratchpad | Langkah penalaran | Rantai pemikiran inline (privat) |

## Pengait Evaluasi (Konseptual)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Pemecahan Masalah

| Masalah | Penyebab | Resolusi |
|---------|----------|----------|
| Jawaban berulang | Jendela konteks terlalu besar/kecil | Sesuaikan parameter jendela memori |
| Alat tidak dipanggil | Sintaks salah | Gunakan format `#tool:tool_name` |
| Orkestrasi lambat | Model dingin yang banyak | Jalankan prompt pemanasan sebelumnya |

## Referensi

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (konsep opsional): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Durasi Sesi**: 30 menit  
**Kesulitan**: Lanjutan

## Skenario Contoh & Pemetaan Workshop

| Skrip Workshop | Skenario | Tujuan | Contoh Prompt |
|-----------------|----------|--------|---------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot penelitian pengetahuan yang menghasilkan ringkasan ramah eksekutif | Pipeline dua agen (penelitian → penyempurnaan editorial) dengan model yang berbeda opsional | Jelaskan mengapa inferensi edge penting untuk kepatuhan. |
| (Diperluas) konsep `tools.py` | Tambahkan alat estimasi waktu & token | Tunjukkan pola pemanggilan alat ringan | #tool:get_time |

### Narasi Skenario
Tim dokumentasi kepatuhan membutuhkan ringkasan internal cepat yang bersumber dari pengetahuan lokal tanpa mengirimkan draf ke layanan cloud. Agen peneliti mengumpulkan poin fakta singkat; agen editor menulis ulang untuk kejelasan eksekutif. Alias model yang berbeda dapat ditugaskan untuk mengoptimalkan latensi (SLM cepat) vs penyempurnaan gaya (model yang lebih besar hanya jika diperlukan).

### Contoh Lingkungan Multi-Model
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Struktur Jejak (Opsional)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

Persist setiap langkah ke file JSONL untuk penilaian rubrik nanti.

### Peningkatan Opsional

| Tema | Peningkatan | Manfaat | Sketsa Implementasi |
|------|-------------|---------|---------------------|
| Peran Multi-Model | Model berbeda per agen (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Spesialisasi & kecepatan | Pilih alias variabel lingkungan, panggil `chat_once` dengan alias per peran |
| Jejak Terstruktur | Jejak JSON dari setiap tindakan (alat, input, latensi, token) | Debug & evaluasi | Tambahkan dict ke daftar; tulis `.jsonl` di akhir |
| Persistensi Memori | Konteks dialog yang dapat dimuat ulang | Kelanjutan sesi | Dump `Agent.memory` ke `sessions/<ts>.json` |
| Registri Alat | Penemuan alat dinamis | Ekstensibilitas | Pertahankan dict `TOOLS` & introspeksi nama/deskripsi |
| Retry & Backoff | Rantai panjang yang tangguh | Kurangi kegagalan sementara | Bungkus `act` dengan try/except + backoff eksponensial |
| Penilaian Rubrik | Label kualitatif otomatis | Lacak perbaikan | Prompt pass sekunder model: "Nilai kejelasan 1-5" |
| Memori Vektor | Pengambilan semantik | Konteks jangka panjang yang kaya | Embed ringkasan, ambil top-k ke dalam pesan sistem |
| Balasan Streaming | Respons yang terasa lebih cepat | Peningkatan UX | Gunakan streaming saat tersedia dan flush token parsial |
| Tes Deterministik | Kontrol regresi | CI stabil | Jalankan dengan `temperature=0`, seed prompt tetap |
| Cabang Paralel | Eksplorasi lebih cepat | Throughput | Gunakan `concurrent.futures` untuk langkah agen independen |

#### Contoh Rekaman Jejak

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Prompt Evaluasi Sederhana

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Persist pasangan (`answer`, `rating`) untuk membangun grafik kualitas historis.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.