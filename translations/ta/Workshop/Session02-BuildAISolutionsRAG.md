# அமர்வு 2: Azure AI Foundry மூலம் AI தீர்வுகளை உருவாக்குதல்

## சுருக்கம்

Foundry Local மற்றும் Azure AI Foundry பயன்படுத்தி செயல்படக்கூடிய GenAI வேலைப்பாடுகளை உருவாக்குவது எப்படி என்பதை ஆராயுங்கள். மேம்பட்ட ப்ராம்ப்ட் இன்ஜினியரிங், கட்டமைக்கப்பட்ட தரவுகளை ஒருங்கிணைத்தல், மற்றும் மறுபுருவிக்கக்கூடிய பைப்ப்லைன்களுடன் பணிகளை ஒருங்கிணைத்தல் ஆகியவற்றை கற்றுக்கொள்ளுங்கள். ஆவணங்கள் மற்றும் தரவுகளுக்கான கேள்வி-பதில் (Q&A) Retrieval-Augmented Generation (RAG) முறைமைகளில் கவனம் செலுத்தப்பட்டாலும், இந்த முறைமைகள் பரந்த GenAI தீர்வு வடிவமைப்புக்கு பொதுவாக பொருந்தும்.

## கற்றல் நோக்கங்கள்

இந்த அமர்வின் முடிவில், நீங்கள்:

- **ப்ராம்ப்ட் இன்ஜினியரிங்கில் நிபுணத்துவம் பெறுவீர்கள்**: செயல்திறன் வாய்ந்த சிஸ்டம் ப்ராம்ப்ட்கள் மற்றும் நிலைமைகள் வடிவமைத்தல்
- **RAG முறைமைகளை செயல்படுத்துவீர்கள்**: வெக்டர் தேடலுடன் ஆவண அடிப்படையிலான Q&A அமைப்புகளை உருவாக்குதல்
- **கட்டமைக்கப்பட்ட தரவுகளை ஒருங்கிணைத்தல்**: AI வேலைப்பாடுகளில் CSV, JSON மற்றும் அட்டவணை தரவுகளுடன் பணிபுரிதல்
- **தயாரிப்பு RAG உருவாக்குதல்**: Chainlit மூலம் அளவளாவிய RAG பயன்பாடுகளை உருவாக்குதல்
- **Foundry Local-இல் இருந்து Cloud-க்கு பாலம் அமைத்தல்**: Azure AI Foundry-க்கு மைக்ரேஷன் பாதைகளை புரிந்துகொள்ளுதல்

## முன் தேவைகள்

- அமர்வு 1 (Foundry Local அமைப்பு) முடித்திருக்க வேண்டும்
- வெக்டர் தரவுத்தொகைகள் மற்றும் எம்பெடிங்குகள் பற்றிய அடிப்படை புரிதல்
- Python நிரலாக்க அனுபவம்
- ஆவண செயலாக்கக் கருத்துக்களில் பரிச்சயம்

