import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL_ID = os.getenv("OPENAI_MODEL_ID")

client = OpenAI(base_url=BASE_URL, api_key=os.getenv("OPENAI_API_KEY", "not-needed"))


def run_reasoning(query: str):
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {
                "role": "system",
                "content": "You are my math teacher. Help the student solve the problems step by step.",
            },
            {"role": "user", "content": query},
        ],
    )

    msg = response.choices[0].message
    # Some OpenAI-compatible servers (e.g. LM Studio, Ollama) expose reasoning
    # as `reasoning_content` on the message. Fall back to message content.
    reasoning = getattr(msg, "reasoning_content", None)
    return reasoning, msg.content


if __name__ == "__main__":
    query = "Explain what the Pythagorean theorem is."
    reasoning, answer = run_reasoning(query)
    if reasoning:
        print("Reasoning:\n", reasoning, "\n")
    print("Answer:\n", answer)
