# Bölüm 06: SLM Agentik Sistemler: Kapsamlı Bir Genel Bakış

Yapay zeka dünyası, basit sohbet botlarından Küçük Dil Modelleri (SLM) tarafından desteklenen sofistike AI ajanlarına doğru temel bir dönüşüm geçiriyor. Bu kapsamlı rehber, modern SLM agentik sistemlerinin üç kritik yönünü inceliyor: temel kavramlar ve dağıtım stratejileri, fonksiyon çağırma yetenekleri ve devrim niteliğindeki Model Context Protocol (MCP) entegrasyonu.

## [Bölüm 1: AI Ajanları ve Küçük Dil Modelleri Temelleri](./01.IntroduceAgent.md)

İlk bölüm, AI ajanları ve Küçük Dil Modelleri hakkında temel bir anlayış oluşturuyor ve 2025'i, 2023'teki sohbet botları dönemi ve 2024'teki yardımcı araç patlamasının ardından AI ajanlarının yılı olarak konumlandırıyor. Bu bölüm, **agentik AI sistemlerini** tanıtıyor; bu sistemler düşünür, akıl yürütür, plan yapar, araçlar kullanır ve minimum insan müdahalesiyle görevleri yerine getirir.

### Ele Alınan Temel Kavramlar:
- **Ajan Sınıflandırma Çerçevesi**: Basit refleks ajanlardan öğrenen ajanlara kadar farklı hesaplama senaryoları için kapsamlı bir taksonomi
- **SLM Temelleri**: Küçük Dil Modellerini, tüketici cihazlarında pratik çıkarım yapabilen 10 milyar parametreden az modele sahip sistemler olarak tanımlama
- **Gelişmiş Optimizasyon Stratejileri**: GGUF formatında dağıtım, kuantizasyon teknikleri (Q4_K_M, Q5_K_S, Q8_0) ve Llama.cpp ile Apple MLX gibi uç cihazlara yönelik optimize edilmiş çerçeveler
- **SLM ve LLM Karşılaştırmaları**: SLM'lerle 10-30× maliyet azaltımı sağlanırken, tipik ajan görevlerinin %70-80'inde etkinliğin korunması

Bölüm, Ollama, VLLM ve Microsoft'un uç çözümlerini kullanarak pratik dağıtım stratejileriyle sona eriyor ve SLM'leri maliyet etkin, gizlilik koruyucu agentik AI dağıtımının geleceği olarak konumlandırıyor.

## [Bölüm 2: Küçük Dil Modellerinde Fonksiyon Çağırma](./02.FunctionCalling.md)

İkinci bölüm, statik dil modellerini gerçek dünya ile etkileşim kurabilen dinamik AI ajanlarına dönüştüren mekanizma olan **fonksiyon çağırma yeteneklerini** derinlemesine inceliyor. Bu teknik inceleme, niyet algılamadan yanıt entegrasyonuna kadar tam iş akışını kapsıyor.

### Temel Uygulama Alanları:
- **Sistematik İş Akışı**: Araç entegrasyonu, fonksiyon tanımı, niyet algılama, JSON çıktısı oluşturma ve harici yürütme konularının detaylı incelenmesi
- **Platforma Özgü Uygulamalar**: Ollama ile Phi-4-mini, Qwen3 fonksiyon çağırma ve Microsoft Foundry Local entegrasyonu için kapsamlı rehberler
- **Gelişmiş Örnekler**: Çoklu ajan iş birliği sistemleri, dinamik araç seçimi ve kapsamlı hata yönetimiyle kurumsal entegrasyon desenleri
- **Üretim Düşünceleri**: Hız sınırlama, denetim kaydı, güvenlik önlemleri ve performans optimizasyon stratejileri

Bu bölüm, geliştiricilerin basit API çağrılarından karmaşık çok adımlı kurumsal iş akışlarına kadar her şeyi yönetebilen sağlam fonksiyon çağırma sistemleri oluşturmasını sağlayan hem teorik anlayış hem de pratik uygulama desenleri sunuyor.

## [Bölüm 3: Model Context Protocol (MCP) Entegrasyonu](./03.IntroduceMCP.md)

Son bölüm, dil modellerinin harici araçlar ve sistemlerle nasıl etkileşim kurduğunu standartlaştıran devrim niteliğindeki bir çerçeve olan **Model Context Protocol (MCP)**'yi tanıtıyor. Bu bölüm, MCP'nin iyi tanımlanmış protokoller aracılığıyla AI modelleri ile gerçek dünya arasında nasıl bir köprü oluşturduğunu gösteriyor.

### Entegrasyon Öne Çıkanlar:
- **Protokol Mimarisi**: Uygulama, LLM istemcisi, MCP istemcisi ve araç işleme katmanlarını kapsayan katmanlı sistem tasarımı
- **Çoklu Arka Uç Desteği**: Hem Ollama (yerel geliştirme) hem de vLLM (üretim) arka uçlarını destekleyen esnek uygulama
- **Bağlantı Protokolleri**: Doğrudan işlem iletişimi için STDIO modu ve HTTP tabanlı akış için SSE modu
- **Gerçek Dünya Uygulamaları**: Web otomasyonu, veri işleme ve API entegrasyonu örnekleriyle kapsamlı hata yönetimi

MCP entegrasyonu, SLM'lerin daha küçük parametre sayısını telafi ederek harici yeteneklerle nasıl artırılabileceğini gösteriyor; bu, yerel dağıtımın ve kaynak verimliliğinin avantajlarını korurken gelişmiş işlevsellik sağlıyor.

## Stratejik Çıkarımlar

Bu üç bölüm bir araya geldiğinde, SLM agentik sistemlerini anlamak ve uygulamak için kapsamlı bir çerçeve sunuyor. Temel kavramlardan fonksiyon çağırmaya ve MCP entegrasyonuna kadar olan evrim, demokratikleşmiş AI dağıtımına doğru açık bir yol gösteriyor; burada:

- **Verimlilik ve yetenek** optimize edilmiş küçük modellerle buluşuyor
- **Maliyet etkinliği** yaygın benimsemeyi mümkün kılıyor
- **Standartlaştırılmış protokoller** birlikte çalışabilirliği sağlıyor
- **Yerel dağıtım** gizliliği koruyor ve gecikmeyi azaltıyor

Bu ilerleme, sadece teknolojik bir gelişme değil, aynı zamanda daha erişilebilir, verimli ve pratik AI sistemlerine doğru bir paradigma değişimini temsil ediyor. Bu sistemler, kaynak kısıtlı ortamlarda etkili bir şekilde çalışırken, endüstriler ve uygulamalar genelinde yapay zekadan nasıl faydalandığımızı ve onunla nasıl etkileşim kurduğumuzu dönüştürecek sofistike agentik yetenekler sunuyor.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.