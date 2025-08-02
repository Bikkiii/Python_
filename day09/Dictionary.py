#dictionary
# {key: value}

programming_dictionary={
"Bug": "An error in a program that prevents a program from running as expected.",
"Function": "A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over again.",
123: "A number"}

#Retrieving otems form the dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary[123]) 


#Adding new item in the dictionary
programming_dictionary["Apple"]="A fruit"
print(programming_dictionary["Apple"])

#creating an empty dictionary
empty_dictionary={}

## wipe an existing dictionary
# programming_dictionary={}
# print(programming_dictionary)

#edit an item in a dictionary
print(programming_dictionary["Bug"])
programming_dictionary["Bug"]="A Insect"
print(programming_dictionary["Bug"])

#Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
