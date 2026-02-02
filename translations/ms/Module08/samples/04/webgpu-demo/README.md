# WebGPU + ONNX Runtime Demo

Demo ini menunjukkan cara menjalankan model AI secara langsung dalam pelayar menggunakan WebGPU untuk pecutan perkakasan dan ONNX Runtime Web.

## Apa Yang Ditunjukkan

- **AI Berasaskan Pelayar**: Jalankan model sepenuhnya dalam pelayar
- **Pecutan WebGPU**: Inferens dipercepatkan perkakasan apabila tersedia
- **Privasi Utama**: Tiada data meninggalkan peranti anda
- **Tanpa Pemasangan**: Berfungsi dalam mana-mana pelayar yang serasi
- **Fallback Lancar**: Beralih kepada CPU jika WebGPU tidak tersedia

## Keperluan

**Keserasian Pelayar:**
- Chrome/Edge 113+ dengan WebGPU diaktifkan
- Semak status WebGPU: `chrome://gpu`
- Aktifkan WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Menjalankan Demo

### Pilihan 1: Pelayan Tempatan (Disyorkan)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Pilihan 2: VS Code Live Server

1. Pasang sambungan "Live Server" dalam VS Code
2. Klik kanan `index.html` → "Open with Live Server"
3. Demo akan dibuka secara automatik dalam pelayar

## Apa Yang Akan Anda Lihat

1. **Pengesanan WebGPU**: Memeriksa keserasian pelayar
2. **Pemuatan Model**: Memuat turun dan memulakan pengklasifikasi MNIST
3. **Pelaksanaan Inferens**: Menjalankan ramalan pada data sampel
4. **Metrik Prestasi**: Menunjukkan masa pemuatan dan kelajuan inferens
5. **Paparan Keputusan**: Keyakinan ramalan dan output mentah

## Prestasi Dijangka

| Penyedia Pelaksanaan | Pemuatan Model | Inferens | Nota |
|-----------------------|----------------|----------|------|
| **WebGPU**           | ~2-5s         | ~10-50ms | Dipercepatkan perkakasan |
| **CPU (WASM)**       | ~2-5s         | ~50-200ms| Fallback perisian |

## Penyelesaian Masalah

**WebGPU Tidak Tersedia:**
- Kemas kini kepada Chrome/Edge 113+
- Aktifkan WebGPU dalam `chrome://flags`
- Pastikan pemacu GPU terkini
- Demo akan secara automatik beralih kepada CPU

**Ralat Pemuatan:**
- Pastikan anda menggunakan HTTP (bukan file://)
- Semak sambungan rangkaian untuk muat turun model
- Pastikan CORS tidak menyekat model ONNX

**Isu Prestasi:**
- WebGPU memberikan peningkatan kelajuan yang ketara berbanding CPU
- Jalankan pertama mungkin lebih perlahan kerana muat turun model
- Jalankan seterusnya menggunakan cache pelayar

## Integrasi dengan Foundry Local

Demo WebGPU ini melengkapi Foundry Local dengan menunjukkan:

- **Inferens sisi klien** untuk privasi maksimum
- **Keupayaan luar talian** apabila internet tidak tersedia  
- **Penggunaan di tepi** untuk persekitaran dengan sumber terhad
- **Seni bina hibrid** yang menggabungkan inferens tempatan dan pelayan

Untuk aplikasi produksi, pertimbangkan:
- Gunakan Foundry Local untuk inferens sisi pelayan
- Gunakan WebGPU untuk prapemprosesan/pemprosesan pasca sisi klien
- Laksanakan penghalaan pintar antara inferens tempatan/jarak jauh

## Butiran Teknikal

**Model Digunakan:**
- Pengklasifikasi digit MNIST (format ONNX)
- Input: Imej skala kelabu 28x28
- Output: Pengagihan kebarangkalian 10 kelas
- Saiz: ~500KB (muat turun pantas)

**ONNX Runtime Web:**
- Penyedia pelaksanaan WebGPU untuk pecutan GPU
- Penyedia pelaksanaan WASM untuk fallback CPU
- Pengoptimuman automatik dan pengoptimuman graf

**API Pelayar:**
- WebGPU untuk akses perkakasan
- Web Workers untuk pemprosesan latar belakang (peningkatan masa depan)
- WebAssembly untuk pengiraan yang cekap

## Langkah Seterusnya

- Cuba dengan model ONNX tersuai
- Laksanakan muat naik imej sebenar dan klasifikasi
- Tambah inferens penstriman untuk model yang lebih besar
- Integrasi dengan input kamera/mikrofon

---

