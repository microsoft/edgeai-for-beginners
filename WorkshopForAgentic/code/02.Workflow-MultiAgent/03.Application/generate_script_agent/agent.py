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

def setup_gen_script_agent():
    """Setup the Ollama-based web search agent."""
    # Create Ollama chat client
    client = OllamaChatClient(model_id=os.getenv("OLLAMA_CHAT_MODEL_ID"))
    
    # Agent instance following Agent Framework conventions
    agent = client.as_agent(
        name="GenerateScriptAgent",
        instructions="""
        您是我的播客中文脚本生成助手。请根据提供的内容，生成10分钟中文播客脚本。
        播客脚本需要注意由主持人Lucy和专家Ken共同主持。脚本内容根据输入的内容产生，最后输出格式如下：

            Speaker 1: …… 
            Speaker 2: …… 
            Speaker 1: …… 
            Speaker 2: …… 
            Speaker 1: …… 
            Speaker 2: …… 
        """
    )
    
    return agent
