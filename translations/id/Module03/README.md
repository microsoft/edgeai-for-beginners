# Bab 03: Menerapkan Small Language Models (SLMs)

Bab ini secara komprehensif membahas siklus hidup lengkap penerapan Small Language Models (SLMs), mencakup dasar teori, strategi implementasi praktis, dan solusi containerized siap produksi. Bab ini disusun dalam tiga bagian progresif yang membawa pembaca dari konsep dasar hingga skenario penerapan tingkat lanjut.

## Struktur Bab dan Perjalanan Pembelajaran

### **[Bagian 1: Pembelajaran Lanjutan SLM - Dasar dan Optimasi](./01.SLMAdvancedLearning.md)**
Bagian pembuka ini membangun dasar teori untuk memahami Small Language Models dan pentingnya strategi mereka dalam penerapan AI di edge. Bagian ini mencakup:

- **Kerangka Klasifikasi Parameter**: Eksplorasi mendalam kategori SLM dari Micro SLMs (100M-1.4B parameter) hingga Medium SLMs (14B-30B parameter), dengan fokus khusus pada model seperti Phi-4-mini-3.8B, seri Qwen3, dan Google Gemma3, termasuk analisis kebutuhan perangkat keras dan jejak memori untuk setiap tingkatan model
- **Teknik Optimasi Lanjutan**: Pembahasan komprehensif metode kuantisasi menggunakan kerangka kerja Llama.cpp, Microsoft Olive, dan Apple MLX, termasuk kuantisasi BitNET 1-bit terbaru dengan contoh kode praktis yang menunjukkan pipeline kuantisasi dan hasil benchmarking
- **Strategi Akuisisi Model**: Analisis mendalam ekosistem Hugging Face dan Azure AI Foundry Model Catalog untuk penerapan SLM tingkat perusahaan, dengan contoh kode untuk pengunduhan model secara programatik, validasi, dan konversi format
- **API Pengembang**: Contoh kode dalam Python, C++, dan C# yang menunjukkan cara memuat model, melakukan inferensi, dan mengintegrasikan dengan kerangka kerja populer seperti PyTorch, TensorFlow, dan ONNX Runtime

Bagian dasar ini menekankan keseimbangan antara efisiensi operasional, fleksibilitas penerapan, dan efektivitas biaya yang membuat SLM ideal untuk skenario komputasi edge, dengan contoh kode praktis yang dapat langsung diterapkan oleh pengembang dalam proyek mereka.

### **[Bagian 2: Penerapan Lingkungan Lokal - Solusi Berbasis Privasi](./02.DeployingSLMinLocalEnv.md)**
Bagian kedua beralih dari teori ke implementasi praktis, berfokus pada strategi penerapan lokal yang memprioritaskan kedaulatan data dan independensi operasional. Area utama meliputi:

- **Platform Universal Ollama**: Eksplorasi komprehensif penerapan lintas platform dengan penekanan pada alur kerja yang ramah pengembang, manajemen siklus hidup model, dan kustomisasi melalui Modelfiles, termasuk contoh integrasi REST API lengkap dan skrip otomatisasi CLI
- **Microsoft Foundry Local**: Solusi penerapan tingkat perusahaan dengan optimasi berbasis ONNX, integrasi Windows ML, dan fitur keamanan yang komprehensif, dengan contoh kode C# dan Python untuk integrasi aplikasi native
- **Analisis Perbandingan**: Perbandingan kerangka kerja yang mendetail mencakup arsitektur teknis, karakteristik kinerja, dan panduan optimasi kasus penggunaan, dengan kode benchmark untuk mengevaluasi kecepatan inferensi dan penggunaan memori pada perangkat keras yang berbeda
- **Integrasi API**: Aplikasi contoh yang menunjukkan cara membangun layanan web, aplikasi chat, dan pipeline pemrosesan data menggunakan penerapan SLM lokal, dengan contoh kode dalam Node.js, Python Flask/FastAPI, dan ASP.NET Core
- **Kerangka Pengujian**: Pendekatan pengujian otomatis untuk jaminan kualitas model, termasuk contoh pengujian unit dan integrasi untuk implementasi SLM

Bagian ini memberikan panduan praktis bagi organisasi yang ingin menerapkan solusi AI berbasis privasi sambil mempertahankan kontrol penuh atas lingkungan penerapan mereka, dengan contoh kode siap pakai yang dapat disesuaikan oleh pengembang sesuai kebutuhan spesifik mereka.

