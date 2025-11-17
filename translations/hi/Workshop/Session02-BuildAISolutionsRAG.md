<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bb6014013b4adb7d7bfc60504eafed5d",
  "translation_date": "2025-11-17T18:43:03+00:00",
  "source_file": "Workshop/Session02-BuildAISolutionsRAG.md",
  "language_code": "hi"
}
-->
# सत्र 2: Azure AI Foundry के साथ AI समाधान बनाएं

## सारांश

Foundry Local और Azure AI Foundry का उपयोग करके GenAI वर्कफ़्लो बनाने का तरीका जानें। उन्नत प्रॉम्प्ट इंजीनियरिंग, संरचित डेटा को एकीकृत करना, और पुनरुत्पादक पाइपलाइनों के साथ कार्यों को व्यवस्थित करना सीखें। जबकि ध्यान दस्तावेज़ और डेटा Q&A के लिए Retrieval-Augmented Generation (RAG) पर है, पैटर्न व्यापक GenAI समाधान डिज़ाइन के लिए सामान्यीकृत हैं।

## सीखने के उद्देश्य

इस सत्र के अंत तक, आप:

- **प्रॉम्प्ट इंजीनियरिंग में महारत हासिल करें**: प्रभावी सिस्टम प्रॉम्प्ट और ग्राउंडिंग रणनीतियाँ डिज़ाइन करें
- **RAG पैटर्न लागू करें**: वेक्टर सर्च के साथ दस्तावेज़-आधारित Q&A सिस्टम बनाएं
- **संरचित डेटा को एकीकृत करें**: AI वर्कफ़्लो में CSV, JSON, और टेबलर डेटा के साथ काम करें
- **प्रोडक्शन RAG बनाएं**: Chainlit के साथ स्केलेबल RAG एप्लिकेशन बनाएं
- **लोकल से क्लाउड तक पुल बनाएं**: Foundry Local से Azure AI Foundry तक माइग्रेशन पथ को समझें

## आवश्यकताएँ

- सत्र 1 (Foundry Local सेटअप) पूरा किया हुआ हो
- वेक्टर डेटाबेस और एम्बेडिंग की बुनियादी समझ
- Python प्रोग्रामिंग का अनुभव
- दस्तावेज़ प्रसंस्करण अवधारणाओं से परिचितता

### क्रॉस-प्लेटफ़ॉर्म वातावरण त्वरित शुरुआत (Windows और macOS)

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

यदि Foundry Local macOS बाइनरी आपके वातावरण में उपलब्ध नहीं हैं, तो सेवा को Windows VM या कंटेनर पर चलाएं और सेट करें:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## मान्यता: Foundry Local वातावरण जांच

डेमो शुरू करने से पहले, अपने लोकल वातावरण को मान्य करें:

```powershell
foundry --version              # Ensure CLI is installed
foundry status                 # Service status
foundry model run phi-4-mini   # Start baseline SLM
curl http://localhost:5273/v1/models  # Validate API (should list running model)
```

यदि अंतिम कमांड विफल हो जाए, तो सेवा शुरू करें (या पुनः प्रारंभ करें): `foundry service start`।

## डेमो प्रवाह (30 मिनट)

### 1. सिस्टम प्रॉम्प्ट और ग्राउंडिंग रणनीतियाँ (10 मिनट)

#### चरण 1.1: उन्नत प्रॉम्प्ट इंजीनियरिंग

`samples/02-rag-solutions/prompt_engineering.py` बनाएं:

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

