from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def cosine_similarity_text(text1, text2):
    """
    Computes the cosine similarity between two text documents using TF-IDF vectorization.

    Args:
        text1 (str): The first text document.
        text2 (str): The second text document.

    Returns:
        float: The cosine similarity score between the two text documents, where a value of 1.0 means identical documents.
    """
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    return cosine_similarity(vectors)[0][1]


def jaccard_similarity(set1, set2):
    """
    Computes the Jaccard similarity between two sets.

    Args:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        float: The Jaccard similarity score between the two sets, where a value of 1.0 means the sets are identical.
    """
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0
