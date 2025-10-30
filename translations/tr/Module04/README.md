<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e8d157e0a282083a1e1c7bb5dda28646",
  "translation_date": "2025-10-30T12:41:19+00:00",
  "source_file": "Module04/README.md",
  "language_code": "tr"
}
-->
# Bölüm 04: Model Format Dönüşümü ve Kuantizasyon - Bölüm Genel Bakış

EdgeAI'nin yükselişi, kaynakları sınırlı cihazlarda gelişmiş makine öğrenimi yeteneklerini dağıtmak için model format dönüşümü ve kuantizasyonu önemli teknolojiler haline getirdi. Bu kapsamlı bölüm, kenar dağıtım senaryoları için modelleri anlamak, uygulamak ve optimize etmek konusunda eksiksiz bir rehber sunar.

## 📚 Bölüm Yapısı ve Öğrenme Yolu

Bu bölüm, kenar bilişim için model optimizasyonunu anlamak için birbiri üzerine inşa edilen yedi bölümden oluşmaktadır:

---

## [Bölüm 1: Model Format Dönüşümü ve Kuantizasyon Temelleri](./01.Introduce.md)

### 🎯 Genel Bakış
Bu temel bölüm, kenar bilişim ortamlarında model optimizasyonu için teorik çerçeveyi oluşturur ve 1-bit ile 8-bit hassasiyet seviyeleri arasındaki kuantizasyon sınırlarını ve ana format dönüşüm stratejilerini kapsar.

**Ana Konular:**
- Hassasiyet sınıflandırma çerçevesi (ultra düşük, düşük, orta hassasiyet)
- GGUF ve ONNX formatlarının avantajları ve kullanım alanları
- Operasyonel verimlilik ve dağıtım esnekliği için kuantizasyonun faydaları
- Performans karşılaştırmaları ve bellek kullanım analizleri

**Öğrenme Çıktıları:**
- Kuantizasyon sınırlarını ve sınıflandırmalarını anlamak
- Uygun format dönüşüm tekniklerini belirlemek
- Kenar dağıtımı için gelişmiş optimizasyon stratejilerini öğrenmek

---

## [Bölüm 2: Llama.cpp Uygulama Rehberi](./02.Llamacpp.md)

### 🎯 Genel Bakış
Llama.cpp'nin uygulanması için kapsamlı bir rehber; bu güçlü C++ çerçevesi, çeşitli donanım yapılandırmalarında minimal kurulumla verimli Büyük Dil Modeli çıkarımı sağlar.

**Ana Konular:**
- Windows, macOS ve Linux platformlarında kurulum
- GGUF format dönüşümü ve çeşitli kuantizasyon seviyeleri (Q2_K'den Q8_0'a)
- CUDA, Metal, OpenCL ve Vulkan ile donanım hızlandırma
- Python entegrasyonu ve üretim dağıtım stratejileri

**Öğrenme Çıktıları:**
- Çapraz platform kurulumunu ve kaynak koddan derlemeyi öğrenmek
- Model kuantizasyonu ve optimizasyon tekniklerini uygulamak
- REST API entegrasyonu ile sunucu modunda modelleri dağıtmak

---

## [Bölüm 3: Microsoft Olive Optimizasyon Paketi](./03.MicrosoftOlive.md)

### 🎯 Genel Bakış
Microsoft Olive'nin keşfi; bu donanım odaklı model optimizasyon aracı, çeşitli donanım platformlarında kurumsal düzeyde model dağıtımı için tasarlanmış 40'tan fazla yerleşik optimizasyon bileşeni sunar.

**Ana Konular:**
- Dinamik ve statik kuantizasyon ile otomatik optimizasyon özellikleri
- CPU, GPU ve NPU dağıtımı için donanım odaklı zeka
- Popüler model desteği (Llama, Phi, Qwen, Gemma) kutudan çıktığı gibi
- Azure ML ile kurumsal entegrasyon ve üretim iş akışları

**Öğrenme Çıktıları:**
- Çeşitli model mimarileri için otomatik optimizasyonu kullanmak
- Çapraz platform dağıtım stratejilerini uygulamak
- Kurumsal düzeyde optimizasyon iş akışları oluşturmak

---

## [Bölüm 4: OpenVINO Araç Takımı Optimizasyon Paketi](./04.openvino.md)

### 🎯 Genel Bakış
Intel'in OpenVINO araç takımı, bulut, şirket içi ve kenar ortamlarında performanslı AI çözümleri dağıtmak için gelişmiş Sinir Ağı Sıkıştırma Çerçevesi (NNCF) yetenekleriyle açık kaynaklı bir platform olarak kapsamlı bir şekilde incelenir.

**Ana Konular:**
- Donanım hızlandırma ile çapraz platform dağıtımı (CPU, GPU, VPU, AI hızlandırıcılar)
- Gelişmiş kuantizasyon ve budama için Sinir Ağı Sıkıştırma Çerçevesi (NNCF)
- OpenVINO GenAI ile büyük dil modeli optimizasyonu ve dağıtımı
- Kurumsal düzeyde model sunucu yetenekleri ve ölçeklenebilir dağıtım stratejileri

**Öğrenme Çıktıları:**
- OpenVINO model dönüşümü ve optimizasyon iş akışlarını öğrenmek
- NNCF ile gelişmiş kuantizasyon tekniklerini uygulamak
- Model sunucu ile optimize edilmiş modelleri çeşitli donanım platformlarında dağıtmak

---

## [Bölüm 5: Apple MLX Çerçevesi Derinlemesine İnceleme](./05.AppleMLX.md)

