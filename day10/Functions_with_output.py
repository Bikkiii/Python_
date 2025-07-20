# def output():
#     result=1+2
#     return result       #result of 'result' is stored in output()

# print(output())

def format_name(f_name,l_name):
    formatted_f_name=f_name.title()     #Keeps first letter of f_name capital
    formatted_l_name=l_name.title()     #Keeps first letter of l_name capital
    return(f"{formatted_f_name} {formatted_l_name}")
    # print(f"{f_name} {l_name}")
     
     
# first=input("Enter your first name: ").capitalize()   
# last=input("Enter your last name: ").capitalize()
first=input("Enter your first name: ") 
last=input("Enter your last name: ")
print(format_name(f_name=first,l_name=last))
