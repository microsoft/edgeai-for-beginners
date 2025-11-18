<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bb6014013b4adb7d7bfc60504eafed5d",
  "translation_date": "2025-11-17T18:45:57+00:00",
  "source_file": "Workshop/Session02-BuildAISolutionsRAG.md",
  "language_code": "mr"
}
-->
# सत्र 2: Azure AI Foundry सह AI सोल्यूशन्स तयार करा

## सारांश

Foundry Local आणि Azure AI Foundry वापरून उपयुक्त GenAI वर्कफ्लो कसे तयार करायचे ते शोधा. प्रगत प्रॉम्प्ट इंजिनिअरिंग, संरचित डेटा समाकलित करणे आणि पुनरुत्पादक पाइपलाइनसह कार्ये समन्वयित करणे शिकून घ्या. दस्तऐवज आणि डेटा Q&A साठी Retrieval-Augmented Generation (RAG) वर लक्ष केंद्रित करत असताना, नमुने व्यापक GenAI सोल्यूशन डिझाइनसाठी सामान्यीकृत आहेत.

## शिकण्याची उद्दिष्टे

या सत्राच्या शेवटी, तुम्ही:

- **प्रॉम्प्ट इंजिनिअरिंगमध्ये प्राविण्य मिळवा**: प्रभावी सिस्टम प्रॉम्प्ट्स आणि ग्राउंडिंग स्ट्रॅटेजी डिझाइन करा
- **RAG नमुने अंमलात आणा**: व्हेक्टर शोधासह दस्तऐवज-आधारित Q&A प्रणाली तयार करा
- **संरचित डेटा समाकलित करा**: AI वर्कफ्लोमध्ये CSV, JSON आणि टॅब्युलर डेटा वापरा
- **प्रॉडक्शन RAG तयार करा**: Chainlit सह स्केलेबल RAG अनुप्रयोग तयार करा
- **लोकल ते क्लाउड ब्रिज करा**: Foundry Local पासून Azure AI Foundry पर्यंत स्थलांतर मार्ग समजून घ्या

## पूर्वतयारी

- सत्र 1 पूर्ण केले (Foundry Local सेटअप)
- व्हेक्टर डेटाबेस आणि एम्बेडिंग्सची मूलभूत समज
- Python प्रोग्रामिंगचा अनुभव
- दस्तऐवज प्रक्रिया संकल्पनांची ओळख

### क्रॉस-प्लॅटफॉर्म वातावरण जलद प्रारंभ (Windows आणि macOS)

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

जर Foundry Local macOS बायनरीज तुमच्या वातावरणात उपलब्ध नसतील, तर Windows VM किंवा कंटेनरवर सेवा चालवा आणि सेट करा:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## पडताळणी: Foundry Local वातावरण तपासणी

डेमो सुरू करण्यापूर्वी, तुमचे स्थानिक वातावरण पडताळा:

```powershell
foundry --version              # Ensure CLI is installed
foundry status                 # Service status
foundry model run phi-4-mini   # Start baseline SLM
curl http://localhost:5273/v1/models  # Validate API (should list running model)
```

जर शेवटचा आदेश अयशस्वी झाला, तर सेवा सुरू (किंवा पुन्हा सुरू) करा: `foundry service start`.

## डेमो फ्लो (30 मिनिटे)

### 1. सिस्टम प्रॉम्प्ट्स आणि ग्राउंडिंग स्ट्रॅटेजी (10 मिनिटे)

#### पायरी 1.1: प्रगत प्रॉम्प्ट इंजिनिअरिंग

`samples/02-rag-solutions/prompt_engineering.py` तयार करा:

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


