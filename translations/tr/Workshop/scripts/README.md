# Atölye Betikleri

Bu dizin, Atölye materyalleri arasında kalite ve tutarlılığı sağlamak için kullanılan otomasyon ve destek betiklerini içerir.

## İçerik

| Dosya | Amaç |
|-------|------|
| `lint_markdown_cli.py` | Markdown kod bloklarını, eski Foundry Local CLI komut desenlerini engellemek için kontrol eder. |
| `export_benchmark_markdown.py` | Çoklu model gecikme benchmark'ını çalıştırır ve Markdown + JSON raporları oluşturur. |

## 1. Markdown CLI Desen Kontrolü

`lint_markdown_cli.py`, çeviri olmayan `.md` dosyalarını **kod blokları içinde** (``` ... ```) yasaklanmış Foundry Local CLI desenleri için tarar. Bilgilendirici metinler, tarihi bağlam için eski komutlardan bahsedebilir.

### Eski Desenler (Kod Blokları İçinde Engellenir)

Kontrol betiği, eski CLI desenlerini engeller. Bunun yerine modern alternatifleri kullanın.

### Gerekli Değişiklikler
| Eski | Bunun Yerine Kullan |
|------|----------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark betiği + sistem araçları (`Görev Yöneticisi`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Çıkış Kodları
| Kod | Anlamı |
|-----|--------|
| 0 | Hiçbir ihlal tespit edilmedi |
| 1 | Bir veya daha fazla eski desen bulundu |

### Yerel Çalıştırma
Depo kökünden (önerilir):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Önceden Taahhüt Kancası (Opsiyonel)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Bu, eski desenler ekleyen taahhütleri engeller.

### CI Entegrasyonu
Bir GitHub Action iş akışı (`.github/workflows/markdown-cli-lint.yml`), `main` ve `Reactor` dallarına yapılan her push ve pull request'te kontrol betiğini çalıştırır. Başarısız işler birleştirilmeden önce düzeltilmelidir.

### Yeni Eski Desenler Eklemek
1. `lint_markdown_cli.py` dosyasını açın.
2. `DEPRECATED` listesine `(regex, suggestion)` şeklinde bir tuple ekleyin. Ham string kullanın ve uygun yerlerde `\b` kelime sınırlarını dahil edin.
3. Tespiti doğrulamak için kontrol betiğini yerel olarak çalıştırın.
4. Taahhüt edin ve push yapın; CI yeni kuralı zorlayacaktır.

Örnek ekleme:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Açıklayıcı Bahisler İzin Verme
Sadece kod blokları zorunlu olduğu için, eski komutları anlatı metninde güvenle açıklayabilirsiniz. Eğer bir çit içinde göstermeniz *gerekirse*, üçlü tırnak işareti **olmayan** bir çit bloğu ekleyin (örneğin, girintili veya alıntı) ya da sahte bir forma yeniden yazın.

### Belirli Dosyaları Atlamak (İleri Düzey)
Gerekirse, eski örnekleri depo dışındaki ayrı bir dosyada saklayın veya taslak oluştururken farklı bir uzantıyla yeniden adlandırın. Çeviri kopyaları için kasıtlı atlamalar otomatik olarak yapılır (`translations` içeren yollar).

### Sorun Giderme
| Sorun | Sebep | Çözüm |
|-------|-------|-------|
| Kontrol betiği güncellediğiniz bir satırı işaretliyor | Regex çok geniş | Ek kelime sınırı (`\b`) veya sabitleyicilerle deseni daraltın |
| CI başarısız ama yerel geçiyor | Farklı Python sürümü veya taahhüt edilmemiş değişiklikler | Yerel olarak yeniden çalıştırın, temiz çalışma ağacını sağlayın, iş akışı Python sürümünü kontrol edin (3.11) |
| Geçici olarak atlamak gerekiyor | Acil düzeltme | Düzeltmeyi hemen uygulayın; geçici bir dal ve takip eden PR kullanmayı düşünün (atlama anahtarları eklemekten kaçının) |

### Gerekçe
Belgeleri *güncel* kararlı CLI yüzeyiyle uyumlu tutmak, atölye sürtüşmesini önler, öğrenenlerin kafa karışıklığını azaltır ve performans ölçümünü Python betikleri üzerinden merkezi hale getirir, CLI alt komutlarının sapmasını önler.

---
Atölye kalite araç zincirinin bir parçası olarak korunmaktadır. Geliştirmeler (örneğin, otomatik düzeltme önerileri veya HTML rapor oluşturma) için bir sorun açın veya bir PR gönderin.

## 2. Örnek Doğrulama Betiği

`validate_samples.py`, tüm Python örnek dosyalarını sözdizimi, importlar ve en iyi uygulama uyumluluğu açısından doğrular.

### Kullanım
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### Kontrol Ettikleri
- ✅ Python sözdizimi geçerliliği
- ✅ Gerekli importlar mevcut
- ✅ Hata işleme uygulaması (ayrıntılı mod)
- ✅ Tip ipuçları kullanımı (ayrıntılı mod)
- ✅ Fonksiyon açıklamaları (ayrıntılı mod)
- ✅ SDK referans bağlantıları (ayrıntılı mod)

### Ortam Değişkenleri
- `SKIP_IMPORT_CHECK=1` - Import doğrulamasını atla
- `SKIP_SYNTAX_CHECK=1` - Sözdizimi doğrulamasını atla

### Çıkış Kodları
- `0` - Tüm örnekler doğrulamayı geçti
- `1` - Bir veya daha fazla örnek başarısız oldu

## 3. Örnek Test Çalıştırıcı

`test_samples.py`, tüm örneklerin hatasız çalışıp çalışmadığını doğrulamak için duman testleri yapar.

### Kullanım
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### Ön Koşullar
- Foundry Local servisi çalışıyor: `foundry service start`
- Modeller yüklü: `foundry model run phi-4-mini`
- Bağımlılıklar yüklü: `pip install -r requirements.txt`

### Test Ettikleri
- ✅ Örnek, çalışma zamanı hatası olmadan çalışabilir
- ✅ Gerekli çıktı üretilir
- ✅ Hata durumunda doğru hata işleme
- ✅ Performans (çalışma süresi)

### Ortam Değişkenleri
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Test için kullanılacak model
- `TEST_TIMEOUT=30` - Örnek başına zaman aşımı süresi (saniye)

### Beklenen Hatalar
Bazı testler, isteğe bağlı bağımlılıklar yüklenmemişse başarısız olabilir (örneğin, `ragas`, `sentence-transformers`). Şu komutla yükleyin:
```bash
pip install sentence-transformers ragas datasets
```

### Çıkış Kodları
- `0` - Tüm testler başarıyla geçti
- `1` - Bir veya daha fazla test başarısız oldu

## 4. Benchmark Markdown İhracatçısı

Betik: `export_benchmark_markdown.py`

Bir dizi model için tekrarlanabilir bir performans tablosu oluşturur.

### Kullanım
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Çıktılar
| Dosya | Açıklama |
|-------|----------|
| `benchmark_report.md` | Markdown tablosu (ortalama, p95, saniye başına token, isteğe bağlı ilk token) |
| `benchmark_report.json` | Fark ve geçmiş için ham metrik dizisi |

### Seçenekler
| Bayrak | Açıklama | Varsayılan |
|-------|----------|-----------|
| `--models` | Virgülle ayrılmış model takma adları | (gerekli) |
| `--prompt` | Her turda kullanılan istem | (gerekli) |
| `--rounds` | Model başına tur sayısı | 3 |
| `--output` | Markdown çıktı dosyası | `benchmark_report.md` |
| `--json` | JSON çıktı dosyası | `benchmark_report.json` |
| `--fail-on-empty` | Tüm benchmark'lar başarısız olursa sıfır olmayan çıkış | kapalı |

Ortam değişkeni `BENCH_STREAM=1`, ilk token gecikme ölçümünü ekler.

### Notlar
- Tutarlı model başlatma ve önbellekleme için `workshop_utils` yeniden kullanılır.
- Farklı bir çalışma dizininden çalıştırılırsa, betik `workshop_utils`'u bulmak için yol yedeklerini dener.
- GPU karşılaştırması için: bir kez çalıştırın, CLI yapılandırması aracılığıyla hızlandırmayı etkinleştirin, yeniden çalıştırın ve JSON'u karşılaştırın.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.