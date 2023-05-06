from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffeemaker = CoffeeMaker()
money_machine =MoneyMachine()
menu =Menu()

is_on =True

#while loop
while is_on:
    options =menu.get_items();
    selected_option  = input(f"what do you want to drink {options} :").lower()
    if selected_option == "off":
        is_on = False
    elif selected_option == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        drink =menu.find_drink(selected_option)
        if(drink):
            if(coffeemaker.is_resource_sufficient(drink)):
                cost = drink.cost
                if( money_machine.make_payment(cost)):
                    coffeemaker.make_coffee(drink)












drink = Menu()
print(drink.get_items())