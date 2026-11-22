# 第二部分：使用 Azure AI Foundry 构建 AI 解决方案

## 摘要

探索如何使用 Foundry Local 和 Azure AI Foundry 构建可操作的生成式 AI 工作流。学习高级提示工程，集成结构化数据，并使用可复现的流水线协调任务。虽然重点是针对文档和数据问答的检索增强生成（RAG），但这些模式可推广到更广泛的生成式 AI 解决方案设计。

## 学习目标

本部分结束后，您将能够：

- <strong>精通提示工程</strong>：设计有效的系统提示和落地策略
- **实现 RAG 模式**：构建基于文档的问答系统并集成向量搜索
- <strong>集成结构化数据</strong>：在 AI 工作流中处理 CSV、JSON 和表格数据
- **构建生产级 RAG**：使用 Chainlit 创建可扩展的 RAG 应用
- <strong>连接本地到云端</strong>：理解从 Foundry Local 到 Azure AI Foundry 的迁移路径

## 前置条件

- 完成第一部分（Foundry Local 设置）
- 具备向量数据库和嵌入的基本知识
- 具备 Python 编程经验
- 熟悉文档处理概念
 
### 跨平台环境快速入门（Windows 和 macOS）

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

如果您环境中尚无 Foundry Local macOS 二进制文件，请在 Windows 虚拟机或容器中运行服务，并设置：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## 验证：Foundry Local 环境检查

在开始演示之前，验证您的本地环境：

```powershell
foundry --version              # 确保已安装CLI
foundry status                 # 服务状态
foundry model run phi-4-mini   # 启动基线SLM
curl http://localhost:5273/v1/models  # 验证API（应列出正在运行的模型）
```

如果最后一条命令失败，请启动（或重启）服务：`foundry service start`。

## 演示流程（30分钟）

### 1. 系统提示与落地策略（10分钟）

#### 第1.1步：高级提示工程

创建 `samples/02-rag-solutions/prompt_engineering.py`：

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
                temperature=0.3,  # 降低温度以获得更一致的响应
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
    
    # 不同领域的示例上下文
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

#### 第1.2步：测试落地策略

```powershell
# 确保 phi-4-mini 正在运行
foundry model run phi-4-mini

# 运行提示工程演示
python samples/02-rag-solutions/prompt_engineering.py
```

### 2. 融合表格数据与提示（CSV 问答）（10分钟）

#### 第2.1步：CSV 数据集成

创建 `samples/02-rag-solutions/csv_qa_system.py`：

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
        
        # 为数值列添加数值统计信息
        numeric_cols = self.data.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            stats["numeric_summary"] = self.data[numeric_cols].describe().to_dict()
        
        # 添加分类汇总
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
        
        # 添加示例数据
        context_parts.append("\nSample Data:")
        for i, row in enumerate(self.summary_stats['sample_rows'][:3]):
            context_parts.append(f"Row {i+1}: {json.dumps(row, default=str)}")
        
        # 根据问题内容添加相关统计信息
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
                temperature=0.2  # 用于事实数据分析的低温参数
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
    
    # 创建示例销售数据
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
    
    # 确保目录存在
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    df.to_csv(csv_path, index=False)
    return csv_path

def demo_csv_qa():
    """Demonstrate CSV Q&A capabilities"""
    
    # 创建示例数据集
    csv_path = create_sample_dataset()
    print(f"Created sample dataset: {csv_path}")
    
    # 初始化问答系统
    qa_system = CSVQASystem()
    
    # 加载数据
    if not qa_system.load_csv_data(csv_path):
        print("Failed to load CSV data")
        return
    
    print(f"\nLoaded dataset with shape: {qa_system.data.shape}")
    
    # 示例问题
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

#### 第2.2步：测试 CSV 问答系统

```powershell
# 运行 CSV 问答演示
python samples/02-rag-solutions/csv_qa_system.py
```

### 3. 入门项目：改造 02-grounding-data（5分钟）

#### 第3.1步：增强文档 RAG 系统

创建 `samples/02-rag-solutions/document_rag.py`：

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
        
        # 向量化查询
        query_vector = self.vectorizer.transform([query])
        
        # 计算相似度
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()
        
        # 获取前k个文档
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # 最小相似度阈值
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
        
        # 检索相关文档
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
    
    # 创建RAG系统
    rag_system = SimpleRAGSystem()
    
    # 添加示例知识库
    documents = create_sample_knowledge_base()
    rag_system.add_documents(documents)
    
    print(f"Loaded {len(documents)} documents into knowledge base")
    
    # 示例问题
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

### 4. 展示 CLI 到 Azure 的迁移路径（5分钟）

#### 第4.1步：迁移策略概览

