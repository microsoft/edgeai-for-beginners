<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a988dfc121c969bcc37d9c1a04fcd6c",
  "translation_date": "2025-12-16T00:47:34+00:00",
  "source_file": "Module08/samples/10/README.md",
  "language_code": "kn"
}
-->
# ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಅನ್ನು ಟೂಲ್ಸ್ ಇಂಟಿಗ್ರೇಶನ್ ಆಗಿ

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಅನ್ನು ದೊಡ್ಡ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಕರೆಮಾಡಬಹುದಾದ ಟೂಲ್ಸ್ ಆಗಿ ಸಂಯೋಜಿಸಲು ಸಮಗ್ರ ಫ್ರೇಮ್ವರ್ಕ್, ಟೂಲ್ ಆಧಾರಿತ AI ಇಂಟಿಗ್ರೇಶನ್‌ಗಾಗಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಅಧಿಕೃತ ಮಾದರಿಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ.

## ಅವಲೋಕನ

ಈ ಮಾದರಿ ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಮಾದರಿಗಳನ್ನು ಮರುಬಳಕೆ ಮಾಡಬಹುದಾದ ಟೂಲ್ಸ್ ಆಗಿ ಹೇಗೆ ಬಹಿರಂಗಪಡಿಸಬಹುದು ಮತ್ತು ಅವುಗಳನ್ನು ಇತ್ತೀಚಿನ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು, ವರ್ಕ್‌ಫ್ಲೋಗಳು ಮತ್ತು ಅಭಿವೃದ್ಧಿ ಪರಿಸರಗಳಲ್ಲಿ ಹೇಗೆ ಸಂಯೋಜಿಸಬಹುದು ಎಂಬುದನ್ನು ತೋರಿಸುತ್ತದೆ. ಇದು ಟೂಲ್ ಇಂಟಿಗ್ರೇಶನ್ ಮತ್ತು ಫಂಕ್ಷನ್ ಕರೆಮಾಡುವಿಕೆಗಾಗಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಶಿಫಾರಸು ಮಾಡಿದ ಮಾದರಿಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ.

## ಪ್ರಮುಖ ಕಲ್ಪನೆಗಳು

### 🔧 **ಟೂಲ್-ಪ್ರಥಮ ವಾಸ್ತುಶಿಲ್ಪ**
- ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಮಾದರಿಗಳನ್ನು ಕರೆಮಾಡಬಹುದಾದ ಫಂಕ್ಷನ್‌ಗಳಾಗಿ
- ಮಾನಕೃತ ಟೂಲ್ ಇಂಟರ್ಫೇಸ್ಗಳು ಮತ್ತು ಸ್ಕೀಮಾಗಳು
- ಇತ್ತೀಚಿನ ಕೋಡ್‌ಬೇಸ್‌ಗಳೊಂದಿಗೆ ನಿರಂತರ ಸಂಯೋಜನೆ
- ಪ್ರಕಾರ-ಸುರಕ್ಷಿತ ಟೂಲ್ ವ್ಯಾಖ್ಯಾನಗಳು ಮತ್ತು ಮಾನ್ಯತೆ

### ⚡ **ಫಂಕ್ಷನ್ ಕರೆಮಾಡುವ ಮಾದರಿಗಳು**
- ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಫಂಕ್ಷನ್ ಕರೆಮಾಡುವ ಅನುಷ್ಠಾನ
- OpenAI-ಸಮ್ಮತ ಟೂಲ್ ವ್ಯಾಖ್ಯಾನಗಳು
- ಸ್ವಯಂಚಾಲಿತ ಪ್ಯಾರಾಮೀಟರ್ ಮಾನ್ಯತೆ ಮತ್ತು ಪರಿವರ್ತನೆ
- ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆ ಸ್ವರೂಪೀಕರಣ

### 🔌 **ಇಂಟಿಗ್ರೇಶನ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು**
- **ಲ್ಯಾಂಗ್‌ಚೈನ್ ಇಂಟಿಗ್ರೇಶನ್**: ಸ್ಥಳೀಯ ಲ್ಯಾಂಗ್‌ಚೈನ್ ಟೂಲ್ ಬೆಂಬಲ
- **ಸೆಮ್ಯಾಂಟಿಕ್ ಕರ್ಣಲ್**: ಮೈಕ್ರೋಸಾಫ್ಟ್ ಸೆಮ್ಯಾಂಟಿಕ್ ಕರ್ಣಲ್ ಫಂಕ್ಷನ್‌ಗಳು
- **REST API**: HTTP ಆಧಾರಿತ ಟೂಲ್ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳು
- **CLI ಟೂಲ್ಸ್**: ಕಮಾಂಡ್-ಲೈನ್ ಇಂಟರ್ಫೇಸ್ ಸಂಯೋಜನೆ
- **ಜುಪೈಟರ್ ನೋಟ್ಬುಕ್‌ಗಳು**: ಸಂವಹನಾತ್ಮಕ ಅಭಿವೃದ್ಧಿ ಟೂಲ್ಸ್

