import math

print("\nWelcome to the Coin Estimator!\n\nWould you like to use grams or pounds?\n ")
choice = int(input("1. Grams\n2. Pounds\n"))

print("\nPlease enter the total weight of each of your coins.\n")

pennies = int(input("Pennies:"))
nickels = int(input("Nickles:"))
dimes = int(input("Dimes:"))
quarters = int(input("Quarters:"))

if choice == 1:
      pennies = round(pennies / 2.5)
      nickels = round(nickels / 5)
      dimes = round(dimes / 2.268)
      quarters = round(quarters / 5.67)
else:
      pennies = round(pennies / 0.00551156)
      nickels = round(nickels / 0.0110231)
      dimes = round(dimes / 0.0050000841)
      quarters = round(quarters / 0.01250021)

print("\nYou have about", pennies, "pennies,", nickels, "nickels,", dimes,
      "dimes, and", quarters, "quarters.")

penny_rolls = math.floor(pennies / 50)
nickel_rolls = math.floor(nickels / 40)
dime_rolls = math.floor(dimes / 50)
quarter_rolls = math.floor(quarters / 40)

print("You'll need", penny_rolls, ("penny roll," if penny_rolls == 1 else "penny rolls,"),
      nickel_rolls, ("nickel roll," if nickel_rolls == 1 else "nickel rolls,"),
      dime_rolls, ("dime roll, and" if dime_rolls == 1 else "dime rolls, and"),
      quarter_rolls, ("quarter roll." if quarter_rolls == 1 else "quarter rolls."))

total_value = (penny_rolls * 50) + (nickel_rolls * 2) + (dime_rolls * 5) + (quarter_rolls * 10)

print("All of your rolls are worth $" + str(total_value) + ". \n\nSpend it wisely!")