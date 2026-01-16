<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:36:41+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "tr"
}
-->
# 🎙️ AI Podcast Stüdyosu Atölyesi

> 🌏 [中文版 (Çince Versiyonu)](translation/zh-cn/README.md)

![logo](../../../translated_images/tr/logo.8711e39dc8257d7b.png)

## Göreviniz

**AI Podcast Stüdyosu'na** hoş geldiniz! Kendi teknoloji podcast'iniz "Future Bytes"ı başlatmak üzeresiniz — ancak işin içinde bir sürpriz var: onu oluşturmak için yapay zeka destekli bir prodüksiyon ekibi kuracaksınız. Sonsuz araştırma, senaryo yazımı ve ses düzenleme saatlerine son. Onun yerine yapay zekanın süper güçleriyle podcast yapımcısı olacaksınız.

## Hikaye

Düşünün: Siz ve arkadaşlarınız en havalı teknoloji trendleri hakkında bir podcast başlatmak istiyorsunuz, ama herkes okul, iş veya hayat telaşında. Ya işin ağır yükünü yapay zeka ajanlarından oluşan bir ekip kursanız? Bir ajan konuları araştırır, başka biri etkileyici senaryolar yazar, bir başkası ise metni doğal sohbetlere dönüştürür. Bilimkurgu gibi mi geliyor? Hadi gerçeğe dönüştürelim.

## Neler Öğreneceksiniz

Bu atölye sonunda şunları bileceksiniz:
- 🤖 Kendi yerel AI modelinizi dağıtmak (API maliyeti yok, bulut bağımlılığı yok!)
- 🔧 Gerçekten birlikte çalışan uzman AI ajanları geliştirmek
- 🎬 Fikirden sese tam bir podcast prodüksiyon hattı yaratmak

## Yolculuğunuz: Üç Perde

![arch](../../../translated_images/tr/arch.5965fe504e4a3a93.png)

İyi bir hikaye gibi, üç perdemiz var. Her biri AI podcast stüdyonuzu parça parça inşa eder:

