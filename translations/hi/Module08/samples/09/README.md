# मल्टी-एजेंट ऑर्केस्ट्रेशन सिस्टम - फाउंड्री लोकल

Microsoft Foundry Local द्वारा संचालित एक उन्नत मल्टी-एजेंट सिस्टम, जो बुद्धिमान एजेंट समन्वय, विशेष कार्य वितरण, और सहयोगात्मक समस्या समाधान पैटर्न को प्रदर्शित करता है।

## अवलोकन

यह सैंपल दिखाता है कि Foundry Local का उपयोग करके परिष्कृत AI एजेंट सिस्टम कैसे बनाया जा सकता है, जिसमें Microsoft के आधिकारिक पैटर्न का उपयोग किया गया है जैसे कि फंक्शन कॉलिंग, एजेंट ऑर्केस्ट्रेशन, और सहयोगात्मक AI वर्कफ़्लो।

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

## मुख्य विशेषताएं

### 🤖 **बुद्धिमान एजेंट समन्वय**
- डायनामिक कार्य विश्लेषण और एजेंट चयन
- स्वचालित कार्यभार वितरण
- परिणाम एकत्रीकरण और संश्लेषण
- क्रॉस-एजेंट संचार प्रोटोकॉल

### 🔧 **विशेष एजेंट प्रकार**
- **कोड विशेषज्ञ**: प्रोग्रामिंग, डिबगिंग, कोड समीक्षा
- **डेटा विश्लेषक**: डेटा प्रोसेसिंग, विज़ुअलाइज़ेशन, इनसाइट्स
- **शोध सहायक**: जानकारी एकत्र करना, सारांश बनाना
- **लेखन विशेषज्ञ**: सामग्री निर्माण, संपादन, दस्तावेज़ीकरण
- **समस्या समाधानकर्ता**: जटिल तर्क, निर्णय लेना

### ⚡ **उन्नत फंक्शन कॉलिंग**
- Microsoft Foundry Local फंक्शन कॉलिंग पैटर्न
- टाइप-सुरक्षित टूल परिभाषाएं
- स्वचालित पैरामीटर सत्यापन
- त्रुटि प्रबंधन और रिकवरी
- टूल चेनिंग और संरचना

### 🎯 **स्मार्ट टास्क रूटिंग**
- इरादा वर्गीकरण और विश्लेषण
- एजेंट क्षमता मिलान
- लोड बैलेंसिंग और अनुकूलन
- फॉलबैक और पुनरावृत्ति प्रबंधन

## आवश्यकताएँ

### सिस्टम आवश्यकताएँ
- **Python**: 3.9+ (asyncio सपोर्ट के साथ)
- **मेमोरी**: 16GB+ (कई एजेंटों के लिए अनुशंसित)
- **स्टोरेज**: 15GB+ (कई मॉडलों के लिए)
- **CPU/GPU**: मल्टी-कोर प्रोसेसर, GPU अनुशंसित

### निर्भरताएँ
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

## त्वरित शुरुआत

### 1. बेसिक मल्टी-एजेंट वर्कफ़्लो
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

### 2. कस्टम एजेंट निर्माण
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

### 3. फंक्शन कॉलिंग इंटीग्रेशन
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

## प्रोजेक्ट संरचना

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

## एजेंट प्रकारों की गहराई से जानकारी

### 1. कोड विशेषज्ञ एजेंट
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

### 2. शोध सहायक एजेंट
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

### 3. डेटा विश्लेषण एजेंट
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

## ऑर्केस्ट्रेशन पैटर्न

### 1. अनुक्रमिक वर्कफ़्लो
```python
# Define a sequential workflow
workflow = orchestrator.create_workflow("sequential")
workflow.add_step("research", ResearchAgent, "gather_requirements")
workflow.add_step("design", CodeAgent, "create_architecture")  
workflow.add_step("implement", CodeAgent, "write_code")
workflow.add_step("test", CodeAgent, "create_tests")

result = await workflow.execute("Build a REST API for user management")
```

