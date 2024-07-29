database = {}
"""
In-memory database to store invoice features.
Each key represents an invoice ID, and the value is the features extracted from the corresponding invoice.
"""


def add_to_database(invoice_id, features):
    """
    Adds an invoice's features to the in-memory database.

    Args:
        invoice_id (str): Unique identifier for the invoice.
        features (dict): Extracted features from the invoice.
    """
    database[invoice_id] = features


def find_most_similar_invoice(input_invoice_features, similarity_func):
    """
    Finds the most similar invoice in the database compared to the input invoice features.

    Args:
        input_invoice_features (dict): Extracted features from the input invoice.
        similarity_func (callable): Function to calculate the similarity between two sets of features.

    Returns:
        tuple: A tuple containing the ID of the most similar invoice and the similarity score.
    """
    max_similarity = 0
    most_similar_invoice = None
    for invoice_id, features in database.items():
        similarity = similarity_func(
            ' '.join(input_invoice_features['keywords']),
            ' '.join(features['keywords'])
        )
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_invoice = invoice_id
    return most_similar_invoice, max_similarity
