# Bab 07: Contoh EdgeAI

Edge AI menggabungkan kecerdasan buatan dengan pengkomputeran tepi, membolehkan pemprosesan pintar terus pada peranti tanpa bergantung kepada sambungan awan. Bab ini meneroka lima pelaksanaan EdgeAI yang berbeza merentasi pelbagai platform dan rangka kerja, menunjukkan kepelbagaian dan kekuatan menjalankan model AI di tepi.

## 1. EdgeAI dalam NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano merupakan satu kejayaan dalam pengkomputeran AI tepi yang mudah diakses, memberikan sehingga 67 TOPS prestasi AI dalam bentuk yang padat, bersaiz kad kredit. Platform AI tepi yang berkuasa ini mendemokrasikan pembangunan AI generatif untuk peminat, pelajar, dan pembangun profesional.

### Ciri Utama
- Memberikan sehingga 67 TOPS prestasi AI—peningkatan 1.7X berbanding pendahulunya
- 1024 teras CUDA dan sehingga 32 Tensor Cores untuk pemprosesan AI
- CPU Arm Cortex-A78AE v8.2 64-bit 6-teras dengan frekuensi maksimum 1.5 GHz
- Harga hanya $249, menyediakan platform yang paling mampu milik dan mudah diakses untuk pembangun, pelajar, dan pencipta

### Aplikasi
Jetson Orin Nano cemerlang dalam menjalankan model AI generatif moden termasuk transformer penglihatan, model bahasa besar, dan model penglihatan-bahasa. Ia direka khusus untuk kes penggunaan GenAI dan kini anda boleh menjalankan beberapa LLM pada peranti bersaiz tapak tangan. Kes penggunaan popular termasuk robotik berkuasa AI, dron pintar, kamera pintar, dan peranti tepi autonomi.

