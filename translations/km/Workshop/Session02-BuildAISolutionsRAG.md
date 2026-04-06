# ការប្រជុំលើកទី 2៖ បង្កើតដំណោះស្រាយ AI ជាមួយ Azure AI Foundry

## សង្ខេប

ស្វែងយល់ពីរបៀបបង្កើតហ្វ្លូវ​សកម្មភាព GenAI ដើម្បីអនុវត្តដោយប្រើ Foundry Local និង Azure AI Foundry។ រៀនបច្ចេកទេសបញ្ចូលពាក្យបញ្ជាប្រកបដោយជំនាញ ខ្សែបញ្ជា និងតំណៀបតភ្ជាប់ទិន្នន័យរចនាសម្ព័ន្ធ ហើយរៀបចំកិរិយាសម្ព័ន្ធដោយប្រើបច្ចេកវិទ្យាផ្លូវការ។ ខណៈពេលដែលផ្តោតសំខាន់លើ Retrieval-Augmented Generation (RAG) សម្រាប់ Q&A ឯកសារ និងទិន្នន័យ គំរូទាំងនេះអាចអនុវត្តទៅការរចនាដំណោះស្រាយ GenAI ទូលំទូលាយជាងនេះ។

## គោលបំណងការសិក្សា

នៅចុងបញ្ចប់នៃវគ្គនេះ អ្នកនឹងអាច៖

- **ជាទីគូសបញ្ចូលពាក្យបញ្ជាប្រកបដោយជំនាញ**៖ រចនាពាក្យបញ្ជាប្រព័ន្ធមានប្រសិទ្ធភាព និងយុទ្ធសាស្រ្តបង្គ្រាប់
- **អនុវត្តគំរូ RAG**៖ បង្កើតប្រព័ន្ធ Q&A អ្នកយកព្រឹតិ្តការណ៍ឯកសារជាមួយស្វែងរកវ៉ិកទ័រ
- **បញ្ចូលទិន្នន័យរចនាសម្ព័ន្ធ**៖ ធ្វើការជាមួយទិន្នន័យ CSV, JSON និងទិន្នន័យក្នុងរូបមាត្រនានាក្នុងហ្វ្លូវ AI
- **បង្កើត RAG ផលិតកម្ម**៖ បង្កើតកម្មវិធី RAG ជាខ្នាតធំជាមួយ Chainlit
- **ភ្ជាប់ពីមូលដ្ឋានដល់ពពក**៖ យល់ដឹងពីផ្លូវការផ្ទេរពី Foundry Local ទៅ Azure AI Foundry

## តម្រូវការមុនពេលចាប់ផ្តើម

- សម្រេចបញ្ចប់វគ្គ 1 (ការតំឡើង Foundry Local)
- ការយល់ដឹងមូលដ្ឋានអំពីមូលដ្ឋានទិន្នន័យវ៉ិកទ័រ និង embeddings
- បទពិសោធន៍កម្មវិធីភាសា Python
- ស្គាល់ពីមាតិកាការដំណើរការឯកសារ

### ចាប់ផ្តើមបរិយាកាសឆ្លើយឆ្លងបាន (Windows & macOS)

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
  
បើនៅមិនមានកម្មវិធីរត់ Foundry Local macOS នៅក្នុងបរិយាកាសរបស់អ្នកទេ សូមរត់សេវាកម្មនៅលើ VM Windows ឬកុងតឺន័រ ហើយកំណត់៖  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## ការត្រួតពិនិត្យ៖ ពិនិត្យបរិយាកាស Foundry Local

មុនចាប់ផ្តើមសាកល្បងកម្មវិធី សូមត្រួតពិនិត្យបរិយាកាសក្នុងស្រុក៖

```powershell
foundry --version              # ប្រាកដថា CLI ត្រូវបានដំឡើង
foundry status                 # ស្ថានភាពសេវា
foundry model run phi-4-mini   # ចាប់ផ្តើម SLM គោលបំណង
curl http://localhost:5273/v1/models  # ផ្ទៀងផ្ទាត់ API (គួរតែបង្ហាញម៉ូដែលកំពុងដំណើរការ)
```
  