### 🎯 **ಬಳಕೆ ಪ್ರಕರಣ ಮಾದರಿಗಳು**
- ಕೋಡ್ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ರಚನೆ ಟೂಲ್ಸ್
- ವಿಷಯ ಪ್ರಕ್ರಿಯೆ ಮತ್ತು ಸಾರಾಂಶ
- ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ದೃಶ್ಯೀಕರಣ
- ಸಂಶೋಧನೆ ಮತ್ತು ಮಾಹಿತಿ ಪಡೆಯುವಿಕೆ
- ನಿರ್ಣಯ ಬೆಂಬಲ ವ್ಯವಸ್ಥೆಗಳು

## ವಾಸ್ತುಶಿಲ್ಪ

```
┌─────────────────────────────────────────────────────────────────┐
│                    Application Layer                            │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │  LangChain  │  │  Semantic   │  │  Custom     │            │
│  │    Tools    │  │   Kernel    │  │    Apps     │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
└─────────────────┬─────────────────┬─────────────────────────────┘
                  │                 │
                  ▼                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Tool Integration Layer                       │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │ Function    │  │   REST      │  │    CLI      │            │
│  │ Registry    │  │  Gateway    │  │  Interface  │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                Microsoft Foundry Local Service                  │
│                                                                 │
│ • Model Management        • Function Calling Support           │
│ • Inference Engine        • Tool Schema Validation             │
│ • Context Handling        • Response Formatting                │
└─────────────────────────────────────────────────────────────────┘
```

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

### ವ್ಯವಸ್ಥೆ ಅಗತ್ಯಗಳು
- **Python**: 3.9+ asyncio ಬೆಂಬಲದೊಂದಿಗೆ
- **Node.js**: v18+ (ಜಾವಾಸ್ಕ್ರಿಪ್ಟ್ ಇಂಟಿಗ್ರೇಶನ್‌ಗಳಿಗೆ)
- **ಮೆಮೊರಿ**: 12GB+ ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ
- **ಸಂಗ್ರಹಣೆ**: ಮಾದರಿಗಳು ಮತ್ತು ಟೂಲ್ಸ್‌ಗಾಗಿ 10GB+

### ಮೂಲ ಅವಲಂಬನೆಗಳು
```bash
pip install foundry-local-sdk openai langchain semantic-kernel fastapi uvicorn typer rich
```

### ಫ್ರೇಮ್ವರ್ಕ್-ನಿರ್ದಿಷ್ಟ ಅವಲಂಬನೆಗಳು
```bash
# ಲಾಂಗ್‌ಚೈನ್ ಏಕೀಕರಣ
pip install langchain-openai langchain-community

# ಸೆಮ್ಯಾಂಟಿಕ್ ಕರ್ಣಲ್ ಏಕೀಕರಣ
pip install semantic-kernel

# ವೆಬ್ ಫ್ರೇಮ್ವರ್ಕ್ ಏಕೀಕರಣ
pip install fastapi uvicorn streamlit gradio

# ಅಭಿವೃದ್ಧಿ ಸಾಧನಗಳು
pip install jupyter ipywidgets
```

## ತ್ವರಿತ ಪ್ರಾರಂಭ

### 1. ಮೂಲ ಟೂಲ್ ರಚನೆ
```python
from foundry_tools import FoundryTool, FoundryToolRegistry

# ಸರಳ ವಿಶ್ಲೇಷಣಾ ಸಾಧನವನ್ನು ರಚಿಸಿ
@FoundryTool(
    name="code_analyzer",
    description="Analyze code quality and suggest improvements",
    model="phi-4-mini"
)
async def analyze_code(code: str, language: str = "python") -> dict:
    """Analyze code and return quality metrics and suggestions."""
    pass

# ಸಾಧನವನ್ನು ನೋಂದಾಯಿಸಿ ಮತ್ತು ಬಳಸಿ
registry = FoundryToolRegistry()
await registry.register(analyze_code)

result = await registry.call("code_analyzer", {
    "code": "def hello(): print('world')",
    "language": "python"
})
```

