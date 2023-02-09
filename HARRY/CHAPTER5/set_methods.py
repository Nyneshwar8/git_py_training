#creting the epty set 

a=set()
print(type(a))


#adding the value in empy set


a.add(4)
a.add(4)
a.add(5)
a.add(5)
# a.add([4,5,6])   #we cannot add the list in to set
# a.add({4,5,6})   #we cannot add the dict in to set
a.add((4,5,6))
print(a)
print(len(a))   #finds the length
a.remove(5)      #remove the value form set
print(a)