# Using list comprehension to iterate through loop
List = [character for character in [1, 2, 3]]

# Displaying list
print(List)

#even numbers in list comparihension



list = [i for i in range(13) if i % 2 == 0]
print(list)


#matrix list using the list comprehension


matrix = [[j for j in range(3)] for i in range(3)]

print(matrix)