#### पायरी 1.2: ग्राउंडिंग स्ट्रॅटेजी तपासा

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the prompt engineering demo
python samples/02-rag-solutions/prompt_engineering.py
```


### 2. प्रॉम्प्ट्ससह टॅब्युलर डेटा समाकलित करा (CSV Q&A) (10 मिनिटे)

#### पायरी 2.1: CSV डेटा समाकलन

`samples/02-rag-solutions/csv_qa_system.py` तयार करा:

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


#### पायरी 2.2: CSV Q&A प्रणाली तपासा

```powershell
# Run the CSV Q&A demo
python samples/02-rag-solutions/csv_qa_system.py
```


### 3. स्टार्टर प्रोजेक्ट: 02-grounding-data अडॅप्ट करा (5 मिनिटे)

#### पायरी 3.1: सुधारित दस्तऐवज RAG प्रणाली

`samples/02-rag-solutions/document_rag.py` तयार करा:

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


### 4. CLI ते Azure स्थलांतर मार्ग दर्शवा (5 मिनिटे)

#### पायरी 4.1: स्थलांतर धोरणाचा आढावा

`samples/02-rag-solutions/migration_guide.py` तयार करा:

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


#### पायरी 4.2: स्थलांतर नमुने तपासा

```powershell
# Run the migration demo
python samples/02-rag-solutions/migration_guide.py
```


## कव्हर केलेली मुख्य संकल्पना

### 1. प्रगत प्रॉम्प्ट इंजिनिअरिंग

- **सिस्टम प्रॉम्प्ट्स**: डोमेन-विशिष्ट तज्ञ व्यक्तिमत्वे
- **ग्राउंडिंग स्ट्रॅटेजी**: संदर्भ समाकलन तंत्र
- **तापमान नियंत्रण**: सर्जनशीलता विरुद्ध सुसंगततेचे संतुलन
- **टोकन व्यवस्थापन**: कार्यक्षम संदर्भ वापर

### 2. संरचित डेटा समाकलन

- **CSV प्रक्रिया**: Pandas सह AI मॉडेल्स समाकलित करा
- **सांख्यिकीय विश्लेषण**: स्वयंचलित डेटा संक्षेपण
- **संदर्भ निर्मिती**: क्वेरींवर आधारित डायनॅमिक संदर्भ निर्मिती
- **मल्टी-फॉर्मॅट सपोर्ट**: JSON, CSV आणि टॅब्युलर डेटा

### 3. RAG अंमलबजावणी नमुने

- **व्हेक्टर शोध**: TF-IDF आणि कोसाइन साम्य
- **दस्तऐवज पुनर्प्राप्ती**: प्रासंगिकता स्कोअरिंग आणि रँकिंग
- **संदर्भ संयोजन**: मल्टी-दस्तऐवज संश्लेषण
- **उत्तर निर्मिती**: ग्राउंडेड प्रतिसाद निर्मिती

### 4. क्लाउड स्थलांतर धोरणे

- **एकत्रित API**: स्थानिक आणि क्लाउडसाठी एकच कोडबेस
- **वातावरण अब्स्ट्रॅक्शन**: कॉन्फिगरेशन-चालित तैनाती
- **विकसन कार्यप्रवाह**: स्थानिक → स्टेजिंग → उत्पादन
- **खर्च अनुकूलन**: स्थानिक विकास, क्लाउड उत्पादन

## उत्पादन विचार

### 1. कार्यक्षमता अनुकूलन

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


### 2. त्रुटी हाताळणी

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


### 3. निरीक्षण आणि निरीक्षणक्षमता

```python
# Track RAG performance
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```


## पुढील पायऱ्या

हे सत्र पूर्ण केल्यानंतर:

1. **सत्र 3 एक्सप्लोर करा**: Foundry Local मधील ओपन-सोर्स मॉडेल्स
2. **प्रॉडक्शन RAG तयार करा**: Chainlit सह अंमलात आणा (नमुना 04)
3. **प्रगत व्हेक्टर शोध**: Chroma किंवा Pinecone सह समाकलित करा
4. **क्लाउड स्थलांतर**: Azure AI Foundry वर तैनात करा
5. **RAG गुणवत्ता मूल्यांकन करा**: `cd Workshop/samples;python -m session02.rag_eval_ragas` चालवा आणि ragas वापरून answer_relevancy, faithfulness, आणि context_precision मोजा

### पर्यायी सुधारणा

| श्रेणी | सुधारणा | कारण | दिशा |
|----------|-------------|-----------|-----------|
| पुनर्प्राप्ती | TF-IDF च्या जागी व्हेक्टर स्टोअर (FAISS / Chroma) वापरा | चांगले सिमॅंटिक रिकॉल आणि स्केलेबिलिटी | डॉक्युमेंट्स चंक्स करा (500–800 अक्षरे), एम्बेड करा, इंडेक्स कायम ठेवा |
| हायब्रिड इंडेक्स | द्वंद्वात्मक सिमॅंटिक + कीवर्ड फिल्टरिंग | संख्यात्मक / कोड क्वेरींवर अचूकता सुधारते | कीवर्डद्वारे फिल्टर करा आणि नंतर कोसाइन साम्याने रँक करा |
| एम्बेडिंग्स | एकाधिक एम्बेडिंग मॉडेल्सचे मूल्यांकन करा | प्रासंगिकता विरुद्ध गती अनुकूलित करा | A/B: MiniLM vs E5-small vs स्थानिक होस्ट केलेला एन्कोडर |
| कॅशिंग | एम्बेडिंग्स आणि पुनर्प्राप्ती परिणाम कॅश करा | पुनरावृत्त क्वेरी विलंब कमी करा | साधे ऑन-डिस्क पिकल / sqlite हॅश कीसह |
| मूल्यांकन | ragas डेटासेट विस्तृत करा | सांख्यिकदृष्ट्या अर्थपूर्ण गुणवत्ता | 50–100 Q/A + संदर्भ क्युरेट करा; विषयानुसार स्तरित करा |
| मेट्रिक्स | पुनर्प्राप्ती आणि निर्मिती वेळा ट्रॅक करा | कार्यक्षमता प्रोफाइलिंग | प्रत्येक कॉलसाठी `retrieval_ms`, `gen_ms`, `tokens` कॅप्चर करा |
| गार्डरेल्स | भ्रमFallback जोडा | सुरक्षित उत्तरे | faithfulness < threshold असल्यास → उत्तर: "अपुरा संदर्भ." |
| फॉलबॅक | स्थानिक → Azure मॉडेल कॅस्केड करा | हायब्रिड गुणवत्ता सुधारणा | कमी विश्वासावर OpenAI API द्वारे क्लाउडकडे मार्ग |
| निर्धारकता | स्थिर तुलना चालवा | पुनरावृत्त मूल्यांकन संच | बीज निश्चित करा, `temperature=0`, सॅम्पलर यादृच्छिकता अक्षम करा |
| निरीक्षण | मूल्यांकन रन इतिहास कायम ठेवा | पुनरावृत्ती शोध | JSON ओळींसह टाइमस्टॅम्प + मेट्रिक डेल्टा जोडणे |

#### उदाहरण: पुनर्प्राप्ती वेळ जोडणे

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


#### ragas सह मूल्यांकन स्केलिंग

1. फील्डसह JSONL एकत्र करा: `question`, `answer`, `contexts`, `ground_truths` (यादी)
2. `Dataset.from_list(list_of_dicts)` मध्ये रूपांतरित करा
3. `evaluate(dataset, metrics=[...])` चालवा
4. ट्रेंड विश्लेषणासाठी मेट्रिक्स (CSV/JSON) संग्रहित करा.

#### व्हेक्टर स्टोअर जलद प्रारंभ (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) normalized
D, I = index.search(query_vec, k)
```

