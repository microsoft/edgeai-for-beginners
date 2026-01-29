# மல்டி-ஏஜென்ட் ஒர்கெஸ்ட்ரேஷன் சிஸ்டம் - Foundry Local

Microsoft Foundry Local மூலம் இயக்கப்படும் ஒரு மேம்பட்ட மல்டி-ஏஜென்ட் சிஸ்டம், புத்திசாலியான ஏஜென்ட் ஒருங்கிணைப்பு, சிறப்பு பணிகளை ஒதுக்கல் மற்றும் கூட்டுறவு பிரச்சினை தீர்வு முறைகளை வெளிப்படுத்துகிறது.

## கண்ணோட்டம்

இந்த மாதிரி Foundry Local-ஐப் பயன்படுத்தி மேம்பட்ட AI ஏஜென்ட் சிஸ்டங்களை உருவாக்குவது எப்படி என்பதை காட்டுகிறது, Microsoft-இன் அதிகாரப்பூர்வ முறைகளை செயல்படுத்துகிறது, செயல்பாட்டு அழைப்பு, ஏஜென்ட் ஒர்கெஸ்ட்ரேஷன் மற்றும் கூட்டுறவு AI வேலைவழிகளை உள்ளடக்கியது.

## கட்டமைப்பு

```
┌─────────────────────────────────────────────────────────────────┐
│                    Agent Orchestration System                   │
├─────────────────┬─────────────────┬─────────────────┬───────────┤
│  Coordinator    │   Specialist    │    Function     │  Context  │
│     Agent       │     Agents      │     Registry    │  Manager  │
│                 │                 │                 │           │
│ • Task Analysis │ • Code Expert   │ • Tool Calling  │ • Memory  │
│ • Agent Router  │ • Data Analyst  │ • Validation    │ • History │
│ • Workflow Mgmt │ • Research Bot  │ • Error Handle  │ • State   │
│ • Result Merge  │ • Writing Aid   │ • Type Safety   │ • Context │
└─────────────────┴─────────────────┴─────────────────┴───────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                Microsoft Foundry Local Service                  │
│                                                                 │
│ • Multi-Model Support     • Function Calling API               │
│ • Concurrent Inference    • Tool Integration                   │
│ • Context Preservation    • Performance Monitoring             │
└─────────────────────────────────────────────────────────────────┘
```

## முக்கிய அம்சங்கள்

### 🤖 **புத்திசாலியான ஏஜென்ட் ஒருங்கிணைப்பு**
- மாறும் பணிகளை பகுப்பாய்வு மற்றும் ஏஜென்ட் தேர்வு
- தானியங்கி பணிச்சுமை பகிர்வு
- முடிவுகளை தொகுத்தல் மற்றும் ஒருங்கிணைப்பு
- ஏஜென்ட் இடையேயான தொடர்பு நெறிமுறைகள்

### 🔧 **சிறப்பு ஏஜென்ட் வகைகள்**
- **கோடு நிபுணர்**: நிரலாக்கம், பிழை திருத்தம், கோடு மதிப்பீடு
- **தரவு பகுப்பாய்வாளர்**: தரவு செயலாக்கம், காட்சிப்படுத்தல், உள்ளடக்கங்கள்
- **ஆராய்ச்சி உதவியாளர்**: தகவல் சேகரிப்பு, சுருக்கம்
- **எழுதும் நிபுணர்**: உள்ளடக்க உருவாக்கம், திருத்தம், ஆவணங்கள்
- **பிரச்சினை தீர்க்கும் நிபுணர்**: சிக்கலான காரணம், முடிவெடுக்கும் திறன்

### ⚡ **மேம்பட்ட செயல்பாட்டு அழைப்பு**
- Microsoft Foundry Local செயல்பாட்டு அழைப்பு முறைகள்
- வகை-பாதுகாப்பான கருவி வரையறைகள்
- தானியங்கி அளவுரு சரிபார்ப்பு
- பிழை கையாளல் மற்றும் மீட்பு
- கருவி சங்கிலி மற்றும் அமைப்பு

