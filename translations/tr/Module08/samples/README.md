# Modül 08 Örnekleri: Foundry Yerel Geliştirme Kılavuzu

## Genel Bakış

Bu kapsamlı koleksiyon, üretime hazır yapay zeka uygulamaları geliştirmek için hem **Foundry Yerel SDK** hem de **Kabuk Komutları** yaklaşımlarını göstermektedir. Her örnek, temel REST entegrasyonundan gelişmiş çoklu ajan sistemlerine kadar uç yapay zeka geliştirme sürecinin farklı yönlerini sergiler.

## Geliştirme Yaklaşımı: SDK vs Kabuk Komutları

### Foundry Yerel SDK'yı Kullanmanız Gereken Durumlar:

- **Programatik Kontrol**: Ajan yaşam döngüsü, değerlendirme veya dağıtım iş akışları üzerinde tam kontrol ihtiyacı
- **Özel Araçlar**: Foundry Yerel etrafında otomasyon oluşturma (CI/CD entegrasyonu, çoklu ajan orkestrasyonu)
- **Detaylı Erişim**: Ayrıntılı ajan meta verileri, sürüm kontrolü veya değerlendirme çalıştırıcı kontrolü gereksinimi
- **Python Entegrasyonu**: Python ağırlıklı ortamlarda çalışma veya Foundry mantığını daha geniş uygulamalara gömme
- **Kurumsal İş Akışları**: Microsoft referans mimarileriyle uyumlu modüler iş akışları ve tekrarlanabilir değerlendirme süreçleri uygulama

### Kabuk Komutlarını Kullanmanız Gereken Durumlar:

- **Hızlı Test**: Yerel hızlı testler, manuel ajan başlatmaları veya kurulum doğrulama işlemleri
- **CLI Basitliği**: Ajanları başlatma/durdurma, günlükleri kontrol etme veya temel değerlendirmeler için basit CLI işlemleri ihtiyacı
- **Hafif Otomasyon**: Tam SDK entegrasyonu gerektirmeyen basit otomasyon betikleri oluşturma
- **Hızlı Yineleme**: Özellikle kısıtlı ortamlarda veya kaynak grubu düzeyindeki dağıtımlarda hata ayıklama ve geliştirme döngüleri
- **Kurulum ve Doğrulama**: İlk ortam yapılandırması ve hızlı doğrulama görevleri

## En İyi Uygulamalar ve Önerilen İş Akışı

Ajan yaşam döngüsü yönetimi, bağımlılık takibi ve en az ayrıcalıkla tekrarlanabilirlik ilkelerine dayalı olarak:

### Aşama 1: Temel ve Kurulum
1. **Kabuk Komutlarıyla Başlayın**: İlk kurulum ve hızlı doğrulama için
2. **Ortamı Doğrulayın**: CLI araçları ve temel model dağıtımı kullanarak
3. **Bağlantıyı Test Edin**: Basit REST çağrıları ve sağlık kontrolleri ile

### Aşama 2: Geliştirme ve Entegrasyon
1. **SDK'ya Geçiş Yapın**: Ölçeklenebilir ve izlenebilir iş akışları için
2. **Programatik Kontrol Uygulayın**: Karmaşık ajan etkileşimleri için
3. **Özel Araçlar Oluşturun**: Topluluk için hazır şablonlar ve Azure OpenAI entegrasyonu için

### Aşama 3: Üretim ve Ölçeklendirme
1. **Hibrit Yaklaşım**: Operasyonlar için CLI ve uygulama mantığı için SDK'yı birleştirme
2. **Kurumsal Entegrasyon**: İzleme, günlük kaydı ve dağıtım süreçleri ile
3. **Topluluk Katkısı**: Yeniden kullanılabilir şablonlar ve en iyi uygulamalar aracılığıyla

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.