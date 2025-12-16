<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a988dfc121c969bcc37d9c1a04fcd6c",
  "translation_date": "2025-12-16T00:45:37+00:00",
  "source_file": "Module08/samples/10/README.md",
  "language_code": "ml"
}
-->
# Foundry Local as Tools Integration

വലിയ ആപ്ലിക്കേഷനുകളിൽ വിളിക്കാവുന്ന ടൂളുകളായി Microsoft Foundry Local സംയോജിപ്പിക്കുന്നതിന് ഒരു സമഗ്രമായ ഫ്രെയിംവർക്ക്, ടൂൾ അടിസ്ഥാനമാക്കിയ AI സംയോജിപ്പിക്കലിനുള്ള Microsoft ന്റെ ഔദ്യോഗിക മാതൃകകൾ പിന്തുടരുന്നു.

## അവലോകനം

ഈ സാമ്പിൾ നിലവിലുള്ള ആപ്ലിക്കേഷനുകളിലും വർക്ക്‌ഫ്ലോകളിലും ഡെവലപ്പ്മെന്റ് പരിസ്ഥിതികളിലും സംയോജിപ്പിക്കാവുന്ന പുനരുപയോഗയോഗ്യമായ ടൂളുകളായി Foundry Local മോഡലുകൾ എങ്ങനെ പ്രദർശിപ്പിക്കാമെന്ന് കാണിക്കുന്നു. ടൂൾ സംയോജിപ്പിക്കൽക്കും ഫംഗ്ഷൻ കോൾ ചെയ്യലിനും Microsoft ന്റെ ശുപാർശ ചെയ്ത മാതൃകകൾ ഇതിൽ കാണിക്കുന്നു.

## പ്രധാന ആശയങ്ങൾ

### 🔧 **ടൂൾ-ഫസ്റ്റ് ആർക്കിടെക്ചർ**
- വിളിക്കാവുന്ന ഫംഗ്ഷനുകളായി Foundry Local മോഡലുകൾ
- സ്റ്റാൻഡേർഡൈസ്ഡ് ടൂൾ ഇന്റർഫേസുകളും സ്കീമകളും
- നിലവിലുള്ള കോഡ്‌ബേസുകളുമായി സുതാര്യമായ സംയോജനം
- ടൈപ്പ്-സേഫ് ടൂൾ നിർവചനങ്ങളും സാധുതയും

### ⚡ **ഫംഗ്ഷൻ കോൾ ചെയ്യൽ മാതൃകകൾ**
- Microsoft Foundry Local ഫംഗ്ഷൻ കോൾ ചെയ്യൽ നടപ്പാക്കൽ
- OpenAI-സമാനമായ ടൂൾ നിർവചനങ്ങൾ
- സ്വയംപരിശോധനയും പരാമീറ്റർ പരിവർത്തനവും
- പിശക് കൈകാര്യം ചെയ്യലും പ്രതികരണ ഫോർമാറ്റിംഗും

### 🔌 **സംയോജനം ഫ്രെയിംവർക്കുകൾ**
- **LangChain സംയോജനം**: നേറ്റീവ് LangChain ടൂൾ പിന്തുണ
- **Semantic Kernel**: Microsoft Semantic Kernel ഫംഗ്ഷനുകൾ
- **REST API**: HTTP അടിസ്ഥാനമാക്കിയ ടൂൾ എൻഡ്‌പോയിന്റുകൾ
- **CLI ടൂളുകൾ**: കമാൻഡ്-ലൈൻ ഇന്റർഫേസ് സംയോജനം
- **Jupyter Notebooks**: ഇന്ററാക്ടീവ് ഡെവലപ്പ്മെന്റ് ടൂളുകൾ

### 🎯 **ഉപയോഗ കേസുകൾ**
- കോഡ് വിശകലനവും സൃഷ്ടിയും
- ഉള്ളടക്ക പ്രോസസ്സിംഗും സംഗ്രഹീകരണവും
- ഡാറ്റ വിശകലനവും ദൃശ്യവൽക്കരണവും
- ഗവേഷണവും വിവര ശേഖരണവും
- തീരുമാന സഹായ സംവിധാനങ്ങൾ

