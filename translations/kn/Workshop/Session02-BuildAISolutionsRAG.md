<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bb6014013b4adb7d7bfc60504eafed5d",
  "translation_date": "2025-12-15T21:16:05+00:00",
  "source_file": "Workshop/Session02-BuildAISolutionsRAG.md",
  "language_code": "kn"
}
-->
# ಸೆಷನ್ 2: ಅಜೂರ್ AI ಫೌಂಡ್ರಿಯೊಂದಿಗೆ AI ಪರಿಹಾರಗಳನ್ನು ನಿರ್ಮಿಸಿ

## ಸಾರಾಂಶ

Foundry Local ಮತ್ತು Azure AI Foundry ಬಳಸಿ ಕಾರ್ಯನಿರ್ವಹಣೀಯ GenAI ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸುವುದು ಎಂಬುದನ್ನು ಅನ್ವೇಷಿಸಿ. ಉನ್ನತ ಪ್ರಾಂಪ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್ ಕಲಿಯಿರಿ, ರಚನಾತ್ಮಕ ಡೇಟಾವನ್ನು ಸಂಯೋಜಿಸಿ, ಮತ್ತು ಪುನರಾವರ್ತನೀಯ ಪೈಪ್ಲೈನ್ಗಳೊಂದಿಗೆ ಕಾರ್ಯಗಳನ್ನು ಸಂಯೋಜಿಸಿ. ಗಮನ Retrieval-Augmented Generation (RAG) ಡಾಕ್ಯುಮೆಂಟ್ ಮತ್ತು ಡೇಟಾ ಪ್ರಶ್ನೋತ್ತರಕ್ಕಾಗಿ ಇದ್ದರೂ, ಮಾದರಿಗಳು ವ್ಯಾಪಕ GenAI ಪರಿಹಾರ ವಿನ್ಯಾಸಕ್ಕೆ ಸಾಮಾನ್ಯವಾಗಿವೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಸೆಷನ್ ಮುಗಿದಾಗ, ನೀವು:

- **ಪ್ರಾಂಪ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್‌ನಲ್ಲಿ ಪರಿಣತಿ ಪಡೆಯಿರಿ**: ಪರಿಣಾಮಕಾರಿ ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಗ್ರೌಂಡಿಂಗ್ ತಂತ್ರಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ
- **RAG ಮಾದರಿಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ**: ವೆಕ್ಟರ್ ಹುಡುಕಾಟದೊಂದಿಗೆ ಡಾಕ್ಯುಮೆಂಟ್ ಆಧಾರಿತ ಪ್ರಶ್ನೋತ್ತರ ವ್ಯವಸ್ಥೆಗಳನ್ನು ನಿರ್ಮಿಸಿ
- **ರಚನಾತ್ಮಕ ಡೇಟಾವನ್ನು ಸಂಯೋಜಿಸಿ**: AI ವರ್ಕ್‌ಫ್ಲೋಗಳಲ್ಲಿ CSV, JSON ಮತ್ತು ಟೇಬ್ಯುಲರ್ ಡೇಟಾ ಜೊತೆಗೆ ಕೆಲಸ ಮಾಡಿ
- **ಉತ್ಪಾದನಾ RAG ನಿರ್ಮಿಸಿ**: Chainlit ಬಳಸಿ ವಿಸ್ತಾರಗೊಳ್ಳುವ RAG ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ರಚಿಸಿ
- **ಸ್ಥಳೀಯದಿಂದ ಕ್ಲೌಡ್‌ಗೆ ಸೇತುವೆ**: Foundry Local ನಿಂದ Azure AI Foundry ಗೆ ಸ್ಥಳಾಂತರ ಮಾರ್ಗಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

- ಸೆಷನ್ 1 (Foundry Local ಸೆಟ್‌ಅಪ್) ಪೂರ್ಣಗೊಂಡಿದೆ
- ವೆಕ್ಟರ್ ಡೇಟಾಬೇಸ್‌ಗಳು ಮತ್ತು ಎಂಬೆಡ್ಡಿಂಗ್‌ಗಳ ಮೂಲಭೂತ ಅರ್ಥ
- ಪೈಥಾನ್ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಅನುಭವ
- ಡಾಕ್ಯುಮೆಂಟ್ ಪ್ರೊಸೆಸಿಂಗ್ ಸಂಪ್ರದಾಯಗಳ ಪರಿಚಯ

### ಕ್ರಾಸ್-ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಪರಿಸರ ತ್ವರಿತ ಪ್ರಾರಂಭ (Windows & macOS)

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
  
Foundry Local macOS ಬೈನರಿಗಳು ನಿಮ್ಮ ಪರಿಸರದಲ್ಲಿ ಇನ್ನೂ ಲಭ್ಯವಿಲ್ಲದಿದ್ದರೆ, Windows VM ಅಥವಾ ಕಂಟೈನರ್‌ನಲ್ಲಿ ಸೇವೆಯನ್ನು ಚಾಲನೆ ಮಾಡಿ ಮತ್ತು ಸೆಟ್ ಮಾಡಿ:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
## ಮಾನ್ಯತೆ: Foundry Local ಪರಿಸರ ಪರಿಶೀಲನೆ

ಡೆಮೋಗಳನ್ನು ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು, ನಿಮ್ಮ ಸ್ಥಳೀಯ ಪರಿಸರವನ್ನು ಪರಿಶೀಲಿಸಿ:  

