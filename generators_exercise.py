# fibonacci series using generators
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b


for c in fib(21):
    print(c)


# fibonacci series using list
def fib1(num):
    x = 0
    y = 1
    list1 = []
    for i in range(num):
        list1.append(x)
        temp1 = x
        x = y
        y = temp1 + y
    return list1


print(fib1(21))