## ആർക്കിടെക്ചർ

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

## മുൻ‌അവശ്യങ്ങൾ

### സിസ്റ്റം ആവശ്യകതകൾ
- **Python**: asyncio പിന്തുണയോടെ 3.9+
- **Node.js**: v18+ (JavaScript സംയോജനംക്കായി)
- **മെമ്മറി**: 12GB+ ശുപാർശ ചെയ്യുന്നു
- **സ്റ്റോറേജ്**: മോഡലുകൾക്കും ടൂളുകൾക്കും 10GB+

### കോർ ആശ്രിതങ്ങൾ
```bash
pip install foundry-local-sdk openai langchain semantic-kernel fastapi uvicorn typer rich
```

### ഫ്രെയിംവർക്ക്-നിർദിഷ്ട ആശ്രിതങ്ങൾ
```bash
# ലാംഗ്‌ചെയിൻ ഇന്റഗ്രേഷൻ
pip install langchain-openai langchain-community

# സെമാന്റിക് കർണൽ ഇന്റഗ്രേഷൻ
pip install semantic-kernel

# വെബ് ഫ്രെയിംവർക്ക് ഇന്റഗ്രേഷൻ
pip install fastapi uvicorn streamlit gradio

# ഡെവലപ്പ്മെന്റ് ടൂളുകൾ
pip install jupyter ipywidgets
```

## വേഗത്തിലുള്ള ആരംഭം

### 1. അടിസ്ഥാന ടൂൾ സൃഷ്ടി
```python
from foundry_tools import FoundryTool, FoundryToolRegistry

# ഒരു ലളിതമായ വിശകലന ഉപകരണം സൃഷ്ടിക്കുക
@FoundryTool(
    name="code_analyzer",
    description="Analyze code quality and suggest improvements",
    model="phi-4-mini"
)
async def analyze_code(code: str, language: str = "python") -> dict:
    """Analyze code and return quality metrics and suggestions."""
    pass

# ഉപകരണം രജിസ്റ്റർ ചെയ്ത് ഉപയോഗിക്കുക
registry = FoundryToolRegistry()
await registry.register(analyze_code)

result = await registry.call("code_analyzer", {
    "code": "def hello(): print('world')",
    "language": "python"
})
```

### 2. LangChain സംയോജനം
```python
from langchain.tools import BaseTool
from foundry_tools.langchain import FoundryLangChainTool

# LangChain-സഹജമായ ടൂൾ സൃഷ്ടിക്കുക
class CodeAnalyzerTool(FoundryLangChainTool):
    name = "code_analyzer"
    description = "Analyze code quality using Foundry Local"
    model = "phi-4-mini"
    
    async def _arun(self, code: str, language: str = "python") -> str:
        return await self.foundry_call({
            "code": code,
            "language": language
        })

# LangChain ഏജന്റുകളുമായി ഉപയോഗിക്കുക
from langchain.agents import initialize_agent, AgentType

tools = [CodeAnalyzerTool()]
agent = initialize_agent(
    tools=tools,
    llm=None,  # Foundry Local ഉപയോഗിക്കുന്നു
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)
```

### 3. REST API സംയോജനം
```python
from fastapi import FastAPI
from foundry_tools.rest import FoundryRESTEndpoint

app = FastAPI()

# Foundry ഉപകരണങ്ങളിൽ നിന്ന് REST എൻഡ്‌പോയിന്റുകൾ സ്വയം സൃഷ്ടിക്കുക
foundry_api = FoundryRESTEndpoint()
await foundry_api.register_tool("code_analyzer", analyze_code)

# എൻഡ്‌പോയിന്റുകൾ മൗണ്ട് ചെയ്യുക
app.include_router(foundry_api.router, prefix="/foundry/v1")

# HTTP വഴി ഉപയോഗിക്കുക
# POST /foundry/v1/code_analyzer
# {
#   "code": "def hello(): print('world')",
#   "language": "python"
# }
```

