#CAESAR CYPHER
#Improved user experience
from caesar_art import logo
print(logo)

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
          'o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n',
          'o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(texts,shifts,directions):
    cipher_text=''
    if directions=="encode":
            shifts*=1
    else:
            shifts*=-1
    for i in texts:
        if i in alphabet:
            position=alphabet.index(i)
            new_position = position + shifts
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        else:
            cipher_text+=i   
    print(f"The {directions}d text is {cipher_text}")        

again=True
while again:
    direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift= int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(texts=text,shifts=shift,directions=direction)
    result=input("Type 'yes' if you want to go again else type 'no' ").lower()
    if result=='no':
            again=False
            print("Goodbye!!")

# again=input("Type 'yes' if you want to go again else type 'no' ").lower()
# while again=="yes":       