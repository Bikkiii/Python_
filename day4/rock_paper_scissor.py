import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice=random.randint(0,2)

if user>=3 or user<0:
    print("Invalid Input!!")
elif user== 0 and computer_choice==1:
         print("Your Choice is :")
         print(hand[user])
         print("Computer's Choice is :")
         print(hand[computer_choice])
         print("Congrats, You Won!!")
elif user==1 and computer_choice==0:
         print("Your Choice is :")
         print(hand[user])
         print("Computer's Choice is :")
         print(hand[computer_choice])
         print("You Lost!!")        
elif user==1 and computer_choice==2:
         print("Your Choice is :")
         print(hand[user])
         print("Computer's Choice is :")
         print(hand[computer_choice])
         print("You Lost!!")
elif user==2 and computer_choice==1:
         print("Your Choice is :")
         print(hand[user])
         print("Computer's Choice is :")
         print(hand[computer_choice])
         print("Congrats, You Won!!")  
elif user==2 and computer_choice==0:
         print("Your Choice is :")
         print(hand[user])
         print("Computer's Choice is :")
         print(hand[computer_choice])
         print("You Lost!!")
elif user==0 and computer_choice==2:
         print("Your Choice is :")
         print(hand[user])
         print("Computer's Choice is :")
         print(hand[computer_choice])
         print("Congrats, You Won!!")
else:
         print("Your Choice is :")
         print(hand[user])
         print("Computer's Choice is :")
         print(hand[computer_choice])
         print("Draw!!,Both have same choices")                                        