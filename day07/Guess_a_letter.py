import random
word_list=["apple","android","mango"]
word=random.choice(word_list)
user_input=input("Guess the word(Enter a letter): ").lower()


for i in word:
    if i==user_input:
        print("Right")
    else:
        print("Wrong")    
# j=0
# while j <= len(word)-1:
#         if(user_input==word[j]):
#             print("Right")
#         else:
#             print("Wrong")    
#         j+=1    
              
print(word)
