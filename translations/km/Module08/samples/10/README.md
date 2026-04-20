# Foundry Local ជាការរួមបញ្ចូលជា Tools

សំណុំស្ដង់ដារពេញលេញសម្រាប់រួមបញ្ចូល Microsoft Foundry Local ជាឧបករណ៍ដែលអាចហៅបាននៅក្នុងកម្មវិធីធំៗ ដោយអនុវត្តតាមគំរូផ្លូវការរបស់ Microsoft សម្រាប់ការរួមបញ្ចូល AI ជាឧបករណ៍។

## សេចក្តីបាក់សោះ

ឧទាហរណ៍នេះបង្ហាញពីវិធីបង្ហាញម៉ូឌែល Foundry Local ជាឧបករណ៍ដែលអាចប្រើឡើងវិញ ហើយអាចរួមបញ្ចូលក្នុងកម្មវិធីដែលមានស្រេច ក្រុមហ៊ុន, និងបរិយាកាសអភិវឌ្ឍន៍។ វាបង្ហាញគំរូណែនាំរបស់ Microsoft សម្រាប់ការរួមបញ្ចូលឧបករណ์ និងការហៅមុខងារ។

## គំនិតសំខាន់

### 🔧 Tool-First Architecture
- ម៉ូឌែល Foundry Local ជាមុខងារអាចហៅបាន
- សំរិទ្ធផ្ទៃមុខនៃឧបករណ៍ និងស្កីម៉ា
- រួមបញ្ចូលយ៉ាងរលូនជាមួយកូដដែលមានស្រេច
- ការកំណត់ប្រភេទឧបករណ៍ដែលមានសុវត្ថិភាព និងការផ្ទៀងផ្ទាត់

### ⚡ Function Calling Patterns
- ការអនុវត្តការហៅមុខងារ Microsoft Foundry Local
- កំណត់អំពីឧបករណ៍ដែលឆបគ្នាជាមួយ OpenAI
- ការផ្ទៀងផ្ទាត់ប៉ារ៉ាម៉ែត្រ និងការបម្លែងដោយស្វ័យប្រវត្តិ
- ការដោះស្រាយកំហុស និងទ្រង់ទ្រាយចម្លើយ

### 🔌 Integration Frameworks
- **LangChain Integration**: ការគាំទ្រឧបករណ៍ LangChain ដើម
- **Semantic Kernel**: មុខងារ Microsoft Semantic Kernel
- **REST API**: ចុងបញ្ចប់ឧបករណ៍ផ្អែកលើយ HTTP
- **CLI Tools**: ការរួមបញ្ចូលចំណុចបញ្ជា(Command-line)
- **Jupyter Notebooks**: ឧបករណ៍អភិវឌ្ឍន៍អន្តរកម្ម

### 🎯 Use Case Patterns
- ឧបករណ៍វិភាគ និងបង្កើតកូដ
- ការបំពាក់មាតិកា និងដាក់សេចកទ្បាយសង្ខេប
- ការវិភាគទិន្នន័យ និងការបង្ហាញទិន្នន័យ
- ការស្រាវជ្រាវ និងការទាញយកព័ត៌មាន
- ប្រព័ន្ធគាំទ្រសេចក្តីសម្រេចចិត្ត

## ស្ថាបត្យភាព

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

## មុនដំណើរការ

### តម្រូវការពិភពលោក
- **Python**: 3.9+ ជាមួយការគាំទ្រ asyncio
- **Node.js**: v18+ (សម្រាប់ការរួមបញ្ចូល JavaScript)
- **Memory**: 12GB+ បញ្ជាក់ជាក់សម្បូរ
- **Storage**: 10GB+ សម្រាប់ម៉ូឌែល និងឧបករណ៍

### ខ្នាតឧបករណ៍គ្រឹះ
```bash
pip install foundry-local-sdk openai langchain semantic-kernel fastapi uvicorn typer rich
```

### ខ្នាតឧបករណ៍ជាក់លាក់របស់ Framework
```bash
# ការរួមបញ្ចូល LangChain
pip install langchain-openai langchain-community

# ការរួមបញ្ចូល Semantic Kernel
pip install semantic-kernel

# ការរួមបញ្ចូលរចនាសម្ព័ន្ធវេប
pip install fastapi uvicorn streamlit gradio

# ឧបករណ៍អភិវឌ្ឍន៍
pip install jupyter ipywidgets
```

