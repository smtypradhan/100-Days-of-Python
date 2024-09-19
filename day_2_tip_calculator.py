print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage_of_tip = tip/100*bill
bill_total = bill + percentage_of_tip
bill_per_person = bill_total / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")