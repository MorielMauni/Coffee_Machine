# Import the menu
from menu import MENU
# Import the resources
from menu import resources

# Function to check if got resources
def got_resources(drink_choice):
    """Check if there are enough resources to make the selected drink.

    Args:
        drink_choice (str): The name of the drink selected by the user.

    Returns:
        bool: True if resources are sufficient, False otherwise.
    """
    ingredients = MENU[drink_choice]["ingredients"]
    if ingredients["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
        return False
    if "milk" in ingredients and ingredients["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    if ingredients["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False

    return True

# Function for the coins
def get_coins():
    """Prompt the user to input the number of coins they are inserting.
        The coins are in NIS- New Israeli Shekel ₪

        Returns:
            int: The total amount of money inserted in shekels.
        """
    print("insert the amount of coins")
    shekel1 = int(input("How many 1₪ coins: "))
    shekel2 = int(input("How many 2₪ coins: "))
    shekel5 = int(input("How many 5₪ coins: "))
    shekel10 = int(input("How many 10₪ coins: "))
    return (shekel1 * 1) + (shekel2 * 2) + (shekel5 * 5) + (shekel10 * 10)

# ints for the money
make_cost = 0
money_earn = 0

# Machine Loop
more_drink = True
while more_drink:
    # Pick the Drink
    drink_choice = input("What would you like? espresso is 15₪, latte is 25₪, cappuccino is 30₪ ").lower()

    # If Statements for each drink
    if drink_choice in MENU:
        # Check for resources
        if got_resources(drink_choice):
            make_cost = MENU[drink_choice]["cost"]
            make_ingredients = MENU[drink_choice]["ingredients"]
            # Money
            all_coins = get_coins()
            if all_coins >= make_cost:
                # Change and earn money
                change = all_coins - make_cost
                money_earn += all_coins - change
                if change == 0:
                    print("You got the exact amount")
                else:
                    print(f"here is {change}₪ in change")
                # Deduct the ingredients from the resources
                resources["water"] -= make_ingredients["water"]
                resources["milk"] -= make_ingredients["milk"]
                resources["coffee"] -= make_ingredients["coffee"]
                print(f"here is you {drink_choice} ENJOY!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    # Off = Exit the script with code (0)
    elif drink_choice == "off":
        print("Coffee Machine Shutdown")
        print(f"Total earns are {money_earn}₪")
        exit(0)
    # While loop for maintenance
    while drink_choice == "maintenance":
        # Enter maintenance mode
        if drink_choice == "maintenance":
            print("You enter maintenance mode, here are your options:\n"
                  "'report': check the amount of ingredients you got left\n"
                  "'restock': add ingredients as you like  \n"
                  "'get_money': take the money out of the machine\n"
                  "'return': return to selection mode")
            maintenance = input("Pick one of the above or type 'return' to go to the drink section: ")
        # Report = Show the current resource values
            if maintenance == "report":
                print(f"You got \nWater {resources["water"]} \nMilk {resources["milk"]} \nCoffee {resources["coffee"]} \nMoney {money_earn}₪")
            # Restock = add water, milk and coffee to the Machine
            elif maintenance == "restock":
                restock_water = int(input("Amount of watter to add? "))
                resources["water"] += restock_water
                restock_milk = int(input("Amount of milk to add? "))
                resources["milk"] += restock_milk
                restock_coffee = int(input("Amount of coffee to add? "))
                resources["coffee"] += restock_coffee
                print(f"You added \n{restock_water} amount of water \n{restock_milk} amount of milk \n{restock_coffee} amount of coffee")
            # Get the money of the machine
            elif maintenance == "get_money":
                print(f"total earn for now is {money_earn}₪")
                money_earn = 0
                print(f"take earns, money in machine is {money_earn}₪")
            # Return to go back to the Coffee Machine Selection
            elif maintenance == "return":
                drink_choice = True