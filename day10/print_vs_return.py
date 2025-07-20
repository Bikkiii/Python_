#calculator1

# from Art import logo
# print(logo)

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def div(n1,n2):
    return n1/n2

def mul(n1,n2):
    return n1*n2

operations = {
    "+":add,
    "-":sub,
    "/":div,
    "*":mul 
    }

num1=int(input('What is the first number?: '))
for symbol in operations:
    print(symbol)
what=input("Which operation do you want to do from above?: ")
num2=int(input('What is the second number?: '))
calculation=operations[what]
result=calculation(num1,num2)
       
    
print(f"{num1} {what} {num2} = {result}")

what=input("Pick another operation: ")
num3=int(input("What is the next number?: "))
calculation=operations[what]
second_result=calculation(result,num3)

print(f"{result} {what} {num3} = {second_result}")
