import re

def extract_credit_cards(text):
    data = {}
    credit_card_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    data['credit_cards'] = re.findall(credit_card_pattern, text)
    return data

