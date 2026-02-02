# सत्र २: Azure AI Foundry संग AI समाधान निर्माण गर्नुहोस्

## सारांश

Foundry Local र Azure AI Foundry प्रयोग गरेर GenAI कार्यप्रवाह निर्माण गर्ने तरिका अन्वेषण गर्नुहोस्। उन्नत प्रम्प्ट इन्जिनियरिङ सिक्नुहोस्, संरचित डाटा समाहित गर्नुहोस्, र पुन: उत्पादनयोग्य पाइपलाइनहरूसँग कार्यहरू समन्वय गर्नुहोस्। यद्यपि ध्यान दस्तावेज र डाटा Q&A को लागि Retrieval-Augmented Generation (RAG) मा केन्द्रित छ, यी ढाँचाहरू व्यापक GenAI समाधान डिजाइनमा सामान्यीकृत गर्न सकिन्छ।

## सिक्ने उद्देश्यहरू

यस सत्रको अन्त्यसम्ममा, तपाईं:

- **प्रम्प्ट इन्जिनियरिङमा निपुण हुनुहोस्**: प्रभावकारी प्रणाली प्रम्प्टहरू र ग्राउन्डिङ रणनीतिहरू डिजाइन गर्नुहोस्
- **RAG ढाँचाहरू कार्यान्वयन गर्नुहोस्**: भेक्टर खोजको साथ दस्तावेज-आधारित Q&A प्रणाली निर्माण गर्नुहोस्
- **संरचित डाटा समाहित गर्नुहोस्**: AI कार्यप्रवाहमा CSV, JSON, र ट्याबुलर डाटासँग काम गर्नुहोस्
- **उत्पादन RAG निर्माण गर्नुहोस्**: Chainlit प्रयोग गरेर स्केलेबल RAG अनुप्रयोगहरू सिर्जना गर्नुहोस्
- **स्थानीयदेखि क्लाउडसम्मको पुल बनाउनुहोस्**: Foundry Local बाट Azure AI Foundry मा माइग्रेशन मार्गहरू बुझ्नुहोस्

## पूर्वापेक्षाहरू

- सत्र १ (Foundry Local सेटअप) पूरा भएको
- भेक्टर डाटाबेस र एम्बेडिङको आधारभूत समझ
- Python प्रोग्रामिङ अनुभव
- दस्तावेज प्रशोधन अवधारणासँग परिचितता

### क्रस-प्ल्याटफर्म वातावरण छिटो सुरु (Windows र macOS)

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

यदि Foundry Local macOS बाइनरीहरू तपाईंको वातावरणमा उपलब्ध छैनन् भने, सेवा Windows VM वा कन्टेनरमा चलाउनुहोस् र सेट गर्नुहोस्:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## मान्यता: Foundry Local वातावरण जाँच

डेमोहरू सुरु गर्नु अघि, तपाईंको स्थानीय वातावरण मान्यता दिनुहोस्:

```powershell
foundry --version              # Ensure CLI is installed
foundry status                 # Service status
foundry model run phi-4-mini   # Start baseline SLM
curl http://localhost:5273/v1/models  # Validate API (should list running model)
```

यदि अन्तिम आदेश असफल हुन्छ भने, सेवा सुरु (वा पुन: सुरु) गर्नुहोस्: `foundry service start`।

## डेमो प्रवाह (३० मिनेट)

### १. प्रणाली प्रम्प्टहरू र ग्राउन्डिङ रणनीतिहरू (१० मिनेट)

#### चरण १.१: उन्नत प्रम्प्ट इन्जिनियरिङ

`samples/02-rag-solutions/prompt_engineering.py` सिर्जना गर्नुहोस्:

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

