import os
import json

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL_ID = os.getenv("OPENAI_MODEL_ID")

client = OpenAI(base_url=BASE_URL, api_key=os.getenv("OPENAI_API_KEY", "not-needed"))


def web_search(query: str) -> str:
    api_key = os.getenv("OLLAMA_API_KEY")
    if not api_key:
        return "Error: OLLAMA_API_KEY environment variable not set"

    url = "https://ollama.com/api/web_search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {"query": query}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(response.text)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching web content: {str(e)}"


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for the given query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                },
                "required": ["query"],
            },
        },
    }
]

TOOL_IMPL = {"web_search": web_search}


def run_agent(query: str) -> str:
    messages = [
        {
            "role": "system",
            "content": "You are my assistant. Answer the questions based on the search engine.",
        },
        {"role": "user", "content": query},
    ]

    while True:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=messages,
            tools=TOOLS,
        )
        msg = response.choices[0].message

        if not msg.tool_calls:
            return msg.content or ""

        messages.append(
            {
                "role": "assistant",
                "content": msg.content,
                "tool_calls": [tc.model_dump() for tc in msg.tool_calls],
            }
        )

        for tc in msg.tool_calls:
            args = json.loads(tc.function.arguments or "{}")
            result = TOOL_IMPL[tc.function.name](**args)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": str(result),
                }
            )


if __name__ == "__main__":
    query = "What's ollama?"
    print(f"User: {query}")
    result = run_agent(query)
    print(f"Agent: {result}\n")
