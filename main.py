from art import logo, win
import re
import os

# control variables
bid_log = {}
continue_bidding = True
bids = []

# keep asking until no more bidders
while continue_bidding:
  print(logo)
  print("Welcome to the Silent Auction program!\n")
  name = input("What's your name?  ").capitalize()
  bid = float(input("What's your bid?  $"))
  bid_log[name] = bid
  bids.append(bid)

  # determine if program should keep asking for input
  valid_repeat_input = False
  while not valid_repeat_input:
    repeat = input("Are there any other bidders? Type 'y' for yes or 'n' for no.  ").lower()
    # if yes, clear the screen to keep it 'blind'
    if repeat == "y":
      os.system("clear")
      valid_repeat_input = True
      # if no, exit loop
    elif repeat == "n":
      continue_bidding = False
      valid_repeat_input = True
    else:
      print("Sorry only 'y' or 'n' are accepted.")
  

# calculate winner and input info
winning_bid = max(bids)

for name, bid in bid_log.items():
    if bid == winning_bid:
        os.system("clear")
        print(f"\nThe winner is {name} with a bid of ${bid}.\n\n")
        print(win)