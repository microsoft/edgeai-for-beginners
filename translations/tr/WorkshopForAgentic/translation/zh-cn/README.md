<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:40:26+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "tr"
}
-->
# 🎙️ AI Podcast Stüdyosu Atölyesi

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.tr.png)

## Görevin

**AI Podcast Stüdyosu**na hoş geldin! Kendi teknoloji podcast’in „Geleceğin Baytı“nı başlatmaya hazırlanıyorsun — ama şöyle bir sürpriz var: Bunu oluşturmak için sana yardımcı olacak AI destekli bir yapım ekibi kuracaksın. Sonsuz araştırma, senaryo yazımı ve ses düzenleme derdi artık yok. Bunun yerine, programlama ile AI süper güçlerine sahip bir podcast yapımcısı olacaksın.

## Hikaye Arka Planı

Düşünsene: Sen ve arkadaşların en havalı teknoloji trendleri hakkında bir podcast başlatmak istiyorsunuz ama herkes eğitimde, işte ya da hayatın koşturmacasında. Peki, işlerin yükünü çekmek için bir AI ajan ekibi kursan nasıl olur? Bir ajan araştırma yapar, diğeri çekici senaryolar yazar, bir başkası metni akıcı ve doğal diyaloğa çevirir. Bu bilim kurgu gibi mi geliyor? Haydi gerçeğe dönüştürelim.

## Neler Öğreneceksin

Bu atölyenin sonunda şunları yapabiliyor olacaksın:
- 🤖 Kendi yerel AI modelini dağıtmak (API ücreti yok, bulut bağımlılığı yok!)
- 🔧 Profesyonel AI ajanlardan oluşan gerçek iş birliği ekipleri kurmak
- 🎬 Yaratıcı fikirden sese kadar tam podcast yapım akışı oluşturmak

## Senin Yolculuğun: Üç Perde

Her iyi hikaye gibi bizim de üç perdemiz var. Her perde senin AI podcast stüdyonun katman katman kurulmasını sağlayacak:

