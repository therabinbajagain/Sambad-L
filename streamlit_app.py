import streamlit as st
from rag_pipeline import *

st.set_page_config(page_title="Nepali Law AI Assistant", layout="wide")
st.title("📜 Nepali Legal RAG Assistant")

query = st.text_input("Ask a legal question:")

if query:
    index = load_vector_store("docs/vector.index")
    chunks = split_text(extract_text_from_pdf("data/Law/CON.pdf"))
    results = query_index(query, index, chunks)
    context = "\n\n".join(results)
    answer = generate_answer(query, context)

    st.markdown("### 🧠 Answer:")
    st.info(answer)

    with st.expander("📄 Retrieved Context"):
        for i, chunk in enumerate(results):
            st.markdown(f"**Chunk {i+1}:**\n{chunk}")