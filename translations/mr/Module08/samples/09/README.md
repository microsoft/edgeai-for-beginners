# मल्टी-एजंट ऑर्केस्ट्रेशन सिस्टम - फाउंड्री लोकल

मायक्रोसॉफ्ट फाउंड्री लोकलद्वारे समर्थित एक प्रगत मल्टी-एजंट सिस्टम, जो बुद्धिमान एजंट समन्वय, विशेष कार्यांचे वाटप, आणि सहकार्याने समस्या सोडवण्याचे नमुने प्रदर्शित करते.

## आढावा

ही नमुना फाउंड्री लोकल वापरून प्रगत AI एजंट सिस्टम तयार करण्याचे प्रदर्शन करते, ज्यामध्ये मायक्रोसॉफ्टचे अधिकृत नमुने कार्य कॉलिंग, एजंट ऑर्केस्ट्रेशन, आणि सहकार्यात्मक AI कार्यप्रवाहांसाठी लागू केले जातात.

## आर्किटेक्चर

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

## मुख्य वैशिष्ट्ये

### 🤖 **बुद्धिमान एजंट समन्वय**
- गतिशील कार्य विश्लेषण आणि एजंट निवड
- स्वयंचलित कार्यभार वितरण
- निकालांचे एकत्रीकरण आणि संश्लेषण
- क्रॉस-एजंट संवाद प्रोटोकॉल

### 🔧 **विशेष एजंट प्रकार**
- **कोड एक्सपर्ट**: प्रोग्रामिंग, डीबगिंग, कोड पुनरावलोकन
- **डेटा विश्लेषक**: डेटा प्रक्रिया, व्हिज्युअलायझेशन, अंतर्दृष्टी
- **संशोधन सहाय्यक**: माहिती गोळा करणे, संक्षेप करणे
- **लेखन विशेषज्ञ**: सामग्री निर्मिती, संपादन, दस्तऐवजीकरण
- **समस्या सोडवणारा**: जटिल विचार, निर्णय घेणे

### ⚡ **प्रगत कार्य कॉलिंग**
- मायक्रोसॉफ्ट फाउंड्री लोकल कार्य कॉलिंग नमुने
- प्रकार-सुरक्षित साधन परिभाषा
- स्वयंचलित पॅरामीटर पडताळणी
- त्रुटी हाताळणी आणि पुनर्प्राप्ती
- साधन साखळी आणि रचना

### 🎯 **स्मार्ट कार्य रूटिंग**
- हेतू वर्गीकरण आणि विश्लेषण
- एजंट क्षमता जुळवणे
- लोड संतुलन आणि ऑप्टिमायझेशन
- फॉलबॅक आणि पुनरावृत्ती हाताळणी

## पूर्वअटी

### सिस्टम आवश्यकता
- **Python**: 3.9+ asyncio समर्थनासह
- **मेमरी**: अनेक एजंटसाठी 16GB+ शिफारस केलेली
- **स्टोरेज**: अनेक मॉडेल्ससाठी 15GB+
- **CPU/GPU**: मल्टी-कोर प्रोसेसर, GPU शिफारस केलेली

### अवलंबित्व
```bash
pip install foundry-local-sdk openai aiohttp asyncio pydantic rich typer
```

### फाउंड्री लोकल सेटअप
```powershell
# Install and verify Foundry Local
winget install Microsoft.FoundryLocal
foundry --version

# Download recommended models for agents
foundry model download phi-4-mini
foundry model download qwen2.5-coder-0.5b
foundry model download phi-3.5-mini
```

## जलद सुरुवात

### 1. मूलभूत मल्टी-एजंट कार्यप्रवाह
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

### 2. कस्टम एजंट निर्मिती
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

### 3. कार्य कॉलिंग एकत्रीकरण
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

## प्रकल्प संरचना

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

## एजंट प्रकार सखोल अभ्यास

### 1. कोड एक्सपर्ट एजंट
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

### 2. संशोधन सहाय्यक एजंट
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

### 3. डेटा विश्लेषण एजंट
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

## ऑर्केस्ट्रेशन नमुने

### 1. अनुक्रमिक कार्यप्रवाह
```python
# Define a sequential workflow
workflow = orchestrator.create_workflow("sequential")
workflow.add_step("research", ResearchAgent, "gather_requirements")
workflow.add_step("design", CodeAgent, "create_architecture")  
workflow.add_step("implement", CodeAgent, "write_code")
workflow.add_step("test", CodeAgent, "create_tests")

result = await workflow.execute("Build a REST API for user management")
```

