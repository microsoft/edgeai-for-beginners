# Sesi 6 Contoh: Model sebagai Alat

Contoh ini mengimplementasikan router minimal + registri alat yang memilih model berdasarkan prompt pengguna dan memanggil endpoint Foundry Local yang kompatibel dengan OpenAI.

## File
- `router.py`: registri sederhana dan routing heuristik; penemuan endpoint + pemeriksaan kesehatan.

## Jalankan (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Catatan
- Router menggunakan heuristik kata kunci sederhana untuk memilih antara alat `general`, `reasoning`, dan `code` serta mencetak `/v1/models` saat memulai.
- Konfigurasi melalui variabel lingkungan:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## Referensi
- Foundry Local (Pelajari): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrasi dengan SDK inferensi: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.