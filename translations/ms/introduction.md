# Pengenalan kepada Edge AI untuk Pemula

![Pengenalan Edge AI](../../translated_images/ms/cover.eb18d1b9605d754b.webp)

Selamat datang ke perjalanan anda dalam **Kecerdasan Buatan Edge** – pendekatan revolusioner yang membawa kuasa AI terus ke tempat data dihasilkan dan keputusan perlu dibuat. Pengenalan ini akan membina asas untuk memahami mengapa Edge AI mewakili masa depan pengkomputeran pintar dan bagaimana anda boleh menguasai pelaksanaannya.

## Apa itu Edge AI?

Edge AI mewakili perubahan asas daripada pemprosesan AI berasaskan awan tradisional kepada **kecerdasan tempatan, pada peranti**. Daripada menghantar data ke pelayan jauh, Edge AI memproses maklumat secara langsung pada peranti edge – telefon pintar, sensor IoT, peralatan industri, kenderaan autonomi, dan sistem terbenam.

### Paradigma Edge AI

```
Traditional AI:     Device → Cloud → Processing → Response → Device
Edge AI:           Device → Local Processing → Immediate Response
```

Peralihan paradigma ini menghapuskan perjalanan ulang-alik ke awan, membolehkan:
- **Tindak balas segera** (latensi sub-milisaat)
- **Privasi dipertingkatkan** (data tidak pernah meninggalkan peranti)
- **Operasi yang boleh dipercayai** (berfungsi tanpa sambungan internet)
- **Kos yang dikurangkan** (penggunaan jalur lebar dan pemprosesan awan yang minimum)

## Mengapa Edge AI Penting Sekarang

### Gabungan Inovasi yang Sempurna

Tiga trend teknologi telah bergabung untuk menjadikan Edge AI bukan sahaja mungkin, tetapi penting:

1. **Revolusi Perkakasan**: Cip moden (Apple Silicon, Qualcomm Snapdragon, NVIDIA Jetson) kini mempunyai pecutan AI dalam pakej yang padat dan cekap tenaga
2. **Pengoptimuman Model**: Model Bahasa Kecil (SLM) seperti Phi-4, Gemma, dan Mistral memberikan 80-90% prestasi model besar dalam saiz 10-20%
3. **Permintaan Dunia Nyata**: Industri memerlukan AI yang segera, peribadi, dan boleh dipercayai yang tidak dapat disediakan oleh penyelesaian awan

### Pemacu Perniagaan Kritikal

**Privasi & Pematuhan**
- Kesihatan: Data pesakit mesti kekal di premis (pematuhan HIPAA)
- Kewangan: Pemprosesan transaksi memerlukan kedaulatan data
- Pembuatan: Proses proprietari perlu dilindungi daripada pendedahan

**Keperluan Prestasi**
- Kenderaan autonomi: Keputusan kritikal dalam kehidupan dalam milisaat
- Automasi industri: Kawalan kualiti dan pemantauan keselamatan masa nyata
- Permainan & AR/VR: Pengalaman imersif memerlukan latensi sifar yang boleh dirasai

**Kecekapan Ekonomi**
- Telekomunikasi: Memproses berjuta-juta bacaan sensor IoT secara tempatan
- Runcit: Analitik dalam kedai tanpa kos jalur lebar yang besar
- Bandar pintar: Kecerdasan teragih merentasi ribuan peranti

## Industri yang Diubah oleh Edge AI

### 🏭 **Pembuatan & Industri 4.0**
- **Penyelenggaraan Ramalan**: Model AI pada peralatan industri meramalkan kegagalan sebelum ia berlaku
- **Kawalan Kualiti**: Pengesanan kecacatan masa nyata pada barisan pengeluaran
- **Pemantauan Keselamatan**: Pengesanan bahaya segera dan tindak balas
- **Rantaian Bekalan**: Pengurusan inventori pintar di setiap nod

**Kesan Dunia Nyata**: Siemens menggunakan Edge AI untuk penyelenggaraan ramalan, mengurangkan masa henti sebanyak 30-50% dan kos penyelenggaraan sebanyak 25%.

### 🏥 **Kesihatan & Peranti Perubatan**
- **Pencitraan Diagnostik**: Analisis X-ray dan MRI berkuasa AI di tempat rawatan
- **Pemantauan Pesakit**: Penilaian kesihatan berterusan melalui peranti boleh pakai
- **Bantuan Pembedahan**: Panduan masa nyata semasa prosedur
- **Penemuan Ubat**: Pemprosesan tempatan simulasi molekul

