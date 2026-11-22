# सत्र 2: Azure AI Foundry सह AI सोल्यूशन्स तयार करा

## सारांश

Foundry Local आणि Azure AI Foundry वापरून कृतीक्षम GenAI वर्कफ्लो कसे तयार करायचे ते शोधा. प्रगत प्रॉम्प्ट अभियांत्रिकी शिकून, संरचित डेटा एकत्रित करा, आणि पुनरुत्पादित होणाऱ्या पाईपलाईन्ससह कार्ये संघटित करा. दस्तऐवज आणि डेटा Q&A साठी Retrieval-Augmented Generation (RAG) या विषयावर लक्ष केंद्रित असले तरी ही पद्धत व्यापक GenAI सोल्यूशन डिझाइनसाठी सामान्य आहे.

## शिक्षण उद्दिष्टे

या सत्राच्या शेवटी, आपण सक्षम असाल:

- **प्रॉम्प्ट अभियांत्रिकीमध्ये प्रभुत्व मिळवा**: प्रभावी सिस्टम प्रॉम्प्ट आणि ग्राउंडिंग धोरणे डिझाइन करा
- **RAG पॅटर्न अंमलात आणा**: व्हेक्टर शोध वापरून दस्तऐवज-आधारित Q&A सिस्टम तयार करा
- **संरचित डेटा एकत्र करा**: AI वर्कफ्लोमध्ये CSV, JSON आणि तक्त्याच्या डेटासह कार्य करा
- **उत्पादन RAG तयार करा**: Chainlit वापरून स्केलेबल RAG अनुप्रयोग तयार करा
- **स्थानिक ते क्लाऊड सेतू उभारणी करा**: Foundry Local कडून Azure AI Foundry कडे स्थलांतर मार्ग समजून घ्या

## पूर्वतयारी

- सत्र 1 पूर्ण केलेले (Foundry Local सेटअप)
- व्हेक्टर डेटाबेस आणि एम्बेडिंगची मूलभूत समज
- Python प्रोग्रामिंगचा अनुभव
- दस्तऐवज प्रक्रिया संकल्पनांची ओळख
 
### क्रॉस-प्लॅटफॉर्म वातावरण त्वरित प्रारंभ (Windows & macOS)

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

आपल्या वातावरणात Foundry Local macOS बायनरीज अजून उपलब्ध नसल्यास, Windows VM किंवा कंटेनरवर सेवा चालवा आणि सेट करा:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## पडताळणी: Foundry Local पर्यावरण तपासणी

डेमो सुरु करण्यापूर्वी आपल्या स्थानिक पर्यावरणाची पडताळणी करा:

```powershell
foundry --version              # CLI स्थापित आहे याची खात्री करा
foundry status                 # सेवा स्थिती
foundry model run phi-4-mini   # बेसलाइन SLM सुरू करा
curl http://localhost:5273/v1/models  # API चे प्रमाणीकरण करा (रनिंग मॉडेलची यादी करावी)
```

शेवटचा आदेश अयशस्वी झाला तर, सेवा सुरु करा (किंवा पुनः सुरु करा): `foundry service start`.

## डेमो प्रवाह (30 मिनिटे)

### 1. सिस्टम प्रॉम्प्ट आणि ग्राउंडिंग धोरणे (10 मिनिटे)

#### पाऊल 1.1: प्रगत प्रॉम्प्ट अभियांत्रिकी

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
                temperature=0.3,  # अधिक सुसंगत प्रतिसादांसाठी तापमान कमी करा
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
    
    # वेगवेगळ्या क्षेत्रांसाठी नमुना संदर्भ
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

#### पाऊल 1.2: ग्राउंडिंग धोरणे तपासा

```powershell
# phi-4-mini चालू आहे याची खात्री करा
foundry model run phi-4-mini

# प्रॉम्प्ट अभियांत्रिकी डेमो चालवा
python samples/02-rag-solutions/prompt_engineering.py
```

### 2. प्रॉम्प्ट्ससह तक्त्यांचा डेटा एकत्र करा (CSV Q&A) (10 मिनिटे)