### 2. ಲ್ಯಾಂಗ್‌ಚೈನ್ ಇಂಟಿಗ್ರೇಶನ್
```python
from langchain.tools import BaseTool
from foundry_tools.langchain import FoundryLangChainTool

# ಲಾಂಗ್‌ಚೈನ್-ಸಮ್ಮತ ಸಾಧನವನ್ನು ರಚಿಸಿ
class CodeAnalyzerTool(FoundryLangChainTool):
    name = "code_analyzer"
    description = "Analyze code quality using Foundry Local"
    model = "phi-4-mini"
    
    async def _arun(self, code: str, language: str = "python") -> str:
        return await self.foundry_call({
            "code": code,
            "language": language
        })

# ಲಾಂಗ್‌ಚೈನ್ ಏಜೆಂಟ್‌ಗಳೊಂದಿಗೆ ಬಳಸಿ
from langchain.agents import initialize_agent, AgentType

tools = [CodeAnalyzerTool()]
agent = initialize_agent(
    tools=tools,
    llm=None,  # ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಅನ್ನು ಬಳಸುತ್ತದೆ
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)
```

### 3. REST API ಇಂಟಿಗ್ರೇಶನ್
```python
from fastapi import FastAPI
from foundry_tools.rest import FoundryRESTEndpoint

app = FastAPI()

# Foundry ಉಪಕರಣಗಳಿಂದ ಸ್ವಯಂಚಾಲಿತವಾಗಿ REST ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ರಚಿಸಿ
foundry_api = FoundryRESTEndpoint()
await foundry_api.register_tool("code_analyzer", analyze_code)

# ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಮೌಂಟ್ ಮಾಡಿ
app.include_router(foundry_api.router, prefix="/foundry/v1")

# HTTP ಮೂಲಕ ಬಳಸಿ
# POST /foundry/v1/code_analyzer
# {
#   "code": "def hello(): print('world')",
#   "language": "python"
# }
```

## ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆ

```
10/
├── README.md                    # This documentation
├── requirements.txt             # Python dependencies
├── foundry_tools/
│   ├── __init__.py             # Package initialization
│   ├── core/
│   │   ├── __init__.py
│   │   ├── tool_base.py        # Base tool implementation
│   │   ├── registry.py         # Tool registry
│   │   ├── validation.py       # Schema validation
│   │   └── client.py           # Foundry Local client
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── langchain.py        # LangChain integration
│   │   ├── semantic_kernel.py  # Semantic Kernel integration
│   │   ├── rest_api.py         # REST API framework
│   │   ├── cli.py              # Command-line interface
│   │   └── jupyter.py          # Jupyter notebook tools
│   ├── frameworks/
│   │   ├── __init__.py
│   │   ├── fastapi_tools.py    # FastAPI integration
│   │   ├── streamlit_tools.py  # Streamlit integration
│   │   ├── gradio_tools.py     # Gradio integration
│   │   └── flask_tools.py      # Flask integration
│   └── tools/
│       ├── __init__.py
│       ├── code_tools.py       # Code analysis tools
│       ├── content_tools.py    # Content processing tools
│       ├── data_tools.py       # Data analysis tools
│       ├── research_tools.py   # Research and retrieval tools
│       └── decision_tools.py   # Decision support tools
├── examples/
│   ├── basic_tools.py          # Simple tool examples
│   ├── langchain_demo.py       # LangChain integration
│   ├── semantic_kernel_demo.py # Semantic Kernel demo
│   ├── rest_api_server.py      # REST API server
│   ├── cli_application.py      # CLI application
│   ├── jupyter_notebook.ipynb  # Interactive notebook
│   ├── streamlit_app.py        # Streamlit application
│   └── production_deployment.py # Production patterns
├── integrations/
│   ├── vscode_extension/       # VS Code extension
│   ├── github_actions/         # CI/CD workflows
│   ├── azure_functions/        # Serverless deployment
│   └── docker_containers/      # Containerization
└── tests/
    ├── test_tools.py           # Tool tests
    ├── test_integrations.py    # Integration tests
    └── test_frameworks.py      # Framework tests
```

## ಮೂಲ ಟೂಲ್ ಮಾದರಿಗಳು

