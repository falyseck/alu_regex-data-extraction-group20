import re


def extract_times(text):
    data = {}
    # Time patterns (24-hour and 12-hour formats)
    time_pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
    data['times'] = re.findall(time_pattern, text)

    return data


# Example usage
if __name__ == "__main__":
    text = """Example text with times 2:30 PM, 14:30, and 3:45 am."""
    print("Extracted times:", extract_times(text))