### 🎯 **சிறந்த பணி வழிமாற்று**
- நோக்கம் வகைப்படுத்தல் மற்றும் பகுப்பாய்வு
- ஏஜென்ட் திறன் பொருத்தம்
- சுமை சமநிலை மற்றும் மேம்பாடு
- மாற்று மற்றும் மீட்பு கையாளல்

## முன் தேவைகள்

### சிஸ்டம் தேவைகள்
- **Python**: 3.9+ asyncio ஆதரவு கொண்டது
- **மெமரி**: பல ஏஜென்ட்களுக்கு 16GB+ பரிந்துரைக்கப்படுகிறது
- **சேமிப்பு**: பல மாதிரிகளுக்கு 15GB+ 
- **CPU/GPU**: பல கோர் செயலி, GPU பரிந்துரைக்கப்படுகிறது

### சார்புகள்
```bash
pip install foundry-local-sdk openai aiohttp asyncio pydantic rich typer
```

### Foundry Local அமைப்பு
```powershell
# Install and verify Foundry Local
winget install Microsoft.FoundryLocal
foundry --version

# Download recommended models for agents
foundry model download phi-4-mini
foundry model download qwen2.5-coder-0.5b
foundry model download phi-3.5-mini
```

## விரைவான தொடக்கம்

### 1. அடிப்படை மல்டி-ஏஜென்ட் வேலைவழி
```python
from agentic_system import AgentOrchestrator, CodeAgent, ResearchAgent

# Initialize the orchestrator
orchestrator = AgentOrchestrator()

# Add specialized agents
await orchestrator.add_agent(CodeAgent("phi-4-mini"))
await orchestrator.add_agent(ResearchAgent("qwen2.5-coder-0.5b"))

# Execute a complex task
result = await orchestrator.execute_task(
    "Create a Python script that analyzes web traffic data and generates a report"
)

print(result.summary)
```

### 2. தனிப்பயன் ஏஜென்ட் உருவாக்கம்
```python
from agentic_system import BaseAgent, tool

class DataAnalystAgent(BaseAgent):
    """Specialized agent for data analysis tasks."""
    
    @tool
    async def analyze_dataset(self, data_path: str, analysis_type: str) -> dict:
        """Analyze a dataset and return insights."""
        # Implementation here
        pass
    
    @tool
    async def create_visualization(self, data: dict, chart_type: str) -> str:
        """Create data visualizations."""
        # Implementation here
        pass

# Use the custom agent
agent = DataAnalystAgent("qwen2.5-0.5b")
result = await agent.analyze_dataset("sales_data.csv", "trend_analysis")
```

### 3. செயல்பாட்டு அழைப்பு ஒருங்கிணைப்பு
```python
# Define tools following Microsoft patterns
tools = [
    {
        "name": "web_search",
        "description": "Search the web for information",
        "parameters": {
            "query": {"description": "Search query", "type": "string"},
            "max_results": {"description": "Maximum results", "type": "integer"}
        }
    },
    {
        "name": "code_analyzer", 
        "description": "Analyze code quality and suggest improvements",
        "parameters": {
            "code": {"description": "Code to analyze", "type": "string"},
            "language": {"description": "Programming language", "type": "string"}
        }
    }
]

# Register tools with orchestrator
orchestrator.register_tools(tools)
```

## திட்ட அமைப்பு

