# సెషన్ 2: Azure AI Foundry తో AI పరిష్కారాలను నిర్మించండి

## సారాంశం

Foundry Local మరియు Azure AI Foundry ఉపయోగించి కార్యాచరణ GenAI వర్క్‌ఫ్లోలను ఎలా నిర్మించాలో అన్వేషించండి. అధునాతన ప్రాంప్ట్ ఇంజనీరింగ్ నేర్చుకోండి, నిర్మిత డేటాను సమీకరించండి, మరియు పునరుత్పాదక పైప్లైన్లతో పనులను సమన్వయపరచండి. దస్త్రం & డేటా Q&A కోసం Retrieval-Augmented Generation (RAG) పై దృష్టి ఉన్నప్పటికీ, ఈ నమూనాలు విస్తృత GenAI పరిష్కార రూపకల్పనకు సాధారణంగా వర్తిస్తాయి.

## నేర్చుకునే లక్ష్యాలు

ఈ సెషన్ ముగిసే వరకు, మీరు:

- **ప్రాంప్ట్ ఇంజనీరింగ్‌లో నైపుణ్యం పొందండి**: సమర్థవంతమైన సిస్టమ్ ప్రాంప్ట్‌లు మరియు గ్రౌండింగ్ వ్యూహాలను రూపకల్పన చేయండి
- **RAG నమూనాలను అమలు చేయండి**: వెక్టర్ శోధనతో దస్త్రం ఆధారిత Q&A వ్యవస్థలను నిర్మించండి
- **నిర్మిత డేటాను సమీకరించండి**: AI వర్క్‌ఫ్లోలలో CSV, JSON, మరియు పట్టిక డేటాతో పని చేయండి
- **ఉత్పత్తి RAG నిర్మించండి**: Chainlit తో స్కేలబుల్ RAG అనువర్తనాలను సృష్టించండి
- **స్థానిక నుండి క్లౌడ్‌కు బ్రిడ్జ్ చేయండి**: Foundry Local నుండి Azure AI Foundry కి మైగ్రేషన్ మార్గాలను అర్థం చేసుకోండి

## ముందస్తు అవసరాలు

- సెషన్ 1 పూర్తి చేసుకున్నది (Foundry Local సెటప్)
- వెక్టర్ డేటాబేసులు మరియు ఎంబెడ్డింగ్స్ యొక్క ప్రాథమిక అవగాహన
- Python ప్రోగ్రామింగ్ అనుభవం
- దస్త్రం ప్రాసెసింగ్ కాన్సెప్ట్‌లతో పరిచయం

### క్రాస్-ప్లాట్‌ఫారమ్ వాతావరణం త్వరిత ప్రారంభం (Windows & macOS)

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
  
మీ వాతావరణంలో Foundry Local macOS బైనరీలు ఇంకా అందుబాటులో లేనట్లయితే, Windows VM లేదా కంటైనర్‌లో సర్వీస్‌ను నడపండి మరియు సెట్ చేయండి:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## ధృవీకరణ: Foundry Local వాతావరణ తనిఖీ

డెమోలను ప్రారంభించే ముందు, మీ స్థానిక వాతావరణాన్ని ధృవీకరించండి:

```powershell
foundry --version              # CLI ఇన్‌స్టాల్ చేయబడిందని నిర్ధారించుకోండి
foundry status                 # సర్వీస్ స్థితి
foundry model run phi-4-mini   # బేస్‌లైన్ SLM ప్రారంభించండి
curl http://localhost:5273/v1/models  # APIని ధృవీకరించండి (పనిచేస్తున్న మోడల్‌ను జాబితా చేయాలి)
```
  
చివరి కమాండ్ విఫలమైతే, సర్వీస్‌ను ప్రారంభించండి (లేదా పునఃప్రారంభించండి): `foundry service start`.

## డెమో ప్రవాహం (30 నిమిషాలు)

### 1. సిస్టమ్ ప్రాంప్ట్‌లు మరియు గ్రౌండింగ్ వ్యూహాలు (10 నిమిషాలు)

#### దశ 1.1: అధునాతన ప్రాంప్ట్ ఇంజనీరింగ్

`samples/02-rag-solutions/prompt_engineering.py` సృష్టించండి:

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
                temperature=0.3,  # మరింత స్థిరమైన ప్రతిస్పందనల కోసం తక్కువ ఉష్ణోగ్రత
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
    
    # వివిధ డొమైన్‌ల కోసం నమూనా సందర్భాలు
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
  
