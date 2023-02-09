# python programm to sub the list from another list
user = [3, 4, 5, 6, 7, 8, 9, 10]
user1 = [1, 2, 3, 4, 5, 6, 7]
sub=[]
for a,b in zip(user,user1):
 sub.append(a-b)
print(sub)