```
09/
├── README.md                    # This documentation
├── requirements.txt             # Python dependencies  
├── agentic_system/
│   ├── __init__.py             # Package initialization
│   ├── orchestrator.py         # Main orchestrator class
│   ├── base_agent.py           # Base agent implementation
│   ├── specialized_agents/
│   │   ├── __init__.py
│   │   ├── code_agent.py       # Programming specialist
│   │   ├── research_agent.py   # Research specialist  
│   │   ├── data_agent.py       # Data analysis specialist
│   │   ├── writing_agent.py    # Content creation specialist
│   │   └── solver_agent.py     # Problem solving specialist
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── function_registry.py # Tool management
│   │   ├── web_tools.py        # Web interaction tools
│   │   ├── file_tools.py       # File system tools
│   │   ├── code_tools.py       # Code analysis tools
│   │   └── data_tools.py       # Data processing tools
│   ├── coordination/
│   │   ├── __init__.py
│   │   ├── task_router.py      # Task routing logic
│   │   ├── result_merger.py    # Result aggregation
│   │   ├── context_manager.py  # Context and memory
│   │   └── workflow_engine.py  # Workflow management
│   └── utils/
│       ├── __init__.py
│       ├── foundry_client.py   # Foundry Local integration
│       ├── logging_config.py   # Logging setup
│       └── validation.py       # Input validation
├── examples/
│   ├── basic_coordination.py   # Simple multi-agent example
│   ├── complex_workflow.py     # Advanced workflow example
│   ├── custom_agents.py        # Custom agent creation
│   ├── function_calling.py     # Tool integration example
│   └── interactive_demo.py     # Interactive demonstration
├── tools/
│   ├── web_search.py          # Web search implementation
│   ├── code_analyzer.py       # Code analysis tools
│   ├── data_processor.py      # Data processing tools
│   └── file_manager.py        # File system operations
└── tests/
    ├── test_orchestrator.py   # Orchestrator tests
    ├── test_agents.py         # Agent tests
    ├── test_tools.py          # Tool tests
    └── test_integration.py    # Integration tests
```

## ஏஜென்ட் வகைகள் விரிவான பார்வை

### 1. கோடு நிபுணர் ஏஜென்ட்
```python
class CodeAgent(BaseAgent):
    """Expert in programming, debugging, and code review."""
    
    specialties = [
        "code_generation", "debugging", "code_review", 
        "refactoring", "testing", "documentation"
    ]
    
    @tool
    async def generate_code(self, specification: str, language: str) -> str:
        """Generate code from specifications."""
        
    @tool  
    async def debug_code(self, code: str, error_message: str) -> dict:
        """Debug code and suggest fixes."""
        
    @tool
    async def review_code(self, code: str, criteria: list) -> dict:
        """Perform comprehensive code review."""
```

### 2. ஆராய்ச்சி உதவியாளர் ஏஜென்ட்
```python
class ResearchAgent(BaseAgent):
    """Specialized in information gathering and analysis."""
    
    specialties = [
        "web_research", "information_synthesis", "fact_checking",
        "summarization", "trend_analysis"
    ]
    
    @tool
    async def research_topic(self, topic: str, depth: str) -> dict:
        """Research a topic comprehensively."""
        
    @tool
    async def summarize_information(self, sources: list, style: str) -> str:
        """Summarize information from multiple sources."""
        
    @tool
    async def fact_check(self, claims: list) -> dict:
        """Verify factual claims."""
```

### 3. தரவு பகுப்பாய்வு ஏஜென்ட்
```python
class DataAgent(BaseAgent):
    """Expert in data processing and analysis."""
    
    specialties = [
        "data_analysis", "statistical_analysis", "visualization",
        "pattern_recognition", "predictive_modeling"
    ]
    
    @tool
    async def analyze_data(self, dataset: str, analysis_type: str) -> dict:
        """Perform data analysis."""
        
    @tool
    async def create_visualization(self, data: dict, viz_type: str) -> str:
        """Create data visualizations."""
        
    @tool
    async def statistical_test(self, data: dict, test_type: str) -> dict:
        """Perform statistical tests."""
```

## ஒர்கெஸ்ட்ரேஷன் முறைகள்

### 1. தொடர் வேலைவழி
```python
# Define a sequential workflow
workflow = orchestrator.create_workflow("sequential")
workflow.add_step("research", ResearchAgent, "gather_requirements")
workflow.add_step("design", CodeAgent, "create_architecture")  
workflow.add_step("implement", CodeAgent, "write_code")
workflow.add_step("test", CodeAgent, "create_tests")

result = await workflow.execute("Build a REST API for user management")
```

