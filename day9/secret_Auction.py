import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids ={}
bidding_finsih = False
def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if(bid_amount > highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(f"The winnner is {winner} with a bid of ${highest_bid}")



def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

while(not bidding_finsih):
    name = input("Enter your name : ")
    bid_price = int(input("Enter your bid price : $ "))
    bids[name]=bid_price
    should_continue = input('Are there any other bidders? Type "yes" or "no".')
    if should_continue == "no":
        bidding_finsih = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()