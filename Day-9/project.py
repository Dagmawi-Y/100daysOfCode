import os

print("Welcome to the secret auction program.")

bidders = {}  # Storing bidders as a dictionary

def secret_auction(name, bid_amount):
    bidders[name] = bid_amount  # Storing bidder's information in the dictionary
    add_another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    while add_another_bidder.lower() == "yes":
        name = input("What is the bidder's name? ")
        bid_amount = int(input("What is the bid amount? "))
        bidders[name] = bid_amount  # Storing new bidder's information
        add_another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")

    winner = max(bidders, key=bidders.get) if bidders else None
    max_bid = bidders[winner] if winner else None

    if winner:
        print(f"The winner is {winner} with a bid of {max_bid}")
    else:
        print("No bidders")

# Taking the first bidder's information
name = input("What is your name? ")
bid_amount = int(input("What is your bid amount? "))

secret_auction(name=name, bid_amount=bid_amount)