### 1. ಫಂಕ್ಷನ್ ಆಧಾರಿತ ಟೂಲ್ಸ್
```python
from foundry_tools import FoundryTool
from typing import List, Dict, Any

@FoundryTool(
    name="summarize_content",
    description="Summarize long-form content into key points",
    model="phi-4-mini",
    parameters={
        "content": {"type": "string", "description": "Content to summarize"},
        "max_points": {"type": "integer", "description": "Maximum summary points", "default": 5},
        "style": {"type": "string", "description": "Summary style", "enum": ["bullet", "paragraph", "outline"]}
    }
)
async def summarize_content(
    content: str, 
    max_points: int = 5, 
    style: str = "bullet"
) -> Dict[str, Any]:
    """Summarize content using Foundry Local model."""
    
    # ಡೆಕೊರೇಟರ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ:
    # - ಪ್ಯಾರಾಮೀಟರ್ ಮಾನ್ಯತೆ
    # - ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಕ್ಲೈಂಟ್ ಸೆಟಪ್
    # - ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಲಾಗಿಂಗ್
    # - ಪ್ರತಿಕ್ರಿಯೆ ಸ್ವರೂಪೀಕರಣ
    
    system_prompt = f"""
    Summarize the following content into {max_points} key points.
    Use {style} format for the summary.
    """
    
    # ಇದು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಫೌಂಡ್ರಿ ಲೋಕಲ್‌ಗೆ ಮಾರ್ಗದರ್ಶನ ಮಾಡಲಾಗುತ್ತದೆ
    return {
        "summary": "Generated summary here...",
        "points": max_points,
        "style": style,
        "word_count": len(content.split())
    }
```

### 2. ಕ್ಲಾಸ್ ಆಧಾರಿತ ಟೂಲ್ಸ್
```python
from foundry_tools.core import BaseFoundryTool

class CodeAnalysisTool(BaseFoundryTool):
    """Advanced code analysis tool with state management."""
    
    name = "advanced_code_analyzer"
    description = "Perform comprehensive code analysis"
    model = "phi-4-mini"
    
    def __init__(self):
        super().__init__()
        self.analysis_cache = {}
        self.supported_languages = ["python", "javascript", "typescript", "java", "csharp"]
    
    async def validate_input(self, **kwargs) -> bool:
        """Custom input validation."""
        language = kwargs.get("language", "").lower()
        return language in self.supported_languages
    
    async def execute(self, code: str, language: str, analysis_type: str = "full") -> Dict[str, Any]:
        """Execute code analysis."""
        
        # ಕ್ಯಾಶೆ ಪರಿಶೀಲಿಸಿ
        cache_key = f"{hash(code)}_{language}_{analysis_type}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        # ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಬಳಸಿ ವಿಶ್ಲೇಷಣೆ ಮಾಡಿ
        result = await self.foundry_call({
            "system_prompt": f"Analyze this {language} code for {analysis_type} analysis",
            "user_prompt": f"Code to analyze:\n\n```{language}\n{code}\n```",
            "max_tokens": 1000
        })
        
        # ಫಲಿತಾಂಶವನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ ಮತ್ತು ಕ್ಯಾಶೆ ಮಾಡಿ
        analysis_result = self.process_analysis_result(result, analysis_type)
        self.analysis_cache[cache_key] = analysis_result
        
        return analysis_result
    
    def process_analysis_result(self, raw_result: str, analysis_type: str) -> Dict[str, Any]:
        """Process the raw analysis result into structured data."""
        # ಇಲ್ಲಿ ಅನುಷ್ಠಾನ
        pass
```

### 3. ಸ್ಟ್ರೀಮಿಂಗ್ ಟೂಲ್ಸ್
```python
from foundry_tools import StreamingFoundryTool
from typing import AsyncGenerator

@StreamingFoundryTool(
    name="code_generator",
    description="Generate code with real-time streaming",
    model="qwen2.5-coder-0.5b"
)
async def generate_code(
    specification: str,
    language: str = "python",
    include_tests: bool = False
) -> AsyncGenerator[Dict[str, Any], None]:
    """Generate code with streaming responses."""
    
    # ಮೆಟಾಡೇಟಾವನ್ನು ಮೊದಲು ನೀಡಿರಿ
    yield {
        "type": "metadata",
        "language": language,
        "include_tests": include_tests,
        "estimated_lines": 50
    }
    
    # ಸ್ಟ್ರೀಮ್ ಕೋಡ್ ಉತ್ಪಾದನೆ
    async for chunk in foundry_stream({
        "prompt": f"Generate {language} code: {specification}",
        "stream": True
    }):
        yield {
            "type": "code_chunk",
            "content": chunk.content,
            "complete": chunk.finish_reason is not None
        }
    
    # ಅಂತಿಮ ಫಲಿತಾಂಶವನ್ನು ನೀಡಿರಿ
    if include_tests:
        async for test_chunk in foundry_stream({
            "prompt": f"Generate unit tests for the above {language} code",
            "stream": True
        }):
            yield {
                "type": "test_chunk", 
                "content": test_chunk.content,
                "complete": test_chunk.finish_reason is not None
            }
```

