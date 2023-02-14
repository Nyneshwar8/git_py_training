# class baap:
#     def nyno(self,name=""):
#         print("this in my lang"+name)
#
#
# object=baap()
# object.nyno()
# object.nyno("python")
# object.nyno("django"

# class Dog:
#     def __init__(self,str):
#         self.name=str
#     def hello(self):
#         print("Bhu Bhu")








class Women:
    def __init__(self,str):
        self.name=str
    def Nyno(self):
        print("She is a strong women")
class Mother:
    def __init__(self, str):
        self.name = str

    def Nyno(self):
        print("She is a strong mother")
class sister:
    def __init__(self, str):
        self.name = str

    def Nyno(self):
        print("She is a strong sister")
class friend:
    def __init__(self,str):
     self.name = str
     print("hello is ")

    def Nyno(self):
        print("She is my friend")

All=[Women("Women"),Mother("mom"),sister("sheetal"),friend("shubhangi")]

for all in All:
    all.Nyno()