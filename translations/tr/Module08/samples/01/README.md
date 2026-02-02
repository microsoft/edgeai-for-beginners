# Örnek 01: OpenAI SDK ile Hızlı Sohbet

Microsoft Foundry Local ile yerel AI çıkarımı için OpenAI SDK kullanımını gösteren basit bir sohbet örneği.

## Genel Bakış

Bu örnek şunları gösterir:
- OpenAI Python SDK'yı Foundry Local ile kullanma
- Hem Azure OpenAI hem de yerel Foundry yapılandırmalarını yönetme
- Doğru hata yönetimi ve yedekleme stratejileri uygulama
- FoundryLocalManager'ı hizmet yönetimi için kullanma

## Ön Koşullar

- **Foundry Local**: Kurulu ve PATH üzerinde erişilebilir
- **Python**: 3.8 veya daha yeni bir sürüm
- **Model**: Foundry Local'de yüklenmiş bir model (örneğin, `phi-4-mini`)

## Kurulum

1. **Python ortamını ayarlayın:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Bağımlılıkları yükleyin:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local hizmetini başlatın ve bir model yükleyin:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Kullanım

### Foundry Local (Varsayılan)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## Kod Özellikleri

### FoundryLocalManager Entegrasyonu

Örnek, doğru hizmet yönetimi için resmi Foundry Local SDK'yı kullanır:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### Hata Yönetimi

Manuel yapılandırmaya yedekleme ile sağlam hata yönetimi:
- Otomatik hizmet keşfi
- SDK kullanılamazsa zarif bir şekilde işlevselliği azaltma
- Sorun giderme için net hata mesajları

## Ortam Değişkenleri

| Değişken | Açıklama | Varsayılan | Gerekli |
|----------|-------------|---------|----------|
| `MODEL` | Model takma adı veya adı | `phi-4-mini` | Hayır |
| `BASE_URL` | Foundry Local temel URL'si | `http://localhost:8000` | Hayır |
| `API_KEY` | API anahtarı (genellikle yerel için gerekli değil) | `""` | Hayır |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI uç noktası | - | Azure için |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API anahtarı | - | Azure için |
| `AZURE_OPENAI_API_VERSION` | Azure API sürümü | `2024-08-01-preview` | Hayır |

## Sorun Giderme

### Yaygın Sorunlar

1. **"Foundry SDK kullanılamadı" uyarısı:**
   - Foundry Local SDK'yı yükleyin: `pip install foundry-local-sdk`
   - Veya manuel yapılandırma için ortam değişkenlerini ayarlayın

2. **Bağlantı reddedildi:**
   - Foundry Local'in çalıştığından emin olun: `foundry service status`
   - Bir modelin yüklü olup olmadığını kontrol edin: `foundry service ps`

3. **Model bulunamadı:**
   - Mevcut modelleri listeleyin: `foundry model list`
   - Bir model yükleyin: `foundry model run phi-4-mini`

### Doğrulama

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Referanslar

- [Foundry Local Belgeleri](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-uyumlu API Referansı](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

