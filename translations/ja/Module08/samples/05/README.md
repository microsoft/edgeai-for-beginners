# セッション5 サンプル: マルチエージェントオーケストレーション

このサンプルは、Foundry LocalのOpenAI互換エンドポイントを使用して、コーディネーター + スペシャリストのパターンを示しています。

## 実行 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## 検証
```cmd
curl http://localhost:8000/v1/models
```

## トラブルシューティング
- VS Codeで`coordinator.py`内の`import specialists`が未解決として表示される場合、モジュールとして実行し、インタープリターが`Module08/.venv`を指していることを確認してください:
	- 実行: `python -m samples.05.agents.coordinator`
	- インタープリターを選択: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## 参考資料
- Foundry Local (学習): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents 概要: https://learn.microsoft.com/azure/ai-services/agents/overview
- 関数呼び出しサンプル (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

