from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print report
# check resources sufficient?
# process coins
# check transaction successful?
# make coffee

choice = input("What would you like? (latte/espresso/cappuccino)")
# choice = CoffeeMaker()
if choice == 'report':
    choice.report()