### 2. समानांतर निष्पादन
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

### 3. डायनामिक एजेंट चयन
```python
# Automatic agent selection based on task analysis
task = "Create a machine learning model to predict customer churn"

# Orchestrator analyzes task and selects appropriate agents
selected_agents = await orchestrator.analyze_task_requirements(task)
# Returns: [DataAgent, CodeAgent, ResearchAgent]

result = await orchestrator.execute_with_agents(task, selected_agents)
```

## फंक्शन कॉलिंग इंटीग्रेशन

### Microsoft Foundry Local पैटर्न
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

## उन्नत समन्वय सुविधाएँ

### 1. संदर्भ प्रबंधन
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

### 3. गुणवत्ता आश्वासन
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

### 1. मॉडल लोड बैलेंसिंग
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

### 2. कैशिंग और मेमोरी
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

### 3. समवर्ती निष्पादन
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

## उपयोग के उदाहरण

### उदाहरण 1: सॉफ़्टवेयर विकास वर्कफ़्लो
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

### उदाहरण 2: शोध और विश्लेषण
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

## कॉन्फ़िगरेशन और कस्टमाइज़ेशन

### एजेंट कॉन्फ़िगरेशन
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

### वर्कफ़्लो कस्टमाइज़ेशन
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

## निगरानी और विश्लेषण

### प्रदर्शन ट्रैकिंग
```python
# Monitor orchestrator performance
metrics = await orchestrator.get_performance_metrics()
print(f"Tasks Completed: {metrics.tasks_completed}")
print(f"Average Response Time: {metrics.avg_response_time}s")
print(f"Success Rate: {metrics.success_rate}%")
print(f"Agent Utilization: {metrics.agent_utilization}")
```

### गुणवत्ता मीट्रिक्स
```python
# Track output quality
quality_report = await orchestrator.generate_quality_report()
print(f"Output Consistency: {quality_report.consistency_score}")
print(f"Factual Accuracy: {quality_report.accuracy_score}")
print(f"Completeness: {quality_report.completeness_score}")
```

## सीखने के परिणाम

इस सैंपल को पूरा करने के बाद, आप समझेंगे:

1. **मल्टी-एजेंट सिस्टम आर्किटेक्चर**
   - एजेंट समन्वय पैटर्न
   - कार्य वितरण रणनीतियाँ
   - परिणाम संश्लेषण तकनीक
   - एजेंटों के बीच संदर्भ प्रबंधन

2. **Microsoft Foundry Local इंटीग्रेशन**
   - फंक्शन कॉलिंग कार्यान्वयन
   - टूल इंटीग्रेशन पैटर्न
   - मल्टी-मॉडल ऑर्केस्ट्रेशन
   - प्रदर्शन अनुकूलन

3. **उन्नत AI ऑर्केस्ट्रेशन**
   - वर्कफ़्लो डिज़ाइन और निष्पादन
   - गुणवत्ता आश्वासन तंत्र
   - त्रुटि प्रबंधन और रिकवरी
   - स्केलेबिलिटी विचार

4. **प्रोडक्शन सिस्टम डिज़ाइन**
   - निगरानी और विश्लेषण
   - कॉन्फ़िगरेशन प्रबंधन
   - सुरक्षा सर्वोत्तम प्रथाएँ
   - प्रदर्शन ट्यूनिंग

## अगले कदम

- **सैंपल 10**: Foundry Local को टूल्स इंटीग्रेशन के रूप में उपयोग करना
- **उन्नत विषय**: कस्टम एजेंट विकास
- **स्केलिंग**: वितरित एजेंट सिस्टम
- **इंटीग्रेशन**: एंटरप्राइज़ वर्कफ़्लो इंटीग्रेशन

## योगदान

योगदान निर्देशों के लिए मुख्य रिपॉजिटरी दिशानिर्देश देखें।

## लाइसेंस

यह सैंपल Microsoft Foundry Local प्रोजेक्ट के समान लाइसेंस का पालन करता है।

---

