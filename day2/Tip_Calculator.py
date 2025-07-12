# My code
print("Welcome to the tip calculator.")
Total_Bill=float(input("What was your Total bill? $"))
Tip_perc=float(input("What percentage would you like to give tip?: "))
total_people=int(input("How many people to split the bill?: "))
Bill=((Total_Bill+ (Tip_perc/100)*Total_Bill)/total_people)
Bill=round(Bill,2)
print(f"Each person should pay: ${Bill}")


#optimized
# if the bill was $150.00, split between 5 people, with 12% Tip
# then each person should pay (150.00 /5 ) *1.12
#Round the result to 2 decimal places=33.60
print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage would you like to give tip?: "))
people=int(input("How many people to split the bill?: "))
tip_as_percent= tip/100
total_tip_amount=bill * tip_as_percent
total_bill=bill + total_tip_amount
bill_per_person = total_bill /people
final_amount=round(bill_per_person,2)           #eg:if result is 33.600, it will print only 33.6
final_amount="{:.2f}".format(bill_per_person)   #used to resolve above problem
print(final_amount)
print(f"Each person should pay ${final_amount}")