```powershell
foundry --version              # CLI ಸ್ಥಾಪಿತವಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
foundry status                 # ಸೇವೆಯ ಸ್ಥಿತಿ
foundry model run phi-4-mini   # ಮೂಲ SLM ಪ್ರಾರಂಭಿಸಿ
curl http://localhost:5273/v1/models  # API ಪರಿಶೀಲಿಸಿ (ಚಲಿಸುತ್ತಿರುವ ಮಾದರಿಯನ್ನು ಪಟ್ಟಿ ಮಾಡಬೇಕು)
```
  
ಕೊನೆಯ ಕಮಾಂಡ್ ವಿಫಲವಾದರೆ, ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ (ಅಥವಾ ಮರುಪ್ರಾರಂಭಿಸಿ): `foundry service start`.

## ಡೆಮೋ ಪ್ರಕ್ರಿಯೆ (30 ನಿಮಿಷಗಳು)

### 1. ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಗ್ರೌಂಡಿಂಗ್ ತಂತ್ರಗಳು (10 ನಿಮಿಷಗಳು)

#### ಹಂತ 1.1: ಉನ್ನತ ಪ್ರಾಂಪ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್

`samples/02-rag-solutions/prompt_engineering.py` ರಚಿಸಿ:  

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
                temperature=0.3,  # ಹೆಚ್ಚು ಸತತ ಪ್ರತಿಕ್ರಿಯೆಗಳಿಗೆ ತಾಪಮಾನವನ್ನು ಕಡಿಮೆ ಮಾಡಿ
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
    
    # ವಿಭಿನ್ನ ಕ್ಷೇತ್ರಗಳಿಗಾಗಿ ಮಾದರಿ ಸಂದರ್ಭಗಳು
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
  
#### ಹಂತ 1.2: ಗ್ರೌಂಡಿಂಗ್ ತಂತ್ರಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ

```powershell
# phi-4-mini ಚಾಲನೆಯಲ್ಲಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿ
foundry model run phi-4-mini

# ಪ್ರಾಂಪ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್ ಡೆಮೋವನ್ನು ಚಾಲನೆ ಮಾಡಿ
python samples/02-rag-solutions/prompt_engineering.py
```
  
### 2. ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ಟೇಬ್ಯುಲರ್ ಡೇಟಾ ಸಂಯೋಜನೆ (CSV ಪ್ರಶ್ನೋತ್ತರ) (10 ನಿಮಿಷಗಳು)

#### ಹಂತ 2.1: CSV ಡೇಟಾ ಸಂಯೋಜನೆ

`samples/02-rag-solutions/csv_qa_system.py` ರಚಿಸಿ:  

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
        
        # ಸಂಖ್ಯಾತ್ಮಕ ಕಾಲಮ್‌ಗಳಿಗೆ ಸಂಖ್ಯಾತ್ಮಕ ಅಂಕಿಅಂಶಗಳನ್ನು ಸೇರಿಸಿ
        numeric_cols = self.data.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            stats["numeric_summary"] = self.data[numeric_cols].describe().to_dict()
        
        # ವರ್ಗೀಕೃತ ಸಾರಾಂಶಗಳನ್ನು ಸೇರಿಸಿ
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
        
        # ಮಾದರಿ ಡೇಟಾವನ್ನು ಸೇರಿಸಿ
        context_parts.append("\nSample Data:")
        for i, row in enumerate(self.summary_stats['sample_rows'][:3]):
            context_parts.append(f"Row {i+1}: {json.dumps(row, default=str)}")
        
        # ಪ್ರಶ್ನೆಯ ವಿಷಯದ ಆಧಾರದ ಮೇಲೆ ಸಂಬಂಧಿತ ಅಂಕಿಅಂಶಗಳನ್ನು ಸೇರಿಸಿ
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
                temperature=0.2  # ವಾಸ್ತವಿಕ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆಗೆ ಕಡಿಮೆ ತಾಪಮಾನ
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
    
    # ಮಾದರಿ ಮಾರಾಟ ಡೇಟಾವನ್ನು ರಚಿಸಿ
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
    
    # ಡೈರೆಕ್ಟರಿ ಇರುವುದನ್ನು ಖಚಿತಪಡಿಸಿ
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    df.to_csv(csv_path, index=False)
    return csv_path

def demo_csv_qa():
    """Demonstrate CSV Q&A capabilities"""
    
    # ಮಾದರಿ ಡೇಟಾಸೆಟ್ ರಚಿಸಿ
    csv_path = create_sample_dataset()
    print(f"Created sample dataset: {csv_path}")
    
    # ಪ್ರಶ್ನೋತ್ತರ ವ್ಯವಸ್ಥೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ
    qa_system = CSVQASystem()
    
    # ಡೇಟಾವನ್ನು ಲೋಡ್ ಮಾಡಿ
    if not qa_system.load_csv_data(csv_path):
        print("Failed to load CSV data")
        return
    
    print(f"\nLoaded dataset with shape: {qa_system.data.shape}")
    
    # ಉದಾಹರಣೆಯ ಪ್ರಶ್ನೆಗಳು
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
  
#### ಹಂತ 2.2: CSV ಪ್ರಶ್ನೋತ್ತರ ವ್ಯವಸ್ಥೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ

