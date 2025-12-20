import ollama

# --- CONFIGURATION ---
# We use the model you just pulled
MODEL_NAME = "qwen2.5-coder:14b" 

def generate_response(user_question, context_text):
    """
    Constructs a prompt with the retrieved context and sends it to the LLM.
    """
    
    # 1. Build the prompt (The "Prompt Engineering" part)
    # We strictly tell the model to use the context.
    prompt = f"""
    You are a helpful personal health assistant.
    
    HERE IS THE CONTEXT I FOUND IN MY MEMORY:
    {context_text}
    
    USER QUESTION:
    {user_question}
    
    INSTRUCTION:
    Answer the user's question using ONLY the context provided above. 
    If the context doesn't contain the answer, say "I don't have that information in my records."
    """

    print(f"[Agent] Thinking with {MODEL_NAME}...")
    
    # 2. Call Ollama
    response = ollama.chat(model=MODEL_NAME, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    # 3. Return the text content of the response
    return response['message']['content']