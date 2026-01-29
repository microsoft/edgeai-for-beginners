# Örnek 02: OpenAI SDK Entegrasyonu

Microsoft Foundry Local ve Azure OpenAI ile gelişmiş entegrasyonu, akış yanıtları ve doğru hata yönetimini destekleyen bir örnek.

## Genel Bakış

Bu örnek şunları sergiler:
- Foundry Local ve Azure OpenAI arasında sorunsuz geçiş
- Daha iyi kullanıcı deneyimi için akışlı sohbet tamamlama
- FoundryLocalManager SDK'nın doğru kullanımı
- Güçlü hata yönetimi ve yedekleme mekanizmaları
- Üretime hazır kod kalıpları

## Ön Koşullar

- **Foundry Local**: Kurulu ve çalışıyor (yerel çıkarım için)
- **Python**: 3.8 veya üstü, OpenAI SDK ile
- **Azure OpenAI**: Geçerli bir uç nokta ve API anahtarı (bulut çıkarımı için)

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

3. **Foundry Local'i başlatın (yerel mod için):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Kullanım Senaryoları

### Foundry Local (Varsayılan)

**Seçenek 1: FoundryLocalManager Kullanımı (Önerilen)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Seçenek 2: Manuel Yapılandırma**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## Kod Mimarisi

### İstemci Fabrika Deseni

Örnek, uygun istemcileri oluşturmak için bir fabrika desenini kullanır:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### Akış Yanıtları

Örnek, gerçek zamanlı yanıt oluşturma için akışı gösterir:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## Ortam Değişkenleri

### Foundry Local Yapılandırması

| Değişken | Açıklama | Varsayılan | Gerekli |
|----------|-------------|---------|----------|
| `MODEL` | Kullanılacak model takma adı | `phi-4-mini` | Hayır |
| `BASE_URL` | Foundry Local uç noktası | `http://localhost:8000` | Hayır |
| `API_KEY` | API anahtarı (yerel için isteğe bağlı) | `""` | Hayır |

### Azure OpenAI Yapılandırması

| Değişken | Açıklama | Varsayılan | Gerekli |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI kaynak uç noktası | - | Evet |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API anahtarı | - | Evet |
| `AZURE_OPENAI_API_VERSION` | API sürümü | `2024-08-01-preview` | Hayır |
| `MODEL` | Azure dağıtım adı | `your-deployment-name` | Evet |

## Gelişmiş Özellikler

### Otomatik Hizmet Keşfi

Örnek, ortam değişkenlerine göre uygun hizmeti otomatik olarak algılar:

1. **Azure Modu**: `AZURE_OPENAI_ENDPOINT` ve `AZURE_OPENAI_API_KEY` ayarlandığında
2. **Foundry SDK Modu**: Foundry Local SDK mevcutsa
3. **Manuel Mod**: Manuel yapılandırmaya geri dönüş

### Hata Yönetimi

- SDK'dan manuel yapılandırmaya zarif bir geçiş
- Sorun giderme için net hata mesajları
- Ağ sorunları için uygun istisna yönetimi
- Gerekli ortam değişkenlerinin doğrulanması

## Performans Düşünceleri

### Yerel ve Bulut Karşılaştırması

**Foundry Local Avantajları:**
- ✅ API maliyeti yok
- ✅ Veri gizliliği (veriler cihazdan çıkmaz)
- ✅ Desteklenen modeller için düşük gecikme süresi
- ✅ Çevrimdışı çalışır

**Azure OpenAI Avantajları:**
- ✅ En son büyük modellere erişim
- ✅ Daha yüksek işlem kapasitesi
- ✅ Yerel hesaplama gereksinimi yok
- ✅ Kurumsal düzeyde SLA

## Sorun Giderme

### Yaygın Sorunlar

1. **"Foundry SDK kullanılamadı" uyarısı:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure kimlik doğrulama hataları:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model mevcut değil:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Sağlık Kontrolleri

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Sonraki Adımlar

- **Örnek 03**: Model keşfi ve performans testi
- **Örnek 04**: Chainlit RAG uygulaması oluşturma
- **Örnek 05**: Çoklu ajan orkestrasyonu
- **Örnek 06**: Araç olarak modeller yönlendirme

## Referanslar

- [Azure OpenAI Belgeleri](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Referansı](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Belgeleri](https://github.com/openai/openai-python)
- [Akış Tamamlama Kılavuzu](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

