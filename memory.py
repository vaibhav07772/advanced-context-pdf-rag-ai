chat_memory = []

def add_memory(q, a):
    chat_memory.append((q, a))

def get_memory():
    context = ""
    for q, a in chat_memory:
        context += f"User: {q}\nAI: {a}\n"
    return context