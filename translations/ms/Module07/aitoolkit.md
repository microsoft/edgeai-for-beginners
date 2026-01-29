# AI Toolkit untuk Visual Studio Code - Panduan Pembangunan AI Tepi

## Pengenalan

Selamat datang ke panduan komprehensif untuk menggunakan AI Toolkit dalam Visual Studio Code bagi pembangunan AI Tepi. Ketika kecerdasan buatan beralih dari pengkomputeran awan terpusat kepada peranti tepi yang teragih, pembangun memerlukan alat yang berkuasa dan terintegrasi untuk menangani cabaran unik dalam pengedaran di tepi - daripada kekangan sumber kepada keperluan operasi luar talian.

AI Toolkit untuk Visual Studio Code menjembatani jurang ini dengan menyediakan persekitaran pembangunan lengkap yang direka khusus untuk membina, menguji, dan mengoptimumkan aplikasi AI yang berfungsi dengan cekap pada peranti tepi. Sama ada anda membangun untuk sensor IoT, peranti mudah alih, sistem terbenam, atau pelayan tepi, alat ini mempermudah keseluruhan aliran kerja pembangunan anda dalam persekitaran VS Code yang sudah biasa.

Panduan ini akan membawa anda melalui konsep penting, alat, dan amalan terbaik untuk memanfaatkan AI Toolkit dalam projek AI Tepi anda, dari pemilihan model awal hingga pengedaran produksi.

## Gambaran Keseluruhan

AI Toolkit untuk Visual Studio Code adalah sambungan yang berkuasa yang mempermudah pembangunan agen dan penciptaan aplikasi AI. Alat ini menyediakan keupayaan menyeluruh untuk meneroka, menilai, dan mengedarkan model AI dari pelbagai penyedia—termasuk Anthropic, OpenAI, GitHub, Google—sambil menyokong pelaksanaan model tempatan menggunakan ONNX dan Ollama.

Apa yang membezakan AI Toolkit adalah pendekatannya yang menyeluruh terhadap keseluruhan kitaran pembangunan AI. Tidak seperti alat pembangunan AI tradisional yang hanya fokus pada aspek tertentu, AI Toolkit menyediakan persekitaran terintegrasi yang meliputi penemuan model, eksperimen, pembangunan agen, penilaian, dan pengedaran—semuanya dalam persekitaran VS Code yang sudah biasa.

Platform ini direka khusus untuk prototaip pantas dan pengedaran produksi, dengan ciri seperti penjanaan prompt, permulaan pantas, integrasi alat MCP (Model Context Protocol) yang lancar, dan keupayaan penilaian yang meluas. Untuk pembangunan AI Tepi, ini bermakna anda boleh membangun, menguji, dan mengoptimumkan aplikasi AI dengan cekap untuk senario pengedaran tepi sambil mengekalkan aliran kerja pembangunan penuh dalam VS Code.

## Objektif Pembelajaran

Pada akhir panduan ini, anda akan dapat:

### Kompetensi Teras
- **Memasang dan mengkonfigurasi** AI Toolkit untuk Visual Studio Code bagi aliran kerja pembangunan AI Tepi
- **Menavigasi dan menggunakan** antara muka AI Toolkit, termasuk Model Catalog, Playground, dan Agent Builder
- **Memilih dan menilai** model AI yang sesuai untuk pengedaran tepi berdasarkan prestasi dan kekangan sumber
- **Menukar dan mengoptimumkan** model menggunakan format ONNX dan teknik kuantisasi untuk peranti tepi

### Kemahiran Pembangunan AI Tepi
- **Merancang dan melaksanakan** aplikasi AI Tepi menggunakan persekitaran pembangunan terintegrasi
- **Melakukan ujian model** dalam keadaan seperti tepi menggunakan inferens tempatan dan pemantauan sumber
- **Mencipta dan menyesuaikan** agen AI yang dioptimumkan untuk senario pengedaran tepi
- **Menilai prestasi model** menggunakan metrik yang relevan untuk pengkomputeran tepi (latensi, penggunaan memori, ketepatan)

