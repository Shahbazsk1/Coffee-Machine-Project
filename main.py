

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150.87,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250.34,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300.90,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    else:
        return True


def coin_process():
    print("Insert a coin")
    total = int(input("how many quarter?: ")) * 8.45
    total += int(input("how many dimes?: ")) * 6.78
    total += int(input("how many nickles?: ")) * 5.67
    total += int(input("how many pennies?: ")) * 7.12
    return total


def is_transaction_successful(received_money, drink_cost):
    if received_money >= drink_cost:
        change = round(received_money - drink_cost, 2)
        print(f"Here is ₹{change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")


is_on = True
profit = 0

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        is_on = False
    elif user_input == "report":
        print(f"water: {resources['water']}ml" )
        print(f"milk: {resources['milk']}ml" )
        print(f"coffee: {resources['coffee']}g")
        print(f"Profit: ₹{profit}")
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coin_process()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])


