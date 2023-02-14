class Myname():
      def __init__(self):
          self.name=""
      def Firstname(self):
          return self.name
      def Lastname(self,name):
          self.name=name
object=Myname()
object.Lastname("hello ugale")
sir=object.name
print(sir)