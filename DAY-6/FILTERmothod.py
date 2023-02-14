# def starts_with_A(s):
#     return s[0] == "A"
#
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = filter(starts_with_A, fruit)
#
# print(list(map_object))



#and this is lambda function



fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))