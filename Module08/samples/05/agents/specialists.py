import os
import requests


foundry_model = os.environ.get("FOUNDRY_MODEL")

if foundry_model:
    from foundry_local import FoundryLocalManager

    # Create a FoundryLocalManager instance. This will start the Foundry
    # Local service if it is not already running and load the specified model.
    manager = FoundryLocalManager(foundry_model)
    model_info = manager.get_model_info(foundry_model)
    MODEL = model_info.id if model_info else foundry_model
    BASE_URL = manager.endpoint
    API_KEY = manager.api_key
else:
    # OpenAI-compatible path
    BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000/v1")
    MODEL = os.environ.get("MODEL", "phi-4-mini")
    API_KEY = os.environ.get("API_KEY", "")

HEADERS = {"Content-Type": "application/json"}
if API_KEY:
    HEADERS["Authorization"] = f"Bearer {API_KEY}"

def chat(messages, max_tokens=300, temperature=0.4):
    r = requests.post(f"{BASE_URL}/chat/completions", json={
        "model": MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }, headers=HEADERS, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

class RetrievalAgent:
    SYSTEM = "You retrieve relevant snippets from knowledge sources based on a query."
    def run(self, query: str) -> str:
        messages = [{"role": "system", "content": self.SYSTEM},
                    {"role": "user", "content": f"Retrieve key facts for: {query}"}]
        return chat(messages)

class ReasoningAgent:
    SYSTEM = "You analyze inputs step by step and produce structured conclusions."
    def run(self, context: str, question: str) -> str:
        messages = [
            {"role": "system", "content": self.SYSTEM},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}\nThink step-by-step and produce a concise answer."}
        ]
        return chat(messages)

class ExecutionAgent:
    SYSTEM = "You transform decisions into actionable steps (JSON with actions)."
    def run(self, decision: str) -> str:
        messages = [
            {"role": "system", "content": self.SYSTEM},
            {"role": "user", "content": f"Turn this decision into 3 executable steps as JSON:\n{decision}"}
        ]
        return chat(messages)
