# Semantic Cache Search System

This project implements a lightweight semantic search system over the 20 Newsgroups dataset.

## Features

• Sentence Transformer embeddings  
• Fuzzy clustering (C-Means)  
• Custom semantic cache (no Redis)  
• FastAPI service  
• Vector similarity retrieval  

## Architecture

Query → Embedding → Semantic Cache  
→ Cache Hit → Return result  

Cache Miss → Vector Search → Fuzzy Cluster  
→ Store in Cache → Return result

## API Endpoints

### POST /query

Input:
{
"query": "space exploration missions"
}

Output:
{
"query": "...",
"cache_hit": true,
"matched_query": "...",
"similarity_score": 0.91,
"result": "...",
"dominant_cluster": 3
}

### GET /cache/stats

Returns cache statistics.

### DELETE /cache

Clears the cache.

## Run
