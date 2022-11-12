def convert_name(letter):
    if letter == "j":
        return "jack"
    if letter == "q":
        return "queen"
    if letter == "k":
        return "king"
    if letter == "a":
        return "ace"
    return letter

def convert_suite(letter):
    if letter == "H":
        return "hearts"
    if letter == "D":
        return "diamonds"
    if letter == "C":
        return "clubs"
    if letter == "S":
        return "spades"