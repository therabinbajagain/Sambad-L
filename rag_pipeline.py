import os
import fitz  # PyMuPDF
import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from config import *

model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join(page.get_text() for page in doc)

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    return splitter.split_text(text)

def embed_chunks(chunks):
    return model.encode(chunks)

def build_vector_store(embeddings):
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def save_vector_store(index, path='docs/vector.index'):
    faiss.write_index(index, path)

def load_vector_store(path='docs/vector.index'):
    return faiss.read_index(path)

def query_index(query, index, chunks, top_k=5):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in I[0]]

def generate_answer(query, context):
    prompt = f"""You are a legal assistant. Use the context to answer the question below:

Context:
{context}

Question: {query}
Answer:"""
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()