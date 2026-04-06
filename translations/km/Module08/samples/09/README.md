# ប្រព័ន្ធសម្របសម្រួលភ្នាក់ងារ​ច្រើន - Foundry Local

ប្រព័ន្ធភ្នាក់ងារច្រើនកម្រិតខ្ពស់ដែលដំណើរការដោយ Microsoft Foundry Local ដែលបង្ហាញពីការសម្របសម្រួលភ្នាក់ងារយល់ដឹង ការចែកចាយភារកិច្ចជាពិសេស និងគ្រោងការដោះស្រាយបញ្ហាផ្នែកសហការណ៍។

## សង្ខេប

គំរូនេះបង្ហាញពីរបៀបកសាងប្រព័ន្ធភ្នាក់ងារ AI ដែលស្មុគស្មាញដោយប្រើ Foundry Local, ដែលអនុវត្តលំនាំផ្លូវការ​របស់ Microsoft សម្រាប់ការហៅ function ការ​សម្របសម្រួលភ្នាក់ងារ និងចរន្តការងារ AI សហការណ៍។

## ស្ថាបត្យកម្ម

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

## លក្ខណៈសំខាន់ៗ

### 🤖 **ការសម្របសម្រួលភ្នាក់ងារយល់ដឹង**
- វិភាគភារកិច្ចឌីណាមិច និងការជ្រើសរើសភ្នាក់ងារ
- ការចែកចាយបន្តិចបន្តួចនៃផ្នែកការងារ secara អូតូម៉ាតិក
- ការបញ្ចូលលទ្ធផល និងការសម្រួល
- ពិចារណាការទំនាក់ទំនងអន្ដរសភា_CORRECTION: cross-agent communication protocols -> preserved meaning.  
- Protocols នៃការទំនាក់ទំនងរវាងភ្នាក់ងារ

### 🔧 **ប្រភេទភ្នាក់ងារពិសេស**
- **Code Expert**: កម្មវិធី ការស្វែងរកកំហុស ពិនិត្យកូដ
- **Data Analyst**: ការបំលែងទិន្នន័យ ការ​វិភាគទិន្នន័យ ទិដ្ឋភាពនិងការទទួលបានដំណឹង
- **Research Assistant**: ការបញ្ចូលព័ត៌មាន ការលាយសេចក្ដីសង្ខេប
- **Writing Specialist**: ការបង្កើតមាតិការសេចក្ដី ការកែសម្រួល ឯកសារការងារ
- **Problem Solver**: ការគិតវិជ្ជាស្មើ ភញ្ញា និងការអនុវត្តសេចក្ដីសម្រេច

### ⚡ **ការហៅ Function កម្រិតខ្ពស់**
- លំនាំហៅ function របស់ Microsoft Foundry Local
- ការបញ្ជាក់ឧបករណ៍មានប្រភេទសុវត្ថិភាព
- ការផ្ទៀងផ្ទាត់ទម្រង់ប៉ារ៉ាម៉ែត្រ secara អូតូម៉ាតិក
- ការគ្រប់គ្រងកំហុស និងការស្តារឡើងវិញ
- ការដាក់ជេរ​ឧបករណ៍ និងការភ្ជាប់គ្នា

### 🎯 **ការបញ្ជូនភារកិច្ចឆ្លាត**
- ការបែងចែកចេតនា និងវិភាគ
- ការចូលគ្នានៃសមត្ថភាពភ្នាក់ងារ
- ការបញ្ជូនបន្ទុក និងបង្កើនប្រសិទ្ធភាព
- ការទាក់ទាន់សម័យ និងការដោះស្រាយជំនួស

## តម្រូវការមុនពេលចាប់ផ្ដើម

### តម្រូវការរបស់ប្រព័ន្ធ
- **Python**: 3.9+ មានគាំទ្រ asyncio
- **Memory**: 16GB+ ទាមទារសម្រាប់ភ្នាក់ងារច្រើន
- **Storage**: 15GB+ សម្រាប់ម៉ូដែលច្រើន
- **CPU/GPU**: ប្រព័ន្ធដំណើរការ​មេញុបនិងកណ្តុរ, GPU ត្រូវបានណែនាំ

### អាស្រ័យភាព
```bash
pip install foundry-local-sdk openai aiohttp asyncio pydantic rich typer
```

### ការតំឡើង Foundry Local
```powershell
# ដំឡើង និងផ្ទៀងផ្ទាត់ Foundry Local
winget install Microsoft.FoundryLocal
foundry --version

# ទាញយកម៉ូដែលដែលបានណែនាំសម្រាប់ភ្នាក់ងារ
foundry model download phi-4-mini
foundry model download qwen2.5-coder-0.5b
foundry model download phi-3.5-mini
```

