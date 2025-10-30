<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T12:36:20+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tr"
}
-->
# Değişiklik Günlüğü

EdgeAI for Beginners'deki tüm önemli değişiklikler burada belgelenmiştir. Bu proje, tarih bazlı girişler ve Keep a Changelog stilini (Eklendi, Değiştirildi, Düzeltildi, Kaldırıldı, Belgeler, Taşındı) kullanır.

## 2025-10-30

### Eklendi - Modül06 AI Ajanları Kapsamlı Geliştirme
- **Microsoft Agent Framework Entegrasyonu** (`Module06/01.IntroduceAgent.md`):
  - Üretime hazır ajan geliştirme için Microsoft Agent Framework hakkında tam bölüm
  - Edge dağıtımı için Foundry Local ile detaylı entegrasyon desenleri
  - Özel SLM modelleriyle çoklu ajan orkestrasyon örnekleri
  - Kaynak yönetimi ve izleme ile kurumsal dağıtım desenleri
  - Edge ajan sistemleri için güvenlik ve uyumluluk özellikleri
  - Gerçek dünya uygulama örnekleri (perakende, sağlık, müşteri hizmetleri)

- **Üretim SLM Ajan Dağıtım Stratejileri**:
  - **Foundry Local**: Kurumsal düzeyde edge AI çalışma zamanı belgeleri, kurulum, yapılandırma ve üretim desenleri
  - **Ollama**: Topluluk odaklı dağıtım için gelişmiş izleme ve model yönetimi
  - **VLLM**: Gelişmiş optimizasyon teknikleri ve kurumsal özelliklere sahip yüksek performanslı çıkarım motoru
  - Üretim dağıtım kontrol listeleri ve tüm platformlar için karşılaştırma tabloları

- **Edge-Optimize Edilmiş SLM Çerçeveleri Geliştirme**:
  - **ONNX Runtime**: Çapraz platform SLM ajan dağıtımı için yeni kapsamlı bölüm
  - Windows, Linux, macOS, iOS ve Android genelinde evrensel dağıtım desenleri
  - Otomatik algılama ile donanım hızlandırma seçenekleri (CPU, GPU, NPU)
  - Üretime hazır özellikler ve ajanlara özel optimizasyonlar
  - Microsoft Agent Framework entegrasyonu ile tam uygulama örnekleri

- **Referanslar ve Ek Okuma**:
  - 100+ otoriter kaynağı içeren kapsamlı kaynak kütüphanesi
  - AI ajanları ve Küçük Dil Modelleri üzerine temel araştırma makaleleri
  - Tüm büyük çerçeveler ve araçlar için resmi belgeler
  - Sektör raporları, pazar analizleri ve teknik karşılaştırmalar
  - Eğitim kaynakları, konferanslar ve topluluk forumları
  - Standartlar, spesifikasyonlar ve uyumluluk çerçeveleri

### Değiştirildi - Modül06 İçerik Modernizasyonu
- **Geliştirilmiş Öğrenme Hedefleri**: Microsoft Agent Framework uzmanlığı ve edge dağıtım yetenekleri eklendi
- **Üretim Odaklılık**: Kavramsaldan uygulama odaklı rehberliğe geçiş, üretim örnekleriyle
- **Kod Örnekleri**: Tüm örnekler modern SDK desenleri ve en iyi uygulamalarla güncellendi
- **Mimari Desenler**: Hiyerarşik ajan mimarileri ve edge-to-cloud koordinasyonu eklendi
- **Performans Optimizasyonu**: Kaynak yönetimi ve otomatik ölçeklendirme önerileriyle geliştirildi

### Belgeler - Modül06 Yapı Geliştirme
- **Kapsamlı Ajan Çerçevesi Kapsamı**: Temel kavramlardan kurumsal dağıtıma kadar
- **Üretim Dağıtım Stratejileri**: Foundry Local, Ollama ve VLLM için tam rehberler
- **Çapraz Platform Optimizasyonu**: Evrensel dağıtım için ONNX Runtime eklendi
- **Kaynak Kütüphanesi**: Sürekli öğrenme ve uygulama için kapsamlı referanslar

