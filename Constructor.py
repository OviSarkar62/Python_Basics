# Constructor
class Student:
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print("Roll: ", self.roll)
        print("Gpa: ", self.gpa)

object1 = Student(52,3.52)
object1.display()

object2 = Student(5,3.85)
object2.display()