# Panduan Integrasi Open WebUI + Foundry Local

Panduan ini menunjukkan cara menghubungkan Open WebUI ke Microsoft Foundry Local untuk mendapatkan antara muka profesional seperti ChatGPT yang dikuasakan oleh model AI tempatan anda.

## Gambaran Keseluruhan

Open WebUI menyediakan antara muka chat yang moden dan mesra pengguna yang boleh disambungkan ke mana-mana API yang serasi dengan OpenAI. Dengan menghubungkannya ke Foundry Local, anda akan mendapat:

- **UI Profesional**: Antara muka seperti ChatGPT dengan reka bentuk moden
- **Privasi Tempatan**: Semua pemprosesan berlaku pada peranti anda
- **Pertukaran Model**: Mudah bertukar antara model tempatan yang berbeza
- **Sejarah Perbualan**: Sejarah chat dan konteks yang berterusan
- **Muat Naik Fail**: Analisis dokumen dan keupayaan pemprosesan fail
- **Persona Tersuai**: Prompt sistem dan penyesuaian peranan

## Prasyarat

### Perisian Diperlukan

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Muatkan Model

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Persediaan Cepat (Disyorkan)

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

### Langkah 2: Persediaan Awal

1. **Buka Pelayar**: Navigasi ke `http://localhost:3000`
2. **Buat Akaun**: Tetapkan pengguna admin (pengguna pertama menjadi admin)
3. **Sahkan Sambungan**: Model sepatutnya muncul secara automatik dalam dropdown

### Langkah 3: Uji Sambungan

1. Pilih model anda dari dropdown (contohnya, "phi-4-mini")
2. Taip mesej ujian: "Hello! Can you introduce yourself?"
3. Anda sepatutnya melihat respons streaming daripada model tempatan anda

## Konfigurasi Lanjutan

### Pembolehubah Persekitaran

| Pembolehubah | Tujuan | Lalai | Contoh |
|--------------|--------|-------|--------|
| `OPENAI_API_BASE_URL` | Endpoint Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | Kunci API (diperlukan tetapi tidak digunakan secara tempatan) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Kunci penyulitan sesi | auto-generated | `your-secret-key` |
| `ENABLE_SIGNUP` | Benarkan pendaftaran pengguna baru | `True` | `False` |

### Konfigurasi Manual (Alternatif)

Jika pembolehubah persekitaran tidak berfungsi, konfigurasikan secara manual:

1. **Buka Tetapan**: Klik Tetapan (ikon gear)
2. **Navigasi ke Sambungan**: Tetapan → Sambungan → OpenAI
3. **Tetapkan Butiran API**:
   - URL Asas API: `http://host.docker.internal:51211/v1`
   - Kunci API: `foundry-local-key` (sebarang nilai berfungsi)
4. **Simpan dan Uji**: Klik "Simpan" kemudian uji dengan model

### Penyimpanan Data Berterusan

Untuk mengekalkan perbualan dan tetapan:

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

## Penyelesaian Masalah

### Masalah Sambungan

**Masalah**: "Connection refused" atau model tidak dimuatkan

**Penyelesaian**:
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

**Masalah**: Open WebUI tidak menunjukkan model dalam dropdown

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

**Penyelesaian**: Pastikan model dimuatkan dengan betul:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Masalah Rangkaian Docker

**Masalah**: `host.docker.internal` tidak dapat diselesaikan

**Penyelesaian Windows**:
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

**Alternatif**: Cari IP mesin anda:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Masalah Prestasi

**Respons Perlahan**:
1. Periksa model menggunakan pecutan GPU: `foundry service ps`
2. Sahkan sumber sistem mencukupi (RAM/memori GPU)
3. Pertimbangkan menggunakan model yang lebih kecil untuk ujian

**Masalah Memori**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Panduan Penggunaan

### Chat Asas

1. **Pilih Model**: Pilih dari dropdown (menunjukkan model Foundry Local)
2. **Taip Mesej**: Gunakan input teks di bahagian bawah
3. **Hantar**: Tekan Enter atau klik butang Hantar
4. **Lihat Respons**: Lihat respons streaming secara langsung

### Ciri Lanjutan

**Muat Naik Fail**:
1. Klik ikon klip kertas
2. Muat naik dokumen (PDF, TXT, dll.)
3. Tanya soalan tentang kandungan
4. Model akan menganalisis dan memberi respons berdasarkan dokumen

**Prompt Sistem Tersuai**:
1. Tetapan → Personalisasi
2. Tetapkan prompt sistem tersuai
3. Mewujudkan personaliti/tingkah laku AI yang konsisten

**Pengurusan Perbualan**:
- **Chat Baru**: Klik "+" untuk memulakan perbualan baru
- **Sejarah Chat**: Akses perbualan sebelumnya dari bar sisi
- **Eksport**: Muat turun sejarah chat sebagai teks/JSON

**Perbandingan Model**:
1. Buka beberapa tab pelayar ke Open WebUI yang sama
2. Pilih model yang berbeza dalam setiap tab
3. Bandingkan respons kepada prompt yang sama

### Corak Integrasi

**Aliran Kerja Pembangunan**:
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

## Penggunaan di Produksi

### Persediaan Selamat

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

### Persediaan Multi-Pengguna

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

### Pemantauan dan Log

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

## Langkah Seterusnya

### Idea Penambahbaikan

1. **Model Tersuai**: Tambahkan model yang telah dihaluskan ke Foundry Local
2. **Integrasi API**: Sambungkan ke API luaran melalui fungsi Open WebUI
3. **Pemprosesan Dokumen**: Tetapkan pipeline RAG yang canggih
4. **Multi-Modal**: Konfigurasikan model penglihatan untuk analisis imej

### Pertimbangan Skalabiliti

- **Pengimbangan Beban**: Beberapa instance Foundry Local di belakang proxy terbalik
- **Penghalaan Model**: Model yang berbeza untuk kegunaan yang berbeza
- **Pengurusan Sumber**: Pengoptimuman memori GPU untuk pengguna serentak
- **Strategi Sandaran**: Sandaran berkala data perbualan dan konfigurasi

## Rujukan

- [Dokumentasi Open WebUI](https://docs.openwebui.com/)
- [Repositori GitHub Open WebUI](https://github.com/open-webui/open-webui)
- [Dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Panduan Pemasangan Docker](https://docs.docker.com/get-docker/)

---

