# function to check card number
def validate_card(card_number):
    # check length and digits only
    if len(card_number) == 16 and card_number.isdigit():
        return "Card number is valid."
    else:
        return "Invalid card number."

# function to check expiry date
def validate_expiry(expiry):
    # expiry should be in MM/YY format
    if len(expiry) == 5 and expiry[2] == "/":
        mm, yy = expiry.split("/")
        if mm.isdigit() and yy.isdigit():
            mm = int(mm)
            # month should be between 1 and 12
            if 1 <= mm <= 12:
                return "Expiry date is valid."
    return "Invalid expiry date."

# demo run with sample values
cards = [
    ("1234567890123456", "12/25"),   # valid
    ("12345abc90123457", "11/23"),   # invalid card
    ("1234567890123458", "13/25"),   # invalid month
    ("1234567890123459", "1225"),    # wrong format
]

# loop through test cases
for card, exp in cards:
    print("Card:", card, "| Expiry:", exp)
    print(" ->", validate_card(card))
    print(" ->", validate_expiry(exp))