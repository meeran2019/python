print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill ? "))
total_tip = int(input("what percentage of tip you would like to give ? "))
total_people = int(input("How many people to split the bill ? "))

print(total_bill)
print(total_tip)
print(total_people)

tip = total_bill * (total_tip/100)
total_amount = ( total_bill + tip ) / total_people
amount = round(total_amount,2)
print(f"Each person should pay: ${amount}")