### குறுக்குவெளி சூழல் விரைவான தொடக்கம் (Windows & macOS)

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai sentence-transformers ragas datasets scikit-learn
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai sentence-transformers ragas datasets scikit-learn
```

Foundry Local macOS binaries உங்கள் சூழலில் இன்னும் கிடைக்கவில்லை என்றால், Windows VM அல்லது கெண்டெய்னரில் சேவையை இயக்கி அமைக்கவும்:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## சரிபார்ப்பு: Foundry Local சூழல் சரிபார்ப்பு

டெமோக்களை தொடங்குவதற்கு முன், உங்கள் உள்ளூர் சூழலை சரிபார்க்கவும்:

```powershell
foundry --version              # Ensure CLI is installed
foundry status                 # Service status
foundry model run phi-4-mini   # Start baseline SLM
curl http://localhost:5273/v1/models  # Validate API (should list running model)
```

கடைசி கட்டளை தோல்வியடைந்தால், சேவையை தொடங்கவும் (அல்லது மீண்டும் தொடங்கவும்): `foundry service start`.

## டெமோ ஓட்டம் (30 நிமிடங்கள்)

### 1. சிஸ்டம் ப்ராம்ப்ட்கள் மற்றும் நிலைமைகள் (10 நிமிடங்கள்)

#### படி 1.1: மேம்பட்ட ப்ராம்ப்ட் இன்ஜினியரிங்

`samples/02-rag-solutions/prompt_engineering.py` உருவாக்கவும்:

```python
#!/usr/bin/env python3
"""
Advanced Prompt Engineering with Foundry Local
Demo: System prompts, grounding, and context management
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os
from openai import OpenAI
from typing import List, Dict, Any

class PromptEngineer:
    """Advanced prompt engineering utilities for Foundry Local"""
    
    def __init__(self, base_url: str = "http://localhost:5273/v1"):
        self.client = OpenAI(
            base_url=base_url,
            api_key="not-needed"
        )
    
    def create_grounded_prompt(self, 
                             context: str, 
                             question: str, 
                             domain: str = "general") -> List[Dict[str, str]]:
        """Create a grounded prompt with context and domain expertise"""
        
        system_prompts = {
            "general": "You are a helpful AI assistant. Use the provided context to answer questions accurately and concisely.",
            "medical": "You are a medical AI assistant. Provide evidence-based responses using the medical literature context. Always include disclaimers about consulting healthcare professionals.",
            "legal": "You are a legal research assistant. Analyze the provided legal documents and statutes. Note that this is for informational purposes only.",
            "technical": "You are a technical documentation assistant. Provide detailed, accurate responses based on the technical documentation provided.",
            "financial": "You are a financial analysis assistant. Use the provided financial data to give insights while noting this is not financial advice."
        }
        
        return [
            {
                "role": "system", 
                "content": system_prompts.get(domain, system_prompts["general"])
            },
            {
                "role": "user", 
                "content": f"""
                Context Information:
                {context}
                
                Question: {question}
                
                Please provide a comprehensive answer based on the context above. If the context doesn't contain enough information to fully answer the question, please state that clearly.
                """.strip()
            }
        ]
    
    def chat_with_grounding(self, 
                          context: str, 
                          question: str, 
                          model: str = "phi-4-mini",
                          domain: str = "general") -> Dict[str, Any]:
        """Execute grounded chat completion"""
        
        messages = self.create_grounded_prompt(context, question, domain)
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=1000,
                temperature=0.3,  # Lower temperature for more consistent responses
                top_p=0.9
            )
            
            return {
                "answer": response.choices[0].message.content,
                "model": response.model,
                "tokens": response.usage.total_tokens if response.usage else None,
                "context_length": len(context),
                "domain": domain
            }
            
        except Exception as e:
            return {"error": str(e)}

def demo_grounding_strategies():
    """Demonstrate different grounding strategies"""
    
    engineer = PromptEngineer()
    
    # Sample contexts for different domains
    contexts = {
        "technical": """
        Microsoft Foundry Local is a development platform that enables running AI models locally on Windows devices. 
        It supports various model formats including ONNX and provides hardware acceleration through DirectML.
        The platform includes a CLI for model management and an OpenAI-compatible API for integration.
        Models can be cached locally and run without internet connectivity.
        """,
        
        "financial": """
        Q3 2024 Results: Revenue $45.2M (up 23% YoY), Operating Margin 18.5%, 
        Cash Flow $12.3M, R&D Investment $8.7M (19% of revenue).
        Key metrics: Customer Acquisition Cost $1,200, Lifetime Value $15,600, Monthly Churn 2.1%.
        Geographic breakdown: North America 65%, Europe 25%, APAC 10%.
        """
    }
    
    questions = {
        "technical": "How does Foundry Local handle model caching and what are the benefits?",
        "financial": "What is the current financial health and what are the key performance indicators?"
    }
    
    for domain in ["technical", "financial"]:
        print(f"\n{'='*50}")
        print(f"Domain: {domain.upper()}")
        print(f"{'='*50}")
        
        result = engineer.chat_with_grounding(
            context=contexts[domain],
            question=questions[domain],
            domain=domain
        )
        
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Answer: {result['answer']}")
            print(f"Tokens used: {result['tokens']}")
            print(f"Context length: {result['context_length']} characters")

if __name__ == "__main__":
    demo_grounding_strategies()
```

#### படி 1.2: நிலைமைகளை சோதிக்கவும்

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the prompt engineering demo
python samples/02-rag-solutions/prompt_engineering.py
```


### 2. அட்டவணை தரவுகளை ப்ராம்ப்ட்களுடன் ஒருங்கிணைத்தல் (CSV Q&A) (10 நிமிடங்கள்)

#### படி 2.1: CSV தரவுகளை ஒருங்கிணைத்தல்

`samples/02-rag-solutions/csv_qa_system.py` உருவாக்கவும்:

```python
#!/usr/bin/env python3
"""
CSV Q&A System with Foundry Local
Demo: Structured data integration and tabular reasoning
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import pandas as pd
import json
import os
from openai import OpenAI
from typing import Dict, Any, List
import io

