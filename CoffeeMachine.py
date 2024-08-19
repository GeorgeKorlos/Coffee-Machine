from menu import MENU, resources

def report():
    return f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}"

def check_resources(MENU, resources, selected_drink):
    ingredients_needed = MENU[selected_drink]['ingredients']
    for ingredient, amount in ingredients_needed.items():
        if resources[ingredient] < amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total_amount 

def check_transaction(selected_drink, total_amount):
    drink_cost = MENU[selected_drink]['cost']
    if total_amount < drink_cost:
        print("Sorry, not enough money.")
        return False
    elif total_amount > drink_cost:
        change = round(total_amount - drink_cost, 2)
        print(f"Here is ${change} in change.")
    return True

def make_coffee(selected_drink):
    ingredients_needed = MENU[selected_drink]['ingredients']
    for ingredient, amount in ingredients_needed.items():
        resources['ingredient'] -= amount  
    print(f"Here is your {selected_drink}. Enjoy!")

machine_on = True
while machine_on:
    user_input = input("What would you like? (Espresso/Latte/Cappuccino): ").capitalize()
    if user_input == 'Off':
        machine_on = False
    elif user_input == 'Report':
        print(report())
    elif user_input in MENU:
        if check_resources(MENU, resources, user_input):
            total_amount = process_coins()
            if check_transaction(user_input, total_amount):
                make_coffee(user_input)
    else:
        print("Sorry, we don't have that option.")
