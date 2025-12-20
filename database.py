import chromadb
from chromadb.utils import embedding_functions

# --- CONFIGURATION ---
DB_PATH = "./my_local_memory"
COLLECTION_NAME = "HealthData"

# --- INITIALIZATION ---
# 1. Setup the Librarian (Embedding Function)
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# 2. Setup the Client (The Database)
client = chromadb.PersistentClient(path=DB_PATH)

# 3. Setup the Collection (The Folder)
collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=ef
)

# --- FUNCTIONS ---

def save_memory(text, unique_id):
    """
    Saves a piece of text (e.g., a diagnosis) to the database.
    """
    print(f"[Database] Saving: '{text}'...")
    collection.add(
        documents=[text],
        ids=[unique_id]
    )

def recall_memory(query_text, n_results=1):
    """
    Searches for the most similar text in the database.
    Returns a list of strings (the found documents).
    """
    print(f"[Database] Searching for context related to: '{query_text}'...")
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    
    # Chroma returns a list of lists (because you can query multiple things at once).
    # We just want the first list of documents found.
    return results['documents'][0]