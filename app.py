from rag_pipeline import *

pdf_path = "data/Law/CON.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = split_text(text)
embeddings = embed_chunks(chunks)
index = build_vector_store(embeddings)
save_vector_store(index)

while True:
    query = input("\nEnter your legal question (or type 'exit'): ")
    if query.lower() in ["exit", "quit"]:
        break
    retrieved_chunks = query_index(query, index, chunks)
    context = "\n\n".join(retrieved_chunks)
    answer = generate_answer(query, context)
    print(f"\nAnswer:\n{answer}")