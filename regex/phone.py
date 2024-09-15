import re

def extract_phone_numbers(text):
    # Regex pattern for matching phone numbers (various formats)
    phone_pattern = r'(\(\d{3}\)\s?\d{3}[-.]?\d{4})|(\d{3}[-.]\d{3}[-.]\d{4})'

    # Find all phone number matches in the text
    phone_numbers = re.findall(phone_pattern, text)
    
    # Extract and return the phone numbers in a clean format
    return [match[0] if match[0] else match[1] for match in phone_numbers]