#### पाऊल 2.1: CSV डेटा एकत्रीकरण

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
        
        # संख्यात्मक स्तंभांसाठी संख्यात्मक आकडेवारी जोडा
        numeric_cols = self.data.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            stats["numeric_summary"] = self.data[numeric_cols].describe().to_dict()
        
        # वर्गवारी संदर्भ माहिती जोडा
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
        
        # नमुना डेटा जोडा
        context_parts.append("\nSample Data:")
        for i, row in enumerate(self.summary_stats['sample_rows'][:3]):
            context_parts.append(f"Row {i+1}: {json.dumps(row, default=str)}")
        
        # प्रश्नाच्या सामग्रीनुसार संबंधित आकडेवारी जोडा
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
                temperature=0.2  # तथ्यात्मक डेटाच्या विश्लेषणासाठी कमी तापमान
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
    
    # नमुना विक्री डेटा तयार करा
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
    
    # निर्देशिका अस्तित्वात असल्याची खात्री करा
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    df.to_csv(csv_path, index=False)
    return csv_path

def demo_csv_qa():
    """Demonstrate CSV Q&A capabilities"""
    
    # नमुना डेटा संच तयार करा
    csv_path = create_sample_dataset()
    print(f"Created sample dataset: {csv_path}")
    
    # प्रश्नोत्तरे प्रणाली प्रारंभ करा
    qa_system = CSVQASystem()
    
    # डेटा लोड करा
    if not qa_system.load_csv_data(csv_path):
        print("Failed to load CSV data")
        return
    
    print(f"\nLoaded dataset with shape: {qa_system.data.shape}")
    
    # उदाहरण प्रश्न
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

#### पाऊल 2.2: CSV Q&A सिस्टम तपासा

```powershell
# CSV Q&A डेमो चालवा
python samples/02-rag-solutions/csv_qa_system.py
```

### 3. प्रारंभिक प्रोजेक्ट: 02-grounding-data मध्ये सुधारणा करा (5 मिनिटे)

#### पाऊल 3.1: सुधारित दस्तऐवज RAG सिस्टम

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
        
        # क्वेरी व्हेक्टर करणे
        query_vector = self.vectorizer.transform([query])
        
        # सारखेपणा मोजा
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()
        
        # टॉप-क दस्तऐवज मिळवा
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # किमान सारखेपणा मर्यादा
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
        
        # संबंधित दस्तऐवज मिळवा
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
    
    # RAG प्रणाली तयार करा
    rag_system = SimpleRAGSystem()
    
    # नमुना ज्ञानआधार जोडा
    documents = create_sample_knowledge_base()
    rag_system.add_documents(documents)
    
    print(f"Loaded {len(documents)} documents into knowledge base")
    
    # उदाहरण प्रश्न
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

### 4. CLI ते Azure स्थलांतर मार्ग दाखवा (5 मिनिटे)

#### पाऊल 4.1: स्थलांतर धोरणाचा आढावा

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
            # फाउंड्री लोकल कॉन्फिगरेशन
            self.client = OpenAI(
                base_url="http://localhost:5273/v1",
                api_key="not-needed"
            )
            self.default_model = "phi-4-mini"
            
        elif environment == "azure":
            # Azure AI फाउंड्री कॉन्फिगरेशन
            if not azure_endpoint or not azure_api_key:
                raise ValueError("Azure endpoint and API key required for Azure environment")
            
            self.client = OpenAI(
                base_url=f"{azure_endpoint}/openai/deployments",
                api_key=azure_api_key,
                default_headers={"api-version": azure_api_version}
            )
            self.default_model = "gpt-4"  # किंवा तुमचे Azure डिप्लॉयमेंट नाव
            
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
                # फाउंड्री लोकसाठी, आम्ही सामान्यपणे CLI वापरतो
                # हे एक साधी उदाहरण आहे
                return {
                    "success": True,
                    "models": ["phi-4-mini", "qwen2.5-0.5b", "deepseek-coder-1.3b"],
                    "environment": "local"
                }
            else:
                # Azure साठी, तुम्ही डिप्लॉयमेंट्स एंडपॉईंट क्वेरी करू शकता
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
    
    # चाचणी संदेश
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
    
    # फाउंड्री लोकसह चाचणी
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
    
    # Azure कॉन्फिगरेशन दाखवा (क्रेडेन्शियल्स आवश्यक असल्याने टिप्पणी केलेले)
    print("\n2. Azure AI Foundry Configuration:")
    print("-" * 40)
    print("""
    # Azure AI फाउंड्री कडे स्थलांतर करण्यासाठी, खालीलप्रमाणे कॉन्फिगर करा:
    
    azure_client = UnifiedAIClient(
        environment="azure",
        azure_endpoint="https://your-resource.openai.azure.com",
        azure_api_key="your-api-key",
        azure_api_version="2024-08-01-preview"
    )
    
    # दोन्ही पर्यावरणात एकसारखे API कॉल कार्य करतात!
    azure_result = azure_client.chat_completion(
        messages=test_messages,
        max_tokens=200,
        temperature=0.7
    )
    """)
    
    # स्थलांतर धोरण
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
    
    # कॉन्फिगरेशन उदाहरणे
    print("\n4. Environment-based Configuration:")
    print("-" * 40)
    print("""
    # विकासासाठी .env फाइल
    AI_ENVIRONMENT=local
    FOUNDRY_LOCAL_URL=http://localhost:5273/v1
    DEFAULT_MODEL=phi-4-mini
    
    # उत्पादनासाठी .env फाइल
    AI_ENVIRONMENT=azure
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
    AZURE_OPENAI_API_KEY=your-api-key
    AZURE_OPENAI_API_VERSION=2024-08-01-preview
    DEFAULT_MODEL=gpt-4
    """)

