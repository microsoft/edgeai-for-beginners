# സെഷൻ 2: Azure AI Foundry ഉപയോഗിച്ച് AI പരിഹാരങ്ങൾ നിർമ്മിക്കുക

## വിവരണം

Foundry Local, Azure AI Foundry എന്നിവ ഉപയോഗിച്ച് പ്രവർത്തനക്ഷമമായ GenAI പ്രവാഹങ്ങൾ എങ്ങനെ നിർമ്മിക്കാമെന്ന് പഠിക്കുക. ഉയർന്ന_prompt എഞ്ചിനീയറിംഗ്, ഘടനാപരമായ ഡാറ്റ ഇൻറഗ്രേഷൻ, പുനരുപയോഗയോഗ്യമായ പൈപ്പ്ലൈനുകളിൽ ടാസ്കുകൾ ഓർക്കസ്ട്രേറ്റ് ചെയ്യൽ എന്നിവ പഠിക്കാം. രേഖകളും ഡാറ്റയും സംബന്ധിച്ച Q&A എന്നിവയ്ക്കായുള്ള Retrieval-Augmented Generation (RAG) ആണ് ശ്രദ്ധയുടെ കേന്ദ്രീകരണം, എന്നാൽ ഈ മാതൃകകൾ വിശാലമായ GenAI പരിഹാര രൂപകല്പനയ്ക്ക് സാധുവാണ്.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ സെഷൻ അവസാനിക്കുമ്പോൾ നിങ്ങൾക്ക്:

- **പ്രോംപ്റ്റ് എഞ്ചിനീയറിംഗ് മികവറിക്കുക**: ഫലപ്രദമായ സിസ്റ്റം പ്രോംപ്റ്റുകളും ഗ്രൗണ്ടിങ് നയങ്ങളും രൂപകല്‍പ്പന ചെയ്യുക
- **RAG മാതൃകകൾ നടപ്പിലാക്കുക**: വെക്റ്റർ സെർച്ച് ഉപയോഗിച്ച് രേഖ അടിസ്ഥാനമായ Q&A സിസ്റ്റങ്ങൾ നിർമ്മിക്കുക
- **ഘടനാപരമായ ഡാറ്റ കൂട്ടിച്ചേർക്കുക**: AI പ്രവാഹങ്ങളിൽ CSV, JSON, ടാബുലാർ ഡാറ്റ ഉപയോഗിക്കുക
- **പ്രൊഡക്ഷൻ RAG തയ്യാറാക്കുക**: Chainlit ഉപയോഗിച്ച് സ്കേലബിൾ RAG അപ്ലിക്കേഷനുകൾ സൃഷ്‌ടിക്കുക
- **ലോകൽ നിന്നും ക്ലൗഡിലേക്ക് പാലം**: Foundry Local മുതൽ Azure AI Foundry വരെ മൈഗ്രേഷൻ മാർഗങ്ങൾ മനസിലാക്കുക

## മുൻകൂട്ടി ആവശ്യമുള്ളത്

- സെഷൻ 1 (Foundry Local സെറ്റപ്) പൂർത്തിയാക്കിയതു
- വെക്റ്റർ ഡാറ്റാബേസുകളും embeddings-ഉം അടിസ്ഥാനമായി അറിയാം
- പൈത്തൺ പ്രോഗ്രാമിങ്ങ് പരിചയം
- രേഖ പ്രോസസ്സിംഗ് ആശയങ്ങളിൽ പരിചയം
 
### ക്രോസ്സ്-പ്ലാറ്റ്ഫോം പരിസ്ഥിതി ദ്രുത ആരംഭം (Windows & macOS)

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

Foundry Local macOS ബൈനറികൾ നിങ്ങളുടെ എന്നിവിടത്തിൽ നിലവിൽ ഇല്ലെങ്കിൽ, Windows VM അല്ലെങ്കിൽ കണ്ടെയ്നറിൽ സർവീസ് ഓടിച്ച് താഴെ സജ്ജമാക്കുക:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## സാധുത ഉറപ്പ് ചെയ്യൽ: Foundry Local പരിസ്ഥിതി പരിശോധന

ഡെമോകൾ തുടങ്ങുന്നതിനു മുൻപ്, നിങ്ങളുടെ ലോക്കൽ പരിസ്ഥിതിയെ സാധുത ഉറപ്പാക്കുക:

