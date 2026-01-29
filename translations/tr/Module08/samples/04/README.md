# Örnek 04: Chainlit ile Üretim Chat Uygulamaları

Microsoft Foundry Local kullanarak üretime hazır chat uygulamaları oluşturmanın çeşitli yaklaşımlarını gösteren kapsamlı bir örnek. Modern web arayüzleri, akış yanıtları ve en son tarayıcı teknolojilerini içerir.

## İçerikler

- **🚀 Chainlit Chat Uygulaması** (`app.py`): Akış destekli üretime hazır chat uygulaması
- **🌐 WebGPU Demo** (`webgpu-demo/`): Donanım hızlandırmalı tarayıcı tabanlı AI çıkarımı
- **🎨 Open WebUI Entegrasyonu** (`open-webui-guide.md`): Profesyonel ChatGPT benzeri arayüz
- **📚 Eğitim Not Defteri** (`chainlit_app.ipynb`): Etkileşimli öğrenme materyalleri

## Hızlı Başlangıç

### 1. Chainlit Chat Uygulaması

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Açılır: `http://localhost:8080`

### 2. WebGPU Tarayıcı Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Açılır: `http://localhost:5173`

### 3. Open WebUI Kurulumu

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Açılır: `http://localhost:3000`

## Mimari Modeller

### Yerel vs Bulut Karar Matrisi

| Senaryo | Öneri | Sebep |
|---------|-------|-------|
| **Gizlilik Hassas Veriler** | 🏠 Yerel (Foundry) | Veri cihazdan çıkmaz |
| **Karmaşık Akıl Yürütme** | ☁️ Bulut (Azure OpenAI) | Daha büyük modellere erişim |
| **Gerçek Zamanlı Chat** | 🏠 Yerel (Foundry) | Daha düşük gecikme, daha hızlı yanıtlar |
| **Belge Analizi** | 🔄 Hibrit | Çıkarım için yerel, analiz için bulut |
| **Kod Üretimi** | 🏠 Yerel (Foundry) | Gizlilik + özel modeller |
| **Araştırma Görevleri** | ☁️ Bulut (Azure OpenAI) | Geniş bilgi tabanı gerekli |

### Teknoloji Karşılaştırması

| Teknoloji | Kullanım Alanı | Avantajlar | Dezavantajlar |
|-----------|----------------|------------|---------------|
| **Chainlit** | Python geliştiricileri, hızlı prototipleme | Kolay kurulum, akış desteği | Sadece Python |
| **WebGPU** | Maksimum gizlilik, çevrimdışı senaryolar | Tarayıcı yerel, sunucu gerekmez | Sınırlı model boyutu |
| **Open WebUI** | Üretim dağıtımı, ekipler | Profesyonel arayüz, kullanıcı yönetimi | Docker gerektirir |

## Ön Koşullar

