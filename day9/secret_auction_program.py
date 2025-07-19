from logo import logo
import os
print(logo)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

name_bid={}
def auction(names,bid_price):
    name_bid[names]=bid_price
    
again=True
while again:
    name=input("Enter your name: ")
    bid=int(input("Enter your bidding price: $"))
    auction(name,bid)
    cont = input("Are there more bidders? 'yes' or 'no': ").lower()
    clear_screen()

    if cont=="no":
        again=False
                
print(name_bid)

winner=""
highest_bid=0
for bids in name_bid:
    paisa=int(name_bid[bids])
    if highest_bid < paisa:
        highest_bid=paisa
        winner=bids
print(f"{winner} has the highest bid amount ${highest_bid}\nso {winner} has won the auction")        