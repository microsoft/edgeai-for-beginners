# Skrip Workshop

Direktori ini berisi skrip otomatisasi dan pendukung yang digunakan untuk menjaga kualitas dan konsistensi materi Workshop.

## Isi

| File | Tujuan |
|------|--------|
| `lint_markdown_cli.py` | Memeriksa kode markdown untuk memblokir pola perintah Foundry Local CLI yang sudah usang. |
| `export_benchmark_markdown.py` | Menjalankan benchmark latensi multi-model dan menghasilkan laporan dalam format Markdown + JSON. |

## 1. Linter Pola Markdown CLI

`lint_markdown_cli.py` memindai semua file `.md` non-terjemahan untuk pola Foundry Local CLI yang tidak diizinkan **di dalam blok kode berpagar** (``` ... ```). Prosa informatif masih dapat menyebutkan perintah yang sudah usang untuk konteks historis.

### Pola Usang (Diblokir di Dalam Blok Kode)

Linter memblokir pola CLI yang sudah usang. Gunakan alternatif modern sebagai gantinya.

### Penggantian yang Diperlukan
| Usang | Gunakan Sebagai Pengganti |
|-------|---------------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Skrip benchmark + alat sistem (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Kode Keluar
| Kode | Makna |
|------|-------|
| 0 | Tidak ada pelanggaran yang terdeteksi |
| 1 | Satu atau lebih pola usang ditemukan |

### Menjalankan Secara Lokal
Dari root repositori (disarankan):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Hook Pre-Commit (Opsional)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Ini memblokir commit yang memperkenalkan pola usang.

### Integrasi CI
Workflow GitHub Action (`.github/workflows/markdown-cli-lint.yml`) menjalankan linter pada setiap push dan pull request ke cabang `main` dan `Reactor`. Job yang gagal harus diperbaiki sebelum merging.

### Menambahkan Pola Usang Baru
1. Buka `lint_markdown_cli.py`.
2. Tambahkan tuple `(regex, suggestion)` ke daftar `DEPRECATED`. Gunakan string mentah dan sertakan batas kata `\b` jika diperlukan.
3. Jalankan linter secara lokal untuk memverifikasi deteksi.
4. Commit dan push; CI akan menerapkan aturan baru.

Contoh penambahan:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Mengizinkan Penyebutan Penjelasan
Karena hanya blok kode berpagar yang ditegakkan, Anda dapat menjelaskan perintah usang dalam teks naratif dengan aman. Jika Anda *harus* menunjukkannya di dalam blok berpagar untuk perbandingan, tambahkan blok berpagar **tanpa** tanda backtick tiga (misalnya, indentasi atau kutipan) atau ubah ke bentuk pseudo.

### Melewati File Tertentu (Lanjutan)
Jika diperlukan, bungkus contoh warisan dalam file terpisah di luar repositori atau ubah nama dengan ekstensi berbeda saat menyusun. Pengabaian yang disengaja untuk salinan terjemahan dilakukan secara otomatis (jalur yang mengandung `translations`).

### Pemecahan Masalah
| Masalah | Penyebab | Resolusi |
|---------|----------|----------|
| Linter menandai baris yang Anda perbarui | Regex terlalu luas | Persempit pola dengan batas kata tambahan (`\b`) atau penanda |
| CI gagal tetapi lokal berhasil | Versi Python berbeda atau perubahan belum di-commit | Jalankan ulang secara lokal, pastikan tree kerja bersih, periksa versi Python workflow (3.11) |
| Perlu melewati sementara | Perbaikan darurat | Terapkan perbaikan segera setelahnya; pertimbangkan menggunakan cabang sementara dan PR lanjutan (hindari menambahkan saklar bypass) |

### Alasan
Menjaga dokumentasi tetap selaras dengan permukaan CLI stabil *saat ini* mencegah friksi workshop, menghindari kebingungan peserta, dan memusatkan pengukuran kinerja melalui skrip Python yang terpelihara daripada subperintah CLI yang tidak konsisten.

---
Dipelihara sebagai bagian dari toolchain kualitas workshop. Untuk peningkatan (misalnya, saran perbaikan otomatis atau pembuatan laporan HTML), buka issue atau kirimkan PR.

## 2. Skrip Validasi Contoh

`validate_samples.py` memvalidasi semua file contoh Python untuk sintaks, impor, dan kepatuhan terhadap praktik terbaik.

### Penggunaan
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### Apa yang Diperiksa
- ✅ Validitas sintaks Python
- ✅ Impor yang diperlukan ada
- ✅ Implementasi penanganan error (mode verbose)
- ✅ Penggunaan type hints (mode verbose)
- ✅ Docstring fungsi (mode verbose)
- ✅ Tautan referensi SDK (mode verbose)

### Variabel Lingkungan
- `SKIP_IMPORT_CHECK=1` - Lewati validasi impor
- `SKIP_SYNTAX_CHECK=1` - Lewati validasi sintaks

### Kode Keluar
- `0` - Semua contoh lolos validasi
- `1` - Satu atau lebih contoh gagal

## 3. Penguji Contoh

`test_samples.py` menjalankan uji coba pada semua contoh untuk memverifikasi bahwa mereka dapat dijalankan tanpa error.

### Penggunaan
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### Prasyarat
- Layanan Foundry Local berjalan: `foundry service start`
- Model dimuat: `foundry model run phi-4-mini`
- Dependensi terinstal: `pip install -r requirements.txt`

### Apa yang Diuji
- ✅ Contoh dapat dijalankan tanpa error runtime
- ✅ Output yang diperlukan dihasilkan
- ✅ Penanganan error yang tepat saat gagal
- ✅ Performa (waktu eksekusi)

### Variabel Lingkungan
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model yang digunakan untuk pengujian
- `TEST_TIMEOUT=30` - Timeout per contoh dalam detik

### Kegagalan yang Diharapkan
Beberapa pengujian mungkin gagal jika dependensi opsional tidak terinstal (misalnya, `ragas`, `sentence-transformers`). Instal dengan:
```bash
pip install sentence-transformers ragas datasets
```

### Kode Keluar
- `0` - Semua pengujian berhasil
- `1` - Satu atau lebih pengujian gagal

## 4. Ekspor Benchmark Markdown

Skrip: `export_benchmark_markdown.py`

Menghasilkan tabel performa yang dapat direproduksi untuk serangkaian model.

### Penggunaan
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Output
| File | Deskripsi |
|------|-----------|
| `benchmark_report.md` | Tabel Markdown (rata-rata, p95, token/detik, token pertama opsional) |
| `benchmark_report.json` | Array metrik mentah untuk perbandingan & riwayat |

### Opsi
| Flag | Deskripsi | Default |
|------|-----------|---------|
| `--models` | Alias model yang dipisahkan koma | (wajib) |
| `--prompt` | Prompt yang digunakan setiap putaran | (wajib) |
| `--rounds` | Putaran per model | 3 |
| `--output` | File output Markdown | `benchmark_report.md` |
| `--json` | File output JSON | `benchmark_report.json` |
| `--fail-on-empty` | Kode keluar non-nol jika semua benchmark gagal | mati |

Variabel lingkungan `BENCH_STREAM=1` menambahkan pengukuran latensi token pertama.

### Catatan
- Menggunakan kembali `workshop_utils` untuk bootstrap model & caching yang konsisten.
- Jika dijalankan dari direktori kerja yang berbeda, skrip mencoba fallback jalur untuk menemukan `workshop_utils`.
- Untuk perbandingan GPU: jalankan sekali, aktifkan akselerasi melalui konfigurasi CLI, jalankan ulang, dan bandingkan JSON.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.