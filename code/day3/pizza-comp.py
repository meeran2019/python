
size = input("What size pizza do you want ? S, M or L : ")
pepp = input("Do you want pepporani ? Y or N : ")
cheese = input("Do you want extra chesse ? Y or N : ")
bill = 0

if cheese == "Y":
    bill+=1

if size == "S":
    bill+=15
    if pepp == "Y":
        bill+=2
elif size == "M":
    bill+=20
    if pepp == "Y":
        bill+=3
elif size == "L":
    bill+=25
    if pepp == "Y":
        bill+=3

print(f"total bill is ${bill}")


