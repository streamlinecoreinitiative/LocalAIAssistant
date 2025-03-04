import chromadb

# Initialize local database
chroma_client = chromadb.PersistentClient(path="./ai_memory")
memory_db = chroma_client.get_or_create_collection(name="memory")

def store_memory(user_input, response):
    """Stores AI interactions in ChromaDB."""
    memory_db.add(
        ids=[str(len(memory_db.get()["ids"]) + 1)],
        documents=[f"User: {user_input}\nAI: {response}"]
    )

def retrieve_memory():
    """Retrieves stored interactions."""
    results = memory_db.get()
    if results and "documents" in results and results["documents"]:
        return "\n".join(results["documents"][-5:])  # Get last 5 messages
    return ""

print("Memory system initialized.")