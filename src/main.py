import os
from src.text_extraction import extract_text_tika
from src.feature_extraction import extract_important_features
from src.database import add_to_database, find_most_similar_invoice
from src.similarity import cosine_similarity_text


def main():
    """
    Main function to run the document similarity matching process.

    This function performs the following steps:
    1. Adds existing invoices from the 'data/existing_invoices' directory to the in-memory database.
    2. Processes the input invoice from the 'data/input_invoice.pdf' file.
    3. Finds and prints the most similar invoice from the database compared to the input invoice.
    """
    # Add existing invoices to database
    for file_name in os.listdir('data/existing_invoices'):
        if file_name.endswith('.pdf'):
            file_path = os.path.join('data/existing_invoices', file_name)
            text = extract_text_tika(file_path)
            features = extract_important_features(text)
            add_to_database(file_name, features)

    # Process input invoice
    input_invoice_path = 'data/input_invoice.pdf'
    input_text = extract_text_tika(input_invoice_path)
    input_features = extract_important_features(input_text)
    similar_invoice, similarity_score = find_most_similar_invoice(input_features, cosine_similarity_text)

    print(f'Most similar invoice: {similar_invoice} with similarity score: {similarity_score}')


if __name__ == '__main__':
    main()
