import os
import chainlit as cl
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

@cl.on_chat_start
async def start():
    await cl.Message(content="Welcome to Local RAG Chat!").send()

@cl.on_message
async def main(message: cl.Message):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": message.content}],
        "max_tokens": 300
    }
    r = requests.post(f"{BASE_URL}/chat/completions", json=payload, headers=HEADERS, timeout=60)
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"]
    await cl.Message(content=content).send()

if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    run_chainlit(__file__) 
