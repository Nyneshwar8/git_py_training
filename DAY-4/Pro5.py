
# list1=[["Alfaiz",2],["akshu",5],["Madhu",10],["Shubhu",30]]
#
# for item , element in list1 :
#     print(item,element)


#
# tub=(20,50,6,4,30,50,82)
#
# for x in tub:
#     print(x)


# items=[int,float,"Alfaiz",1,24,3,44,5,15,2,33,4,54]
#
# for item in items:
#     if str(item).isnumeric() and item>6:
#         print(item)




# lis=[245,546,789,123,]
#
# for i in lis:
#     if str(i).isnumeric() and i>100:
#         print(i)


# num=0
# while num <= 20:
#   print(num ,end=" ")
#   num=num+2


# i = 1
# while i < 6:
#   print(i)
#   i+=1

# num=0
# while (True):
#   print(num+1 ,end=" ")
#   if (num==44):
#     break
#   num=num+2




# def function1(a,b):
#   print(a+b)
# function1(5,3)


x=(lambda a,b:a+b)(3,5)
print(x)

x=lambda a,b:a+b
print(x(5,8))