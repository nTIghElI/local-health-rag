# Local Health RAG 🏥🔒

A privacy-first, fully local Retrieval-Augmented Generation (RAG) system designed to manage personal health records without sending data to the cloud.

Built with **Python**, **ChromaDB**, and **Ollama**, this agent runs entirely on consumer hardware (tested on NVIDIA RTX 5060 Ti 16GB).

## 🚀 Features

* **100% Offline Privacy:** No API keys, no cloud data transfer. Your health data never leaves your machine.
* **Vector Memory (RAG):** Uses `all-MiniLM-L6-v2` embeddings to semantically search your records.
* **Structured Ingestion:** Includes a "Safe Ingestion" pipeline for Excel/CSV data with user-validation steps (Sanity Check) before database committal.
* **Local LLM Intelligence:** Powered by **Qwen 2.5 Coder (14B)** via Ollama for accurate, context-aware answers.

## 🛠️ Tech Stack

* **Brain (agent.py):** [Ollama](https://ollama.com) running `qwen2.5-coder:14b`
* **Memory (database.py):** [ChromaDB](https://www.trychroma.com/) (Persistent vector storage)
* **Embeddings (database.py):** `sentence-transformers/all-MiniLM-L6-v2`
* **Data Processing (ingest.py):** Pandas (for Excel/CSV ingestion)
* **Orchestrator (main.py):**

## 📦 Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/local-health-rag.git](https://github.com/YOUR_USERNAME/local-health-rag.git)
    cd local-health-rag
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Ollama**
    * Download and install [Ollama](https://ollama.com).
    * Pull the model:
        ```bash
        ollama pull qwen2.5-coder:14b
        ```

## 🖥️ Usage

### 1. The Main Agent
Start the interactive chat interface:
```bash
python main.py