```powershell
# CSV ಪ್ರಶ್ನೆ ಮತ್ತು ಉತ್ತರ ಡೆಮೋವನ್ನು ಚಾಲನೆ ಮಾಡಿ
python samples/02-rag-solutions/csv_qa_system.py
```
  
### 3. ಪ್ರಾರಂಭಿಕ ಪ್ರಾಜೆಕ್ಟ್: 02-grounding-data ಅನ್ನು ಹೊಂದಿಸಿ (5 ನಿಮಿಷಗಳು)

#### ಹಂತ 3.1: ಸುಧಾರಿತ ಡಾಕ್ಯುಮೆಂಟ್ RAG ವ್ಯವಸ್ಥೆ

`samples/02-rag-solutions/document_rag.py` ರಚಿಸಿ:  

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
        
        # ಪ್ರಶ್ನೆಯನ್ನು ವೆಕ್ಟರೀಕರಿಸಿ
        query_vector = self.vectorizer.transform([query])
        
        # ಸಾದೃಶ್ಯಗಳನ್ನು ಲೆಕ್ಕಿಸಿ
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()
        
        # ಟಾಪ್-k ದಾಖಲೆಗಳನ್ನು ಪಡೆಯಿರಿ
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # ಕನಿಷ್ಠ ಸಾದೃಶ್ಯ ಮಿತಿ
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
        
        # ಸಂಬಂಧಿತ ದಾಖಲೆಗಳನ್ನು ಪಡೆಯಿರಿ
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
    
    # RAG ವ್ಯವಸ್ಥೆಯನ್ನು ರಚಿಸಿ
    rag_system = SimpleRAGSystem()
    
    # ಮಾದರಿ ಜ್ಞಾನ ಆಧಾರವನ್ನು ಸೇರಿಸಿ
    documents = create_sample_knowledge_base()
    rag_system.add_documents(documents)
    
    print(f"Loaded {len(documents)} documents into knowledge base")
    
    # ಉದಾಹರಣೆಯ ಪ್ರಶ್ನೆಗಳು
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
  
### 4. CLI-ನಿಂದ Azure ಗೆ ಸ್ಥಳಾಂತರ ಮಾರ್ಗವನ್ನು ತೋರಿಸಿ (5 ನಿಮಿಷಗಳು)

#### ಹಂತ 4.1: ಸ್ಥಳಾಂತರ ತಂತ್ರಗಳ ಅವಲೋಕನ

`samples/02-rag-solutions/migration_guide.py` ರಚಿಸಿ:  

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
            # ಫೌಂಡ್ರಿ ಸ್ಥಳೀಯ ಸಂರಚನೆ
            self.client = OpenAI(
                base_url="http://localhost:5273/v1",
                api_key="not-needed"
            )
            self.default_model = "phi-4-mini"
            
        elif environment == "azure":
            # ಅಜೂರ್ AI ಫೌಂಡ್ರಿ ಸಂರಚನೆ
            if not azure_endpoint or not azure_api_key:
                raise ValueError("Azure endpoint and API key required for Azure environment")
            
            self.client = OpenAI(
                base_url=f"{azure_endpoint}/openai/deployments",
                api_key=azure_api_key,
                default_headers={"api-version": azure_api_version}
            )
            self.default_model = "gpt-4"  # ಅಥವಾ ನಿಮ್ಮ ಅಜೂರ್ ನಿಯೋಜನೆ ಹೆಸರು
            
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
                # ಫೌಂಡ್ರಿ ಸ್ಥಳೀಯಕ್ಕಾಗಿ, ನಾವು ಸಾಮಾನ್ಯವಾಗಿ CLI ಅನ್ನು ಬಳಸುತ್ತೇವೆ
                # ಇದು ಸರಳೀಕೃತ ಉದಾಹರಣೆ
                return {
                    "success": True,
                    "models": ["phi-4-mini", "qwen2.5-0.5b", "deepseek-coder-1.3b"],
                    "environment": "local"
                }
            else:
                # ಅಜೂರ್‌ಗಾಗಿ, ನೀವು ನಿಯೋಜನೆಗಳ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಪ್ರಶ್ನಿಸಬಹುದು
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
    
    # ಪರೀಕ್ಷಾ ಸಂದೇಶ
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
    
    # ಫೌಂಡ್ರಿ ಸ್ಥಳೀಯದೊಂದಿಗೆ ಪರೀಕ್ಷೆ
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
    
    # ಅಜೂರ್ ಸಂರಚನೆಯನ್ನು ತೋರಿಸಿ (ಅಧಿಕಾರಪತ್ರಗಳು ಬೇಕಾಗಿರುವುದರಿಂದ ಕಾಮೆಂಟ್ ಮಾಡಲಾಗಿದೆ)
    print("\n2. Azure AI Foundry Configuration:")
    print("-" * 40)
    print("""
    # ಅಜೂರ್ AI ಫೌಂಡ್ರಿಗೆ ಸ್ಥಳಾಂತರಿಸಲು, ಕೆಳಗಿನಂತೆ ಸಂರಚಿಸಿ:
    
    azure_client = UnifiedAIClient(
        environment="azure",
        azure_endpoint="https://your-resource.openai.azure.com",
        azure_api_key="your-api-key",
        azure_api_version="2024-08-01-preview"
    )
    
    # ಎರಡೂ ಪರಿಸರಗಳಲ್ಲಿ ಒಂದೇ API ಕರೆಗಳು ಕೆಲಸ ಮಾಡುತ್ತವೆ!
    azure_result = azure_client.chat_completion(
        messages=test_messages,
        max_tokens=200,
        temperature=0.7
    )
    """)
    
    # ಸ್ಥಳಾಂತರಣಾ ತಂತ್ರ
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
    
    # ಸಂರಚನಾ ಉದಾಹರಣೆಗಳು
    print("\n4. Environment-based Configuration:")
    print("-" * 40)
    print("""
    # ಅಭಿವೃದ್ಧಿಗಾಗಿ .env ಫೈಲ್
    AI_ENVIRONMENT=local
    FOUNDRY_LOCAL_URL=http://localhost:5273/v1
    DEFAULT_MODEL=phi-4-mini
    
    # ಉತ್ಪಾದನೆಗಾಗಿ .env ಫೈಲ್
    AI_ENVIRONMENT=azure
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
    AZURE_OPENAI_API_KEY=your-api-key
    AZURE_OPENAI_API_VERSION=2024-08-01-preview
    DEFAULT_MODEL=gpt-4
    """)

