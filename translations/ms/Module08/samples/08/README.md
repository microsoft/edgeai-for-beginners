# Windows 11 Chat Sample - Foundry Local

Aplikasi sembang moden untuk Windows 11 yang mengintegrasikan Microsoft Foundry Local dengan antara muka asli yang menarik. Dibangunkan menggunakan Electron dan mengikuti corak rasmi Microsoft Foundry Local.

## Gambaran Keseluruhan

Contoh ini menunjukkan cara untuk mencipta aplikasi sembang yang sedia untuk pengeluaran, yang memanfaatkan model AI tempatan melalui Foundry Local, memberikan pengguna perbualan AI yang fokus pada privasi tanpa kebergantungan kepada awan.

## Ciri-ciri

### 🎨 **Reka Bentuk Asli Windows 11**
- Integrasi Sistem Reka Bentuk Fluent
- Kesan bahan Mica dan ketelusan
- Sokongan tema asli Windows 11
- Susun atur responsif untuk semua saiz skrin
- Penukaran automatik mod Gelap/Terang

### 🤖 **Integrasi Model AI**
- Integrasi perkhidmatan Foundry Local
- Sokongan pelbagai model dengan pertukaran pantas
- Respons penstriman masa nyata
- Penukaran model tempatan dan awan
- Pemantauan kesihatan model dan status

### 💬 **Pengalaman Sembang**
- Penunjuk menaip masa nyata
- Sejarah mesej yang berterusan
- Eksport perbualan sembang
- Arahan sistem tersuai
- Cabang dan pengurusan perbualan

### ⚡ **Ciri-ciri Prestasi**
- Pemuatan malas dan pengvirtualan
- Rendering dioptimumkan untuk perbualan panjang
- Pra-pemuatan model latar belakang
- Pengurusan memori yang cekap
- Animasi dan peralihan yang lancar

## Seni Bina

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

### Keperluan Sistem
- **OS**: Windows 11 (22H2 atau lebih baru disyorkan)
- **RAM**: Minimum 8GB, 16GB+ disyorkan untuk model yang lebih besar
- **Storan**: Ruang kosong 10GB+ untuk model
- **GPU**: Pilihan tetapi disyorkan untuk inferens yang lebih pantas

### Kebergantungan Perisian
- **Node.js**: v18.0.0 atau lebih baru
- **Foundry Local**: Versi terkini dari Microsoft
- **Git**: Untuk klon dan pembangunan

## Pemasangan

### 1. Pasang Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klon dan Sediakan
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Konfigurasi Persekitaran
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

## Struktur Projek

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

## Penjelasan Ciri Utama

### Integrasi Windows 11

**Sistem Reka Bentuk Fluent**
- Bahan latar belakang Mica
- Kesan ketelusan Acrylic
- Sudut bulat dan jarak moden
- Palet warna asli Windows 11
- Token warna semantik untuk kebolehaksesan

**Ciri Asli Windows**
- Integrasi senarai lompat untuk sembang terkini
- Pemberitahuan Windows untuk mesej baru
- Kemajuan bar tugas untuk operasi model
- Integrasi dulang sistem dengan tindakan pantas
- Sokongan pengesahan Windows Hello

### Pengurusan Model AI

**Model Tempatan**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Sokongan Hibrid Awan/Tempatan**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Ciri Antara Muka Sembang

**Penstriman Masa Nyata**
- Paparan respons token demi token
- Animasi menaip yang lancar
- Permintaan boleh dibatalkan
- Penunjuk menaip dan status

**Pengurusan Perbualan**
- Sejarah sembang yang berterusan
- Eksport/Import perbualan
- Carian dan penapisan mesej
- Cabang perbualan
- Arahan sistem tersuai untuk setiap perbualan

**Kebolehaksesan**
- Navigasi penuh papan kekunci
- Keserasian pembaca skrin
- Sokongan mod kontras tinggi
- Saiz fon yang boleh disesuaikan
- Integrasi input suara

## Contoh Penggunaan

### Integrasi Sembang Asas
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

### Pengurusan Model
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

### Tetapan dan Penyesuaian
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

## Pilihan Konfigurasi

