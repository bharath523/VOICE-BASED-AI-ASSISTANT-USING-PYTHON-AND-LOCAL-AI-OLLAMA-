import ollama

def ask_ai(text):
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant."},
            {"role": "user", "content": text}
        ]
    )
    return response["message"]["content"]
