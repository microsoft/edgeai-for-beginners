# Windows 11 Sohbet Örneği - Foundry Local

Windows 11 için modern bir sohbet uygulaması; Microsoft Foundry Local ile entegre edilmiş, şık ve doğal bir arayüze sahip. Electron ile geliştirilmiş ve Microsoft'un resmi Foundry Local tasarım kalıplarını takip ediyor.

## Genel Bakış

Bu örnek, Foundry Local üzerinden yerel yapay zeka modellerini kullanarak bulut bağımlılığı olmadan, gizlilik odaklı yapay zeka sohbetleri sunan üretime hazır bir sohbet uygulamasının nasıl oluşturulacağını gösterir.

## Özellikler

### 🎨 **Windows 11 Doğal Tasarım**
- Fluent Design System entegrasyonu
- Mica materyal efektleri ve şeffaflık
- Windows 11 doğal tema desteği
- Tüm ekran boyutları için duyarlı tasarım
- Karanlık/Aydınlık mod otomatik geçişi

### 🤖 **Yapay Zeka Model Entegrasyonu**
- Foundry Local hizmet entegrasyonu
- Birden fazla model desteği ve hızlı geçiş
- Gerçek zamanlı akış yanıtları
- Yerel ve bulut modeli geçişi
- Model sağlık durumu izleme ve raporlama

### 💬 **Sohbet Deneyimi**
- Gerçek zamanlı yazma göstergeleri
- Mesaj geçmişi kalıcılığı
- Sohbet konuşmalarını dışa aktarma
- Özel sistem komutları
- Konuşma dallanması ve yönetimi

### ⚡ **Performans Özellikleri**
- Lazy loading ve sanallaştırma
- Uzun konuşmalar için optimize edilmiş render
- Arka planda model ön yükleme
- Verimli bellek yönetimi
- Akıcı animasyonlar ve geçişler

## Mimari

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

## Ön Koşullar

### Sistem Gereksinimleri
- **İşletim Sistemi**: Windows 11 (22H2 veya daha yeni önerilir)
- **RAM**: Minimum 8GB, daha büyük modeller için 16GB+ önerilir
- **Depolama**: Modeller için 10GB+ boş alan
- **GPU**: Opsiyonel, ancak daha hızlı çıkarım için önerilir

### Yazılım Bağımlılıkları
- **Node.js**: v18.0.0 veya daha yeni
- **Foundry Local**: Microsoft'tan en son sürüm
- **Git**: Klonlama ve geliştirme için

## Kurulum

### 1. Foundry Local'ı Yükleyin
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Klonlama ve Kurulum
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Ortamı Yapılandırma
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Uygulamayı Çalıştırma
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Proje Yapısı

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

## Öne Çıkan Özelliklerin Detayları

### Windows 11 Entegrasyonu

**Fluent Design System**
- Mica arka plan materyalleri
- Akrilik şeffaflık efektleri
- Yuvarlatılmış köşeler ve modern boşluklar
- Windows 11 doğal renk paleti
- Erişilebilirlik için semantik renk belirteçleri

**Doğal Windows Özellikleri**
- Son sohbetler için Jump list entegrasyonu
- Yeni mesajlar için Windows bildirimleri
- Model işlemleri için görev çubuğu ilerleme göstergesi
- Hızlı işlemler için sistem tepsisi entegrasyonu
- Windows Hello kimlik doğrulama desteği

### Yapay Zeka Model Yönetimi

**Yerel Modeller**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hibrit Bulut/Yerel Destek**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Sohbet Arayüzü Özellikleri

**Gerçek Zamanlı Akış**
- Token bazlı yanıt görüntüleme
- Akıcı yazma animasyonları
- İptal edilebilir istekler
- Yazma göstergeleri ve durum

**Konuşma Yönetimi**
- Kalıcı sohbet geçmişi
- Sohbeti dışa aktarma/içe aktarma
- Mesaj arama ve filtreleme
- Konuşma dallanması
- Her konuşma için özel sistem komutları

**Erişilebilirlik**
- Tam klavye navigasyonu
- Ekran okuyucu uyumluluğu
- Yüksek kontrast modu desteği
- Özelleştirilebilir yazı tipi boyutları
- Sesli giriş entegrasyonu

## Kullanım Örnekleri

### Temel Sohbet Entegrasyonu
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

### Model Yönetimi
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

### Ayarlar ve Özelleştirme
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

## Yapılandırma Seçenekleri

