# 🔥 Advanced Context AI + PDF RAG System

An intelligent AI system that combines **PDF-based knowledge retrieval (RAG)**, **memory**, and **LLM (Ollama - Llama3)** to answer user questions using uploaded documents.

---

## 🧠 Project Overview

This project is a **Retrieval-Augmented Generation (RAG) system** where:

- 📄 User uploads a PDF
- ✂️ Text is extracted and split into chunks
- 🧠 Embeddings are created using Sentence Transformers
- 🔍 FAISS is used for fast similarity search
- 💬 User questions are answered using retrieved PDF context + memory
- 🤖 LLM (Llama3 via Ollama API) generates final response

---

## ⚙️ Tech Stack

- Python 🐍
- Streamlit (Frontend UI)
- SentenceTransformers (Embeddings)
- FAISS (Vector Search)
- PyPDF (PDF processing)
- Ollama LLM (Llama3)

---

## 📁 Project Structure

ADVANCED-CONTEXT-PDF-AI/
│── app.py # Main Streamlit app
│── pdf_rag.py # PDF processing + vector DB (FAISS)
│── context_builder.py # Builds AI context (RAG + memory + tools)
│── memory.py # Chat memory system
│── tools.py # Calculator tool
│── requirements.txt # Dependencies


---

## 🚀 How It Works

### 1️⃣ PDF Upload
User uploads a PDF file.

### 2️⃣ Text Extraction
PyPDF extracts text from all pages.

### 3️⃣ Chunking
Text is split into smaller chunks (~1000 chars).

### 4️⃣ Embedding Generation
SentenceTransformer converts chunks into vectors.

### 5️⃣ FAISS Indexing
Vectors are stored in FAISS for fast similarity search.

### 6️⃣ Question Answering Flow
When user asks a question:

- Chat memory is added
- Relevant PDF chunks are retrieved (RAG)
- Calculator tool is checked
- Final context is created

### 7️⃣ LLM Response
Context + question is sent to Llama3 (Ollama API)
→ AI generates final answer

---

## 🧠 Key Features

✔ PDF-based AI Q&A  
✔ RAG (Retrieval-Augmented Generation)  
✔ Chat memory system  
✔ Tool integration (calculator)  
✔ Fast vector search using FAISS  
✔ Local LLM (Ollama - no API cost)

---

## 💬 Example Use Cases

- Ask questions from textbooks 📚
- Summarize research papers 📄
- Understand notes instantly 🧠
- Solve math expressions ➗
- AI study assistant 🤖

---

## ⚡ Run Project

```bash
pip install -r requirements.txt
streamlit run app.py


Make sure Ollama is running:
ollama run llama3


🔥 Author

Built by Vaibhav Singh
AI/ML + NLP Engineer in progress 🚀

📌 Future Improvements
ChatGPT-style UI
Multi-PDF support
Streaming responses
Faster FAISS optimization
Deployment on cloud (AWS / Render)
=======
# advanced-context-pdf-rag-ai
An AI-powered PDF Question Answering system using RAG, FAISS, SentenceTransformers, and Llama3 (Ollama) with memory and tool integration.