### **[Bagian 3: Penerapan Cloud Berbasis Container - Solusi Skala Produksi](./03.DeployingSLMinCloud.md)**
Bagian terakhir ini berfokus pada strategi penerapan berbasis container tingkat lanjut, dengan studi kasus utama Microsoft Phi-4-mini-instruct. Bagian ini mencakup:

- **Penerapan vLLM**: Optimasi inferensi berkinerja tinggi dengan API yang kompatibel dengan OpenAI, akselerasi GPU tingkat lanjut, dan konfigurasi siap produksi, termasuk Dockerfiles lengkap, manifest Kubernetes, dan parameter penyetelan kinerja
- **Orkestrasi Container Ollama**: Alur kerja penerapan yang disederhanakan dengan Docker Compose, varian optimasi model, dan integrasi UI web, dengan contoh pipeline CI/CD untuk penerapan dan pengujian otomatis
- **Implementasi ONNX Runtime**: Penerapan yang dioptimalkan untuk edge dengan konversi model yang komprehensif, strategi kuantisasi, dan kompatibilitas lintas platform, termasuk contoh kode mendetail untuk optimasi dan penerapan model
- **Pemantauan & Observabilitas**: Implementasi dashboard Prometheus/Grafana dengan metrik khusus untuk pemantauan kinerja SLM, termasuk konfigurasi peringatan dan agregasi log
- **Load Balancing & Scaling**: Contoh praktis strategi penskalaan horizontal dan vertikal dengan konfigurasi autoscaling berdasarkan penggunaan CPU/GPU dan pola permintaan
- **Penguatan Keamanan**: Praktik terbaik keamanan container termasuk pengurangan hak istimewa, kebijakan jaringan, dan manajemen rahasia untuk kunci API dan kredensial akses model

Setiap pendekatan penerapan disajikan dengan contoh konfigurasi lengkap, prosedur pengujian, daftar periksa kesiapan produksi, dan template infrastruktur sebagai kode yang dapat langsung diterapkan oleh pengembang ke alur kerja penerapan mereka.

## Hasil Pembelajaran Utama

Dengan menyelesaikan bab ini, pembaca akan menguasai:

1. **Pemilihan Model Strategis**: Memahami batas parameter dan memilih SLM yang sesuai berdasarkan keterbatasan sumber daya dan kebutuhan kinerja
2. **Penguasaan Optimasi**: Menerapkan teknik kuantisasi lanjutan di berbagai kerangka kerja untuk mencapai keseimbangan kinerja-efisiensi yang optimal
3. **Fleksibilitas Penerapan**: Memilih antara solusi berbasis privasi lokal dan penerapan berbasis container yang dapat diskalakan sesuai kebutuhan organisasi
4. **Kesiapan Produksi**: Mengonfigurasi sistem pemantauan, keamanan, dan penskalaan untuk penerapan SLM tingkat perusahaan

## Fokus Praktis dan Aplikasi Dunia Nyata

Bab ini mempertahankan orientasi praktis yang kuat sepanjang pembahasan, menampilkan:

- **Contoh Langsung**: File konfigurasi lengkap, prosedur pengujian API, dan skrip penerapan
- **Benchmarking Kinerja**: Perbandingan mendetail kecepatan inferensi, penggunaan memori, dan kebutuhan sumber daya
- **Pertimbangan Keamanan**: Praktik keamanan tingkat perusahaan, kerangka kerja kepatuhan, dan strategi perlindungan data
- **Praktik Terbaik**: Panduan yang telah terbukti untuk pemantauan, penskalaan, dan pemeliharaan

## Perspektif Masa Depan

Bab ini diakhiri dengan wawasan ke depan tentang tren yang sedang berkembang, termasuk:

- Arsitektur model yang lebih canggih dengan rasio efisiensi yang lebih baik
- Integrasi perangkat keras yang lebih dalam dengan akselerator AI khusus
- Evolusi ekosistem menuju standarisasi dan interoperabilitas
- Pola adopsi perusahaan yang didorong oleh privasi dan persyaratan kepatuhan

Pendekatan komprehensif ini memastikan pembaca siap menghadapi tantangan penerapan SLM saat ini maupun perkembangan teknologi di masa depan, membuat keputusan yang tepat sesuai dengan kebutuhan dan keterbatasan organisasi mereka.

Bab ini berfungsi sebagai panduan praktis untuk implementasi langsung dan sumber daya strategis untuk perencanaan penerapan AI jangka panjang, menekankan keseimbangan kritis antara kemampuan, efisiensi, dan keunggulan operasional yang mendefinisikan keberhasilan penerapan SLM.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.