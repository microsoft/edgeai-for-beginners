<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:02:18+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "ja"
}
-->
# Podcastアプリケーション

AIエージェントを使ってポッドキャストのスクリプトを生成するコンソールアプリケーションです。

## 使い方

```bash
python podcast_app.py
```

## ワークフロー

1. **歓迎** - アプリケーションがユーザーに挨拶します
2. **トピック入力** - ユーザーがポッドキャストのトピックを提供します
3. **検索エージェント** - 関連情報を検索します
4. **スクリプト生成エージェント** - ポッドキャストのスクリプトを作成します
5. **レビュー** - ユーザーがスクリプトを確認し、承認または却下します
6. **保存** - 承認されたスクリプトが`podcast.md`に保存されます

## 要件

- Python 3.12+
- agent_framework
- 02.WorkflowDevUIのすべての依存関係

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の言語の文書が正式な情報源として優先されるべきです。重要な情報については、専門の人による翻訳を推奨します。本翻訳の利用に起因するいかなる誤解や誤訳についても当社は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->