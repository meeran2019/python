
number_ip = int(input("Enter the number: "))

if number_ip%2 == 0:
    print("This is an even number")
else: 
    print("This is odd number")

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_r = round((weight/(height**2)),0)   # retuns 29.0 
# bmi_r = round((weight/(height**2)))   # retuns 29 


bmi=int(bmi_r)


if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >=25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >=30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
