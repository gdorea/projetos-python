MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def tem_recursos(type_of_coffee):
    if type_of_coffee == 'espresso':
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    if type_of_coffee == 'latte':
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    if type_of_coffee == 'cappuccino':
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            return True
        else:
            return False


still_serving = True

while still_serving is True:
    coffee = input("What would you like? (espresso/latte/cappuccino)")
    if coffee == 'espresso':
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        if tem_recursos(coffee) == False:
            still_serving = False
        else:
            print("Here's your coffee.")
    elif coffee == 'latte':
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        if tem_recursos(coffee) == False:
            still_serving = False
        else:
            print("Here's your coffee.")
    elif coffee == 'cappuccino':
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        if tem_recursos(coffee) == False:
            still_serving = False
        else:
            print("Here's your coffee.")
    elif coffee == 'report':
        print(resources)
    elif coffee == 'off':
        still_serving = False

        