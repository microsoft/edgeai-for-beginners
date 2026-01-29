# সেশন ২: Azure AI Foundry দিয়ে AI সমাধান তৈরি করুন

## সারসংক্ষেপ

Foundry Local এবং Azure AI Foundry ব্যবহার করে কার্যকরী GenAI ওয়ার্কফ্লো তৈরি করার উপায় শিখুন। উন্নত প্রম্পট ইঞ্জিনিয়ারিং, কাঠামোবদ্ধ ডেটা সংযুক্তিকরণ এবং পুনরায় ব্যবহারযোগ্য পাইপলাইনের মাধ্যমে কাজ পরিচালনা করার কৌশল শিখুন। যদিও ফোকাস Retrieval-Augmented Generation (RAG) এর উপর, যা ডকুমেন্ট এবং ডেটা Q&A এর জন্য ব্যবহৃত হয়, এই প্যাটার্নগুলো বৃহত্তর GenAI সমাধান ডিজাইনের জন্যও প্রযোজ্য।

## শেখার লক্ষ্যসমূহ

এই সেশন শেষে আপনি:

- **প্রম্পট ইঞ্জিনিয়ারিংয়ে দক্ষতা অর্জন করবেন**: কার্যকরী সিস্টেম প্রম্পট এবং গ্রাউন্ডিং কৌশল ডিজাইন করবেন
- **RAG প্যাটার্ন প্রয়োগ করবেন**: ভেক্টর সার্চ ব্যবহার করে ডকুমেন্ট-ভিত্তিক Q&A সিস্টেম তৈরি করবেন
- **কাঠামোবদ্ধ ডেটা সংযুক্ত করবেন**: AI ওয়ার্কফ্লোতে CSV, JSON এবং ট্যাবুলার ডেটা ব্যবহার করবেন
- **প্রোডাকশন RAG তৈরি করবেন**: Chainlit দিয়ে স্কেলযোগ্য RAG অ্যাপ্লিকেশন তৈরি করবেন
- **লোকাল থেকে ক্লাউডে সংযোগ স্থাপন করবেন**: Foundry Local থেকে Azure AI Foundry-এ মাইগ্রেশনের পথ বুঝবেন

## পূর্বশর্ত

- সেশন ১ সম্পন্ন করেছেন (Foundry Local সেটআপ)
- ভেক্টর ডেটাবেস এবং এমবেডিং সম্পর্কে প্রাথমিক ধারণা
- পাইথন প্রোগ্রামিংয়ে অভিজ্ঞতা
- ডকুমেন্ট প্রসেসিং ধারণার সাথে পরিচিত

### ক্রস-প্ল্যাটফর্ম পরিবেশ দ্রুত শুরু (Windows & macOS)

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

যদি Foundry Local macOS বাইনারি আপনার পরিবেশে উপলব্ধ না থাকে, তাহলে Windows VM বা কন্টেইনারে সার্ভিস চালান এবং সেট করুন:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## যাচাই: Foundry Local পরিবেশ পরীক্ষা

ডেমো শুরু করার আগে আপনার লোকাল পরিবেশ যাচাই করুন:

```powershell
foundry --version              # Ensure CLI is installed
foundry status                 # Service status
foundry model run phi-4-mini   # Start baseline SLM
curl http://localhost:5273/v1/models  # Validate API (should list running model)
```

যদি শেষ কমান্ডটি ব্যর্থ হয়, তাহলে সার্ভিস শুরু (বা পুনরায় শুরু) করুন: `foundry service start`।

## ডেমো প্রবাহ (৩০ মিনিট)

### ১. সিস্টেম প্রম্পট এবং গ্রাউন্ডিং কৌশল (১০ মিনিট)

#### ধাপ ১.১: উন্নত প্রম্পট ইঞ্জিনিয়ারিং

`samples/02-rag-solutions/prompt_engineering.py` তৈরি করুন:

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

