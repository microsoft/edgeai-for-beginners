import os
import json
from datetime import datetime, timezone
from random import randint

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL_ID = os.getenv("OPENAI_MODEL_ID")

client = OpenAI(base_url=BASE_URL, api_key=os.getenv("OPENAI_API_KEY", "not-needed"))


def get_weather(location: str) -> str:
    """Get the weather for a given location."""
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    return f"The weather in {location} is {conditions[randint(0, 3)]} with a high of {randint(10, 30)}°C."


def get_time() -> str:
    """Get the current UTC time."""
    current_time = datetime.now(timezone.utc)
    return f"The current UTC time is {current_time.strftime('%Y-%m-%d %H:%M:%S')}."


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location to get the weather for.",
                    }
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_time",
            "description": "Get the current UTC time.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]

TOOL_IMPL = {
    "get_weather": get_weather,
    "get_time": get_time,
}


def run_agent(query: str) -> str:
    messages = [
        {
            "role": "system",
            "content": "You are my assistant. Answer the questions based on the provided context.",
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
    query = "how's the weather like in Seattle?"
    print(f"User: {query}")
    result = run_agent(query)
    print(f"Agent: {result}\n")
