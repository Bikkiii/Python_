from Art import logo 
from Art import vs
from Game_data import data
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear' )
 
def format_data(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f" {name}, {description},{country}"

def compare(guess,a,b):
    a_count=int(a['follower_count'])
    b_count=int(b['follower_count'])
    
    if (guess=="a" and a_count >= b_count) or (guess=="b" and b_count >= a_count):
        return True
    else:
        return False
    
    # if a_count>b_count:
    #     if guess=="a":
    #         return True
    #     else:
    #         return False

def game():    
    is_game_over=False 
    score=0    
    b=random.choice(data)   
    print(logo)
    while not is_game_over:
        
        a=b
        b=random.choice(data)
        
        if a==b:
            b=random.choice(data)

        print(f"compare A: {format_data(a)}")
        print(vs)
        print(f"Against B: {format_data(b)}")

        guess=input("\nWho has more followers? 'A' or 'B': ").lower()
        is_correct=compare(guess,a,b)

        clear_screen()
        print(logo)
        if is_correct:
            score += 1
            print(f"\nYou're Right and your current score is {score}\n")
        else:
            print(f"\nSorry, That's wrong!!! and the final score is {score}")
            is_game_over=True
    feri_khelne=input("Do you like to play again? type 'y' or 'n': ").lower()        
    if feri_khelne=="y":
        game()
             
game()        
clear_screen() 
            
    
    





    
    