### 2. இணைச் செயல்பாடு
```python
# Execute tasks in parallel
parallel_tasks = [
    ("research_market", ResearchAgent, "analyze_market_trends"),
    ("analyze_competitors", DataAgent, "competitor_analysis"),
    ("technical_feasibility", CodeAgent, "assess_technical_requirements")
]

results = await orchestrator.execute_parallel(parallel_tasks)
synthesized = await orchestrator.synthesize_results(results)
```

### 3. மாறும் ஏஜென்ட் தேர்வு
```python
# Automatic agent selection based on task analysis
task = "Create a machine learning model to predict customer churn"

# Orchestrator analyzes task and selects appropriate agents
selected_agents = await orchestrator.analyze_task_requirements(task)
# Returns: [DataAgent, CodeAgent, ResearchAgent]

result = await orchestrator.execute_with_agents(task, selected_agents)
```

## செயல்பாட்டு அழைப்பு ஒருங்கிணைப்பு

### Microsoft Foundry Local முறைகள்
```python
# Define tools following Microsoft's function calling schema
def define_foundry_tools():
    return [
        {
            "name": "analyze_code_quality",
            "description": "Analyze code quality and suggest improvements",
            "parameters": {
                "code": {
                    "description": "The source code to analyze",
                    "type": "string"
                },
                "language": {
                    "description": "Programming language",
                    "type": "string"
                },
                "criteria": {
                    "description": "Analysis criteria",
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },
        {
            "name": "search_documentation",
            "description": "Search technical documentation",
            "parameters": {
                "query": {"description": "Search query", "type": "string"},
                "source": {"description": "Documentation source", "type": "string"}
            }
        }
    ]

# Integration with Foundry Local
async def setup_function_calling():
    tools = define_foundry_tools()
    
    # Configure Foundry Local for function calling
    client = openai.OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Use tools in conversation
    response = await client.chat.completions.create(
        model=manager.get_model_info("phi-4-mini").id,
        messages=[
            {"role": "user", "content": "Analyze this Python code for quality issues"}
        ],
        tools=[{"type": "function", "function": tool} for tool in tools],
        tool_choice="auto"
    )
```

## மேம்பட்ட ஒருங்கிணைப்பு அம்சங்கள்

### 1. சூழல் மேலாண்மை
```python
class ContextManager:
    """Manages shared context across agents."""
    
    async def share_context(self, agent_id: str, context: dict):
        """Share context with specific agent."""
        
    async def get_shared_memory(self) -> dict:
        """Retrieve shared memory state."""
        
    async def update_global_state(self, updates: dict):
        """Update global orchestrator state."""
```

### 2. முடிவுகளை ஒருங்கிணைப்பு
```python
class ResultMerger:
    """Intelligently merge results from multiple agents."""
    
    async def merge_analyses(self, results: list) -> dict:
        """Merge analysis results."""
        
    async def resolve_conflicts(self, conflicting_results: list) -> dict:
        """Resolve conflicting agent outputs."""
        
    async def create_summary(self, all_results: dict) -> str:
        """Create comprehensive summary."""
```

### 3. தர உறுதிப்பாடு
```python
class QualityController:
    """Ensures output quality and consistency."""
    
    async def validate_output(self, result: dict, criteria: list) -> bool:
        """Validate agent output quality."""
        
    async def cross_check_facts(self, claims: list) -> dict:
        """Cross-verify facts across agents."""
        
    async def ensure_consistency(self, outputs: list) -> dict:
        """Ensure consistent outputs."""
```

## செயல்திறன் மேம்பாடு

### 1. மாதிரி சுமை சமநிலை
```python
# Distribute models across agents for optimal resource usage
model_allocation = {
    "code_tasks": "phi-4-mini",
    "research_tasks": "qwen2.5-coder-0.5b", 
    "analysis_tasks": "phi-3.5-mini",
    "general_tasks": "phi-4-mini"
}

orchestrator.configure_model_allocation(model_allocation)
```

