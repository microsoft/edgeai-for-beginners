<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T22:40:57+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "ms"
}
-->
# Sesi 5: Bina Ejen Berkuasa AI dengan Cepat menggunakan Foundry Local

## Abstrak

Reka bentuk dan orkestrasi ejen AI pelbagai peranan dengan memanfaatkan runtime Foundry Local yang rendah latensi dan melindungi privasi. Anda akan menentukan peranan ejen, strategi memori, corak pemanggilan alat, dan graf pelaksanaan. Sesi ini memperkenalkan corak scaffolding yang boleh anda kembangkan dengan Chainlit atau LangGraph. Projek permulaan memperluaskan sampel seni bina ejen sedia ada untuk menambah ketekalan memori + cangkuk penilaian.

## Objektif Pembelajaran

- **Tentukan Peranan**: Prompt sistem & sempadan keupayaan
- **Laksanakan Memori**: Jangka pendek (perbualan), jangka panjang (vektor / fail), scratchpad sementara
- **Scaffold Aliran Kerja**: Langkah ejen berurutan, bercabang, dan selari
- **Integrasi Alat**: Corak pemanggilan alat fungsi ringan
- **Penilaian**: Jejak asas + penilaian hasil berdasarkan rubrik

## Prasyarat

- Sesi 1–4 selesai
- Python dengan `foundry-local-sdk`, `openai`, opsional `chainlit`
- Model tempatan berjalan (sekurang-kurangnya `phi-4-mini`)

### Petikan Persekitaran Merentas Platform

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

Jika menjalankan ejen dari macOS terhadap perkhidmatan hos Windows jauh:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Aliran Demo (30 min)

### 1. Tentukan Peranan & Memori Ejen (7 min)

Cipta `samples/05-agents/agents_core.py`:

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

### 2. Corak Scaffolding CLI (3 min)

```powershell
python samples/05-agents/agents_core.py
```

### 3. Tambah Pemanggilan Alat (7 min)

Kembangkan dengan `samples/05-agents/tools.py`:

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

Ubah suai `agents_core.py` untuk membolehkan sintaks alat yang mudah: pengguna menulis `#tool:get_time` dan ejen mengembangkan output alat ke dalam konteks sebelum penjanaan.

### 4. Aliran Kerja Berorkestrasi (6 min)

Cipta `samples/05-agents/orchestrator.py`:

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

### 5. Projek Permulaan: Kembangkan `05-agent-architecture` (7 min)

Tambah:
1. Lapisan memori berterusan (contohnya, append baris JSON perbualan)
2. Rubrik penilaian mudah: placeholder faktualiti / kejelasan / gaya
3. Front-end Chainlit opsional (dua tab: perbualan & jejak)
4. Mesin keadaan gaya LangGraph opsional (jika menambah kebergantungan) untuk keputusan bercabang

## Senarai Semak Pengesahan

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Harapkan output saluran paip berstruktur dengan nota suntikan alat.

## Gambaran Strategi Memori

| Lapisan | Tujuan | Contoh |
|---------|--------|--------|
| Jangka pendek | Kesinambungan dialog | N mesej terakhir |
| Episodik | Ingatan sesi | JSON setiap sesi |
| Semantik | Pengambilan jangka panjang | Simpanan vektor ringkasan |
| Scratchpad | Langkah penaakulan | Rantaian pemikiran dalam talian (peribadi) |

## Cangkuk Penilaian (Konseptual)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```

## Penyelesaian Masalah

| Isu | Punca | Penyelesaian |
|-----|-------|-------------|
| Jawapan berulang | Tetingkap konteks terlalu besar/kecil | Laraskan parameter tetingkap memori |
| Alat tidak dipanggil | Sintaks salah | Gunakan format `#tool:tool_name` |
| Orkestrasi perlahan | Model sejuk berganda | Jalankan prompt pemanasan awal |

## Rujukan

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (konsep opsional): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Tempoh Sesi**: 30 min  
**Kesukaran**: Lanjutan

## Senario Sampel & Pemetaan Bengkel

| Skrip Bengkel | Senario | Objektif | Contoh Prompt |
|---------------|---------|----------|---------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot penyelidikan pengetahuan menghasilkan ringkasan mesra eksekutif | Saluran paip dua ejen (penyelidikan → penggilapan editorial) dengan model berbeza opsional | Terangkan mengapa inferens tepi penting untuk pematuhan. |
| (Dikembangkan) konsep `tools.py` | Tambah alat anggaran masa & token | Tunjukkan corak pemanggilan alat ringan | #tool:get_time |

### Naratif Senario
Pasukan dokumentasi pematuhan memerlukan ringkasan dalaman pantas yang diperoleh daripada pengetahuan tempatan tanpa menghantar draf ke perkhidmatan awan. Ejen penyelidik mengumpulkan fakta ringkas; ejen editor menulis semula untuk kejelasan eksekutif. Alias model berbeza boleh diberikan untuk mengoptimumkan latensi (SLM pantas) vs penghalusan gaya (model lebih besar hanya apabila diperlukan).

### Contoh Persekitaran Multi-Model
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

Simpan setiap langkah ke fail JSONL untuk penilaian rubrik kemudian.

### Penambahbaikan Opsional

| Tema | Penambahbaikan | Manfaat | Lakaran Pelaksanaan |
|------|----------------|---------|---------------------|
| Peranan Multi-Model | Model berbeza setiap ejen (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Pengkhususan & kelajuan | Pilih alias env vars, panggil `chat_once` dengan alias per-peranan |
| Jejak Berstruktur | Jejak JSON setiap tindakan (alat, input, latensi, token) | Debug & penilaian | Tambah dict ke senarai; tulis `.jsonl` pada akhir |
| Ketekalan Memori | Konteks dialog boleh dimuat semula | Kesinambungan sesi | Dump `Agent.memory` ke `sessions/<ts>.json` |
| Pendaftaran Alat | Penemuan alat dinamik | Kebolehluasan | Kekalkan dict `TOOLS` & introspeksi nama/deskripsi |
| Ulang & Backoff | Rantai panjang yang kukuh | Kurangkan kegagalan sementara | Bungkus `act` dengan try/except + backoff eksponen |
| Penilaian Rubrik | Label kualitatif automatik | Jejak penambahbaikan | Prompt pas kedua model: "Nilai kejelasan 1-5" |
| Memori Vektor | Pengambilan semantik | Konteks jangka panjang yang kaya | Embed ringkasan, ambil top-k ke dalam mesej sistem |
| Balasan Streaming | Respons yang dirasakan lebih pantas | Penambahbaikan UX | Gunakan streaming apabila tersedia dan flush token separa |
| Ujian Deterministik | Kawalan regresi | CI stabil | Jalankan dengan `temperature=0`, benih prompt tetap |
| Cabang Selari | Penerokaan lebih pantas | Throughput | Gunakan `concurrent.futures` untuk langkah ejen bebas |

#### Contoh Rekod Jejak

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```

#### Prompt Penilaian Mudah

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Simpan pasangan (`answer`, `rating`) untuk membina graf kualiti sejarah.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.