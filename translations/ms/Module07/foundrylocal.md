# Foundry Local pada Windows & Mac

Panduan ini membantu anda memasang, menjalankan, dan mengintegrasikan Microsoft Foundry Local pada Windows dan Mac. Semua langkah dan arahan telah disahkan berdasarkan dokumen Microsoft Learn.

- Bermula: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Seni bina: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Rujukan CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrasi SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompilasi Model HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Tempatan vs Awan: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Pasang / Tingkatkan pada Windows

- Pasang:
```cmd
winget install Microsoft.FoundryLocal
```
- Tingkatkan:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Semak versi:
```cmd
foundry --version
```
     
**Pasang / Mac**

**MacOS**: 
Buka terminal dan jalankan arahan berikut:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Asas CLI (Tiga Kategori)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Perkhidmatan:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Nota:
- Perkhidmatan ini menyediakan API REST yang serasi dengan OpenAI. Port endpoint diperuntukkan secara dinamik; gunakan `foundry service status` untuk mengetahuinya.
- Gunakan SDK untuk kemudahan; ia secara automatik menguruskan penemuan endpoint di mana disokong.

## 3) Menemui Endpoint Tempatan (Port Dinamik)

Foundry Local memperuntukkan port dinamik setiap kali perkhidmatan dimulakan:
```cmd
foundry service status
```
Gunakan `http://localhost:<PORT>` yang dilaporkan sebagai `base_url` anda dengan laluan serasi OpenAI (contohnya, `/v1/chat/completions`).

## 4) Ujian Pantas melalui OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Rujukan:
- Integrasi SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Bawa Model Anda Sendiri (Kompilasi dengan Olive)

Jika anda memerlukan model yang tidak terdapat dalam katalog, kompilasikannya ke ONNX untuk Foundry Local menggunakan Olive.

Aliran tahap tinggi (lihat dokumen untuk langkah-langkah):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumen:
- Kompilasi BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Penyelesaian Masalah

- Semak status perkhidmatan dan log:
```cmd
foundry service status
foundry service diag
```
- Kosongkan atau pindahkan cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Kemas kini ke pratonton terkini:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Pengalaman Pembangun Windows Berkaitan

- Pilihan AI tempatan vs awan Windows, termasuk Foundry Local dan Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit dengan Foundry Local (gunakan `foundry service status` untuk mendapatkan URL endpoint chat):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Next Windows Developer](./windowdeveloper.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.