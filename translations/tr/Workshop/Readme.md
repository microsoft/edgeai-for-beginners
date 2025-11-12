<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "04951692a100dcd716df01efca2d3f0d",
  "translation_date": "2025-11-11T23:00:15+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "tr"
}
-->
# EdgeAI için Yeni Başlayanlar - Atölye Çalışması

> **Üretime Hazır Edge AI Uygulamaları Oluşturmak İçin Uygulamalı Öğrenme Yolu**
>
> Microsoft Foundry Local ile yerel AI dağıtımını öğrenin; ilk sohbet tamamlama işleminden çoklu ajan düzenlemesine kadar 6 ilerleyici oturumda ustalaşın.

---

## 🎯 Giriş

**EdgeAI için Yeni Başlayanlar Atölyesi**'ne hoş geldiniz - tamamen yerel donanımda çalışan akıllı uygulamalar oluşturmak için pratik, uygulamalı rehberiniz. Bu atölye, teorik Edge AI kavramlarını Microsoft Foundry Local ve Küçük Dil Modelleri (SLM'ler) kullanarak gerçek dünya becerilerine dönüştüren giderek zorlaşan alıştırmalar içerir.

### Neden Bu Atölye?

**Edge AI Devrimi Başladı**

Dünya çapındaki kuruluşlar, üç kritik nedenden dolayı bulut bağımlı AI'dan edge computing'e geçiş yapıyor:

1. **Gizlilik ve Uyumluluk** - Hassas verileri buluta aktarmadan yerel olarak işleyin (HIPAA, GDPR, finansal düzenlemeler)
2. **Performans** - Ağ gecikmesini ortadan kaldırın (yerel 50-500ms vs bulut 500-2000ms gidiş-dönüş süresi)
3. **Maliyet Kontrolü** - Token başına API maliyetlerini kaldırın ve bulut masrafları olmadan ölçeklendirin

**Ancak Edge AI Farklıdır**

AI'ı yerel olarak çalıştırmak yeni beceriler gerektirir:
- Kaynak kısıtlamaları için model seçimi ve optimizasyonu
- Yerel hizmet yönetimi ve donanım hızlandırma
- Küçük modeller için prompt mühendisliği
- Edge cihazları için üretim dağıtım desenleri

**Bu Atölye Bu Becerileri Kazandırır**

6 odaklanmış oturumda (~3 saat toplam), "Merhaba Dünya"dan üretime hazır çoklu ajan sistemlerini dağıtmaya kadar ilerleyeceksiniz - hepsi yerel olarak bilgisayarınızda çalışacak.

---

## 📚 Öğrenme Hedefleri

Bu atölyeyi tamamladığınızda şunları yapabileceksiniz:

### Temel Yetkinlikler
1. **Yerel AI Hizmetlerini Dağıtma ve Yönetme**
   - Microsoft Foundry Local'ı kurun ve yapılandırın
   - Edge dağıtımı için uygun modelleri seçin
   - Model yaşam döngüsünü yönetin (indirme, yükleme, önbellekleme)
   - Kaynak kullanımını izleyin ve performansı optimize edin

2. **AI Destekli Uygulamalar Oluşturma**
   - OpenAI uyumlu sohbet tamamlama işlemlerini yerel olarak uygulayın
   - Küçük Dil Modelleri için etkili promptlar tasarlayın
   - Daha iyi kullanıcı deneyimi için akış yanıtlarını yönetin
   - Yerel modelleri mevcut uygulamalara entegre edin

3. **RAG (Retrieval Augmented Generation) Sistemleri Oluşturma**
   - Gömülü semantik arama oluşturun
   - LLM yanıtlarını alan spesifik bilgiyle temellendirin
   - Endüstri standart metriklerle RAG kalitesini değerlendirin
   - Prototipten üretime ölçeklendirin

4. **Model Performansını Optimize Etme**
   - Kullanım durumunuz için birden fazla modeli karşılaştırın
   - Gecikme, işlem hacmi ve ilk token süresini ölçün
   - Hız/kalite dengelerine göre optimal modelleri seçin
   - Gerçek senaryolarda SLM ve LLM karşılaştırmalarını yapın