```powershell
foundry --version              # CLI ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പ് വരുത്തുക
foundry status                 # സേവന സ്ഥിതിവിവരം
foundry model run phi-4-mini   # അടിസ്ഥാന SLM ആരംഭിക്കുക
curl http://localhost:5273/v1/models  # API പരിശോധന (ഓടുന്ന മോഡൽ ലിസ്റ്റ് കാണിക്കണം)
```

അവസാന കമാൻഡ് പരാജയപ്പെടുകയാണെങ്കിൽ, സർവീസ് ആരംഭിക്കുക (അല്ലെങ്കിൽ പുനരാരംഭിക്കുക): `foundry service start`.

## ഡെമോ പ്രവാഹം (30 മിനിറ്റ്)

### 1. സിസ്റ്റം പ്രോംപ്റ്റുകളും ഗ്രൗണ്ടിങ് നയങ്ങളും (10 മിനിറ്റ്)

#### ഘട്ടം 1.1: ഉയർന്ന പ്രോംപ്റ്റ് എഞ്ചിനീയറിംഗ്

`samples/02-rag-solutions/prompt_engineering.py` ഫയൽ സൃഷ്‌ടിക്കുക:

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
                temperature=0.3,  # കൂടുതൽ സ്ഥിരമായ പ്രതികരണങ്ങൾക്ക് താപനില കുറയ്ക്കുക
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
    
    # വ്യത്യസ്ത മേഖലകളിലേക്കുള്ള സാമ്പിള്‍ സന്ദർഭങ്ങൾ
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

#### ഘട്ടം 1.2: ഗ്രൗണ്ടിങ് നയങ്ങൾ പരീക്ഷിക്കുക

```powershell
# phi-4-mini പ്രവർത്തനത്തിലാണെന്ന് ഉറപ്പാക്കുക
foundry model run phi-4-mini

# പ്രോംപ്റ്റ് എഞ്ചിനീയറിംഗ് ഡെമോ ഓടിക്കുക
python samples/02-rag-solutions/prompt_engineering.py
```

### 2. പ്രോംപ്റ്റുകളോടുകൂടിയ ടാബുലാർ ഡാറ്റ ഇൻറഗ്രേഷൻ (CSV Q&A) (10 മിനിറ്റ്)

#### ഘട്ടം 2.1: CSV ഡാറ്റ ഇൻറഗ്രേഷൻ

`samples/02-rag-solutions/csv_qa_system.py` സൃഷ്‌ടിക്കുക:

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
        
        # സംഖ്യാത്മക കോളങ്ങളുടെ ന്യუმറിക്കൽ സ്റ്റാറ്റിസ്റ്റിക്സ് ചേർക്കുക
        numeric_cols = self.data.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            stats["numeric_summary"] = self.data[numeric_cols].describe().to_dict()
        
        # വർഗ്ഗികൃത സമ്പൂർണങ്ങൾ ചേർക്കുക
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
        
        # സാമ്പിൾ ഡാറ്റ ചേർക്കുക
        context_parts.append("\nSample Data:")
        for i, row in enumerate(self.summary_stats['sample_rows'][:3]):
            context_parts.append(f"Row {i+1}: {json.dumps(row, default=str)}")
        
        # ചോദ്യ ഉള്ളടക്കത്തെ അടിസ്ഥാനമാക്കി ബന്ധപ്പെട്ട സ്റ്റാറ്റിസ്റ്റിക്സ് ചേർക്കുക
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
                temperature=0.2  # ഫാക്ട്വൽ ഡാറ്റ വിശകലനത്തിന് കുറഞ്ഞ താപനില
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
    
    # സാമ്പിൾ വിൽപ്പന ഡാറ്റ സൃഷ്ടിക്കുക
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
    
    # ഡയറക്ടറി നിലവിലുണ്ടെന്ന് ഉറപ്പാക്കുക
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    df.to_csv(csv_path, index=False)
    return csv_path

