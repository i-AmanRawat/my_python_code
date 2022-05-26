from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

ison = True
while ison:
    choice = input(f"What would you like to have {menu.get_items()} ?")

    if choice == "off":
        ison = not ison

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
