<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T20:46:04+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "hk"
}
-->
# 工作坊腳本

此目錄包含用於維持工作坊材料質量和一致性的自動化及支援腳本。

## 內容

| 文件 | 用途 |
|------|------|
| `lint_markdown_cli.py` | 檢查 Markdown 代碼塊中是否存在已棄用的 Foundry Local CLI 命令模式。 |
| `export_benchmark_markdown.py` | 執行多模型延遲基準測試並生成 Markdown + JSON 報告。 |

## 1. Markdown CLI 模式檢查工具

`lint_markdown_cli.py` 會掃描所有非翻譯的 `.md` 文件，檢查 **代碼塊內**（``` ... ```）是否存在不允許的 Foundry Local CLI 模式。信息性文字仍可提及已棄用的命令以提供歷史背景。

### 已棄用模式（代碼塊內禁止使用）

檢查工具會阻止使用已棄用的 CLI 模式。請使用現代替代方案。

### 必須替換的內容
| 已棄用 | 替代使用 |
|--------|----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | 基準測試腳本 + 系統工具（`Task Manager`、`nvidia-smi`） |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### 退出代碼
| 代碼 | 含義 |
|------|------|
| 0 | 未檢測到違規 |
| 1 | 發現一個或多個已棄用模式 |

### 本地運行
從倉庫根目錄運行（推薦）：

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### 預提交鉤子（可選）
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
此功能可阻止引入已棄用模式的提交。

### CI 集成
GitHub Action 工作流（`.github/workflows/markdown-cli-lint.yml`）會在每次推送和拉取請求到 `main` 和 `Reactor` 分支時運行檢查工具。失敗的任務必須修復後才能合併。

### 添加新的已棄用模式
1. 打開 `lint_markdown_cli.py`。
2. 在 `DEPRECATED` 列表中添加一個元組 `(regex, suggestion)`。使用原始字符串並在適當位置包含 `\b` 單詞邊界。
3. 本地運行檢查工具以驗證檢測。
4. 提交並推送；CI 會強制執行新規則。

示例添加：
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### 允許解釋性提及
由於僅強制代碼塊，因此您可以在敘述性文字中安全地描述已棄用的命令。如果您*必須*在代碼塊中顯示它們以作對比，請添加一個**不使用**三個反引號的代碼塊（例如，縮排或引用），或重寫為偽形式。

### 跳過特定文件（進階）
如有需要，可將舊版示例包裹在倉庫外的單獨文件中，或在草稿期間重命名為其他擴展名。翻譯副本的有意跳過是自動的（包含 `translations` 的路徑）。

### 疑難排解
| 問題 | 原因 | 解決方案 |
|------|------|----------|
| 檢查工具標記了您更新的行 | 正則表達式過於寬泛 | 使用額外的單詞邊界（`\b`）或錨點縮小模式 |
| CI 失敗但本地通過 | Python 版本不同或未提交的更改 | 本地重新運行，確保工作樹乾淨，檢查工作流的 Python 版本（3.11） |
| 需要臨時繞過 | 緊急修復 | 修復後立即應用；考慮使用臨時分支和後續 PR（避免添加繞過開關） |

### 理由
保持文檔與*當前*穩定的 CLI 表面一致可避免工作坊摩擦，減少學習者的困惑，並通過維護的 Python 腳本集中性能測量，而非使用分散的 CLI 子命令。

---
作為工作坊質量工具鏈的一部分進行維護。如需增強功能（例如自動修復建議或 HTML 報告生成），請開啟問題或提交 PR。

## 2. 示例驗證腳本

`validate_samples.py` 驗證所有 Python 示例文件的語法、導入和最佳實踐合規性。

### 使用方法
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### 檢查內容
- ✅ Python 語法有效性
- ✅ 必需的導入存在
- ✅ 錯誤處理實現（詳細模式）
- ✅ 類型提示使用（詳細模式）
- ✅ 函數文檔字符串（詳細模式）
- ✅ SDK 參考鏈接（詳細模式）

### 環境變量
- `SKIP_IMPORT_CHECK=1` - 跳過導入驗證
- `SKIP_SYNTAX_CHECK=1` - 跳過語法驗證

### 退出代碼
- `0` - 所有示例通過驗證
- `1` - 一個或多個示例未通過

## 3. 示例測試運行器

`test_samples.py` 對所有示例進行煙霧測試，以驗證它們是否能正常執行。

### 使用方法
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### 先決條件
- Foundry Local 服務正在運行：`foundry service start`
- 模型已加載：`foundry model run phi-4-mini`
- 依賴已安裝：`pip install -r requirements.txt`

### 測試內容
- ✅ 示例能夠正常執行且無運行時錯誤
- ✅ 生成所需輸出
- ✅ 失敗時正確的錯誤處理
- ✅ 性能（執行時間）

### 環境變量
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - 用於測試的模型
- `TEST_TIMEOUT=30` - 每個示例的超時時間（秒）

### 預期失敗
如果未安裝可選依賴（例如 `ragas`、`sentence-transformers`），某些測試可能會失敗。安裝方法：
```bash
pip install sentence-transformers ragas datasets
```

### 退出代碼
- `0` - 所有測試通過
- `1` - 一個或多個測試失敗

## 4. 基準 Markdown 導出器

腳本：`export_benchmark_markdown.py`

生成一組模型的可重現性能表。

### 使用方法
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### 輸出
| 文件 | 描述 |
|------|------|
| `benchmark_report.md` | Markdown 表格（平均值、p95、每秒 token 數、可選首 token） |
| `benchmark_report.json` | 用於差異和歷史記錄的原始指標數據 |

### 選項
| 標誌 | 描述 | 預設值 |
|------|------|--------|
| `--models` | 逗號分隔的模型別名 | （必需） |
| `--prompt` | 每輪使用的提示 | （必需） |
| `--rounds` | 每個模型的測試輪數 | 3 |
| `--output` | Markdown 輸出文件 | `benchmark_report.md` |
| `--json` | JSON 輸出文件 | `benchmark_report.json` |
| `--fail-on-empty` | 如果所有基準測試失敗則非零退出 | 關閉 |

環境變量 `BENCH_STREAM=1` 可添加首 token 延遲測量。

### 注意事項
- 重用 `workshop_utils` 以保持模型啟動和緩存的一致性。
- 如果從其他工作目錄運行，腳本會嘗試路徑回退以定位 `workshop_utils`。
- GPU 比較：運行一次，通過 CLI 配置啟用加速，重新運行並對 JSON 進行差異分析。

---

**免責聲明**：  
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋承擔責任。