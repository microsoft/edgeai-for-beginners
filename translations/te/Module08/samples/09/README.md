<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "de485a95e80a332f14ca1dcf2aca3961",
  "translation_date": "2025-12-16T00:49:25+00:00",
  "source_file": "Module08/samples/09/README.md",
  "language_code": "te"
}
-->
# మల్టీ-ఏజెంట్ ఆర్కెస్ట్రేషన్ సిస్టమ్ - ఫౌండ్రీ లోకల్

మైక్రోసాఫ్ట్ ఫౌండ్రీ లోకల్ ద్వారా శక్తివంతమైన ఒక ఆధునిక మల్టీ-ఏజెంట్ సిస్టమ్, ఇది తెలివైన ఏజెంట్ సమన్వయం, ప్రత్యేక పనుల కేటాయింపు, మరియు సహకార సమస్య పరిష్కార నమూనాలను ప్రదర్శిస్తుంది.

## అవలోకనం

ఈ నమూనా ఫౌండ్రీ లోకల్ ఉపయోగించి సాంకేతిక AI ఏజెంట్ సిస్టమ్స్‌ను ఎలా నిర్మించాలో చూపిస్తుంది, మైక్రోసాఫ్ట్ అధికారిక నమూనాలను ఫంక్షన్ కాలింగ్, ఏజెంట్ ఆర్కెస్ట్రేషన్, మరియు సహకార AI వర్క్‌ఫ్లోల కోసం అమలు చేస్తుంది.

## నిర్మాణం

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

## ముఖ్య లక్షణాలు

### 🤖 **తెలివైన ఏజెంట్ సమన్వయం**
- డైనమిక్ టాస్క్ విశ్లేషణ మరియు ఏజెంట్ ఎంపిక
- ఆటోమేటిక్ వర్క్‌లోడ్ పంపిణీ
- ఫలితాల సమాహారం మరియు సంశ్లేషణ
- క్రాస్-ఏజెంట్ కమ్యూనికేషన్ ప్రోటోకాల్స్

### 🔧 **ప్రత్యేక ఏజెంట్ రకాలు**
- **కోడ్ నిపుణుడు**: ప్రోగ్రామింగ్, డీబగ్గింగ్, కోడ్ సమీక్ష
- **డేటా విశ్లేషకుడు**: డేటా ప్రాసెసింగ్, విజువలైజేషన్, అవగాహనలు
- **సంశోధన సహాయకుడు**: సమాచారం సేకరణ, సారాంశం
- **రచనా నిపుణుడు**: కంటెంట్ సృష్టి, సవరణ, డాక్యుమెంటేషన్
- **సమస్య పరిష్కర్త**: సంక్లిష్ట తర్కం, నిర్ణయ తీసుకోవడం

### ⚡ **అధునాతన ఫంక్షన్ కాలింగ్**
- మైక్రోసాఫ్ట్ ఫౌండ్రీ లోకల్ ఫంక్షన్ కాలింగ్ నమూనాలు
- టైప్-సేఫ్ టూల్ నిర్వచనలు
- ఆటోమేటిక్ పారామీటర్ ధృవీకరణ
- లోప నిర్వహణ మరియు పునరుద్ధరణ
- టూల్ చైనింగ్ మరియు సంయోజనం

### 🎯 **స్మార్ట్ టాస్క్ రౌటింగ్**
- ఉద్దేశ్య వర్గీకరణ మరియు విశ్లేషణ
- ఏజెంట్ సామర్థ్య సరిపోలిక
- లోడ్ బ్యాలెన్సింగ్ మరియు ఆప్టిమైజేషన్
- ఫాల్బ్యాక్ మరియు రెడండెన్సీ నిర్వహణ

## ముందస్తు అవసరాలు

### సిస్టమ్ అవసరాలు
- **Python**: 3.9+ asyncio మద్దతుతో
- **మెమరీ**: బహుళ ఏజెంట్ల కోసం 16GB+ సిఫార్సు
- **స్టోరేజ్**: బహుళ మోడల్స్ కోసం 15GB+
- **CPU/GPU**: మల్టీ-కోర్ ప్రాసెసర్, GPU సిఫార్సు

### ఆధారాలు
```bash
pip install foundry-local-sdk openai aiohttp asyncio pydantic rich typer
```

### ఫౌండ్రీ లోకల్ సెటప్
```powershell
# ఫౌండ్రీ లోకల్‌ను ఇన్‌స్టాల్ చేసి ధృవీకరించండి
winget install Microsoft.FoundryLocal
foundry --version

# ఏజెంట్ల కోసం సిఫార్సు చేసిన మోడల్స్‌ను డౌన్‌లోడ్ చేయండి
foundry model download phi-4-mini
foundry model download qwen2.5-coder-0.5b
foundry model download phi-3.5-mini
```

