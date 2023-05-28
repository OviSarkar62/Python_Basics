def add(x,y):
    sum = x+y
    return sum

def sub(x,y):
    sub = x-y
    return sub


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    result1 = add(a,b)
    result2 = sub(a,b)
    print(result1)
    print(result2)
