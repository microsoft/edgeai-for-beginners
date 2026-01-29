# Modul 08 Contoh: Panduan Pengembangan Lokal Foundry

## Ikhtisar

Koleksi ini memberikan demonstrasi lengkap tentang pendekatan **Foundry Local SDK** dan **Perintah Shell** untuk membangun aplikasi AI siap produksi. Setiap contoh menampilkan berbagai aspek pengembangan AI di edge, mulai dari integrasi REST dasar hingga sistem multi-agen yang canggih.

## Pendekatan Pengembangan: SDK vs Perintah Shell

### Gunakan Foundry Local SDK Ketika:

- **Kontrol Programatik**: Anda membutuhkan kontrol penuh atas siklus hidup agen, evaluasi, atau alur kerja penerapan
- **Alat Kustom**: Membangun otomatisasi di sekitar Foundry Local (integrasi CI/CD, orkestrasi multi-agen)
- **Akses Mendetail**: Memerlukan metadata agen yang rinci, versi, atau kontrol evaluasi runner
- **Integrasi Python**: Bekerja di lingkungan yang banyak menggunakan Python atau menyematkan logika Foundry ke dalam aplikasi yang lebih luas
- **Alur Kerja Perusahaan**: Mengimplementasikan alur kerja modular dan pipeline evaluasi yang dapat direproduksi sesuai dengan arsitektur referensi Microsoft

### Gunakan Perintah Shell Ketika:

- **Pengujian Cepat**: Melakukan pengujian lokal cepat, peluncuran agen manual, atau verifikasi pengaturan
- **Kesederhanaan CLI**: Membutuhkan operasi CLI yang sederhana untuk memulai/menghentikan agen, memeriksa log, atau evaluasi dasar
- **Otomatisasi Ringan**: Menyusun skrip otomatisasi sederhana tanpa kebutuhan integrasi SDK penuh
- **Iterasi Cepat**: Siklus debugging dan pengembangan, terutama di lingkungan yang terbatas atau penerapan tingkat grup sumber daya
- **Pengaturan & Validasi**: Konfigurasi awal lingkungan dan tugas verifikasi cepat

## Praktik Terbaik & Alur Kerja yang Direkomendasikan

Berdasarkan prinsip manajemen siklus hidup agen, pelacakan dependensi, dan reproduktibilitas dengan hak akses minimal:

### Fase 1: Dasar & Pengaturan
1. **Mulai dengan Perintah Shell** untuk pengaturan awal dan validasi cepat
2. **Verifikasi Lingkungan** menggunakan alat CLI dan penerapan model dasar
3. **Uji Konektivitas** dengan panggilan REST sederhana dan pemeriksaan kesehatan

### Fase 2: Pengembangan & Integrasi
1. **Beralih ke SDK** untuk alur kerja yang skalabel dan dapat dilacak
2. **Implementasikan Kontrol Programatik** untuk interaksi agen yang kompleks
3. **Bangun Alat Kustom** untuk template siap komunitas dan integrasi Azure OpenAI

### Fase 3: Produksi & Skalabilitas
1. **Pendekatan Hibrid** yang menggabungkan CLI untuk operasi dan SDK untuk logika aplikasi
2. **Integrasi Perusahaan** dengan pemantauan, pencatatan, dan pipeline penerapan
3. **Kontribusi Komunitas** melalui template yang dapat digunakan kembali dan praktik terbaik

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.