### 2. समांतर अंमलबजावणी
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

### 3. गतिशील एजंट निवड
```python
# Automatic agent selection based on task analysis
task = "Create a machine learning model to predict customer churn"

# Orchestrator analyzes task and selects appropriate agents
selected_agents = await orchestrator.analyze_task_requirements(task)
# Returns: [DataAgent, CodeAgent, ResearchAgent]

result = await orchestrator.execute_with_agents(task, selected_agents)
```

## कार्य कॉलिंग एकत्रीकरण

### मायक्रोसॉफ्ट फाउंड्री लोकल नमुने
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

## प्रगत समन्वय वैशिष्ट्ये

### 1. संदर्भ व्यवस्थापन
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

### 2. निकाल संश्लेषण
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

### 3. गुणवत्ता हमी
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

## कार्यक्षमता ऑप्टिमायझेशन

### 1. मॉडेल लोड संतुलन
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

### 2. कॅशिंग आणि मेमरी
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

### 3. एकत्रित अंमलबजावणी
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

## वापर उदाहरणे

### उदाहरण 1: सॉफ्टवेअर विकास कार्यप्रवाह
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

### उदाहरण 2: संशोधन आणि विश्लेषण
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

### उदाहरण 3: समस्या सोडवण्याचे सत्र
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

## कॉन्फिगरेशन आणि सानुकूलन

### एजंट कॉन्फिगरेशन
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

### कार्यप्रवाह सानुकूलन
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

## निरीक्षण आणि विश्लेषण

### कार्यक्षमता ट्रॅकिंग
```python
# Monitor orchestrator performance
metrics = await orchestrator.get_performance_metrics()
print(f"Tasks Completed: {metrics.tasks_completed}")
print(f"Average Response Time: {metrics.avg_response_time}s")
print(f"Success Rate: {metrics.success_rate}%")
print(f"Agent Utilization: {metrics.agent_utilization}")
```

### गुणवत्ता मेट्रिक्स
```python
# Track output quality
quality_report = await orchestrator.generate_quality_report()
print(f"Output Consistency: {quality_report.consistency_score}")
print(f"Factual Accuracy: {quality_report.accuracy_score}")
print(f"Completeness: {quality_report.completeness_score}")
```

## शिकण्याचे परिणाम

या नमुन्याचा अभ्यास केल्यानंतर तुम्हाला समजेल:

1. **मल्टी-एजंट सिस्टम आर्किटेक्चर**
   - एजंट समन्वय नमुने
   - कार्य वितरण धोरणे
   - निकाल संश्लेषण तंत्र
   - एजंट्समधील संदर्भ व्यवस्थापन

2. **मायक्रोसॉफ्ट फाउंड्री लोकल एकत्रीकरण**
   - कार्य कॉलिंग अंमलबजावणी
   - साधन एकत्रीकरण नमुने
   - मल्टी-मॉडेल ऑर्केस्ट्रेशन
   - कार्यक्षमता ऑप्टिमायझेशन

3. **प्रगत AI ऑर्केस्ट्रेशन**
   - कार्यप्रवाह डिझाइन आणि अंमलबजावणी
   - गुणवत्ता हमी यंत्रणा
   - त्रुटी हाताळणी आणि पुनर्प्राप्ती
   - स्केलेबिलिटी विचार

4. **उत्पादन प्रणाली डिझाइन**
   - निरीक्षण आणि विश्लेषण
   - कॉन्फिगरेशन व्यवस्थापन
   - सुरक्षा सर्वोत्तम पद्धती
   - कार्यक्षमता ट्यूनिंग

## पुढील पावले

- **नमुना 10**: फाउंड्री लोकल साधन एकत्रीकरण म्हणून
- **प्रगत विषय**: कस्टम एजंट विकास
- **स्केलिंग**: वितरित एजंट सिस्टम्स
- **एकत्रीकरण**: एंटरप्राइझ कार्यप्रवाह एकत्रीकरण

## योगदान

योगदानाच्या सूचनांसाठी मुख्य रेपॉजिटरी मार्गदर्शक पहा.

## परवाना

हा नमुना मायक्रोसॉफ्ट फाउंड्री लोकल प्रकल्पाच्या समान परवान्याचे अनुसरण करतो.

---