def demo_csv_qa():
    """Demonstrate CSV Q&A capabilities"""
    
    # സാമ്പിൾ ഡാറ്റാസെറ്റ് സൃഷ്ടിക്കുക
    csv_path = create_sample_dataset()
    print(f"Created sample dataset: {csv_path}")
    
    # Q&A സിസ്റ്റം ആരംഭിക്കുക
    qa_system = CSVQASystem()
    
    # ഡാറ്റ ലോഡ് ചെയ്യുക
    if not qa_system.load_csv_data(csv_path):
        print("Failed to load CSV data")
        return
    
    print(f"\nLoaded dataset with shape: {qa_system.data.shape}")
    
    # ഉദാഹരണ ചോദ്യങ്ങൾ
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

#### ഘട്ടം 2.2: CSV Q&A സിസ്റ്റം പരീക്ഷിക്കുക

```powershell
# CSV Q&A ഡെമോ പ്രവർത്തിപ്പിക്കുക
python samples/02-rag-solutions/csv_qa_system.py
```

### 3. സ്റ്റാർട്ടർ പ്രോജക്ട്: 02-grounding-data ആഡാപ്റ്റ് ചെയ്യുക (5 മിനിറ്റ്)

#### ഘട്ടം 3.1: മെച്ചപ്പെടുത്തിയ രേഖ RAG സിസ്റ്റം

`samples/02-rag-solutions/document_rag.py` സൃഷ്‌ടിക്കുക:

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
        
        # ചോദ്യത്തെ വെക്ടറൈസ് ചെയ്യുക
        query_vector = self.vectorizer.transform([query])
        
        # സമാനതകൾ ഗണിക്കുക
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()
        
        # ടോപ്പ്-കെ ഡോക്യുമെന്റുകൾ ലഭിക്കുക
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # കുറഞ്ഞ സമാനതാ പരിധി
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
        
        # ബന്ധപ്പെട്ട ഡോക്യുമെന്റുകൾ തിരയുക
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
    
    # RAG സിസ്റ്റം സൃഷ്ടിക്കുക
    rag_system = SimpleRAGSystem()
    
    # സാമ്പിൾ നോളജ് ബേസ് ചേർക്കുക
    documents = create_sample_knowledge_base()
    rag_system.add_documents(documents)
    
    print(f"Loaded {len(documents)} documents into knowledge base")
    
    # ഉദാഹരണ ചോദ്യങ്ങൾ
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

### 4. CLI-ൽ നിന്നുള്ള Azure മൈഗ്രേഷൻ പാത കാണിക്കുക (5 മിനിറ്റ്)

#### ഘട്ടം 4.1: മൈഗ്രേഷൻ നയ അവലോകനം

