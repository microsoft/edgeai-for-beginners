<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e8d157e0a282083a1e1c7bb5dda28646",
  "translation_date": "2025-10-30T13:42:43+00:00",
  "source_file": "Module04/README.md",
  "language_code": "id"
}
-->
# Bab 04: Konversi Format Model dan Kuantisasi - Ikhtisar Bab

Kemunculan EdgeAI telah menjadikan konversi format model dan kuantisasi sebagai teknologi penting untuk menerapkan kemampuan pembelajaran mesin canggih pada perangkat dengan sumber daya terbatas. Bab ini memberikan panduan lengkap untuk memahami, menerapkan, dan mengoptimalkan model untuk skenario penerapan di edge.

## 📚 Struktur Bab dan Jalur Pembelajaran

Bab ini disusun dalam tujuh bagian progresif, masing-masing membangun pemahaman yang komprehensif tentang optimasi model untuk komputasi edge:

---

## [Bagian 1: Dasar-Dasar Konversi Format Model dan Kuantisasi](./01.Introduce.md)

### 🎯 Ikhtisar
Bagian dasar ini menetapkan kerangka teori untuk optimasi model di lingkungan komputasi edge, mencakup batas kuantisasi dari presisi 1-bit hingga 8-bit dan strategi konversi format utama.

**Topik Utama:**
- Kerangka klasifikasi presisi (ultra-rendah, rendah, presisi sedang)
- Keunggulan dan kasus penggunaan format GGUF dan ONNX
- Manfaat kuantisasi untuk efisiensi operasional dan fleksibilitas penerapan
- Perbandingan kinerja dan jejak memori

**Hasil Pembelajaran:**
- Memahami batas kuantisasi dan klasifikasi
- Mengidentifikasi teknik konversi format yang sesuai
- Mempelajari strategi optimasi lanjutan untuk penerapan di edge

---

## [Bagian 2: Panduan Implementasi Llama.cpp](./02.Llamacpp.md)

### 🎯 Ikhtisar
Tutorial lengkap untuk mengimplementasikan Llama.cpp, kerangka kerja C++ yang kuat untuk inferensi Model Bahasa Besar dengan pengaturan minimal di berbagai konfigurasi perangkat keras.

**Topik Utama:**
- Instalasi di platform Windows, macOS, dan Linux
- Konversi format GGUF dan berbagai tingkat kuantisasi (Q2_K hingga Q8_0)
- Akselerasi perangkat keras dengan CUDA, Metal, OpenCL, dan Vulkan
- Integrasi Python dan strategi penerapan produksi

**Hasil Pembelajaran:**
- Menguasai instalasi lintas platform dan membangun dari sumber
- Menerapkan teknik kuantisasi dan optimasi model
- Menerapkan model dalam mode server dengan integrasi REST API

---

## [Bagian 3: Microsoft Olive Optimization Suite](./03.MicrosoftOlive.md)

### 🎯 Ikhtisar
Eksplorasi Microsoft Olive, alat optimasi model yang sadar perangkat keras dengan lebih dari 40 komponen optimasi bawaan, dirancang untuk penerapan model tingkat perusahaan di berbagai platform perangkat keras.

**Topik Utama:**
- Fitur auto-optimasi dengan kuantisasi dinamis dan statis
- Intelijen yang sadar perangkat keras untuk penerapan CPU, GPU, dan NPU
- Dukungan model populer (Llama, Phi, Qwen, Gemma) secara langsung
- Integrasi perusahaan dengan Azure ML dan alur kerja produksi

**Hasil Pembelajaran:**
- Memanfaatkan optimasi otomatis untuk berbagai arsitektur model
- Menerapkan strategi penerapan lintas platform
- Membuat pipeline optimasi yang siap untuk perusahaan

---

## [Bagian 4: OpenVINO Toolkit Optimization Suite](./04.openvino.md)

### 🎯 Ikhtisar
Eksplorasi komprehensif toolkit OpenVINO dari Intel, platform open-source untuk menerapkan solusi AI yang berkinerja tinggi di lingkungan cloud, on-premises, dan edge dengan kemampuan Neural Network Compression Framework (NNCF) yang canggih.

**Topik Utama:**
- Penerapan lintas platform dengan akselerasi perangkat keras (CPU, GPU, VPU, akselerator AI)
- Neural Network Compression Framework (NNCF) untuk kuantisasi dan pruning tingkat lanjut
- OpenVINO GenAI untuk optimasi dan penerapan model bahasa besar
- Kemampuan server model tingkat perusahaan dan strategi penerapan yang skalabel

**Hasil Pembelajaran:**
- Menguasai alur kerja konversi dan optimasi model OpenVINO
- Menerapkan teknik kuantisasi tingkat lanjut dengan NNCF
- Menerapkan model yang dioptimalkan di berbagai platform perangkat keras dengan Model Server

---

## [Bagian 5: Pendalaman Kerangka Apple MLX](./05.AppleMLX.md)

### 🎯 Ikhtisar
Cakupan komprehensif Apple MLX, kerangka kerja revolusioner yang dirancang khusus untuk pembelajaran mesin yang efisien pada Apple Silicon, dengan penekanan pada kemampuan Model Bahasa Besar dan penerapan lokal.

