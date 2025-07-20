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
num2=int(input('What is the second number?: '))
for symbol in operations:
    print(symbol)
what=input("Which operation do you want to do from above?: ")
calculation=operations[what]
result=calculation(num1,num2)


# if what=="+":
#     result=add(num1,num2)
# elif what=="-":
#     result=sub(num1,num2)
# elif what=="/":
#     result=div(num1,num2)
# elif what=="*":
#     result=mul(num1,num2)
# else:
#     print("invalid input!!")   
    #   exit()           
    
print(f"{num1} {what} {num2} = {result}")