#### चरण 1.2: ग्राउंडिंग रणनीतियों का परीक्षण करें

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the prompt engineering demo
python samples/02-rag-solutions/prompt_engineering.py
```


### 2. प्रॉम्प्ट के साथ टेबलर डेटा को एकीकृत करें (CSV Q&A) (10 मिनट)

#### चरण 2.1: CSV डेटा एकीकरण

`samples/02-rag-solutions/csv_qa_system.py` बनाएं:

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

#### चरण 2.2: CSV Q&A सिस्टम का परीक्षण करें

```powershell
# Run the CSV Q&A demo
python samples/02-rag-solutions/csv_qa_system.py
```


### 3. स्टार्टर प्रोजेक्ट: 02-grounding-data को अनुकूलित करें (5 मिनट)

#### चरण 3.1: उन्नत दस्तावेज़ RAG सिस्टम

`samples/02-rag-solutions/document_rag.py` बनाएं:

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


### 4. CLI से Azure माइग्रेशन पथ दिखाएं (5 मिनट)

#### चरण 4.1: माइग्रेशन रणनीति का अवलोकन

`samples/02-rag-solutions/migration_guide.py` बनाएं:

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

#### चरण 4.2: माइग्रेशन पैटर्न का परीक्षण करें

```powershell
# Run the migration demo
python samples/02-rag-solutions/migration_guide.py
```


## कवर किए गए प्रमुख अवधारणाएँ

### 1. उन्नत प्रॉम्प्ट इंजीनियरिंग

- **सिस्टम प्रॉम्प्ट**: डोमेन-विशिष्ट विशेषज्ञ व्यक्तित्व
- **ग्राउंडिंग रणनीतियाँ**: संदर्भ एकीकरण तकनीकें
- **टेम्परेचर नियंत्रण**: रचनात्मकता बनाम स्थिरता का संतुलन
- **टोकन प्रबंधन**: कुशल संदर्भ उपयोग

### 2. संरचित डेटा एकीकरण

- **CSV प्रसंस्करण**: Pandas का AI मॉडल्स के साथ एकीकरण
- **सांख्यिकीय विश्लेषण**: स्वचालित डेटा सारांश
- **संदर्भ निर्माण**: क्वेरी के आधार पर गतिशील संदर्भ निर्माण
- **मल्टी-फॉर्मेट समर्थन**: JSON, CSV, और टेबलर डेटा

### 3. RAG कार्यान्वयन पैटर्न

- **वेक्टर सर्च**: TF-IDF और कोसाइन समानता
- **दस्तावेज़ पुनर्प्राप्ति**: प्रासंगिकता स्कोरिंग और रैंकिंग
- **संदर्भ संयोजन**: मल्टी-दस्तावेज़ संश्लेषण
- **उत्तर निर्माण**: ग्राउंडेड प्रतिक्रिया निर्माण

### 4. क्लाउड माइग्रेशन रणनीतियाँ

- **एकीकृत API**: लोकल और क्लाउड के लिए एकल कोडबेस
- **वातावरण अमूर्तता**: कॉन्फ़िगरेशन-चालित परिनियोजन
- **विकास वर्कफ़्लो**: लोकल → स्टेजिंग → प्रोडक्शन
- **लागत अनुकूलन**: लोकल विकास, क्लाउड प्रोडक्शन

## प्रोडक्शन विचार

### 1. प्रदर्शन अनुकूलन

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

### 2. त्रुटि प्रबंधन

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

### 3. निगरानी और अवलोकन

```python
# Track RAG performance
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```


## अगले कदम

इस सत्र को पूरा करने के बाद:

1. **सत्र 3 का अन्वेषण करें**: Foundry Local में ओपन-सोर्स मॉडल
2. **प्रोडक्शन RAG बनाएं**: Chainlit के साथ कार्यान्वित करें (नमूना 04)
3. **उन्नत वेक्टर सर्च**: Chroma या Pinecone के साथ एकीकृत करें
4. **क्लाउड माइग्रेशन**: Azure AI Foundry पर परिनियोजित करें
5. **RAG गुणवत्ता का मूल्यांकन करें**: `cd Workshop/samples;python -m session02.rag_eval_ragas` चलाकर उत्तर की प्रासंगिकता, सत्यता, और संदर्भ सटीकता को मापें

### वैकल्पिक संवर्द्धन

| श्रेणी | संवर्द्धन | कारण | दिशा |
|----------|-------------|-----------|-----------|
| पुनर्प्राप्ति | TF-IDF को वेक्टर स्टोर (FAISS / Chroma) से बदलें | बेहतर सेमांटिक रिकॉल और स्केलेबिलिटी | डॉक को चंक करें (500–800 वर्ण), एम्बेड करें, इंडेक्स को स्थायी बनाएं |
| हाइब्रिड इंडेक्स | डुअल सेमांटिक + कीवर्ड फ़िल्टरिंग | संख्यात्मक / कोड क्वेरी पर सटीकता में सुधार | कीवर्ड द्वारा फ़िल्टर करें फिर कोसाइन समानता द्वारा रैंक करें |
| एम्बेडिंग | कई एम्बेडिंग मॉडल का मूल्यांकन करें | प्रासंगिकता बनाम गति को अनुकूलित करें | A/B: MiniLM बनाम E5-small बनाम लोकल होस्टेड एन्कोडर |
| कैशिंग | एम्बेडिंग और पुनर्प्राप्ति परिणामों को कैश करें | दोहराए गए क्वेरी विलंबता को कम करें | सरल ऑन-डिस्क पिकल / sqlite के साथ हैश कुंजी |
| मूल्यांकन | रागास डेटासेट का विस्तार करें | सांख्यिकीय रूप से सार्थक गुणवत्ता | 50–100 Q/A + संदर्भों को क्यूरेट करें; विषय द्वारा स्तरीकरण करें |
| मीट्रिक्स | पुनर्प्राप्ति और निर्माण समय को ट्रैक करें | प्रदर्शन प्रोफाइलिंग | प्रत्येक कॉल पर `retrieval_ms`, `gen_ms`, `tokens` कैप्चर करें |
| गार्डरेल्स | मतिभ्रम फॉलबैक जोड़ें | सुरक्षित उत्तर | यदि सत्यता < सीमा → उत्तर: "पर्याप्त संदर्भ नहीं।" |
| फॉलबैक | लोकल → Azure मॉडल को कैस्केड करें | हाइब्रिड गुणवत्ता में सुधार | कम आत्मविश्वास पर क्लाउड को OpenAI API के माध्यम से रूट करें |
| निर्धारण | स्थिर तुलना रन | पुनरावृत्त मूल्यांकन सेट | बीज को फिक्स करें, `temperature=0`, सैंपलर रैंडमनेस को अक्षम करें |
| निगरानी | मूल्यांकन रन इतिहास को स्थायी बनाएं | प्रतिगमन का पता लगाना | JSON लाइनों को टाइमस्टैम्प + मीट्रिक डेल्टा के साथ जोड़ें |

#### उदाहरण: पुनर्प्राप्ति समय जोड़ना

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


#### रागास के साथ मूल्यांकन को स्केल करना

1. JSONL को इकट्ठा करें जिसमें फ़ील्ड हों: `question`, `answer`, `contexts`, `ground_truths` (सूची)
2. इसे `Dataset.from_list(list_of_dicts)` में बदलें
3. `evaluate(dataset, metrics=[...])` चलाएं
4. ट्रेंड विश्लेषण के लिए मीट्रिक्स (CSV/JSON) स्टोर करें।

#### वेक्टर स्टोर त्वरित शुरुआत (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) normalized
D, I = index.search(query_vec, k)
```

