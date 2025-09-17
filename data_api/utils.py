import matplotlib.pyplot as plt
from io import BufferedReader
from typing import Any, List
import faiss
from numpy.typing import ArrayLike
import numpy as np
import pandas


class Embedding:
    def __init__(self, vector: ArrayLike, chunk_text: str, meta: dict = {}) -> None:
        self.vector = vector
        self.chunk_text = chunk_text.replace("\n", " ")
        self.meta = meta


def plot_string_lengths(strings: list[str]):
    lengths = [len(s) for s in strings]

    bins = [0, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

    # Step 3: Plot histogram with custom bins
    plt.figure(figsize=(10, 6))
    counts, edges, patches = plt.hist(lengths, bins=bins, edgecolor="black")

    # Step 4: Labeling
    plt.title("Distribution of String Lengths (Grouped)")
    plt.xlabel("String length (characters)")
    plt.ylabel("Count")

    # Nice x-axis labels (ranges instead of raw bin edges)
    bin_labels = [f"{edges[i]}–{edges[i+1]}" for i in range(len(edges)-1)]
    plt.xticks(
        [(edges[i]+edges[i+1])/2 for i in range(len(edges)-1)],
        bin_labels,
        rotation=45
    )
    print()

# def indexation(embeddings:list[Embedding]):
#     _embeddings = np.array([e.vector for e in embeddings], dtype="float32")
#     d = _embeddings.shape[1]
#     index = faiss.IndexFlatL2(d)
#     index.add(_embeddings)


def embeddings_to_csv(embeddings: list[Embedding], name="words", base_path="store/"):
    embedding_dicts = [
        {"vector": e.vector, "text": e.chunk_text, "meta": e.meta} for e in embeddings]
    pandas.DataFrame(embedding_dicts).to_csv(
        f"{base_path}{name}.csv", index=False)


def embeddings_from_csv(name="test", base_path=""):
    df = pandas.read_csv(f"{base_path}{name}.csv")
    return [Embedding(eval(e["vector"]), e["text"], eval(e["meta"])) for e in df.to_dict("records")]
