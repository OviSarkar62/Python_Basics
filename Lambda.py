# Lambda function
sqr = lambda x:x*x
def fibonacci(n):
    list = []
    a,b = 0, 1
    for i in range(n):
        list.append(a)
        a, b = b, a+b
    return list

if __name__ == '__main__':
    n = int(input())
    print(list(map(sqr, fibonacci(n))))