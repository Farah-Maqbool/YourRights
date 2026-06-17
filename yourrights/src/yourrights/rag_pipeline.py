import os
from pathlib import Path
import pdfplumber
import chromadb
from chromadb.utils import embedding_functions

LAWS_DIR = Path("data/laws")
CHROMA_DIR = Path("data/chroma_db")

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

def ingest_laws():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    # Delete and recreate to ensure fresh ingestion
    try:
        client.delete_collection("pakistan_laws")
    except:
        pass

    collection = client.get_or_create_collection(
        name="pakistan_laws",
        embedding_function=embedding_fn
    )
    if collection.count() > 0:
        print(f"Already ingested {collection.count()} chunks. Skipping.")
        return collection

    print("Starting ingestion...")

    pdf_files = list(LAWS_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDFs found in data/laws/")
        return collection

    all_chunks = []
    all_ids = []
    all_metadata = []

    for pdf_path in pdf_files:
        law_name = pdf_path.stem
        print(f"Processing {law_name}...")

        text = extract_text_from_pdf(str(pdf_path))
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            all_ids.append(f"{law_name}_{i}")
            all_metadata.append({"source": law_name})

        print(f"  {len(chunks)} chunks from {law_name}")

    batch_size = 100
    for i in range(0, len(all_chunks), batch_size):
        collection.add(
            documents=all_chunks[i:i + batch_size],
            ids=all_ids[i:i + batch_size],
            metadatas=all_metadata[i:i + batch_size]
        )

    print(f"Ingestion complete. Total chunks: {collection.count()}")
    return collection


def query_laws(query: str, n_results: int = 2) -> str:
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    collection = client.get_or_create_collection(
        name="pakistan_laws",
        embedding_function=embedding_fn
    )

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    output = ""
    for i, (doc, meta) in enumerate(zip(results["documents"][0], results["metadatas"][0])):
        output += f"[Source: {meta['source'].upper()}]\n{doc}\n\n"  # Fixed: added doc

    return output

if __name__ == "__main__":
    ingest_laws()