## ចាប់ផ្តើមយ៉ាងរហ័ស

### 1. ការបង្កើតឧបករណ៍មូលដ្ឋាន
```python
from foundry_tools import FoundryTool, FoundryToolRegistry

# បង្កើតឧបករណ៍វិភាគសាមញ្ញ
@FoundryTool(
    name="code_analyzer",
    description="Analyze code quality and suggest improvements",
    model="phi-4-mini"
)
async def analyze_code(code: str, language: str = "python") -> dict:
    """Analyze code and return quality metrics and suggestions."""
    pass

# ចុះបញ្ជីឧបករណ៍ និងប្រើវា
registry = FoundryToolRegistry()
await registry.register(analyze_code)

result = await registry.call("code_analyzer", {
    "code": "def hello(): print('world')",
    "language": "python"
})
```

### 2. ការរួមបញ្ចូល LangChain
```python
from langchain.tools import BaseTool
from foundry_tools.langchain import FoundryLangChainTool

# បង្កើតឧបករណ៍ដែលអាចប្រើបានជាមួយ LangChain
class CodeAnalyzerTool(FoundryLangChainTool):
    name = "code_analyzer"
    description = "Analyze code quality using Foundry Local"
    model = "phi-4-mini"
    
    async def _arun(self, code: str, language: str = "python") -> str:
        return await self.foundry_call({
            "code": code,
            "language": language
        })

# ប្រើជាមួយភ្នាក់ងារ LangChain
from langchain.agents import initialize_agent, AgentType

tools = [CodeAnalyzerTool()]
agent = initialize_agent(
    tools=tools,
    llm=None,  # ប្រើប្រាស់ Foundry Local
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)
```

### 3. ការរួមបញ្ចូល REST API
```python
from fastapi import FastAPI
from foundry_tools.rest import FoundryRESTEndpoint

app = FastAPI()

# បង្កើតចុងបញ្ចប់ REST ដោយស្វ័យប្រវัตពីឧបករណ៍ Foundry
foundry_api = FoundryRESTEndpoint()
await foundry_api.register_tool("code_analyzer", analyze_code)

# ភ្ជាប់ចុងបញ្ចប់
app.include_router(foundry_api.router, prefix="/foundry/v1")

# ប្រើតាមរយៈ HTTP
# POST /foundry/v1/code_analyzer
# {
#   "code": "def hello(): print('world')",
#   "language": "python"
# }
```

## រចនាសម្ព័ន្ធគម្រោង

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

## គំរូឧបករណ៍មូលដ្ឋាន

### 1. ឧបករណ៍ជាមុខងារ
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
    
    # decorator នេះដំណើរការជាស្វ័យប្រវត្តិ:
    # - ការផ្ទៀងផ្ទាត់ប៉ារ៉ាម៉ែត្រ
    # - ការកំណត់ client សម្រាប់ Foundry Local
    # - ការដោះស្រាយកំហុស និងការចុះកំណត់ហេតុ
    # - ការរៀបចំទ្រង់ទ្រាយនៃការឆ្លើយតប
    
    system_prompt = f"""
    Summarize the following content into {max_points} key points.
    Use {style} format for the summary.
    """
    
    # នេះត្រូវបានបញ្ជូនទៅ Foundry Local ដោយស្វ័យប្រវត្តិ
    return {
        "summary": "Generated summary here...",
        "points": max_points,
        "style": style,
        "word_count": len(content.split())
    }
```

### 2. ឧបករណ៍ជាបណ្ណាសារ (Class-Based Tools)
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
        
        # ពិនិត្យកែស
        cache_key = f"{hash(code)}_{language}_{analysis_type}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        # ធ្វើវិភាគដោយប្រើ Foundry Local
        result = await self.foundry_call({
            "system_prompt": f"Analyze this {language} code for {analysis_type} analysis",
            "user_prompt": f"Code to analyze:\n\n```{language}\n{code}\n```",
            "max_tokens": 1000
        })
        
        # ដំណើរការ និងរក្សាលទ្ធផលក្នុងកែស
        analysis_result = self.process_analysis_result(result, analysis_type)
        self.analysis_cache[cache_key] = analysis_result
        
        return analysis_result
    
    def process_analysis_result(self, raw_result: str, analysis_type: str) -> Dict[str, Any]:
        """Process the raw analysis result into structured data."""
        # ការអនុវត្តនៅទីនេះ
        pass
```