បើបញ្ជាលិខិតចុងក្រោយបរាជ័យ សូមចាប់ផ្តើម (ឬចាប់ផ្តើមឡើងវិញ) សេវាកម្ម៖ `foundry service start` ។

## ប្រតិបត្តិការណ៍ដំណើរការសាកល្បង (30 នាទី)

### 1. ពាក្យបញ្ជាប្រព័ន្ធ និងយុទ្ធសាស្រ្តបង្គ្រាប់ (10 នាទី)

#### ជំហាន 1.1៖ បញ្ចូលពាក្យបញ្ជាប្រកបដោយជំនាញ

បង្កើត `samples/02-rag-solutions/prompt_engineering.py`៖

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
                temperature=0.3,  # បញ្ចុះសីតុណ្ហភាពសម្រាប់ចម្លើយដែលមានស្ថេរភាពជាងមុន
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
    
    # ឧទាហរណ៍បរិបទសម្រាប់ដែនផ្សេងៗ
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
  
#### ជំហាន 1.2៖ សាកល្បងយុទ្ធសាស្រ្តបង្គ្រាប់

```powershell
# ប្រាកដថា phi-4-mini កំពុងដំណើរការ
foundry model run phi-4-mini

# បង្ហាញការប្រតិបត្តិការជាមួយ prompt engineering
python samples/02-rag-solutions/prompt_engineering.py
```
  

### 2. បញ្ចូលទិន្នន័យក្នុងរូបមាត្រជាមួយពាក្យបញ្ជា (Q&A CSV) (10 នាទី)

#### ជំហាន 2.1៖ បញ្ចូលទិន្នន័យ CSV

បង្កើត `samples/02-rag-solutions/csv_qa_system.py`៖

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
        
        # បន្ថែមស្ថិតិផ្នែកចំនួនសម្រាប់ជួរឈរចំនួន
        numeric_cols = self.data.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            stats["numeric_summary"] = self.data[numeric_cols].describe().to_dict()
        
        # បន្ថែមសេចក្ដីសង្ខេបប្រភេទ
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
        
        # បន្ថែមទិន្នន័យនមួយឧទាហរណ៍
        context_parts.append("\nSample Data:")
        for i, row in enumerate(self.summary_stats['sample_rows'][:3]):
            context_parts.append(f"Row {i+1}: {json.dumps(row, default=str)}")
        
        # បន្ថែមស្ថិតិដែលពាក់ព័ន្ធដោយផ្អែកលើមាតិកាសំណួរ
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
                temperature=0.2  # សីតុណ្ហភាពទាបសម្រាប់វិភាគទិន្នន័យជាការពិត
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
    
    # បង្កើតទិន្នន័យលក់នមួយឧទាហរណ៍
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
    
    # ធានាថាផ្លូវការបានមានស្រាប់
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    df.to_csv(csv_path, index=False)
    return csv_path

def demo_csv_qa():
    """Demonstrate CSV Q&A capabilities"""
    
    # បង្កើតមូលដ្ឋានទិន្នន័យនមួយឧទាហរណ៍
    csv_path = create_sample_dataset()
    print(f"Created sample dataset: {csv_path}")
    
    # ចាប់ផ្តើមប្រព័ន្ធសំណួរ និងចម្លើយ
    qa_system = CSVQASystem()
    
    # ចំណូលទិន្នន័យ
    if not qa_system.load_csv_data(csv_path):
        print("Failed to load CSV data")
        return
    
    print(f"\nLoaded dataset with shape: {qa_system.data.shape}")
    
    # សំណួរឧទាហរណ៍
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
  
#### ជំហាន 2.2៖ សាកល្បងប្រព័ន្ធ Q&A CSV

```powershell
# រត់ការបង្ហាញសំណួរចម្លើយ CSV
python samples/02-rag-solutions/csv_qa_system.py
```
  

