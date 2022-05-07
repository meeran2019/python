
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
no_of_names = len(names)

random_position = random.randrange(0,no_of_names)

# print(random_position)
# print(no_of_names)
# print(names)
selected_person = names[random_position]

#print(selected_person)
print(f"{selected_person} is going to buy the meal today!")