### 3. ឧបករណ៍បញ្ជូនបន្ត (Streaming Tools)
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
    
    # បញ្ចេញទិន្នន័យមេតាជាមុន
    yield {
        "type": "metadata",
        "language": language,
        "include_tests": include_tests,
        "estimated_lines": 50
    }
    
    # បង្កើតកូដជាចរន្ត
    async for chunk in foundry_stream({
        "prompt": f"Generate {language} code: {specification}",
        "stream": True
    }):
        yield {
            "type": "code_chunk",
            "content": chunk.content,
            "complete": chunk.finish_reason is not None
        }
    
    # បញ្ចេញលទ្ធផលចុងក្រោយ
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

## ឧទាហរណ៍រួមបញ្ចូល

### LangChain Integration
```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate
from foundry_tools.langchain import FoundryToolkit

# បង្កើតកញ្ចប់ឧបករណ៍ដែលដំណើរការដោយ Foundry
toolkit = FoundryToolkit()
toolkit.add_tool("code_analyzer", model="phi-4-mini")
toolkit.add_tool("content_summarizer", model="qwen2.5-0.5b") 
toolkit.add_tool("research_assistant", model="phi-3.5-mini")

# បង្កើតភ្នាក់ងារដោយប្រើឧបករណ៍ Foundry
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to Foundry Local tools."),
    ("user", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

agent = create_openai_functions_agent(
    llm=toolkit.get_llm(),  # ប្រើ Foundry Local ជា LLM
    tools=toolkit.get_tools(),
    prompt=prompt
)

agent_executor = AgentExecutor(agent=agent, tools=toolkit.get_tools())

# ប្រើភ្នាក់ងារ
result = await agent_executor.ainvoke({
    "input": "Analyze this Python code and summarize any issues you find"
})
```

### Semantic Kernel Integration
```python
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from foundry_tools.semantic_kernel import FoundryKernelPlugin

# ចាប់ផ្តើមកឺណែលជាមួយ Foundry Local
kernel = Kernel()

# បន្ថែម Foundry Local ជាសេវាឆាត
foundry_service = OpenAIChatCompletion(
    service_id="foundry_chat",
    ai_model_id="phi-4-mini",
    api_key="not-needed",
    base_url="http://localhost:5273/v1"
)
kernel.add_service(foundry_service)

# បង្កើត និងបន្ថែមផ្លាក់អ៊ីន Foundry
foundry_plugin = FoundryKernelPlugin()
foundry_plugin.add_function("analyze_code", model="phi-4-mini")
foundry_plugin.add_function("summarize_text", model="qwen2.5-0.5b")

kernel.add_plugin(foundry_plugin, plugin_name="foundry_tools")

# ប្រើនៅក្នុងដំណើរការរបស់ Semantic Kernel
result = await kernel.invoke(
    "foundry_tools", 
    "analyze_code",
    code="def hello(): print('world')",
    language="python"
)
```

### FastAPI Integration
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from foundry_tools.rest import FoundryRESTFramework

app = FastAPI(title="Foundry Local Tools API")

# ចាប់ផ្តើមក្របខ័ណ្ឌ REST របស់ Foundry
foundry_framework = FoundryRESTFramework()

# ចុះបញ្ជីឧបករណ៍ទាំងអស់ដែលមានដោយស្វ័យប្រវត្តិ
await foundry_framework.auto_register_tools([
    "code_analyzer",
    "content_summarizer", 
    "data_processor",
    "research_assistant"
])

# ភ្ជាប់ចំណុចបញ្ចប់របស់ Foundry
app.include_router(
    foundry_framework.get_router(),
    prefix="/api/v1/foundry",
    tags=["foundry-tools"]
)

# ចំណុចបញ្ចប់ផ្ទាល់ខ្លួនដែលប្រើឧបករណ៍ Foundry
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