### 🎯 Genel Bakış
Apple MLX'in kapsamlı bir şekilde ele alınması; bu devrim niteliğindeki çerçeve, Apple Silicon üzerinde verimli makine öğrenimi için özel olarak tasarlanmıştır ve Büyük Dil Modeli yetenekleri ve yerel dağıtım üzerine odaklanır.

**Ana Konular:**
- Birleşik bellek mimarisi avantajları ve Metal Performans Shader'ları
- LLaMA, Mistral, Phi-3, Qwen ve Code Llama modelleri desteği
- Verimli model özelleştirme için LoRA ince ayarı
- Hugging Face entegrasyonu ve kuantizasyon desteği (4-bit ve 8-bit)

**Öğrenme Çıktıları:**
- Apple Silicon optimizasyonunu LLM dağıtımı için öğrenmek
- İnce ayar ve model özelleştirme tekniklerini uygulamak
- Gelişmiş gizlilik özellikleriyle kurumsal AI uygulamaları oluşturmak

---

## [Bölüm 6: Edge AI Geliştirme İş Akışı Sentezi](./06.workflow-synthesis.md)

### 🎯 Genel Bakış
Tüm optimizasyon çerçevelerinin birleşik iş akışlarına, karar matrislerine ve mobil, masaüstü ve bulut ortamları dahil olmak üzere çeşitli platformlar ve kullanım durumları için üretime hazır Edge AI dağıtımına yönelik en iyi uygulamalara kapsamlı bir sentezi.

**Ana Konular:**
- Birden fazla optimizasyon çerçevesini entegre eden birleşik iş akışı mimarisi
- Çerçeve seçimi karar ağaçları ve performans ödünleşimi analizi
- Üretim hazır doğrulama ve kapsamlı dağıtım stratejileri
- Gelişen donanım ve model mimarileri için geleceğe yönelik stratejiler

**Öğrenme Çıktıları:**
- Gereksinimler ve kısıtlamalara dayalı sistematik çerçeve seçimini öğrenmek
- Kapsamlı izleme ile üretim düzeyinde Edge AI iş akışları uygulamak
- Gelişen teknolojiler ve gereksinimlerle uyumlu iş akışları tasarlamak

---

## [Bölüm 7: Qualcomm QNN Optimizasyon Paketi](./07.QualcommQNN.md)

### 🎯 Genel Bakış
Qualcomm QNN'nin kapsamlı bir şekilde incelenmesi; bu birleşik AI çıkarım çerçevesi, Qualcomm'un heterojen hesaplama mimarisinden maksimum performans ve enerji verimliliği sağlamak için Hexagon NPU, Adreno GPU ve Kryo CPU'yu kullanır.

**Ana Konular:**
- NPU, GPU ve CPU'ya birleşik erişim ile heterojen hesaplama
- Snapdragon platformları için akıllı iş yükü dağıtımı ile donanım odaklı optimizasyon
- Mobil dağıtım için gelişmiş kuantizasyon teknikleri (INT8, INT16, karma hassasiyet)
- Pil gücüyle çalışan cihazlar ve gerçek zamanlı uygulamalar için enerji verimli çıkarım

**Öğrenme Çıktıları:**
- Mobil AI dağıtımı için Qualcomm donanım hızlandırmayı öğrenmek
- Kenar bilişim için enerji verimli optimizasyon stratejilerini uygulamak
- Qualcomm ekosisteminde üretime hazır modelleri optimal performansla dağıtmak

---

## 🎯 Bölüm Öğrenme Çıktıları

Bu kapsamlı bölümü tamamladıktan sonra okuyucular şunları başaracaktır:

### **Teknik Uzmanlık**
- Kuantizasyon sınırlarını ve pratik uygulamalarını derinlemesine anlamak
- Birden fazla optimizasyon çerçevesiyle uygulamalı deneyim
- Kenar bilişim ortamları için üretim dağıtım becerileri

### **Stratejik Anlayış**
- Donanım odaklı optimizasyon seçimi yetenekleri
- Performans ödünleşimleri hakkında bilinçli karar verme
- Kurumsal düzeyde dağıtım ve izleme stratejileri

### **Performans Karşılaştırmaları**

| Çerçeve    | Kuantizasyon | Bellek Kullanımı | Hız Artışı | Kullanım Durumu                |
|------------|--------------|------------------|------------|--------------------------------|
| Llama.cpp  | Q4_K_M       | ~4GB            | 2-3x       | Çapraz platform dağıtımı       |
| Olive      | INT4         | %60-75 azalma   | 2-6x       | Kurumsal iş akışları           |
| OpenVINO   | INT8/INT4    | %50-75 azalma   | 2-5x       | Intel donanım optimizasyonu    |
| QNN        | INT8/INT4    | %50-80 azalma   | 5-15x      | Qualcomm mobil/kenar          |
| MLX        | 4-bit        | ~4GB            | 2-4x       | Apple Silicon optimizasyonu    |

## 🚀 Sonraki Adımlar ve İleri Uygulamalar

Bu bölüm, aşağıdaki konular için eksiksiz bir temel sağlar:
- Belirli alanlar için özel model geliştirme
- Kenar AI optimizasyonunda araştırma
- Ticari AI uygulama geliştirme
- Büyük ölçekli kurumsal kenar AI dağıtımları

Bu yedi bölümden elde edilen bilgiler, hızla gelişen kenar AI model optimizasyonu ve dağıtımı alanında gezinmek için kapsamlı bir araç seti sunar.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.