# Sitzung 5: Schnelle Entwicklung KI-gestützter Agenten mit Foundry Local

## Zusammenfassung

Entwerfen und orchestrieren Sie Multi-Rollen-KI-Agenten mit der latenzarmen und datenschutzfreundlichen Laufzeitumgebung von Foundry Local. Sie definieren Agentenrollen, Speicherstrategien, Muster für Werkzeugaufrufe und Ausführungsgraphen. Die Sitzung führt in Gerüstmuster ein, die Sie mit Chainlit oder LangGraph erweitern können. Das Starterprojekt erweitert die bestehende Agentenarchitektur, um Speicherpersistenz und Bewertungsmechanismen hinzuzufügen.

## Lernziele

- **Rollen definieren**: System-Prompts und Kompetenzgrenzen
- **Speicher implementieren**: Kurzfristig (Konversation), langfristig (Vektor / Datei), temporäre Notizblöcke
- **Workflows strukturieren**: Sequentielle, verzweigte und parallele Agentenschritte
- **Werkzeuge integrieren**: Leichtgewichtige Muster für Werkzeugaufrufe
- **Bewerten**: Grundlegende Nachverfolgung + ergebnisorientierte Bewertung mit Rubriken

## Voraussetzungen

- Sitzungen 1–4 abgeschlossen
- Python mit `foundry-local-sdk`, `openai`, optional `chainlit`
- Lokale Modelle laufen (mindestens `phi-4-mini`)

### Plattformübergreifender Umgebungs-Snippet

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

Falls Agenten von macOS aus gegen einen Remote-Windows-Hostdienst ausgeführt werden:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo-Ablauf (30 Minuten)

### 1. Agentenrollen und Speicher definieren (7 Minuten)

Erstellen Sie `samples/05-agents/agents_core.py`:

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


### 2. CLI-Gerüstmuster (3 Minuten)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Werkzeugaufruf hinzufügen (7 Minuten)

Erweitern Sie mit `samples/05-agents/tools.py`:

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

Ändern Sie `agents_core.py`, um eine einfache Werkzeugsyntax zu ermöglichen: Der Benutzer schreibt `#tool:get_time`, und der Agent erweitert die Werkzeugausgabe in den Kontext vor der Generierung.

### 4. Orchestrierter Workflow (6 Minuten)

Erstellen Sie `samples/05-agents/orchestrator.py`:

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


### 5. Starterprojekt: Erweiterung der `05-agent-architecture` (7 Minuten)

Hinzufügen:
1. Persistente Speicherschicht (z. B. JSON-Zeilenanhang von Konversationen)
2. Einfache Bewertungsrubrik: Platzhalter für Faktizität / Klarheit / Stil
3. Optionales Chainlit-Frontend (zwei Tabs: Konversation & Nachverfolgungen)
4. Optionaler LangGraph-Stil-Zustandsautomat (bei Hinzufügung der Abhängigkeit) für verzweigte Entscheidungen

## Validierungs-Checkliste

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Erwarten Sie strukturierten Pipeline-Ausgang mit Hinweis auf Werkzeuginjektion.

## Übersicht Speicherstrategien

| Ebene | Zweck | Beispiel |
|-------|-------|----------|
| Kurzfristig | Dialogkontinuität | Letzte N Nachrichten |
| Episodisch | Sitzungsrückruf | JSON pro Sitzung |
| Semantisch | Langfristige Abrufbarkeit | Vektorspeicher von Zusammenfassungen |
| Notizblock | Argumentationsschritte | Inline-Kette von Gedanken (privat) |

## Bewertungshooks (Konzeptuell)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Fehlerbehebung

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Wiederholte Antworten | Kontextfenster zu groß/klein | Speicherfensterparameter anpassen |
| Werkzeug nicht aufgerufen | Falsche Syntax | Format `#tool:tool_name` verwenden |
| Langsame Orchestrierung | Mehrere kalte Modelle | Vorab-Warmup-Prompts ausführen |

