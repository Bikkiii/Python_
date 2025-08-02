import random
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';',
           '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the PyPassword Generator")
let = int(input("How many letters would you like in your password?: "))
sym = int(input("How many symbols would you like?: "))
num = int(input("How many numbers would you like?: "))


#easy password
# password=""  #empty string

# for i in range(1,let+1):  
#     random_char=random.choice(letters)
#     password = password + random_char
    

# for i in range(1,sym+1):  
#     random_char=random.choice(symbols)
#     password = password + random_char

# for i in range(1,num+1):  
#     random_char=random.choice(numbers)
#     password = password + random_char

# print(password)

#hard passwords

password_list=[]

for i in range(1,let+1):  
    password_list.append(random.choice(letters))
    

for i in range(1,sym+1):  
    random_char=random.choice(symbols)
    password_list+=random_char

for i in range(1,num+1):  
    random_char=random.choice(numbers)
    password_list+= random_char

print(password_list)

random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+= char
    
print(f"Your password is: {password}")    