## ಇಂಟಿಗ್ರೇಶನ್ ಉದಾಹರಣೆಗಳು

### ಲ್ಯಾಂಗ್‌ಚೈನ್ ಇಂಟಿಗ್ರೇಶನ್
```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate
from foundry_tools.langchain import FoundryToolkit

# ಫೌಂಡ್ರಿ ಚಾಲಿತ ಟೂಲ್ಕಿಟ್ ರಚಿಸಿ
toolkit = FoundryToolkit()
toolkit.add_tool("code_analyzer", model="phi-4-mini")
toolkit.add_tool("content_summarizer", model="qwen2.5-0.5b") 
toolkit.add_tool("research_assistant", model="phi-3.5-mini")

# ಫೌಂಡ್ರಿ ಟೂಲ್ಸ್‌ನೊಂದಿಗೆ ಏಜೆಂಟ್ ರಚಿಸಿ
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to Foundry Local tools."),
    ("user", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

agent = create_openai_functions_agent(
    llm=toolkit.get_llm(),  # LLM ಆಗಿ ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಅನ್ನು ಬಳಸುತ್ತದೆ
    tools=toolkit.get_tools(),
    prompt=prompt
)

agent_executor = AgentExecutor(agent=agent, tools=toolkit.get_tools())

# ಏಜೆಂಟ್ ಅನ್ನು ಬಳಸಿ
result = await agent_executor.ainvoke({
    "input": "Analyze this Python code and summarize any issues you find"
})
```

### ಸೆಮ್ಯಾಂಟಿಕ್ ಕರ್ಣಲ್ ಇಂಟಿಗ್ರೇಶನ್
```python
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from foundry_tools.semantic_kernel import FoundryKernelPlugin

# ಫೌಂಡ್ರಿ ಲೋಕಲ್‌ನೊಂದಿಗೆ ಕರ್ಣಲ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
kernel = Kernel()

# ಚಾಟ್ ಸೇವೆಯಾಗಿ ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಅನ್ನು ಸೇರಿಸಿ
foundry_service = OpenAIChatCompletion(
    service_id="foundry_chat",
    ai_model_id="phi-4-mini",
    api_key="not-needed",
    base_url="http://localhost:5273/v1"
)
kernel.add_service(foundry_service)

# ಫೌಂಡ್ರಿ ಪ್ಲಗಿನ್ ಅನ್ನು ರಚಿಸಿ ಮತ್ತು ಸೇರಿಸಿ
foundry_plugin = FoundryKernelPlugin()
foundry_plugin.add_function("analyze_code", model="phi-4-mini")
foundry_plugin.add_function("summarize_text", model="qwen2.5-0.5b")

kernel.add_plugin(foundry_plugin, plugin_name="foundry_tools")

# ಸೆಮ್ಯಾಂಟಿಕ್ ಕರ್ಣಲ್ ವರ್ಕ್‌ಫ್ಲೋಗಳಲ್ಲಿ ಬಳಸಿ
result = await kernel.invoke(
    "foundry_tools", 
    "analyze_code",
    code="def hello(): print('world')",
    language="python"
)
```

### ಫಾಸ್ಟ್‌ಎಪಿಐ ಇಂಟಿಗ್ರೇಶನ್
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from foundry_tools.rest import FoundryRESTFramework

app = FastAPI(title="Foundry Local Tools API")

# ಫೌಂಡ್ರಿ REST ಫ್ರೇಮ್ವರ್ಕ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
foundry_framework = FoundryRESTFramework()

# ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನೋಂದಣಿ ಮಾಡಿ
await foundry_framework.auto_register_tools([
    "code_analyzer",
    "content_summarizer", 
    "data_processor",
    "research_assistant"
])

# ಫೌಂಡ್ರಿ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಮೌಂಟ್ ಮಾಡಿ
app.include_router(
    foundry_framework.get_router(),
    prefix="/api/v1/foundry",
    tags=["foundry-tools"]
)

# ಫೌಂಡ್ರಿ ಸಾಧನಗಳನ್ನು ಬಳಸಿ ಕಸ್ಟಮ್ ಎಂಡ್‌ಪಾಯಿಂಟ್
class AnalysisRequest(BaseModel):
    code: str
    language: str = "python"

