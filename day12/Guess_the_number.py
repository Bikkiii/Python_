from Art import logo
import os
import random

EASY_LEVEL=10
HARD_LEVEL=5

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') 

def difficulty():
    level=input("Choose a difficulty, 'easy' or 'hard': ").lower()
    if level=="hard":
        return HARD_LEVEL
    else:
        return EASY_LEVEL
    

def compare(user_guess,random_num,turns):
    if user_guess> random_num:
        print("Too High\nGuess Again")
        return turns-1
    elif user_guess< random_num:
        print("Too Low\nGuess Again")   
        return turns-1
    else:
        print(f"You won, the answer was {random_num}")
        
  
def game():
    print(logo)
    print("Welcome to the Number guessing game!!\nThe number is between 1 and 100")
    no_of_attempts=difficulty() 
    random_num=random.randint(1,100)
    user_guess=0
    while user_guess!= random_num:
        print(f"You have {no_of_attempts} attempts left")
        user_guess=int(input("Guess a number: "))
        no_of_attempts=compare(user_guess,random_num,no_of_attempts)
        
        if no_of_attempts==0:
            print("You have no attempts left\nYou Lose")
            
game()  