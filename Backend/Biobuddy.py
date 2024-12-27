from langchain_ollama import OllamaLLM
import sqlite3
from flask import Flask, request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.route('/', methods=['POST'])
def chat():  
    model = OllamaLLM(model="llama3.2")
    connection = sqlite3.connect("buddy_db.db")
    cursor = connection.cursor()
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS CHATS(
                   user text not null,
                   bot text not null
                   )
        """)
    data = request.json
    prompt = data.get('user')
    result = model.invoke(input=prompt)  # Assuming result contains the bot's response
    print(result)
    # Use cursor.execute if inserting one row
    cursor.execute("""
        INSERT INTO CHATS(user, bot)
        VALUES(?,?)
    """, (prompt, result))
    
    # Commit changes to the database
    connection.commit()
    return ''

if __name__=="__main__":
    app.run(debug=True)