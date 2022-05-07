
print("Welcome to Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

print(name1)
print(name2)

combined_name_l = name1 + name2 
combined_name = combined_name_l.upper()

print(combined_name)
true_count = 0
love_count=0

for i in combined_name:
    print(i)
    if i == "T" or i=="R" or i=="U" or i=="E":
        true_count+=1
print(true_count)        
        
for i in combined_name:
    print(i)
    if i == "L" or i=="O" or i=="V" or i=="E":
        love_count+=1
print(love_count)       
print(f"Total count is {true_count}{love_count}")
total_count_str=str(true_count)+str(love_count)
total_count_int = int(total_count_str)
print(total_count_int)
if total_count_int <=10 or total_count_int >=90: 
    print(f"Your score is {total_count_int}, you go together like coke and mentos.")
elif total_count_int >=40 and total_count_int <=50: 
    print(f"Your score is {total_count_int}, you are alright together.")
else: 
    print(f"Your score is {total_count_int}.")