### 2. கேஷிங் மற்றும் மெமரி
```python
# Implement intelligent caching
cache_config = {
    "response_cache": True,
    "context_cache": True,
    "tool_result_cache": True,
    "cache_ttl": 3600  # 1 hour
}

orchestrator.configure_caching(cache_config)
```

### 3. ஒரே நேரத்தில் செயல்பாடு
```python
# Optimize for parallel processing
concurrency_config = {
    "max_concurrent_agents": 4,
    "agent_pool_size": 8,
    "task_queue_size": 100,
    "timeout_seconds": 300
}

orchestrator.configure_concurrency(concurrency_config)
```

## பயன்பாட்டு உதாரணங்கள்

### உதாரணம் 1: மென்பொருள் மேம்பாட்டு வேலைவழி
```python
async def software_development_workflow():
    """Complete software development using multiple agents."""
    
    # Initialize orchestrator with specialized agents
    orchestrator = AgentOrchestrator()
    await orchestrator.add_agent(ResearchAgent("qwen2.5-coder-0.5b"))
    await orchestrator.add_agent(CodeAgent("phi-4-mini"))
    await orchestrator.add_agent(DataAgent("phi-3.5-mini"))
    
    # Define the development task
    task = """
    Create a web application that:
    1. Analyzes user behavior data
    2. Provides real-time analytics dashboard
    3. Includes user authentication
    4. Has comprehensive tests
    """
    
    # Execute coordinated workflow
    result = await orchestrator.execute_workflow(
        task=task,
        workflow_type="software_development",
        quality_gates=["code_review", "testing", "security_check"]
    )
    
    return result
```

### உதாரணம் 2: ஆராய்ச்சி மற்றும் பகுப்பாய்வு
```python
async def comprehensive_research():
    """Multi-agent research coordination."""
    
    research_query = "Impact of AI on software development productivity"
    
    # Parallel research execution
    tasks = [
        ("literature_review", ResearchAgent, research_query),
        ("data_analysis", DataAgent, "productivity_metrics"),
        ("case_studies", ResearchAgent, "ai_adoption_cases"),
        ("technical_analysis", CodeAgent, "ai_tool_evaluation")
    ]
    
    results = await orchestrator.execute_parallel(tasks)
    
    # Synthesize findings
    final_report = await orchestrator.synthesize_research(
        results=results,
        format="comprehensive_report",
        include_recommendations=True
    )
    
    return final_report
```

### உதாரணம் 3: பிரச்சினை தீர்க்கும் அமர்வு
```python
async def collaborative_problem_solving():
    """Multi-agent collaborative problem solving."""
    
    problem = """
    A company's API response times have increased 300% over the past month.
    Analyze the issue and propose solutions.
    """
    
    # Deploy specialist agents
    investigation_plan = await orchestrator.create_investigation_plan(problem)
    
    agents_deployed = [
        (CodeAgent, "analyze_code_performance"),
        (DataAgent, "analyze_performance_metrics"), 
        (ResearchAgent, "research_similar_issues"),
        (SolverAgent, "propose_solutions")
    ]
    
    # Coordinate investigation
    findings = await orchestrator.coordinate_investigation(
        problem=problem,
        agents=agents_deployed,
        investigation_plan=investigation_plan
    )
    
    # Generate action plan
    action_plan = await orchestrator.create_action_plan(findings)
    
    return action_plan
```

## கட்டமைப்பு மற்றும் தனிப்பயனாக்கம்

### ஏஜென்ட் கட்டமைப்பு
```python
# Configure individual agents
agent_configs = {
    "CodeAgent": {
        "model": "phi-4-mini",
        "temperature": 0.3,
        "max_tokens": 2000,
        "specialization_level": "expert"
    },
    "ResearchAgent": {
        "model": "qwen2.5-coder-0.5b",
        "temperature": 0.7,
        "max_tokens": 1500,
        "research_depth": "comprehensive"
    }
}

orchestrator.configure_agents(agent_configs)
```