class CSVQASystem:
    """CSV Question-Answering system using Foundry Local"""
    
    def __init__(self, base_url: str = "http://localhost:5273/v1"):
        self.client = OpenAI(
            base_url=base_url,
            api_key="not-needed"
        )
        self.data = None
        self.summary_stats = None
    
    def load_csv_data(self, csv_path: str) -> bool:
        """Load and analyze CSV data"""
        try:
            self.data = pd.read_csv(csv_path)
            self.summary_stats = self._generate_summary_stats()
            return True
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return False
    
    def _generate_summary_stats(self) -> Dict[str, Any]:
        """Generate comprehensive summary statistics"""
        stats = {
            "shape": self.data.shape,
            "columns": list(self.data.columns),
            "dtypes": self.data.dtypes.to_dict(),
            "null_counts": self.data.isnull().sum().to_dict(),
            "sample_rows": self.data.head(3).to_dict('records')
        }
        
        # Add numerical statistics for numeric columns
        numeric_cols = self.data.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            stats["numeric_summary"] = self.data[numeric_cols].describe().to_dict()
        
        # Add categorical summaries
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            stats["categorical_summary"] = {}
            for col in categorical_cols:
                stats["categorical_summary"][col] = {
                    "unique_count": self.data[col].nunique(),
                    "top_values": self.data[col].value_counts().head(5).to_dict()
                }
        
        return stats
    
    def create_data_context(self, question: str) -> str:
        """Create relevant data context for the question"""
        context_parts = [
            f"Dataset Overview:",
            f"- Shape: {self.summary_stats['shape'][0]} rows, {self.summary_stats['shape'][1]} columns",
            f"- Columns: {', '.join(self.summary_stats['columns'])}"
        ]
        
        # Add sample data
        context_parts.append("\nSample Data:")
        for i, row in enumerate(self.summary_stats['sample_rows'][:3]):
            context_parts.append(f"Row {i+1}: {json.dumps(row, default=str)}")
        
        # Add relevant statistics based on question content
        question_lower = question.lower()
        
        if any(word in question_lower for word in ['average', 'mean', 'sum', 'count', 'max', 'min', 'statistics']):
            if 'numeric_summary' in self.summary_stats:
                context_parts.append("\nNumerical Statistics:")
                for col, stats in self.summary_stats['numeric_summary'].items():
                    context_parts.append(f"{col}: mean={stats['mean']:.2f}, std={stats['std']:.2f}, min={stats['min']}, max={stats['max']}")
        
        if any(word in question_lower for word in ['category', 'group', 'type', 'unique']):
            if 'categorical_summary' in self.summary_stats:
                context_parts.append("\nCategorical Data Summary:")
                for col, info in self.summary_stats['categorical_summary'].items():
                    context_parts.append(f"{col}: {info['unique_count']} unique values, top: {list(info['top_values'].keys())[:3]}")
        
        return "\n".join(context_parts)
    
    def answer_question(self, question: str, model: str = "phi-4-mini") -> Dict[str, Any]:
        """Answer questions about the CSV data"""
        
        if self.data is None:
            return {"error": "No data loaded. Please load CSV data first."}
        
        context = self.create_data_context(question)
        
        messages = [
            {
                "role": "system",
                "content": """
                You are a data analysis assistant. You have access to a CSV dataset and its summary statistics.
                Answer questions about the data accurately based on the provided context.
                If calculations are needed, explain your reasoning.
                If the data doesn't contain enough information to answer the question, state that clearly.
                """.strip()
            },
            {
                "role": "user",
                "content": f"""
                Data Context:
                {context}
                
                Question: {question}
                
                Please analyze the data and provide a comprehensive answer.
                """.strip()
            }
        ]
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=800,
                temperature=0.2  # Low temperature for factual data analysis
            )
            
            return {
                "answer": response.choices[0].message.content,
                "model": response.model,
                "tokens": response.usage.total_tokens if response.usage else None,
                "dataset_shape": self.data.shape
            }
            
        except Exception as e:
            return {"error": str(e)}

def create_sample_dataset():
    """Create a sample dataset for demonstration"""
    
    # Create sample sales data
    sales_data = {
        'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
                 '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10'],
        'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 
                   'Accessories', 'Laptop', 'Tablet', 'Phone', 'Accessories'],
        'Sales_Amount': [1200, 800, 600, 1100, 850, 150, 1300, 580, 780, 200],
        'Quantity': [1, 1, 1, 1, 1, 3, 1, 1, 1, 4],
        'Region': ['North', 'South', 'East', 'West', 'North', 
                  'South', 'East', 'West', 'North', 'South'],
        'Sales_Rep': ['Alice', 'Bob', 'Charlie', 'Diana', 'Alice',
                     'Bob', 'Charlie', 'Diana', 'Alice', 'Bob']
    }
    
    df = pd.DataFrame(sales_data)
    csv_path = "samples/02-rag-solutions/sample_sales_data.csv"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    df.to_csv(csv_path, index=False)
    return csv_path

