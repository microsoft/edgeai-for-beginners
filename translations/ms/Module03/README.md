# Bab 03: Melaksanakan Model Bahasa Kecil (SLM)

Bab yang komprehensif ini meneroka keseluruhan kitaran hayat pelaksanaan Model Bahasa Kecil (SLM), merangkumi asas teori, strategi pelaksanaan praktikal, dan penyelesaian kontena yang sedia untuk pengeluaran. Bab ini disusun dalam tiga bahagian progresif yang membawa pembaca daripada konsep asas kepada senario pelaksanaan yang lebih maju.

## Struktur Bab dan Perjalanan Pembelajaran

### **[Bahagian 1: Pembelajaran Lanjutan SLM - Asas dan Pengoptimuman](./01.SLMAdvancedLearning.md)**
Bahagian pembukaan ini menetapkan asas teori untuk memahami Model Bahasa Kecil dan kepentingan strategiknya dalam pelaksanaan AI di peranti tepi. Bahagian ini merangkumi:

- **Kerangka Pengelasan Parameter**: Penerokaan terperinci kategori SLM daripada Micro SLMs (100M-1.4B parameter) kepada Medium SLMs (14B-30B parameter), dengan fokus khusus pada model seperti Phi-4-mini-3.8B, siri Qwen3, dan Google Gemma3, termasuk analisis keperluan perkakasan dan jejak memori untuk setiap tahap model
- **Teknik Pengoptimuman Lanjutan**: Liputan menyeluruh kaedah kuantisasi menggunakan rangka kerja Llama.cpp, Microsoft Olive, dan Apple MLX, termasuk kuantisasi BitNET 1-bit terkini dengan contoh kod praktikal yang menunjukkan saluran kuantisasi dan hasil penanda aras
- **Strategi Perolehan Model**: Analisis mendalam ekosistem Hugging Face dan Katalog Model Azure AI Foundry untuk pelaksanaan SLM peringkat perusahaan, dengan contoh kod untuk muat turun model secara programatik, pengesahan, dan penukaran format
- **API Pembangun**: Contoh kod dalam Python, C++, dan C# yang menunjukkan cara memuatkan model, melakukan inferens, dan mengintegrasikan dengan rangka kerja popular seperti PyTorch, TensorFlow, dan ONNX Runtime

Bahagian asas ini menekankan keseimbangan antara kecekapan operasi, fleksibiliti pelaksanaan, dan keberkesanan kos yang menjadikan SLM sesuai untuk senario pengkomputeran tepi, dengan contoh kod praktikal yang boleh terus dilaksanakan oleh pembangun dalam projek mereka.

### **[Bahagian 2: Pelaksanaan Persekitaran Tempatan - Penyelesaian Berorientasikan Privasi](./02.DeployingSLMinLocalEnv.md)**
Bahagian kedua ini beralih daripada teori kepada pelaksanaan praktikal, dengan fokus pada strategi pelaksanaan tempatan yang mengutamakan kedaulatan data dan kebebasan operasi. Kawasan utama termasuk:

- **Platform Universal Ollama**: Penerokaan menyeluruh pelaksanaan merentas platform dengan penekanan pada aliran kerja mesra pembangun, pengurusan kitaran hayat model, dan penyesuaian melalui Modelfiles, termasuk contoh integrasi REST API lengkap dan skrip automasi CLI
- **Microsoft Foundry Local**: Penyelesaian pelaksanaan peringkat perusahaan dengan pengoptimuman berasaskan ONNX, integrasi Windows ML, dan ciri keselamatan yang komprehensif, dengan contoh kod C# dan Python untuk integrasi aplikasi asli
- **Analisis Perbandingan**: Perbandingan rangka kerja terperinci yang merangkumi seni bina teknikal, ciri prestasi, dan garis panduan pengoptimuman kes penggunaan, dengan kod penanda aras untuk menilai kelajuan inferens dan penggunaan memori pada perkakasan yang berbeza
- **Integrasi API**: Aplikasi contoh yang menunjukkan cara membina perkhidmatan web, aplikasi sembang, dan saluran pemprosesan data menggunakan pelaksanaan SLM tempatan, dengan contoh kod dalam Node.js, Python Flask/FastAPI, dan ASP.NET Core
- **Rangka Kerja Pengujian**: Pendekatan pengujian automatik untuk jaminan kualiti model, termasuk contoh ujian unit dan integrasi untuk pelaksanaan SLM

Bahagian ini menyediakan panduan praktikal untuk organisasi yang ingin melaksanakan penyelesaian AI yang memelihara privasi sambil mengekalkan kawalan penuh ke atas persekitaran pelaksanaan mereka, dengan contoh kod sedia guna yang boleh disesuaikan oleh pembangun mengikut keperluan khusus mereka.