- **Foundry Local**: Kurulu ve çalışıyor ([İndir](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ ve sanal ortam
- **Model**: En az bir model yüklü (`foundry model run phi-4-mini`)
- **Tarayıcı**: Chrome/Edge ile WebGPU desteği için
- **Docker**: Open WebUI için (isteğe bağlı)

## Kurulum ve Ayar

### 1. Python Ortamı Kurulumu

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local Ayarı

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Örnek Uygulamalar

### Chainlit Chat Uygulaması

**Özellikler:**
- 🚀 **Gerçek Zamanlı Akış**: Tokenlar oluşturuldukça görünür
- 🛡️ **Güçlü Hata Yönetimi**: Sorunsuz bozulma ve kurtarma
- 🎨 **Modern Arayüz**: Kutudan çıkan profesyonel chat arayüzü
- 🔧 **Esnek Yapılandırma**: Ortam değişkenleri ve otomatik algılama
- 📱 **Duyarlı Tasarım**: Masaüstü ve mobil cihazlarda çalışır

**Hızlı Başlangıç:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### WebGPU Tarayıcı Demo

**Özellikler:**
- 🌐 **Tarayıcı Yerel AI**: Sunucu gerekmez, tamamen tarayıcıda çalışır
- ⚡ **WebGPU Hızlandırma**: Donanım hızlandırması mevcut olduğunda
- 🔒 **Maksimum Gizlilik**: Veri cihazınızdan asla çıkmaz
- 🎯 **Sıfır Kurulum**: Uyumlu herhangi bir tarayıcıda çalışır
- 🔄 **Sorunsuz Geri Dönüş**: WebGPU yoksa CPU'ya geçer

**Çalıştırma:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Entegrasyonu

**Özellikler:**
- 🎨 **ChatGPT Benzeri Arayüz**: Profesyonel, tanıdık arayüz
- 👥 **Çoklu Kullanıcı Desteği**: Kullanıcı hesapları ve sohbet geçmişi
- 📁 **Dosya İşleme**: Belgeleri yükleyip analiz etme
- 🔄 **Model Değiştirme**: Farklı modeller arasında kolay geçiş
- 🐳 **Docker Dağıtımı**: Üretime hazır konteyner kurulumu

**Hızlı Kurulum:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Yapılandırma Referansı

### Ortam Değişkenleri

| Değişken | Açıklama | Varsayılan | Örnek |
|----------|----------|------------|-------|
| `MODEL` | Kullanılacak model takma adı | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local uç noktası | Otomatik algılanır | `http://localhost:51211` |
| `API_KEY` | API anahtarı (yerel için isteğe bağlı) | `""` | `your-api-key` |

## Sorun Giderme

### Yaygın Sorunlar

**Chainlit Uygulaması:**

1. **Hizmet mevcut değil:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Port çakışmaları:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python ortam sorunları:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU Demo:**

1. **WebGPU desteklenmiyor:**
   - Chrome/Edge 113+ sürümüne güncelleyin
   - WebGPU'yu etkinleştirin: `chrome://flags/#enable-unsafe-webgpu`
   - GPU durumunu kontrol edin: `chrome://gpu`
   - Demo otomatik olarak CPU'ya geçer

2. **Model yükleme hataları:**
   - Model indirme için internet bağlantısını kontrol edin
   - Tarayıcı konsolunda CORS hatalarını kontrol edin
   - HTTP üzerinden hizmet verdiğinizden emin olun (file:// değil)

**Open WebUI:**

1. **Bağlantı reddedildi:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modeller görünmüyor:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Doğrulama Kontrol Listesi

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## İleri Düzey Kullanım

### Performans Optimizasyonu

**Chainlit:**
- Daha iyi algılanan performans için akış kullanın
- Yüksek eşzamanlılık için bağlantı havuzu uygulayın
- Tekrarlanan sorgular için model yanıtlarını önbelleğe alın
- Büyük sohbet geçmişleriyle bellek kullanımını izleyin

**WebGPU:**
- Maksimum gizlilik ve hız için WebGPU kullanın
- Daha küçük modeller için model kuantizasyonu uygulayın
- Arka plan işlemleri için Web Workers kullanın
- Derlenmiş modelleri tarayıcı depolamasında önbelleğe alın

**Open WebUI:**
- Sohbet geçmişi için kalıcı hacimler kullanın
- Docker konteyneri için kaynak sınırlarını yapılandırın
- Kullanıcı verileri için yedekleme stratejileri uygulayın
- SSL sonlandırma için ters proxy ayarlayın

### Entegrasyon Modelleri

**Hibrit Yerel/Bulut:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Çok Modlu İşlem Hattı:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Üretim Dağıtımı

### Güvenlik Hususları

- **API Anahtarları**: Ortam değişkenlerini kullanın, asla kod içine yazmayın
- **Ağ**: Üretimde HTTPS kullanın, ekip erişimi için VPN düşünün
- **Erişim Kontrolü**: Open WebUI için kimlik doğrulama uygulayın
- **Veri Gizliliği**: Hangi verilerin yerel kaldığını ve hangilerinin buluta gittiğini denetleyin
- **Güncellemeler**: Foundry Local ve konteynerleri güncel tutun

### İzleme ve Bakım

- **Sağlık Kontrolleri**: Uç nokta izleme uygulayın
- **Günlükler**: Tüm bileşenlerden gelen günlükleri merkezileştirin
- **Metrikler**: Yanıt sürelerini, hata oranlarını, kaynak kullanımını takip edin
- **Yedekleme**: Sohbet verileri ve yapılandırmaların düzenli yedeğini alın

## Referanslar ve Kaynaklar

### Dokümantasyon
- [Chainlit Dokümantasyonu](https://docs.chainlit.io/) - Tam çerçeve rehberi
- [Foundry Local Dokümantasyonu](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Resmi Microsoft belgeleri
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU entegrasyonu
- [Open WebUI Dokümantasyonu](https://docs.openwebui.com/) - Gelişmiş yapılandırma

### Örnek Dosyalar
- [`app.py`](../../../../../Module08/samples/04/app.py) - Üretim Chainlit uygulaması
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Eğitim not defteri
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Tarayıcı tabanlı AI çıkarımı
- [`open-webui-guide.md`](./open-webui-guide.md) - Tam Open WebUI kurulumu

### İlgili Örnekler
- [Oturum 4 Dokümantasyonu](../../04.CuttingEdgeModels.md) - Tam oturum rehberi
- [Foundry Local Örnekleri](https://github.com/microsoft/foundry-local/tree/main/samples) - Resmi örnekler

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.