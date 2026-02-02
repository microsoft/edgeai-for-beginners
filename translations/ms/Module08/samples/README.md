# Modul 08 Contoh: Panduan Pembangunan Tempatan Foundry

## Gambaran Keseluruhan

Koleksi komprehensif ini menunjukkan pendekatan **Foundry Local SDK** dan **Shell Command** untuk membina aplikasi AI yang bersedia untuk pengeluaran. Setiap contoh mempamerkan aspek berbeza pembangunan AI di hujung, daripada integrasi REST asas hingga sistem multi-ejen yang canggih.

## Pendekatan Pembangunan: SDK vs Shell Commands

### Gunakan Foundry Local SDK Apabila:

- **Kawalan Programatik**: Anda memerlukan kawalan penuh ke atas kitaran hayat ejen, penilaian, atau aliran kerja penyebaran
- **Alat Tersuai**: Membina automasi di sekitar Foundry Local (integrasi CI/CD, orkestrasi multi-ejen)
- **Akses Terperinci**: Memerlukan metadata ejen yang terperinci, versi, atau kawalan pelari penilaian
- **Integrasi Python**: Bekerja dalam persekitaran yang banyak menggunakan Python atau menggabungkan logik Foundry ke dalam aplikasi yang lebih luas
- **Aliran Kerja Perusahaan**: Melaksanakan aliran kerja modular dan saluran penilaian yang boleh dihasilkan semula sejajar dengan seni bina rujukan Microsoft

### Gunakan Shell Commands Apabila:

- **Ujian Pantas**: Melakukan ujian tempatan yang cepat, pelancaran ejen secara manual, atau pengesahan persediaan
- **Kesederhanaan CLI**: Memerlukan operasi CLI yang mudah untuk memulakan/menghentikan ejen, memeriksa log, atau penilaian asas
- **Automasi Ringan**: Menulis skrip automasi mudah tanpa keperluan integrasi SDK penuh
- **Iterasi Pantas**: Kitaran debugging dan pembangunan, terutamanya dalam persekitaran yang terhad atau penyebaran pada tahap kumpulan sumber
- **Persediaan & Pengesahan**: Konfigurasi persekitaran awal dan tugas pengesahan cepat

## Amalan Terbaik & Aliran Kerja yang Disyorkan

Berdasarkan pengurusan kitaran hayat ejen, penjejakan kebergantungan, dan prinsip kebolehhasilan dengan keistimewaan minimum:

### Fasa 1: Asas & Persediaan
1. **Mulakan dengan Shell Commands** untuk persediaan awal dan pengesahan cepat
2. **Sahkan Persekitaran** menggunakan alat CLI dan penyebaran model asas
3. **Uji Sambungan** dengan panggilan REST mudah dan pemeriksaan kesihatan

### Fasa 2: Pembangunan & Integrasi
1. **Berpindah ke SDK** untuk aliran kerja yang boleh diskalakan dan boleh dijejaki
2. **Laksanakan Kawalan Programatik** untuk interaksi ejen yang kompleks
3. **Bina Alat Tersuai** untuk templat yang bersedia untuk komuniti dan integrasi Azure OpenAI

### Fasa 3: Pengeluaran & Skala
1. **Pendekatan Hibrid** menggabungkan CLI untuk operasi dan SDK untuk logik aplikasi
2. **Integrasi Perusahaan** dengan pemantauan, log, dan saluran penyebaran
3. **Sumbangan Komuniti** melalui templat yang boleh digunakan semula dan amalan terbaik

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.