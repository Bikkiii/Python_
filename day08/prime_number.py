n=int(input("Enter a number to check whether it is a prime number or not: "))
def prime(number):
    count=0
    for i in range(1,number+1):
        if n%i==0:
            count+=1   
            
    if count==2:
        print(f"{number} is a prime number")  
    else:      
        print(f"{number} is not a prime number")    
        
prime(n)        