#### దశ 1.2: గ్రౌండింగ్ వ్యూహాలను పరీక్షించండి

```powershell
# phi-4-mini నడుస్తున్నదని నిర్ధారించుకోండి
foundry model run phi-4-mini

# ప్రాంప్ట్ ఇంజనీరింగ్ డెమోను నడపండి
python samples/02-rag-solutions/prompt_engineering.py
```
  
### 2. ప్రాంప్ట్‌లతో పట్టిక డేటాను సమీకరించండి (CSV Q&A) (10 నిమిషాలు)

#### దశ 2.1: CSV డేటా సమీకరణ

`samples/02-rag-solutions/csv_qa_system.py` సృష్టించండి:

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
        
        # సంఖ్యా కాలమ్స్ కోసం సంఖ్యా గణాంకాలు జోడించండి
        numeric_cols = self.data.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            stats["numeric_summary"] = self.data[numeric_cols].describe().to_dict()
        
        # వర్గీకరణ సారాంశాలు జోడించండి
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
        
        # నమూనా డేటా జోడించండి
        context_parts.append("\nSample Data:")
        for i, row in enumerate(self.summary_stats['sample_rows'][:3]):
            context_parts.append(f"Row {i+1}: {json.dumps(row, default=str)}")
        
        # ప్రశ్న విషయంపై ఆధారపడి సంబంధిత గణాంకాలు జోడించండి
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
                temperature=0.2  # వాస్తవ డేటా విశ్లేషణ కోసం తక్కువ ఉష్ణోగ్రత
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
    
    # నమూనా అమ్మకాల డేటా సృష్టించండి
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
    
    # డైరెక్టరీ ఉన్నదని నిర్ధారించుకోండి
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    df.to_csv(csv_path, index=False)
    return csv_path

def demo_csv_qa():
    """Demonstrate CSV Q&A capabilities"""
    
    # నమూనా డేటాసెట్ సృష్టించండి
    csv_path = create_sample_dataset()
    print(f"Created sample dataset: {csv_path}")
    
    # ప్రశ్నలు & సమాధానాల వ్యవస్థ ప్రారంభించండి
    qa_system = CSVQASystem()
    
    # డేటా లోడ్ చేయండి
    if not qa_system.load_csv_data(csv_path):
        print("Failed to load CSV data")
        return
    
    print(f"\nLoaded dataset with shape: {qa_system.data.shape}")
    
    # ఉదాహరణ ప్రశ్నలు
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
  
#### దశ 2.2: CSV Q&A వ్యవస్థను పరీక్షించండి

```powershell
# CSV Q&A డెమోను నడపండి
python samples/02-rag-solutions/csv_qa_system.py
```
  
### 3. స్టార్టర్ ప్రాజెక్ట్: 02-grounding-data ను అనుకూలీకరించండి (5 నిమిషాలు)

#### దశ 3.1: మెరుగైన దస్త్రం RAG వ్యవస్థ

`samples/02-rag-solutions/document_rag.py` సృష్టించండి:

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
        
        # ప్రశ్నను వెక్టరైజ్ చేయండి
        query_vector = self.vectorizer.transform([query])
        
        # సాదృశ్యాలను లెక్కించండి
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()
        
        # టాప్-k డాక్యుమెంట్లను పొందండి
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # కనిష్ట సాదృశ్య పరిమితి
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
        
        # సంబంధిత డాక్యుమెంట్లను పొందండి
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
    
    # RAG సిస్టమ్ సృష్టించండి
    rag_system = SimpleRAGSystem()
    
    # నమూనా జ్ఞాన ఆధారాన్ని జోడించండి
    documents = create_sample_knowledge_base()
    rag_system.add_documents(documents)
    
    print(f"Loaded {len(documents)} documents into knowledge base")
    
    # ఉదాహరణ ప్రశ్నలు
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
  
### 4. CLI నుండి Azure కి మైగ్రేషన్ మార్గాన్ని చూపించండి (5 నిమిషాలు)

#### దశ 4.1: మైగ్రేషన్ వ్యూహం అవలోకనం