डिस्क टिकावासाठी `faiss.write_index(index, "kb.index")` वापरा.

## अतिरिक्त संसाधने

### दस्तऐवज
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG Patterns](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [Prompt Engineering Guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Ragas Evaluation Docs](https://docs.ragas.io)

### नमुना कोड
- [Module08 Sample 04](./samples/04/README.md) - Chainlit RAG Application
- [Advanced Multi-Agent System](./samples/09/README.md) - Agent coordination patterns

---

**सत्र कालावधी**: 30 मिनिटे हाताळणी + 15 मिनिटे Q&A  
**अडचणीची पातळी**: मध्यम  
**पूर्वतयारी**: सत्र 1 पूर्ण केले, Python ची मूलभूत माहिती

## नमुना परिस्थिती आणि कार्यशाळा मॅपिंग

| कार्यशाळा स्क्रिप्ट / नोटबुक | परिस्थिती | उद्दिष्ट | मुख्य डेटासेट / स्रोत | उदाहरण प्रश्न |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | अंतर्गत समर्थन ज्ञान तळ गोपनीयता + कार्यक्षमता FAQs उत्तर देणे | एम्बेडिंग्ससह मिनिमल इन-मेमरी RAG | स्क्रिप्टमधील `DOCS` यादी (5 लहान उतारे) | स्थानिक अनुमानासह RAG का वापरावे? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | गुणवत्ता विश्लेषक बेसलाइन पुनर्प्राप्ती विश्वासार्हता मेट्रिक्स स्थापित करणे | लहान सिंथेटिक डेटासेटवर ragas मेट्रिक्स गणना करा | `DOCS`, `QUESTIONS`, `GROUND_TRUTH` अ‍ॅरे | स्थानिक अनुमानाचा फायदा काय आहे? |
| `prompt_engineering.py` (प्रगत) | डोमेन SME अनेक क्षेत्रांसाठी ग्राउंडेड प्रॉम्प्ट्स तयार करणे | डोमेन सिस्टम प्रॉम्प्ट्स आणि टोकन प्रभावाची तुलना करा | इनलाइन `contexts` dict | Foundry Local मॉडेल कॅशिंग कसे हाताळते? |
| `csv_qa_system.py` | विक्री ऑप्स निर्यातांवर परस्पर विश्लेषण शोधत आहेत | लहान विक्री स्लाइस संक्षेपित करा आणि क्वेरी करा | व्युत्पन्न `sample_sales_data.csv` (10 ओळी) | कोणत्या उत्पादनाचा सरासरी विक्री रक्कम सर्वाधिक आहे? |
| `document_rag.py` | उत्पादन संघ अंतर्गत विकीसाठी दस्तऐवज RAG एक्सप्लोर करत आहे | संबंधित दस्तऐवज पुनर्प्राप्त करा + उद्धृत करा | `create_sample_knowledge_base()` यादी | Edge AI चे फायदे काय आहेत? |
| `migration_guide.py` | आर्किटेक्ट क्लाउड स्थलांतर योजना तयार करत आहे | स्थानिक→Azure API समता प्रदर्शित करा | स्थिर चाचणी प्रॉम्प्ट्स | Edge AI चे फायदे 2–3 वाक्यांत स्पष्ट करा. |

### डेटासेट स्निपेट्स
इनलाइन RAG पाइपलाइन डॉक यादी:
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```


Ragas मूल्यांकन सत्य जोड्या:
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```


### परिस्थिती कथन
सपोर्ट इंजिनिअरिंग ग्रुपला ग्राहक डेटा बाहेर उघड न करता अंतर्गत FAQs उत्तर देण्यासाठी जलद प्रोटोटाइप हवे आहे. सत्र 2 आर्टिफॅक्ट्स मिनिमल इफेमरल RAG (कोणतेही टिकाव नाही) → संरचित CSV Q&A → दस्तऐवज पुनर्प्राप्ती उद्धरणासह → उद्देशपूर्ण गुणवत्ता मूल्यांकन (ragas) → Azure स्टेजिंगसाठी तयार स्थलांतर धोरणापर्यंत प्रगती करतात.

### विस्तार मार्ग
पर्यायी सुधारणा टेबल वापरून विकसित करा: TF‑IDF च्या जागी FAISS/Chroma वापरा, मूल्यांकन कॉर्पस (50–100 Q/A) मोठा करा, faithfulness < threshold असताना मोठ्या मॉडेलकडे फॉलबॅक एस्कलेशन जोडा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपयास लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->