#### ধাপ ১.২: গ্রাউন্ডিং কৌশল পরীক্ষা করুন

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the prompt engineering demo
python samples/02-rag-solutions/prompt_engineering.py
```


### ২. ট্যাবুলার ডেটা প্রম্পটের সাথে সংযুক্ত করুন (CSV Q&A) (১০ মিনিট)

#### ধাপ ২.১: CSV ডেটা সংযুক্তিকরণ

`samples/02-rag-solutions/csv_qa_system.py` তৈরি করুন:

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

#### ধাপ ২.২: CSV Q&A সিস্টেম পরীক্ষা করুন

```powershell
# Run the CSV Q&A demo
python samples/02-rag-solutions/csv_qa_system.py
```


### ৩. স্টার্টার প্রজেক্ট: ০২-grounding-data অভিযোজন (৫ মিনিট)

#### ধাপ ৩.১: উন্নত ডকুমেন্ট RAG সিস্টেম

`samples/02-rag-solutions/document_rag.py` তৈরি করুন:

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


### ৪. CLI থেকে Azure মাইগ্রেশন পথ দেখান (৫ মিনিট)

#### ধাপ ৪.১: মাইগ্রেশন কৌশলের সংক্ষিপ্ত বিবরণ

`samples/02-rag-solutions/migration_guide.py` তৈরি করুন:

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

#### ধাপ ৪.২: মাইগ্রেশন প্যাটার্ন পরীক্ষা করুন

```powershell
# Run the migration demo
python samples/02-rag-solutions/migration_guide.py
```


## আলোচিত মূল ধারণা

### ১. উন্নত প্রম্পট ইঞ্জিনিয়ারিং

- **সিস্টেম প্রম্পট**: ডোমেইন-নির্দিষ্ট বিশেষজ্ঞ ব্যক্তিত্ব
- **গ্রাউন্ডিং কৌশল**: প্রসঙ্গ সংযুক্তিকরণ কৌশল
- **তাপমাত্রা নিয়ন্ত্রণ**: সৃজনশীলতা বনাম সামঞ্জস্যের ভারসাম্য
- **টোকেন ব্যবস্থাপনা**: কার্যকর প্রসঙ্গ ব্যবহার

### ২. কাঠামোবদ্ধ ডেটা সংযুক্তিকরণ

- **CSV প্রসেসিং**: Pandas দিয়ে AI মডেলের সাথে ইন্টিগ্রেশন
- **পরিসংখ্যান বিশ্লেষণ**: স্বয়ংক্রিয় ডেটা সারসংক্ষেপ
- **প্রসঙ্গ তৈরি**: প্রশ্নের উপর ভিত্তি করে গতিশীল প্রসঙ্গ তৈরি
- **মাল্টি-ফরম্যাট সাপোর্ট**: JSON, CSV এবং ট্যাবুলার ডেটা

### ৩. RAG প্রয়োগ প্যাটার্ন

- **ভেক্টর সার্চ**: TF-IDF এবং কসাইন সিমিলারিটি
- **ডকুমেন্ট রিট্রিভাল**: প্রাসঙ্গিকতা স্কোরিং এবং র‍্যাংকিং
- **প্রসঙ্গ সংমিশ্রণ**: মাল্টি-ডকুমেন্ট সংশ্লেষণ
- **উত্তর তৈরি**: গ্রাউন্ডেড রেসপন্স তৈরি

### ৪. ক্লাউড মাইগ্রেশন কৌশল

- **একীভূত API**: লোকাল এবং ক্লাউডের জন্য একক কোডবেস
- **পরিবেশ বিমূর্তকরণ**: কনফিগারেশন-চালিত ডিপ্লয়মেন্ট
- **উন্নয়ন কর্মপ্রবাহ**: লোকাল → স্টেজিং → প্রোডাকশন
- **খরচ অপ্টিমাইজেশন**: লোকাল উন্নয়ন, ক্লাউড প্রোডাকশন

## প্রোডাকশন বিবেচনা

### ১. পারফরম্যান্স অপ্টিমাইজেশন

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

### ২. ত্রুটি পরিচালনা

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

### ৩. পর্যবেক্ষণ এবং দৃশ্যমানতা

```python
# Track RAG performance
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```


## পরবর্তী পদক্ষেপ

এই সেশন সম্পন্ন করার পর:

1. **সেশন ৩ অন্বেষণ করুন**: Foundry Local-এ ওপেন-সোর্স মডেল
2. **প্রোডাকশন RAG তৈরি করুন**: Chainlit দিয়ে বাস্তবায়ন করুন (Sample 04)
3. **উন্নত ভেক্টর সার্চ**: Chroma বা Pinecone এর সাথে সংযুক্ত করুন
4. **ক্লাউড মাইগ্রেশন**: Azure AI Foundry-এ ডিপ্লয় করুন
5. **RAG গুণমান মূল্যায়ন করুন**: `cd Workshop/samples;python -m session02.rag_eval_ragas` চালিয়ে answer_relevancy, faithfulness, এবং context_precision ragas দিয়ে পরিমাপ করুন

### ঐচ্ছিক উন্নয়ন

| বিভাগ | উন্নয়ন | কারণ | নির্দেশনা |
|-------|--------|-------|-----------|
| রিট্রিভাল | TF-IDF এর পরিবর্তে ভেক্টর স্টোর (FAISS / Chroma) ব্যবহার করুন | ভালো সেমান্টিক রিকল এবং স্কেল | ডকুমেন্ট চাঙ্ক করুন (৫০০–৮০০ অক্ষর), এমবেড করুন, ইনডেক্স সংরক্ষণ করুন |
| হাইব্রিড ইনডেক্স | দ্বৈত সেমান্টিক + কীওয়ার্ড ফিল্টারিং | সংখ্যাগত / কোড প্রশ্নে নির্ভুলতা উন্নত করে | কীওয়ার্ড দিয়ে ফিল্টার করুন, তারপর কসাইন সিমিলারিটি দিয়ে র‍্যাংক করুন |
| এমবেডিং | একাধিক এমবেডিং মডেল মূল্যায়ন করুন | প্রাসঙ্গিকতা বনাম গতি অপ্টিমাইজ করুন | A/B: MiniLM বনাম E5-small বনাম লোকাল হোস্টেড এনকোডার |
| ক্যাশিং | এমবেডিং এবং রিট্রিভাল ফলাফল ক্যাশ করুন | পুনরাবৃত্ত প্রশ্নের লেটেন্সি কমান | সহজ অন-ডিস্ক পিকল / sqlite হ্যাশ কী দিয়ে |
| মূল্যায়ন | ragas ডেটাসেট প্রসারিত করুন | পরিসংখ্যানগতভাবে অর্থপূর্ণ গুণমান | ৫০–১০০ Q/A + প্রসঙ্গ কিউরেট করুন; টপিক অনুযায়ী স্ট্রাটিফাই করুন |
| মেট্রিক | রিট্রিভাল এবং জেনারেশন টাইমিং ট্র্যাক করুন | পারফরম্যান্স প্রোফাইলিং | প্রতি কল `retrieval_ms`, `gen_ms`, `tokens` ক্যাপচার করুন |
| গার্ডরেল | হ্যালুসিনেশন ফালব্যাক যোগ করুন | নিরাপদ উত্তর | যদি faithfulness < থ্রেশহোল্ড → উত্তর: "পর্যাপ্ত প্রসঙ্গ নেই।" |
| ফালব্যাক | লোকাল → Azure মডেল ক্যাসকেড করুন | হাইব্রিড গুণমান উন্নতি | কম আত্মবিশ্বাসে একই OpenAI API দিয়ে ক্লাউডে রুট করুন |
| নির্ধারকতা | স্থিতিশীল তুলনা রান | পুনরাবৃত্তি মূল্যায়ন সেট | সিড ঠিক করুন, `temperature=0`, স্যাম্পলার র‍্যান্ডমনেস নিষ্ক্রিয় করুন |
| পর্যবেক্ষণ | মূল্যায়ন রান ইতিহাস সংরক্ষণ করুন | রিগ্রেশন সনাক্তকরণ | JSON লাইন যোগ করুন টাইমস্ট্যাম্প + মেট্রিক ডেল্টাস সহ |

#### উদাহরণ: রিট্রিভাল টাইমিং যোগ করা

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


#### ragas দিয়ে মূল্যায়ন স্কেলিং

1. JSONL তৈরি করুন যেখানে ফিল্ড থাকবে: `question`, `answer`, `contexts`, `ground_truths` (লিস্ট)
2. `Dataset.from_list(list_of_dicts)` এ রূপান্তর করুন
3. `evaluate(dataset, metrics=[...])` চালান
4. মেট্রিক সংরক্ষণ করুন (CSV/JSON) ট্রেন্ড বিশ্লেষণের জন্য।

#### ভেক্টর স্টোর দ্রুত শুরু (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) normalized
D, I = index.search(query_vec, k)
```

