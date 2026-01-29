# Oturum 6 Örneği: Araç Olarak Modeller

Bu örnek, kullanıcı istemine göre bir model seçen ve Foundry Local’ın OpenAI uyumlu uç noktasını çağıran minimal bir yönlendirici + araç kaydı uygular.

## Dosyalar
- `router.py`: basit kayıt ve sezgisel yönlendirme; uç nokta keşfi + sağlık kontrolü.

## Çalıştırma (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Notlar
- Yönlendirici, `general`, `reasoning` ve `code` araçları arasında seçim yapmak için basit anahtar kelime sezgilerini kullanır ve başlangıçta `/v1/models` yazdırır.
- Ortam değişkenleri ile yapılandırın:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## Referanslar
- Foundry Local (Öğren): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Çıkarım SDK'ları ile entegrasyon: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.