## త్వరిత ప్రారంభం

### 1. ప్రాథమిక మల్టీ-ఏజెంట్ వర్క్‌ఫ్లో
```python
from agentic_system import AgentOrchestrator, CodeAgent, ResearchAgent

# ఆర్కెస్ట్రేటర్‌ను ప్రారంభించండి
orchestrator = AgentOrchestrator()

# ప్రత్యేక ఏజెంట్లను జోడించండి
await orchestrator.add_agent(CodeAgent("phi-4-mini"))
await orchestrator.add_agent(ResearchAgent("qwen2.5-coder-0.5b"))

# ఒక సంక్లిష్ట పనిని అమలు చేయండి
result = await orchestrator.execute_task(
    "Create a Python script that analyzes web traffic data and generates a report"
)

print(result.summary)
```

### 2. కస్టమ్ ఏజెంట్ సృష్టి
```python
from agentic_system import BaseAgent, tool

class DataAnalystAgent(BaseAgent):
    """Specialized agent for data analysis tasks."""
    
    @tool
    async def analyze_dataset(self, data_path: str, analysis_type: str) -> dict:
        """Analyze a dataset and return insights."""
        # ఇక్కడ అమలు
        pass
    
    @tool
    async def create_visualization(self, data: dict, chart_type: str) -> str:
        """Create data visualizations."""
        # ఇక్కడ అమలు
        pass

# కస్టమ్ ఏజెంట్ ఉపయోగించండి
agent = DataAnalystAgent("qwen2.5-0.5b")
result = await agent.analyze_dataset("sales_data.csv", "trend_analysis")
```

### 3. ఫంక్షన్ కాలింగ్ ఇంటిగ్రేషన్
```python
# మైక్రోసాఫ్ట్ నమూనాలను అనుసరించి టూల్స్ నిర్వచించండి
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

# ఆర్కెస్ట్రేటర్‌తో టూల్స్‌ను నమోదు చేయండి
orchestrator.register_tools(tools)
```

## ప్రాజెక్ట్ నిర్మాణం

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

## ఏజెంట్ రకాలు లోతైన అవగాహన

### 1. కోడ్ నిపుణుడు ఏజెంట్
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

### 2. పరిశోధన సహాయకుడు ఏజెంట్
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

### 3. డేటా విశ్లేషణ ఏజెంట్
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

## ఆర్కెస్ట్రేషన్ నమూనాలు

### 1. వరుస వర్క్‌ఫ్లో
```python
# ఒక వరుస వర్క్‌ఫ్లోని నిర్వచించండి
workflow = orchestrator.create_workflow("sequential")
workflow.add_step("research", ResearchAgent, "gather_requirements")
workflow.add_step("design", CodeAgent, "create_architecture")  
workflow.add_step("implement", CodeAgent, "write_code")
workflow.add_step("test", CodeAgent, "create_tests")

result = await workflow.execute("Build a REST API for user management")
```

### 2. సమాంతర అమలు
```python
# పనులను సమాంతరంగా అమలు చేయండి
parallel_tasks = [
    ("research_market", ResearchAgent, "analyze_market_trends"),
    ("analyze_competitors", DataAgent, "competitor_analysis"),
    ("technical_feasibility", CodeAgent, "assess_technical_requirements")
]

results = await orchestrator.execute_parallel(parallel_tasks)
synthesized = await orchestrator.synthesize_results(results)
```

### 3. డైనమిక్ ఏజెంట్ ఎంపిక
```python
# పనితీరు విశ్లేషణ ఆధారంగా ఆటోమేటిక్ ఏజెంట్ ఎంపిక
task = "Create a machine learning model to predict customer churn"

# ఆర్కెస్ట్రేటర్ పనిని విశ్లేషించి సరైన ఏజెంట్లను ఎంచుకుంటుంది
selected_agents = await orchestrator.analyze_task_requirements(task)
# తిరిగి ఇస్తుంది: [డేటా ఏజెంట్, కోడ్ ఏజెంట్, రీసెర్చ్ ఏజెంట్]

result = await orchestrator.execute_with_agents(task, selected_agents)
```

## ఫంక్షన్ కాలింగ్ ఇంటిగ్రేషన్

