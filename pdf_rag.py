from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Global storage
index = None
chunks = []


# 📄 Read PDF
def load_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


# ✂️ Split text
def split_text(text, chunk_size=1000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


# 🧠 Create Vector DB
def create_index(text):
    global index, chunks

    chunks = split_text(text)

    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)


# 🔍 Retrieve
def retrieve(query, top_k=2):
    global index, chunks

    if index is None:
        return []

    q_vec = model.encode([query])
    q_vec = np.array(q_vec).astype("float32")

    D, I = index.search(q_vec, top_k)

    return [chunks[i] for i in I[0]]