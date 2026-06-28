from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    # Ask the user for input 
    choice = input(f"What would you like? ({coffee_menu.get_items()}): ")

    if choice == 'off':
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Check if the resources are sufficient
        item_to_buy = coffee_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item_to_buy) and money_machine.make_payment(item_to_buy.cost):
            coffee_maker.make_coffee(item_to_buy)
    
