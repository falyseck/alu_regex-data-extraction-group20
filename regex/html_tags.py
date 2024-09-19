import re

def extract_html_tags(text):
    data = {}
    html_tag_pattern = r'<\s*([a-zA-Z]+)(?:\s[^>]*?)?\s*>'
    extracted = re.findall(html_tag_pattern, text)
    data['html_tags'] = [f'<{tag}>' for tag in extracted]
    return data