## Referenzen

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (optionales Konzept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Sitzungsdauer**: 30 Minuten  
**Schwierigkeitsgrad**: Fortgeschritten

## Beispiel-Szenario & Workshop-Zuordnung

| Workshop-Skript | Szenario | Ziel | Beispiel-Prompt |
|-----------------|----------|------|-----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Wissensforschungs-Bot, der executive-freundliche Zusammenfassungen erstellt | Zwei-Agenten-Pipeline (Forschung → redaktionelle Überarbeitung) mit optional unterschiedlichen Modellen | Erklären Sie, warum Edge-Inferenz für Compliance wichtig ist. |
| (Erweitertes) `tools.py` Konzept | Zeit- und Token-Schätzungswerkzeuge hinzufügen | Leichtgewichtiges Werkzeugaufrufmuster demonstrieren | #tool:get_time |

### Szenario-Erzählung
Das Compliance-Dokumentationsteam benötigt schnelle interne Berichte, die aus lokalem Wissen stammen, ohne Entwürfe an Cloud-Dienste zu senden. Ein Forschungsagent sammelt prägnante Faktenpunkte; ein Redaktionsagent überarbeitet für executive Klarheit. Unterschiedliche Modell-Aliase können zugewiesen werden, um Latenz zu optimieren (schnelles SLM) vs stilistische Verfeinerung (größeres Modell nur bei Bedarf).

### Beispiel für Multi-Modell-Umgebung
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Struktur der Nachverfolgung (Optional)
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

Speichern Sie jeden Schritt in einer JSONL-Datei für spätere Bewertungsrubriken.

### Optionale Verbesserungen

| Thema | Verbesserung | Vorteil | Implementierungsskizze |
|-------|-------------|---------|------------------------|
| Multi-Modell-Rollen | Unterschiedliche Modelle pro Agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Spezialisierung & Geschwindigkeit | Alias-Umgebungsvariablen auswählen, `chat_once` mit rollenbasiertem Alias aufrufen |
| Strukturierte Nachverfolgungen | JSON-Nachverfolgung jedes Aktes (Werkzeug, Eingabe, Latenz, Tokens) | Debugging & Bewertung | Dikt zu einer Liste hinzufügen; `.jsonl` am Ende schreiben |
| Speicherpersistenz | Wiederladbarer Dialogkontext | Sitzungsfortsetzung | `Agent.memory` in `sessions/<ts>.json` speichern |
| Werkzeugregister | Dynamische Werkzeugerkennung | Erweiterbarkeit | `TOOLS`-Dikt pflegen & Namen/Beschreibungen introspektieren |
| Wiederholungs- & Backoff-Strategien | Robuste lange Ketten | Reduzierung vorübergehender Fehler | `act` mit try/except + exponentiellem Backoff umwickeln |
| Rubrik-Bewertung | Automatisierte qualitative Labels | Verbesserungen verfolgen | Sekundärer Durchgang, Modell auffordern: "Bewerten Sie Klarheit 1-5" |
| Vektorspeicher | Semantischer Rückruf | Reichhaltiger Langzeitkontext | Zusammenfassungen einbetten, top-k in Systemnachricht abrufen |
| Streaming-Antworten | Schnellere wahrgenommene Antwort | UX-Verbesserung | Streaming verwenden, sobald verfügbar, und partielle Tokens ausgeben |
| Deterministische Tests | Regressionskontrolle | Stabile CI | Mit `temperature=0`, festen Prompt-Samen ausführen |
| Parallele Verzweigung | Schnellere Exploration | Durchsatz | `concurrent.futures` für unabhängige Agentenschritte verwenden |

#### Beispiel für Nachverfolgungsaufzeichnung

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Einfacher Bewertungs-Prompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Speichern Sie (`answer`, `rating`)-Paare, um einen historischen Qualitätsgraphen zu erstellen.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.