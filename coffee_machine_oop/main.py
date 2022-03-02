from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
def reorder(user_choice):
    if user_choice == 'Y':
        main()
    else:
        print("thankyou")
item = Menu()
items = item.get_items()
var_for_report = CoffeeMaker()
var_for_money = MoneyMachine()
var_for_process = CoffeeMaker()
var_for_process_money = MoneyMachine()

def main():

    drink_name = str(input(f" Hello , What would you like to order: {items}").lower())
    if drink_name == 'report':
        var_for_report.report()
        var_for_money.report()
    else:
        drink = item.find_drink(drink_name)
        if var_for_process.is_resource_sufficient(drink):
            print(f"it will cost you :{drink.cost}")
            if var_for_process_money.make_payment(drink.cost):
                var_for_process.make_coffee(drink)
                user_choice = str(input("would you take another coffee? Y/N").upper())
                reorder(user_choice)
            else:
                print("you don't have enough money right now ")
                user_choice = str(input("would you like to take another coffee? Y/N").upper())
                reorder(user_choice)
        else:
            print("We don't have enough resources right now ")
            user_choice = str(input("would you like to take another coffee for which we might have resources? Y/N").upper())
            reorder(user_choice)

main()

