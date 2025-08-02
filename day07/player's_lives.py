import random


word_list=["apple","android","mango"]
word=random.choice(word_list)
print(f"the word is {word}")    #for testing
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6

#adding "_" to each letter in the random word
display=[]
for i in word:
    display+="_"
print(display)

end_of_game=False
while not end_of_game:
    user_input=input("Guess the word(Enter a letter): ").lower()
    #replacing "_" with the guessed letter if it matches the letter in the chosen word 
    for i in range(len(word)):
        if(user_input==word[i]):
            display[i]=user_input
        
    if(user_input not in word):
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose")
            
        
    print(stages[lives])                    
    print(display)  
    if "_" not in display:
        end_of_game=True
        print("You Win!!")
         