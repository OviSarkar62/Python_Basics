# Class & Object & Method
class Student:
    roll = ""
    gpa = ""

    def value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print("Roll: ", self.roll)
        print("Gpa: ", self.gpa)

object1 = Student()
object1.value(52,3.52)
object1.display()

object2 = Student()
object2.value(5,3.85)
object2.display()