## പ്രോജക്ട് ഘടന

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

## കോർ ടൂൾ മാതൃകകൾ

### 1. ഫംഗ്ഷൻ അടിസ്ഥാനമാക്കിയ ടൂളുകൾ
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
    
    # ഡെക്കറേറ്റർ സ്വയം കൈകാര്യം ചെയ്യുന്നു:
    # - പാരാമീറ്റർ പരിശോധന
    # - ഫൗണ്ടറി ലോക്കൽ ക്ലയന്റ് സജ്ജീകരണം
    # - പിശക് കൈകാര്യം ചെയ്യലും ലോഗിംഗും
    # - പ്രതികരണ ഫോർമാറ്റിംഗ്
    
    system_prompt = f"""
    Summarize the following content into {max_points} key points.
    Use {style} format for the summary.
    """
    
    # ഇത് സ്വയം ഫൗണ്ടറി ലോക്കലിലേക്ക് റൂട്ടുചെയ്യപ്പെടുന്നു
    return {
        "summary": "Generated summary here...",
        "points": max_points,
        "style": style,
        "word_count": len(content.split())
    }
```

### 2. ക്ലാസ് അടിസ്ഥാനമാക്കിയ ടൂളുകൾ
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
        
        # കാഷെ പരിശോധിക്കുക
        cache_key = f"{hash(code)}_{language}_{analysis_type}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        # ഫൗണ്ട്രി ലോക്കൽ ഉപയോഗിച്ച് വിശകലനം നടത്തുക
        result = await self.foundry_call({
            "system_prompt": f"Analyze this {language} code for {analysis_type} analysis",
            "user_prompt": f"Code to analyze:\n\n```{language}\n{code}\n```",
            "max_tokens": 1000
        })
        
        # ഫലം പ്രോസസ്സ് ചെയ്ത് കാഷെ ചെയ്യുക
        analysis_result = self.process_analysis_result(result, analysis_type)
        self.analysis_cache[cache_key] = analysis_result
        
        return analysis_result
    
    def process_analysis_result(self, raw_result: str, analysis_type: str) -> Dict[str, Any]:
        """Process the raw analysis result into structured data."""
        # ഇവിടെ നടപ്പാക്കൽ
        pass
```

### 3. സ്ട്രീമിംഗ് ടൂളുകൾ
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
    
    # ആദ്യം മെറ്റാഡേറ്റ നൽകുക
    yield {
        "type": "metadata",
        "language": language,
        "include_tests": include_tests,
        "estimated_lines": 50
    }
    
    # കോഡ് ജനറേഷൻ സ്ട്രീം ചെയ്യുക
    async for chunk in foundry_stream({
        "prompt": f"Generate {language} code: {specification}",
        "stream": True
    }):
        yield {
            "type": "code_chunk",
            "content": chunk.content,
            "complete": chunk.finish_reason is not None
        }
    
    # അന്തിമ ഫലം നൽകുക
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

## സംയോജനം ഉദാഹരണങ്ങൾ

### LangChain സംയോജനം
```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate
from foundry_tools.langchain import FoundryToolkit

# ഫൗണ്ട്രി-ചാലിത ടൂൾകിറ്റ് സൃഷ്ടിക്കുക
toolkit = FoundryToolkit()
toolkit.add_tool("code_analyzer", model="phi-4-mini")
toolkit.add_tool("content_summarizer", model="qwen2.5-0.5b") 
toolkit.add_tool("research_assistant", model="phi-3.5-mini")

# ഫൗണ്ട്രി ടൂളുകൾ ഉപയോഗിച്ച് ഏജന്റ് സൃഷ്ടിക്കുക
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to Foundry Local tools."),
    ("user", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

agent = create_openai_functions_agent(
    llm=toolkit.get_llm(),  # ഫൗണ്ട്രി ലോക്കൽ LLM ആയി ഉപയോഗിക്കുന്നു
    tools=toolkit.get_tools(),
    prompt=prompt
)

agent_executor = AgentExecutor(agent=agent, tools=toolkit.get_tools())

# ഏജന്റ് ഉപയോഗിക്കുക
result = await agent_executor.ainvoke({
    "input": "Analyze this Python code and summarize any issues you find"
})
```

