# enemies=1

# def increase_enemies():
#     enemies=2
#     print(f"Enemies inside function: {enemies}")
# increase_enemies()
# print(f"Enemies outside function: {enemies}")


# LOCAL SCOPE

def increase_enemies():
    enemies=2
    print(f"Enemies inside function: {enemies}")
increase_enemies()
# print(f"Enemies outside function: {enemies}")     #Throws error


# GLOBAL SCOPE

enemies=1               #Global Variable
def increase_enemies():
    # enemies=2         #Local Variable
    print(f"Enemies inside function: {enemies}")
increase_enemies()
print(f"Enemies outside function: {enemies}")