### 3. គម្រោងចាប់ផ្តើម៖ ត្រូវបត់បែន 02-grounding-data (5 នាទី)

#### ជំហាន 3.1៖ ប្រព័ន្ធ RAG ឯកសារកែលម្អ

បង្កើត `samples/02-rag-solutions/document_rag.py`៖

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
        
        # វ៉ិចទ័រក្នុងការសួរ
        query_vector = self.vectorizer.transform([query])
        
        # គណនាភាពស្រដៀងគ្នា
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()
        
        # ទទួលបានឯកសារមុខមាត់-k
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # កម្រិតស្រដៀងតិចបំផុត
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
        
        # ប្រមូលឯកសារដែលពាក់ព័ន្ធ
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
    
    # បង្កើតប្រព័ន្ធ RAG
    rag_system = SimpleRAGSystem()
    
    # បន្ថែមមូលដ្ឋានចំណេះដឹងឧទាហរណ៍
    documents = create_sample_knowledge_base()
    rag_system.add_documents(documents)
    
    print(f"Loaded {len(documents)} documents into knowledge base")
    
    # សំនួរឧទាហរណ៍
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
  

### 4. បង្ហាញផ្លូវចាប់ផ្តើមផ្ទេរ CLI ទៅ Azure (5 នាទី)

#### ជំហាន 4.1៖ ទិដ្ឋភាពយុទ្ធសាស្រ្តផ្ទេរ

បង្កើត `samples/02-rag-solutions/migration_guide.py`៖

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
            # ការកំណត់តំបន់ Foundry Local
            self.client = OpenAI(
                base_url="http://localhost:5273/v1",
                api_key="not-needed"
            )
            self.default_model = "phi-4-mini"
            
        elif environment == "azure":
            # ការកំណត់តំបន់ Azure AI Foundry
            if not azure_endpoint or not azure_api_key:
                raise ValueError("Azure endpoint and API key required for Azure environment")
            
            self.client = OpenAI(
                base_url=f"{azure_endpoint}/openai/deployments",
                api_key=azure_api_key,
                default_headers={"api-version": azure_api_version}
            )
            self.default_model = "gpt-4"  # ឬឈ្មោះការបញ្ចេញ Azure របស់អ្នក
            
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
                # សម្រាប់ Foundry Local យើងពេញនិយមប្រើ CLI
                # នេះគឺជាឧទាហរណ៍ដែលបានសម្រួល
                return {
                    "success": True,
                    "models": ["phi-4-mini", "qwen2.5-0.5b", "deepseek-coder-1.3b"],
                    "environment": "local"
                }
            else:
                # សម្រាប់ Azure អ្នកអាច​សួរសំណួរ endpoint ការបញ្ចេញ
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
    
    # សារ​សាកល្បង
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
    
    # សាកល្បងជាមួយ Foundry Local
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
    
    # បង្ហាញការកំណត់តំបន់ Azure (បានបង្ហោះចេញព្រោះត្រូវការបញ្ជាក់សញ្ញាបត្រ)
    print("\n2. Azure AI Foundry Configuration:")
    print("-" * 40)
    print("""
    # ដើម្បីផ្ទេរទៅ Azure AI Foundry សូមកំណត់ដូចខាងក្រោម៖
    
    azure_client = UnifiedAIClient(
        environment="azure",
        azure_endpoint="https://your-resource.openai.azure.com",
        azure_api_key="your-api-key",
        azure_api_version="2024-08-01-preview"
    )
    
    # ការហៅ API ដូចគ្នាដំណើរការនៅពីរបរិដ្ឋានទាំងពីរ!
    azure_result = azure_client.chat_completion(
        messages=test_messages,
        max_tokens=200,
        temperature=0.7
    )
    """)
    
    # strategy ផ្ទេរ
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
    
    # ឧទាហរណ៍កំណត់តំបន់
    print("\n4. Environment-based Configuration:")
    print("-" * 40)
    print("""
    # ឯកសារ .env សម្រាប់ការអភិវឌ្ឍន៍
    AI_ENVIRONMENT=local
    FOUNDRY_LOCAL_URL=http://localhost:5273/v1
    DEFAULT_MODEL=phi-4-mini
    
    # ឯកសារ .env សម្រាប់ការផលិត
    AI_ENVIRONMENT=azure
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
    AZURE_OPENAI_API_KEY=your-api-key
    AZURE_OPENAI_API_VERSION=2024-08-01-preview
    DEFAULT_MODEL=gpt-4
    """)

