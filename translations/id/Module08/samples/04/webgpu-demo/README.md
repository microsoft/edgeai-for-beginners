# Demo WebGPU + ONNX Runtime

Demo ini menunjukkan cara menjalankan model AI langsung di browser menggunakan WebGPU untuk akselerasi perangkat keras dan ONNX Runtime Web.

## Apa yang Ditunjukkan

- **AI Berbasis Browser**: Menjalankan model sepenuhnya di browser
- **Akselerasi WebGPU**: Inferensi dengan akselerasi perangkat keras jika tersedia
- **Privasi Utama**: Tidak ada data yang meninggalkan perangkat Anda
- **Tanpa Instalasi**: Berfungsi di browser yang kompatibel
- **Fallback yang Mulus**: Beralih ke CPU jika WebGPU tidak tersedia

## Persyaratan

**Kompatibilitas Browser:**
- Chrome/Edge 113+ dengan WebGPU diaktifkan
- Periksa status WebGPU: `chrome://gpu`
- Aktifkan WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Menjalankan Demo

### Opsi 1: Server Lokal (Direkomendasikan)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Opsi 2: VS Code Live Server

1. Instal ekstensi "Live Server" di VS Code
2. Klik kanan `index.html` → "Open with Live Server"
3. Demo akan terbuka secara otomatis di browser

## Apa yang Akan Anda Lihat

1. **Deteksi WebGPU**: Memeriksa kompatibilitas browser
2. **Pemuatan Model**: Mengunduh dan menginisialisasi classifier MNIST
3. **Eksekusi Inferensi**: Menjalankan prediksi pada data sampel
4. **Metode Performa**: Menampilkan waktu pemuatan dan kecepatan inferensi
5. **Tampilan Hasil**: Kepercayaan prediksi dan output mentah

## Performa yang Diharapkan

| Penyedia Eksekusi | Pemuatan Model | Inferensi | Catatan |
|-------------------|----------------|-----------|---------|
| **WebGPU** | ~2-5s | ~10-50ms | Akselerasi perangkat keras |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Fallback perangkat lunak |

## Pemecahan Masalah

**WebGPU Tidak Tersedia:**
- Perbarui ke Chrome/Edge 113+
- Aktifkan WebGPU di `chrome://flags`
- Periksa apakah driver GPU sudah terbaru
- Demo akan otomatis beralih ke CPU

**Kesalahan Pemuatan:**
- Pastikan Anda menjalankan melalui HTTP (bukan file://)
- Periksa koneksi jaringan untuk mengunduh model
- Verifikasi bahwa CORS tidak memblokir model ONNX

**Masalah Performa:**
- WebGPU memberikan peningkatan kecepatan yang signifikan dibandingkan CPU
- Jalankan pertama mungkin lebih lambat karena pengunduhan model
- Jalankan berikutnya menggunakan cache browser

## Integrasi dengan Foundry Local

Demo WebGPU ini melengkapi Foundry Local dengan menunjukkan:

- **Inferensi sisi klien** untuk privasi maksimal
- **Kemampuan offline** saat internet tidak tersedia  
- **Penerapan edge** untuk lingkungan dengan sumber daya terbatas
- **Arsitektur hibrid** yang menggabungkan inferensi lokal dan server

Untuk aplikasi produksi, pertimbangkan:
- Gunakan Foundry Local untuk inferensi sisi server
- Gunakan WebGPU untuk preprocessing/postprocessing sisi klien
- Implementasikan routing cerdas antara inferensi lokal/remote

## Detail Teknis

**Model yang Digunakan:**
- Classifier digit MNIST (format ONNX)
- Input: Gambar grayscale 28x28
- Output: Distribusi probabilitas 10 kelas
- Ukuran: ~500KB (unduhan cepat)

**ONNX Runtime Web:**
- Penyedia eksekusi WebGPU untuk akselerasi GPU
- Penyedia eksekusi WASM untuk fallback CPU
- Optimasi otomatis dan optimasi graf

**API Browser:**
- WebGPU untuk akses perangkat keras
- Web Workers untuk pemrosesan latar belakang (peningkatan di masa depan)
- WebAssembly untuk komputasi yang efisien

## Langkah Selanjutnya

- Coba dengan model ONNX kustom
- Implementasikan pengunggahan gambar nyata dan klasifikasi
- Tambahkan inferensi streaming untuk model yang lebih besar
- Integrasikan dengan input kamera/mikrofon

---

