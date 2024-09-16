import re

def extract_credit_cards(text):
    data = {}
    # Credit card number patterns (with optional separators)
    credit_card_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    data['credit_cards'] = re.findall(credit_card_pattern, text)
    
    return data

# Example usage
if __name__ == "__main__":
    text = """Example text with credit card numbers 1234 5678 9012 3456 and 9876-5432-1098-7654."""
    print("Extracted credit card numbers:", extract_credit_cards(text))

