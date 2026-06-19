import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

print("Loading metadata...")

df = pd.read_csv("metaData.csv")

# Better retrieval representation
texts = (
    df["document"].fillna("").astype(str)
    + " "
    + df["section"].fillna("").astype(str)
    + " "
    + df["topic"].fillna("").astype(str)
    + " "
    + df["text"].fillna("").astype(str)
).tolist()

print(f"Total Chunks: {len(texts)}")

print("Loading embedding model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Creating embeddings...")

embeddings = model.encode(
    texts,
    batch_size=32,
    show_progress_bar=True
)

embeddings = np.array(
    embeddings
).astype("float32")

print("Building FAISS index...")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    "faiss.index"
)

with open("metadata.pkl", "wb") as f:
    pickle.dump(df, f)

print("=" * 50)
print("FAISS Index Created Successfully")
print(f"Vectors Stored: {index.ntotal}")
print("=" * 50)
