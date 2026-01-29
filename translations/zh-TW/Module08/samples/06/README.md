# 第六節範例：模型作為工具

此範例實現了一個簡易的路由器和工具註冊表，根據使用者的提示選擇模型，並調用 Foundry Local 的 OpenAI 兼容端點。

## 文件
- `router.py`：簡單的註冊表和啟發式路由；端點發現和健康檢查。

## 執行 (cmd.exe)
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
- 路由器使用簡單的關鍵字啟發式方法在 `general`、`reasoning` 和 `code` 工具之間進行選擇，並在啟動時打印 `/v1/models`。
- 通過環境變數進行配置：
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

## 參考資料
- Foundry Local (學習)：https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- 與推理 SDK 整合：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。