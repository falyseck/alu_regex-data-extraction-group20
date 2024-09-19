import re

def extract_currency(text):
    data = {}
    currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    data['currency'] = re.findall(currency_pattern, text)
    return data

