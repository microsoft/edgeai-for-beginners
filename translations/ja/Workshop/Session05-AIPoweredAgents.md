# セッション5: Foundry LocalでAIエージェントを迅速に構築

## 概要

Foundry Localの低遅延でプライバシーを保護するランタイムを活用して、複数の役割を持つAIエージェントを設計・オーケストレーションします。エージェントの役割、メモリ戦略、ツール呼び出しパターン、実行グラフを定義します。このセッションでは、ChainlitやLangGraphで拡張可能なスキャフォールディングパターンを紹介します。スタータープロジェクトでは、既存のエージェントアーキテクチャサンプルを拡張し、メモリ永続性と評価フックを追加します。

## 学習目標

- **役割の定義**: システムプロンプトと能力の境界
- **メモリの実装**: 短期（会話）、長期（ベクトル/ファイル）、一時的なスクラッチパッド
- **ワークフローのスキャフォールディング**: 順次、分岐、並列エージェントステップ
- **ツールの統合**: 軽量な関数ツール呼び出しパターン
- **評価**: 基本的なトレース + ルーブリックに基づく結果スコアリング

## 前提条件

- セッション1～4を完了していること
- Python環境に`foundry-local-sdk`、`openai`、オプションで`chainlit`がインストールされていること
- ローカルモデルが稼働していること（最低でも`phi-4-mini`）

### クロスプラットフォーム環境スニペット

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOSからリモートWindowsホストサービスでエージェントを実行する場合:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## デモフロー (30分)

### 1. エージェントの役割とメモリの定義 (7分)

`samples/05-agents/agents_core.py`を作成:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. CLIスキャフォールディングパターン (3分)

```powershell
python samples/05-agents/agents_core.py
```


### 3. ツール呼び出しの追加 (7分)

`samples/05-agents/tools.py`を拡張:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```

`agents_core.py`を修正して簡単なツール構文を許可します。ユーザーが`#tool:get_time`と記述すると、エージェントが生成前にツール出力をコンテキストに展開します。

### 4. オーケストレーションされたワークフロー (6分)

`samples/05-agents/orchestrator.py`を作成:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. スタータープロジェクト: `05-agent-architecture`を拡張 (7分)

追加内容:
1. 永続的なメモリ層（例: JSON行形式で会話を追加）
2. 簡単な評価ルーブリック: 正確性 / 明確性 / スタイルのプレースホルダー
3. オプションのChainlitフロントエンド（2つのタブ: 会話 & トレース）
4. オプションのLangGraphスタイルの状態機械（依存関係を追加する場合）で分岐決定を実現

## 検証チェックリスト

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

ツール注入のメモ付きで構造化されたパイプライン出力を期待します。

## メモリ戦略概要

| 層 | 目的 | 例 |
|----|------|----|
| 短期 | 会話の継続性 | 最後のNメッセージ |
| エピソード | セッションの記憶 | セッションごとのJSON |
| セマンティック | 長期的な検索 | 要約のベクトルストア |
| スクラッチパッド | 推論ステップ | インラインの思考連鎖（非公開） |

## 評価フック (概念)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## トラブルシューティング

| 問題 | 原因 | 解決策 |
|------|------|--------|
| 繰り返しの回答 | コンテキストウィンドウが大きすぎる/小さすぎる | メモリウィンドウパラメータを調整 |
| ツールが呼び出されない | 構文が間違っている | `#tool:tool_name`形式を使用 |
| オーケストレーションが遅い | 複数のコールドモデル | 事前にウォームアッププロンプトを実行 |

## 参考資料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (オプションの概念): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**セッション時間**: 30分  
**難易度**: 上級

## サンプルシナリオとワークショップマッピング

| ワークショップスクリプト | シナリオ | 目的 | 例のプロンプト |
|--------------------------|----------|------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | エグゼクティブ向けの要約を作成する知識リサーチボット | 2エージェントパイプライン（リサーチ → 編集の仕上げ）でオプションで異なるモデルを使用 | エッジ推論がコンプライアンスにおいて重要な理由を説明してください。 |
| (拡張版)`tools.py`の概念 | 時間とトークン推定ツールを追加 | 軽量なツール呼び出しパターンを示す | #tool:get_time |

### シナリオのストーリー
コンプライアンス文書チームは、クラウドサービスにドラフトを送信せずに、ローカル知識から迅速な内部要約を必要としています。リサーチエージェントが簡潔な事実の箇条書きを収集し、編集エージェントがエグゼクティブ向けの明確な文章に書き直します。レイテンシーを最適化するために、異なるモデルエイリアスを割り当てることができます（高速SLM vs 必要に応じた大規模モデルによるスタイルの洗練）。

### サンプルマルチモデル環境
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### トレース構造 (オプション)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

各ステップをJSONLファイルに保存し、後でルーブリック評価を行います。

### オプションの拡張

| テーマ | 拡張 | 利点 | 実装スケッチ |
|-------|------|------|-------------|
| マルチモデル役割 | エージェントごとに異なるモデル (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | 専門性と速度 | エイリアス環境変数を選択し、役割ごとに`chat_once`を呼び出す |
| 構造化トレース | 各アクト(tool,input,latency,tokens)のJSONトレース | デバッグと評価 | 辞書をリストに追加し、終了時に`.jsonl`を書き込む |
| メモリ永続性 | 再ロード可能な対話コンテキスト | セッションの継続性 | `Agent.memory`を`sessions/<ts>.json`にダンプ |
| ツールレジストリ | 動的なツール検出 | 拡張性 | `TOOLS`辞書を維持し、名前/説明をインスペクト |
| リトライとバックオフ | 長いチェーンの堅牢性 | 一時的な失敗を減らす | `act`をtry/except +指数バックオフでラップ |
| ルーブリック評価 | 自動化された質的ラベル | 改善の追跡 | モデルにセカンダリパスを促す: "明確さを1-5で評価してください" |
| ベクトルメモリ | セマンティックリコール | 豊富な長期的コンテキスト | 要約を埋め込み、システムメッセージにトップkを取得 |
| ストリーミング返信 | 速い応答の体感 | UXの改善 | ストリーミングが利用可能になったら使用し、部分的なトークンをフラッシュ |
| 決定論的テスト | 回帰制御 | 安定したCI | `temperature=0`、固定プロンプトシードで実行 |
| 並列分岐 | 迅速な探索 | スループット | 独立したエージェントステップに`concurrent.futures`を使用 |

#### トレース記録例

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### 簡単な評価プロンプト

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

`answer`と`rating`のペアを保存し、履歴的な品質グラフを構築します。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は責任を負いません。