创建 `samples/02-rag-solutions/migration_guide.py`：

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
            self.default_model = "gpt-4"  # 或者您的 Azure 部署名称
            
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
                # 对于 Foundry 本地，我们通常使用 CLI
                # 这是一个简化的示例
                return {
                    "success": True,
                    "models": ["phi-4-mini", "qwen2.5-0.5b", "deepseek-coder-1.3b"],
                    "environment": "local"
                }
            else:
                # 对于 Azure，您可以查询部署端点
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
    
    # 测试消息
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
    
    # 使用 Foundry 本地测试
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
    
    # 显示 Azure 配置（已注释，因为需要凭据）
    print("\n2. Azure AI Foundry Configuration:")
    print("-" * 40)
    print("""
    # 迁移到 Azure AI Foundry，请按如下配置：
    
    azure_client = UnifiedAIClient(
        environment="azure",
        azure_endpoint="https://your-resource.openai.azure.com",
        azure_api_key="your-api-key",
        azure_api_version="2024-08-01-preview"
    )
    
    # 相同的 API 调用在两个环境中都有效！
    azure_result = azure_client.chat_completion(
        messages=test_messages,
        max_tokens=200,
        temperature=0.7
    )
    """)
    
    # 迁移策略
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
    
    # 配置示例
    print("\n4. Environment-based Configuration:")
    print("-" * 40)
    print("""
    # 开发环境的 .env 文件
    AI_ENVIRONMENT=local
    FOUNDRY_LOCAL_URL=http://localhost:5273/v1
    DEFAULT_MODEL=phi-4-mini
    
    # 生产环境的 .env 文件
    AI_ENVIRONMENT=azure
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
    AZURE_OPENAI_API_KEY=your-api-key
    AZURE_OPENAI_API_VERSION=2024-08-01-preview
    DEFAULT_MODEL=gpt-4
    """)

if __name__ == "__main__":
    demo_migration_patterns()
```

#### 第4.2步：测试迁移模式

```powershell
# 运行迁移演示
python samples/02-rag-solutions/migration_guide.py
```

## 涉及的关键概念

### 1. 高级提示工程

- <strong>系统提示</strong>：领域特定专家角色
- <strong>落地策略</strong>：上下文集成技术
- <strong>温度控制</strong>：在创造性与一致性间平衡
- <strong>令牌管理</strong>：高效利用上下文

### 2. 结构化数据集成

- **CSV 处理**：Pandas 与 AI 模型集成
- <strong>统计分析</strong>：自动化数据汇总
- <strong>上下文创建</strong>：基于查询的动态上下文生成
- <strong>多格式支持</strong>：JSON、CSV 及表格数据

### 3. RAG 实现模式

- <strong>向量搜索</strong>：TF-IDF 和余弦相似度
- <strong>文档检索</strong>：相关性评分与排序
- <strong>上下文组合</strong>：多文档综合
- <strong>答案生成</strong>：基于落地的响应创建

### 4. 云端迁移策略

- **统一 API**：本地与云端单一代码库
- <strong>环境抽象</strong>：配置驱动部署
- <strong>开发工作流</strong>：本地 → 预生产 → 生产
- <strong>成本优化</strong>：本地开发，云端生产

## 生产考虑事项

### 1. 性能优化

```python
# 优化生产环境中的检索增强生成（RAG）
rag_config = {
    "max_context_docs": 5,
    "similarity_threshold": 0.15,
    "max_tokens": 1000,
    "temperature": 0.2,
    "chunk_size": 500,
    "chunk_overlap": 50
}
```

### 2. 错误处理

```python
# 强大的错误处理
try:
    result = rag_system.generate_answer(question)
    if "error" in result:
        # 回退到一般知识
        fallback_result = client.chat.completions.create(
            model="phi-4-mini",
            messages=[{"role": "user", "content": question}]
        )
except Exception as e:
    # 记录错误并提供优雅降级
    logger.error(f"RAG system error: {e}")
