# เซสชัน 2: สร้างโซลูชัน AI ด้วย Azure AI Foundry

## บทคัดย่อ

เรียนรู้วิธีสร้างเวิร์กโฟลว์ GenAI ที่นำไปใช้ได้จริงโดยใช้ Foundry Local และ Azure AI Foundry ศึกษาเทคนิคการออกแบบคำสั่งขั้นสูง ผสานข้อมูลที่มีโครงสร้าง และจัดการงานด้วยกระบวนการที่สามารถทำซ้ำได้ แม้ว่าเนื้อหาจะเน้นที่ Retrieval-Augmented Generation (RAG) สำหรับการถามตอบเอกสารและข้อมูล แต่รูปแบบเหล่านี้สามารถนำไปปรับใช้กับการออกแบบโซลูชัน GenAI ในวงกว้างได้

## วัตถุประสงค์การเรียนรู้

เมื่อจบเซสชันนี้ คุณจะสามารถ:

- **เชี่ยวชาญการออกแบบคำสั่ง (Prompt Engineering)**: ออกแบบคำสั่งระบบและกลยุทธ์การตั้งค่าพื้นฐานที่มีประสิทธิภาพ
- **นำรูปแบบ RAG ไปใช้**: สร้างระบบถามตอบที่ใช้เอกสารโดยใช้การค้นหาแบบเวกเตอร์
- **ผสานข้อมูลที่มีโครงสร้าง**: ทำงานกับข้อมูล CSV, JSON และข้อมูลแบบตารางในเวิร์กโฟลว์ AI
- **สร้าง RAG สำหรับการใช้งานจริง**: สร้างแอปพลิเคชัน RAG ที่สามารถขยายได้ด้วย Chainlit
- **เชื่อมต่อจาก Local สู่ Cloud**: เข้าใจเส้นทางการย้ายจาก Foundry Local ไปยัง Azure AI Foundry

## ความต้องการเบื้องต้น

- ผ่านการเรียนเซสชัน 1 (การตั้งค่า Foundry Local)
- มีความเข้าใจพื้นฐานเกี่ยวกับฐานข้อมูลเวกเตอร์และ embeddings
- มีประสบการณ์การเขียนโปรแกรม Python
- คุ้นเคยกับแนวคิดการประมวลผลเอกสาร

### การเริ่มต้นใช้งานข้ามแพลตฟอร์ม (Windows & macOS)

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

หากยังไม่มีไบนารี Foundry Local สำหรับ macOS ในสภาพแวดล้อมของคุณ ให้รันบริการบน Windows VM หรือ container และตั้งค่า:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## การตรวจสอบ: การตรวจสอบสภาพแวดล้อม Foundry Local

ก่อนเริ่มการสาธิต ให้ตรวจสอบสภาพแวดล้อมในเครื่องของคุณ:

```powershell
foundry --version              # Ensure CLI is installed
foundry status                 # Service status
foundry model run phi-4-mini   # Start baseline SLM
curl http://localhost:5273/v1/models  # Validate API (should list running model)
```

หากคำสั่งสุดท้ายล้มเหลว ให้เริ่ม (หรือเริ่มใหม่) บริการ: `foundry service start`.

## ลำดับการสาธิต (30 นาที)

### 1. คำสั่งระบบและกลยุทธ์การตั้งค่าพื้นฐาน (10 นาที)

#### ขั้นตอน 1.1: การออกแบบคำสั่งขั้นสูง

สร้าง `samples/02-rag-solutions/prompt_engineering.py`:

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

