import re


def extract_features(text):
    """
    Extracts keywords from the provided text using regular expressions.

    Args:
        text (str): The text content from which to extract keywords.

    Returns:
        list: A list of keywords extracted from the text.
    """
    keywords = re.findall(r'\b\w+\b', text.lower())
    return keywords


def extract_important_features(text):
    """
    Extracts important features from the text, including invoice number, date, amounts, and keywords.

    Args:
        text (str): The text content of the invoice.

    Returns:
        dict: A dictionary containing the extracted features:
            - 'invoice_number' (str or None): The invoice number extracted from the text.
            - 'date' (str or None): The date extracted from the text.
            - 'amounts' (list): A list of amounts extracted from the text.
            - 'keywords' (list): A list of keywords extracted from the text.
    """
    invoice_number = re.search(r'invoice\s*#\s*(\d+)', text, re.IGNORECASE)
    date = re.search(r'\d{2}/\d{2}/\d{4}', text)
    amounts = re.findall(r'\$\s?\d+\.?\d*', text)
    return {
        'invoice_number': invoice_number.group(1) if invoice_number else None,
        'date': date.group(0) if date else None,
        'amounts': amounts,
        'keywords': extract_features(text)
    }