#### चरण १.२: ग्राउन्डिङ रणनीतिहरू परीक्षण गर्नुहोस्

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the prompt engineering demo
python samples/02-rag-solutions/prompt_engineering.py
```


### २. ट्याबुलर डाटालाई प्रम्प्टहरूसँग समाहित गर्नुहोस् (CSV Q&A) (१० मिनेट)

#### चरण २.१: CSV डाटा समाहित

`samples/02-rag-solutions/csv_qa_system.py` सिर्जना गर्नुहोस्:

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

#### चरण २.२: CSV Q&A प्रणाली परीक्षण गर्नुहोस्

```powershell
# Run the CSV Q&A demo
python samples/02-rag-solutions/csv_qa_system.py
```


### ३. स्टार्टर प्रोजेक्ट: ०२-ग्राउन्डिङ-डाटा अनुकूलन गर्नुहोस् (५ मिनेट)

#### चरण ३.१: उन्नत दस्तावेज RAG प्रणाली

`samples/02-rag-solutions/document_rag.py` सिर्जना गर्नुहोस्:

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


### ४. CLI देखि Azure माइग्रेशन मार्ग देखाउनुहोस् (५ मिनेट)

#### चरण ४.१: माइग्रेशन रणनीति अवलोकन

`samples/02-rag-solutions/migration_guide.py` सिर्जना गर्नुहोस्:

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

#### चरण ४.२: माइग्रेशन ढाँचाहरू परीक्षण गर्नुहोस्

```powershell
# Run the migration demo
python samples/02-rag-solutions/migration_guide.py
```


## समेटिएका प्रमुख अवधारणाहरू

### १. उन्नत प्रम्प्ट इन्जिनियरिङ

- **प्रणाली प्रम्प्टहरू**: डोमेन-विशिष्ट विशेषज्ञ व्यक्तित्वहरू
- **ग्राउन्डिङ रणनीतिहरू**: सन्दर्भ समाहित गर्ने प्रविधिहरू
- **तापमान नियन्त्रण**: रचनात्मकता बनाम स्थिरता सन्तुलन
- **टोकन व्यवस्थापन**: सन्दर्भको कुशल प्रयोग

### २. संरचित डाटा समाहित

- **CSV प्रशोधन**: Pandas को AI मोडेलहरूसँग समाहित
- **सांख्यिकीय विश्लेषण**: स्वचालित डाटा सारांश
- **सन्दर्भ सिर्जना**: प्रश्नहरूको आधारमा गतिशील सन्दर्भ सिर्जना
- **बहु-ढाँचाको समर्थन**: JSON, CSV, र ट्याबुलर डाटा

### ३. RAG कार्यान्वयन ढाँचाहरू

- **भेक्टर खोज**: TF-IDF र कोसाइन समानता
- **दस्तावेज पुनःप्राप्ति**: प्रासंगिकता स्कोरिङ र रैंकिङ
- **सन्दर्भ संयोजन**: बहु-दस्तावेज संश्लेषण
- **उत्तर सिर्जना**: ग्राउन्डेड प्रतिक्रिया सिर्जना

### ४. क्लाउड माइग्रेशन रणनीतिहरू

- **एकीकृत APIs**: स्थानीय र क्लाउडको लागि एकल कोडबेस
- **वातावरण अमूर्तता**: कन्फिगरेसन-चालित परिनियोजन
- **विकास कार्यप्रवाह**: स्थानीय → स्टेजिङ → उत्पादन
- **लागत अनुकूलन**: स्थानीय विकास, क्लाउड उत्पादन

## उत्पादन विचारहरू

### १. प्रदर्शन अनुकूलन

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

### २. त्रुटि ह्यान्डलिङ

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

### ३. अनुगमन र अवलोकनीयता

```python
# Track RAG performance
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```


## आगामी कदमहरू

यस सत्र पूरा गरेपछि:

१. **सत्र ३ अन्वेषण गर्नुहोस्**: Foundry Local मा ओपन-सोर्स मोडेलहरू
२. **उत्पादन RAG निर्माण गर्नुहोस्**: Chainlit (नमूना ०४) प्रयोग गरेर कार्यान्वयन गर्नुहोस्
३. **उन्नत भेक्टर खोज**: Chroma वा Pinecone सँग समाहित गर्नुहोस्
४. **क्लाउड माइग्रेशन**: Azure AI Foundry मा परिनियोजन गर्नुहोस्
५. **RAG गुणस्तर मूल्याङ्कन गर्नुहोस्**: `cd Workshop/samples;python -m session02.rag_eval_ragas` चलाएर उत्तर प्रासंगिकता, सत्यता, र सन्दर्भ सटीकता मापन गर्नुहोस्

### वैकल्पिक सुधारहरू

| श्रेणी | सुधार | कारण | दिशा |
|----------|-------------|-----------|-----------|
| पुनःप्राप्ति | TF-IDF लाई भेक्टर स्टोर (FAISS / Chroma) सँग प्रतिस्थापन गर्नुहोस् | राम्रो अर्थपूर्ण पुनःस्मरण र स्केलेबिलिटी | दस्तावेजहरू (५००–८०० अक्षरहरू) टुक्रा गर्नुहोस्, एम्बेड गर्नुहोस्, अनुक्रमणिका कायम गर्नुहोस् |
| हाइब्रिड अनुक्रमणिका | दोहोरो अर्थपूर्ण + कीवर्ड फिल्टरिङ | संख्यात्मक / कोड प्रश्नहरूमा सटीकता सुधार गर्दछ | कीवर्डद्वारा फिल्टर गर्नुहोस् र कोसाइन समानताद्वारा रैंक गर्नुहोस् |
| एम्बेडिङ | बहु एम्बेडिङ मोडेलहरू मूल्याङ्कन गर्नुहोस् | प्रासंगिकता बनाम गति अनुकूलन गर्नुहोस् | A/B: MiniLM बनाम E5-small बनाम स्थानीय होस्ट गरिएको एन्कोडर |
| क्यासिङ | एम्बेडिङ र पुनःप्राप्ति परिणामहरू क्यास गर्नुहोस् | दोहोरिएको प्रश्न ढिलाइ कम गर्नुहोस् | साधारण डिस्क पिकल / sqlite ह्यास कुञ्जीको साथ |
| मूल्याङ्कन | ragas डेटासेट विस्तार गर्नुहोस् | सांख्यिकीय रूपमा अर्थपूर्ण गुणस्तर | ५०–१०० Q/A + सन्दर्भहरू क्युरेट गर्नुहोस्; विषयद्वारा स्तरीकरण गर्नुहोस् |
| मेट्रिक्स | पुनःप्राप्ति र सिर्जना समय ट्र्याक गर्नुहोस् | प्रदर्शन प्रोफाइलिङ | प्रत्येक कलमा `retrieval_ms`, `gen_ms`, `tokens` कैप्चर गर्नुहोस् |
| गार्डरेल्स | भ्रम fallback थप्नुहोस् | सुरक्षित उत्तरहरू | यदि सत्यता < थ्रेसहोल्ड → उत्तर: "पर्याप्त सन्दर्भ छैन।" |
| फलब्याक | स्थानीय → Azure मोडेल क्यास्केड गर्नुहोस् | हाइब्रिड गुणस्तर वृद्धि | कम विश्वासमा OpenAI API मार्फत क्लाउडमा मार्ग |
| निर्धारण | स्थिर तुलना रनहरू | पुनःप्राप्ति योग्य मूल्याङ्कन सेटहरू | बीज फिक्स गर्नुहोस्, `temperature=0`, स्याम्पलर अनियमितता अक्षम गर्नुहोस् |
| अनुगमन | मूल्याङ्कन रन इतिहास कायम गर्नुहोस् | प्रतिगमन पत्ता लगाउने | JSON लाइनहरू टाइमस्ट्याम्प + मेट्रिक डेल्टासँग थप्नुहोस् |

#### उदाहरण: पुनःप्राप्ति समय थप्दै

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


#### ragas सँग मूल्याङ्कन स्केलिङ

१. `question`, `answer`, `contexts`, `ground_truths` (सूची) क्षेत्रहरू सहित JSONL तयार गर्नुहोस्
२. `Dataset.from_list(list_of_dicts)` मा रूपान्तरण गर्नुहोस्
३. `evaluate(dataset, metrics=[...])` चलाउनुहोस्
४. प्रवृत्ति विश्लेषणको लागि मेट्रिक्स (CSV/JSON) भण्डारण गर्नुहोस्।

#### भेक्टर स्टोर छिटो सुरु (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) normalized
D, I = index.search(query_vec, k)
```