### Eklendi - Modül06 Model Context Protocol (MCP) Belge Güncellemesi
- **MCP Tanıtımı Modernizasyonu** (`Module06/03.IntroduceMCP.md`):
  - modelcontextprotocol.io'dan en son MCP spesifikasyonlarıyla güncellendi (2025-06-18 versiyonu)
  - Standartlaştırılmış AI uygulama bağlantıları için resmi USB-C benzetmesi eklendi
  - Resmi iki katmanlı tasarımla mimari bölümü güncellendi (Veri Katmanı + Taşıma Katmanı)
  - Sunucu primitifleri (Araçlar, Kaynaklar, İstekler) ve istemci primitifleri (Örnekleme, Çıkarsama, Günlükleme) ile temel primitifler belgesi geliştirildi

- **Kapsamlı MCP Referansları ve Kaynakları**:
  - **MCP for Beginners** bağlantısı eklendi (https://aka.ms/mcp-for-beginners)
  - Resmi MCP belgeleri ve spesifikasyonları (modelcontextprotocol.io)
  - MCP Inspector ve referans uygulamalar dahil geliştirme kaynakları
  - Teknik standartlar (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Eklendi - Modül04 Qualcomm QNN Entegrasyonu
- **Yeni Bölüm 7: Qualcomm QNN Optimizasyon Paketi** (`Module04/05.QualcommQNN.md`):
  - Qualcomm'un birleşik AI çıkarım çerçevesini kapsayan kapsamlı 400+ satırlık rehber
  - Heterojen bilgi işlem (Hexagon NPU, Adreno GPU, Kryo CPU) hakkında detaylı bilgiler
  - Snapdragon platformları için donanım odaklı optimizasyon ve akıllı iş yükü dağıtımı
  - Mobil dağıtım için gelişmiş kuantizasyon teknikleri (INT8, INT16, karma hassasiyet)
  - Pil gücüyle çalışan cihazlar ve gerçek zamanlı uygulamalar için enerji verimli çıkarım optimizasyonu
  - QNN SDK kurulum ve ortam yapılandırması ile tam kurulum rehberi
  - Pratik örnekler: PyTorch'tan QNN dönüşümü, çoklu arka uç optimizasyonu, bağlam ikili dosya oluşturma
  - Gelişmiş kullanım desenleri: özel arka uç yapılandırması, dinamik kuantizasyon, performans profilleme
  - Kapsamlı sorun giderme bölümü ve topluluk kaynakları

- **Geliştirilmiş Modül04 yapısı**:
  - README.md güncellendi, 7 ilerleyici bölüm eklendi (önceden 6 idi)
  - Qualcomm QNN performans karşılaştırma tablosuna eklendi (5-15x hız artışı, %50-80 bellek tasarrufu)
  - Mobil AI dağıtımı ve enerji optimizasyonu için kapsamlı öğrenme çıktıları eklendi

### Değiştirildi - Modül04 Belge Güncellemeleri
- **Microsoft Olive belge geliştirmesi** (`Module04/03.MicrosoftOlive.md`):
  - 100+ önceden hazırlanmış optimizasyon tariflerini kapsayan kapsamlı "Olive Recipes Repository" bölümü eklendi
  - Desteklenen model aileleri hakkında detaylı bilgiler (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Tarif özelleştirme ve topluluk katkıları için pratik kullanım örnekleri
  - Performans karşılaştırmaları ve entegrasyon rehberliği ile geliştirildi

- **Modül04'te bölüm sıralaması değişikliği**:
  - Apple MLX Bölüm 5'e taşındı (önceden Bölüm 6 idi)
  - İş Akışı Sentezi Bölüm 6'ya taşındı (önceden Bölüm 7 idi)
  - Qualcomm QNN, Bölüm 7 olarak konumlandırıldı (mobil/edge odaklı)
  - Tüm dosya referansları ve navigasyon bağlantıları buna göre güncellendi

### Düzeltildi - Atölye Örnek Doğrulama
- **chat_bootstrap.py doğrulama ve onarım**:
  - Bozuk import ifadesi düzeltildi (`util.util.workshop_utils` → `util.workshop_utils`)
  - Doğru Python modül çözümü için util paketinde eksik `__init__.py` oluşturuldu
  - Gerekli bağımlılıklar (openai, foundry-local-sdk) conda ortamına kuruldu
  - Varsayılan ve özel istemlerle örnek çalıştırma başarıyla doğrulandı
  - Foundry Local hizmeti ve model yükleme (phi-4-mini, CUDA optimizasyonu ile) entegrasyonu onaylandı

### Belgeler - Kapsamlı Rehber Güncellemeleri
- **Modül04 README.md tam yapılandırma**:
  - Qualcomm QNN, OpenVINO, Olive, MLX ile birlikte büyük optimizasyon çerçevesi olarak eklendi
  - Mobil AI dağıtımı ve enerji optimizasyonunu içeren bölüm öğrenme çıktıları güncellendi
  - QNN metrikleri ve mobil/edge kullanım durumları ile performans karşılaştırma tablosu geliştirildi
  - Kurumsal çözümlerden platforma özel optimizasyonlara mantıklı ilerleme korundu

- **Çapraz referanslar ve navigasyon**:
  - Yeni bölüm numaralandırması için tüm dahili bağlantılar ve dosya referansları güncellendi
  - Mobil, masaüstü ve bulut ortamlarını içeren iş akışı sentezi açıklaması geliştirildi
  - Qualcomm geliştirici ekosistemi için kapsamlı kaynak bağlantıları eklendi

## 2025-10-08

### Eklendi - Atölye Kapsamlı Güncelleme
- **Atölye README.md tam yeniden yazımı**:
  - Edge AI değer önerisini açıklayan kapsamlı giriş eklendi (gizlilik, performans, maliyet)
  - Detaylı yetkinliklerle 6 temel öğrenme hedefi oluşturuldu
  - Teslimatlar ve yetkinlik matrisi içeren öğrenme çıktıları tablosu eklendi
  - Endüstriyle ilgili kariyer odaklı beceriler bölümü eklendi
  - Ön koşullar ve 3 adımlı kurulum ile hızlı başlangıç rehberi eklendi
  - Python örnekleri için kaynak tabloları oluşturuldu (8 dosya ve çalışma süreleri)
  - Jupyter not defterleri tablosu eklendi (8 not defteri ve zorluk dereceleri)
  - Belgeler tablosu oluşturuldu (7 ana belge ve "Ne Zaman Kullanılır" rehberi)
  - Farklı beceri seviyeleri için öğrenme yolu önerileri eklendi

- **Atölye doğrulama ve test altyapısı**:
  - `scripts/validate_samples.py` oluşturuldu - Tüm Python örnekleri için kapsamlı doğrulama aracı
  - `scripts/test_samples.py` oluşturuldu - Tüm Python örnekleri için hızlı test çalıştırıcı
  - `scripts/README.md` dosyasına doğrulama belgeleri eklendi

- **Kapsamlı belgeler**:
  - `SAMPLES_UPDATE_SUMMARY.md` oluşturuldu - Tüm iyileştirmeleri kapsayan 400+ satırlık detaylı rehber
  - `UPDATE_COMPLETE.md` oluşturuldu - Güncelleme tamamlanma özeti
  - `QUICK_REFERENCE.md` oluşturuldu - Atölye için hızlı referans kartı

### Değiştirildi - Atölye Python Örnek Modernizasyonu
- **Tüm 8 Python örneği en iyi uygulamalarla güncellendi**:
  - Tüm I/O işlemleri etrafında try-except blokları ile hata yönetimi geliştirildi
  - Tip ipuçları ve kapsamlı docstring'ler eklendi
  - Tutarlı [INFO]/[ERROR]/[RESULT] günlükleme deseni uygulandı
  - Opsiyonel importlar için kurulum ipuçlarıyla koruma sağlandı
  - Tüm örneklerde kullanıcı geri bildirimi geliştirildi

- **session01/chat_bootstrap.py**:
  - Müşteri başlatma işlemi kapsamlı hata mesajlarıyla geliştirildi
  - Akış hatası yönetimi chunk doğrulaması ile iyileştirildi
  - Hizmet kullanılabilirliği için daha iyi istisna yönetimi eklendi

- **session02/rag_pipeline.py**:
  - sentence-transformers için import korumaları eklendi, kurulum ipuçlarıyla
  - Gömme ve üretim işlemleri için hata yönetimi geliştirildi
  - Yapılandırılmış sonuçlarla çıktı formatlama iyileştirildi

- **session02/rag_eval_ragas.py**:
  - Opsiyonel importlar (ragas, datasets) kullanıcı dostu hata mesajlarıyla korundu
  - Değerlendirme metrikleri için hata yönetimi eklendi
  - Değerlendirme sonuçları için çıktı formatlama geliştirildi

- **session03/benchmark_oss_models.py**:
  - Zarif bozulma uygulandı (model hatalarında devam eder)
  - Detaylı ilerleme raporlama ve model başına hata yönetimi eklendi
  - Kapsamlı hata kurtarma ile istatistik hesaplama geliştirildi

- **session04/model_compare.py**:
  - Tip ipuçları eklendi (Tuple dönüş türleri)
  - Yapılandırılmış JSON sonuçlarıyla çıktı formatlama geliştirildi
  - Model başına hata yönetimi ve kurtarma uygulandı

- **session05/agents_orchestrator.py**:
  - Agent.act() kapsamlı docstring'lerle geliştirildi
  - Aşama aşama günlükleme ile pipeline hata yönetimi eklendi
  - Bellek yönetimi ve durum takibi geliştirildi

- **session06/models_router.py**:
  - Tüm yönlendirme bileşenleri için işlev belgeleri geliştirildi
  - route() işlevinde detaylı günlükleme eklendi
  - Yapılandırılmış sonuçlarla test çıktısı geliştirildi

- **session06/models_pipeline.py**:
  - chat() yardımcı işlevine hata yönetimi eklendi
  - pipeline() aşama günlükleme ve ilerleme raporlama ile geliştirildi
  - main() kapsamlı hata kurtarma ile iyileştirildi

### Belgeler - Atölye Belge Geliştirme
- Ana README.md, Atölye bölümünü vurgulayan eller üzerinde öğrenme yoluyla güncellendi
- STUDY_GUIDE.md, Atölye bölümünü içeren kapsamlı şekilde geliştirildi:
  - Öğrenme hedefleri ve çalışma odak alanları
  - Öz değerlendirme soruları
  - Zaman tahminleriyle eller üzerinde egzersizler
  - Yoğun ve yarı zamanlı çalışma için zaman tahsisi
  - İlerleme izleme şablonuna Atölye eklendi
- Zaman tahsisi rehberi 20 saatten 30 saate güncellendi (Atölye dahil)
- Atölye örnek açıklamaları ve öğrenme çıktıları README'ye eklendi

### Düzeltildi
- Atölye örnekleri arasında tutarsız hata yönetimi desenleri giderildi
- Opsiyonel bağımlılık import hataları uygun korumalarla düzeltildi
- Kritik işlevlerde eksik tip ipuçları düzeltildi
- Hata senaryolarında yetersiz kullanıcı geri bildirimi düzeltildi
- Kapsamlı test altyapısıyla doğrulama sorunları düzeltildi

---

## 2025-09-23

### Değiştirildi - Büyük Modül 08 Modernizasyonu
- **Microsoft Foundry-Local depo desenleriyle kapsamlı uyum**:
  - Tüm kod örnekleri modern `FoundryLocalManager` ve OpenAI SDK entegrasyonu kullanacak şekilde güncellendi
  - Eski manuel `requests` çağrıları uygun SDK kullanımıyla değiştirildi
  - Resmi Microsoft belgeleri ve örnekleriyle uygulama desenleri uyumlu hale getirildi

- **05.AIPoweredAgents.md modernizasyonu**:
  - Çoklu ajan orkestrasyonu modern SDK desenleri kullanacak şekilde güncellendi
  - Gelişmiş özelliklerle koordinatör uygulaması geliştirildi (geri bildirim döngüleri, performans izleme)
  - Kapsamlı hata yönetimi ve hizmet sağlık kontrolü eklendi
  - Yerel örneklere uygun referanslar eklendi (`samples/05/multi_agent_orchestration.ipynb`)
  - Eski `functions` yerine modern `tools` parametresi kullanılarak işlev çağrı örnekleri güncellendi
  - İzleme ve istatistik takibi ile üretime hazır desenler eklendi

- **06.ModelsAsTools.md tam yeniden yazımı**:
  - Temel araç kaydı, akıllı model yönlendirici uygulamasıyla değiştirildi
  - Farklı görev türleri için anahtar kelime tabanlı model seçimi eklendi (genel, akıl yürütme, kod, yaratıcı)
  - Esnek model atamasıyla ortam tabanlı yapılandırma entegre edildi
  - Kapsamlı hizmet sağlık izleme ve hata yönetimi ile geliştirildi
  - İstek izleme ve performans takibi ile üretim dağıtım desenleri eklendi
  - Yerel uygulama ile uyumlu hale getirildi (`samples/06/router.py` ve `samples/06/model_router.ipynb`)

- **Belge yapısı iyileştirmeleri**:
  - Modernizasyon ve SDK uyumunu vurgulayan genel bakış bölümleri eklendi
  - Daha iyi okunabilirlik için emojiler ve daha iyi formatlama ile geliştirildi
  - Yerel örnek dosyalara uygun referanslar belgeler boyunca eklendi
  - Üretime hazır uygulama rehberliği ve en iyi uygulamalar dahil edildi

### Eklendi
- Modül 08 dosyalarında modern SDK entegrasyonunu vurgulayan kapsamlı genel bakış bölümleri
- Gelişmiş özellikleri sergileyen mimari öne çıkanlar (
  - `Module08/samples/01`–`06` altında çalıştırılabilir örnekler ve Windows cmd talimatları
    - `01` REST hızlı sohbet (`chat_quickstart.py`)
    - `02` SDK hızlı başlangıç OpenAI/Foundry Local ve Azure OpenAI desteği ile (`sdk_quickstart.py`)
    - `03` CLI listeleme ve kıyaslama (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Çoklu ajan orkestrasyonu (`python -m samples.05.agents.coordinator`)
    - `06` Modelleri Araç Olarak yönlendirme (`router.py`)
- Azure OpenAI desteği, Çevre Değişkeni yapılandırması ile Oturum 2 SDK örneğinde
- Python analiz çözümlemesini iyileştirmek için `.vscode/settings.json` dosyasının `Module08/.venv`'e işaret etmesi
- VS Code/Pylance farkındalığı için `PYTHONPATH` ipucu içeren `.env`

### Değiştirildi
- Varsayılan model, `phi-4-mini` olarak güncellendi; Module 08 belgeleri ve örneklerinde `phi-3.5` referansları kaldırıldı
- Yönlendirici (`Module08/samples/06/router.py`) iyileştirmeleri:
  - Regex ile `foundry service status` üzerinden uç nokta keşfi
  - Başlangıçta `/v1/models` sağlık kontrolü
  - Çevre değişkeni ile yapılandırılabilir model kaydı (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Gereksinimler güncellendi: `Module08/requirements.txt` artık `openai` içeriyor (`requests`, `chainlit` ile birlikte)
- Chainlit örnek rehberi netleştirildi ve sorun giderme eklendi; çalışma alanı ayarları ile ithalat çözümü

### Düzeltildi
- İthalat sorunları çözüldü:
  - Yönlendirici artık var olmayan bir `utils` modülüne bağlı değil; işlevler iç içe yerleştirildi
  - Koordinatör, göreceli ithalat kullanıyor (`from .specialists import ...`) ve modül yolu üzerinden çağrılıyor
  - VS Code/Pylance yapılandırması, `chainlit` ve paket ithalatlarını çözmek için güncellendi
- `STUDY_GUIDE.md` dosyasındaki küçük bir yazım hatası düzeltildi ve Module 08 kapsamı eklendi

### Kaldırıldı
- Kullanılmayan `Module08/infra/obs.py` silindi ve boş `infra/` dizini kaldırıldı; gözlemlenebilirlik desenleri belgelerde isteğe bağlı olarak tutuldu

### Taşındı
- Module 08 demoları, oturum numaralı klasörlerle `Module08/samples` altında birleştirildi
  - Chainlit uygulaması `samples/04`'e taşındı
  - Ajanlar `samples/05`'e taşındı ve paket çözümü için `__init__.py` dosyaları eklendi

### Belgeler
- Module 08 oturum belgeleri ve tüm örnek README'leri Microsoft Learn ve güvenilir satıcı referansları ile zenginleştirildi
- `Module08/README.md` örnekler genel bakışı, yönlendirici yapılandırması ve doğrulama ipuçları ile güncellendi
- `Module07/README.md` Windows Foundry Local bölümü Learn belgelerine göre doğrulandı
- `STUDY_GUIDE.md` güncellendi:
  - Genel bakış, programlar, ilerleme takipçisi için Module 08 eklendi
  - Kapsamlı Referanslar bölümü eklendi (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Tarihsel (özet)
- Kurs mimarisi ve modüller oluşturuldu (Modüller 01–07)
- İçerik modernizasyonu, formatlama standartlaştırması ve ek vaka çalışmaları ile iteratif geliştirme
- Optimizasyon çerçeveleri kapsamı genişletildi (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Yayınlanmamış / Bekleyen (öneriler)
- Foundry Local kullanılabilirliğini doğrulamak için isteğe bağlı örnek başına duman testleri
- Model referanslarını hizalamak için çevirileri gözden geçirme (ör. `phi-4-mini`)
- Takımların çalışma alanı genelinde katılık tercih etmesi durumunda minimal pyright yapılandırması ekleme

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.