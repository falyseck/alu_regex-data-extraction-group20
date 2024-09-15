import re

def extract_data(text):
    data = {}

    # Regex pattern for matching phone numbers (various formats)
    phone_pattern = r'(\(\d{3}\)\s?\d{3}[-.]?\d{4})|(\d{3}[-.]\d{3}[-.]\d{4})'
    
    # Find all phone number matches in the text
    phone_numbers = re.findall(phone_pattern, text)
    
    # Store the extracted phone numbers in the dictionary
    # Choose the first match (from either format) for each phone number
    data['phone_numbers'] = [match[0] if match[0] else match[1] for match in phone_numbers]
    
    return data