if __name__ == "__main__":
    demo_migration_patterns()
```

#### पाऊल 4.2: स्थलांतर पॅटर्न तपासा

```powershell
# स्थलांतर डेमो चालवा
python samples/02-rag-solutions/migration_guide.py
```

## महत्वाचे संकल्पना आढळले

### 1. प्रगत प्रॉम्प्ट अभियांत्रिकी

- **सिस्टम प्रॉम्प्ट्स**: क्षेत्र-विशिष्ट विशेषज्ञ व्यक्तिमत्त्वे
- **ग्राउंडिंग धोरणे**: संदर्भ समाकलन तंत्र
- **तापमान नियंत्रण**: सर्जनशीलता विरुद्ध सातत्य संतुलित करणे
- **टोकन व्यवस्थापन**: कार्यक्षम संदर्भ वापर

### 2. संरचित डेटा एकत्रीकरण

- **CSV प्रक्रिया**: AI मॉडेल्ससह Pandas एकत्रीकरण
- **सांख्यिकीय विश्लेषण**: स्वयंचलित डेटा संक्षेप
- **संदर्भ निर्मिती**: क्वेरीजनुसार डायनॅमिक संदर्भ निर्मिती
- **मुल्टी-फॉरमॅट समर्थन**: JSON, CSV आणि तक्त्याचा डेटा

### 3. RAG अंमलबजावणी पॅटर्न

- **व्हेक्टर शोध**: TF-IDF आणि कॉसाईन सादृश्यता
- **दस्तऐवज पुनर्प्राप्ती**: संबंधिततेचा गुणांकन आणि क्रमवारी
- **संदर्भ संयोजन**: बहु-दस्तऐवज संश्लेषण
- **उत्तर निर्मिती**: आधारित प्रतिसाद तयार करणे

### 4. क्लाऊड स्थलांतर धोरणे

- **एकत्रित API**: स्थानिक आणि क्लाऊडसाठी एकच कोडबेस
- **पर्यावरण सारांश**: कॉन्फिगरेशन-चालित आयडीप्लॉइमेंट
- **विकास वर्कफ्लो**: स्थानिक → स्टेजिंग → उत्पादन
- **खर्च अनुकूलन**: स्थानिक विकास, क्लाऊड उत्पादन

## उत्पादन विचार

### 1. कार्यक्षमता अनुकूलन

```python
# उत्पादन RAG साठी ऑप्टिमाइझ करा
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
# मजबूत त्रुटी हाताळणी
try:
    result = rag_system.generate_answer(question)
    if "error" in result:
        # सामान्य ज्ञानाकडे पुनर्बाँड
        fallback_result = client.chat.completions.create(
            model="phi-4-mini",
            messages=[{"role": "user", "content": question}]
        )
except Exception as e:
    # त्रुटीची नोंद करा आणि सौम्य ऱ्हास प्रदान करा
    logger.error(f"RAG system error: {e}")
