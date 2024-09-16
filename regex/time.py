import re

def extract_times(text):
    data = {}
    time_pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
    data['times'] = re.findall(time_pattern, text)
    return data

