import random
word_list=["apple","android","mango"]
word=random.choice(word_list)
print(f"the word is {word}")    #for testing

#adding "_" to each letter in the random word
display=[]
for i in word:
    display+="_"
print(display)


user_input=input("Guess the word(Enter a letter): ").lower()
#replacing "_" with the guessed letter if it matches the letter in the chosen word 
# for position in range(len(word)):
#     letter=word[position]
#     if(user_input==letter):
#         display[position]=user_input

for i in range(len(word)):
    if(user_input==word[i]):
        display[i]=user_input        
print(display)       



for i in word:
    if i==user_input:
        print("Right")
    else:
        print("Wrong")     
              
print(word)