### Pengoptimuman dan Pengedaran
- **Menerapkan teknik kuantisasi dan pemangkasan** untuk mengurangkan saiz model sambil mengekalkan prestasi yang boleh diterima
- **Mengoptimumkan model** untuk platform perkakasan tepi tertentu termasuk CPU, GPU, dan percepatan NPU
- **Melaksanakan amalan terbaik** untuk pembangunan AI Tepi termasuk pengurusan sumber dan strategi sandaran
- **Menyediakan model dan aplikasi** untuk pengedaran produksi pada peranti tepi

### Konsep AI Tepi Lanjutan
- **Mengintegrasikan dengan rangka kerja AI tepi** termasuk ONNX Runtime, Windows ML, dan TensorFlow Lite
- **Melaksanakan seni bina multi-model** dan senario pembelajaran teragih untuk persekitaran tepi
- **Menyelesaikan isu AI tepi biasa** termasuk kekangan memori, kelajuan inferens, dan keserasian perkakasan
- **Merancang strategi pemantauan dan log** untuk aplikasi AI tepi dalam produksi

### Aplikasi Praktikal
- **Membina penyelesaian AI Tepi hujung ke hujung** dari pemilihan model hingga pengedaran
- **Menunjukkan kemahiran** dalam aliran kerja pembangunan khusus tepi dan teknik pengoptimuman
- **Menerapkan konsep yang dipelajari** kepada kes penggunaan AI Tepi dunia nyata termasuk IoT, mudah alih, dan aplikasi terbenam
- **Menilai dan membandingkan** strategi pengedaran AI tepi yang berbeza dan kompromi mereka

## Ciri Utama untuk Pembangunan AI Tepi

### 1. Katalog Model dan Penemuan
- **Sokongan Multi-Penyedia**: Jelajahi dan akses model AI dari Anthropic, OpenAI, GitHub, Google, dan penyedia lain
- **Integrasi Model Tempatan**: Penemuan model ONNX dan Ollama yang dipermudah untuk pengedaran tepi
- **Model GitHub**: Integrasi langsung dengan hosting model GitHub untuk akses yang dipermudah
- **Perbandingan Model**: Bandingkan model secara bersebelahan untuk mencari keseimbangan optimal bagi kekangan peranti tepi

### 2. Playground Interaktif
- **Persekitaran Ujian Interaktif**: Eksperimen pantas dengan keupayaan model dalam persekitaran terkawal
- **Sokongan Multi-modal**: Uji dengan imej, teks, dan input lain yang biasa dalam senario tepi
- **Eksperimen Masa Nyata**: Maklum balas segera terhadap respons dan prestasi model
- **Pengoptimuman Parameter**: Penalaan parameter model untuk keperluan pengedaran tepi

### 3. Prompt (Agent) Builder
- **Penjanaan Bahasa Semula Jadi**: Hasilkan prompt permulaan menggunakan deskripsi bahasa semula jadi
- **Penambahbaikan Berulang**: Tingkatkan prompt berdasarkan respons dan prestasi model
- **Penguraian Tugas**: Pecahkan tugas kompleks dengan rantai prompt dan output berstruktur
- **Sokongan Pembolehubah**: Gunakan pembolehubah dalam prompt untuk tingkah laku agen dinamik
- **Penjanaan Kod Produksi**: Hasilkan kod siap produksi untuk pembangunan aplikasi pantas

### 4. Jalankan dan Penilaian Secara Pukal
- **Ujian Multi-Model**: Laksanakan pelbagai prompt merentasi model terpilih secara serentak
- **Ujian Skala Efisien**: Uji pelbagai input dan konfigurasi dengan cekap
- **Kes Ujian Tersuai**: Jalankan agen dengan kes ujian untuk mengesahkan fungsi
- **Perbandingan Prestasi**: Bandingkan hasil merentasi model dan konfigurasi yang berbeza