| Bölüm | Görevin | Ne Olacak | Açılacak Yetkinlikler |
|---------|-----------|--------------|----------------|
| **Birinci Perde** | [AI Asistanını Tanı](01.BuildAIAgentWithSLM.md) | Sohbet edebilen, internette arama yapabilen ve problem çözebilen AI ajanlar nasıl oluşturulur öğren. Onları hiç uyumayan araştırma stajyerleri gibi düşün. | 🎯 İlk ajanın oluştur<br>🛠️ Ona süper güçler ver (Araçlar!)<br>🧠 Düşünmesini sağla<br>🌐 İnternete bağla |
| **İkinci Perde** | [Yapım Ekibini Kur](02.AIAgentOrchestrationAndWorkflows.md) | Şimdi işler ilginçleşiyor! Birden fazla AI ajanını gerçek bir podcast ekibi gibi birlikte çalıştıracaksın. Biri araştırır, biri yazar, sen onaylarsın — ekip çalışması hayalleri gerçeğe dönüştürür. | 🎭 Çoklu ajanları koordine et<br>🔄 Onay iş akışları oluştur<br>🖥️ DevUI arayüzü ile test et<br>✋ İnsan kontrolünü sürdür |
| **Üçüncü Perde** | [Podcast’ini Hayata Geçir](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Final! Metin senaryonu gerçekçi sesler ve doğal sohbet halinde podcast sesine çevir. „Geleceğin Baytı“ yayına hazır! | 🎤 Metni sese dönüştür<br>👥 Çok konuşmacılı sesler<br>⏱️ Uzun format ses<br>🚀 Tam otomasyon |

Her perde yeni yetenekler kazandırır. Cesaretliysen atlayabilirsin ama sırasıyla gitmeni öneriyoruz!

## Gereksinimler

Atölye farklı donanım ortamlarını destekler:
- **CPU**: Test ve küçük ölçekli kullanım için uygun
- **GPU**: Üretim ortamı için önerilir, çıkarım hızını önemli ölçüde artırır
- **NPU**: Yeni nesil sinir ağı işlemci hızlandırmayı destekler

## İhtiyacın Olanlar

### Yazılım Listesi ✅
- **Python 3.10+** (programlama dilin)
- **Ollama** (makinende AI modeli çalıştırıcı)
- **VS Code** (kod editörün)
- **Python uzantısı** (VS Code’u daha akıllı yapar)
- **Git** (kodu almak için)

### Donanım Kontrolü 💻
- **Çalıştırabilir miyim?**: 8GB RAM, 10GB boş alan (çalışır ama biraz yavaş olabilir)
- **İdeal Konfigürasyon**: 16GB+ RAM, iyi bir GPU (pürüzsüz çalışma!)
- **NPU Var mı?**: Daha da iyi! Yeni nesil performans açılır 🚀

## Stüdyonu Kur 🎬

### Adım 1: Python Güncellemesi

Python 3.10 veya daha güncel bir sürüme sahip olduğundan emin ol:

```bash
python --version
# Python 3.10.x veya daha yeni bir sürüm gösterilmelidir
```

Python yok mu? [python.org](https://python.org) adresinden ücretsiz alabilirsin!

### Adım 2: Ollama’yı Al (AI model koşumcusu)

İşletim sistemine uygun Ollama‘yı [ollama.ai](https://ollama.ai)’den indir. Yerelde AI modeli çalıştıran bir motor gibi düşün.

Hazır mı kontrol et:

```bash
ollama --version
```

### Adım 3: AI Beynini İndir 🧠

Qwen-3-8B modelini şimdi indir (ilk AI asistanını işe alıyormuş gibi):

```bash
ollama pull qwen3:8b
```

*Birkaç dakika sürebilir. Mükemmel kahve molası!☕*

### Adım 4: VS Code Kur

Henüz yapmadıysan, [Visual Studio Code](https://code.visualstudio.com/) al. En iyi kod editörüdür (tartışmaya açık 😄).

### Adım 5: Python Uzantısı Yükle

VS Code’da:
1. `Ctrl+Shift+X` (Mac’de `Cmd+Shift+X`) tuşlarına bas
2. „Python“ ara
3. Microsoft’un resmi Python uzantısını yükle

### Adım 6: Hadi Başlayalım! 🎉

Cidden, hazırsın. Haydi biraz AI sihri yaratalım!

### Adım 7: Microsoft Agent Framework ve Gerekli Paketleri Yükle 📦

Atölyede gereken tüm bağımlılıkları kur:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Microsoft Agent Framework ve tüm gereken paketleri yükleyecek. Kahveni al — ilk kurulum biraz zaman alabilir!☕*

## Atölye Notları

Detaylı proje yapısı, kurulum adımları ve nasıl çalıştırılır atölye boyunca adım adım anlatılacak.

## Sorun Giderme (Bir şeyler yanlış giderse) 🔧

### "Ah, model indirisi çok yavaş!"
**Çözüm**: VPN kullan veya Ollama ayna kaynaklarını ayarla. Bazen internet iş yapmaz.

### "Bilgisayarım donuyor! Bellek yetmiyor!"
**Çözüm**: Daha küçük model kullan veya `num_ctx` ayarını azalt, AI’na diyet yaptırıyorsun.

### "GPU ile hızlandırabilir miyim?"
**Çözüm**: Ollama GPU’yu otomatik algılar! Sadece GPU sürücüsünün güncel olduğundan emin ol. Bedava hız artışı!🏎️

## Ek Kaynaklar (Meraklılar için) 📚

- [Ollama Dokümantasyonu](https://github.com/ollama/ollama) — Yerel AI modeller hakkında detay
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Ajan ekipleri kurmayı öğren
- [Qwen Model Bilgisi](https://qwenlm.github.io/) — AI arkadaşının beynini tanı

## Lisans

MIT Lisansı — Harika şeyler yap, paylaş, dünyayı güzelleştir!🌍

## Katkıda Bulunmak İster misin?

Hata mı buldun? Fikirlerin mi var? Issue veya PR aç! Topluluğu seviyoruz.✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->