```

### 3. निरीक्षण आणि दृष्यते

```python
# RAG कार्यक्षमता ट्रॅक करा
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```

## पुढील पावले

हे सत्र पूर्ण केल्यावर:

1. **सत्र 3 शोधा**: Foundry Local मध्ये ओपन-सोर्स मॉडेल्स
2. **उत्पादन RAG तयार करा**: Chainlit वापरून अंमलात आणा (नमुना 04)
3. **प्रगत व्हेक्टर शोध**: Chroma किंवा Pinecone सह एकत्रित करा
4. **क्लाऊड स्थलांतर**: Azure AI Foundry मध्ये तैनात करा
5. **RAG गुणवत्ता मूल्यांकन**: `cd Workshop/samples;python -m session02.rag_eval_ragas` चालवा जेणेकरून उत्तर_संबंध, प्रामाणिकपणा, आणि संदर्भ_अचूकता ragas वापरून मोजली जाईल

### ऐच्छिक सुधारणा

| श्रेणी | सुधारणा | कारण | दिशा |
|----------|-------------|-----------|-----------|
| पुनर्प्राप्ती | TF-IDF ऐवजी व्हेक्टर स्टोअर (FAISS / Chroma) बदला | चांगले सेमँटिक रीकॉल व स्केलेबिलिटी | दस्तऐवज भाग करा (500–800 अक्षरे), एम्बेड करा, सूची टिकवा |
| हायब्रिड निर्देशांक | द्वैत सेमँटिक + कीवर्ड फिल्टरिंग | संख्यात्मक / कोड प्रश्नांवरील अचूकता सुधारते | आधी कीवर्डने फिल्टर करा, नंतर कॉसाईन सादृश्यतेनुसार क्रम लावा |
| एम्बेडिंग | एकाधिक एम्बेडिंग मॉडेल चाचणी करा | सुसंगतता विरुद्ध गती सुधारित करा | A/B: MiniLM विरुद्ध E5-small विरुद्ध स्थानिक होस्टेड एनकोडर |
| कॅशिंग | एम्बेडिंग् आणि पुनर्प्राप्ती निकाल कॅश करा | पुनरावृत्ती क्वेरी विलंबता कमी करा | सोपा ऑन-डिस्क पिकल / sqlite सह हॅश की |
| मूल्यांकन | ragas डेटासेट विस्तारित करा | सांख्यिकीय अर्थपूर्ण गुणवत्ता | 50–100 Q/A + संदर्भ तयार करा; विषयानुसार वर्गीकरण करा |
| मेट्रिक्स | पुनर्प्राप्ती आणि निर्मिती वेळ नोंदवा | कार्यक्षमतेचे प्रोफाइलिंग | प्रत्येकी कॉलसाठी `retrieval_ms`, `gen_ms`, `tokens` टिपा |
| गार्डरेल्स | हलुसिनेशन फॉलबॅक जोडा | अधिक सुरक्षित उत्तरे | जर प्रामाणिकपणा < मर्यादा → उत्तर द्या: "पुरेशा संदर्भाशिवाय." |
| फॉलबॅक | स्थानिक → Azure मॉडेल कॅस्केड | हायब्रिड गुणवत्ता वाढवा | कमी आत्मविश्वास असलेल्या प्रश्नांना स्थानिक मॉडेलपासून OpenAI API द्वारे क्लाऊडवर मार्गदर्शन करा |
| निश्चितता | स्थिर तुलना रन | पुनरावृत्तीयोग्य मूल्यांकन संच | बीज निश्चित करा, `temperature=0`, सॅम्पलर रॅन्डमनेस बंद करा |
| निरीक्षण | मूल्यांकन रन इतिहास टिकवा | अभिगमन शोधा | टाइमस्टँप + मेट्रिक फरकांसह JSON लाईन्स जोडा |

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

#### ragas सह प्रमाणपत्र मूल्यांकन वाढवा

1. `question`, `answer`, `contexts`, `ground_truths` (यादी) या फील्डसह JSONL तयार करा
2. `Dataset.from_list(list_of_dicts)` मध्ये रूपांतर करा
3. `evaluate(dataset, metrics=[...])` चालवा
4. ट्रेंड विश्लेषणासाठी मेट्रिक्स (CSV/JSON) साठवून ठेवा.

#### व्हेक्टर स्टोअर त्वरित प्रारंभ (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) सामान्यीकृत
D, I = index.search(query_vec, k)
```

डिस्क टिकवणीसाठी `faiss.write_index(index, "kb.index")` वापरा.

## अतिरिक्त संसाधने

