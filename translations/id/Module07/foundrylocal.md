# Foundry Local di Windows & Mac

Panduan ini membantu Anda menginstal, menjalankan, dan mengintegrasikan Microsoft Foundry Local di Windows dan Mac. Semua langkah dan perintah telah divalidasi berdasarkan dokumen Microsoft Learn.

- Memulai: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arsitektur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referensi CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrasi SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompilasi Model HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokal vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Instalasi / Upgrade di Windows

- Instal:
```cmd
winget install Microsoft.FoundryLocal
```
- Upgrade:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Cek versi:
```cmd
foundry --version
```
     
**Instalasi / Mac**

**MacOS**: 
Buka terminal dan jalankan perintah berikut:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Dasar CLI (Tiga Kategori)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Layanan:
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

Catatan:
- Layanan menyediakan REST API yang kompatibel dengan OpenAI. Port endpoint dialokasikan secara dinamis; gunakan `foundry service status` untuk menemukannya.
- Gunakan SDK untuk kemudahan; mereka secara otomatis menangani penemuan endpoint di mana didukung.

## 3) Menemukan Endpoint Lokal (Port Dinamis)

Foundry Local menetapkan port dinamis setiap kali layanan dimulai:
```cmd
foundry service status
```
Gunakan `http://localhost:<PORT>` yang dilaporkan sebagai `base_url` Anda dengan jalur yang kompatibel dengan OpenAI (misalnya, `/v1/chat/completions`).

## 4) Uji Cepat melalui OpenAI Python SDK

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
Referensi:
- Integrasi SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Gunakan Model Anda Sendiri (Kompilasi dengan Olive)

Jika Anda membutuhkan model yang tidak ada di katalog, kompilasikan ke ONNX untuk Foundry Local menggunakan Olive.

Alur tingkat tinggi (lihat dokumen untuk langkah-langkah):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumen:
- Kompilasi BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Pemecahan Masalah

- Periksa status layanan dan log:
```cmd
foundry service status
foundry service diag
```
- Hapus atau pindahkan cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Perbarui ke pratinjau terbaru:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Pengalaman Pengembang Windows Terkait

- Pilihan AI lokal vs cloud di Windows, termasuk Foundry Local dan Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit dengan Foundry Local (gunakan `foundry service status` untuk mendapatkan URL endpoint chat):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Pengembang Windows Berikutnya](./windowdeveloper.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.