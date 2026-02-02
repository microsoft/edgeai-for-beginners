# セッション6 サンプル: ツールとしてのモデル

このサンプルでは、ユーザープロンプトに基づいてモデルを選択し、Foundry LocalのOpenAI互換エンドポイントを呼び出す、最小限のルーターとツールレジストリを実装します。

## ファイル
- `router.py`: シンプルなレジストリとヒューリスティックルーティング、エンドポイントの検出とヘルスチェック。

## 実行方法 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## 注意事項
- ルーターはシンプルなキーワードヒューリスティックを使用して、`general`、`reasoning`、`code`ツールの間で選択を行い、起動時に`/v1/models`を出力します。
- 環境変数で設定を行います:
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

## 参考資料
- Foundry Local (学習): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- 推論SDKとの統合: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。