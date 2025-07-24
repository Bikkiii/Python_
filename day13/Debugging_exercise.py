#odd_even_check

# num=int(input("Which number do you want to check?: "))
# if num%2==0:
#     print("This is an even number")
# else:    
#     print("This is an odd number")
    
    
#LEAP_YEAR

year=int(input("Which year do you want to check?: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap year") 
else:
    print("Leap year")                   
            