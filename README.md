# 🧠 Nepali Legal RAG Assistant

A Retrieval-Augmented Generation (RAG) system to answer legal queries from Nepali law documents (in English) using LangChain, FAISS, and OpenAI.

## 📦 Features
- PDF ingestion and text chunking
- Semantic search with multilingual embeddings
- Query interface (CLI + Streamlit UI)
- GPT-4-powered answer generation

## 🚀 How to Run

### 1. Clone Repo & Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Add your PDF(s)
Place your PDF(s) in the `data/` directory.

### 3. Run the App
```bash
python app.py  # For CLI
streamlit run streamlit_app.py  # For web UI
```

### 4. Ask Legal Questions
Interactively ask legal questions, and the system retrieves and summarizes the most relevant law sections.

## 📁 Directory Structure
```
legal-rag-assistant/
├── data/                   # Source PDFs
├── docs/                   # Processed files
├── app.py                  # CLI-based RAG system
├── streamlit_app.py        # Streamlit UI
├── rag_pipeline.py         # Core logic
├── config.py               # Settings & API keys
├── requirements.txt
└── README.md
```