if __name__ == "__main__":
    demo_migration_patterns()
```
  
#### ជំហាន 4.2៖ សាកល្បងគំរូផ្ទេរ

```powershell
# ឆ្លងកាត់ការបង្ហាញពីការផ្លាស់ទី
python samples/02-rag-solutions/migration_guide.py
```
  

## គំនិតសំខាន់ៗដែលបានគ្របដណ្តប់

### 1. បញ្ចូលពាក្យបញ្ជាប្រកបដោយជំនាញ

- **ពាក្យបញ្ជាប្រព័ន្ធ**៖ តួអង្គជំនាញនៅក្នុងដំណាលពិសេស
- **យុទ្ធសាស្រ្តបង្គ្រាប់**៖ បច្ចេកទេសបញ្ចូលបរិបទ
- **ការគ្រប់គ្រងសីតុណ្ហភាព**៖ តុល្យភាពច្នៃប្រឌិត និងភាពស្របតាមគ្នា
- **ការគ្រប់គ្រងតំណាក់កាល**៖ ការប្រើប្រាស់បរិបទបានមានប្រសិទ្ធភាព

### 2. បញ្ចូលទិន្នន័យរចនាសម្ព័ន្ធ

- **ដំណើរការ CSV**៖ បញ្ចូល Pandas ជាមួយម៉ូដែល AI
- **វិភាគស្ថិតិ**៖ សង្ខេបទិន្នន័យដោយស្វ័យប្រវត្តិ
- **បង្កើតបរិបទ**៖ ការបង្កើតបរិបទបណ្តែតផ្អែកលើសំនួរ
- **គាំទ្រប្រភេទច្រើន**៖ JSON, CSV និងទិន្នន័យក្នុងរូបមាត្រ

### 3. គំរូអនុវត្ត RAG

- **ស្វែងរកវ៉ិកទ័រ**៖ TF-IDF និងស្រដៀងខេត្ត cosine
- **ការយកឯកសារ**៖ ពិន្ទុភាពសព្វវចនានុក្រម និងចំណាត់ថ្នាក់
- **ការរួមបញ្ចូលបរិបទ**៖ សមាសធាតុឯកសារច្រើន
- **ការបង្កើតចម្លើយ**៖ ការឆ្លើយតបមូលដ្ឋាន

### 4. យុទ្ធសាស្រ្តផ្ទេរទៅពពក

- **API ផ្តាច់មុខ**៖ កូដដូចគ្នាសម្រាប់មូលដ្ឋាន និងពពក
- **ការបម្លែងបរិយាកាស**៖ ការតំរូវការតាមការកំណត់រចនា
- **ហ្វ្លូវអភិវឌ្ឍន៍**៖ មូលដ្ឋាន → Staging → ផលិតកម្ម
- **ការបង្កើនប្រសិទ្ធភាពចំណាយ**៖ អភិវឌ្ឍក្នុងស្រុក, ផលិតកម្មក្នុងពពក

## ការពិចារណាក្នុងផលិតកម្ម

### 1. ការបង្កើនការសម្រួលកំណត់

```python
# បង្កើតអុប់ធីម៉ាញសម្រាប់ RAG ផលិត
rag_config = {
    "max_context_docs": 5,
    "similarity_threshold": 0.15,
    "max_tokens": 1000,
    "temperature": 0.2,
    "chunk_size": 500,
    "chunk_overlap": 50
}
```
  
### 2. ការគ្រប់គ្រងកំហុស

```python
# ការដោះស្រាយកំហុសយ៉ាងរឹងមាំ
try:
    result = rag_system.generate_answer(question)
    if "error" in result:
        # ត្រឡប់ទៅចំណេះដឹងទូទៅ
        fallback_result = client.chat.completions.create(
            model="phi-4-mini",
            messages=[{"role": "user", "content": question}]
        )
