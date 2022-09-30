#This program will return the exact amount each person on a table should pay, tip included
print("Wecolme to the tip calculator")
totalBill = float(input("What was the total bill? $"))
tipPercentage = int(input("What percentage tip would you like to give? 10 ,12 or 15?"))
pplOnTable = int(input("How many people to split the bill?"))

totalAfterTip = totalBill + (totalBill * (tipPercentage / 100))
totalPerPerson = round(totalAfterTip / pplOnTable,2)
finalAmount = "{:.2f}".format(totalPerPerson)

print(f"Each person should pay ${finalAmount}")
