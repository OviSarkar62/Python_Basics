# Triangle Constructor
class Triangle:
    base = ""
    height = ""

    def __init__(self,base,height):
       self.base = base
       self.height = height
    def area(self):
        print("Area: ",self.base*self.height*.5)

object1 = Triangle(10,20)
object1.area()

object2 = Triangle(20,30)
object2.area()