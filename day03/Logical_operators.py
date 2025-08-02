# A and B (and operator): Both A and B mus be true to result true 
# A or B (or operator): Either of A and B must be true to reult true
# !A (not operator)

age=int(input("Enter your age: "))
if age<=19 and age>=13:
    print("You are a teenager")
else:
    print("You are not a teenager!!")    


print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0

if height >= 120:
    print("You can ride rollercoaster.")
    age=int(input("Enter your age: "))
    if age < 12:
        bill=5
        print("Child tickets is $5.")
        print("\n Do you want photos?")
    elif age<=18 :
        bill=7
        print("Youth ticket is $7")
    elif age>=45 and age <= 55:         #and operator
        print("Have a free ride")    
    else:
        bill=12
        print("Adult ticket is $12")
    photo=input("Do you want a photo? Y or N: ")
    if photo=="Y"or"y":
        bill+=3
        print(f"Your total bill is ${bill}" )
    else:
        print(f"Your total bill is ${bill}")
else:
    print("You can't ride rollercoaster.")