`samples/02-rag-solutions/migration_guide.py` సృష్టించండి:

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
            # ఫౌండ్రీ లోకల్ కాన్ఫిగరేషన్
            self.client = OpenAI(
                base_url="http://localhost:5273/v1",
                api_key="not-needed"
            )
            self.default_model = "phi-4-mini"
            
        elif environment == "azure":
            # అజ్యూర్ AI ఫౌండ్రీ కాన్ఫిగరేషన్
            if not azure_endpoint or not azure_api_key:
                raise ValueError("Azure endpoint and API key required for Azure environment")
            
            self.client = OpenAI(
                base_url=f"{azure_endpoint}/openai/deployments",
                api_key=azure_api_key,
                default_headers={"api-version": azure_api_version}
            )
            self.default_model = "gpt-4"  # లేదా మీ అజ్యూర్ డిప్లాయ్‌మెంట్ పేరు
            
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
                # ఫౌండ్రీ లోకల్ కోసం, సాధారణంగా CLI ఉపయోగిస్తాము
                # ఇది ఒక సరళీకృత ఉదాహరణ
                return {
                    "success": True,
                    "models": ["phi-4-mini", "qwen2.5-0.5b", "deepseek-coder-1.3b"],
                    "environment": "local"
                }
            else:
                # అజ్యూర్ కోసం, మీరు డిప్లాయ్‌మెంట్స్ ఎండ్‌పాయింట్‌ను ప్రశ్నించవచ్చు
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
    
    # పరీక్ష సందేశం
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
    
    # ఫౌండ్రీ లోకల్‌తో పరీక్షించండి
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
    
    # అజ్యూర్ కాన్ఫిగరేషన్ చూపించండి (అది క్రెడెన్షియల్స్ అవసరం కావడంతో కామెంట్ చేయబడింది)
    print("\n2. Azure AI Foundry Configuration:")
    print("-" * 40)
    print("""
    # అజ్యూర్ AI ఫౌండ్రీకి మైగ్రేట్ చేయడానికి, క్రింది విధంగా కాన్ఫిగర్ చేయండి:
    
    azure_client = UnifiedAIClient(
        environment="azure",
        azure_endpoint="https://your-resource.openai.azure.com",
        azure_api_key="your-api-key",
        azure_api_version="2024-08-01-preview"
    )
    
    # రెండు వాతావరణాల్లో కూడా అదే API కాల్స్ పనిచేస్తాయి!
    azure_result = azure_client.chat_completion(
        messages=test_messages,
        max_tokens=200,
        temperature=0.7
    )
    """)
    
    # మైగ్రేషన్ వ్యూహం
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
    
    # కాన్ఫిగరేషన్ ఉదాహరణలు
    print("\n4. Environment-based Configuration:")
    print("-" * 40)
    print("""
    # అభివృద్ధి కోసం .env ఫైల్
    AI_ENVIRONMENT=local
    FOUNDRY_LOCAL_URL=http://localhost:5273/v1
    DEFAULT_MODEL=phi-4-mini
    
    # ఉత్పత్తి కోసం .env ఫైల్
    AI_ENVIRONMENT=azure
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
    AZURE_OPENAI_API_KEY=your-api-key
    AZURE_OPENAI_API_VERSION=2024-08-01-preview
    DEFAULT_MODEL=gpt-4
    """)

if __name__ == "__main__":
    demo_migration_patterns()
