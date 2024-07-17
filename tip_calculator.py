#Just a simple tip calculator that I have learned to program during my course

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill CZK?"))
print(type(bill))
tip = int(input("How much tip would you like to give? 25, 50, 100 or 200?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip + bill
#print(bill_with_tip)
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print (f"Each person should pay: {final_amount}")
