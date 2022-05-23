MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money" : 0
}

def update_report(choice):   #kitna dudh paani or coffe bachi hai and kitna chanda katha kr liya hai 
    resources['water'] = resources['water'] - MENU[choice]['ingredients']['water']
    resources['milk'] = resources['milk'] - MENU[choice]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[choice]['ingredients']['coffee']
    resources["money"] = resources["money"] + MENU[choice]['cost']

    # print("I m a report function")

def display_report ():
    print("Water : ", resources['water'])
    print("Milk : ", resources['milk'])
    print("Coffee : ",  resources['coffee'])
    print("Money : ",  resources['money'])

def check_resources(choice):  #dudh paani or coffe pure hai ya nahi 
    if (MENU[choice]['ingredients']['water'] > resources['water']):
        print("Sorry there is not enough water.")
        return 0
    elif (MENU[choice]["ingredients"]["milk"] > resources["milk"]):
        print("Sorry there is not enough milk.")
        return 0
    elif (MENU[choice]['ingredients']['coffee'] > resources['coffee']):
        print("Sorry there is not enough coffee")
        return 0
    return 1
    # print("I m a resouring checking function")


def process_coin(choice):     #calculate monetary value of the coins inserted 
    print("Please insert coins.")
    q = int (input("Quarter : "))
    d = int (input("Dimes : "))
    n = int (input("Nickel : "))
    p = int (input("Pennies : "))
    given = round(q*0.25 + d*0.1 + n*0.05 + p*0.01 , 3)
    # print (given)
    transaction_successful(given)
    # print("I will calculate kya aapne pure paise diye")


def transaction_successful(given):   #pure paise diye ya nahi , agr jaada diye toh offer change
    if given > MENU[choice]['cost'] :
        change = given - MENU[choice]['cost']
        print(f"Here is ${change} dollars in change.")
        make_coffee(choice)
        update_report(choice)
      
    elif given == MENU[choice]['cost'] :
        # continue
        make_coffee(choice)
        update_report(choice)
        pass

    elif given < MENU[choice]['cost'] :
        print("Sorry that's not enough money. Money refunded")

    # print("I will monitor the transaction")

def make_coffee(choice): 
    print(f"Here is your {choice}☕️. Enjoy!!")
    # print("I will serve you")


#main
off = False
while (not off):
    choice = input ("What would you like? (espresso/latte/cappuccino):")
    if (choice == 'espresso'):
        if check_resources(choice) == 0:
            continue
        process_coin(choice)
        # print("i will make espresso")
        
    elif (choice == 'latte'):
        if check_resources(choice) == 0:
            continue
        process_coin(choice)
        # print("i will make latte")

    elif (choice == 'cappuccino'):
        if check_resources(choice) == 0:
            continue
        process_coin(choice)
        # print("i will make cappuccino")

    elif (choice == 'report'):
        display_report()
        # print("i will show you report")
    
    else :
        off = True
     
