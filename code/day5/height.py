total_hight = 0 
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

# split function is used to split the string into list. 

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#  print(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  total_hight = total_hight  + student_heights[n]
#print(student_heights)
#print(total_hight)
average_height = round(total_hight / len(student_heights))
print(average_height)







