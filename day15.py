#COFFEE MACHINE PROJECT

current_water = 300
current_milk = 200
current_coffee = 100
current_amount = 0.0

while True:
    flag=True
    prompt=input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "off":
        break
    elif prompt == "report":
        print(f"Water :{current_water}")
        print(f"Milk:{current_milk}")
        print(f"Coffee:{current_coffee}")
        print(f"Money: ${current_amount}")
    else:
        if prompt=="espresso":
            if current_water<50:
                flag=False
                print("Sorry there is not enough water")
            if current_coffee<18:
                flag=False
                print("Sorry there is not enough coffee")

        elif prompt=="latte":
            if current_water<200:
                flag=False
                print("Sorry there is not enough water")
            if current_coffee<24:
                flag=False
                print("Sorry there is enough coffee")
            if current_milk<150:
                flag=False
                print("Sorry there is not enough milk")
        elif prompt=="cappuccino":
            if current_water<250:
                flag=False
                print("Sorry there is not enough water")
            if current_coffee<24:
                flag=False
                print("Sorry there is not enough coffee")
            if current_milk<100:
                flag=False
                print("Sorry there is not enough milk")

        if flag:
            penny=float(input("How many pennies? "))
            dime=float(input("How many dimes? "))
            nickel=float(input("How many nickels? "))
            quarter=float(input("How many quarters? "))

            total_cost = (penny * 0.01) +(dime * 0.10) + (nickel * 0.05) + (quarter * 0.25)
            flag=True
            change=0.0
            if prompt=="espresso" and total_cost>=1.5:
                change=total_cost-1.5
                current_amount+=1.5
                current_water-=50
                current_coffee-=18
            elif prompt=="latte" and total_cost>=2.50:
                change=total_cost-2.5
                current_amount+=2.5
                current_water-=200
                current_coffee-=24
                current_milk-=150
            elif prompt=="cappuccino" and total_cost>=3.0:
                change=total_cost-3.0
                current_amount+=3.0
                current_water-=250
                current_coffee-=24
                current_milk-=100
            else:
                flag=False
                print("Sorry there is not enough money. Money refunded")

            if flag:
                if change!=0:
                    print(f"Here is ${change} dollars in change")

                print(f"Here is your {prompt}!!! Enjoy")