```
  
#### దశ 4.2: మైగ్రేషన్ నమూనాలను పరీక్షించండి

```powershell
# మైగ్రేషన్ డెమోను నడపండి
python samples/02-rag-solutions/migration_guide.py
```
  
## కీ కాన్సెప్ట్‌లు కవర్ చేయబడ్డాయి

### 1. అధునాతన ప్రాంప్ట్ ఇంజనీరింగ్

- **సిస్టమ్ ప్రాంప్ట్‌లు**: డొమైన్-స్పెసిఫిక్ నిపుణుల వ్యక్తిత్వాలు  
- **గ్రౌండింగ్ వ్యూహాలు**: సందర్భం సమీకరణ సాంకేతికతలు  
- **తాపన నియంత్రణ**: సృజనాత్మకత మరియు స్థిరత్వం మధ్య సమతుల్యం  
- **టోకెన్ నిర్వహణ**: సమర్థవంతమైన సందర్భ వినియోగం  

### 2. నిర్మిత డేటా సమీకరణ

- **CSV ప్రాసెసింగ్**: AI మోడల్స్‌తో Pandas సమీకరణ  
- **సాంఖ్యిక విశ్లేషణ**: ఆటోమేటెడ్ డేటా సారాంశం  
- **సందర్భం సృష్టి**: ప్రశ్నల ఆధారంగా డైనమిక్ సందర్భం ఉత్పత్తి  
- **బహుళ ఫార్మాట్ మద్దతు**: JSON, CSV, మరియు పట్టిక డేటా  

### 3. RAG అమలు నమూనాలు

- **వెక్టర్ శోధన**: TF-IDF మరియు కోసైన్ సాదృశ్యం  
- **దస్త్రం రిట్రీవల్**: సంబంధిత స్కోరింగ్ మరియు ర్యాంకింగ్  
- **సందర్భం కలయిక**: బహుళ-దస్త్రం సంశ్లేషణ  
- **జవాబు ఉత్పత్తి**: గ్రౌండెడ్ ప్రతిస్పందన సృష్టి  

### 4. క్లౌడ్ మైగ్రేషన్ వ్యూహాలు

- **ఒకీకృత APIలు**: స్థానిక మరియు క్లౌడ్ కోసం ఏకైక కోడ్‌బేస్  
- **వాతావరణ సారాంశం**: కాన్ఫిగరేషన్ ఆధారిత డిప్లాయ్‌మెంట్  
- **అభివృద్ధి వర్క్‌ఫ్లో**: స్థానిక → స్టేజింగ్ → ఉత్పత్తి  
- **ఖర్చు ఆప్టిమైజేషన్**: స్థానిక అభివృద్ధి, క్లౌడ్ ఉత్పత్తి  

## ఉత్పత్తి పరిగణనలు

### 1. పనితీరు ఆప్టిమైజేషన్

```python
# ఉత్పత్తి RAG కోసం ఆప్టిమైజ్ చేయండి
rag_config = {
    "max_context_docs": 5,
    "similarity_threshold": 0.15,
    "max_tokens": 1000,
    "temperature": 0.2,
    "chunk_size": 500,
    "chunk_overlap": 50
}
```
  
### 2. లోపాల నిర్వహణ

```python
# బలమైన లోప నిర్వహణ
try:
    result = rag_system.generate_answer(question)
    if "error" in result:
        # సాధారణ జ్ఞానానికిFallback
        fallback_result = client.chat.completions.create(
            model="phi-4-mini",
            messages=[{"role": "user", "content": question}]
        )
except Exception as e:
    # లోపాన్ని లాగ్ చేసి సున్నితమైన తగ్గుదలని అందించండి
    logger.error(f"RAG system error: {e}")
