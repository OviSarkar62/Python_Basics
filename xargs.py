# xargs
def add(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum)

add(10,20)
add(166,44,50)

# xxargs
def student(**details):
    print(details)

student(id=52, name="Ovi")