except Exception as e:
    # កត់ត្រាកំហុស និងផ្តល់ការកាត់បន្ថយយ៉ាងទន់ភ្លន់
    logger.error(f"RAG system error: {e}")
```
  
### 3. ការហាមឃាត់ និងការត្រួតពិនិត្យក្រោយ

```python
# តាមដានការសម្តែង RAG
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```
  

## ជំហានបន្ទាប់

បន្ទាប់ពីបញ្ចប់វគ្គនេះ៖

1. **ស្វែងយល់វគ្គ 3**៖ ម៉ូដែលកូដអូបិនសូសក្នុង Foundry Local  
2. **បង្កើត RAG ផលិតកម្ម**៖ អនុវត្តជាមួយ Chainlit (គំរូ 04)  
3. **ស្វែងរកវ៉ិកទ័រជាច្រើនជាន់**៖ បញ្ចូលជាមួយ Chroma ឬ Pinecone  
4. **ផ្ទេរទៅពពក**៖ ចាក់បញ្ចូលទៅ Azure AI Foundry  
5. **វាយតម្លៃគុណភាព RAG**៖ រត់ `cd Workshop/samples;python -m session02.rag_eval_ragas` ដើម្បីវាស់វែង answer_relevancy, faithfulness, និង context_precision ដោយប្រើ ragas  

### ការកែលម្អជាជម្រើស

| ប្រភេទ | ការកែលម្អ | មូលហេតុ | ទិសដៅ |
|----------|-------------|-----------|-----------|
| ការយក | ជំនួស TF-IDF ជាមួយជាមួយហាងវ៉ិកទ័រ (FAISS / Chroma) | ការស្ដារឡើងវិញល្អ និងអាចទំហំធំ | ខ្នាតឯកសារ (500–800 តួអក្សរ), បញ្ចូល, រក្សាទុកឯកសារចំណង |
| ការតម្រៀបរួម | សេវា semantic និងតម្រងពាក្យគ្រប់គ្រាន់ | កែលម្អភាពត្រឹមត្រូវជាមួយសំណួរលេខកូដ | តម្រងដោយពាក្យគន្លឹះ បន្ទាប់មកចាត់ថ្នាក់ដោយស្រដៀងខេត្ត cosine |
| ឯកសារ Embeddings | វាយតម្លៃម៉ូដែល embedding មួយចំនួន | បង្កើនប្រសិទ្ធភាពរវាងភាពពាក់ព័ន្ធ និងល្បឿន | A/B៖ MiniLM ជាមួយ E5-small និងកម្មវិធីបំលែងសន្តិសុខក្នុងស្រុក |
| ការផ្ទុកសមតុល្យ | ផ្ទុកការបញ្ចូល និងលទ្ធផលស្វែងរក | កែរកំណត់ពេលស្នើសុំម្តងទៀតទាប | pickle / sqlite នៅលើឌីសក៏ដោយ មាន key hash |
| ការវាយតម្លៃ | ពង្រីកឃោសនារបស់ ragas | គុណភាពមានតុល្យភាពស្ថិតិ | ជ្រើសរើស 50–100 Q/A + បរិបទ; ចែកតាមប្រធានបទ |
| ម៉ែត្រិច | តាមដានពេលវេលាស្វែងរក និងបង្កើត | ពិចារណាប្រសិទ្ធភាព | ស្ទាប់បូម `retrieval_ms`, `gen_ms`, `tokens` ក្នុងការហៅមួយ |
| ការការពារ | បន្ថែម fallback hallucination | ចម្លើយមានសុវត្ថិភាព | ប្រសិន faithfulness < ជាបន្ទាន់ → ចម្លើយ៖ "បរិបទមិនគ្រប់គ្រាន់ទេ។" |
| Fallback | របៀបកាត់កបន្ទាត់មូលដ្ឋាន → ម៉ូដែល Azure | កែលម្អគុណភាពមួយចំនួន | នៅពេលមានការប៉ុនប៉ងទាប ចុះទៅកាន់ពពកតាមការប្រើបច្ចេកវិទ្យា OpenAI ដូចគ្នា |
| ដំណើរការកំណត់ | ការប្រកួតប្រជែងមានស្ថេរភាព | ការវាយតំលៃអាចធ្វើឡើងឡើងវិញបាន | កំណត់គ្រាប់ព្រួញ, `temperature=0`, បិទភាពចម្លែកនៃ sampler |
| ពិនិត្យមើល | រក្សាទុកប្រវត្តិរត់វាយតំលៃ | រកឃើញការវិលត្រឡប់ | បន្ថែម JSON ជួរ ដោយមានពេលវេលានិងការប្រែប្រួលម៉ែត្រិច |

#### ឧទាហរណ៍៖ បន្ថែមពេលវេលាស្វែងរក

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
  
#### ការវាស់វែងសមត្ថភាពជាមួយ ragas

1. រៀបចំ JSONL មានវាល៖ `question`, `answer`, `contexts`, `ground_truths` (បញ្ជី)  
2. បម្លែងទៅជា `Dataset.from_list(list_of_dicts)`  
3. រត់ `evaluate(dataset, metrics=[...])`  
4. រក្សាទុកម៉ែត្រិច (CSV/JSON) សម្រាប់វិភាគនិន្នាការ។  

#### ចាប់ផ្តើមប្រើ Vector Store (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) បានធ្វើប្រសើរឡើង
D, I = index.search(query_vec, k)
```
  
