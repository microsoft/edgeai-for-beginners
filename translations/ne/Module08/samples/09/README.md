# मल्टी-एजेन्ट समन्वय प्रणाली - फाउन्ड्री लोकल

Microsoft Foundry Local द्वारा संचालित एक उन्नत मल्टी-एजेन्ट प्रणाली जसले बौद्धिक एजेन्ट समन्वय, विशेष कार्य प्रतिनिधि, र सहकार्यात्मक समस्या समाधान ढाँचाहरू प्रदर्शन गर्दछ।

## अवलोकन

यो नमूनाले Foundry Local प्रयोग गरेर परिष्कृत AI एजेन्ट प्रणाली निर्माण गर्ने तरिका देखाउँछ, जसमा Microsoft का आधिकारिक ढाँचाहरू कार्य कलिंग, एजेन्ट समन्वय, र सहकार्यात्मक AI कार्यप्रवाहहरू समावेश छन्।

## वास्तुकला

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

## मुख्य विशेषताहरू

### 🤖 **बौद्धिक एजेन्ट समन्वय**
- गतिशील कार्य विश्लेषण र एजेन्ट चयन
- स्वचालित कार्यभार वितरण
- परिणाम संकलन र संश्लेषण
- क्रस-एजेन्ट सञ्चार प्रोटोकलहरू

### 🔧 **विशेष एजेन्ट प्रकारहरू**
- **कोड विशेषज्ञ**: प्रोग्रामिङ, डिबगिङ, कोड समीक्षा
- **डाटा विश्लेषक**: डाटा प्रशोधन, दृश्यात्मकता, अन्तर्दृष्टि
- **अनुसन्धान सहायक**: जानकारी सङ्कलन, संक्षेपण
- **लेखन विशेषज्ञ**: सामग्री सिर्जना, सम्पादन, दस्तावेजीकरण
- **समस्या समाधानकर्ता**: जटिल तर्क, निर्णय लिने

### ⚡ **उन्नत कार्य कलिंग**
- Microsoft Foundry Local कार्य कलिंग ढाँचाहरू
- प्रकार-सुरक्षित उपकरण परिभाषा
- स्वचालित प्यारामिटर प्रमाणीकरण
- त्रुटि व्यवस्थापन र पुनःप्राप्ति
- उपकरण श्रृंखला र संरचना

### 🎯 **स्मार्ट कार्य रुटिङ**
- उद्देश्य वर्गीकरण र विश्लेषण
- एजेन्ट क्षमता मिलान
- लोड सन्तुलन र अनुकूलन
- फलब्याक र अतिरिक्त व्यवस्थापन

## पूर्वापेक्षाहरू

### प्रणाली आवश्यकताहरू
- **Python**: 3.9+ asyncio समर्थनसहित
- **मेमोरी**: बहु-एजेन्टहरूको लागि 16GB+ सिफारिस गरिएको
- **स्टोरेज**: बहु-मोडलहरूको लागि 15GB+
- **CPU/GPU**: बहु-कोर प्रोसेसर, GPU सिफारिस गरिएको

### निर्भरताहरू
```bash
pip install foundry-local-sdk openai aiohttp asyncio pydantic rich typer
```

### फाउन्ड्री लोकल सेटअप
```powershell
# Install and verify Foundry Local
winget install Microsoft.FoundryLocal
foundry --version

# Download recommended models for agents
foundry model download phi-4-mini
foundry model download qwen2.5-coder-0.5b
foundry model download phi-3.5-mini
```

## छिटो सुरु

### 1. आधारभूत मल्टी-एजेन्ट कार्यप्रवाह
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

### 2. अनुकूलित एजेन्ट सिर्जना
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

### 3. कार्य कलिंग एकीकरण
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

## परियोजना संरचना

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

## एजेन्ट प्रकारहरूको विस्तृत अध्ययन

### 1. कोड विशेषज्ञ एजेन्ट
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

### 2. अनुसन्धान सहायक एजेन्ट
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

### 3. डाटा विश्लेषण एजेन्ट
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

## समन्वय ढाँचाहरू

### 1. क्रमिक कार्यप्रवाह
```python
# Define a sequential workflow
workflow = orchestrator.create_workflow("sequential")
workflow.add_step("research", ResearchAgent, "gather_requirements")
workflow.add_step("design", CodeAgent, "create_architecture")  
workflow.add_step("implement", CodeAgent, "write_code")
workflow.add_step("test", CodeAgent, "create_tests")

result = await workflow.execute("Build a REST API for user management")
```