@app.post("/api/v1/analyze")
async def analyze_code_endpoint(request: AnalysisRequest):
    try:
        result = await foundry_framework.call_tool(
            "code_analyzer",
            code=request.code,
            language=request.language
        )
        return {"success": True, "analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ ಎಂಡ್‌ಪಾಯಿಂಟ್
@app.get("/api/v1/health")
async def health_check():
    status = await foundry_framework.get_health_status()
    return {
        "foundry_status": status.foundry_running,
        "active_models": status.loaded_models,
        "available_tools": status.available_tools
    }
```

### ಕಮಾಂಡ್-ಲೈನ್ ಇಂಟಿಗ್ರೇಶನ್
```python
import typer
from rich.console import Console
from rich.table import Table
from foundry_tools.cli import FoundryCLI

app = typer.Typer(name="foundry-tools")
console = Console()
foundry_cli = FoundryCLI()

@app.command()
async def analyze(
    file_path: str = typer.Argument(..., help="Path to code file"),
    language: str = typer.Option("python", help="Programming language"),
    output: str = typer.Option("table", help="Output format (table, json, yaml)")
):
    """Analyze code file using Foundry Local."""
    
    try:
        with open(file_path, 'r') as f:
            code = f.read()
        
        result = await foundry_cli.call_tool(
            "code_analyzer",
            code=code,
            language=language
        )
        
        if output == "table":
            table = Table(title=f"Code Analysis: {file_path}")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="magenta")
            
            for key, value in result.items():
                table.add_row(key, str(value))
            
            console.print(table)
        
        elif output == "json":
            console.print_json(data=result)
        
        else:
            console.print(result)
            
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)

@app.command()
async def list_tools():
    """List all available Foundry tools."""
    
    tools = await foundry_cli.list_available_tools()
    
    table = Table(title="Available Foundry Tools")
    table.add_column("Name", style="cyan")
    table.add_column("Description", style="white")
    table.add_column("Model", style="yellow")
    
    for tool in tools:
        table.add_row(
            tool["name"],
            tool["description"][:50] + "..." if len(tool["description"]) > 50 else tool["description"],
            tool["model"]
        )
    
    console.print(table)

if __name__ == "__main__":
    app()
```

## ಉನ್ನತ ಮಟ್ಟದ ಮಾದರಿಗಳು

### 1. ಟೂಲ್ ಸಂಯೋಜನೆ
```python
from foundry_tools import CompositeFoundryTool

@CompositeFoundryTool(
    name="full_code_review",
    description="Comprehensive code review using multiple analysis tools"
)
async def comprehensive_code_review(code: str, language: str = "python") -> Dict[str, Any]:
    """Perform comprehensive code review using multiple tools."""
    
    # ಹಲವಾರು ವಿಶ್ಲೇಷಣೆಗಳನ್ನು ಸಮಾಂತರವಾಗಿ ನಡೆಸಿ
    analyses = await asyncio.gather(
        call_tool("code_analyzer", code=code, language=language),
        call_tool("security_scanner", code=code, language=language),
        call_tool("performance_analyzer", code=code, language=language),
        call_tool("style_checker", code=code, language=language)
    )
    
    # ಫಲಿತಾಂಶಗಳನ್ನು ಸಂಶ್ಲೇಷಿಸಿ
    return await call_tool("analysis_synthesizer", analyses=analyses)
```

### 2. ಸಂದರ್ಭ-ಜಾಗರೂಕ ಟೂಲ್ಸ್
```python
from foundry_tools.context import ContextAwareFoundryTool

class ProjectAnalyzerTool(ContextAwareFoundryTool):
    """Analyze entire project with context awareness."""
    
    async def execute(self, project_path: str, analysis_depth: str = "shallow") -> Dict[str, Any]:
        """Analyze project with full context."""
        
        # ಪ್ರಾಜೆಕ್ಟ್ ಸನ್ನಿವೇಶವನ್ನು ನಿರ್ಮಿಸಿ
        context = await self.build_project_context(project_path)
        
        # ಸನ್ನಿವೇಶದೊಂದಿಗೆ ವಿಶ್ಲೇಷಿಸಿ
        return await self.foundry_call_with_context({
            "prompt": f"Analyze this {context.language} project",
            "context": context.to_dict(),
            "analysis_depth": analysis_depth
        })
    
    async def build_project_context(self, project_path: str) -> ProjectContext:
        """Build comprehensive project context."""
        # ಇಲ್ಲಿ ಅನುಷ್ಠಾನ
        pass
```

### 3. ಟೂಲ್ ಚೈನಿಂಗ್
```python
from foundry_tools.chains import FoundryToolChain

