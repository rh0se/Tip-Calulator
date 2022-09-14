print("welcome to the tip calculator")
bill = input("What was the total bill? $")
bill_1 = float(bill)

percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
percent = int(percentage)

people = input("How many people to split the bill? ")
people_1 = int(people)

per = (bill_1 / people_1) * 1.10
per_formatted = format(per, ".2f")
per_float = float(per_formatted)

percent_1 = (bill_1 / people_1) * 1.12
b_formatted = format(percent_1, ".2f")
b_float = (b_formatted)

per_3 = (bill_1 / people_1) * 1.15
c_formatted = format(per_3, ".2f")
c_float = float(c_formatted)

if (percent == 10): print(f"Each person should pay: ${per_float}")
if (percent == 12): print(f"Each person should pay: ${b_float}")
if (percent == 15): print(f"Each person should pay: ${c_float}")
if(percent == 15):                                                                                        print(f"Each person should pay: ${c_float}")
