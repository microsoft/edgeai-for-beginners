<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:04:54+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "tr"
}
-->
# Podcast Uygulaması

Yapay zeka ajanları kullanarak podcast senaryoları oluşturmak için bir konsol uygulaması.

## Kullanım

```bash
python podcast_app.py
```

## İş Akışı

1. **Hoş Geldiniz** - Uygulama kullanıcıyı selamlar
2. **Konu Girişi** - Kullanıcı podcast için bir konu sağlar
3. **Arama Ajanı** - İlgili bilgileri arar
4. **Senaryo Oluşturma Ajanı** - Podcast senaryosu oluşturur
5. **İnceleme** - Kullanıcı senaryoyu gözden geçirir ve onaylar/redder
6. **Kaydetme** - Onaylanan senaryo `podcast.md` dosyasına kaydedilir

## Gereksinimler

- Python 3.12+
- agent_framework
- 02.WorkflowDevUI içindeki tüm bağımlılıklar

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hatalar veya yanlışlıklar bulunabileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlardan sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->