# ಡಾಕ್ಯುಮೆಂಟ್ ಪ್ರಕ್ರಿಯೆಗಾಗಿ ಉಪಕರಣ ಸರಪಳಿ ನಿರ್ಧರಿಸಿ
doc_processing_chain = FoundryToolChain([
    ("extract_text", {"input": "document_path"}),
    ("summarize_content", {"input": "extracted_text", "style": "outline"}),
    ("generate_keywords", {"input": "summary"}),
    ("create_metadata", {"input": ["summary", "keywords"]})
])

# ಸರಪಳಿಯನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ
result = await doc_processing_chain.execute({
    "document_path": "/path/to/document.pdf"
})
```

## ಕಾರ್ಯಕ್ಷಮತೆ ಸುಧಾರಣೆ

### 1. ಕ್ಯಾಶಿಂಗ್ ತಂತ್ರಗಳು
```python
from foundry_tools.cache import CacheConfig, CacheStrategy

cache_config = CacheConfig(
    strategy=CacheStrategy.LRU,
    max_size=1000,
    ttl=3600,  # 1 ಗಂಟೆ
    key_generator="content_hash"
)

# ನಿರ್ದಿಷ್ಟ ಸಾಧನಗಳಿಗೆ ಅನ್ವಯಿಸಿ
@FoundryTool(
    name="cached_analyzer",
    cache_config=cache_config
)
async def cached_code_analyzer(code: str) -> Dict[str, Any]:
    # ಕ್ಯಾಶಿಂಗ್‌ನಿಂದ ಲಾಭ ಪಡೆಯುವ ದುಬಾರಿ ವಿಶ್ಲೇಷಣೆ
    pass
```

### 2. ಮಾದರಿ ಪೂಲ್ ನಿರ್ವಹಣೆ
```python
from foundry_tools.pool import ModelPoolConfig

pool_config = ModelPoolConfig(
    models={
        "phi-4-mini": {"instances": 2, "priority": "high"},
        "qwen2.5-coder-0.5b": {"instances": 1, "priority": "medium"},
        "phi-3.5-mini": {"instances": 1, "priority": "low"}
    },
    load_balancing="round_robin",
    health_check_interval=30
)

# ಪೂಲ್‌ನೊಂದಿಗೆ ಸಾಧನ ರಿಜಿಸ್ಟ್ರಿಯನ್ನು ಸಂರಚಿಸಿ
registry = FoundryToolRegistry(model_pool_config=pool_config)
```

### 3. ಬ್ಯಾಚ್ ಪ್ರಕ್ರಿಯೆ
```python
from foundry_tools.batch import BatchProcessor

@BatchProcessor(
    batch_size=10,
    timeout=60,
    parallel_batches=3
)
async def batch_code_analysis(code_files: List[str]) -> List[Dict[str, Any]]:
    """Process multiple code files in batches."""
    results = []
    
    for code_file in code_files:
        with open(code_file, 'r') as f:
            code = f.read()
        
        result = await call_tool("code_analyzer", code=code)
        results.append(result)
    
    return results
```

## ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಗಮನಾರ್ಹತೆ

### 1. ಟೂಲ್ ಮೆಟ್ರಿಕ್ಸ್
```python
from foundry_tools.monitoring import ToolMetrics

# ಸ್ವಯಂಚಾಲಿತ ಮೆಟ್ರಿಕ್ ಸಂಗ್ರಹಣೆ
metrics = await ToolMetrics.get_tool_performance("code_analyzer")
print(f"Average execution time: {metrics.avg_execution_time}s")
print(f"Success rate: {metrics.success_rate}%")
print(f"Cache hit rate: {metrics.cache_hit_rate}%")
```

### 2. ಆರೋಗ್ಯ ಮೇಲ್ವಿಚಾರಣೆ
```python
from foundry_tools.health import HealthMonitor

health_monitor = HealthMonitor()

# ಸಾಧನ ಆರೋಗ್ಯವನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ
health_status = await health_monitor.check_all_tools()
print(f"Healthy tools: {health_status.healthy_count}")
print(f"Failed tools: {health_status.failed_tools}")
```

### 3. ಬಳಕೆ ವಿಶ್ಲೇಷಣೆ
```python
from foundry_tools.analytics import UsageAnalytics

analytics = UsageAnalytics()

# ಉಪಕರಣ ಬಳಕೆ ಮಾದರಿಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ
usage_report = await analytics.generate_usage_report(
    start_date="2024-01-01",
    end_date="2024-01-31"
)

