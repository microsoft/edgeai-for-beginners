# Open WebUI + Foundry Local Entegrasyon Kılavuzu

Bu kılavuz, Open WebUI'yi Microsoft Foundry Local ile nasıl bağlayacağınızı ve yerel AI modellerinizle çalışan profesyonel bir ChatGPT benzeri arayüz oluşturacağınızı gösterir.

## Genel Bakış

Open WebUI, herhangi bir OpenAI uyumlu API'ye bağlanabilen modern ve kullanıcı dostu bir sohbet arayüzü sunar. Foundry Local ile bağlandığında şu avantajları elde edersiniz:

- **Profesyonel Arayüz**: Modern tasarıma sahip ChatGPT benzeri bir arayüz
- **Yerel Gizlilik**: Tüm işlemler cihazınızda gerçekleşir
- **Model Değiştirme**: Farklı yerel modeller arasında kolay geçiş
- **Sohbet Geçmişi**: Kalıcı sohbet geçmişi ve bağlam
- **Dosya Yükleme**: Belge analizi ve dosya işleme yetenekleri
- **Özel Karakterler**: Sistem komutları ve rol özelleştirme

## Gereksinimler

### Gerekli Yazılımlar

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Bir Model Yükleme

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Hızlı Kurulum (Önerilen)

### Adım 1: Open WebUI'yi Docker ile Çalıştırma

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

### Adım 2: İlk Kurulum

1. **Tarayıcıyı Açın**: `http://localhost:3000` adresine gidin
2. **Hesap Oluşturun**: Yönetici kullanıcıyı ayarlayın (ilk kullanıcı yönetici olur)
3. **Bağlantıyı Doğrulayın**: Modeller otomatik olarak açılır menüde görünmelidir

### Adım 3: Bağlantıyı Test Etme

1. Açılır menüden modelinizi seçin (ör. "phi-4-mini")
2. Test mesajı yazın: "Merhaba! Kendinizi tanıtabilir misiniz?"
3. Yerel modelinizden akan bir yanıt görmelisiniz

## Gelişmiş Yapılandırma

### Ortam Değişkenleri

| Değişken | Amaç | Varsayılan | Örnek |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local uç noktası | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API anahtarı (yerelde gerekli değil) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Oturum şifreleme anahtarı | otomatik oluşturulur | `your-secret-key` |
| `ENABLE_SIGNUP` | Yeni kullanıcı kaydına izin ver | `True` | `False` |

### Manuel Yapılandırma (Alternatif)

Eğer ortam değişkenleri çalışmazsa, manuel olarak yapılandırın:

1. **Ayarları Açın**: Ayarlar simgesine (dişli) tıklayın
2. **Bağlantılara Gidin**: Ayarlar → Bağlantılar → OpenAI
3. **API Detaylarını Ayarlayın**:
   - API Temel URL: `http://host.docker.internal:51211/v1`
   - API Anahtarı: `foundry-local-key` (herhangi bir değer çalışır)
4. **Kaydet ve Test Et**: "Kaydet"e tıklayın ve bir modelle test edin

### Kalıcı Veri Depolama

Sohbetleri ve ayarları kalıcı hale getirmek için:

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

## Sorun Giderme

### Bağlantı Sorunları

**Sorun**: "Bağlantı reddedildi" veya modeller yüklenmiyor

**Çözümler**:
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

### Model Görünmüyor

**Sorun**: Open WebUI açılır menüde model göstermiyor

**Hata Ayıklama Adımları**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Çözüm**: Modelin düzgün yüklendiğinden emin olun:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker Ağ Sorunları

**Sorun**: `host.docker.internal` çözümlenmiyor

**Windows Çözümü**:
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

**Alternatif**: Makinenizin IP adresini bulun:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Performans Sorunları

**Yavaş Yanıtlar**:
1. Modelin GPU hızlandırma kullandığını kontrol edin: `foundry service ps`
2. Yeterli sistem kaynaklarını doğrulayın (RAM/GPU belleği)
3. Test için daha küçük bir model kullanmayı düşünün

**Bellek Sorunları**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Kullanım Kılavuzu

### Temel Sohbet

1. **Model Seçin**: Açılır menüden Foundry Local modellerini seçin
2. **Mesaj Yazın**: Alttaki metin girişini kullanın
3. **Gönder**: Enter tuşuna basın veya Gönder düğmesine tıklayın
4. **Yanıtı Görün**: Gerçek zamanlı olarak akan yanıtı izleyin

### Gelişmiş Özellikler

**Dosya Yükleme**:
1. Ataç simgesine tıklayın
2. Belge yükleyin (PDF, TXT, vb.)
3. İçerikle ilgili sorular sorun
4. Model belgeyi analiz eder ve yanıt verir

**Özel Sistem Komutları**:
1. Ayarlar → Kişiselleştirme
2. Özel sistem komutunu ayarlayın
3. Tutarlı bir AI kişiliği/davranışı oluşturur

**Sohbet Yönetimi**:
- **Yeni Sohbet**: "+" simgesine tıklayarak yeni bir sohbet başlatın
- **Sohbet Geçmişi**: Yan menüden önceki sohbetlere erişin
- **Dışa Aktar**: Sohbet geçmişini metin/JSON olarak indirin

**Model Karşılaştırması**:
1. Aynı Open WebUI'yi birden fazla tarayıcı sekmesinde açın
2. Her sekmede farklı modeller seçin
3. Aynı komutlara verilen yanıtları karşılaştırın

### Entegrasyon Modelleri

**Geliştirme İş Akışı**:
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

## Üretim Dağıtımı

### Güvenli Kurulum

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

### Çok Kullanıcılı Kurulum

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

### İzleme ve Günlükleme

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Temizlik

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

## Sonraki Adımlar

### Geliştirme Fikirleri

1. **Özel Modeller**: Kendi ince ayar yapılmış modellerinizi Foundry Local'a ekleyin
2. **API Entegrasyonu**: Open WebUI işlevleri aracılığıyla harici API'lere bağlanın
3. **Belge İşleme**: Gelişmiş RAG iş akışlarını ayarlayın
4. **Çok Modlu**: Görüntü analizi için görsel modelleri yapılandırın

### Ölçeklendirme Düşünceleri

- **Yük Dengeleme**: Ters proxy arkasında birden fazla Foundry Local örneği
- **Model Yönlendirme**: Farklı kullanım durumları için farklı modeller
- **Kaynak Yönetimi**: Eşzamanlı kullanıcılar için GPU belleği optimizasyonu
- **Yedekleme Stratejisi**: Sohbet verilerinin ve yapılandırmaların düzenli yedeklenmesi

## Referanslar

- [Open WebUI Belgeleri](https://docs.openwebui.com/)
- [Open WebUI GitHub Deposu](https://github.com/open-webui/open-webui)
- [Foundry Local Belgeleri](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Kurulum Kılavuzu](https://docs.docker.com/get-docker/)

---

