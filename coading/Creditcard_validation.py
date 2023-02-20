import re

def validate_credit_cards():
    # Define the regular expression pattern for a valid credit card number
    pattern = re.compile(r'^([456]\d{3})(-?\d{4}){3}$')
    # Define the regular expression pattern for consecutive repeated digits
    repeat_pattern = re.compile(r'(\d)\1{3,}')
    # Loop through each credit card cvnumber entered by the user and validate it using the patterns
    while True:
        card = input("Enter a credit card number (or 'q' to quit): ")
        if card == 'q':
            break
        if pattern.match(card) and not repeat_pattern.search(card):
            print('Valid')
        else:
            print('Invalid')
validate_credit_cards()

