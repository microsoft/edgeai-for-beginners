#!/usr/bin/env python3
"""Session 2 Sample: RAG evaluation with ragas.

Demonstrates evaluating a tiny RAG pipeline using ragas metrics.
Metrics used: answer_relevancy, faithfulness, context_precision.

NOTE: This is a minimal demonstration; in real scenarios you would build a
larger evaluation dataset and possibly persist results.

Usage:
  From inside the Workshop/Samples directory, run:
    python -m session02.rag_eval_ragas

Environment Variables:
  FOUNDRY_LOCAL_ALIAS=phi-4-mini     # Model for generation
  EMBED_MODEL=sentence-transformers/... # Embedding model
  FOUNDRY_LOCAL_ENDPOINT=<url>       # Override endpoint

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
"""
from __future__ import annotations
import os
import sys
from utils.workshop_utils import get_client, chat_once

try:
    from sentence_transformers import SentenceTransformer
    from ragas import evaluate
    from ragas.metrics import answer_relevancy, faithfulness, context_precision
    from datasets import Dataset
    from langchain_openai import ChatOpenAI
except ImportError as e:
    print(f"[ERROR] Missing required package: {e}")
    print("[INFO] Install with: pip install sentence-transformers ragas datasets numpy")
    sys.exit(1)

DOCS = [
    "Foundry Local exposes an OpenAI-compatible endpoint for local model inference.",
    "RAG combines retrieval of knowledge snippets with generation to improve grounding.",
    "Local inference improves privacy and lowers latency compared to remote APIs.",
]

QUESTIONS = [
    "What advantage does local inference offer?",
    "How does RAG improve answer grounding?",
]

GROUND_TRUTH = [
    "Local inference reduces latency and preserves privacy.",
    "RAG adds retrieved context snippets to improve factual grounding.",
]

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")

try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    sys.exit(1)

embed_model_name = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
print(f"[INFO] Loading embedding model: {embed_model_name}")

try:
    embedder = SentenceTransformer(embed_model_name)
    doc_embeddings = embedder.encode(DOCS, convert_to_numpy=True, normalize_embeddings=True)
except Exception as e:
    print(f"[ERROR] Failed to initialize embedding model: {e}")
    sys.exit(1)

class LocalEmbeddings:
    def embed_documents(self, texts):
        return embedder.encode(texts, convert_to_numpy=True, normalize_embeddings=True).tolist()
    def embed_query(self, text):
        return embedder.encode([text], convert_to_numpy=True, normalize_embeddings=True)[0].tolist()

def retrieve(query: str, k: int = 2):
    q_emb = embedder.encode([query], convert_to_numpy=True, normalize_embeddings=True)[0]
    sims = doc_embeddings @ q_emb
    top_idx = sims.argsort()[::-1][:k]
    return [DOCS[i] for i in top_idx]

def generate(query: str, contexts):
    ctx = "\n\n".join(contexts)
    messages = [
        {"role": "system", "content": "Answer using ONLY the provided context."},
        {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {query}"}
    ]
    text, _ = chat_once(alias, messages=messages, max_tokens=150, temperature=0.1)
    return text

records = []
for q, gt in zip(QUESTIONS, GROUND_TRUTH):
    ctxs = retrieve(q)
    ans = generate(q, ctxs)
    records.append({
        "question": q,
        "answer": ans,
        "contexts": ctxs,
        "ground_truths": [gt],
        "reference": gt
    })

try:
    ragas_llm = ChatOpenAI(model=model_id, base_url=manager.endpoint, api_key=manager.api_key or 'not-needed', temperature=0.0, timeout=60)
    ds = Dataset.from_list(records)
    print("[INFO] Running RAGAS evaluation...")
    results = evaluate(ds, metrics=[answer_relevancy, faithfulness, context_precision], llm=ragas_llm, embeddings=LocalEmbeddings())
    print("\n[RAGAS EVALUATION RESULTS]")
    print(results)
except Exception as e:
    print(f"[ERROR] Evaluation failed: {e}")
    sys.exit(1)