डिस्क स्थायित्वको लागि `faiss.write_index(index, "kb.index")` प्रयोग गर्नुहोस्।

## थप स्रोतहरू

### दस्तावेज
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG Patterns](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [Prompt Engineering Guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Ragas Evaluation Docs](https://docs.ragas.io)

### नमूना कोड
- [Module08 Sample 04](./samples/04/README.md) - Chainlit RAG अनुप्रयोग
- [Advanced Multi-Agent System](./samples/09/README.md) - एजेन्ट समन्वय ढाँचाहरू

---

**सत्र अवधि**: ३० मिनेट व्यावहारिक + १५ मिनेट Q&A  
**कठिनाई स्तर**: मध्यम  
**पूर्वापेक्षाहरू**: सत्र १ पूरा भएको, Python को आधारभूत ज्ञान

## नमूना परिदृश्य र कार्यशाला म्यापिङ

| कार्यशाला स्क्रिप्ट / नोटबुक | परिदृश्य | लक्ष्य | कोर डेटासेट / स्रोत | उदाहरण प्रश्न |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | आन्तरिक समर्थन ज्ञान आधार गोपनीयता + प्रदर्शन FAQs उत्तर दिने | न्यूनतम इन-मेमोरी RAG एम्बेडिङको साथ | स्क्रिप्टमा `DOCS` सूची (५ छोटो पासेजहरू) | किन स्थानीय अनुमानसँग RAG प्रयोग गर्ने? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | गुणस्तर विश्लेषक आधारभूत पुनःप्राप्ति सत्यता मेट्रिक्स स्थापना गर्दै | सानो कृत्रिम डेटासेटमा ragas मेट्रिक्स गणना गर्नुहोस् | `DOCS`, `QUESTIONS`, `GROUND_TRUTH` एरेहरू | स्थानीय अनुमानले के फाइदा दिन्छ? |
| `prompt_engineering.py` (उन्नत) | डोमेन SME बहु क्षेत्रहरूको लागि ग्राउन्डेड प्रम्प्टहरू निर्माण गर्दै | डोमेन प्रणाली प्रम्प्टहरू र टोकन प्रभाव तुलना गर्नुहोस् | इनलाइन `contexts` dict | Foundry Local मोडेल क्यासिङ कसरी ह्यान्डल गर्छ? |
| `csv_qa_system.py` | बिक्री अपरेसनहरू निर्यातमा अन्तरक्रियात्मक एनालिटिक्स अन्वेषण गर्दै | सानो बिक्री स्लाइस सारांश र प्रश्न गर्नुहोस् | उत्पन्न `sample_sales_data.csv` (१० पङ्क्तिहरू) | कुन उत्पादनको औसत बिक्री रकम उच्च छ? |
| `document_rag.py` | उत्पादन टोली आन्तरिक विकीको लागि दस्तावेज RAG अन्वेषण गर्दै | प्रासंगिक दस्तावेज पुनःप्राप्ति + उद्धरण गर्नुहोस् | `create_sample_knowledge_base()` सूची | Edge AI का फाइदाहरू के हुन्? |
| `migration_guide.py` | आर्किटेक्ट क्लाउड माइग्रेशन योजना तयार गर्दै | स्थानीय → Azure API समानता प्रदर्शन गर्नुहोस् | स्थिर परीक्षण प्रम्प्टहरू | Edge AI का फाइदाहरू २–३ वाक्यमा व्याख्या गर्नुहोस्। |

### डेटासेट स्निपेटहरू
इनलाइन RAG पाइपलाइन दस्तावेज सूची:
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```

Ragas मूल्याङ्कन सत्यता ट्युपलहरू:
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```


### परिदृश्य कथा
समर्थन इन्जिनियरिङ समूहले आन्तरिक FAQs उत्तर दिनको लागि छिटो प्रोटोटाइप चाहन्छ जसले ग्राहक डाटा बाह्य रूपमा उजागर गर्दैन। सत्र २ कलाकृतिहरू न्यूनतम अस्थायी RAG (कुनै स्थायित्व छैन) → संरचित CSV Q&A → उद्धरणसहित दस्तावेज पुनःप्राप्ति → उद्देश्य गुणस्तर मूल्याङ्कन (ragas) → Azure स्टेजिङको लागि तयार माइग्रेशन रणनीति सम्म प्रगति गर्दछ।

### विस्तार मार्गहरू
वैकल्पिक सुधारहरूको तालिका प्रयोग गरेर विकास गर्नुहोस्: TF-IDF लाई FAISS/Chroma सँग बदल्नुहोस्, मूल्याङ्कन कोष (५०–१०० Q/A) बढाउनुहोस्, सत्यता < थ्रेसहोल्ड हुँदा ठूलो मोडेलमा फलब्याक वृद्धि थप्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->