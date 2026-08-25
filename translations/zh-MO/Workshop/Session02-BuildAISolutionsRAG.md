# 第 2 節：使用 Azure AI Foundry 構建 AI 解決方案

## 摘要

探索如何使用 Foundry Local 和 Azure AI Foundry 構建可行的 GenAI 工作流程。學習進階提示工程，整合結構化數據，並通過可複製的管道協調任務。雖然重點在於用於文件與數據問答的檢索增強生成 (RAG)，但這些模式可推廣到更廣泛的 GenAI 解決方案設計。

## 學習目標

在本節結束時，您將能夠：

- <strong>掌握提示工程</strong>：設計有效的系統提示和基礎策略
- **實現 RAG 模式**：使用向量搜尋構建基於文件的問答系統
- <strong>整合結構化數據</strong>：在 AI 工作流程中處理 CSV、JSON 和表格式數據
- **構建生產級 RAG**：使用 Chainlit 創建可擴展的 RAG 應用
- <strong>橋接本地與雲端</strong>：了解從 Foundry Local 到 Azure AI Foundry 的遷移路徑

## 先決條件

- 完成第 1 節（Foundry Local 設置）
- 基本了解向量資料庫和嵌入技術
- Python 編程經驗
- 熟悉文件處理概念
 
### 跨平台環境快速啟動（Windows 和 macOS）

Windows PowerShell：
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai sentence-transformers ragas datasets scikit-learn
```

macOS / Linux：
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai sentence-transformers ragas datasets scikit-learn
```

如果您的環境尚未提供 Foundry Local macOS 二進制檔，請在 Windows 虛擬機或容器上運行服務，並設置：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## 驗證：Foundry Local 環境檢查

在開始示範之前，請驗證您的本地環境：

```powershell
foundry --version              # 確保已安裝 CLI
foundry status                 # 服務狀態
foundry model run phi-4-mini   # 啟動基線 SLM
curl http://localhost:5273/v1/models  # 驗證 API（應列出正在運行的模型）
```

如果最後一個命令失敗，請啟動（或重新啟動）服務：`foundry service start`。

## 示範流程（30 分鐘）

### 1. 系統提示和基礎策略（10 分鐘）

#### 步驟 1.1：進階提示工程

建立 `samples/02-rag-solutions/prompt_engineering.py`：

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
                temperature=0.3,  # 降低溫度以獲得更一致的回應
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
    
    # 為不同領域抽取範例上下文
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

#### 步驟 1.2：測試基礎策略

```powershell
# 確保 phi-4-mini 正在運行
foundry model run phi-4-mini

# 運行提示工程示範
python samples/02-rag-solutions/prompt_engineering.py
```

### 2. 與提示整合表格式數據（CSV 問答）（10 分鐘）

#### 步驟 2.1：CSV 數據整合

建立 `samples/02-rag-solutions/csv_qa_system.py`：

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
        
        # 為數字欄位新增數值統計
        numeric_cols = self.data.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            stats["numeric_summary"] = self.data[numeric_cols].describe().to_dict()
        
        # 新增類別的摘要
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
        
        # 新增範例數據
        context_parts.append("\nSample Data:")
        for i, row in enumerate(self.summary_stats['sample_rows'][:3]):
            context_parts.append(f"Row {i+1}: {json.dumps(row, default=str)}")
        
        # 根據問題內容新增相關統計
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
                temperature=0.2  # 針對事實數據分析的低溫度設定
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
    
    # 建立範例銷售數據
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
    
    # 確保目錄存在
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    df.to_csv(csv_path, index=False)
    return csv_path

def demo_csv_qa():
    """Demonstrate CSV Q&A capabilities"""
    
    # 建立範例資料集
    csv_path = create_sample_dataset()
    print(f"Created sample dataset: {csv_path}")
    
    # 初始化問答系統
    qa_system = CSVQASystem()
    
    # 載入數據
    if not qa_system.load_csv_data(csv_path):
        print("Failed to load CSV data")
        return
    
    print(f"\nLoaded dataset with shape: {qa_system.data.shape}")
    
    # 問題範例
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

#### 步驟 2.2：測試 CSV 問答系統

```powershell
# 運行 CSV 問答示範
python samples/02-rag-solutions/csv_qa_system.py
```

### 3. 入門專案：調整 02-grounding-data（5 分鐘）

#### 步驟 3.1：強化文件 RAG 系統

建立 `samples/02-rag-solutions/document_rag.py`：

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
        
        # 向量化查詢
        query_vector = self.vectorizer.transform([query])
        
        # 計算相似度
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()
        
        # 獲取前k個文件
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # 最低相似度閾值
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
        
        # 檢索相關文件
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
    
    # 創建RAG系統
    rag_system = SimpleRAGSystem()
    
    # 添加示例知識庫
    documents = create_sample_knowledge_base()
    rag_system.add_documents(documents)
    
    print(f"Loaded {len(documents)} documents into knowledge base")
    
    # 範例問題
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

### 4. 示範 CLI 至 Azure 遷移路徑（5 分鐘）