### 2. समानान्तर कार्यान्वयन
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

### 3. गतिशील एजेन्ट चयन
```python
# Automatic agent selection based on task analysis
task = "Create a machine learning model to predict customer churn"

# Orchestrator analyzes task and selects appropriate agents
selected_agents = await orchestrator.analyze_task_requirements(task)
# Returns: [DataAgent, CodeAgent, ResearchAgent]

result = await orchestrator.execute_with_agents(task, selected_agents)
```

## कार्य कलिंग एकीकरण

### Microsoft Foundry Local ढाँचाहरू
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

## उन्नत समन्वय सुविधाहरू

### 1. सन्दर्भ व्यवस्थापन
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

### 2. परिणाम संश्लेषण
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

### 3. गुणस्तर सुनिश्चितता
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

## प्रदर्शन अनुकूलन

### 1. मोडेल लोड सन्तुलन
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

### 2. क्यासिङ र मेमोरी
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

### 3. समानान्तर कार्यान्वयन
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

## प्रयोग उदाहरणहरू

### उदाहरण 1: सफ्टवेयर विकास कार्यप्रवाह
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

### उदाहरण 2: अनुसन्धान र विश्लेषण
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

### उदाहरण 3: समस्या समाधान सत्र
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

## कन्फिगरेसन र अनुकूलन

### एजेन्ट कन्फिगरेसन
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

### कार्यप्रवाह अनुकूलन
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

## अनुगमन र विश्लेषण

### प्रदर्शन ट्र्याकिङ
```python
# Monitor orchestrator performance
metrics = await orchestrator.get_performance_metrics()
print(f"Tasks Completed: {metrics.tasks_completed}")
print(f"Average Response Time: {metrics.avg_response_time}s")
print(f"Success Rate: {metrics.success_rate}%")
print(f"Agent Utilization: {metrics.agent_utilization}")
```

### गुणस्तर मेट्रिक्स
```python
# Track output quality
quality_report = await orchestrator.generate_quality_report()
print(f"Output Consistency: {quality_report.consistency_score}")
print(f"Factual Accuracy: {quality_report.accuracy_score}")
print(f"Completeness: {quality_report.completeness_score}")
```

## सिकाइ परिणामहरू

यो नमूना पूरा गरेपछि, तपाईंले बुझ्नुहुनेछ:

1. **मल्टी-एजेन्ट प्रणाली वास्तुकला**
   - एजेन्ट समन्वय ढाँचाहरू
   - कार्य वितरण रणनीतिहरू
   - परिणाम संश्लेषण प्रविधिहरू
   - एजेन्टहरू बीच सन्दर्भ व्यवस्थापन

2. **Microsoft Foundry Local एकीकरण**
   - कार्य कलिंग कार्यान्वयन
   - उपकरण एकीकरण ढाँचाहरू
   - बहु-मोडल समन्वय
   - प्रदर्शन अनुकूलन

3. **उन्नत AI समन्वय**
   - कार्यप्रवाह डिजाइन र कार्यान्वयन
   - गुणस्तर सुनिश्चितता संयन्त्रहरू
   - त्रुटि व्यवस्थापन र पुनःप्राप्ति
   - मापनयोग्यता विचारहरू

4. **उत्पादन प्रणाली डिजाइन**
   - अनुगमन र विश्लेषण
   - कन्फिगरेसन व्यवस्थापन
   - सुरक्षा उत्तम अभ्यासहरू
   - प्रदर्शन ट्युनिङ

## आगामी कदमहरू

- **नमूना 10**: उपकरण एकीकरणको रूपमा Foundry Local
- **उन्नत विषयहरू**: अनुकूलित एजेन्ट विकास
- **मापन**: वितरित एजेन्ट प्रणालीहरू
- **एकीकरण**: उद्यम कार्यप्रवाह एकीकरण

## योगदान

योगदान निर्देशनहरूको लागि मुख्य रिपोजिटरी दिशानिर्देशहरू हेर्नुहोस्।

## लाइसेन्स

यो नमूनाले Microsoft Foundry Local परियोजनाको समान लाइसेन्स अनुसरण गर्दछ।

---

