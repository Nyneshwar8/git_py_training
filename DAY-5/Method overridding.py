# class area:
#     def  find_area(self,a=None,b=None):
#                if a!=None and b!=None:
#                    print("area of rectangle",a*b)
#                elif b!=None:
#                    print("area of square",b*b)
#                else:
#                    print("module not find")
#
#
#
# object=area()
# object.find_area()
# object.find_area(10,40)
# object.find_area(30,20)

class a:
    def nyno(self):
        print("im in  a")
class b(a):
    def nyno(self):
        print("im in b")
object=b()
object.nyno()