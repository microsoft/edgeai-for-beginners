# Foundry Local เป็นเครื่องมือสำหรับการผสานรวม

กรอบการทำงานที่ครอบคลุมสำหรับการผสานรวม Microsoft Foundry Local เป็นเครื่องมือที่เรียกใช้งานได้ภายในแอปพลิเคชันขนาดใหญ่ โดยปฏิบัติตามรูปแบบการผสานรวม AI แบบใช้เครื่องมือของ Microsoft อย่างเป็นทางการ

## ภาพรวม

ตัวอย่างนี้แสดงให้เห็นวิธีการเปิดเผยโมเดล Foundry Local เป็นเครื่องมือที่นำกลับมาใช้ใหม่ได้ ซึ่งสามารถผสานรวมเข้ากับแอปพลิเคชัน เวิร์กโฟลว์ และสภาพแวดล้อมการพัฒนาเดิมได้ โดยแสดงรูปแบบที่ Microsoft แนะนำสำหรับการผสานรวมเครื่องมือและการเรียกใช้งานฟังก์ชัน

## แนวคิดสำคัญ

### 🔧 **สถาปัตยกรรมที่เน้นเครื่องมือ**
- โมเดล Foundry Local ในรูปแบบฟังก์ชันที่เรียกใช้งานได้
- อินเทอร์เฟซและสคีมาของเครื่องมือที่ได้มาตรฐาน
- การผสานรวมที่ราบรื่นกับฐานโค้ดที่มีอยู่
- การกำหนดและตรวจสอบเครื่องมือที่ปลอดภัยต่อประเภทข้อมูล

### ⚡ **รูปแบบการเรียกใช้งานฟังก์ชัน**
- การเรียกใช้งานฟังก์ชันของ Microsoft Foundry Local
- การกำหนดเครื่องมือที่เข้ากันได้กับ OpenAI
- การตรวจสอบและแปลงพารามิเตอร์อัตโนมัติ
- การจัดการข้อผิดพลาดและการจัดรูปแบบการตอบกลับ

### 🔌 **กรอบการผสานรวม**
- **การผสานรวม LangChain**: รองรับเครื่องมือ LangChain โดยตรง
- **Semantic Kernel**: ฟังก์ชัน Microsoft Semantic Kernel
- **REST API**: จุดเชื่อมต่อเครื่องมือผ่าน HTTP
- **CLI Tools**: การผสานรวมผ่านอินเทอร์เฟซบรรทัดคำสั่ง
- **Jupyter Notebooks**: เครื่องมือพัฒนาที่ใช้งานแบบโต้ตอบ

### 🎯 **รูปแบบการใช้งาน**
- เครื่องมือวิเคราะห์และสร้างโค้ด
- การประมวลผลและสรุปเนื้อหา
- การวิเคราะห์และการแสดงผลข้อมูล
- การค้นคว้าและการดึงข้อมูล
- ระบบสนับสนุนการตัดสินใจ

## สถาปัตยกรรม

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

## ข้อกำหนดเบื้องต้น

### ความต้องการของระบบ
- **Python**: 3.9+ พร้อมรองรับ asyncio
- **Node.js**: v18+ (สำหรับการผสานรวม JavaScript)
- **หน่วยความจำ**: แนะนำ 12GB ขึ้นไป
- **พื้นที่จัดเก็บ**: 10GB ขึ้นไปสำหรับโมเดลและเครื่องมือ

### การพึ่งพาหลัก
```bash
pip install foundry-local-sdk openai langchain semantic-kernel fastapi uvicorn typer rich
```

### การพึ่งพาเฉพาะกรอบการทำงาน
```bash
# LangChain integration
pip install langchain-openai langchain-community

# Semantic Kernel integration  
pip install semantic-kernel

# Web framework integration
pip install fastapi uvicorn streamlit gradio

# Development tools
pip install jupyter ipywidgets
```

## เริ่มต้นใช้งานอย่างรวดเร็ว

### 1. การสร้างเครื่องมือพื้นฐาน
```python
from foundry_tools import FoundryTool, FoundryToolRegistry

# Create a simple analysis tool
@FoundryTool(
    name="code_analyzer",
    description="Analyze code quality and suggest improvements",
    model="phi-4-mini"
)
async def analyze_code(code: str, language: str = "python") -> dict:
    """Analyze code and return quality metrics and suggestions."""
    pass

# Register and use the tool
registry = FoundryToolRegistry()
await registry.register(analyze_code)

result = await registry.call("code_analyzer", {
    "code": "def hello(): print('world')",
    "language": "python"
})
```

