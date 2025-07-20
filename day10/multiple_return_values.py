# def output():
#     result=1+2
#     return result       #result of 'result' is stored in output()
#     # print("Hello")      will not be printed

# print(output())

def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "You did not enter valid input"
    formatted_f_name=f_name.title()     #Keeps first letter of f_name capital
    formatted_l_name=l_name.title()     #Keeps first letter of l_name capital
    return(f"{formatted_f_name} {formatted_l_name}")
     
# first=input("Enter your first name: ") 
# last=input("Enter your last name: ")
# print(format_name(f_name=first,l_name=last))
print(format_name(input("What is your first name: "),
    input("What is last first name: ")))