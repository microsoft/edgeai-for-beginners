# Copyright (c) Microsoft. All rights reserved.
"""Ollama-based web search agent for Agent Framework Debug UI.

This agent uses Ollama with web search capabilities.
"""

import os
import asyncio
from typing import Annotated
from datetime import datetime, timezone
from random import randint
from dotenv import load_dotenv

from agent_framework.ollama import OllamaChatClient
from pydantic import Field

load_dotenv()

def web_search(
    query: Annotated[str, Field(description="Search query")],
) -> str:
    """Perform web search using Ollama API."""
    import requests
    
    api_key = os.getenv("OLLAMA_API_KEY")
    if not api_key:
        return "Error: OLLAMA_API_KEY environment variable not set"
    
    url = "https://ollama.com/api/web_search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "query": query
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(response.text)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching web content: {str(e)}"


def setup_agent():
    """Setup the Ollama-based web search agent."""
    # Create Ollama chat client
    client = OllamaChatClient(model_id=os.getenv("OLLAMA_CHAT_MODEL_ID"))
    
    # Agent instance following Agent Framework conventions
    agent = client.create_agent(
        name="SearchAgent",
        instructions="You are my assistant. Answer the questions based on the search engine.",
        tools=[web_search],
    )
    
    return agent

def main():
    """Launch the Ollama web search agent in DevUI."""
    import logging
    from agent_framework.devui import serve

    # Setup logging
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger = logging.getLogger(__name__)
    

    logger.info("Starting Ollama Web Search Agent")
    logger.info("Available at: http://localhost:8090")
    logger.info("Entity ID: SearchAgent")
    logger.info("Note: Make sure OLLAMA_CHAT_MODEL_ID and OLLAMA_API_KEY are set in environment variables")

    # Setup agent
    agent = setup_agent()

    # Launch server with the agent
    serve(entities=[agent], port=8090, auto_open=True, tracing_enabled=True)

if __name__ == "__main__":
    main()
