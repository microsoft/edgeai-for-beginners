# Sesi 6 Contoh: Model sebagai Alat

Contoh ini melaksanakan router + pendaftaran alat yang minimum, yang memilih model berdasarkan arahan pengguna dan memanggil endpoint Foundry Local yang serasi dengan OpenAI.

## Fail
- `router.py`: pendaftaran ringkas dan penghalaan heuristik; penemuan endpoint + pemeriksaan kesihatan.

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

## Nota
- Router menggunakan heuristik kata kunci ringkas untuk memilih antara alat `general`, `reasoning`, dan `code` serta mencetak `/v1/models` semasa permulaan.
- Konfigurasi melalui pembolehubah persekitaran:
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

## Rujukan
- Foundry Local (Belajar): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrasi dengan SDK inferens: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.