```
  
### 3. మానిటరింగ్ మరియు పరిశీలన

```python
# RAG పనితీరు ట్రాక్ చేయండి
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```
  
## తదుపరి దశలు

ఈ సెషన్ పూర్తి చేసిన తర్వాత:

1. **సెషన్ 3 అన్వేషించండి**: Foundry Local లో ఓపెన్-సోర్స్ మోడల్స్  
2. **ఉత్పత్తి RAG నిర్మించండి**: Chainlit తో అమలు చేయండి (సాంపిల్ 04)  
3. **అధునాతన వెక్టర్ శోధన**: Chroma లేదా Pinecone తో సమీకరించండి  
4. **క్లౌడ్ మైగ్రేషన్**: Azure AI Foundry కి డిప్లాయ్ చేయండి  
5. **RAG నాణ్యతను అంచనా వేయండి**: `cd Workshop/samples;python -m session02.rag_eval_ragas` ను నడిపి answer_relevancy, faithfulness, మరియు context_precision ను ragas ఉపయోగించి కొలవండి

### ఐచ్ఛిక మెరుగుదలలు

| వర్గం | మెరుగుదల | కారణం | దిశ |
|----------|-------------|-----------|-----------|
| రిట్రీవల్ | TF-IDF ను వెక్టర్ స్టోర్ (FAISS / Chroma) తో మార్చండి | మెరుగైన సేమాంటిక్ రీకాల్ & స్కేలబిలిటీ | డాక్స్‌ను చంక్ చేయండి (500–800 అక్షరాలు), ఎంబెడ్ చేసి, సూచికను నిలుపుకోండి |
| హైబ్రిడ్ సూచిక | ద్విభాషా సేమాంటిక్ + కీవర్డ్ ఫిల్టరింగ్ | సంఖ్యాత్మక / కోడ్ ప్రశ్నలపై ఖచ్చితత్వం మెరుగుపరుస్తుంది | కీవర్డ్ ద్వారా ఫిల్టర్ చేసి తరువాత కోసైన్ సాదృశ్యంతో ర్యాంక్ చేయండి |
| ఎంబెడ్డింగ్స్ | బహుళ ఎంబెడ్డింగ్ మోడల్స్‌ను అంచనా వేయండి | సంబంధం మరియు వేగం మధ్య ఆప్టిమైజ్ చేయండి | A/B: MiniLM vs E5-small vs స్థానికంగా హోస్ట్ చేసిన ఎంకోడర్ |
| క్యాచింగ్ | ఎంబెడ్డింగ్స్ & రిట్రీవల్ ఫలితాలను క్యాచ్ చేయండి | పునరావృత ప్రశ్నల ఆలస్యం తగ్గిస్తుంది | సాదా ఆన్-డిస్క్ పికిల్ / sqlite హాష్ కీతో |
| అంచనా | ragas డేటాసెట్‌ను విస్తరించండి | గణాంకపరమైన అర్థవంతమైన నాణ్యత | 50–100 Q/A + సందర్భాలను క్యూయేట్ చేయండి; టాపిక్ ప్రకారం వర్గీకరించండి |
| మెట్రిక్స్ | రిట్రీవల్ & జనరేషన్ సమయాలను ట్రాక్ చేయండి | పనితీరు ప్రొఫైలింగ్ | ప్రతి కాల్‌కు `retrieval_ms`, `gen_ms`, `tokens` ను క్యాప్చర్ చేయండి |
| గార్డ్‌రెయిల్స్ | హల్యూసినేషన్ ఫాల్‌బ్యాక్ జోడించండి | భద్రతైన జవాబులు | faithfulness < సరిహద్దు అయితే → జవాబు: "అసమర్థమైన సందర్భం." |
| ఫాల్‌బ్యాక్ | స్థానిక → Azure మోడల్ కాస్కేడ్ చేయండి | హైబ్రిడ్ నాణ్యత పెంపు | తక్కువ విశ్వాసం ఉన్నప్పుడు అదే OpenAI API ద్వారా క్లౌడ్‌కు మార్గం |
| డిటర్మినిజం | స్థిరమైన పోలిక రన్స్ | పునరావృత అంచనా సెట్‌లు | సీడ్ ఫిక్స్ చేయండి, `temperature=0`, శాంప్లర్ రాండమ్నెస్‌ను నిలిపివేయండి |
| మానిటరింగ్ | అంచనా రన్ చరిత్ర నిలుపుకోండి | రిగ్రెషన్ గుర్తింపు | టైమ్‌స్టాంప్ + మెట్రిక్ డెల్టాలతో JSON లైన్స్ జోడించండి |

#### ఉదాహరణ: రిట్రీవల్ సమయాన్ని జోడించడం

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
  
#### ragas తో అంచనా స్కేలింగ్

1. `question`, `answer`, `contexts`, `ground_truths` (జాబితా) ఫీల్డ్స్‌తో JSONL సేకరించండి  
2. `Dataset.from_list(list_of_dicts)` గా మార్చండి  
3. `evaluate(dataset, metrics=[...])` నడపండి  
4. ట్రెండ్ విశ్లేషణ కోసం మెట్రిక్స్ (CSV/JSON) నిల్వ చేయండి.

#### వెక్టర్ స్టోర్ త్వరిత ప్రారంభం (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) సాధారణీకరించబడింది
D, I = index.search(query_vec, k)
```
  
డిస్క్ నిల్వ కోసం `faiss.write_index(index, "kb.index")` ఉపయోగించండి.

## అదనపు వనరులు

