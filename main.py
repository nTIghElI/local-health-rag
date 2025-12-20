import database
import agent
import uuid # Standard library for generating unique IDs

def add_new_record():
    """Helper to add data manually via console"""
    text = input("\nEnter the health record text: ")
    # Create a random ID so we don't have to think of one
    record_id = str(uuid.uuid4())
    database.save_memory(text, record_id)
    print("Record saved!")

def query_system():
    """The main RAG loop"""
    question = input("\nWhat would you like to know? ")
    
    # 1. Retrieve Context (The "R" in RAG)
    retrieved_info = database.recall_memory(question, n_results=2)
    
    # Flatten the list of strings into one big text block
    context_block = "\n".join(retrieved_info)
    
    # 2. Generate Answer (The "G" in RAG)
    answer = agent.generate_response(question, context_block)
    
    print("\n--- ANSWER ---")
    print(answer)
    print("--------------")

def main():
    while True:
        print("\n=== PERSONAL HEALTH AGENT ===")
        print("1. Add a new memory")
        print("2. Ask a question")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            add_new_record()
        elif choice == '2':
            query_system()
        elif choice == '3':
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()