#### 步驟 4.1：遷移策略概述

建立 `samples/02-rag-solutions/migration_guide.py`：

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
            # Foundry 本地配置
            self.client = OpenAI(
                base_url="http://localhost:5273/v1",
                api_key="not-needed"
            )
            self.default_model = "phi-4-mini"
            
        elif environment == "azure":
            # Azure AI Foundry 配置
            if not azure_endpoint or not azure_api_key:
                raise ValueError("Azure endpoint and API key required for Azure environment")
            
            self.client = OpenAI(
                base_url=f"{azure_endpoint}/openai/deployments",
                api_key=azure_api_key,
                default_headers={"api-version": azure_api_version}
            )
            self.default_model = "gpt-4"  # 或者你的 Azure 部署名稱
            
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
                # 對於 Foundry 本地，我們通常會使用 CLI
                # 這是一個簡化範例
                return {
                    "success": True,
                    "models": ["phi-4-mini", "qwen2.5-0.5b", "deepseek-coder-1.3b"],
                    "environment": "local"
                }
            else:
                # 對於 Azure，你可能會查詢部署端點
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
    
    # 測試訊息
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
    
    # 使用 Foundry 本地測試
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
    
    # 顯示 Azure 配置（已註解，因為需要憑證）
    print("\n2. Azure AI Foundry Configuration:")
    print("-" * 40)
    print("""
    # 要遷移到 Azure AI Foundry，請按以下方式配置：
    
    azure_client = UnifiedAIClient(
        environment="azure",
        azure_endpoint="https://your-resource.openai.azure.com",
        azure_api_key="your-api-key",
        azure_api_version="2024-08-01-preview"
    )
    
    # 兩個環境都可使用相同的 API 呼叫！
    azure_result = azure_client.chat_completion(
        messages=test_messages,
        max_tokens=200,
        temperature=0.7
    )
    """)
    
    # 遷移策略
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
    
    # 配置範例
    print("\n4. Environment-based Configuration:")
    print("-" * 40)
    print("""
    # 開發用 .env 檔案
    AI_ENVIRONMENT=local
    FOUNDRY_LOCAL_URL=http://localhost:5273/v1
    DEFAULT_MODEL=phi-4-mini
    
    # 生產用 .env 檔案
    AI_ENVIRONMENT=azure
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
    AZURE_OPENAI_API_KEY=your-api-key
    AZURE_OPENAI_API_VERSION=2024-08-01-preview
    DEFAULT_MODEL=gpt-4
    """)

if __name__ == "__main__":
    demo_migration_patterns()
```

#### 步驟 4.2：測試遷移模式

```powershell
# 運行遷移示範
python samples/02-rag-solutions/migration_guide.py
```

## 涵蓋的關鍵概念

### 1. 進階提示工程

- <strong>系統提示</strong>：特定領域專家角色
- <strong>基礎策略</strong>：上下文整合技術
- <strong>溫度控制</strong>：創造力與一致性的平衡
- <strong>代幣管理</strong>：高效使用上下文

### 2. 結構化數據整合

- **CSV 處理**：Pandas 與 AI 模型整合
- <strong>統計分析</strong>：自動化數據摘要
- <strong>上下文創建</strong>：基於查詢動態生成上下文
- <strong>多格式支持</strong>：JSON、CSV 及表格式數據

### 3. RAG 實現模式

- <strong>向量搜尋</strong>：TF-IDF 與餘弦相似度
- <strong>文件檢索</strong>：相關性打分與排序
- <strong>上下文組合</strong>：多文件綜合
- <strong>答案生成</strong>：基於依據的回答創建

### 4. 雲端遷移策略

- **統一 API**：單一代碼庫同時支持本地與雲端
- <strong>環境抽象</strong>：配置驅動部署
- <strong>開發流程</strong>：本地 → 預備 → 生產
- <strong>成本優化</strong>：本地開發，雲端生產

## 生產考量

### 1. 性能優化

```python
# 為生產 RAG 進行優化
rag_config = {
    "max_context_docs": 5,
    "similarity_threshold": 0.15,
    "max_tokens": 1000,
    "temperature": 0.2,
    "chunk_size": 500,
    "chunk_overlap": 50
}
```

### 2. 錯誤處理

```python
# 強健的錯誤處理
try:
    result = rag_system.generate_answer(question)
    if "error" in result:
        # 回退到一般知識
        fallback_result = client.chat.completions.create(
            model="phi-4-mini",
            messages=[{"role": "user", "content": question}]
        )
except Exception as e:
    # 記錄錯誤並提供優雅降級
    logger.error(f"RAG system error: {e}")