### Semantic Kernel സംയോജനം
```python
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from foundry_tools.semantic_kernel import FoundryKernelPlugin

# ഫൗണ്ട്രി ലോക്കലുമായി കർണൽ ആരംഭിക്കുക
kernel = Kernel()

# ചാറ്റ് സേവനമായി ഫൗണ്ട്രി ലോക്കൽ ചേർക്കുക
foundry_service = OpenAIChatCompletion(
    service_id="foundry_chat",
    ai_model_id="phi-4-mini",
    api_key="not-needed",
    base_url="http://localhost:5273/v1"
)
kernel.add_service(foundry_service)

# ഫൗണ്ട്രി പ്ലഗിൻ സൃഷ്ടിച്ച് ചേർക്കുക
foundry_plugin = FoundryKernelPlugin()
foundry_plugin.add_function("analyze_code", model="phi-4-mini")
foundry_plugin.add_function("summarize_text", model="qwen2.5-0.5b")

kernel.add_plugin(foundry_plugin, plugin_name="foundry_tools")

# സെമാന്റിക് കർണൽ വർക്ക്‌ഫ്ലോകളിൽ ഉപയോഗിക്കുക
result = await kernel.invoke(
    "foundry_tools", 
    "analyze_code",
    code="def hello(): print('world')",
    language="python"
)
```

### FastAPI സംയോജനം
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from foundry_tools.rest import FoundryRESTFramework

app = FastAPI(title="Foundry Local Tools API")

# ഫൗണ്ട്രി REST ഫ്രെയിംവർക്ക് ആരംഭിക്കുക
foundry_framework = FoundryRESTFramework()

# ലഭ്യമായ എല്ലാ ടൂളുകളും സ്വയം രജിസ്റ്റർ ചെയ്യുക
await foundry_framework.auto_register_tools([
    "code_analyzer",
    "content_summarizer", 
    "data_processor",
    "research_assistant"
])

# ഫൗണ്ട്രി എന്റ്പോയിന്റുകൾ മൗണ്ട് ചെയ്യുക
app.include_router(
    foundry_framework.get_router(),
    prefix="/api/v1/foundry",
    tags=["foundry-tools"]
)

# ഫൗണ്ട്രി ടൂളുകൾ ഉപയോഗിച്ച് കസ്റ്റം എന്റ്പോയിന്റ്
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

# ഹെൽത്ത് ചെക്ക് എന്റ്പോയിന്റ്
@app.get("/api/v1/health")
async def health_check():
    status = await foundry_framework.get_health_status()
    return {
        "foundry_status": status.foundry_running,
        "active_models": status.loaded_models,
        "available_tools": status.available_tools
    }
```

### കമാൻഡ്-ലൈൻ സംയോജനം
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

## പുരോഗമന മാതൃകകൾ

### 1. ടൂൾ സംയോജനം
```python
from foundry_tools import CompositeFoundryTool

@CompositeFoundryTool(
    name="full_code_review",
    description="Comprehensive code review using multiple analysis tools"
)
async def comprehensive_code_review(code: str, language: str = "python") -> Dict[str, Any]:
    """Perform comprehensive code review using multiple tools."""
    
    # പാരലൽ ആയി നിരവധി വിശകലനങ്ങൾ നടത്തുക
    analyses = await asyncio.gather(
        call_tool("code_analyzer", code=code, language=language),
        call_tool("security_scanner", code=code, language=language),
        call_tool("performance_analyzer", code=code, language=language),
        call_tool("style_checker", code=code, language=language)
    )
    
    # ഫലങ്ങൾ സംയോജിപ്പിക്കുക
    return await call_tool("analysis_synthesizer", analyses=analyses)
