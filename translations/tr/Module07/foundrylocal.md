# Foundry Local Windows ve Mac'te

Bu rehber, Microsoft Foundry Local'ı Windows ve Mac'te nasıl kuracağınızı, çalıştıracağınızı ve entegre edeceğinizi anlatır. Tüm adımlar ve komutlar Microsoft Learn belgelerine göre doğrulanmıştır.

- Başlangıç: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Mimari: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Referansı: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK'ları Entegre Etme: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF Modellerini Derleme (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Yerel vs Bulut: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows'ta Kurulum / Güncelleme

- Kurulum:
```cmd
winget install Microsoft.FoundryLocal
```
- Güncelleme:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Sürüm kontrolü:
```cmd
foundry --version
```
     
**Kurulum / Mac**

**MacOS**: 
Bir terminal açın ve aşağıdaki komutu çalıştırın:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI Temelleri (Üç Kategori)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Servis:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Önbellek:
```cmd
foundry cache --help
foundry cache list
```

Notlar:
- Servis, OpenAI uyumlu bir REST API sunar. Endpoint portu dinamik olarak atanır; bunu keşfetmek için `foundry service status` komutunu kullanın.
- SDK'ları kullanarak kolaylık sağlayabilirsiniz; desteklenen yerlerde endpoint keşfini otomatik olarak hallederler.

## 3) Yerel Endpoint'i Keşfetme (Dinamik Port)

Foundry Local, servis her başlatıldığında dinamik bir port atar:
```cmd
foundry service status
```
Rapor edilen `http://localhost:<PORT>` adresini OpenAI uyumlu yollarla (örneğin, `/v1/chat/completions`) `base_url` olarak kullanın.

## 4) OpenAI Python SDK ile Hızlı Test

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Referanslar:
- SDK Entegrasyonu: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Kendi Modelinizi Getirin (Olive ile Derleme)

Katalogda bulunmayan bir modele ihtiyacınız varsa, Olive kullanarak onu ONNX formatına dönüştürüp Foundry Local için derleyin.

Yüksek seviyeli akış (adımlar için belgeleri inceleyin):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Belgeler:
- BYOM derleme: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Sorun Giderme

- Servis durumu ve logları kontrol etme:
```cmd
foundry service status
foundry service diag
```
- Önbelleği temizleme veya taşıma:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- En son önizlemeye güncelleme:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) İlgili Windows Geliştirici Deneyimi

- Windows yerel vs bulut AI seçenekleri, Foundry Local ve Windows ML dahil:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit ile Foundry Local (sohbet endpoint URL'sini almak için `foundry service status` kullanın):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Sonraki Windows Geliştirici](./windowdeveloper.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.