## ចាប់ផ្តើមយ៉ាងរហ័ស

### 1. លំនាំការងារ​ភ្នាក់ងារ​ច្រើន​មូលដ្ឋាន
```python
from agentic_system import AgentOrchestrator, CodeAgent, ResearchAgent

# ចាប់ផ្តើមកម្មវិធីសម្របសម្រួល
orchestrator = AgentOrchestrator()

# បន្ថែមភ្នាក់ងារឯកទេស
await orchestrator.add_agent(CodeAgent("phi-4-mini"))
await orchestrator.add_agent(ResearchAgent("qwen2.5-coder-0.5b"))

# អនុវត្តភារៈកិច្ចស្មុគស្មាញ
result = await orchestrator.execute_task(
    "Create a Python script that analyzes web traffic data and generates a report"
)

print(result.summary)
```

### 2. ការបង្កើតភ្នាក់ងាររូបភាពលក្ខណៈផ្ទាល់ខ្លួន
```python
from agentic_system import BaseAgent, tool

class DataAnalystAgent(BaseAgent):
    """Specialized agent for data analysis tasks."""
    
    @tool
    async def analyze_dataset(self, data_path: str, analysis_type: str) -> dict:
        """Analyze a dataset and return insights."""
        # អនុវត្តនៅទីនេះ
        pass
    
    @tool
    async def create_visualization(self, data: dict, chart_type: str) -> str:
        """Create data visualizations."""
        # អនុវត្តនៅទីនេះ
        pass

# ប្រើភ្នាក់ងារផ្ទាល់ខ្លួន
agent = DataAnalystAgent("qwen2.5-0.5b")
result = await agent.analyze_dataset("sales_data.csv", "trend_analysis")
```

### 3. ការរួមបញ្ចូលការហៅ Function
```python
# កំណត់ឧបករណ៍ដោយអនុវត្តតាមលំនាំរបស់ Microsoft
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

# ចុះបញ្ជីឧបករណ៍ជាមួយកម្មវិធីសម្របសម្រួល
orchestrator.register_tools(tools)
```

## រៀបចំគម្រោង

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

## រៀនជ្រាលជ្រៅអំពីប្រភេទភ្នាក់ងារ

### 1. ភ្នាក់ងារប្រឹក្សាកូដ
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

### 2. ភ្នាក់ងារជំនួយស្រាវ​ជ្រាវ
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

### 3. ភ្នាក់ងារវិភាគទិន្នន័យ
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

## ម៉ូដែលសម្របសម្រួល

### 1. លំនាំដំណើរការ​តាមលំដាប់
```python
# កំណត់ដំណើរការតាមលំដាប់
workflow = orchestrator.create_workflow("sequential")
workflow.add_step("research", ResearchAgent, "gather_requirements")
workflow.add_step("design", CodeAgent, "create_architecture")  
workflow.add_step("implement", CodeAgent, "write_code")
workflow.add_step("test", CodeAgent, "create_tests")

result = await workflow.execute("Build a REST API for user management")
```

### 2. ការប្រតិបត្តិជាសុវត្ថិភាពស្របពេល
```python
# អនុវត្តភារកិច្ចក្នុងពេលតែមួយ
parallel_tasks = [
    ("research_market", ResearchAgent, "analyze_market_trends"),
    ("analyze_competitors", DataAgent, "competitor_analysis"),
    ("technical_feasibility", CodeAgent, "assess_technical_requirements")
]

results = await orchestrator.execute_parallel(parallel_tasks)
synthesized = await orchestrator.synthesize_results(results)
```

### 3. ការជ្រើសរើសភ្នាក់ងារដោយឌីណាមិច
```python
# ការជ្រើសរើសភ្នាក់ងារដោយស្វ័យប្រវត្តិដោយផ្អែកលើការវិភាគភារកិច្ច
task = "Create a machine learning model to predict customer churn"

# អ្នករៀបចំវិភាគភារកិច្ច ហើយជ្រើសរើសភ្នាក់ងារដែលសមរម្យ
selected_agents = await orchestrator.analyze_task_requirements(task)
# ត្រឡប់: [DataAgent, CodeAgent, ResearchAgent]

result = await orchestrator.execute_with_agents(task, selected_agents)
```

## ការរួមបញ្ចូលការហៅ Function

### លំនាំ Microsoft Foundry Local
```python
# កំណត់ឧបករណ៍តាមរចនាសម្ព័ន្ធ​ការ​ហៅ​មុខងារ​របស់ Microsoft
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

# ការរួមបញ្ចូលជាមួយ Foundry Local
async def setup_function_calling():
    tools = define_foundry_tools()
    
    # កំណត់ Foundry Local សម្រាប់ការហៅមុខងារ
    client = openai.OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # ប្រើឧបករណ៍ក្នុងសន្ទនា
    response = await client.chat.completions.create(
        model=manager.get_model_info("phi-4-mini").id,
        messages=[
            {"role": "user", "content": "Analyze this Python code for quality issues"}
        ],
        tools=[{"type": "function", "function": tool} for tool in tools],
        tool_choice="auto"
    )
```

