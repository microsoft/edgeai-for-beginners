<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:50:12+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "ms"
}
-->
# 🎙️ Bengkel Studio Podcast AI

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.ms.png)

## Tugas Anda

Selamat datang di **Studio Podcast AI**! Anda akan melancarkan podcast teknologi anda sendiri bernama "Byte Masa Depan" — tetapi ada satu perubahan: anda akan membina sebuah pasukan pengeluaran yang dijana AI untuk membantu anda membuatnya. Tidak perlu lagi penyelidikan tanpa henti, penulisan skrip, dan penyuntingan audio. Sebaliknya, anda akan menjadi penerbit podcast dengan kuasa AI melalui pengaturcaraan.

## Latar Cerita

Bayangkan: anda dan rakan ingin memulakan podcast tentang trend teknologi paling menarik, tetapi semua orang sibuk belajar, bekerja, atau menjalani kehidupan. Bagaimana jika anda boleh membina satu pasukan agen AI untuk mengendalikan kerja berat? Satu agen bertanggungjawab menyelidik topik, satu lagi menulis skrip yang menarik, satu lagi menukar teks kepada dialog yang lancar dan semula jadi. Kedengaran seperti fiksyen sains? Mari kita jadikannya realiti.

## Apa yang Anda Akan Pelajari

Pada akhir bengkel ini, anda akan tahu cara untuk:
- 🤖 Melancarkan model AI tempatan anda sendiri (tiada kos API, tiada kebergantungan awan!)
- 🔧 Membina agen AI profesional yang bekerja sama secara praktikal
- 🎬 Mencipta proses pengeluaran podcast lengkap dari idea ke audio

## Perjalanan Anda: Tiga Babak

Seperti mana-mana cerita yang bagus, kami mempunyai tiga babak. Setiap babak akan secara berperingkat membina Studio Podcast AI anda:

