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


def calculate_score(cards):
    '''Take a list of cards and return the score calculated from th cards'''

    # if 11 in cards and 10 in cards and len(cards)==2:
    if sum(cards)==21 and len(cards)==2:
        return 0    
    
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        
    
    return sum(cards)


user_card=[]
computer_card=[]

for i in range(2):
    
    user_card.append(deal_card())
    computer_card.append(deal_card())
    
is_game_over=False
while not is_game_over:
     
    user_score=calculate_score(user_card) 
    computer_score=calculate_score(computer_card) 
    print(f"Your cards:  {user_card} and score is {user_score}")
    print(f"computer's first cards:  {computer_card[0]} ")

    
    if user_score==0 or computer_score ==0 or user_score>21:
        is_game_over=True
    else:
        again=input("Type 'y' to get another card  type 'n' to pass:  ")
        if again=='y':
            user_card.append(deal_card())
        else:
            is_game_over= True
        

    
# print(deal_card())
print(user_card)
print(computer_card)

