import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("regulatory_vectors.faiss")

with open("regulatory_vectors_meta.pkl", "rb") as f:
    metadata = pickle.load(f)


def retrieve_rules(query, k=5):

    embedding = model.encode(query)

    distances, indices = index.search(
        np.array([embedding]), k
    )

    rules = []

    for i in indices[0]:
        rules.append(metadata[i]["text"])

    return rules