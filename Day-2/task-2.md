    *Exercise 1 — Load PDFs*

    Use PyPDFLoader from LangChain to load 2 different PDF files of your choice (e.g., a textbook chapter, a research paper, personal notes).

    ⸻

    *Exercise 2 — Split into Chunks*

    Use RecursiveCharacterTextSplitter with chunk_size=1000 and chunk_overlap=200 to split the loaded documents into chunks.

    ⸻

    *Exercise 3 — Attach Metadata*

    For each chunk, attach the following metadata fields:
    - filename
    - page_number
    - upload_date
    - source_type (e.g., "textbook", "paper", "notes" — your choice)

    ⸻

    *Exercise 4 — Build a Filter Function*

    Write a function filter_chunks(chunks, **filters) that returns only the chunks matching the given metadata key-value pairs.

    Example usage: filter_chunks(chunks, filename="paper1.pdf", page_number=3)

    ⸻

    *Exercise 5 — Test Your Filters*

    Use the functions created and test your data

    ⸻

    *Deliverable:* A single Python file day2_document_loader.py containing the loader, splitter, metadata attachment, filter function, and test block.

    *Key takeaway:* Chunks are not just text — they carry metadata, and metadata is what makes selective retrieval possible later.

⸻
