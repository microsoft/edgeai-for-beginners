# Panduan Integrasi Open WebUI + Foundry Local

Panduan ini menjelaskan cara menghubungkan Open WebUI ke Microsoft Foundry Local untuk mendapatkan antarmuka profesional seperti ChatGPT yang didukung oleh model AI lokal Anda.

## Gambaran Umum

Open WebUI menyediakan antarmuka chat modern yang ramah pengguna dan dapat terhubung ke API yang kompatibel dengan OpenAI. Dengan menghubungkannya ke Foundry Local, Anda mendapatkan:

- **UI Profesional**: Antarmuka seperti ChatGPT dengan desain modern
- **Privasi Lokal**: Semua pemrosesan dilakukan di perangkat Anda
- **Pergantian Model**: Mudah beralih antara berbagai model lokal
- **Riwayat Percakapan**: Riwayat chat dan konteks yang tersimpan
- **Unggah File**: Analisis dokumen dan kemampuan pemrosesan file
- **Persona Kustom**: Prompt sistem dan kustomisasi peran

## Prasyarat

### Perangkat Lunak yang Dibutuhkan

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Memuat Model

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Pengaturan Cepat (Direkomendasikan)

### Langkah 1: Jalankan Open WebUI dengan Docker

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### Langkah 2: Pengaturan Awal

1. **Buka Browser**: Akses `http://localhost:3000`
2. **Buat Akun**: Atur pengguna admin (pengguna pertama menjadi admin)
3. **Verifikasi Koneksi**: Model akan muncul secara otomatis di dropdown

### Langkah 3: Uji Koneksi

1. Pilih model Anda dari dropdown (misalnya, "phi-4-mini")
2. Ketik pesan uji: "Halo! Bisakah Anda memperkenalkan diri?"
3. Anda akan melihat respons streaming dari model lokal Anda

## Konfigurasi Lanjutan

### Variabel Lingkungan

| Variabel | Tujuan | Default | Contoh |
|----------|--------|---------|--------|
| `OPENAI_API_BASE_URL` | Endpoint Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API key (dibutuhkan tetapi tidak digunakan secara lokal) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Kunci enkripsi sesi | auto-generated | `your-secret-key` |
| `ENABLE_SIGNUP` | Mengizinkan pendaftaran pengguna baru | `True` | `False` |

### Konfigurasi Manual (Alternatif)

Jika variabel lingkungan tidak berfungsi, konfigurasikan secara manual:

1. **Buka Pengaturan**: Klik Pengaturan (ikon gear)
2. **Navigasi ke Koneksi**: Pengaturan → Koneksi → OpenAI
3. **Atur Detail API**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (nilai apa pun dapat digunakan)
4. **Simpan dan Uji**: Klik "Simpan" lalu uji dengan model

### Penyimpanan Data Persisten

Untuk menyimpan percakapan dan pengaturan:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Pemecahan Masalah

### Masalah Koneksi

**Masalah**: "Connection refused" atau model tidak muncul

**Solusi**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### Model Tidak Muncul

**Masalah**: Open WebUI tidak menunjukkan model di dropdown

**Langkah Debugging**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Perbaikan**: Pastikan model telah dimuat dengan benar:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Masalah Jaringan Docker

**Masalah**: `host.docker.internal` tidak dapat diakses

**Solusi Windows**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**Alternatif**: Temukan IP mesin Anda:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Masalah Performa

**Respons Lambat**:
1. Periksa apakah model menggunakan akselerasi GPU: `foundry service ps`
2. Pastikan sumber daya sistem cukup (RAM/memori GPU)
3. Pertimbangkan menggunakan model yang lebih kecil untuk pengujian

**Masalah Memori**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Panduan Penggunaan

### Chat Dasar

1. **Pilih Model**: Pilih dari dropdown (menampilkan model Foundry Local)
2. **Ketik Pesan**: Gunakan input teks di bagian bawah
3. **Kirim**: Tekan Enter atau klik tombol Kirim
4. **Lihat Respons**: Lihat respons streaming secara real-time

### Fitur Lanjutan

**Unggah File**:
1. Klik ikon penjepit kertas
2. Unggah dokumen (PDF, TXT, dll.)
3. Ajukan pertanyaan tentang konten
4. Model akan menganalisis dan merespons berdasarkan dokumen

**Prompt Sistem Kustom**:
1. Pengaturan → Personalisasi
2. Atur prompt sistem kustom
3. Membuat kepribadian/perilaku AI yang konsisten

**Manajemen Percakapan**:
- **Chat Baru**: Klik "+" untuk memulai percakapan baru
- **Riwayat Chat**: Akses percakapan sebelumnya dari sidebar
- **Ekspor**: Unduh riwayat chat sebagai teks/JSON

**Perbandingan Model**:
1. Buka beberapa tab browser ke Open WebUI yang sama
2. Pilih model berbeda di setiap tab
3. Bandingkan respons terhadap prompt yang sama

### Pola Integrasi

**Alur Kerja Pengembangan**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Penerapan Produksi

### Pengaturan Aman

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Pengaturan Multi-Pengguna

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Pemantauan dan Logging

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Pembersihan

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## Langkah Berikutnya

### Ide Peningkatan

1. **Model Kustom**: Tambahkan model yang telah Anda fine-tune ke Foundry Local
2. **Integrasi API**: Hubungkan ke API eksternal melalui fungsi Open WebUI
3. **Pemrosesan Dokumen**: Atur pipeline RAG yang canggih
4. **Multi-Modal**: Konfigurasikan model visi untuk analisis gambar

### Pertimbangan Skalabilitas

- **Load Balancing**: Beberapa instance Foundry Local di belakang reverse proxy
- **Routing Model**: Model berbeda untuk kasus penggunaan yang berbeda
- **Manajemen Sumber Daya**: Optimasi memori GPU untuk pengguna bersamaan
- **Strategi Backup**: Backup reguler data percakapan dan konfigurasi

## Referensi

- [Dokumentasi Open WebUI](https://docs.openwebui.com/)
- [Repositori GitHub Open WebUI](https://github.com/open-webui/open-webui)
- [Dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Panduan Instalasi Docker](https://docs.docker.com/get-docker/)

---

