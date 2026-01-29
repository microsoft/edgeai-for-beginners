# WindowsとMacでFoundry Localを使用する

このガイドでは、WindowsとMacでMicrosoft Foundry Localをインストール、実行、統合する方法を説明します。すべての手順とコマンドはMicrosoft Learnのドキュメントに基づいて検証されています。

- 始める: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- アーキテクチャ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLIリファレンス: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKの統合: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HFモデルのコンパイル (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: ローカル vs クラウド: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windowsでのインストール / アップグレード

- インストール:
```cmd
winget install Microsoft.FoundryLocal
```
- アップグレード:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- バージョン確認:
```cmd
foundry --version
```
     
**インストール / Mac**

**MacOS**: 
ターミナルを開き、以下のコマンドを実行してください:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLIの基本 (3つのカテゴリ)

- モデル:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- サービス:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- キャッシュ:
```cmd
foundry cache --help
foundry cache list
```

注意事項:
- サービスはOpenAI互換のREST APIを公開します。エンドポイントのポートは動的に割り当てられるため、`foundry service status`を使用して確認してください。
- SDKを使用すると便利です。対応している場合、SDKはエンドポイントの自動検出を行います。

## 3) ローカルエンドポイントの確認 (動的ポート)

Foundry Localはサービス開始時に動的ポートを割り当てます:
```cmd
foundry service status
```
報告された`http://localhost:<PORT>`をOpenAI互換のパス（例: `/v1/chat/completions`）とともに`base_url`として使用してください。

## 4) OpenAI Python SDKを使った簡易テスト

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
参考:
- SDK統合: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) 独自モデルの利用 (Oliveでコンパイル)

カタログにないモデルが必要な場合、Oliveを使用してONNX形式にコンパイルし、Foundry Localで使用できます。

概要フロー (手順はドキュメントを参照):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ドキュメント:
- BYOMコンパイル: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) トラブルシューティング

- サービスの状態とログを確認:
```cmd
foundry service status
foundry service diag
```
- キャッシュのクリアまたは移動:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- 最新のプレビュー版に更新:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) 関連するWindows開発者向け情報

- Foundry LocalやWindows MLを含む、WindowsローカルとクラウドAIの選択肢:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI ToolkitとFoundry Local (チャットエンドポイントURLを取得するには`foundry service status`を使用):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[次のWindows開発者](./windowdeveloper.md)

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。