#!/usr/bin/env python3
"""Session 2 Sample: Minimal RAG pipeline using Foundry Local + in-memory embeddings.

Steps:
  1. Bootstrap model via FoundryLocalManager
  2. Build embedding index with sentence-transformers
  3. Retrieve top-k docs using vector similarity
  4. Generate grounded answer with retrieved context

Produces a JSON-like result with retrieved doc ids and answer text.

Usage:
    From inside the Workshop/Samples directory, run:
        python -m session02.rag_pipeline

Environment Variables:
  FOUNDRY_LOCAL_ALIAS=phi-4-mini           # Model for generation
  EMBED_MODEL=sentence-transformers/...    # Embedding model
  RAG_QUESTION="Your question"             # Test question
  FOUNDRY_LOCAL_ENDPOINT=<url>             # Override endpoint

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
"""
from __future__ import annotations
import os
import sys
from typing import List, Dict, Any
from utils.workshop_utils import get_client, chat_once

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)

DOCS = [
    "Foundry Local provides an OpenAI-compatible local inference endpoint.",
    "Retrieval Augmented Generation (RAG) improves answer grounding by injecting relevant context passages.",
    "Edge AI reduces latency and preserves privacy by executing models locally.",
    "Small Language Models can achieve competitive quality with reduced resource usage.",
    "Vector similarity search retrieves semantically relevant documents for a query.",
]

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")

try:
    _, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    sys.exit(1)

embed_model_name = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
print(f"[INFO] Loading embedding model: {embed_model_name}")

try:
    embedder = SentenceTransformer(embed_model_name)
    doc_embeddings = embedder.encode(DOCS, convert_to_numpy=True, normalize_embeddings=True)
    print(f"[INFO] Indexed {len(DOCS)} documents")
except Exception as e:
    print(f"[ERROR] Failed to initialize embedding model: {e}")
    sys.exit(1)

def retrieve(query: str, k: int = 3) -> List[int]:
    q_emb = embedder.encode([query], convert_to_numpy=True, normalize_embeddings=True)[0]
    sims = doc_embeddings @ q_emb
    top_idx = sims.argsort()[::-1][:k]
    return top_idx.tolist()

def answer(query: str) -> Dict[str, Any]:
    """Generate answer using RAG pipeline.
    
    Args:
        query: User question
    
    Returns:
        Dictionary with query, answer, retrieved doc indices, and token usage
    """
    try:
        idxs = retrieve(query)
        context = "\n\n".join(f"Doc {i}: {DOCS[i]}" for i in idxs)
        messages = [
            {"role": "system", "content": "Use ONLY the provided context to answer. If insufficient, say you are unsure."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ]
        text, usage = chat_once(alias, messages=messages, max_tokens=250, temperature=0.2)
        return {
            "query": query,
            "answer": text,
            "retrieved": idxs,
            "usage": getattr(usage, 'total_tokens', None) if usage else None
        }
    except Exception as e:
        print(f"[ERROR] RAG pipeline failed: {e}")
        raise

if __name__ == "__main__":
    test_q = os.getenv("RAG_QUESTION", "Why use RAG with local inference?")
    print(f"[INFO] Processing query: {test_q}")
    try:
        result = answer(test_q)
        print("\n[RESULT]")
        print(f"Query: {result['query']}")
        print(f"Retrieved docs: {result['retrieved']}")
        print(f"Answer: {result['answer']}")
        if result['usage']:
            print(f"Tokens used: {result['usage']}")
    except Exception as e:
        print(f"[ERROR] Failed to generate answer: {e}")
        sys.exit(1)
