#sum of all even number from 1 to 100(also include 1 and 100)

sum1=0
for i in range(1,101):
    if i%2==0:
        print(i)
        sum1+=i
print(f"The total sum of even numbers form 1 to 100 is {sum1}")    

sum2=0
for i in range(2,101,2):
    sum2+=i    
print(f"The total sum of even numbers form 1 to 100 is {sum2}")    
    