### Uygulama Ayarları
- **Tema**: Otomatik, Aydınlık, Karanlık mod
- **Model**: Varsayılan model seçimi
- **Performans**: Çıkarım ayarları
- **Gizlilik**: Veri saklama politikaları
- **Bildirimler**: Mesaj uyarıları
- **Kısayollar**: Klavye kısayolları

### Sohbet Ayarları
- **Akış**: Gerçek zamanlı yanıtları etkinleştir/devre dışı bırak
- **Bağlam Uzunluğu**: Konuşma hafızası
- **Sıcaklık**: Yanıt yaratıcılığı
- **Maksimum Token**: Yanıt uzunluk sınırları
- **Sistem Komutları**: Varsayılan asistan davranışı

### Model Ayarları
- **Otomatik İndirme**: Otomatik model güncellemeleri
- **Önbellek Boyutu**: Yerel model depolama sınırları
- **Performans Modu**: CPU vs GPU tercihleri
- **Sağlık Kontrolleri**: İzleme aralıkları

## Geliştirme

### Kaynaktan Derleme
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

### Hata Ayıklama
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Test Etme
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Performans Optimizasyonu

### Bellek Yönetimi
- Verimli mesaj sanallaştırma
- Otomatik çöp toplama
- Model bellek izleme
- Çıkışta kaynak temizleme

### Render Optimizasyonu
- Uzun konuşmalar için sanal kaydırma
- Mesaj geçmişinin lazy loading ile yüklenmesi
- Optimize edilmiş React/DOM güncellemeleri
- GPU hızlandırmalı animasyonlar

### Ağ Optimizasyonu
- Bağlantı havuzu
- İstek toplama
- Otomatik yeniden deneme mantığı
- Çevrimdışı mod desteği

## Güvenlik Düşünceleri

### Veri Gizliliği
- Yerel öncelikli mimari
- Bulut veri iletimi yok (yerel mod)
- Şifrelenmiş sohbet depolama
- Güvenli kimlik bilgisi yönetimi

### Uygulama Güvenliği
- Sandboxed renderer süreçleri
- İçerik Güvenlik Politikası (CSP)
- Uzaktan kod yürütme yok
- Güvenli IPC iletişimi

## Sorun Giderme

### Yaygın Sorunlar

**Foundry Local Başlamıyor**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Model Yükleme Hataları**
- Yeterli disk alanını doğrulayın
- İndirmeler için internet bağlantısını kontrol edin
- GPU sürücülerinin güncel olduğundan emin olun
- Farklı model varyantlarını deneyin

**Performans Sorunları**
- Sistem kaynaklarını izleyin
- Model ayarlarını düzenleyin
- Donanım hızlandırmayı etkinleştirin
- Diğer kaynak yoğun uygulamaları kapatın

### Hata Ayıklama Modu
Hata ayıklama günlüklerini etkinleştirmek için ortam değişkenlerini ayarlayın:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Katkıda Bulunma

### Geliştirme Kurulumu
1. Depoyu çatallayın
2. Bir özellik dalı oluşturun
3. Bağımlılıkları yükleyin: `npm install`
4. Değişiklik yapın ve test edin
5. Bir çekme isteği gönderin

### Kod Stili
- ESLint yapılandırması sağlanmıştır
- Kod biçimlendirme için Prettier
- Tür güvenliği için TypeScript
- Belgeler için JSDoc yorumları

## Öğrenim Çıktıları

Bu örneği tamamladıktan sonra şunları anlayacaksınız:

1. **Windows 11 Doğal Geliştirme**
   - Fluent Design System uygulaması
   - Doğal Windows entegrasyonu
   - Electron güvenlik en iyi uygulamaları

2. **Yapay Zeka Model Entegrasyonu**
   - Foundry Local hizmet mimarisi
   - Model yaşam döngüsü yönetimi
   - Performans izleme ve optimizasyon

3. **Gerçek Zamanlı Sohbet Sistemleri**
   - Akış yanıtlarının işlenmesi
   - Konuşma durumu yönetimi
   - Kullanıcı deneyimi kalıpları

4. **Üretim Uygulaması Geliştirme**
   - Hata yönetimi ve kurtarma
   - Performans optimizasyonu
   - Güvenlik düşünceleri
   - Test stratejileri

## Sonraki Adımlar

- **Örnek 09**: Çoklu Ajan Orkestrasyon Sistemi
- **Örnek 10**: Foundry Local ile Araç Entegrasyonu
- **İleri Konular**: Özel model ince ayarı
- **Dağıtım**: Kurumsal dağıtım kalıpları

## Lisans

Bu örnek, Microsoft Foundry Local projesiyle aynı lisansı takip eder.

---