### दस्तऐवज
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG पॅटर्न्स](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [प्रॉम्प्ट अभियांत्रिकी मार्गदर्शक](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Ragas मूल्यांकन दस्तऐवज](https://docs.ragas.io)

### नमुना कोड
- [Module08 Sample 04](./samples/04/README.md) - Chainlit RAG अनुप्रयोग
- [प्रगत मल्टि-एजंट सिस्टम](./samples/09/README.md) - एजंट समन्वय पॅटर्न्स

---

**सत्र कालावधी**: 30 मिनिटे हस्तगत + 15 मिनिटे Q&A
**कठीणाई पातळी**: मध्यम
**पूर्वतयारी**: सत्र 1 पूर्ण केलेले, मूलभूत Python ज्ञान

## नमुना परिस्थिती आणि कार्यशाळेची मॅपिंग

| कार्यशाळा स्क्रिप्ट / नोटबुक | परिस्थिती | लक्ष्य | मुख्य डेटासेट / स्रोत | उदाहरण प्रश्न |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | अंतर्गत समर्थन ज्ञान आधार ज्याने गोपनीयता आणि कार्यक्षमतेच्या FAQ उत्तर दिले | अतिमिती RAG सह एम्बेडिंग्ज | स्क्रिप्टमधील `DOCS` सूची (5 लहान परिच्छेद) | स्थानिक अनुमानासह RAG का वापरता? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | गुणवत्ता विश्लेषकाने बेसलाइन पुनर्प्राप्ती प्रामाणिकपणे मोजणी स्थापित केली | लहान कृत्रिम डेटासेटवर ragas मेट्रिक्स सांगा | `DOCS`, `QUESTIONS`, `GROUND_TRUTH` अ‍ॅरे | स्थानिक अनुमानाचा काय फायदा आहे? |
| `prompt_engineering.py` (प्रगत) | क्षेत्र तज्ज्ञाने विविध क्षेत्रांकरिता आधारित प्रॉम्प्ट तयार केले | क्षेत्रीय सिस्टम प्रॉम्प्ट्स आणि टोकन प्रभावाची तुलना करा | इनलाइन `contexts` डिक्शनरी | Foundry Local मॉडेल कॅशिंग कसे हाताळते? |
| `csv_qa_system.py` | विक्री ऑपरेशन्स लहान विक्री विभागांवर संवादात्मक विश्लेषण शोधतात | संक्षेप व क्वेरी लहान विक्री विभाग | तयार केलेले `sample_sales_data.csv` (10 रकाने) | कोणत्या उत्पादनाची सरासरी विक्री सर्वाधिक आहे? |
| `document_rag.py` | उत्पादन टीम अंतर्गत विकी करीता दस्तऐवज RAG तपासते | संबंधित दस्तऐवज पुनर्प्राप्ति आणि उद्धृत करा | `create_sample_knowledge_base()` सूची | Edge AI चे फायदे काय आहेत? |
| `migration_guide.py` | आर्किटेक्ट क्लाऊड स्थलांतर योजना तयार करतो | स्थानिक→Azure API समतोल दाखवा | स्थिर चाचणी प्रॉम्प्ट्स | Edge AI च्या फायद्यांचे 2–3 वाक्यांत स्पष्टीकरण द्या. |

### डेटासेट तुकडे
इनलाइन RAG पाईपलाईन दस्तऐवज सूची:
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```

Ragas मूल्यांकन सत्य जोडी:
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```

### परिस्थिती कथा
समर्थन अभियांत्रिकी गटाला ग्राहक डेटा बाह्यरित्या प्रदर्शित न करता अंतर्गत FAQ उत्तर देणारा जलद प्रोटोटाइप आवश्यक आहे. सत्र 2 चे घटक एक अतिमिती तात्पुरता RAG (टिकाऊपणा नाही) → संरचित CSV Q&A → दस्तऐवज पुनःप्राप्ति उद्धृत करत → वस्तुनिष्ठ गुणवत्ता मूल्यांकन (ragas) → Azure स्टेजिंगसाठी तयार स्थलांतर धोरण वेगवेगळ्या टप्प्यांत प्रगती करतात.

### विस्तार मार्ग
ऐच्छिक सुधारणा तक्त्याचा वापर करून विकसित करा: TF-IDF चे FAISS/Chroma ने स्थानापन्न करा, मूल्यांकन कॉर्पस वाढवा (50–100 Q/A), प्रामाणिकपणा < मर्यादा ठेवल्यास मोठ्या मॉडेलकडे फॉलबॅक एस्केलेशन जोडा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->