# ចំណុចបញ្ចប់សម្រាប់ពិនិត្យសុខភាព
@app.get("/api/v1/health")
async def health_check():
    status = await foundry_framework.get_health_status()
    return {
        "foundry_status": status.foundry_running,
        "active_models": status.loaded_models,
        "available_tools": status.available_tools
    }
```

### Command-Line Integration
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

## គំរូខ្ពស់

### 1. ការរួមបញ្ចូលឧបករណ៍ (Tool Composition)
```python
from foundry_tools import CompositeFoundryTool

@CompositeFoundryTool(
    name="full_code_review",
    description="Comprehensive code review using multiple analysis tools"
)
async def comprehensive_code_review(code: str, language: str = "python") -> Dict[str, Any]:
    """Perform comprehensive code review using multiple tools."""
    
    # រត់វិភាគច្រើនពេលតែមួយ
    analyses = await asyncio.gather(
        call_tool("code_analyzer", code=code, language=language),
        call_tool("security_scanner", code=code, language=language),
        call_tool("performance_analyzer", code=code, language=language),
        call_tool("style_checker", code=code, language=language)
    )
    
    # សម្រួលលទ្ធផល
    return await call_tool("analysis_synthesizer", analyses=analyses)
```

### 2. ឧបករណ៍មានការយល់ដឹងពីបរិបទ (Context-Aware Tools)
```python
from foundry_tools.context import ContextAwareFoundryTool

class ProjectAnalyzerTool(ContextAwareFoundryTool):
    """Analyze entire project with context awareness."""
    
    async def execute(self, project_path: str, analysis_depth: str = "shallow") -> Dict[str, Any]:
        """Analyze project with full context."""
        
        # បង្កើតបរិបទគម្រោង
        context = await self.build_project_context(project_path)
        
        # វិភាគដោយមានបរិបទ
        return await self.foundry_call_with_context({
            "prompt": f"Analyze this {context.language} project",
            "context": context.to_dict(),
            "analysis_depth": analysis_depth
        })
    
    async def build_project_context(self, project_path: str) -> ProjectContext:
        """Build comprehensive project context."""
        # អនុវត្តនៅទីនេះ
        pass
```

### 3. ចងជើងឧបករណ៍ (Tool Chaining)
```python
from foundry_tools.chains import FoundryToolChain

# កំណត់ខ្សែឧបករណ៍សម្រាប់ការដំណើរការ​ឯកសារ
doc_processing_chain = FoundryToolChain([
    ("extract_text", {"input": "document_path"}),
    ("summarize_content", {"input": "extracted_text", "style": "outline"}),
    ("generate_keywords", {"input": "summary"}),
    ("create_metadata", {"input": ["summary", "keywords"]})
])

# អនុវត្តខ្សែ​នោះ
result = await doc_processing_chain.execute({
    "document_path": "/path/to/document.pdf"
})
```

## បង្ហាប់ប្រសិទ្ធភាព

### 1. របៀបផ្ទុកចងចាំ (Caching Strategies)
```python
from foundry_tools.cache import CacheConfig, CacheStrategy

cache_config = CacheConfig(
    strategy=CacheStrategy.LRU,
    max_size=1000,
    ttl=3600,  # 1 ម៉ោង
    key_generator="content_hash"
)

# អនុវត្តចំពោះឧបករណ៍ជាក់លាក់
@FoundryTool(
    name="cached_analyzer",
    cache_config=cache_config
)
async def cached_code_analyzer(code: str) -> Dict[str, Any]:
    # ការវិភាគដែលមានចំណាយខ្ពស់ ដែលទទួលបានអត្ថប្រយោជន៍ពីការប្រើប្រាស់ cache
    pass
```

### 2. ការគ្រប់គ្រងហូលម៉ូឌែល (Model Pool Management)
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

# កំណត់រចនាសម្ព័ន្ធបញ្ជីឧបករណ៍ជាមួយพูล
registry = FoundryToolRegistry(model_pool_config=pool_config)
```

### 3. ដំណើរការជាក្រុម (Batch Processing)
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

## ការតាមដាន និងការសង្កេត

