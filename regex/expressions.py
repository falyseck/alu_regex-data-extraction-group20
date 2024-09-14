import re 
def extract_data(text):
    data = {}
 # Email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    data['emails'] = re.findall(email_pattern, text)


    return data 