### మైక్రోసాఫ్ట్ ఫౌండ్రీ లోకల్ నమూనాలు
```python
# మైక్రోసాఫ్ట్ యొక్క ఫంక్షన్ కాలింగ్ స్కీమాను అనుసరించి టూల్స్ నిర్వచించండి
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

# ఫౌండ్రీ లోకల్‌తో సమగ్రత
async def setup_function_calling():
    tools = define_foundry_tools()
    
    # ఫంక్షన్ కాలింగ్ కోసం ఫౌండ్రీ లోకల్‌ను కాన్ఫిగర్ చేయండి
    client = openai.OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # సంభాషణలో టూల్స్ ఉపయోగించండి
    response = await client.chat.completions.create(
        model=manager.get_model_info("phi-4-mini").id,
        messages=[
            {"role": "user", "content": "Analyze this Python code for quality issues"}
        ],
        tools=[{"type": "function", "function": tool} for tool in tools],
        tool_choice="auto"
    )
```

## అధునాతన సమన్వయ లక్షణాలు

### 1. సందర్భ నిర్వహణ
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

### 2. ఫలిత సంశ్లేషణ
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

### 3. నాణ్యత హామీ
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

## పనితీరు ఆప్టిమైజేషన్

### 1. మోడల్ లోడ్ బ్యాలెన్సింగ్
```python
# ఆప్టిమల్ వనరుల వినియోగం కోసం ఏజెంట్ల మధ్య మోడల్స్ పంపిణీ చేయండి
model_allocation = {
    "code_tasks": "phi-4-mini",
    "research_tasks": "qwen2.5-coder-0.5b", 
    "analysis_tasks": "phi-3.5-mini",
    "general_tasks": "phi-4-mini"
}

orchestrator.configure_model_allocation(model_allocation)
```

### 2. క్యాచింగ్ మరియు మెమరీ
```python
# తెలివైన క్యాచింగ్‌ను అమలు చేయండి
cache_config = {
    "response_cache": True,
    "context_cache": True,
    "tool_result_cache": True,
    "cache_ttl": 3600  # 1 గంట
}

orchestrator.configure_caching(cache_config)
```

### 3. సమకాలీన అమలు
```python
# సమాంతర ప్రాసెసింగ్ కోసం ఆప్టిమైజ్ చేయండి
concurrency_config = {
    "max_concurrent_agents": 4,
    "agent_pool_size": 8,
    "task_queue_size": 100,
    "timeout_seconds": 300
}

orchestrator.configure_concurrency(concurrency_config)
```

## ఉపయోగ ఉదాహరణలు

### ఉదాహరణ 1: సాఫ్ట్‌వేర్ అభివృద్ధి వర్క్‌ఫ్లో
```python
async def software_development_workflow():
    """Complete software development using multiple agents."""
    
    # ప్రత్యేక ఏజెంట్లతో ఆర్కెస్ట్రేటర్‌ను ప్రారంభించండి
    orchestrator = AgentOrchestrator()
    await orchestrator.add_agent(ResearchAgent("qwen2.5-coder-0.5b"))
    await orchestrator.add_agent(CodeAgent("phi-4-mini"))
    await orchestrator.add_agent(DataAgent("phi-3.5-mini"))
    
    # అభివృద్ధి పనిని నిర్వచించండి
    task = """
    Create a web application that:
    1. Analyzes user behavior data
    2. Provides real-time analytics dashboard
    3. Includes user authentication
    4. Has comprehensive tests
    """
    
    # సమన్వయిత వర్క్‌ఫ్లోను అమలు చేయండి
    result = await orchestrator.execute_workflow(
        task=task,
        workflow_type="software_development",
        quality_gates=["code_review", "testing", "security_check"]
    )
    
    return result
```

### ఉదాహరణ 2: పరిశోధన మరియు విశ్లేషణ
```python
async def comprehensive_research():
    """Multi-agent research coordination."""
    
    research_query = "Impact of AI on software development productivity"
    
    # సమాంతర పరిశోధన నిర్వహణ
    tasks = [
        ("literature_review", ResearchAgent, research_query),
        ("data_analysis", DataAgent, "productivity_metrics"),
        ("case_studies", ResearchAgent, "ai_adoption_cases"),
        ("technical_analysis", CodeAgent, "ai_tool_evaluation")
    ]
    
    results = await orchestrator.execute_parallel(tasks)
    
    # ఫలితాలను సమ్మిళితం చేయండి
    final_report = await orchestrator.synthesize_research(
        results=results,
        format="comprehensive_report",
        include_recommendations=True
    )
    
    return final_report
```

