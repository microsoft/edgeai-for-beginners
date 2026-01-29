# WebGPU + ONNX Runtime Demo

Bu demo, AI modellerini doğrudan tarayıcıda WebGPU donanım hızlandırması ve ONNX Runtime Web kullanarak çalıştırmayı gösterir.

## Bu Demo Ne Gösteriyor?

- **Tarayıcı Tabanlı AI**: Modelleri tamamen tarayıcıda çalıştırır
- **WebGPU Hızlandırma**: Donanım destekli çıkarım (mümkün olduğunda)
- **Gizlilik Öncelikli**: Veriler cihazınızdan dışarı çıkmaz
- **Kurulum Gerektirmez**: Uyumlu herhangi bir tarayıcıda çalışır
- **Sorunsuz Geri Dönüş**: WebGPU yoksa CPU'ya geçiş yapar

## Gereksinimler

**Tarayıcı Uyumluluğu:**
- WebGPU etkinleştirilmiş Chrome/Edge 113+
- WebGPU durumunu kontrol edin: `chrome://gpu`
- WebGPU'yu etkinleştirin: `chrome://flags/#enable-unsafe-webgpu`

## Demoyu Çalıştırma

### Seçenek 1: Yerel Sunucu (Önerilen)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Seçenek 2: VS Code Live Server

1. VS Code'da "Live Server" uzantısını yükleyin
2. `index.html` dosyasına sağ tıklayın → "Open with Live Server"
3. Demo tarayıcıda otomatik olarak açılır

## Göreceğiniz Şeyler

1. **WebGPU Algılama**: Tarayıcı uyumluluğunu kontrol eder
2. **Model Yükleme**: MNIST sınıflandırıcıyı indirir ve başlatır
3. **Çıkarım Çalıştırma**: Örnek veri üzerinde tahmin yapar
4. **Performans Metrikleri**: Yükleme süresi ve çıkarım hızını gösterir
5. **Sonuç Gösterimi**: Tahmin güveni ve ham çıktılar

## Beklenen Performans

| Çalıştırma Sağlayıcı | Model Yükleme | Çıkarım | Notlar |
|-------------------|------------|-----------|-------|
| **WebGPU** | ~2-5s | ~10-50ms | Donanım hızlandırmalı |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Yazılım geri dönüşü |

## Sorun Giderme

**WebGPU Kullanılamıyor:**
- Chrome/Edge 113+ sürümüne güncelleyin
- `chrome://flags` altında WebGPU'yu etkinleştirin
- GPU sürücülerinizin güncel olduğundan emin olun
- Demo otomatik olarak CPU'ya geçiş yapar

**Yükleme Hataları:**
- HTTP üzerinden sunulduğundan emin olun (file:// değil)
- Model indirme için ağ bağlantısını kontrol edin
- ONNX modelini engelleyen CORS olmadığından emin olun

**Performans Sorunları:**
- WebGPU, CPU'ya göre önemli bir hız artışı sağlar
- İlk çalıştırma model indirme nedeniyle daha yavaş olabilir
- Sonraki çalıştırmalar tarayıcı önbelleğini kullanır

## Foundry Local ile Entegrasyon

Bu WebGPU demosu, Foundry Local ile şu özellikleri gösterir:

- **İstemci tarafı çıkarım** için maksimum gizlilik
- **Çevrimdışı yetenekler** internet olmadığında  
- **Edge dağıtımı** kaynak kısıtlı ortamlar için
- **Hibrit mimariler** yerel ve sunucu çıkarımını birleştirir

Üretim uygulamaları için şunları düşünün:
- Sunucu tarafı çıkarım için Foundry Local kullanın
- İstemci tarafı ön işleme/son işleme için WebGPU kullanın
- Yerel/uzak çıkarım arasında akıllı yönlendirme uygulayın

## Teknik Detaylar

**Kullanılan Model:**
- MNIST rakam sınıflandırıcı (ONNX formatında)
- Girdi: 28x28 gri tonlama görüntüler
- Çıktı: 10 sınıflı olasılık dağılımı
- Boyut: ~500KB (hızlı indirme)

**ONNX Runtime Web:**
- GPU hızlandırma için WebGPU çalıştırma sağlayıcısı
- CPU geri dönüşü için WASM çalıştırma sağlayıcısı
- Otomatik optimizasyon ve grafik optimizasyonu

**Tarayıcı API'leri:**
- Donanım erişimi için WebGPU
- Arka plan işlemleri için Web Workers (gelecekteki geliştirme)
- Verimli hesaplama için WebAssembly

## Sonraki Adımlar

- Özel ONNX modelleriyle deneyin
- Gerçek görüntü yükleme ve sınıflandırma ekleyin
- Daha büyük modeller için akış çıkarımı ekleyin
- Kamera/mikrofon girişleriyle entegrasyon yapın

---

