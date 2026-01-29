print("This is a menu driven fast food order system. \n")
print('''Press 1 to order a Sandwich
Press 2 to order a Pizza
Press 3 to order a Burger''')
num = int(input("Press the number to order your desired fast food: "))
match num:
    case 1:
        print('''\nPress G to order Grilled Sandwich
Press V to order Veg Sandwich''')
        sand = input("Enter the Code to order your desired Sandwich.")
        match sand:
            case 'G':
                print("Thankyou for ordering a Grilled Sandwich. Collect your order from the counter when called.")
            case 'V':
                print("Thankyou for ordering a Veg Sandwich. Collect your order from the counter when called.")
            case _:
                print("Invalid Code")
    case 2:
        print('''\nPress 1 to order Thin Crust Pizza
Press 2 to order Cheese Burst Pizza
Press 3 to order Fresh Dough Pizza''')
        pizza = int(input("Enter the Code to order your desired Pizza."))
        match pizza:
            case 1:
                print("Thankyou for ordering a Thin Crust Pizza. Collect your order from the counter when called.")
            case 2:
                print("Thankyou for ordering a Cheese Burst Pizza. Collect your order from the counter when called.")
            case 3:
                print("Thankyou for ordering a Fresh Dough Pizza. Collect your order from the counter when called.")
            case _:
                print("Invalid Code")

    case 3:
        print('''\nPress 1 to order Veg Burger
Press 2 to order Aloo Tikki Burger
Press 3 to order Sam Burger
Press 4 to order Cheese Burger''')
        burg = int(input("Enter the Code to order your desired Burger."))
        match burg:
            case 1:
                print("Thankyou for ordering a Veg Burger. Collect your order from the counter when called.")
            case 2:
                print("Thankyou for ordering a Aloo Tikki Burger. Collect your order from the counter when called.")
            case 3:
                print("Thankyou for ordering a Sam Burger. Collect your order from the counter when called.")
            case 4:
                print("Thankyou for ordering a Cheese Burger. Collect your order from the counter when called.")
            case _:
                print("Invalid Code")
