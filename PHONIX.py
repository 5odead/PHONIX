# PHONIX
# MADE 5odead

## Imports
import phonenumbers
from phonenumbers import geocoder, carrier

banner = """
██████  ██   ██  ██████  ███    ██ ██ ██   ██
██   ██ ██   ██ ██    ██ ████   ██ ██  ██ ██
██████  ███████ ██    ██ ██ ██  ██ ██   ███
██      ██   ██ ██    ██ ██  ██ ██ ██  ██ ██
██      ██   ██  ██████  ██   ████ ██ ██   ██
"""
print(banner)

## File to store number history
history_file = "Number_History.txt"

## Function to save number to history file
def save_to_history(number):
    with open(history_file, "a") as file:
        file.write(number + "\n")

number = input("Enter Your Number With Country Code: ")  # User Input For Number

# Sanitize input
number = (number.replace('-', ''))
number = (number.replace('(', ''))
number = (number.replace(')', ''))
number = (number.replace(' ', ''))

# Ensure the number starts with a '+' for international format
if not number.startswith('+'):
    number = '+' + number

## Information Retrieving
def process():
    try:
        ch_nmbrs = phonenumbers.parse(number, None)  # Number and No Country Assumptions
        print("Country Name:", geocoder.description_for_number(ch_nmbrs, "en"))  # Print in English
        service_nmbr = phonenumbers.parse(number, None)  # Carrier Name Analysis
        print("Carrier Name:", carrier.name_for_number(service_nmbr, "en"))  # Print Carrier Name
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error: Invalid phone number format. {e}")

## Validation
try:
    ch_nmbrs = phonenumbers.parse(number, None)  # Number and No Country Assumptions
    if phonenumbers.is_valid_number(ch_nmbrs):
        save_to_history(number)
        process()
    else:
        raise ValueError("Invalid phone number format or incorrect number.")
except Exception as e:
    print(f"Error: {e}")
