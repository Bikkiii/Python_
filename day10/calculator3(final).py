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
def calculator():
    
    num1=int(input('What is the first number?: '))
    for symbol in operations:
        print(symbol)


    next=True 
    while next:
        what=input("Which operation do you want to do from above?: ")
        num2=int(input('What is the second number?: '))
        calculation=operations[what]
        result=calculation(num1,num2)
        print(f"{num1} {what} {num2} = {result}")
        
        again=input("type 'y' to continue or 'n' to new calculator: ").lower()
        
        if again== 'y':
            num1=result
        else:
            next= False
            calculator()
            
