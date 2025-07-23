# There is no blockspace in python

money=100
food=["Momo","Chowmein","Pizza"]
if money<500:
    new_food=food[0]

print(new_food)      #Throws error in c/c++ because of blockspace(new_food variable is declared within the if loop)      


#Modifying Global Scope

enemies=1               #Global Variable
def increase_enemies():
    # global enemies
    print(f"Enemies inside function: {enemies}")
    return enemies+2         
enemies=increase_enemies()
print(f"Enemies outside function: {enemies}")
# But this is not an effective way to declare any global variable inside any function, It can prone to more bugs and errors

#GLOBAL CONSTANTS

PI=3.14159 
URL="https.//www.facebook.com"

def calculate():
    print(PI)
    print(URL)
calculate()    
    