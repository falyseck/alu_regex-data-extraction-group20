import re
def extract_data(text):
    data = {}
# Regex pattern for matching URLs
url_pattern = r'\b(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?\b'
# Find all matches in the text
urls = re.findall(url_pattern, text)
