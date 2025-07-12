#BMI=Weight(kg)/height^2 (m)
#its unit is kg/m^2
#under_Weight(BMI<18.5)
#Normal_Weight(18.5<BMI<25)
#over_Weight(BMI>18.5)

weight=float(input("Enter your weight in kg: "))
Height=float(input("\nEnter your Height in m: "))

BMI=weight/(Height**2)
print(BMI)