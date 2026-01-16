<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T09:24:28+00:00",
  "source_file": "README.md",
  "language_code": "tr"
}
-->
# Yeni Başlayanlar için EdgeAI


![Kurs kapak resmi](../../translated_images/tr/cover.eb18d1b9605d754b.png)

[![GitHub katkıda bulunanlar](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub sorunları](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub çekme istekleri](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub izleyiciler](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub çatallar](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub yıldızlar](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Bu kaynakları kullanmaya başlamak için şu adımları izleyin:

1. **Depoyu çatallayın**: Tıklayın [![GitHub çatallar](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Depoyu klonlayın**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Azure AI Foundry Discord’a Katılın ve uzmanlar ile diğer geliştiricilerle tanışın**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Çok Dilli Destek

#### GitHub Action ile desteklenir (Otomatik ve Her Zaman Güncel)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arapça](../ar/README.md) | [Bengalce](../bn/README.md) | [Bulgarca](../bg/README.md) | [Birmanca (Myanmar)](../my/README.md) | [Çince (Basitleştirilmiş)](../zh/README.md) | [Çince (Geleneksel, Hong Kong)](../hk/README.md) | [Çince (Geleneksel, Makao)](../mo/README.md) | [Çince (Geleneksel, Tayvan)](../tw/README.md) | [Hırvatça](../hr/README.md) | [Çekçe](../cs/README.md) | [Danca](../da/README.md) | [Felemenkçe](../nl/README.md) | [Estonca](../et/README.md) | [Fince](../fi/README.md) | [Fransızca](../fr/README.md) | [Almanca](../de/README.md) | [Yunanca](../el/README.md) | [İbranice](../he/README.md) | [Hintçe](../hi/README.md) | [Macarca](../hu/README.md) | [Endonezce](../id/README.md) | [İtalyanca](../it/README.md) | [Japonca](../ja/README.md) | [Kannada](../kn/README.md) | [Korece](../ko/README.md) | [Litvanca](../lt/README.md) | [Malayca](../ms/README.md) | [Malayalamca](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalce](../ne/README.md) | [Nijerya Pidgin](../pcm/README.md) | [Norveççe](../no/README.md) | [Farsça (Farsi)](../fa/README.md) | [Lehçe](../pl/README.md) | [Portekizce (Brezilya)](../br/README.md) | [Portekizce (Portekiz)](../pt/README.md) | [Pencapça (Gurmukhi)](../pa/README.md) | [Rumence](../ro/README.md) | [Rusça](../ru/README.md) | [Sırpça (Kiril)](../sr/README.md) | [Slovakça](../sk/README.md) | [Slovence](../sl/README.md) | [İspanyolca](../es/README.md) | [Svahili](../sw/README.md) | [İsveççe](../sv/README.md) | [Tagalogca (Filipince)](../tl/README.md) | [Tamilce](../ta/README.md) | [Telugu](../te/README.md) | [Tayca](../th/README.md) | [Türkçe](./README.md) | [Ukraynaca](../uk/README.md) | [Urduca](../ur/README.md) | [Vietnamca](../vi/README.md)

> **Yerel Olarak Klonlamayı Tercih Ediyor musunuz?**

> Bu depo, indirme boyutunu önemli ölçüde artıran 50+ dil çevirisini içerir. Çeviriler olmadan klonlamak için, seyrek checkout kullanın:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Bu, kursu tamamlamak için ihtiyacınız olan her şeyi çok daha hızlı bir indirme ile size verir.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ek çeviri dillerinin desteklenmesini istiyorsanız, bunlar [burada](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) listelenmiştir**
## Giriş

**Yeni Başlayanlar için EdgeAI'ye** hoş geldiniz – Edge Yapay Zeka'nın dönüştürücü dünyasına kapsamlı yolculuğunuz. Bu kurs güçlü AI yetenekleri ile gerçek dünyada cihazlarda uygulama arasındaki boşluğu kapatır ve verilerin üretildiği ve kararların verilmesi gereken yerlerde AI’nın potansiyelini doğrudan kullanmanızı sağlar.

### Öğrenecekleriniz

Bu kurs sizi temel kavramlardan üretime hazır uygulamalara götürür ve şunları kapsar:
- Kenar dağıtımı için optimize edilmiş **Küçük Dil Modelleri (SLM'ler)**
- Çeşitli platformlarda **donanım farkındalığı ile optimizasyon**
- **Gizliliği koruyan yeteneklerle gerçek zamanlı çıkarım**
- Kurumsal uygulamalar için **üretim dağıtım** stratejileri

### Neden EdgeAI Önemlidir

Edge AI, kritik modern zorlukları ele alan bir paradigma değişimini temsil eder:
- **Gizlilik ve Güvenlik**: Bulut erişimi olmadan hassas verileri yerel olarak işleyin
- **Gerçek Zamanlı Performans**: Zaman kritik uygulamalar için ağ gecikmesini ortadan kaldırır
- **Maliyet Verimliliği**: Bant genişliği ve bulut bilgi işlem giderlerini azaltır
- **Dayanıklı Operasyonlar**: Ağ kesintileri sırasında işlevselliği sürdürür
- **Regülasyonlara Uyum**: Veri egemenliği gereksinimlerini karşılar

### Edge AI

Edge AI, yapay zeka algoritmalarının ve dil modellerinin verinin üretildiği yere yakın donanımda yerel olarak çalıştırılması anlamına gelir, çıkarım için bulut kaynaklarına bağlı değildir. Gecikmeyi azaltır, gizliliği artırır ve gerçek zamanlı karar almayı mümkün kılar.

### Temel İlkeler:
- **Cihazda çıkarım**: Yapay zeka modelleri kenar cihazlarda (telefonlar, yönlendiriciler, mikrodenetleyiciler, endüstriyel PC'ler) çalışır
- **Çevrimdışı yetenek**: Sürekli internet bağlantısı olmadan çalışır
- **Düşük gecikme**: Gerçek zamanlı sistemlere uygun anlık yanıtlar
- **Veri egemenliği**: Hassas verileri yerel tutarak güvenlik ve uyumu artırır

### Küçük Dil Modelleri (SLM'ler)

Phi-4, Mistral-7B ve Gemma gibi SLM'ler, daha büyük LLM’lerin optimize edilmiş versiyonlarıdır—eğitilmiş veya distill edilmiş:
- **Azaltılmış bellek kullanımı**: Sınırlı kenar cihaz belleğinin verimli kullanımı
- **Düşük işlem talebi**: CPU ve kenar GPU performansı için optimize edilmiş
- **Daha hızlı başlatma süreleri**: Yanıt veren uygulamalar için hızlı başlatma

Aşağıdaki sınırlamalara uyarken güçlü NLP yeteneklerini sunarlar:
- **Gömülü sistemler**: Nesnelerin İnterneti cihazları ve endüstriyel kontrolörler
- **Mobil cihazlar**: Çevrimdışı yeteneklere sahip akıllı telefonlar ve tabletler
- **IoT Cihazları**: Sınırlı kaynaklara sahip sensörler ve akıllı cihazlar
- **Kenar sunucuları**: Sınırlı GPU kaynakları ile yerel işleme birimleri
- **Kişisel Bilgisayarlar**: Masaüstü ve dizüstü dağıtım senaryoları

## Kurs Modülleri ve Navigasyon

| Modül | Konu | Odak Alanı | Temel İçerik | Seviye | Süre |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI’ye Giriş](./introduction.md) | Temel ve Bağlam | EdgeAI Genel Bakış • Sektör Uygulamaları • SLM Tanıtımı • Öğrenme Hedefleri | Başlangıç | 1-2 saat |
| [📚 01](../../Module01) | [EdgeAI Temelleri](./Module01/README.md) | Bulut ve Edge AI karşılaştırması | EdgeAI Temelleri • Gerçek Dünya Vaka Çalışmaları • Uygulama Kılavuzu • Kenar Dağıtımı | Başlangıç | 3-4 saat |
| [🧠 02](../../Module02) | [SLM Model Temelleri](./Module02/README.md) | Model aileleri ve mimari | Phi Ailesi • Qwen Ailesi • Gemma Ailesi • BitNET • μModel • Phi-Silica | Başlangıç | 4-5 saat |
| [🚀 03](../../Module03) | [SLM Dağıtım Uygulaması](./Module03/README.md) | Yerel ve bulut dağıtımı | İleri Öğrenim • Yerel Ortam • Bulut Dağıtımı | Orta | 4-5 saat |
| [⚙️ 04](../../Module04) | [Model Optimizasyon Araçları](./Module04/README.md) | Çok platformlu optimizasyon | Giriş • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • İş Akışı Sentezi | Orta | 5-6 saat |
| [🔧 05](../../Module05) | [SLMOps Üretim](./Module05/README.md) | Üretim operasyonları | SLMOps Tanıtımı • Model Distillasyonu • İnce Ayar • Üretim Dağıtımı | İleri | 5-6 saat |
| [🤖 06](../../Module06) | [AI Ajanları ve Fonksiyon Çağrısı](./Module06/README.md) | Ajan çerçeveleri ve MCP | Ajan Tanıtımı • Fonksiyon Çağrısı • Model Bağlam Protokolü | İleri | 4-5 saat |
| [💻 07](../../Module07) | [Platform Uygulaması](./Module07/README.md) | Çok platformlu örnekler | AI Araç Takımı • Foundry Local • Windows Geliştirme | İleri | 3-4 saat |
| [🏭 08](../../Module08) | [Foundry Local Araç Takımı](./Module08/README.md) | Üretime hazır örnekler | Örnek uygulamalar (detaylar aşağıda) | Uzman | 8-10 saat |

### 🏭 **Modül 08: Örnek Uygulamalar**

- [01: REST Chat Hızlı Başlangıç](./Module08/samples/01/README.md)
- [02: OpenAI SDK Entegrasyonu](./Module08/samples/02/README.md)
- [03: Model Keşfi ve Kıyaslama](./Module08/samples/03/README.md)
- [04: Chainlit RAG Uygulaması](./Module08/samples/04/README.md)
- [05: Çoklu Ajan Orkestrasyonu](./Module08/samples/05/README.md)
- [06: Araç Olarak Modeller Yönlendiricisi](./Module08/samples/06/README.md)
- [07: Doğrudan API İstemcisi](./Module08/samples/07/README.md)
- [08: Windows 11 Sohbet Uygulaması](./Module08/samples/08/README.md)
- [09: Gelişmiş Çoklu Ajan Sistemi](./Module08/samples/09/README.md)
- [10: Foundry Araçları Çerçevesi](./Module08/samples/10/README.md)

### 🎓 **Atölye: Uygulamalı Öğrenme Yolu**

Üretime hazır uygulamalarla kapsamlı uygulamalı atölye materyalleri:

- **[Atölye Kılavuzu](./Workshop/Readme.md)** - Tam öğrenme hedefleri, çıktı ve kaynak navigasyonu
- **Python Örnekleri** (6 oturum) - En iyi uygulamalar, hata yönetimi ve kapsamlı dokümantasyon ile güncellendi
- **Jupyter Not Defterleri** (8 interaktif) - Benchmark ve performans izlemeli adım adım öğreticiler
- **Oturum Kılavuzları** - Her atölye oturumu için detaylı markdown rehberleri
- **Doğrulama Araçları** - Kod kalitesini doğrulamak ve hızlı testler çalıştırmak için betikler

**Ne İnşa Edeceksiniz:**
- Akış desteğiyle yerel AI sohbet uygulamaları
- Kalite değerlendirmeli RAG boru hatları (RAGAS)
- Çoklu model kıyaslama ve karşılaştırma araçları
- Çoklu ajan orkestrasyon sistemleri
- Göreve dayalı seçimle akıllı model yönlendirme

### 🎙️ **Agentic için Atölye: Uygulamalı - AI Podcast Stüdyosu**

Başından sona AI destekli bir podcast üretim hattı oluşturun! Bu kapsamlı atölye, fikirleri profesyonel podcast bölümlerine dönüştüren tam kapsamlı çoklu ajan sistemi oluşturmayı öğretir.
**[🎬 AI Podcast Stüdyosu Atölyesine Başlayın](./WorkshopForAgentic/README.md)**

**Göreviniz**: Tamamen kendinizin oluşturacağı AI ajanları tarafından desteklenen "Future Bytes" adlı bir teknoloji podcast'i başlatın. Bulut bağımlılığı yok, API maliyeti yok — her şey yerel olarak makinenizde çalışıyor.

**Bunu Özel Kılan Nedir:**
- **🤖 Gerçek Çoklu Ajan Orkestrasyonu** - Araştıran, yazan ve ses üretimi yapan uzman AI ajanları oluşturun
- **🎯 Tam Üretim Hattı** - Konu seçmeden son podcast ses çıktısına kadar
- **💻 %100 Yerel Kurulum** - Tam gizlilik ve kontrol için Ollama ve yerel modelleri (Qwen-3-8B) kullanır
- **🎤 Metinden Sese Entegrasyonu** - Metinleri doğal konuşmalar gibi çok konuşmacılı diyaloglara dönüştürün
- **✋ İnsan-Onaylı İş Akışları** - Onay kapıları kaliteyi garanti ederken otomasyonu sürdürür

**Üç Perdelik Öğrenme Yolculuğu:**

| Perde | Odak | Temel Beceriler | Süre |
|-------|-------|-----------------|-------|
| **[Perde 1: AI Asistanlarınla Tanış](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | İlk AI ajanınla kurulum | Araç entegrasyonu • Web araması • Problem çözme • Ajanik muhakeme | 2-3 saat |
| **[Perde 2: Üretim Ekibini Kur](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Birden fazla ajanı yönetin | Takım koordinasyonu • Onay iş akışları • DevUI arayüzü • İnsan gözetimi | 3-4 saat |
| **[Perde 3: Podcast’ini Hayata Geçir](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Podcast sesini üret | Metinden sese • Çok konuşmacılı sentez • Uzun form ses • Tam otomasyon | 2-3 saat |

**Kullanılan Teknolojiler:**
- **Microsoft Agent Framework** - Çoklu ajan orkestrasyonu ve koordinasyonu
- **Ollama** - Yerel AI model çalışma zamanı (bulut gerektirmez)
- **Qwen-3-8B** - Ajanik görevler için optimize edilmiş açık kaynak dil modeli
- **Metinden Sese API'leri** - Podcast üretimi için doğal ses sentezi

**Donanım Desteği:**
- ✅ **CPU Modu** - Her modern bilgisayarda çalışır (8GB+ RAM önerilir)
- 🚀 **GPU Hızlandırma** - NVIDIA/AMD GPU'larla önemli ölçüde daha hızlı çıkarım
- ⚡ **NPU Desteği** - Yeni nesil sinir işleme birimi hızlandırması

**Mükemmel Kullanım Alanları:**
- Çoklu ajan AI sistemleri öğrenen geliştiriciler
- AI otomasyonu ve iş akışlarıyla ilgilenen herkes
- AI destekli üretimi keşfeden içerik oluşturucular
- Pratik AI orkestrasyon kalıplarını inceleyen öğrenciler

**İnşa Etmeye Başlayın**: [🎙️ AI Podcast Stüdyosu Atölyesi →](./WorkshopForAgentic/README.md)

### 📊 **Öğrenme Yolu Özeti**
- **Toplam Süre**: 36-45 saat
- **Başlangıç Yolu**: Modüller 01-02 (7-9 saat)  
- **Orta Seviye Yolu**: Modüller 03-04 (9-11 saat)
- **İleri Seviye Yolu**: Modüller 05-07 (12-15 saat)
- **Uzman Yolu**: Modül 08 (8-10 saat)

## Neler İnşa Edeceksiniz

### 🎯 Temel Yetkinlikler
- **Edge AI Mimarisi**: Bulut entegrasyonlu yerel öncelikli AI sistemleri tasarlama
- **Model Optimizasyonu**: Edge dağıtımı için modelleri kuantize ve sıkıştırma (yüzde 85 hız artışı, yüzde 75 boyut azaltma)
- **Çoklu Platform Dağıtımı**: Windows, mobil, gömülü ve bulut-edge hibrit sistemleri
- **Üretim Operasyonları**: Edge AI’yı üretimde izleme, ölçeklendirme ve sürdürme

### 🏗️ Pratik Projeler
- **Foundry Yerel Sohbet Uygulamaları**: Windows 11 yerel uygulaması ile model geçişi
- **Çoklu Ajan Sistemleri**: Karmaşık iş akışları için koordinatör ve uzman ajanlar  
- **RAG Uygulamaları**: Yerel belge işleme ve vektör araması
- **Model Yönlendiriciler**: Görev analizine göre modeller arasında akıllı seçim
- **API Çerçeveleri**: Yayın ve sağlık izlemesi özellikli üretime hazır istemciler
- **Çapraz Platform Araçları**: LangChain/Semantik Kernel entegrasyon kalıpları

### 🏢 Endüstri Uygulamaları
**Üretim** • **Sağlık** • **Otonom Araçlar** • **Akıllı Şehirler** • **Mobil Uygulamalar**

## Hızlı Başlangıç

**Önerilen Öğrenme Yolu** (toplam 20-30 saat):

0. **📖 Giriş** ([Introduction.md](./introduction.md)): EdgeAI temelleri + sektör bağlamı + öğrenme çerçevesi
1. **📚 Temel** (Modüller 01-02): EdgeAI kavramları + SLM model aileleri
2. **⚙️ Optimizasyon** (Modüller 03-04): Dağıtım + kuantizasyon çerçeveleri  
3. **🚀 Üretim** (Modüller 05-06): SLMOps + AI ajanları + fonksiyon çağırma
4. **💻 Uygulama** (Modüller 07-08): Platform örnekleri + Foundry Yerel araç kiti

Her modül teori, uygulamalı egzersizler ve üretime hazır kod örnekleri içerir.

## Kariyer Etkisi

**Teknik Roller**: EdgeAI Çözüm Mimarı • ML Mühendisi (Edge) • IoT AI Geliştiricisi • Mobil AI Geliştiricisi

**Sektörler**: Üretim 4.0 • Sağlık Teknolojisi • Otonom Sistemler • FinTech • Tüketici Elektroniği

**Portföy Projeleri**: Çoklu ajan sistemleri • Üretim RAG uygulamaları • Çapraz platform dağıtımı • Performans optimizasyonu

## Depo Yapısı

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Kurs Öne Çıkanlar

✅ **Aşamalandırılmış Öğrenme**: Teori → Pratik → Üretim dağıtımı  
✅ **Gerçek Vaka İncelemeleri**: Microsoft, Japan Airlines, kurumsal uygulamalar  
✅ **Uygulamalı Örnekler**: 50+ örnek, 10 kapsamlı Foundry Yerel demosu  
✅ **Performans Odaklı**: %85 hız artışı, %75 boyut azalması  
✅ **Çoklu Platform**: Windows, mobil, gömülü, bulut-edge hibrit  
✅ **Üretime Hazır**: İzleme, ölçeklendirme, güvenlik, uyumluluk çerçeveleri

📖 **[Çalışma Rehberi Mevcut](STUDY_GUIDE.md)**: Zaman dağılımı rehberi ve öz-değerlendirme araçlarıyla yapılandırılmış 20 saatlik öğrenme yolu.

---

**EdgeAI, AI dağıtımının geleceğini temsil eder**: yerel öncelikli, gizliliğe saygılı ve verimli. Bu becerileri öğrenerek yeni nesil zeki uygulamalar geliştirin.

## Diğer Kurslar

Ekibimiz başka kurslar da üretiyor! Şunlara göz atın:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Ajanlar
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Üretken AI Serisi
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Temel Öğrenme
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Serisi
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Yardım Alma

Takılırsanız veya AI uygulamaları geliştirme hakkında herhangi bir sorunuz olursa, katılın:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ürün geri bildirimi veya geliştirme sırasında oluşan hatalar için ziyaret edin:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf edilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum farklılıklarından dolayı sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->