## លក្ខណៈពិសេសសម្របសម្រួលកម្រិតខ្ពស់

### 1. ការគ្រប់គ្រងបរិបទ
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

### 2. ការសម្រួលលទ្ធផល
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

### 3. ការធានាគុណភាព
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

## ការបង្កើនប្រសិទ្ធភាព

### 1. ការតុល្យភាពផ្ទុកម៉ូដែល
```python
# ចែកចាយម៉ូដែលទៅកាន់ភ្នាក់ងារ ដើម្បីប្រើប្រាស់ធនធានឱ្យបានប្រសើរបំផុត
model_allocation = {
    "code_tasks": "phi-4-mini",
    "research_tasks": "qwen2.5-coder-0.5b", 
    "analysis_tasks": "phi-3.5-mini",
    "general_tasks": "phi-4-mini"
}

orchestrator.configure_model_allocation(model_allocation)
```

### 2. Caching និងអង្គចងចាំ
```python
# អនុវត្តការផ្ទុកទិន្នន័យ​រហ័សឆ្លាត
cache_config = {
    "response_cache": True,
    "context_cache": True,
    "tool_result_cache": True,
    "cache_ttl": 3600  # 1 ម៉ោង
}

orchestrator.configure_caching(cache_config)
```

### 3. ការប្រតិបត្តិស្របពេល
```python
# បង្កើនប្រសិទ្ធភាពសម្រាប់ការដំណើរការដោយស្របគ្នា
concurrency_config = {
    "max_concurrent_agents": 4,
    "agent_pool_size": 8,
    "task_queue_size": 100,
    "timeout_seconds": 300
}

orchestrator.configure_concurrency(concurrency_config)
```

## ឧទាហរណ៍ការប្រើ

### ឧទាហរណ៍ 1: លំនាំអភិវឌ្ឍន៍កម្មវិធី
```python
async def software_development_workflow():
    """Complete software development using multiple agents."""
    
    # ចាប់ផ្តើម​អ្នករៀបចំជាមួយភ្នាក់ងារដែលមានជំនាញពិសេស
    orchestrator = AgentOrchestrator()
    await orchestrator.add_agent(ResearchAgent("qwen2.5-coder-0.5b"))
    await orchestrator.add_agent(CodeAgent("phi-4-mini"))
    await orchestrator.add_agent(DataAgent("phi-3.5-mini"))
    
    # កំណត់ភារកិច្ចអភិវឌ្ឍន៍
    task = """
    Create a web application that:
    1. Analyzes user behavior data
    2. Provides real-time analytics dashboard
    3. Includes user authentication
    4. Has comprehensive tests
    """
    
    # អនុវត្តដំណើរការការងារដែលបានសម្របសម្រួល
    result = await orchestrator.execute_workflow(
        task=task,
        workflow_type="software_development",
        quality_gates=["code_review", "testing", "security_check"]
    )
    
    return result
```

### ឧទាហរណ៍ 2: ស្រាវជ្រាវ និងវិភាគ
```python
async def comprehensive_research():
    """Multi-agent research coordination."""
    
    research_query = "Impact of AI on software development productivity"
    
    # ការអនុវត្តស្រាវជ្រាវដោយស្របពេល
    tasks = [
        ("literature_review", ResearchAgent, research_query),
        ("data_analysis", DataAgent, "productivity_metrics"),
        ("case_studies", ResearchAgent, "ai_adoption_cases"),
        ("technical_analysis", CodeAgent, "ai_tool_evaluation")
    ]
    
    results = await orchestrator.execute_parallel(tasks)
    
    # បង្កើតសេចក្តីសន្និដ្ឋានពីលទ្ធផល
    final_report = await orchestrator.synthesize_research(
        results=results,
        format="comprehensive_report",
        include_recommendations=True
    )
    
    return final_report
```

### ឧទាហរណ៍ 3: សម័យដោះស្រាយបញ្ហា
```python
async def collaborative_problem_solving():
    """Multi-agent collaborative problem solving."""
    
    problem = """
    A company's API response times have increased 300% over the past month.
    Analyze the issue and propose solutions.
    """
    
    # ផ្ញើភ្នាក់ងារឯកទេស
    investigation_plan = await orchestrator.create_investigation_plan(problem)
    
    agents_deployed = [
        (CodeAgent, "analyze_code_performance"),
        (DataAgent, "analyze_performance_metrics"), 
        (ResearchAgent, "research_similar_issues"),
        (SolverAgent, "propose_solutions")
    ]
    
    # សម្របសម្រួលការស៊ើបអង្កេត
    findings = await orchestrator.coordinate_investigation(
        problem=problem,
        agents=agents_deployed,
        investigation_plan=investigation_plan
    )
    
    # បង្កើតផែនការសកម្មភាព
    action_plan = await orchestrator.create_action_plan(findings)
    
    return action_plan
```