#### ขั้นตอน 1.2: ทดสอบกลยุทธ์การตั้งค่าพื้นฐาน

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the prompt engineering demo
python samples/02-rag-solutions/prompt_engineering.py
```


### 2. ผสานข้อมูลแบบตารางกับคำสั่ง (ถามตอบ CSV) (10 นาที)

#### ขั้นตอน 2.1: การผสานข้อมูล CSV

สร้าง `samples/02-rag-solutions/csv_qa_system.py`:

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

#### ขั้นตอน 2.2: ทดสอบระบบถามตอบ CSV

```powershell
# Run the CSV Q&A demo
python samples/02-rag-solutions/csv_qa_system.py
```


### 3. โครงการเริ่มต้น: ปรับปรุง 02-grounding-data (5 นาที)

#### ขั้นตอน 3.1: ระบบ RAG เอกสารที่ปรับปรุงแล้ว

สร้าง `samples/02-rag-solutions/document_rag.py`:

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


### 4. แสดงเส้นทางการย้ายจาก CLI สู่ Azure (5 นาที)

#### ขั้นตอน 4.1: ภาพรวมกลยุทธ์การย้าย

สร้าง `samples/02-rag-solutions/migration_guide.py`:

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

#### ขั้นตอน 4.2: ทดสอบรูปแบบการย้าย

```powershell
# Run the migration demo
python samples/02-rag-solutions/migration_guide.py
```


## แนวคิดสำคัญที่ครอบคลุม

### 1. การออกแบบคำสั่งขั้นสูง

- **คำสั่งระบบ**: บุคคลผู้เชี่ยวชาญเฉพาะด้าน
- **กลยุทธ์การตั้งค่าพื้นฐาน**: เทคนิคการผสานบริบท
- **การควบคุมอุณหภูมิ**: สมดุลระหว่างความคิดสร้างสรรค์และความสม่ำเสมอ
- **การจัดการโทเค็น**: การใช้บริบทอย่างมีประสิทธิภาพ

### 2. การผสานข้อมูลที่มีโครงสร้าง

- **การประมวลผล CSV**: การผสาน Pandas กับโมเดล AI
- **การวิเคราะห์ทางสถิติ**: การสรุปข้อมูลอัตโนมัติ
- **การสร้างบริบท**: การสร้างบริบทแบบไดนามิกตามคำถาม
- **การรองรับหลายรูปแบบ**: JSON, CSV และข้อมูลแบบตาราง

### 3. รูปแบบการนำ RAG ไปใช้

- **การค้นหาแบบเวกเตอร์**: TF-IDF และความคล้ายคลึงของโคไซน์
- **การดึงเอกสาร**: การให้คะแนนและการจัดอันดับความเกี่ยวข้อง
- **การผสมผสานบริบท**: การสังเคราะห์เอกสารหลายฉบับ
- **การสร้างคำตอบ**: การสร้างคำตอบที่มีพื้นฐาน

### 4. กลยุทธ์การย้ายไปยัง Cloud

- **API แบบรวม**: โค้ดเบสเดียวสำหรับ Local และ Cloud
- **การแยกสภาพแวดล้อม**: การปรับใช้ที่ขับเคลื่อนด้วยการกำหนดค่า
- **เวิร์กโฟลว์การพัฒนา**: Local → Staging → Production
- **การเพิ่มประสิทธิภาพต้นทุน**: การพัฒนาใน Local การผลิตใน Cloud

## ข้อควรพิจารณาสำหรับการผลิต

### 1. การเพิ่มประสิทธิภาพการทำงาน

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

### 2. การจัดการข้อผิดพลาด

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

### 3. การตรวจสอบและการสังเกตการณ์

```python
# Track RAG performance
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```


## ขั้นตอนถัดไป

หลังจากจบเซสชันนี้:

1. **สำรวจเซสชัน 3**: โมเดลโอเพ่นซอร์สใน Foundry Local
2. **สร้าง RAG สำหรับการผลิต**: ใช้ Chainlit (ตัวอย่าง 04)
3. **การค้นหาเวกเตอร์ขั้นสูง**: ผสานกับ Chroma หรือ Pinecone
4. **การย้ายไปยัง Cloud**: ปรับใช้กับ Azure AI Foundry
5. **ประเมินคุณภาพ RAG**: รัน `cd Workshop/samples;python -m session02.rag_eval_ragas` เพื่อวัดความเกี่ยวข้องของคำตอบ ความถูกต้อง และความแม่นยำของบริบทโดยใช้ ragas

### การปรับปรุงเพิ่มเติม

| หมวดหมู่ | การปรับปรุง | เหตุผล | ทิศทาง |
|----------|-------------|-----------|-----------|
| การดึงข้อมูล | แทนที่ TF-IDF ด้วย vector store (FAISS / Chroma) | การเรียกคืนเชิงความหมายที่ดีกว่าและความสามารถในการขยาย | แบ่งเอกสาร (500–800 ตัวอักษร), ฝัง, บันทึกดัชนี |
| ดัชนีแบบไฮบริด | การกรองแบบคำหลัก + เชิงความหมาย | เพิ่มความแม่นยำในคำถามเชิงตัวเลข / โค้ด | กรองด้วยคำหลักแล้วจัดอันดับด้วยความคล้ายคลึงของโคไซน์ |
| Embeddings | ประเมินโมเดล embedding หลายตัว | ปรับปรุงความเกี่ยวข้องเทียบกับความเร็ว | A/B: MiniLM vs E5-small vs ตัวเข้ารหัสที่โฮสต์ในเครื่อง |
| การแคช | แคช embeddings และผลลัพธ์การดึงข้อมูล | ลดเวลาแฝงของคำถามซ้ำ | แคชง่าย ๆ บนดิสก์ pickle / sqlite พร้อมคีย์แฮช |
| การประเมิน | ขยายชุดข้อมูล ragas | คุณภาพที่มีความหมายทางสถิติ | สร้างคำถาม/คำตอบ + บริบท 50–100 รายการ; แบ่งตามหัวข้อ |
| เมตริก | ติดตามเวลาในการดึงข้อมูลและการสร้าง | การวิเคราะห์ประสิทธิภาพ | บันทึก `retrieval_ms`, `gen_ms`, `tokens` ต่อการเรียก |
| การป้องกัน | เพิ่มการตอบกลับสำรองเมื่อเกิดข้อผิดพลาด | คำตอบที่ปลอดภัยกว่า | หากความถูกต้อง < เกณฑ์ → คำตอบ: "บริบทไม่เพียงพอ." |
| การสำรอง | การเปลี่ยนเส้นทางจาก Local → โมเดล Azure | เพิ่มคุณภาพแบบไฮบริด | เมื่อความมั่นใจต่ำให้เปลี่ยนไปใช้ Cloud ผ่าน OpenAI API เดียวกัน |
| การกำหนดค่า | การเปรียบเทียบที่เสถียร | ชุดการประเมินที่ทำซ้ำได้ | กำหนด seed, `temperature=0`, ปิดการสุ่มของตัวสุ่ม |
| การตรวจสอบ | บันทึกประวัติการประเมิน | การตรวจจับการถดถอย | เพิ่ม JSON lines พร้อม timestamp + การเปลี่ยนแปลงเมตริก |

#### ตัวอย่าง: การเพิ่มเวลาในการดึงข้อมูล

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


#### การขยายการประเมินด้วย ragas

1. สร้าง JSONL พร้อมฟิลด์: `question`, `answer`, `contexts`, `ground_truths` (list)
2. แปลงเป็น `Dataset.from_list(list_of_dicts)`
3. รัน `evaluate(dataset, metrics=[...])`
4. บันทึกเมตริก (CSV/JSON) เพื่อวิเคราะห์แนวโน้ม

#### การเริ่มต้นใช้งาน Vector Store (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) normalized
D, I = index.search(query_vec, k)
```