`samples/02-rag-solutions/migration_guide.py` സൃഷ്‌ടിക്കുക:

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
            # ഫൗണ്ട്രി ലോക്കൽ കോൺഫിഗറേഷൻ
            self.client = OpenAI(
                base_url="http://localhost:5273/v1",
                api_key="not-needed"
            )
            self.default_model = "phi-4-mini"
            
        elif environment == "azure":
            # അസ്യൂർ എഐ ഫൗണ്ട്രി കോൺഫിഗറേഷൻ
            if not azure_endpoint or not azure_api_key:
                raise ValueError("Azure endpoint and API key required for Azure environment")
            
            self.client = OpenAI(
                base_url=f"{azure_endpoint}/openai/deployments",
                api_key=azure_api_key,
                default_headers={"api-version": azure_api_version}
            )
            self.default_model = "gpt-4"  # അല്ലെങ്കിൽ നിങ്ങളുടെ അസ്യൂർ ഡിപ്ലോയ്മെന്റ് നാമം
            
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
                # ഫൗണ്ട്രി ലോക്കലിനായി, സാധാരണയായി നാം CLI ഉപയോഗിക്കും
                # ഇത് ഒരു ലളിതമായ ഉദാഹരണമാണ്
                return {
                    "success": True,
                    "models": ["phi-4-mini", "qwen2.5-0.5b", "deepseek-coder-1.3b"],
                    "environment": "local"
                }
            else:
                # അസ്യൂറിന്, നിങ്ങൾ ഡിപ്ലോയ്മെന്റ്‌സ് എൻഡ്‌പോയിന്റ് ആരെത്തിക്കാവുന്നതാണ്
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
    
    # ടെസ്റ്റ് സന്ദേശം
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
    
    # ഫൗണ്ട്രി ലോക്കലുമായി ടെസ്റ്റ്
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
    
    # അസ്യൂർ കോൺഫിഗറേഷൻ കാണിക്കുക (ക്രെഡൻഷ്യലുകൾ ആവശ്യമായതിനാൽ കമന്റ് ചെയ്തിരിക്കുന്നു)
    print("\n2. Azure AI Foundry Configuration:")
    print("-" * 40)
    print("""
    # അസ്യൂർ എഐ ഫൗണ്ട്രിയിലേക്ക് മൈഗ്രേറ്റ് ചെയ്യാൻ, ഇങ്ങനെ കോൺഫിഗർ ചെയ്യുക:
    
    azure_client = UnifiedAIClient(
        environment="azure",
        azure_endpoint="https://your-resource.openai.azure.com",
        azure_api_key="your-api-key",
        azure_api_version="2024-08-01-preview"
    )
    
    # ഒരേ API കോളുകൾ രണ്ട് محیطങ്ങളിലും പ്രവർത്തിക്കുന്നു!
    azure_result = azure_client.chat_completion(
        messages=test_messages,
        max_tokens=200,
        temperature=0.7
    )
    """)
    
    # മൈഗ്രേഷൻ തന്ത്രം
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
    
    # കോൺഫിഗറേഷൻ ഉദാഹരണങ്ങൾ
    print("\n4. Environment-based Configuration:")
    print("-" * 40)
    print("""
    # ഡെവലപ്പ്മെന്റിന് .env ഫയൽ
    AI_ENVIRONMENT=local
    FOUNDRY_LOCAL_URL=http://localhost:5273/v1
    DEFAULT_MODEL=phi-4-mini
    
    # പ്രൊഡക്ഷനുമായി .env ഫയൽ
    AI_ENVIRONMENT=azure
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
    AZURE_OPENAI_API_KEY=your-api-key
    AZURE_OPENAI_API_VERSION=2024-08-01-preview
    DEFAULT_MODEL=gpt-4
    """)

if __name__ == "__main__":
    demo_migration_patterns()