### 2. การผสานรวม LangChain
```python
from langchain.tools import BaseTool
from foundry_tools.langchain import FoundryLangChainTool

# Create LangChain-compatible tool
class CodeAnalyzerTool(FoundryLangChainTool):
    name = "code_analyzer"
    description = "Analyze code quality using Foundry Local"
    model = "phi-4-mini"
    
    async def _arun(self, code: str, language: str = "python") -> str:
        return await self.foundry_call({
            "code": code,
            "language": language
        })

# Use with LangChain agents
from langchain.agents import initialize_agent, AgentType

tools = [CodeAnalyzerTool()]
agent = initialize_agent(
    tools=tools,
    llm=None,  # Uses Foundry Local
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)
```

### 3. การผสานรวม REST API
```python
from fastapi import FastAPI
from foundry_tools.rest import FoundryRESTEndpoint

app = FastAPI()

# Auto-generate REST endpoints from Foundry tools
foundry_api = FoundryRESTEndpoint()
await foundry_api.register_tool("code_analyzer", analyze_code)

# Mount endpoints
app.include_router(foundry_api.router, prefix="/foundry/v1")

# Use via HTTP
# POST /foundry/v1/code_analyzer
# {
#   "code": "def hello(): print('world')",
#   "language": "python"
# }
```

## โครงสร้างโครงการ

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

## รูปแบบเครื่องมือหลัก

### 1. เครื่องมือที่ใช้ฟังก์ชัน
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
    
    # The decorator automatically handles:
    # - Parameter validation
    # - Foundry Local client setup
    # - Error handling and logging
    # - Response formatting
    
    system_prompt = f"""
    Summarize the following content into {max_points} key points.
    Use {style} format for the summary.
    """
    
    # This gets automatically routed to Foundry Local
    return {
        "summary": "Generated summary here...",
        "points": max_points,
        "style": style,
        "word_count": len(content.split())
    }
```

### 2. เครื่องมือที่ใช้คลาส
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
        
        # Check cache
        cache_key = f"{hash(code)}_{language}_{analysis_type}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        # Perform analysis using Foundry Local
        result = await self.foundry_call({
            "system_prompt": f"Analyze this {language} code for {analysis_type} analysis",
            "user_prompt": f"Code to analyze:\n\n```{language}\n{code}\n```",
            "max_tokens": 1000
        })
        
        # Process and cache result
        analysis_result = self.process_analysis_result(result, analysis_type)
        self.analysis_cache[cache_key] = analysis_result
        
        return analysis_result
    
    def process_analysis_result(self, raw_result: str, analysis_type: str) -> Dict[str, Any]:
        """Process the raw analysis result into structured data."""
        # Implementation here
        pass
```

### 3. เครื่องมือแบบสตรีมมิ่ง
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
    
    # Yield metadata first
    yield {
        "type": "metadata",
        "language": language,
        "include_tests": include_tests,
        "estimated_lines": 50
    }
    
    # Stream code generation
    async for chunk in foundry_stream({
        "prompt": f"Generate {language} code: {specification}",
        "stream": True
    }):
        yield {
            "type": "code_chunk",
            "content": chunk.content,
            "complete": chunk.finish_reason is not None
        }
    
    # Yield final result
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

## ตัวอย่างการผสานรวม

### การผสานรวม LangChain
```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate
from foundry_tools.langchain import FoundryToolkit

# Create Foundry-powered toolkit
toolkit = FoundryToolkit()
toolkit.add_tool("code_analyzer", model="phi-4-mini")
toolkit.add_tool("content_summarizer", model="qwen2.5-0.5b") 
toolkit.add_tool("research_assistant", model="phi-3.5-mini")

# Create agent with Foundry tools
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to Foundry Local tools."),
    ("user", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

agent = create_openai_functions_agent(
    llm=toolkit.get_llm(),  # Uses Foundry Local as LLM
    tools=toolkit.get_tools(),
    prompt=prompt
)

agent_executor = AgentExecutor(agent=agent, tools=toolkit.get_tools())

# Use the agent
result = await agent_executor.ainvoke({
    "input": "Analyze this Python code and summarize any issues you find"
})
```

