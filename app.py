import streamlit as st
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("models/gemini-2.5-flash")

index = faiss.read_index("faiss.index")

with open("metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

embedder = SentenceTransformer("all-MiniLM-L6-v2")

st.title("DefenceRAG Assistant")

question = st.text_input("Ask a question")

if st.button("Generate Answer"):

    q_emb = embedder.encode([question])

    D, I = index.search(
        np.array(q_emb).astype("float32"),
        5
    )

    context = "\n".join(
        str(metadata.iloc[idx]["text"])
        for idx in I[0]
    )

    prompt = f"""
    Use only the context.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = model.generate_content(prompt)

    st.subheader("Answer")
    st.write(response.text)

    st.subheader("Sources")

    for idx in I[0]:
        st.write(
            f"{metadata.iloc[idx]['document']} | {metadata.iloc[idx]['section']}"
        )
