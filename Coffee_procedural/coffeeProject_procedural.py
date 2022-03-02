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
    "income": 0,
}
# TODO:1 PRINT REPORT
user_choice = input("What Would you like to have?\n ESPRESSO / Latte / Cappuccino : ").lower()
while user_choice != "report" or user_choice != "end":
    check_resources = MENU[user_choice]
    print(f"cost = {MENU[user_choice]['cost']}")
    if (resources['water'] - check_resources['ingredients']['water'] > 0) and (resources['milk'] - check_resources['ingredients']['milk'] > 0) and (resources['coffee'] - check_resources['ingredients']['coffee'] > 0):
        print("please Insert Coins")
        quaters = float(input("how many quaters: "))
        dimes = float(input("how many dimes: "))
        nickel = float(input("how many nickel: "))
        penny = float(input("how many penny: "))
        sum_of_all = (quaters * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (penny * 0.01)
        if sum_of_all > (check_resources['cost']):
            resources['income'] += check_resources['cost']
            change = sum_of_all - (check_resources['cost'])
            print(f"Here is your change : {change}")
            print("enjoy your Coffee")
            user_continue = input("do you want to continue your order Y or N").upper()
            if user_continue == "Y":
                user_choice = input("What Would you like to have?\n ESPRESSO / Latte / Cappuccino : ").lower()
            else:
                user_choice = "end"

        else:
            print("you did not enter enough money to buy the drink.")
            user_choice = input("Try Something New in Budget ?\n ESPRESSO / Latte / Cappuccino : ").lower()
    else:
        print("sorry We don't Have Enough Resources.Come Back Again")
        user_choice = "end"