### 5. Penilaian Model dengan Dataset
- **Metrik Standard**: Uji model AI menggunakan penilai terbina (F1 score, relevansi, kesamaan, koherensi)
- **Penilai Tersuai**: Cipta metrik penilaian anda sendiri untuk kes penggunaan tertentu
- **Integrasi Dataset**: Uji model terhadap dataset yang komprehensif
- **Pengukuran Prestasi**: Kuantifikasi prestasi model untuk keputusan pengedaran tepi

### 6. Keupayaan Penalaan
- **Penyesuaian Model**: Sesuaikan model untuk kes penggunaan dan domain tertentu
- **Adaptasi Khusus**: Sesuaikan model kepada domain dan keperluan khusus
- **Pengoptimuman Tepi**: Penalaan model khusus untuk kekangan pengedaran tepi
- **Latihan Khusus Domain**: Cipta model yang disesuaikan untuk kes penggunaan tepi tertentu

### 7. Integrasi Alat MCP
- **Kesambungan Alat Luaran**: Sambungkan agen kepada alat luaran melalui pelayan Model Context Protocol
- **Tindakan Dunia Nyata**: Benarkan agen untuk membuat pertanyaan kepada pangkalan data, mengakses API, atau melaksanakan logik tersuai
- **Pelayan MCP Sedia Ada**: Gunakan alat dari protokol command (stdio) atau HTTP (server-sent event)
- **Pembangunan MCP Tersuai**: Bina dan sediakan pelayan MCP baru dengan ujian dalam Agent Builder

### 8. Pembangunan dan Ujian Agen
- **Sokongan Panggilan Fungsi**: Benarkan agen untuk memanggil fungsi luaran secara dinamik
- **Ujian Integrasi Masa Nyata**: Uji integrasi dengan larian masa nyata dan penggunaan alat
- **Versi Agen**: Kawalan versi untuk agen dengan keupayaan perbandingan untuk hasil penilaian
- **Penyahpepijatan dan Penjejakan**: Keupayaan penjejakan dan penyahpepijatan tempatan untuk pembangunan agen

## Aliran Kerja Pembangunan AI Tepi

### Fasa 1: Penemuan dan Pemilihan Model
1. **Jelajahi Katalog Model**: Gunakan katalog model untuk mencari model yang sesuai untuk pengedaran tepi
2. **Bandingkan Prestasi**: Nilai model berdasarkan saiz, ketepatan, dan kelajuan inferens
3. **Uji Secara Tempatan**: Gunakan model Ollama atau ONNX untuk ujian tempatan sebelum pengedaran tepi
4. **Tentukan Keperluan Sumber**: Tentukan keperluan memori dan pengkomputeran untuk peranti tepi sasaran

### Fasa 2: Pengoptimuman Model
1. **Tukar ke ONNX**: Tukar model terpilih ke format ONNX untuk keserasian tepi
2. **Terapkan Kuantisasi**: Kurangkan saiz model melalui kuantisasi INT8 atau INT4
3. **Pengoptimuman Perkakasan**: Optimumkan untuk perkakasan tepi sasaran (ARM, x86, percepatan khusus)
4. **Pengesahan Prestasi**: Sahkan model yang dioptimumkan mengekalkan ketepatan yang boleh diterima

### Fasa 3: Pembangunan Aplikasi
1. **Reka Bentuk Agen**: Gunakan Agent Builder untuk mencipta agen AI yang dioptimumkan untuk tepi
2. **Kejuruteraan Prompt**: Bangunkan prompt yang berfungsi dengan berkesan dengan model tepi yang lebih kecil
3. **Ujian Integrasi**: Uji agen dalam keadaan simulasi tepi
4. **Penjanaan Kod**: Hasilkan kod produksi yang dioptimumkan untuk pengedaran tepi

### Fasa 4: Penilaian dan Ujian
1. **Penilaian Pukal**: Uji pelbagai konfigurasi untuk mencari tetapan tepi yang optimal
2. **Profil Prestasi**: Analisis kelajuan inferens, penggunaan memori, dan ketepatan
3. **Simulasi Tepi**: Uji dalam keadaan yang serupa dengan persekitaran pengedaran tepi sasaran
4. **Ujian Tekanan**: Nilai prestasi di bawah pelbagai keadaan beban