**Kesan Dunia Nyata**: Penyelesaian Edge AI Philips membolehkan pakar radiologi mendiagnosis keadaan 40% lebih cepat sambil mengekalkan ketepatan 99%.

### 🚗 **Sistem Autonomi & Pengangkutan**
- **Kenderaan Pandu Sendiri**: Pembuatan keputusan dalam masa singkat untuk navigasi dan keselamatan
- **Pengurusan Trafik**: Kawalan persimpangan pintar dan pengoptimuman aliran
- **Operasi Armada**: Pengoptimuman laluan masa nyata dan pemantauan kesihatan kenderaan
- **Logistik**: Robot gudang autonomi dan sistem penghantaran

**Kesan Dunia Nyata**: Sistem Pandu Sendiri Penuh Tesla memproses data sensor secara tempatan, membuat lebih daripada 40 keputusan sesaat untuk navigasi autonomi yang selamat.

### 🏙️ **Bandar Pintar & Infrastruktur**
- **Keselamatan Awam**: Pengesanan ancaman masa nyata dan tindak balas kecemasan
- **Pengurusan Tenaga**: Pengoptimuman grid pintar dan integrasi tenaga boleh diperbaharui
- **Pemantauan Alam Sekitar**: Kualiti udara, pencemaran bunyi, dan penjejakan iklim
- **Perancangan Bandar**: Analisis aliran trafik dan pengoptimuman infrastruktur

**Kesan Dunia Nyata**: Inisiatif bandar pintar Singapura menggunakan lebih daripada 100,000 sensor Edge AI untuk pengurusan trafik, mengurangkan masa perjalanan sebanyak 25%.

### 📱 **Teknologi Pengguna & Mudah Alih**
- **AI Telefon Pintar**: Fotografi yang dipertingkatkan, pembantu suara, dan personalisasi
- **Rumah Pintar**: Automasi pintar dan sistem keselamatan
- **Peranti Boleh Pakai**: Pemantauan kesihatan dan pengoptimuman kecergasan
- **Permainan**: Peningkatan grafik masa nyata dan pengoptimuman permainan

**Kesan Dunia Nyata**: Enjin Neural Apple memproses 15.8 trilion operasi sesaat secara tempatan, membolehkan ciri seperti terjemahan bahasa masa nyata dan fotografi komputasi.

## Model Bahasa Kecil: Enjin Edge AI

### Apa itu Model Bahasa Kecil (SLM)?

SLM ialah **versi mampat dan dioptimumkan** model bahasa besar, direka khusus untuk penggunaan edge:

- **Phi-4**: 14B parameter, dioptimumkan untuk penaakulan dan penjanaan kod
- **Gemma 2B/7B**: Model cekap Google untuk pelbagai tugas NLP
- **Mistral-7B**: Model berprestasi tinggi dengan pelesenan mesra komersial
- **Siri Qwen**: Model pelbagai bahasa Alibaba yang dioptimumkan untuk penggunaan mudah alih

### Kelebihan SLM

| Keupayaan | Model Bahasa Besar | Model Bahasa Kecil |
|-----------|---------------------|---------------------|
| **Saiz** | 70B-405B parameter | 1B-14B parameter |
| **Memori** | 40-200GB RAM | 2-16GB RAM |
| **Kelajuan Inferens** | 2-10 saat | 50-500ms |
| **Penggunaan** | Pelayan berprestasi tinggi | Telefon pintar, peranti terbenam |
| **Kos** | $1000s/bulan | Kos perkakasan sekali sahaja |
| **Privasi** | Data dihantar ke awan | Pemprosesan kekal tempatan |

### Realiti Prestasi

SLM moden mencapai keupayaan yang luar biasa:
- **90% prestasi GPT-3.5** dalam banyak tugas
- **Keupayaan perbualan masa nyata**
- **Penjanaan dan penyahpepijatan kod**
- **Terjemahan pelbagai bahasa**
- **Analisis dan ringkasan dokumen**

## Objektif Pembelajaran

Dengan melengkapkan kursus EdgeAI untuk Pemula ini, anda akan:

### 🎯 **Pengetahuan Asas**
- Memahami pemacu teknikal dan perniagaan di sebalik penerimaan Edge AI
- Membandingkan seni bina AI edge vs. awan dan kes penggunaan yang sesuai
- Mengenal pasti ciri dan keupayaan keluarga SLM yang berbeza
- Menganalisis keperluan perkakasan untuk penggunaan Edge AI

### 🛠️ **Kemahiran Teknikal**
- Menggunakan SLM pada platform yang pelbagai (Windows, mudah alih, terbenam, hibrid awan-edge)
- Mengoptimumkan model untuk kekangan edge menggunakan kuantisasi, pemangkasan, dan pemampatan
- Melaksanakan aplikasi Edge AI yang sedia untuk pengeluaran dengan pemantauan dan penskalaan
- Membina sistem berbilang ejen dan rangka kerja panggilan fungsi untuk aliran kerja yang kompleks