डिस्क स्थायित्व के लिए `faiss.write_index(index, "kb.index")` का उपयोग करें।

## अतिरिक्त संसाधन

### दस्तावेज़ीकरण
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG Patterns](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [प्रॉम्प्ट इंजीनियरिंग गाइड](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Ragas मूल्यांकन दस्तावेज़](https://docs.ragas.io)

### नमूना कोड
- [Module08 Sample 04](./samples/04/README.md) - Chainlit RAG एप्लिकेशन
- [उन्नत मल्टी-एजेंट सिस्टम](./samples/09/README.md) - एजेंट समन्वय पैटर्न

---

**सत्र अवधि**: 30 मिनट हैंड्स-ऑन + 15 मिनट Q&A  
**कठिनाई स्तर**: मध्यम  
**आवश्यकताएँ**: सत्र 1 पूरा किया हुआ, Python का बुनियादी ज्ञान

## नमूना परिदृश्य और कार्यशाला मैपिंग

| कार्यशाला स्क्रिप्ट / नोटबुक | परिदृश्य | लक्ष्य | मुख्य डेटासेट / स्रोत | उदाहरण प्रश्न |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | गोपनीयता + प्रदर्शन FAQs का उत्तर देने के लिए आंतरिक समर्थन ज्ञान आधार | एम्बेडिंग के साथ न्यूनतम इन-मेमोरी RAG | स्क्रिप्ट में `DOCS` सूची (5 छोटे अंश) | लोकल इंफेरेंस के साथ RAG का उपयोग क्यों करें? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | गुणवत्ता विश्लेषक जो पुनर्प्राप्ति सत्यता मीट्रिक्स का आधारभूत स्तर स्थापित कर रहा है | छोटे सिंथेटिक डेटासेट पर रागास मीट्रिक्स की गणना करें | `DOCS`, `QUESTIONS`, `GROUND_TRUTH` ऐरे | लोकल इंफेरेंस क्या लाभ प्रदान करता है? |
| `prompt_engineering.py` (उन्नत) | डोमेन SME जो कई वर्टिकल के लिए ग्राउंडेड प्रॉम्प्ट तैयार कर रहा है | डोमेन सिस्टम प्रॉम्प्ट और टोकन प्रभाव की तुलना करें | इनलाइन `contexts` डिक्ट | Foundry Local मॉडल कैशिंग को कैसे संभालता है? |
| `csv_qa_system.py` | बिक्री संचालन जो निर्यात पर इंटरैक्टिव एनालिटिक्स का पता लगा रहा है | छोटे बिक्री स्लाइस को सारांशित करें और क्वेरी करें | उत्पन्न `sample_sales_data.csv` (10 पंक्तियाँ) | किस उत्पाद की औसत बिक्री राशि सबसे अधिक है? |
| `document_rag.py` | उत्पाद टीम जो आंतरिक विकी के लिए दस्तावेज़ RAG का पता लगा रही है | प्रासंगिक दस्तावेज़ पुनर्प्राप्त करें + उद्धृत करें | `create_sample_knowledge_base()` सूची | Edge AI के लाभ क्या हैं? |
| `migration_guide.py` | आर्किटेक्ट जो क्लाउड माइग्रेशन योजना तैयार कर रहा है | लोकल→Azure API समानता का प्रदर्शन करें | स्थिर परीक्षण प्रॉम्प्ट | Edge AI के लाभों को 2–3 वाक्यों में समझाएँ। |

### डेटासेट स्निपेट्स
इनलाइन RAG पाइपलाइन डॉक सूची:
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```

रागास मूल्यांकन सत्य ट्यूपल:
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```


### परिदृश्य कथा
सपोर्ट इंजीनियरिंग समूह एक तेज़ प्रोटोटाइप चाहता है जो आंतरिक FAQs का उत्तर दे सके बिना ग्राहक डेटा को बाहरी रूप से उजागर किए। सत्र 2 आर्टिफैक्ट्स न्यूनतम अस्थायी RAG (कोई स्थायित्व नहीं) → संरचित CSV Q&A → उद्धरण के साथ दस्तावेज़ पुनर्प्राप्ति → उद्देश्य गुणवत्ता मूल्यांकन (रागास) → Azure स्टेजिंग के लिए तैयार माइग्रेशन रणनीति तक प्रगति करते हैं।

### विस्तार पथ
वैकल्पिक संवर्द्धन तालिका का उपयोग करें: TF‑IDF को FAISS/Chroma से बदलें, मूल्यांकन कॉर्पस को बड़ा करें (50–100 Q/A), जब सत्यता < सीमा हो तो बड़े मॉडल पर फॉलबैक वृद्धि जोड़ें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->