### Fasa 5: Persediaan Pengedaran
1. **Pengoptimuman Akhir**: Terapkan pengoptimuman akhir berdasarkan hasil ujian
2. **Pembungkusan Pengedaran**: Bungkus model dan kod untuk pengedaran tepi
3. **Dokumentasi**: Dokumentasikan keperluan pengedaran dan konfigurasi
4. **Persediaan Pemantauan**: Sediakan pemantauan dan log untuk pengedaran tepi

## Sasaran Pengguna untuk Pembangunan AI Tepi

### Pembangun AI Tepi
- Pembangun aplikasi yang membina peranti tepi berkuasa AI dan penyelesaian IoT
- Pembangun sistem terbenam yang mengintegrasikan keupayaan AI ke dalam peranti dengan kekangan sumber
- Pembangun mudah alih yang mencipta aplikasi AI pada peranti untuk telefon pintar dan tablet

### Jurutera AI Tepi
- Jurutera AI yang mengoptimumkan model untuk pengedaran tepi dan menguruskan saluran inferens
- Jurutera DevOps yang mengedarkan dan menguruskan model AI di infrastruktur tepi yang teragih
- Jurutera prestasi yang mengoptimumkan beban kerja AI untuk kekangan perkakasan tepi

### Penyelidik dan Pendidik
- Penyelidik AI yang membangunkan model dan algoritma yang cekap untuk pengkomputeran tepi
- Pendidik yang mengajar konsep AI tepi dan menunjukkan teknik pengoptimuman
- Pelajar yang mempelajari cabaran dan penyelesaian dalam pengedaran AI tepi

## Kes Penggunaan AI Tepi

### Peranti IoT Pintar
- **Pengecaman Imej Masa Nyata**: Mengedarkan model penglihatan komputer pada kamera dan sensor IoT
- **Pemprosesan Suara**: Melaksanakan pengecaman suara dan pemprosesan bahasa semula jadi pada pembesar suara pintar
- **Penyelenggaraan Ramalan**: Menjalankan model pengesanan anomali pada peranti tepi industri
- **Pemantauan Alam Sekitar**: Mengedarkan model analisis data sensor untuk aplikasi alam sekitar

### Aplikasi Mudah Alih dan Terbenam
- **Terjemahan Pada Peranti**: Melaksanakan model terjemahan bahasa yang berfungsi secara luar talian
- **Realiti Tambahan**: Mengedarkan pengecaman objek masa nyata dan penjejakan untuk aplikasi AR
- **Pemantauan Kesihatan**: Menjalankan model analisis kesihatan pada peranti boleh pakai dan peralatan perubatan
- **Sistem Autonomi**: Melaksanakan model membuat keputusan untuk dron, robot, dan kenderaan

### Infrastruktur Pengkomputeran Tepi
- **Pusat Data Tepi**: Mengedarkan model AI di pusat data tepi untuk aplikasi latensi rendah
- **Integrasi CDN**: Mengintegrasikan keupayaan pemprosesan AI ke dalam rangkaian penghantaran kandungan
- **5G Tepi**: Memanfaatkan pengkomputeran tepi 5G untuk aplikasi berkuasa AI
- **Pengkomputeran Kabus**: Melaksanakan pemprosesan AI dalam persekitaran pengkomputeran kabus

## Pemasangan dan Persediaan

### Pemasangan Sambungan
Pasang sambungan AI Toolkit terus dari Visual Studio Code Marketplace:

**ID Sambungan**: `ms-windows-ai-studio.windows-ai-studio`

