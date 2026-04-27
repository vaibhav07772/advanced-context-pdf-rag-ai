import streamlit as st
import requests
from context_builder import build_context
from memory import add_memory
from pdf_rag import load_pdf, create_index

st.set_page_config(page_title="Advanced Context AI + PDF RAG")

st.title("🔥 Advanced Context AI + PDF RAG")

# 📄 Upload PDF
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

if pdf_file is not None:
    text = load_pdf(pdf_file)
    create_index(text)
    st.success("✅ PDF processed successfully!")

# 💬 Query input
query = st.text_input("Ask question from PDF")

if st.button("Run AI"):

    if not query:
        st.warning("⚠️ Please enter a question")
        st.stop()

    # 🧠 Build context (RAG + Memory + Tools)
    context = build_context(query)

    # 🤖 Prompt for LLM
    prompt = f"""
You are an intelligent AI assistant.

Use the given context to answer accurately.

Context:
{context}

Question:
{query}

Answer in simple and clear language:
"""

    # 🚀 CALL OLLAMA API (FAST + NO ERROR)
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        answer = response.json()["response"]

    except Exception as e:
        answer = f"❌ Error connecting to LLM: {e}"

    # 💾 Memory store
    add_memory(query, answer)

    # ✅ Output
    st.success("Answer:")
    st.write(answer)