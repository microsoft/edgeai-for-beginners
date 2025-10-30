<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T13:43:35+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ms"
}
-->
# Log Perubahan

Semua perubahan penting pada EdgeAI untuk Pemula didokumentasikan di sini. Projek ini menggunakan entri berdasarkan tarikh dan gaya Keep a Changelog (Ditambah, Diubah, Diperbaiki, Dihapus, Dokumen, Dipindahkan).

## 2025-10-30

### Ditambah - Peningkatan Komprehensif Modul06 AI Agents
- **Integrasi Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Bahagian lengkap mengenai Microsoft Agent Framework untuk pembangunan agen yang sedia untuk produksi
  - Corak integrasi terperinci dengan Foundry Local untuk pengedaran di edge
  - Contoh orkestrasi multi-agen dengan model SLM khusus
  - Corak pengedaran perusahaan dengan pengurusan sumber dan pemantauan
  - Ciri keselamatan dan pematuhan untuk sistem agen edge
  - Contoh pelaksanaan dunia nyata (peruncitan, penjagaan kesihatan, perkhidmatan pelanggan)

- **Strategi Pengedaran Agen SLM Produksi**:
  - **Foundry Local**: Dokumentasi runtime AI edge kelas perusahaan lengkap dengan pemasangan, konfigurasi, dan corak pengedaran produksi
  - **Ollama**: Pengedaran yang fokus kepada komuniti dengan pemantauan dan pengurusan model yang komprehensif
  - **VLLM**: Enjin inferens berprestasi tinggi dengan teknik pengoptimuman maju dan ciri perusahaan
  - Senarai semak pengedaran produksi dan jadual perbandingan untuk ketiga-tiga platform

- **Peningkatan Rangka Kerja SLM yang Dioptimumkan untuk Edge**:
  - **ONNX Runtime**: Bahagian baru yang komprehensif untuk pengedaran agen SLM merentas platform
  - Corak pengedaran universal di Windows, Linux, macOS, iOS, dan Android
  - Pilihan pecutan perkakasan (CPU, GPU, NPU) dengan pengesanan automatik
  - Ciri sedia produksi dan pengoptimuman khusus agen
  - Contoh pelaksanaan lengkap dengan integrasi Microsoft Agent Framework

- **Rujukan dan Bacaan Lanjut**:
  - Perpustakaan sumber yang komprehensif dengan lebih 100 sumber yang berwibawa
  - Kertas penyelidikan utama mengenai agen AI dan Model Bahasa Kecil
  - Dokumentasi rasmi untuk semua rangka kerja dan alat utama
  - Laporan industri, analisis pasaran, dan penanda aras teknikal
  - Sumber pendidikan, persidangan, dan forum komuniti
  - Piawaian, spesifikasi, dan rangka kerja pematuhan

### Diubah - Pemodenan Kandungan Modul06
- **Objektif Pembelajaran yang Ditingkatkan**: Ditambah penguasaan Microsoft Agent Framework dan keupayaan pengedaran edge
- **Fokus Produksi**: Beralih daripada konsep kepada panduan sedia pelaksanaan dengan contoh produksi
- **Contoh Kod**: Dikemas kini semua contoh untuk menggunakan corak SDK moden dan amalan terbaik
- **Corak Seni Bina**: Ditambah seni bina agen hierarki dan koordinasi edge-ke-cloud
- **Pengoptimuman Prestasi**: Ditingkatkan dengan cadangan pengurusan sumber dan penskalaan automatik

### Dokumen - Peningkatan Struktur Modul06
- **Liputan Rangka Kerja Agen yang Komprehensif**: Dari konsep asas hingga pengedaran perusahaan
- **Strategi Pengedaran Produksi**: Panduan lengkap untuk Foundry Local, Ollama, dan VLLM
- **Pengoptimuman Merentas Platform**: Ditambah ONNX Runtime untuk pengedaran universal
- **Perpustakaan Sumber**: Rujukan yang luas untuk pembelajaran dan pelaksanaan berterusan

### Ditambah - Kemas Kini Dokumentasi Protokol Konteks Model (MCP) Modul06
- **Pemodenan Pengenalan MCP** (`Module06/03.IntroduceMCP.md`):
  - Dikemas kini dengan spesifikasi MCP terkini dari modelcontextprotocol.io (versi 2025-06-18)
  - Ditambah analogi USB-C rasmi untuk sambungan aplikasi AI yang standard
  - Dikemas kini bahagian seni bina dengan reka bentuk dua lapisan rasmi (Lapisan Data + Lapisan Pengangkutan)
  - Ditingkatkan dokumentasi primitif teras dengan primitif pelayan (Alat, Sumber, Prompts) dan primitif klien (Sampling, Elicitation, Logging)

