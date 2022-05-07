# NOTE: This game checks whetehr computer generated or user computed are same. 

import random 
input_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

chosen_value = random.choice([0,1,2])
print(chosen_value)
print(input_choice)

if input_choice == chosen_value:
    print("You won")
else: 
    print("you lose")





