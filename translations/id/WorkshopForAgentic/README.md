<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:45:58+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "id"
}
-->
# 🎙️ Workshop Studio Podcast AI

> 🌏 [中文版 (Versi Bahasa Cina)](translation/zh-cn/README.md)

![logo](../../../translated_images/id/logo.8711e39dc8257d7b.png)

## Misi Anda

Selamat datang di **The AI Podcast Studio**! Anda akan memulai podcast teknologi Anda sendiri yang disebut "Future Bytes" — tapi ini ada twistnya: Anda akan membangun tim produksi bertenaga AI untuk membantu Anda membuatnya. Tidak perlu lagi berjam-jam melakukan riset, menulis naskah, dan mengedit audio. Sebagai gantinya, Anda akan memprogram cara menjadi produser podcast dengan kekuatan super AI.

## Ceritanya

Bayangkan ini: Anda dan teman-teman ingin memulai podcast tentang tren teknologi terkeren, tapi semua orang sibuk dengan sekolah, pekerjaan, atau hanya kehidupan. Bagaimana jika Anda bisa membangun tim agen AI untuk melakukan pekerjaan berat? Satu agen melakukan riset topik, satu lagi menulis naskah menarik, dan yang ketiga mengubah teks menjadi percakapan yang terdengar alami. Terasa seperti fiksi ilmiah? Mari kita buat jadi nyata.

## Apa yang Akan Anda Pelajari

Di akhir workshop ini, Anda akan tahu cara:
- 🤖 Menggunakan model AI lokal Anda sendiri (tanpa biaya API, tanpa ketergantungan cloud!)
- 🔧 Membangun agen AI khusus yang benar-benar bekerja sama
- 🎬 Membuat alur produksi podcast lengkap dari ide sampai audio

## Perjalanan Anda: Tiga Babak

![arch](../../../translated_images/id/arch.5965fe504e4a3a93.png)

Seperti cerita yang baik, kita punya tiga babak. Masing-masing membangun studio podcast AI Anda sedikit demi sedikit:

