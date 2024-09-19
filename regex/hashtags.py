import re

def extract_hashtags(text):
    data = {}
    hashtag_pattern = r'\B#[\w-]+\b'
    data['hashtags'] = re.findall(hashtag_pattern, text)
    return data