สำหรับการบันทึกลงดิสก์ใช้ `faiss.write_index(index, "kb.index")`.

## แหล่งข้อมูลเพิ่มเติม

### เอกสาร
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG Patterns](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [คู่มือการออกแบบคำสั่ง](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [เอกสารการประเมิน Ragas](https://docs.ragas.io)

### ตัวอย่างโค้ด
- [ตัวอย่าง Module08 Sample 04](./samples/04/README.md) - แอปพลิเคชัน RAG ด้วย Chainlit
- [ระบบหลายตัวแทนขั้นสูง](./samples/09/README.md) - รูปแบบการประสานงานตัวแทน

---

**ระยะเวลาเซสชัน**: 30 นาทีปฏิบัติ + 15 นาทีถามตอบ  
**ระดับความยาก**: ระดับกลาง  
**ความต้องการเบื้องต้น**: ผ่านเซสชัน 1, มีความรู้ Python เบื้องต้น  

## ตัวอย่างสถานการณ์และการจับคู่กับเวิร์กช็อป

| สคริปต์ / โน้ตบุ๊กเวิร์กช็อป | สถานการณ์ | เป้าหมาย | ชุดข้อมูล / แหล่งข้อมูลหลัก | ตัวอย่างคำถาม |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | ฐานความรู้สนับสนุนภายในที่ตอบคำถามเกี่ยวกับความเป็นส่วนตัว + ประสิทธิภาพ | RAG แบบง่ายในหน่วยความจำ | รายการ `DOCS` ในสคริปต์ (5 ข้อความสั้น) | ทำไมต้องใช้ RAG กับการอนุมานในเครื่อง? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | นักวิเคราะห์คุณภาพที่สร้างเมตริกความถูกต้องของการดึงข้อมูล | คำนวณเมตริก ragas บนชุดข้อมูลสังเคราะห์ขนาดเล็ก | อาร์เรย์ `DOCS`, `QUESTIONS`, `GROUND_TRUTH` | ข้อดีของการอนุมานในเครื่องคืออะไร? |
| `prompt_engineering.py` (ขั้นสูง) | ผู้เชี่ยวชาญด้านโดเมนที่ออกแบบคำสั่งที่มีพื้นฐานสำหรับหลายอุตสาหกรรม | เปรียบเทียบคำสั่งระบบโดเมนและผลกระทบของโทเค็น | พจนานุกรม `contexts` ในตัว | Foundry Local จัดการการแคชโมเดลอย่างไร? |
| `csv_qa_system.py` | ทีมขายที่สำรวจการวิเคราะห์เชิงโต้ตอบผ่านการส่งออกข้อมูล | สรุปและถามตอบข้อมูลการขายขนาดเล็ก | `sample_sales_data.csv` ที่สร้างขึ้น (10 แถว) | ผลิตภัณฑ์ใดมีจำนวนยอดขายเฉลี่ยสูงสุด? |
| `document_rag.py` | ทีมผลิตภัณฑ์ที่สำรวจ RAG เอกสารสำหรับวิกิภายใน | ดึงข้อมูล + อ้างอิงเอกสารที่เกี่ยวข้อง | รายการ `create_sample_knowledge_base()` | ข้อดีของ Edge AI คืออะไร? |
| `migration_guide.py` | สถาปนิกที่เตรียมแผนการย้ายไปยัง Cloud | แสดงความเท่าเทียมของ API Local → Azure | คำสั่งทดสอบแบบคงที่ | อธิบายข้อดีของ Edge AI ใน 2–3 ประโยค. |

### ตัวอย่างชุดข้อมูล
รายการเอกสาร RAG pipeline:
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```

คู่ความจริงสำหรับการประเมิน ragas:
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```


### เรื่องราวสถานการณ์
กลุ่มวิศวกรรมสนับสนุนต้องการต้นแบบที่รวดเร็วเพื่อตอบคำถามภายในโดยไม่เปิดเผยข้อมูลลูกค้าไปภายนอก สิ่งประดิษฐ์ในเซสชัน 2 พัฒนาจาก RAG แบบง่ายที่ไม่มีการบันทึก → ถามตอบ CSV แบบมีโครงสร้าง → การดึงเอกสารพร้อมการอ้างอิง → การประเมินคุณภาพเชิงวัตถุประสงค์ (ragas) → กลยุทธ์การย้ายที่พร้อมสำหรับการทดสอบใน Azure

### เส้นทางการขยาย
ใช้ตารางการปรับปรุงเพิ่มเติมเพื่อพัฒนา: แทนที่ TF-IDF ด้วย FAISS/Chroma, ขยายชุดการประเมิน (50–100 คำถาม/คำตอบ), เพิ่มการสำรองเมื่อความถูกต้อง < เกณฑ์.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->