if __name__ == "__main__":
    demo_migration_patterns()
```
  
#### ಹಂತ 4.2: ಸ್ಥಳಾಂತರ ಮಾದರಿಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ

```powershell
# ಮೈಗ್ರೇಶನ್ ಡೆಮೋವನ್ನು ಚಾಲನೆ ಮಾಡಿ
python samples/02-rag-solutions/migration_guide.py
```
  
## ಪ್ರಮುಖ ಸಂಪ್ರದಾಯಗಳು

### 1. ಉನ್ನತ ಪ್ರಾಂಪ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್

- **ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳು**: ಕ್ಷೇತ್ರ-ನಿರ್ದಿಷ್ಟ ತಜ್ಞ ವ್ಯಕ್ತಿತ್ವಗಳು  
- **ಗ್ರೌಂಡಿಂಗ್ ತಂತ್ರಗಳು**: ಸಂದರ್ಭ ಸಂಯೋಜನೆ ತಂತ್ರಗಳು  
- **ತಾಪಮಾನ ನಿಯಂತ್ರಣ**: ಸೃಜನಶೀಲತೆ ಮತ್ತು ಸ್ಥಿರತೆಯ ಸಮತೋಲನ  
- **ಟೋಕನ್ ನಿರ್ವಹಣೆ**: ಪರಿಣಾಮಕಾರಿ ಸಂದರ್ಭ ಬಳಕೆ  

### 2. ರಚನಾತ್ಮಕ ಡೇಟಾ ಸಂಯೋಜನೆ

- **CSV ಪ್ರೊಸೆಸಿಂಗ್**: Pandas ನೊಂದಿಗೆ AI ಮಾದರಿಗಳ ಸಂಯೋಜನೆ  
- **ಸಾಂಖ್ಯಿಕ ವಿಶ್ಲೇಷಣೆ**: ಸ್ವಯಂಚಾಲಿತ ಡೇಟಾ ಸಾರಾಂಶ  
- **ಸಂದರ್ಭ ಸೃಷ್ಟಿ**: ಪ್ರಶ್ನೆಗಳ ಆಧಾರದ ಮೇಲೆ ಡೈನಾಮಿಕ್ ಸಂದರ್ಭ ರಚನೆ  
- **ಬಹು-ರೂಪ ಬೆಂಬಲ**: JSON, CSV ಮತ್ತು ಟೇಬ್ಯುಲರ್ ಡೇಟಾ  

### 3. RAG ಅನುಷ್ಠಾನ ಮಾದರಿಗಳು

- **ವೆಕ್ಟರ್ ಹುಡುಕಾಟ**: TF-IDF ಮತ್ತು ಕೋಸೈನ್ ಸಾದೃಶ್ಯತೆ  
- **ಡಾಕ್ಯುಮೆಂಟ್ ರಿಟ್ರೀವಲ್**: ಪ್ರಾಸಂಗಿಕತೆ ಅಂಕಿಅಂಶ ಮತ್ತು ರ್ಯಾಂಕಿಂಗ್  
- **ಸಂದರ್ಭ ಸಂಯೋಜನೆ**: ಬಹು-ಡಾಕ್ಯುಮೆಂಟ್ ಸಂಶ್ಲೇಷಣೆ  
- **ಉತ್ತರ ಉತ್ಪಾದನೆ**: ಗ್ರೌಂಡೆಡ್ ಪ್ರತಿಕ್ರಿಯೆ ರಚನೆ  

### 4. ಕ್ಲೌಡ್ ಸ್ಥಳಾಂತರ ತಂತ್ರಗಳು

- **ಒಕ್ಕೂಟ APIಗಳು**: ಸ್ಥಳೀಯ ಮತ್ತು ಕ್ಲೌಡ್‌ಗೆ ಏಕ ಕೋಡ್‌ಬೇಸ್  
- **ಪರಿಸರ ಅವಲೋಕನ**: ಸಂರಚನೆ-ಚಾಲಿತ ನಿಯೋಜನೆ  
- **ವಿಕಾಸ ವರ್ಕ್‌ಫ್ಲೋ**: ಸ್ಥಳೀಯ → ಸ್ಟೇಜಿಂಗ್ → ಉತ್ಪಾದನೆ  
- **ಖರ್ಚು ಆಪ್ಟಿಮೈಜೆಷನ್**: ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿ, ಕ್ಲೌಡ್ ಉತ್ಪಾದನೆ  

## ಉತ್ಪಾದನಾ ಪರಿಗಣನೆಗಳು

### 1. ಕಾರ್ಯಕ್ಷಮತೆ ಆಪ್ಟಿಮೈಜೆಷನ್

```python
# ಉತ್ಪಾದನೆ RAG ಗಾಗಿ ಆಪ್ಟಿಮೈಸ್ ಮಾಡಿ
rag_config = {
    "max_context_docs": 5,
    "similarity_threshold": 0.15,
    "max_tokens": 1000,
    "temperature": 0.2,
    "chunk_size": 500,
    "chunk_overlap": 50
}
```
  
### 2. ದೋಷ ನಿರ್ವಹಣೆ

```python
# ಬಲವಾದ ದೋಷ ನಿರ್ವಹಣೆ
try:
    result = rag_system.generate_answer(question)
    if "error" in result:
        # ಸಾಮಾನ್ಯ ಜ್ಞಾನಕ್ಕೆ ಹಿಂತಿರುಗಿ
        fallback_result = client.chat.completions.create(
            model="phi-4-mini",
            messages=[{"role": "user", "content": question}]
        )
