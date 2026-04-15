Exercise 1 — Store Chunks in a Vector Database

Reuse the chunked documents from your Day 2 work. Use OllamaEmbeddings with the nomic-embed-text model to generate embeddings, and store the chunks in a *ChromaDB* vector store.

⸻

Exercise 2 — Build a Semantic Retriever

Create a retriever from the ChromaDB vector store that returns the *top-k* most semantically similar chunks for a given query. Test it with a sample question relevant to your documents.

⸻

Exercise 3 — Build a RAG Chain

Build a simple RAG chain that:
- Takes a user question
- Retrieves the top chunks using your semantic retriever
- Stuffs them into a prompt template with {context} and {question}
- Sends the prompt to ChatOllama (model: qwen2.5:1.5b) and returns the generated answer

⸻

Exercise 4 — Test with Multiple Questions

Ask at least *3 different questions* about your documents. For each, print the question, the retrieved chunks, and the generated answer.