### డాక్యుమెంటేషన్
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)  
- [Azure AI Foundry RAG నమూనాలు](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)  
- [ప్రాంప్ట్ ఇంజనీరింగ్ గైడ్](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)  
- [Ragas అంచనా డాక్స్](https://docs.ragas.io)  

### సాంపిల్ కోడ్
- [Module08 Sample 04](./samples/04/README.md) - Chainlit RAG అనువర్తనం  
- [అధునాతన బహుళ-ఏజెంట్ వ్యవస్థ](./samples/09/README.md) - ఏజెంట్ సమన్వయ నమూనాలు  

---

**సెషన్ వ్యవధి**: 30 నిమిషాల హ్యాండ్స్-ఆన్ + 15 నిమిషాల Q&A  
**కష్టత స్థాయి**: మధ్యస్థ  
**ముందస్తు అవసరాలు**: సెషన్ 1 పూర్తి, ప్రాథమిక Python పరిజ్ఞానం  

## సాంపిల్ సన్నివేశం & వర్క్‌షాప్ మ్యాపింగ్

| వర్క్‌షాప్ స్క్రిప్ట్ / నోట్‌బుక్ | సన్నివేశం | లక్ష్యం | ప్రధాన డేటాసెట్ / మూలం | ఉదాహరణ ప్రశ్న |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | అంతర్గత మద్దతు జ్ఞాన బేస్ గోప్యత + పనితీరు FAQలకు సమాధానం | ఎంబెడ్డింగ్స్‌తో కనిష్ట మెమరీ RAG | స్క్రిప్ట్‌లో `DOCS` జాబితా (5 చిన్న భాగాలు) | స్థానిక ఇన్ఫరెన్స్‌తో RAG ఎందుకు ఉపయోగించాలి? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | నాణ్యత విశ్లేషకుడు ప్రాథమిక రిట్రీవల్ faithfulness మెట్రిక్స్ స్థాపన | చిన్న సింథటిక్ డేటాసెట్‌పై ragas మెట్రిక్స్ లెక్కించండి | `DOCS`, `QUESTIONS`, `GROUND_TRUTH` అర్రేస్ | స్థానిక ఇన్ఫరెన్స్ ఏ ప్రయోజనం ఇస్తుంది? |
| `prompt_engineering.py` (అధునాతన) | డొమైన్ SME బహుళ వేరియంట్ల కోసం గ్రౌండెడ్ ప్రాంప్ట్‌లు రూపొందించడం | డొమైన్ సిస్టమ్ ప్రాంప్ట్‌లు & టోకెన్ ప్రభావం పోల్చండి | ఇన్‌లైన్ `contexts` డిక్ట్ | Foundry Local మోడల్ క్యాచింగ్‌ను ఎలా నిర్వహిస్తుంది? |
| `csv_qa_system.py` | సేల్స్ ఆప్స్ ఎక్స్‌పోర్ట్లపై ఇంటరాక్టివ్ అనలిటిక్స్ అన్వేషణ | చిన్న సేల్స్ స్లైస్‌ను సారాంశం & ప్రశ్నించండి | ఉత్పత్తి చేసిన `sample_sales_data.csv` (10 వరుసలు) | ఏ ఉత్పత్తికి అత్యధిక సగటు అమ్మకాలు ఉన్నాయి? |
| `document_rag.py` | ఉత్పత్తి బృందం అంతర్గత వికీ కోసం దస్త్రం RAG అన్వేషణ | సంబంధిత డాక్స్‌ను రిట్రీవ్ చేసి సూచించండి | `create_sample_knowledge_base()` జాబితా | ఎడ్జ్ AI ప్రయోజనాలు ఏమిటి? |
| `migration_guide.py` | ఆర్కిటెక్ట్ క్లౌడ్ మైగ్రేషన్ ప్రణాళిక సిద్ధం చేయడం | స్థానిక→Azure API సమానత్వం చూపించండి | స్థిరమైన పరీక్ష ప్రాంప్ట్‌లు | 2–3 వాక్యాలలో ఎడ్జ్ AI ప్రయోజనాలు వివరించండి. |

### డేటాసెట్ స్నిపెట్లు  
ఇన్‌లైన్ RAG పైప్లైన్ డాక్ జాబితా:  
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```
  
Ragas అంచనా సత్య టుపుల్స్:  
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```
  
### సన్నివేశ కథనం  
సపోర్ట్ ఇంజనీరింగ్ గ్రూప్ కస్టమర్ డేటాను బాహ్యంగా వెల్లడించకుండా అంతర్గత FAQలకు వేగవంతమైన ప్రోటోటైప్ కావాలి. సెషన్ 2 ఆర్టిఫాక్ట్స్ కనిష్ట తాత్కాలిక RAG (పర్సిస్టెన్స్ లేకుండా) → నిర్మిత CSV Q&A → దస్త్రం రిట్రీవల్‌తో సూచన → లక్ష్య నాణ్యత అంచనా (ragas) → Azure స్టేజింగ్‌కు సిద్ధమైన మైగ్రేషన్ వ్యూహం వరకు అభివృద్ధి చెందుతాయి.

### విస్తరణ మార్గాలు  
ఐచ్ఛిక మెరుగుదలల పట్టికను ఉపయోగించి అభివృద్ధి చేయండి: TF-IDF ను FAISS/Chroma తో మార్చండి, అంచనా కార్పస్‌ను (50–100 Q/A) పెంచండి, faithfulness < సరిహద్దు ఉన్నప్పుడు పెద్ద మోడల్‌కు ఫాల్‌బ్యాక్ ఎస్కలేషన్ జోడించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->