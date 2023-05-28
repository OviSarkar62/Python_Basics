# ZeroDivisionError
try:
    list = [20, 0, 30]
    num = int(input())
    result = list[0] / num
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index Error")
except ValueError:
    print("ValueError")
finally:
    print("successful")