### **[Bahagian 3: Pelaksanaan Kontena di Awan - Penyelesaian Skala Pengeluaran](./03.DeployingSLMinCloud.md)**
Bahagian terakhir ini memuncak dalam strategi pelaksanaan kontena yang maju, dengan kajian kes utama menggunakan Microsoft Phi-4-mini-instruct. Bahagian ini merangkumi:

- **Pelaksanaan vLLM**: Pengoptimuman inferens berprestasi tinggi dengan API serasi OpenAI, pecutan GPU lanjutan, dan konfigurasi sedia pengeluaran, termasuk Dockerfiles lengkap, manifest Kubernetes, dan parameter penalaan prestasi
- **Orkestrasi Kontena Ollama**: Aliran kerja pelaksanaan yang dipermudahkan dengan Docker Compose, varian pengoptimuman model, dan integrasi UI web, dengan contoh saluran CI/CD untuk pelaksanaan dan pengujian automatik
- **Pelaksanaan ONNX Runtime**: Pelaksanaan yang dioptimumkan untuk tepi dengan penukaran model yang komprehensif, strategi kuantisasi, dan keserasian merentas platform, termasuk contoh kod terperinci untuk pengoptimuman dan pelaksanaan model
- **Pemantauan & Pemerhatian**: Pelaksanaan papan pemuka Prometheus/Grafana dengan metrik tersuai untuk pemantauan prestasi SLM, termasuk konfigurasi amaran dan pengagregatan log
- **Pengimbangan Beban & Penskalaan**: Contoh praktikal strategi penskalaan mendatar dan menegak dengan konfigurasi penskalaan automatik berdasarkan penggunaan CPU/GPU dan corak permintaan
- **Pengukuhan Keselamatan**: Amalan terbaik keselamatan kontena termasuk pengurangan keistimewaan, dasar rangkaian, dan pengurusan rahsia untuk kunci API dan kelayakan akses model

Setiap pendekatan pelaksanaan disampaikan dengan contoh konfigurasi lengkap, prosedur pengujian, senarai semak kesediaan pengeluaran, dan templat infrastruktur sebagai kod yang boleh terus digunakan oleh pembangun dalam aliran kerja pelaksanaan mereka.

## Hasil Pembelajaran Utama

Dengan melengkapkan bab ini, pembaca akan menguasai:

1. **Pemilihan Model Strategik**: Memahami sempadan parameter dan memilih SLM yang sesuai berdasarkan kekangan sumber dan keperluan prestasi
2. **Penguasaan Pengoptimuman**: Melaksanakan teknik kuantisasi lanjutan merentas rangka kerja yang berbeza untuk mencapai keseimbangan prestasi-kecekapan yang optimum
3. **Fleksibiliti Pelaksanaan**: Memilih antara penyelesaian berorientasikan privasi tempatan dan pelaksanaan kontena yang boleh diskalakan berdasarkan keperluan organisasi
4. **Kesediaan Pengeluaran**: Mengkonfigurasi sistem pemantauan, keselamatan, dan penskalaan untuk pelaksanaan SLM peringkat perusahaan

## Fokus Praktikal dan Aplikasi Dunia Nyata

Bab ini mengekalkan orientasi praktikal yang kuat sepanjang, menampilkan:

- **Contoh Praktikal**: Fail konfigurasi lengkap, prosedur pengujian API, dan skrip pelaksanaan
- **Penanda Aras Prestasi**: Perbandingan terperinci kelajuan inferens, penggunaan memori, dan keperluan sumber
- **Pertimbangan Keselamatan**: Amalan keselamatan peringkat perusahaan, rangka kerja pematuhan, dan strategi perlindungan data
- **Amalan Terbaik**: Garis panduan yang terbukti untuk pemantauan, penskalaan, dan penyelenggaraan

## Perspektif Masa Depan

Bab ini diakhiri dengan pandangan ke hadapan tentang trend yang sedang muncul termasuk:

- Seni bina model lanjutan dengan nisbah kecekapan yang lebih baik
- Integrasi perkakasan yang lebih mendalam dengan pemecut AI khusus
- Evolusi ekosistem ke arah penyeragaman dan keserasian
- Corak penerimaan perusahaan yang didorong oleh privasi dan keperluan pematuhan

Pendekatan yang komprehensif ini memastikan pembaca dilengkapi dengan baik untuk menghadapi cabaran pelaksanaan SLM semasa dan perkembangan teknologi masa depan, membuat keputusan yang berinformasi yang selaras dengan keperluan dan kekangan organisasi mereka.

Bab ini berfungsi sebagai panduan praktikal untuk pelaksanaan segera dan sumber strategik untuk perancangan pelaksanaan AI jangka panjang, menekankan keseimbangan kritikal antara keupayaan, kecekapan, dan kecemerlangan operasi yang mentakrifkan pelaksanaan SLM yang berjaya.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.