```

### 3. 監控與可觀察性

```python
# 跟踪RAG績效
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```

## 後續步驟

完成本節後：

1. **探索第 3 節**：Foundry Local 的開源模型
2. **構建生產級 RAG**：使用 Chainlit 實作（範例 04）
3. <strong>進階向量搜尋</strong>：整合 Chroma 或 Pinecone
4. <strong>雲端遷移</strong>：部署至 Azure AI Foundry
5. **評估 RAG 品質**：執行 `cd Workshop/samples;python -m session02.rag_eval_ragas` 以使用 ragas 衡量答案相關性、真實性及上下文精確度

### 選擇性強化

| 類別 | 強化 | 理由 | 方向 |
|----------|-------------|-----------|-----------|
| 檢索 | 以向量庫（FAISS / Chroma）取代 TF-IDF | 更佳語義召回與擴展性 | 分段文件（500–800 字元）、嵌入、持久化索引 |
| 混合索引 | 雙重語義 + 關鍵詞過濾 | 改善數字 / 程式碼查詢的精確度 | 先按關鍵詞過濾，後按餘弦相似度排序 |
| 嵌入 | 評估多種嵌入模型 | 優化相關性與速度 | A/B 測試：MiniLM 與 E5-small 及本地編碼器 |
| 快取 | 快取嵌入與檢索結果 | 降低重複查詢延遲 | 簡易磁碟 pickle / sqlite 搭配雜湊鍵 |
| 評估 | 擴充 ragas 數據集 | 統計上有意義的品質 | 選取 50–100 組問答與上下文；按主題分層 |
| 指標 | 追蹤檢索與生成時間 | 性能分析 | 捕捉每次呼叫的 `retrieval_ms`、`gen_ms`、`tokens` |
| 防護機制 | 新增幻覺備援 | 更安全的答案 | 若真實性<門檻，回答：「上下文不足。」 |
| 備援 | 層疊本地→Azure 模型 | 混合品質提升 | 低信心時經由相同 OpenAI API 路由至雲端 |
| 確定性 | 穩定比對運行 | 可重複評估集 | 固定種子，`temperature=0`，禁用取樣器隨機性 |
| 監控 | 持久化評估運行歷史 | 回歸偵測 | 附加帶時間戳及指標變化的 JSON 行 |

#### 範例：新增檢索計時

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

#### 使用 ragas 擴展評估

1. 組成包含欄位：`question`、`answer`、`contexts`、`ground_truths`（列表）的 JSONL
2. 轉換為 `Dataset.from_list(list_of_dicts)`
3. 執行 `evaluate(dataset, metrics=[...])`
4. 儲存指標（CSV/JSON）以進行趨勢分析。

#### 向量庫快速啟動（FAISS）

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # 嵌入 = np.array([...]) 正規化
D, I = index.search(query_vec, k)
```

如需磁碟持久化，使用 `faiss.write_index(index, "kb.index")`。

## 附加資源

### 文件
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG 模式](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [提示工程指南](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Ragas 評估文件](https://docs.ragas.io)

### 範例程式碼
- [Module08 範例 04](./samples/04/README.md) - Chainlit RAG 應用
- [進階多代理系統](./samples/09/README.md) - 代理協調模式

---

<strong>課程時長</strong>：30 分鐘實作 + 15 分鐘問答
<strong>難度等級</strong>：中階
<strong>先修條件</strong>：完成第 1 節，具備基本 Python 知識

## 範例場景與工作坊對應

| 工作坊腳本 / 筆記本 | 場景 | 目標 | 核心數據集 / 來源 | 範例問題 |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | 內部支援知識庫回答隱私與效能常見問題 | 最小記憶體 RAG 搭配嵌入 | 腳本中的 `DOCS` 清單（5 段短文） | 為什麼使用本地推理的 RAG？ |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | 品質分析師建立基本檢索真實性指標 | 在微小合成數據集上計算 ragas 指標 | `DOCS`、`QUESTIONS`、`GROUND_TRUTH` 陣列 | 本地推理有何優勢？ |
| `prompt_engineering.py`（進階） | 領域主題專家為多個垂直領域製作基礎提示 | 比較領域系統提示與代幣影響 | 內嵌的 `contexts` 字典 | Foundry Local 如何處理模型快取？ |
| `csv_qa_system.py` | 銷售營運探索對匯出資料的互動分析 | 摘要並查詢小型銷售數據片段 | 產生的 `sample_sales_data.csv`（10 行） | 哪個產品的平均銷售額最高？ |
| `document_rag.py` | 產品團隊探索內部維基文件的 RAG | 檢索並引用相關文件 | `create_sample_knowledge_base()` 清單 | 邊緣 AI 有何好處？ |
| `migration_guide.py` | 架構師準備雲端遷移計畫 | 展示本地→Azure API 等價性 | 靜態測試提示 | 用 2–3 句話解釋邊緣 AI 的優勢。 |

### 數據集截取
內嵌 RAG 管道文件清單：
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```

Ragas 評估真實元組：
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```

### 場景敘述
支援工程團隊希望快速建立能回答內部 FAQ 的原型，且不會將客戶數據暴露給外部。第 2 節的產物從最小化臨時 RAG（無持久化）→結構化 CSV 問答→帶引用的文件檢索→客觀品質評估（ragas）→準備好 Azure 預備環境的遷移策略。

### 擴展路徑
利用選擇性強化表進行擴充：用 FAISS/Chroma 替換 TF‑IDF、擴充評估語料（50–100 組問答）、真實性不足時新增向更大模型的備援升級。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->