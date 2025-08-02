weight=float(input("What is your weight in kg?: "))
height=float(input("What is your height in m?: "))

BMI= round(weight/(height**2))

if BMI < 18.5:
    print(f"your BMI is {BMI}, You are under weight")
elif BMI < 25:
    print(f"your BMI is {BMI}, You have normal weight")
elif BMI < 30:
    print(f"your BMI is {BMI}, You are over weight")
elif BMI < 35:
    print(f"your BMI is {BMI}, You are obese")
else:
    print(f"your BMI is {BMI}, You are clinically obese")        
            
