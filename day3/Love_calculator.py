print("Welcome to Love calculator")
name1 = input("What is your name? \n")
name2 = input("What is his/her name? \n")

print("Your name is " + name1)
print("His/her name is " + name2)

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true = t+r+u+e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love= l+o+v+e

love_score= int(str(true)+str(love))

print(love_score)

if (love_score<100) or (love_score>90):
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif (love_score>=40) and (love_score<=50):
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")