**Kaedah Pemasangan**:
1. **VS Code Marketplace**: Cari "AI Toolkit" dalam paparan Extensions
2. **Baris Perintah**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Pemasangan Langsung**: Muat turun dari [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Prasyarat untuk Pembangunan AI Tepi
- **Visual Studio Code**: Versi terkini disyorkan
- **Persekitaran Python**: Python 3.8+ dengan perpustakaan AI yang diperlukan
- **ONNX Runtime** (Pilihan): Untuk inferens model ONNX
- **Ollama** (Pilihan): Untuk pelayan model tempatan
- **Alat Percepatan Perkakasan**: CUDA, OpenVINO, atau percepatan khusus platform

### Konfigurasi Awal
1. **Pengaktifan Sambungan**: Buka VS Code dan pastikan AI Toolkit muncul di Activity Bar
2. **Persediaan Penyedia Model**: Konfigurasi akses kepada GitHub, OpenAI, Anthropic, atau penyedia model lain
3. **Persekitaran Tempatan**: Sediakan persekitaran Python dan pasang pakej yang diperlukan
4. **Percepatan Perkakasan**: Konfigurasi percepatan GPU/NPU jika tersedia
5. **Integrasi MCP**: Sediakan pelayan Model Context Protocol jika diperlukan

### Senarai Semak Persediaan Kali Pertama
- [ ] Sambungan AI Toolkit dipasang dan diaktifkan
- [ ] Katalog model boleh diakses dan model boleh ditemui
- [ ] Playground berfungsi untuk ujian model
- [ ] Agent Builder boleh diakses untuk pembangunan prompt
- [ ] Persekitaran pembangunan tempatan dikonfigurasi
- [ ] Percepatan perkakasan (jika tersedia) dikonfigurasi dengan betul

## Memulakan dengan AI Toolkit

### Panduan Permulaan Pantas

Kami mengesyorkan bermula dengan model yang dihoskan oleh GitHub untuk pengalaman yang paling dipermudah:

1. **Pemasangan**: Ikuti [panduan pemasangan](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) untuk menyediakan AI Toolkit pada peranti anda
2. **Penemuan Model**: Dari paparan pokok sambungan, pilih **CATALOG > Models** untuk meneroka model yang tersedia
3. **Model GitHub**: Mulakan dengan model yang dihoskan oleh GitHub untuk integrasi yang optimal
4. **Ujian Playground**: Dari mana-mana kad model, pilih **Try in Playground** untuk mula bereksperimen dengan keupayaan model

### Langkah Demi Langkah Pembangunan AI Tepi

#### Langkah 1: Penjelajahan dan Pemilihan Model
1. Buka paparan AI Toolkit dalam Activity Bar VS Code
2. Jelajahi Katalog Model untuk model yang sesuai untuk pengedaran tepi
3. Tapis mengikut penyedia (GitHub, ONNX, Ollama) berdasarkan keperluan tepi anda
4. Gunakan **Try in Playground** untuk menguji keupayaan model dengan segera

#### Langkah 2: Pembangunan Agen
1. Gunakan **Prompt (Agent) Builder** untuk mencipta agen AI yang dioptimumkan untuk tepi
2. Hasilkan permulaan arahan menggunakan penerangan bahasa semula jadi  
3. Ulang dan perbaiki arahan berdasarkan respons model  
4. Integrasikan alat MCP untuk meningkatkan keupayaan agen  

#### Langkah 3: Ujian dan Penilaian  
1. Gunakan **Bulk Run** untuk menguji pelbagai arahan merentasi model yang dipilih  
2. Jalankan agen dengan kes ujian untuk mengesahkan fungsi  
3. Nilai ketepatan dan prestasi menggunakan metrik terbina dalam atau tersuai  
4. Bandingkan model dan konfigurasi yang berbeza  

#### Langkah 4: Penyesuaian dan Pengoptimuman  
1. Sesuaikan model untuk kes penggunaan khusus  
2. Terapkan penyesuaian khusus domain  
3. Optimumkan untuk kekangan pelaksanaan di peranti tepi  
4. Versikan dan bandingkan konfigurasi agen yang berbeza  

#### Langkah 5: Persediaan Pelaksanaan  
1. Hasilkan kod sedia produksi menggunakan Agent Builder  
2. Sediakan sambungan pelayan MCP untuk penggunaan produksi  
3. Sediakan pakej pelaksanaan untuk peranti tepi  
4. Konfigurasikan metrik pemantauan dan penilaian  

## Sampel untuk AI Toolkit  

Cuba Sampel Kami  
[Sampel AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) direka untuk membantu pembangun dan penyelidik meneroka serta melaksanakan penyelesaian AI dengan berkesan.  

Sampel kami termasuk:  

Kod Sampel: Contoh binaan untuk menunjukkan fungsi AI, seperti latihan, pelaksanaan, atau integrasi model ke dalam aplikasi.  
Dokumentasi: Panduan dan tutorial untuk membantu pengguna memahami ciri AI Toolkit dan cara menggunakannya.  
Keperluan  

- Visual Studio Code  
- AI Toolkit untuk Visual Studio Code  
- Token akses peribadi GitHub Fine-grained (PAT)  
- Foundry Local  

## Amalan Terbaik untuk Pembangunan AI Tepi  

### Pemilihan Model  
- **Kekangan Saiz**: Pilih model yang sesuai dengan had memori peranti sasaran  
- **Kelajuan Inferens**: Utamakan model dengan kelajuan inferens pantas untuk aplikasi masa nyata  
- **Pertukaran Ketepatan**: Imbangkan ketepatan model dengan kekangan sumber  
- **Keserasian Format**: Pilih format ONNX atau yang dioptimumkan untuk perkakasan bagi pelaksanaan tepi  

### Teknik Pengoptimuman  
- **Kuantisasi**: Gunakan kuantisasi INT8 atau INT4 untuk mengurangkan saiz model dan meningkatkan kelajuan  
- **Pemangkasan**: Buang parameter model yang tidak diperlukan untuk mengurangkan keperluan pengiraan  
- **Distilasi Pengetahuan**: Cipta model yang lebih kecil tetapi mengekalkan prestasi model yang lebih besar  
- **Pecutan Perkakasan**: Manfaatkan NPU, GPU, atau pemecut khusus jika tersedia  

### Aliran Kerja Pembangunan  
- **Ujian Berulang**: Uji secara kerap dalam keadaan seperti tepi semasa pembangunan  
- **Pemantauan Prestasi**: Pantau penggunaan sumber dan kelajuan inferens secara berterusan  
- **Kawalan Versi**: Jejak versi model dan tetapan pengoptimuman  
- **Dokumentasi**: Dokumentasikan semua keputusan pengoptimuman dan pertukaran prestasi  

### Pertimbangan Pelaksanaan  
- **Pemantauan Sumber**: Pantau penggunaan memori, CPU, dan kuasa dalam produksi  
- **Strategi Sandaran**: Laksanakan mekanisme sandaran untuk kegagalan model  
- **Mekanisme Kemas Kini**: Rancang untuk kemas kini model dan pengurusan versi  
- **Keselamatan**: Laksanakan langkah keselamatan yang sesuai untuk aplikasi AI tepi  

## Integrasi dengan Rangka Kerja AI Tepi  

### ONNX Runtime  
- **Pelaksanaan Merentas Platform**: Laksanakan model ONNX merentasi platform tepi yang berbeza  
- **Pengoptimuman Perkakasan**: Manfaatkan pengoptimuman khusus perkakasan ONNX Runtime  
- **Sokongan Mudah Alih**: Gunakan ONNX Runtime Mobile untuk aplikasi telefon pintar dan tablet  
- **Integrasi IoT**: Laksanakan pada peranti IoT menggunakan pengedaran ringan ONNX Runtime  

### Windows ML  
- **Peranti Windows**: Optimumkan untuk peranti tepi dan PC berasaskan Windows  
- **Pecutan NPU**: Manfaatkan Unit Pemprosesan Neural pada peranti Windows  
- **DirectML**: Gunakan DirectML untuk pecutan GPU pada platform Windows  
- **Integrasi UWP**: Integrasikan dengan aplikasi Universal Windows Platform  

### TensorFlow Lite  
- **Pengoptimuman Mudah Alih**: Laksanakan model TensorFlow Lite pada peranti mudah alih dan tertanam  
- **Delegasi Perkakasan**: Gunakan delegasi perkakasan khusus untuk pecutan  
- **Mikro Pengawal**: Laksanakan pada mikro pengawal menggunakan TensorFlow Lite Micro  
- **Sokongan Merentas Platform**: Laksanakan merentasi Android, iOS, dan sistem Linux tertanam  

### Azure IoT Edge  
- **Hibrid Awan-Tepi**: Gabungkan latihan awan dengan inferens tepi  
- **Pelaksanaan Modul**: Laksanakan model AI sebagai modul IoT Edge  
- **Pengurusan Peranti**: Urus peranti tepi dan kemas kini model dari jauh  
- **Telemetri**: Kumpulkan data prestasi dan metrik model dari pelaksanaan tepi  

## Senario AI Tepi Lanjutan  

### Pelaksanaan Multi-Model  
- **Ensemble Model**: Laksanakan pelbagai model untuk meningkatkan ketepatan atau redundansi  
- **Ujian A/B**: Uji model yang berbeza secara serentak pada peranti tepi  
- **Pemilihan Dinamik**: Pilih model berdasarkan keadaan semasa peranti  
- **Perkongsian Sumber**: Optimumkan penggunaan sumber merentasi model yang dilaksanakan  

### Pembelajaran Teragih  
- **Latihan Teragih**: Latih model merentasi pelbagai peranti tepi  
- **Pemeliharaan Privasi**: Kekalkan data latihan secara tempatan sambil berkongsi penambahbaikan model  
- **Pembelajaran Kolaboratif**: Benarkan peranti belajar daripada pengalaman kolektif  
- **Penyelarasan Tepi-Awan**: Selaraskan pembelajaran antara peranti tepi dan infrastruktur awan  

### Pemprosesan Masa Nyata  
- **Pemprosesan Aliran**: Proses aliran data berterusan pada peranti tepi  
- **Inferens Rendah Latensi**: Optimumkan untuk latensi inferens minimum  
- **Pemprosesan Batch**: Proses batch data dengan cekap pada peranti tepi  
- **Pemprosesan Adaptif**: Sesuaikan pemprosesan berdasarkan keupayaan semasa peranti  

## Penyelesaian Masalah Pembangunan AI Tepi  

### Isu Biasa  
- **Kekangan Memori**: Model terlalu besar untuk memori peranti sasaran  
- **Kelajuan Inferens**: Inferens model terlalu perlahan untuk keperluan masa nyata  
- **Kemerosotan Ketepatan**: Pengoptimuman mengurangkan ketepatan model secara tidak dapat diterima  
- **Keserasian Perkakasan**: Model tidak serasi dengan perkakasan sasaran  

### Strategi Penyahpepijat  
- **Profil Prestasi**: Gunakan ciri penjejakan AI Toolkit untuk mengenal pasti halangan  
- **Pemantauan Sumber**: Pantau penggunaan memori dan CPU semasa pembangunan  
- **Ujian Bertahap**: Uji pengoptimuman secara bertahap untuk mengasingkan isu  
- **Simulasi Perkakasan**: Gunakan alat pembangunan untuk mensimulasikan perkakasan sasaran  

### Penyelesaian Pengoptimuman  
- **Kuantisasi Lanjutan**: Terapkan teknik kuantisasi yang lebih agresif  
- **Seni Bina Model**: Pertimbangkan seni bina model yang dioptimumkan untuk tepi  
- **Pengoptimuman Prapemprosesan**: Optimumkan prapemprosesan data untuk kekangan tepi  
- **Pengoptimuman Inferens**: Gunakan pengoptimuman inferens khusus perkakasan  

## Sumber dan Langkah Seterusnya  

### Dokumentasi Rasmi  
- [Dokumentasi Pembangun AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Panduan Pemasangan dan Persediaan](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Dokumentasi Aplikasi Pintar VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Dokumentasi Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Komuniti dan Sokongan  
- [Repositori GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Isu dan Permintaan Ciri GitHub](https://aka.ms/AIToolkit/feedback)  
- [Komuniti Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Pasaran Sambungan VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Sumber Teknikal  
- [Dokumentasi ONNX Runtime](https://onnxruntime.ai/)  
- [Dokumentasi Ollama](https://ollama.ai/)  
- [Dokumentasi Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Dokumentasi Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Laluan Pembelajaran  
- [Kursus Asas AI Tepi](../Module01/README.md)  
- [Panduan Model Bahasa Kecil](../Module02/README.md)  
- [Strategi Pelaksanaan Tepi](../Module03/README.md)  
- [Pembangunan AI Tepi Windows](./windowdeveloper.md)  

### Sumber Tambahan  
- **Statistik Repositori**: 1.8k+ bintang, 150+ cabang, 18+ penyumbang  
- **Lesen**: Lesen MIT  
- **Keselamatan**: Polisi keselamatan Microsoft terpakai  
- **Telemetri**: Menghormati tetapan telemetri VS Code  

## Kesimpulan  

AI Toolkit untuk Visual Studio Code mewakili platform komprehensif untuk pembangunan AI moden, menyediakan keupayaan pembangunan agen yang dipermudahkan yang sangat bernilai untuk aplikasi AI tepi. Dengan katalog model yang luas menyokong penyedia seperti Anthropic, OpenAI, GitHub, dan Google, digabungkan dengan pelaksanaan tempatan melalui ONNX dan Ollama, toolkit ini menawarkan fleksibiliti yang diperlukan untuk pelbagai senario pelaksanaan tepi.  

Kekuatan toolkit terletak pada pendekatan bersepadu—daripada penemuan model dan eksperimen di Playground kepada pembangunan agen yang canggih dengan Prompt Builder, keupayaan penilaian yang komprehensif, dan integrasi alat MCP yang lancar. Bagi pembangun AI tepi, ini bermakna prototaip dan ujian agen AI yang pantas sebelum pelaksanaan tepi, dengan keupayaan untuk mengulang dengan cepat dan mengoptimumkan untuk persekitaran yang terhad sumber.  

Kelebihan utama untuk pembangunan AI tepi termasuk:  
- **Eksperimen Pantas**: Uji model dan agen dengan cepat sebelum komitmen kepada pelaksanaan tepi  
- **Fleksibiliti Multi-Penyedia**: Akses model dari pelbagai sumber untuk mencari penyelesaian tepi yang optimum  
- **Pembangunan Tempatan**: Uji dengan ONNX dan Ollama untuk pembangunan luar talian dan pemeliharaan privasi  
- **Kesediaan Produksi**: Hasilkan kod sedia produksi dan integrasikan dengan alat luaran melalui MCP  
- **Penilaian Komprehensif**: Gunakan metrik terbina dalam dan tersuai untuk mengesahkan prestasi AI tepi  

Apabila AI terus bergerak ke arah senario pelaksanaan tepi, AI Toolkit untuk VS Code menyediakan persekitaran pembangunan dan aliran kerja yang diperlukan untuk membina, menguji, dan mengoptimumkan aplikasi pintar untuk persekitaran yang terhad sumber. Sama ada anda sedang membangunkan penyelesaian IoT, aplikasi AI mudah alih, atau sistem kecerdasan tertanam, set ciri komprehensif toolkit dan aliran kerja bersepadu menyokong keseluruhan kitaran hayat pembangunan AI tepi.  

Dengan pembangunan berterusan dan komuniti yang aktif (1.8k+ bintang GitHub), AI Toolkit kekal di barisan hadapan alat pembangunan AI, terus berkembang untuk memenuhi keperluan pembangun AI moden yang membina untuk senario pelaksanaan tepi.  

[Next Foundry Local](./foundrylocal.md)  

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.