ডিস্কে সংরক্ষণের জন্য ব্যবহার করুন `faiss.write_index(index, "kb.index")`।

## অতিরিক্ত সম্পদ

### ডকুমেন্টেশন
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG Patterns](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [Prompt Engineering Guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Ragas Evaluation Docs](https://docs.ragas.io)

### নমুনা কোড
- [Module08 Sample 04](./samples/04/README.md) - Chainlit RAG অ্যাপ্লিকেশন
- [Advanced Multi-Agent System](./samples/09/README.md) - এজেন্ট সমন্বয় প্যাটার্ন

---

**সেশন সময়কাল**: ৩০ মিনিট হাতে-কলম + ১৫ মিনিট Q&A  
**কঠিনতার স্তর**: মধ্যম  
**পূর্বশর্ত**: সেশন ১ সম্পন্ন, পাইথনের প্রাথমিক জ্ঞান

## নমুনা পরিস্থিতি এবং ওয়ার্কশপ ম্যাপিং

| ওয়ার্কশপ স্ক্রিপ্ট / নোটবুক | পরিস্থিতি | লক্ষ্য | মূল ডেটাসেট / উৎস | উদাহরণ প্রশ্ন |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | অভ্যন্তরীণ সাপোর্ট নলেজ বেস যা গোপনীয়তা + পারফরম্যান্স FAQ উত্তর দেয় | এমবেডিং সহ মিনিমাল ইন-মেমরি RAG | স্ক্রিপ্টে `DOCS` তালিকা (৫টি সংক্ষিপ্ত প্যাসেজ) | কেন লোকাল ইনফারেন্সের সাথে RAG ব্যবহার করবেন? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | গুণমান বিশ্লেষক বেসলাইন রিট্রিভাল ফেইথফুলনেস মেট্রিক স্থাপন করছেন | ছোট সিনথেটিক ডেটাসেটে ragas মেট্রিক গণনা করুন | `DOCS`, `QUESTIONS`, `GROUND_TRUTH` অ্যারে | লোকাল ইনফারেন্স কী সুবিধা দেয়? |
| `prompt_engineering.py` (উন্নত) | ডোমেইন SME বিভিন্ন ভার্টিকালের জন্য গ্রাউন্ডেড প্রম্পট তৈরি করছেন | ডোমেইন সিস্টেম প্রম্পট এবং টোকেন প্রভাব তুলনা করুন | ইনলাইন `contexts` dict | Foundry Local কীভাবে মডেল ক্যাশিং পরিচালনা করে? |
| `csv_qa_system.py` | সেলস অপস ইন্টারেক্টিভ অ্যানালিটিক্স অন্বেষণ করছেন | ছোট সেলস স্লাইস সারসংক্ষেপ এবং প্রশ্ন করুন | তৈরি করা `sample_sales_data.csv` (১০টি সারি) | কোন পণ্যটির গড় বিক্রয় পরিমাণ সবচেয়ে বেশি? |
| `document_rag.py` | প্রোডাক্ট টিম অভ্যন্তরীণ উইকির জন্য ডক RAG অন্বেষণ করছেন | প্রাসঙ্গিক ডক রিট্রিভ করুন এবং উল্লেখ করুন | `create_sample_knowledge_base()` তালিকা | Edge AI এর সুবিধাগুলো কী? |
| `migration_guide.py` | আর্কিটেক্ট ক্লাউড মাইগ্রেশন পরিকল্পনা প্রস্তুত করছেন | লোকাল→Azure API সমতা প্রদর্শন করুন | স্ট্যাটিক টেস্ট প্রম্পট | Edge AI এর সুবিধাগুলো ২–৩ বাক্যে ব্যাখ্যা করুন। |

### ডেটাসেট স্নিপেট
ইনলাইন RAG পাইপলাইন ডক তালিকা:
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```

Ragas মূল্যায়ন সত্য টুপল:
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```


### পরিস্থিতি বিবরণ
সাপোর্ট ইঞ্জিনিয়ারিং গ্রুপ একটি দ্রুত প্রোটোটাইপ চায় যা অভ্যন্তরীণ FAQ উত্তর দিতে পারে, কিন্তু গ্রাহকের ডেটা বাহ্যিকভাবে প্রকাশ না করে। সেশন ২ এর আর্টিফ্যাক্টগুলো একটি মিনিমাল ইফেমেরাল RAG (কোনো স্থায়িত্ব নেই) → কাঠামোবদ্ধ CSV Q&A → ডকুমেন্ট রিট্রিভাল উল্লেখ সহ → উদ্দেশ্যমূলক গুণমান মূল্যায়ন (ragas) → Azure স্টেজিংয়ের জন্য প্রস্তুত একটি মাইগ্রেশন কৌশল।

### সম্প্রসারণ পথ
ঐচ্ছিক উন্নয়ন টেবিল ব্যবহার করে উন্নতি করুন: TF‑IDF এর পরিবর্তে FAISS/Chroma ব্যবহার করুন, মূল্যায়ন কর্পাস (৫০–১০০ Q/A) বড় করুন, faithfulness < থ্রেশহোল্ড হলে বড় মডেলে ফালব্যাক এসকেলেশন যোগ করুন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->