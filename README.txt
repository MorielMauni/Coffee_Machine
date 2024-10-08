Coffee Machine Project

Overview
This is a simple Python-based coffee machine simulation. The coffee machine offers three types of drinks (espresso, latte, and cappuccino), checks for ingredient availability, handles coin inputs, and manages resources. It also supports viewing reports of resources and restocking the machine.

Features
- Offers three drinks: espresso, latte, and cappuccino.
- Checks if the machine has enough resources (water, milk, coffee) to make the selected drink.
- Accepts input for coins and returns change if the user inserts more money than required.
- Allows the user to view a report of the current resources.
- Supports restocking of the machine by adding more water, milk, and coffee.
- Can be turned off by entering "off".

How to Run the Program

Prerequisites
- Python 3. x installed on your system.

Steps to Run:
  1. Clone the repository from GitHub:
     git clone https://github.com/MorielMauni/Coffee_Machine.git

 2. Navigate to the project folder:
    cd Coffee_Machine

 3. Run the `machine.py` file to start the coffee machine:
    python machine.py

4. Follow the on-screen prompts to:
- Select a drink.
- Insert coins.
- View the current resources (`report`).
- Restock the machine (`restock`).
- Turn off the machine (`off`).

How the Program Works

Drink Choices:
When prompted, you can choose one of the following drinks:
- `espresso`: Costs 15₪
- `latte`: Costs 25₪
- `cappuccino`: Costs 30₪

The machine will check if it has enough water, milk, and coffee for the selected drink.

Inserting Coins:
You'll be asked how many coins you want to insert in denominations of 1₪, 2₪, 5₪, and 10₪. The total amount will be calculated and checked against the drink's cost. If the amount is insufficient, the money will be refunded.

Viewing the Report:
Type `report` to view the current levels of water, milk, coffee, and the total amount of money earned.

Restocking the Machine:
Type `restock` to add more water, milk, and coffee to the machine. You'll be prompted to input the amount of each resource you want to add.

Turning Off the Machine:
To turn off the machine, type `off`. This will stop the program and shut down the coffee machine.

Notes:
- Restock the machine as needed to avoid running out of ingredients.
- You can only select drinks the machine has sufficient resources to make.

Contact
If you have any questions or encounter issues, please contact me at morielmauni@gmail.com or through GitHub.