**Topik Utama:**
- Keunggulan arsitektur memori terpadu dan Metal Performance Shaders
- Dukungan untuk model LLaMA, Mistral, Phi-3, Qwen, dan Code Llama
- Fine-tuning LoRA untuk kustomisasi model yang efisien
- Integrasi Hugging Face dan dukungan kuantisasi (4-bit dan 8-bit)

**Hasil Pembelajaran:**
- Menguasai optimasi Apple Silicon untuk penerapan LLM
- Menerapkan teknik fine-tuning dan kustomisasi model
- Membangun aplikasi AI tingkat perusahaan dengan fitur privasi yang ditingkatkan

---

## [Bagian 6: Sintesis Alur Kerja Pengembangan Edge AI](./06.workflow-synthesis.md)

### 🎯 Ikhtisar
Sintesis komprehensif semua kerangka optimasi ke dalam alur kerja terpadu, matriks keputusan, dan praktik terbaik untuk penerapan Edge AI yang siap produksi di berbagai platform dan kasus penggunaan termasuk mobile, desktop, dan cloud.

**Topik Utama:**
- Arsitektur alur kerja terpadu yang mengintegrasikan berbagai kerangka optimasi
- Pohon keputusan pemilihan kerangka kerja dan analisis trade-off kinerja
- Validasi kesiapan produksi dan strategi penerapan yang komprehensif
- Strategi untuk masa depan perangkat keras dan arsitektur model yang muncul

**Hasil Pembelajaran:**
- Menguasai pemilihan kerangka kerja secara sistematis berdasarkan kebutuhan dan batasan
- Menerapkan pipeline Edge AI yang siap produksi dengan pemantauan yang komprehensif
- Merancang alur kerja yang dapat beradaptasi dengan teknologi dan kebutuhan yang berkembang

---

## [Bagian 7: Qualcomm QNN Optimization Suite](./07.QualcommQNN.md)

### 🎯 Ikhtisar
Eksplorasi komprehensif Qualcomm QNN (Qualcomm Neural Network), kerangka inferensi AI terpadu yang dirancang untuk memanfaatkan arsitektur komputasi heterogen Qualcomm termasuk Hexagon NPU, Adreno GPU, dan Kryo CPU untuk kinerja maksimal dan efisiensi energi pada perangkat mobile dan edge.

**Topik Utama:**
- Komputasi heterogen dengan akses terpadu ke NPU, GPU, dan CPU
- Optimasi yang sadar perangkat keras untuk platform Snapdragon dengan distribusi beban kerja yang cerdas
- Teknik kuantisasi tingkat lanjut (INT8, INT16, presisi campuran) untuk penerapan mobile
- Inferensi hemat daya yang dioptimalkan untuk perangkat bertenaga baterai dan aplikasi real-time

**Hasil Pembelajaran:**
- Menguasai akselerasi perangkat keras Qualcomm untuk penerapan AI mobile
- Menerapkan strategi optimasi hemat daya untuk komputasi edge
- Menerapkan model yang siap produksi di ekosistem Qualcomm dengan kinerja optimal

---

## 🎯 Hasil Pembelajaran Bab

Setelah menyelesaikan bab ini, pembaca akan mencapai:

### **Penguasaan Teknis**
- Pemahaman mendalam tentang batas kuantisasi dan aplikasi praktis
- Pengalaman langsung dengan berbagai kerangka optimasi
- Keterampilan penerapan produksi untuk lingkungan komputasi edge

### **Pemahaman Strategis**
- Kemampuan pemilihan optimasi yang sadar perangkat keras
- Pengambilan keputusan yang terinformasi tentang trade-off kinerja
- Strategi penerapan dan pemantauan yang siap untuk perusahaan

### **Benchmark Kinerja**

| Kerangka | Kuantisasi | Penggunaan Memori | Peningkatan Kecepatan | Kasus Penggunaan |
|----------|------------|-------------------|-----------------------|------------------|
| Llama.cpp | Q4_K_M | ~4GB | 2-3x | Penerapan lintas platform |
| Olive | INT4 | Pengurangan 60-75% | 2-6x | Alur kerja perusahaan |
| OpenVINO | INT8/INT4 | Pengurangan 50-75% | 2-5x | Optimasi perangkat keras Intel |
| QNN | INT8/INT4 | Pengurangan 50-80% | 5-15x | Mobile/edge Qualcomm |
| MLX | 4-bit | ~4GB | 2-4x | Optimasi Apple Silicon |

## 🚀 Langkah Selanjutnya dan Aplikasi Lanjutan

Bab ini memberikan dasar lengkap untuk:
- Pengembangan model kustom untuk domain spesifik
- Penelitian dalam optimasi Edge AI
- Pengembangan aplikasi AI komersial
- Penerapan Edge AI tingkat perusahaan dalam skala besar

Pengetahuan dari tujuh bagian ini menawarkan toolkit komprehensif untuk menjelajahi lanskap yang terus berkembang dalam optimasi dan penerapan model AI di edge.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.