5. **Çoklu Ajan Sistemlerini Düzenleme**
   - Farklı görevler için özel ajanlar tasarlayın
   - Ajan hafızası ve bağlam yönetimini uygulayın
   - Karmaşık iş akışlarında ajanları koordine edin
   - Birden fazla model arasında istekleri akıllıca yönlendirin

6. **Üretime Hazır Çözümler Dağıtma**
   - Hata işleme ve yeniden deneme mantığını uygulayın
   - Token kullanımını ve sistem kaynaklarını izleyin
   - Model-as-tools desenleriyle ölçeklenebilir mimariler oluşturun
   - Edge'den hibrit (edge + bulut) geçiş yollarını planlayın

---

## 🎓 Öğrenme Çıktıları

### Neler Yapacaksınız?

Atölye sonunda şunları oluşturmuş olacaksınız:

| Oturum | Çıktı | Gösterilen Beceriler |
|--------|-------|-----------------------|
| **1** | Akışlı sohbet uygulaması | Hizmet kurulumu, temel tamamlama, akış UX |
| **2** | Değerlendirme ile RAG sistemi | Gömülü semantik arama, kalite metrikleri |
| **3** | Çoklu model karşılaştırma paketi | Performans ölçümü, model karşılaştırması |
| **4** | SLM ve LLM karşılaştırıcı | Denge analizi, optimizasyon stratejileri |
| **5** | Çoklu ajan düzenleyici | Ajan tasarımı, hafıza yönetimi, koordinasyon |
| **6** | Akıllı yönlendirme sistemi | Niyet algılama, model seçimi, ölçeklenebilirlik |

### Yetkinlik Matrisi

| Beceri Seviyesi | Oturum 1-2 | Oturum 3-4 | Oturum 5-6 |
|-----------------|------------|------------|------------|
| **Başlangıç** | ✅ Kurulum ve temel bilgiler | ⚠️ Zorlayıcı | ❌ Çok ileri düzey |
| **Orta Seviye** | ✅ Hızlı gözden geçirme | ✅ Temel öğrenme | ⚠️ Zorlayıcı hedefler |
| **İleri Seviye** | ✅ Kolayca geçer | ✅ İyileştirme | ✅ Üretim desenleri |

### Kariyer Hazırlığı Becerileri

**Bu atölyeden sonra şunlara hazır olacaksınız:**

✅ **Gizlilik Odaklı Uygulamalar Oluşturma**
- PHI/PII'yi yerel olarak işleyen sağlık uygulamaları
- Uyumluluk gereksinimleri olan finansal hizmetler
- Veri egemenliği gerektiren devlet sistemleri

✅ **Edge Ortamları için Optimize Etme**
- Sınırlı kaynaklara sahip IoT cihazları
- Çevrimdışı öncelikli mobil uygulamalar
- Düşük gecikmeli gerçek zamanlı sistemler

✅ **Akıllı Mimariler Tasarlama**
- Karmaşık iş akışları için çoklu ajan sistemleri
- Hibrit edge-bulut dağıtımları
- Maliyet optimize edilmiş AI altyapısı

✅ **Edge AI Girişimlerine Liderlik Etme**
- Projeler için Edge AI uygulanabilirliğini değerlendirme
- Uygun modeller ve çerçeveler seçme
- Ölçeklenebilir yerel AI çözümleri tasarlama

---

## 🗺️ Atölye Yapısı

### Oturum Özeti (6 Oturum × 30 Dakika = 3 Saat)

| Oturum | Konu | Odak | Süre |
|--------|------|------|------|
| **1** | Foundry Local ile Başlangıç | Kurulum, doğrulama, ilk tamamlama | 30 dk |
| **2** | RAG ile AI Çözümleri Oluşturma | Prompt mühendisliği, gömülü semantik arama, değerlendirme | 30 dk |
| **3** | Açık Kaynak Modeller | Model keşfi, karşılaştırma, seçim | 30 dk |
| **4** | En Son Modeller | SLM ve LLM, optimizasyon, çerçeveler | 30 dk |
| **5** | AI Destekli Ajanlar | Ajan tasarımı, düzenleme, hafıza | 30 dk |
| **6** | Araç Olarak Modeller | Yönlendirme, zincirleme, ölçekleme stratejileri | 30 dk |