```

#### ഘട്ടം 4.2: മൈഗ്രേഷൻ മാതൃകകൾ പരീക്ഷിക്കുക

```powershell
# മൈഗ്രേഷൻ ഡെമോ പ്രവർത്തിപ്പിക്കുക
python samples/02-rag-solutions/migration_guide.py
```

## പ്രധാന ആശയങ്ങൾ

### 1. ഉയർന്ന പ്രോംപ്റ്റ് എഞ്ചിനീയറിംഗ്

- **സിസ്റ്റം പ്രോംപ്റ്റുകൾ**: മേഖലയുമായി ബന്ധപ്പെട്ട വിദഗ്ധ പേഴ്സണാസുകൾ
- **ഗ്രൗണ്ടിങ് നയങ്ങൾ**: പശ്ചാത്തല സംയോജനം സാങ്കേതിക വിദ്യകൾ
- **ടെംപറേച്ചർ നിയന്ത്രണം**: സൃഷ്ടിപരത്വവും സ്ഥിരതയും തമ്മിലുള്ള തുലനം
- **ടോക്കൺ മാനേജ്മെന്റ്**: കാര്യക്ഷമമായ കോൺടക്സ്റ്റ് ഉപയോഗം

### 2. ഘടനാപരമായ ഡാറ്റ ഇൻറഗ്രേഷൻ

- **CSV പ്രോസസ്സിംഗ്**: Pandas-ഉം AI മോഡലുകളുമായുള്ള ഇൻറഗ്രേഷൻ
- **സാങ്കേതിക വിശകലനം**: ഓട്ടോമേറ്റഡ് ഡാറ്റ സംഗ്രഹണം
- **കോൺടക്സ്റ്റ് സൃഷ്ടിക്കൽ**: ചോദനകൾ അടിസ്ഥാനമാക്കി ഡൈനാമിക് കോൺടക്സ്റ്റ് ജനറേഷൻ
- **മൾട്ടി-ഫോർമാറ്റ് പിന്തുണ**: JSON, CSV, ടാബുലാർ ഡാറ്റ

### 3. RAG നടപ്പാക്കൽ മാതൃകകൾ

- **വെക്റ്റർ സെർച്ച്**: TF-IDF,കോസൈൻ സമാനത
- **ഡോക്യുമെന്റ് റിട്ട്രീവൽ**: പ്രസക്തി സ്കോറിങ്, റാങ്കിംഗ്
- **കോൺടക്സ്റ്റ് സംയോജനം**: മൾട്ടി-ഡോക്യൂമെന്റ് സംശ്ലേഷണം
- **ഉത്തരം വികസനം**: ഗ്രൗണ്ടഡ് പ്രതികരണം സൃഷ്‌ടിക്കൽ

### 4. ക്ലൗഡ് മൈഗ്രേഷൻ നയങ്ങൾ

- **ഏകീകൃത APIകൾ**: ലോക്കലിനും ക്ലൗഡിനും ഒറ്റ കോഡ്ബേസ്
- **പരിസ്ഥിതി ആബ്സ്ട്രാക്‌ഷൻ**: കോൺഫിഗറേഷൻ-ആധാരിത ഡിപ്ലോയ്മെന്റ്
- **ഡെവലപ്പ്മെന്റ് പ്രവാഹം**: ലോക്കൽ → സ്റ്റേജിങ് → പ്രൊഡക്ഷൻ
- **ചെലവ് ഒപ്റ്റിമൈസേഷൻ**: ലോക്കൽ ഡെവലപ്പ്മെന്റ്, ക്ലൗഡ് പ്രൊഡക്ഷൻ

## പ്രൊഡക്ഷൻ പരിഗണനകൾ

### 1. പെർഫോർമൻസ് ഒപ്റ്റിമൈസേഷൻ

```python
# ഉൽപ്പാദന RAG ഇടത്തരം ਕਰਨായി മെച്ചപ്പെടുത്തുക
rag_config = {
    "max_context_docs": 5,
    "similarity_threshold": 0.15,
    "max_tokens": 1000,
    "temperature": 0.2,
    "chunk_size": 500,
    "chunk_overlap": 50
}
```

### 2. പിശക് കൈകാര്യം ചെയ്യൽ

```python
# ദൃഢമായ പിഴവു കൈകാര്യം
try:
    result = rag_system.generate_answer(question)
    if "error" in result:
        # പൊതുവായ അറിവിലേക്ക് പിന്മാറ്റം
        fallback_result = client.chat.completions.create(
            model="phi-4-mini",
            messages=[{"role": "user", "content": question}]
        )
except Exception as e:
    # പിഴവ് രേഖപ്പെടുത്തുകയും സൗമ്യമായ പിഴവ് കുറവാക്കലും നൽകുകയും ചെയ്യുക
    logger.error(f"RAG system error: {e}")