```

### 2. കോൺടെക്സ്റ്റ്-അവേർ ടൂളുകൾ
```python
from foundry_tools.context import ContextAwareFoundryTool

class ProjectAnalyzerTool(ContextAwareFoundryTool):
    """Analyze entire project with context awareness."""
    
    async def execute(self, project_path: str, analysis_depth: str = "shallow") -> Dict[str, Any]:
        """Analyze project with full context."""
        
        # പ്രോജക്ട് സാന്ദർഭ്യം നിർമ്മിക്കുക
        context = await self.build_project_context(project_path)
        
        # സാന്ദർഭ്യത്തോടെ വിശകലനം ചെയ്യുക
        return await self.foundry_call_with_context({
            "prompt": f"Analyze this {context.language} project",
            "context": context.to_dict(),
            "analysis_depth": analysis_depth
        })
    
    async def build_project_context(self, project_path: str) -> ProjectContext:
        """Build comprehensive project context."""
        # നടപ്പാക്കൽ ഇവിടെ
        pass
```

### 3. ടൂൾ ചെയിനിംഗ്
```python
from foundry_tools.chains import FoundryToolChain

# ഡോക്യുമെന്റ് പ്രോസസ്സിംഗിനുള്ള ഒരു ടൂൾ ചെയിൻ നിർവചിക്കുക
doc_processing_chain = FoundryToolChain([
    ("extract_text", {"input": "document_path"}),
    ("summarize_content", {"input": "extracted_text", "style": "outline"}),
    ("generate_keywords", {"input": "summary"}),
    ("create_metadata", {"input": ["summary", "keywords"]})
])

# ചെയിൻ പ്രവർത്തിപ്പിക്കുക
result = await doc_processing_chain.execute({
    "document_path": "/path/to/document.pdf"
})
```

## പ്രകടന മെച്ചപ്പെടുത്തൽ

### 1. കാഷിംഗ് തന്ത്രങ്ങൾ
```python
from foundry_tools.cache import CacheConfig, CacheStrategy

cache_config = CacheConfig(
    strategy=CacheStrategy.LRU,
    max_size=1000,
    ttl=3600,  # 1 മണിക്കൂർ
    key_generator="content_hash"
)

# പ്രത്യേക ഉപകരണങ്ങൾക്ക് അപേക്ഷിക്കുക
@FoundryTool(
    name="cached_analyzer",
    cache_config=cache_config
)
async def cached_code_analyzer(code: str) -> Dict[str, Any]:
    # കാഷിംഗ് ഉപയോഗിച്ച് ലാഭം ലഭിക്കുന്ന ചെലവേറിയ വിശകലനം
    pass
```

### 2. മോഡൽ പൂൾ മാനേജ്മെന്റ്
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

# ടൂൾ രജിസ്ട്രി പൂലുമായി കോൺഫിഗർ ചെയ്യുക
registry = FoundryToolRegistry(model_pool_config=pool_config)
```

### 3. ബാച്ച് പ്രോസസ്സിംഗ്
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

## നിരീക്ഷണവും ദൃശ്യവൽക്കരണവും

### 1. ടൂൾ മെട്രിക്‌സ്
```python
from foundry_tools.monitoring import ToolMetrics

# സ്വയം പ്രവർത്തിക്കുന്ന മെട്രിക്‌സ് ശേഖരണം
metrics = await ToolMetrics.get_tool_performance("code_analyzer")
print(f"Average execution time: {metrics.avg_execution_time}s")
print(f"Success rate: {metrics.success_rate}%")
print(f"Cache hit rate: {metrics.cache_hit_rate}%")
```

### 2. ഹെൽത്ത് നിരീക്ഷണം
```python
from foundry_tools.health import HealthMonitor

health_monitor = HealthMonitor()

# ഉപകരണത്തിന്റെ ആരോഗ്യനില നിരീക്ഷിക്കുക
health_status = await health_monitor.check_all_tools()
print(f"Healthy tools: {health_status.healthy_count}")
print(f"Failed tools: {health_status.failed_tools}")
```

