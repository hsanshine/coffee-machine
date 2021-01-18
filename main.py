from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu = Menu()  # provides all the drinks, their costs and their ingredients
my_coffee_maker = CoffeeMaker()  # manages its own resources and make me coffee by deducting on the available resources
my_money_machine = MoneyMachine()  # takes money to make a payment

close_system = False
while not close_system:
    options = my_menu.get_items()
    desire = input(f'What would you like? ({options}): ').lower()
    if desire == 'off':
        print('The coffee machine has been turned off!')
        close_system = 'True'
    elif desire == 'report':
        my_money_machine.report()
        my_coffee_maker.report()
    elif desire == 'espresso' or desire == 'latte' or desire == 'cappuccino':
        ordered_drink = my_menu.find_drink(desire)
        if my_coffee_maker.is_resource_sufficient(ordered_drink):
            if my_money_machine.make_payment(ordered_drink.cost):
                my_coffee_maker.make_coffee(ordered_drink)
    else:
        print('invalid input')

