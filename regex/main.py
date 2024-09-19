from credit_cards import extract_credit_cards
from currency_amounts import extract_currency
from expressions import extract_data as extract_emails  # Assuming this file handles emails
from hashtags import extract_hashtags
from html_tags import extract_html_tags
from phone import extract_phone_numbers
from time import extract_times
from url import extract_urls

def main():
    text = """
    For support, email us at help@example.com. Visit our site at https://www.example.com. 

    Call us at (555) 123-4567 or pay using your credit card 4111-1111-1111-1111. 

    Our meeting is scheduled for 3:00 PM. Check our updates with #NewLaunch and prices starting at $29.99.
    """

    # Extract data
    emails = extract_emails(text)
    urls = extract_urls(text)
    phone_numbers = extract_phone_numbers(text)
    credit_cards = extract_credit_cards(text)
    times = extract_times(text)
    html_tags = extract_html_tags(text)
    hashtags = extract_hashtags(text)
    currency = extract_currency(text)

    # Print results
    print("Emails:", emails)
    print("URLs:", urls)
    print("Phone Numbers:", phone_numbers)
    print("Credit Cards:", credit_cards)
    print("Times:", times)
    print("HTML Tags:", html_tags)
    print("Hashtags:", hashtags)
    print("Currency:", currency)

if __name__ == "__main__":
    main()

