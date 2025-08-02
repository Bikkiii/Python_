print("Welcome to python pizza deliveries!\n")
print("Small pizza:$15\nMedium pizza:$20\nLarge pizza:$25\n")
print("pepperoni for small pizza: +$2\npepperoni for medium or large:+$3\n\nextra cheese for any size pizza:+$1")
size=input("What size pizza do you want?, S for small,M for medium, L for large: ")
add_pepperoni=input("Do you want pepperoni?, Y or N: ")
extra_cheese=input("Do you want extra cheese? ,Y or N: ")
total_bill=0

if size == "S" :
    total_bill+=15
    if add_pepperoni == "Y":
        total_bill+=3
    if extra_cheese == "Y":
            total_bill+=1           
elif size == "M":
    total_bill+=20
    if add_pepperoni == "Y":
        total_bill+=2
    if extra_cheese == "Y":
            total_bill+=1
elif size == "L":
    total_bill+=25
    if add_pepperoni == "Y":
        total_bill+=3
    if extra_cheese == "Y":
            total_bill+=1
else:
    print("Invalid size selected!!")            
print(f"Your total bill is ${total_bill}")
    
    
#OPTIMIZED CODE BELOW    
    
# print("Welcome to Python Pizza Deliveries!\n")
# print("Small Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25")
# print("Pepperoni for small pizza: +$2")
# print("Pepperoni for medium or large pizza: +$3")
# print("Extra cheese for any size pizza: +$1\n")

# size = input("What size pizza do you want? (S for Small, M for Medium, L for Large): ").lower()
# add_pepperoni = input("Do you want pepperoni? (Y or N): ").lower()
# extra_cheese = input("Do you want extra cheese? (Y or N): ").lower()

# total_bill = 0

# # Base pizza price
# if size == "S":
#     total_bill += 15
# elif size == "M":
#     total_bill += 20
# elif size == "L":
#     total_bill += 25
# else:
#     print("Invalid size selected!")

# # Pepperoni
# if add_pepperoni == "y":
#     if size == "S":
#         total_bill += 2
#     elif size == "M" or size == "L":
#         total_bill += 3

# # Cheese
# if extra_cheese == "Y":
#     total_bill += 1

# print(f"\nYour total bill is: ${total_bill}")
                       