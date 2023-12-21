import os

print("logo")

bids = {}
bidding_finished = False


def find_highest_bidder (bidding_rec) :
    highest_bid = 0
    winner = ""
    for bidder in bidding_rec:
        bid_amount = bidding_rec[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print (f"The winner is {winner} with a bid of {highest_bid}")

while not bidding_finished:
    name = input ("Enter your name: ")
    price = int(input ("What is your bid? $ "))
    bids[name] = price

    should_continue = input ("Are there any other bidders? type 'yes' or 'no'")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system("cls")