### வேலைவழி தனிப்பயனாக்கம்
```python
# Custom workflow definitions
custom_workflows = {
    "data_science_project": [
        "data_collection",
        "exploratory_analysis", 
        "model_development",
        "validation_testing",
        "deployment_preparation"
    ],
    "security_audit": [
        "vulnerability_scan",
        "code_review", 
        "penetration_testing",
        "compliance_check",
        "remediation_plan"
    ]
}

orchestrator.register_workflows(custom_workflows)
```

## கண்காணிப்பு மற்றும் பகுப்பாய்வு

### செயல்திறன் கண்காணிப்பு
```python
# Monitor orchestrator performance
metrics = await orchestrator.get_performance_metrics()
print(f"Tasks Completed: {metrics.tasks_completed}")
print(f"Average Response Time: {metrics.avg_response_time}s")
print(f"Success Rate: {metrics.success_rate}%")
print(f"Agent Utilization: {metrics.agent_utilization}")
```

### தர அளவுகள்
```python
# Track output quality
quality_report = await orchestrator.generate_quality_report()
print(f"Output Consistency: {quality_report.consistency_score}")
print(f"Factual Accuracy: {quality_report.accuracy_score}")
print(f"Completeness: {quality_report.completeness_score}")
```

## கற்றல் முடிவுகள்

இந்த மாதிரியை முடித்த பிறகு, நீங்கள் புரிந்துகொள்வீர்கள்:

1. **மல்டி-ஏஜென்ட் சிஸ்டம் கட்டமைப்பு**
   - ஏஜென்ட் ஒருங்கிணைப்பு முறைகள்
   - பணி பகிர்வு உத்திகள்
   - முடிவுகளை ஒருங்கிணைக்கும் தொழில்நுட்பங்கள்
   - ஏஜென்ட்களுக்கிடையிலான சூழல் மேலாண்மை

2. **Microsoft Foundry Local ஒருங்கிணைப்பு**
   - செயல்பாட்டு அழைப்பு செயல்படுத்தல்
   - கருவி ஒருங்கிணைப்பு முறைகள்
   - பல மாதிரி ஒர்கெஸ்ட்ரேஷன்
   - செயல்திறன் மேம்பாடு

3. **மேம்பட்ட AI ஒர்கெஸ்ட்ரேஷன்**
   - வேலைவழி வடிவமைப்பு மற்றும் செயல்பாடு
   - தர உறுதிப்பாட்டு முறைமைகள்
   - பிழை கையாளல் மற்றும் மீட்பு
   - அளவீட்டு கருத்துக்கள்

4. **தயாரிப்பு சிஸ்டம் வடிவமைப்பு**
   - கண்காணிப்பு மற்றும் பகுப்பாய்வு
   - கட்டமைப்பு மேலாண்மை
   - பாதுகாப்பு சிறந்த நடைமுறைகள்
   - செயல்திறன் சீரமைப்பு

## அடுத்த படிகள்

- **மாதிரி 10**: Foundry Local கருவி ஒருங்கிணைப்பு
- **மேம்பட்ட தலைப்புகள்**: தனிப்பயன் ஏஜென்ட் மேம்பாடு
- **அளவீடு**: பகிர்ந்த ஏஜென்ட் சிஸ்டங்கள்
- **ஒருங்கிணைப்பு**: நிறுவன வேலைவழி ஒருங்கிணைப்பு

## பங்களிப்பு

பங்களிப்பு வழிகாட்டலுக்கான முக்கிய களஞ்சிய வழிகாட்டுதல்களைப் பார்க்கவும்.

## உரிமம்

இந்த மாதிரி Microsoft Foundry Local திட்டத்தின் அதே உரிமத்தைப் பின்பற்றுகிறது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.