| Babak | Tugas Anda | Apa Yang Berlaku | Kemahiran Dibuka Kunci |
|---------|-----------|--------------|----------------|
| **Babak Pertama** | [Kenali Pembantu AI Anda](01.BuildAIAgentWithSLM.md) | Anda akan belajar bagaimana untuk mencipta agen AI yang boleh bersembang, mencari maklumat internet, dan menyelesaikan masalah. Bayangkannya sebagai pelatih penyelidik yang tidak pernah tidur. | 🎯 Membina agen pertama anda<br>🛠️ Memberi kuasa (alat!)<br>🧠 Mengajarnya berfikir<br>🌐 Sambungkan ke internet |
| **Babak Kedua** | [Bina Pasukan Pengeluaran Anda](02.AIAgentOrchestrationAndWorkflows.md) | Sekarang ia menjadi menarik! Anda akan mengaturkan beberapa agen AI bekerja bersama seperti pasukan podcast sebenar. Satu menyelidik, satu menulis, anda menyemak—kerjasama membuat impian menjadi kenyataan. | 🎭 Menyelaras pelbagai agen<br>🔄 Membina alir kerja kelulusan<br>🖥️ Ujian menggunakan antara muka DevUI<br>✋ Kekalkan kawalan manusia |
| **Babak Ketiga** | [Hidupkan Podcast Anda](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Penutup! Tukarkan skrip teks anda menjadi audio podcast sebenar dengan suara nyata dan perbualan semula jadi. Podcast "Byte Masa Depan" anda sudah bersedia untuk dilancarkan! | 🎤 Magik teks ke suara<br>👥 Suara berbilang pencerita<br>⏱️ Audio format panjang<br>🚀 Automasi sepenuhnya |

Setiap babak membuka kemahiran baru. Jika anda cukup berani, anda boleh melompat tetapi kami sarankan belajar secara berurutan!

## Keperluan Persekitaran

Bengkel ini menyokong pelbagai persekitaran perkakasan:
- **CPU**: Sesuai untuk ujian dan penggunaan kecil
- **GPU**: Disyorkan untuk persekitaran produksi, meningkatkan kelajuan inferens dengan ketara
- **NPU**: Menyokong pemecut pemprosesan neural generasi akan datang

## Apa yang Anda Perlukan

### Senarai Perisian ✅
- **Python 3.10+** (bahasa pengaturcaraan anda)
- **Ollama** (menjalankan model AI pada mesin anda)
- **VS Code** (penyunting kod anda)
- **Sambungan Python** (membuat VS Code lebih pintar)
- **Git** (untuk mendapatkan kod)

### Semakan Perkakasan 💻
- **Bolehkah saya jalankan?**: 8GB RAM, 10GB ruang tersedia (boleh guna, mungkin agak perlahan)
- **Konfigurasi ideal**: 16GB+ RAM, GPU yang baik (jalan lancar!)
- **Ada NPU?**: Lebih bagus lagi! Membuka potensi prestasi generasi seterusnya 🚀

## Memasang Studio Anda 🎬

### Langkah 1: Kemas Kini Python

Pastikan anda ada Python 3.10 atau lebih baru:

```bash
python --version
# Harus menunjukkan Python 3.10.x atau versi yang lebih tinggi
```

Tiada Python? Dapatkan dari [python.org](https://python.org) — ia percuma!

### Langkah 2: Dapatkan Ollama (penjalankan model AI anda)

Lawati [ollama.ai](https://ollama.ai) untuk muat turun Ollama yang sesuai dengan sistem operasi anda. Fikirkan ia sebagai enjin untuk menjalankan model AI secara tempatan.

Semak kesiapan:

```bash
ollama --version
```

### Langkah 3: Muat Turun Otak AI Anda 🧠

Masa untuk dapatkan model Qwen-3-8B (seperti mengupah pembantu AI pertama anda):

```bash
ollama pull qwen3:8b
```

*Ini mungkin mengambil beberapa minit. Masa terbaik untuk secawan kopi! ☕*

### Langkah 4: Pasang VS Code

Jika belum ada, dapatkan [Visual Studio Code](https://code.visualstudio.com/). Ini ialah penyunting kod terbaik (cuba tandingi 😄).

### Langkah 5: Sambungan Python

Dalam VS Code:
1. Tekan `Ctrl+Shift+X` (Mac `Cmd+Shift+X`)
2. Cari "Python"
3. Pasang sambungan Python rasmi dari Microsoft

### Langkah 6: Bersedia! 🎉

Betul-betul siap sekarang. Mari bina sihir AI!

### Langkah 7: Pasang Microsoft Agent Framework dan Pek Berkaitan 📦

Pasang segala kebergantungan untuk bengkel:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Ini akan pasang Microsoft Agent Framework dan semua pek perlu. Minum kopi — pemasangan pertama mungkin ambil masa! ☕*

## Arahan Bengkel

Struktur projek, langkah konfigurasi, dan cara menjalankan akan diajar satu persatu semasa bengkel.

## Penyelesaian Masalah (Jika Ada Masalah) 🔧

### "Alamak, muat turun model terlalu perlahan!"
**Penyelesaian**: Gunakan VPN atau konfigurasikan sumber cermin Ollama. Kadang-kadang rangkaian perlahan.

### "Komputer saya hampir hang! RAM tak cukup!"
**Penyelesaian**: Tukar ke model lebih kecil atau laraskan tetapan `num_ctx` untuk guna kurang RAM. Bayangkan beri diet kepada AI anda.

### "Bolehkah saya guna GPU untuk lebih laju?"
**Penyelesaian**: Ollama automatik kesan GPU! Pastikan pemandu GPU anda terkini. Peningkatan kelajuan percuma! 🏎️

## Sumber Tambahan (Untuk Anda Yang Ingin Tahu Lebih) 📚

- [Dokumentasi Ollama](https://github.com/ollama/ollama) — Dalami model AI tempatan
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Ketahui lebih tentang bina pasukan agen
- [Maklumat Model Qwen](https://qwenlm.github.io/) — Kenali otak pembantu AI anda

## Lesen

Lesen MIT — Bina benda hebat, kongsi, dan buat dunia lebih baik! 🌍

## Mahu Menyumbang?

Jumpa bug? Ada idea? Buat Isu atau PR! Kami suka komuniti yang aktif. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber rasmi. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah interpretasi yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->