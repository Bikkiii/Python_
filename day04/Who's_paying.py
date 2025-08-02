import random
names_string= input("Give me everybody's names, separated by a comma. ")
names= names_string.split(", ")

length=len(names)
a=random.randint(0,length-1) 
b=names[a]
print(b + " is going to pay the bill ")



# import random
# names_string= input("Give me everybody's names, separated by a comma. ")
# names= names_string.split(", ")

# random_names=random.choice(names)
# print(random_names + " is going to pay the bill ")