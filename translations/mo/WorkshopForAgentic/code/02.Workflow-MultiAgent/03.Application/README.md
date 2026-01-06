<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:01:39+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "mo"
}
-->
# Podcast Application

一個使用 AI 代理生成播客腳本的控制台應用程序。

## Usage

```bash
python podcast_app.py
```

## Workflow

1. **Welcome** - 應用程序歡迎用戶
2. **Topic Input** - 用戶提供播客主題
3. **Search Agent** - 搜索相關資訊
4. **Generate Script Agent** - 創建播客腳本
5. **Review** - 用戶審閱並批准/拒絕腳本
6. **Save** - 已批准的腳本保存至 `podcast.md`

## Requirements

- Python 3.12+
- agent_framework
- 所有 02.WorkflowDevUI 的依賴項

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於關鍵資訊，建議採用專業人士嘅人工翻譯。我哋不對因使用此翻譯而引起嘅任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->