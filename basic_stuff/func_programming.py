from functools import reduce
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
list3 = [100, 200, 300, 400]


def multiply(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(list(map(multiply, list1)))
print(list(filter(only_odd, list1)))
print(list(zip(list1, list2, list3)))
print(reduce(accumulator, list1, 10))

# lambda expressions
print(list(map(lambda item: item * 3, list1)))