**Ketahui Lebih Lanjut**: [Superkomputer Jetson Orin Nano NVIDIA: Perkara Besar Seterusnya dalam EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI dalam Aplikasi Mudah Alih dengan .NET MAUI dan ONNX Runtime GenAI

Penyelesaian ini menunjukkan cara mengintegrasikan AI Generatif dan Model Bahasa Besar (LLM) ke dalam aplikasi mudah alih merentas platform menggunakan .NET MAUI (Multi-platform App UI) dan ONNX Runtime GenAI. Pendekatan ini membolehkan pembangun .NET membina aplikasi mudah alih berkuasa AI yang berjalan secara asli pada peranti Android dan iOS.

### Ciri Utama
- Dibina di atas rangka kerja .NET MAUI, menyediakan satu kod asas untuk aplikasi Android dan iOS
- Integrasi ONNX Runtime GenAI membolehkan model AI generatif dijalankan terus pada peranti mudah alih
- Menyokong pelbagai pemecut perkakasan yang disesuaikan untuk peranti mudah alih, termasuk CPU, GPU, dan pemproses AI mudah alih khusus
- Pengoptimuman khusus platform seperti CoreML untuk iOS dan NNAPI untuk Android melalui ONNX Runtime
- Melaksanakan keseluruhan gelung AI generatif termasuk pra dan pasca pemprosesan, inferens, pemprosesan logits, carian dan pensampelan, serta pengurusan cache KV

### Faedah Pembangunan
Pendekatan .NET MAUI membolehkan pembangun memanfaatkan kemahiran C# dan .NET sedia ada mereka sambil membina aplikasi AI merentas platform. Rangka kerja ONNX Runtime GenAI menyokong pelbagai seni bina model termasuk Llama, Mistral, Phi, Gemma, dan banyak lagi. Kernel ARM64 yang dioptimumkan mempercepatkan pendaraban matriks kuantifikasi INT4, memastikan prestasi cekap pada perkakasan mudah alih sambil mengekalkan pengalaman pembangunan .NET yang biasa.

### Kes Penggunaan
Penyelesaian ini sesuai untuk pembangun yang ingin membina aplikasi mudah alih berkuasa AI menggunakan teknologi .NET, termasuk chatbot pintar, aplikasi pengecaman imej, alat terjemahan bahasa, dan sistem cadangan peribadi yang berjalan sepenuhnya pada peranti untuk privasi yang dipertingkatkan dan keupayaan luar talian.

**Ketahui Lebih Lanjut**: [.NET MAUI ONNX Runtime GenAI Contoh](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI dalam Azure dengan Enjin Model Bahasa Kecil

Penyelesaian EdgeAI berasaskan Azure Microsoft memberi tumpuan kepada penggunaan Model Bahasa Kecil (SLM) secara cekap dalam persekitaran hibrid awan-tepi. Pendekatan ini merapatkan jurang antara perkhidmatan AI berskala awan dan keperluan penggunaan tepi.

### Kelebihan Seni Bina
- Integrasi lancar dengan perkhidmatan AI Azure
- Menjalankan SLM/LLM dan model multi-modal pada peranti dan di awan dengan ONNX Runtime
- Dioptimumkan untuk penggunaan berskala perusahaan
- Sokongan untuk kemas kini dan pengurusan model berterusan

### Kes Penggunaan
Pelaksanaan EdgeAI Azure cemerlang dalam senario yang memerlukan penggunaan AI berskala perusahaan dengan keupayaan pengurusan awan. Ini termasuk pemprosesan dokumen pintar, analitik masa nyata, dan aliran kerja AI hibrid yang memanfaatkan sumber pengkomputeran awan dan tepi.

**Ketahui Lebih Lanjut**: [Enjin SLM EdgeAI Azure](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI dengan Windows ML](./windowdeveloper.md)

Windows ML mewakili runtime terkini Microsoft yang dioptimumkan untuk inferens model pada peranti dan penggunaan yang dipermudahkan, berfungsi sebagai asas Windows AI Foundry. Platform ini membolehkan pembangun mencipta aplikasi Windows berkuasa AI yang memanfaatkan spektrum penuh perkakasan PC.

### Keupayaan Platform
- Berfungsi pada semua PC Windows 11 yang menjalankan versi 24H2 (binaan 26100) atau lebih tinggi
- Berfungsi pada semua perkakasan PC x64 dan ARM64, termasuk PC yang tidak mempunyai NPU atau GPU
- Membolehkan pembangun membawa model mereka sendiri dan menggunakannya dengan cekap merentasi ekosistem rakan kongsi silikon termasuk AMD, Intel, NVIDIA, dan Qualcomm yang merangkumi CPU, GPU, NPU
- Dengan memanfaatkan API infrastruktur, pembangun tidak lagi perlu mencipta pelbagai binaan aplikasi mereka untuk menyasarkan silikon yang berbeza

### Faedah Pembangun
Windows ML mengabstrakkan perkakasan dan penyedia pelaksanaan, jadi anda boleh memberi tumpuan kepada menulis kod anda. Selain itu, Windows ML secara automatik dikemas kini untuk menyokong NPU, GPU, dan CPU terkini apabila ia dikeluarkan. Platform ini menyediakan rangka kerja bersatu untuk pembangunan AI merentasi ekosistem perkakasan Windows yang pelbagai.

**Ketahui Lebih Lanjut**: 
- [Gambaran Keseluruhan Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Panduan Pembangunan EdgeAI Windows](./windowdeveloper.md) - Panduan komprehensif untuk pembangunan Edge AI Windows

## [5. EdgeAI dengan Aplikasi Tempatan Foundry](./foundrylocal.md)

Foundry Local membolehkan pembangun Windows dan Mac membina aplikasi Retrieval Augmented Generation (RAG) menggunakan sumber tempatan dalam .NET, menggabungkan model bahasa tempatan dengan keupayaan carian semantik. Pendekatan ini menyediakan penyelesaian AI yang berfokuskan privasi yang beroperasi sepenuhnya pada infrastruktur tempatan.

### Seni Bina Teknikal
- Menggabungkan model bahasa Phi, Embedding Tempatan, dan Kernel Semantik untuk mencipta senario RAG
- Menggunakan embedding sebagai vektor (array) nilai titik terapung yang mewakili kandungan dan makna semantiknya
- Kernel Semantik bertindak sebagai pengatur utama, mengintegrasikan Phi dan Komponen Pintar untuk mencipta saluran RAG yang lancar
- Sokongan untuk pangkalan data vektor tempatan termasuk SQLite dan Qdrant

### Faedah Pelaksanaan
RAG, atau Retrieval Augmented Generation, hanyalah cara canggih untuk mengatakan "cari beberapa maklumat dan masukkan ke dalam prompt". Pelaksanaan tempatan ini memastikan privasi data sambil menyediakan respons pintar yang berasaskan pangkalan pengetahuan tersuai. Pendekatan ini amat bernilai untuk senario perusahaan yang memerlukan kedaulatan data dan keupayaan operasi luar talian.

**Ketahui Lebih Lanjut**: 
- [Foundry Local](./foundrylocal.md)
- [Contoh RAG Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local menyediakan pelayan REST yang serasi dengan OpenAI yang dikuasakan oleh ONNX Runtime untuk menjalankan model secara tempatan pada Windows. Berikut adalah ringkasan pantas yang telah disahkan; lihat dokumen rasmi untuk butiran penuh.

- Bermula: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Seni bina: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Rujukan CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Panduan penuh Windows dalam repo ini: [foundrylocal.md](./foundrylocal.md)

Pasang atau tingkatkan pada Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Terokai kategori CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Jalankan model dan temui titik akhir dinamik:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Semak REST pantas untuk menyenaraikan model (gantikan PORT daripada status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Petua:
- Integrasi SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Bawa model anda sendiri (kompilasi): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Sumber Pembangunan EdgeAI Windows

Untuk pembangun yang secara khusus menyasarkan platform Windows, kami telah mencipta panduan komprehensif yang merangkumi keseluruhan ekosistem EdgeAI Windows. Sumber ini menyediakan maklumat terperinci tentang Windows AI Foundry, termasuk API, alat, dan amalan terbaik untuk pembangunan EdgeAI pada Windows.

### Platform Windows AI Foundry
Platform Windows AI Foundry menyediakan suite alat dan API yang komprehensif yang direka khusus untuk pembangunan AI tepi pada peranti Windows. Ini termasuk sokongan khusus untuk perkakasan yang dipercepatkan NPU, integrasi Windows ML, dan teknik pengoptimuman khusus platform.

**Panduan Komprehensif**: [Panduan Pembangunan EdgeAI Windows](../windowdeveloper.md)

Panduan ini merangkumi:
- Gambaran keseluruhan platform Windows AI Foundry dan komponennya
- API Phi Silica untuk inferens yang cekap pada perkakasan NPU
- API Penglihatan Komputer untuk pemprosesan imej dan OCR
- Integrasi dan pengoptimuman runtime Windows ML
- CLI Foundry Local untuk pembangunan dan ujian tempatan
- Strategi pengoptimuman perkakasan untuk peranti Windows
- Contoh pelaksanaan praktikal dan amalan terbaik

### [Toolkit AI untuk Pembangunan Edge AI](./aitoolkit.md)
Untuk pembangun yang menggunakan Visual Studio Code, sambungan AI Toolkit menyediakan persekitaran pembangunan yang komprehensif yang direka khusus untuk membina, menguji, dan menggunakan aplikasi Edge AI. Toolkit ini mempermudahkan keseluruhan aliran kerja pembangunan Edge AI dalam VS Code.

**Panduan Pembangunan**: [Toolkit AI untuk Pembangunan Edge AI](./aitoolkit.md)

Panduan AI Toolkit merangkumi:
- Penemuan dan pemilihan model untuk penggunaan tepi
- Aliran kerja ujian dan pengoptimuman tempatan
- Integrasi ONNX dan Ollama untuk model tepi
- Teknik penukaran dan kuantifikasi model
- Pembangunan agen untuk senario tepi
- Penilaian prestasi dan pemantauan
- Persediaan penggunaan dan amalan terbaik

## Kesimpulan

Lima pelaksanaan EdgeAI ini menunjukkan kematangan dan kepelbagaian penyelesaian AI tepi yang tersedia hari ini. Daripada peranti tepi yang dipercepatkan perkakasan seperti Jetson Orin Nano kepada rangka kerja perisian seperti ONNX Runtime GenAI dan Windows ML, pembangun mempunyai pilihan yang belum pernah ada sebelumnya untuk menggunakan aplikasi pintar di tepi.

Benang merah di semua platform ini adalah pendemokrasian keupayaan AI, menjadikan pembelajaran mesin yang canggih dapat diakses oleh pembangun merentasi pelbagai tahap kemahiran dan kes penggunaan. Sama ada membina aplikasi mudah alih, perisian desktop, atau sistem terbenam, penyelesaian EdgeAI ini menyediakan asas untuk generasi seterusnya aplikasi pintar yang beroperasi dengan cekap dan secara peribadi di tepi.

Setiap platform menawarkan kelebihan unik: Jetson Orin Nano untuk pengkomputeran tepi yang dipercepatkan perkakasan, ONNX Runtime GenAI untuk pembangunan mudah alih merentas platform, Azure EdgeAI untuk integrasi awan-tepi perusahaan, Windows ML untuk aplikasi asli Windows, dan Foundry Local untuk pelaksanaan RAG yang berfokuskan privasi. Bersama-sama, mereka mewakili ekosistem yang komprehensif untuk pembangunan EdgeAI.

[Toolkit AI Seterusnya](aitoolkit.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.