class Nyno():
    def DisplayA(self):
        print("this is my work1")
    def DisplayB(self):
        print("this is also my work2")
class Nyno1(Nyno):
    def DisplayC(self):
        print("this also my work3")
    def DisplayD(self):
        print("fandababloues performance4")

object=Nyno1()

object.DisplayA()
object.DisplayB()
object.DisplayC()
object.DisplayD()