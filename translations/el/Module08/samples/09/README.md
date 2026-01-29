# Σύστημα Ορχήστρωσης Πολλαπλών Πρακτόρων - Foundry Local

Ένα προηγμένο σύστημα πολλαπλών πρακτόρων που υποστηρίζεται από το Microsoft Foundry Local, το οποίο επιδεικνύει συντονισμό ευφυών πρακτόρων, εξειδικευμένη ανάθεση εργασιών και μοτίβα συνεργατικής επίλυσης προβλημάτων.

## Επισκόπηση

Αυτό το δείγμα παρουσιάζει πώς να δημιουργήσετε εξελιγμένα συστήματα AI πρακτόρων χρησιμοποιώντας το Foundry Local, εφαρμόζοντας τα επίσημα μοτίβα της Microsoft για κλήση λειτουργιών, ορχήστρωση πρακτόρων και συνεργατικές ροές εργασίας AI.

## Αρχιτεκτονική

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

## Βασικά Χαρακτηριστικά

### 🤖 **Συντονισμός Ευφυών Πρακτόρων**
- Δυναμική ανάλυση εργασιών και επιλογή πρακτόρων
- Αυτόματη κατανομή φόρτου εργασίας
- Συγκέντρωση και σύνθεση αποτελεσμάτων
- Πρωτόκολλα επικοινωνίας μεταξύ πρακτόρων

### 🔧 **Εξειδικευμένοι Τύποι Πρακτόρων**
- **Code Expert**: Προγραμματισμός, αποσφαλμάτωση, ανασκόπηση κώδικα
- **Data Analyst**: Επεξεργασία δεδομένων, οπτικοποίηση, εξαγωγή συμπερασμάτων
- **Research Assistant**: Συλλογή πληροφοριών, περίληψη
- **Writing Specialist**: Δημιουργία περιεχομένου, επεξεργασία, τεκμηρίωση
- **Problem Solver**: Σύνθετη λογική, λήψη αποφάσεων

### ⚡ **Προηγμένη Κλήση Λειτουργιών**
- Μοτίβα κλήσης λειτουργιών του Microsoft Foundry Local
- Ορισμοί εργαλείων με ασφάλεια τύπου
- Αυτόματη επικύρωση παραμέτρων
- Διαχείριση σφαλμάτων και ανάκαμψη
- Σύνδεση και σύνθεση εργαλείων

### 🎯 **Έξυπνη Δρομολόγηση Εργασιών**
- Ταξινόμηση και ανάλυση προθέσεων
- Αντιστοίχιση δυνατοτήτων πρακτόρων
- Εξισορρόπηση φόρτου και βελτιστοποίηση
- Διαχείριση εφεδρείας και πτώσης

## Προαπαιτούμενα

### Απαιτήσεις Συστήματος
- **Python**: Έκδοση 3.9+ με υποστήριξη asyncio
- **Μνήμη**: Συνιστάται 16GB+ για πολλαπλούς πράκτορες
- **Αποθήκευση**: 15GB+ για πολλαπλά μοντέλα
- **CPU/GPU**: Πολυπύρηνος επεξεργαστής, συνιστάται GPU

### Εξαρτήσεις
```bash
pip install foundry-local-sdk openai aiohttp asyncio pydantic rich typer
```

### Ρύθμιση Foundry Local
```powershell
# Install and verify Foundry Local
winget install Microsoft.FoundryLocal
foundry --version

# Download recommended models for agents
foundry model download phi-4-mini
foundry model download qwen2.5-coder-0.5b
foundry model download phi-3.5-mini
```

## Γρήγορη Εκκίνηση

### 1. Βασική Ροή Εργασίας Πολλαπλών Πρακτόρων
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

### 2. Δημιουργία Εξατομικευμένων Πρακτόρων
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

### 3. Ενσωμάτωση Κλήσης Λειτουργιών
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

## Δομή Έργου

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

## Εμβάθυνση στους Τύπους Πρακτόρων

### 1. Πράκτορας Ειδικός στον Κώδικα
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

### 2. Πράκτορας Βοηθός Έρευνας
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

### 3. Πράκτορας Ανάλυσης Δεδομένων
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

## Μοτίβα Ορχήστρωσης

### 1. Διαδοχική Ροή Εργασίας
```python
# Define a sequential workflow
workflow = orchestrator.create_workflow("sequential")
workflow.add_step("research", ResearchAgent, "gather_requirements")
workflow.add_step("design", CodeAgent, "create_architecture")  
workflow.add_step("implement", CodeAgent, "write_code")
workflow.add_step("test", CodeAgent, "create_tests")

result = await workflow.execute("Build a REST API for user management")
```

