class Nyno():
    def DisplayA(self):
        print("this is my work1")
    def DisplayB(self):
        print("this is also my work2")
class Nyno1():
    def DisplayC(self):
        print("this also my work3")
    def DisplayD(self):
        print("fandababloues performance4")
class Nyno2():
    def DisplayE(self):
        print("this also my work5")
    def DisplayF(self):
        print("fandababloues performance6")
class Nyno3():
    def DisplayG(self):
        print("this also my work7")
    def DisplayH(self):
        print("fandababloues performance8")
class Nyno4():
    def DisplayI(self):
        print("this also my work9")
    def DisplayJ(self):
        print("fandababloues performance10")
class Nyno5(Nyno,Nyno1,Nyno2,Nyno3,Nyno4):
    def DisplayK(self):
        print("this also my work11")
    def DisplayL(self):
        print("fandababloues performance12")



object=Nyno5()
object.DisplayA()
object.DisplayB()
object.DisplayC()
object.DisplayD()
object.DisplayE()
object.DisplayF()
object.DisplayG()
object.DisplayH()
object.DisplayI()
object.DisplayJ()
object.DisplayK()
object.DisplayL()

