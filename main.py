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

MONETARY_VALUE = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01,
}

user_input = ''

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def print_report():
    print('Water: {remaining_water_ml}ml'.format(remaining_water_ml=resources['water']))
    print(f"Milk: {resources['milk']}ml")
    print('Coffee: {remaining_coffee_g}g'.format(remaining_coffee_g=resources['coffee']))
    print(f'Money: ${round(profit, 2)}')


def are_resources_sufficient(user_choice):
    if user_input in MENU:
        for ingredient in MENU[user_choice]['ingredients']:
            if resources[ingredient] < MENU[user_choice]['ingredients'][ingredient]:
                print('Sorry there is not enough {ingredient}.'.format(ingredient=ingredient))

                return False

            return True

    return


def process_coins():
    print('Please insert coins.')
    quarters_inserted_value = int(input('How many quarters?: ')) * MONETARY_VALUE['quarters']
    dimes_inserted_value = int(input('How many dimes?: ')) * MONETARY_VALUE['dimes']
    nickles_inserted_value = int(input('How many nickles?: ')) * MONETARY_VALUE['nickles']
    pennies_inserted_value = int(input('How many pennies?: ')) * MONETARY_VALUE['pennies']

    return quarters_inserted_value + dimes_inserted_value + nickles_inserted_value + pennies_inserted_value


def was_transaction_successful():
    if total_monetary_value >= MENU[user_input]['cost']:
        global profit
        profit += MENU[user_input]['cost']

        if total_monetary_value > MENU[user_input]['cost']:
            change = total_monetary_value - MENU[user_input]['cost']

            print('Here is ${0:.{1}f} dollars in change.'.format(change, 2))

        return True

    print('Sorry that\'s not enough money. Money refunded.')

    return False


def make_coffee(user_choice):
    for ingredient in MENU[user_choice]['ingredients']:
        resources[ingredient] -= MENU[user_input]['ingredients'][ingredient]

    print(f'Here is your {user_input} ☕. Enjoy!')


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): ” [DONE]
#              - a. Check the user’s input to decide what to do next. [COMPLETED]
#              - b. The prompt should show every time action has completed, e.g. once the drink is
#                    dispensed. The prompt should show again to serve the next customer. [COMPLETED]

# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
#              - a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#                   the machine. Your code should end execution when this happens. [COMPLETED]

while user_input != 'off':
    user_input = input('What would you like? (espresso/latte/cappuccino): ')

    # TODO: 3. Print report. [DONE]
    #              - a. When the user enters “report” to the prompt, a report should be generated that shows
    #                    the current resource values. e.g.
    #                    Water: 100ml
    #                    Milk: 50ml
    #                    Coffee: 76g
    #                    Money: $2.5
    #                    [COMPLETED]
    if user_input == 'report':
        print_report()

    # TODO: 4. Check resources sufficient? [DONE]
    #             - a. When the user chooses a drink, the program should check if there are enough
    #                   resources to make that drink. [COMPLETED]
    #             - b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    #                   not continue to make the drink but print: “Sorry there is not enough water.” [COMPLETED]
    #             - c. The same should happen if another resource is depleted, e.g. milk or coffee. [COMPLETED]
    else:
        if are_resources_sufficient(user_input):
            # TODO: 5. Process coins. [COMPLETED]
            #              - a. If there are sufficient resources to make the drink selected, then the
            #                    program should prompt the user to insert coins. [COMPLETED]
            #              - b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies =
            #                    $0.01 [COMPLETED]
            #              - c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes,
            #                    1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52 [COMPLETED]
            total_monetary_value = process_coins()

            # TODO: 6. Check transaction successful? [DONE]
            #              - a. Check that the user has inserted enough money to purchase the drink they
            #                    selected. E.g Latte cost $2.50, but they only inserted $0.52 then after
            #                    counting the coins the program should say “Sorry that's not enough money.
            #                    Money refunded.”. [COMPLETED]
            #              - b. But if the user has inserted enough money, then the cost of the drink gets
            #                    added to the machine as the profit and this will be reflected the next time
            #                    “report” is triggered. E.g.
            #                    Water: 100ml
            #                    Milk: 50ml
            #                    Coffee: 76g
            #                    Money: $2.5
            #                    [COMPLETED]
            #              - c. If the user has inserted too much money, the machine should offer change.
            #                    E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2
            #                    decimal places. [COMPLETED]
            if was_transaction_successful():
                # TODO: 7. Make Coffee. [DONE]
                #              - a. If the transaction is successful and there are enough resources to make
                #                    the drink the user selected, then the ingredients to make the drink
                #                    should be deducted from the coffee machine resources.
                #                    E.g. report before purchasing latte:
                #                    Water: 300ml
                #                    Milk: 200ml
                #                    Coffee: 100g
                #                    Money: $0
                #                    Report after purchasing latte:
                #                    Water: 100ml
                #                    Milk: 50ml
                #                    Coffee: 76g
                #                    Money: $2.5
                #                    [COMPLETED]
                #              - b. Once all resources have been deducted, tell the user “Here is your
                #                    latte. Enjoy!”. If latte was their choice of drink. [COMPLETED]
                make_coffee(user_input)