---

## 🚀 Hızlı Başlangıç

### Ön Koşullar

**Sistem Gereksinimleri:**
- **OS**: Windows 10/11, macOS 11+, veya Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, önerilen 16GB+
- **Depolama**: Modeller için 10GB+ boş alan
- **CPU**: AVX2 destekli modern işlemci
- **GPU** (isteğe bağlı): CUDA uyumlu veya Qualcomm NPU hızlandırma için

**Yazılım Gereksinimleri:**
- **Python 3.8+** ([İndir](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Kurulum Kılavuzu](../../../Workshop))
- **Git** ([İndir](https://git-scm.com/downloads))
- **Visual Studio Code** (önerilir) ([İndir](https://code.visualstudio.com/))

### 3 Adımda Kurulum

#### 1. Foundry Local'ı Kurun

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Kurulumu Doğrulama:**
```bash
foundry --version
foundry service status
```

**Azure AI Foundry Local'ın sabit bir port ile çalıştığından emin olun**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Çalıştığını doğrulayın:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Mevcut Modelleri Bulma**
Foundry Local örneğinizde hangi modellerin mevcut olduğunu görmek için modeller uç noktasını sorgulayabilirsiniz:

```bash
# cmd/bash/powershell
foundry model list
```

Web Uç Noktası Kullanımı 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Depoyu Klonlayın ve Bağımlılıkları Kurun

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. İlk Örneğinizi Çalıştırın

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Başarılı!** Edge AI hakkında akışlı bir yanıt görmelisiniz.

---

## 📦 Atölye Kaynakları

### Python Örnekleri

Her kavramı gösteren ilerleyici uygulamalı örnekler:

| Oturum | Örnek | Açıklama | Çalışma Süresi |
|--------|-------|----------|----------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Temel ve akışlı sohbet | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | Gömülü semantik arama ile RAG | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG kalite değerlendirmesi | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Çoklu model karşılaştırması | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM ve LLM karşılaştırması | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Çoklu ajan sistemi | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Niyet tabanlı yönlendirme | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Çok adımlı işlem hattı | ~60s |

### Jupyter Notebooks

Açıklamalar ve görselleştirmelerle interaktif keşif:

| Oturum | Notebook | Açıklama | Zorluk |
|--------|----------|----------|--------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Sohbet temelleri ve akış | ⭐ Başlangıç |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | RAG sistemi oluşturma | ⭐⭐ Orta |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | RAG kalitesini değerlendirme | ⭐⭐ Orta |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Model karşılaştırması | ⭐⭐ Orta |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Model karşılaştırması | ⭐⭐ Orta |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Ajan düzenleme | ⭐⭐⭐ İleri |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Niyet yönlendirme | ⭐⭐⭐ İleri |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | İşlem hattı düzenleme | ⭐⭐⭐ İleri |

### Dokümantasyon

Kapsamlı kılavuzlar ve referanslar:

| Doküman | Açıklama | Kullanım Durumu |
|---------|----------|-----------------|
| [QUICK_START.md](./QUICK_START.md) | Hızlı kurulum kılavuzu | Sıfırdan başlarken |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Komut ve API hızlı referansı | Hızlı cevaplara ihtiyaç duyduğunuzda |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK desenleri ve örnekleri | Kod yazarken |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Ortam değişkeni kılavuzu | Örnekleri yapılandırırken |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Yaygın sorunlar ve çözümler | Sorun giderirken |

---

## 🎓 Öğrenme Yolu Önerileri

### Yeni Başlayanlar İçin (3-4 saat)
1. ✅ Oturum 1: Başlangıç (kurulum ve temel sohbet üzerine odaklanın)
2. ✅ Oturum 2: RAG Temelleri (başlangıçta değerlendirmeyi atlayın)
3. ✅ Oturum 3: Basit Karşılaştırma (sadece 2 model)
4. ⏭️ Şimdilik Oturum 4-6'yı atlayın
5. 🔄 İlk uygulamanızı oluşturduktan sonra Oturum 4-6'ya geri dönün

### Orta Seviye Geliştiriciler İçin (3 saat)
1. ⚡ Oturum 1: Hızlı kurulum doğrulaması
2. ✅ Oturum 2: Tam RAG işlem hattı ve değerlendirme
3. ✅ Oturum 3: Tam karşılaştırma paketi
4. ✅ Oturum 4: Model optimizasyonu
5. ✅ Oturum 5-6: Mimari desenlere odaklanın

### İleri Seviye Uygulayıcılar İçin (2-3 saat)
1. ⚡ Oturum 1-3: Hızlı gözden geçirme ve doğrulama
2. ✅ Oturum 4: Optimizasyon derinlemesine inceleme
3. ✅ Oturum 5: Çoklu ajan mimarisi
4. ✅ Oturum 6: Üretim desenleri ve ölçeklendirme
5. 🚀 Genişletme: Özel yönlendirme mantığı ve hibrit dağıtımlar oluşturun

---

## Atölye Oturum Paketi (Odaklanmış 30 Dakikalık Laboratuvarlar)

Yoğunlaştırılmış 6 oturumluk atölye formatını takip ediyorsanız, bu özel kılavuzları kullanın (her biri yukarıdaki daha geniş modül dokümanlarıyla eşleşir ve tamamlar):

| Atölye Oturumu | Kılavuz | Temel Odak |
|----------------|---------|------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Kurulum, doğrulama, phi & GPT-OSS-20B çalıştırma, hızlandırma |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt mühendisliği, RAG desenleri, CSV ve belge temellendirme, geçiş |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face entegrasyonu, karşılaştırma, model seçimi |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM ve LLM, WebGPU, Chainlit RAG, ONNX hızlandırma |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Ajan rolleri, hafıza, araçlar, düzenleme |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Azure'a yönlendirme, zincirleme, ölçeklendirme yolu |

Her oturum dosyası şunları içerir: özet, öğrenme hedefleri, 30 dakikalık demo akışı, başlangıç projesi, doğrulama kontrol listesi, sorun giderme ve resmi Foundry Local Python SDK'ya referanslar.

### Örnek Scriptler

Workshop bağımlılıklarını yükleyin (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Foundry Local hizmetini macOS'tan farklı bir (Windows) makine veya VM'de çalıştırıyorsanız, uç noktayı dışa aktarın:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Oturum | Script(ler) | Açıklama |
|--------|-------------|----------|
| 1 | `samples/session01/chat_bootstrap.py` | Hizmet başlatma ve akışlı sohbet |
| 2 | `samples/session02/rag_pipeline.py` | Minimal RAG (hafızada gömülü veriler) |
|   | `samples/session02/rag_eval_ragas.py` | RAG değerlendirmesi ragas metrikleriyle |
| 3 | `samples/session03/benchmark_oss_models.py` | Çoklu model gecikme ve throughput kıyaslaması |
| 4 | `samples/session04/model_compare.py` | SLM ve LLM karşılaştırması (gecikme ve örnek çıktı) |
| 5 | `samples/session05/agents_orchestrator.py` | İki ajan araştırma → editoryal süreç |
| 6 | `samples/session06/models_router.py` | Niyet tabanlı yönlendirme demosu |
|   | `samples/session06/models_pipeline.py` | Çok adımlı planlama/uygulama/düzeltme zinciri |

### Ortam Değişkenleri (Örnekler Arasında Ortak)

| Değişken | Amaç | Örnek |
|----------|------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Temel örnekler için varsayılan tek model takma adı | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Karşılaştırma için açık SLM ve daha büyük model | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Kıyaslama için takma adların virgülle ayrılmış listesi | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Model başına kıyaslama tekrarları | `3` |
| `BENCH_PROMPT` | Kıyaslamada kullanılan istem | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers gömme modeli | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | RAG hattı için test sorgusunu geçersiz kıl | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Ajanlar hattı sorgusunu geçersiz kıl | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Araştırma ajanı için model takma adı | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Editör ajanı için model takma adı (farklı olabilir) | `gpt-oss-20b` |
| `SHOW_USAGE` | `1` olduğunda, tamamlamalar başına token kullanımını yazdırır | `1` |
| `RETRY_ON_FAIL` | `1` olduğunda, geçici sohbet hatalarında bir kez yeniden dener | `1` |
| `RETRY_BACKOFF` | Yeniden denemeden önce bekleme süresi (saniye) | `1.0` |

Bir değişken ayarlanmadığında, scriptler mantıklı varsayılanlara geri döner. Tek model demoları için genellikle sadece `FOUNDRY_LOCAL_ALIAS` gereklidir.

### Yardımcı Modül

Tüm örnekler artık `samples/workshop_utils.py` adlı bir yardımcı dosyayı paylaşır ve şunları sağlar:

* Önbelleğe alınmış `FoundryLocalManager` + OpenAI istemci oluşturma
* Opsiyonel yeniden deneme ve kullanım yazdırma ile `chat_once()` yardımcısı
* Basit token kullanım raporlama (`SHOW_USAGE=1` ile etkinleştirin)

Bu, tekrarı azaltır ve yerel model düzenlemesi için en iyi uygulamaları vurgular.

## İsteğe Bağlı Geliştirmeler (Oturumlar Arası)

| Tema | Geliştirme | Oturumlar | Ortam / Anahtar |
|------|-----------|-----------|-----------------|
| Determinizm | Sabit sıcaklık + stabil istem setleri | 1–6 | `temperature=0`, `top_p=1` ayarla |
| Token Kullanım Görünürlüğü | Tutarlı maliyet/verimlilik öğretimi | 1–6 | `SHOW_USAGE=1` |
| İlk Token Akışı | Algılanan gecikme metriği | 1,3,4,6 | `BENCH_STREAM=1` (kıyaslama) |
| Yeniden Deneme Dayanıklılığı | Geçici soğuk başlangıcı ele alır | Tümü | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Çoklu Model Ajanlar | Heterojen rol uzmanlığı | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Uyarlanabilir Yönlendirme | Niyet + maliyet sezgileri | 6 | Yönlendiriciyi yükseltme mantığıyla genişletin |
| Vektör Belleği | Uzun vadeli semantik hatırlama | 2,5,6 | FAISS/Chroma gömme indeksini entegre edin |
| İzleme Dışa Aktarımı | Denetim ve değerlendirme | 2,5,6 | Her adım için JSON satırları ekleyin |
| Kalite Ölçütleri | Niteliksel izleme | 3–6 | İkincil puanlama istemleri |
| Hızlı Testler | Workshop öncesi hızlı doğrulama | Tümü | `python Workshop/tests/smoke.py` |

### Deterministik Hızlı Başlangıç

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Tekrarlanan aynı girdilerde sabit token sayıları bekleyin.

### RAG Değerlendirmesi (Oturum 2)

Cevap alaka düzeyini, doğruluğunu ve bağlam hassasiyetini küçük bir sentetik veri setinde hesaplamak için `rag_eval_ragas.py` kullanın:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Daha büyük bir JSONL dosyası sağlayarak soruları, bağlamları ve gerçekleri ekleyin, ardından Hugging Face `Dataset`'e dönüştürün.

## CLI Komut Doğruluk Ekleri

Workshop, yalnızca şu anda belgelenmiş / stabil Foundry Local CLI komutlarını kullanır.

### Referans Verilen Stabil Komutlar

| Kategori | Komut | Amaç |
|----------|-------|------|
| Çekirdek | `foundry --version` | Yüklü sürümü göster |
| Hizmet | `foundry service start` | Yerel hizmeti başlat (otomatik değilse) |
| Hizmet | `foundry service status` | Hizmet durumunu göster |
| Modeller | `foundry model list` | Katalog / mevcut modelleri listele |
| Modeller | `foundry model download <alias>` | Model ağırlıklarını önbelleğe indir |
| Modeller | `foundry model run <alias>` | Bir modeli yerel olarak başlat (yükle); bir defalık için `--prompt` ile birleştir |
| Modeller | `foundry model unload <alias>` / `foundry model stop <alias>` | Bir modeli bellekten çıkar (destekleniyorsa) |
| Önbellek | `foundry cache list` | Önbelleğe alınmış (indirilmiş) modelleri listele |

### Tek Seferlik İstem Deseni

Eskimiş `model chat` alt komutu yerine şunu kullanın:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Bu, tek bir istem/yanıt döngüsünü yürütür ve ardından çıkar.

### Kaldırılan / Kaçınılan Desenler

| Eskimiş / Belgelenmemiş | Yerine Geçen / Yönerge |
|-------------------------|-----------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Düz `foundry model list` + son etkinlik / günlükler kullanın |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Kıyaslama Python scripti + OS araçları (Görev Yöneticisi / `nvidia-smi`) kullanın |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Kıyaslama ve Telemetri

- Gecikme, p95, token/sn: `samples/session03/benchmark_oss_models.py`
- İlk token gecikmesi (akış): `BENCH_STREAM=1` ayarla
- Kaynak kullanımı: OS monitörleri (Görev Yöneticisi, Aktivite Monitörü, `nvidia-smi`).

Yeni CLI telemetri komutları yukarı akışta stabil hale geldikçe, oturum markdownlarına minimum düzenlemeyle entegre edilebilir.

### Otomatik Lint Koruması

Otomatik bir linter, markdown dosyalarının kod blokları içinde eskimiş CLI desenlerinin yeniden eklenmesini engeller:

Script: `Workshop/scripts/lint_markdown_cli.py`

Kod çitleri içinde eskimiş desenler engellenir.

Önerilen değişiklikler:
| Eskimiş | Yerine Geçen |
|---------|--------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Kıyaslama scripti + sistem araçları |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Yerel olarak çalıştırın:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` her push ve PR'de çalışır.

İsteğe bağlı ön-commit kancası:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Hızlı CLI → SDK Geçiş Tablosu

| Görev | CLI Tek Satır | SDK (Python) Eşdeğeri | Notlar |
|-------|---------------|-----------------------|--------|
| Bir modeli bir kez çalıştır (istem) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK hizmeti ve önbelleği otomatik olarak başlatır |
| Modeli indir (önbelleğe al) | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Yöneticisi, takma ad birden fazla yapıya eşleşiyorsa en iyi varyantı seçer |
| Katalog listele | `foundry model list` | `# use manager for each alias or maintain known list` | CLI toplar; SDK şu anda her takma ad için başlatma gerektirir |
| Önbelleğe alınmış modelleri listele | `foundry cache list` | `manager.list_cached_models()` | Yöneticiyi başlattıktan sonra (herhangi bir takma ad) |
| Uç nokta URL'sini al | (örtük) | `manager.endpoint` | OpenAI uyumlu istemci oluşturmak için kullanılır |
| Bir modeli ısıt | `foundry model run <alias>` ardından ilk istem | `chat_once(alias, messages=[...])` (yardımcı) | Yardımcılar ilk soğuk gecikme ısınmasını ele alır |
| Gecikmeyi ölç | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (veya yeni dışa aktarma scripti) | Tutarlı metrikler için scripti tercih edin |
| Modeli durdur / bellekten çıkar | `foundry model unload <alias>` | (Açık değil – hizmeti / süreci yeniden başlatın) | Workshop akışı için genellikle gerekli değildir |
| Token kullanımını al | (çıktıyı görüntüle) | `resp.usage.total_tokens` | Backend kullanım nesnesi döndürürse sağlanır |

## Kıyaslama Markdown Dışa Aktarımı

`Workshop/scripts/export_benchmark_markdown.py` scriptini kullanarak yeni bir kıyaslama çalıştırın (aynı mantık `samples/session03/benchmark_oss_models.py` ile) ve GitHub uyumlu bir Markdown tablosu ile ham JSON oluşturun.

### Örnek

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Oluşturulan dosyalar:
| Dosya | İçerik |
|-------|--------|
| `benchmark_report.md` | Markdown tablosu + yorumlama ipuçları |
| `benchmark_report.json` | Ham metrik dizisi (karşılaştırma / trend takibi için) |

Destekleniyorsa ilk token gecikmesini dahil etmek için ortamda `BENCH_STREAM=1` ayarlayın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->