def demo_csv_qa():
    """Demonstrate CSV Q&A capabilities"""
    
    # Create sample dataset
    csv_path = create_sample_dataset()
    print(f"Created sample dataset: {csv_path}")
    
    # Initialize Q&A system
    qa_system = CSVQASystem()
    
    # Load data
    if not qa_system.load_csv_data(csv_path):
        print("Failed to load CSV data")
        return
    
    print(f"\nLoaded dataset with shape: {qa_system.data.shape}")
    
    # Example questions
    questions = [
        "What is the total sales amount?",
        "Which product has the highest average sales amount?",
        "How many sales were made in the North region?",
        "Who is the top performing sales representative?",
        "What is the average quantity sold per transaction?"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n{'='*60}")
        print(f"Question {i}: {question}")
        print(f"{'='*60}")
        
        result = qa_system.answer_question(question)
        
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Answer: {result['answer']}")
            print(f"Tokens used: {result['tokens']}")

if __name__ == "__main__":
    demo_csv_qa()
```

#### படி 2.2: CSV Q&A அமைப்பை சோதிக்கவும்

```powershell
# Run the CSV Q&A demo
python samples/02-rag-solutions/csv_qa_system.py
```


### 3. தொடக்க திட்டம்: 02-grounding-data-ஐ மாற்றுதல் (5 நிமிடங்கள்)

#### படி 3.1: மேம்பட்ட ஆவண RAG அமைப்பு

`samples/02-rag-solutions/document_rag.py` உருவாக்கவும்:

```python
#!/usr/bin/env python3
"""
Document RAG System with Foundry Local
Demo: Document processing, vector search, and retrieval-augmented generation
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os
from openai import OpenAI
import requests
from typing import List, Dict, Any
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import json

class SimpleRAGSystem:
    """Simple RAG system using TF-IDF for demonstration"""
    
    def __init__(self, base_url: str = "http://localhost:5273/v1"):
        self.client = OpenAI(
            base_url=base_url,
            api_key="not-needed"
        )
        self.documents = []
        self.vectorizer = None
        self.doc_vectors = None
    
    def add_documents(self, documents: List[str]):
        """Add documents to the knowledge base"""
        self.documents.extend(documents)
        self._create_vectors()
    
    def _create_vectors(self):
        """Create TF-IDF vectors for documents"""
        if not self.documents:
            return
        
        self.vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words='english',
            ngram_range=(1, 2)
        )
        
        self.doc_vectors = self.vectorizer.fit_transform(self.documents)
    
    def retrieve_relevant_docs(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Retrieve most relevant documents for a query"""
        if not self.documents or self.vectorizer is None:
            return []
        
        # Vectorize query
        query_vector = self.vectorizer.transform([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()
        
        # Get top-k documents
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # Minimum similarity threshold
                results.append({
                    "content": self.documents[idx],
                    "similarity": float(similarities[idx]),
                    "index": int(idx)
                })
        
        return results
    
    def generate_answer(self, 
                       question: str, 
                       model: str = "phi-4-mini",
                       max_context_docs: int = 3) -> Dict[str, Any]:
        """Generate answer using retrieved documents"""
        
        # Retrieve relevant documents
        relevant_docs = self.retrieve_relevant_docs(question, max_context_docs)
        
        if not relevant_docs:
            context = "No relevant documents found in the knowledge base."
        else:
            context_parts = []
            for i, doc in enumerate(relevant_docs, 1):
                context_parts.append(f"Document {i} (relevance: {doc['similarity']:.3f}):\n{doc['content']}")
            context = "\n\n".join(context_parts)
        
        messages = [
            {
                "role": "system",
                "content": """
                You are a helpful AI assistant that answers questions based on provided documents.
                Use the context documents to provide accurate, detailed answers.
                If the documents don't contain sufficient information, say so clearly.
                Always cite which documents you're referencing in your answer.
                """.strip()
            },
            {
                "role": "user",
                "content": f"""
                Context Documents:
                {context}
                
                Question: {question}
                
                Please provide a comprehensive answer based on the context documents above.
                """.strip()
            }
        ]
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=1000,
                temperature=0.3
            )
            
            return {
                "answer": response.choices[0].message.content,
                "model": response.model,
                "tokens": response.usage.total_tokens if response.usage else None,
                "retrieved_docs": len(relevant_docs),
                "context_length": len(context)
            }
            
        except Exception as e:
            return {"error": str(e)}

def create_sample_knowledge_base() -> List[str]:
    """Create a sample knowledge base about AI and technology"""
    
    documents = [
        """
        Microsoft Foundry Local is a comprehensive development platform that enables developers to run AI models locally on Windows devices.
        It provides hardware acceleration through DirectML and supports various model formats including ONNX.
        The platform includes a command-line interface for model management and an OpenAI-compatible API for seamless integration.
        """,
        
        """
        Edge AI refers to the deployment of artificial intelligence algorithms directly on edge devices, such as smartphones, IoT devices, and local computers.
        This approach reduces latency, improves privacy, and enables offline functionality.
        Edge AI is particularly important for real-time applications and scenarios where data privacy is critical.
        """,
        
        """
        Small Language Models (SLMs) are compressed versions of large language models that maintain much of their capabilities while requiring significantly fewer computational resources.
        Examples include Microsoft's Phi models, which can run efficiently on consumer hardware.
        SLMs are ideal for edge deployment and privacy-sensitive applications.
        """,
        
        """
        Vector databases store and retrieve data based on vector representations, enabling semantic search and similarity matching.
        They are essential components in RAG (Retrieval-Augmented Generation) systems, where relevant context is retrieved to enhance AI responses.
        Popular vector databases include Chroma, Pinecone, and Weaviate.
        """,
        
        """
        Prompt engineering is the practice of crafting effective prompts to guide AI model behavior and improve response quality.
        Techniques include few-shot learning, chain-of-thought prompting, and system message optimization.
        Well-designed prompts can significantly improve model performance on specific tasks.
        """,
        
        """
        Azure AI Foundry provides cloud-based AI development capabilities, including model training, deployment, and monitoring.
        It offers integration with Azure services and supports both custom and pre-trained models.
        The platform enables seamless scaling from local development to enterprise deployment.
        """
    ]
    
    return [doc.strip() for doc in documents]

def demo_document_rag():
    """Demonstrate document RAG capabilities"""
    
    # Create RAG system
    rag_system = SimpleRAGSystem()
    
    # Add sample knowledge base
    documents = create_sample_knowledge_base()
    rag_system.add_documents(documents)
    
    print(f"Loaded {len(documents)} documents into knowledge base")
    
    # Example questions
    questions = [
        "What is Microsoft Foundry Local and what are its key features?",
        "How do Small Language Models differ from regular language models?",
        "What is the role of vector databases in RAG systems?",
        "What are the benefits of Edge AI?",
        "How can I improve my prompt engineering skills?"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n{'='*70}")
        print(f"Question {i}: {question}")
        print(f"{'='*70}")
        
        result = rag_system.generate_answer(question)
        
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Answer: {result['answer']}")
            print(f"Retrieved {result['retrieved_docs']} documents")
            print(f"Tokens used: {result['tokens']}")

if __name__ == "__main__":
    demo_document_rag()
```


### 4. CLI-இல் இருந்து Azure மைக்ரேஷன் பாதையை காட்டுதல் (5 நிமிடங்கள்)

#### படி 4.1: மைக்ரேஷன் உத்தி கண்ணோட்டம்

`samples/02-rag-solutions/migration_guide.py` உருவாக்கவும்:

```python
#!/usr/bin/env python3
"""
Foundry Local to Azure AI Foundry Migration Guide
Demo: Code patterns and migration strategies
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os
from openai import OpenAI
from typing import Dict, Any, Optional

class UnifiedAIClient:
    """Unified client that works with both Foundry Local and Azure AI Foundry"""
    
    def __init__(self, 
                 environment: str = "local",
                 azure_endpoint: Optional[str] = None,
                 azure_api_key: Optional[str] = None,
                 azure_api_version: str = "2024-08-01-preview"):
        
        self.environment = environment
        
        if environment == "local":
            # Foundry Local configuration
            self.client = OpenAI(
                base_url="http://localhost:5273/v1",
                api_key="not-needed"
            )
            self.default_model = "phi-4-mini"
            
        elif environment == "azure":
            # Azure AI Foundry configuration
            if not azure_endpoint or not azure_api_key:
                raise ValueError("Azure endpoint and API key required for Azure environment")
            
            self.client = OpenAI(
                base_url=f"{azure_endpoint}/openai/deployments",
                api_key=azure_api_key,
                default_headers={"api-version": azure_api_version}
            )
            self.default_model = "gpt-4"  # Or your Azure deployment name
            
        else:
            raise ValueError("Environment must be 'local' or 'azure'")
    
    def chat_completion(self, 
                       messages: list,
                       model: Optional[str] = None,
                       **kwargs) -> Dict[str, Any]:
        """Unified chat completion that works in both environments"""
        
        model = model or self.default_model
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs
            )
            
            return {
                "success": True,
                "response": response.choices[0].message.content,
                "model": response.model,
                "tokens": response.usage.total_tokens if response.usage else None,
                "environment": self.environment
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "environment": self.environment
            }
    
    def get_available_models(self) -> Dict[str, Any]:
        """Get available models in current environment"""
        
        try:
            if self.environment == "local":
                # For Foundry Local, we'd typically use the CLI
                # This is a simplified example
                return {
                    "success": True,
                    "models": ["phi-4-mini", "qwen2.5-0.5b", "deepseek-coder-1.3b"],
                    "environment": "local"
                }
            else:
                # For Azure, you might query the deployments endpoint
                models_response = self.client.models.list()
                return {
                    "success": True,
                    "models": [model.id for model in models_response.data],
                    "environment": "azure"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "environment": self.environment
            }

def demo_migration_patterns():
    """Demonstrate migration patterns between local and cloud"""
    
    print("Foundry Local to Azure AI Foundry Migration Demo")
    print("=" * 60)
    
    # Test message
    test_messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Provide concise, accurate responses."
        },
        {
            "role": "user",
            "content": "Explain the benefits of edge AI in 2-3 sentences."
        }
    ]
    
    # Test with Foundry Local
    print("\n1. Testing with Foundry Local:")
    print("-" * 40)
    
    try:
        local_client = UnifiedAIClient(environment="local")
        local_result = local_client.chat_completion(
            messages=test_messages,
            max_tokens=200,
            temperature=0.7
        )
        
        if local_result["success"]:
            print(f"✓ Local Response: {local_result['response']}")
            print(f"  Model: {local_result['model']}")
            print(f"  Tokens: {local_result['tokens']}")
        else:
            print(f"✗ Local Error: {local_result['error']}")
            
    except Exception as e:
        print(f"✗ Local Setup Error: {e}")
    
    # Show Azure configuration (commented out as it requires credentials)
    print("\n2. Azure AI Foundry Configuration:")
    print("-" * 40)
    print("""
    # To migrate to Azure AI Foundry, configure as follows:
    
    azure_client = UnifiedAIClient(
        environment="azure",
        azure_endpoint="https://your-resource.openai.azure.com",
        azure_api_key="your-api-key",
        azure_api_version="2024-08-01-preview"
    )
    
    # Same API calls work in both environments!
    azure_result = azure_client.chat_completion(
        messages=test_messages,
        max_tokens=200,
        temperature=0.7
    )
    """)
    
    # Migration strategy
    print("\n3. Migration Strategy:")
    print("-" * 40)
    print("""
    Step 1: Develop and test locally with Foundry Local
    Step 2: Use environment variables for configuration
    Step 3: Test with Azure AI Foundry in staging
    Step 4: Deploy to production with Azure AI Foundry
    
    Benefits of this approach:
    ✓ Faster development cycle (no network latency)
    ✓ Lower development costs (no API charges)
    ✓ Privacy during development (local processing)
    ✓ Easy scaling to production (same API)
    """)
    
    # Configuration examples
    print("\n4. Environment-based Configuration:")
    print("-" * 40)
    print("""
    # .env file for development
    AI_ENVIRONMENT=local
    FOUNDRY_LOCAL_URL=http://localhost:5273/v1
    DEFAULT_MODEL=phi-4-mini
    
    # .env file for production
    AI_ENVIRONMENT=azure
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
    AZURE_OPENAI_API_KEY=your-api-key
    AZURE_OPENAI_API_VERSION=2024-08-01-preview
    DEFAULT_MODEL=gpt-4
    """)

if __name__ == "__main__":
    demo_migration_patterns()
```

#### படி 4.2: மைக்ரேஷன் முறைமைகளை சோதிக்கவும்

```powershell
# Run the migration demo
python samples/02-rag-solutions/migration_guide.py
```


## முக்கிய கருத்துக்கள்

### 1. மேம்பட்ட ப்ராம்ப்ட் இன்ஜினியரிங்

- **சிஸ்டம் ப்ராம்ப்ட்கள்**: துறைக்கு ஏற்ற நிபுணர் ப்ரோபைல்கள்
- **நிலைமைகள்**: சூழல் ஒருங்கிணைப்பு உத்திகள்
- **தீவிரத்தன்மை கட்டுப்பாடு**: படைப்பாற்றல் மற்றும் நிலைத்தன்மை இடையே சமநிலை
- **டோக்கன் மேலாண்மை**: செயல்திறன் வாய்ந்த சூழல் பயன்பாடு

### 2. கட்டமைக்கப்பட்ட தரவுகளை ஒருங்கிணைத்தல்

- **CSV செயலாக்கம்**: Pandas மற்றும் AI மாடல்களுடன் ஒருங்கிணைப்பு
- **புள்ளியியல் பகுப்பாய்வு**: தானியங்கி தரவ சுருக்கம்
- **சூழல் உருவாக்கம்**: கேள்விகளின் அடிப்படையில் மாறும் சூழல் உருவாக்கம்
- **பல வடிவமைப்பு ஆதரவு**: JSON, CSV மற்றும் அட்டவணை தரவுகள்

### 3. RAG செயல்படுத்தல் முறைமைகள்

- **வெக்டர் தேடல்**: TF-IDF மற்றும் கோசைன் சிமிலாரிட்டி
- **ஆவண மீட்பு**: தொடர்புடைய மதிப்பீடு மற்றும் தரவரிசை
- **சூழல் இணைப்பு**: பல ஆவணங்களின் தொகுப்பு
- **பதில் உருவாக்கம்**: நிலைமைகளுடன் கூடிய பதில்கள்

### 4. Cloud மைக்ரேஷன் உத்திகள்

- **ஒற்றை APIகள்**: உள்ளூர் மற்றும் Cloud-க்கு ஒரே குறியீட்டு அடிப்படை
- **சூழல் சுருக்கம்**: கட்டமைப்பின் அடிப்படையில் வெளியீடு
- **வளர்ச்சி வேலைப்பாடு**: உள்ளூர் → இடைநிலை → தயாரிப்பு
- **செலவச் சுருக்கம்**: உள்ளூர் வளர்ச்சி, Cloud தயாரிப்பு

## தயாரிப்பு கருத்துக்கள்

### 1. செயல்திறன் மேம்பாடு

```python
# Optimize for production RAG
rag_config = {
    "max_context_docs": 5,
    "similarity_threshold": 0.15,
    "max_tokens": 1000,
    "temperature": 0.2,
    "chunk_size": 500,
    "chunk_overlap": 50
}
```

### 2. பிழை கையாளுதல்

```python
# Robust error handling
try:
    result = rag_system.generate_answer(question)
    if "error" in result:
        # Fallback to general knowledge
        fallback_result = client.chat.completions.create(
            model="phi-4-mini",
            messages=[{"role": "user", "content": question}]
        )
except Exception as e:
    # Log error and provide graceful degradation
    logger.error(f"RAG system error: {e}")
```

### 3. கண்காணிப்பு மற்றும் பார்வையிடுதல்

```python
# Track RAG performance
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```


## அடுத்த படிகள்

இந்த அமர்வை முடித்த பிறகு:

1. **அமர்வு 3-ஐ ஆராயுங்கள்**: Foundry Local-இல் திறந்த மூல மாடல்கள்
2. **தயாரிப்பு RAG உருவாக்குங்கள்**: Chainlit (Sample 04) மூலம் செயல்படுத்துங்கள்
3. **மேம்பட்ட வெக்டர் தேடல்**: Chroma அல்லது Pinecone உடன் ஒருங்கிணைத்தல்
4. **Cloud மைக்ரேஷன்**: Azure AI Foundry-க்கு வெளியிடுங்கள்
5. **RAG தரத்தை மதிப்பீடு செய்யுங்கள்**: `cd Workshop/samples;python -m session02.rag_eval_ragas` இயக்கி answer_relevancy, faithfulness, மற்றும் context_precision ஆகியவற்றை ragas மூலம் அளவிடுங்கள்

### விருப்ப மேம்பாடுகள்

| வகை | மேம்பாடு | காரணம் | திசை |
|----------|-------------|-----------|-----------|
| மீட்பு | TF-IDF-ஐ வெக்டர் ஸ்டோருடன் (FAISS / Chroma) மாற்றுங்கள் | semantic நினைவாற்றல் மற்றும் அளவளாவிய திறன் | ஆவணங்களை (500–800 எழுத்துகள்) துண்டாக்கி, எம்பெட் செய்து, குறியீட்டை நிரந்தரமாக சேமிக்கவும் |
| ஹைப்ரிட் குறியீடு | semantic + கீவேர்ட் வடிகட்டலை இணைத்தல் | எண் / குறியீட்டு கேள்விகளில் துல்லியத்தை மேம்படுத்துகிறது | கீவேர்ட் மூலம் வடிகட்டி, கோசைன் சிமிலாரிட்டி மூலம் தரவரிசை |
| எம்பெடிங்குகள் | பல எம்பெடிங் மாடல்களை மதிப்பீடு செய்யுங்கள் | தொடர்பு மற்றும் வேகத்தை மேம்படுத்துங்கள் | A/B: MiniLM vs E5-small vs உள்ளூர் ஹோஸ்டட் என்கோடர் |
| கேஷிங் | எம்பெடிங்குகள் மற்றும் மீட்பு முடிவுகளை கேஷ் செய்யுங்கள் | மீண்டும் மீண்டும் கேள்வி நேரத்தை குறைக்கிறது | எளிய டிஸ்க் பிக்கிள் / sqlite ஹாஷ் கீயுடன் |
| மதிப்பீடு | ragas தரவுத்தொகையை விரிவாக்குங்கள் | புள்ளியியல் அடிப்படையிலான தரம் | 50–100 Q/A + சூழல்களை உருவாக்கி, தலைப்பின் அடிப்படையில் பிரிக்கவும் |
| அளவீடுகள் | மீட்பு மற்றும் உருவாக்க நேரங்களை கண்காணிக்கவும் | செயல்திறன் சுயவிவரமிடல் | `retrieval_ms`, `gen_ms`, `tokens` ஆகியவற்றை ஒவ்வொரு அழைப்பிலும் பதிவு செய்யுங்கள் |
| பாதுகாப்பு | தவறான தகவல்களைத் தவிர்க்கும் fallback சேர்க்கவும் | பாதுகாப்பான பதில்கள் | faithfulness < threshold என்றால் → பதில்: "போதுமான சூழல் இல்லை." |
| fallback | உள்ளூர் → Azure மாடலை cascade செய்யுங்கள் | ஹைப்ரிட் தரத்தை மேம்படுத்துகிறது | குறைந்த நம்பகத்தன்மை உள்ளபோது OpenAI API வழியாக Cloud-க்கு வழிமாற்றுங்கள் |
| தீர்மானம் | நிலையான ஒப்பீட்டு ஓட்டங்கள் | மீண்டும் செய்யக்கூடிய மதிப்பீடு தொகுப்புகள் | seed-ஐ நிர்ணயிக்கவும், `temperature=0`, sampler randomness-ஐ முடக்கவும் |
| கண்காணிப்பு | மதிப்பீடு ஓட்ட வரலாற்றை நிரந்தரமாக சேமிக்கவும் | பின்வாங்கல் கண்டறிதல் | JSON வரிகளை timestamp + metric deltas உடன் சேர்க்கவும் |

#### உதாரணம்: மீட்பு நேரத்தைச் சேர்த்தல்

```python
import time
start_ret = time.time()
idxs = retrieve(query)
retrieval_ms = (time.time() - start_ret) * 1000
start_gen = time.time()
text, usage = chat_once(alias, messages=messages, max_tokens=250, temperature=0.2)
gen_ms = (time.time() - start_gen) * 1000
record = {"retrieval_ms": retrieval_ms, "gen_ms": gen_ms, "tokens": getattr(usage,'total_tokens',None)}
```


#### ragas மூலம் மதிப்பீட்டை அளவளாவியமாக்குதல்

1. `question`, `answer`, `contexts`, `ground_truths` (list) ஆகிய புலங்களுடன் JSONL ஒன்றை உருவாக்கவும்
2. `Dataset.from_list(list_of_dicts)`-க்கு மாற்றவும்
3. `evaluate(dataset, metrics=[...])` இயக்கவும்
4. தரவுகளை (CSV/JSON) சேமித்து போக்குவரத்தை பகுப்பாய்வு செய்யுங்கள்.

#### வெக்டர் ஸ்டோர் விரைவான தொடக்கம் (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) normalized
D, I = index.search(query_vec, k)
```

டிஸ்க் நிரந்தரத்திற்காக `faiss.write_index(index, "kb.index")` பயன்படுத்தவும்.

## கூடுதல் வளங்கள்

### ஆவணங்கள்
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG Patterns](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [Prompt Engineering Guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Ragas Evaluation Docs](https://docs.ragas.io)

### மாதிரிக் குறியீடு
- [Module08 Sample 04](./samples/04/README.md) - Chainlit RAG பயன்பாடு
- [Advanced Multi-Agent System](./samples/09/README.md) - ஏஜென்ட் ஒருங்கிணைப்பு முறைமைகள்

---

**அமர்வு காலம்**: 30 நிமிடங்கள் கையொப்பம் + 15 நிமிடங்கள் கேள்வி & பதில்
**சிரம நிலை**: இடைநிலை
**முன் தேவைகள்**: அமர்வு 1 முடிக்கப்பட்டது, Python அடிப்படை அறிவு

## மாதிரி சூழல் & பணிக்கூடம் வரைபடம்

| பணிக்கூடம் ஸ்கிரிப்ட் / நோட்புக் | சூழல் | இலக்கு | முக்கிய தரவுத்தொகை / மூல | உதாரண கேள்வி |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | உள்துறை ஆதரவு அறிவு அடிப்படையை தனியுரிமை + செயல்திறன் FAQs பதிலளிக்க | எளிய உள்ளூர் RAG எம்பெடிங்குகளுடன் | `DOCS` ஸ்கிரிப்டில் பட்டியல் (5 குறுகிய பத்திகள்) | ஏன் உள்ளூர் inference உடன் RAG பயன்படுத்த வேண்டும்? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | தரம் பகுப்பாய்வாளர் அடிப்படை மீட்பு நம்பகத்தன்மை அளவீட்டு அளவுகளை நிறுவ | சிறிய செயற்கை தரவுத்தொகையில் ragas அளவீடுகளை கணக்கிடுங்கள் | `DOCS`, `QUESTIONS`, `GROUND_TRUTH` வரிசைகள் | உள்ளூர் inference எந்த நன்மையை வழங்குகிறது? |
| `prompt_engineering.py` (மேம்பட்டது) | துறை SME பல துறைகளுக்கான நிலைமைகளை உருவாக்குதல் | துறை சிஸ்டம் ப்ராம்ப்ட்கள் மற்றும் டோக்கன் தாக்கத்தை ஒப்பிடுங்கள் | Inline `contexts` dict | Foundry Local மாடல் கேஷிங்கை எப்படி கையாளுகிறது? |
| `csv_qa_system.py` | விற்பனை செயல்பாடுகள் ஏற்றுமதிகளின் மீது இடையக பகுப்பாய்வை ஆராய்கின்றன | சிறிய விற்பனை துண்டை சுருக்கி கேள்வி | உருவாக்கப்பட்ட `sample_sales_data.csv` (10 வரிசைகள்) | எந்த தயாரிப்பு அதிக சராசரி விற்பனை தொகையை கொண்டுள்ளது? |
| `document_rag.py` | தயாரிப்பு குழு உள்துறை விக்கிக்கான ஆவண RAG-ஐ ஆராய்கிறது | தொடர்புடைய ஆவணங்களை மீட்டெடுத்து மேற்கோள் கொடுக்கவும் | `create_sample_knowledge_base()` பட்டியல் | Edge AI-யின் நன்மைகள் என்ன? |
| `migration_guide.py` | Cloud மைக்ரேஷன் திட்டத்தை தயாரிக்கும் ஆர்கிடெக்ட் | உள்ளூர் → Azure API சமநிலை காட்டுங்கள் | நிலையான சோதனை ப்ராம்ப்ட்கள் | Edge AI-யின் நன்மைகளை 2–3 வாக்கியங்களில் விளக்குங்கள். |

### Dataset Snippets
Inline RAG பைப்ப்லைன் ஆவண பட்டியல்:
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```

Ragas மதிப்பீட்டு உண்மை tuples:
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```


### சூழல் கதை
ஆதரவு பொறியியல் குழு வாடிக்கையாளர் தரவுகளை வெளிப்படுத்தாமல் உள்துறை FAQs-க்கு பதிலளிக்க விரைவான மாதிரியை விரும்புகிறது. அமர்வு 2 ஆவணங்கள் குறைந்த அளவிலான RAG (நிலையானது இல்லை) → கட்டமைக்கப்பட்ட CSV Q&A → மேற்கோளுடன் ஆவண மீட்பு → நோக்கமான தரம் மதிப்பீடு (ragas) → Azure இடைநிலைக்கு தயாராக மைக்ரேஷன் உத்தி வரை முன்னேறுகிறது.

### விரிவாக்க பாதைகள்
விருப்ப மேம்பாடுகள் அட்டவணையை பயன்படுத்தி மேம்படுத்துங்கள்: TF-IDF-ஐ FAISS/Chroma-க்கு மாற்றுங்கள், மதிப்பீட்டு தொகுப்பை (50–100 Q/A) பெரிதாக்குங்கள், faithfulness < threshold என்றால் பெரிய மாடலுக்கு fallback escalation சேர்க்கவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->