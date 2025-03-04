import chromadb
import ollama

# Initialize ChromaDB memory
chroma_client = chromadb.PersistentClient(path="./ai_memory")
memory_db = chroma_client.get_or_create_collection(name="memory")


def get_embedding(text):
    """Generate embeddings using Mistral."""
    response = ollama.embeddings(model="mistral", prompt=text)
    return response["embedding"]


def store_memory(user_input, response):
    """Stores user conversations in memory."""
    memory_db.add(
        ids=[str(len(memory_db.get()["ids"]) + 1)],
        documents=[f"User: {user_input}\nAI: {response}"]
    )


def retrieve_memory(user_input):
    """Retrieves past interactions relevant to user input."""
    results = memory_db.query(
        query_embeddings=[get_embedding(user_input)],
        n_results=3
    )
    if results and "documents" in results and results["documents"]:
        return "\n".join(results["documents"])
    return ""


def chat_with_ai(user_input):
    """Processes user input and generates AI response."""
    memory = retrieve_memory(user_input)

    prompt = f"Memory: {memory}\nUser: {user_input}\nAI:"

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )["message"]["content"]

    store_memory(user_input, response)
    return response


# Run Chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("AI:", chat_with_ai(user_input))