### Tetapan Aplikasi
- **Tema**: Mod Auto, Terang, Gelap
- **Model**: Pemilihan model lalai
- **Prestasi**: Tetapan inferens
- **Privasi**: Polisi pengekalan data
- **Pemberitahuan**: Amaran mesej
- **Pintasan**: Pintasan papan kekunci

### Tetapan Sembang
- **Penstriman**: Aktifkan/nyahaktifkan respons masa nyata
- **Panjang Konteks**: Memori perbualan
- **Suhu**: Kreativiti respons
- **Token Maksimum**: Had panjang respons
- **Arahan Sistem**: Tingkah laku pembantu lalai

### Tetapan Model
- **Muat Turun Automatik**: Kemas kini model automatik
- **Saiz Cache**: Had storan model tempatan
- **Mod Prestasi**: Keutamaan CPU vs GPU
- **Pemeriksaan Kesihatan**: Selang pemantauan

## Pembangunan

### Membina dari Sumber
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

### Penyahpepijatan
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

## Pengoptimuman Prestasi

### Pengurusan Memori
- Pengvirtualan mesej yang cekap
- Pengumpulan sampah automatik
- Pemantauan memori model
- Pembersihan sumber semasa keluar

### Pengoptimuman Rendering
- Penatalan maya untuk perbualan panjang
- Pemuatan malas sejarah mesej
- Kemas kini React/DOM yang dioptimumkan
- Animasi dipercepat GPU

### Pengoptimuman Rangkaian
- Pengumpulan sambungan
- Pengelompokan permintaan
- Logik percubaan semula automatik
- Sokongan mod luar talian

## Pertimbangan Keselamatan

### Privasi Data
- Seni bina tempatan terlebih dahulu
- Tiada penghantaran data awan (mod tempatan)
- Penyimpanan perbualan yang disulitkan
- Pengurusan kelayakan yang selamat

### Keselamatan Aplikasi
- Proses renderer yang diasingkan
- Polisi Keselamatan Kandungan (CSP)
- Tiada pelaksanaan kod jauh
- Komunikasi IPC yang selamat

## Penyelesaian Masalah

### Isu Biasa

**Foundry Local Tidak Bermula**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Kegagalan Memuatkan Model**
- Sahkan ruang cakera yang mencukupi
- Periksa sambungan internet untuk muat turun
- Pastikan pemacu GPU dikemas kini
- Cuba varian model yang berbeza

**Isu Prestasi**
- Pantau sumber sistem
- Laraskan tetapan model
- Aktifkan pecutan perkakasan
- Tutup aplikasi lain yang menggunakan sumber intensif

### Mod Debug
Aktifkan log debug dengan menetapkan pembolehubah persekitaran:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Menyumbang

### Persediaan Pembangunan
1. Fork repositori
2. Cipta cabang ciri
3. Pasang kebergantungan: `npm install`
4. Lakukan perubahan dan uji
5. Hantar permintaan tarik

### Gaya Kod
- Konfigurasi ESLint disediakan
- Prettier untuk pemformatan kod
- TypeScript untuk keselamatan jenis
- Komen JSDoc untuk dokumentasi

## Hasil Pembelajaran

Selepas melengkapkan contoh ini, anda akan memahami:

1. **Pembangunan Asli Windows 11**
   - Pelaksanaan Sistem Reka Bentuk Fluent
   - Integrasi asli Windows
   - Amalan terbaik keselamatan Electron

2. **Integrasi Model AI**
   - Seni bina perkhidmatan Foundry Local
   - Pengurusan kitaran hayat model
   - Pemantauan dan pengoptimuman prestasi

3. **Sistem Sembang Masa Nyata**
   - Pengendalian respons penstriman
   - Pengurusan keadaan perbualan
   - Corak pengalaman pengguna

4. **Pembangunan Aplikasi Pengeluaran**
   - Pengendalian ralat dan pemulihan
   - Pengoptimuman prestasi
   - Pertimbangan keselamatan
   - Strategi pengujian

## Langkah Seterusnya

- **Contoh 09**: Sistem Orkestrasi Multi-Ejen
- **Contoh 10**: Foundry Local sebagai Integrasi Alat
- **Topik Lanjutan**: Penalaan model tersuai
- **Penghantaran**: Corak penghantaran perusahaan

## Lesen

Contoh ini mengikuti lesen yang sama seperti projek Microsoft Foundry Local.

---