except Exception as e:
    # ದೋಷವನ್ನು ಲಾಗ್ ಮಾಡಿ ಮತ್ತು ಸೌಮ್ಯ ಕುಸಿತವನ್ನು ಒದಗಿಸಿ
    logger.error(f"RAG system error: {e}")
```
  
### 3. ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಗಮನಾರ್ಹತೆ

```python
# RAG ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ
metrics = {
    "retrieval_time": time.time() - start_time,
    "context_relevance": avg_similarity_score,
    "token_usage": response.usage.total_tokens,
    "user_satisfaction": feedback_score
}
```
  
## ಮುಂದಿನ ಹಂತಗಳು

ಈ ಸೆಷನ್ ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ:

1. **ಸೆಷನ್ 3 ಅನ್ವೇಷಿಸಿ**: Foundry Local ನಲ್ಲಿ ಓಪನ್-ಸೋರ್ಸ್ ಮಾದರಿಗಳು  
2. **ಉತ್ಪಾದನಾ RAG ನಿರ್ಮಿಸಿ**: Chainlit (ಸ್ಯಾಂಪಲ್ 04) ಬಳಸಿ ಅನುಷ್ಠಾನಗೊಳಿಸಿ  
3. **ಉನ್ನತ ವೆಕ್ಟರ್ ಹುಡುಕಾಟ**: Chroma ಅಥವಾ Pinecone ಜೊತೆಗೆ ಸಂಯೋಜಿಸಿ  
4. **ಕ್ಲೌಡ್ ಸ್ಥಳಾಂತರ**: Azure AI Foundry ಗೆ ನಿಯೋಜಿಸಿ  
5. **RAG ಗುಣಮಟ್ಟ ಮೌಲ್ಯಮಾಪನ**: `cd Workshop/samples;python -m session02.rag_eval_ragas` ರನ್ ಮಾಡಿ ragas ಬಳಸಿ answer_relevancy, faithfulness, ಮತ್ತು context_precision ಅಳೆಯಿರಿ  

### ಐಚ್ಛಿಕ ಸುಧಾರಣೆಗಳು

| ವರ್ಗ | ಸುಧಾರಣೆ | ಕಾರಣ | ದಿಕ್ಕು |
|----------|-------------|-----------|-----------|
| Retrieval | TF-IDF ಅನ್ನು ವೆಕ್ಟರ್ ಸ್ಟೋರ್ (FAISS / Chroma) ಮೂಲಕ ಬದಲಿಸಿ | ಉತ್ತಮ ಅರ್ಥಪೂರ್ಣ ಸ್ಮರಣೆ ಮತ್ತು ವಿಸ್ತರಣೆ | ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಚಂಕ್ ಮಾಡಿ (500–800 ಅಕ್ಷರಗಳು), ಎಂಬೆಡ್ ಮಾಡಿ, ಸೂಚ್ಯಂಕವನ್ನು ಉಳಿಸಿ |
| ಹೈಬ್ರಿಡ್ ಸೂಚ್ಯಂಕ | ದ್ವಂದ್ವ ಅರ್ಥಪೂರ್ಣ + ಕೀವರ್ಡ್ ಫಿಲ್ಟರಿಂಗ್ | ಸಂಖ್ಯಾತ್ಮಕ / ಕೋಡ್ ಪ್ರಶ್ನೆಗಳಲ್ಲಿ ನಿಖರತೆ ಸುಧಾರಣೆ | ಮೊದಲು ಕೀವರ್ಡ್ ಮೂಲಕ ಫಿಲ್ಟರ್ ಮಾಡಿ ನಂತರ ಕೋಸೈನ್ ಸಾದೃಶ್ಯತೆ ಮೂಲಕ ರ್ಯಾಂಕ್ ಮಾಡಿ |
| ಎಂಬೆಡ್ಡಿಂಗ್‌ಗಳು | ಹಲವಾರು ಎಂಬೆಡ್ಡಿಂಗ್ ಮಾದರಿಗಳನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಿ | ಪ್ರಾಸಂಗಿಕತೆ ಮತ್ತು ವೇಗದ ಮಧ್ಯೆ ಆಪ್ಟಿಮೈಸ್ ಮಾಡಿ | A/B: MiniLM vs E5-small vs ಸ್ಥಳೀಯವಾಗಿ ಹೋಸ್ಟ್ ಮಾಡಿದ ಎಂಕೋಡರ್ |
| ಕ್ಯಾಶಿಂಗ್ | ಎಂಬೆಡ್ಡಿಂಗ್‌ಗಳು ಮತ್ತು ರಿಟ್ರೀವಲ್ ಫಲಿತಾಂಶಗಳನ್ನು ಕ್ಯಾಶ್ ಮಾಡಿ | ಪುನರಾವರ್ತಿತ ಪ್ರಶ್ನೆಗಳ ವಿಳಂಬ ಕಡಿಮೆ ಮಾಡಿ | ಸರಳ on-disk pickle / sqlite ಹ್ಯಾಶ್ ಕೀ ಜೊತೆಗೆ |
| ಮೌಲ್ಯಮಾಪನ | ragas ಡೇಟಾಸೆಟ್ ವಿಸ್ತರಿಸಿ | ಸಾಂಖ್ಯಿಕವಾಗಿ ಅರ್ಥಪೂರ್ಣ ಗುಣಮಟ್ಟ | 50–100 ಪ್ರಶ್ನೋತ್ತರ + ಸಂದರ್ಭಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ; ವಿಷಯದ ಪ್ರಕಾರ ವರ್ಗೀಕರಿಸಿ |
| ಮೆಟ್ರಿಕ್ಸ್ | ರಿಟ್ರೀವಲ್ ಮತ್ತು ಉತ್ಪಾದನೆ ಸಮಯಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ | ಕಾರ್ಯಕ್ಷಮತೆ ಪ್ರೊಫೈಲಿಂಗ್ | ಪ್ರತಿ ಕರೆಗಾಗಿ `retrieval_ms`, `gen_ms`, `tokens` ಸೆರೆಹಿಡಿಯಿರಿ |
| ಗಾರ್ಡ್‌ರೈಲ್ಸ್ | ಹ್ಯಾಲುಸಿನೇಷನ್ ಫಾಲ್ಬ್ಯಾಕ್ ಸೇರಿಸಿ | ಸುರಕ್ಷಿತ ಉತ್ತರಗಳು | ನಂಬಿಕೆಯಿಂದ ಕಡಿಮೆ ಇದ್ದರೆ → ಉತ್ತರ: "ಅಪರ್ಯಾಪ್ತ ಸಂದರ್ಭ." |
| ಫಾಲ್ಬ್ಯಾಕ್ | ಸ್ಥಳೀಯ → Azure ಮಾದರಿಯ ಕ್ಯಾಸ್ಕೇಡ್ | ಸಂಯುಕ್ತ ಗುಣಮಟ್ಟ ವೃದ್ಧಿ | ಕಡಿಮೆ ನಂಬಿಕೆಯಿಂದ ಕ್ಲೌಡ್‌ಗೆ ಅದೇ OpenAI API ಮೂಲಕ ಮಾರ್ಗದರ್ಶನ |
| ನಿರ್ಧಾರಾತ್ಮಕತೆ | ಸ್ಥಿರ ಹೋಲಿಕೆ ರನ್‌ಗಳು | ಪುನರಾವರ್ತನೀಯ ಮೌಲ್ಯಮಾಪನ ಸೆಟ್‌ಗಳು | ಬೀಜ ನಿಗದಿಪಡಿಸಿ, `temperature=0`, ಸ್ಯಾಂಪ್ಲರ್ ರ್ಯಾಂಡಮ್ನೆಸ್ ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಿ |
| ಮೇಲ್ವಿಚಾರಣೆ | ಮೌಲ್ಯಮಾಪನ ರನ್ ಇತಿಹಾಸವನ್ನು ಉಳಿಸಿ | ಹಿಂಪಡೆಯುವಿಕೆ ಪತ್ತೆ | ಟೈಮ್‌ಸ್ಟ್ಯಾಂಪ್ + ಮೆಟ್ರಿಕ್ ವ್ಯತ್ಯಾಸಗಳೊಂದಿಗೆ JSON ಸಾಲುಗಳನ್ನು ಸೇರಿಸಿ |

#### ಉದಾಹರಣೆ: ರಿಟ್ರೀವಲ್ ಸಮಯ ಸೇರಿಸುವುದು

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
  
#### ragas ಬಳಸಿ ಮೌಲ್ಯಮಾಪನ ವಿಸ್ತರಣೆ

1. `question`, `answer`, `contexts`, `ground_truths` (ಪಟ್ಟಿ) ಕ್ಷೇತ್ರಗಳೊಂದಿಗೆ JSONL ರಚಿಸಿ  
2. `Dataset.from_list(list_of_dicts)` ಗೆ ಪರಿವರ್ತಿಸಿ  
3. `evaluate(dataset, metrics=[...])` ರನ್ ಮಾಡಿ  
4. ಪ್ರವೃತ್ತಿ ವಿಶ್ಲೇಷಣೆಗೆ ಮೆಟ್ರಿಕ್‌ಗಳನ್ನು (CSV/JSON) ಸಂಗ್ರಹಿಸಿ  

#### ವೆಕ್ಟರ್ ಸ್ಟೋರ್ ತ್ವರಿತ ಪ್ರಾರಂಭ (FAISS)

```python
import faiss, numpy as np
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)  # embeddings = np.array([...]) ಸಾಮಾನ್ಯೀಕೃತ
D, I = index.search(query_vec, k)
```
  
ಡಿಸ್ಕ್ ಸ್ಥಿರತೆಗಾಗಿ `faiss.write_index(index, "kb.index")` ಬಳಸಿ.

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

### ಡಾಕ್ಯುಮೆಂಟೇಶನ್
- [Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)  
- [Azure AI Foundry RAG ಮಾದರಿಗಳು](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)  
- [ಪ್ರಾಂಪ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್ ಮಾರ್ಗದರ್ಶಿ](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)  
- [Ragas ಮೌಲ್ಯಮಾಪನ ಡಾಕ್ಸ್](https://docs.ragas.io)  

### ಸ್ಯಾಂಪಲ್ ಕೋಡ್
- [Module08 Sample 04](./samples/04/README.md) - Chainlit RAG ಅಪ್ಲಿಕೇಶನ್  
- [ಉನ್ನತ ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆ](./samples/09/README.md) - ಏಜೆಂಟ್ ಸಂಯೋಜನೆ ಮಾದರಿಗಳು  

---

**ಸೆಷನ್ ಅವಧಿ**: 30 ನಿಮಿಷಗಳ ಹ್ಯಾಂಡ್ಸ್-ಆನ್ + 15 ನಿಮಿಷಗಳ ಪ್ರಶ್ನೋತ್ತರ  
**ಕಷ್ಟದ ಮಟ್ಟ**: ಮಧ್ಯಮ  
**ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು**: ಸೆಷನ್ 1 ಪೂರ್ಣಗೊಂಡಿದೆ, ಮೂಲಭೂತ ಪೈಥಾನ್ ಜ್ಞಾನ  

## ಸ್ಯಾಂಪಲ್ ದೃಶ್ಯ ಮತ್ತು ಕಾರ್ಯಾಗಾರ ನಕ್ಷೆ

| ಕಾರ್ಯಾಗಾರ ಸ್ಕ್ರಿಪ್ಟ್ / ನೋಟ್ಬುಕ್ | ದೃಶ್ಯ | ಗುರಿ | ಮುಖ್ಯ ಡೇಟಾಸೆಟ್ / ಮೂಲ | ಉದಾಹರಣಾ ಪ್ರಶ್ನೆ |
|----------------------------|----------|------|-----------------------|------------------|
| `samples/session02/rag_pipeline.py` / `notebooks/session02_rag_pipeline.ipynb` | ಆಂತರಿಕ ಬೆಂಬಲ ಜ್ಞಾನ ಆಧಾರವು ಗೌಪ್ಯತೆ + ಕಾರ್ಯಕ್ಷಮತೆ FAQಗಳಿಗೆ ಉತ್ತರ ನೀಡುತ್ತದೆ | ಎಂಬೆಡ್ಡಿಂಗ್‌ಗಳೊಂದಿಗೆ ಕನಿಷ್ಠ ಮೆಮೊರಿ RAG | ಸ್ಕ್ರಿಪ್ಟ್‌ನ `DOCS` ಪಟ್ಟಿ (5 ಚಿಕ್ಕ ಪ್ಯಾರಾಗ್ರಾಫ್‌ಗಳು) | ಸ್ಥಳೀಯ ಇನ್ಫರೆನ್ಸ್‌ಗೆ RAG ಯಾಕೆ ಬಳಸಬೇಕು? |
| `samples/session02/rag_eval_ragas.py` / `notebooks/session02_rag_eval_ragas.ipynb` | ಗುಣಮಟ್ಟ ವಿಶ್ಲೇಷಕ ಮೂಲಭೂತ ರಿಟ್ರೀವಲ್ ನಂಬಿಕೆಯಿಂದ ಮೌಲ್ಯಮಾಪನ ಮಾಡುತ್ತಾನೆ | ಸಣ್ಣ ಸಿಂಥೆಟಿಕ್ ಡೇಟಾಸೆಟ್‌ನಲ್ಲಿ ragas ಮೆಟ್ರಿಕ್‌ಗಳನ್ನು ಲೆಕ್ಕಿಸಿ | `DOCS`, `QUESTIONS`, `GROUND_TRUTH` ಸರಣಿಗಳು | ಸ್ಥಳೀಯ ಇನ್ಫರೆನ್ಸ್‌ಗೆ ಏನು ಲಾಭ? |
| `prompt_engineering.py` (ಉನ್ನತ) | ಕ್ಷೇತ್ರ SME ಬಹು-ವೆರ್ಟಿಕಲ್‌ಗಳಿಗೆ ಗ್ರೌಂಡೆಡ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ರಚಿಸುತ್ತಾರೆ | ಕ್ಷೇತ್ರ ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಟೋಕನ್ ಪ್ರಭಾವವನ್ನು ಹೋಲಿಸಿ | ಇನ್‌ಲೈನ್ `contexts` ಡಿಕ್‌ಟ್ | Foundry Local ಮಾದರಿ ಕ್ಯಾಶಿಂಗ್ ಅನ್ನು ಹೇಗೆ ನಿರ್ವಹಿಸುತ್ತದೆ? |
| `csv_qa_system.py` | ಮಾರಾಟ ಕಾರ್ಯಾಚರಣೆಗಳು ರಫ್ತುಗಳ ಮೇಲೆ ಇಂಟರಾಕ್ಟಿವ್ ವಿಶ್ಲೇಷಣೆಗಳನ್ನು ಅನ್ವೇಷಿಸುತ್ತವೆ | ಸಣ್ಣ ಮಾರಾಟ ತುಣುಕು ಸಾರಾಂಶ ಮತ್ತು ಪ್ರಶ್ನೋತ್ತರ | ರಚಿಸಲಾದ `sample_sales_data.csv` (10 ಸಾಲುಗಳು) | ಯಾವ ಉತ್ಪನ್ನಕ್ಕೆ ಗರಿಷ್ಠ ಸರಾಸರಿ ಮಾರಾಟ ಮೊತ್ತವಿದೆ? |
| `document_rag.py` | ಉತ್ಪನ್ನ ತಂಡ ಆಂತರಿಕ ವಿಕಿಗೆ ಡಾಕ್ಯುಮೆಂಟ್ RAG ಅನ್ನು ಅನ್ವೇಷಿಸುತ್ತದೆ | ಸಂಬಂಧಿತ ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ರಿಟ್ರೀವ್ ಮಾಡಿ ಉಲ್ಲೇಖಿಸಿ | `create_sample_knowledge_base()` ಪಟ್ಟಿ | ಎಡ್ಜ್ AI ಯ ಲಾಭಗಳು ಯಾವುವು? |
| `migration_guide.py` | ವಾಸ್ತುಶಿಲ್ಪಿ ಕ್ಲೌಡ್ ಸ್ಥಳಾಂತರ ಯೋಜನೆಯನ್ನು ಸಿದ್ಧಪಡಿಸುತ್ತಾರೆ | ಸ್ಥಳೀಯ→Azure API ಸಮಾನತೆಯನ್ನು ಪ್ರದರ್ಶಿಸಿ | ಸ್ಥಿರ ಪರೀಕ್ಷಾ ಪ್ರಾಂಪ್ಟ್‌ಗಳು | 2–3 ವಾಕ್ಯಗಳಲ್ಲಿ ಎಡ್ಜ್ AI ಯ ಲಾಭಗಳನ್ನು ವಿವರಿಸಿ. |

### ಡೇಟಾಸೆಟ್ ತುಣುಕುಗಳು  
ಇನ್‌ಲೈನ್ RAG ಪೈಪ್ಲೈನ್ ಡಾಕ್ಯುಮೆಂಟ್ ಪಟ್ಟಿ:  
```python
DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]
```
  
Ragas ಮೌಲ್ಯಮಾಪನ ಸತ್ಯ ಟ್ಯೂಪಲ್ಸ್:  
```python
QUESTIONS = ["What advantage does local inference offer?", "How does RAG improve answer grounding?"]
GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding."
]
```
  
### ದೃಶ್ಯ ಕಥನ  
ಬೆಂಬಲ ಎಂಜಿನಿಯರಿಂಗ್ ಗುಂಪು ಗ್ರಾಹಕ ಡೇಟಾವನ್ನು ಹೊರಗಡೆ ಬಹಿರಂಗಪಡಿಸದೆ ಆಂತರಿಕ FAQಗಳಿಗೆ ತ್ವರಿತ ಪ್ರೋಟೋಟೈಪ್ ಬೇಕು. ಸೆಷನ್ 2 ವಸ್ತುಗಳು ಕನಿಷ್ಠ ಅಸ್ಥಿರ RAG (ಸ್ಥಿರತೆ ಇಲ್ಲ) → ರಚನಾತ್ಮಕ CSV ಪ್ರಶ್ನೋತ್ತರ → ಉಲ್ಲೇಖದೊಂದಿಗೆ ಡಾಕ್ಯುಮೆಂಟ್ ರಿಟ್ರೀವಲ್ → ಗುರ್ತಿಸಿದ ಗುಣಮಟ್ಟ ಮೌಲ್ಯಮಾಪನ (ragas) → Azure ಸ್ಟೇಜಿಂಗ್‌ಗೆ ಸಿದ್ಧ ಸ್ಥಳಾಂತರ ತಂತ್ರವನ್ನು ಕ್ರಮವಾಗಿ ಅಭಿವೃದ್ಧಿಪಡಿಸುತ್ತವೆ.

### ವಿಸ್ತರಣೆ ಮಾರ್ಗಗಳು  
ಐಚ್ಛಿಕ ಸುಧಾರಣೆಗಳ ಪಟ್ಟಿಯನ್ನು ಬಳಸಿ: TF-IDF ಅನ್ನು FAISS/Chroma ಗೆ ಬದಲಿಸಿ, ಮೌಲ್ಯಮಾಪನ ಕಾರ್ಪಸ್ (50–100 ಪ್ರಶ್ನೋತ್ತರ) ವಿಸ್ತರಿಸಿ, ನಂಬಿಕೆಯಿಂದ ಕಡಿಮೆ ಇದ್ದಾಗ ದೊಡ್ಡ ಮಾದರಿಗೆ ಫಾಲ್ಬ್ಯಾಕ್ ಏರಿಸು.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->