### การผสานรวม Semantic Kernel
```python
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from foundry_tools.semantic_kernel import FoundryKernelPlugin

# Initialize kernel with Foundry Local
kernel = Kernel()

# Add Foundry Local as chat service
foundry_service = OpenAIChatCompletion(
    service_id="foundry_chat",
    ai_model_id="phi-4-mini",
    api_key="not-needed",
    base_url="http://localhost:5273/v1"
)
kernel.add_service(foundry_service)

# Create and add Foundry plugin
foundry_plugin = FoundryKernelPlugin()
foundry_plugin.add_function("analyze_code", model="phi-4-mini")
foundry_plugin.add_function("summarize_text", model="qwen2.5-0.5b")

kernel.add_plugin(foundry_plugin, plugin_name="foundry_tools")

# Use in Semantic Kernel workflows
result = await kernel.invoke(
    "foundry_tools", 
    "analyze_code",
    code="def hello(): print('world')",
    language="python"
)
```

### การผสานรวม FastAPI
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from foundry_tools.rest import FoundryRESTFramework

app = FastAPI(title="Foundry Local Tools API")

# Initialize Foundry REST framework
foundry_framework = FoundryRESTFramework()

# Auto-register all available tools
await foundry_framework.auto_register_tools([
    "code_analyzer",
    "content_summarizer", 
    "data_processor",
    "research_assistant"
])

# Mount Foundry endpoints
app.include_router(
    foundry_framework.get_router(),
    prefix="/api/v1/foundry",
    tags=["foundry-tools"]
)

# Custom endpoint using Foundry tools
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

# Health check endpoint
@app.get("/api/v1/health")
async def health_check():
    status = await foundry_framework.get_health_status()
    return {
        "foundry_status": status.foundry_running,
        "active_models": status.loaded_models,
        "available_tools": status.available_tools
    }
```

### การผสานรวมผ่านบรรทัดคำสั่ง
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

## รูปแบบขั้นสูง

### 1. การประกอบเครื่องมือ
```python
from foundry_tools import CompositeFoundryTool

@CompositeFoundryTool(
    name="full_code_review",
    description="Comprehensive code review using multiple analysis tools"
)
async def comprehensive_code_review(code: str, language: str = "python") -> Dict[str, Any]:
    """Perform comprehensive code review using multiple tools."""
    
    # Run multiple analyses in parallel
    analyses = await asyncio.gather(
        call_tool("code_analyzer", code=code, language=language),
        call_tool("security_scanner", code=code, language=language),
        call_tool("performance_analyzer", code=code, language=language),
        call_tool("style_checker", code=code, language=language)
    )
    
    # Synthesize results
    return await call_tool("analysis_synthesizer", analyses=analyses)
```

### 2. เครื่องมือที่รับรู้บริบท
```python
from foundry_tools.context import ContextAwareFoundryTool

class ProjectAnalyzerTool(ContextAwareFoundryTool):
    """Analyze entire project with context awareness."""
    
    async def execute(self, project_path: str, analysis_depth: str = "shallow") -> Dict[str, Any]:
        """Analyze project with full context."""
        
        # Build project context
        context = await self.build_project_context(project_path)
        
        # Analyze with context
        return await self.foundry_call_with_context({
            "prompt": f"Analyze this {context.language} project",
            "context": context.to_dict(),
            "analysis_depth": analysis_depth
        })
    
    async def build_project_context(self, project_path: str) -> ProjectContext:
        """Build comprehensive project context."""
        # Implementation here
        pass
```

### 3. การเชื่อมโยงเครื่องมือ
```python
from foundry_tools.chains import FoundryToolChain

# Define a tool chain for document processing
doc_processing_chain = FoundryToolChain([
    ("extract_text", {"input": "document_path"}),
    ("summarize_content", {"input": "extracted_text", "style": "outline"}),
    ("generate_keywords", {"input": "summary"}),
    ("create_metadata", {"input": ["summary", "keywords"]})
])

# Execute the chain
result = await doc_processing_chain.execute({
    "document_path": "/path/to/document.pdf"
})
```

## การปรับปรุงประสิทธิภาพ

### 1. กลยุทธ์การแคช
```python
from foundry_tools.cache import CacheConfig, CacheStrategy

