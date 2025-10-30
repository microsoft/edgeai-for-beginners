<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T13:39:22+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "id"
}
-->
# Catatan Perubahan

Semua perubahan penting pada EdgeAI untuk Pemula didokumentasikan di sini. Proyek ini menggunakan entri berbasis tanggal dan gaya Keep a Changelog (Ditambahkan, Diubah, Diperbaiki, Dihapus, Dokumentasi, Dipindahkan).

## 2025-10-30

### Ditambahkan - Peningkatan Komprehensif Modul06 AI Agents
- **Integrasi Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Bagian lengkap tentang Microsoft Agent Framework untuk pengembangan agen siap produksi
  - Pola integrasi mendetail dengan Foundry Local untuk penerapan di edge
  - Contoh orkestrasi multi-agen dengan model SLM khusus
  - Pola penerapan di perusahaan dengan manajemen sumber daya dan pemantauan
  - Fitur keamanan dan kepatuhan untuk sistem agen edge
  - Contoh implementasi nyata (ritel, kesehatan, layanan pelanggan)

- **Strategi Penerapan Agen SLM Produksi**:
  - **Foundry Local**: Dokumentasi runtime AI edge kelas perusahaan lengkap dengan instalasi, konfigurasi, dan pola produksi
  - **Ollama**: Penerapan yang berfokus pada komunitas dengan pemantauan dan manajemen model yang komprehensif
  - **VLLM**: Mesin inferensi berkinerja tinggi dengan teknik optimasi canggih dan fitur perusahaan
  - Daftar periksa penerapan produksi dan tabel perbandingan untuk ketiga platform

- **Peningkatan Kerangka Kerja SLM yang Dioptimalkan untuk Edge**:
  - **ONNX Runtime**: Bagian baru yang komprehensif untuk penerapan agen SLM lintas platform
  - Pola penerapan universal di Windows, Linux, macOS, iOS, dan Android
  - Opsi akselerasi perangkat keras (CPU, GPU, NPU) dengan deteksi otomatis
  - Fitur siap produksi dan optimasi khusus agen
  - Contoh implementasi lengkap dengan integrasi Microsoft Agent Framework

- **Referensi dan Bacaan Lebih Lanjut**:
  - Perpustakaan sumber daya komprehensif dengan lebih dari 100 sumber otoritatif
  - Makalah penelitian inti tentang agen AI dan Model Bahasa Kecil
  - Dokumentasi resmi untuk semua kerangka kerja dan alat utama
  - Laporan industri, analisis pasar, dan tolok ukur teknis
  - Sumber daya pendidikan, konferensi, dan forum komunitas
  - Standar, spesifikasi, dan kerangka kerja kepatuhan

### Diubah - Modernisasi Konten Modul06
- **Tujuan Pembelajaran yang Ditingkatkan**: Ditambahkan penguasaan Microsoft Agent Framework dan kemampuan penerapan di edge
- **Fokus Produksi**: Beralih dari panduan konseptual ke panduan siap implementasi dengan contoh produksi
- **Contoh Kode**: Semua contoh diperbarui menggunakan pola SDK modern dan praktik terbaik
- **Pola Arsitektur**: Ditambahkan arsitektur agen hierarkis dan koordinasi edge-to-cloud
- **Optimasi Kinerja**: Ditingkatkan dengan rekomendasi manajemen sumber daya dan penskalaan otomatis

### Dokumentasi - Peningkatan Struktur Modul06
- **Cakupan Kerangka Kerja Agen yang Komprehensif**: Dari konsep dasar hingga penerapan di perusahaan
- **Strategi Penerapan Produksi**: Panduan lengkap untuk Foundry Local, Ollama, dan VLLM
- **Optimasi Lintas Platform**: Ditambahkan ONNX Runtime untuk penerapan universal
- **Perpustakaan Sumber Daya**: Referensi ekstensif untuk pembelajaran dan implementasi lanjutan

### Ditambahkan - Pembaruan Dokumentasi Protokol Konteks Model (MCP) Modul06
- **Modernisasi Pengantar MCP** (`Module06/03.IntroduceMCP.md`):
  - Diperbarui dengan spesifikasi MCP terbaru dari modelcontextprotocol.io (versi 2025-06-18)
  - Ditambahkan analogi USB-C resmi untuk koneksi aplikasi AI yang terstandarisasi
  - Bagian arsitektur diperbarui dengan desain dua lapisan resmi (Lapisan Data + Lapisan Transportasi)
  - Dokumentasi primitif inti yang ditingkatkan dengan primitif server (Alat, Sumber Daya, Prompt) dan primitif klien (Sampling, Elicitation, Logging)