| Bölüm | Göreviniz | Ne Oluyor | Kazanılan Beceriler |
|---------|-----------|--------------|----------------|
| **Perde 1** | [AI Asistanlarınızla Tanışın](md/01.BuildAIAgentWithSLM.md) | Sohbet edebilen, webde arama yapabilen hatta sorun çözebilen AI ajanları nasıl oluşturacağınızı keşfediyorsunuz. Bu onların hiç uyumayan araştırma görevlileriniz olduğunu düşünün. | 🎯 İlk ajanınızı oluştur<br>🛠️ Ona süper güçler ver (araçlar!)<br>🧠 Düşünmesini öğret<br>🌐 İnternete bağla |
| **Perde 2** | [Prodüksiyon Ekibinizi Kurun](md/02.AIAgentOrchestrationAndWorkflows.md) | İşler şimdi ilginçleşiyor! Gerçek bir podcast takımı gibi birlikte çalışacak çoklu AI ajanlarını koordine edeceksiniz. Biri araştırır, biri yazar, siz onaylarsınız — ekip çalışması hayalleri gerçeğe dönüştürür. | 🎭 Çoklu ajan koordinasyonu<br>🔄 Onay iş akışları geliştir<br>🖥️ DevUI arayüzü ile test et<br>✋ İnsanları kontrol altında tut |
| **Perde 3** | [Podcast'inizi Hayata Geçirin](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Final! Metin senaryolarınızı gerçekçi sesler ve doğal sohbetlerle gerçek podcast sesine dönüştürün. "Future Bytes" podcast'iniz gönderilmeye hazır! | 🎤 Metinden sese sihir<br>👥 Çoklu konuşmacı sesleri<br>⏱️ Uzun biçimli ses<br>🚀 Tam otomasyon |

Her perde yeni yeteneklerin kilidini açar. Cesursanız doğrudan atlayabilirsiniz ama hikayeyi takip etmenizi öneririz!

## Ortam Gereksinimleri

Bu atölye çeşitli donanım ortamlarını destekler:
- **CPU**: Test ve küçük ölçekli kullanım için uygun
- **GPU**: Üretim ortamları için önerilir, çıkarım hızını önemli ölçüde artırır
- **NPU**: Yeni nesil sinir işleme birimi hızlandırmasını destekler

## İhtiyacınız Olanlar

### Yazılım Kontrol Listesi ✅
- **Python 3.10+** (Kodlama diliniz)
- **Ollama** (AI modellerini makinenizde çalıştırır)
- **VS Code** (Kod editörünüz)
- **Python Eklentisi** (VS Code'u daha akıllı yapar)
- **Git** (Kodu almak için)

### Donanım Kontrolü 💻
- **Çalıştırabilir miyim?**: 8GB RAM, 10GB boş alan (çalışır ama yavaş olabilir)
- **İdeal kurulum**: 16GB+ RAM, iyi bir GPU (sorunsuz!)
- **NPU var mı?**: Daha da iyi! Yeni nesil performans açıldı 🚀

## Stüdyonuzu Kurun 🎬

### 1. Adım: Python Güçlendirmesi

Python 3.10 veya daha yenisine sahip olduğunuza emin olun:

```bash
python --version
# Python 3.10.x veya daha yüksek sürüm gösterilmelidir
```

Python yok mu? [python.org](https://python.org)’dan ücretsiz alabilirsiniz!

### 2. Adım: Ollama'yı Edinin (AI Model Koşucunuz)

İşletim sisteminiz için [ollama.ai](https://ollama.ai)’den Ollama’yı indirin. Bu, AI modellerinizi yerel olarak çalıştıran motor gibi düşünün.

Hazır mı kontrol edin:

```bash
ollama --version
```

### 3. Adım: AI Beyninizi İndirin 🧠

Qwen-3-8B modelini indirme zamanı (ilk AI asistanınızı işe almak gibi):

```bash
ollama pull qwen3:8b
```

*Bu birkaç dakika sürebilir. Kahve molası için harika bir zaman! ☕*

### 4. Adım: VS Code'u Kurun

Henüz yoksa [Visual Studio Code](https://code.visualstudio.com/)u kurun. En iyi kod editörüdür (bunu tartışırız 😄).

### 5. Adım: Python Eklentisi

VS Code’da:
1. `Ctrl+Shift+X` (veya Mac’te `Cmd+Shift+X`) tuşlarına basın
2. “Python” arayın
3. Microsoft’un resmi Python eklentisini kurun

### 6. Adım: Hepsi Hazır! 🎉

Gerçekten, hazırsınız. Haydi biraz AI sihri yaratalım!

### 7. Adım: Microsoft Agent Framework ve İlgili Paketleri Yükleyin 📦

Atölye için gerekli tüm bağımlılıkları kurun:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Bu Microsoft Agent Framework ve gereken tüm paketleri yükleyecek. Kahve alın — ilk kurulum birkaç dakika sürebilir! ☕*

## Atölye Talimatları

Detaylı proje yapısı, yapılandırma adımları ve çalıştırma yöntemleri, atölye sırasında adım adım açıklanacaktır.

## Sorun Giderme (Bir Şeyler Ters Gittiğinde) 🔧

### "Aman Tanrım, model indirmesi sonsuza kadar sürüyor!"
**Çözüm**: VPN kullanın veya Ollama'yı yansıyıcı bir kaynakla yapılandırın. Bazen internet bizimle dalga geçer.

### "Bilgisayarım kilitleniyor! Bellek doldu!"
**Çözüm**: Daha küçük bir modele geçin veya `num_ctx` ayarını düşürerek daha az bellek kullanmasını sağlayın. AI'nızı diyet yaptırmak gibi düşünün.

### "GPU ile bunu daha hızlı yapabilir miyim?"
**Çözüm**: Ollama GPU’ları otomatik algılar! Sadece GPU sürücülerinizin güncel olduğundan emin olun. Ücretsiz hız artışı! 🏎️

## Ek Kaynaklar (Meraklılar İçin) 📚

- [Ollama Belgeleri](https://github.com/ollama/ollama) — Yerel AI modellerine derin dalış
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Ajan takımları geliştirmeyi öğrenin
- [Qwen Model Bilgisi](https://qwenlm.github.io/) — AI asistanınızın beyniyle tanışın

## Lisans

MIT Lisansı — Harika şeyler yap, paylaş, dünyayı daha iyi yap! 🌍

## Katkıda Bulunmak İster Misiniz?

Bir hata mı buldunuz? Fikrin mi var? Issue veya PR açın! Topluluk ruhunu seviyoruz. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->