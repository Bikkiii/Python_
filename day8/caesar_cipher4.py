#CAESAR CYPHER
#Improved user experience
from caesar_art import logo
print(logo)

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
          'o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n',
          'o','p','q','r','s','t','u','v','w','x','y','z']
direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))


def caesar(texts,shifts,directions):
    if direction=="encode":
        cipher_text=''
        for i in texts:
            position=alphabet.index(i)
            new_position = position + shifts
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        print(f"The ecoded text is {cipher_text}")            
    elif direction=="decode":
        plain_text=''
        for i in texts:
            position=alphabet.index(i)
            new_position= position - shifts
            plain_text+=alphabet[new_position] 
        print(f"The decoded text is {plain_text}") 
    else:
        print("Invalid Input!!")


# def caesar(texts,shifts,directions):
#     cipher_text=''
#     if directions=="encode":
#             shifts*=1
#     else:
#             shifts*=-1
#     for i in texts:
#         position=alphabet.index(i)
                
#         new_position = position + shifts
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The {directions}d text is {cipher_text}")           
# caesar(texts=text,shifts=shift,directions=direction) 

       