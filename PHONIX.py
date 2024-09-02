# PHONIX
# MADE by 5odead

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

# File to store number history
history_file = "Number_History.txt"

# Function to save number to history file
def save_to_history(number):
    with open(history_file, "a") as file:
        file.write(number + "\n")

number = input("Enter Your Number With Country Code: ");    #User Input For Number

number = (number.replace('-', ''));
number = (number.replace('(', ''));
number = (number.replace(')', ''));
number = (number.replace(' ', ''));

## Information Retrieving
def process():
    ch_nmbrs = phonenumbers.parse(number, None) #Number and No Country Assumptions
    print("Country Name:",geocoder.description_for_number(ch_nmbrs, "en"))  #Output in English
    service_nmbr = phonenumbers.parse(number, "RO")
    print("Carrier Name:",carrier.name_for_number(service_nmbr, "en"));

## Fixing "+"
if number[0] == "+":
    save_to_history(number)
    process();
else:   #Concatenates a Plus Sign when needed
    number = "+" + number
    save_to_history(number)
    process();