## ការកំណត់រចនាបទ និងការកែសំរួល

### ការកំណត់ភ្នាក់ងារ
```python
# កំណត់រចនាសម្ព័ន្ធសម្រាប់ភ្នាក់ងារនីមួយៗ
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

### ការកែប្រែលំនាំការ
```python
# ការកំណត់ដំណើរការផ្ទាល់ខ្លួន
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

## ការតាមដាន និងវិភាគ

### ការតាមដានប្រសិទ្ធភាព
```python
# តាមដានប្រសិទ្ធភាពរបស់កម្មវិធីរៀបចំ
metrics = await orchestrator.get_performance_metrics()
print(f"Tasks Completed: {metrics.tasks_completed}")
print(f"Average Response Time: {metrics.avg_response_time}s")
print(f"Success Rate: {metrics.success_rate}%")
print(f"Agent Utilization: {metrics.agent_utilization}")
```

### មាត្រដ្ឋានគុណភាព
```python
# តាមដានគុណភាពនៃលទ្ធផល
quality_report = await orchestrator.generate_quality_report()
print(f"Output Consistency: {quality_report.consistency_score}")
print(f"Factual Accuracy: {quality_report.accuracy_score}")
print(f"Completeness: {quality_report.completeness_score}")
```

## លទ្ធផលដែលនឹងរៀនចប់

បន្ទាប់ពីបញ្ចប់គំរូនេះ អ្នកនឹងយល់ពី៖

1. **ស្ថាបត្យកម្មប្រព័ន្ធភ្នាក់ងារ​ច្រើន**
   - លំនាំសម្របសម្រួលភ្នាក់ងារ
   - យុទ្ធសាស្រ្តចែកចាយភារកិច្ច
   - វិធីសាស្រ្តសម្រួលលទ្ធផល
   - ការគ្រប់គ្រងបរិបទឆ្លងកាត់ភ្នាក់ងារ

2. **ការរួមបញ្ចូល Microsoft Foundry Local**
   - ការអនុវត្តការហៅ function
   - លំនាំការរួមបញ្ចូលឧបករណ៍
   - ការសម្របសម្រួលម៉ូដែលច្រើន
   - ការបង្កើនប្រសិទ្ធភាព

3. **ការសម្របសម្រួល AI កម្រិតខ្ពស់**
   - ការរចនា និងការប្រតិបត្តិលំនាំការ
   - مکانិចធានាគុណភាព
   - ការគ្រប់គ្រងកំហុស និងការស្តារឡើងវិញ
   - ការពិចារណាសមាសភាពស្ពឹកឡើង

4. **ការរចនាប្រព័ន្ធផលិតកម្ម**
   - ការតាមដាន និងវិភាគ
   - ការគ្រប់គ្រងការកំណត់តម្លៃ
   - អនុវិធីសាស្រ្តសុវត្ថិភាព
   - ការបន្ថែមប្រសិទ្ធភាព

## ជំហានបន្ទាប់

- **Sample 10**: Foundry Local as Tools Integration
- **Advanced Topics**: ការអភិវឌ្ឍភ្នាក់ងារផ្ទាល់ខ្លួន
- **Scaling**: ប្រព័ន្ធភ្នាក់ងារបែងចែក
- **Integration**: ការរួមបញ្ចូលលំនាំការងារអង្គការ

## ការរួមចំណែក

សូមមើលការណែនាំក្នុង repository ចម្បងសម្រាប់សេចក្ដីណែនាំអំពីវិធានការរួមចំណែក។

## អាជ្ញាបណ្ណ

គំរូនេះអនុវត្តតាមអាជ្ញាបណ្ណដូចគ្នានឹងគម្រោង Microsoft Foundry Local។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ខណៈពេលយើងខំប្រឹងសម្រាប់ភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យ​ប្រវត្តិ​អាច​មាន​កំហុស ឬ​មិន​ត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានគេចាត់ទុកថាជាប្រភពផ្លូវការនៃព័ត៌មាន។ សម្រាប់ព័ត៌មានដែលសំខាន់ៗ យើងសូមផ្តល់អនុសាសន៍ឱ្យធ្វើការបកប្រែដោយអ្នកបកប្រែជាមនុស្សដែលមានវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->