- **Rujukan dan Sumber MCP yang Komprehensif**:
  - Ditambah pautan **MCP untuk Pemula** (https://aka.ms/mcp-for-beginners)
  - Dokumentasi dan spesifikasi MCP rasmi (modelcontextprotocol.io)
  - Sumber pembangunan termasuk MCP Inspector dan pelaksanaan rujukan
  - Piawaian teknikal (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Ditambah - Integrasi Qualcomm QNN Modul04
- **Bahagian Baru 7: Suite Pengoptimuman Qualcomm QNN** (`Module04/05.QualcommQNN.md`):
  - Panduan komprehensif 400+ baris yang merangkumi rangka kerja inferens AI bersatu Qualcomm
  - Liputan terperinci pengkomputeran heterogen (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Pengoptimuman yang sedar perkakasan untuk platform Snapdragon dengan pengagihan beban kerja yang pintar
  - Teknik kuantisasi maju (INT8, INT16, ketepatan campuran) untuk pengedaran mudah alih
  - Pengoptimuman inferens yang cekap tenaga untuk peranti berkuasa bateri dan aplikasi masa nyata
  - Panduan pemasangan lengkap dengan persediaan SDK QNN dan konfigurasi persekitaran
  - Contoh praktikal: Penukaran PyTorch ke QNN, pengoptimuman multi-backend, penjanaan binari konteks
  - Corak penggunaan maju: konfigurasi backend khusus, kuantisasi dinamik, profil prestasi
  - Bahagian penyelesaian masalah yang komprehensif dan sumber komuniti

- **Struktur Modul04 yang Ditingkatkan**:
  - Dikemas kini README.md untuk memasukkan 7 bahagian progresif (dahulu 6)
  - Ditambah Qualcomm QNN ke jadual penanda aras prestasi (peningkatan kelajuan 5-15x, pengurangan memori 50-80%)
  - Hasil pembelajaran yang komprehensif untuk pengedaran AI mudah alih dan pengoptimuman kuasa

### Diubah - Kemas Kini Dokumentasi Modul04
- **Peningkatan dokumentasi Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Ditambah bahagian "Repositori Resipi Olive" yang komprehensif merangkumi 100+ resipi pengoptimuman pra-bina
  - Liputan terperinci keluarga model yang disokong (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Contoh penggunaan praktikal untuk penyesuaian resipi dan sumbangan komuniti
  - Ditingkatkan dengan penanda aras prestasi dan panduan integrasi

- **Penyusunan semula bahagian dalam Modul04**:
  - Apple MLX dipindahkan ke Bahagian 5 (dahulu Bahagian 6)
  - Sintesis Alur Kerja dipindahkan ke Bahagian 6 (dahulu Bahagian 7)
  - Qualcomm QNN diposisikan sebagai Bahagian 7 (fokus mudah alih/edge khusus)
  - Dikemas kini semua rujukan fail dan pautan navigasi dengan sewajarnya

### Diperbaiki - Pengesahan Sampel Bengkel
- **pengesahan dan pembaikan chat_bootstrap.py**:
  - Diperbaiki pernyataan import yang rosak (`util.util.workshop_utils` → `util.workshop_utils`)
  - Dicipta `__init__.py` yang hilang dalam pakej util untuk resolusi modul Python yang betul
  - Dipasang kebergantungan yang diperlukan (openai, foundry-local-sdk) dalam persekitaran conda
  - Sampel pelaksanaan berjaya disahkan dengan prompt lalai dan tersuai
  - Pengesahan integrasi dengan perkhidmatan Foundry Local dan pemuatan model (phi-4-mini dengan pengoptimuman CUDA)

### Dokumen - Kemas Kini Panduan Komprehensif
- **Penyusunan semula README.md Modul04 sepenuhnya**:
  - Ditambah Qualcomm QNN sebagai rangka kerja pengoptimuman utama bersama OpenVINO, Olive, MLX
  - Dikemas kini hasil pembelajaran bab untuk memasukkan pengedaran AI mudah alih dan pengoptimuman kuasa
  - Ditingkatkan jadual perbandingan prestasi dengan metrik QNN dan kes penggunaan mudah alih/edge
  - Mengekalkan perkembangan logik dari penyelesaian perusahaan ke pengoptimuman khusus platform

- **Rujukan silang dan navigasi**:
  - Dikemas kini semua pautan dalaman dan rujukan fail untuk penomboran bahagian baru
  - Ditingkatkan penerangan sintesis alur kerja untuk memasukkan persekitaran mudah alih, desktop, dan cloud
  - Ditambah pautan sumber yang komprehensif untuk ekosistem pembangun Qualcomm

## 2025-10-08

### Ditambah - Kemas Kini Komprehensif Bengkel
- **Penulisan semula README.md Bengkel sepenuhnya**:
  - Ditambah pengenalan komprehensif yang menerangkan nilai tambah Edge AI (privasi, prestasi, kos)
  - Dicipta 6 objektif pembelajaran teras dengan kecekapan terperinci
  - Ditambah jadual hasil pembelajaran dengan deliverables dan matriks kecekapan
  - Termasuk bahagian kemahiran sedia kerjaya untuk relevansi industri
  - Ditambah panduan permulaan cepat dengan prasyarat dan persediaan 3 langkah
  - Dicipta jadual sumber untuk sampel Python (8 fail dengan masa pelaksanaan)
  - Ditambah jadual Jupyter notebooks (8 notebooks dengan penilaian kesukaran)
  - Dicipta jadual dokumentasi (7 dokumen utama dengan panduan "Gunakan Bila")
  - Ditambah cadangan laluan pembelajaran untuk tahap kemahiran yang berbeza

- **Infrastruktur pengesahan dan ujian Bengkel**:
  - Dicipta `scripts/validate_samples.py` - Alat pengesahan komprehensif untuk sintaks, import, dan amalan terbaik
  - Dicipta `scripts/test_samples.py` - Pelari ujian pantas untuk semua sampel Python
  - Ditambah dokumentasi pengesahan ke `scripts/README.md`

- **Dokumentasi komprehensif**:
  - Dicipta `SAMPLES_UPDATE_SUMMARY.md` - Panduan terperinci 400+ baris yang merangkumi semua peningkatan
  - Dicipta `UPDATE_COMPLETE.md` - Ringkasan eksekutif penyelesaian kemas kini
  - Dicipta `QUICK_REFERENCE.md` - Kad rujukan cepat untuk Bengkel

### Diubah - Pemodenan Sampel Python Bengkel
- **Semua 8 sampel Python dikemas kini dengan amalan terbaik**:
  - Ditingkatkan pengendalian ralat dengan blok try-except di semua operasi I/O
  - Ditambah petunjuk jenis dan docstrings yang komprehensif
  - Melaksanakan corak log yang konsisten [INFO]/[ERROR]/[RESULT]
  - Melindungi import pilihan dengan petunjuk pemasangan
  - Meningkatkan maklum balas pengguna di semua sampel

- **session01/chat_bootstrap.py**:
  - Ditingkatkan inisialisasi klien dengan mesej ralat yang komprehensif
  - Meningkatkan pengendalian ralat streaming dengan pengesahan chunk
  - Ditambah pengendalian pengecualian yang lebih baik untuk perkhidmatan yang tidak tersedia

- **session02/rag_pipeline.py**:
  - Ditambah pengawal import untuk sentence-transformers dengan petunjuk pemasangan
  - Meningkatkan pengendalian ralat untuk operasi embedding dan generasi
  - Meningkatkan pemformatan output dengan hasil yang terstruktur

- **session02/rag_eval_ragas.py**:
  - Melindungi import pilihan (ragas, datasets) dengan mesej ralat mesra pengguna
  - Ditambah pengendalian ralat untuk metrik penilaian
  - Meningkatkan pemformatan output untuk hasil penilaian

- **session03/benchmark_oss_models.py**:
  - Melaksanakan degradasi yang anggun (teruskan pada kegagalan model)
  - Ditambah pelaporan kemajuan terperinci dan pengendalian ralat per-model
  - Meningkatkan pengiraan statistik dengan pemulihan ralat yang komprehensif

- **session04/model_compare.py**:
  - Ditambah petunjuk jenis (Jenis Tuple)
  - Meningkatkan pemformatan output dengan hasil JSON yang terstruktur
  - Melaksanakan pengendalian ralat per-model dengan pemulihan

- **session05/agents_orchestrator.py**:
  - Ditingkatkan Agent.act() dengan docstrings yang komprehensif
  - Ditambah pengendalian ralat pipeline dengan log tahap demi tahap
  - Meningkatkan pengurusan memori dan penjejakan keadaan

- **session06/models_router.py**:
  - Ditingkatkan dokumentasi fungsi untuk semua komponen routing
  - Ditambah log terperinci dalam fungsi route()
  - Meningkatkan output ujian dengan hasil yang terstruktur

- **session06/models_pipeline.py**:
  - Ditambah pengendalian ralat pada fungsi pembantu chat()
  - Meningkatkan pipeline() dengan log tahap dan pelaporan kemajuan
  - Meningkatkan main() dengan pemulihan ralat yang komprehensif

### Dokumen - Peningkatan Dokumentasi Bengkel
- Dikemas kini README.md utama dengan bahagian Bengkel yang menonjolkan laluan pembelajaran hands-on
- Ditingkatkan STUDY_GUIDE.md dengan bahagian Bengkel yang komprehensif termasuk:
  - Objektif pembelajaran dan kawasan fokus kajian
  - Soalan penilaian diri
  - Latihan hands-on dengan anggaran masa
  - Peruntukan masa untuk kajian intensif dan separuh masa
  - Ditambah Bengkel ke templat penjejakan kemajuan
- Dikemas kini panduan peruntukan masa dari 20 jam ke 30 jam (termasuk Bengkel)
- Ditambah penerangan sampel Bengkel dan hasil pembelajaran ke README

### Diperbaiki
- Menyelesaikan corak pengendalian ralat yang tidak konsisten di semua sampel Bengkel
- Diperbaiki ralat import kebergantungan pilihan dengan pengawal yang betul
- Membetulkan petunjuk jenis yang hilang dalam fungsi kritikal
- Menangani maklum balas pengguna yang tidak mencukupi dalam senario ralat
- Diperbaiki isu pengesahan dengan infrastruktur ujian yang komprehensif

---

## 2025-09-23

### Diubah - Pemodenan Utama Modul 08
- **Penyelarasan komprehensif dengan corak repositori Microsoft Foundry-Local**
  - Dikemas kini semua contoh kod untuk menggunakan `FoundryLocalManager` moden dan integrasi SDK OpenAI
  - Menggantikan panggilan manual `requests` yang usang dengan penggunaan SDK yang betul
  - Menyelaraskan corak pelaksanaan dengan dokumentasi rasmi Microsoft dan sampel

- **Pemodenan 05.AIPoweredAgents.md**:
  - Dikemas kini orkestrasi multi-agen untuk menggunakan corak SDK moden
  - Meningkatkan pelaksanaan penyelaras dengan ciri maju (gelung maklum balas, pemantauan prestasi)
  - Ditambah pengendalian ralat yang komprehensif dan pemeriksaan kesihatan perkhidmatan
  - Mengintegrasikan rujukan yang betul kepada sampel tempatan (`samples/05/multi_agent_orchestration.ipynb`)
  - Dikemas kini contoh panggilan fungsi untuk menggunakan parameter `tools` moden dan bukannya `functions` yang usang
  - Ditambah corak sedia produksi dengan pemantauan dan penjejakan statistik

- **Penulisan semula lengkap 06.ModelsAsTools.md**:
  - Menggantikan pendaftaran alat asas dengan pelaksanaan router model pintar
  - Ditambah pemilihan model berdasarkan kata kunci untuk jenis tugas yang berbeza (umum, penaakulan, kod, kreatif)
  - Mengintegrasikan konfigurasi berdasarkan persekitaran dengan penugasan model yang fleksibel
  - Ditingkatkan dengan pemantauan kesihatan perkhidmatan yang komprehensif dan pengendalian ralat
  - Ditambah corak pengedaran produksi dengan pemantauan permintaan dan penjejakan prestasi
  - Menyelaraskan dengan pelaksanaan tempatan dalam `samples/06/router.py` dan `samples/06/model_router.ipynb`

- **Peningkatan struktur dokumentasi**:
  - Ditambah bahagian gambaran keseluruhan yang menonjolkan pemodenan dan penyelarasan SDK
  - Ditingkatkan dengan emoji dan pemformatan yang lebih baik untuk meningkatkan kebolehbacaan
  - Ditambah rujukan yang betul kepada fail sampel tempatan di seluruh dokumentasi
  - Termasuk panduan pelaksanaan sedia produksi dan amalan terbaik

### Ditambah
- Bahagian gambaran keseluruhan yang komprehensif dalam fail Modul 08 yang menonjolkan integrasi SDK moden
- Sorotan seni bina yang mempamerkan ciri maju (sistem multi-agen, routing pintar)
- Rujukan langsung kepada pelaksanaan sampel tempatan untuk pengalaman hands-on
- Panduan pengedaran produksi dengan corak pemantauan dan pengendalian ralat
- Contoh Jupyter notebook interaktif dengan ciri maju dan penanda aras

### Diperbaiki
- Ketidakkonsistenan penyelarasan antara dokumentasi dan pelaksanaan sampel sebenar
- Corak penggunaan SDK yang usang di seluruh Modul 08
- Rujukan yang hilang kepada perpustakaan sampel tempatan yang komprehensif
- Pendekatan pelaksanaan yang tidak konsisten di bahagian yang berbeza

---

## 2025-09
  - Sampel boleh dijalankan di bawah `Module08/samples/01`–`06` dengan arahan cmd Windows
    - `01` REST sembang pantas (`chat_quickstart.py`)
    - `02` SDK permulaan pantas dengan sokongan OpenAI/Foundry Local dan Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI senarai-dan-uji (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkestrasi multi-ejen (`python -m samples.05.agents.coordinator`)
    - `06` Router Model-sebagai-Alat (`router.py`)
- Sokongan Azure OpenAI dalam sampel SDK Sesi 2 dengan konfigurasi pembolehubah persekitaran
- `.vscode/settings.json` menunjuk kepada `Module08/.venv` dan meningkatkan resolusi analisis Python
- `.env` dengan petunjuk `PYTHONPATH` untuk kesedaran VS Code/Pylance

### Berubah
- Model lalai dikemas kini kepada `phi-4-mini` di seluruh dokumen dan sampel Modul 08; menghapuskan sebutan `phi-3.5` yang tinggal dalam Modul 08
- Penambahbaikan Router (`Module08/samples/06/router.py`):
  - Penemuan titik akhir melalui `foundry service status` dengan parsing regex
  - Pemeriksaan kesihatan `/v1/models` semasa permulaan
  - Pendaftaran model yang boleh dikonfigurasi melalui persekitaran (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Keperluan dikemas kini: `Module08/requirements.txt` kini termasuk `openai` (bersama `requests`, `chainlit`)
- Panduan sampel Chainlit diperjelaskan dan penyelesaian masalah ditambah; resolusi import melalui tetapan ruang kerja

### Diperbaiki
- Isu import diselesaikan:
  - Router tidak lagi bergantung pada modul `utils` yang tidak wujud; fungsi dimasukkan secara langsung
  - Koordinator menggunakan import relatif (`from .specialists import ...`) dan dipanggil melalui laluan modul
  - Konfigurasi VS Code/Pylance untuk menyelesaikan import `chainlit` dan pakej
- Pembetulan typo kecil dalam `STUDY_GUIDE.md` dan menambah liputan Modul 08

### Dihapuskan
- Menghapuskan `Module08/infra/obs.py` yang tidak digunakan dan menghapuskan direktori `infra/` yang kosong; corak pemerhatian dikekalkan sebagai pilihan dalam dokumen

### Dipindahkan
- Demo Modul 08 disatukan di bawah `Module08/samples` dengan folder bernombor sesi
  - Memindahkan aplikasi Chainlit ke `samples/04`
  - Memindahkan ejen ke `samples/05` dan menambah fail `__init__.py` untuk resolusi pakej

### Dokumen
- Dokumen sesi Modul 08 dan semua README sampel diperkaya dengan rujukan Microsoft Learn dan vendor yang dipercayai
- `Module08/README.md` dikemas kini dengan Gambaran Keseluruhan Sampel, konfigurasi router, dan petua pengesahan
- Bahagian Foundry Local Windows dalam `Module07/README.md` disahkan terhadap dokumen Learn
- `STUDY_GUIDE.md` dikemas kini:
  - Menambah Modul 08 kepada gambaran keseluruhan, jadual, penjejak kemajuan
  - Menambah bahagian Rujukan yang komprehensif (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Sejarah (ringkasan)
- Seni bina kursus dan modul ditubuhkan (Modul 01–07)
- Pemodenan kandungan secara iteratif, penyeragaman format, dan penambahan kajian kes
- Liputan rangka kerja pengoptimuman diperluaskan (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Belum Dikeluarkan / Tertunda (cadangan)
- Ujian asap pilihan per sampel untuk mengesahkan ketersediaan Foundry Local
- Semak terjemahan untuk menyelaraskan rujukan model (contohnya, `phi-4-mini`) di mana sesuai
- Tambah konfigurasi pyright minimum jika pasukan lebih suka ketegasan seluruh ruang kerja

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.