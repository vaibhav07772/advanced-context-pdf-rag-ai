from memory import get_memory
from pdf_rag import retrieve
from tools import calculator

def build_context(query):

    context = ""

    # 🧠 Memory
    memory = get_memory()
    context += f"Chat History:\n{memory}\n"

    # 📄 PDF RAG
    docs = retrieve(query)
    context += f"Relevant PDF Knowledge:\n{docs}\n"

    # 🔧 Tool
    calc = calculator(query)
    if calc:
        context += f"Tool Result: {calc}\n"

    return context