cache_config = CacheConfig(
    strategy=CacheStrategy.LRU,
    max_size=1000,
    ttl=3600,  # 1 hour
    key_generator="content_hash"
)

# Apply to specific tools
@FoundryTool(
    name="cached_analyzer",
    cache_config=cache_config
)
async def cached_code_analyzer(code: str) -> Dict[str, Any]:
    # Expensive analysis that benefits from caching
    pass
```

### 2. การจัดการกลุ่มโมเดล
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

# Configure tool registry with pool
registry = FoundryToolRegistry(model_pool_config=pool_config)
```

### 3. การประมวลผลแบบแบตช์
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

## การตรวจสอบและการสังเกตการณ์

### 1. เมตริกของเครื่องมือ
```python
from foundry_tools.monitoring import ToolMetrics

# Automatic metrics collection
metrics = await ToolMetrics.get_tool_performance("code_analyzer")
print(f"Average execution time: {metrics.avg_execution_time}s")
print(f"Success rate: {metrics.success_rate}%")
print(f"Cache hit rate: {metrics.cache_hit_rate}%")
```

### 2. การตรวจสอบสุขภาพ
```python
from foundry_tools.health import HealthMonitor

health_monitor = HealthMonitor()

# Monitor tool health
health_status = await health_monitor.check_all_tools()
print(f"Healthy tools: {health_status.healthy_count}")
print(f"Failed tools: {health_status.failed_tools}")
```

### 3. การวิเคราะห์การใช้งาน
```python
from foundry_tools.analytics import UsageAnalytics

analytics = UsageAnalytics()

# Track tool usage patterns
usage_report = await analytics.generate_usage_report(
    start_date="2024-01-01",
    end_date="2024-01-31"
)

print(f"Most used tool: {usage_report.most_used_tool}")
print(f"Peak usage time: {usage_report.peak_usage_time}")
```

## ผลลัพธ์การเรียนรู้

หลังจากทำตัวอย่างนี้เสร็จ คุณจะเข้าใจ:

1. **รูปแบบการผสานรวมเครื่องมือ**
   - การออกแบบเครื่องมือที่ใช้ฟังก์ชันและคลาส
   - รูปแบบการผสานรวม Microsoft Foundry Local
   - การตรวจสอบสคีมาและความปลอดภัยของประเภทข้อมูล
   - การจัดการข้อผิดพลาดและการกู้คืน

2. **การผสานรวมกรอบการทำงาน**
   - การพัฒนาเครื่องมือ LangChain
   - การผสานรวมฟังก์ชัน Semantic Kernel
   - การผสานรวมกรอบ REST API
   - การพัฒนาแอปพลิเคชัน CLI

3. **ข้อควรพิจารณาสำหรับการใช้งานจริง**
   - กลยุทธ์การปรับปรุงประสิทธิภาพ
   - การจัดการแคชและทรัพยากร
   - การตรวจสอบและการสังเกตการณ์
   - ความปลอดภัยและการตรวจสอบ

4. **รูปแบบเครื่องมือขั้นสูง**
   - การประกอบและการเชื่อมโยงเครื่องมือ
   - การประมวลผลที่รับรู้บริบท
   - การดำเนินการแบบแบตช์และสตรีมมิ่ง
   - การพัฒนาการผสานรวมแบบกำหนดเอง

## ขั้นตอนถัดไป

- **โครงการผสานรวม**: สร้างการผสานรวมแบบกำหนดเองกับกรอบการทำงานที่คุณชื่นชอบ
- **การพัฒนาเครื่องมือ**: สร้างเครื่องมือเฉพาะสำหรับโดเมนของคุณ
- **การปรับแต่งประสิทธิภาพ**: ปรับปรุงให้เหมาะสมกับกรณีการใช้งานเฉพาะของคุณ
- **การใช้งานในระดับผลิต**: ขยายเครื่องมือสำหรับการใช้งานในองค์กร

## การมีส่วนร่วม

ดูแนวทางในที่เก็บหลักสำหรับคำแนะนำในการมีส่วนร่วม

## ใบอนุญาต

ตัวอย่างนี้ใช้ใบอนุญาตเดียวกันกับโครงการ Microsoft Foundry Local

---