- **Referensi dan Sumber Daya MCP yang Komprehensif**:
  - Ditambahkan tautan **MCP untuk Pemula** (https://aka.ms/mcp-for-beginners) 
  - Dokumentasi dan spesifikasi MCP resmi (modelcontextprotocol.io)
  - Sumber daya pengembangan termasuk MCP Inspector dan implementasi referensi
  - Standar teknis (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Ditambahkan - Integrasi Qualcomm QNN Modul04
- **Bagian Baru 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Panduan komprehensif lebih dari 400 baris yang mencakup kerangka kerja inferensi AI terpadu Qualcomm
  - Cakupan mendetail tentang komputasi heterogen (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimasi yang sadar perangkat keras untuk platform Snapdragon dengan distribusi beban kerja yang cerdas
  - Teknik kuantisasi canggih (INT8, INT16, presisi campuran) untuk penerapan di perangkat seluler
  - Optimasi inferensi hemat daya untuk perangkat bertenaga baterai dan aplikasi waktu nyata
  - Panduan instalasi lengkap dengan pengaturan SDK QNN dan konfigurasi lingkungan
  - Contoh praktis: konversi PyTorch ke QNN, optimasi multi-backend, pembuatan biner konteks
  - Pola penggunaan lanjutan: konfigurasi backend khusus, kuantisasi dinamis, profil kinerja
  - Bagian pemecahan masalah yang komprehensif dan sumber daya komunitas

- **Struktur Modul04 yang Ditingkatkan**:
  - README.md diperbarui untuk mencakup 7 bagian progresif (sebelumnya 6)
  - Ditambahkan Qualcomm QNN ke tabel tolok ukur kinerja (peningkatan kecepatan 5-15x, pengurangan memori 50-80%)
  - Hasil pembelajaran yang komprehensif untuk penerapan AI seluler dan optimasi daya

### Diubah - Pembaruan Dokumentasi Modul04
- **Peningkatan dokumentasi Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Ditambahkan bagian "Repositori Resep Olive" yang mencakup lebih dari 100 resep optimasi yang telah dibuat sebelumnya
  - Cakupan mendetail tentang keluarga model yang didukung (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Contoh penggunaan praktis untuk kustomisasi resep dan kontribusi komunitas
  - Ditingkatkan dengan tolok ukur kinerja dan panduan integrasi

- **Pengurutan ulang bagian dalam Modul04**:
  - Apple MLX dipindahkan ke Bagian 5 (sebelumnya Bagian 6)
  - Workflow Synthesis dipindahkan ke Bagian 6 (sebelumnya Bagian 7)  
  - Qualcomm QNN diposisikan sebagai Bagian 7 (fokus khusus pada seluler/edge)
  - Semua referensi file dan tautan navigasi diperbarui sesuai

### Diperbaiki - Validasi Contoh Workshop
- **Validasi dan perbaikan chat_bootstrap.py**:
  - Memperbaiki pernyataan impor yang rusak (`util.util.workshop_utils` → `util.workshop_utils`)
  - Membuat `__init__.py` yang hilang di paket util untuk resolusi modul Python yang tepat
  - Menginstal dependensi yang diperlukan (openai, foundry-local-sdk) di lingkungan conda
  - Berhasil memvalidasi eksekusi contoh dengan prompt default dan kustom
  - Mengonfirmasi integrasi dengan layanan Foundry Local dan pemuatan model (phi-4-mini dengan optimasi CUDA)

### Dokumentasi - Pembaruan Panduan Komprehensif
- **README.md Modul04 restrukturisasi lengkap**:
  - Ditambahkan Qualcomm QNN sebagai kerangka kerja optimasi utama bersama OpenVINO, Olive, MLX
  - Hasil pembelajaran bab diperbarui untuk mencakup penerapan AI seluler dan optimasi daya
  - Tabel perbandingan kinerja ditingkatkan dengan metrik QNN dan kasus penggunaan seluler/edge
  - Menjaga progresi logis dari solusi perusahaan ke optimasi spesifik platform

- **Referensi silang dan navigasi**:
  - Semua tautan internal dan referensi file diperbarui untuk penomoran bagian baru
  - Deskripsi workflow synthesis ditingkatkan untuk mencakup lingkungan seluler, desktop, dan cloud
  - Ditambahkan tautan sumber daya komprehensif untuk ekosistem pengembang Qualcomm

## 2025-10-08

### Ditambahkan - Pembaruan Komprehensif Workshop
- **Penulisan ulang lengkap README.md Workshop**:
  - Ditambahkan pengantar komprehensif yang menjelaskan nilai proposisi Edge AI (privasi, kinerja, biaya)
  - Dibuat 6 tujuan pembelajaran inti dengan kompetensi yang mendetail
  - Ditambahkan tabel hasil pembelajaran dengan deliverables dan matriks kompetensi
  - Termasuk bagian keterampilan siap karir untuk relevansi industri
  - Ditambahkan panduan mulai cepat dengan prasyarat dan pengaturan 3 langkah
  - Dibuat tabel sumber daya untuk sampel Python (8 file dengan waktu eksekusi)
  - Ditambahkan tabel Jupyter notebook (8 notebook dengan tingkat kesulitan)
  - Dibuat tabel dokumentasi (7 dokumen utama dengan panduan "Gunakan Saat")
  - Ditambahkan rekomendasi jalur pembelajaran untuk tingkat keterampilan yang berbeda

- **Validasi dan infrastruktur pengujian Workshop**:
  - Dibuat `scripts/validate_samples.py` - Alat validasi komprehensif untuk sintaks, impor, dan praktik terbaik
  - Dibuat `scripts/test_samples.py` - Penguji smoke untuk semua sampel Python
  - Dokumentasi validasi ditambahkan ke `scripts/README.md`

- **Dokumentasi komprehensif**:
  - Dibuat `SAMPLES_UPDATE_SUMMARY.md` - Panduan mendetail lebih dari 400 baris yang mencakup semua peningkatan
  - Dibuat `UPDATE_COMPLETE.md` - Ringkasan eksekutif dari penyelesaian pembaruan
  - Dibuat `QUICK_REFERENCE.md` - Kartu referensi cepat untuk Workshop

### Diubah - Modernisasi Sampel Python Workshop
- **Semua 8 sampel Python diperbarui dengan praktik terbaik**:
  - Penanganan kesalahan ditingkatkan dengan blok try-except di semua operasi I/O
  - Ditambahkan petunjuk tipe dan docstring yang komprehensif
  - Menerapkan pola logging konsisten [INFO]/[ERROR]/[RESULT]
  - Melindungi impor opsional dengan petunjuk instalasi
  - Umpan balik pengguna ditingkatkan di semua sampel

- **session01/chat_bootstrap.py**:
  - Inisialisasi klien ditingkatkan dengan pesan kesalahan yang komprehensif
  - Penanganan kesalahan streaming ditingkatkan dengan validasi chunk
  - Ditambahkan penanganan pengecualian yang lebih baik untuk ketidaktersediaan layanan

- **session02/rag_pipeline.py**:
  - Ditambahkan pengamanan impor untuk sentence-transformers dengan petunjuk instalasi
  - Penanganan kesalahan ditingkatkan untuk operasi embedding dan generasi
  - Pemformatan output ditingkatkan dengan hasil terstruktur

- **session02/rag_eval_ragas.py**:
  - Melindungi impor opsional (ragas, datasets) dengan pesan kesalahan yang ramah pengguna
  - Ditambahkan penanganan kesalahan untuk metrik evaluasi
  - Pemformatan output ditingkatkan untuk hasil evaluasi

- **session03/benchmark_oss_models.py**:
  - Menerapkan degradasi yang anggun (melanjutkan pada kegagalan model)
  - Ditambahkan pelaporan kemajuan yang mendetail dan penanganan kesalahan per model
  - Perhitungan statistik ditingkatkan dengan pemulihan kesalahan yang komprehensif

- **session04/model_compare.py**:
  - Ditambahkan petunjuk tipe (Jenis pengembalian Tuple)
  - Pemformatan output ditingkatkan dengan hasil JSON terstruktur
  - Penanganan kesalahan per model diterapkan dengan pemulihan

- **session05/agents_orchestrator.py**:
  - Ditingkatkan Agent.act() dengan docstring yang komprehensif
  - Ditambahkan penanganan kesalahan pipeline dengan logging tahap demi tahap
  - Manajemen memori dan pelacakan status ditingkatkan

- **session06/models_router.py**:
  - Dokumentasi fungsi ditingkatkan untuk semua komponen routing
  - Ditambahkan logging mendetail dalam fungsi route()
  - Output pengujian ditingkatkan dengan hasil terstruktur

- **session06/models_pipeline.py**:
  - Ditambahkan penanganan kesalahan ke fungsi pembantu chat()
  - pipeline() ditingkatkan dengan logging tahap dan pelaporan kemajuan
  - main() ditingkatkan dengan pemulihan kesalahan yang komprehensif

### Dokumentasi - Peningkatan Dokumentasi Workshop
- README.md utama diperbarui dengan bagian Workshop yang menyoroti jalur pembelajaran langsung
- STUDY_GUIDE.md ditingkatkan dengan bagian Workshop yang komprehensif termasuk:
  - Tujuan pembelajaran dan area fokus studi
  - Pertanyaan penilaian diri
  - Latihan langsung dengan estimasi waktu
  - Alokasi waktu untuk studi terfokus dan paruh waktu
  - Ditambahkan Workshop ke template pelacakan kemajuan
- Panduan alokasi waktu diperbarui dari 20 jam menjadi 30 jam (termasuk Workshop)
- Deskripsi sampel Workshop dan hasil pembelajaran ditambahkan ke README

### Diperbaiki
- Pola penanganan kesalahan yang tidak konsisten di seluruh sampel Workshop
- Kesalahan impor dependensi opsional dengan pengamanan yang tepat
- Petunjuk tipe yang hilang diperbaiki di fungsi-fungsi penting
- Umpan balik pengguna yang tidak memadai dalam skenario kesalahan diperbaiki
- Masalah validasi diperbaiki dengan infrastruktur pengujian yang komprehensif

---

## 2025-09-23

### Diubah - Modernisasi Utama Modul 08
- **Penyelarasan komprehensif dengan pola repositori Microsoft Foundry-Local**
  - Semua contoh kode diperbarui menggunakan `FoundryLocalManager` modern dan integrasi SDK OpenAI
  - Panggilan manual `requests` yang usang diganti dengan penggunaan SDK yang tepat
  - Pola implementasi diselaraskan dengan dokumentasi dan sampel resmi Microsoft

- **Modernisasi 05.AIPoweredAgents.md**:
  - Orkestrasi multi-agen diperbarui menggunakan pola SDK modern
  - Implementasi koordinator ditingkatkan dengan fitur canggih (loop umpan balik, pemantauan kinerja)
  - Ditambahkan penanganan kesalahan yang komprehensif dan pemeriksaan kesehatan layanan
  - Referensi yang tepat ke sampel lokal (`samples/05/multi_agent_orchestration.ipynb`) diintegrasikan
  - Contoh pemanggilan fungsi diperbarui menggunakan parameter `tools` modern alih-alih `functions` yang usang
  - Ditambahkan pola siap produksi dengan pemantauan dan pelacakan statistik

- **Penulisan ulang lengkap 06.ModelsAsTools.md**:
  - Registri alat dasar diganti dengan implementasi router model cerdas
  - Pemilihan model berbasis kata kunci ditambahkan untuk berbagai jenis tugas (umum, penalaran, kode, kreatif)
  - Konfigurasi berbasis lingkungan diintegrasikan dengan penugasan model yang fleksibel
  - Ditingkatkan dengan pemantauan kesehatan layanan yang komprehensif dan penanganan kesalahan
  - Ditambahkan pola penerapan produksi dengan pemantauan permintaan dan pelacakan kinerja
  - Diselaraskan dengan implementasi lokal di `samples/06/router.py` dan `samples/06/model_router.ipynb`

- **Peningkatan struktur dokumentasi**:
  - Ditambahkan bagian ikhtisar yang menyoroti modernisasi dan penyelarasan SDK
  - Ditingkatkan dengan emoji dan format yang lebih baik untuk meningkatkan keterbacaan
  - Referensi yang tepat ke file sampel lokal di seluruh dokumentasi ditambahkan
  - Panduan implementasi siap produksi dan praktik terbaik disertakan

### Ditambahkan
- Bagian ikhtisar komprehensif di file Modul 08 yang menyoroti integrasi SDK modern
- Sorotan arsitektur yang menampilkan fitur canggih (sistem multi-agen, routing cerdas)
- Referensi langsung ke implementasi sampel lokal untuk pengalaman langsung
- Panduan penerapan produksi dengan pola pemantauan dan penanganan kesalahan
- Contoh Jupyter notebook interaktif dengan fitur canggih dan tolok ukur

### Diperbaiki
- Ketidaksesuaian penyelarasan antara dokumentasi dan implementasi sampel aktual
- Pola penggunaan SDK yang usang di seluruh Modul 08
- Referensi yang hilang ke perpustakaan sampel lokal yang komprehensif
- Pendekatan implementasi yang tidak konsisten di berbagai bagian

---

## 2025-09-18

### Ditambahkan
- Modul 08: Microsoft Foundry Local – Toolkit Pengembang Lengkap
  - Enam sesi: pengaturan, integrasi Azure AI Foundry, model open-source, demo mutakhir, agen, dan model sebagai alat
  - Contoh yang dapat dijalankan di bawah `Module08/samples/01`–`06` dengan instruksi cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart dengan dukungan OpenAI/Foundry Local dan Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkestrasi multi-agent (`python -m samples.05.agents.coordinator`)
    - `06` Router Models-as-Tools (`router.py`)
- Dukungan Azure OpenAI dalam contoh SDK Sesi 2 dengan konfigurasi variabel lingkungan
- `.vscode/settings.json` diarahkan ke `Module08/.venv` untuk meningkatkan resolusi analisis Python
- `.env` dengan petunjuk `PYTHONPATH` untuk kesadaran VS Code/Pylance

### Diubah
- Model default diperbarui ke `phi-4-mini` di seluruh dokumen dan contoh Module 08; menghapus sisa referensi `phi-3.5` dalam Module 08
- Peningkatan Router (`Module08/samples/06/router.py`):
  - Penemuan endpoint melalui `foundry service status` dengan parsing regex
  - Pemeriksaan kesehatan `/v1/models` saat startup
  - Registri model yang dapat dikonfigurasi melalui lingkungan (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Persyaratan diperbarui: `Module08/requirements.txt` sekarang mencakup `openai` (bersama dengan `requests`, `chainlit`)
- Panduan contoh Chainlit diperjelas dan penanganan masalah ditambahkan; resolusi impor melalui pengaturan workspace

### Diperbaiki
- Masalah impor diselesaikan:
  - Router tidak lagi bergantung pada modul `utils` yang tidak ada; fungsi diintegrasikan langsung
  - Koordinator menggunakan impor relatif (`from .specialists import ...`) dan dijalankan melalui jalur modul
  - Konfigurasi VS Code/Pylance untuk menyelesaikan impor `chainlit` dan paket
- Typo kecil diperbaiki dalam `STUDY_GUIDE.md` dan cakupan Module 08 ditambahkan

### Dihapus
- Menghapus `Module08/infra/obs.py` yang tidak digunakan dan menghapus direktori `infra/` yang kosong; pola observabilitas tetap sebagai opsional dalam dokumen

### Dipindahkan
- Demo Module 08 dikonsolidasikan di bawah `Module08/samples` dengan folder bernomor sesi
  - Memindahkan aplikasi Chainlit ke `samples/04`
  - Memindahkan agen ke `samples/05` dan menambahkan file `__init__.py` untuk resolusi paket

### Dokumen
- Dokumen sesi Module 08 dan semua README contoh diperkaya dengan referensi Microsoft Learn dan vendor terpercaya
- `Module08/README.md` diperbarui dengan Ikhtisar Contoh, konfigurasi router, dan tips validasi
- Bagian Foundry Local Windows dalam `Module07/README.md` divalidasi terhadap dokumen Learn
- `STUDY_GUIDE.md` diperbarui:
  - Menambahkan Module 08 ke ikhtisar, jadwal, pelacak kemajuan
  - Menambahkan bagian Referensi yang komprehensif (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Sejarah (ringkasan)
- Arsitektur kursus dan modul ditetapkan (Module 01–07)
- Modernisasi konten secara iteratif, standarisasi format, dan penambahan studi kasus
- Cakupan kerangka kerja optimasi diperluas (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Belum Dirilis / Backlog (usulan)
- Pengujian smoke opsional per contoh untuk memvalidasi ketersediaan Foundry Local
- Tinjau terjemahan untuk menyelaraskan referensi model (misalnya, `phi-4-mini`) jika sesuai
- Tambahkan konfigurasi pyright minimal jika tim lebih memilih keketatan di seluruh workspace

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.