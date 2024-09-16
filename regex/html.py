import re

def extract_data(text):
    data = {}

    p_tag_pattern = r"<p>(.*?)<\/p>"
    p_tags = re.findall(p_tag_pattern, text)
    data['p_tags'] = p_tags

    div_tag_pattern = r'<div\s+class="example">(.*?)<\/div>'
    div_tags = re.findall(div_tag_pattern, text)
    data['div_tags'] = div_tags

    img_tag_pattern = r'<img\s+src="[^"]"\s+alt="[^"]"\s*\/?>'
    img_tags = re.findall(img_tag_pattern, text)
    data['img_tags'] = img_tags

    hashtag_pattern = r"#\w+"
    hashtags = re.findall(hashtag_pattern, text)
    data['hashtags'] = hashtags

    currency_pattern = r"\$\d{1,3}(,\d{3})*(\.\d{2})?"
    currency_matches = re.findall(currency_pattern, text)
    data['currency_amounts'] = currency_matches

    return data