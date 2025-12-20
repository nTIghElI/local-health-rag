import pandas as pd
import database
import os
import uuid

def ingest_excel(file_path):
    print(f"\n--- READING FILE: {file_path} ---")
    
    # 1. Load the data
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 2. The Sanity Check List
    memories_to_save = []
    
    print("\n--- PREVIEWING DATA (SANITY CHECK) ---")
    for index, row in df.iterrows():
        # Construct the "Memory" sentence from the columns
        # You can adjust this string format based on your columns
        memory_text = (
            f"On {row['Date']}, {row['Metric']} was {row['Value']} {row['Unit']}. "
            f"Notes: {row['Notes']}"
        )
        
        unique_id = str(uuid.uuid4())
        memories_to_save.append((unique_id, memory_text))
        
        # Print the check
        print(f"Row {index + 1}: {memory_text}")

    # 3. User Confirmation
    print(f"\n-----------------------------------------")
    print(f"Found {len(memories_to_save)} valid records.")
    confirm = input("Do these look correct? Type 'yes' to save to database: ").lower()

    if confirm == 'yes':
        print("\n--- INGESTING... ---")
        for unique_id, text in memories_to_save:
            database.save_memory(text, unique_id)
        print("Success! All records added to memory.")
    else:
        print("Operation cancelled. Nothing was saved.")

if __name__ == "__main__":
    # Point this to your actual file
    file_path = "./documents/health_log.xlsx"
    
    if os.path.exists(file_path):
        ingest_excel(file_path)
    else:
        print(f"Could not find file at: {file_path}")
        print("Please create an Excel file with columns: Date, Metric, Value, Unit, Notes")