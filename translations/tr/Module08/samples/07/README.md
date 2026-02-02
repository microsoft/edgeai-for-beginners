# Foundry Local API Örneği

Bu örnek, Microsoft Foundry Local'ı OpenAI SDK'ya bağlı kalmadan bir REST API hizmeti olarak nasıl kullanacağınızı gösterir. Maksimum kontrol ve özelleştirme için doğrudan HTTP entegrasyon desenlerini sunar.

## Genel Bakış

Microsoft'un resmi Foundry Local desenlerine dayanarak, bu örnek şunları sağlar:
- FoundryLocalManager ile doğrudan REST API entegrasyonu
- Özel HTTP istemci uygulaması
- Model yönetimi ve sağlık izleme
- Akışlı ve akışsız yanıt işleme
- Üretime hazır hata yönetimi ve yeniden deneme mantığı

## Ön Koşullar

1. **Foundry Local Kurulumu**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python Bağımlılıkları**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Mimari

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Temel Özellikler

### 1. **Doğrudan HTTP Entegrasyonu**
- SDK bağımlılığı olmadan saf REST API çağrıları
- Özel kimlik doğrulama ve başlıklar
- İstek/yanıt işleme üzerinde tam kontrol

### 2. **Model Yönetimi**
- Dinamik model yükleme ve kaldırma
- Sağlık izleme ve durum kontrolleri
- Performans metriklerinin toplanması

### 3. **Üretim Desenleri**
- Üstel geri çekilme ile yeniden deneme mekanizmaları
- Hata toleransı için devre kesici
- Kapsamlı günlükleme ve izleme

### 4. **Esnek Yanıt İşleme**
- Gerçek zamanlı uygulamalar için akışlı yanıtlar
- Yüksek verim senaryoları için toplu işleme
- Özel yanıt ayrıştırma ve doğrulama

## Kullanım Örnekleri

### Temel API Entegrasyonu
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Akışlı Entegrasyon
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Sağlık İzleme
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Dosya Yapısı

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Microsoft Foundry Local Entegrasyonu

Bu örnek, Microsoft'un resmi desenlerini takip eder:

1. **SDK Entegrasyonu**: Hizmet yönetimi için `FoundryLocalManager` kullanır
2. **REST Uç Noktaları**: `/v1/chat/completions` ve diğer uç noktalara doğrudan çağrılar
3. **Kimlik Doğrulama**: Yerel hizmetler için uygun API anahtarı yönetimi
4. **Model Yönetimi**: Katalog listeleme, indirme ve yükleme desenleri
5. **Hata Yönetimi**: Microsoft tarafından önerilen hata kodları ve yanıtlar

## Başlarken

1. **Bağımlılıkları Yükleyin**
   ```bash
   pip install -r requirements.txt
   ```

2. **Temel Örneği Çalıştırın**
   ```bash
   python examples/basic_usage.py
   ```

3. **Akışlı İşlemi Deneyin**
   ```bash
   python examples/streaming.py
   ```

4. **Üretim Kurulumu**
   ```bash
   python examples/production.py
   ```

## Yapılandırma

Özelleştirme için ortam değişkenleri:
- `FOUNDRY_MODEL`: Kullanılacak varsayılan model (varsayılan: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: İstek zaman aşımı süresi (varsayılan: 30 saniye)
- `FOUNDRY_RETRIES`: Yeniden deneme girişim sayısı (varsayılan: 3)
- `FOUNDRY_LOG_LEVEL`: Günlükleme seviyesi (varsayılan: "INFO")

## En İyi Uygulamalar

1. **Bağlantı Yönetimi**: Daha iyi performans için HTTP bağlantılarını yeniden kullanın
2. **Hata Yönetimi**: Üstel geri çekilme ile uygun yeniden deneme mantığını uygulayın
3. **Kaynak İzleme**: Model bellek kullanımı ve performansı izleyin
4. **Güvenlik**: Yerel hizmetler için bile uygun kimlik doğrulama kullanın
5. **Test**: Hem birim hem de entegrasyon testlerini dahil edin

## Sorun Giderme

### Yaygın Sorunlar

**Hizmet Çalışmıyor**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Model Yükleme Sorunları**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Bağlantı Hataları**
- Foundry Local'ın doğru portta çalıştığını doğrulayın
- Güvenlik duvarı ayarlarını kontrol edin
- Uygun kimlik doğrulama başlıklarını sağlayın

## Performans Optimizasyonu

1. **Bağlantı Havuzu**: Birden fazla istek için oturum nesneleri kullanın
2. **Asenkron İşlemler**: Eşzamanlı istekler için asyncio kullanın
3. **Önbellekleme**: Uygun yerlerde model yanıtlarını önbelleğe alın
4. **İzleme**: Yanıt sürelerini izleyin ve zaman aşımı ayarlarını düzenleyin

## Öğrenim Çıktıları

Bu örneği tamamladıktan sonra şunları anlayacaksınız:
- Foundry Local ile doğrudan REST API entegrasyonu
- Özel HTTP istemci uygulama desenleri
- Üretime hazır hata yönetimi ve izleme
- Microsoft Foundry Local hizmet mimarisi
- Yerel AI hizmetleri için performans optimizasyon teknikleri

## Sonraki Adımlar

- Örnek 08: Windows 11 Sohbet Uygulamasını Keşfedin
- Örnek 09: Çoklu Aracı Orkestrasyonunu Deneyin
- Örnek 10: Foundry Local'ı Araç Entegrasyonu Olarak Öğrenin

---

