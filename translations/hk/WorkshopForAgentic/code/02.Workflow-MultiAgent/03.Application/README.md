<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:01:52+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "hk"
}
-->
# Podcast 應用程式

一個使用 AI 代理生成播客腳本的控制台應用程式。

## 使用方法

```bash
python podcast_app.py
```

## 工作流程

1. **歡迎** - 應用程式向用戶問好
2. **主題輸入** - 用戶提供播客主題
3. **搜尋代理** - 搜尋相關資訊
4. **生成腳本代理** - 創建播客腳本
5. **審核** - 用戶審核並批准/拒絕腳本
6. **保存** - 批准的腳本保存至 `podcast.md`

## 需求

- Python 3.12+
- agent_framework
- 來自 02.WorkflowDevUI 的所有依賴項

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件乃使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應被視為權威來源。對於重要資訊，建議聘請專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->