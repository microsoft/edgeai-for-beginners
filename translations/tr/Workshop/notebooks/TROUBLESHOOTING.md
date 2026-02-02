# Atölye Not Defterleri - Sorun Giderme Kılavuzu

## İçindekiler

- [Yaygın Sorunlar ve Çözümler](../../../../Workshop/notebooks)
- [Oturum 04'e Özgü Sorunlar](../../../../Workshop/notebooks)
- [Oturum 05'e Özgü Sorunlar](../../../../Workshop/notebooks)
- [Oturum 06'ya Özgü Sorunlar](../../../../Workshop/notebooks)
- [Donanıma Özgü Sorunlar](../../../../Workshop/notebooks)
- [Tanı Komutları](../../../../Workshop/notebooks)
- [Yardım Alma](../../../../Workshop/notebooks)

---

## Yaygın Sorunlar ve Çözümler

### 🔴 CUDA Bellek Yetersizliği

**Hata Mesajı:**
```
CUDA failure 2: out of memory
```

**Temel Sebep:** GPU, modeli yüklemek için yeterli VRAM'e sahip değil.

**Çözümler:**

#### Seçenek 1: CPU Varyantlarını Kullan (Önerilen)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Seçenek 2: GPU'da Daha Küçük Modeller Kullan
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Seçenek 3: GPU Belleğini Temizle
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Seçenek 4: GPU Belleğini Artır (mümkünse)
- Tarayıcı sekmelerini, video düzenleyicileri veya diğer GPU uygulamalarını kapatın
- Windows görsel efektlerini azaltın
- Entegre + ayrık GPU varsa ayrık GPU'yu kullanın

---

### 🔴 APIConnectionError: Bağlantı Hatası

**Hata Mesajı:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Temel Sebep:** Foundry Local servisi çalışmıyor veya erişilebilir değil.

**Çözümler:**

#### Adım 1: Servis Durumunu Kontrol Et
```bash
foundry service status
```

#### Adım 2: Servis Durdurulmuşsa Başlat
```bash
foundry service start
```

#### Adım 3: Uç Noktayı Doğrula
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Adım 4: Gerekli Modelleri Yükle
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Adım 5: Not Defteri Çekirdeğini Yeniden Başlat
Servisi başlattıktan ve modelleri yükledikten sonra not defteri çekirdeğini yeniden başlatın ve tüm hücreleri yeniden çalıştırın.

---

### 🔴 Katalogda Model Bulunamadı

**Hata Mesajı:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Temel Sebep:** Model, Foundry Local'da indirilmemiş veya yüklenmemiş.

**Çözümler:**

#### Seçenek 1: Modelleri İndir ve Yükle
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Seçenek 2: Otomatik Seçim Modunu Kullan
KATALOG'unuzu temel model adlarını (örneğin, `-cpu` eki olmadan) kullanacak şekilde güncelleyin:

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK, donanımınız için en iyi varyantı (CPU, GPU veya NPU) otomatik olarak seçecektir.

---

### 🔴 HttpResponseError: 500 - Model Yükleme Başarısız

**Hata Mesajı:**
```
HttpResponseError: 500 - Failed loading model
```

**Temel Sebep:** Model dosyası bozuk veya donanımla uyumsuz.

**Çözümler:**

#### Modeli Yeniden İndir
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Farklı Bir Varyant Kullan
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: Modül Bulunamadı

**Hata Mesajı:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Temel Sebep:** foundry-local-sdk paketi yüklenmemiş.

**Çözümler:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � İlk İstek Yavaş

**Belirti:** İlk tamamlama 30+ saniye sürüyor, sonraki istekler hızlı.

**Temel Sebep:** Bu normal bir davranış - servis, ilk istekte modeli belleğe yüklüyor.

**Çözümler:**

#### Modelleri Önceden Yükle
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Servisi Çalışır Durumda Tut
```bash
# Start service manually and leave it running
foundry service start
```

---

## Oturum 04'e Özgü Sorunlar

### Yanlış Port Yapılandırması

**Sorun:** Not defteri yanlış porta bağlanıyor (55769 yerine 59959 veya 57127)

**Çözüm:**

1. Foundry Local'ın hangi portu kullandığını kontrol edin:
```bash
foundry service status
# Note the port number displayed
```

2. Not defterindeki Hücre 10'u güncelleyin:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Çekirdeği yeniden başlatın ve hücreleri 6, 8, 10, 12, 16, 20, 22 sırasıyla yeniden çalıştırın.

---

### Yanlış Model Seçimi

**Sorun:** Not defteri gpt-oss-20b veya qwen2.5-7b gösteriyor, qwen2.5-3b yerine.

**Çözüm:**

1. Not defteri çekirdeğini yeniden başlatın (eski değişken durumunu temizler)
2. Hücre 10'u yeniden çalıştırın (Model Takma Adlarını Ayarla)
3. Hücre 12'yi yeniden çalıştırın (Yapılandırmayı Göster)
4. **Doğrula:** Hücre 12, `LLM Model: qwen2.5-3b` göstermelidir.

---

### Tanı Hücresi Başarısız

**Sorun:** Hücre 16 "❌ Foundry Local servisi bulunamadı!" gösteriyor.

**Çözüm:**

1. Servisin çalıştığını doğrulayın:
```bash
foundry service status
```

2. Uç noktayı manuel olarak test edin:
```bash
curl http://localhost:59959/v1/models
```

3. Eğer curl çalışıyor ama not defteri çalışmıyorsa:
   - Not defteri çekirdeğini yeniden başlatın
   - Hücreleri sırayla yeniden çalıştırın: 6, 8, 10, 12, 14, 16

4. Eğer curl başarısız olursa:
   - Servisi başlatın: `foundry service start`
   - Modelleri yükleyin: `foundry model run phi-4-mini` ve `foundry model run qwen2.5-3b`

---

### Ön Kontrol Başarısız

**Sorun:** Hücre 20, tanı geçtiği halde bağlantı hataları gösteriyor.

**Çözüm:**

1. Modellerin yüklü olduğunu kontrol edin:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Eğer modeller eksikse:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Modeller yüklendikten sonra Hücre 20'yi yeniden çalıştırın.

---

### Karşılaştırma None Değerleriyle Başarısız

**Sorun:** Hücre 22 tamamlanıyor ama gecikme None olarak gösteriliyor.

**Çözüm:**

1. Ön kontrolün önce geçtiğinden emin olun (Hücre 20)
2. Hücre 22'yi yeniden çalıştırın - modeller ilk istekte ısınmaya ihtiyaç duyabilir.
3. Her iki modelin de yüklü olduğunu doğrulayın: `foundry model ls`

---

## Oturum 05'e Özgü Sorunlar

### Ajan Yanlış Model Kullanıyor

**Sorun:** Ajan beklenen modeli kullanmıyor.

**Çözüm:**

Yapılandırmayı doğrulayın:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Eğer modeller yanlışsa çekirdeği yeniden başlatın.

---

### Bellek Bağlamı Taşması

**Sorun:** Ajan yanıtları zamanla kötüleşiyor.

**Çözüm:** Zaten otomatik olarak ele alınıyor - ajanlar bellekte yalnızca son 6 mesajı tutar.

---

## Oturum 06'ya Özgü Sorunlar

### CPU ve GPU Model Karışıklığı

**Sorun:** Varsayılan yapılandırma kullanılırken CUDA hataları alınıyor.

**Çözüm:** Varsayılan yapılandırma artık CPU modellerini kullanıyor. Eğer CUDA hataları görüyorsanız:

1. Varsayılan CPU katalogunu kullandığınızı doğrulayın:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Çekirdeği yeniden başlatın ve tüm hücreleri yeniden çalıştırın.

---

### Niyet Algılama Çalışmıyor

**Sorun:** İstekler yanlış modellere yönlendiriliyor.

**Çözüm:**

Niyet algılamayı test edin:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Eğer desenlerin ayarlanması gerekiyorsa RULES'u güncelleyin.

---

## Donanıma Özgü Sorunlar

### NVIDIA GPU

**GPU Durumunu Kontrol Et:**
```bash
nvidia-smi
```

**Yaygın Sorunlar:**
- **Sürücü güncel değil:** NVIDIA sürücülerini güncelleyin
- **CUDA sürüm uyumsuzluğu:** Foundry Local'ı yeniden yükleyin
- **GPU belleği parçalanmış:** Sistemi yeniden başlatın

### Qualcomm NPU

**NPU Durumunu Kontrol Et:**
```bash
foundry device info
```

**Yaygın Sorunlar:**
- **NPU sürücüleri yüklenmemiş:** Qualcomm NPU sürücülerini yükleyin
- **NPU varyantı mevcut değil:** CPU varyantını kullanın
- **Windows sürümü çok eski:** En son Windows 11'e güncelleyin

### Sadece CPU Sistemleri

**Önerilen Modeller:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Performans İpuçları:**
- En küçük modelleri kullanın
- max_tokens değerini azaltın
- İlk istek için sabırlı olun

---

## Tanı Komutları

### Her Şeyi Kontrol Et
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### Python'da
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## Yardım Alma

### 1. Günlükleri Kontrol Et
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub Sorunları
- Mevcut sorunları arayın: https://github.com/microsoft/Foundry-Local/issues
- Yeni bir sorun oluşturun ve şunları ekleyin:
  - Hata mesajı (tam metin)
  - `foundry service status` çıktısı
  - `foundry --version` çıktısı
  - GPU/NPU bilgisi (nvidia-smi, vb.)
  - Yeniden üretme adımları

### 3. Belgeler
- **Ana Depo:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Referansı:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Sorun Giderme:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Hızlı Çözümler Kontrol Listesi

Bir şeyler ters gittiğinde, sırayla şunları deneyin:

- [ ] Servisin çalıştığını kontrol edin: `foundry service status`
- [ ] Servisi yeniden başlatın: `foundry service stop && foundry service start`
- [ ] Modelin mevcut olduğunu doğrulayın: `foundry model ls | grep phi-4-mini`
- [ ] Gerekli modelleri yükleyin: `foundry model run phi-4-mini`
- [ ] GPU belleğini kontrol edin: `nvidia-smi` (eğer NVIDIA kullanıyorsanız)
- [ ] CPU varyantını deneyin: `phi-4-mini-cpu` yerine `phi-4-mini` kullanın
- [ ] Not defteri çekirdeğini yeniden başlatın
- [ ] Not defteri çıktısını temizleyin ve tüm hücreleri yeniden çalıştırın
- [ ] SDK'yı yeniden yükleyin: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Sistemi yeniden başlatın (son çare)

---

## Önleme İpuçları

### En İyi Uygulamalar

1. **Önce servisi her zaman kontrol edin:**
   ```bash
   foundry service status
   ```

2. **Varsayılan olarak CPU varyantlarını kullanın:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Not defterlerini çalıştırmadan önce modelleri önceden yükleyin:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Servisi çalışır durumda tutun:**
   - Servisi gereksiz yere durdurup başlatmayın
   - Oturumlar arasında arka planda çalışmasına izin verin

5. **Kaynakları izleyin:**
   - Çalıştırmadan önce GPU belleğini kontrol edin
   - Gereksiz GPU uygulamalarını kapatın
   - Görev Yöneticisi / nvidia-smi kullanın

6. **Düzenli olarak güncelleyin:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Son Güncelleme:** 8 Ekim 2025

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.