print(f"Most used tool: {usage_report.most_used_tool}")
print(f"Peak usage time: {usage_report.peak_usage_time}")
```

## ಕಲಿಕೆಯ ಫಲಿತಾಂಶಗಳು

ಈ ಮಾದರಿಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ತಿಳಿದುಕೊಳ್ಳುತ್ತೀರಿ:

1. **ಟೂಲ್ ಇಂಟಿಗ್ರೇಶನ್ ಮಾದರಿಗಳು**
   - ಫಂಕ್ಷನ್ ಆಧಾರಿತ ಮತ್ತು ಕ್ಲಾಸ್ ಆಧಾರಿತ ಟೂಲ್ ವಿನ್ಯಾಸ
   - ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಇಂಟಿಗ್ರೇಶನ್ ಮಾದರಿಗಳು
   - ಸ್ಕೀಮಾ ಮಾನ್ಯತೆ ಮತ್ತು ಪ್ರಕಾರ ಸುರಕ್ಷತೆ
   - ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಪುನಃಪ್ರಾಪ್ತಿ

2. **ಫ್ರೇಮ್ವರ್ಕ್ ಇಂಟಿಗ್ರೇಶನ್**
   - ಲ್ಯಾಂಗ್‌ಚೈನ್ ಟೂಲ್ ಅಭಿವೃದ್ಧಿ
   - ಸೆಮ್ಯಾಂಟಿಕ್ ಕರ್ಣಲ್ ಫಂಕ್ಷನ್ ಇಂಟಿಗ್ರೇಶನ್
   - REST API ಫ್ರೇಮ್ವರ್ಕ್ ಇಂಟಿಗ್ರೇಶನ್
   - CLI ಅಪ್ಲಿಕೇಶನ್ ಅಭಿವೃದ್ಧಿ

3. **ಉತ್ಪಾದನಾ ಪರಿಗಣನೆಗಳು**
   - ಕಾರ್ಯಕ್ಷಮತೆ ಸುಧಾರಣಾ ತಂತ್ರಗಳು
   - ಕ್ಯಾಶಿಂಗ್ ಮತ್ತು ಸಂಪನ್ಮೂಲ ನಿರ್ವಹಣೆ
   - ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಗಮನಾರ್ಹತೆ
   - ಭದ್ರತೆ ಮತ್ತು ಮಾನ್ಯತೆ

4. **ಉನ್ನತ ಮಟ್ಟದ ಟೂಲ್ ಮಾದರಿಗಳು**
   - ಟೂಲ್ ಸಂಯೋಜನೆ ಮತ್ತು ಚೈನಿಂಗ್
   - ಸಂದರ್ಭ-ಜಾಗರೂಕ ಪ್ರಕ್ರಿಯೆ
   - ಬ್ಯಾಚ್ ಮತ್ತು ಸ್ಟ್ರೀಮಿಂಗ್ ಕಾರ್ಯಾಚರಣೆಗಳು
   - ಕಸ್ಟಮ್ ಇಂಟಿಗ್ರೇಶನ್ ಅಭಿವೃದ್ಧಿ

## ಮುಂದಿನ ಹಂತಗಳು

- **ಇಂಟಿಗ್ರೇಶನ್ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳು**: ನಿಮ್ಮ ಇಷ್ಟದ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಕಸ್ಟಮ್ ಇಂಟಿಗ್ರೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿ
- **ಟೂಲ್ ಅಭಿವೃದ್ಧಿ**: ನಿಮ್ಮ ಕ್ಷೇತ್ರಕ್ಕೆ ವಿಶೇಷ ಟೂಲ್ಸ್ ರಚಿಸಿ
- **ಕಾರ್ಯಕ್ಷಮತೆ ಟ್ಯೂನಿಂಗ್**: ನಿಮ್ಮ ನಿರ್ದಿಷ್ಟ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಗೆ ಅನುಗುಣವಾಗಿ ಸುಧಾರಿಸಿ
- **ಉತ್ಪಾದನಾ ನಿಯೋಜನೆ**: ಎಂಟರ್‌ಪ್ರೈಸ್ ಬಳಕೆಗೆ ಟೂಲ್ಸ್‌ಗಳನ್ನು ವಿಸ್ತರಿಸಿ

## ಕೊಡುಗೆ ನೀಡುವುದು

ಕೊಡುಗೆ ಸೂಚನೆಗಳಿಗಾಗಿ ಮುಖ್ಯ ರೆಪೊಸಿಟರಿ ಮಾರ್ಗಸೂಚಿಗಳನ್ನು ನೋಡಿ.

## ಪರವಾನಗಿ

ಈ ಮಾದರಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಅದೇ ಪರವಾನಗಿಯನ್ನು ಅನುಸರಿಸುತ್ತದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->