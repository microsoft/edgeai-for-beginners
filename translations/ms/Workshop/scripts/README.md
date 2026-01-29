# Skrip Bengkel

Direktori ini mengandungi skrip automasi dan sokongan yang digunakan untuk mengekalkan kualiti dan konsistensi bahan Bengkel.

## Kandungan

| Fail | Tujuan |
|------|---------|
| `lint_markdown_cli.py` | Memeriksa blok kod markdown untuk corak arahan Foundry Local CLI yang telah usang. |
| `export_benchmark_markdown.py` | Menjalankan penanda aras kependaman pelbagai model dan menghasilkan laporan dalam format Markdown + JSON. |

## 1. Pemeriksa Corak Markdown CLI

`lint_markdown_cli.py` mengimbas semua fail `.md` bukan terjemahan untuk corak Foundry Local CLI yang tidak dibenarkan **di dalam blok kod berpagar** (``` ... ```). Prosa maklumat masih boleh menyebut arahan yang telah usang untuk konteks sejarah.

### Corak Usang (Disekat Dalam Blok Kod)

Pemeriksa ini menyekat corak CLI yang telah usang. Gunakan alternatif yang lebih moden.

### Penggantian Diperlukan
| Usang | Gunakan Sebaliknya |
|-------|--------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Skrip penanda aras + alat sistem (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Kod Keluar
| Kod | Maksud |
|-----|--------|
| 0 | Tiada pelanggaran dikesan |
| 1 | Satu atau lebih corak usang ditemui |

### Menjalankan Secara Tempatan
Dari akar repositori (disarankan):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Cangkuk Pra-Komitan (Pilihan)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Ini menyekat komitmen yang memperkenalkan corak usang.

### Integrasi CI
Aliran kerja GitHub Action (`.github/workflows/markdown-cli-lint.yml`) menjalankan pemeriksa pada setiap push dan permintaan tarik ke cabang `main` dan `Reactor`. Tugas yang gagal mesti diperbaiki sebelum digabungkan.

### Menambah Corak Usang Baru
1. Buka `lint_markdown_cli.py`.
2. Tambahkan tuple `(regex, suggestion)` ke senarai `DEPRECATED`. Gunakan string mentah dan sertakan sempadan perkataan `\b` jika sesuai.
3. Jalankan pemeriksa secara tempatan untuk mengesahkan pengesanan.
4. Komit dan push; CI akan menguatkuasakan peraturan baru.

Contoh penambahan:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Membenarkan Sebutan Penjelasan
Oleh kerana hanya blok kod berpagar yang dikuatkuasakan, anda boleh menerangkan arahan yang telah usang dalam teks naratif dengan selamat. Jika anda *perlu* menunjukkannya di dalam blok berpagar untuk perbandingan, tambahkan blok berpagar **tanpa** tanda backtick tiga (contohnya, indentasi atau petikan) atau tulis semula dalam bentuk pseudo.

### Melangkau Fail Tertentu (Lanjutan)
Jika diperlukan, bungkus contoh warisan dalam fail berasingan di luar repositori atau tukar nama dengan sambungan yang berbeza semasa draf. Langkauan yang disengajakan untuk salinan terjemahan adalah automatik (laluan yang mengandungi `translations`).

### Penyelesaian Masalah
| Isu | Punca | Penyelesaian |
|-----|-------|--------------|
| Pemeriksa menandakan baris yang anda kemas kini | Regex terlalu luas | Persempit corak dengan sempadan perkataan tambahan (`\b`) atau penanda |
| CI gagal tetapi lulus secara tempatan | Versi Python berbeza atau perubahan tidak dikomit | Jalankan semula secara tempatan, pastikan pokok kerja bersih, periksa versi Python aliran kerja (3.11) |
| Perlu memintas sementara | Pembetulan kecemasan | Lakukan pembetulan segera selepas itu; pertimbangkan menggunakan cabang sementara dan PR susulan (elakkan menambah suis pintasan) |

### Rasional
Menjaga dokumentasi sejajar dengan permukaan CLI stabil *semasa* mengelakkan geseran bengkel, mengelakkan kekeliruan peserta, dan memusatkan pengukuran prestasi melalui skrip Python yang dikekalkan daripada subkomando CLI yang berubah-ubah.

---
Diselenggara sebagai sebahagian daripada alat kualiti bengkel. Untuk penambahbaikan (contohnya, cadangan pembetulan automatik atau penjanaan laporan HTML), buka isu atau serahkan PR.

## 2. Skrip Pengesahan Contoh

`validate_samples.py` mengesahkan semua fail contoh Python untuk kesahihan sintaks, import, dan pematuhan amalan terbaik.

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

### Apa yang diperiksa
- ✅ Kesahihan sintaks Python
- ✅ Import yang diperlukan ada
- ✅ Pelaksanaan pengendalian ralat (mod verbose)
- ✅ Penggunaan petunjuk jenis (mod verbose)
- ✅ Docstring fungsi (mod verbose)
- ✅ Pautan rujukan SDK (mod verbose)

### Pembolehubah Persekitaran
- `SKIP_IMPORT_CHECK=1` - Langkau pengesahan import
- `SKIP_SYNTAX_CHECK=1` - Langkau pengesahan sintaks

### Kod Keluar
- `0` - Semua contoh lulus pengesahan
- `1` - Satu atau lebih contoh gagal

## 3. Pelari Ujian Contoh

`test_samples.py` menjalankan ujian pantas pada semua contoh untuk mengesahkan ia dapat dijalankan tanpa ralat.

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
- Perkhidmatan Foundry Local berjalan: `foundry service start`
- Model dimuatkan: `foundry model run phi-4-mini`
- Kebergantungan dipasang: `pip install -r requirements.txt`

### Apa yang diuji
- ✅ Contoh dapat dijalankan tanpa ralat masa jalan
- ✅ Output yang diperlukan dihasilkan
- ✅ Pengendalian ralat yang betul semasa kegagalan
- ✅ Prestasi (masa pelaksanaan)

### Pembolehubah Persekitaran
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model yang digunakan untuk ujian
- `TEST_TIMEOUT=30` - Had masa setiap contoh dalam saat

### Kegagalan Dijangka
Beberapa ujian mungkin gagal jika kebergantungan pilihan tidak dipasang (contohnya, `ragas`, `sentence-transformers`). Pasang dengan:
```bash
pip install sentence-transformers ragas datasets
```

### Kod Keluar
- `0` - Semua ujian lulus
- `1` - Satu atau lebih ujian gagal

## 4. Penjana Eksport Markdown Penanda Aras

Skrip: `export_benchmark_markdown.py`

Menjana jadual prestasi yang boleh diulang untuk satu set model.

### Penggunaan
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Output
| Fail | Penerangan |
|------|------------|
| `benchmark_report.md` | Jadual Markdown (avg, p95, tokens/sec, token pertama pilihan) |
| `benchmark_report.json` | Array metrik mentah untuk perbezaan & sejarah |

### Pilihan
| Bendera | Penerangan | Lalai |
|---------|------------|-------|
| `--models` | Alias model yang dipisahkan dengan koma | (diperlukan) |
| `--prompt` | Prompt yang digunakan setiap pusingan | (diperlukan) |
| `--rounds` | Pusingan setiap model | 3 |
| `--output` | Fail output Markdown | `benchmark_report.md` |
| `--json` | Fail output JSON | `benchmark_report.json` |
| `--fail-on-empty` | Keluar bukan sifar jika semua penanda aras gagal | mati |

Pembolehubah persekitaran `BENCH_STREAM=1` menambah pengukuran kependaman token pertama.

### Nota
- Menggunakan semula `workshop_utils` untuk bootstrap model & caching yang konsisten.
- Jika dijalankan dari direktori kerja yang berbeza, skrip cuba laluan sandaran untuk mencari `workshop_utils`.
- Untuk perbandingan GPU: jalankan sekali, aktifkan pecutan melalui konfigurasi CLI, jalankan semula dan bandingkan JSON.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.