### 2. Παράλληλη Εκτέλεση
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

### 3. Δυναμική Επιλογή Πρακτόρων
```python
# Automatic agent selection based on task analysis
task = "Create a machine learning model to predict customer churn"

# Orchestrator analyzes task and selects appropriate agents
selected_agents = await orchestrator.analyze_task_requirements(task)
# Returns: [DataAgent, CodeAgent, ResearchAgent]

result = await orchestrator.execute_with_agents(task, selected_agents)
```

## Ενσωμάτωση Κλήσης Λειτουργιών

### Μοτίβα του Microsoft Foundry Local
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

## Προηγμένα Χαρακτηριστικά Συντονισμού

### 1. Διαχείριση Πλαισίου
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

### 2. Σύνθεση Αποτελεσμάτων
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

### 3. Διασφάλιση Ποιότητας
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

## Βελτιστοποίηση Απόδοσης

### 1. Εξισορρόπηση Φόρτου Μοντέλων
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

### 2. Cache και Μνήμη
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

### 3. Παράλληλη Εκτέλεση
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

## Παραδείγματα Χρήσης

### Παράδειγμα 1: Ροή Εργασίας Ανάπτυξης Λογισμικού
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

### Παράδειγμα 2: Έρευνα και Ανάλυση
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

### Παράδειγμα 3: Συνεδρία Επίλυσης Προβλημάτων
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

## Ρύθμιση και Εξατομίκευση

### Ρύθμιση Πρακτόρων
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

### Εξατομίκευση Ροής Εργασίας
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

## Παρακολούθηση και Αναλυτικά Στοιχεία

### Παρακολούθηση Απόδοσης
```python
# Monitor orchestrator performance
metrics = await orchestrator.get_performance_metrics()
print(f"Tasks Completed: {metrics.tasks_completed}")
print(f"Average Response Time: {metrics.avg_response_time}s")
print(f"Success Rate: {metrics.success_rate}%")
print(f"Agent Utilization: {metrics.agent_utilization}")
```

### Μετρήσεις Ποιότητας
```python
# Track output quality
quality_report = await orchestrator.generate_quality_report()
print(f"Output Consistency: {quality_report.consistency_score}")
print(f"Factual Accuracy: {quality_report.accuracy_score}")
print(f"Completeness: {quality_report.completeness_score}")
```

## Μαθησιακά Αποτελέσματα

Με την ολοκλήρωση αυτού του δείγματος, θα κατανοήσετε:

1. **Αρχιτεκτονική Συστημάτων Πολλαπλών Πρακτόρων**
   - Μοτίβα συντονισμού πρακτόρων
   - Στρατηγικές κατανομής εργασιών
   - Τεχνικές σύνθεσης αποτελεσμάτων
   - Διαχείριση πλαισίου μεταξύ πρακτόρων

2. **Ενσωμάτωση Microsoft Foundry Local**
   - Εφαρμογή κλήσης λειτουργιών
   - Μοτίβα ενσωμάτωσης εργαλείων
   - Ορχήστρωση πολλαπλών μοντέλων
   - Βελτιστοποίηση απόδοσης

3. **Προηγμένη Ορχήστρωση AI**
   - Σχεδιασμός και εκτέλεση ροών εργασίας
   - Μηχανισμοί διασφάλισης ποιότητας
   - Διαχείριση σφαλμάτων και ανάκαμψη
   - Σκέψεις για κλιμάκωση

4. **Σχεδιασμός Συστήματος Παραγωγής**
   - Παρακολούθηση και αναλυτικά στοιχεία
   - Διαχείριση ρυθμίσεων
   - Βέλτιστες πρακτικές ασφάλειας
   - Ρύθμιση απόδοσης

## Επόμενα Βήματα

- **Δείγμα 10**: Foundry Local ως Ενσωμάτωση Εργαλείων
- **Προχωρημένα Θέματα**: Ανάπτυξη εξατομικευμένων πρακτόρων
- **Κλιμάκωση**: Διανεμημένα συστήματα πρακτόρων
- **Ενσωμάτωση**: Ενσωμάτωση ροών εργασίας σε επιχειρήσεις

## Συνεισφορά

Δείτε τις οδηγίες του κύριου αποθετηρίου για οδηγίες συνεισφοράς.

## Άδεια Χρήσης

Αυτό το δείγμα ακολουθεί την ίδια άδεια χρήσης με το έργο Microsoft Foundry Local.

---