```

### 3. മോണിറ്ററിങ്ങും ഒബ്സർവബിലിറ്റിയും

```python
# RAG പ്രകടനം ട്രാക്ക് ചെയ്യുക
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```

## തുടർന്ന് എടുത്തു പോകേണ്ടത്

ഈ സെഷൻ പൂർത്തിയാക്കിയ ശേഷം:

1. **സെഷൻ 3 പരിശോധിക്കുക**: Foundry Local ൽ ഓപ്പൺ-സോഴ്സ് മോഡലുകൾ
2. **പ്രൊഡക്ഷൻ RAG നിർമ്മിക്കുക**: Chainlit ഉപയോഗിച്ച് നടപ്പിലാക്കുക (സാമ്പിൾ 04)
3. **ആധുനിക വെക്റ്റർ സെർച്ച്**: Chroma അല്ലെങ്കിൽ Pinecone സംയോജിപ്പിക്കുക
4. **ക്ലൗഡ് മൈഗ്രേഷൻ**: Azure AI Foundry യിലേക്ക് ഡിപ്ലോയ് ചെയ്യുക
5. **RAG ഗുണമേന്മ വിലയിരുത്തുക**: `cd Workshop/samples;python -m session02.rag_eval_ragas` റൺ ചെയ്ത് answer_relevancy, faithfulness, context_precision ragas ഉപയോഗിച്ച് അളവുകൾ നേടുക

### ഐച്ഛിക മെച്ചപ്പെടുത്തലുകൾ

| വിഭാഗം | മെച്ചപ്പെടുത്തൽ | കാരണം | ദിശ |
|----------|-------------|-----------|-----------|
| റിട്ട്രീവൽ | TF-IDF നെ വെക്റ്റർ സ്റ്റോർ (FAISS / Chroma) ഉപയോഗിച്ച് മാറ്റുക | മെച്ചപ്പെട്ട സാംമെന്റിക് റിക്കാൾ & സ്കേലബിലിറ്റി | ഡോക്യുമെന്റുകൾ (500–800 അക്ഷരങ്ങൾ), എൻബെഡ് ചെയ്ത് ഇൻഡക്സ്മെന്റ് സ്ഥിരപ്പെടുത്തുക |
| ഹൈബ്രിഡ് ഇൻഡക്സം | ഇരട്ട സാംമെന്റിക് + കീവർഡ് ഫിൽറ്ററിംഗ് | സംഖ്യാത്മക/കോഡ് ചോദനകളിൽ മികച്ച കൃത്യത | ആദ്യം കീവർഡിൽ ഫിൽറ്റർ ചെയ്ത് ശേഷം കോസൈൻ സമാനത അനുസരിച്ച് റാങ്ക് ചെയ്യുക |
| എൻബെഡിങ്ങുകൾ | വിവിധ എൻബെഡിങ്ങ് മോഡലുകൾ വിലയിരുത്തുക | പ്രസക്തിയും വേഗവും ഒപ്റ്റിമൈസ് ചെയ്യുക | A/B: MiniLM, E5-small, ലോക്കൽ എൻകോടർ |
| ക്യാഷിംഗ് | എൻബെഡിങ്ങുകൾ & റിട്ട്രീവൽ ഫലങ്ങൾ ക്യാഷ് ചെയ്യുക | ആവർത്തിച്ച ചോദനകളുടെ വൈകല്യം കുറക്കുക | ലളിതമായ ഓൺ-ഡിസ്‌ക് പിക്കിൽ / SQLite ഹാഷ് കീയിൽ |
| വിലയിരുത്തൽ | ragas ഡാറ്റാസെറ്റ് വിപുലീകരിക്കുക | സാങ്കേതികമായി അർത്ഥവത്തായ ഗുണമേന്മ | 50–100 Q/A + കോൺടക്സ്റ്റുകൾ ക്രമീകരിക്കുക; വിഷയം അടിസ്ഥാനമാക്കി വിഭജിക്കുക |
| മീട്രിക്കുകൾ | റിട്ട്രീവൽ & ജനറേഷൻ സമയങ്ങൾ ട്രാക്ക് ചെയ്യുക | പെർഫോർമൻസ് പ്രൊഫൈലിങ് | ഓരോ കോൾക്കും `retrieval_ms`, `gen_ms`, `tokens` പിടിക്കുക |
| ഗാർഡ്‌റെയിൽസ് | ഹാലൂസിൻ ഫാൾബാക്ക് ചേർക്കുക | സുരക്ഷിത ഉത്തരം | വിശ്വാസ്യത<threshold ആയാൽ → ഉത്തരം: "അപര്യാപ്തമായ കോൺടക്സ്റ്റ്." |
| ഫാൾബാക്ക് | ലോക്കൽ → Azure മോഡൽ കASCADE ചെയ്യുക | ഹൈബ്രിഡ് ഗുണമേന്മ കൂട്ടുക | കുറഞ്ഞ ആത്മവിശ്വാസം ഉണ്ടെങ്കിൽ ഒറ്റ OpenAI API വഴി ക്ലൗഡ് വഴിയേ മടങ്ങുക |
| നിർണ്ണായകത | സ്ഥിരതയുള്ള താരതമ്യ റൺസ് | പുനരാവൃത മൂല്യനിർണയം | സീഡ് ഫിക്സ് ചെയ്യുക, `temperature=0`, സാമ്പിൾ ചെയ്യൽ റാൻഡംനസ് അപ്രാപ്തമാക്കുക |
| മോണിറ്ററിങ്ങ് | മൂല്യനിർണയ റൺ ചരിത്രം സ്ഥിരപ്പെടുത്തുക | റെഗ്രഷൻ കണ്ടെത്തൽ | JSON ലൈൻസും ടൈംസ്റ്റാമ്പും + മീറ്റ്‌റിക് വ്യത്യാസങ്ങൾ ചേർക്കുക |

#### ഉദാഹരണം: റിട്ട്രീവൽ ടൈമിംഗ് ചേർക്കൽ

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

#### ragas ഉപയോഗിച്ച് സ്കേലിംഗ് വിലയിരുത്തൽ

1. JSONL സൂത്രവാക്യങ്ങളോടെ സൃഷ്ടിക്കുക: `question`, `answer`, `contexts`, `ground_truths` (ലിസ്റ്റ്)
2. `Dataset.from_list(list_of_dicts)` ആയി മാറ്റുക
3. `evaluate(dataset, metrics=[...])` റൺ ചെയ്യുക
4. ട്രെൻഡ് വിശകലനത്തിനായി മീട്രിക്സ് (CSV/JSON) സൂക്ഷിക്കുക

#### വെക്റ്റർ സ്റ്റോർ ദ്രുത ആരംഭം (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) സാധാരണമാക്കിയിരിക്കുന്നു
D, I = index.search(query_vec, k)
```