### 🏗️ **Pelaksanaan Praktikal**
- Mencipta aplikasi sembang dengan penukaran model tempatan dan pengurusan perbualan
- Membangunkan sistem RAG (Retrieval-Augmented Generation) dengan pemprosesan dokumen tempatan
- Membina router model yang memilih secara pintar antara model AI khusus
- Merancang rangka kerja API dengan penstriman, pemantauan kesihatan, dan pengendalian ralat

### 🚀 **Penggunaan Pengeluaran**
- Menubuhkan saluran SLMOps untuk versi model, ujian, dan penggunaan
- Melaksanakan amalan terbaik keselamatan untuk aplikasi Edge AI
- Merancang seni bina yang boleh diskalakan yang mengimbangi pemprosesan edge dan awan
- Mencipta strategi pemantauan dan penyelenggaraan untuk sistem Edge AI pengeluaran

## Hasil Pembelajaran

Setelah tamat kursus, anda akan dilengkapi untuk:

### **Penguasaan Teknikal**
✅ **Menggunakan penyelesaian Edge AI yang sedia untuk pengeluaran** merentasi Windows, mudah alih, dan platform terbenam  
✅ **Mengoptimumkan model AI untuk kekangan edge** mencapai pengurangan saiz sebanyak 75% dengan pengekalan prestasi sebanyak 85%  
✅ **Membina sistem ejen pintar** dengan panggilan fungsi dan orkestrasi berbilang model  
✅ **Mencipta seni bina hibrid edge-awanan yang boleh diskalakan** untuk aplikasi perusahaan  

### **Aplikasi Industri**
✅ **Merancang penyelesaian pembuatan** untuk penyelenggaraan ramalan dan kawalan kualiti  
✅ **Membangunkan aplikasi kesihatan** dengan pemprosesan data pesakit yang mematuhi privasi  
✅ **Membina sistem automotif** untuk pembuatan keputusan masa nyata dan keselamatan  
✅ **Mencipta infrastruktur bandar pintar** untuk trafik, keselamatan, dan pemantauan alam sekitar  

### **Kemajuan Kerjaya**
✅ **Arkitek Penyelesaian EdgeAI**: Merancang strategi Edge AI yang komprehensif  
✅ **Jurutera ML (Kepakaran Edge)**: Mengoptimumkan dan menggunakan model untuk persekitaran edge  
✅ **Pembangun IoT AI**: Mencipta sistem IoT pintar dengan pemprosesan tempatan  
✅ **Pembangun AI Mudah Alih**: Membina aplikasi mudah alih berkuasa AI dengan inferens tempatan  

## Seni Bina Kursus

Kursus ini mengikuti pendekatan **penguasaan progresif**:

### **Fasa 1: Asas** (Modul 01-02)
Membina pemahaman konsep dan meneroka keluarga model

### **Fasa 2: Pelaksanaan** (Modul 03-04) 
Menguasai teknik penggunaan dan pengoptimuman

### **Fasa 3: Pengeluaran** (Modul 05-06)
Belajar SLMOps dan rangka kerja ejen lanjutan

### **Fasa 4: Pengkhususan** (Modul 07-08)
Pelaksanaan khusus platform dan sampel komprehensif

## Metrik Kejayaan

Jejaki kemajuan anda dengan hasil konkrit ini:

- **Projek Portfolio**: 10+ aplikasi sedia pengeluaran merentasi pelbagai industri
- **Penanda Aras Prestasi**: Model berjalan dengan masa inferens <500ms pada peranti edge
- **Sasaran Penggunaan**: Aplikasi berjalan pada Windows, mudah alih, dan platform terbenam
- **Kesediaan Perusahaan**: Penyelesaian dengan rangka kerja pemantauan, penskalaan, dan keselamatan

## Memulakan

Bersedia untuk mengubah pemahaman anda tentang penggunaan AI? Perjalanan anda bermula dengan **[Modul 01: Asas EdgeAI](./Module01/README.md)**, di mana anda akan meneroka asas teknikal yang menjadikan Edge AI mungkin dan mengkaji kajian kes dunia nyata daripada pemimpin industri.

**Langkah Seterusnya**: [📚 Modul 01 - Asas EdgeAI →](./Module01/README.md)

---

**Masa depan AI adalah tempatan, segera, dan peribadi. Kuasai Edge AI untuk membina aplikasi pintar generasi akan datang.**

---