```

### 3. 监控与可观测性

```python
# 跟踪RAG性能
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```

## 下一步

完成本部分后：

1. <strong>探索第三部分</strong>：Foundry Local 中的开源模型
2. **构建生产级 RAG**：使用 Chainlit 实现（示例 04）
3. <strong>高级向量搜索</strong>：集成 Chroma 或 Pinecone
4. <strong>云端迁移</strong>：部署到 Azure AI Foundry
5. **评估 RAG 质量**：运行 `cd Workshop/samples;python -m session02.rag_eval_ragas`，使用 ragas 测量 answer_relevancy、faithfulness 和 context_precision

### 可选增强

| 分类 | 增强 | 理由 | 方向 |
|----------|-------------|-----------|-----------|
| 检索 | 用向量存储替代 TF-IDF（FAISS / Chroma） | 语义召回和可扩展性更优 | 分块文档（500–800 字符），嵌入，持久化索引 |
| 混合索引 | 语义 + 关键词双重过滤 | 提升数值/代码查询精确度 | 先按关键词过滤，再按余弦相似度排序 |
| 嵌入 | 评估多种嵌入模型 | 优化相关性与速度 | A/B 测试：MiniLM 对比 E5-small 及本地编码器 |
| 缓存 | 缓存嵌入和检索结果 | 降低重复查询延迟 | 简单的磁盘pickle / sqlite 哈希键缓存 |
| 评估 | 扩充 ragas 数据集 | 提供统计学意义的质量保证 | 筛选 50–100 Q/A + 上下文，按主题分层 |
| 指标 | 跟踪检索与生成耗时 | 性能分析 | 捕获每次调用的 `retrieval_ms`、`gen_ms`、`tokens` |
| 安全保护 | 添加幻觉回退机制 | 答案更安全 | 若忠实度 < 阈值 → 回答：“上下文不足。” |
| 回退 | 本地 → Azure 模型级联 | 混合质量提升 | 在置信度低时通过相同 OpenAI API 路由到云端 |
| 确定性 | 稳定的比较测试 | 可重复评估集 | 固定随机种子，`temperature=0`，禁用采样随机性 |
| 监控 | 保留评估运行历史 | 回归检测 | 追加 JSON 行，含时间戳和指标差异 |

#### 示例：添加检索耗时

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

#### 使用 ragas 扩展评估规模

1. 组装一个包含字段：`question`、`answer`、`contexts`、`ground_truths`（列表）的 JSONL 文件
2. 转换为 `Dataset.from_list(list_of_dicts)`
3. 运行 `evaluate(dataset, metrics=[...])`
4. 存储指标（CSV/JSON）以便趋势分析。

#### 向量存储快速入门（FAISS）

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) 已归一化
D, I = index.search(query_vec, k)
```

磁盘持久化使用 `faiss.write_index(index, "kb.index")`。

## 额外资源

### 文档
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Azure AI Foundry RAG 模式](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [提示工程指南](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Ragas 评估文档](https://docs.ragas.io)

### 示例代码
- [模块08 示例 04](./samples/04/README.md) - Chainlit RAG 应用
- [高级多代理系统](./samples/09/README.md) - 代理协调模式

---

<strong>课程时长</strong>：30 分钟实践 + 15 分钟问答
<strong>难度等级</strong>：中级
<strong>前置条件</strong>：完成第一部分，具备基本 Python 知识

## 示例场景与工作坊映射

| 工作坊脚本 / 笔记本 | 场景 | 目标 | 核心数据集 / 源 | 示例问题 |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | 内部支持知识库回答隐私和性能常见问题 | 带嵌入的最简内存 RAG | 脚本中的 `DOCS` 列表（5 段简短内容） | 为什么使用本地推理的 RAG？ |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | 质量分析员建立基线检索忠实度指标 | 在小型合成数据集上计算 ragas 指标 | `DOCS`、`QUESTIONS`、`GROUND_TRUTH` 数组 | 本地推理有什么优势？ |
| `prompt_engineering.py`（高级） | 领域专家为多垂直场景制作落地提示 | 比较领域系统提示及令牌影响 | 内联的 `contexts` 字典 | Foundry Local 如何管理模型缓存？ |
| `csv_qa_system.py` | 销售运维探索导出的交互式分析 | 汇总并查询小型销售切片 | 生成的 `sample_sales_data.csv`（10 行） | 哪个产品的平均销售额最高？ |
| `document_rag.py` | 产品团队探索内部 Wiki 的文档 RAG | 检索并引用相关文档 | `create_sample_knowledge_base()` 列表 | Edge AI 的好处是什么？ |
| `migration_guide.py` | 架构师准备云迁移计划 | 展示本地→Azure API 等效性 | 静态测试提示 | 用 2-3 句说明边缘 AI 的优势。 |

### 数据集片段
内联 RAG 流水线文档列表：
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```

Ragas 评估真值元组：
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```

### 场景叙述
支持工程组希望快速原型化以回答内部常见问题，且不将客户数据暴露给外部。第二部分工件从最简的短暂 RAG（无持久化） → 结构化 CSV 问答 → 带引用的文档检索 → 客观质量评估（ragas）→ Azure 预生产就绪迁移策略逐步推进。

### 扩展路径
使用可选增强表演进：用 FAISS/Chroma 替换 TF-IDF，扩大评估语料库（50-100 Q/A），在忠实度低于阈值时增加回退升级到更大模型。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->