ഡിസ്ക് സ്ഥിരതയ്ക്കായുള്ള `faiss.write_index(index, "kb.index")` ഉപയോഗിക്കുക.

## അധിക വിഭവങ്ങൾ

### ഡോക്യുമെന്റേഷൻ
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG Patterns](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [Prompt Engineering Guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Ragas Evaluation Docs](https://docs.ragas.io)

### സാമ്പിൾ കോഡ്
- [Module08 Sample 04](./samples/04/README.md) - Chainlit RAG അപ്ലിക്കേഷൻ
- [ഉയർന്ന മൾട്ടി-ഏജന്റ് സിസ്റ്റം](./samples/09/README.md) - ഏജന്റ് കോഓർഡിനേഷൻ മാതൃകകൾ

---

**സെഷൻ ദൈർഘ്യം**: 30 മിനിറ്റ് ജനറൽ + 15 മിനിറ്റ് Q&A
**പ്രയാസത്തിന്റെ തരം**: മധ്യസ്ഥരം
**മുൻകൂട്ടി ആവശ്യമുള്ളത്**: സെഷൻ 1 പൂർത്തിയായിട്ടുണ്ട്, അടിസ്ഥാന പൈത്തൺ അറിവ്

## സാമ്പിൾ ദൃശ്യവും വർക്‌ഷോപ്പ് മാപ്പിംഗും

| വർക്‌ഷോപ്പ് സ്ക്രിപ്റ്റ് / നോട്ട്‌ബുക്ക് | ദൃശ്യ സാന്ദർഭം | ലക്ഷ്യം | മുഖ്യ ഡാറ്റാസെറ്റ് / ഉറവിടം | ഉദാഹരണ ചോദ്യം |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | ആന്തരിക പിന്തുണാ അറിവ് ബേസിൽ പ്രൈവസി + പെർഫോർമൻസ് FAQ-കൾക്ക് ഉത്തരം നൽകൽ | ചെറിയ-അന്തരീക്ഷ RAG embeddings ഉപയോഗിച്ച് | സ്ക്രിപ്റ്റിലേ DOCS ലിസ്റ്റ് (5 ചെറുചുരുണ്ട ഭാഗങ്ങൾ) | ലോക്കൽ ഇൻഫറൻസ് ഉപയോഗിച്ച് RAG എന്തിന്? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | ഗുണനിലവാര വിശകലകൻ അടിസ്ഥാന രീറ്റ്രീവൽ വിശ്വാസ്യത മെട്രിക്‌സ് സ്ഥാപിക്കൽ | ചെറിയ സിന്ധെറ്റിക് ഡാറ്റാസെറ്റിലേ ragas മെട്രിക്‌സ് കണക്കുകൽ | DOCS, QUESTIONS, GROUND_TRUTH അരെയ്‌സ് | ലോക്കൽ ഇൻഫറൻസ് നൽകുന്ന നേട്ടം എന്താണ്? |
| `prompt_engineering.py` (ഉയർന്ന) | വ്യത്യസ്ത മേഖലയിലെ SME-കൾ ഗ്രൗണ്ടഡ് പ്രോംപ്റ്റുകൾ തയ്യാറാക്കുന്നു | മേഖലാ സിസ്റ്റം പ്രോംപ്റ്റുകളും ടോക്കൺ പ്രഭാവവും താരതമ്യം ചെയ്യുക | ആഭ്യന്തര `contexts` ഡിക്‌ഷണറി | Foundry Local മോഡൽ ക്യാഷിംഗ് എങ്ങനെ കൈകാര്യം ചെയ്യുന്നു? |
| `csv_qa_system.py` | സെയിൽസ് ഓപ്പറേഷൻസ് കയറ്റുമതികൾക്കായുള്ള ഇന്ററാക്ടീവ് അനലിറ്റിക്സ് പരീക്ഷിക്കുന്നു | ചെറിയ സെയിൽസ് ഭാഗം സംഗ്രഹിച്ചു ചോദിക്കുക | സൃഷ്ടിച്ച `sample_sales_data.csv` (10 വരികൾ) | എവിടെ ഉൽപ്പന്നം ഏറ്റവും ഉയർന്ന ശരാശരി വിൽപ്പനാ തുക കാണിക്കുന്നു? |
| `document_rag.py` | ഉൽപ്പന്ന സംഘം ആന്തരിക വിക്കിയുടെ ആത്മാർഥ RAG പരിശോധിക്കുന്നു | പ്രസക്ത ഡോക്യൂമെന്റുകൾ റിട്ട്രീവ് ചെയ്ത് ഉദ്ധരിച്ചു കാണിക്കുക | `create_sample_knowledge_base()` ലിസ്റ്റ് | എഡ്ജ് AI ന്റെ ഗുണങ്ങൾ എന്തൊക്കെയാണ്? |
| `migration_guide.py` | ആർക്കിടെക്റ്റ് ക്ലൗഡ് മൈഗ്രേഷൻ പദ്ധതി തയ്യാറാക്കുന്നു | ലോക്കൽ→Azure API സാധുത തെളിയിക്കുക | സ്റ്റാറ്റിക് ടെസ്റ്റ് പ്രോംപ്റ്റുകൾ | 2–3 വാക്യങ്ങളിൽ എഡ്ജ് AI ന്റെ ഗുണങ്ങൾ വിശദീകരിക്കുക. |

### ഡാറ്റാസെറ്റ് സ്നിപ്പറ്റുകൾ
അഭ്യന്തര RAG പൈപ്പ്ലൈൻ ഡോക്ക് ലിസ്റ്റ്:
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```

Ragas മൂല്യനിർണയ ട്രൂത്ത് ട്യൂപ്പിൾസ്:
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```

### ദൃശ്യ സാന്ദർഭ കഥ
പിന്തുണ എഞ്ചിനീയറിംഗ് സംഘം, ഉപഭോക്തൃ ഡാറ്റ പുറത്ത് വെക്കാതെ ആന്തരിക FAQ-കൾക്ക് വേഗത്തിൽ പ്രോട്ടോടൈപ്പ് ഉത്തരം നൽകാൻ ആഗ്രഹിക്കുന്നു. സെഷൻ 2 ആർട്ടിഫാക്റ്റുകൾ ഏറ്റവും ലഘു എഫെമറൽ RAG (സ്ഥിരതയില്ലാതെ) → ഘടനാപരമായ CSV Q&A → രേഖ റിട്ട്രീവൽ ഉദ്ധരണിയോടുകൂടി → ലക്ഷ്യമിടുന്ന ഗുണമേന്മ വിലയിരുത്തൽ (ragas) → Azure സ്റ്റേജിങ്ങിനുള്ള മൈഗ്രേഷൻ തന്ത്രം എന്നിലേക്കുള്ള പുരോഗതി ആണ്.

### വിപുലീകരണ മാർഗ്ഗങ്ങൾ
ഐച്ഛിക മെച്ചപ്പെടുത്തലുകളുടെ പട്ടിക ഉപയോഗിച്ച് വികസിപ്പിക്കുക: TF-IDF മൊത്തം FAISS/Chroma നൽകി മാറ്റുക, വിലയിരുത്തൽ കോർപ്പസ് (50–100 Q/A) കൂടുതൽ വലുതാക്കുക, വിശ്വാസ്യത<threshold ആയാൽ വലിയ മോഡലിലേക്ക് ഫാൾബാക്ക് ഉയർത്തുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->