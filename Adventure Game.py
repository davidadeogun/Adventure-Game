#Adventure Game
#If Else statement
money = input("Do you want DOLLARS, NAIRA or POUNDS? ")

if money.upper() == "DOLLARS":
    how_much = input("Do you want MILLION, THOUSAND or HUNDRED? ")
    if how_much.upper() == "MILLION":
            print("Crpyto may be the answer!!")
    elif how_much.upper() == "THOUSAND":
            check_type = input("Do you want a MONEY-ORDER OR CHECK? ") 
            if check_type.upper() == "MONEY-ORDER":    #Gave the user the option of a money-order or check if the user selected THOUSAND
                print("Dookey Dookey Doo, you've got it!")
            else:
                print("The check will be Wells Fargo.")
    else:
        print("I will give you cash!")

elif money.upper() == "NAIRA":
    denomination = input("Do you want in COINS, PAPER or COWRY? ")
    if denomination.upper() == "COINS":
        thickess = input("Do you want THICKCOIN or BITCOIN? ")
        if thickess.lower() == "thickcoin":
                print("Horray, I got you covered.")
        else:
                print("No problem, I will give you a sack!")
    elif denomination.upper() == "PAPER":
        print("Take the paper envelope over there.")
    else:
        print("I've got enough cowries for you.")

else:
    royalty = input("Do you want the KING'S face or QUEEN'S? ")
    if royalty.upper() == "KING'S":
        print("That's got to be Prince Charles!")
    else:
        print("It's her Majesty, Queen Elizabeth!")