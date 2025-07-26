from Data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_suff(order_ingredients):
    '''To check if there is enough resources or not'''
    for item in order_ingredients:
        if order_ingredients[item]> resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True
    
def coins():
    '''Returns the total calculated money from coins inserted'''
    print("Please Insert coins.")    
    total=int(input("How many quaters?: ")) *0.25
    total+=int(input("How many dimes?: ")) *0.1
    total+=int(input("How many nickles?: ")) *0.05
    total+=int(input("How many pennies?: ")) *0.01
    return total

def is_transaction_succ(money_received, drink_cost):
    '''Return true when the payment is accepted or false if the money is insufficient'''
    if money_received >= drink_cost:
        change=round(money_received - drink_cost, 2)
        global profit
        profit+=drink_cost
        print(f"Here is a change of ${change}")
        return True
    else:
        print("Sorry that's not enough money, MOney is refunded")
        return False
    
def make_coffee(drink_name,order_ingredients):
    '''deduct the required ingredients from the resources'''
    
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your coffee 🍵🍵")    

profit=0
is_on=True

while is_on:
    user_input=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input=="off":
        is_on=False
    elif user_input=="report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}gm")
        print(f"Money:${profit}")
    else:
        drink=MENU[user_input]
        if is_resource_suff(drink["ingredients"]):
            payment=coins()
            if is_transaction_succ(payment,drink["cost"]):
                make_coffee(user_input,drink["ingredients"])
            
            