### 3. ഉപയോഗ വിശകലനം
```python
from foundry_tools.analytics import UsageAnalytics

analytics = UsageAnalytics()

# ഉപകരണ ഉപയോഗ പാറ്റേണുകൾ ട്രാക്ക് ചെയ്യുക
usage_report = await analytics.generate_usage_report(
    start_date="2024-01-01",
    end_date="2024-01-31"
)

print(f"Most used tool: {usage_report.most_used_tool}")
print(f"Peak usage time: {usage_report.peak_usage_time}")
```

## പഠന ഫലങ്ങൾ

ഈ സാമ്പിൾ പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്ക് മനസ്സിലാകും:

1. **ടൂൾ സംയോജനം മാതൃകകൾ**
   - ഫംഗ്ഷൻ അടിസ്ഥാനമാക്കിയും ക്ലാസ് അടിസ്ഥാനമാക്കിയും ടൂൾ ഡിസൈൻ
   - Microsoft Foundry Local സംയോജനം മാതൃകകൾ
   - സ്കീമാ സാധുതയും ടൈപ്പ് സുരക്ഷയും
   - പിശക് കൈകാര്യം ചെയ്യലും പുനരുദ്ധാരണം

2. **ഫ്രെയിംവർക്ക് സംയോജനം**
   - LangChain ടൂൾ വികസനം
   - Semantic Kernel ഫംഗ്ഷൻ സംയോജനം
   - REST API ഫ്രെയിംവർക്ക് സംയോജനം
   - CLI ആപ്ലിക്കേഷൻ വികസനം

3. **പ്രൊഡക്ഷൻ പരിഗണനകൾ**
   - പ്രകടന മെച്ചപ്പെടുത്തൽ തന്ത്രങ്ങൾ
   - കാഷിംഗ്, റിസോഴ്‌സ് മാനേജ്മെന്റ്
   - നിരീക്ഷണവും ദൃശ്യവൽക്കരണവും
   - സുരക്ഷയും സാധുതയും

4. **പുരോഗമന ടൂൾ മാതൃകകൾ**
   - ടൂൾ സംയോജനം, ചെയിനിംഗ്
   - കോൺടെക്സ്റ്റ്-അവേർ പ്രോസസ്സിംഗ്
   - ബാച്ച്, സ്ട്രീമിംഗ് ഓപ്പറേഷനുകൾ
   - കസ്റ്റം സംയോജനം വികസനം

## അടുത്ത ഘട്ടങ്ങൾ

- **സംയോജനം പ്രോജക്ടുകൾ**: നിങ്ങളുടെ ഇഷ്ടപ്പെട്ട ഫ്രെയിംവർക്കുകളുമായി കസ്റ്റം സംയോജനം നിർമ്മിക്കുക
- **ടൂൾ വികസനം**: നിങ്ങളുടെ ഡൊമെയ്‌നിനായി പ്രത്യേക ടൂളുകൾ സൃഷ്ടിക്കുക
- **പ്രകടന ട്യൂണിംഗ്**: നിങ്ങളുടെ പ്രത്യേക ഉപയോഗ കേസുകൾക്കായി മെച്ചപ്പെടുത്തുക
- **പ്രൊഡക്ഷൻ ഡിപ്ലോയ്മെന്റ്**: എന്റർപ്രൈസ് ഉപയോഗത്തിനായി ടൂളുകൾ സ്കെയിൽ ചെയ്യുക

## സംഭാവന

സംഭാവന നിർദ്ദേശങ്ങൾക്കായി പ്രധാന റിപോസിറ്ററി മാർഗ്ഗനിർദ്ദേശങ്ങൾ കാണുക.

## ലൈസൻസ്

ഈ സാമ്പിൾ Microsoft Foundry Local പ്രോജക്ടിന്റെ സമാനമായ ലൈസൻസ് പിന്തുടരുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->