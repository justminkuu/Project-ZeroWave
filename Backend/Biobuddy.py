from langchain_ollama import OllamaLLM
import sqlite3

model = OllamaLLM(model="llama3.2")

connection = sqlite3.connect("buddy_db.db")
cursor = connection.cursor()

while True:
    user = input("Enter message: ")
    result = model.invoke(input=user)  # Assuming result contains the bot's response
    
    # Use cursor.execute if inserting one row
    cursor.execute("""
        INSERT INTO CHATS(user, bot)
        VALUES(?,?)
    """, (user, result))
    
    # Commit changes to the database
    connection.commit()
    
    print(result)