### ఉదాహరణ 3: సమస్య పరిష్కార సెషన్
```python
async def collaborative_problem_solving():
    """Multi-agent collaborative problem solving."""
    
    problem = """
    A company's API response times have increased 300% over the past month.
    Analyze the issue and propose solutions.
    """
    
    # నిపుణుల ఏజెంట్లను నియమించండి
    investigation_plan = await orchestrator.create_investigation_plan(problem)
    
    agents_deployed = [
        (CodeAgent, "analyze_code_performance"),
        (DataAgent, "analyze_performance_metrics"), 
        (ResearchAgent, "research_similar_issues"),
        (SolverAgent, "propose_solutions")
    ]
    
    # దర్యాప్తును సమన్వయించండి
    findings = await orchestrator.coordinate_investigation(
        problem=problem,
        agents=agents_deployed,
        investigation_plan=investigation_plan
    )
    
    # చర్యా ప్రణాళికను రూపొందించండి
    action_plan = await orchestrator.create_action_plan(findings)
    
    return action_plan
```

## కాన్ఫిగరేషన్ మరియు అనుకూలీకరణ

### ఏజెంట్ కాన్ఫిగరేషన్
```python
# వ్యక్తిగత ఏజెంట్లను కాన్ఫిగర్ చేయండి
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

### వర్క్‌ఫ్లో అనుకూలీకరణ
```python
# కస్టమ్ వర్క్‌ఫ్లో నిర్వచనాలు
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

## మానిటరింగ్ మరియు విశ్లేషణ

### పనితీరు ట్రాకింగ్
```python
# ఆర్కెస్ట్రేటర్ పనితీరును పర్యవేక్షించండి
metrics = await orchestrator.get_performance_metrics()
print(f"Tasks Completed: {metrics.tasks_completed}")
print(f"Average Response Time: {metrics.avg_response_time}s")
print(f"Success Rate: {metrics.success_rate}%")
print(f"Agent Utilization: {metrics.agent_utilization}")
```

### నాణ్యత మెట్రిక్స్
```python
# అవుట్పుట్ నాణ్యతను ట్రాక్ చేయండి
quality_report = await orchestrator.generate_quality_report()
print(f"Output Consistency: {quality_report.consistency_score}")
print(f"Factual Accuracy: {quality_report.accuracy_score}")
print(f"Completeness: {quality_report.completeness_score}")
```

## నేర్చుకున్న ఫలితాలు

ఈ నమూనాను పూర్తి చేసిన తర్వాత, మీరు అర్థం చేసుకుంటారు:

1. **మల్టీ-ఏజెంట్ సిస్టమ్ నిర్మాణం**
   - ఏజెంట్ సమన్వయ నమూనాలు
   - పనుల పంపిణీ వ్యూహాలు
   - ఫలిత సంశ్లేషణ సాంకేతికతలు
   - ఏజెంట్ల మధ్య సందర్భ నిర్వహణ

2. **మైక్రోసాఫ్ట్ ఫౌండ్రీ లోకల్ ఇంటిగ్రేషన్**
   - ఫంక్షన్ కాలింగ్ అమలు
   - టూల్ ఇంటిగ్రేషన్ నమూనాలు
   - బహుళ-మోడల్ ఆర్కెస్ట్రేషన్
   - పనితీరు ఆప్టిమైజేషన్

3. **అధునాతన AI ఆర్కెస్ట్రేషన్**
   - వర్క్‌ఫ్లో డిజైన్ మరియు అమలు
   - నాణ్యత హామీ యంత్రాంగాలు
   - లోప నిర్వహణ మరియు పునరుద్ధరణ
   - స్కేలబిలిటీ పరిగణనలు

4. **ఉత్పత్తి సిస్టమ్ డిజైన్**
   - మానిటరింగ్ మరియు విశ్లేషణ
   - కాన్ఫిగరేషన్ నిర్వహణ
   - భద్రత ఉత్తమ పద్ధతులు
   - పనితీరు ట్యూనింగ్

## తదుపరి దశలు

- **నమూనా 10**: ఫౌండ్రీ లోకల్ టూల్స్ ఇంటిగ్రేషన్‌గా
- **అధునాతన అంశాలు**: కస్టమ్ ఏజెంట్ అభివృద్ధి
- **స్కేలింగ్**: పంపిణీ చేసిన ఏజెంట్ సిస్టమ్స్
- **ఇంటిగ్రేషన్**: ఎంటర్ప్రైజ్ వర్క్‌ఫ్లో ఇంటిగ్రేషన్

## సహకారం

కాంట్రిబ్యూషన్ సూచనల కోసం ప్రధాన రిపోజిటరీ మార్గదర్శకాలను చూడండి.

## లైసెన్స్

ఈ నమూనా మైక్రోసాఫ్ట్ ఫౌండ్రీ లోకల్ ప్రాజెక్ట్ లైసెన్స్‌ను అనుసరిస్తుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. అసలు పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->