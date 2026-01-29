# Windows 11 Chat Sample - Foundry Local

Aplikasi chat modern untuk Windows 11 yang mengintegrasikan Microsoft Foundry Local dengan antarmuka asli yang indah. Dibangun menggunakan Electron dan mengikuti pola resmi Foundry Local dari Microsoft.

## Gambaran Umum

Contoh ini menunjukkan cara membuat aplikasi chat siap produksi yang memanfaatkan model AI lokal melalui Foundry Local, memberikan pengguna percakapan AI yang berfokus pada privasi tanpa ketergantungan pada cloud.

## Fitur

### 🎨 **Desain Asli Windows 11**
- Integrasi Fluent Design System
- Efek material Mica dan transparansi
- Dukungan tema asli Windows 11
- Tata letak responsif untuk semua ukuran layar
- Pergantian mode Gelap/Terang secara otomatis

### 🤖 **Integrasi Model AI**
- Integrasi layanan Foundry Local
- Dukungan beberapa model dengan pergantian cepat
- Respons streaming secara real-time
- Pergantian model lokal dan cloud
- Pemantauan kesehatan model dan status

### 💬 **Pengalaman Chat**
- Indikator mengetik secara real-time
- Penyimpanan riwayat pesan
- Ekspor percakapan chat
- Prompt sistem yang dapat disesuaikan
- Cabang percakapan dan pengelolaan

### ⚡ **Fitur Performa**
- Pemuatan lambat dan virtualisasi
- Rendering yang dioptimalkan untuk percakapan panjang
- Pemuatan model di latar belakang
- Manajemen memori yang efisien
- Animasi dan transisi yang mulus

## Arsitektur

```
┌─────────────────────────────────────────────────────────────┐
│                    Windows 11 Chat App                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Electron UI   │   IPC Bridge    │    Foundry Manager      │
│                 │                 │                         │
│ • Fluent Design │ • Secure Comms  │ • Model Loading         │
│ • Chat Interface│ • Event Routing │ • Health Monitoring     │
│ • Settings      │ • State Sync    │ • Performance Tracking │
│ • Themes        │ • Error Handler │ • Resource Management   │
└─────────────────┴─────────────────┴─────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               Microsoft Foundry Local Service               │
│                                                             │
│ • Local Model Hosting    • OpenAI API Compatibility        │
│ • Real-time Inference    • Model Catalog Management        │
│ • Streaming Responses    • Health & Status Monitoring      │
└─────────────────────────────────────────────────────────────┘
```

## Prasyarat

### Persyaratan Sistem
- **OS**: Windows 11 (22H2 atau lebih baru disarankan)
- **RAM**: Minimal 8GB, 16GB+ disarankan untuk model yang lebih besar
- **Penyimpanan**: Ruang kosong 10GB+ untuk model
- **GPU**: Opsional tetapi disarankan untuk inferensi yang lebih cepat

### Ketergantungan Perangkat Lunak
- **Node.js**: v18.0.0 atau lebih baru
- **Foundry Local**: Versi terbaru dari Microsoft
- **Git**: Untuk cloning dan pengembangan

## Instalasi

### 1. Instal Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Clone dan Setup
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigurasi Lingkungan
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Jalankan Aplikasi
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Struktur Proyek

```
08/
├── README.md                 # This documentation
├── package.json             # Project dependencies and scripts
├── electron.js              # Main Electron process
├── preload.js              # Secure preload script
├── src/
│   ├── index.html          # Main application UI
│   ├── styles/
│   │   ├── fluent.css      # Windows 11 Fluent Design
│   │   ├── chat.css        # Chat interface styles
│   │   └── themes.css      # Light/Dark theme support
│   ├── scripts/
│   │   ├── app.js          # Main application logic
│   │   ├── chat.js         # Chat functionality
│   │   ├── models.js       # Model management
│   │   ├── settings.js     # Settings and preferences
│   │   └── utils.js        # Utility functions
│   └── assets/
│       ├── icons/          # Application icons
│       ├── sounds/         # Notification sounds
│       └── images/         # UI images and illustrations
├── foundry/
│   ├── manager.js          # Foundry Local integration
│   └── health.js           # Health monitoring
└── build/
    ├── icon.ico            # Windows application icon
    └── installer.nsi       # NSIS installer script
```

## Penjelasan Mendalam Fitur Utama

### Integrasi Windows 11

**Fluent Design System**
- Material latar belakang Mica
- Efek transparansi Acrylic
- Sudut membulat dan jarak modern
- Palet warna asli Windows 11
- Token warna semantik untuk aksesibilitas

**Fitur Asli Windows**
- Integrasi daftar lompatan untuk chat terbaru
- Notifikasi Windows untuk pesan baru
- Kemajuan taskbar untuk operasi model
- Integrasi tray sistem dengan tindakan cepat
- Dukungan autentikasi Windows Hello

### Pengelolaan Model AI

**Model Lokal**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Dukungan Hybrid Cloud/Lokal**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Fitur Antarmuka Chat

**Streaming Real-time**
- Tampilan respons token demi token
- Animasi mengetik yang mulus
- Permintaan yang dapat dibatalkan
- Indikator mengetik dan status

**Pengelolaan Percakapan**
- Riwayat chat yang persisten
- Ekspor/impor percakapan
- Pencarian dan penyaringan pesan
- Cabang percakapan
- Prompt sistem yang dapat disesuaikan per percakapan

**Aksesibilitas**
- Navigasi penuh dengan keyboard
- Kompatibilitas pembaca layar
- Dukungan mode kontras tinggi
- Ukuran font yang dapat disesuaikan
- Integrasi input suara

