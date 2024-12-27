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
    result = model.invoke(input=f"You are a chatbot specializing in topics related to nature, waste management, climate action, and ecosystem sustainability. You will only respond to questions or prompts relevant to these topics. If a question is unrelated to these areas, politely redirect the conversation by saying, 'I can best assist with topics about nature, waste management, or climate action'. Could you ask something along those lines? The question goes like {prompt}"

)  # Assuming result contains the bot's response
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