### 1. គោលនយោបាយមេត្រីកឧបករណ៍ (Tool Metrics)
```python
from foundry_tools.monitoring import ToolMetrics

# ការប្រមូលម៉ែត្រីកដោយស្វ័យប្រវត្តិ
metrics = await ToolMetrics.get_tool_performance("code_analyzer")
print(f"Average execution time: {metrics.avg_execution_time}s")
print(f"Success rate: {metrics.success_rate}%")
print(f"Cache hit rate: {metrics.cache_hit_rate}%")
```

### 2. ការតាមដានសុខភាព (Health Monitoring)
```python
from foundry_tools.health import HealthMonitor

health_monitor = HealthMonitor()

# ត្រួតពិនិត្យសុខភាពនៃឧបករណ៍
health_status = await health_monitor.check_all_tools()
print(f"Healthy tools: {health_status.healthy_count}")
print(f"Failed tools: {health_status.failed_tools}")
```

### 3. វិភាគការប្រើប្រាស់ (Usage Analytics)
```python
from foundry_tools.analytics import UsageAnalytics

analytics = UsageAnalytics()

# តាមដានលំនាំការប្រើប្រាស់ឧបករណ៍
usage_report = await analytics.generate_usage_report(
    start_date="2024-01-01",
    end_date="2024-01-31"
)

print(f"Most used tool: {usage_report.most_used_tool}")
print(f"Peak usage time: {usage_report.peak_usage_time}")
```

## អ្វីដែលត្រូវរៀន

បន្ទាប់ពីបញ្ចប់ឧទាហរណ៍នេះ អ្នកនឹងយល់ដឹង៖

1. **Tool Integration Patterns**
   - ការរចនាឧបករណ៍ជាមុខងារ និងជាបណ្ណាសារ
   - គំរូរួមបញ្ចូល Microsoft Foundry Local
   - ការផ្ទៀងផ្ទាត់ស្កីម៉ា និងសុវត្ថិភាពប្រភេទ
   - ការដោះស្រាយកំហុស និងការស្ដារឡើងវិញ

2. **Framework Integration**
   - ការអភិវឌ្ឍឧបករណ៍ LangChain
   - ការរួមបញ្ចូលមុខងារ Semantic Kernel
   - ការរួមបញ្ចូលក្នុង REST API framework
   - ការអភិវឌ្ឍកម្មវិធី CLI

3. **Production Considerations**
   - យុទ្ធសាស្ត្របង្ហាប់ប្រសិទ្ធភាព
   - ការផ្ទុកចងចាំ និងការគ្រប់គ្រងធនធាន
   - ការតាមដាន និងការសង្កេត
   - សុវត្ថិភាព និងការផ្ទៀងផ្ទាត់

4. **Advanced Tool Patterns**
   - ការរួមបញ្ចូល និងចងជើងឧបករណ៍
   - ការដំណើរការដែលយល់ដឹងពីបរិបទ
   - ដំណើរការជាក្រុម និងបញ្ជូនបន្ត
   - ការអភិវឌ្ឍន៍ការរួមបញ្ចូលផ្ទាល់ខ្លួន

## ជំហានបន្ទាប់

- **Integration Projects**: បង្កើតការរួមបញ្ចូលផ្ទាល់ខ្លួនជាមួយ framework ដែលអ្នកចូលចិត្ត
- **Tool Development**: បង្កើតឧបករណ៍ជាក់លាក់សម្រាប់ដែនរបស់អ្នក
- **Performance Tuning**: បើកបរិមាណប្រសិទ្ធភាពសម្រាប់ករណីប្រើប្រាស់របស់អ្នក
- **Production Deployment**: ពង្រីកឧបករណ៍សម្រាប់ការប្រើប្រាស់ក្រុមហ៊ុន

## Contributing

មើលលក្ខខណ្ឌឃ្លាំងគម្រោងសក្តិសមនៃ repository សម្រាប់សេចក្តីណែនាំអំពីការរួមចំណែក។

## License

ឧទាហរណ៍នេះអនុវត្តសិទ្ធិបញ្ញាស្រដៀងគ្នាជាមួយគម្រោង Microsoft Foundry Local។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែដោយ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំអោយបានត្រឹមត្រូវ សូមយល់ឲ្យបានថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមាតុភូមិគួរត្រូវបានចាត់ទុកជាប្រភពដែលមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ សូមពិចារណាឲ្យមានការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->