## Contoh Penggunaan

### Integrasi Chat Dasar
```javascript
// Initialize the chat system
const chat = new ChatManager({
    foundryEndpoint: 'http://localhost:5273',
    defaultModel: 'phi-4-mini',
    streaming: true
});

// Send a message
const response = await chat.sendMessage({
    content: 'Explain quantum computing',
    model: 'phi-4-mini',
    systemPrompt: 'You are a helpful physics teacher.'
});

// Handle streaming responses
chat.on('chunk', (chunk) => {
    appendMessageChunk(chunk.content);
});
```

### Pengelolaan Model
```javascript
// Load a new model
await modelManager.loadModel('qwen2.5-coder-0.5b', {
    showProgress: true,
    autoStart: true
});

// Monitor model performance
modelManager.on('performance', (metrics) => {
    updatePerformanceUI(metrics);
});

// Switch models mid-conversation
await chat.switchModel('phi-4-mini', {
    preserveContext: true
});
```

### Pengaturan dan Kustomisasi
```javascript
// Configure chat behavior
const settings = {
    theme: 'system', // auto, light, dark
    model: 'phi-4-mini',
    streaming: true,
    maxTokens: 1000,
    temperature: 0.7,
    systemPrompt: 'You are a helpful assistant.'
};

await settingsManager.updateSettings(settings);
```

## Opsi Konfigurasi

### Pengaturan Aplikasi
- **Tema**: Mode Otomatis, Terang, Gelap
- **Model**: Pemilihan model default
- **Performa**: Pengaturan inferensi
- **Privasi**: Kebijakan retensi data
- **Notifikasi**: Peringatan pesan
- **Shortcut**: Pintasan keyboard

### Pengaturan Chat
- **Streaming**: Aktif/nonaktifkan respons real-time
- **Panjang Konteks**: Memori percakapan
- **Temperatur**: Kreativitas respons
- **Maksimal Token**: Batas panjang respons
- **Prompt Sistem**: Perilaku asisten default

### Pengaturan Model
- **Unduhan Otomatis**: Pembaruan model otomatis
- **Ukuran Cache**: Batas penyimpanan model lokal
- **Mode Performa**: Preferensi CPU vs GPU
- **Pemeriksaan Kesehatan**: Interval pemantauan

## Pengembangan

### Membangun dari Sumber
```bash
# Install development dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Debugging
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Pengujian
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Optimasi Performa

### Manajemen Memori
- Virtualisasi pesan yang efisien
- Pengumpulan sampah otomatis
- Pemantauan memori model
- Pembersihan sumber daya saat keluar

### Optimasi Rendering
- Pengguliran virtual untuk percakapan panjang
- Pemuatan lambat riwayat pesan
- Pembaruan React/DOM yang dioptimalkan
- Animasi yang dipercepat GPU

### Optimasi Jaringan
- Pooling koneksi
- Pengelompokan permintaan
- Logika pengulangan otomatis
- Dukungan mode offline

## Pertimbangan Keamanan

### Privasi Data
- Arsitektur lokal-pertama
- Tidak ada transmisi data cloud (mode lokal)
- Penyimpanan percakapan terenkripsi
- Manajemen kredensial yang aman

### Keamanan Aplikasi
- Proses renderer yang terisolasi
- Kebijakan Keamanan Konten (CSP)
- Tidak ada eksekusi kode jarak jauh
- Komunikasi IPC yang aman

## Pemecahan Masalah

### Masalah Umum

**Foundry Local Tidak Berjalan**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Kegagalan Memuat Model**
- Verifikasi ruang disk yang cukup
- Periksa koneksi internet untuk unduhan
- Pastikan driver GPU diperbarui
- Coba varian model yang berbeda

**Masalah Performa**
- Pantau sumber daya sistem
- Sesuaikan pengaturan model
- Aktifkan akselerasi perangkat keras
- Tutup aplikasi lain yang memakan banyak sumber daya

### Mode Debug
Aktifkan logging debug dengan mengatur variabel lingkungan:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Kontribusi

### Pengaturan Pengembangan
1. Fork repositori
2. Buat cabang fitur
3. Instal ketergantungan: `npm install`
4. Lakukan perubahan dan uji
5. Kirimkan pull request

### Gaya Kode
- Konfigurasi ESLint disediakan
- Prettier untuk format kode
- TypeScript untuk keamanan tipe
- Komentar JSDoc untuk dokumentasi

## Hasil Pembelajaran

Setelah menyelesaikan contoh ini, Anda akan memahami:

1. **Pengembangan Asli Windows 11**
   - Implementasi Fluent Design System
   - Integrasi asli Windows
   - Praktik terbaik keamanan Electron

2. **Integrasi Model AI**
   - Arsitektur layanan Foundry Local
   - Pengelolaan siklus hidup model
   - Pemantauan dan optimasi performa

3. **Sistem Chat Real-time**
   - Penanganan respons streaming
   - Pengelolaan status percakapan
   - Pola pengalaman pengguna

4. **Pengembangan Aplikasi Produksi**
   - Penanganan kesalahan dan pemulihan
   - Optimasi performa
   - Pertimbangan keamanan
   - Strategi pengujian

## Langkah Selanjutnya

- **Contoh 09**: Sistem Orkestrasi Multi-Agent
- **Contoh 10**: Foundry Local sebagai Integrasi Alat
- **Topik Lanjutan**: Fine-tuning model khusus
- **Penerapan**: Pola penerapan untuk perusahaan

## Lisensi

Contoh ini mengikuti lisensi yang sama dengan proyek Microsoft Foundry Local.

---