| Episode | Misi Anda | Apa yang Terjadi | Keterampilan yang Dibuka |
|---------|-----------|------------------|--------------------------|
| **Babak 1** | [Temui Asisten AI Anda](md/01.BuildAIAgentWithSLM.md) | Anda belajar cara membuat agen AI yang bisa mengobrol, mencari di web, dan bahkan memecahkan masalah. Anggap mereka seperti asisten riset yang tidak pernah tidur. | 🎯 Bangun agen pertama Anda<br>🛠️ Beri kekuatan super (alat!)<br>🧠 Ajari mereka berpikir<br>🌐 Hubungkan ke internet |
| **Babak 2** | [Susun Tim Produksi Anda](md/02.AIAgentOrchestrationAndWorkflows.md) | Sekarang jadi menarik! Anda akan mengatur beberapa agen AI untuk bekerja sama seperti tim podcast nyata. Satu riset, satu menulis, Anda menyetujui — kerjasama membuat mimpi jadi nyata. | 🎭 Koordinasi beberapa agen<br>🔄 Bangun alur kerja persetujuan<br>🖥️ Uji dengan antarmuka DevUI<br>✋ Pertahankan kontrol manusia |
| **Babak 3** | [Hidupkan Podcast Anda](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Finalnya! Ubah naskah teks Anda jadi audio podcast dengan suara realistis dan percakapan alami. Podcast "Future Bytes" Anda siap diluncurkan! | 🎤 Sulap teks ke suara<br>👥 Banyak suara pembicara<br>⏱️ Audio panjang<br>🚀 Otomasi penuh |

Setiap babak membuka kemampuan baru. Langsung lompat kalau berani, tapi kami sarankan mengikuti ceritanya!

## Persyaratan Lingkungan

Workshop ini mendukung berbagai lingkungan perangkat keras:
- **CPU**: Cocok untuk pengujian dan penggunaan skala kecil
- **GPU**: Direkomendasikan untuk lingkungan produksi, mempercepat inferensi secara signifikan
- **NPU**: Mendukung akselerasi unit pemrosesan neural generasi berikutnya

## Yang Akan Anda Butuhkan

### Checklist Perangkat Lunak ✅
- **Python 3.10+** (Bahasa pemrograman Anda)
- **Ollama** (Menjalankan model AI di mesin Anda)
- **VS Code** (Editor kode Anda)
- **Ekstensi Python** (Membuat VS Code lebih pintar)
- **Git** (Untuk mengambil kode)

### Pemeriksaan Perangkat Keras 💻
- **Bisa jalankan ini?**: RAM 8GB, ruang kosong 10GB (bisa, tapi mungkin lambat)
- **Setup ideal**: RAM 16GB+, GPU yang layak (lancar jaya!)
- **Punya NPU?**: Lebih baik! Performa generasi berikutnya terbuka 🚀

## Siapkan Studio Anda 🎬

### Langkah 1: Upgrade Python

Pastikan Anda memiliki Python 3.10 atau lebih baru:

```bash
python --version
# Harus menampilkan Python 3.10.x atau lebih tinggi
```

Belum ada Python? Dapatkan di [python.org](https://python.org) — gratis!

### Langkah 2: Dapatkan Ollama (Runner Model AI Anda)

Kunjungi [ollama.ai](https://ollama.ai) dan download Ollama untuk OS Anda. Anggap ini mesin yang menjalankan model AI lokal Anda.

Periksa apakah sudah siap:

```bash
ollama --version
```

### Langkah 3: Unduh Otak AI Anda 🧠

Saatnya mengambil model Qwen-3-8B (seperti mempekerjakan asisten AI pertama Anda):

```bash
ollama pull qwen3:8b
```

*Ini mungkin butuh beberapa menit. Waktu yang pas untuk istirahat ngopi! ☕*

### Langkah 4: Siapkan VS Code

Download [Visual Studio Code](https://code.visualstudio.com/) jika belum punya. Ini editor kode terbaik (berani bantah? 😄).

### Langkah 5: Ekstensi Python

Di VS Code:
1. Tekan `Ctrl+Shift+X` (atau `Cmd+Shift+X` di Mac)
2. Cari "Python"
3. Pasang ekstensi Python resmi dari Microsoft

### Langkah 6: Anda Siap! 🎉

Serius, Anda sudah siap bermain AI. Mari buat keajaiban AI!

### Langkah 7: Instal Microsoft Agent Framework dan Paket Terkait 📦

Pasang semua dependensi yang diperlukan untuk workshop:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Ini akan menginstal Microsoft Agent Framework dan semua paket yang dibutuhkan. Sambil ngopi ya — setup pertama bisa makan waktu beberapa menit! ☕*

## Instruksi Workshop

Struktur proyek, langkah konfigurasi, dan cara menjalankan akan dijelaskan secara rinci selama workshop.

## Pemecahan Masalah (Saat Ada Masalah) 🔧

### "Duh, unduhan model lambat banget!"
**Solusi**: Gunakan VPN atau konfigurasi Ollama dengan sumber mirror. Kadang internet kurang bersahabat.

### "Komputerk'e mati! Memori habis!"
**Solusi**: Ganti ke model yang lebih kecil atau atur `num_ctx` supaya pakai memori lebih sedikit. Anggap aja seperti mendietkan AI Anda.

### "Bisakah ini dipercepat dengan GPU saya?"
**Solusi**: Ollama otomatis mendeteksi GPU! Pastikan driver GPU Anda terbaru. Dapatkan percepatan gratis! 🏎️

## Sumber Tambahan (Untuk Yang Penasaran) 📚

- [Ollama Docs](https://github.com/ollama/ollama) — Mendalami model AI lokal
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Pelajari lebih lanjut tentang membangun tim agen
- [Info Model Qwen](https://qwenlm.github.io/) — Kenali otak asisten AI Anda

## Lisensi

Lisensi MIT — Bangun karya keren, bagikan, buat dunia lebih baik! 🌍

## Ingin Berkontribusi?

Ketik bug? Ada ide? Buat Issue atau PR! Kami suka suasana komunitas. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk menghasilkan terjemahan yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan jasa terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->