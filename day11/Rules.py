############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    '''returns a random card from the deck of the cards'''
    card= random.choice(cards)
    return card

user_card=[]
computer_card=[]

for i in range(2):
    new_card= deal_card()
    user_card.append(new_card)
    computer_card.append(new_card)
    
# print(deal_card())
print(user_card)
print(computer_card)

