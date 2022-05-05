''' e.g. The year 2000:
2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.
'''

input_year = int(input("Enter the year: "))
if input_year%4 == 0: 
    if input_year%100 == 0:
        if input_year%400 == 0:
            print("leap year")
        else:
            print("Not a leap year")
    else: 
        print(" leap year")
else: 
    print("not a leap year.")
