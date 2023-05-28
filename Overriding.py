# Overriding
class Nokia:
    def call(self):
        print("Can call from Nokia")
    def text(self):
        print("Can text")

class OnePlus(Nokia):
    def call(self):
        #super().call()
        print("Can call from OnePlus")
    def photo(self):
        print("Can capture")

object = OnePlus()
object.call()
object.text()
object.photo()