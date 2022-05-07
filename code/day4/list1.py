
list1 = ["apple","orange","banana","mango"]
print(list1)
print(list1[1])

list2 = ["string1", 22, ["list-value-1","list-value-2"]]
print(list2[2][1])

list2.append("append-value")
print(list2)

print(list2[-1])

print(list2[-1:])

list2[1] = 33
print(list2)

x = list2.count(33)
print(x)

list2.extend(["extend1","extend2"])
print(list2)