សម្រាប់ការរក្សាទុកលើឌីសក៏ដោយ ប្រើ `faiss.write_index(index, "kb.index")` ។

## មានធនធានបន្ថែម

### របៀបអះអាង  
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)  
- [គំរូ RAG នៅ Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)  
- [មគ្គុទេសក៍បញ្ចូលពាក្យបញ្ជាយ៉ាងជំនាញ](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)  
- [ឯកសារ Ragas Evaluation](https://docs.ragas.io)  

### គំរូកូដ  
- [Module08 គំរូ 04](./samples/04/README.md) - កម្មវិធី RAG ជាមួយ Chainlit  
- [ប្រព័ន្ធ Multi-Agent ជំនាញ](./samples/09/README.md) - គំរូសម្របសម្រួលភ្នាក់ងារ  

---

**រយៈពេលវគ្គ**៖ ៣០ នាទីសកម្ម + ១៥ នាទី Q&A  
**កម្រិតភិល្ជិល**៖ មធ្យម  
**តម្រូវការរួចមក**៖ បានបញ្ចប់វគ្គ ១ មានចំណេះដឹង Python មូលដ្ឋាន  

## ទស្សនាវដ្តីគំរូ & ផែនទីវគ្គ

| ស្គ្រីប / សៀវភៅកំណត់ត្រា | ស្ថានភាព | គោលបំណង | ទិន្នន័យស្នូល / ប្រភព | សំណួរឧទាហរណ៍ |
|----------------------------|----------|----------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | មូលដ្ឋានចំណេះដឹងគាំទ្រផ្ទៃក្នុងឆ្លើយសំណួរផ្នែកភាពឯកជន + ប្រសិទ្ធភាព | RAG កម្រិតតិចតួច ជាមួយ embeddings | បញ្ជី `DOCS` ក្នុងស្គ្រីប (អត្ថបទខ្លី ៥) | ហេតុអ្វីបានជាអ្នកប្រើ RAG ជាមួយ inference ក្នុងស្រុក? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | អ្នកវិភាគគុណភាពកំណត់មូលដ្ឋានពិនិត្យការស្តាប់ពិត | គណនាម៉ែត្រឲ្យ ragas ទៅលើទិន្នន័យក្លីនិកតូច | `DOCS`, `QUESTIONS`, `GROUND_TRUTH` អារេ | អត្ថិភាពអ្វីដែលមានពី inference ក្នុងស្រុក? |
| `prompt_engineering.py` (ជំនាញ) | SME ដែនកំណត់ពាក្យបញ្ជាបង្គ្រាប់សម្រាប់ជាច្រើនសេវាកម្ម | ប្រៀបធៀបឡើងវិញពាក្យបញ្ជាប្រព័ន្ធ និងផលប៉ះពាល់ token | ពាក្យបញ្ជា inline `contexts` | តើ Foundry Local រៀបចំការផ្ទុកម៉ូដែលយ៉ាងដូចម្តេច? |
| `csv_qa_system.py` | ការលក់ប្រតិបត្តិការស្វែងរកការវិភាគអន្តរកម្មលើទិន្នន័យនាំចេញ | សង្ខេប និងសួរពីការលក់តិចតួច | `sample_sales_data.csv` (ជួរដេក ១០) | ផលិតផលណាដែលមានការលក់មធ្យមខ្ពស់បំផុត? |
| `document_rag.py` | ក្រុមផលិតផលស្វែងរកប្រព័ន្ធ RAG ឯកសារសម្រាប់គេហទំព័រផ្ទៃក្នុង | យកឡើងវិញ + បញ្ជាក់ឯកសារសមស្រប | បញ្ជី `create_sample_knowledge_base()` | អត្ថប្រយោជន៍នៃ Edge AI មានអ្វីខ្លះ? |
| `migration_guide.py` | អាគីតិចត្រាស្រៀវផែនការផ្ទេរពពក | បង្ហាញភាពស្រដៀង API រវាងមូលដ្ឋាន និង Azure | ពាក្យបញ្ជាការតេស្តថេរ | សូមពន្យល់អត្ថប្រយោជន៍នៃ Edge AI ក្នុង ២–៣ វេយ្យាករណ៍។ |

### ខ្លឹមសារ Dataset  
បញ្ជីឯកសារ Inline RAG pipeline៖  
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```
  
ការវាយតម្លៃ ragas សេចក្តីពិត៖  
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```
  

### រឿងផ្ទាល់ខ្លួនស្ថានភាព  
ក្រុមវិស្វករគាំទ្រចង់បានគំរូលឿនសម្រាប់ឆ្លើយសំណួរផ្ទៃក្នុងដោយគ្មានការបង្ហាញទិន្នន័យអតិថិជនចេញក្រៅ។ បទពិសោធន៍ក្នុងវគ្គ ២ ដំណើរ​ពី RAG អនុវត្តតិចតួច (គ្មានការរក្សាទុក) ទៅ Q&A CSV រចនាសម្ព័ន្ធ → យកឯកសារជាមួយបញ្ជាក់ → វាយតម្លៃគុណភាព(របាយការណ៍ ragas) → ផែនការផ្ទេរពពកស្រេច។

### ផ្លូវបង្កើនលក្ខណៈ  
ប្រើតារាងកែលម្អជាជម្រើសដើម្បីចែកចាយ៖ ជំនួស TF-IDF ជាមួយ FAISS/Chroma, ពង្រីកកម្រិតវាយតម្លៃ (50–100 Q/A), បន្ថែម fallback ដល់ម៉ូដែលធំនៅពេល faithfulness < ជាបន្ទាន់។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំរកសុពលភាព​ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិក្នុងនេះអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាតាមដើមគួរត្រូវបានគិតថាជាភាសាជាភាសា ដែលមានឥណទានលើសម្រាប់ព័ត៌មានសំខាន់ៗ។ សម្រាប់ព័ត៌មានចាំបាច់ ការបកប្រែដោយអ្នកជំនាញមនុស្សត្រូវបានផ្ដល់អនុសាសន៍។ យើងមិនទទួលបន្ទុកចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសបង្កឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->