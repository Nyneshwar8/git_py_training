# printing the diffrence between two list

list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 3, 15]

list3 = []
for element in list1:
    if element not in list2:
      list3.append(element)

print(list3)